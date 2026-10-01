# Mission 01 Claim Set — Gate 4 Approved Bounded Record

- **Status:** `APPROVED_BOUNDED_CLAIM_SET`
- **Pre-registration:** `cbd4e4a081d0b5b1af8a062b6cdf5c4a4ac7d4e7`
- **Gate 3 disposition:** Accepted as a limited diagnostic; see `gates/gate3_execution.md` and `reviews/REV-01_methodological_review.md`.
- **Gate 4 human decision:** `APPROVE_BOUNDED` (2026-10-01; recorded in `gates/gate4_claim.md` and friction-log event F-013).
- **Outcome class:** `inconclusive_result` for the broad local-to-global / agent-coordination research question, with C01–C03 approved only as finite-scope descriptive findings.

> **Interpretive ceiling:** The claims below describe outputs of fixed, manually constructed variants and deterministic code paths in the audited `rl_eval_generator` cohort. “Type I/gluing” and “Sheaf-Cocycle” are retained as frozen field/protocol labels, not as mathematical results. No claim is made about an ordinary sheaf failing its gluing axiom, a Čech cohomology class, independent LLM agents, or Astra-vs-swarm performance.

---

## Claim C01 — Existing judges accepted designated bypass variants in the fixed cohort

- **CLAIM:** At `seed=42`, among the fixed 21-environment cohort and the pre-registered hand-constructed candidate variants, the existing `Grader A` accepted at least one `law_bypass_type1` variant that the implemented `AUDIT_DISPATCH` reference oracle rejected in **1/12 Stratum A1 environments** (`8.33%`, `95% Wilson interval 1.49%–35.39%`) and **4/9 Stratum A2 environments** (`44.44%`, `95% Wilson interval 18.88%–73.33%`). The single A1 case is in Discovery; no such Type I-A event was observed in the A1 Holdout slice (`0/9`, upper Wilson bound 29.91%). These are cohort- and variant-construction-specific rates.
- **EVIDENCE:** `mission-01/results/part_a_stratum_a1.json` (`beta_A_glue_discovery`, `beta_A_glue_holdout`, `beta_A_glue_total`, per-environment variants); `mission-01/results/part_a_stratum_a2.json` (`beta_A_glue_a2`, per-environment variants); `mission-01/results/part_a_confidence_intervals_addendum.json` (`beta_A_glue_environment_level`); `mission-01/results/blackbox_hashes.json` (`judge_excluded: true`, fixed seed).
- **HYPOTHESIS SUPPORTED:** H1 only at the level of observing some operational false-pass cases. **The registered H1 headline threshold is not met:** A1 is `1/12`, below the preregistered `50%` requirement; A2 is `4/9`, also below `50%`.
- **ALTERNATIVE EXPLANATION:** The candidate families and oracle predicates were manually constructed. The oracle's semantic correctness was not independently validated; the fixed cohort is not a probability sample of coding tasks; the A1/A2 selection and prior hardening differ.
- **CONTROL:** `CTRL01` black-box hash/judge exclusion; `CTRL02` strict stratum separation; `FALS-01` variant-count sensitivity; `FALS-02` syntax/import check for `reference_alt` candidates.
- **REMAINING UNCERTAINTY:** No random sample of patches from independent language models was collected. `evaluate_grader_b()` calls `evaluate_truth_oracle()` with the same `AUDIT_DISPATCH`, so the 170/170 agreement cannot independently validate the oracle.
- **CLAIM CEILING CHECK:** **PASS**, only as a descriptive result for these fixed environments, variants, seed, and implemented oracle. No general benchmark or LLM-evaluation rate is claimed.
- **FALSIFICATION STATUS:** **Weakened at the registered headline threshold.** FALS-01 found a larger variant-count sensitivity in A2 than A1; it does not rescue the unmet H1 threshold.

---

## Claim C02 — Oracle-accepted alternatives disagreed with Grader A in Stratum A2

- **CLAIM:** Under the implemented reference-oracle predicate, `Grader A` rejected **7/27 Stratum A2 `reference_alt` executions** (`25.93%`, `95% Wilson interval 13.17%–44.68%`) that the oracle classified as passing, across `functorial_augmentation`, `monadic_reward`, `sheaf_physical_constraints`, and `sheaf_invariant_gluing`; A1 had **0/29** such rejections. All `56/56` `reference_alt` executions had zero syntax/import errors under the pre-registered control. This is a disagreement with the constructed oracle, not an independently established count of valid real-world implementations.
- **EVIDENCE:** `mission-01/results/part_a_stratum_a1.json` (`gamma_A_total`, variants); `mission-01/results/part_a_stratum_a2.json` (`gamma_A_a2`, `gamma_A_variant_level_a2`, environment list); `mission-01/results/type2_gauge_audit.json`; `mission-01/results/part_a_confidence_intervals_addendum.json` (`gamma_A_variant_level`); `mission-01/falsification/falsification_results.json` (`FALS-02`).
- **HYPOTHESIS SUPPORTED:** The operational Type II mismatch mechanism described by H2 is observed in Stratum A2 only; this is **not support for the registered cohort-wide H2 claim**. The `gamma_A > 0.20` cohort requirement is not met on the pooled environment rate (`4/21 = 19.05%`); A1 is `0/12`, so a uniform claim across hardened and compile-only judges is rejected.
- **ALTERNATIVE EXPLANATION:** The public task prompts leave some semantics underdetermined, and the `reference_alt` families encode one interpretation. The reference oracle and Grader B share the same dispatcher and were not externally adjudicated.
- **CONTROL:** `CTRL02` stratification; `CTRL05` zero syntax/import errors; `CTRL06` reference-oracle polarity; `FALS-02` multi-variant audit.
- **REMAINING UNCERTAINTY:** Independent domain adjudication of each alternative implementation is absent. In particular, hidden judge conventions may or may not be the only interpretation of an under-specified task prompt.
- **CLAIM CEILING CHECK:** **PASS**, only for the enumerated alternative variants and the implemented oracle's classification. Do not call these independently verified “valid global sections.”
- **FALSIFICATION STATUS:** **Partially supported at A2; not supported as a cohort-wide or universal judge property.**

---

## Claim C03 — Implemented checker arms differ over a finite generated workspace set

- **CLAIM:** In the deterministic Part B generator, which produced `27` designated workspace variants for each of six tasks (`162` total), the implemented `Chart-Only`, `Pairwise-Tree`, `Pairwise-UpToGauge`, `Circular-AG`, and historically named `Sheaf-Cocycle` predicates yielded orbit-failure fractions of **0.6111, 0.1605, 0.2963, 0.0741, and 0.0000**, respectively. The `Sheaf-Cocycle` checker therefore differed from `Pairwise-Tree` by `16.05` percentage points and from `Circular-AG` by `7.41` points on this exact generator; its conditional accepted-handoff FPR difference from `Circular-AG` was `20.10` points.
- **EVIDENCE:** `mission-01/results/part_b_multichart_gluing.json` (`summary`, per-environment results, generated orbit records); `mission-01/falsification/falsification_results.json` (`FALS-03`, `FALS-03b`).
- **HYPOTHESIS SUPPORTED:** Only the numerical comparator component of H3 is supported by these **implemented predicates on this finite constructed set**; the full registered H3 conjunction is mixed (see the hypothesis disposition below). This does not establish an ordinary sheaf model, a cohomological obstruction, or improved multi-agent composition.
- **ALTERNATIVE EXPLANATION:** The workspace generator, compatibility predicates, and reference oracle were designed together. The `Sheaf-Cocycle` name should be read as an implementation-arm label. No separately dispatched agents or human integration were involved.
- **CONTROL:** `FALS-03` finite enumeration against `Pairwise-Tree`; `FALS-03b` comparison against `Circular-AG`; the table in `gates/gate3_execution.md` gives per-task results.
- **REMAINING UNCERTAINTY:** No Protocol A/B/C agent trial; no independent oracle review; no formal definitions or computation of a Čech cocycle/cohomology class; no population sampling.
- **CLAIM CEILING CHECK:** **PASS** only as finite implementation-level arithmetic. The `15 pp` unconditional threshold against `Circular-AG` in `FALS-03b` was **not met** (`7.41 pp`); the `20.10 pp` conditional FPR difference is retained as a separate conditional metric and does not substitute for that failed threshold.
- **FALSIFICATION STATUS:** `FALS-03` met its registered finite-set margin versus `Pairwise-Tree`; `FALS-03b` failed its `15 pp` unconditional margin versus `Circular-AG`. No theoretical or real-agent claim survives from this result.

---

## Hypothesis disposition (preserved, not averaged)

| Hypothesis | Gate 4 disposition |
| :--- | :--- |
| **H0** | The fixed-cohort A1 `beta_A_glue` rate is below `0.20` (`1/12`), but the Part B `Chart-Only` minus `Sheaf-Cocycle` failure-rate difference is `0.6111`, exceeding the registered `0.10` parity bound. Thus the operationalized compound null is **not supported**; this is not a population-level conclusion. |
| **H1** | Registered A1 `50%` headline threshold **not met** (`1/12`); ABORT-01's Holdout replication warning is retained. Operational false-pass cases are recorded in C01. |
| **H2** | A2-only oracle disagreement observed; pooled environment rate is `4/21 = 19.05%`, below the registered `>20%` cohort threshold, with only two systematic-rejection environments (fewer than the five required for a benchmark-wide systematic claim). Uniform claim rejected. |
| **H3** | Mixed finite-set result: `Sheaf-Cocycle` is `0/162`; its margin over `Pairwise-Tree` is at least 5 pp on the cyclic environments, and its margin over `Circular-AG` is at least 5 pp on four of six. However, the registered `>=20%` `Pairwise-Tree` failure-rate premise is not met overall (`0.1605`), and the stricter `FALS-03b` 15 pp unconditional margin against `Circular-AG` failed. No cohomological interpretation or actual multi-agent test. |
| **H4** | **Not adjudicable:** M07 inputs are hard-coded source constants without linked independent solo-agent outputs (`reviews/post_run_analysis_errata.yaml`). |
| **H5** | **Not adjudicable:** M08 `E_J/E_O` sets are hard-coded in `NERVE_METADATA`, not independently measured (`reviews/post_run_analysis_errata.yaml`). |

## Quarantined measurements and remaining critiques

- Decision-table/posterior-shaped values are preserved but are not calibrated Bayesian posteriors (`reviews/posterior_audit.yaml`).
- M10 and Mission 01's total coordination-efficiency ratios are not estimable because the real-time log is incomplete; the recorded zero in `summary_metrics.json` is invalid (`reviews/post_run_analysis_errata.yaml`).
- M09 AST/LOC counts are descriptive code-size measurements, not grader accuracy or runtime efficiency.
- Council prompts were leading; no Mindcluster export/context pack informed Mission 01.
- The current repeat of the target test suite could not collect due to missing `torch`; the earlier recorded 17-test pass is retained, but no fresh rerun is claimed.
- The protocol amendment and retrospective overlap manifest were made after execution and were not treatments in the locked experiment.

## Explicit cannot-justify list (Gate 2 preserved)

Mission 01 cannot justify:

- Mathematical novelty for sheaf theory, restriction maps, or Čech cohomology; being the first to propose sheaf cohomology for multi-agent AI/RL; pairwise-compatible non-gluing in an ordinary sheaf; or that cyclic dependencies require sheaf theory.
- A pooled, unstratified A1/A2 headline rate, or conflation of Type 0 lookup-table false passes with Type I bypasses.
- General LLM-judge failure rates, ecological multi-agent gauge-collision rates, or use of uniform combinatorial gauge-mixing failure as an ecological rate.
- Efficacy of explicit boundary contracts for real agents; independent-agent A/B/C results; or an Astra-vs-swarm advantage.
- Systematic benchmark-wide H2 absent the required independent variants/environments; H4/H5 empirical support; calibrated Bayesian posteriors or posterior collapse; or general Grader B accuracy inferred from agreement with the shared TruthOracle dispatcher.
- A paper-title/abstract claim of sheaf cohomology or cocycle lift unless the frozen claim-ceiling condition is met; this packet does not authorize publication in any case.
- Any SWE-ABS citation without a resolvable primary arXiv/DOI identifier; no such citation is used in this claim set.
