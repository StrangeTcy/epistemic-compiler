"""Resumable DAG scheduler and append-only execution records for local UI jobs."""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
import re
import shutil
import uuid
from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from runtime.models import (
    ExecutionResult,
    JobContext,
    JobExecutor,
    JobSpec,
    MissionSpec,
    RetryableJobError,
    WaitingForHuman,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUN_ROOT = PROJECT_ROOT / "runtime" / "runs"
STATE_FILE = "run_state.json"
EVENT_FILE = "events.jsonl"

_ALLOWED_TRANSITIONS: dict[str, set[str]] = {
    "queued": {"running", "failed", "blocked", "waiting_for_human"},
    "running": {"completed", "failed", "blocked", "waiting_for_human"},
    "waiting_for_human": {"queued", "completed"},
    "failed": {"queued"},
    "blocked": {"queued"},
    "completed": set(),
}


class MissionValidationError(ValueError):
    pass


class ArtifactReferenceError(ValueError):
    pass


def utc_now() -> str:
    return (
        datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _text(value: Any, field: str, *, required: bool = True) -> str:
    if value is None and not required:
        return ""
    if not isinstance(value, str) or (required and not value.strip()):
        raise MissionValidationError(f"{field} must be a non-empty string")
    return value.strip()


def _string_list(value: Any, field: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        raise MissionValidationError(f"{field} must be a list of non-empty strings")
    return tuple(item.strip() for item in value)


def _load_inputs(raw: Any) -> dict[str, str]:
    if raw is None:
        return {}
    result: dict[str, str] = {}
    if isinstance(raw, dict):
        for name, path in raw.items():
            if (
                not isinstance(name, str)
                or not name.strip()
                or not isinstance(path, str)
                or not path.strip()
            ):
                raise MissionValidationError(
                    "inputs must map non-empty names to file paths"
                )
            result[name.strip()] = path.strip()
        return result
    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, str):
                path = item.strip()
                if not path:
                    raise MissionValidationError("input paths cannot be empty")
                name = Path(path).stem or f"input_{len(result) + 1}"
            elif isinstance(item, dict):
                unknown = set(item) - {"id", "path"}
                if unknown:
                    raise MissionValidationError(
                        f"unknown fields in inputs[]: {', '.join(sorted(str(key) for key in unknown))}"
                    )
                name = _text(item.get("id"), "inputs[].id")
                path = _text(item.get("path"), f"inputs[{name}].path")
            else:
                raise MissionValidationError(
                    "inputs must be a mapping or a list of paths/records"
                )
            if name in result:
                raise MissionValidationError(f"duplicate mission input id: {name}")
            result[name] = path
        return result
    raise MissionValidationError("inputs must be a mapping or list")


def _validate_acyclic(jobs: tuple[JobSpec, ...]) -> None:
    mapping = {job.job_id: job for job in jobs}
    for job in jobs:
        unknown = sorted(set(job.dependencies) - mapping.keys())
        if unknown:
            raise MissionValidationError(
                f"job {job.job_id!r} has unknown dependencies: {', '.join(unknown)}"
            )
        if job.job_id in job.dependencies:
            raise MissionValidationError(f"job {job.job_id!r} cannot depend on itself")
    remaining = {job.job_id: set(job.dependencies) for job in jobs}
    ready = [job_id for job_id, dependencies in remaining.items() if not dependencies]
    seen: set[str] = set()
    while ready:
        current = ready.pop()
        if current in seen:
            continue
        seen.add(current)
        for job_id, dependencies in remaining.items():
            if current in dependencies:
                dependencies.remove(current)
                if not dependencies:
                    ready.append(job_id)
    if len(seen) != len(jobs):
        cycle = sorted(set(mapping) - seen)
        raise MissionValidationError(
            f"mission dependency graph contains a cycle involving: {', '.join(cycle)}"
        )


def load_mission(path: str | Path) -> MissionSpec:
    mission_path = Path(path).expanduser().resolve()
    if not mission_path.is_file():
        raise FileNotFoundError(f"mission YAML not found: {mission_path}")
    try:
        raw = yaml.safe_load(mission_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise MissionValidationError(f"invalid YAML in {mission_path}: {exc}") from exc
    if not isinstance(raw, dict):
        raise MissionValidationError("mission YAML must contain a mapping")
    unknown_top_level = set(raw) - {"mission_id", "type", "inputs", "defaults", "jobs"}
    if unknown_top_level:
        raise MissionValidationError(
            f"unknown mission fields: {', '.join(sorted(str(key) for key in unknown_top_level))}"
        )

    mission_id = _text(raw.get("mission_id"), "mission_id")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", mission_id):
        raise MissionValidationError(
            "mission_id must be a filesystem-safe identifier (letters, digits, dot, underscore, hyphen)"
        )
    mission_type = _text(raw.get("type", "mission"), "type")
    inputs = _load_inputs(raw.get("inputs"))
    defaults = raw.get("defaults", {})
    if defaults is None:
        defaults = {}
    if not isinstance(defaults, dict):
        raise MissionValidationError("defaults must be a mapping")
    unknown_defaults = set(defaults) - {"site", "model", "profile", "timeout_seconds"}
    if unknown_defaults:
        raise MissionValidationError(
            f"unknown defaults fields: {', '.join(sorted(str(key) for key in unknown_defaults))}"
        )
    jobs_raw = raw.get("jobs")
    if not isinstance(jobs_raw, list) or not jobs_raw:
        raise MissionValidationError("jobs must be a non-empty list")

    jobs: list[JobSpec] = []
    seen: set[str] = set()
    for index, item in enumerate(jobs_raw):
        if not isinstance(item, dict):
            raise MissionValidationError(f"jobs[{index}] must be a mapping")
        allowed_job_fields = {
            "id",
            "job_id",
            "mission_id",
            "role",
            "prompt_artifact",
            "input_artifacts",
            "dependencies",
            "depends_on",
            "site",
            "provider",
            "model",
            "profile",
            "output_artifact",
            "timeout_seconds",
        }
        unknown_job_fields = set(item) - allowed_job_fields
        if unknown_job_fields:
            raise MissionValidationError(
                f"unknown fields for jobs[{index}]: {', '.join(sorted(str(key) for key in unknown_job_fields))}"
            )
        job_id = _text(item.get("job_id", item.get("id")), f"jobs[{index}].job_id")
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", job_id):
            raise MissionValidationError(
                f"invalid job id {job_id!r}; use letters, digits, dot, underscore or hyphen"
            )
        if job_id in seen:
            raise MissionValidationError(f"duplicate job id: {job_id}")
        seen.add(job_id)
        job_mission_id = item.get("mission_id", mission_id)
        if job_mission_id != mission_id:
            raise MissionValidationError(
                f"job {job_id!r} mission_id must match top-level mission_id"
            )
        role = _text(item.get("role"), f"jobs[{job_id}].role")
        prompt_artifact = _text(
            item.get("prompt_artifact"), f"jobs[{job_id}].prompt_artifact"
        )
        input_artifacts = _string_list(
            item.get("input_artifacts"), f"jobs[{job_id}].input_artifacts"
        )
        dependency_raw = item.get("dependencies", item.get("depends_on"))
        dependencies = _string_list(dependency_raw, f"jobs[{job_id}].dependencies")
        if len(set(dependencies)) != len(dependencies):
            raise MissionValidationError(
                f"job {job_id!r} contains duplicate dependencies"
            )
        site = _text(
            item.get("site", item.get("provider", defaults.get("site", "arena"))),
            f"jobs[{job_id}].site",
        ).lower()
        model_value = item.get("model", defaults.get("model"))
        if model_value is not None and (
            not isinstance(model_value, str) or not model_value.strip()
        ):
            raise MissionValidationError(
                f"jobs[{job_id}].model must be a non-empty string or null"
            )
        profile = item.get("profile", defaults.get("profile", site))
        if profile is not None and (
            not isinstance(profile, str) or not profile.strip()
        ):
            raise MissionValidationError(
                f"jobs[{job_id}].profile must be a non-empty string or null"
            )
        output_artifact = item.get(
            "output_artifact", f"artifacts/jobs/{job_id}/response.md"
        )
        output_artifact = _text(output_artifact, f"jobs[{job_id}].output_artifact")
        timeout_seconds = item.get(
            "timeout_seconds", defaults.get("timeout_seconds", 300)
        )
        if not isinstance(timeout_seconds, int) or timeout_seconds < 10:
            raise MissionValidationError(
                f"jobs[{job_id}].timeout_seconds must be an integer >= 10"
            )
        jobs.append(
            JobSpec(
                job_id=job_id,
                mission_id=mission_id,
                role=role,
                prompt_artifact=prompt_artifact,
                input_artifacts=input_artifacts,
                dependencies=dependencies,
                site=site,
                model=model_value.strip() if isinstance(model_value, str) else None,
                profile=profile.strip() if isinstance(profile, str) else None,
                output_artifact=output_artifact,
                timeout_seconds=timeout_seconds,
            )
        )

    job_tuple = tuple(jobs)
    _validate_acyclic(job_tuple)
    mapping = {job.job_id: job for job in job_tuple}
    output_owners: dict[str, str] = {}
    validation_root = Path("/__runtime_output_validation__")
    for job in job_tuple:
        output_path = _safe_run_directory(_format_output_artifact(job), validation_root)
        output_key = str(output_path.relative_to(validation_root))
        if output_key in output_owners:
            raise MissionValidationError(
                f"jobs {output_owners[output_key]!r} and {job.job_id!r} share output_artifact {output_key!r}"
            )
        output_owners[output_key] = job.job_id
        for reference in job.input_artifacts:
            if reference.startswith("mission:"):
                input_id = reference.split(":", 1)[1]
                if input_id not in inputs:
                    raise MissionValidationError(
                        f"job {job.job_id!r} references unknown mission input {reference!r}"
                    )
            elif reference.startswith("job:"):
                parts = reference.split(":")
                if len(parts) != 3 or parts[2] != "response":
                    raise MissionValidationError(
                        f"job artifact reference must be job:<job_id>:response, got {reference!r}"
                    )
                upstream_id = parts[1]
                if upstream_id not in mapping:
                    raise MissionValidationError(
                        f"job {job.job_id!r} references unknown job {upstream_id!r}"
                    )
                if upstream_id not in job.dependencies:
                    raise MissionValidationError(
                        f"job {job.job_id!r} references {upstream_id!r} without depending on it"
                    )
    return MissionSpec(
        mission_id=mission_id,
        mission_type=mission_type,
        path=mission_path,
        inputs=inputs,
        jobs=job_tuple,
        sha256=sha256_file(mission_path),
    )


def _atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, sort_keys=True)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


def _atomic_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    with temp.open("wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)



def _write_once(path: Path, data: bytes) -> None:
    """Create an artifact without ever replacing an earlier response."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    except FileExistsError as exc:
        raise FileExistsError(f"immutable artifact already exists: {path}") from exc
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except Exception:
        path.unlink(missing_ok=True)
        raise



def _append_event(run_dir: Path, event: dict[str, Any]) -> None:
    path = run_dir / EVENT_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
        stream.flush()
        os.fsync(stream.fileno())


def _new_run_state(spec: MissionSpec, run_id: str) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "run_id": run_id,
        "mission_id": spec.mission_id,
        "mission_type": spec.mission_type,
        "mission_path": str(spec.path),
        "mission_sha256": spec.sha256,
        "created_at": utc_now(),
        "updated_at": utc_now(),
        "jobs": {
            job.job_id: {
                "job_id": job.job_id,
                "mission_id": job.mission_id,
                "role": job.role,
                "site": job.site,
                "model_requested": job.model,
                "profile_id": job.profile,
                "dependencies": list(job.dependencies),
                "prompt_artifact": job.prompt_artifact,
                "input_artifacts": list(job.input_artifacts),
                "output_artifact": None,
                "status": "queued",
                "attempts": 0,
                "interaction": {},
                "created_at": utc_now(),
                "updated_at": utc_now(),
            }
            for job in spec.jobs
        },
    }


def _persist_state(run_dir: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = utc_now()
    _atomic_json(run_dir / STATE_FILE, state)


def _transition(
    run_dir: Path,
    state: dict[str, Any],
    job_id: str,
    status: str,
    *,
    reason: str | None = None,
    announce: Callable[[dict[str, Any]], None] | None = None,
) -> None:
    job_state = state["jobs"][job_id]
    previous = job_state["status"]
    if status == previous:
        return
    if status not in _ALLOWED_TRANSITIONS.get(previous, set()):
        raise RuntimeError(f"invalid job transition {job_id}: {previous} -> {status}")
    now = utc_now()
    job_state["status"] = status
    job_state["updated_at"] = now
    if status == "running":
        job_state["attempts"] += 1
        job_state["started_at"] = now
        job_state.pop("ended_at", None)
        job_state.pop("error", None)
        job_state.pop("status_reason", None)
        job_state.pop("screenshot", None)
        interaction = job_state.get("interaction", {})
        interaction.pop("stage", None)
        interaction.pop("screenshot", None)
    if status in {"completed", "failed", "blocked", "waiting_for_human"}:
        job_state["ended_at"] = now
    if reason:
        job_state["status_reason"] = reason
    event = {
        "timestamp": now,
        "mission_id": state["mission_id"],
        "run_id": state["run_id"],
        "job_id": job_id,
        "from": previous,
        "to": status,
        "reason": reason,
    }
    _append_event(run_dir, event)
    _persist_state(run_dir, state)
    if announce:
        announce(event)


def _format_output_artifact(job: JobSpec) -> Path:
    try:
        value = job.output_artifact.format(job_id=job.job_id, mission_id=job.mission_id)
    except (KeyError, ValueError) as exc:
        raise MissionValidationError(
            f"invalid output_artifact template for job {job.job_id!r}: {exc}"
        ) from exc
    return Path(value)


def _safe_run_directory(path: Path, run_dir: Path) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        raise ArtifactReferenceError(
            "output_artifact must be relative to the run directory"
        )
    resolved = (run_dir / candidate).resolve()
    try:
        resolved.relative_to(run_dir.resolve())
    except ValueError as exc:
        raise ArtifactReferenceError(
            "output_artifact cannot escape the run directory"
        ) from exc
    return resolved


def _resolve_input_reference(
    spec: MissionSpec,
    run_dir: Path,
    job: JobSpec,
    reference: str,
    state: dict[str, Any],
) -> Path:
    if reference.startswith("mission:"):
        key = reference.split(":", 1)[1]
        if key not in spec.inputs:
            raise ArtifactReferenceError(
                f"unknown mission input reference {reference!r}"
            )
        return (spec.path.parent / spec.inputs[key]).expanduser().resolve()
    if reference.startswith("job:"):
        parts = reference.split(":")
        if len(parts) != 3 or parts[2] != "response":
            raise ArtifactReferenceError(
                f"job artifact reference must be job:<job_id>:response, got {reference!r}"
            )
        upstream_id = parts[1]
        if upstream_id not in job.dependencies:
            raise ArtifactReferenceError(
                f"job {job.job_id!r} references {upstream_id!r} without depending on it"
            )
        upstream = state["jobs"].get(upstream_id, {})
        path_value = upstream.get("output_artifact")
        if not path_value:
            raise ArtifactReferenceError(
                f"upstream job {upstream_id!r} has no response artifact yet"
            )
        return (run_dir / path_value).resolve()
    return (spec.path.parent / reference).expanduser().resolve()


def _snapshot_file(source: Path, destination: Path) -> tuple[Path, str, int]:
    if not source.is_file():
        raise FileNotFoundError(f"artifact file not found: {source}")
    digest = sha256_file(source)
    size = source.stat().st_size
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        if sha256_file(destination) != digest:
            raise RuntimeError(
                f"snapshot path collision or modified snapshot: {destination}"
            )
    else:
        shutil.copy2(source, destination)
    return destination, digest, size


def _make_context(
    spec: MissionSpec,
    job: JobSpec,
    run_dir: Path,
    state: dict[str, Any],
    provenance: dict[str, Any],
    announce: Callable[[dict[str, Any]], None] | None,
) -> JobContext:
    job_dir = run_dir / "artifacts" / "jobs" / job.job_id
    job_dir.mkdir(parents=True, exist_ok=True)
    prompt_path = (spec.path.parent / job.prompt_artifact).expanduser().resolve()
    prompt_snapshot = run_dir / "inputs" / "prompts" / f"{job.job_id}.md"
    prompt_snapshot.parent.mkdir(parents=True, exist_ok=True)
    if prompt_snapshot.exists():
        # A retry must use the exact prompt first presented, even if the source file
        # has since changed. The run-local snapshot is the execution authority.
        prompt_bytes = prompt_snapshot.read_bytes()
        prompt_source_hash = sha256_file(prompt_path) if prompt_path.is_file() else None
    else:
        if not prompt_path.is_file():
            raise FileNotFoundError(f"prompt artifact not found: {prompt_path}")
        prompt_bytes = prompt_path.read_bytes()
        _atomic_bytes(prompt_snapshot, prompt_bytes)
        prompt_source_hash = sha256_bytes(prompt_bytes)
    prompt_text = prompt_bytes.decode("utf-8")
    prompt_hash = sha256_bytes(prompt_bytes)
    recorded_prompt_hash = state["jobs"][job.job_id].get("prompt_sha256")
    if recorded_prompt_hash and recorded_prompt_hash != prompt_hash:
        raise RuntimeError(f"prompt snapshot hash changed for job {job.job_id!r}")

    input_paths: list[Path] = []
    input_records: list[dict[str, Any]] = []
    stored_input_records = state["jobs"][job.job_id].get("input_records") or []
    if stored_input_records and len(stored_input_records) != len(job.input_artifacts):
        raise RuntimeError(
            f"stored input snapshot count does not match job {job.job_id!r}"
        )
    for index, reference in enumerate(job.input_artifacts):
        if stored_input_records:
            stored = stored_input_records[index]
            if stored.get("reference") != reference:
                raise RuntimeError(
                    f"stored input reference changed for job {job.job_id!r}"
                )
            snapshot = _safe_run_directory(Path(stored["snapshot_path"]), run_dir)
            if not snapshot.is_file():
                raise FileNotFoundError(f"stored input snapshot is missing: {snapshot}")
            digest = sha256_file(snapshot)
            if digest != stored.get("sha256"):
                raise RuntimeError(f"stored input snapshot hash changed: {snapshot}")
            size = snapshot.stat().st_size
            record = dict(stored)
            record["size_bytes"] = size
        else:
            source = _resolve_input_reference(spec, run_dir, job, reference, state)
            if not source.is_file():
                raise FileNotFoundError(
                    f"input artifact {reference!r} not found: {source}"
                )
            digest = sha256_file(source)
            snapshot_name = f"{digest[:16]}-{source.name}"
            snapshot, _, size = _snapshot_file(
                source, run_dir / "inputs" / "files" / snapshot_name
            )
            record = {
                "reference": reference,
                "source_path": str(source),
                "snapshot_path": str(snapshot.relative_to(run_dir)),
                "sha256": digest,
                "size_bytes": size,
                "attachment_index": index,
            }
        input_paths.append(snapshot)
        input_records.append(record)

    output_path = _safe_run_directory(_format_output_artifact(job), run_dir)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    provenance.update(
        {
            "prompt_artifact": job.prompt_artifact,
            "prompt_snapshot": str(prompt_snapshot.relative_to(run_dir)),
            "prompt_sha256": prompt_hash,
            "prompt_source_sha256": prompt_source_hash,
            "prompt_source_changed_since_snapshot": bool(
                prompt_source_hash and prompt_source_hash != prompt_hash
            ),
            "input_artifacts": input_records,
            "response_artifact": str(output_path.relative_to(run_dir)),
            "profile_id": job.profile,
        }
    )
    _atomic_json(job_dir / "provenance.json", provenance)
    job_state = state["jobs"][job.job_id]
    job_state["output_artifact"] = str(output_path.relative_to(run_dir))
    job_state["prompt_sha256"] = prompt_hash
    job_state["prompt_source_sha256"] = prompt_source_hash
    job_state["input_sha256"] = [record["sha256"] for record in input_records]
    job_state["input_records"] = input_records
    _persist_state(run_dir, state)

    def update_progress(updates: dict[str, Any]) -> None:
        if not isinstance(updates, dict):
            raise TypeError("progress update must be a mapping")
        job_state.setdefault("interaction", {}).update(updates)
        for key in (
            "conversation_id",
            "current_url",
            "screenshot",
            "submission_state",
            "stage",
            "model_selected",
            "attachments_verified",
            "handoff_kind",
            "handoff_json",
            "prompt_to_paste",
            "expected_response_artifact",
            "post_id",
            "next_stage",
        ):
            if key in updates:
                job_state[key] = updates[key]
        provenance["interaction"] = dict(job_state.get("interaction", {}))
        for key in ("conversation_id", "current_url", "screenshot", "model_selected"):
            if key in updates:
                provenance[key] = updates[key]
        _atomic_json(job_dir / "provenance.json", provenance)
        _persist_state(run_dir, state)

    return JobContext(
        mission=spec,
        job=job,
        run_dir=run_dir,
        job_dir=job_dir,
        prompt_text=prompt_text,
        prompt_snapshot=prompt_snapshot,
        prompt_sha256=prompt_hash,
        input_paths=tuple(input_paths),
        input_records=tuple(input_records),
        job_state=job_state,
        update_progress=update_progress,
    )


async def _execute_one(
    spec: MissionSpec,
    job: JobSpec,
    run_dir: Path,
    state: dict[str, Any],
    executor: JobExecutor,
    announce: Callable[[dict[str, Any]], None] | None,
) -> None:
    _transition(run_dir, state, job.job_id, "running", announce=announce)
    job_state = state["jobs"][job.job_id]
    start_time = job_state["started_at"]
    provenance: dict[str, Any] = {
        "schema_version": 1,
        "mission_id": job.mission_id,
        "job_id": job.job_id,
        "role": job.role,
        "provider": job.site,
        "site": job.site,
        "model_requested": job.model,
        "profile_id": job.profile,
        "started_at": start_time,
        "ended_at": None,
        "prompt_artifact": job.prompt_artifact,
        "prompt_sha256": None,
        "input_artifacts": [],
        "response_artifact": None,
        "response_sha256": None,
        "conversation_id": job_state.get("conversation_id"),
        "current_url": job_state.get("current_url"),
        "screenshot": job_state.get("screenshot"),
        "error": None,
    }
    job_dir = run_dir / "artifacts" / "jobs" / job.job_id
    job_dir.mkdir(parents=True, exist_ok=True)
    _atomic_json(job_dir / "provenance.json", provenance)
    try:
        context = _make_context(spec, job, run_dir, state, provenance, announce)
        result = await executor.execute(context)
        if not isinstance(result, ExecutionResult):
            raise TypeError("site executor must return an ExecutionResult")
        output_path = _safe_run_directory(_format_output_artifact(job), run_dir)
        response_bytes = result.response_text.encode("utf-8")
        _atomic_bytes(output_path, response_bytes)
        ended_at = utc_now()
        provenance.update(
            {
                "status": "completed",
                "ended_at": ended_at,
                "model_observed": result.model_name,
                "conversation_id": result.conversation_id
                or job_state.get("conversation_id"),
                "current_url": result.current_url or job_state.get("current_url"),
                "response_artifact": str(output_path.relative_to(run_dir)),
                "response_sha256": sha256_bytes(response_bytes),
                "response_bytes": len(response_bytes),
                "result_metadata": result.metadata,
                "error": None,
            }
        )
        _atomic_json(job_dir / "provenance.json", provenance)
        job_state.update(
            {
                "output_artifact": str(output_path.relative_to(run_dir)),
                "response_sha256": sha256_bytes(response_bytes),
                "model_observed": result.model_name,
                "conversation_id": result.conversation_id
                or job_state.get("conversation_id"),
                "current_url": result.current_url or job_state.get("current_url"),
                "ended_at": ended_at,
            }
        )
        _transition(run_dir, state, job.job_id, "completed", announce=announce)
    except WaitingForHuman as exc:
        ended_at = utc_now()
        interaction_updates = dict(exc.details)
        job_state.setdefault("interaction", {}).update(interaction_updates)
        for key in (
            "conversation_id",
            "current_url",
            "screenshot",
            "submission_state",
            "stage",
            "model_selected",
            "attachments_verified",
            "handoff_kind",
            "handoff_json",
            "prompt_to_paste",
            "expected_response_artifact",
            "post_id",
            "next_stage",
        ):
            if key in interaction_updates:
                job_state[key] = interaction_updates[key]
                provenance[key] = interaction_updates[key]
        reason = str(exc)
        job_state["error"] = {
            "type": type(exc).__name__,
            "message": reason,
            "details": interaction_updates,
        }
        provenance.update(
            {
                "status": "waiting_for_human",
                "ended_at": ended_at,
                "error": {
                    "type": type(exc).__name__,
                    "message": reason,
                    "details": interaction_updates,
                },
            }
        )
        _atomic_json(job_dir / "provenance.json", provenance)
        _transition(
            run_dir,
            state,
            job.job_id,
            "waiting_for_human",
            reason=reason,
            announce=announce,
        )
    except asyncio.CancelledError:
        reason = "runner interrupted while job was active; inspect the saved conversation before resuming"
        ended_at = utc_now()
        job_state["error"] = {"type": "Interrupted", "message": reason}
        provenance.update(
            {
                "status": "waiting_for_human",
                "ended_at": ended_at,
                "error": job_state["error"],
            }
        )
        _atomic_json(job_dir / "provenance.json", provenance)
        _transition(
            run_dir,
            state,
            job.job_id,
            "waiting_for_human",
            reason=reason,
            announce=announce,
        )
        raise
    except (
        Exception
    ) as exc:  # Persist the failure and let independent DAG siblings continue.
        ended_at = utc_now()
        error = {"type": type(exc).__name__, "message": str(exc)[:2000]}
        if isinstance(exc, RetryableJobError):
            error["retryable"] = True
        job_state["error"] = error
        provenance.update({"status": "failed", "ended_at": ended_at, "error": error})
        _atomic_json(job_dir / "provenance.json", provenance)
        _transition(
            run_dir,
            state,
            job.job_id,
            "failed",
            reason=error["message"],
            announce=announce,
        )


def _event_printer(event: dict[str, Any]) -> None:
    reason = f" — {event['reason']}" if event.get("reason") else ""
    print(
        f"[{event['timestamp']}] {event['job_id']}: {event['from']} -> {event['to']}{reason}",
        flush=True,
    )


def _acquire_run_lock(run_dir: Path) -> Path:
    lock_path = run_dir / ".runner.lock"
    try:
        descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise MissionValidationError(
            f"run is already locked ({lock_path}); verify no runner is active before removing a stale lock"
        ) from exc
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            json.dump({"pid": os.getpid(), "started_at": utc_now()}, stream)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
    except Exception:
        lock_path.unlink(missing_ok=True)
        raise
    return lock_path


def _release_run_lock(lock_path: Path) -> None:
    lock_path.unlink(missing_ok=True)



def ingest_human_response(
    run_dir: str | Path,
    job_id: str,
    response_path: str | Path | bytes,
    *,
    model_label: str | None = None,
) -> dict[str, Any]:
    """Ingest one saved Battle response into its waiting job exactly once.

    The human-provided file is copied byte-for-byte to the job's declared output
    artifact. Neither that response nor its ingestion record can be overwritten.
    The waiting job is then transitioned to completed so the ordinary DAG
    scheduler can resume its dependents.
    """
    run_path = Path(run_dir).expanduser().resolve()
    state_path = run_path / STATE_FILE
    if not state_path.is_file():
        raise FileNotFoundError(f"run state not found: {state_path}")
    lock_path = _acquire_run_lock(run_path)
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
        if job_id not in state.get("jobs", {}):
            raise MissionValidationError(f"unknown job in run: {job_id}")
        job_state = state["jobs"][job_id]
        if job_state.get("status") != "waiting_for_human":
            raise MissionValidationError(
                f"job {job_id!r} is {job_state.get('status')!r}, not waiting_for_human"
            )
        interaction = job_state.get("interaction", {})
        if interaction.get("handoff_kind") != "model_response":
            raise MissionValidationError(
                f"job {job_id!r} is not waiting for a model response"
            )
        handoff_relative = interaction.get("handoff_json")
        expected_output = job_state.get("output_artifact")
        if not isinstance(handoff_relative, str) or not isinstance(expected_output, str):
            raise MissionValidationError("handoff metadata is incomplete")
        handoff_path = _safe_run_directory(Path(handoff_relative), run_path)
        if not handoff_path.is_file():
            raise FileNotFoundError(f"handoff record not found: {handoff_path}")
        handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
        if handoff.get("job_id") != job_id:
            raise MissionValidationError("handoff job_id does not match run state")
        if handoff.get("expected_response_artifact") != expected_output:
            raise MissionValidationError(
                "handoff response artifact does not match run state"
            )
        prompt_relative = handoff.get("prompt_to_paste")
        prompt_hash = handoff.get("prompt_sha256")
        if not isinstance(prompt_relative, str) or not isinstance(prompt_hash, str):
            raise MissionValidationError("handoff prompt metadata is incomplete")
        prompt_path = _safe_run_directory(Path(prompt_relative), run_path)
        if not prompt_path.is_file() or sha256_file(prompt_path) != prompt_hash:
            raise MissionValidationError("saved handoff prompt is missing or changed")

        if isinstance(response_path, bytes):
            source_label = "<stdin>"
            response_bytes = response_path
        else:
            source = Path(response_path).expanduser().resolve()
            if not source.is_file():
                raise FileNotFoundError(f"response file not found: {source}")
            source_label = str(source)
            response_bytes = source.read_bytes()
        if not response_bytes or len(response_bytes) > 20 * 1024 * 1024:
            raise MissionValidationError(
                "response must be non-empty and no larger than 20 MiB"
            )
        try:
            response_text = response_bytes.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise MissionValidationError("response must be UTF-8 text") from exc
        if not response_text.strip():
            raise MissionValidationError("response must contain non-whitespace text")

        output_path = _safe_run_directory(Path(expected_output), run_path)
        job_dir = output_path.parent
        ingest_path = job_dir / "human_ingestion.json"
        if output_path.exists() or ingest_path.exists():
            raise MissionValidationError(
                "response artifact already exists; human responses are immutable"
            )
        response_hash = sha256_bytes(response_bytes)
        ingested_at = utc_now()
        ingestion = {
            "schema_version": 1,
            "ingested_at": ingested_at,
            "method": "post_workflow_cli",
            "run_id": state.get("run_id"),
            "mission_id": state.get("mission_id"),
            "job_id": job_id,
            "role": job_state.get("role"),
            "post_id": interaction.get("post_id"),
            "source_path": source_label,
            "source_sha256": response_hash,
            "response_artifact": expected_output,
            "response_sha256": response_hash,
            "prompt_to_paste": prompt_relative,
            "prompt_sha256": prompt_hash,
            "model_label": (model_label or "").strip() or None,
            "input_artifacts": job_state.get("input_records", []),
            "expanded_source_inputs": handoff.get("expanded_source_inputs", []),
        }
        _write_once(output_path, response_bytes)
        _write_once(
            ingest_path,
            (json.dumps(ingestion, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8"),
        )

        provenance_path = job_dir / "provenance.json"
        provenance = (
            json.loads(provenance_path.read_text(encoding="utf-8"))
            if provenance_path.is_file()
            else {}
        )
        provenance.update(
            {
                "status": "completed",
                "ended_at": ingested_at,
                "response_sha256": response_hash,
                "response_origin": {
                    "type": "human_ingested_external_model_response",
                    "model_label": ingestion["model_label"],
                    "ingestion_record": str(ingest_path.relative_to(run_path)),
                },
                "human_ingestion": ingestion,
            }
        )
        _atomic_json(provenance_path, provenance)
        job_state.update(
            {
                "response_sha256": response_hash,
                "model_observed": ingestion["model_label"],
                "human_ingestion": str(ingest_path.relative_to(run_path)),
            }
        )
        job_state.pop("error", None)
        _transition(
            run_path,
            state,
            job_id,
            "completed",
            reason=f"human response ingested; sha256={response_hash}",
        )
        state["run_status"] = _summary(state)
        _persist_state(run_path, state)
        return {
            "run_dir": str(run_path),
            "run_id": state.get("run_id"),
            "job_id": job_id,
            "response_artifact": str(output_path),
            "response_sha256": response_hash,
            "human_ingestion": ingestion,
            "run_status": state["run_status"],
        }
    finally:
        _release_run_lock(lock_path)



def _prepare_run(
    spec: MissionSpec, resume_dir: Path | None
) -> tuple[Path, dict[str, Any]]:
    if resume_dir is None:
        RUN_ROOT.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        run_id = f"{spec.mission_id}-{stamp}-{uuid.uuid4().hex[:8]}"
        run_dir = RUN_ROOT / spec.mission_id / run_id
        run_dir.mkdir(parents=True, exist_ok=False)
        state = _new_run_state(spec, run_id)
        _persist_state(run_dir, state)
        return run_dir, state

    run_dir = resume_dir.expanduser().resolve()
    state_path = run_dir / STATE_FILE
    if not state_path.is_file():
        raise FileNotFoundError(f"run state not found: {state_path}")
    state = json.loads(state_path.read_text(encoding="utf-8"))
    if state.get("mission_id") != spec.mission_id:
        raise MissionValidationError("resume mission_id does not match the run state")
    if state.get("mission_sha256") != spec.sha256:
        raise MissionValidationError(
            "mission YAML changed since this run started; use the original YAML to resume"
        )
    if set(state.get("jobs", {})) != set(spec.job_map):
        raise MissionValidationError("job set does not match the stored run state")
    return run_dir, state


def _reset_for_resume(
    run_dir: Path,
    state: dict[str, Any],
    *,
    retry_failed: bool,
    announce: Callable[[dict[str, Any]], None] | None,
    resume_waiting_for_human: bool = True,
    retry_job_ids: set[str] | None = None,
    retry_blocked: bool = False,
) -> None:
    retry_job_ids = retry_job_ids or set()
    unknown_retry_jobs = retry_job_ids - set(state["jobs"])
    if unknown_retry_jobs:
        raise MissionValidationError(
            "retry_job_ids contains unknown jobs: "
            + ", ".join(sorted(unknown_retry_jobs))
        )
    unsafe_retry_jobs = {
        job_id
        for job_id in retry_job_ids
        if state["jobs"][job_id].get("status") != "failed"
        or not state["jobs"][job_id].get("error", {}).get("retryable", False)
    }
    if unsafe_retry_jobs:
        raise MissionValidationError(
            "retry_job_ids may name only failed jobs marked retryable: "
            + ", ".join(sorted(unsafe_retry_jobs))
        )

    for job_id, job_state in state["jobs"].items():
        status = job_state["status"]
        if status == "running":
            job_state["error"] = {
                "type": "Interrupted",
                "message": "previous process ended while this job was running; adapter will inspect saved interaction state before any resubmission",
            }
            _transition(
                run_dir,
                state,
                job_id,
                "waiting_for_human",
                reason=job_state["error"]["message"],
                announce=announce,
            )
            # A previously running job is distinct from a human-paused job: it is
            # safe to resume because the adapter checks persisted interaction state
            # before it can submit anything again.
            _transition(
                run_dir,
                state,
                job_id,
                "queued",
                reason="resuming interrupted job; adapter will inspect saved interaction state",
                announce=announce,
            )
            continue
        if status == "waiting_for_human":
            handoff_kind = job_state.get("interaction", {}).get("handoff_kind")
            # A saved model-response handoff awaits human input; never resubmit it.
            if resume_waiting_for_human and handoff_kind != "model_response":
                _transition(
                    run_dir,
                    state,
                    job_id,
                    "queued",
                    reason="explicitly resuming saved human-paused job",
                    announce=announce,
                )
            continue
        if status == "failed" and (retry_failed or job_id in retry_job_ids):
            reason = (
                "explicit retry requested"
                if retry_failed
                else "bounded retry of an explicitly retryable failure"
            )
            _transition(
                run_dir,
                state,
                job_id,
                "queued",
                reason=reason,
                announce=announce,
            )
        elif status == "blocked" and (retry_failed or retry_blocked):
            _transition(
                run_dir,
                state,
                job_id,
                "queued",
                reason="retrying after a dependency retry",
                announce=announce,
            )


def _block_failed_dependencies(
    run_dir: Path,
    state: dict[str, Any],
    announce: Callable[[dict[str, Any]], None] | None,
) -> None:
    for job_id, job_state in list(state["jobs"].items()):
        if job_state["status"] != "queued":
            continue
        bad = [
            dependency
            for dependency in job_state.get("dependencies", [])
            if state["jobs"][dependency]["status"] in {"failed", "blocked"}
        ]
        if bad:
            _transition(
                run_dir,
                state,
                job_id,
                "blocked",
                reason=f"dependency did not complete: {', '.join(bad)}",
                announce=announce,
            )


def _summary(state: dict[str, Any]) -> str:
    statuses = [row["status"] for row in state["jobs"].values()]
    if statuses and all(status == "completed" for status in statuses):
        return "completed"
    if "waiting_for_human" in statuses:
        return "waiting_for_human"
    if "failed" in statuses or "blocked" in statuses:
        return "failed_or_blocked"
    return "in_progress"


async def run_mission(
    mission_path: str | Path,
    *,
    resume_dir: str | Path | None = None,
    retry_failed: bool = False,
    retry_job_ids: set[str] | None = None,
    retry_blocked: bool = False,
    resume_waiting_for_human: bool = True,
    max_parallel: int = 1,
    executor: JobExecutor | None = None,
    announce: Callable[[dict[str, Any]], None] | None = _event_printer,
) -> tuple[Path, dict[str, Any]]:
    """Run or resume a mission. Completed jobs are immutable and never repeated."""
    if max_parallel < 1 or max_parallel > 16:
        raise ValueError("max_parallel must be between 1 and 16")
    if not resume_dir and (retry_job_ids or retry_blocked or not resume_waiting_for_human):
        raise ValueError("retry/resume controls require an existing resume_dir")
    spec = load_mission(mission_path)
    run_dir, state = _prepare_run(spec, Path(resume_dir) if resume_dir else None)
    lock_path = _acquire_run_lock(run_dir)
    tasks: set[asyncio.Task[None]] = set()
    try:
        if resume_dir:
            # Reload after acquiring the lock to avoid acting on a stale state read
            # if another runner finished between our initial path lookup and lock.
            run_dir, state = _prepare_run(spec, run_dir)
            _reset_for_resume(
                run_dir,
                state,
                retry_failed=retry_failed,
                announce=announce,
                resume_waiting_for_human=resume_waiting_for_human,
                retry_job_ids=retry_job_ids,
                retry_blocked=retry_blocked,
            )
        if executor is None:
            from runtime.executor import BrowserSiteExecutor

            executor = BrowserSiteExecutor()

        while True:
            _block_failed_dependencies(run_dir, state, announce)
            ready = [
                job
                for job in spec.jobs
                if state["jobs"][job.job_id]["status"] == "queued"
                and all(
                    state["jobs"][dependency]["status"] == "completed"
                    for dependency in job.dependencies
                )
            ]
            capacity = max_parallel - len(tasks)
            for job in ready[: max(0, capacity)]:
                task = asyncio.create_task(
                    _execute_one(spec, job, run_dir, state, executor, announce)
                )
                tasks.add(task)
            if tasks:
                done, pending = await asyncio.wait(
                    tasks, return_when=asyncio.FIRST_COMPLETED
                )
                tasks = set(pending)
                # _execute_one records failures; retrieve unexpected cancellation/errors.
                for task in done:
                    try:
                        await task
                    except asyncio.CancelledError:
                        raise
                    except Exception as exc:
                        print(
                            f"Internal scheduler error: {type(exc).__name__}: {exc}",
                            flush=True,
                        )
                continue
            if not ready:
                break
        state["run_status"] = _summary(state)
        _persist_state(run_dir, state)
        return run_dir, state
    except asyncio.CancelledError:
        for task in tasks:
            task.cancel()
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        state["run_status"] = _summary(state)
        _persist_state(run_dir, state)
        raise
    finally:
        try:
            close = getattr(executor, "close", None) if executor is not None else None
            if close is not None:
                await close()
        finally:
            _release_run_lock(lock_path)
