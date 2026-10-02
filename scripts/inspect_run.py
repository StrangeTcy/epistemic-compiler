#!/usr/bin/env python3
"""Print a concise status and provenance index for one saved run."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_directory")
    args = parser.parse_args()
    run_dir = Path(args.run_directory).expanduser().resolve()
    state_path = run_dir / "run_state.json"
    if not state_path.is_file():
        print(f"No run_state.json found under {run_dir}", file=sys.stderr)
        return 2
    state = json.loads(state_path.read_text(encoding="utf-8"))
    print(f"Mission: {state.get('mission_id')} ({state.get('mission_type')})")
    print(f"Run: {state.get('run_id')}")
    print(f"Status: {state.get('run_status', 'in progress')}")
    print(f"Created: {state.get('created_at')}")
    lock_path = run_dir / ".runner.lock"
    if lock_path.exists():
        try:
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
            print(
                f"Runner lock present: pid={lock.get('pid')} started_at={lock.get('started_at')} (verify before removing)"
            )
        except (OSError, json.JSONDecodeError):
            print("Runner lock present but unreadable (verify before removing)")
    print("Jobs:")
    for job_id, job in state.get("jobs", {}).items():
        deps = ", ".join(job.get("dependencies", [])) or "—"
        print(f"  {job_id:<24} {job.get('status', 'unknown'):<20} deps=[{deps}]")
        if job.get("model_observed") or job.get("model_requested"):
            print(
                f"    model requested={job.get('model_requested')!r}; observed={job.get('model_observed')!r}"
            )
        if job.get("current_url"):
            print(f"    URL: {job['current_url']}")
        if job.get("prompt_sha256"):
            print(f"    prompt sha256: {job['prompt_sha256']}")
        for input_record in job.get("input_records", []):
            print(
                f"    input {input_record.get('reference')}: sha256={input_record.get('sha256')} ({input_record.get('size_bytes')} bytes)"
            )
        if job.get("output_artifact"):
            print(f"    response: {job['output_artifact']}")
        if job.get("response_sha256"):
            print(f"    response sha256: {job['response_sha256']}")
        if job.get("screenshot"):
            print(f"    screenshot: {job['screenshot']}")
        if job.get("status_reason"):
            print(f"    note: {job['status_reason']}")
        if job.get("error"):
            print(
                f"    error: {job['error'].get('type')}: {job['error'].get('message')}"
            )
        provenance = run_dir / "artifacts" / "jobs" / job_id / "provenance.json"
        if provenance.exists():
            print(f"    provenance: {provenance.relative_to(run_dir)}")
    events = run_dir / "events.jsonl"
    if events.exists():
        print(f"Transition log: {events}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
