from __future__ import annotations

import asyncio
import hashlib
import json
from pathlib import Path

import pytest
import yaml

from runtime import engine
from runtime.models import ExecutionResult, WaitingForHuman


class FakeExecutor:
    """Deterministic site boundary; tests never open a network/browser session."""

    def __init__(self, responses=None, *, wait_once=()):
        self.responses = dict(responses or {})
        self.wait_once = set(wait_once)
        self.calls = []
        self.contexts = {}
        self.closed = False

    async def execute(self, context):
        job_id = context.job.job_id
        self.calls.append(job_id)
        self.contexts.setdefault(job_id, []).append(
            {
                "prompt_text": context.prompt_text,
                "inputs": [path.read_bytes() for path in context.input_paths],
                "prompt_sha256": context.prompt_sha256,
                "input_records": context.input_records,
            }
        )
        if job_id in self.wait_once:
            self.wait_once.remove(job_id)
            context.update_progress(
                {
                    "stage": "fake_manual_gate",
                    "current_url": "https://arena.ai/text/direct?model_a=max",
                }
            )
            raise WaitingForHuman(
                "fake manual gate", details={"stage": "fake_manual_gate"}
            )
        text = self.responses.get(job_id, f"response for {job_id}\n")
        return ExecutionResult(
            response_text=text,
            model_name="Max",
            conversation_id=f"fake-{job_id}",
            current_url="https://arena.ai/text/direct?model_a=max",
            metadata={"fake": True},
        )

    async def close(self):
        self.closed = True


def write_mission(directory: Path, *, jobs, inputs=None) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    payload = {
        "mission_id": "test-runtime",
        "type": "test",
        "inputs": inputs or {},
        "jobs": jobs,
    }
    path = directory / "mission.yaml"
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    return path


def job(job_id, prompt="prompt.md", *, deps=(), inputs=(), output=None):
    return {
        "job_id": job_id,
        "role": job_id,
        "prompt_artifact": prompt,
        "input_artifacts": list(inputs),
        "dependencies": list(deps),
        "output_artifact": output or f"artifacts/jobs/{job_id}/response.md",
    }


def test_dag_execution_snapshots_and_verbatim_response(tmp_path, monkeypatch):
    mission_dir = tmp_path / "mission"
    mission_dir.mkdir()
    (mission_dir / "prompt.md").write_text(
        "  retain prompt bytes  \n", encoding="utf-8"
    )
    (mission_dir / "evidence.txt").write_bytes(b"evidence bytes\n")
    mission = write_mission(
        mission_dir,
        inputs={"evidence": "evidence.txt"},
        jobs=[
            job("ingest", inputs=["mission:evidence"]),
            job("theorist", deps=["ingest"], inputs=["job:ingest:response"]),
            job("skeptic", deps=["ingest"], inputs=["job:ingest:response"]),
        ],
    )
    monkeypatch.setattr(engine, "RUN_ROOT", tmp_path / "runs")
    verbatim = "```md\nExact visible response.\n```\n"
    executor = FakeExecutor(responses={"ingest": "inventory\n", "theorist": verbatim})

    run_dir, state = asyncio.run(
        engine.run_mission(mission, executor=executor, max_parallel=3, announce=None)
    )

    assert state["run_status"] == "completed"
    assert all(row["status"] == "completed" for row in state["jobs"].values())
    assert executor.calls[0] == "ingest"
    assert set(executor.calls) == {"ingest", "theorist", "skeptic"}
    assert executor.closed
    assert (run_dir / "artifacts/jobs/theorist/response.md").read_text(
        encoding="utf-8"
    ) == verbatim
    assert executor.contexts["ingest"][0]["prompt_text"] == "  retain prompt bytes  \n"
    assert executor.contexts["ingest"][0]["inputs"] == [b"evidence bytes\n"]
    assert executor.contexts["theorist"][0]["inputs"] == [b"inventory\n"]

    provenance = json.loads(
        (run_dir / "artifacts/jobs/theorist/provenance.json").read_text()
    )
    assert (
        provenance["response_sha256"] == hashlib.sha256(verbatim.encode()).hexdigest()
    )
    assert provenance["input_artifacts"][0]["reference"] == "job:ingest:response"
    assert provenance["model_observed"] == "Max"
    events = [
        json.loads(line) for line in (run_dir / "events.jsonl").read_text().splitlines()
    ]
    assert any(event["to"] == "completed" for event in events)


def test_resume_uses_first_prompt_and_input_snapshots_and_keeps_completed_job(
    tmp_path, monkeypatch
):
    mission_dir = tmp_path / "mission"
    mission_dir.mkdir()
    prompt = mission_dir / "prompt.md"
    source = mission_dir / "source.txt"
    prompt.write_text("first prompt\n", encoding="utf-8")
    source.write_text("first source\n", encoding="utf-8")
    mission = write_mission(
        mission_dir,
        inputs={"source": "source.txt"},
        jobs=[job("only", inputs=["mission:source"])],
    )
    monkeypatch.setattr(engine, "RUN_ROOT", tmp_path / "runs")
    first = FakeExecutor(wait_once={"only"})
    run_dir, state = asyncio.run(
        engine.run_mission(mission, executor=first, announce=None)
    )
    assert state["jobs"]["only"]["status"] == "waiting_for_human"
    assert state["run_status"] == "waiting_for_human"
    assert first.calls == ["only"]

    prompt.write_text("changed prompt\n", encoding="utf-8")
    source.write_text("changed source\n", encoding="utf-8")
    second = FakeExecutor(responses={"only": "done\n"})
    resumed_dir, resumed = asyncio.run(
        engine.run_mission(mission, resume_dir=run_dir, executor=second, announce=None)
    )

    assert resumed_dir == run_dir
    assert resumed["jobs"]["only"]["status"] == "completed"
    assert resumed["jobs"]["only"]["attempts"] == 2
    assert second.contexts["only"][0]["prompt_text"] == "first prompt\n"
    assert second.contexts["only"][0]["inputs"] == [b"first source\n"]
    assert (
        resumed["jobs"]["only"]["prompt_source_sha256"]
        == hashlib.sha256(b"changed prompt\n").hexdigest()
    )
    provenance = json.loads(
        (run_dir / "artifacts/jobs/only/provenance.json").read_text()
    )
    assert provenance["prompt_source_changed_since_snapshot"] is True
    assert provenance["prompt_sha256"] == hashlib.sha256(b"first prompt\n").hexdigest()
    assert (
        provenance["input_artifacts"][0]["sha256"]
        == hashlib.sha256(b"first source\n").hexdigest()
    )


def test_failed_dependency_blocks_descendants_but_not_independent_job(
    tmp_path, monkeypatch
):
    mission_dir = tmp_path / "mission"
    mission_dir.mkdir()
    (mission_dir / "prompt.md").write_text("prompt", encoding="utf-8")
    mission = write_mission(
        mission_dir,
        jobs=[
            job("bad"),
            job("child", deps=["bad"], inputs=["job:bad:response"]),
            job("independent"),
        ],
    )

    class FailingExecutor(FakeExecutor):
        async def execute(self, context):
            self.calls.append(context.job.job_id)
            if context.job.job_id == "bad":
                raise RuntimeError("deterministic fake failure")
            return await super().execute(context)

    monkeypatch.setattr(engine, "RUN_ROOT", tmp_path / "runs")
    executor = FailingExecutor()
    _, state = asyncio.run(
        engine.run_mission(mission, executor=executor, announce=None)
    )
    assert state["jobs"]["bad"]["status"] == "failed"
    assert state["jobs"]["child"]["status"] == "blocked"
    assert state["jobs"]["independent"]["status"] == "completed"
    assert "child" not in executor.calls


def test_loader_rejects_cycles_unsafe_and_duplicate_outputs(tmp_path):
    mission_dir = tmp_path / "mission"
    mission_dir.mkdir()
    (mission_dir / "prompt.md").write_text("prompt", encoding="utf-8")
    cyclic = write_mission(
        mission_dir,
        jobs=[job("a", deps=["b"]), job("b", deps=["a"])],
    )
    with pytest.raises(engine.MissionValidationError, match="cycle"):
        engine.load_mission(cyclic)

    unsafe = write_mission(mission_dir, jobs=[job("unsafe", output="../escape.md")])
    with pytest.raises(engine.ArtifactReferenceError):
        engine.load_mission(unsafe)

    duplicate = write_mission(
        mission_dir,
        jobs=[job("a", output="same.md"), job("b", output="same.md")],
    )
    with pytest.raises(engine.MissionValidationError, match="share output_artifact"):
        engine.load_mission(duplicate)


def test_campaign_example_is_an_inert_five_job_dag():
    root = Path(__file__).resolve().parents[1]
    spec = engine.load_mission(root / "examples/campaign-analysis.yaml")
    mapping = spec.job_map
    assert set(mapping) == {
        "evidence_ingest",
        "theorist",
        "experimentalist",
        "skeptic",
        "prior_work_killer",
    }
    council = {"theorist", "experimentalist", "skeptic", "prior_work_killer"}
    assert all(
        mapping[job_id].dependencies == ("evidence_ingest",) for job_id in council
    )
    assert all(
        mapping[job_id].input_artifacts == ("job:evidence_ingest:response",)
        for job_id in council
    )
    assert not (root / "atria-campaign-state-56.zip").exists()


def test_run_lock_rejects_a_second_resume(tmp_path, monkeypatch):
    mission_dir = tmp_path / "mission"
    mission_dir.mkdir()
    (mission_dir / "prompt.md").write_text("prompt", encoding="utf-8")
    mission = write_mission(mission_dir, jobs=[job("only")])
    runs = tmp_path / "runs"
    monkeypatch.setattr(engine, "RUN_ROOT", runs)
    run_dir, _ = asyncio.run(
        engine.run_mission(mission, executor=FakeExecutor(), announce=None)
    )
    lock = engine._acquire_run_lock(run_dir)
    try:
        with pytest.raises(engine.MissionValidationError, match="already locked"):
            asyncio.run(
                engine.run_mission(
                    mission, resume_dir=run_dir, executor=FakeExecutor(), announce=None
                )
            )
    finally:
        engine._release_run_lock(lock)


def test_cancellation_records_waiting_state_and_releases_lock(tmp_path, monkeypatch):
    mission_dir = tmp_path / "mission"
    mission_dir.mkdir()
    (mission_dir / "prompt.md").write_text("prompt", encoding="utf-8")
    mission = write_mission(mission_dir, jobs=[job("only")])
    runs = tmp_path / "runs"
    monkeypatch.setattr(engine, "RUN_ROOT", runs)

    class BlockingExecutor:
        def __init__(self, started):
            self.started = started
            self.closed = False

        async def execute(self, context):
            context.update_progress(
                {"stage": "before_cancel", "submission_state": "submitting"}
            )
            self.started.set()
            await asyncio.Event().wait()

        async def close(self):
            self.closed = True

    async def cancel_run():
        started = asyncio.Event()
        executor = BlockingExecutor(started)
        running = asyncio.create_task(
            engine.run_mission(mission, executor=executor, announce=None)
        )
        await started.wait()
        running.cancel()
        with pytest.raises(asyncio.CancelledError):
            await running
        return executor

    executor = asyncio.run(cancel_run())
    assert executor.closed
    run_state_path = next(runs.rglob("run_state.json"))
    state = json.loads(run_state_path.read_text(encoding="utf-8"))
    assert state["run_status"] == "waiting_for_human"
    assert state["jobs"]["only"]["status"] == "waiting_for_human"
    assert not (run_state_path.parent / ".runner.lock").exists()
