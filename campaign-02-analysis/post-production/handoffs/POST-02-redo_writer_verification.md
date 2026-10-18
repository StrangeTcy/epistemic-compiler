# POST-02 redo — Stage B (Writer) response: verification against archived evidence

Source: `campaign-02-analysis/comparison_22.md` (saved as `POST-02-redo_writer_response.md`).
Outputs in the response: (a) Sonnet 5 full draft, inline; (b) Opus 5.5 output, which refers to a file in `/tmp/outputs` that is not in the workspace or the repository, so only the chat summary is available. Stage B draft used for checks below = Sonnet 5 output.

Verification method: recomputed from `evidence/generated2/environment_difficulty_matrix.csv`, `evidence/generated2/environment_summary_v2.csv`, `evidence/generated/case_results.csv`, `evidence/generated/campaign_exclusions.csv`, `evidence/PROVENANCE.md`. No campaign rerun; local parsing only.

## Confirmed
| Claim in draft | Check |
|---|---|
| 416 selected cases, 38 environments | 416 rows in case_results; 38 rows in environment_summary_v2 |
| 405 scored, 277 PASS, 128 FAIL, 11 unscored | status / verdict counts in case_results |
| 277/405 = 68.4% scored pass rate | arithmetic |
| 17 all-pass (172/172), 12 mixed (105/165, 1 unscored), 7 all-fail (0/68), 2 no scored (10 unscored) | environment_summary_v2 recomputed |
| 7 zero-pass environments: functorial_augmentation, monadic_reward, sheaf_invariant_gluing, sheaf_physical_constraints, ts_one_step, ts_trajectory, glyph | environment_summary_v2 with n_pass=0 and n_scored>0 |
| Matrix: 340 rows, 4–15 rows per env, 6 envs with >10 rows | matrix recomputed |
| 296 single-case rows; 44 multi-case rows (moco 15, glyph 12, css_state_machine 9, epistemic_games 8) summing to 416 | matrix recomputed |
| 34 dimension keys | matrix recomputed (34 distinct key names; 113 distinct tuple strings) |
| 214 rows (63%) in environments with homogeneous outcome | matrix recomputed |
| moco is the only environment with fractional pass_rate values | moco: 9 non-binary rows; no other env has non-binary rows |
| CSS 18/18 cannot be non-monotonic | arithmetic (each row must be 2/2) |
| Failure modes: underfit 51, overfit_visible_tests 49, runtime_error 11 (9 RUNTIME_ERROR + 2 runtime_error consolidated), source_invalid 9, invalid_action 5, training_failed 3 | case_results counts |
| Judge guarantees: 189 behavioral_reference, 227 compile_only | case_results counts |
| Unscored rows: epistemic_silence 6, epistemic_type_games 4, rd_adaptive_halting 1 | matrix n_unscored |
| Source repo dirty at run time | PROVENANCE.md (dirty=true) |

## Errors in the draft (must be corrected before any further stage)
1. **Binary row count is wrong.** Draft: "314 of 329 scored rows (95.4%) take 0 or 1"; and "285 single-case rows plus 29 multi-case rows" = 314. Actual: **320 of 329 scored rows (97.3%)** take 0 or 1; **9** rows are non-binary.
2. **"15 non-binary rows, every moco row is mixed" is wrong.** Actual: 9 non-binary rows, all in moco. Six moco rows are already at 0.0 or 1.0 (e.g., 3/3, 2/0, 2/2, 4/4). Not every moco row is mixed. The draft's "148 + 56 + 10" breakdown and "all 15 non-binary rows" claim need to be recomputed.
3. **The 10-vs-7 hypothesis is falsified as written.** Draft: ANALYSIS_OVERVIEW's 10 may be a tuple-level count. Actual: 19 environments contain at least one zero-pass tuple (98 zero-pass tuples in total). The hypothesis does not produce 10. The 10 remains unexplained. Draft's "settled at 7" is defensible for the environment-level count, but the reconciliation is still open.
4. **rd_adaptive_halting unscored tuple IS identifiable.** Draft says it cannot be identified from the packet. Actual: the matrix row with n_unscored=1 is `{"batching_complexity":"easy","clue_clarity":"easy","implementation_obfuscation":"easy","recurrence_depth":"easy","visible_tests":"easy"}` (case `rd_adaptive_halting__recurrence_depth=easy_clue_clarity=easy_visible_tests=easy_implementation_obfuscation=easy_batching_complexity=easy__seed-0`, status infrastructure_unscored, stage_statuses empty). Gating item 4 is resolved by data.
5. **Omitted from draft: campaign-level omissions.** campaign_exclusions.csv lists 80 omitted cases outside the 416 selected: 56 intervention_twin_omission, 14 known_gate_calibration_failure, 10 unsupported_provider_input_modality. Per-environment rows: moco 35, glyph 21, rope 15, epistemic_games 9. The draft says nothing about them, though they affect the selection frame.
6. **Evidence-document discrepancy, unresolved.** PROVENANCE.md says 24 known gate-blocked omissions and 10 rope omissions. campaign_exclusions.csv has 14 known-gate rows and 15 rope rows. Needs reconciliation before any number is cited.
7. **Omitted from draft: 10 `rejected` dispositions.** case_results has case_disposition=rejected on 10 cases, all scored FAIL: monadic_reward 8 (**8 of its 9 scored cases are rejected**; its 0/9 zero-pass result therefore rests on 8 rejected cases plus 1 non-rejected case), batchnorm_ema 1, transformer_ssm_lift 1. The meaning of "rejected" is not defined in the packet. This bears directly on the zero-pass claim for monadic_reward (0/9). Must be explained or disclosed.
8. **Omitted: performance_eligible=False on 12 cases.** 11 are infrastructure_unscored; 1 is ts_parse_only__witness_status=broken_representation=flat__seed-0 (scored PASS, provider outage, exclusion_reason "campaign report provider-outage case..."). That case is in the 277 PASS count. The draft does not mention this; the pooled rate depends on it.
9. **Public-copy violations in the draft.** Revision note cites internal finding IDs ("F-006, F-008") and the words "the packet", "evidence packet", "source analysis". The file also contains production metadata (Original ideas / Synthesis / Prose / Certainty / Importance block) and a "house style not applied" note. These must be removed from public copy. (Note: the revision note may stay internally; public copy must not contain it.)
10. **Figure link** `../figures/fig2_lollipop.svg` is inherited from the original post and is unverified. Check it exists before publication.
11. **Date.** Draft keeps the original 2026-10-16 date. Confirm.
12. **Opus 5.5 output** is only a chat summary; its essay is not available in the workspace. It cannot be assessed.

## Not verifiable from workspace
- The draft's "10 → 7" conclusion relies on environment-level totals, which check out.
- The draft's claim that moco shows genuine fractional gradation: true, but the draft's "every moco row is mixed" is false (see 2).
- The 2.4% vs 3.9% monotone-grid figure dispute (Sonnet's own figure 3.9% at 50%, ~8% at 68.4%). Not recomputed; treat as unverified.

## Status
Stage B response is received and archived. The draft is NOT accepted as final. Corrections 1–9 must be applied and the open items (6, 7, 8, and the 10 unexplained) decided before Stage C.
