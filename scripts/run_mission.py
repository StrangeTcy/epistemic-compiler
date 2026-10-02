#!/usr/bin/env python3
"""Run or resume a local browser-backed mission DAG."""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.engine import MissionValidationError, run_mission  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mission", help="path to a mission YAML file")
    parser.add_argument(
        "--resume", metavar="RUN_DIRECTORY", help="resume an existing run directory"
    )
    parser.add_argument(
        "--retry-failed",
        action="store_true",
        help="explicitly requeue failed/blocked jobs when resuming",
    )
    parser.add_argument(
        "--max-parallel",
        type=int,
        default=1,
        help="maximum concurrently runnable jobs (1–16; browser jobs use separate tabs)",
    )
    args = parser.parse_args()
    try:
        run_dir, state = asyncio.run(
            run_mission(
                args.mission,
                resume_dir=args.resume,
                retry_failed=args.retry_failed,
                max_parallel=args.max_parallel,
            )
        )
    except (MissionValidationError, FileNotFoundError, ValueError) as exc:
        print(f"Mission runner error: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print(
            "Interrupted. Any job still marked running will be converted to waiting_for_human on resume.",
            file=sys.stderr,
        )
        return 130

    print(f"\nRun directory: {run_dir}")
    print(f"Mission status: {state.get('run_status', 'unknown')}")
    for job_id, job_state in state["jobs"].items():
        print(f"  {job_id}: {job_state['status']}")
    print(f"Inspect with: python scripts/inspect_run.py {run_dir}")
    return 0 if state.get("run_status") == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
