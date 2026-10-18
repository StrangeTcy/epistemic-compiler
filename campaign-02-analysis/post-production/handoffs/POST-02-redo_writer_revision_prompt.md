# POST-02 redo — Stage B2 (Writer revision) prompt

> **Status (2026-10-18): executed directly, not dispatched.** The revision was written in-session as the article at `campaign-02-analysis/posts/POST-02-cross-environment-map.md` (commit `f07e246`), applying the corrections below. No independent Battle Arena Writer round has been run on this prompt. This file is kept as the record of the requested corrections, not as pending work. Dispatch it only if an independent Writer pass is wanted.


Revise the cross-environment map article on Mercury-2.5 using the verified corrections below. Output the full article only, as one Markdown document. Do not include production metadata, notes, or reviewer commentary inside the article.

## Scope and constraints (standing)
- Analysis of archived evidence only. No new runs, no provider calls, no claims of repeated execution.
- Mercury is not Atria. Do not import Atria denominators, exclusions, or categories.
- Do not relabel a retrospective plan as preregistration.
- Public copy: no internal file paths, finding IDs (F-###), trace IDs, or draft labels. Do not mention "the packet", "evidence packet", "source analysis", or "overview document".
- Bracketed tokens such as [ac-word], [d-word], [m-word] are intentional replacements. Keep them as written.
- Every number and strong factual claim must be traceable, with its limitation stated beside it.

## Headline (keep)
- 416 selected cases, 38 environments; 405 scored; 277 PASS, 128 FAIL; 11 unscored (judge-coverage gap, not a third outcome).
- Scored pass rate 277/405 = 68.4%. All-selected 277/416 = 66.6% answers a different question; label it as such.
- Environment outcomes: 17 all-pass (172/172); 12 mixed (105/165, plus 1 unscored); 7 all-fail (0/68); 2 with no scored case (10 unscored).
- Zero-pass environments: functorial_augmentation, monadic_reward, sheaf_invariant_gluing, sheaf_physical_constraints, ts_one_step, ts_trajectory, glyph. The ANALYSIS_OVERVIEW figure of 10 is not reproduced by the environment-level count; state that the reconciliation is open.

## Corrections required (verified)
1. Binary rows: 320 of 329 scored matrix rows take 0 or 1 (97.3%). 9 rows are non-binary, all in moco. (Previous draft said 314 / 95.4%: wrong.)
2. moco: 15 rows, 55 cases, 36/55 pass. 9 rows are fractional; 6 rows sit at 0.0 or 1.0. Do NOT say every moco row is mixed.
3. The tuple-level explanation for the 10 figure is falsified: 19 environments contain at least one zero-pass tuple (98 zero-pass tuples). Say the 10 figure is not reproduced by either the environment-level count (7) or the tuple-level count (19); its source is unexplained.
4. rd_adaptive_halting unscored tuple IS identified: {"batching_complexity":"easy","clue_clarity":"easy","implementation_obfuscation":"easy","recurrence_depth":"easy","visible_tests":"easy"}. Report it as an unscored case at that tuple, with the scored total 8/14 unchanged.
5. Campaign omissions (outside the 416 selected cases): 80 rows in the exclusions record — 56 intervention-twin omissions, 14 known-gate calibration failures, 10 unsupported provider input-modality cases. Per-environment: moco 35, glyph 21, rope 15, epistemic_games 9. State that these are outside the selection frame. Note that the provenance summary gives different counts (24 known-gate, 10 rope); the discrepancy is unresolved and must be stated, not resolved.
6. Rejected dispositions: 10 scored FAIL cases carry case_disposition = rejected: monadic_reward 8 (of its 9 scored), batchnorm_ema 1, transformer_ssm_lift 1. The packet does not define "rejected". Keep all 10 in the counts (disclose-only policy), and state beside the monadic_reward zero-pass claim that 8 of its 9 scored cases carry this disposition, and that its meaning is not defined in the archive.
7. Performance-eligibility: one PASS (ts_parse_only__witness_status=broken_representation=flat__seed-0) is a recorded provider-outage case with performance_eligible = False. Keep it in the 277 count, disclose it beside the headline pass rate.
8. Failure modes: underfit 51, overfit_visible_tests 49, runtime_error 11 (consolidated from RUNTIME_ERROR 9 + runtime_error 2), source_invalid 9, invalid_action 5, training_failed 3. These are global counts; no environment-level breakdown is available.
9. Judge guarantees: 189 behavioral_reference, 227 compile_only; global counts only.
10. Source repository was dirty at run time (provenance record). State this as a limitation.
11. Figure link (../figures/fig2_lollipop.svg) is unverified: either drop it or check the file exists.
12. CSS: css_state_machine is 18/18, so its nine tuple rows are all 2/2. A non-monotonic claim cannot hold. Retract it.
13. Multi-case rows: cell = environment × difficulty-tuple row (interpretation, not stated in the record). Each case has seed 0. Say the interpretation is an inference.
14. Do not present a monotonicity or "difficulty effect" finding. Do not rank the 34 difficulty keys.

## Structure
Keep the environment table as the headline. Keep the tuple matrix as a second, exploratory layer with binary/non-binary counts, the 214-row homogeneity point, and moco as the only fractional environment. Include a selection-frame section (corrections 5–7), a judge-coverage section (corrections 4, and 11 unscored rows), a failure-mode section (global only), and a limitations section.

## Output
Full article in Markdown, first-person, plain prose. Provide front matter with title, date (keep 2026-10-16 as original or state revision date 2026-10-18 — choose and state it in the front matter only), and byline. No tables of internal fields. End with a short "What this does not show" section.
