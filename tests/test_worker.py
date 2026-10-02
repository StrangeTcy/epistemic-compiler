from __future__ import annotations

import asyncio
import json
from pathlib import Path

import yaml

from runtime import engine
from runtime.models import ExecutionResult, RetryableJobError, WaitingForHuman
from runtime.worker import LocalMissionWorker


class FakeExecutor:
    def __init__(self, factory):
        self.factory = factory
        self.closed = False

    async def execute(self, context):
        job_id = context.job.job_id
        self.factory.calls.append(job_id)
        attempt = self.factory.attempts.get(job_id, 0) + 1
        self.factory.attempts[job_id] = attempt

        if job_id in self.factory.fail_jobs:
            raise RuntimeError("non-retryable failure")
        if job_id in self.factory.wait_jobs:
            raise WaitingForHuman(
                "manual recovery required", details={"stage": "fake_gate"}
            )
        if job_id in self.factory.always_retry or attempt <= self.factory.retry_first.get(
            job_id, 0
        ):
            raise RetryableJobError("temporary navigation timeout")

        return ExecutionResult(
            response_text=f"response for {job_id}\n",
            model_name="Max",
            current_url="https://arena.ai/text/direct?model_a=max",
        )

    async def close(self):
        self.closed = True
        self.factory.closed_count += 1


class FakeExecutorFactory:
    def __init__(
        self, *, wait_jobs=(), retry_first=None, always_retry=(), fail_jobs=()
    ):
        self.wait_jobs = set(wait_jobs)
        self.retry_first = dict(retry_first or {})
        self.always_retry = set(always_retry)
        self.fail_jobs = set(fail_jobs)
        self.calls = []
        self.attempts = {}
        self.closed_count = 0

    def __call__(self):
        return FakeExecutor(self)


def queue_mission(queue_dir: Path, mission_id: str, jobs: list[dict]) -> Path:
    queue_dir.mkdir(parents=True, exist_ok=True)
    for job in jobs:
        prompt_name = f"{job['id']}.md"
        (queue_dir / prompt_name).write_text(
            f"Prompt for {job['id']}\n", encoding="utf-8"
        )
        job["role"] = job.get("role", job["id"])
        job["prompt_artifact"] = prompt_name
        job["site"] = job.get("site", "arena")
    mission_path = queue_dir / f"{mission_id}.yaml"
    mission_path.write_text(
        yaml.safe_dump({"mission_id": mission_id, "jobs": jobs}, sort_keys=False),
        encoding="utf-8",
    )
    return mission_path


def read_run_state(run_root: Path, mission_id: str) -> tuple[Path, dict]:
    candidates = sorted((run_root / mission_id).glob("*/run_state.json"))
    assert candidates
    state_path = candidates[-1]
    return state_path.parent, json.loads(state_path.read_text(encoding="utf-8"))


def worker_for(
    queue_dir, factory, *, max_retries=2, retry_base_delay=0, sleep=None
):
    options = {
        "queue_dir": queue_dir,
        "max_parallel": 1,
        "max_retries": max_retries,
        "retry_base_delay": retry_base_delay,
        "executor_factory": factory,
        "announce": None,
    }
    if sleep is not None:
        options["sleep"] = sleep
    return LocalMissionWorker(**options)


def test_worker_discovers_queued_mission_and_advances_dependencies(tmp_path, monkeypatch):
    queue_dir = tmp_path / "queue"
    run_root = tmp_path / "runs"
    monkeypatch.setattr(engine, "RUN_ROOT", run_root)
    queue_mission(
        queue_dir,
        "worker-dag",
        [
            {"id": "first"},
            {"id": "second", "dependencies": ["first"]},
        ],
    )
    factory = FakeExecutorFactory()
    worker = worker_for(queue_dir, factory, max_retries=0)

    asyncio.run(worker.run(once=True))

    run_dir, state = read_run_state(run_root, "worker-dag")
    assert factory.calls == ["first", "second"]
    assert state["run_status"] == "completed"
    assert all(job["status"] == "completed" for job in state["jobs"].values())
    events = [
        json.loads(line)
        for line in (run_dir / "events.jsonl").read_text().splitlines()
    ]
    second_started = next(
        index
        for index, event in enumerate(events)
        if event["job_id"] == "second" and event["to"] == "running"
    )
    first_completed = next(
        index
        for index, event in enumerate(events)
        if event["job_id"] == "first" and event["to"] == "completed"
    )
    assert first_completed < second_started
    assert factory.closed_count == 1
    assert not (queue_dir / ".worker.lock").exists()
    assert not (run_dir / ".runner.lock").exists()


def test_worker_leaves_human_wait_paused_and_runs_independent_job(
    tmp_path, monkeypatch
):
    queue_dir = tmp_path / "queue"
    run_root = tmp_path / "runs"
    monkeypatch.setattr(engine, "RUN_ROOT", run_root)
    queue_mission(
        queue_dir,
        "human-gate",
        [{"id": "paused"}, {"id": "independent"}],
    )
    factory = FakeExecutorFactory(wait_jobs={"paused"})
    worker = worker_for(queue_dir, factory)

    asyncio.run(worker.run(once=True))
    run_dir, state = read_run_state(run_root, "human-gate")
    events_before = (run_dir / "events.jsonl").read_text(encoding="utf-8")

    assert factory.calls == ["paused", "independent"]
    assert state["jobs"]["paused"]["status"] == "waiting_for_human"
    assert state["jobs"]["independent"]["status"] == "completed"

    second_factory = FakeExecutorFactory()
    asyncio.run(worker_for(queue_dir, second_factory).run(once=True))
    _, state_after = read_run_state(run_root, "human-gate")
    assert second_factory.calls == []
    assert state_after["jobs"]["paused"]["status"] == "waiting_for_human"
    assert (run_dir / "events.jsonl").read_text(encoding="utf-8") == events_before


def test_worker_resume_of_other_work_preserves_existing_human_wait(
    tmp_path, monkeypatch
):
    queue_dir = tmp_path / "queue"
    run_root = tmp_path / "runs"
    monkeypatch.setattr(engine, "RUN_ROOT", run_root)
    queue_mission(
        queue_dir,
        "paused-with-queued-work",
        [{"id": "manual"}, {"id": "other"}],
    )
    first_factory = FakeExecutorFactory(wait_jobs={"manual", "other"})
    asyncio.run(worker_for(queue_dir, first_factory).run(once=True))
    run_dir, state = read_run_state(run_root, "paused-with-queued-work")

    # A queued independent job can remain after a crash/partial handoff. Resuming
    # it must not auto-reset the separately human-paused job.
    state["jobs"]["other"]["status"] = "queued"
    state["run_status"] = "waiting_for_human"
    (run_dir / "run_state.json").write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    second_factory = FakeExecutorFactory()
    asyncio.run(worker_for(queue_dir, second_factory).run(once=True))
    _, resumed = read_run_state(run_root, "paused-with-queued-work")

    assert second_factory.calls == ["other"]
    assert resumed["jobs"]["manual"]["status"] == "waiting_for_human"
    assert resumed["jobs"]["manual"]["attempts"] == 1
    assert resumed["jobs"]["other"]["status"] == "completed"
    assert resumed["jobs"]["other"]["attempts"] == 2


def test_worker_retries_only_marked_transient_failure_with_bounded_backoff(
    tmp_path, monkeypatch
):
    queue_dir = tmp_path / "queue"
    run_root = tmp_path / "runs"
    monkeypatch.setattr(engine, "RUN_ROOT", run_root)
    queue_mission(
        queue_dir,
        "retry-once",
        [{"id": "fetch"}, {"id": "downstream", "dependencies": ["fetch"]}],
    )
    factory = FakeExecutorFactory(retry_first={"fetch": 1})
    delays = []

    async def no_wait(delay):
        delays.append(delay)

    worker = worker_for(
        queue_dir, factory, max_retries=2, retry_base_delay=1, sleep=no_wait
    )
    asyncio.run(worker.run(once=True))

    _, state = read_run_state(run_root, "retry-once")
    assert factory.calls == ["fetch", "fetch", "downstream"]
    assert state["jobs"]["fetch"]["attempts"] == 2
    assert state["jobs"]["fetch"]["status"] == "completed"
    assert state["jobs"]["downstream"]["status"] == "completed"
    assert state["jobs"]["downstream"]["attempts"] == 1
    assert delays == [1]


def test_worker_stops_retrying_at_attempt_limit_and_does_not_retry_permanent_failures(
    tmp_path, monkeypatch
):
    queue_dir = tmp_path / "queue"
    run_root = tmp_path / "runs"
    monkeypatch.setattr(engine, "RUN_ROOT", run_root)
    queue_mission(
        queue_dir,
        "retry-limit",
        [{"id": "fetch"}, {"id": "permanent"}],
    )
    factory = FakeExecutorFactory(
        always_retry={"fetch"}, fail_jobs={"permanent"}
    )
    worker = worker_for(queue_dir, factory, max_retries=1)

    asyncio.run(worker.run(once=True))
    _, state = read_run_state(run_root, "retry-limit")
    assert factory.calls == ["fetch", "permanent", "fetch"]
    assert state["jobs"]["fetch"]["attempts"] == 2
    assert state["jobs"]["fetch"]["status"] == "failed"
    assert state["jobs"]["fetch"]["error"]["retryable"] is True
    assert state["jobs"]["permanent"]["attempts"] == 1
    assert state["jobs"]["permanent"]["status"] == "failed"
    assert "retryable" not in state["jobs"]["permanent"]["error"]

    second_factory = FakeExecutorFactory()
    asyncio.run(worker_for(queue_dir, second_factory, max_retries=1).run(once=True))
    _, state_after = read_run_state(run_root, "retry-limit")
    assert second_factory.calls == []
    assert state_after["jobs"]["fetch"]["attempts"] == 2


def test_worker_clean_shutdown_releases_lock(tmp_path):
    queue_dir = tmp_path / "queue"
    worker = LocalMissionWorker(queue_dir, poll_interval=3600, announce=None)

    async def start_and_stop():
        running = asyncio.create_task(worker.run())
        await asyncio.sleep(0)
        worker.request_stop()
        await asyncio.wait_for(running, timeout=1)

    asyncio.run(start_and_stop())

    assert not (queue_dir / ".worker.lock").exists()


def test_worker_restart_skips_completed_jobs_and_resumes_only_interrupted_work(
    tmp_path, monkeypatch
):
    queue_dir = tmp_path / "queue"
    run_root = tmp_path / "runs"
    monkeypatch.setattr(engine, "RUN_ROOT", run_root)
    queue_mission(
        queue_dir,
        "restart-safe",
        [{"id": "done"}, {"id": "interrupted", "dependencies": ["done"]}],
    )
    initial_factory = FakeExecutorFactory()
    asyncio.run(worker_for(queue_dir, initial_factory).run(once=True))
    run_dir, state = read_run_state(run_root, "restart-safe")
    assert initial_factory.calls == ["done", "interrupted"]

    # Simulate a process stop after the second job was marked running. The first
    # completed job remains immutable; the engine's resume path handles the active
    # job and the adapter is responsible for checking persisted interaction state.
    state["jobs"]["interrupted"]["status"] = "running"
    state["jobs"]["interrupted"].pop("ended_at", None)
    state["run_status"] = "in_progress"
    (run_dir / "run_state.json").write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    resumed_factory = FakeExecutorFactory()
    asyncio.run(worker_for(queue_dir, resumed_factory).run(once=True))
    _, resumed = read_run_state(run_root, "restart-safe")

    assert resumed_factory.calls == ["interrupted"]
    assert resumed["jobs"]["done"]["status"] == "completed"
    assert resumed["jobs"]["done"]["attempts"] == 1
    assert resumed["jobs"]["interrupted"]["status"] == "completed"
    assert resumed["jobs"]["interrupted"]["attempts"] == 2


def test_worker_restart_does_not_duplicate_completed_run(tmp_path, monkeypatch):
    queue_dir = tmp_path / "queue"
    run_root = tmp_path / "runs"
    monkeypatch.setattr(engine, "RUN_ROOT", run_root)
    queue_mission(queue_dir, "already-done", [{"id": "only"}])
    first_factory = FakeExecutorFactory()
    asyncio.run(worker_for(queue_dir, first_factory).run(once=True))
    second_factory = FakeExecutorFactory()

    asyncio.run(worker_for(queue_dir, second_factory).run(once=True))

    assert first_factory.calls == ["only"]
    assert second_factory.calls == []
