from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
import yaml

from runtime import engine, workbench


REQUIRED_METADATA = ["arena_mode", "model_label", "session_time", "tools"]


def make_manifest(
    root: Path,
    *,
    mission_id: str = "mission-99",
    prompt: dict | None = None,
    role: dict | None = None,
    lifecycle: str = "active",
    human_hold: bool = False,
    stage_status: str = "active",
    authorized: bool = True,
    blockers: list[str] | None = None,
) -> Path:
    mission_dir = root / mission_id
    (mission_dir / "prompts").mkdir(parents=True, exist_ok=True)
    if prompt is None:
        prompt = {"source": f"{mission_id}/prompts/role.md"}
        (mission_dir / "prompts/role.md").write_bytes(b"Exact role prompt.\n")
    if role is None:
        role = {
            "id": "skeptic",
            "label": "Skeptic",
            "prompt": prompt,
            "inputs": {},
            "sample_artifacts": {"single": f"{mission_id}/responses/skeptic.md"},
            "min_samples": 1,
            "max_samples": 1,
            "metadata_required": REQUIRED_METADATA,
        }
    payload = {
        "schema_version": 1,
        "mission_id": mission_id,
        "title": "Temporary configured mission",
        "lifecycle": lifecycle,
        "human_hold": human_hold,
        "gate_status": {"gate_1": "pending"},
        "stages": [
            {
                "id": "council_round_1",
                "label": "Council round 1",
                "status": stage_status,
                "authorized": authorized,
                "blockers": blockers or [],
                "roles": [role],
            }
        ],
    }
    path = mission_dir / "workbench.yaml"
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    return path


def configure_sandbox(tmp_path: Path, monkeypatch, *, mission_id: str = "mission-99") -> Path:
    monkeypatch.setattr(workbench, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(workbench, "WORKBENCH_SPEC_ROOT", tmp_path / "runtime/workbench_specs")
    monkeypatch.setattr(engine, "RUN_ROOT", tmp_path / "runtime/runs")
    return make_manifest(tmp_path, mission_id=mission_id)


def read_state(run_dir: Path) -> dict:
    return json.loads((run_dir / engine.STATE_FILE).read_text(encoding="utf-8"))


def test_repository_discovery_uses_actual_mission_state_and_preserves_holds():
    root = Path(__file__).resolve().parents[1]
    missions = {mission.mission_id for mission in workbench.discover_missions()}
    assert missions == {"mission-01", "mission-02", "mission-03", "mission-04"}

    m01 = workbench.mission_status("mission-01")
    m02 = workbench.mission_status("mission-02")
    m03 = workbench.mission_status("mission-03")
    m04 = workbench.mission_status("mission-04")

    assert m01["lifecycle"] == "closed"
    assert m02["pending_role"] == {"stage_id": "council_round_1", "role_id": "skeptic"}
    role_rows = {row["id"]: row for row in m02["stages"][0]["roles"]}
    assert role_rows["theorist"]["recorded_samples"] == 1
    assert role_rows["experimentalist"]["recorded_samples"] == 2
    assert role_rows["skeptic"]["recorded_samples"] == 0
    assert role_rows["prior_work_killer"]["recorded_samples"] == 2
    assert "missing for every pre-workbench response" in role_rows["theorist"]["legacy_metadata_note"]
    assert m03["stages"][0]["status"] == "blocked"
    assert len(m03["stages"][0]["blockers"]) == 5
    blockers = "\n".join(m03["stages"][0]["blockers"])
    assert "015416020fab575e7b968d64969f4df4c8ab453fe033314f7812b2f1a66bdfb7" in blockers
    assert "claim_with_searchable_state_space" in blockers
    assert "fb109998c31c0dc2d7ddd2bc9ee99e2bc8e51d66e6b4aca5f55e99d562d50fa0" in blockers
    assert m04["human_hold"] is True
    assert m04["gate_status"]["gate_2"] == "unauthorized"
    assert (root / "mission-03/workbench.yaml").is_file()


def test_validate_checks_manifest_prompt_paths_and_is_read_only(tmp_path, monkeypatch):
    manifest = configure_sandbox(tmp_path, monkeypatch)

    report = workbench.validate_mission("mission-99")

    assert "Manifest and configured prompt/input paths validate" in report
    assert "Next required role: council_round_1 / skeptic" in report
    assert not (tmp_path / "runtime/runs").exists()
    assert not (tmp_path / "runtime/workbench_specs").exists()

    (manifest.parent / "prompts/role.md").unlink()
    with pytest.raises(FileNotFoundError, match="prompt.source not found"):
        workbench.validate_mission("mission-99")
    assert not (tmp_path / "runtime/runs").exists()


def test_next_stages_exact_manual_prompt_and_makes_no_model_call(tmp_path, monkeypatch):
    manifest = configure_sandbox(tmp_path, monkeypatch)
    prompt_path = manifest.parent / "prompts/role.md"
    exact_prompt = b"  Exact prompt with trailing spaces.  \r\nSecond line.\n"
    prompt_path.write_bytes(exact_prompt)

    staged = workbench.stage_next("mission-99")

    assert staged.state["run_status"] == "waiting_for_human"
    assert staged.state["jobs"]["skeptic_single"]["status"] == "waiting_for_human"
    assert staged.prompt_path.read_bytes() == exact_prompt
    handoff_path = staged.run_dir / "handoffs/skeptic_single.json"
    handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
    assert handoff["interface"] == "manual_arena_ui"
    assert handoff["model_call_made"] is False
    assert handoff["prompt_sha256"] == hashlib.sha256(exact_prompt).hexdigest()
    assert handoff["canonical_response_artifact"] == "mission-99/responses/skeptic.md"
    assert not (tmp_path / "runtime/browser_profiles").exists()
    assert list((tmp_path / "runtime/runs/mission-99").glob("*/run_state.json")) == [
        staged.run_dir / engine.STATE_FILE
    ]


def test_resume_reprints_same_hash_checked_prompt_without_resubmission(tmp_path, monkeypatch):
    configure_sandbox(tmp_path, monkeypatch)
    monkeypatch.chdir(tmp_path)
    staged = workbench.stage_next("mission-99")
    run_dir, resumed_state, message = workbench.resume("mission-99")

    assert run_dir == staged.run_dir
    assert resumed_state["jobs"]["skeptic_single"]["attempts"] == 1
    assert message.count(str(staged.prompt_path)) >= 1
    assert hashlib.sha256(staged.prompt_path.read_bytes()).hexdigest() in message
    assert len(list((tmp_path / "runtime/runs/mission-99").iterdir())) == 1


def test_interrupted_manual_handoff_recovers_from_original_prompt_snapshot(tmp_path, monkeypatch):
    configure_sandbox(tmp_path, monkeypatch)
    staged = workbench.stage_next("mission-99")
    handoff_path = staged.run_dir / "handoffs/skeptic_single.json"
    first_handoff = handoff_path.read_bytes()

    state = read_state(staged.run_dir)
    state["jobs"]["skeptic_single"]["status"] = "running"
    state["run_status"] = "in_progress"
    (staged.run_dir / engine.STATE_FILE).write_text(
        json.dumps(state, indent=2), encoding="utf-8"
    )
    source_prompt = Path(manifest_prompt := state["mission_path"]).parent / state["jobs"]["skeptic_single"]["prompt_artifact"]
    source_prompt.write_text("changed after interruption\n", encoding="utf-8")

    run_dir, resumed_state, message = workbench.resume("mission-99")

    assert run_dir == staged.run_dir
    assert resumed_state["jobs"]["skeptic_single"]["status"] == "waiting_for_human"
    assert resumed_state["jobs"]["skeptic_single"]["attempts"] == 2
    assert handoff_path.read_bytes() == first_handoff
    assert staged.prompt_path.read_bytes() == b"Exact role prompt.\n"
    assert "Prompt SHA-256" in message


def test_paired_samples_are_two_independent_jobs_with_identical_prompt(tmp_path, monkeypatch):
    configure_sandbox(tmp_path, monkeypatch)
    path = tmp_path / "mission-99/workbench.yaml"
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    role = payload["stages"][0]["roles"][0]
    role["sample_artifacts"] = {
        "a": "mission-99/responses/skeptic.a.md",
        "b": "mission-99/responses/skeptic.b.md",
    }
    role["max_samples"] = 2
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    staged = workbench.stage_next("mission-99", sample_ids=["a", "b"])

    assert set(staged.state["jobs"]) == {"skeptic_a", "skeptic_b"}
    assert all(row["status"] == "waiting_for_human" for row in staged.state["jobs"].values())
    assert (staged.run_dir / "inputs/prompts/skeptic_a.md").read_bytes() == (
        staged.run_dir / "inputs/prompts/skeptic_b.md"
    ).read_bytes()


def test_ingest_preserves_verbatim_bytes_metadata_and_immutable_mirror(tmp_path, monkeypatch):
    configure_sandbox(tmp_path, monkeypatch)
    staged = workbench.stage_next("mission-99")
    response_path = tmp_path / "arena-response.txt"
    response_bytes = "  Response stays exact.\r\nUnicode: naïve.\n```text\nend  \n".encode("utf-8")
    response_path.write_bytes(response_bytes)
    metadata_path = tmp_path / "arena-metadata.json"
    metadata_bytes = json.dumps(
        {
            "arena_mode": "Direct",
            "model_label": "  Model X  ",
            "session_time": "2026-10-05 13:00 PDT (observed, source timezone unknown)",
            "tools": {"browsing": False, "code_execution": False},
            "account_note": "retained without normalization",
        },
        ensure_ascii=False,
        indent=2,
    ).encode("utf-8")
    metadata_path.write_bytes(metadata_bytes)

    result = workbench.ingest(
        staged.run_dir,
        "skeptic_single",
        response_path,
        metadata_path=metadata_path,
    )

    run_response = staged.run_dir / "artifacts/jobs/skeptic_single/response.md"
    canonical = tmp_path / "mission-99/responses/skeptic.md"
    intake = tmp_path / "mission-99/responses/skeptic.intake.json"
    assert run_response.read_bytes() == response_bytes
    assert canonical.read_bytes() == response_bytes
    assert result["response_sha256"] == hashlib.sha256(response_bytes).hexdigest()
    record = json.loads(intake.read_text(encoding="utf-8"))
    assert record["method"] == "manual_arena_ui"
    assert record["model_label"] == "  Model X  "
    assert record["run_metadata"]["account_note"] == "retained without normalization"
    assert record["missing_metadata"] == []
    assert record["run_metadata_source"]["sha256"] == hashlib.sha256(metadata_bytes).hexdigest()
    assert record["prompt_sha256"] == staged.prompt_sha256

    duplicate = workbench.ingest(
        staged.run_dir,
        "skeptic_single",
        response_path,
        metadata_path=metadata_path,
    )
    assert duplicate["already_ingested"] is True
    assert canonical.read_bytes() == response_bytes
    response_path.write_bytes(b"different model response\n")
    with pytest.raises(workbench.WorkbenchError, match="immutable"):
        workbench.ingest(staged.run_dir, "skeptic_single", response_path)


def test_missing_run_metadata_is_recorded_not_invented(tmp_path, monkeypatch):
    configure_sandbox(tmp_path, monkeypatch)
    staged = workbench.stage_next("mission-99")
    response_path = tmp_path / "response.txt"
    response_path.write_bytes(b"A real response\n")

    workbench.ingest(staged.run_dir, "skeptic_single", response_path)

    record = json.loads(
        (tmp_path / "mission-99/responses/skeptic.intake.json").read_text(encoding="utf-8")
    )
    assert record["model_label"] is None
    assert record["run_metadata"] == {}
    assert record["missing_metadata"] == REQUIRED_METADATA
    assert record["run_metadata_source"] is None
    sample = workbench.mission_status("mission-99")["stages"][0]["roles"][0]["samples"][0]
    assert sample["intake_status"] == "recorded"
    assert sample["missing_metadata"] == REQUIRED_METADATA


def test_invalid_response_never_advances_or_writes_canonical_outputs(tmp_path, monkeypatch):
    configure_sandbox(tmp_path, monkeypatch)
    staged = workbench.stage_next("mission-99")
    invalid_path = tmp_path / "invalid.txt"
    invalid_path.write_bytes(b"\xff\xfe")

    with pytest.raises(workbench.WorkbenchError, match="UTF-8"):
        workbench.ingest(staged.run_dir, "skeptic_single", invalid_path)
    assert read_state(staged.run_dir)["jobs"]["skeptic_single"]["status"] == "waiting_for_human"
    assert not (staged.run_dir / "artifacts/jobs/skeptic_single/response.md").exists()
    assert not (tmp_path / "mission-99/responses/skeptic.md").exists()

    invalid_path.write_bytes(b" \r\n\t")
    with pytest.raises(workbench.WorkbenchError, match="non-whitespace"):
        workbench.ingest(staged.run_dir, "skeptic_single", invalid_path)


def test_real_mission_holds_and_stage0_blockers_refuse_before_materialization(tmp_path, monkeypatch):
    root = Path(__file__).resolve().parents[1]
    monkeypatch.setattr(workbench, "PROJECT_ROOT", root)
    monkeypatch.setattr(workbench, "WORKBENCH_SPEC_ROOT", tmp_path / "specs")
    monkeypatch.setattr(engine, "RUN_ROOT", tmp_path / "runs")

    for mission_id in ("mission-01", "mission-03", "mission-04"):
        with pytest.raises(workbench.WorkbenchBlocked):
            workbench.stage_next(mission_id)

    assert not (tmp_path / "runs").exists()
    assert not (tmp_path / "specs").exists()


def test_manifest_rejects_escape_paths_and_duplicate_yaml_keys(tmp_path, monkeypatch):
    configure_sandbox(tmp_path, monkeypatch)
    path = tmp_path / "mission-99/workbench.yaml"
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    payload["stages"][0]["roles"][0]["sample_artifacts"]["single"] = "../escape.md"
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    with pytest.raises(workbench.WorkbenchError, match="safe repository-relative"):
        workbench.load_mission("mission-99")

    path.write_text(
        "schema_version: 1\nschema_version: 1\nmission_id: mission-99\n",
        encoding="utf-8",
    )
    with pytest.raises(workbench.WorkbenchError, match="duplicate YAML key"):
        workbench.load_mission("mission-99")


def test_template_context_is_hashed_and_blindness_guard_blocks_leaks(tmp_path, monkeypatch):
    root = tmp_path
    monkeypatch.setattr(workbench, "PROJECT_ROOT", root)
    (root / "mission-99/prompts").mkdir(parents=True)
    (root / "mission-99/prompts/template.md").write_text(
        "Classify only from this vocabulary:\n{{feature_vocabulary}}\n",
        encoding="utf-8",
    )
    (root / "mission-99/features.yaml").write_text("features: [alpha]\n", encoding="utf-8")
    (root / "mission-99/candidate_measurements.yaml").write_text(
        "hidden expectation: secret-result\n", encoding="utf-8"
    )
    role = {
        "id": "blind_characterizer",
        "prompt": {
            "template": "mission-99/prompts/template.md",
            "context": {"feature_vocabulary": "mission-99/features.yaml"},
        },
        "blindness": {
            "forbidden_sources": ["mission-99/candidate_measurements.yaml"],
            "forbidden_literals": ["secret-result", "counterexample card text"],
        },
    }

    prompt, sources, source_paths = workbench._render_prompt(role)
    assert prompt == b"Classify only from this vocabulary:\nfeatures: [alpha]\n\n"
    assert {row["kind"] for row in sources} == {"template", "context"}
    assert "mission-99/candidate_measurements.yaml" not in source_paths

    role["prompt"]["context"]["compiler_expectation"] = "mission-99/candidate_measurements.yaml"
    (root / "mission-99/prompts/template.md").write_text(
        "{{feature_vocabulary}}\n{{compiler_expectation}}\n", encoding="utf-8"
    )
    with pytest.raises(workbench.WorkbenchError, match="forbidden source"):
        workbench._render_prompt(role)

    role["prompt"]["context"] = {"feature_vocabulary": "mission-99/features.yaml"}
    (root / "mission-99/prompts/template.md").write_text(
        "{{feature_vocabulary}}\nsecret-result\n", encoding="utf-8"
    )
    with pytest.raises(workbench.WorkbenchError, match="forbidden literal"):
        workbench._render_prompt(role)
