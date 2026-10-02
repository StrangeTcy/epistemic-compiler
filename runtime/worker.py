"""Single-machine queue worker built on the existing mission engine."""

from __future__ import annotations

import asyncio
import json
import math
import os
from collections.abc import Awaitable, Callable
from pathlib import Path
from typing import Any

from runtime import engine
from runtime.models import JobExecutor, MissionSpec

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE_ROOT = PROJECT_ROOT / "runtime" / "queue"
SUPPORTED_SITES = frozenset({"arena"})
MISSION_SUFFIXES = frozenset({".yaml", ".yml"})
MAX_RETRY_DELAY_SECONDS = 60.0


class WorkerAlreadyRunning(RuntimeError):
    """A second worker was started against the same queue directory."""


class WorkerStateError(RuntimeError):
    """Existing runtime state could not be read safely."""


class LocalMissionWorker:
    """Poll a local mission inbox and delegate all DAG work to ``engine.run_mission``.

    Only YAML files placed directly in ``queue_dir`` are eligible. Existing run
    state is matched by mission id and content hash; completed jobs are never
    submitted again. Human-paused jobs stay paused until an explicit one-shot
    ``run_mission.py --resume`` operation requeues them.
    """

    def __init__(
        self,
        queue_dir: str | Path = DEFAULT_QUEUE_ROOT,
        *,
        poll_interval: float = 30.0,
        max_parallel: int = 1,
        max_retries: int = 2,
        retry_base_delay: float = 2.0,
        sites: set[str] | frozenset[str] | None = None,
        executor_factory: Callable[[], JobExecutor] | None = None,
        sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
        announce: Callable[[dict[str, Any]], None] | None = engine._event_printer,
    ) -> None:
        if not math.isfinite(poll_interval) or poll_interval <= 0:
            raise ValueError("poll_interval must be a finite number greater than zero")
        if not 1 <= max_parallel <= 16:
            raise ValueError("max_parallel must be between 1 and 16")
        if not 0 <= max_retries <= 10:
            raise ValueError("max_retries must be between 0 and 10")
        if not math.isfinite(retry_base_delay) or retry_base_delay < 0:
            raise ValueError("retry_base_delay must be a finite non-negative number")

        selected_sites = (
            {site.strip().lower() for site in sites}
            if sites
            else set(SUPPORTED_SITES)
        )
        if not selected_sites:
            raise ValueError("at least one site must be selected")
        unsupported = selected_sites - SUPPORTED_SITES
        if unsupported:
            raise ValueError(
                "unsupported worker site(s): " + ", ".join(sorted(unsupported))
            )

        self.queue_dir = Path(queue_dir).expanduser().resolve()
        self.poll_interval = poll_interval
        self.max_parallel = max_parallel
        self.max_retries = max_retries
        self.max_attempts = 1 + max_retries
        self.retry_base_delay = retry_base_delay
        self.sites = frozenset(selected_sites)
        self.executor_factory = executor_factory
        self.sleep = sleep
        self.announce = announce
        self._stop_requested = asyncio.Event()

    def request_stop(self) -> None:
        """Ask the worker to stop after the current queue scan/run drains."""
        self._stop_requested.set()

    def discover_missions(self) -> list[Path]:
        """Return pending YAML mission files in the explicit local inbox."""
        if not self.queue_dir.exists():
            return []
        return sorted(
            path
            for path in self.queue_dir.iterdir()
            if path.is_file() and path.suffix.lower() in MISSION_SUFFIXES
        )

    async def process_available(self) -> int:
        """Process all currently runnable queued missions; return run calls made."""
        processed = 0
        for mission_path in self.discover_missions():
            if self._stop_requested.is_set():
                break
            try:
                spec = engine.load_mission(mission_path)
            except Exception as exc:
                self._log(
                    f"Skipping invalid mission {mission_path}: {type(exc).__name__}: {exc}"
                )
                continue

            mission_sites = {job.site for job in spec.jobs}
            if not mission_sites.issubset(self.sites):
                self._log(
                    f"Skipping {spec.mission_id}: mission sites {sorted(mission_sites)} "
                    f"are outside the selected set {sorted(self.sites)}"
                )
                continue

            try:
                processed += await self._process_mission(spec)
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                self._log(
                    f"Worker could not process {spec.mission_id}: "
                    f"{type(exc).__name__}: {exc}"
                )
        return processed

    async def run(self, *, once: bool = False) -> None:
        """Run one scan or keep polling until ``request_stop``/Ctrl+C."""
        self.queue_dir.mkdir(parents=True, exist_ok=True)
        lock_path = self._acquire_worker_lock()
        try:
            if once:
                processed = await self.process_available()
                if processed == 0:
                    self._log("No runnable queued missions.")
                return

            self._log(
                f"Worker started; watching {self.queue_dir} every {self.poll_interval:g}s."
            )
            while not self._stop_requested.is_set():
                await self.process_available()
                if self._stop_requested.is_set():
                    break
                try:
                    await asyncio.wait_for(
                        self._stop_requested.wait(), timeout=self.poll_interval
                    )
                except asyncio.TimeoutError:
                    pass
        finally:
            self._release_worker_lock(lock_path)
            self._log("Worker stopped; queue lock released.")

    async def _process_mission(self, spec: MissionSpec) -> int:
        found = self._latest_run(spec)
        if found is None:
            self._log(f"Discovered queued mission {spec.mission_id}: {spec.path}")
            run_dir, state = await self._call_engine(spec)
            calls = 1
        else:
            run_dir, state = found
            calls = 0
            self._log(f"Found saved run for {spec.mission_id}: {run_dir}")
            retry_job_ids = self._retryable_jobs(state)
            if self._has_pending_jobs(state) or retry_job_ids:
                if self._stop_requested.is_set():
                    return calls
                await self._wait_before_retry(spec, state, retry_job_ids)
                if self._stop_requested.is_set():
                    return calls
                run_dir, state = await self._call_engine(
                    spec,
                    resume_dir=run_dir,
                    retry_job_ids=set(retry_job_ids),
                    retry_blocked=bool(retry_job_ids),
                )
                calls += 1

        while not self._stop_requested.is_set():
            retry_job_ids = self._retryable_jobs(state)
            if not retry_job_ids:
                return calls
            await self._wait_before_retry(spec, state, retry_job_ids)
            if self._stop_requested.is_set():
                return calls
            run_dir, state = await self._call_engine(
                spec,
                resume_dir=run_dir,
                retry_job_ids=set(retry_job_ids),
                retry_blocked=bool(retry_job_ids),
            )
            calls += 1
        return calls

    async def _wait_before_retry(
        self, spec: MissionSpec, state: dict[str, Any], retry_job_ids: list[str]
    ) -> None:
        if not retry_job_ids:
            return
        delay = self._retry_delay(state, retry_job_ids)
        self._log(
            f"Retrying explicitly retryable job(s) for {spec.mission_id}: "
            f"{', '.join(retry_job_ids)} (attempt limit {self.max_attempts}, "
            f"delay {delay:g}s)"
        )
        if delay:
            await self.sleep(delay)

    @staticmethod
    def _has_pending_jobs(state: dict[str, Any]) -> bool:
        # DAG readiness and dependency blocking belong to the engine. The worker
        # delegates any queued/running state to it once per poll; it does not
        # independently interpret dependency edges.
        return any(
            job.get("status") in {"queued", "running"}
            for job in state.get("jobs", {}).values()
        )

    async def _call_engine(
        self,
        spec: MissionSpec,
        *,
        resume_dir: Path | None = None,
        retry_job_ids: set[str] | None = None,
        retry_blocked: bool = False,
    ) -> tuple[Path, dict[str, Any]]:
        options: dict[str, Any] = {
            "max_parallel": self.max_parallel,
            "announce": self.announce,
        }
        if resume_dir is not None:
            options.update(
                {
                    "resume_dir": resume_dir,
                    "retry_job_ids": retry_job_ids or set(),
                    "retry_blocked": retry_blocked,
                    "resume_waiting_for_human": False,
                }
            )
        if self.executor_factory is not None:
            options["executor"] = self.executor_factory()
        return await engine.run_mission(spec.path, **options)

    def _latest_run(
        self, spec: MissionSpec
    ) -> tuple[Path, dict[str, Any]] | None:
        mission_root = engine.RUN_ROOT / spec.mission_id
        if not mission_root.is_dir():
            return None

        matching: list[tuple[str, str, Path, dict[str, Any]]] = []
        for run_dir in mission_root.iterdir():
            state_path = run_dir / engine.STATE_FILE
            if not run_dir.is_dir() or not state_path.is_file():
                continue
            try:
                state = json.loads(state_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                raise WorkerStateError(
                    f"cannot read existing run state {state_path}; refusing to create a duplicate run"
                ) from exc
            if (
                state.get("mission_id") == spec.mission_id
                and state.get("mission_sha256") == spec.sha256
            ):
                matching.append(
                    (
                        str(state.get("created_at", "")),
                        run_dir.name,
                        run_dir,
                        state,
                    )
                )
        if not matching:
            return None
        _, _, run_dir, state = max(matching, key=lambda row: (row[0], row[1]))
        return run_dir, state

    def _retryable_jobs(self, state: dict[str, Any]) -> list[str]:
        retryable: list[str] = []
        for job_id, job_state in state.get("jobs", {}).items():
            error = job_state.get("error") or {}
            if (
                job_state.get("status") == "failed"
                and error.get("retryable") is True
                and int(job_state.get("attempts", 0)) < self.max_attempts
            ):
                retryable.append(job_id)
        return sorted(retryable)

    def _retry_delay(self, state: dict[str, Any], job_ids: list[str]) -> float:
        attempts = max(
            int(state["jobs"][job_id].get("attempts", 1)) for job_id in job_ids
        )
        exponent = max(0, attempts - 1)
        return min(self.retry_base_delay * (2**exponent), MAX_RETRY_DELAY_SECONDS)

    def _acquire_worker_lock(self) -> Path:
        lock_path = self.queue_dir / ".worker.lock"
        try:
            descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError as exc:
            try:
                existing = lock_path.read_text(encoding="utf-8").strip()
            except OSError:
                existing = "unreadable lock metadata"
            raise WorkerAlreadyRunning(
                f"worker lock exists at {lock_path} ({existing}); verify no worker is active before removing it"
            ) from exc
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                json.dump(
                    {"pid": os.getpid(), "started_at": engine.utc_now()}, stream
                )
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
        except Exception:
            lock_path.unlink(missing_ok=True)
            raise
        return lock_path

    @staticmethod
    def _release_worker_lock(lock_path: Path) -> None:
        lock_path.unlink(missing_ok=True)

    @staticmethod
    def _log(message: str) -> None:
        print(f"[{engine.utc_now()}] worker: {message}", flush=True)
