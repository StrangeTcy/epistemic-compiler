from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Callable

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
CARD_COUNT = len(list((PROJECT_ROOT / "strategies" / "cards").glob("*.yaml")))  # every card file must be accounted for

from scripts.retrieve_strategies import (  # noqa: E402
    MANIFEST_NAME,
    PACK_NAME,
    Library,
    RetrievalError,
    assess_card,
    describe_features,
    load_library,
    main,
    retrieve_strategies,
)

MUTILATED = PROJECT_ROOT / "strategies" / "examples" / "mutilated-board.episode.yaml"
BOUNDARY = PROJECT_ROOT / "strategies" / "examples" / "boundary-contract.episode.yaml"
REACH = "transition_system_reachability_question"
CONSERVED_FEATURE = "candidate_conserved_quantity_suspected"


# --------------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------------
def _card(conditions: list[list[str]], *, exclusions: list[list[str]] | None = None, parent: str | None = None) -> dict[str, Any]:
    return {
        "trigger": {
            "structural_conditions": [
                {"id": f"TC{i}", "text": f"condition {i}", "requires_features": feats} for i, feats in enumerate(conditions, start=1)
            ],
            "exclusion_conditions": [
                {"id": f"XC{i}", "text": f"exclusion {i}", "excluded_by_features": feats} for i, feats in enumerate(exclusions or [], start=1)
            ],
        },
        "relations": [{"type": "specializes", "target": parent}] if parent else [],
    }


def _assess(card: dict[str, Any], present: set[str], absent: set[str] = frozenset(), cards: dict[str, Any] | None = None, sid: str = "card"):  # type: ignore[assignment]
    return assess_card(sid, card, cards or {sid: card}, set(present), set(absent))


def _state_doc(present: tuple[str, ...] = (REACH,), absent: tuple[str, ...] = ()) -> dict[str, Any]:
    return {
        "ir_kind": "problem_state",
        "schema_version": "0.2",
        "problem_state_id": "PS-test",
        "title": "A test problem",
        "statement": "Can the target be reached?",
        "goal": "Decide.",
        "features": [{"feature": f, "evidence": f"evidence for {f}", "confidence": "high", "asserted_by": "human"} for f in present],
        "absent_features": [{"feature": f, "evidence": f"{f} does not hold here", "asserted_by": "human"} for f in absent],
    }


def _write_yaml(path: Path, data: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=10_000), encoding="utf-8")
    return path


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
        "knowledge/nodes.yaml",  # cited by the game-family cards' source_refs
    ):
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(PROJECT_ROOT / rel, root / rel)
    return root


def _edit_card(root: Path, name: str, mutate: Callable[[dict[str, Any]], None]) -> None:
    path = root / "strategies" / "cards" / f"{name}.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    mutate(data)
    _write_yaml(path, data)


def _ids(entries: list[dict[str, Any]]) -> list[str]:
    return [e["strategy_id"] for e in entries]


def _tree_hash(root: Path) -> dict[str, str]:
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob("*")) if p.is_file()}


# --------------------------------------------------------------------------------------------
# Three-valued matching, on synthetic cards
# --------------------------------------------------------------------------------------------
def test_a_condition_is_satisfied_only_when_every_required_feature_is_declared_present() -> None:
    card = _card([["a", "b"]])
    assert _assess(card, {"a", "b"}).kind == "matched"
    assert _assess(card, {"a"}).kind == "open"
    assert _assess(card, set()).kind == "none"


def test_unknown_is_not_absent_so_unknown_features_leave_a_card_open_rather_than_blocked() -> None:
    open_result = _assess(_card([["a", "b"]]), {"a"})
    (condition,) = open_result.open
    assert condition.present == ("a",) and condition.unknown == ("b",) and condition.absent == ()
    assert open_result.blocked == ()


def test_a_feature_declared_absent_blocks_the_condition_even_when_the_others_are_present() -> None:
    result = _assess(_card([["a", "b"]]), {"a"}, {"b"})
    assert result.kind == "none"
    assert [c.absent for c in result.blocked] == [("b",)]


def test_any_one_satisfied_condition_is_enough_and_other_conditions_may_be_blocked() -> None:
    card = _card([["a", "b"], ["a"]])
    result = _assess(card, {"a"}, {"b"})
    assert result.kind == "matched"
    assert [c.condition_id for c in result.satisfied] == ["TC2"]


def test_an_exclusion_fires_only_when_all_of_its_features_are_present() -> None:
    card = _card([["a"]], exclusions=[["x", "y"]])
    assert _assess(card, {"a", "x"}).kind == "matched"
    fired = _assess(card, {"a", "x", "y"})
    assert fired.kind == "exclusion_fired" and [x.condition_id for x in fired.fired] == ["XC1"]


def test_an_exclusion_on_a_card_that_does_not_match_does_not_make_it_appear() -> None:
    assert _assess(_card([["a"]], exclusions=[["x"]]), {"x"}).kind == "none"


def test_ordering_prefers_specific_triggers_then_specialization_depth_then_more_conditions_then_id() -> None:
    general = _card([["a"]])
    parent = _card([["a", "b"]])
    child = _card([["a", "b"]], parent="parent")
    cards = {"general": general, "parent": parent, "child": child, "zeta": _card([["a"]]), "alpha": _card([["a"]])}
    present = {"a", "b"}
    keys = {sid: assess_card(sid, card, cards, present, set()).rank_key for sid, card in cards.items()}
    order = sorted(keys, key=keys.__getitem__)
    assert order[:2] == ["child", "parent"]  # two required features beat one; depth breaks the tie
    assert order[2:] == ["alpha", "general", "zeta"]  # equal specificity falls back to the id

    two_conditions = _card([["a"], ["a", "b"]])
    one_condition = _card([["a", "b"]])
    both = {"two": two_conditions, "one": one_condition}
    assert assess_card("two", two_conditions, both, present, set()).rank_key < assess_card("one", one_condition, both, present, set()).rank_key


def test_status_is_not_an_input_to_ordering() -> None:
    plain, supported = _card([["a"]]), {**_card([["a"]]), "status": "supported_in_scope"}
    assert _assess(plain, {"a"}, sid="m").rank_key[:3] == _assess(supported, {"a"}, sid="m").rank_key[:3]


# --------------------------------------------------------------------------------------------
# The shipped library
# --------------------------------------------------------------------------------------------
def test_mutilated_board_matches_the_specialization_first_and_flags_the_open_and_blocked_cards(tmp_path: Path) -> None:
    manifest = retrieve_strategies(MUTILATED, tmp_path / "out")
    assert _ids(manifest["matched"]) == ["invariant-conserved-quantity", "invariant-closed-predicate"]
    assert manifest["matched"][0]["satisfied_conditions"] == ["TC1"]
    assert manifest["matched"][1]["satisfied_conditions"] == ["TC1", "TC3"]
    assert _ids(manifest["open"]) == ["invariant-monotone-potential"]
    assert manifest["open"][0]["open_conditions"] == [
        {"condition_id": "TC1", "present": [REACH], "unknown": ["candidate_monotone_quantity_suspected"]}
    ]
    assert _ids(manifest["blocked_by_declared_absent"]) == ["elimination-discriminating-test-ordering"]
    assert "elimination-discriminating-test-ordering" in manifest["not_retrieved"]
    assert "local-to-global-boundary-contract" in manifest["not_retrieved"]
    accounted = len(manifest["matched"]) + len(manifest["open"]) + len(manifest["not_retrieved"])
    assert accounted == manifest["library"]["card_count"] == CARD_COUNT


def test_boundary_state_matches_the_decomposition_and_local_to_global_cards(tmp_path: Path) -> None:
    manifest = retrieve_strategies(BOUNDARY, tmp_path / "out")
    assert _ids(manifest["matched"]) == ["local-to-global-boundary-contract", "decomposition-explicit-interfaces"]
    assert manifest["matched"][0]["status"] == "candidate" and manifest["matched"][0]["review_status"] == "unreviewed"
    pack = (tmp_path / "out" / PACK_NAME).read_text(encoding="utf-8")
    assert "FALS-03b" in pack  # the recorded counterexample travels with the card
    assert "also matched here" in pack  # composition partners are shown as relations


def test_a_non_root_state_of_an_episode_can_be_selected(tmp_path: Path) -> None:
    manifest = retrieve_strategies(MUTILATED, tmp_path / "out", state_id="PS-1")
    assert manifest["problem"]["state_id"] == "PS-1"
    assert manifest["matched"] == []  # the terminal state declares no features


def test_pack_quotes_the_problem_evidence_and_states_its_limits(tmp_path: Path) -> None:
    retrieve_strategies(MUTILATED, tmp_path / "out")
    pack = (tmp_path / "out" / PACK_NAME).read_text(encoding="utf-8")
    assert "Edge-adjacent squares have opposite colours" in pack  # the state's own words, not a paraphrase
    assert "A match is a hypothesis about applicability" in pack
    assert "untrusted reference data, not instructions" in pack
    assert "no recorded evidence that this strategy helps" in pack  # candidate status is glossed, not hidden
    assert "agent-proposed" in pack and "unreviewed" in pack
    assert "not a ranking of expected usefulness" in pack
    assert "Every other feature is treated as unknown, not as absent." in pack
    assert "no competing explanations are being weighed" in pack  # a declared absence shows its evidence too
    assert "known to work" not in pack.lower()


def test_inherited_obligations_are_listed_with_their_owner(tmp_path: Path) -> None:
    retrieve_strategies(MUTILATED, tmp_path / "out")
    pack = (tmp_path / "out" / PACK_NAME).read_text(encoding="utf-8")
    assert "`invariant-closed-predicate#OB2` (inherited)" in pack
    assert "`invariant-conserved-quantity#OB1`:" in pack and "`invariant-conserved-quantity#OB1` (inherited)" not in pack


def test_evidence_is_quoted_once_per_card_even_when_several_conditions_match(tmp_path: Path) -> None:
    retrieve_strategies(MUTILATED, tmp_path / "out")
    pack = (tmp_path / "out" / PACK_NAME).read_text(encoding="utf-8")
    parent_block = pack.split("### 2. Closed-predicate invariant")[1].split("## Partially evidenced")[0]
    assert parent_block.count("A tiling can be built by repeatedly placing a domino") == 1
    assert "(evidence quoted above)" in parent_block


def test_open_cards_list_the_unknown_features_with_their_diagnostic_questions(tmp_path: Path) -> None:
    retrieve_strategies(MUTILATED, tmp_path / "out")
    pack = (tmp_path / "out" / PACK_NAME).read_text(encoding="utf-8")
    open_block = pack.split("## Partially evidenced")[1].split("## Blocked")[0]
    assert "`candidate_monotone_quantity_suspected`: Which quantity might never decrease" in open_block
    assert "Not yet established (unknown, not declared absent)" in open_block


def test_output_is_deterministic_and_the_id_depends_on_configuration(tmp_path: Path) -> None:
    first = retrieve_strategies(MUTILATED, tmp_path / "a")
    second = retrieve_strategies(MUTILATED, tmp_path / "b")
    for name in (PACK_NAME, MANIFEST_NAME):
        assert (tmp_path / "a" / name).read_bytes() == (tmp_path / "b" / name).read_bytes()
    assert first["retrieval_id"] == second["retrieval_id"]
    assert retrieve_strategies(MUTILATED, tmp_path / "c", max_candidates=1)["retrieval_id"] != first["retrieval_id"]
    assert retrieve_strategies(BOUNDARY, tmp_path / "d")["retrieval_id"] != first["retrieval_id"]


def test_retrieval_writes_only_into_the_output_directory(tmp_path: Path) -> None:
    root = _make_root(tmp_path)
    before = _tree_hash(root)
    retrieve_strategies(root / "strategies" / "examples" / "mutilated-board.episode.yaml", tmp_path / "out", root=root)
    assert _tree_hash(root) == before
    assert sorted(p.name for p in (tmp_path / "out").iterdir()) == sorted([PACK_NAME, MANIFEST_NAME])


def test_max_candidates_expands_only_the_leading_matches_and_lists_the_rest(tmp_path: Path) -> None:
    manifest = retrieve_strategies(MUTILATED, tmp_path / "out", max_candidates=1)
    assert [e["rendered_in_full"] for e in manifest["matched"]] == [True, False]
    pack = (tmp_path / "out" / PACK_NAME).read_text(encoding="utf-8")
    assert "### Further matches, not expanded (1)" in pack
    assert "### 2. Closed-predicate invariant" not in pack
    with pytest.raises(RetrievalError, match="at least 1"):
        retrieve_strategies(MUTILATED, tmp_path / "bad", max_candidates=0)


def test_manifest_records_inputs_and_the_standing_warning(tmp_path: Path) -> None:
    manifest = retrieve_strategies(MUTILATED, tmp_path / "out")
    on_disk = json.loads((tmp_path / "out" / MANIFEST_NAME).read_text(encoding="utf-8"))
    assert on_disk == manifest
    assert manifest["problem"]["declared_present"] == sorted([REACH, CONSERVED_FEATURE])
    assert manifest["problem"]["declared_absent"] == ["competing_hypotheses_remain"]
    assert set(manifest["library"]["file_sha256"]) >= {"research_protocol/structural_features.yaml", "strategies/cards/invariant-conserved-quantity.yaml"}
    assert manifest["pack_sha256"] == hashlib.sha256((tmp_path / "out" / PACK_NAME).read_bytes()).hexdigest()
    assert "No match is not evidence that no strategy applies" in manifest["warning"]
    assert "no automatic selection" in manifest["method"]


# --------------------------------------------------------------------------------------------
# Result buckets, with edited copies of the library
# --------------------------------------------------------------------------------------------
HUMAN_REVIEW = {"review_status": "human_reviewed", "reviewed_by": "reviewer"}


def _standalone(tmp_path: Path, present: tuple[str, ...], absent: tuple[str, ...] = ()) -> Path:
    return _write_yaml(tmp_path / "work" / "problem_state.yaml", _state_doc(present, absent))


def test_retired_cards_are_withheld_unless_asked_for(tmp_path: Path) -> None:
    root = _make_root(tmp_path)
    _edit_card(root, "invariant-conserved-quantity", lambda c: (c.update(status="retired"), c["provenance"].update(HUMAN_REVIEW)))
    problem = _standalone(tmp_path, (REACH, CONSERVED_FEATURE))
    hidden = retrieve_strategies(problem, tmp_path / "a", root=root)
    assert "invariant-conserved-quantity" not in _ids(hidden["matched"])
    assert _ids(hidden["withheld_retired"]) == ["invariant-conserved-quantity"]
    assert "--include-retired" in (tmp_path / "a" / PACK_NAME).read_text(encoding="utf-8")
    shown = retrieve_strategies(problem, tmp_path / "b", root=root, include_retired=True)
    assert "invariant-conserved-quantity" in _ids(shown["matched"]) and shown["withheld_retired"] == []


def test_disconfirmed_cards_get_their_own_section_instead_of_the_candidate_list(tmp_path: Path) -> None:
    root = _make_root(tmp_path)

    def disconfirm(card: dict[str, Any]) -> None:
        card.update(status="disconfirmed_in_scope")
        card["provenance"].update(HUMAN_REVIEW)
        card["counterexamples"] = [{"id": "CX1", "ref": "strategies/examples/mutilated-board.episode.yaml", "note": "A recorded failure on a comparable instance."}]

    _edit_card(root, "invariant-conserved-quantity", disconfirm)
    manifest = retrieve_strategies(_standalone(tmp_path, (REACH, CONSERVED_FEATURE)), tmp_path / "out", root=root)
    assert _ids(manifest["disconfirmed_in_scope"]) == ["invariant-conserved-quantity"]
    assert "invariant-conserved-quantity" not in _ids(manifest["matched"])
    pack = (tmp_path / "out" / PACK_NAME).read_text(encoding="utf-8")
    assert "## Recorded disconfirmation in scope (1)" in pack and "A recorded failure on a comparable instance." in pack


def test_a_fired_exclusion_moves_the_card_out_of_the_recommendations(tmp_path: Path) -> None:
    root = _make_root(tmp_path)
    exclusion = {"id": "XC1", "text": "A cheap discriminating test already settles the question.", "excluded_by_features": ["cheap_discriminating_test_available"]}
    _edit_card(root, "invariant-conserved-quantity", lambda c: c["trigger"].update(exclusion_conditions=[exclusion]))
    plain = retrieve_strategies(_standalone(tmp_path, (REACH, CONSERVED_FEATURE)), tmp_path / "a", root=root)
    assert "invariant-conserved-quantity" in _ids(plain["matched"])
    fired = retrieve_strategies(_standalone(tmp_path, (REACH, CONSERVED_FEATURE, "cheap_discriminating_test_available")), tmp_path / "b", root=root)
    assert _ids(fired["exclusion_fired"]) == ["invariant-conserved-quantity"]
    assert "invariant-conserved-quantity" not in _ids(fired["matched"])
    assert "## Not recommended" in (tmp_path / "b" / PACK_NAME).read_text(encoding="utf-8")


def test_a_standalone_state_without_features_returns_nothing_and_says_why(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    problem = _standalone(tmp_path, ())
    assert main(["--problem", str(problem), "--out", str(tmp_path / "out")]) == 0
    assert "matched=0" in capsys.readouterr().out
    pack = (tmp_path / "out" / PACK_NAME).read_text(encoding="utf-8")
    assert "No features are declared present, so nothing can match" in pack
    assert "No card has a trigger condition fully satisfied" in pack and "not evidence that no strategy applies" in pack
    assert "no features declared" in pack  # the validator's warning is passed along


def test_declared_features_that_no_card_uses_are_reported_as_a_coverage_gap(tmp_path: Path) -> None:
    manifest = retrieve_strategies(_standalone(tmp_path, ("strategic_actors", REACH)), tmp_path / "out")
    assert manifest["declared_features_no_card_uses"] == ["strategic_actors"]
    assert "The library has nothing to offer on those" in (tmp_path / "out" / PACK_NAME).read_text(encoding="utf-8")
    assert "asymmetry" in manifest["families_without_cards"]  # a family that still has no card


# --------------------------------------------------------------------------------------------
# Failing closed
# --------------------------------------------------------------------------------------------
def test_an_invalid_library_stops_retrieval_and_writes_nothing(tmp_path: Path) -> None:
    root = _make_root(tmp_path)
    _edit_card(root, "invariant-closed-predicate", lambda c: c.pop("obligations"))
    out = tmp_path / "out"
    with pytest.raises(RetrievalError) as caught:
        retrieve_strategies(root / "strategies" / "examples" / "mutilated-board.episode.yaml", out, root=root)
    assert "missing-field" in {i.code for i in caught.value.issues}
    assert not out.exists()


def test_cli_reports_an_invalid_library_on_stderr_with_exit_code_one(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    root = _make_root(tmp_path)
    _edit_card(root, "invariant-closed-predicate", lambda c: c.pop("obligations"))
    code = main(["--root", str(root), "--problem", str(root / "strategies/examples/mutilated-board.episode.yaml"), "--out", str(tmp_path / "out")])
    captured = capsys.readouterr()
    assert code == 1 and captured.out == ""
    assert "validation error" in captured.err and "[missing-field]" in captured.err
    assert not (tmp_path / "out").exists()


def test_an_invalid_problem_state_is_rejected_with_the_validator_issue(tmp_path: Path) -> None:
    doc = _state_doc()
    doc["features"][0]["feature"] = "not_in_the_vocabulary"
    with pytest.raises(RetrievalError) as caught:
        retrieve_strategies(_write_yaml(tmp_path / "p.yaml", doc), tmp_path / "out")
    assert "unknown-feature" in {i.code for i in caught.value.issues}
    doc = _state_doc()
    del doc["features"][0]["evidence"]
    with pytest.raises(RetrievalError) as caught:
        retrieve_strategies(_write_yaml(tmp_path / "q.yaml", doc), tmp_path / "out")
    assert "missing-field" in {i.code for i in caught.value.issues}  # a feature label without evidence is not accepted
    assert not (tmp_path / "out").exists()


def test_only_the_selected_state_needs_to_be_valid(tmp_path: Path) -> None:
    episode = yaml.safe_load(MUTILATED.read_text(encoding="utf-8"))
    episode["problem_states"][1]["goal"] = ""  # PS-1 is broken, PS-0 is untouched
    path = _write_yaml(tmp_path / "ep.yaml", episode)
    assert _ids(retrieve_strategies(path, tmp_path / "ok")["matched"])
    with pytest.raises(RetrievalError):
        retrieve_strategies(path, tmp_path / "bad", state_id="PS-1")


@pytest.mark.parametrize(
    ("builder", "state_id", "message"),
    [
        (lambda tmp: tmp / "missing.yaml", None, "not found"),
        (lambda tmp: PROJECT_ROOT / "strategies" / "cards" / "meta-unfix-assumptions.yaml", None, "expected a `problem_state` or `episode`"),
        (lambda tmp: MUTILATED, "PS-404", "no problem state 'PS-404'"),
        (lambda tmp: _write_yaml(tmp / "s.yaml", _state_doc()), "PS-other", "not 'PS-other'"),
    ],
    ids=["missing-file", "wrong-document-kind", "unknown-state-in-episode", "state-id-mismatch"],
)
def test_unusable_problem_inputs_raise_a_clear_error(tmp_path: Path, builder: Callable[[Path], Path], state_id: str | None, message: str) -> None:
    with pytest.raises(RetrievalError, match=message):
        retrieve_strategies(builder(tmp_path), tmp_path / "out", state_id=state_id)
    assert not (tmp_path / "out").exists()


# --------------------------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------------------------
def test_cli_writes_the_pack_and_prints_a_summary(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--problem", str(MUTILATED), "--out", str(tmp_path / "out")]) == 0
    out = capsys.readouterr().out
    assert "matched=2 open=1 exclusion_fired=0" in out
    assert (tmp_path / "out" / PACK_NAME).is_file() and (tmp_path / "out" / MANIFEST_NAME).is_file()


def test_cli_requires_problem_and_out_unless_listing_features() -> None:
    with pytest.raises(SystemExit) as caught:
        main(["--out", "somewhere"])
    assert caught.value.code == 2


def test_list_features_prints_every_feature_with_its_question_and_the_unused_count(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--list-features"]) == 0
    out = capsys.readouterr().out
    library = load_library()
    for feature in library.features:
        assert feature in out
    assert f"[strategies] {len(library.features)} features;" in out and "used by no card trigger yet" in out
    assert "Which quantity might every allowed operation leave unchanged" in out


def test_describe_features_counts_trigger_and_exclusion_use_on_a_synthetic_library() -> None:
    library = Library(
        cards={"c": _card([["a"], ["a", "b"]], exclusions=[["b"]])},
        features={
            "a": {"derived_from_family": "fam", "diagnostic_question": "Is it a?"},
            "b": {"derived_from_family": "fam", "diagnostic_question": "Is it b?"},
            "z": {"derived_from_family": "other", "diagnostic_question": "Is it z?"},
        },
        families=("fam", "other"),
        file_sha256={},
        warnings=(),
    )
    lines = describe_features(library)
    assert "a  [fam]  trigger of 1 card(s), exclusion of 0" in lines
    assert "b  [fam]  trigger of 1 card(s), exclusion of 1" in lines
    assert "z  [other]  trigger of 0 card(s), exclusion of 0" in lines
    assert lines[-1] == "[strategies] 3 features; 1 used by no card trigger yet"
