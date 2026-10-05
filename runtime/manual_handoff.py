"""Generic human-operated Arena handoffs for the existing DAG runtime.

This adapter only saves an exact prompt and waits. It does not open a browser,
call a model, use an API key, or infer that an experiment is authorized.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from runtime.models import ExecutionResult, JobContext, WaitingForHuman


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _write_once(path: Path, data: bytes) -> None:
    """Create an immutable handoff file; identical retries are harmless."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    except FileExistsError:
        if path.read_bytes() == data:
            return
        raise RuntimeError(f"immutable manual handoff changed: {path}")
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except Exception:
        path.unlink(missing_ok=True)
        raise


def execute_arena_manual_handoff(context: JobContext) -> ExecutionResult:
    """Write a paste-ready handoff and pause until a human ingests the response."""
    prompt_bytes = context.prompt_snapshot.read_bytes()
    prompt_hash = _sha256(prompt_bytes)
    prompt_relative = str(context.prompt_snapshot.relative_to(context.run_dir))
    expected_response = str(context.job_state["output_artifact"])
    handoff_path = context.run_dir / "handoffs" / f"{context.job.job_id}.json"
    handoff_relative = str(handoff_path.relative_to(context.run_dir))
    required_metadata = list(context.job.metadata_required)
    handoff: dict[str, Any] = {
        "schema_version": 1,
        "interface": "manual_arena_ui",
        "model_call_made": False,
        "created_at": context.job_state.get("created_at") or _utc_now(),
        "mission_id": context.mission.mission_id,
        "run_id": context.run_dir.name,
        "job_id": context.job.job_id,
        "role": context.job.role,
        "prompt_artifact": context.job.prompt_artifact,
        "prompt_to_paste": prompt_relative,
        "prompt_sha256": prompt_hash,
        "prompt_bytes": len(prompt_bytes),
        "expected_response_artifact": expected_response,
        "canonical_response_artifact": context.job.canonical_response_artifact,
        "canonical_ingestion_artifact": context.job.canonical_ingestion_artifact,
        "required_metadata": required_metadata,
        "input_artifacts": [
            {
                "reference": record.get("reference"),
                "source_path": record.get("source_path"),
                "snapshot_path": record.get("snapshot_path"),
                "sha256": record.get("sha256"),
                "size_bytes": record.get("size_bytes"),
                "attachment_index": record.get("attachment_index"),
            }
            for record in context.input_records
        ],
        "instructions": [
            "Open the configured prompt file and paste its full contents exactly; do not add or remove text.",
            "Use Arena's authenticated UI manually. This run has made no Arena/model call.",
            "Save the visible response without editing it, then ingest it with the workbench CLI.",
            "Record only metadata actually visible or known; missing required metadata will be recorded as missing.",
        ],
    }
    serialized = (json.dumps(handoff, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    _write_once(handoff_path, serialized)
    context.update_progress(
        {
            "stage": "manual_arena_handoff",
            "handoff_kind": "model_response",
            "handoff_json": handoff_relative,
            "prompt_to_paste": prompt_relative,
            "expected_response_artifact": expected_response,
        }
    )
    raise WaitingForHuman(
        f"Manual Arena handoff ready for {context.job.job_id}; no model call was made.",
        details={
            "stage": "manual_arena_handoff",
            "handoff_kind": "model_response",
            "handoff_json": handoff_relative,
            "prompt_to_paste": prompt_relative,
            "expected_response_artifact": expected_response,
            "prompt_sha256": prompt_hash,
        },
    )
