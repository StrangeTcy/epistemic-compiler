"""Configuration-driven mission workbench over the existing local DAG runner.

The workbench discovers ``mission-*/workbench.yaml`` files, materializes one
immutable DAG run per manually dispatched role/sample set, and delegates run
state, prompt/input snapshots, transitions, and response hashes to
``runtime.engine``. It never calls a model or changes a human gate.
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

from runtime import engine

PROJECT_ROOT = Path(__file__).resolve().parents[1]
WORKBENCH_SPEC_ROOT = PROJECT_ROOT / "runtime" / "workbench_specs"
_MISSION_ID = re.compile(r"mission-[A-Za-z0-9][A-Za-z0-9._-]{0,55}\Z")
_ITEM_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}\Z")
_PLACEHOLDER = re.compile(r"\{\{\s*([A-Za-z0-9_.-]+)\s*\}\}")


class WorkbenchError(ValueError):
    """Invalid workbench configuration, run, or response artifact."""


class WorkbenchBlocked(WorkbenchError):
    """A human hold, gate, or unresolved design decision prevents staging."""


class _UniqueKeyLoader(yaml.SafeLoader):
    pass


def _construct_unique_mapping(loader: _UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False):
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise WorkbenchError(f"duplicate YAML key: {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping
)


@dataclass(frozen=True)
class WorkbenchMission:
    mission_id: str
    title: str
    path: Path
    data: dict[str, Any]

    @property
    def sha256(self) -> str:
        return _sha256_file(self.path)


@dataclass(frozen=True)
class StagedRun:
    run_dir: Path
    state: dict[str, Any]
    stage_id: str
    role_id: str
    sample_ids: tuple[str, ...]
    prompt_path: Path
    prompt_sha256: str


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")


def _write_once_or_verify(path: Path, data: bytes) -> None:
    """Create a file once, accepting an identical retry but never replacing it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    except FileExistsError:
        if path.read_bytes() == data:
            return
        raise WorkbenchError(f"immutable workbench artifact already exists with different bytes: {path}")
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except Exception:
        path.unlink(missing_ok=True)
        raise


def _repo_path(value: Any, field: str, *, must_exist: bool = False) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise WorkbenchError(f"{field} must be a repository-relative path")
    raw = value.strip()
    pure = PurePosixPath(raw)
    if (
        pure.is_absolute()
        or "\\" in raw
        or ":" in raw
        or any(part in {"", ".", ".."} for part in pure.parts)
    ):
        raise WorkbenchError(f"{field} must be a safe repository-relative path: {raw!r}")
    root = PROJECT_ROOT.resolve()
    resolved = (root / Path(*pure.parts)).resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise WorkbenchError(f"{field} escapes the repository: {raw!r}") from exc
    if must_exist and not resolved.is_file():
        raise FileNotFoundError(f"{field} not found: {resolved}")
    return resolved


def _normalized_repo_key(path: Path) -> str:
    return path.resolve().relative_to(PROJECT_ROOT.resolve()).as_posix().casefold()


def _require_mapping(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict) or any(not isinstance(key, str) for key in value):
        raise WorkbenchError(f"{field} must be a mapping with string keys")
    return value


def _require_string(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise WorkbenchError(f"{field} must be a non-empty string")
    return value.strip()


def _require_bool(value: Any, field: str) -> bool:
    if not isinstance(value, bool):
        raise WorkbenchError(f"{field} must be a boolean")
    return value


def _require_string_list(value: Any, field: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
        raise WorkbenchError(f"{field} must be a list of non-empty strings")
    values = [item.strip() for item in value]
    if len(values) != len(set(values)):
        raise WorkbenchError(f"{field} must not contain duplicates")
    return values


def _validate_prompt(prompt: Any, field: str, *, check_files: bool) -> dict[str, Any]:
    prompt_map = _require_mapping(prompt, field)
    unknown = set(prompt_map) - {"source", "template", "context"}
    if unknown:
        raise WorkbenchError(f"unknown fields in {field}: {', '.join(sorted(unknown))}")
    source = prompt_map.get("source")
    template = prompt_map.get("template")
    if (source is None) == (template is None):
        raise WorkbenchError(f"{field} requires exactly one of source or template")
    if source is not None:
        _repo_path(source, f"{field}.source", must_exist=check_files)
        if prompt_map.get("context") not in (None, {}):
            raise WorkbenchError(f"{field}.context is only valid with a template")
        return {"source": source}
    _repo_path(template, f"{field}.template", must_exist=check_files)
    context = _require_mapping(prompt_map.get("context", {}), f"{field}.context")
    for name, path in context.items():
        if not _ITEM_ID.fullmatch(name):
            raise WorkbenchError(f"invalid prompt context id {name!r} in {field}")
        _repo_path(path, f"{field}.context.{name}", must_exist=check_files)
    return {"template": template, "context": dict(context)}


def _validate_manifest(path: Path, raw: Any, *, check_files: bool) -> WorkbenchMission:
    data = _require_mapping(raw, str(path))
    allowed = {
        "schema_version", "mission_id", "title", "lifecycle", "human_hold",
        "gate_status", "stages", "description",
    }
    unknown = set(data) - allowed
    if unknown:
        raise WorkbenchError(f"unknown fields in {path}: {', '.join(sorted(unknown))}")
    if data.get("schema_version") != 1:
        raise WorkbenchError(f"{path}: schema_version must be 1")
    mission_id = _require_string(data.get("mission_id"), f"{path}.mission_id")
    if not _MISSION_ID.fullmatch(mission_id):
        raise WorkbenchError(f"invalid mission_id {mission_id!r}")
    title = _require_string(data.get("title"), f"{path}.title")
    lifecycle = data.get("lifecycle")
    if not isinstance(lifecycle, str) or lifecycle not in {"active", "proposal", "on_hold", "closed"}:
        raise WorkbenchError(f"{path}.lifecycle must be active, proposal, on_hold, or closed")
    human_hold = _require_bool(data.get("human_hold"), f"{path}.human_hold")
    gate_status = _require_mapping(data.get("gate_status", {}), f"{path}.gate_status")
    for key, value in gate_status.items():
        _require_string(key, f"{path}.gate_status key")
        _require_string(value, f"{path}.gate_status.{key}")
    stages = data.get("stages")
    if not isinstance(stages, list):
        raise WorkbenchError(f"{path}.stages must be a list")
    stage_ids: set[str] = set()
    canonical_outputs: set[str] = set()
    for index, stage in enumerate(stages):
        stage_field = f"{path}.stages[{index}]"
        stage_map = _require_mapping(stage, stage_field)
        stage_allowed = {
            "id", "label", "status", "authorized", "authorization_basis",
            "blockers", "next_action", "roles",
        }
        stage_unknown = set(stage_map) - stage_allowed
        if stage_unknown:
            raise WorkbenchError(f"unknown fields in {stage_field}: {', '.join(sorted(stage_unknown))}")
        stage_id = _require_string(stage_map.get("id"), f"{stage_field}.id")
        if not _ITEM_ID.fullmatch(stage_id) or stage_id in stage_ids:
            raise WorkbenchError(f"invalid or duplicate stage id {stage_id!r}")
        stage_ids.add(stage_id)
        _require_string(stage_map.get("label"), f"{stage_field}.label")
        if not isinstance(stage_map.get("status"), str) or stage_map["status"] not in {"active", "planned", "blocked", "complete", "closed"}:
            raise WorkbenchError(f"{stage_field}.status is invalid")
        _require_bool(stage_map.get("authorized"), f"{stage_field}.authorized")
        if stage_map.get("authorization_basis") is not None:
            _require_string(stage_map["authorization_basis"], f"{stage_field}.authorization_basis")
        _require_string_list(stage_map.get("blockers", []), f"{stage_field}.blockers")
        if stage_map.get("next_action") is not None:
            _require_string(stage_map["next_action"], f"{stage_field}.next_action")
        roles = stage_map.get("roles", [])
        if not isinstance(roles, list):
            raise WorkbenchError(f"{stage_field}.roles must be a list")
        role_ids: set[str] = set()
        for role_index, role in enumerate(roles):
            role_field = f"{stage_field}.roles[{role_index}]"
            role_map = _require_mapping(role, role_field)
            role_allowed = {
                "id", "label", "prompt", "inputs", "sample_artifacts",
                "min_samples", "max_samples", "metadata_required", "blindness",
                "legacy_metadata_note",
            }
            role_unknown = set(role_map) - role_allowed
            if role_unknown:
                raise WorkbenchError(f"unknown fields in {role_field}: {', '.join(sorted(role_unknown))}")
            role_id = _require_string(role_map.get("id"), f"{role_field}.id")
            if not _ITEM_ID.fullmatch(role_id) or role_id in role_ids:
                raise WorkbenchError(f"invalid or duplicate role id {role_id!r} in {stage_id}")
            role_ids.add(role_id)
            _require_string(role_map.get("label"), f"{role_field}.label")
            _validate_prompt(role_map.get("prompt"), f"{role_field}.prompt", check_files=check_files)
            role_inputs = _require_mapping(role_map.get("inputs", {}), f"{role_field}.inputs")
            for input_id, input_path in role_inputs.items():
                if not _ITEM_ID.fullmatch(input_id):
                    raise WorkbenchError(f"invalid input id {input_id!r} in {role_field}")
                _repo_path(input_path, f"{role_field}.inputs.{input_id}", must_exist=check_files)
            sample_artifacts = _require_mapping(role_map.get("sample_artifacts"), f"{role_field}.sample_artifacts")
            if not sample_artifacts:
                raise WorkbenchError(f"{role_field}.sample_artifacts must not be empty")
            for sample_id, artifact in sample_artifacts.items():
                if not _ITEM_ID.fullmatch(sample_id):
                    raise WorkbenchError(f"invalid sample id {sample_id!r} in {role_field}")
                artifact_path = _repo_path(artifact, f"{role_field}.sample_artifacts.{sample_id}")
                artifact_key = artifact_path.as_posix().casefold()
                intake_path = _intake_path(artifact_path)
                for output_path in (artifact_path, intake_path):
                    output_key = output_path.as_posix().casefold()
                    if output_key in canonical_outputs:
                        raise WorkbenchError(f"canonical output path is reused: {output_path}")
                    canonical_outputs.add(output_key)
                if artifact_key == intake_path.as_posix().casefold():
                    raise WorkbenchError(f"invalid canonical response/intake path for {artifact}")
            min_samples = role_map.get("min_samples")
            max_samples = role_map.get("max_samples")
            if not isinstance(min_samples, int) or isinstance(min_samples, bool) or min_samples < 1:
                raise WorkbenchError(f"{role_field}.min_samples must be a positive integer")
            if not isinstance(max_samples, int) or isinstance(max_samples, bool) or max_samples < min_samples:
                raise WorkbenchError(f"{role_field}.max_samples must be an integer >= min_samples")
            if max_samples > len(sample_artifacts):
                raise WorkbenchError(f"{role_field}.max_samples exceeds declared sample_artifacts")
            _require_string_list(
                role_map.get("metadata_required", []), f"{role_field}.metadata_required"
            )
            if role_map.get("legacy_metadata_note") is not None:
                _require_string(role_map["legacy_metadata_note"], f"{role_field}.legacy_metadata_note")
            blindness = role_map.get("blindness")
            if blindness is not None:
                blindness_map = _require_mapping(blindness, f"{role_field}.blindness")
                blindness_unknown = set(blindness_map) - {"forbidden_sources", "forbidden_literals"}
                if blindness_unknown:
                    raise WorkbenchError(f"unknown fields in {role_field}.blindness: {', '.join(sorted(blindness_unknown))}")
                for forbidden_path in _require_string_list(
                    blindness_map.get("forbidden_sources", []), f"{role_field}.blindness.forbidden_sources"
                ):
                    _repo_path(forbidden_path, f"{role_field}.blindness.forbidden_sources")
                _require_string_list(
                    blindness_map.get("forbidden_literals", []), f"{role_field}.blindness.forbidden_literals"
                )

    return WorkbenchMission(mission_id=mission_id, title=title, path=path, data=data)


def load_mission(mission_id: str, *, check_files: bool = True) -> WorkbenchMission:
    if not isinstance(mission_id, str) or not _MISSION_ID.fullmatch(mission_id):
        raise WorkbenchError(f"invalid mission id {mission_id!r}")
    manifest_path = _repo_path(f"{mission_id}/workbench.yaml", "workbench manifest", must_exist=True)
    try:
        raw = yaml.load(manifest_path.read_text(encoding="utf-8"), Loader=_UniqueKeyLoader)
    except yaml.YAMLError as exc:
        raise WorkbenchError(f"invalid YAML in {manifest_path}: {exc}") from exc
    return _validate_manifest(manifest_path, raw, check_files=check_files)


def discover_missions(*, check_files: bool = True) -> list[WorkbenchMission]:
    missions: list[WorkbenchMission] = []
    for path in sorted(PROJECT_ROOT.glob("mission-*/workbench.yaml")):
        try:
            raw = yaml.load(path.read_text(encoding="utf-8"), Loader=_UniqueKeyLoader)
        except yaml.YAMLError as exc:
            raise WorkbenchError(f"invalid YAML in {path}: {exc}") from exc
        mission = _validate_manifest(path, raw, check_files=check_files)
        if mission.path.parent.name != mission.mission_id:
            raise WorkbenchError(f"manifest mission_id does not match its directory: {mission.path}")
        missions.append(mission)
    return missions


def _intake_path(response_path: Path) -> Path:
    if response_path.suffix.lower() == ".md":
        return response_path.with_name(response_path.stem + ".intake.json")
    return response_path.with_name(response_path.name + ".intake.json")


def _role_by_id(stage: dict[str, Any], role_id: str) -> dict[str, Any]:
    for role in stage.get("roles", []):
        if role.get("id") == role_id:
            return role
    raise WorkbenchError(f"unknown role {role_id!r} in stage {stage.get('id')!r}")


def _sample_records(role: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for sample_id, artifact in role["sample_artifacts"].items():
        path = _repo_path(artifact, f"sample artifact {sample_id}")
        intake_path = _intake_path(path)
        record: dict[str, Any] = {
            "sample_id": sample_id,
            "path": path,
            "intake_path": intake_path,
            "intake_status": "missing",
            "missing_metadata": None,
        }
        if not path.exists():
            record.update({"status": "missing", "sha256": None})
        elif not path.is_file():
            record.update({"status": "invalid_not_file", "sha256": None})
        elif path.stat().st_size == 0:
            record.update({"status": "invalid_empty", "sha256": _sha256_file(path)})
        else:
            record.update({"status": "recorded", "sha256": _sha256_file(path)})
            if not intake_path.is_file():
                record["intake_status"] = "no_structured_sidecar"
            else:
                try:
                    intake = json.loads(intake_path.read_text(encoding="utf-8"))
                    if not isinstance(intake, dict):
                        raise ValueError("intake record is not a mapping")
                    missing = intake.get("missing_metadata", [])
                    if not isinstance(missing, list) or any(not isinstance(item, str) for item in missing):
                        raise ValueError("missing_metadata must be a list of strings")
                    record["intake_status"] = "recorded"
                    record["missing_metadata"] = missing
                    record["model_label"] = intake.get("model_label")
                except (OSError, json.JSONDecodeError, ValueError) as exc:
                    record["intake_status"] = "invalid_sidecar"
                    record["intake_error"] = str(exc)
        records.append(record)
    return records


def _stage_status(mission: WorkbenchMission, stage: dict[str, Any]) -> dict[str, Any]:
    role_rows: list[dict[str, Any]] = []
    for role in stage.get("roles", []):
        samples = _sample_records(role)
        recorded = sum(row["status"] == "recorded" for row in samples)
        invalid = [row for row in samples if row["status"].startswith("invalid_")]
        role_rows.append(
            {
                "id": role["id"],
                "label": role["label"],
                "recorded_samples": recorded,
                "minimum_samples": role["min_samples"],
                "maximum_samples": role["max_samples"],
                "complete": recorded >= role["min_samples"],
                "legacy_metadata_note": role.get("legacy_metadata_note"),
                "samples": samples,
                "invalid_artifacts": invalid,
            }
        )
    return {
        "id": stage["id"],
        "label": stage["label"],
        "status": stage["status"],
        "authorized": stage["authorized"],
        "authorization_basis": stage.get("authorization_basis"),
        "blockers": list(stage.get("blockers", [])),
        "next_action": stage.get("next_action"),
        "roles": role_rows,
    }


def _run_directories(mission_id: str) -> list[Path]:
    root = engine.RUN_ROOT / mission_id
    if not root.is_dir():
        return []
    candidates = [path for path in root.iterdir() if path.is_dir() and (path / engine.STATE_FILE).is_file()]
    return sorted(candidates, key=lambda path: path.stat().st_mtime, reverse=True)


def _load_run_state(run_dir: Path) -> dict[str, Any]:
    state_path = run_dir / engine.STATE_FILE
    if not state_path.is_file():
        raise FileNotFoundError(f"run state not found: {state_path}")
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise WorkbenchError(f"invalid run state {state_path}: {exc}") from exc
    if not isinstance(state, dict) or not isinstance(state.get("jobs"), dict):
        raise WorkbenchError(f"run state has an invalid structure: {state_path}")
    return state


def mission_status(mission_id: str) -> dict[str, Any]:
    mission = load_mission(mission_id, check_files=False)
    stages = [_stage_status(mission, stage) for stage in mission.data["stages"]]
    pending = next(
        (
            (stage["id"], role["id"], role)
            for stage in mission.data["stages"]
            if stage["status"] == "active"
            for role in stage.get("roles", [])
            if sum(row["status"] == "recorded" for row in _sample_records(role)) < role["min_samples"]
        ),
        None,
    )
    runs = []
    for run_dir in _run_directories(mission_id)[:5]:
        state = _load_run_state(run_dir)
        runs.append(
            {
                "run_id": state.get("run_id"),
                "run_dir": str(run_dir),
                "run_status": state.get("run_status", "unknown"),
                "created_at": state.get("created_at"),
                "jobs": {
                    job_id: row.get("status", "unknown")
                    for job_id, row in state.get("jobs", {}).items()
                },
            }
        )
    return {
        "mission_id": mission.mission_id,
        "title": mission.title,
        "lifecycle": mission.data["lifecycle"],
        "human_hold": mission.data["human_hold"],
        "gate_status": mission.data.get("gate_status", {}),
        "stages": stages,
        "pending_role": {"stage_id": pending[0], "role_id": pending[1]} if pending else None,
        "runs": runs,
    }


def _format_status(status: dict[str, Any]) -> str:
    lifecycle = status["lifecycle"].upper()
    hold = " | HUMAN HOLD" if status["human_hold"] else ""
    lines = [f"{status['mission_id']} — {status['title']}", f"Lifecycle: {lifecycle}{hold}"]
    gates = status["gate_status"]
    if gates:
        lines.append("Gates:")
        for gate, value in gates.items():
            lines.append(f"  {gate}: {value}")
    for stage in status["stages"]:
        authorization = "authorized" if stage["authorized"] else "not authorized"
        lines.append(f"Stage {stage['id']}: {stage['status']} ({authorization})")
        if stage.get("authorization_basis"):
            lines.append(f"  Authorization basis: {stage['authorization_basis']}")
        for blocker in stage["blockers"]:
            lines.append(f"  BLOCKER: {blocker}")
        if stage.get("next_action"):
            lines.append(f"  Next action: {stage['next_action']}")
        for role in stage["roles"]:
            lines.append(
                f"  {role['label']}: {role['recorded_samples']}/{role['minimum_samples']} required samples "
                f"(max {role['maximum_samples']})"
            )
            if role.get("legacy_metadata_note"):
                lines.append(f"    Legacy provenance note: {role['legacy_metadata_note']}")
            for sample in role["samples"]:
                if sample["status"] == "recorded":
                    lines.append(f"    {sample['sample_id']}: sha256={sample['sha256']} ({sample['path']})")
                    if sample["intake_status"] == "recorded":
                        lines.append(
                            f"      intake metadata: model_label={sample.get('model_label')!r}; "
                            f"missing={sample.get('missing_metadata', [])!r} ({sample['intake_path']})"
                        )
                    elif sample["intake_status"] == "invalid_sidecar":
                        lines.append(f"      INVALID intake sidecar: {sample.get('intake_error')} ({sample['intake_path']})")
                    else:
                        lines.append(f"      intake sidecar: {sample['intake_status']} ({sample['intake_path']})")
                elif sample["status"].startswith("invalid_"):
                    lines.append(f"    {sample['sample_id']}: {sample['status']} ({sample['path']})")
    if status["pending_role"]:
        lines.append(
            f"Next required role: {status['pending_role']['stage_id']} / {status['pending_role']['role_id']}"
        )
    elif status["lifecycle"] == "active":
        lines.append("No required role is pending. Human gate decisions remain separate.")
    if status["runs"]:
        latest = status["runs"][0]
        lines.append(f"Latest local run: {latest['run_id']} ({latest['run_status']}) — {latest['run_dir']}")
        for job_id, job_status in latest["jobs"].items():
            lines.append(f"  {job_id}: {job_status}")
    return "\n".join(lines)


def validate_mission(mission_id: str) -> str:
    """Validate one manifest, its configured prompt/input paths, and recorded role artifacts."""
    mission = load_mission(mission_id, check_files=True)
    status = mission_status(mission_id)
    errors: list[str] = []
    for stage in status["stages"]:
        for role in stage["roles"]:
            for sample in role["samples"]:
                sample_name = f"{stage['id']}/{role['id']}/{sample['sample_id']}"
                if sample["status"].startswith("invalid_"):
                    errors.append(f"{sample_name}: {sample['status']}")
                if sample["intake_status"] == "invalid_sidecar":
                    errors.append(f"{sample_name}: invalid intake sidecar ({sample.get('intake_error')})")
                if sample["status"] == "recorded":
                    response_bytes = sample["path"].read_bytes()
                    if len(response_bytes) > 20 * 1024 * 1024:
                        errors.append(f"{sample_name}: response exceeds the 20 MiB ingestion limit")
                    try:
                        response_text = response_bytes.decode("utf-8")
                    except UnicodeDecodeError:
                        errors.append(f"{sample_name}: response is not UTF-8 text")
                    else:
                        if not response_text.strip():
                            errors.append(f"{sample_name}: response is whitespace-only")
    if errors:
        raise WorkbenchError("validation failed:\n- " + "\n- ".join(errors))
    return (
        f"Manifest and configured prompt/input paths validate: {mission.path} "
        f"(sha256={mission.sha256})\n"
        + _format_status(status)
    )


def list_statuses() -> list[dict[str, Any]]:
    return [mission_status(mission.mission_id) for mission in discover_missions(check_files=False)]


def _active_handoffs(mission_id: str) -> list[tuple[Path, dict[str, Any], str, dict[str, Any]]]:
    active: list[tuple[Path, dict[str, Any], str, dict[str, Any]]] = []
    for run_dir in _run_directories(mission_id):
        state = _load_run_state(run_dir)
        for job_id, job_state in state.get("jobs", {}).items():
            interaction = job_state.get("interaction", {})
            if (
                job_state.get("status") == "waiting_for_human"
                and interaction.get("handoff_kind") == "model_response"
            ):
                active.append((run_dir, state, job_id, job_state))
        if active:
            break
    return active


def _stage_for_job(mission: WorkbenchMission, job_state: dict[str, Any]) -> dict[str, Any]:
    role_name = job_state.get("role")
    if not isinstance(role_name, str):
        raise WorkbenchError("run job has no workbench role label")
    parts = role_name.split(":")
    if len(parts) != 3:
        raise WorkbenchError(f"run job role is not a workbench role: {role_name!r}")
    stage_id, role_id, sample_id = parts
    stage = next((item for item in mission.data["stages"] if item["id"] == stage_id), None)
    if stage is None:
        raise WorkbenchError(f"run references unknown workbench stage {stage_id!r}")
    role = _role_by_id(stage, role_id)
    if sample_id not in role["sample_artifacts"]:
        raise WorkbenchError(f"run references unknown sample {sample_id!r} for {role_id}")
    return stage


def _assert_stage_can_run(mission: WorkbenchMission, stage: dict[str, Any]) -> None:
    if mission.data["human_hold"] or mission.data["lifecycle"] == "on_hold":
        raise WorkbenchBlocked(f"{mission.mission_id} is on human HOLD; no workbench action can override it")
    if mission.data["lifecycle"] == "closed":
        raise WorkbenchBlocked(f"{mission.mission_id} is closed; it will not be reopened by the workbench")
    if stage["status"] == "blocked" or stage.get("blockers"):
        blockers = stage.get("blockers", []) or ["stage is blocked"]
        message = "\n".join(f"- {item}" for item in blockers)
        raise WorkbenchBlocked(f"{stage['label']} is blocked:\n{message}")
    if stage["status"] != "active":
        raise WorkbenchBlocked(f"stage {stage['id']} is {stage['status']!r}, not active")
    if not stage["authorized"]:
        raise WorkbenchBlocked(f"stage {stage['id']} has no human authorization")


def _assert_job_authorized(mission: WorkbenchMission, job_state: dict[str, Any]) -> None:
    stage = _stage_for_job(mission, job_state)
    _assert_stage_can_run(mission, stage)


def _assert_run_jobs_authorized(mission: WorkbenchMission, state: dict[str, Any]) -> None:
    active_statuses = {"queued", "running", "waiting_for_human", "failed", "blocked"}
    for job_state in state.get("jobs", {}).values():
        if job_state.get("status") not in active_statuses:
            continue
        _assert_job_authorized(mission, job_state)


def _render_prompt(role: dict[str, Any]) -> tuple[bytes, list[dict[str, Any]], set[str]]:
    prompt_cfg = role["prompt"]
    source_records: list[dict[str, Any]] = []
    source_paths: set[str] = set()
    if "source" in prompt_cfg:
        source_path = _repo_path(prompt_cfg["source"], "prompt source", must_exist=True)
        prompt_bytes = source_path.read_bytes()
        source_paths.add(_normalized_repo_key(source_path))
        source_records.append({"path": prompt_cfg["source"], "sha256": _sha256_bytes(prompt_bytes), "kind": "exact_source"})
    else:
        template_path = _repo_path(prompt_cfg["template"], "prompt template", must_exist=True)
        template_bytes = template_path.read_bytes()
        try:
            prompt_text = template_bytes.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise WorkbenchError(f"prompt template must be UTF-8: {template_path}") from exc
        source_paths.add(_normalized_repo_key(template_path))
        source_records.append({"path": prompt_cfg["template"], "sha256": _sha256_bytes(template_bytes), "kind": "template"})
        for name, relative_path in prompt_cfg.get("context", {}).items():
            context_path = _repo_path(relative_path, f"prompt context {name}", must_exist=True)
            context_bytes = context_path.read_bytes()
            try:
                context_text = context_bytes.decode("utf-8")
            except UnicodeDecodeError as exc:
                raise WorkbenchError(f"prompt context must be UTF-8: {context_path}") from exc
            marker = "{{" + name + "}}"
            if marker not in prompt_text:
                raise WorkbenchError(f"prompt template lacks required marker {marker}")
            prompt_text = prompt_text.replace(marker, context_text)
            source_paths.add(_normalized_repo_key(context_path))
            source_records.append({"path": relative_path, "sha256": _sha256_bytes(context_bytes), "kind": "context"})
        unresolved = _PLACEHOLDER.findall(prompt_text)
        if unresolved:
            raise WorkbenchError("unresolved prompt placeholders: " + ", ".join(sorted(set(unresolved))))
        prompt_bytes = prompt_text.encode("utf-8")

    blindness = role.get("blindness") or {}
    forbidden_sources = {
        _normalized_repo_key(_repo_path(path, "blindness forbidden source"))
        for path in blindness.get("forbidden_sources", [])
    }
    leaking_sources = sorted(source_paths & forbidden_sources)
    if leaking_sources:
        raise WorkbenchError("blind prompt includes forbidden source(s): " + ", ".join(leaking_sources))
    try:
        prompt_text = prompt_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise WorkbenchError("manual Arena prompts must be UTF-8 text") from exc
    prompt_folded = prompt_text.casefold()
    leaking_literals = [
        literal
        for literal in blindness.get("forbidden_literals", [])
        if literal.casefold() in prompt_folded
    ]
    if leaking_literals:
        raise WorkbenchError("blind prompt contains forbidden literal(s): " + ", ".join(leaking_literals))
    return prompt_bytes, source_records, source_paths


def _materialize_role_run(
    mission: WorkbenchMission,
    stage: dict[str, Any],
    role: dict[str, Any],
    sample_ids: list[str],
) -> StagedRun:
    prompt_bytes, prompt_sources, _ = _render_prompt(role)
    input_paths: dict[str, Path] = {
        input_id: _repo_path(relative_path, f"{role['id']} input {input_id}", must_exist=True)
        for input_id, relative_path in role.get("inputs", {}).items()
    }
    prompt_cfg = role["prompt"]
    if "template" in prompt_cfg:
        for context_id, relative_path in prompt_cfg.get("context", {}).items():
            if context_id in input_paths and input_paths[context_id] != _repo_path(relative_path, f"prompt context {context_id}"):
                raise WorkbenchError(f"prompt context id {context_id!r} conflicts with an input path")
            input_paths.setdefault(context_id, _repo_path(relative_path, f"prompt context {context_id}", must_exist=True))
    input_hashes = {input_id: _sha256_file(path) for input_id, path in input_paths.items()}
    config_identity = {
        "manifest_sha256": mission.sha256,
        "mission_id": mission.mission_id,
        "stage": stage["id"],
        "role": role["id"],
        "sample_ids": sample_ids,
        "prompt_sha256": _sha256_bytes(prompt_bytes),
        "prompt_sources": prompt_sources,
        "input_hashes": input_hashes,
    }
    digest = _sha256_bytes(_canonical_json(config_identity))
    spec_dir = WORKBENCH_SPEC_ROOT / mission.mission_id / stage["id"] / role["id"] / digest[:20]
    spec_dir.mkdir(parents=True, exist_ok=True)
    if "source" in prompt_cfg:
        prompt_path = _repo_path(prompt_cfg["source"], "prompt source", must_exist=True)
    else:
        prompt_path = spec_dir / "prompt.md"
        _write_once_or_verify(prompt_path, prompt_bytes)

    mission_inputs = {input_id: str(path.resolve()) for input_id, path in input_paths.items()}
    jobs = []
    for sample_id in sample_ids:
        job_id = f"{role['id']}_{sample_id}"
        response_path = _repo_path(role["sample_artifacts"][sample_id], f"response artifact {sample_id}")
        intake_path = _intake_path(response_path)
        for output_path in (response_path, intake_path):
            if output_path.exists():
                raise WorkbenchError(f"canonical sample output already exists; refusing overwrite: {output_path}")
        jobs.append(
            {
                "id": job_id,
                "role": f"{stage['id']}:{role['id']}:{sample_id}",
                "site": "manual_arena",
                "model": None,
                "prompt_artifact": str(prompt_path.resolve()),
                "input_artifacts": [f"mission:{input_id}" for input_id in input_paths],
                "metadata_required": role.get("metadata_required", []),
                "canonical_response_artifact": response_path.relative_to(PROJECT_ROOT.resolve()).as_posix(),
                "canonical_ingestion_artifact": intake_path.relative_to(PROJECT_ROOT.resolve()).as_posix(),
                "output_artifact": f"artifacts/jobs/{job_id}/response.md",
            }
        )

    spec_payload = {
        "mission_id": mission.mission_id,
        "type": f"workbench:{stage['id']}",
        "inputs": mission_inputs,
        "jobs": jobs,
    }
    spec_bytes = yaml.safe_dump(spec_payload, sort_keys=False, allow_unicode=True).encode("utf-8")
    spec_path = spec_dir / "mission.yaml"
    _write_once_or_verify(spec_path, spec_bytes)
    run_dir, state = asyncio.run(engine.run_mission(spec_path, max_parallel=1))
    prompt_hash = _sha256_bytes(prompt_bytes)
    return StagedRun(
        run_dir=run_dir,
        state=state,
        stage_id=stage["id"],
        role_id=role["id"],
        sample_ids=tuple(sample_ids),
        prompt_path=run_dir / "inputs" / "prompts" / f"{role['id']}_{sample_ids[0]}.md",
        prompt_sha256=prompt_hash,
    )


def _choose_active_stage(mission: WorkbenchMission, stage_id: str | None) -> dict[str, Any]:
    stages = mission.data["stages"]
    if stage_id is not None:
        stage = next((item for item in stages if item["id"] == stage_id), None)
        if stage is None:
            raise WorkbenchError(f"unknown stage {stage_id!r} in {mission.mission_id}")
        return stage
    for stage in stages:
        if stage["status"] == "active":
            return stage
    raise WorkbenchBlocked(f"{mission.mission_id} has no active stage")


def _existing_active_run(mission: WorkbenchMission) -> tuple[Path, dict[str, Any]] | None:
    for run_dir in _run_directories(mission.mission_id):
        state = _load_run_state(run_dir)
        if state.get("run_status") != "completed":
            return run_dir, state
    return None


def stage_next(
    mission_id: str,
    *,
    stage_id: str | None = None,
    role_id: str | None = None,
    sample_ids: list[str] | None = None,
) -> StagedRun:
    mission = load_mission(mission_id, check_files=False)
    if mission.data["human_hold"] or mission.data["lifecycle"] in {"on_hold", "closed"}:
        _assert_stage_can_run(mission, mission.data["stages"][0] if mission.data["stages"] else {"id": "none", "status": "blocked", "authorized": False, "blockers": []})
    stage = _choose_active_stage(mission, stage_id)
    _assert_stage_can_run(mission, stage)

    active = _existing_active_run(mission)
    if active is not None:
        run_dir, state = active
        waiting = _active_handoffs(mission_id)
        if waiting and waiting[0][0] == run_dir:
            raise WorkbenchBlocked(
                f"{mission_id} already has an active manual handoff in {run_dir}; use `resume {mission_id}` to display the saved exact prompt"
            )
        raise WorkbenchBlocked(
            f"{mission_id} already has a resumable run in {run_dir}; use `resume {mission_id}` before staging another role"
        )

    if role_id is None:
        role = next(
            (
                candidate
                for candidate in stage.get("roles", [])
                if sum(row["status"] == "recorded" for row in _sample_records(candidate)) < candidate["min_samples"]
            ),
            None,
        )
        if role is None:
            raise WorkbenchBlocked(
                f"all required roles in {stage['id']} are recorded; no human gate is inferred or approved"
            )
    else:
        role = _role_by_id(stage, role_id)
        if sum(row["status"] == "invalid_empty" or row["status"] == "invalid_not_file" for row in _sample_records(role)):
            raise WorkbenchError(f"role {role_id} has an invalid existing response artifact; inspect it before continuing")

    records = _sample_records(role)
    recorded_ids = {row["sample_id"] for row in records if row["status"] == "recorded"}
    if sample_ids is None:
        needed = max(0, role["min_samples"] - len(recorded_ids))
        sample_ids = [row["sample_id"] for row in records if row["sample_id"] not in recorded_ids][:needed]
    if not sample_ids:
        raise WorkbenchBlocked(
            f"role {role['id']} has met its required sample count; pass --role and --samples to stage an optional additional sample"
        )
    if len(sample_ids) != len(set(sample_ids)):
        raise WorkbenchError("sample ids must be unique")
    unknown_samples = sorted(set(sample_ids) - set(role["sample_artifacts"]))
    if unknown_samples:
        raise WorkbenchError(f"unknown sample id(s) for {role['id']}: {', '.join(unknown_samples)}")
    if len(recorded_ids | set(sample_ids)) > role["max_samples"]:
        raise WorkbenchError(f"staging these samples would exceed {role['id']}'s max_samples")
    occupied = [sample for sample in sample_ids if _repo_path(role["sample_artifacts"][sample], "response artifact").exists()]
    if occupied:
        raise WorkbenchError("refusing to overwrite existing sample artifact(s): " + ", ".join(occupied))
    if stage.get("status") == "active":
        return _materialize_role_run(mission, stage, role, sample_ids)
    raise WorkbenchBlocked(f"stage {stage['id']} is not active")


def _print_handoff(run_dir: Path, state: dict[str, Any]) -> str:
    lines = [f"Run: {run_dir}", f"Status: {state.get('run_status', 'unknown')}"]
    for job_id, job_state in state.get("jobs", {}).items():
        if job_state.get("status") != "waiting_for_human":
            continue
        interaction = job_state.get("interaction", {})
        handoff_rel = interaction.get("handoff_json")
        prompt_rel = interaction.get("prompt_to_paste")
        if not isinstance(handoff_rel, str) or not isinstance(prompt_rel, str):
            lines.append(f"  {job_id}: waiting, but handoff metadata is incomplete")
            continue
        handoff_path = engine._safe_run_directory(Path(handoff_rel), run_dir)
        prompt_path = engine._safe_run_directory(Path(prompt_rel), run_dir)
        handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
        prompt_bytes = prompt_path.read_bytes()
        digest = _sha256_bytes(prompt_bytes)
        if digest != handoff.get("prompt_sha256"):
            raise WorkbenchError(f"saved prompt hash mismatch for {job_id}: {prompt_path}")
        lines.extend(
            [
                f"  Role/job: {job_state.get('role')} / {job_id}",
                f"  Exact prompt to paste: {prompt_path}",
                f"  Prompt SHA-256: {digest}",
                f"  Expected run artifact: {run_dir / job_state.get('output_artifact', '')}",
                f"  Canonical response: {handoff.get('canonical_response_artifact') or '(none configured)'}",
                f"  Required metadata: {', '.join(handoff.get('required_metadata', [])) or '(none declared)'}",
                "  No Arena/model call was made by the workbench.",
            ]
        )
    return "\n".join(lines)


def _mirror_response(run_dir: Path, job_id: str, state: dict[str, Any]) -> list[Path]:
    job_state = state.get("jobs", {}).get(job_id)
    if not isinstance(job_state, dict) or job_state.get("status") != "completed":
        return []
    ingestion_rel = job_state.get("human_ingestion")
    response_rel = job_state.get("output_artifact")
    if not isinstance(ingestion_rel, str) or not isinstance(response_rel, str):
        return []
    ingestion_path = engine._safe_run_directory(Path(ingestion_rel), run_dir)
    response_path = engine._safe_run_directory(Path(response_rel), run_dir)
    if not ingestion_path.is_file() or not response_path.is_file():
        raise WorkbenchError(f"completed manual response is missing its saved files for {job_id}")
    ingestion = json.loads(ingestion_path.read_text(encoding="utf-8"))
    if ingestion.get("method") != "manual_arena_ui":
        return []
    mirrored: list[Path] = []
    for state_key, content in (
        ("canonical_response_artifact", response_path.read_bytes()),
        ("canonical_ingestion_artifact", ingestion_path.read_bytes()),
    ):
        relative = job_state.get(state_key)
        if not relative:
            continue
        destination = _repo_path(relative, state_key)
        _write_once_or_verify(destination, content)
        mirrored.append(destination)
    return mirrored


def resume(target: str) -> tuple[Path, dict[str, Any], str]:
    """Display an outstanding exact prompt or safely resume an interrupted workbench DAG."""
    candidate = Path(target).expanduser()
    mission_manifest_exists = bool(
        isinstance(target, str)
        and _MISSION_ID.fullmatch(target)
        and (PROJECT_ROOT / target / "workbench.yaml").is_file()
    )
    if mission_manifest_exists:
        mission_id = target
        load_mission(mission_id, check_files=False)
        run_dirs = _run_directories(mission_id)
        if not run_dirs:
            raise WorkbenchError(f"no persisted run exists for {mission_id}; use `next {mission_id}` to stage its next role")
        run_dir = run_dirs[0]
        state = _load_run_state(run_dir)
    elif candidate.exists():
        run_dir = candidate.resolve()
        try:
            run_dir.relative_to(engine.RUN_ROOT.resolve())
        except ValueError as exc:
            raise WorkbenchError("resume path must be under runtime/runs") from exc
        state = _load_run_state(run_dir)
        mission_id = state.get("mission_id")
    else:
        raise WorkbenchError(f"resume target is neither a configured mission id nor an existing run path: {target}")
    if not isinstance(mission_id, str):
        raise WorkbenchError("run state has no mission_id")
    mission = load_mission(mission_id, check_files=False)
    if state.get("mission_id") != mission_id:
        raise WorkbenchError("run path and run_state mission_id disagree")
    _assert_run_jobs_authorized(mission, state)

    active = [job for job in state["jobs"].values() if job.get("status") == "waiting_for_human"]
    if active and all(job.get("interaction", {}).get("handoff_kind") == "model_response" for job in active):
        message = _print_handoff(run_dir, state)
        return run_dir, state, message
    if state.get("run_status") == "completed":
        mirrored: list[str] = []
        for job_id in state.get("jobs", {}):
            mirrored.extend(str(path) for path in _mirror_response(run_dir, job_id, state))
        message = f"Run is already completed: {run_dir}"
        if mirrored:
            message += "\nRecovered canonical mirror(s):\n  " + "\n  ".join(mirrored)
        return run_dir, state, message

    mission_path_value = state.get("mission_path")
    if not isinstance(mission_path_value, str):
        raise WorkbenchError("run state has no mission_path to resume")
    mission_path = Path(mission_path_value).expanduser().resolve()
    try:
        mission_path.relative_to(WORKBENCH_SPEC_ROOT.resolve())
    except ValueError as exc:
        raise WorkbenchError("run is not a workbench-generated DAG; refusing generic resume") from exc
    run_dir, state = asyncio.run(engine.run_mission(mission_path, resume_dir=run_dir))
    message = _print_handoff(run_dir, state) if state.get("run_status") != "completed" else f"Run resumed: {run_dir}\nStatus: {state['run_status']}"
    if state.get("run_status") == "completed":
        mirrored = []
        for job_id in state.get("jobs", {}):
            mirrored.extend(str(path) for path in _mirror_response(run_dir, job_id, state))
        if mirrored:
            message += "\nRecovered canonical mirror(s):\n  " + "\n  ".join(mirrored)
    return run_dir, state, message


def _read_metadata(metadata_path: str | Path | None, model_label: str | None) -> tuple[dict[str, Any], dict[str, str] | None]:
    metadata: dict[str, Any] = {}
    source_record: dict[str, str] | None = None
    if metadata_path is not None:
        path = Path(metadata_path).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"metadata file not found: {path}")
        data = path.read_bytes()
        try:
            parsed = json.loads(data.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise WorkbenchError(f"metadata file must be UTF-8 JSON: {path}") from exc
        if not isinstance(parsed, dict):
            raise WorkbenchError("metadata file must contain a JSON object")
        metadata = parsed
        source_record = {"path": str(path), "sha256": _sha256_bytes(data)}
    if model_label is not None:
        if not isinstance(model_label, str):
            raise WorkbenchError("model label must be text")
        if "model_label" in metadata and metadata["model_label"] != model_label:
            raise WorkbenchError("--model-label conflicts with metadata.model_label")
        metadata.setdefault("model_label", model_label)
    return metadata, source_record


def ingest(
    run_directory: str | Path,
    job_id: str,
    response_path: str | Path,
    *,
    metadata_path: str | Path | None = None,
    model_label: str | None = None,
) -> dict[str, Any]:
    run_dir = Path(run_directory).expanduser().resolve()
    try:
        run_dir.relative_to(engine.RUN_ROOT.resolve())
    except ValueError as exc:
        raise WorkbenchError("ingestion run directory must be under runtime/runs") from exc
    state = _load_run_state(run_dir)
    mission_id = state.get("mission_id")
    if not isinstance(mission_id, str):
        raise WorkbenchError("run state has no mission_id")
    mission = load_mission(mission_id, check_files=False)
    job_state = state.get("jobs", {}).get(job_id)
    if not isinstance(job_state, dict):
        raise WorkbenchError(f"unknown job {job_id!r} in run")
    if job_state.get("site") != "manual_arena":
        raise WorkbenchError("workbench ingestion accepts only manual_arena jobs")
    _assert_job_authorized(mission, job_state)
    _assert_run_jobs_authorized(mission, state)

    response_source = Path(response_path).expanduser().resolve()
    if not response_source.is_file():
        raise FileNotFoundError(f"response file not found: {response_source}")
    response_bytes = response_source.read_bytes()
    if not response_bytes or len(response_bytes) > 20 * 1024 * 1024:
        raise WorkbenchError("response must be non-empty and no larger than 20 MiB")
    try:
        response_text = response_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise WorkbenchError("response must be UTF-8 text") from exc
    if not response_text.strip():
        raise WorkbenchError("response must contain non-whitespace text")
    metadata, metadata_source = _read_metadata(metadata_path, model_label)
    response_hash = _sha256_bytes(response_bytes)

    if job_state.get("status") == "completed":
        response_rel = job_state.get("output_artifact")
        saved_response = engine._safe_run_directory(Path(response_rel), run_dir) if isinstance(response_rel, str) else None
        if (
            saved_response is None
            or not saved_response.is_file()
            or _sha256_file(saved_response) != response_hash
        ):
            raise WorkbenchError("a different response is already ingested; human response artifacts are immutable")
        mirrored = _mirror_response(run_dir, job_id, state)
        return {
            "already_ingested": True,
            "run_dir": str(run_dir),
            "job_id": job_id,
            "response_sha256": response_hash,
            "canonical_artifacts": [str(path) for path in mirrored],
            "human_ingestion": json.loads(
                (run_dir / job_state["human_ingestion"]).read_text(encoding="utf-8")
            ),
        }

    result = engine.ingest_human_response(
        run_dir,
        job_id,
        response_source,
        run_metadata=metadata,
        run_metadata_source=metadata_source,
        ingestion_method="manual_arena_ui",
    )
    ingested_state = _load_run_state(run_dir)
    mirrored = _mirror_response(run_dir, job_id, ingested_state)
    result["canonical_artifacts"] = [str(path) for path in mirrored]
    result["already_ingested"] = False
    return result


def format_list() -> str:
    rows: list[str] = []
    for status in list_statuses():
        hold = " | HOLD" if status["human_hold"] else ""
        pending = status["pending_role"]
        next_text = (
            f"next {pending['stage_id']}/{pending['role_id']}"
            if pending
            else "no required role"
        )
        blockers = sum(len(stage["blockers"]) for stage in status["stages"])
        blocker_text = f" | {blockers} blocker(s)" if blockers else ""
        rows.append(
            f"{status['mission_id']:<12} {status['lifecycle']:<9}{hold:<7} {next_text}{blocker_text}\n"
            f"  {status['title']}"
        )
    return "\n".join(rows) if rows else "No mission workbench manifests found."


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="discover configured missions and summarize the next action")
    status_parser = commands.add_parser("status", help="show gates, role records, and resumable runs")
    status_parser.add_argument("mission_id")
    validate_parser = commands.add_parser("validate", help="validate one manifest, its paths, and recorded responses")
    validate_parser.add_argument("mission_id")
    next_parser = commands.add_parser("next", help="stage the next authorized manual role on the existing DAG runner")
    next_parser.add_argument("mission_id")
    next_parser.add_argument("--stage")
    next_parser.add_argument("--role")
    next_parser.add_argument("--samples", help="comma-separated sample ids; use two for a paired Arena response")
    resume_parser = commands.add_parser("resume", help="display a saved prompt or resume an interrupted workbench run")
    resume_parser.add_argument("target", help="mission id or runtime/runs/<mission>/<run-id>")
    ingest_parser = commands.add_parser("ingest", help="ingest a verbatim saved Arena response")
    ingest_parser.add_argument("run_directory")
    ingest_parser.add_argument("job_id")
    ingest_parser.add_argument("response_file")
    ingest_parser.add_argument("--metadata-file", help="optional UTF-8 JSON with available Arena run metadata")
    ingest_parser.add_argument("--model-label", help="exact model label as displayed in Arena")
    args = parser.parse_args(argv)

    try:
        if args.command == "list":
            print(format_list())
            return 0
        if args.command == "status":
            print(_format_status(mission_status(args.mission_id)))
            return 0
        if args.command == "validate":
            print(validate_mission(args.mission_id))
            return 0
        if args.command == "next":
            selected = None
            if args.samples:
                selected = [part.strip() for part in args.samples.split(",") if part.strip()]
                if not selected:
                    raise WorkbenchError("--samples must name at least one sample id")
            staged = stage_next(
                args.mission_id,
                stage_id=args.stage,
                role_id=args.role,
                sample_ids=selected,
            )
            print(f"Manual Arena handoff staged; no model call was made.")
            print(f"Mission/stage/role: {args.mission_id} / {staged.stage_id} / {staged.role_id}")
            print(f"Run directory: {staged.run_dir}")
            print(_print_handoff(staged.run_dir, staged.state))
            print("Next: open the exact prompt above in Arena's UI, save the response verbatim, then use `ingest`.")
            return 0
        if args.command == "resume":
            _, _, message = resume(args.target)
            print(message)
            return 0
        if args.command == "ingest":
            result = ingest(
                args.run_directory,
                args.job_id,
                args.response_file,
                metadata_path=args.metadata_file,
                model_label=args.model_label,
            )
            print(f"Ingested response sha256={result['response_sha256']}")
            print(f"Run: {result['run_dir']} | status={result.get('run_status', 'already completed')}")
            for artifact in result.get("canonical_artifacts", []):
                print(f"Canonical artifact: {artifact}")
            missing = result.get("human_ingestion", {}).get("missing_metadata", [])
            if missing:
                print("Missing run metadata (recorded, not inferred): " + ", ".join(missing))
            return 0
    except (WorkbenchError, engine.MissionValidationError, engine.ArtifactReferenceError, FileNotFoundError, OSError, ValueError) as exc:
        print(f"Workbench error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
