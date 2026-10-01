# Strategy IR — v0.2 Draft

- **Status:** `draft_for_human_review`
- **Version:** `0.2-draft`
- **Scope:** a record-keeping and retrieval schema for *problem transformations* ("strategies"), with two small deterministic tools: a structural validator (`scripts/validate_ir.py`) and a trigger matcher (`scripts/retrieve_strategies.py`). It is **not** a dispatcher, an agent runtime, an automatic strategy selector, a planner, or a promotion engine, and it is not a validated problem-solving calculus (section 13).
- **Provenance:** the twelve families come from the user's supplied strategy-library reflection. The pipeline placement, the card/episode structure, the specialization idea, and the Compiler / Machine / Frontier-agent division come from a follow-up design discussion the user supplied. Both are design input, not evidence that any strategy improves outcomes. Every card in `strategies/cards/` is an agent-proposed, unreviewed `candidate`.

## 1. What this is for

A research mission can be started from a seed. This IR adds an optional step before the Council: **characterize the problem, retrieve candidate transformations whose triggers fit, make their obligations explicit, and record what happened when one was applied.** The aim is that a transformation which worked (or failed) leaves an inspectable trace rather than a label.

It separates three kinds of memory and keeps them from being converted into each other silently:

| Memory | Where | Role |
| :--- | :--- | :--- |
| Declarative research memory | `knowledge/` | source-backed claims and interpretive relations |
| Procedural memory | `strategies/` | candidate transformations with triggers, obligations, and records of use |
| Runtime | not in this repository | whoever applies a strategy (a human or an agent) |

## 2. Where this sits

```text
seed ─► problem characterization ─► retrieve candidate strategies ─► choose / apply / compose
          (problem_state)             (retrieve_strategies.py)          (human or agent)
                                                                              │
                         research execution ◄─ measurement & adversarial ◄─ candidate hypotheses
                         (Gates 3–4)            tests (Gates 1–2)            (Council)
```

| Step | Status in this repository |
| :--- | :--- |
| Seed, Council, Gates 1–4, execution | existing human-gated protocol (`protocol.md`); unchanged |
| Problem characterization | a `problem_state` record written by a human or agent; checked by `validate_ir.py` |
| Retrieve candidate strategies | `scripts/retrieve_strategies.py`: deterministic feature matching |
| Choose, apply, compose | **not implemented.** Done by a human or agent and recorded as an `episode` |
| Promote a strategy | **not implemented.** A human decision (section 7) |

### Artifacts

| Artifact | `ir_kind` | Location | Checked by `validate_ir.py` |
| :--- | :--- | :--- | :--- |
| Family registry (legacy file; recognised by `registry_kind` + `families`) | `family_registry` | `research_protocol/strategy_families.yaml` | structure, unique ids |
| Feature vocabulary | `feature_vocabulary` | `research_protocol/structural_features.yaml` | ids, family references, a diagnostic question per feature |
| Strategy card | `strategy_card` | `strategies/cards/<strategy_id>.yaml` | yes (section 3) |
| Problem state (standalone, or embedded in an episode) | `problem_state` | e.g. `mission-XX/problem_state.yaml` | yes (section 4) |
| Episode | `episode` | `strategies/examples/*.episode.yaml`, or per mission | yes (section 6) |
| Retrieval pack (generated, not committed) | none | `<out>/strategies.md`, `<out>/strategy_retrieval_manifest.json` | n/a |

Every IR document carries `ir_kind` and `schema_version: "0.2"` (a string; a float is rejected).

## 3. Strategy card (v0.2)

A card is a versioned, scoped **hypothesis** about a transformation. The worked reference is `strategies/cards/invariant-conserved-quantity.yaml`.

```yaml
ir_kind: strategy_card
schema_version: "0.2"
strategy_id: kebab-case-id          # file name must be <strategy_id>.yaml
version: 1                          # integer; bump when the meaning changes (episodes pin it)
name: Human-readable name
family: invariant                   # an id in strategy_families.yaml
status: candidate                   # candidate | under_test | supported_in_scope | disconfirmed_in_scope | retired
scope: {problem_classes: [...], preconditions: [...]}
parameters: [{name: Q, description: ...}]   # optional; only for abstract cards (section 5)
trigger:
  structural_conditions:            # TC<n>; each is a conjunction of features; any one condition suffices
    - {id: TC1, text: ..., requires_features: [feature_id, ...]}
  diagnostic_questions: [...]       # answered about the problem before applying
  exclusion_conditions:             # XC<n>; fires when all of its features are declared present
    - {id: XC1, text: ..., excluded_by_features: [feature_id, ...]}
transformation: {input_representation: ..., operation: ..., output_representation: ...}
expected_effect: {measurable_prediction: ..., outcome_measure: ...}
obligations: [{id: OB1, text: ...}]         # what must be checked when the card is applied
failure_modes: [{id: FM1, text: ...}]
validation:
  discriminating_tests: [...]
  baseline: ...
  falsification_condition: ...
  counterexample_attempts: [{description: ..., outcome: found_counterexample | none_found | not_run, ref: ...}]
exemplars: [{id: EX1, kind: textbook_illustration | bounded_pilot | recorded_episode, ref: ..., note: ...}]
counterexamples: [{id: CX1, ref: ..., note: ...}]
relations: [{type: specializes | composes_with | alternative_to | conflicts_with, target: strategy_id, rationale: ..., bindings: {...}}]
provenance: {origin: source-backed | episode-derived | user-proposed | agent-proposed,
             source_refs: [...], episode_refs: [...], review_status: unreviewed | human_reviewed,
             reviewed_by: ..., notes: ...}
```

Rules the validator enforces beyond field presence and the controlled vocabularies: ids are unique and follow their patterns; every feature a trigger uses is in the vocabulary; an exclusion whose features are a subset of a trigger condition's features is rejected (that condition could never match); `source_refs` and exemplar refs that look like repository paths (they contain a `/` or a file extension and are not URLs) must resolve under the repository root, and a `#fragment` on the family registry must name a family; an `exemplar` of kind `recorded_episode` must point at an episode that is `recorded` and that applies the card or a card that specializes it; a counterexample attempt that was actually run needs a `ref` to its record.

## 4. Problem characterization and trigger-first matching

**Trigger is the retrieval key.** Retrieval does not search card prose. It compares the features a problem state *declares* with the structural conditions a card *declares*.

### Problem state

A problem state has a `statement`, a `goal`, and two lists:

- `features`: each with `feature` (a vocabulary id), `evidence`, `confidence` (`low` | `moderate` | `high`) and `asserted_by`;
- `absent_features`: each with `feature`, `evidence`, `asserted_by`.

Features are **three-valued**: present, absent, or unknown. A feature that is not declared is *unknown*, never absent. **Asserting a feature is a claim about a problem, and it must carry evidence**: a feature label without evidence is rejected by the validator, because a label alone is only a guess that looks like a measurement. Declaring a feature both present and absent is an error.

The vocabulary (`structural_features.yaml`) gives each feature a `diagnostic_question`; `scripts/retrieve_strategies.py --list-features` prints them. The vocabulary is a coordination device so that triggers can be matched mechanically. It is not a validated ontology of problems, and the tools never infer features from text. Characterization is the weak point of the whole scheme: retrieval is exactly as good as the characterization that feeds it, and that part remains a human or agent judgment.

### Matching rule

For a state with present set *P* and absent set *A*:

| Class | Definition |
| :--- | :--- |
| condition satisfied | all of its `requires_features` are in *P* |
| condition open | some are in *P*, none in *A*, not all in *P* |
| condition blocked | any is in *A* |
| exclusion fired | all of its `excluded_by_features` are in *P* |
| card **matched** | at least one condition satisfied and no exclusion fired |
| card **open** | no condition satisfied, at least one open, no exclusion fired |
| card **exclusion-fired** | an exclusion fired on a matched or open card; shown separately, not recommended |
| card **disconfirmed in scope** | status `disconfirmed_in_scope` and matched or open; shown with its counterexamples instead of among the candidates |
| card **retired** | withheld unless `--include-retired` |

Matched cards are listed by trigger specificity (more required features first), then specialization depth, then number of satisfied conditions, then id. Status is displayed and is not an input to the order. **The order is a presentation order, not a ranking of expected usefulness.** Open cards list the unknown features together with their diagnostic questions, so the next step is to assess those features and record the evidence. Cards blocked only by a declared absence are listed so a wrong absence can be caught.

### What the pack says

For each matched card the pack shows, in this order: the trigger evidence (quoting the problem state's own words), the diagnostic questions, an exclusion check, the move, the obligations (including inherited ones), the failure modes, the expected effect and how it would be judged, and last the status and provenance. The pack opens by stating that **a match is a hypothesis about applicability**, that retrieved text is untrusted reference data and not instructions, and that no match is not evidence that no strategy applies.

## 5. Specialization and inherited obligations

The follow-up discussion proposed collapsing variants such as invariant, conservation and parity into one abstract strategy. The IR supports this with an abstract card that declares `parameters` and specializations that supply `bindings`.

- `invariant-closed-predicate` is the abstract card (parameters `P` and `Q`): find a quantity *Q* and a predicate *P* such that *P(Q(s))* holds at the start, is closed under every allowed transition, and fails at every target.
- `invariant-conserved-quantity` and `invariant-monotone-potential` specialize it by binding `P` and `Q`.
- The parent is stated in the **closed-predicate form** rather than as "seek a preserved quantity" because equality with the start value is only one choice of *P*; a monotone argument needs an inequality. Exact conservation is therefore a specialization, not the general case.

Rules: a `specializes` relation needs `bindings`; every binding key must be a declared parameter of the parent; the parent must declare parameters; specialization must be acyclic. **A card's effective obligations are its own plus those inherited through `specializes`**, referred to as `<strategy_id>#OBn`; a bare `OBn` in an application record means the applied card's own obligation. A specialization can add obligations and cannot drop inherited ones. The validator does not check that a specialization's trigger implies its parent's.

`composes_with` is directional: it says the output of one card is a plausible input to another. At episode level a chained step must say how the interface is satisfied (section 6). `alternative_to` and `conflicts_with` are descriptive only. Whether collapsing the variants into one parameterised card is *useful* is a hypothesis; the schema permits it and does not show it.

## 6. Episodes: applications, composition, and terminal claims

An episode records one attempt over a graph of problem states: `root_state`, `problem_states`, `applications`, and a `terminal` claim (`solved` | `unsolved` | `abandoned`). Each application names a strategy and version, an input state, and an output state (or `null`), and carries:

- `trigger_evidence`: the conditions of the card (by `TCn`) that justify the application. Each cited condition must be one the input state's declared features satisfy, otherwise the record is rejected. A strategy tried off-trigger gives an `off_trigger_rationale` instead of trigger evidence;
- `obligation_checks`: for each effective obligation, `status` (`passed` | `failed` | `not_checked`) and `evidence`;
- `assumptions_introduced`, `information_discarded`, `transformation_record`, `selection_rationale`;
- `interface_check`: required whenever the input state was produced by another application (`null` for a first step);
- `outcome` (`solved` | `reduced` | `no_effect` | `invalid_transform` | `inconclusive`) and `measurement_refs`.

Record-consistency rules: a state has at most one producing application; the graph is acyclic and the root is not a product; `solved` or `reduced` requires every effective obligation to be checked and `passed`; `invalid_transform` requires a failed check; a terminal claim of `solved` requires an unbroken chain of successful applications from the root ending in `solved`; failed, neutral and `no_effect` applications stay in the record.

An application pins the card version it used. If the library card has since moved to a newer version, the validator warns (`stale-card-version`) and skips the trigger and obligation checks for that application, because the old record cannot be judged against the new card; a pinned version newer than the library's is an error.

An episode is `illustrative` or `recorded`. A `recorded` episode must cite `measurement_refs` for each successful application. **An illustrative episode carries no evidential weight**: it shows the trace format and exercises the schema, and it cannot support promotion. Both shipped episodes are illustrative (textbook mathematics and a constructed software scenario), and neither is evidence that retrieval or any card helps on new problems.

## 7. Promotion and evidence policy

Lifecycle: `candidate → under_test → supported_in_scope | disconfirmed_in_scope → retired` (where appropriate). **Promotion is human-adjudicated and scoped to the problem classes and conditions named in the card.** No tool in this repository promotes a card.

| Status | Requirement checked by the validator |
| :--- | :--- |
| `candidate` | schema only (the status of every new card, including every agent-proposed one) |
| `under_test` | `review_status: human_reviewed` with `reviewed_by`; at least one discriminating test |
| `supported_in_scope` | as above, plus a `recorded_episode` exemplar (a `recorded` episode that applies the card or a specialization of it) and a counterexample attempt that was actually run |
| `disconfirmed_in_scope` | human review; at least one recorded counterexample |
| `retired` | human review |

The validator checks that these records exist. It cannot check that the evidence is sufficient, that the discriminating tests are adequate, or that the scope is right; those remain the reviewer's judgment. A strategy discovered by an agent stays `agent-proposed` until a human reviews it. The user's reflections can seed candidates but cannot establish effectiveness, and the imported Mindcluster graph is not converted into strategy cards. This document avoids describing any card as "known to work": a status describes evidence in a stated scope, and no card has any yet.

## 8. What is enforced and what is judged by humans

| Aspect | Enforced by `validate_ir.py` | Left to human or experimental judgment |
| :--- | :--- | :--- |
| Structure | required fields, controlled vocabularies, id formats, unique ids, resolving references | whether the schema is the right one |
| Features | a declared feature is in the vocabulary and carries evidence and confidence | whether the feature actually holds for the problem |
| Triggers | trigger evidence cites conditions that the input state's declared features satisfy; no self-excluding trigger | whether the trigger is the right trigger; whether the state was characterized fairly |
| Obligations | every effective obligation has a recorded status; success outcomes need all `passed` with evidence | whether each check was carried out soundly; whether the obligations are sufficient |
| Composition | a chained step records an `interface_check`; no cycles; one producer per state | whether the interface is really satisfied |
| Outcomes | outcome consistent with the checks; `solved` claims need an unbroken successful chain | whether the problem is actually solved |
| Status | the review and evidence records each status requires | whether to promote |
| Provenance | path references resolve; episode ids resolve | whether the sources support the claim |

A document that passes validation is well-formed. It is not thereby true, and a card that passes is not thereby effective.

## 9. Compiler and runtime exchange (file-based)

The follow-up discussion divided labour between a **Compiler** (schemas, validation, retrieval, human gates), a **Machine** or runtime (whatever applies a strategy), and a **Frontier agent** (a strong model asked for new strategy candidates). This repository implements only the Compiler side, and the exchange is files:

- **Compiler → runtime:** the problem state and the retrieval pack (`strategies.md`), whose obligations tell the runtime what it must record.
- **Runtime → Compiler:** an `episode` file, and optionally `strategy_card` proposals with a worked example, counterexamples, and provenance.
- A proposal enters the library only as `status: candidate`, `origin: agent-proposed`, `review_status: unreviewed`, by a reviewed commit. The validator checks the file; a human decides what happens next.

There is no delegation protocol, no RPC, no persistent agent state, and no automatic ingestion of proposals.

## 10. Empirical gate and stop rule

Nothing in this repository shows that trigger-matched strategies improve problem solving. The question that decides whether this IR deserves further investment is:

> Do problems characterized *before* the attempt, with strategies retrieved by trigger match, get solved or reduced better (verified outcome, or effort to a verified outcome) than under a suitable control?

**Gate.** Before building anything beyond the files and two scripts here (more cards at scale, richer matching, any runtime), register and run one comparison under the existing Gates, with at least: problems with known ground truth; characterization fixed before results are seen; a control receiving prose of comparable length that is not trigger-matched; a random-card control; problems where the trigger is absent; and toy instances where the trigger is present but the move is invalid, to see whether the obligations catch it.

**Stop rule.** If the registered comparison does not beat its controls by the margin fixed in advance, extension stops: the result is recorded, cards stay `candidate` or are retired, and the library is not expanded on the strength of plausibility. Obligation checks that never fail on planted invalid transforms are also a negative result for the obligation mechanism.

This gate has not been run. The tests in this repository check that the tools behave as specified; they say nothing about whether strategies help.

## 11. Non-goals

No dispatcher, agent runtime, planner, DAG engine, automatic strategy selection or composition, embedding or semantic retrieval, promotion engine, strategy learning, persistent agent society, or UI. No claim that a strategy library creates general intelligence or "impossible" capabilities. Mission 01 is frozen and is not reinterpreted or re-registered by this IR; its results appear only as a `bounded_pilot` exemplar and one counterexample on a single candidate card, and nothing here supports a sheaf theorem or an agent-coordination benefit.

Known gaps: five of the twelve families have no card yet (`asymmetry`, `constraint`, `representation`, `search`, `transformation`); the `game` family has five narrow cards written for Mission 02 (`strategies/README.md`); and a "bottleneck" move in the supplied reflection maps to no family and has no card.

## 12. Changes from 0.1

- Every document carries `ir_kind` and a string `schema_version: "0.2"`.
- Cards: triggers became structured (`structural_conditions` as feature conjunctions with ids, `exclusion_conditions`); `obligations` and `failure_modes` became id-bearing items; added `parameters`, `validation.counterexample_attempts`, typed `exemplars` and `counterexamples` with ids, and `provenance.reviewed_by`; `related_strategy_ids` became typed `relations` (`specializes` with `bindings`, `composes_with`, `alternative_to`, `conflicts_with`).
- New artifact types: feature vocabulary, problem state, episode.
- The 0.1 application record was reworked into the episode's application: `problem_state_ref` is replaced by `input_state_ref` and `output_state_ref`; `obligation_checks` became per-obligation status with evidence; added `interface_check`, `off_trigger_rationale`, `assumptions_introduced`, `information_discarded`.
- Obligation inheritance through `specializes`.
- Promotion policy turned from prose into checked records (section 7).
- `scripts/validate_ir.py` and `scripts/retrieve_strategies.py` exist; 0.1 said the validator was not implemented. They cover Strategy IR artifacts only, not the rest of the protocol.
- The 0.1 "candidate follow-up question" about boundary compatibility is now the candidate card `local-to-global-boundary-contract`. No mission has been registered for it.

## 13. A caveat on "calculus"

The follow-up discussion floated "Problem-Solving Calculus" as a name. Nothing here is a calculus: there are no composition laws, no notion of soundness or completeness, and no proof that composition preserves obligations. The IR is a schema for recording and retrieving candidate transformations, plus checks that the records are consistent. The word would be earned only by composition rules with checkable properties that have survived testing. Until then it is an aspiration and is not used for any file, tool, or claim in this repository.
