# Strategy library (candidate cards)

> **Read this first.** Every card here is an **agent-proposed, unreviewed `candidate`**. Both example episodes are **illustrative** (textbook or constructed material). Nothing in this directory shows that any strategy works, that trigger matching picks useful strategies, or that using a strategy improves problem solving. The validator and the matcher are small deterministic tools, not a runtime: they never choose, apply, or promote a strategy. The schema and its rules are in [`research_protocol/strategy_ir.md`](../research_protocol/strategy_ir.md).

## Contents

| Path | What it is |
| :--- | :--- |
| `cards/*.yaml` | strategy cards (`strategy_card`); the file name is the `strategy_id` |
| `examples/*.episode.yaml` | two illustrative episodes showing the trace format |
| `../research_protocol/structural_features.yaml` | the feature vocabulary that triggers and problem states share |
| `../research_protocol/strategy_families.yaml` | the twelve proposed families (legacy registry; unchanged) |

### Cards

| `strategy_id` | Family | Notes |
| :--- | :--- | :--- |
| `invariant-closed-predicate` | invariant | abstract parent (parameters `P`, `Q`); a reachability obstruction by a predicate closed under every move |
| `invariant-conserved-quantity` | invariant | specializes the parent (equality with the start value); conservation, parity and colouring arguments |
| `invariant-monotone-potential` | invariant | specializes the parent (an inequality); one-directional quantities |
| `decomposition-explicit-interfaces` | decomposition | `composes_with` the card below |
| `local-to-global-boundary-contract` | local_to_global | cites Mission 01 only as a `bounded_pilot` exemplar plus one counterexample (FALS-03b) |
| `elimination-discriminating-test-ordering` | elimination | |
| `counterexample-minimal-failure` | counterexample | |
| `meta-unfix-assumptions` | meta | |

### Episodes

| Episode | Shows | Evidential weight |
| :--- | :--- | :--- |
| `EP-MUTILATED-BOARD` | one application of `invariant-conserved-quantity`, with the inherited obligations checked | none (textbook mathematics) |
| `EP-BOUNDARY-CONTRACT` | a decomposition → local-to-global chain with an interface check, ending unsolved | none (constructed scenario) |

## Using it

Requires PyYAML, like the existing scripts. Run from the repository root.

```bash
# 1. See the vocabulary, the question that settles each feature, and how many cards use it.
python scripts/retrieve_strategies.py --list-features

# 2. Write a problem state (template below), then check it against the vocabulary.
python scripts/validate_ir.py mission-XX/problem_state.yaml

# 3. Retrieve candidates. This writes strategies.md and strategy_retrieval_manifest.json.
python scripts/retrieve_strategies.py --problem mission-XX/problem_state.yaml --out mission-XX/context

# 4. A human or an agent decides what to try, applies it, and records an episode
#    (copy the shape of an example). Then check the record's consistency.
python scripts/validate_ir.py mission-XX/episodes/EP-....yaml
```

To see the output on a shipped example:

```bash
python scripts/retrieve_strategies.py --problem strategies/examples/mutilated-board.episode.yaml --out /tmp/strategy-pack
```

For that state the pack lists `invariant-conserved-quantity` and its parent `invariant-closed-predicate` as matched, `invariant-monotone-potential` as only partially evidenced, and `elimination-discriminating-test-ordering` as blocked because `competing_hypotheses_remain` is declared absent.

`validate_ir.py` always validates the whole standard library together with any extra paths you pass. `--strict` turns warnings into failures; `--json` gives a machine-readable report. `retrieve_strategies.py` refuses to run if the library or the selected problem state does not validate, so a broken file cannot produce a confident-looking pack.

### Problem-state template

```yaml
ir_kind: problem_state
schema_version: "0.2"
problem_state_id: PS-my-problem
title: Short title
statement: >-
  The problem in a few sentences.
goal: What would count as an answer.
features:
  - feature: transition_system_reachability_question   # a vocabulary id
    evidence: >-
      Why you believe this holds, in terms of this problem.
    confidence: moderate        # low | moderate | high
    asserted_by: human          # who asserted it
absent_features:
  - feature: competing_hypotheses_remain
    evidence: Why you believe this does not hold.
    asserted_by: human
```

A feature that is not listed is *unknown*, not absent, and a feature without evidence is rejected. Declaring a feature absent blocks every card whose trigger requires it, so declare absence only when you can say why. The matcher does not infer features from the problem text. Characterization is the weak point of the whole scheme: retrieval is only as good as the features someone declares.

## Adding a card

1. Copy `cards/invariant-conserved-quantity.yaml` (a specialization) or `cards/meta-unfix-assumptions.yaml` (a standalone card) and rename it to `<strategy_id>.yaml`.
2. Keep `status: candidate`, `review_status: unreviewed`, and the honest `origin` (`agent-proposed` for anything an agent wrote).
3. Express the trigger with vocabulary features. If a needed feature is missing, add it to `structural_features.yaml` with a `diagnostic_question`; do not put the trigger in prose only.
4. State obligations that can actually fail, a baseline, and a falsification condition. A card whose obligations can never fail is decoration.
5. Give exemplars their true kind. A textbook illustration is not a recorded episode.
6. Run `python scripts/validate_ir.py` and `python -m pytest`.

Promotion is a human decision and is not done by any script. The validator only checks that the records a status requires exist (see section 7 of the spec).

## Coverage and known gaps

- **8 cards cover 6 of the 12 families.** There is no card yet for `asymmetry`, `constraint`, `game`, `representation`, `search`, or `transformation`. A problem characterized only by those families' features will get no matches, and a short or empty list reflects the library's size, not the problem.
- **6 of the 15 vocabulary features are used by no card trigger yet:** `capability_or_access_asymmetry`, `enumerable_candidate_space`, `oversized_or_underdetermined_solution_space`, `representation_hides_structure`, `resembles_known_problem_under_mapping`, `strategic_actors`.
- A "bottleneck" move in the supplied design discussion corresponds to no family and has no card.
- The invariant parent is stated in closed-predicate form: exact conservation is a specialization (equality), and a monotone argument needs an inequality, so "seek a preserved quantity" would be too narrow for the general card.
- Whether collapsing the invariant variants into one parameterised card is useful is a hypothesis the schema permits and does not test. The empirical gate in the spec (section 10) has not been run.
