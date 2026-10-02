#!/usr/bin/env python3
"""Poll a local mission queue and execute eligible work until stopped."""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.worker import (  # noqa: E402
    DEFAULT_QUEUE_ROOT,
    SUPPORTED_SITES,
    LocalMissionWorker,
    WorkerAlreadyRunning,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--queue-dir",
        type=Path,
        default=DEFAULT_QUEUE_ROOT,
        help=f"directory containing queued .yaml/.yml missions (default: {DEFAULT_QUEUE_ROOT})",
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="process the work currently runnable in the queue, then exit",
    )
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=30.0,
        help="seconds to sleep between queue scans (default: 30)",
    )
    parser.add_argument(
        "--max-parallel",
        type=int,
        default=1,
        help="maximum concurrent browser jobs per mission (1–16; default: 1)",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=2,
        help="additional attempts for explicitly retryable transient failures (0–10; default: 2)",
    )
    parser.add_argument(
        "--retry-base-delay",
        type=float,
        default=2.0,
        help="base seconds for exponential retry backoff (default: 2)",
    )
    parser.add_argument(
        "--site",
        "--provider",
        dest="sites",
        action="append",
        choices=sorted(SUPPORTED_SITES),
        help="process only missions whose jobs use this site/provider; repeatable",
    )
    args = parser.parse_args()

    try:
        worker = LocalMissionWorker(
            args.queue_dir,
            poll_interval=args.poll_interval,
            max_parallel=args.max_parallel,
            max_retries=args.max_retries,
            retry_base_delay=args.retry_base_delay,
            sites=set(args.sites) if args.sites else None,
        )
        asyncio.run(worker.run(once=args.once))
    except WorkerAlreadyRunning as exc:
        print(f"Worker startup error: {exc}", file=sys.stderr)
        return 2
    except ValueError as exc:
        parser.error(str(exc))
    except KeyboardInterrupt:
        print(
            "Worker interrupted; active jobs were persisted as waiting_for_human for safe inspection/resume.",
            file=sys.stderr,
        )
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
