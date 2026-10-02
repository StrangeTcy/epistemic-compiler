# Epistemic Compiler — Research Protocol & Mission 01

> V0 is a **protocol-defined research IR**, not a machine-enforced typed graph or an autonomous research factory. It combines provenance conventions, four human gates, manually executed work packages, and a real-time friction-log schema. Mathematical formalisms (sheaves, presheaves, descent, assume-guarantee contracts, relational joins) are candidates to be justified, not premises.

## Current State

- Mission 01 executed WP-01..WP-07 and the pre-registered falsification suite against `StrangeTcy/rl_eval_generator`.
- Pre-registration lock: `cbd4e4a081d0b5b1af8a062b6cdf5c4a4ac7d4e7`.
- Initial combined target-repository test run: **17 passed** (historical); a later repeat could not collect two harness modules because the resumed sandbox lacked `torch`, so no fresh target-suite pass is claimed. The 17 tests verify listed engineering behavior, not mathematical gluing proofs.
- Post-Gate-4 Mindcluster importer/retriever checks: **9 passed** (`tests/test_import_mindcluster_html.py` + `tests/test_retrieve_context.py`), including graph integrity, provenance, uncertainty preservation, and candidate-link rendering.
- Strategy IR v0.2 draft checks: **149 passed** (`tests/test_validate_ir.py`: 113; `tests/test_retrieve_strategies.py`: 36). Further tests check that the frozen Mission 02 cards and features are unchanged (`tests/test_mission_02_freeze.py`) and that the Mission 03 proposal is internally consistent and its power table reproduces (`tests/test_mission_03_proposal.py`). The full suite (`python -m pytest`) is **163 passed** at the time of writing. These tests show that the validator and the matcher behave as specified (structural rules, three-valued matching, failing closed on invalid input). They say nothing about whether any strategy helps.
- Mission 01 has **human approval through Gate 4 as a bounded diagnostic**. The user accepted `accept_bounded_record` at Gate 3 and approved C01–C03 at Gate 4; the broad local-to-global / agent-coordination question is classified `inconclusive_result`. See `mission-01/gates/` and `mission-01/claim_set.md`.
- Preserve the locked spec and raw results. Do not infer a general sheaf theorem, cohomology class, real-agent contract benefit, or Astra-vs-swarm advantage from this run. Part B is a deterministic enumerated compatibility stress test, not a comparison of independent LLM agents.
- The Gate 2 decision-table update outputs are quarantined as exploratory, not calibrated Bayesian posteriors. Mission 01 coordination-efficiency metrics are not estimable from the incomplete real-time friction log.
- Mission 02 (started 2026-10-02) is at its **kickoff**: `mission-02/seed.yaml`, an evidence digest and four Council prompts exist, and **two of four Council roles have been stored** (the Theorist, and the Experimentalist with two samples); the cross-critique and Gate 1 wait for the Skeptic and the Prior-Work Killer. It asks what a higher-order epistemic-game instance family needs for independently checkable ground truth, and registers a comparison of trigger-matched strategy packs against controls. Nothing in it has been run. Its seed lists published work on dynamic-epistemic-logic benchmarks for LLMs and on strategy and template retrieval as collisions to be checked, not as open ground.
- Mission 03 is a **proposal** (`mission-03/`, 2026-10-02): a matched/mismatched comparison of two strategy cards on two hardened task families, gated by a blind-characterization stage and a pilot. Nothing has been run. `mission-03/DESIGN.md` states what was checked and what was not, and why it is recommended before Mission 02.

## Architecture Boundary & Pilot Lessons (Prospective)

The intended product boundary is a research-control layer above a replaceable agent runtime—not a hand-built swarm runtime. V0 provides the research-memory schema/retriever, mission design conventions, provenance, human gates, and validation/claim controls; it does **not** provide persistent agents, dispatch, a DAG runtime, automatic delegation, or a research-factory framework. Do not expand runtime machinery without a separately justified need.

A draft Strategy IR (v0.2) separates procedural problem transformations from declarative Mindcluster memory and from runtime execution. It consists of a schema, thirteen **agent-proposed, unreviewed `candidate`** cards (five of them, in the `game` family, written for Mission 02), two **illustrative** episodes, a structural validator, and a deterministic trigger matcher. There is still no automatic strategy selector, application engine, or promotion mechanism, and nothing yet shows that any strategy helps: the empirical gate that would decide whether to extend it (`research_protocol/strategy_ir.md`, section 10) has not been run. See `research_protocol/strategy_ir.md` and `strategies/README.md`.

Mission 01's manual execution is retained as a pilot, but its lessons are kept separate: (1) the human had to perform runtime-like context/coordination work, which is a qualitative design observation only because the friction log is incomplete and total burden/κ is not estimable; and (2) the initial mission framing had a conceptual/methodological defect, documented in `mission-01/reviews/REV-01_methodological_review.md`. A future registration may begin with **local validity → declared boundary compatibility → global validity**, treating sheaf/presheaf/descent formalisms as candidate models rather than premises. This is a prospective design direction, not a retroactive result or revision of Mission 01's frozen registration.

## Repository Layout

```text
.
├── README.md
├── research_protocol/
│   ├── protocol.md             # Ontological separation, provenance, Gates 1–4, canonical boundary contracts, optional strategy-pack step
│   ├── instrumentation.md      # Append-only friction schema, controlled vocabulary, coordination efficiency
│   ├── strategy_ir.md          # Strategy IR v0.2 draft: schema, matching rule, episode records, promotion policy, empirical gate
│   ├── strategy_families.yaml  # Twelve proposed trigger families (legacy registry; no promoted strategies)
│   └── structural_features.yaml # Feature vocabulary shared by triggers and problem states (proposed, unvalidated)
├── strategies/                 # Thirteen candidate cards (agent-proposed, unreviewed) + two illustrative episodes; see its README
├── knowledge/                  # Imported 118-node Mindcluster graph with source/edge provenance caveats
├── scripts/import_mindcluster_html.py # Safe literal-JSON importer for the uploaded HTML export
├── scripts/retrieve_context.py # Deterministic lexical + graph-hop context compiler (no vector DB)
├── scripts/validate_ir.py      # Structural validator for Strategy IR artifacts only (not seeds, specs, or claim sets)
├── scripts/retrieve_strategies.py # Deterministic trigger matcher -> strategies.md + manifest; selects and applies nothing
├── tests/test_import_mindcluster_html.py
├── tests/test_retrieve_context.py
├── tests/test_validate_ir.py
├── tests/test_retrieve_strategies.py
├── tests/test_mission_02_freeze.py # Change-detector for the frozen Mission 02 cards and features
├── tests/test_mission_03_proposal.py # Traceability of the Mission 03 proposal and reproducibility of its power table
├── mission-02/
│   ├── seed.yaml               # S02: higher-order epistemic-game instances and a registered strategy-pack comparison (kickoff)
│   ├── council/                # Round-1 prompts for the four roles and run instructions; no responses collected yet
│   ├── context/                # Evidence digest and retrieval manifest
│   ├── sources/                # Notes on user-supplied background material (unverified claims flagged)
│   └── freeze/                 # Hashes of the frozen game-family cards and features
├── mission-03/
│   ├── seed.yaml               # S03: does matching a strategy to a task's structure matter? (proposal; nothing run)
│   ├── DESIGN.md               # Design note: question, evidence, comparison, kill attempts, power, decisions for a human
│   ├── candidate_measurements.yaml # Measurements, controls, stop conditions, decision regimes, falsification tests (candidate)
│   ├── work_packages/          # Candidate work packages (pre-Gate 2)
│   └── analysis/               # Reproducible power simulation and its output
└── mission-01/
    ├── seed.yaml               # Historical pre-registration seed; inaccurate statements are documented in REV-01
    ├── council/                # Four completed role responses and original prompts
    ├── critiques/              # Cross-critique and preserved disagreements
    ├── spec/                   # Draft and Gate-2-frozen approved spec
    ├── work_packages/          # WP-01..WP-07; overlaps.yaml is retrospective only
    ├── results/                # Generated audit, benchmark, and summary artifacts
    ├── falsification/          # WP-07 falsification output
    ├── reviews/                # Post-run review, migration snapshots, and analysis errata
    └── gates/                  # Human Gate packets; Gate 4 approves the bounded claim set
```

## Mindcluster Retrieval (Prospective)

The user's knowledge graph is designed as source records, claim-bearing nodes, and typed edges. Source-backed claims remain distinct from interpretive relations. `scripts/retrieve_context.py` compiles one shared evidence view plus role-specific packs and a provenance manifest using deterministic lexical matches and explicit graph hops. No embeddings, external searches, orchestration runtime, or automated truth validator are included.

The user-uploaded `epistemic_research_graph(2).html` was imported after Mission 01: `knowledge/` now contains 118 nodes, 301 directed edges, and 77 source records (including the export itself). The importer records the HTML hash and Git provenance without executing scripts; its external links and annotations remain unverified, and uncertain edges are preserved. Mission 01's Council did not receive compiled context packs; do not describe it as mindcluster-informed. See `knowledge/README.md` for import scope, caveats, and usage.

## Strategy IR (Prospective)

The Strategy IR records candidate **problem transformations** ("strategies") so that a transformation which was tried leaves an inspectable trace. A card states a trigger as a conjunction of features from a shared vocabulary, a move, obligations, failure modes, and how it would be falsified. A *problem state* declares which features hold, with evidence. An *episode* records which strategies were applied, which obligations were checked, and what happened.

- `scripts/validate_ir.py` checks that these documents are well-formed and internally consistent: references resolve, success outcomes have every obligation checked, a `solved` claim has an unbroken chain, and a status above `candidate` has the review and evidence records it requires. It does not check that a feature is true, that a check was sound, or that a strategy works.
- `scripts/retrieve_strategies.py` compares a problem state's declared features with each card's trigger and writes a candidate pack. Absent and unknown features are distinguished, a declared absence blocks a card, and a match is presented as a hypothesis about applicability. It fails closed on an invalid library or state. It does not choose or apply a strategy.
- Retrieval is only as good as the problem characterization behind it, which remains a human or agent judgment. All cards are unreviewed candidates, the library covers 7 of the 12 families, and the two episodes are illustrative and carry no evidential weight. Mission 01 did not use any of this and appears only as a bounded-pilot exemplar and one counterexample on a single card.

See `strategies/README.md` to use it and `research_protocol/strategy_ir.md` for the schema and rules.

## Target Repository

- [`StrangeTcy/rl_eval_generator`](https://github.com/StrangeTcy/rl_eval_generator)
- Mission branch: `mission-01/sheaf-gluing-protocol`
- Gate decisions and approved bounded claims: `mission-01/gates/gate3_execution.md`, `mission-01/gates/gate4_claim.md`, and `mission-01/claim_set.md`.
- The uploaded HTML arrived on remote `main` in commit `2e3847a`; that commit was merged locally before importing it, preserving the user's upload in history.
