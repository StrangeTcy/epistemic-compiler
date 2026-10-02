"""Integrity checks for the Mission 04 proposal (mission-04/).

These test the proposal's internal consistency only. They say nothing about whether the phenomenon is
real, whether any model shows common-knowledge neglect, or whether the oracle sketch is correct.
"""
from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
M4 = ROOT / "mission-04"

PROTOCOL_SEED_KEYS = [
    "seed_id", "title", "repo_context", "intuition", "precise_research_question", "why_it_might_be_true",
    "what_would_surprise_us", "candidate_hypotheses", "known_alternatives", "possible_experiment",
    "known_unknowns", "likely_confounds", "relevant_prior_work", "candidate_claim_ceiling",
    "possible_future_research_on_failure",
]

REQUIRED_DESIGN_SECTIONS = [
    "Formal environment definition",
    "Treatment and control conditions",
    "Oracle specification",
    "FALS-01",
    "FALS-02",
    "FALS-03",
    "Claim ceiling",
]


def _seed():
    return yaml.safe_load((M4 / "seed.yaml").read_text(encoding="utf-8"))


def test_seed_follows_the_protocol_schema_and_names_a_null() -> None:
    seed = _seed()
    assert list(seed) == PROTOCOL_SEED_KEYS
    ids = [h["id"] for h in seed["candidate_hypotheses"]]
    assert ids[0] == "H0" and len(ids) == len(set(ids))
    cf = [c["id"] for c in seed["likely_confounds"]]
    assert len(cf) == len(set(cf))
    lp = [p["id"] for p in seed["relevant_prior_work"]]
    assert len(lp) == len(set(lp))
    assert seed["seed_id"] == "S04"


def test_seed_does_not_claim_what_it_says_it_does_not() -> None:
    seed = _seed()
    ceiling = seed["candidate_claim_ceiling"]
    assert ceiling["cannot_justify"], "the ceiling must bind the claim, not just state it"
    # the seed's own honesty markers survive serialization
    assert "NOT present in this workspace" in seed["repo_context"]


def test_design_exists_and_covers_the_briefs_required_sections() -> None:
    text = (M4 / "design.md").read_text(encoding="utf-8")
    for section in REQUIRED_DESIGN_SECTIONS:
        assert section in text, f"design.md is missing: {section}"


def test_harvest_exists_and_points_at_real_evidence_paths() -> None:
    harvest = (ROOT / "mission-01" / "harvest.md").read_text(encoding="utf-8")
    for evidence in [
        "results/part_a_stratum_a1.json",
        "results/part_a_stratum_a2.json",
        "results/summary_metrics.json",
        "falsification/falsification_results.json",
        "results/part_b_multichart_gluing.json",
        "claim_set.md",
    ]:
        assert evidence in harvest, f"harvest cites {evidence} but the test expects it"
        assert (ROOT / "mission-01" / evidence).exists(), f"harvest cites a missing file: {evidence}"
