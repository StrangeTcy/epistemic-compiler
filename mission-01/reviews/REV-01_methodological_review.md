# REV-01 — Post-Execution Methodological Review & Disposition

- **Source:** User-provided external review attributed to “GPT 5.6 luna” (the review text was supplied in the conversation; this file is our structured disposition, not a new model run).
- **When:** After WP-01..WP-07 had run and before Human Gate 3 sign-off.
- **Affected mission:** `mission-01`.
- **Pre-registration:** `cbd4e4a081d0b5b1af8a062b6cdf5c4a4ac7d4e7` remains immutable.
- **Disposition:** Preserve all executed artifacts as historical evidence; do not rewrite `spec/approved.yaml`, seed, Council responses, or raw result JSON. Correct the interpretation and protocol prospectively. Mission 01 has **not** tested the proposed Astra-vs-swarm comparison.

---

## 1. Mathematical correction: a sheaf is not the failed-gluing premise

For a genuine sheaf `F` on a cover `{U_i}`, a family `s_i ∈ F(U_i)` whose restrictions agree on every overlap is a matching family, and the sheaf axiom supplies a unique global section. Therefore the conjunction “all pairwise restrictions agree” and “there is no global section” cannot be an ordinary sheaf counterexample.

Three objects must not be conflated:

1. A **presheaf of locally admissible artifacts** with restriction maps, which need not satisfy the sheaf axiom.
2. **Boundary/interface compatibility**, operationally tested by canonical projections into a shared boundary schema.
3. **Descent or cohomological obstruction**, which requires explicit transition maps, a specified coefficient/group structure, a defined cocycle/coboundary and equivalence relation, and a reason the resulting invariant is the relevant obstruction.

A non-zero product such as `g31 g23 g12 != 1` can describe holonomy when the group action and transitions are defined. It is not, by itself, a demonstrated Čech `H^1` computation. The executed labels `Sheaf-Cocycle` and `holonomy` are retained for historical alignment with the frozen spec, but should be described as names for the benchmark's implemented compatibility predicates/orbit labels—not as proof of a sheaf theorem or a measured cohomology class.

**Prospective change:** The amended `research_protocol/protocol.md` makes presheaf/sheaf/descent language a candidate formalism and adds the sheaf-axiom caveat. The amendment does not rewrite the frozen Gate 2 specification.

---

## 2. Canonical interface ownership

The review correctly notes that a package should not define its own shared-interface semantics. A mission-level overlap manifest should be authored and frozen before execution; WPs may reference it, not redefine it.

`mission-01/work_packages/overlaps.yaml` is now explicitly marked **retrospective and not used in the locked run**. The completed WP files remain byte-for-byte at their post-execution, pre-review versions; the temporary `canonical_overlaps_instantiated` additions were removed. This draft can inform a future registration, but cannot be cited as an executed Mission 01 control.

For the concrete `rope` interface, the future contract should state that `position_offset()` is read **before** appending the current chunk, returns the number of tokens seen before that chunk, and is then advanced by `append(chunk_len)`. This is a useful engineering boundary contract; it is not automatically a sheaf restriction map.

---

## 3. Corrected repository-grounding notes

The external reviewer inspected current target-repository files. The relevant corrections are:

- `rope` is a concrete three-file integration task: `envs/rope/files/rope.py`, `attention.py`, and `cache.py`. The current `attention.py` uses `offset = 0`; `cache.py` has placeholders for the offset and append update; and `rope.py::_angles()` currently uses `torch.arange(seq_len)` when positions are omitted, ignoring its `offset` parameter. A future boundary contract must cover both the pre-advance cache read/advance order and the absolute-index semantics of the RoPE implementation.
- `compositional_optimizer`'s judge does **not** merely make one update at `t=1`. It computes `v1 = opt1.update(p, g)` and then `v2 = opt2.update(p, v1)` for two separate module instances, checking a narrow `state_isolated` property. It does not test a long repeated-update horizon or general associativity, despite the task description. This is a specification/judge mismatch, not evidence for a sheaf theorem.
- `categorical_lenses` checks the listed lens laws but does not anchor the intended coordinate interpretation such as `view((x,y)) == x`; this is an observability/specification issue.
- `sheaf_physical_constraints`'s public prompt specifies local and global capacity bounds but not the judge's hidden `5:3` ratio. This supports a public-specification/judge-semantics mismatch; it is not an “internal sheaf contradiction.”

These facts do not change the locked input or results. Any future seed must fix the inaccurate `compositional_optimizer` statement before measurement design.

---

## 4. Mission 01's actual scope versus the proposed two-arm research program

The external review distinguishes:

- **Dual A — evaluator observability:** what a benchmark judge certifies or rejects.
- **Dual B — distributed construction:** what separate agents build under decomposition and whether their artifacts integrate.

Mission 01 preregistered both, but its execution does **not** contain the proposed causal comparison of:

- A: independent local agents with ordinary signatures;
- B: local agents with explicit boundary contracts;
- C: one agent with global task context.

Part B evaluates a deterministic, finite set of generated chart/workspace variants (162 tuples over six tasks) against implemented protocol predicates. It does not dispatch independent language-model agents, measure real integration/re-dispatch burden, or compare inference/token cost. Thus Part B can be reported as an **enumerated compatibility stress test of those implementations**, not as an estimate of swarm performance or evidence that contracts help real agents. Part A is a separate evaluator audit and cannot be treated as the same causal experiment.

The appropriate claim ceiling at Gate 3 must therefore exclude “Astra-vs-swarm,” general agent coordination, real-world contract efficacy, and cohomological novelty. Any claim about a result must remain conditional on the audited `rl_eval_generator` cohort, the constructed variants, the implemented oracles, and the fixed protocol predicates.

---

## 5. Additional implementation audit: M07/M08 and oracle agreement

A source-level audit after the external review found three further limitations that must be resolved before any claim extraction:

- `tools/gauge_and_parsimony_analysis.py` defines `SOLO_CHART_EMPIRICAL_SAMPLES` as literal source constants with `k_samples_per_chart: 5`; the reported `4/5`, `2/5`, etc. have no linked raw completions, model-run IDs, or provenance artifacts in this workspace. They are **hand-entered counts**, not demonstrated independent solo-agent samples. Consequently M07 (`\hat{\kappa}`, `\hat{g}`), its “empirical prior-weighted collision” rates, and H4's ecological/shared-prior interpretation are not empirical evidence and are quarantined.
- `tools/multichart_gluing_benchmark.py:NERVE_METADATA` hard-codes `E_J` and `E_O`; M08 computes Jaccard from those metadata lists. The reported `16/18 = 0.8889` is a deterministic comparison of hand-entered edge annotations, not a measured independent evaluator/orchestrator co-location. H5 is not empirically tested by this artifact.
- `tools/grader_b_and_truth_oracles.py:evaluate_grader_b()` calls `evaluate_truth_oracle()`, which dispatches the same `AUDIT_DISPATCH` function. Thus the reported 170/170 agreement between Grader B and TruthOracle is true by implementation design (apart from the patch-validity wrapper), not an independent validation of oracle accuracy. Part A remains a comparison of existing judges with a constructed reference oracle; the oracle itself requires an independent audit.

These are source-code facts, not inferential interpretations. The generated files are retained, but those metrics must be described as constructed/implementation-defined and cannot support H4/H5 or a claim of independently validated Grader B performance.

---

## 6. Statistical and process-metric quarantine

Two derived outputs require explicit caveats before Gate 4:

1. **Bayesian posterior fields:** The pre-registered outcome regimes are threshold flags that can overlap (for example, O4 is defined in terms of O3, while O5/O6 are abort flags), so they do not form a mutually exclusive observation partition even though the numerical likelihood entries sum to one over the listed rows for each hypothesis. The Skeptic's `H4_or_Residual` mass was later split between H4/H5, and the composite `O4^0.50 × O3^0.30 × O6^0.20` weighting was not a pre-registered joint-likelihood model with a dependency/factorization justification. Thus the composite posterior-shaped numbers in `summary_metrics.json` and `falsification_results.json` are **not calibrated Bayesian posteriors** and must not be used as inferential evidence. Individual row updates are, at most, illustrative conditional reweightings under subjective likelihoods. All generated values are preserved; a post-run audit is recorded in `posterior_audit.yaml`.
2. **M10 / coordination efficiency:** `summary_metrics.json` records zero human interventions even though the legacy friction log contains F-001..F-007 and the execution history includes code/test repairs. The log was not complete in real time, and its old manually entered duration estimates do not have observed start/end timestamps. Consequently M10's zero is invalid; Mission 01's full intervention/time totals and `κ` ratios are **not estimable** from the current record. Preserve the seven legacy events and report their total reported duration separately (24 minutes, as originally entered), not as a derived measurement.

A corrected append-only logging schema and migration notes are now in `research_protocol/instrumentation.md` and `mission-01/friction_log.yaml`. The historical timezone conversion is marked as inferred rather than independently verified.

---

## 7. Council and typed-IR limitations

- The four Mission 01 prompts were leading: they substantially specified the sheaf framing and repository-specific conclusions before the roles critiqued it. Their verbatim prompts and responses remain part of the historical record; the Council cannot be retrospectively described as independent discovery of the framing.
- The protocol's identifiers and YAML conventions are a **protocol-defined research IR**, not a machine-validated graph. `scripts/validate_ir.py` has not been implemented and is deferred; no claim of automated `C → H → X → M → E` enforcement is made.
- The user Mindcluster export was not available to Mission 01's Council. A schema-only `knowledge/` shell and small deterministic lexical/hop retriever are now present for prospective use. No research nodes or sources were invented, and no Mission 01 context pack was generated or used.

For a future Council, compile one shared evidence pack with stable source/claim provenance, then attach role-specific emphasis. The roles must be allowed to reject the proposed formalism, operationalization, and novelty claim.

---

## 8. Prospective redesign (not executed or preregistered)

A new mission or explicitly re-registered revision should make Dual B primary and test the causal claim directly. Candidate design:

- **A:** split task among independent agents with ordinary signatures/local tests;
- **B:** same decomposition with a mission-owned canonical boundary contract;
- **C:** one agent receives the full task context.

Start with `rope` and select two or three more tasks only after verifying that each requires a real multi-file change. Hold model, task, sampling, retry budget, and evaluation constant as far as feasible; randomize/run multiple seeds; use a blinded global evaluator. Measure local pass, global success, semantic integration failures, repair/re-dispatch count, human coordination time, token/inference cost, and missing-context explanations. Keep evaluator-oracle audit (Dual A) as a separate study or an explicitly secondary factor. Define the contract before dispatch, and do not assume that its best mathematical description is a sheaf.

This is a proposal for a new registration, not a retroactive analysis of the existing 162 tuples.

---

## 9. Gate 3 decision requested

Human Gate 3 should decide whether to accept Mission 01 as a **limited V0 diagnostic with the caveats above**, hold it as inconclusive and redesign before claim extraction, or reject the current measurement design and authorize a separately preregistered run. No Gate 4 claims had been extracted or approved at the time of this initial review; see the append-only status update below.

## 10. Post-review Gate Decision Record

On 2026-10-01, the user selected `accept_bounded_record` at Gate 3 and later `approve_bounded` at Gate 4. The approved candidate set is `mission-01/claim_set.md` (C01–C03), with overall outcome class `inconclusive_result` for the broad research question. These decisions authorize only the fixed-cohort/constructed-benchmark descriptive record; they do not authorize publication or theory, H4/H5, calibrated-posterior, or real-agent efficacy claims. The full adjudication record is in `mission-01/gates/gate3_execution.md` and `mission-01/gates/gate4_claim.md`.

## 11. Post-Gate-4 Mindcluster Import and Prospective Architecture Note

After Gate 4, the user-uploaded `epistemic_research_graph(2).html` was imported to `knowledge/` (118 nodes, 301 edges, 77 source records including the export). External links and graph annotations remain unverified; no context pack informed Mission 01, and the import makes no retroactive change to its registration or claims.

The follow-up architecture reflection separates two pilot observations: (1) human context/coordination work is a qualitative runtime-interface requirement signal, not an estimable intervention/time/cost result because the friction log is incomplete; (2) the mission's sheaf framing/prompt ontology was a distinct research-design defect. V0 remains a research-control layer above a replaceable runtime; this repository does not implement a persistent agent swarm. A future registered question may operationalize local validity → declared boundary compatibility → global validity, with mathematical formalisms treated as candidate models. This is prospective only; see the updated project README.
