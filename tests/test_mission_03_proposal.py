"""Integrity checks for the Mission 03 proposal (mission-03/).

These test the proposal's internal consistency and the power table's reproducibility. They say nothing
about whether the experiment would find an effect, and nothing about whether strategies help.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
M3 = ROOT / "mission-03"

PROTOCOL_SEED_KEYS = [
    "seed_id", "title", "repo_context", "intuition", "precise_research_question", "why_it_might_be_true",
    "what_would_surprise_us", "candidate_hypotheses", "known_alternatives", "possible_experiment",
    "known_unknowns", "likely_confounds", "relevant_prior_work", "candidate_claim_ceiling",
    "possible_future_research_on_failure",
]


def _load(name: str):
    return yaml.safe_load((M3 / name).read_text(encoding="utf-8"))


def test_seed_follows_the_protocol_schema_and_names_a_null() -> None:
    seed = _load("seed.yaml")
    assert list(seed) == PROTOCOL_SEED_KEYS
    ids = [h["id"] for h in seed["candidate_hypotheses"]]
    assert ids[0] == "H0" and len(ids) == len(set(ids))
    cf = [c["id"] for c in seed["likely_confounds"]]
    assert len(cf) == len(set(cf))


def test_every_identifier_a_work_package_cites_exists_and_nothing_is_orphaned() -> None:
    seed = _load("seed.yaml")
    spec = _load("candidate_measurements.yaml")
    wps = _load("work_packages/candidates.yaml")["work_packages"]

    hypotheses = {h["id"] for h in seed["candidate_hypotheses"]}
    confounds = {c["id"] for c in seed["likely_confounds"]}
    measurements = {m["id"] for m in spec["measurements"]}
    controls = {c["id"] for c in spec["controls"]}
    aborts = {a["id"] for a in spec["abort_conditions"]}
    falsifications = {f["id"] for f in spec["falsification"]["tests"]}

    cited = {"hypotheses": set(), "measurements": set(), "controls": set(), "aborts": set(), "falsification": set()}
    universe = {"hypotheses": hypotheses, "measurements": measurements, "controls": controls,
                "aborts": aborts, "falsification": falsifications}
    for wp in wps:
        for kind, ids in wp["serves"].items():
            assert kind in universe, f"{wp['id']} serves unknown kind {kind}"
            for i in ids:
                assert i in universe[kind], f"{wp['id']} cites {i}, which is not defined"
            cited[kind].update(ids)

    # protocol rule 2 in reverse: every control, measurement, abort condition and test is built or run by some package
    for kind in ("measurements", "controls", "aborts", "falsification"):
        assert universe[kind] <= cited[kind], f"no work package serves: {sorted(universe[kind] - cited[kind])}"

    # every control names confounds that exist; every decision regime names hypotheses that exist
    for c in spec["controls"]:
        assert set(c["rules_out"]) <= confounds, c["id"]
    for key, regime in spec["decision_regimes"].items():
        if key == "note":
            continue
        assert set(regime.get("supports", [])) <= hypotheses, key
        assert set(regime.get("inconsistent_with", [])) <= hypotheses, key


def _power_module():
    path = M3 / "analysis" / "power_simulation.py"
    spec = importlib.util.spec_from_file_location("mission_03_power_simulation", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_committed_power_rows_reproduce_exactly() -> None:
    module = _power_module()
    table = json.loads((M3 / "analysis" / "power_table.json").read_text(encoding="utf-8"))
    rows = [r for r in table["results"] if r["runs_per_arm_per_family"] == 40][:4]
    assert rows
    for row in rows:
        fresh = module.one_config(row["baseline_pass_rate"], row["true_S"], row["runs_per_arm_per_family"])
        assert {k: row[k] for k in fresh} == fresh


def test_power_table_has_the_expected_shape() -> None:
    table = json.loads((M3 / "analysis" / "power_table.json").read_text(encoding="utf-8"))
    results = table["results"]
    tolerance = 0.04  # Monte Carlo noise at 2,000 simulations
    for p0 in sorted({r["baseline_pass_rate"] for r in results}):
        by = {(r["runs_per_arm_per_family"], r["true_S"]): r for r in results if r["baseline_pass_rate"] == p0}
        sizes = sorted({n for n, _ in by})
        effects = sorted({s for _, s in by})
        for n in sizes:
            assert by[(n, 0.0)]["p_detect"] <= 0.06, "false positive rate too high"
            detect = [by[(n, s)]["p_detect"] for s in effects]
            assert all(b >= a - tolerance for a, b in zip(detect, detect[1:])), "detection should not fall as the effect grows"
        for s in effects:
            if s == 0.0:
                continue
            detect = [by[(n, s)]["p_detect"] for n in sizes]
            assert all(b >= a - tolerance for a, b in zip(detect, detect[1:])), "detection should not fall as the sample grows"
