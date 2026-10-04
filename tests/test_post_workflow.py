from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

import pytest

from runtime import engine
from runtime.post_production import (
    _audit_numeric_claim_traceability,
    _compact_writer_template,
    _normalize_cross_review,
    _render_model_artifact,
    validate_article,
)
from scripts import post_workflow


@pytest.fixture
def mission(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    mission_path = post_workflow.ensure_workflow()
    spec = engine.load_mission(mission_path)
    monkeypatch.setattr(engine, "RUN_ROOT", tmp_path / "runs")
    return mission_path, spec


def test_existing_mission_uses_frozen_snapshots_without_rebuilding(monkeypatch: pytest.MonkeyPatch):
    mission_path = post_workflow.MISSION_PATH
    assert mission_path.is_file()

    def unexpected_rebuild():
        pytest.fail("existing immutable snapshots should not be regenerated")

    monkeypatch.setattr(post_workflow, "_snapshot_sources", unexpected_rebuild)
    assert post_workflow.ensure_workflow() == mission_path


def test_post04_writer_prompt_keeps_campaign_denominators_and_provider_rows_distinct():
    prompt = _compact_writer_template("POST-04")
    assert "194 raw scored rows" in prompt
    assert "24 separate omissions" in prompt
    assert "193-row single-provider-exclusion sensitivity set" in prompt
    assert "192-row two-provider-exclusion analysis set" in prompt
    assert "Two raw rows have `invalid_action` labels" in prompt
    assert "no spend field" in prompt
    assert "never present it as a rate for this campaign" in prompt
    assert "Do not import unrelated cross-post bibliography items" in prompt


def test_post04_reference_packet_includes_only_relevant_prior_work():
    references = (post_workflow.SNAPSHOT_ROOT / "shared" / "references.md").read_text(encoding="utf-8")
    rendered = _render_model_artifact("references", references, "POST-04", "a" * 64)
    assert "Are ‘Solved Issues’ in SWE-bench Really Solved Correctly?" in rendered
    assert "10.1145/3744916.3764576" in rendered
    assert "not an estimate for the Atria campaign" in rendered
    assert "VarBench" not in rendered


def _packet() -> str:
    metadata = {
        "post_id": "POST-02",
        "publication_date": "2026-10-03",
        "trace_row_ids": ["POST-02-C01"],
        "allowed_numbers": ["1"],
        "evidence_input_sha256": {"mission:source_draft_POST-02": "a" * 64},
    }
    return (
        "# Evidence packet\n\n<!-- POST_PRODUCTION_VALIDATOR_METADATA\n"
        + json.dumps(metadata)
        + "\n-->\n"
    )


def _valid_article(extra: str = "") -> str:
    caveats = (
        "This Bayesian inference task is not a recursive theory of mind benchmark. "
        "It is one seed per cell. The campaign source repository was dirty, so the "
        "clean comparator does not prove the exact paid-run source. The compile-only "
        "judgment is exploratory rather than a validated behavioral reference. "
        "The judge's guarantee is local to the specified task and does not establish "
        "a general capability. The role passes are not independent replications."
    )
    filler = "The evidence supports a narrow description, not a general ranking of reasoning. "
    body = (
        "{% include mathjax.html %}\n\n"
        "*by <span class=\"icon-self\">StrangeTcy</span>*\n\n"
        "<dl class=\"epistemic-status\"><dt>Evidence</dt>"
        "<dd>One campaign; bounded interpretation.</dd></dl>\n\n"
        + caveats
        + "\n\n"
        + extra
        + "\n\n"
        + (filler * 100)
    )
    return (
        '---\ntitle: "Bayesian evidence and its limits"\n'
        "date: 2026-10-03\nlayout: post\n---\n\n"
        + body
    )


def test_mission_uses_exact_internal_drafts_and_parallel_identical_inputs(mission):
    mission_path, spec = mission
    assert len(spec.jobs) == 54
    for post_id in post_workflow.POST_IDS:
        key = f"source_draft_{post_id}"
        snapshot = (mission_path.parent / spec.inputs[key]).read_bytes()
        source = (post_workflow.POSTS / post_workflow.SOURCE_DRAFTS[post_id]).read_bytes()
        assert snapshot == source
        writer_a = spec.job_map[f"post{post_id[-2:]}_battle_writer_a"]
        writer_b = spec.job_map[f"post{post_id[-2:]}_battle_writer_b"]
        assert writer_a.input_artifacts == writer_b.input_artifacts == (
            f"job:post{post_id[-2:]}_prepare_post:response",
        )
        assert writer_a.dependencies == writer_b.dependencies == (
            f"post{post_id[-2:]}_prepare_post",
        )
        assert writer_a.site == writer_b.site == "manual"
        assert writer_a.prompt_artifact == writer_b.prompt_artifact
    assert spec.job_map["post02_prepare_post"].dependencies == (
        "post01_validation_revision_validator",
    )
    style_snapshot = mission_path.parent / spec.inputs["style_reference_material"]
    assert "The Diagram Is the Spec" in style_snapshot.read_text(encoding="utf-8")
    assert not any("-DRAFT.md" in path for path in spec.inputs.values())


def test_start_waits_for_pair_then_critic_and_preserves_ingest(mission):
    mission_path, _ = mission
    run_dir, state = asyncio.run(
        engine.run_mission(mission_path, max_parallel=2, announce=None)
    )
    assert state["run_status"] == "waiting_for_human"
    job_a = state["jobs"]["post01_battle_writer_a"]
    job_b = state["jobs"]["post01_battle_writer_b"]
    assert job_a["status"] == job_b["status"] == "waiting_for_human"
    assert job_a["prompt_sha256"] == job_b["prompt_sha256"]
    assert job_a["input_sha256"] == job_b["input_sha256"]
    assert state["jobs"]["post02_prepare_post"]["status"] == "queued"
    for job_id, job_state in (("post01_battle_writer_a", job_a), ("post01_battle_writer_b", job_b)):
        handoff_path = run_dir / job_state["interaction"]["handoff_json"]
        handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
        assert handoff["workflow_id"] == post_workflow.MISSION_ID
        assert handoff["post_id"] == "POST-01"
        assert handoff["job_id"] == job_id
        assert handoff["next_stage"] == "editorial_critic"
        assert handoff["expected_response_artifact"] == job_state["output_artifact"]
        assert handoff["inputs"][0]["sha256"] == job_state["input_sha256"][0]
        expanded = {row["reference"]: row for row in handoff["expanded_source_inputs"]}
        assert "mission:source_draft_POST-01" in expanded
        assert expanded["mission:source_draft_POST-01"]["sha256"]
        prompt = (run_dir / handoff["prompt_to_paste"]).read_text(encoding="utf-8")
        assert len(prompt) < 32_768
        assert "verbatim excerpts from actual StrangeTcy posts" in prompt
        assert "The benchmark’s “hard” is not one difficulty scale" in prompt
        assert "The Diagram Is the Spec" in prompt
        assert "A unit test says:" in prompt
        assert "Most benchmarks hand the agent its context for free." in prompt
        assert "The first formalisation was wrong." in prompt
        assert "POST_PRODUCTION_VALIDATOR_METADATA" not in prompt
        expanded = handoff["input_renderings"][0]["source_renderings"]
        style_rendering = next(row for row in expanded if row["reference"] == "mission:style_reference_material")
        assert len(style_rendering["source_sha256"]) == len(style_rendering["rendered_sha256"]) == 64

    engine.ingest_human_response(
        run_dir,
        "post01_battle_writer_a",
        b"# Writer A response\nA complete, distinct essay draft.\n",
        model_label="left side-by-side response",
    )
    state_after_a = json.loads((run_dir / engine.STATE_FILE).read_text(encoding="utf-8"))
    assert state_after_a["jobs"]["post01_battle_writer_a"]["status"] == "completed"
    assert state_after_a["jobs"]["post01_battle_writer_b"]["status"] == "waiting_for_human"
    with pytest.raises(engine.MissionValidationError, match="not waiting_for_human"):
        engine.ingest_human_response(
            run_dir, "post01_battle_writer_a", b"attempted replacement"
        )

    engine.ingest_human_response(
        run_dir,
        "post01_battle_writer_b",
        b"# Writer B response\nA differently structured essay draft.\n",
        model_label="right side-by-side response",
    )
    run_dir, resumed = asyncio.run(
        engine.run_mission(
            mission_path,
            resume_dir=run_dir,
            resume_waiting_for_human=False,
            max_parallel=2,
            announce=None,
        )
    )
    assert resumed["jobs"]["post01_battle_writer_a"]["status"] == "completed"
    assert resumed["jobs"]["post01_battle_writer_b"]["status"] == "completed"
    assert resumed["jobs"]["post01_editorial_critic"]["status"] == "waiting_for_human"
    assert resumed["jobs"]["post02_prepare_post"]["status"] == "queued"
    critic_handoff = json.loads(
        (run_dir / resumed["jobs"]["post01_editorial_critic"]["interaction"]["handoff_json"]).read_text(encoding="utf-8")
    )
    critic_prompt = (run_dir / critic_handoff["prompt_to_paste"]).read_text(encoding="utf-8")
    packet_size = (run_dir / resumed["jobs"]["post01_prepare_post"]["output_artifact"]).stat().st_size
    assert len(critic_prompt) < packet_size + 20_000
    assert "Rendered message SHA-256" not in critic_prompt
    critic_renderings = critic_handoff["input_renderings"][0]["source_renderings"]
    assert any(row["reference"] == "mission:style_reference_material" for row in critic_renderings)
    assert "Actual StrangeTcy reference-post excerpts" in critic_prompt
    assert "Writer A response" in critic_prompt
    assert "Writer B response" in critic_prompt
    assert (run_dir / job_a["interaction"]["handoff_json"]).is_file()
    assert (run_dir / "artifacts/jobs/post01_battle_writer_a/human_ingestion.json").is_file()


def test_compact_trace_rows_follow_numeric_support_through_finding_records():
    trace_rows = [
        {"post_id": "POST-01", "claim_id": "POST-01-C01", "finding_ids": "F-02"}
    ]
    findings = [
        {
            "id": "F-02",
            "claim": "The campaign report records scored selected cases.",
            "quantitative_result": "194 scored cases; 131 PASS / 63 FAIL raw, and 131 PASS / 61 FAIL among 192 eligible cases.",
            "limitations": ["Provider transients are a sensitivity exclusion."],
        }
    ]
    audit = _audit_numeric_claim_traceability(
        "The archive contains 194 scored cases.", trace_rows, findings
    )
    assert audit["unmapped_numeric_claim_sentences"] == []
    assert audit["mapped_numeric_claim_sentences"][0]["candidate_trace_rows"][0]["claim_id"] == "POST-01-C01"


def test_numeric_traceability_includes_linked_selected_case_details():
    trace_rows = [
        {"post_id": "POST-01", "claim_id": "POST-01-C03", "finding_ids": "F-06;F-10"}
    ]
    findings = [
        {
            "id": "F-06",
            "claim": "Selected regex outcomes differ across levels.",
            "quantitative_result": "At easy surface, lengths 32, 128, and 512 pass; medium/hard labels at length 32 fail.",
            "limitations": ["One seed per cell."],
        }
    ]
    failure_rows = [
        {"environment": "regex_state_machine", "condition": "surface=medium", "judge": "behavioral_reference", "score": "0.208333", "failure": "underfit", "detail": "length mismatch: input 32, output 34"},
        {"environment": "regex_state_machine", "condition": "surface=hard", "judge": "behavioral_reference", "score": "0.208333", "failure": "underfit", "detail": "length mismatch: input 32, output 66"},
    ]
    audit = _audit_numeric_claim_traceability(
        "At length 32, the medium and hard outputs are 34 and 66 characters.",
        trace_rows,
        findings,
        failure_rows,
    )
    candidate = audit["mapped_numeric_claim_sentences"][0]["candidate_trace_rows"][0]
    assert set(candidate["matched_numbers"]) >= {"32", "34", "66"}


def test_validator_flags_numeric_and_recursive_tom_overclaims():
    valid = validate_article(_valid_article(), "POST-02", _packet(), expected_date="2026-10-03")
    assert valid["valid"] is True, valid["errors"]
    bad = validate_article(
        _valid_article("The task demonstrates recursive theory of mind and has 987 episodes."),
        "POST-02",
        _packet(),
        expected_date="2026-10-03",
    )
    assert bad["valid"] is False
    assert any("987" in error for error in bad["errors"])
    assert any("recursive-ToM" in error for error in bad["errors"])


def test_validator_flags_turing_completeness_claim_and_internal_trace_leak():
    article = _valid_article("The task establishes Turing completeness. It cites F-04.")
    bad = validate_article(article, "POST-05", _packet(), expected_date="2026-10-03")
    # POST-05 metadata is normally supplied by its own packet; this test focuses
    # the shared internal-leak and Turing-claim checks despite a post-metadata mismatch.
    assert bad["valid"] is False
    assert any("F-xx" in error or "trace" in error for error in bad["errors"])
    assert any("Turing-completeness" in error for error in bad["errors"])


def test_cross_post_review_router_normalizes_only_targeted_revisions():
    raw = json.dumps(
        {
            "revisions": [
                {"post_id": "POST-03", "needed": True, "issues": ["Repeat"], "change_request": "Vary the opening only."}
            ]
        }
    )
    normalized = _normalize_cross_review(raw)
    assert len(normalized["revisions"]) == 5
    assert normalized["revisions"][2]["needed"] is True
    assert normalized["revisions"][2]["change_request"] == "Vary the opening only."
    assert normalized["revisions"][0]["needed"] is False
