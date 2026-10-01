from __future__ import annotations

import copy
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.validate_ir import (  # noqa: E402
    STANDARD_PATHS,
    Document,
    ancestors,
    collect_cards,
    effective_obligations,
    load_documents,
    main,
    specialization_depth,
    validate_documents,
)

CONSERVED = "invariant-conserved-quantity.yaml"
CLOSED = "invariant-closed-predicate.yaml"
MUTILATED = "mutilated-board.episode.yaml"
BOUNDARY = "boundary-contract.episode.yaml"


# --------------------------------------------------------------------------------------------
# Helpers: edit the shipped library in memory and check which issue codes appear.
# --------------------------------------------------------------------------------------------
_LIBRARY_CACHE: list[Document] = []


def _library() -> list[Document]:
    """The shipped library, parsed once. Safe to share: `_edit` deep-copies before it mutates anything."""
    if not _LIBRARY_CACHE:
        docs, problems = load_documents([PROJECT_ROOT / p for p in STANDARD_PATHS], PROJECT_ROOT)
        assert not problems
        _LIBRARY_CACHE.extend(docs)
    return list(_LIBRARY_CACHE)


def _keys(expr: str) -> list[str | int]:
    return [int(t[1:-1]) if t.startswith("[") else t for t in re.findall(r"[^.\[\]]+|\[\d+\]", expr)]


def _apply(data: Any, op: tuple) -> None:
    kind, expr, *rest = op
    *head, last = _keys(expr)
    node = data
    for key in head:
        node = node[key]
    if kind == "set":
        node[last] = rest[0]
    elif kind == "del":
        del node[last]
    elif kind == "append":
        node[last].append(rest[0])
    elif kind == "pop":
        node[last].pop(rest[0])
    else:  # pragma: no cover - guards the test DSL itself
        raise AssertionError(kind)


def _edit(docs: list[Document], suffix: str, ops: list[tuple]) -> list[Document]:
    out, hits = [], 0
    for doc in docs:
        if doc.where.endswith(suffix):
            data = copy.deepcopy(doc.data)
            for op in ops:
                _apply(data, op)
            out.append(Document(doc.where, data, doc.path))
            hits += 1
        else:
            out.append(doc)
    assert hits == 1, f"expected exactly one document ending in {suffix!r}, found {hits}"
    return out


def _codes(issues, severity: str = "error") -> set[str]:
    return {i.code for i in issues if i.severity == severity}


def _valid_state() -> dict[str, Any]:
    return {
        "ir_kind": "problem_state",
        "schema_version": "0.2",
        "problem_state_id": "PS-test",
        "title": "A test problem",
        "statement": "Can a target be reached from the start?",
        "goal": "Decide reachability.",
        "features": [
            {
                "feature": "transition_system_reachability_question",
                "evidence": "Moves are explicit operations on a state.",
                "confidence": "high",
                "asserted_by": "human",
            }
        ],
        "absent_features": [],
    }


def _with_state(docs: list[Document], state: dict[str, Any]) -> list[Document]:
    return [*docs, Document("mission-x/problem_state.yaml", state)]


# --------------------------------------------------------------------------------------------
# Baseline
# --------------------------------------------------------------------------------------------
def test_shipped_library_validates_cleanly_including_path_references() -> None:
    issues = validate_documents(_library(), PROJECT_ROOT)
    assert issues == []


def test_validation_does_not_mutate_its_inputs() -> None:
    docs = _library()
    snapshot = copy.deepcopy([d.data for d in docs])
    validate_documents(docs, PROJECT_ROOT)
    validate_documents(_edit(docs, MUTILATED, [("set", "applications[0].outcome", "invalid_transform")]), PROJECT_ROOT)
    assert [d.data for d in docs] == snapshot


def test_library_contains_the_expected_artifacts() -> None:
    kinds = sorted(d.data.get("ir_kind", "family_registry") for d in _library())
    assert kinds.count("strategy_card") == 8
    assert kinds.count("episode") == 2
    assert kinds.count("feature_vocabulary") == 1


# --------------------------------------------------------------------------------------------
# Strategy cards
# --------------------------------------------------------------------------------------------
HUMAN_REVIEW = [("set", "provenance.review_status", "human_reviewed"), ("set", "provenance.reviewed_by", "reviewer")]

CARD_CASES = [
    ("missing-obligations", CONSERVED, [("del", "obligations")], "missing-field"),
    ("empty-obligations", CONSERVED, [("set", "obligations", [])], "empty-field"),
    ("float-schema-version", CONSERVED, [("set", "schema_version", 0.2)], "schema-version"),
    ("bad-strategy-id", CONSERVED, [("set", "strategy_id", "Bad_ID")], "invalid-id"),
    ("filename-mismatch", CONSERVED, [("set", "strategy_id", "invariant-conserved-quantity-2")], "filename"),
    ("unknown-family", CONSERVED, [("set", "family", "magic")], "unknown-family"),
    ("bad-status", CONSERVED, [("set", "status", "great")], "invalid-field"),
    ("bad-version", CONSERVED, [("set", "version", 0)], "invalid-field"),
    ("unknown-feature", CONSERVED, [("set", "trigger.structural_conditions[0].requires_features", ["no_such_feature"])], "unknown-feature"),
    ("empty-requires-features", CONSERVED, [("set", "trigger.structural_conditions[0].requires_features", [])], "empty-field"),
    ("bad-condition-id", CONSERVED, [("set", "trigger.structural_conditions[0].id", "T1")], "invalid-id"),
    (
        "duplicate-condition-id", CLOSED,
        [("append", "trigger.structural_conditions", {"id": "TC1", "text": "dup", "requires_features": ["strategic_actors"]})],
        "duplicate-id",
    ),
    (
        "self-excluding-trigger", CONSERVED,
        [("set", "trigger.exclusion_conditions", [{"id": "XC1", "text": "x", "excluded_by_features": ["transition_system_reachability_question"]}])],
        "self-excluding-trigger",
    ),
    ("duplicate-obligation-id", CONSERVED, [("append", "obligations", {"id": "OB1", "text": "again"})], "duplicate-id"),
    ("missing-falsification-condition", CONSERVED, [("del", "validation.falsification_condition")], "missing-field"),
    ("missing-baseline", CONSERVED, [("set", "validation.baseline", "  ")], "invalid-field"),
    (
        "attempt-that-was-run-needs-a-record", CONSERVED,
        [("set", "validation.counterexample_attempts", [{"description": "d", "outcome": "none_found"}])],
        "missing-field",
    ),
    ("bad-exemplar-kind", CONSERVED, [("set", "exemplars[0].kind", "anecdote")], "invalid-field"),
    ("recorded-exemplar-needs-episode-id", CONSERVED, [("set", "exemplars[0].kind", "recorded_episode"), ("set", "exemplars[0].ref", "mission-01/claim_set.md")], "invalid-id"),
    ("bad-origin", CONSERVED, [("set", "provenance.origin", "robot")], "invalid-field"),
    ("episode-derived-needs-episode-refs", CONSERVED, [("set", "provenance.origin", "episode-derived")], "missing-provenance"),
    ("bad-episode-ref", CONSERVED, [("append", "provenance.episode_refs", "not-an-episode")], "invalid-id"),
    # Promotion policy.
    ("promotion-needs-human-review", CONSERVED, [("set", "status", "under_test")], "unreviewed-promotion"),
    ("human-review-needs-a-reviewer", CONSERVED, [("set", "provenance.review_status", "human_reviewed")], "missing-reviewer"),
    ("under-test-needs-tests", CONSERVED, [*HUMAN_REVIEW, ("set", "status", "under_test"), ("set", "validation.discriminating_tests", [])], "missing-tests"),
    ("supported-needs-recorded-exemplar", CONSERVED, [*HUMAN_REVIEW, ("set", "status", "supported_in_scope")], "unsupported-status"),
    ("disconfirmed-needs-a-counterexample", CONSERVED, [*HUMAN_REVIEW, ("set", "status", "disconfirmed_in_scope")], "unsupported-status"),
    # Exemplars must exemplify and must be of the right kind.
    ("recorded-exemplar-cannot-be-illustrative", CONSERVED, [("set", "exemplars[0].kind", "recorded_episode"), ("set", "exemplars[0].ref", "EP-MUTILATED-BOARD")], "illustrative-exemplar"),
    (
        "exemplar-must-apply-the-strategy", "decomposition-explicit-interfaces.yaml",
        [("set", "exemplars", [{"id": "EX1", "kind": "textbook_illustration", "ref": "strategies/examples/mutilated-board.episode.yaml", "note": "n"}])],
        "exemplar-mismatch",
    ),
    # Relations, parameters and bindings.
    ("relation-to-unknown-target", CONSERVED, [("set", "relations[0].target", "nope")], "unresolved-target"),
    ("specialization-needs-bindings", CONSERVED, [("del", "relations[0].bindings")], "missing-bindings"),
    ("binding-must-name-a-parent-parameter", CONSERVED, [("set", "relations[0].bindings", {"Z": "x"})], "unknown-parameter"),
    ("binding-must-be-text", CONSERVED, [("set", "relations[0].bindings", {"Q": ""})], "invalid-field"),
    ("self-relation", CONSERVED, [("set", "relations[0].target", "invariant-conserved-quantity")], "self-relation"),
    ("parent-without-parameters", CONSERVED, [("set", "relations[0].target", "decomposition-explicit-interfaces")], "unbindable-parent"),
    ("bindings-only-for-specializes", CONSERVED, [("set", "relations[0].type", "composes_with")], "invalid-field"),
    ("unknown-relation-type", CONSERVED, [("set", "relations[0].type", "kind-of")], "invalid-field"),
    (
        "specialization-cycle", CLOSED,
        [("set", "relations", [{"type": "specializes", "target": "invariant-conserved-quantity", "rationale": "r", "bindings": {"Q": "x"}}])],
        "specialization-cycle",
    ),
    ("duplicate-parameter-name", CLOSED, [("append", "parameters", {"name": "Q", "description": "again"})], "duplicate-id"),
]


@pytest.mark.parametrize(("case", "suffix", "ops", "code"), CARD_CASES, ids=[c[0] for c in CARD_CASES])
def test_card_defects_are_reported(case: str, suffix: str, ops: list[tuple], code: str) -> None:
    assert _codes(validate_documents(_library(), None)) == set()  # the unedited library is clean
    issues = validate_documents(_edit(_library(), suffix, ops), None)
    assert code in _codes(issues), [i.render() for i in issues]


def test_unknown_card_field_is_a_warning_and_strict_mode_escalates_it() -> None:
    issues = validate_documents(_edit(_library(), CONSERVED, [("set", "notes", "typo")]), None)
    assert _codes(issues) == set()
    assert "unknown-field" in _codes(issues, "warning")


def test_duplicate_strategy_id_across_files_is_reported() -> None:
    docs = _library()
    original = next(d for d in docs if d.where.endswith(CONSERVED))
    clone = Document("strategies/cards/clone.yaml", copy.deepcopy(original.data))
    assert "duplicate-id" in _codes(validate_documents([*docs, clone], None))


def test_source_reference_paths_and_family_fragments_are_checked_when_a_root_is_given() -> None:
    bad_path = _edit(_library(), CONSERVED, [("append", "provenance.source_refs", "research_protocol/missing.md")])
    assert "ref-not-found" in _codes(validate_documents(bad_path, PROJECT_ROOT))
    assert "ref-not-found" not in _codes(validate_documents(bad_path, None))  # no root: path checks are skipped
    bad_fragment = _edit(_library(), CONSERVED, [("append", "provenance.source_refs", "research_protocol/strategy_families.yaml#nonsense")])
    assert "ref-fragment" in _codes(validate_documents(bad_fragment, PROJECT_ROOT))


def test_a_fully_evidenced_supported_card_can_satisfy_the_policy_and_an_illustrative_episode_cannot() -> None:
    recorded_episode = next(d for d in _library() if d.where.endswith(MUTILATED))
    episode = copy.deepcopy(recorded_episode.data)
    episode.update(episode_id="EP-REC-1", status="recorded")
    episode["applications"][0]["measurement_refs"] = ["results/run-1.json"]
    card_ops = [
        *HUMAN_REVIEW,
        ("set", "status", "supported_in_scope"),
        ("append", "exemplars", {"id": "EX2", "kind": "recorded_episode", "ref": "EP-REC-1", "note": "A recorded run with artifacts."}),
        ("set", "validation.counterexample_attempts", [{"description": "Adversarial instance search", "outcome": "none_found", "ref": "results/attempt-1.json"}]),
        ("append", "provenance.episode_refs", "EP-REC-1"),
    ]
    docs = [*_edit(_library(), CONSERVED, card_ops), Document("strategies/examples/rec.episode.yaml", episode)]
    assert validate_documents(docs, None) == []

    episode["status"] = "illustrative"
    docs = [*_edit(_library(), CONSERVED, card_ops), Document("strategies/examples/rec.episode.yaml", episode)]
    assert "illustrative-exemplar" in _codes(validate_documents(docs, None))


# --------------------------------------------------------------------------------------------
# Problem states
# --------------------------------------------------------------------------------------------
STATE_CASES = [
    ("unknown-feature", [("set", "features[0].feature", "no_such_feature")], "unknown-feature"),
    ("feature-needs-evidence", [("del", "features[0].evidence")], "missing-field"),
    ("blank-evidence-is-only-a-label", [("set", "features[0].evidence", " ")], "invalid-field"),
    ("bad-confidence", [("set", "features[0].confidence", "certain")], "invalid-field"),
    ("duplicate-feature", [("append", "features", {"feature": "transition_system_reachability_question", "evidence": "e", "confidence": "low", "asserted_by": "human"})], "duplicate-feature"),
    ("present-and-absent", [("append", "absent_features", {"feature": "transition_system_reachability_question", "evidence": "e", "asserted_by": "human"})], "contradictory-feature"),
    ("absent-features-required", [("del", "absent_features")], "missing-field"),
    ("bad-state-id", [("set", "problem_state_id", "state-1")], "invalid-id"),
    ("missing-goal", [("del", "goal")], "missing-field"),
]


@pytest.mark.parametrize(("case", "ops", "code"), STATE_CASES, ids=[c[0] for c in STATE_CASES])
def test_problem_state_defects_are_reported(case: str, ops: list[tuple], code: str) -> None:
    assert _codes(validate_documents(_with_state(_library(), _valid_state()), None)) == set()
    state = _valid_state()
    for op in ops:
        _apply(state, op)
    issues = validate_documents(_with_state(_library(), state), None)
    assert code in _codes(issues), [i.render() for i in issues]


def test_standalone_state_without_features_warns_that_retrieval_will_be_empty() -> None:
    state = _valid_state()
    state["features"] = []
    issues = validate_documents(_with_state(_library(), state), None)
    assert _codes(issues) == set()
    assert "empty-features" in _codes(issues, "warning")


def test_duplicate_standalone_state_ids_are_reported() -> None:
    docs = _with_state(_with_state(_library(), _valid_state()), _valid_state())
    assert "duplicate-id" in _codes(validate_documents(docs, None))


# --------------------------------------------------------------------------------------------
# Episodes and application records
# --------------------------------------------------------------------------------------------
EPISODE_CASES = [
    # Strategy and trigger evidence.
    ("unknown-strategy", MUTILATED, [("set", "applications[0].strategy_ref.strategy_id", "no-such-strategy")], "unknown-strategy"),
    ("future-card-version", MUTILATED, [("set", "applications[0].strategy_ref.version", 3)], "future-version"),
    ("trigger-needs-declared-features", MUTILATED, [("pop", "problem_states[0].features", 1)], "trigger-not-supported"),
    ("unknown-trigger-condition", MUTILATED, [("set", "applications[0].trigger_evidence[0].condition_id", "TC9")], "unknown-condition"),
    ("no-trigger-basis", MUTILATED, [("set", "applications[0].trigger_evidence", [])], "missing-trigger-basis"),
    ("off-trigger-rationale-must-be-text", MUTILATED, [("set", "applications[0].off_trigger_rationale", 5)], "invalid-field"),
    # Obligation coverage: own and inherited obligations all count.
    ("success-with-unchecked-obligation", MUTILATED, [("set", "applications[0].obligation_checks[4].status", "not_checked")], "unverified-success"),
    ("success-missing-an-inherited-check", MUTILATED, [("pop", "applications[0].obligation_checks", 1)], "unverified-success"),
    ("success-with-a-failed-check", MUTILATED, [("set", "applications[0].obligation_checks[2].status", "failed")], "unverified-success"),
    ("unknown-obligation-id", MUTILATED, [("set", "applications[0].obligation_checks[0].obligation_id", "invariant-closed-predicate#OB9")], "unknown-obligation"),
    ("passed-check-needs-evidence", MUTILATED, [("del", "applications[0].obligation_checks[0].evidence")], "missing-evidence"),
    ("invalid-transform-needs-a-failed-check", MUTILATED, [("set", "applications[0].outcome", "invalid_transform")], "unsupported-outcome"),
    ("duplicate-obligation-check", MUTILATED, [("set", "applications[0].obligation_checks[1].obligation_id", "invariant-closed-predicate#OB1")], "duplicate-id"),
    # Composition and graph structure.
    ("chained-step-needs-interface-check", BOUNDARY, [("set", "applications[1].interface_check", None)], "missing-interface-check"),
    ("interface-check-key-required", BOUNDARY, [("del", "applications[0].interface_check")], "missing-field"),
    ("unknown-input-state", MUTILATED, [("set", "applications[0].input_state_ref", "PS-9")], "unknown-state-ref"),
    ("unknown-root-state", MUTILATED, [("set", "root_state", "PS-9")], "unknown-state-ref"),
    ("application-cycle", BOUNDARY, [("set", "applications[1].output_state_ref", "PS-0")], "cycle"),
    ("root-cannot-be-produced", BOUNDARY, [("set", "applications[1].output_state_ref", "PS-0")], "invalid-root"),
    ("one-producer-per-state", BOUNDARY, [("set", "applications[1].output_state_ref", "PS-1")], "multiple-producers"),
    ("application-must-change-state", MUTILATED, [("set", "applications[0].output_state_ref", "PS-0")], "unchanged-state"),
    ("success-needs-an-output-state", MUTILATED, [("set", "applications[0].output_state_ref", None)], "missing-output-state"),
    ("duplicate-application-id", BOUNDARY, [("set", "applications[1].application_id", "APP-1")], "duplicate-id"),
    ("duplicate-state-id", BOUNDARY, [("set", "problem_states[1].problem_state_id", "PS-0")], "duplicate-id"),
    ("assumptions-must-be-a-list", MUTILATED, [("set", "applications[0].assumptions_introduced", "none")], "invalid-field"),
    # Episode-level claims.
    ("solved-needs-a-solved-final-step", BOUNDARY, [("set", "terminal.claim", "solved")], "unsupported-claim"),
    ("solved-needs-a-state", MUTILATED, [("set", "terminal.state_ref", None)], "unsupported-claim"),
    ("terminal-state-ref-must-be-a-state-id", MUTILATED, [("set", "terminal.state_ref", ["PS-1"])], "unknown-state-ref"),
    ("unhashable-outcome-is-reported-not-fatal", MUTILATED, [("set", "applications[0].outcome", ["solved"])], "invalid-field"),
    ("recorded-episode-needs-measurements", MUTILATED, [("set", "status", "recorded")], "missing-measurement"),
    ("bad-episode-status", MUTILATED, [("set", "status", "anecdotal")], "invalid-field"),
    ("episode-needs-an-epistemic-note", MUTILATED, [("del", "epistemic_note")], "missing-field"),
    ("episode-id-format", MUTILATED, [("set", "episode_id", "ep-1")], "invalid-id"),
]


@pytest.mark.parametrize(("case", "suffix", "ops", "code"), EPISODE_CASES, ids=[c[0] for c in EPISODE_CASES])
def test_episode_defects_are_reported(case: str, suffix: str, ops: list[tuple], code: str) -> None:
    issues = validate_documents(_edit(_library(), suffix, ops), None)
    assert code in _codes(issues), [i.render() for i in issues]


def test_a_solved_claim_needs_every_step_on_the_chain_to_have_succeeded() -> None:
    # The final step is `solved`, but an earlier step on the path from the root had no effect.
    docs = _edit(
        _library(), BOUNDARY,
        [
            ("set", "applications[0].outcome", "no_effect"),
            ("set", "applications[1].outcome", "solved"),
            ("set", "terminal.claim", "solved"),
        ],
    )
    messages = [i.message for i in validate_documents(docs, None) if i.code == "unsupported-claim"]
    assert any("on the chain has outcome 'no_effect'" in m for m in messages), messages


def test_off_trigger_use_is_recordable_with_a_rationale() -> None:
    docs = _edit(
        _library(), MUTILATED,
        [("set", "applications[0].trigger_evidence", []), ("set", "applications[0].off_trigger_rationale", "Tried off-trigger to probe how narrow the trigger is.")],
    )
    assert validate_documents(docs, None) == []


def test_a_failed_obligation_is_recordable_as_an_invalid_transform() -> None:
    docs = _edit(
        _library(), MUTILATED,
        [
            ("set", "applications[0].obligation_checks[3].status", "failed"),
            ("set", "applications[0].outcome", "invalid_transform"),
            ("set", "applications[0].output_state_ref", None),
            ("pop", "problem_states", 1),  # the output state no longer exists, so drop it rather than orphan it
            ("set", "terminal", {"state_ref": None, "claim": "unsolved"}),
        ],
    )
    assert validate_documents(docs, None) == []


def test_stale_card_version_warns_instead_of_failing() -> None:
    docs = _edit(_library(), CONSERVED, [("set", "version", 2)])
    issues = validate_documents(docs, None)
    assert _codes(issues) == set()
    assert "stale-card-version" in _codes(issues, "warning")


def test_unreachable_state_is_flagged_as_a_warning() -> None:
    extra = {
        "problem_state_id": "PS-9", "title": "Unattached", "statement": "s", "goal": "g",
        "features": [], "absent_features": [],
    }
    docs = _edit(_library(), BOUNDARY, [("append", "problem_states", extra)])
    issues = validate_documents(docs, None)
    assert _codes(issues) == set()
    assert "orphan-state" in _codes(issues, "warning")


def test_recorded_episode_with_measurements_validates() -> None:
    docs = _edit(
        _library(), MUTILATED,
        [("set", "status", "recorded"), ("set", "applications[0].measurement_refs", ["results/run-1.json"])],
    )
    assert validate_documents(docs, None) == []


# --------------------------------------------------------------------------------------------
# Specialization, inheritance, and vocabulary
# --------------------------------------------------------------------------------------------
def test_specialization_inherits_obligations_parent_first() -> None:
    cards = collect_cards(_library())
    parent = [qid for qid, _ in effective_obligations("invariant-closed-predicate", cards)]
    child = [qid for qid, _ in effective_obligations("invariant-conserved-quantity", cards)]
    assert parent == [f"invariant-closed-predicate#OB{n}" for n in (1, 2, 3, 4)]
    assert child == [*parent, "invariant-conserved-quantity#OB1"]
    assert specialization_depth("invariant-closed-predicate", cards) == 0
    assert specialization_depth("invariant-monotone-potential", cards) == 1
    assert ancestors("invariant-monotone-potential", cards) == {"invariant-closed-predicate"}
    assert ancestors("invariant-closed-predicate", cards) == set()


def test_effective_obligations_tolerate_cycles_and_unknown_cards() -> None:
    cards = {
        "a": {"obligations": [{"id": "OB1", "text": "x"}], "relations": [{"type": "specializes", "target": "b"}]},
        "b": {"obligations": [{"id": "OB1", "text": "y"}], "relations": [{"type": "specializes", "target": "a"}]},
    }
    assert [q for q, _ in effective_obligations("a", cards)] == ["b#OB1", "a#OB1"]
    assert effective_obligations("missing", cards) == []
    assert specialization_depth("a", cards) >= 0


VOCAB_CASES = [
    ("duplicate-feature-id", [("append", "features", {"id": "strategic_actors", "label": "l", "description": "d", "diagnostic_question": "q", "derived_from_family": "game"})], "duplicate-id"),
    ("unknown-source-family", [("set", "features[0].derived_from_family", "magic")], "unknown-family"),
    ("missing-diagnostic-question", [("del", "features[0].diagnostic_question")], "missing-field"),
    ("bad-feature-id", [("set", "features[0].id", "Bad-Feature")], "invalid-id"),
]


@pytest.mark.parametrize(("case", "ops", "code"), VOCAB_CASES, ids=[c[0] for c in VOCAB_CASES])
def test_vocabulary_defects_are_reported(case: str, ops: list[tuple], code: str) -> None:
    issues = validate_documents(_edit(_library(), "structural_features.yaml", ops), None)
    assert code in _codes(issues), [i.render() for i in issues]


def test_family_registry_duplicates_are_reported() -> None:
    docs = _edit(_library(), "strategy_families.yaml", [("set", "families[1].id", "representation")])
    assert "duplicate-id" in _codes(validate_documents(docs, None))


# --------------------------------------------------------------------------------------------
# Documentation that carries machine-checkable claims
# --------------------------------------------------------------------------------------------
def test_the_problem_state_template_in_the_strategies_readme_is_valid() -> None:
    text = (PROJECT_ROOT / "strategies" / "README.md").read_text(encoding="utf-8")
    match = re.search(r"```yaml\n(ir_kind: problem_state\n.*?)```", text, re.S)
    assert match, "the README no longer contains a problem_state template"
    template = yaml.safe_load(match.group(1))
    issues = validate_documents(_with_state(_library(), template), None)
    assert _codes(issues) == set(), [i.render() for i in issues]
    assert _codes(issues, "warning") == set()


def test_the_readme_coverage_claims_match_the_library() -> None:
    text = (PROJECT_ROOT / "strategies" / "README.md").read_text(encoding="utf-8")
    docs = _library()
    cards = [d.data for d in docs if d.data.get("ir_kind") == "strategy_card"]
    registry = next(d.data for d in docs if "families" in d.data)
    families = {f["id"] for f in registry["families"]}
    covered = {c["family"] for c in cards}
    used = {f for c in cards for t in c["trigger"]["structural_conditions"] for f in t["requires_features"]}
    vocabulary = {f["id"] for d in docs if d.data.get("ir_kind") == "feature_vocabulary" for f in d.data["features"]}
    assert f"**{len(cards)} cards cover {len(covered)} of the {len(families)} families.**" in text
    for family in sorted(families - covered):
        assert f"`{family}`" in text
    assert f"**{len(vocabulary - used)} of the {len(vocabulary)} vocabulary features are used by no card trigger yet:**" in text
    for feature in sorted(vocabulary - used):
        assert f"`{feature}`" in text
    assert all(c["status"] == "candidate" and c["provenance"]["review_status"] == "unreviewed" for c in cards)  # the README's headline claim


# --------------------------------------------------------------------------------------------
# Loading, kinds, and the CLI
# --------------------------------------------------------------------------------------------
def test_missing_or_unknown_kind_is_reported() -> None:
    no_kind = Document("x.yaml", {"strategy_id": "x"})
    wrong_kind = Document("y.yaml", {"ir_kind": "strategy_cardx"})
    not_a_mapping = Document("z.yaml", ["a", "b"])
    issues = validate_documents([*_library(), no_kind, wrong_kind, not_a_mapping], None)
    assert {i.where for i in issues if i.code == "unknown-kind"} == {"x.yaml", "y.yaml", "z.yaml"}


def test_cards_without_a_vocabulary_or_registry_are_reported() -> None:
    cards_only = [d for d in _library() if d.data.get("ir_kind") == "strategy_card"]
    codes = _codes(validate_documents(cards_only, None))
    assert {"no-vocabulary", "no-family-registry"} <= codes
    assert "unknown-feature" not in codes and "unknown-family" not in codes  # no secondary noise


def test_load_documents_reports_bad_yaml_and_missing_paths(tmp_path: Path) -> None:
    bad = tmp_path / "bad.yaml"
    bad.write_text("key: [unclosed\n", encoding="utf-8")
    good = tmp_path / "sub" / "good.yml"
    good.parent.mkdir()
    good.write_text("a: 1\n", encoding="utf-8")
    docs, problems = load_documents([tmp_path, tmp_path / "nope.yaml", good], tmp_path)
    assert [d.where for d in docs] == ["sub/good.yml"]  # directories are searched; the same file is not loaded twice
    assert {(p.where, p.code) for p in problems} == {("bad.yaml", "yaml-parse"), ("nope.yaml", "missing-path")}


def _make_root(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    (root / "research_protocol").mkdir(parents=True)
    for name in ("strategy_families.yaml", "structural_features.yaml", "strategy_ir.md", "protocol.md"):
        shutil.copy(PROJECT_ROOT / "research_protocol" / name, root / "research_protocol" / name)
    shutil.copytree(PROJECT_ROOT / "strategies", root / "strategies")
    for rel in (
        "mission-01/claim_set.md",
        "mission-01/reviews/REV-01_methodological_review.md",
        "mission-01/falsification/falsification_results.json",
    ):
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(PROJECT_ROOT / rel, root / rel)
    return root


def test_cli_passes_on_a_clean_tree(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--root", str(_make_root(tmp_path))]) == 0
    out = capsys.readouterr().out
    assert "documents=12 errors=0 warnings=0 -> ok" in out
    assert "does not show that a strategy works" in out


def test_cli_fails_and_names_the_defect(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    root = _make_root(tmp_path)
    card = root / "strategies" / "cards" / CONSERVED
    card.write_text(card.read_text(encoding="utf-8").replace("status: candidate", "status: retired", 1), encoding="utf-8")
    assert main(["--root", str(root)]) == 1
    out = capsys.readouterr().out
    assert "[unreviewed-promotion]" in out and "-> FAIL" in out


def test_cli_strict_mode_turns_warnings_into_failures(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    root = _make_root(tmp_path)
    card = root / "strategies" / "cards" / CONSERVED
    card.write_text(card.read_text(encoding="utf-8") + "notes: a stray field\n", encoding="utf-8")
    assert main(["--root", str(root)]) == 0
    assert "[unknown-field]" in capsys.readouterr().out
    assert main(["--root", str(root), "--strict"]) == 1


def test_cli_validates_extra_paths_against_the_library(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    root = _make_root(tmp_path)
    state = root / "mission-x" / "problem_state.yaml"
    state.parent.mkdir()
    doc = _valid_state()
    state.write_text(json.dumps(doc), encoding="utf-8")  # JSON is valid YAML
    assert main(["--root", str(root), str(state)]) == 0
    assert "documents=13" in capsys.readouterr().out
    doc["features"][0]["feature"] = "not_in_vocabulary"
    state.write_text(json.dumps(doc), encoding="utf-8")
    assert main(["--root", str(root), str(state)]) == 1
    assert "[unknown-feature]" in capsys.readouterr().out


def test_cli_json_report_is_machine_readable(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--root", str(_make_root(tmp_path)), "--json"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report == {"documents": 12, "errors": 0, "warnings": 0, "issues": []}
