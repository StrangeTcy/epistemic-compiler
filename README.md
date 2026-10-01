# Epistemic Compiler — Research Protocol & Mission 01

> V0 is a **protocol-defined research IR**, not a machine-enforced typed graph or an autonomous research factory. It combines provenance conventions, four human gates, manually executed work packages, and a real-time friction-log schema. Mathematical formalisms (sheaves, presheaves, descent, assume-guarantee contracts, relational joins) are candidates to be justified, not premises.

## Current State

- Mission 01 executed WP-01..WP-07 and the pre-registered falsification suite against `StrangeTcy/rl_eval_generator`.
- Pre-registration lock: `cbd4e4a081d0b5b1af8a062b6cdf5c4a4ac7d4e7`.
- Initial combined target-repository test run: **17 passed** (historical); a later repeat could not collect two harness modules because the resumed sandbox lacked `torch`, so no fresh target-suite pass is claimed. The 17 tests verify listed engineering behavior, not mathematical gluing proofs.
- Post-Gate-4 Mindcluster importer/retriever checks: **9 passed** (`tests/test_import_mindcluster_html.py` + `tests/test_retrieve_context.py`), including graph integrity, provenance, uncertainty preservation, and candidate-link rendering.
- Mission 01 has **human approval through Gate 4 as a bounded diagnostic**. The user accepted `accept_bounded_record` at Gate 3 and approved C01–C03 at Gate 4; the broad local-to-global / agent-coordination question is classified `inconclusive_result`. See `mission-01/gates/` and `mission-01/claim_set.md`.
- Preserve the locked spec and raw results. Do not infer a general sheaf theorem, cohomology class, real-agent contract benefit, or Astra-vs-swarm advantage from this run. Part B is a deterministic enumerated compatibility stress test, not a comparison of independent LLM agents.
- The Gate 2 decision-table update outputs are quarantined as exploratory, not calibrated Bayesian posteriors. Mission 01 coordination-efficiency metrics are not estimable from the incomplete real-time friction log.

## Architecture Boundary & Pilot Lessons (Prospective)

The intended product boundary is a research-control layer above a replaceable agent runtime—not a hand-built swarm runtime. V0 provides the research-memory schema/retriever, mission design conventions, provenance, human gates, and validation/claim controls; it does **not** provide persistent agents, dispatch, a DAG runtime, automatic delegation, or a research-factory framework. Do not expand runtime machinery without a separately justified need.

A draft, first-class Strategy IR proposal now separates procedural problem transformations from declarative Mindcluster memory and from runtime execution. Its trigger-first taxonomy is explicitly unvalidated; there is no automatic strategy selector, application engine, or promotion mechanism yet. See `research_protocol/strategy_ir.md` and `research_protocol/strategy_families.yaml`.

Mission 01's manual execution is retained as a pilot, but its lessons are kept separate: (1) the human had to perform runtime-like context/coordination work, which is a qualitative design observation only because the friction log is incomplete and total burden/κ is not estimable; and (2) the initial mission framing had a conceptual/methodological defect, documented in `mission-01/reviews/REV-01_methodological_review.md`. A future registration may begin with **local validity → declared boundary compatibility → global validity**, treating sheaf/presheaf/descent formalisms as candidate models rather than premises. This is a prospective design direction, not a retroactive result or revision of Mission 01's frozen registration.

## Repository Layout

```text
.
├── README.md
├── research_protocol/
│   ├── protocol.md             # Ontological separation, provenance, Gates 1–4, canonical boundary contracts
│   ├── instrumentation.md      # Append-only friction schema, controlled vocabulary, coordination efficiency
│   ├── strategy_ir.md          # Draft problem-transformation IR; human reviewed, not implemented/validated
│   └── strategy_families.yaml  # Twelve proposed trigger families; no promoted strategy cards yet
├── knowledge/                  # Imported 118-node Mindcluster graph with source/edge provenance caveats
├── scripts/import_mindcluster_html.py # Safe literal-JSON importer for the uploaded HTML export
├── scripts/retrieve_context.py # Deterministic lexical + graph-hop context compiler (no vector DB)
├── tests/test_import_mindcluster_html.py
├── tests/test_retrieve_context.py
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

## Target Repository

- [`StrangeTcy/rl_eval_generator`](https://github.com/StrangeTcy/rl_eval_generator)
- Mission branch: `mission-01/sheaf-gluing-protocol`
- Gate decisions and approved bounded claims: `mission-01/gates/gate3_execution.md`, `mission-01/gates/gate4_claim.md`, and `mission-01/claim_set.md`.
- The uploaded HTML arrived on remote `main` in commit `2e3847a`; that commit was merged locally before importing it, preserving the user's upload in history.
