# Initial Code Snippets Proposal v1

**Target:** `rl_eval_generator` (a separate repository).
**Status:** initial code proposals for selection, not implemented or tested against the target checkout. Any module placement or API shape is illustrative until checked in that repository. This file contains one code hook for each Mission 02 question (E1–E8, S1–S4, V1–V3), plus T1 for the separate matched-fact-presentation research line. These are independent candidates, not one benchmark, metric, or capability ladder.

The snippets are intentionally small: they identify concrete domain functions and validation points to carry into a later implementation session. Their tests are noted after each snippet; no experiment or model call is authorized by this proposal.

## Shared imports

The snippets below assume these standard-library imports in the relevant modules:

```python
from __future__ import annotations

import ast
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from hashlib import sha256
from math import fsum, isclose, isfinite
from typing import Hashable, Literal

World = Hashable
```

## E — Epistemic-reasoning questions

### E1 — Updating from a supplied behaviour policy

```python
def bayes_posterior(prior, likelihoods, observed):
    if not prior or set(prior) != set(likelihoods):
        raise ValueError("prior and likelihood hypotheses must match")
    weights = {
        h: prior[h] * likelihoods[h].get(observed, 0.0)
        for h in prior
    }
    z = fsum(weights.values())
    if z == 0.0:
        raise ValueError("observation is impossible under every hypothesis")
    return {h: w / z for h, w in weights.items()}
```

**Test:** vary prior odds and likelihood ratios; compare with hand-calculated posterior fixtures and prior-only/surface-cue baselines.

### E2 — Sequential public-announcement updates

```python
def public_announcement_trace(
    worlds: Iterable[World],
    announcements: Sequence[Callable[[World], bool]],
) -> tuple[frozenset[World], ...]:
    current = frozenset(worlds)
    trace = []
    for is_true in announcements:
        current = frozenset(w for w in current if is_true(w))
        if not current:
            raise ValueError("announcement eliminates every possible world")
        trace.append(current)
    return tuple(trace)
```

**Test:** score accuracy after each announcement prefix. Under standard truthful public-announcement semantics, reordering the same announcements should not change the final surviving worlds, so intermediate steps are where order effects belong.

### E3 — Information carried by silence

```python
def posterior_after_silence(prior, probability_of_speaking):
    likelihoods = {
        h: {
            "silent": 1.0 - probability_of_speaking[h],
            "spoke": probability_of_speaking[h],
        }
        for h in prior
    }
    return bayes_posterior(prior, likelihoods, "silent")
```

**Test:** identical speak probabilities across hypotheses should leave the posterior unchanged; differing policy probabilities should update it as specified.

### E4 — Nested knowledge order

```python
@dataclass(frozen=True)
class Atom:
    name: str


@dataclass(frozen=True)
class Knows:
    agent: str
    child: "Formula"


Formula = Atom | Knows


def holds(phi, world, accessibility, atom_is_true):
    if isinstance(phi, Atom):
        return atom_is_true(phi.name, world)
    return all(
        holds(phi.child, other, accessibility, atom_is_true)
        for other in accessibility[phi.agent][world]
    )
```

**Test:** hand-build finite accessibility relations and verify formulas at depths 1, 2, and 3. Keep the narrative fixed while varying only the queried nesting.

### E5 — Asymmetric or fragmented observation

```python
def accessibility_from_observation(
    worlds: Iterable[World],
    observe: Callable[[World], Hashable],
) -> dict[World, frozenset[World]]:
    worlds = tuple(worlds)
    return {
        w: frozenset(v for v in worlds if observe(v) == observe(w))
        for w in worlds
    }
```

**Test:** each world must be accessible from itself; worlds are mutually accessible exactly when the declared observation function gives them the same observation.

### E6 — Finite type spaces and common priors

```python
def verify_bne_deviations(current_payoff, deviation_payoffs, *, tol=1e-9):
    # Keys are (player, type); each value lists all unilateral
    # deviation payoffs for that player-type under the candidate profile.
    if set(current_payoff) != set(deviation_payoffs):
        raise ValueError("every player-type needs a deviation check")
    return all(
        all(payoff <= current_payoff[key] + tol for payoff in deviations)
        for key, deviations in deviation_payoffs.items()
    )
```

**Test:** compare the checker against independently enumerated small games with unique Bayesian–Nash equilibria. This checks a candidate profile; it is not itself the equilibrium enumerator.

### E7 — Level-k versus a competing solution concept

```python
def discriminating_instances(cases, predict_level_k, predict_alternative):
    return [
        (case_id, predict_level_k(case), predict_alternative(case))
        for case_id, case in cases
        if predict_level_k(case) != predict_alternative(case)
    ]
```

**Test:** reject an evaluation set with no discriminating instances; report accuracy against each prediction separately rather than a generic “reasoning depth” score.

### E8 — Belief and action in a signaling game

```python
def receiver_response(prior, signal_likelihoods, signal, utility):
    belief = bayes_posterior(prior, signal_likelihoods, signal)
    action = max(
        utility,
        key=lambda a: fsum(belief[h] * utility[a][h] for h in belief),
    )
    return belief, action
```

**Test:** generate games on both sides of precomputed pooling/separating boundaries and verify the independently derived belief and best response.

## S — Strategy-pack questions

### S1 — Strategy-card content versus generic advice

```python
def paired_accuracy_delta(results, arm_a="card", arm_b="generic"):
    # results[case_id][arm] is a boolean correctness outcome.
    diffs = []
    for case_id, outcomes in results.items():
        if set(outcomes) != {arm_a, arm_b}:
            raise ValueError(f"incomplete pair: {case_id}")
        diffs.append(int(outcomes[arm_a]) - int(outcomes[arm_b]))
    if not diffs:
        raise ValueError("no paired cases")
    return fsum(diffs) / len(diffs)
```

**Test:** both arms must use the same cases and matched instruction length/format; report the paired difference and per-case outcomes.

### S2 — Incremental value of trigger matching

```python
@dataclass(frozen=True)
class Card:
    card_id: str
    family: str
    trigger: str
    text: str

    @property
    def digest(self) -> str:
        return sha256(self.text.encode("utf-8")).hexdigest()


def validate_matched_yoked(case, matched: Card, yoked: Card) -> tuple[str, str]:
    if matched.card_id == yoked.card_id:
        raise ValueError("arms require distinct cards")
    if matched.family != case.family or yoked.family != case.family:
        raise ValueError("cards must be from the same family as the case")
    if matched.trigger != case.trigger or yoked.trigger == case.trigger:
        raise ValueError("invalid matched/yoked trigger assignment")
    return matched.digest, yoked.digest
```

**Test:** freeze the manifest before solving; reject cross-family or accidentally matched yoked cards. Handle absent-trigger cases as their own specified arm, not as a matched pair.

### S3 — Incremental effect of validity obligations

```python
@dataclass(frozen=True)
class ObligationVariant:
    family: str
    trigger: str
    core_text: str
    obligations: tuple[str, ...]


def validate_obligation_ablation(with_obligations, without_obligations):
    if (with_obligations.family, with_obligations.trigger, with_obligations.core_text) != (
        without_obligations.family,
        without_obligations.trigger,
        without_obligations.core_text,
    ):
        raise ValueError("only the obligations may differ")
    if not with_obligations.obligations or without_obligations.obligations:
        raise ValueError("expected obligations-on versus obligations-off pair")
```

**Test:** use independently verified trigger-present / move-invalid cases and score misapplication separately from S2 accuracy.

### S4 — Transfer across epistemic families

```python
def validate_transfer_split(
    source_family, heldout_family, source_instance_hashes, heldout_instance_hashes
):
    if source_family == heldout_family:
        raise ValueError("transfer requires a distinct held-out family")
    overlap = set(source_instance_hashes) & set(heldout_instance_hashes)
    if overlap:
        raise ValueError(f"instance leakage: {sorted(overlap)}")
```

**Test:** freeze the shared structural feature before evaluation; check both instance-hash separation and that the held-out family was not used to author or select the card.

## V — Supporting validation questions

### V1 — Faithfulness of English renderings

```python
def blind_rendering_packet(opaque_id: str, task_text: str, query_text: str) -> dict:
    if not opaque_id or not task_text or not query_text:
        raise ValueError("packet fields must be non-empty")
    return {"packet_id": opaque_id, "task_text": task_text, "query_text": query_text}
```

**Test:** serialize packets and assert their keys are exactly the allowlist—no answer, formal state, generator parameters, or outcome labels.

### V2 — Characterization reliability and leakage

```python
FORBIDDEN_CHARACTERIZATION_FIELDS = {
    "answer", "generator_parameters", "outcome_label", "hidden_trigger"
}


def validate_characterization_packet(packet: Mapping[str, object]) -> None:
    leaked = FORBIDDEN_CHARACTERIZATION_FIELDS & packet.keys()
    if leaked:
        raise ValueError(f"characterization leakage: {sorted(leaked)}")


def exact_pairwise_agreement(ratings: Sequence[Mapping[str, str]]) -> float:
    if len(ratings) < 2 or any(set(r) != set(ratings[0]) for r in ratings):
        raise ValueError("need at least two raters with identical case sets")
    pairs = [(i, j) for i in range(len(ratings)) for j in range(i + 1, len(ratings))]
    return fsum(
        ratings[i][case] == ratings[j][case]
        for i, j in pairs
        for case in ratings[0]
    ) / (len(pairs) * len(ratings[0]))
```

**Test:** deliberately add each forbidden field and confirm the export validator rejects it; report agreement alongside the leakage audit.

### V3 — Feasibility of independent verification

```python
def assert_no_shared_core_imports(source: str, forbidden_prefixes: set[str]) -> None:
    tree = ast.parse(source)
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.append(node.module)
    leaked = [
        name for name in imported
        if any(name == prefix or name.startswith(prefix + ".")
               for prefix in forbidden_prefixes)
    ]
    if leaked:
        raise AssertionError(f"verifier imports generator internals: {leaked}")
```

**Test:** run this on the verifier source and separately check known-answer fixtures. The blocked import names must be set to the actual generator modules after inspecting the target repo.

## Separate research line — not one of the 15 questions

### T1 — Matched-fact presentation

```python
@dataclass(frozen=True)
class Fact:
    fact_id: str
    canonical_text: str


def assert_same_fact_set(control: Sequence[Fact], treatment: Sequence[Fact]) -> None:
    def canonical(facts):
        return frozenset(
            (fact.fact_id, sha256(fact.canonical_text.encode("utf-8")).hexdigest())
            for fact in facts
        )
    if canonical(control) != canonical(treatment):
        raise ValueError("presentation arms do not contain the same canonical facts")


def inquiry_regret(test_values: Mapping[str, float], chosen_test: str) -> float:
    if chosen_test not in test_values or not test_values:
        raise ValueError("chosen test must be scored by the oracle")
    return max(test_values.values()) - test_values[chosen_test]
```

**Test:** permuting or emphasizing a presentation must preserve canonical fact IDs and content hashes; regret is computed only from oracle-provided test values.

## Review boundary

These sketches are starter code for approval and refinement, not production-ready implementations. They do not select a single research question, combine metrics into a leaderboard score, assert that the named modules exist, or authorize experiments. Implement only the snippets selected for the subsequent `rl_eval_generator` session, after adapting them to its verified interfaces.
