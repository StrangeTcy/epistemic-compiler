#!/usr/bin/env python3
"""Validate Strategy IR artifacts: strategy cards, problem states, episodes, vocabularies.

Scope: structure and record-keeping consistency only. The checks cover required fields,
controlled vocabularies, cross-references, the status/review policy, specialization bindings and
obligation inheritance, and the internal consistency of application records. A document that
passes is well-formed; it is not thereby true, and a card that passes is not thereby effective.
Whether a declared feature holds, whether obligations are adequate, and whether a transformation
was carried out correctly remain human or experimental judgments.

Nothing here dispatches, selects, applies, or promotes a strategy.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = "0.2"

KIND_CARD = "strategy_card"
KIND_STATE = "problem_state"
KIND_EPISODE = "episode"
KIND_VOCAB = "feature_vocabulary"
KIND_FAMILIES = "family_registry"
KINDS = (KIND_CARD, KIND_STATE, KIND_EPISODE, KIND_VOCAB, KIND_FAMILIES)

CARD_STATUSES = ("candidate", "under_test", "supported_in_scope", "disconfirmed_in_scope", "retired")
ORIGINS = ("source-backed", "episode-derived", "user-proposed", "agent-proposed")
REVIEW_STATUSES = ("unreviewed", "human_reviewed")
EXEMPLAR_KINDS = ("textbook_illustration", "bounded_pilot", "recorded_episode")
RELATION_TYPES = ("specializes", "composes_with", "alternative_to", "conflicts_with")
ATTEMPT_OUTCOMES = ("found_counterexample", "none_found", "not_run")
CONFIDENCES = ("low", "moderate", "high")
OUTCOMES = ("solved", "reduced", "no_effect", "invalid_transform", "inconclusive")
SUCCESS_OUTCOMES = frozenset({"solved", "reduced"})
CHECK_STATUSES = ("passed", "failed", "not_checked")
EPISODE_STATUSES = ("illustrative", "recorded")
TERMINAL_CLAIMS = ("solved", "unsolved", "abandoned")

STRATEGY_ID = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
SNAKE_ID = re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$")
STATE_ID = re.compile(r"^PS-[A-Za-z0-9][A-Za-z0-9._-]*$")
EPISODE_ID = re.compile(r"^EP-[A-Za-z0-9][A-Za-z0-9._-]*$")
APPLICATION_ID = re.compile(r"^APP-[A-Za-z0-9][A-Za-z0-9._-]*$")
TC_ID, XC_ID = re.compile(r"^TC\d+$"), re.compile(r"^XC\d+$")
OB_ID, FM_ID = re.compile(r"^OB\d+$"), re.compile(r"^FM\d+$")
EX_ID, CX_ID = re.compile(r"^EX\d+$"), re.compile(r"^CX\d+$")

CARD_KEYS = {
    "ir_kind", "schema_version", "strategy_id", "version", "name", "family", "status", "scope",
    "parameters", "trigger", "transformation", "expected_effect", "obligations", "failure_modes",
    "validation", "exemplars", "counterexamples", "relations", "provenance",
}
STATE_KEYS = {"problem_state_id", "title", "statement", "goal", "features", "absent_features", "notes"}
APPLICATION_KEYS = {
    "application_id", "strategy_ref", "input_state_ref", "output_state_ref", "trigger_evidence",
    "off_trigger_rationale", "selection_rationale", "transformation_record", "assumptions_introduced",
    "information_discarded", "interface_check", "obligation_checks", "outcome", "measurement_refs",
    "review_status",
}
STANDARD_PATHS = ("research_protocol/strategy_families.yaml", "research_protocol/structural_features.yaml", "strategies")


# --------------------------------------------------------------------------------------------
# Issues and documents
# --------------------------------------------------------------------------------------------
@dataclass(frozen=True, order=True)
class Issue:
    where: str
    severity: str  # "error" | "warning"
    code: str
    message: str

    def render(self) -> str:
        return f"{self.where}: {self.severity} [{self.code}] {self.message}"


@dataclass(frozen=True)
class Document:
    where: str
    data: Any
    path: Path | None = None


def document_kind(data: Any) -> str | None:
    """The IR kind of a parsed YAML document, or None when it cannot be determined."""
    if not isinstance(data, dict):
        return None
    kind = data.get("ir_kind")
    if isinstance(kind, str):
        return kind
    if "registry_kind" in data and "families" in data:  # legacy 0.1 family registry
        return KIND_FAMILIES
    return None


def _display(path: Path, root: Path | None) -> str:
    if root is not None:
        try:
            return path.resolve().relative_to(root.resolve()).as_posix()
        except ValueError:
            pass
    return path.as_posix()


def load_documents(paths: Iterable[Path], root: Path | None = None) -> tuple[list[Document], list[Issue]]:
    """Parse YAML files (directories are searched recursively); problems become Issues."""
    docs: list[Document] = []
    problems: list[Issue] = []
    seen: set[Path] = set()
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            files = sorted([*path.rglob("*.yaml"), *path.rglob("*.yml")])
        elif path.is_file():
            files = [path]
        else:
            problems.append(Issue(_display(path, root), "error", "missing-path", "path does not exist"))
            continue
        for file in files:
            if file.resolve() in seen:
                continue
            seen.add(file.resolve())
            where = _display(file, root)
            try:
                data = yaml.safe_load(file.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
                problems.append(Issue(where, "error", "yaml-parse", " ".join(str(exc).split())))
                continue
            docs.append(Document(where, data, file))
    return docs, problems


# --------------------------------------------------------------------------------------------
# Small shared helpers (also used by retrieve_strategies.py)
# --------------------------------------------------------------------------------------------
def _is_text(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def _is_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _items(value: Any) -> list[dict[str, Any]]:
    """Mapping items of a list; any other shape yields an empty list (shape errors are reported elsewhere)."""
    return [item for item in value if isinstance(item, dict)] if isinstance(value, list) else []


def trigger_conditions(card: dict[str, Any]) -> list[dict[str, Any]]:
    trigger = card.get("trigger")
    return _items(trigger.get("structural_conditions")) if isinstance(trigger, dict) else []


def condition_features(condition: dict[str, Any], key: str = "requires_features") -> list[str]:
    """The feature ids a trigger or exclusion condition refers to (empty if malformed)."""
    values = condition.get(key)
    return [v for v in values if isinstance(v, str)] if isinstance(values, list) else []


def exclusion_conditions(card: dict[str, Any]) -> list[dict[str, Any]]:
    trigger = card.get("trigger")
    return _items(trigger.get("exclusion_conditions")) if isinstance(trigger, dict) else []


def state_features(state: dict[str, Any]) -> tuple[set[str], set[str]]:
    """(declared-present, declared-absent) feature ids of a problem state."""
    present = {f["feature"] for f in _items(state.get("features")) if isinstance(f.get("feature"), str)}
    absent = {f["feature"] for f in _items(state.get("absent_features")) if isinstance(f.get("feature"), str)}
    return present, absent


def card_parents(card: dict[str, Any]) -> list[str]:
    """Strategy ids that this card specializes."""
    return [
        rel["target"] for rel in _items(card.get("relations"))
        if rel.get("type") == "specializes" and isinstance(rel.get("target"), str)
    ]


def ancestors(strategy_id: str, cards: dict[str, dict[str, Any]]) -> set[str]:
    """All strategy ids that the given card (transitively) specializes."""
    found: set[str] = set()
    stack = [strategy_id]
    while stack:
        card = cards.get(stack.pop())
        for parent in card_parents(card) if card else []:
            if parent not in found:
                found.add(parent)
                stack.append(parent)
    return found


def specialization_depth(strategy_id: str, cards: dict[str, dict[str, Any]], _stack: tuple[str, ...] = ()) -> int:
    """Length of the longest chain of `specializes` links above the card (0 for a root)."""
    card = cards.get(strategy_id)
    if card is None or strategy_id in _stack:
        return 0
    parents = [p for p in card_parents(card) if p in cards]
    if not parents:
        return 0
    return 1 + max(specialization_depth(p, cards, _stack + (strategy_id,)) for p in parents)


def qualify(strategy_id: str, obligation_id: str) -> str:
    """Obligation ids are `<strategy_id>#<OBn>`; a bare `OBn` refers to the applied card's own obligation."""
    return obligation_id if "#" in obligation_id else f"{strategy_id}#{obligation_id}"


def effective_obligations(strategy_id: str, cards: dict[str, dict[str, Any]], _stack: tuple[str, ...] = ()) -> list[tuple[str, str]]:
    """(qualified id, text) of a card's own obligations plus those inherited from what it specializes."""
    card = cards.get(strategy_id)
    if card is None or strategy_id in _stack:
        return []
    out: list[tuple[str, str]] = []
    known: set[str] = set()
    for parent in card_parents(card):
        for qid, text in effective_obligations(parent, cards, _stack + (strategy_id,)):
            if qid not in known:
                known.add(qid)
                out.append((qid, text))
    for ob in _items(card.get("obligations")):
        if isinstance(ob.get("id"), str):
            qid = f"{strategy_id}#{ob['id']}"
            if qid not in known:
                known.add(qid)
                out.append((qid, ob.get("text", "") if isinstance(ob.get("text"), str) else ""))
    return out


def collect_cards(documents: Iterable[Document]) -> dict[str, dict[str, Any]]:
    """Strategy cards by id (first occurrence wins; duplicates are reported by validation)."""
    cards: dict[str, dict[str, Any]] = {}
    for doc in documents:
        if document_kind(doc.data) == KIND_CARD and isinstance(doc.data.get("strategy_id"), str):
            cards.setdefault(doc.data["strategy_id"], doc.data)
    return cards


def collect_features(documents: Iterable[Document]) -> dict[str, dict[str, Any]]:
    features: dict[str, dict[str, Any]] = {}
    for doc in documents:
        if document_kind(doc.data) == KIND_VOCAB:
            for feature in _items(doc.data.get("features")):
                if isinstance(feature.get("id"), str):
                    features.setdefault(feature["id"], feature)
    return features


# --------------------------------------------------------------------------------------------
# Issue sink with typed field accessors
# --------------------------------------------------------------------------------------------
class _Sink:
    def __init__(self) -> None:
        self.issues: list[Issue] = []

    def error(self, where: str, code: str, message: str) -> None:
        self.issues.append(Issue(where, "error", code, message))

    def warn(self, where: str, code: str, message: str) -> None:
        self.issues.append(Issue(where, "warning", code, message))

    def text(self, where: str, obj: dict[str, Any], key: str) -> str | None:
        if key not in obj:
            self.error(where, "missing-field", f"missing required field `{key}`")
            return None
        if not _is_text(obj[key]):
            self.error(where, "invalid-field", f"`{key}` must be a non-empty string")
            return None
        return obj[key]

    def integer(self, where: str, obj: dict[str, Any], key: str) -> int | None:
        if key not in obj:
            self.error(where, "missing-field", f"missing required field `{key}`")
            return None
        if not _is_int(obj[key]) or obj[key] < 1:
            self.error(where, "invalid-field", f"`{key}` must be an integer >= 1")
            return None
        return obj[key]

    def choice(self, where: str, obj: dict[str, Any], key: str, allowed: Iterable[str]) -> str | None:
        allowed = tuple(allowed)
        if key not in obj:
            self.error(where, "missing-field", f"missing required field `{key}`")
            return None
        if obj[key] not in allowed:
            self.error(where, "invalid-field", f"`{key}` must be one of {', '.join(allowed)}; got {obj[key]!r}")
            return None
        return obj[key]

    def ident(self, where: str, obj: dict[str, Any], key: str, pattern: re.Pattern[str], what: str) -> str | None:
        value = self.text(where, obj, key)
        if value is not None and not pattern.match(value):
            self.error(where, "invalid-id", f"`{key}` {value!r} is not a valid {what}")
            return None
        return value

    def mapping(self, where: str, obj: dict[str, Any], key: str) -> dict[str, Any] | None:
        if key not in obj:
            self.error(where, "missing-field", f"missing required field `{key}`")
            return None
        if not isinstance(obj[key], dict):
            self.error(where, "invalid-field", f"`{key}` must be a mapping")
            return None
        return obj[key]

    def seq(self, where: str, obj: dict[str, Any], key: str, *, non_empty: bool = False) -> list[Any] | None:
        if key not in obj:
            self.error(where, "missing-field", f"missing required field `{key}`")
            return None
        if not isinstance(obj[key], list):
            self.error(where, "invalid-field", f"`{key}` must be a list")
            return None
        if non_empty and not obj[key]:
            self.error(where, "empty-field", f"`{key}` must not be empty")
            return None
        return obj[key]

    def texts(self, where: str, obj: dict[str, Any], key: str, *, non_empty: bool = False) -> list[str] | None:
        values = self.seq(where, obj, key, non_empty=non_empty)
        if values is None:
            return None
        if not all(_is_text(v) for v in values):
            self.error(where, "invalid-field", f"every entry of `{key}` must be a non-empty string")
            return None
        return values

    def unknown_keys(self, where: str, obj: dict[str, Any], allowed: Iterable[str]) -> None:
        allowed = set(allowed)
        for key in sorted(map(str, obj)):
            if key not in allowed:
                self.warn(where, "unknown-field", f"unknown field `{key}` (typo?)")

    def header(self, where: str, doc: dict[str, Any], kind: str) -> None:
        if doc.get("ir_kind") != kind:
            self.error(where, "invalid-field", f"`ir_kind` must be {kind!r}")
        if doc.get("schema_version") != SCHEMA_VERSION:
            self.error(where, "schema-version", f"`schema_version` must be the string {SCHEMA_VERSION!r}")

    def id_text_items(
        self, where: str, obj: dict[str, Any], key: str, pattern: re.Pattern[str], what: str, *, non_empty: bool
    ) -> list[dict[str, Any]]:
        """Validate a list of {id, text} items with unique ids; return the well-formed items."""
        values = self.seq(where, obj, key, non_empty=non_empty)
        good: list[dict[str, Any]] = []
        seen: set[str] = set()
        for i, item in enumerate(values or []):
            iw = f"{where}.{key}[{i}]"
            if not isinstance(item, dict):
                self.error(iw, "invalid-field", "must be a mapping with `id` and `text`")
                continue
            self.unknown_keys(iw, item, {"id", "text"})
            item_id, text = self.ident(iw, item, "id", pattern, what), self.text(iw, item, "text")
            if item_id is None or text is None:
                continue
            if item_id in seen:
                self.error(iw, "duplicate-id", f"duplicate id {item_id!r} in `{key}`")
                continue
            seen.add(item_id)
            good.append(item)
        return good


@dataclass(frozen=True)
class _Ctx:
    families: frozenset[str]
    features: frozenset[str]
    root: Path | None
    registries: dict[str, frozenset[str]]  # display path of a family registry -> its family ids


# --------------------------------------------------------------------------------------------
# Family registry and feature vocabulary
# --------------------------------------------------------------------------------------------
def _validate_families(docs: list[Document], sink: _Sink) -> dict[str, frozenset[str]]:
    registries: dict[str, frozenset[str]] = {}
    seen: set[str] = set()
    for doc in docs:
        w, data = doc.where, doc.data
        ids: set[str] = set()
        families = sink.seq(w, data, "families", non_empty=True)
        for i, fam in enumerate(families or []):
            fw = f"{w}::families[{i}]"
            if not isinstance(fam, dict):
                sink.error(fw, "invalid-field", "must be a mapping")
                continue
            fid = sink.ident(fw, fam, "id", SNAKE_ID, "snake_case id")
            sink.text(fw, fam, "label")
            trigger = sink.mapping(fw, fam, "trigger")
            if trigger is not None:
                sink.texts(f"{fw}.trigger", trigger, "conditions", non_empty=True)
                sink.texts(f"{fw}.trigger", trigger, "questions", non_empty=True)
            if fid is None:
                continue
            if fid in seen:
                sink.error(fw, "duplicate-id", f"family id {fid!r} is defined more than once")
                continue
            seen.add(fid)
            ids.add(fid)
        registries[w] = frozenset(ids)
    return registries


def _validate_vocabulary(docs: list[Document], families: frozenset[str], sink: _Sink) -> frozenset[str]:
    seen: set[str] = set()
    for doc in docs:
        w, data = doc.where, doc.data
        sink.header(w, data, KIND_VOCAB)
        sink.unknown_keys(w, data, {"ir_kind", "schema_version", "status", "provenance", "features"})
        sink.text(w, data, "status")
        for i, feature in enumerate(sink.seq(w, data, "features", non_empty=True) or []):
            fw = f"{w}::features[{i}]"
            if not isinstance(feature, dict):
                sink.error(fw, "invalid-field", "must be a mapping")
                continue
            sink.unknown_keys(fw, feature, {"id", "label", "description", "diagnostic_question", "derived_from_family"})
            fid = sink.ident(fw, feature, "id", SNAKE_ID, "snake_case feature id")
            for key in ("label", "description", "diagnostic_question"):
                sink.text(fw, feature, key)
            family = sink.text(fw, feature, "derived_from_family")
            if family and families and family not in families:
                sink.error(fw, "unknown-family", f"`derived_from_family` {family!r} is not in the family registry")
            if fid is None:
                continue
            if fid in seen:
                sink.error(fw, "duplicate-id", f"feature id {fid!r} is defined more than once")
            seen.add(fid)
    return frozenset(seen)


# --------------------------------------------------------------------------------------------
# Strategy cards
# --------------------------------------------------------------------------------------------
def _check_features(sink: _Sink, where: str, names: list[str] | None, ctx: _Ctx) -> list[str]:
    if names is None:
        return []
    if len(set(names)) != len(names):
        sink.warn(where, "duplicate-feature", "a feature is listed more than once")
    for name in names:
        if ctx.features and name not in ctx.features:
            sink.error(where, "unknown-feature", f"feature {name!r} is not in the feature vocabulary")
    return list(dict.fromkeys(names))


def _check_ref(sink: _Sink, where: str, ref: str, ctx: _Ctx) -> None:
    """Check a repo-relative `path[#fragment]` reference; other reference styles are not checked."""
    base, _, fragment = ref.partition("#")
    if not base or "://" in base:
        return
    if "/" not in base and not re.search(r"\.[A-Za-z0-9]+$", base):
        return
    if base in ctx.registries:
        if fragment and fragment not in ctx.registries[base]:
            sink.error(where, "ref-fragment", f"{ref!r}: {fragment!r} is not a family id in {base}")
        return
    if ctx.root is not None and not (ctx.root / base).exists():
        sink.error(where, "ref-not-found", f"reference {ref!r} does not resolve to a path under the repository root")


def _validate_card(doc: Document, ctx: _Ctx, sink: _Sink) -> dict[str, Any] | None:
    w, card = doc.where, doc.data
    if not isinstance(card, dict):
        sink.error(w, "type", "document must be a mapping")
        return None
    sink.unknown_keys(w, card, CARD_KEYS)
    sink.header(w, card, KIND_CARD)
    sid = sink.ident(w, card, "strategy_id", STRATEGY_ID, "kebab-case strategy id")
    if sid and doc.path is not None and doc.path.stem != sid:
        sink.error(w, "filename", f"file name must match strategy_id ({sid}.yaml)")
    sink.integer(w, card, "version")
    sink.text(w, card, "name")
    family = sink.text(w, card, "family")
    if family and ctx.families and family not in ctx.families:
        sink.error(w, "unknown-family", f"`family` {family!r} is not in the family registry")
    status = sink.choice(w, card, "status", CARD_STATUSES)

    scope = sink.mapping(w, card, "scope")
    if scope is not None:
        sink.unknown_keys(f"{w}::scope", scope, {"problem_classes", "preconditions"})
        sink.texts(f"{w}::scope", scope, "problem_classes", non_empty=True)
        sink.texts(f"{w}::scope", scope, "preconditions")

    if "parameters" in card:
        names: set[str] = set()
        for i, param in enumerate(sink.seq(w, card, "parameters") or []):
            pw = f"{w}::parameters[{i}]"
            if not isinstance(param, dict):
                sink.error(pw, "invalid-field", "must be a mapping with `name` and `description`")
                continue
            sink.unknown_keys(pw, param, {"name", "description"})
            name, _ = sink.text(pw, param, "name"), sink.text(pw, param, "description")
            if name in names:
                sink.error(pw, "duplicate-id", f"duplicate parameter name {name!r}")
            if name:
                names.add(name)

    conditions: dict[str, list[str]] = {}
    exclusions: dict[str, list[str]] = {}
    trigger = sink.mapping(w, card, "trigger")
    if trigger is not None:
        tw = f"{w}::trigger"
        sink.unknown_keys(tw, trigger, {"structural_conditions", "diagnostic_questions", "exclusion_conditions"})
        for i, cond in enumerate(sink.seq(tw, trigger, "structural_conditions", non_empty=True) or []):
            cw = f"{tw}.structural_conditions[{i}]"
            if not isinstance(cond, dict):
                sink.error(cw, "invalid-field", "must be a mapping")
                continue
            sink.unknown_keys(cw, cond, {"id", "text", "requires_features"})
            cid, _ = sink.ident(cw, cond, "id", TC_ID, "condition id (TC<n>)"), sink.text(cw, cond, "text")
            feats = _check_features(sink, cw, sink.texts(cw, cond, "requires_features", non_empty=True), ctx)
            if cid and cid in conditions:
                sink.error(cw, "duplicate-id", f"duplicate condition id {cid!r}")
            elif cid and feats:
                conditions[cid] = feats
        sink.texts(tw, trigger, "diagnostic_questions", non_empty=True)
        for i, excl in enumerate(sink.seq(tw, trigger, "exclusion_conditions") or []):
            xw = f"{tw}.exclusion_conditions[{i}]"
            if not isinstance(excl, dict):
                sink.error(xw, "invalid-field", "must be a mapping")
                continue
            sink.unknown_keys(xw, excl, {"id", "text", "excluded_by_features"})
            xid, _ = sink.ident(xw, excl, "id", XC_ID, "exclusion id (XC<n>)"), sink.text(xw, excl, "text")
            feats = _check_features(sink, xw, sink.texts(xw, excl, "excluded_by_features", non_empty=True), ctx)
            if xid and xid in exclusions:
                sink.error(xw, "duplicate-id", f"duplicate exclusion id {xid!r}")
            elif xid and feats:
                exclusions[xid] = feats
        for xid, xfeats in exclusions.items():
            for cid, cfeats in conditions.items():
                if set(xfeats) <= set(cfeats):
                    sink.error(
                        f"{tw}.exclusion_conditions", "self-excluding-trigger",
                        f"exclusion {xid} fires whenever condition {cid} is satisfied, so {cid} can never yield a match",
                    )

    transformation = sink.mapping(w, card, "transformation")
    if transformation is not None:
        sink.unknown_keys(f"{w}::transformation", transformation, {"input_representation", "operation", "output_representation"})
        for key in ("input_representation", "operation", "output_representation"):
            sink.text(f"{w}::transformation", transformation, key)

    effect = sink.mapping(w, card, "expected_effect")
    if effect is not None:
        sink.unknown_keys(f"{w}::expected_effect", effect, {"measurable_prediction", "outcome_measure"})
        for key in ("measurable_prediction", "outcome_measure"):
            sink.text(f"{w}::expected_effect", effect, key)

    sink.id_text_items(w, card, "obligations", OB_ID, "obligation id (OB<n>)", non_empty=True)
    sink.id_text_items(w, card, "failure_modes", FM_ID, "failure-mode id (FM<n>)", non_empty=True)

    tests: list[str] = []
    attempts: list[dict[str, Any]] = []
    validation = sink.mapping(w, card, "validation")
    if validation is not None:
        vw = f"{w}::validation"
        sink.unknown_keys(vw, validation, {"discriminating_tests", "baseline", "falsification_condition", "counterexample_attempts"})
        tests = sink.texts(vw, validation, "discriminating_tests") or []
        sink.text(vw, validation, "baseline")
        sink.text(vw, validation, "falsification_condition")
        for i, attempt in enumerate(sink.seq(vw, validation, "counterexample_attempts") or []):
            aw = f"{vw}.counterexample_attempts[{i}]"
            if not isinstance(attempt, dict):
                sink.error(aw, "invalid-field", "must be a mapping")
                continue
            sink.unknown_keys(aw, attempt, {"description", "outcome", "ref"})
            sink.text(aw, attempt, "description")
            outcome = sink.choice(aw, attempt, "outcome", ATTEMPT_OUTCOMES)
            if outcome in ("found_counterexample", "none_found") and not _is_text(attempt.get("ref")):
                sink.error(aw, "missing-field", "an attempt that was run needs a `ref` to its record")
            if outcome:
                attempts.append(attempt)

    exemplar_kinds: list[str] = []
    for key, id_pattern in (("exemplars", EX_ID), ("counterexamples", CX_ID)):
        seen: set[str] = set()
        for i, item in enumerate(sink.seq(w, card, key) or []):
            iw = f"{w}.{key}[{i}]"
            if not isinstance(item, dict):
                sink.error(iw, "invalid-field", "must be a mapping")
                continue
            allowed = {"id", "kind", "ref", "note"} if key == "exemplars" else {"id", "ref", "note"}
            sink.unknown_keys(iw, item, allowed)
            item_id = sink.ident(iw, item, "id", id_pattern, "id")
            ref, _ = sink.text(iw, item, "ref"), sink.text(iw, item, "note")
            kind = sink.choice(iw, item, "kind", EXEMPLAR_KINDS) if key == "exemplars" else None
            if item_id in seen:
                sink.error(iw, "duplicate-id", f"duplicate id {item_id!r}")
            if item_id:
                seen.add(item_id)
            if kind:
                exemplar_kinds.append(kind)
            if ref and kind == "recorded_episode" and not EPISODE_ID.match(ref):
                sink.error(iw, "invalid-id", "a recorded_episode exemplar must reference an episode id (EP-...)")
            elif ref:
                _check_ref(sink, iw, ref, ctx)

    sink.seq(w, card, "relations")  # per-relation checks need the whole library; see _check_relations

    provenance = sink.mapping(w, card, "provenance")
    review = origin = None
    if provenance is not None:
        pw = f"{w}::provenance"
        sink.unknown_keys(pw, provenance, {"origin", "source_refs", "episode_refs", "review_status", "reviewed_by", "notes"})
        origin = sink.choice(pw, provenance, "origin", ORIGINS)
        for ref in sink.texts(pw, provenance, "source_refs", non_empty=True) or []:
            _check_ref(sink, pw, ref, ctx)
        episode_refs = sink.texts(pw, provenance, "episode_refs") or []
        for ref in episode_refs:
            if not EPISODE_ID.match(ref):
                sink.error(pw, "invalid-id", f"episode_refs entry {ref!r} is not an episode id (EP-...)")
        if origin == "episode-derived" and not episode_refs:
            sink.error(pw, "missing-provenance", "origin `episode-derived` requires at least one episode_refs entry")
        review = sink.choice(pw, provenance, "review_status", REVIEW_STATUSES)
        if review == "human_reviewed" and not _is_text(provenance.get("reviewed_by")):
            sink.error(pw, "missing-reviewer", "`review_status: human_reviewed` requires `reviewed_by`")

    # Promotion policy (strategy_ir.md, "Promotion and evidence policy").
    if status and status != "candidate" and review is not None and review != "human_reviewed":
        sink.error(
            f"{w}::status", "unreviewed-promotion",
            f"status `{status}` requires provenance.review_status `human_reviewed`; promotion is human-adjudicated",
        )
    if status in ("under_test", "supported_in_scope") and validation is not None and not tests:
        sink.error(f"{w}::validation", "missing-tests", f"status `{status}` requires at least one discriminating test")
    if status == "supported_in_scope":
        if "recorded_episode" not in exemplar_kinds:
            sink.error(
                f"{w}::exemplars", "unsupported-status",
                "status `supported_in_scope` requires a `recorded_episode` exemplar; illustrations and bounded pilots do not suffice",
            )
        if not any(a.get("outcome") in ("found_counterexample", "none_found") for a in attempts):
            sink.error(
                f"{w}::validation", "unsupported-status",
                "status `supported_in_scope` requires at least one counterexample attempt that was actually run",
            )
    if status == "disconfirmed_in_scope" and isinstance(card.get("counterexamples"), list) and not card["counterexamples"]:
        sink.error(f"{w}::counterexamples", "unsupported-status", "status `disconfirmed_in_scope` requires a recorded counterexample")
    return card


def _check_relations(card_docs: dict[str, Document], sink: _Sink) -> None:
    cards = {sid: doc.data for sid, doc in card_docs.items()}
    for sid, doc in card_docs.items():
        card, w = doc.data, doc.where
        seen: set[tuple[str, str]] = set()
        for i, rel in enumerate(card.get("relations") if isinstance(card.get("relations"), list) else []):
            rw = f"{w}.relations[{i}]"
            if not isinstance(rel, dict):
                sink.error(rw, "invalid-field", "must be a mapping")
                continue
            sink.unknown_keys(rw, rel, {"type", "target", "rationale", "bindings"})
            rtype = sink.choice(rw, rel, "type", RELATION_TYPES)
            target = sink.text(rw, rel, "target")
            sink.text(rw, rel, "rationale")
            if target is None or rtype is None:
                continue
            if (rtype, target) in seen:
                sink.warn(rw, "duplicate-relation", f"relation {rtype} -> {target} is listed more than once")
            seen.add((rtype, target))
            if target == sid:
                sink.error(rw, "self-relation", "a strategy cannot relate to itself")
                continue
            if target not in cards:
                sink.error(rw, "unresolved-target", f"relation target {target!r} is not a known strategy_id")
                continue
            if rtype != "specializes":
                if "bindings" in rel:
                    sink.error(rw, "invalid-field", "`bindings` is only meaningful for `specializes`")
                continue
            parent_params = [p.get("name") for p in _items(cards[target].get("parameters")) if _is_text(p.get("name"))]
            bindings = rel.get("bindings")
            if not parent_params:
                sink.error(rw, "unbindable-parent", f"{target!r} declares no parameters, so it cannot be specialized")
            elif not isinstance(bindings, dict) or not bindings:
                sink.error(rw, "missing-bindings", f"`specializes` must bind at least one parameter of {target!r}: {', '.join(parent_params)}")
            else:
                for name, value in bindings.items():
                    if name not in parent_params:
                        sink.error(rw, "unknown-parameter", f"binding {name!r} is not a parameter of {target!r} ({', '.join(parent_params)})")
                    elif not _is_text(value):
                        sink.error(rw, "invalid-field", f"binding for {name!r} must be a non-empty string")

    # Specialization must be acyclic.
    color: dict[str, int] = {}  # 1 = on the current path, 2 = finished

    def visit(node: str, path: list[str]) -> None:
        color[node] = 1
        for parent in card_parents(cards[node]):
            if parent not in cards:
                continue
            if color.get(parent) == 1:
                cycle = [*path[path.index(parent):], parent] if parent in path else [node, parent]
                sink.error(card_docs[node].where, "specialization-cycle", "specialization cycle: " + " -> ".join(cycle))
            elif parent not in color:
                visit(parent, [*path, parent])
        color[node] = 2

    for sid in sorted(cards):
        if sid not in color:
            visit(sid, [sid])


# --------------------------------------------------------------------------------------------
# Problem states and episodes
# --------------------------------------------------------------------------------------------
def validate_problem_state(
    state: Any, where: str, feature_ids: Iterable[str], *, standalone: bool = False
) -> tuple[list[Issue], tuple[set[str], set[str]] | None]:
    """Validate one problem state mapping; returns issues and its (present, absent) features."""
    sink = _Sink()
    ctx = _Ctx(frozenset(), frozenset(feature_ids), None, {})
    result = _validate_state(state, where, ctx, sink, standalone=standalone)
    return sink.issues, result


def _validate_state(state: Any, w: str, ctx: _Ctx, sink: _Sink, *, standalone: bool) -> tuple[set[str], set[str]] | None:
    if not isinstance(state, dict):
        sink.error(w, "type", "a problem state must be a mapping")
        return None
    sink.unknown_keys(w, state, STATE_KEYS | ({"ir_kind", "schema_version"} if standalone else set()))
    if standalone:
        sink.header(w, state, KIND_STATE)
    sink.ident(w, state, "problem_state_id", STATE_ID, "problem state id (PS-...)")
    for key in ("title", "statement", "goal"):
        sink.text(w, state, key)
    present: set[str] = set()
    absent: set[str] = set()
    for key, bucket in (("features", present), ("absent_features", absent)):
        for i, item in enumerate(sink.seq(w, state, key) or []):
            iw = f"{w}.{key}[{i}]"
            if not isinstance(item, dict):
                sink.error(iw, "invalid-field", "must be a mapping")
                continue
            allowed = {"feature", "evidence", "asserted_by"} | ({"confidence"} if key == "features" else set())
            sink.unknown_keys(iw, item, allowed)
            feature = sink.text(iw, item, "feature")
            sink.text(iw, item, "evidence")  # a feature label without evidence is only a label
            sink.text(iw, item, "asserted_by")
            if key == "features":
                sink.choice(iw, item, "confidence", CONFIDENCES)
            if feature is None:
                continue
            if ctx.features and feature not in ctx.features:
                sink.error(iw, "unknown-feature", f"feature {feature!r} is not in the feature vocabulary")
            if feature in bucket:
                sink.error(iw, "duplicate-feature", f"feature {feature!r} is declared more than once in `{key}`")
            bucket.add(feature)
    for feature in sorted(present & absent):
        sink.error(w, "contradictory-feature", f"feature {feature!r} is declared both present and absent")
    if standalone and isinstance(state.get("features"), list) and not state["features"]:
        sink.warn(w, "empty-features", "no features declared, so strategy retrieval will return no candidates for this state")
    return present, absent


def _validate_episode(doc: Document, ctx: _Ctx, cards: dict[str, dict[str, Any]], sink: _Sink) -> None:
    w, ep = doc.where, doc.data
    if not isinstance(ep, dict):
        sink.error(w, "type", "document must be a mapping")
        return
    sink.unknown_keys(
        w, ep,
        {"ir_kind", "schema_version", "episode_id", "title", "status", "epistemic_note", "root_state",
         "problem_states", "applications", "terminal"},
    )
    sink.header(w, ep, KIND_EPISODE)
    sink.ident(w, ep, "episode_id", EPISODE_ID, "episode id (EP-...)")
    sink.text(w, ep, "title")
    ep_status = sink.choice(w, ep, "status", EPISODE_STATUSES)
    sink.text(w, ep, "epistemic_note")
    root_state = sink.text(w, ep, "root_state")

    states: dict[str, tuple[set[str], set[str]]] = {}
    for i, state in enumerate(sink.seq(w, ep, "problem_states", non_empty=True) or []):
        sw = f"{w}::problem_states[{i}]"
        result = _validate_state(state, sw, ctx, sink, standalone=False)
        sid = state.get("problem_state_id") if isinstance(state, dict) else None
        if result is None or not isinstance(sid, str):
            continue
        if sid in states:
            sink.error(sw, "duplicate-id", f"duplicate problem state id {sid!r} in this episode")
        states[sid] = result

    applications = sink.seq(w, ep, "applications", non_empty=True) or []
    # First pass: who produces each state; second pass: validate every application.
    producer: dict[str, dict[str, Any]] = {}
    for app in _items(applications):
        out_ref = app.get("output_state_ref")
        if isinstance(out_ref, str):
            if out_ref in producer:
                sink.error(w, "multiple-producers", f"state {out_ref!r} is the output of more than one application")
            producer.setdefault(out_ref, app)

    edges: dict[str, list[str]] = {}
    app_ids: set[str] = set()
    for j, app in enumerate(applications):
        aw = f"{w}::applications[{j}]"
        if not isinstance(app, dict):
            sink.error(aw, "invalid-field", "must be a mapping")
            continue
        app_id = sink.ident(aw, app, "application_id", APPLICATION_ID, "application id (APP-...)")
        if app_id:
            aw = f"{aw}({app_id})"
            if app_id in app_ids:
                sink.error(aw, "duplicate-id", f"duplicate application id {app_id!r}")
            app_ids.add(app_id)
        sink.unknown_keys(aw, app, APPLICATION_KEYS)
        outcome = sink.choice(aw, app, "outcome", OUTCOMES)
        sink.choice(aw, app, "review_status", REVIEW_STATUSES)
        sink.text(aw, app, "selection_rationale")
        sink.text(aw, app, "transformation_record")
        sink.texts(aw, app, "assumptions_introduced")
        sink.texts(aw, app, "information_discarded")
        measurement_refs = sink.texts(aw, app, "measurement_refs") or []
        if ep_status == "recorded" and outcome in SUCCESS_OUTCOMES and not measurement_refs:
            sink.error(aw, "missing-measurement", "a recorded episode must cite measurement_refs for a successful application")

        in_ref = sink.text(aw, app, "input_state_ref")
        out_ref = app.get("output_state_ref")
        if "output_state_ref" not in app:
            sink.error(aw, "missing-field", "missing required field `output_state_ref` (use null when no state results)")
        elif out_ref is not None and not _is_text(out_ref):
            sink.error(aw, "invalid-field", "`output_state_ref` must be a state id or null")
            out_ref = None
        if outcome in SUCCESS_OUTCOMES and not isinstance(out_ref, str):
            sink.error(aw, "missing-output-state", f"outcome `{outcome}` requires an `output_state_ref`")
        for label, ref in (("input_state_ref", in_ref), ("output_state_ref", out_ref)):
            if isinstance(ref, str) and ref not in states:
                sink.error(aw, "unknown-state-ref", f"`{label}` {ref!r} is not a problem state of this episode")
        if isinstance(in_ref, str) and in_ref == out_ref:
            sink.error(aw, "unchanged-state", "an application must produce a new state; use a null output_state_ref for no_effect")
        if isinstance(in_ref, str) and isinstance(out_ref, str):
            edges.setdefault(in_ref, []).append(out_ref)

        chained = isinstance(in_ref, str) and in_ref in producer
        interface_check = app.get("interface_check")
        if "interface_check" not in app:
            sink.error(aw, "missing-field", "missing required field `interface_check` (use null for a first step)")
        elif chained and not _is_text(interface_check):
            sink.error(aw, "missing-interface-check", f"input state {in_ref!r} was produced by another application; explain how it satisfies this strategy's input")
        elif interface_check is not None and not _is_text(interface_check):
            sink.error(aw, "invalid-field", "`interface_check` must be a non-empty string or null")

        _validate_application_strategy(app, aw, outcome, states.get(in_ref) if isinstance(in_ref, str) else None, cards, sink)

    # Graph structure.
    if root_state:
        if root_state not in states:
            sink.error(w, "unknown-state-ref", f"`root_state` {root_state!r} is not a problem state of this episode")
        elif root_state in producer:
            sink.error(w, "invalid-root", f"`root_state` {root_state!r} is the output of an application; the root must be an initial state")
    color: dict[str, int] = {}  # 1 = on the current path, 2 = finished

    def visit(node: str, trail: list[str]) -> None:
        color[node] = 1
        for nxt in edges.get(node, []):
            if color.get(nxt) == 1:
                cycle = [*trail[trail.index(nxt):], nxt] if nxt in trail else [node, nxt]
                sink.error(w, "cycle", "application cycle: " + " -> ".join(cycle))
            elif nxt not in color:
                visit(nxt, [*trail, nxt])
        color[node] = 2

    for node in sorted(edges):
        if node not in color:
            visit(node, [node])
    if root_state in states:
        reachable, stack = {root_state}, [root_state]
        while stack:
            for nxt in edges.get(stack.pop(), []):
                if nxt not in reachable:
                    reachable.add(nxt)
                    stack.append(nxt)
        for orphan in sorted(set(states) - reachable):
            sink.warn(w, "orphan-state", f"state {orphan!r} is not reachable from the root state")

    terminal = sink.mapping(w, ep, "terminal")
    if terminal is not None:
        tw = f"{w}::terminal"
        sink.unknown_keys(tw, terminal, {"state_ref", "claim", "note"})
        claim = sink.choice(tw, terminal, "claim", TERMINAL_CLAIMS)
        state_ref = terminal.get("state_ref")
        if "state_ref" not in terminal:
            sink.error(tw, "missing-field", "missing required field `state_ref` (use null when there is none)")
        elif state_ref is not None and not (isinstance(state_ref, str) and state_ref in states):
            sink.error(tw, "unknown-state-ref", f"`state_ref` {state_ref!r} is not a problem state of this episode")
        elif claim == "solved":
            _check_solved_chain(tw, state_ref, root_state, producer, sink)


def _check_solved_chain(tw: str, state_ref: Any, root_state: str | None, producer: dict[str, dict[str, Any]], sink: _Sink) -> None:
    """A `solved` claim needs an unbroken chain of successful applications from the root, ending in `solved`."""
    if not isinstance(state_ref, str) or state_ref not in producer:
        sink.error(tw, "unsupported-claim", "claim `solved` requires `state_ref` to be the output of an application")
        return
    if producer[state_ref].get("outcome") != "solved":
        sink.error(tw, "unsupported-claim", "claim `solved` requires the final application to have outcome `solved`")
    current, seen = state_ref, set()
    while current != root_state:
        app = producer.get(current) if isinstance(current, str) else None
        if app is None or current in seen:
            sink.error(tw, "unsupported-claim", f"claim `solved`: the chain from the root state does not reach {current!r}")
            return
        seen.add(current)
        step_outcome = app.get("outcome")
        if not (isinstance(step_outcome, str) and step_outcome in SUCCESS_OUTCOMES):
            sink.error(tw, "unsupported-claim", f"claim `solved`: application {app.get('application_id')!r} on the chain has outcome {step_outcome!r}")
        current = app.get("input_state_ref")


def _validate_application_strategy(
    app: dict[str, Any], aw: str, outcome: str | None, input_state: tuple[set[str], set[str]] | None,
    cards: dict[str, dict[str, Any]], sink: _Sink,
) -> None:
    """Checks that need the strategy card: trigger evidence and obligation coverage."""
    ref = sink.mapping(aw, app, "strategy_ref")
    sid = version = None
    if ref is not None:
        sink.unknown_keys(f"{aw}.strategy_ref", ref, {"strategy_id", "version"})
        sid = sink.text(f"{aw}.strategy_ref", ref, "strategy_id")
        version = sink.integer(f"{aw}.strategy_ref", ref, "version")

    evidence = sink.seq(aw, app, "trigger_evidence")
    rationale = app.get("off_trigger_rationale")
    if "off_trigger_rationale" not in app:
        sink.error(aw, "missing-field", "missing required field `off_trigger_rationale` (use null when trigger evidence is given)")
    elif rationale is not None and not _is_text(rationale):
        sink.error(aw, "invalid-field", "`off_trigger_rationale` must be a non-empty string or null")
    if evidence is not None and not evidence and not _is_text(rationale):
        sink.error(aw, "missing-trigger-basis", "give trigger_evidence, or an off_trigger_rationale if the strategy was tried off-trigger")

    checks = sink.seq(aw, app, "obligation_checks")
    parsed: dict[str, dict[str, Any]] = {}
    for k, check in enumerate(checks or []):
        kw = f"{aw}.obligation_checks[{k}]"
        if not isinstance(check, dict):
            sink.error(kw, "invalid-field", "must be a mapping")
            continue
        sink.unknown_keys(kw, check, {"obligation_id", "status", "evidence"})
        oid, status = sink.text(kw, check, "obligation_id"), sink.choice(kw, check, "status", CHECK_STATUSES)
        if status == "passed" and not _is_text(check.get("evidence")):
            sink.error(kw, "missing-evidence", "a passed check must cite evidence")
        if oid and sid:
            key = qualify(sid, oid)
            if key in parsed:
                sink.error(kw, "duplicate-id", f"obligation {key!r} is checked more than once")
            parsed[key] = check
    if outcome == "invalid_transform" and not any(c.get("status") == "failed" for c in parsed.values()):
        sink.error(aw, "unsupported-outcome", "outcome `invalid_transform` requires at least one failed obligation check")

    if sid is None or version is None:
        return
    card = cards.get(sid)
    if card is None:
        sink.error(f"{aw}.strategy_ref", "unknown-strategy", f"strategy {sid!r} is not in the strategy library")
        return
    current = card.get("version")
    if _is_int(current) and version > current:
        sink.error(f"{aw}.strategy_ref", "future-version", f"version {version} is newer than the library card (version {current})")
        return
    if _is_int(current) and version < current:
        sink.warn(
            f"{aw}.strategy_ref", "stale-card-version",
            f"recorded against version {version} but the library card is at version {current}; trigger and obligation checks were skipped",
        )
        return

    conditions = {c["id"]: c for c in trigger_conditions(card) if isinstance(c.get("id"), str)}
    for k, item in enumerate(evidence or []):
        ew = f"{aw}.trigger_evidence[{k}]"
        if not isinstance(item, dict):
            sink.error(ew, "invalid-field", "must be a mapping with `condition_id` and `note`")
            continue
        sink.unknown_keys(ew, item, {"condition_id", "note"})
        cid, _ = sink.text(ew, item, "condition_id"), sink.text(ew, item, "note")
        if cid is None:
            continue
        if cid not in conditions:
            sink.error(ew, "unknown-condition", f"strategy {sid!r} has no trigger condition {cid!r}")
        elif input_state is not None:
            missing = [f for f in condition_features(conditions[cid]) if f not in input_state[0]]
            if missing:
                sink.error(
                    ew, "trigger-not-supported",
                    f"condition {cid} requires feature(s) {', '.join(missing)}, which the input state does not declare as present",
                )

    required = effective_obligations(sid, cards)
    required_ids = {qid for qid, _ in required}
    for key in sorted(set(parsed) - required_ids):
        sink.error(aw, "unknown-obligation", f"obligation {key!r} is not an obligation of {sid!r} or of a strategy it specializes")
    if outcome in SUCCESS_OUTCOMES:
        unverified = [qid for qid, _ in required if parsed.get(qid, {}).get("status") != "passed"]
        if unverified:
            sink.error(
                aw, "unverified-success",
                f"outcome `{outcome}` requires every obligation to be checked and passed; not passed: {', '.join(unverified)}",
            )


# --------------------------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------------------------
def validate_documents(documents: Iterable[Document], root: Path | None = None) -> list[Issue]:
    """Validate a set of documents together; cross-references resolve only within the set."""
    sink = _Sink()
    by_kind: dict[str, list[Document]] = {kind: [] for kind in KINDS}
    for doc in documents:
        kind = document_kind(doc.data)
        if kind in by_kind:
            by_kind[kind].append(doc)
        elif kind is None:
            sink.error(doc.where, "unknown-kind", "cannot determine the document kind (missing `ir_kind`)")
        else:
            sink.error(doc.where, "unknown-kind", f"unknown `ir_kind` {kind!r}; expected one of {', '.join(KINDS)}")

    registries = _validate_families(by_kind[KIND_FAMILIES], sink)
    families = frozenset().union(*registries.values()) if registries else frozenset()
    features = _validate_vocabulary(by_kind[KIND_VOCAB], families, sink)
    ctx = _Ctx(families, features, root, registries)

    needs_vocab = by_kind[KIND_CARD] or by_kind[KIND_STATE] or by_kind[KIND_EPISODE]
    if needs_vocab and not features:
        sink.error("<library>", "no-vocabulary", "no feature vocabulary was loaded, so features cannot be checked")
    if by_kind[KIND_CARD] and not families:
        sink.error("<library>", "no-family-registry", "no family registry was loaded, so card families cannot be checked")

    card_docs: dict[str, Document] = {}
    for doc in by_kind[KIND_CARD]:
        card = _validate_card(doc, ctx, sink)
        sid = card.get("strategy_id") if card else None
        if isinstance(sid, str):
            if sid in card_docs:
                sink.error(doc.where, "duplicate-id", f"strategy_id {sid!r} is also defined in {card_docs[sid].where}")
            else:
                card_docs[sid] = doc
    _check_relations(card_docs, sink)
    cards = {sid: doc.data for sid, doc in card_docs.items()}

    state_ids: dict[str, str] = {}
    for doc in by_kind[KIND_STATE]:
        _validate_state(doc.data, doc.where, ctx, sink, standalone=True)
        sid = doc.data.get("problem_state_id") if isinstance(doc.data, dict) else None
        if isinstance(sid, str):
            if sid in state_ids:
                sink.error(doc.where, "duplicate-id", f"problem_state_id {sid!r} is also defined in {state_ids[sid]}")
            state_ids.setdefault(sid, doc.where)

    episodes: dict[str, Document] = {}
    for doc in by_kind[KIND_EPISODE]:
        _validate_episode(doc, ctx, cards, sink)
        eid = doc.data.get("episode_id") if isinstance(doc.data, dict) else None
        if isinstance(eid, str):
            if eid in episodes:
                sink.error(doc.where, "duplicate-id", f"episode_id {eid!r} is also defined in {episodes[eid].where}")
            episodes.setdefault(eid, doc)

    _check_exemplar_links(card_docs, episodes, sink)
    return sorted(set(sink.issues))


def _episode_strategy_ids(episode: dict[str, Any]) -> set[str]:
    return {
        app["strategy_ref"]["strategy_id"] for app in _items(episode.get("applications"))
        if isinstance(app.get("strategy_ref"), dict) and isinstance(app["strategy_ref"].get("strategy_id"), str)
    }


def _check_exemplar_links(card_docs: dict[str, Document], episodes: dict[str, Document], sink: _Sink) -> None:
    """An exemplar must exemplify; an illustrative episode cannot back a `recorded_episode` claim."""
    cards = {sid: doc.data for sid, doc in card_docs.items()}
    by_path = {doc.where: doc.data for doc in episodes.values()}
    for sid, doc in card_docs.items():
        card, w = doc.data, doc.where
        for i, ex in enumerate(_items(card.get("exemplars"))):
            ref, kind = ex.get("ref"), ex.get("kind")
            if not isinstance(ref, str):
                continue
            ew = f"{w}.exemplars[{i}]"
            episode = episodes[ref].data if kind == "recorded_episode" and ref in episodes else by_path.get(ref.partition("#")[0])
            if kind == "recorded_episode" and episode is None:
                sink.warn(ew, "unresolved-episode-ref", f"episode {ref!r} was not loaded, so the exemplar cannot be checked")
                continue
            if episode is None:
                continue
            if kind == "recorded_episode" and episode.get("status") != "recorded":
                sink.error(ew, "illustrative-exemplar", f"episode {ref!r} has status {episode.get('status')!r}, not `recorded`")
            applied = _episode_strategy_ids(episode)
            if sid not in applied and not any(sid in ancestors(other, cards) for other in applied):
                sink.error(ew, "exemplar-mismatch", f"the referenced episode never applies {sid!r} or a strategy that specializes it")
        for ref in _items_text(card.get("provenance"), "episode_refs"):
            if ref not in episodes:
                sink.warn(f"{w}::provenance", "unresolved-episode-ref", f"episode {ref!r} was not loaded, so it cannot be checked")
            elif episodes[ref].data.get("status") != "recorded" and card.get("status") == "supported_in_scope":
                sink.error(f"{w}::provenance", "illustrative-exemplar", f"episode {ref!r} is not `recorded` and cannot support promotion")


def _items_text(container: Any, key: str) -> list[str]:
    values = container.get(key) if isinstance(container, dict) else None
    return [v for v in values if isinstance(v, str)] if isinstance(values, list) else []


def validate_paths(paths: Iterable[Path], root: Path = PROJECT_ROOT) -> tuple[int, list[Issue]]:
    """Load and validate the given files/directories; returns (document count, issues)."""
    documents, problems = load_documents(paths, root)
    return len(documents), sorted(set([*problems, *validate_documents(documents, root)]))


# --------------------------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "paths", nargs="*", type=Path,
        help="extra YAML files or directories (for example a mission's problem_state.yaml); the standard library is always validated too",
    )
    parser.add_argument("--root", type=Path, default=PROJECT_ROOT, help="repository root (default: this checkout)")
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    parser.add_argument("--json", action="store_true", help="emit a JSON report instead of text")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    standard = [root / p for p in STANDARD_PATHS]
    count, issues = validate_paths([*standard, *args.paths], root)
    errors = [i for i in issues if i.severity == "error"]
    warnings = [i for i in issues if i.severity == "warning"]
    failed = bool(errors) or (args.strict and bool(warnings))
    if args.json:
        print(json.dumps({
            "documents": count, "errors": len(errors), "warnings": len(warnings),
            "issues": [issue.__dict__ for issue in issues],
        }, indent=2, sort_keys=True))
    else:
        for issue in issues:
            print(issue.render())
        print(f"[validate_ir] documents={count} errors={len(errors)} warnings={len(warnings)} -> {'FAIL' if failed else 'ok'}")
        print("[validate_ir] structural and record-keeping checks only; passing does not show that a strategy works.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
