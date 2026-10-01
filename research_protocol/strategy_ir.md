# Strategy IR — Draft Design Proposal

- **Status:** `draft_for_human_review`
- **Version:** `0.1-proposal`
- **Scope:** A prospective procedural-memory object for the research-control layer. This is a schema/design proposal, not an implemented dispatcher, strategy selector, or validated problem-solving calculus.
- **Provenance:** The initial family taxonomy is derived from the user's supplied strategy-library reflection. That reflection is design input, not evidence that any strategy improves outcomes.

## 1. Architectural role

The Strategy IR represents **problem transformations** that can be retrieved, applied, checked, and learned from. It is distinct from both:

1. **Declarative research memory** — source-backed claims and interpretive relations in `knowledge/`.
2. **Agent runtime** — delegation, tools, execution, retries, and persistent state. This repository does not implement that runtime.

The epistemic compiler's prospective job is to characterize a problem, retrieve candidate transformations, make their triggers and obligations explicit, compile them into a testable mission, and connect observed results back to provenance-bearing strategy records. A frontier agent or other runtime may propose/apply a transformation; the compiler should not silently treat generated suggestions as validated strategies.

## 2. Strategy card schema

An individual strategy card is a versioned, scoped hypothesis about a transformation. Required fields:

```yaml
strategy_id: stable-id
version: 1
name: Human-readable name
family: representation # one of the IDs in strategy_families.yaml
status: candidate | under_test | supported_in_scope | disconfirmed_in_scope | retired
scope:
  problem_classes: []
  preconditions: []
trigger:
  structural_conditions: []
  diagnostic_questions: []
  exclusion_conditions: []
transformation:
  input_representation: description or schema reference
  operation: explicit transformation
  output_representation: description or schema reference
expected_effect:
  measurable_prediction: statement
  outcome_measure: metric or observable
obligations:
  - property/information/invariant that must be preserved
failure_modes:
  - predicted way the transformation can mislead, lose information, or fail
validation:
  discriminating_tests: []
  baseline: comparison to be used
  falsification_condition: explicit condition
exemplars: []
counterexamples: []
related_strategy_ids: []
provenance:
  origin: source-backed | episode-derived | user-proposed | agent-proposed
  source_refs: []
  episode_refs: []
  review_status: unreviewed | human_reviewed
```

This YAML illustrates required fields; it is not currently a machine-enforced schema. `scripts/validate_ir.py` is not implemented. A card should not be promoted merely because its prose sounds plausible or an agent selected it once.

## 3. Trigger-first retrieval and application record

**Trigger is the retrieval key.** Candidate retrieval should surface the structural conditions and diagnostic questions before presenting a suggested move. A match is a hypothesis about applicability, not an instruction to apply the strategy.

Each application should be recorded separately from the card:

```yaml
application_id: stable-episode-step-id
problem_state_ref: problem-state-id
strategy_ref:
  strategy_id: stable-id
  version: 1
trigger_evidence: []
selection_rationale: text
input_state_ref: problem-state-id
transformation_record: text or artifact reference
output_state_ref: problem-state-id
obligation_checks: []
outcome: solved | reduced | no_effect | invalid_transform | inconclusive
measurement_refs: []
review_status: unreviewed | human_reviewed
```

This records the trace:

```text
problem state P0 --[strategy/version + trigger evidence]--> transformed state P1
       |                                                       |
       +-------------------- measured evidence ----------------+
```

The “problem state” and transformation artifacts must be inspectable; a label such as `invariant` or `decomposition` alone is not an explanation.

## 4. Composition rules

Strategies may be composed only when their representation interfaces connect and their obligations are checked. In particular:

- the output representation of one application must satisfy the next strategy's input/preconditions;
- any assumptions introduced by a transformation must be recorded and tested;
- information discarded by a representation change must be listed;
- composition is not evidence of validity; the final problem and all intermediate obligations still require evaluation;
- failed, neutral, and counterexample-producing applications remain in the record.

Initially, composition should be manual and auditable. No planner, automatic delegation, DAG runtime, or persistent agent society is specified here.

## 5. Candidate family registry

`strategy_families.yaml` contains twelve **proposed families**, paraphrased from the user's reflection. Families are prompts for authoring more specific cards; they are not twelve validated strategies. The candidate moves include:

- **Representation:** change encoding/abstraction so useful structure is explicit.
- **Invariant:** search for a preserved or monotone quantity that constrains reachable outcomes.
- **Asymmetry:** identify differences in information, cost, access, or capabilities.
- **Decomposition:** split along real structural boundaries and make cross-boundary dependencies visible.
- **Elimination:** choose cheap discriminating tests that remove candidate explanations.
- **Constraint:** add justified constraints that reduce the solution space, then check for overconstraint.
- **Counterexample:** construct and minimize the smallest failure of a proposed explanation or generalization.
- **Meta:** inspect assumptions, objectives, rules, timing, or access that were treated as fixed.
- **Search:** use enumeration or computation where the search space is tractable.
- **Game:** model strategic actors, incentives, beliefs, and information.
- **Local-to-global:** identify what local components must preserve across interfaces for composition.
- **Transformation:** map the problem to known machinery and state the conditions under which the mapping is valid.

## 6. Promotion and evidence policy

Lifecycle: `candidate → under_test → supported_in_scope | disconfirmed_in_scope → retired` (where appropriate). Promotion is human-adjudicated and scoped to specified problem classes and conditions. It requires:

1. a trigger that can be recognized and challenged;
2. an explicit input-to-output transformation;
3. measurable expected effects and a baseline;
4. preservation obligations and failure modes;
5. discriminating tests, including counterexample attempts;
6. provenance to source material and/or tested episodes;
7. a record of negative and inconclusive applications.

A new strategy discovered by an agent remains `agent-proposed` until reviewed. User-provided general reflections can seed candidate families but cannot establish effectiveness. The imported Mindcluster graph is declarative memory and is not silently converted into procedural strategy cards.

## 7. Candidate follow-up question (not registered)

A future mission could test whether an explicitly specified boundary-compatibility transformation improves **global task validity** relative to a matched decomposition without that transformation. A candidate phenomenon is:

```text
local validity → declared boundary compatibility → global validity
```

The mission would need independently specified tasks, treatment, baseline, success measures, controls, and falsification criteria before execution. Sheaf, presheaf, descent, invariants, and interface contracts remain candidate formalisms, not premises. Mission 01 remains frozen and is not modified by this proposal.

## 8. Non-goals

This draft does not claim that a strategy library creates general intelligence or “impossible” capabilities. It does not implement runtime orchestration, strategy learning, semantic search, automatic strategy composition, a new UI, or a research-factory framework. The empirical question is whether trigger-matched transformations improve measured problem-solving or research quality beyond a suitable baseline, and under which conditions.
