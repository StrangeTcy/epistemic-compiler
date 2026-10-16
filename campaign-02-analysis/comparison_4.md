unknown model:

Here is the comprehensive claim-by-claim verification table assessing both drafts against the verified ground truth and the accepted Stage C Editorial Blueprint.

### CLAIM VERIFICATION TABLE

| Claim | Draft | Verdict | Evidence Source | Required Action |
| :--- | :--- | :--- | :--- | :--- |
| "scored pass rate of 0.684. Out of 405 scored cases, the model passed 277 and failed 128" | A | SUPPORTED / CORRECT-ARITHMETIC | Packet: 277 PASS / 128 FAIL (sum 405). Scored pass rate: 0.684 | Keep as is. |
| "We have 416 selected cases spanning 38 distinct environments (with 11 cases remaining unscored)." | A | SUPPORTED | Packet: 38 environments total; 416 selected cases; 405 scored; 11 unscored. | Keep as is. |
| "What Mercury-2.5 [ac-word] did..." | A | UNSUPPORTED | Editorial Blueprint: Remove `[ac-word]` placeholders. | **Delete placeholder.** |
| "exactly two-thirds reside at the absolute extremes" | A | SUPPORTED / CORRECT-ARITHMETIC | Packet: 24 of 36 scored environments are at endpoints (17 + 7). 24/36 = 2/3. | Keep as is. |
| "flawless performance in 🤬 half the scored environments." | A | UNSUPPORTED | Packet: 17/36. Editorial Blueprint: Correct "half" to 17/36 (47%); Remove stray emoji. | **Delete emoji 🤬.** Change "half" to "17 of the 36 (47%)". |
| "17 perfect-pass environments... 9/9 in `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`..." | A | SUPPORTED | Packet: Lists exact 17 environments and their perfect counts. | Keep counts as verified. |
| "7 zero-pass environments... 0/9 in `functorial_augmentation`... 0/24 in `glyph`..." | A | SUPPORTED | Packet: Lists exact 7 environments and their zero-pass counts. | Keep counts as verified. |
| "12 partial-pass environments... exactly 165 out of the 405 scored cases, or 40.7%" | A | SUPPORTED / CORRECT-ARITHMETIC | Packet: Partial environments hold 165/405 scored cases = 40.7%. | Keep as is. |
| "sheaf_schema_sync, sql_fixed_point, and transformer_ssm_lift (all 8/9, or 0.889)... batchnorm_ema... 2/15 (0.133)" | A | SUPPORTED | Packet: Matches exact partial counts and decimals. | Keep as is. |
| "ts_parse_only (4/4)... ts_one_step and ts_trajectory... 0/4 in both" | A | SUPPORTED | Packet: Matches perfect-pass and zero-pass records. | Keep as is. |
| "underfit: 51 cases... overfit_visible_tests: 49 cases" | A | SUPPORTED | Packet: Failure modes exact counts. | Keep as is. |
| "These are standard cognitive failure modes..." | A | UNSUPPORTED | Editorial Blueprint: Remove "cognitive failure modes" framing. | **Delete phrase.** |
| "It is highly probable that these failure modes perfectly map to the zero-pass (0/9) environments." | A | UNSUPPORTED | Editorial Blueprint: Remove Draft A's causal speculation. | **Delete speculation.** The archive does not link specific failure modes to specific environments. |
| "moco: 55 cases generated from just 15 tuples... glyph: 24/12... epistemic_games: 23/8... css_state_machine: 18/9" | A | SUPPORTED | Packet: Cases vs tuples counts exactly match. | Keep as is. |
| "11 unscored cases... 6 in epistemic_silence, 4 in epistemic_type_games, and 1 orphaned case in rd_adaptive_halting." | A | SUPPORTED | Packet: Matches 11 unscored breakdown. | Keep as is. |
| "all-selected rate... 277/416 (0.666)" | A | SUPPORTED / CORRECT-ARITHMETIC | Packet: 277/416 = 0.66587 → 0.666. | Keep as is. |
| "189 cases evaluated via behavioral_reference and 227 via compile_only" | A | SUPPORTED | Packet: Judge guarantees exact counts. | Keep as is. |
| "[ac-word] judge-conditioned variance." | A | UNSUPPORTED | Editorial Blueprint: Remove `[ac-word]` placeholders. | **Delete placeholder.** |
| "Each selected cell in this dataset was run with a single seed... source repository was dirty at run time." | A | SUPPORTED | Packet: "Single seed per selected cell. Source repo dirty at run time." | Keep as is. |
| "what does this map [ac-word] tell us" | A | UNSUPPORTED | Editorial Blueprint: Remove `[ac-word]` placeholders. | **Delete placeholder.** |
| "brittle, contextual engine" closing | A | UNSUPPORTED | Editorial Blueprint: Remove "brittle, contextual engine" closing. | **Rewrite closing.** |
| Caveats are grouped in a "Methodological Confounds We Cannot Ignore" section | A | UNSUPPORTED | Editorial Blueprint: Inline caveats, not batched. | **Restructure Draft A** to inline these cautions as Draft B did. |
| "ts_parse_only is 4/4, while ts_one_step and ts_trajectory are each 0/4" | B | SUPPORTED | Packet: Endpoints list matching counts. | Keep as is. |
| "416 selected cases in 38 environments. Of those, 405 received a PASS or FAIL... 277/405, or 68.4%" | B | SUPPORTED | Packet: Exact match to ground truth. | Keep as is. |
| Table 1: 17 envs (172/172, 42.5%), 7 envs (0/68, 16.8%), 12 envs (105/165, 40.7%), 2 envs (0, unscored-only) | B | SUPPORTED / CORRECT-ARITHMETIC | Packet: 172+68+165 = 405. Fractions exactly align with percentages. | Keep Table 1. |
| Table 2 (Keeps unscored visible) | B | SUPPORTED | Editorial Blueprint: Keep Draft B's table convention with unscored column. | Keep Table 2. |
| "Twenty-four of the 36 environments with scored cases sit at an observed endpoint" | B | SUPPORTED | Packet: 17 perfect + 7 zero = 24. | Keep as is. |
| "discard the comparison that [m-word]s." | B | UNSUPPORTED | Editorial Blueprint: Remove `[m-word]` placeholders. | **Delete placeholder.** |
| "glyph has 0/24... moco has 36/55, or 65.5%, with 19 failures... batchnorm_ema has 2/15, or 13.3%, with 13 failures." | B | SUPPORTED / CORRECT-ARITHMETIC | Packet: Math is strictly verified. | Keep as is. |
| "these three environments supply 94/405 scored cases but 56/128 failures." | B | SUPPORTED / CORRECT-ARITHMETIC | Packet: Combined exposure stat validates 94 cases / 56 failures. | Keep as is. |
| "paired counts [m-word]" | B | UNSUPPORTED | Editorial Blueprint: Remove `[m-word]` placeholders. | **Delete placeholder.** |
| "mean of their observed pass fractions is about 69.2%... median is 8/9, or 88.9%" | B | SUPPORTED / CORRECT-ARITHMETIC | Packet: Explicitly matches unweighted mean and median. | Keep as is. |
| "rd_adaptive_halting remains 8/14 scored, plus one unscored" | B | SUPPORTED | Packet: Exact breakdown for rd_adaptive_halting. | Keep as is. |
| lists exact failure mode labels and counts (e.g. underfit 51, overfit_visible_tests 49) | B | SUPPORTED | Packet: Failure modes exact match. | Keep as is. |
| "The first two labels account for 100/128 failures." | B | SUPPORTED / CORRECT-ARITHMETIC | Packet: 51 + 49 = 100. | Keep as is. |
| "The counts provided here do not match failure modes to environments." | B | SUPPORTED | Editorial Blueprint: Remove Draft A's causal speculation. | Excellent framing; keep as is. |
| "189 behavioral_reference and 227 compile_only judge guarantees" | B | SUPPORTED | Packet: Judge guarantees exact match. | Keep as is. |
| "one seed, and the source repository was dirty at run time." | B | SUPPORTED | Packet: Variables match exactly. | Keep as is. |
| "environment identity 'dominates difficulty'" | B | NARROW / CAREFUL | Blueprint says endpoint heavy, not bimodal. The draft explicitly says the map does *not* mean identity dominates difficulty. | Keep sentence, it correctly avoids outrunning the evidence. |

---

### SAFE CLAIM SET (No Caveats Required)
*   The archive contains 416 selected cases across 38 distinct environments.
*   Exactly 405 cases were scored, yielding a 68.4% pass rate (277 PASS / 128 FAIL). 11 cases were unscored.
*   Performance is heavily localized at endpoints: 17 environments experienced a 100% pass rate (172/172 cases total), and 7 environments experienced a 0% pass rate (0/68 cases total).
*   12 partial-pass environments contain 40.7% of all scored cases (165 total).
*   Case generation from tuples is uneven, resulting in unequal environment weights (e.g., `moco` generated 55 cases from 15 tuples, contributing 13.6% of the entire scored dataset; `glyph` generated 24 cases from 12 tuples).
*   The bulk of failures (100 out of 128) were categorized as either `underfit` (51) or `overfit_visible_tests` (49). 28 failures were infrastructural/code errors (`RUNTIME_ERROR`, `source_invalid`, etc.).
*   There were two distinct judging methodologies used: 189 cases were evaluated via `behavioral_reference` and 227 via `compile_only`.

### QUALIFIED CLAIM SET (Caveats Required in the Same Sentence/Paragraph)
*   **The 66.6% Pass Rate:** May only be cited if explicitly qualified as the "all-selected pass rate" that factors in the 11 unscored cases, acknowledging that unscored does not necessarily mean failure.
*   **Comparing 'Difficulty' Across Environments:** Any assertion about relative environment difficulty (e.g., `ts_parse_only` vs `ts_trajectory`) must immediately carry the caveat that there is no shared difficulty scale, cases represent different unrolled tuples, and the dataset lacks variance bounds.
*   **Model Capability based on Endpoints:** When noting perfect passes or zero passes, you must explicitly state the lack of statistical stability testing, citing that each cell utilized only a single seed and the repository was "dirty" at run time.
*   **Inferring Causes of 0/9 Failures:** You may note that 9-count infrastructural flags (`RUNTIME_ERROR`, `source_invalid`) perfectly match the case size of several 0/9 environments, but you *must* add the caveat that the archival counts do not formally map specific failure modes to specific environments.


&&&&&&&&&&&&&&


openhard 3.0 cot 1015:

# Claim Killer verification — POST-02 cross-environment map

**Scope:** Draft A = Gemini 3.1 Pro grounding; Draft B = GPT 6 sol max. Ground truth is the supplied evidence packet only. External CDN checks are noted separately under production artifacts.

**Verdict key**
- **SUPPORTED**: directly stated or arithmetically entailed by packet.
- **CORRECT-ARITHMETIC**: numeric claim checks out, but is descriptive only.
- **NARROW**: true only with an explicit scope limitation.
- **UNSUPPORTED**: no packet evidence, or evidence is absent for the inference.
- **NEEDS-CHECK**: requires a cross-tab, log inspection, rerun, or source not included in packet.
- **PRODUCTION-ARTIFACT**: placeholder, emoji, broken figure, script, markup, or formatting issue.

## Production artifacts flagged before content review

| Item | Draft | Verdict | Evidence / issue | Required action |
|---|---|---|---|---|
| `[ac-word]` in “what Mercury-2.5 [ac-word] did” | A | PRODUCTION-ARTIFACT | Editorial blueprint explicitly says remove `[ac-word]` placeholders. | Replace with intended verb or delete. |
| `[ac-word]` in “judge-conditioned variance” | A | PRODUCTION-ARTIFACT | Same placeholder remains. | Replace/delete. |
| `[ac-word]` in “map [ac-word] tell us” | A | PRODUCTION-ARTIFACT | Same placeholder remains. | Replace/delete. |
| `🤬` before “half the scored environments” | A | PRODUCTION-ARTIFACT | Blueprint says remove stray emoji. | Delete emoji. |
| `[m-word]` in “comparison that [m-word]s” | B | PRODUCTION-ARTIFACT | Blueprint says remove `[m-word]` placeholder. | Replace with intended verb. |
| `[m-word]` in “Those paired counts [m-word] because” | B | PRODUCTION-ARTIFACT | Same placeholder remains. | Replace with intended verb. |
| Figure line containing only `!` | B | PRODUCTION-ARTIFACT | Incomplete image markup/caption. | Restore complete figure include and caption. |
| Lollipop caption says “across the 38 environments” | A | NEEDS-CHECK | Two environments are unscored-only and have no scored pass fraction to plot. | Plot 36 scored rates, or explicitly show 2 unscored-only separately. |
| `https://polyfill.io/v3/polyfill.min.js` | A, B | PRODUCTION-ARTIFACT / SECURITY | polyfill.io has known supply-chain risk and should not be used; Cloudflare recommends removing or replacing it with a trusted mirror/self-hosted copy. | Remove the script or replace with a trusted, pinned dependency. |
| MathJax URL uses `mathjax@3` rather than exact version | A, B | PRODUCTION-ARTIFACT | The fetched file identifies MathJax **3.2.2**, but unpinned `@3` can change over time. | Pin exact version, e.g. `mathjax@3.2.2`, and preferably add SRI. |
| Section heading “Infrastructure Ghosts” | A | UNSUPPORTED FRAMING | Packet contains failure labels, not proof of harness failure. | Retitle to neutral “Failure labels and unresolved checks.” |
| Closing “brittle, contextual engine” | A | UNSUPPORTED / EDITORIAL | Blueprint explicitly requires removal. | Delete. |

---

## Claim-by-claim verification table

| # | Draft | Claim as written or closely paraphrased | Verdict | Packet evidence | Required action |
|---:|---|---|---|---|---|
| 1 | A | Campaign has a scored pass rate of **0.684**. | CORRECT-ARITHMETIC | 277/405 = 0.68395 → 0.684. | Keep, state denominator. |
| 2 | A | **405 scored cases**, **277 passed**, **128 failed**. | SUPPORTED | Packet: 405 scored; 277 PASS / 128 FAIL. | Keep. |
| 3 | A | **416 selected cases** across **38 environments**. | SUPPORTED | Packet totals. | Keep. |
| 4 | A | **11 cases remained unscored**. | CORRECT-ARITHMETIC | 416 − 405 = 11. | Keep. |
| 5 | A | The pooled number suggests “roughly two-thirds” capability. | NARROW | 68.4% is about two-thirds, but it is case-weighted, not environment-weighted. | Keep only as descriptive, not capability estimate. |
| 6 | A | Outcome map is “heavily environment-conditioned.” | NARROW | Outcomes vary sharply by environment; no controlled difficulty scale is supplied. | Say “observed outcomes vary sharply by environment,” not causal. |
| 7 | A | Distribution is “dominated by endpoint extremes.” | SUPPORTED | 24/36 scored environments are all-pass or all-fail. | Keep; use “endpoint-heavy.” |
| 8 | A | “Plagued by infrastructural ghosts.” | UNSUPPORTED | Packet has failure labels but no environment-to-failure-mode cross-tab or log proof. | Remove or downgrade to “possible infrastructure issues require log inspection.” |
| 9 | A | Of **36 scored environments**, **exactly two-thirds** are at extremes. | CORRECT-ARITHMETIC | 24/36 = 2/3. | Keep. |
| 10 | A | **17 perfect-pass environments**. | SUPPORTED | Packet lists 17. | Keep. |
| 11 | A | Perfect-pass environments are “half the scored environments.” | NARROW / IMPRECISE | 17/36 = 47.2%, not exactly half. Blueprint specifically flags this. | Change to **17/36, or 47%**. |
| 12 | A | `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, `tokenizer_adjunction` are 9/9. | SUPPORTED | Perfect-pass list. | Keep. |
| 13 | A | `css_state_machine` is 18/18. | SUPPORTED | Perfect-pass list. | Keep. |
| 14 | A | `rd_gradient_credit` and `rd_state_carry` are 15/15. | SUPPORTED | Perfect-pass list. | Keep. |
| 15 | A | `epistemic_games` is 23/23. | SUPPORTED | Perfect-pass list. | Keep. |
| 16 | A | `epistemic_announcements` 6/6, `epistemic_nested_knowledge` 6/6, `epistemic_fragmented_observation` 4/4, `ts_parse_only` 4/4. | SUPPORTED | Perfect-pass list. | Keep. |
| 17 | A | **7 zero-pass environments**. | SUPPORTED | Packet lists 7. | Keep. |
| 18 | A | `functorial_augmentation`, `monadic_reward`, `sheaf_invariant_gluing`, `sheaf_physical_constraints` are 0/9. | SUPPORTED | Zero-pass list. | Keep. |
| 19 | A | `ts_one_step` and `ts_trajectory` are 0/4. | SUPPORTED | Zero-pass list. | Keep. |
| 20 | A | `glyph` is 0/24. | SUPPORTED | Zero-pass list. | Keep. |
| 21 | A | **12 partial-pass environments**. | SUPPORTED | 36 − 24 endpoint = 12; packet lists them. | Keep. |
| 22 | A | Partial environments hold **165/405 scored cases = 40.7%**. | CORRECT-ARITHMETIC | Packet gives 165/405 = 40.7%. | Keep. |
| 23 | A | `sheaf_schema_sync`, `sql_fixed_point`, `transformer_ssm_lift` are 8/9 = 0.889. | SUPPORTED | Partial list. | Keep. |
| 24 | A | `compositional_optimizer` and `equivariant_diagram` are 7/9 = 0.778. | SUPPORTED | Partial list. | Keep. |
| 25 | A | `moco` is 36/55 = 0.655. | SUPPORTED | Partial list. | Keep. |
| 26 | A | `batchnorm_ema` is 2/15 = 0.133. | SUPPORTED | Partial list. | Keep. |
| 27 | A | Model is more likely to perfectly solve or completely fail an environment than to score near 68%. | NARROW | 24/36 environments are endpoints, but 40.7% of scored cases are partial. | Keep as environment-count observation; note case-weight caveat. |
| 28 | A | “Family labels do not predict outcomes.” | OVERBROAD / NARROW | Examples show prefixes do not guarantee similar outcomes *in this archive*. No general predictive test was run. | Reword: “Shared prefix did not imply similar observed outcomes in these examples.” |
| 29 | A | Evidence “proves that assumption completely false.” | UNSUPPORTED | Examples disprove a strong uniform-family claim, but do not prove labels have zero predictive value generally. | Soften to “contradicts a strong uniform-family assumption.” |
| 30 | A | `ts_parse_only` 4/4 while `ts_one_step` and `ts_trajectory` are 0/4. | SUPPORTED | Packet lists all three. | Keep. |
| 31 | A | `sheaf_schema_sync` 8/9 while two sheaf environments are 0/9. | SUPPORTED | Partial and zero-pass lists. | Keep. |
| 32 | A | Shared prefix does not imply shared cognitive demands or shared infrastructure. | NARROW | The outcome difference is consistent with this, but packet does not identify causes. | State as possibility, not established fact. |
| 33 | A | Failure labels: underfit 51, overfit_visible_tests 49. | SUPPORTED | Failure-mode list. | Keep as recorded labels. |
| 34 | A | Together these are **100 cases**. | CORRECT-ARITHMETIC | 51 + 49 = 100. | Keep. |
| 35 | A | Calls these “standard cognitive failure modes.” | UNSUPPORTED / EDITORIAL | Blueprint says remove “cognitive failure modes” framing; labels are classifications, not observed internal cognition. | Replace with “two largest recorded failure categories.” |
| 36 | A | Remaining failures = 28. | CORRECT-ARITHMETIC | 128 − 100 = 28. | Keep. |
| 37 | A | RUNTIME_ERROR 9, source_invalid 9, invalid_action 5, training_failed 3, runtime_error 2. | SUPPORTED | Failure-mode list. | Keep exact casing. |
| 38 | A | Counts of 9 are a “glaring data-quality flag.” | NARROW | Coincidence motivates inspection; several environments have 9 cases. | Keep as reason to inspect, not proof. |
| 39 | A | “It is highly probable that these failure modes perfectly map to the zero-pass 0/9 environments.” | UNSUPPORTED | Packet explicitly gives no environment-by-failure-mode cross-tab. Blueprint says remove this causal speculation. | Delete. |
| 40 | A | If a whole 9-case environment throws one of these labels, it is a broken harness rather than model reasoning. | NARROW | Plausible, but conditional and unverified. | Keep only as a hypothetical after cross-tab/log evidence. |
| 41 | A | Casing discrepancy is “a classic tell of disjoint evaluation pipelines.” | UNSUPPORTED | Casing is a data-quality flag; pipeline cause is not established. | Say “may indicate inconsistent logging or aggregation; requires source inspection.” |
| 42 | A | Suspects test failed to run for at least part of seven zero-pass environments. | NEEDS-CHECK / UNSUPPORTED | No case-level mapping supplied. | Do not publish without logs/cross-tab. |
| 43 | A | Formula: pass rate = passed cases / scored cases. | SUPPORTED | Matches 277/405. | Keep. |
| 44 | A | Denominator is not evenly distributed across environments. | SUPPORTED | Case counts range from 4 to 55 among scored environments. | Keep. |
| 45 | A | `moco`: 55 cases from 15 tuples. | SUPPORTED | Cases-vs-tuples list. | Keep. |
| 46 | A | `glyph`: 24 cases from 12 tuples. | SUPPORTED | Cases-vs-tuples list. | Keep. |
| 47 | A | `epistemic_games`: 23 cases from 8 tuples. | SUPPORTED | Cases-vs-tuples list. | Keep. |
| 48 | A | `css_state_machine`: 18 cases from 9 tuples. | SUPPORTED | Cases-vs-tuples list. | Keep. |
| 49 | A | `moco` “heavily dictates” the global average. | NARROW | It is the largest scored environment, 55/405 = 13.6%, but “dictates” is stronger than evidence. | Say “has the largest single-environment weight.” |
| 50 | A | If `moco` were 9 cases, pooled rate would be “demonstrably different.” | NEEDS-CHECK | Counterfactual requires specifying which 9 cases are retained; packet does not define that. | Do not assert; discuss weighting generally. |
| 51 | A | `glyph` acts as a large anchor dragging average down. | NARROW | 24 all-fail cases contribute 24 failures; causal wording should be neutral. | Say “contributes 24 failures.” |
| 52 | A | Top-line is a product of tuple unrolling rather than balanced capability reflection. | NARROW | Unbalanced case counts affect weighted average, but this is not the sole determinant. | Say “case-weighted result is affected by unequal unrolling.” |
| 53 | A | 11 unscored = 6 `epistemic_silence`, 4 `epistemic_type_games`, 1 `rd_adaptive_halting`. | SUPPORTED | Packet unscored breakdown. | Keep. |
| 54 | A | Two epistemic environments are entirely unscored, reducing scored environments from 38 to 36. | CORRECT-ARITHMETIC | 38 − 2 = 36. | Keep. |
| 55 | A | Unscored cases must not be recoded as failures. | SUPPORTED | Packet distinguishes scored and all-selected rates. | Keep. |
| 56 | A | Scored rate is 277/405 = 0.684. | SUPPORTED | Packet. | Keep. |
| 57 | A | All-selected rate is 277/416 = 0.666. | CORRECT-ARITHMETIC | 277/416 = 0.66587 → 0.666. | Keep, define as PASS / all selected, not ordinary pass rate. |
| 58 | A | Scored rate is mathematically sound for evaluated tasks. | SUPPORTED | Correct denominator treatment. | Keep. |
| 59 | A | 189 behavioral_reference + 227 compile_only = 416. | CORRECT-ARITHMETIC | 189 + 227 = 416. | Keep. |
| 60 | A | No crossover tests between judge types. | SUPPORTED BY ABSENCE | Packet gives totals only, no pairwise crossover. | State “packet provides no crossover results.” |
| 61 | A | Cannot determine how much variance is judge-conditioned. | SUPPORTED | No environment-by-judge cross-tab. | Keep as limitation. |
| 62 | A | Each selected cell used one seed. | SUPPORTED | Packet: single seed per selected cell. | Keep. |
| 63 | A | No insight into variance or stability. | SUPPORTED CONSEQUENCE | Single seed cannot estimate seed variance. | Keep. |
| 64 | A | Single seed is less concerning in endpoint environments. | UNSUPPORTED / OVERREACH | Endpoints may also change under reruns; no variance data. | Remove or say “endpoint labels do not eliminate seed uncertainty.” |
| 65 | A | Dirty source repo is a reproducibility problem. | NARROW / SUPPORTED | Packet says source repo dirty at run time. This supports reproducibility concern, not specific effects. | Keep as caveat. |
| 66 | A | Dirty repo implies possible leaked state or broken state effects. | UNSUPPORTED | No evidence of leakage or state-induced failure. | Delete specific mechanisms; retain reproducibility caveat. |
| 67 | A | Outcomes are “profoundly environment-conditioned.” | NARROW | Strong descriptive association; no causal isolation. | Use “observed outcomes differ sharply by environment.” |
| 68 | A | Domain names and family prefixes are “useless for predicting performance.” | OVERBROAD | Examples show unreliability, not zero predictive validity. | Change to “unreliable shortcut in this archive.” |
| 69 | A | Cannot claim environment identity dominates difficulty. | SUPPORTED | No common difficulty scale in packet. | Keep; this is a correct limitation. |
| 70 | A | 9/9 and 0/24 do not mean model is “smart” or “dumb” at domains. | SUPPORTED / EDITORIAL | Correct caution against trait inference. | Keep in neutral form. |
| 71 | A | Mercury-2.5 is a “brittle, contextual engine.” | UNSUPPORTED / EDITORIAL | Blueprint explicitly removes this closing. | Delete. |
| 72 | B | Mercury-2.5 passed **68.4% of scored cases**. | CORRECT-ARITHMETIC | 277/405. | Keep. |
| 73 | B | `ts_parse_only` 4/4; `ts_one_step` and `ts_trajectory` each 0/4. | SUPPORTED | Packet. | Keep. |
| 74 | B | Outcomes are not repeated measurements of general capability. | SUPPORTED | Single seed, selected cases, no repeated runs. | Keep. |
| 75 | B | Environment name is not a difficulty rating. | SUPPORTED | No shared difficulty scale supplied. | Keep. |
| 76 | B | 416 selected cases in 38 environments. | SUPPORTED | Packet. | Keep. |
| 77 | B | 405 received judgment: 277 PASS, 128 FAIL. | SUPPORTED | Packet. | Keep. |
| 78 | B | 277/405 = 68.4% scored-case pass rate. | CORRECT-ARITHMETIC | Packet. | Keep. |
| 79 | B | 11 cases unscored. | SUPPORTED | Packet. | Keep. |
| 80 | B | 277/416 = 66.6% is share of all selected cases with observed PASS. | CORRECT-ARITHMETIC | Packet. | Keep with precise definition. |
| 81 | B | Summary table: 17 all-pass environments, 172/172, 42.5%, 0 unscored. | CORRECT-ARITHMETIC | 172/405 = 42.47% → 42.5%. | Keep. |
| 82 | B | 7 no-pass environments, 0/68, 16.8%, 0 unscored. | CORRECT-ARITHMETIC | Zero-pass total 68; 68/405 = 16.79%. | Keep. |
| 83 | B | 12 partial environments, 105/165, 40.7%, 1 unscored. | CORRECT-ARITHMETIC | Packet: partial holds 165 scored; mixed 105/165 + 1 unscored. | Keep. |
| 84 | B | 2 no-scored environments, 10 unscored. | CORRECT-ARITHMETIC | 6 + 4 = 10. | Keep. |
| 85 | B | Totals: 38 environments, 277/405, 11 unscored. | SUPPORTED | Packet. | Keep. |
| 86 | B | **24 of 36** scored environments are endpoints. | CORRECT-ARITHMETIC | 17 + 7 = 24. | Keep. |
| 87 | B | Calls map **endpoint-heavy**, not bimodal. | SUPPORTED / EDITORIAL COMPLIANT | Blueprint explicitly says endpoint-heavy, not bimodal. | Keep. |
| 88 | B | Endpoints vary in size from 4 to 23/24 cases. | SUPPORTED | Smallest 4, largest perfect 23, largest zero 24. | Keep. |
| 89 | B | Table alone cannot establish stability under new cases or seeds. | SUPPORTED | Single seed, no reruns. | Keep. |
| 90 | B | Partial environments contain 165/405 = 40.7%. | CORRECT-ARITHMETIC | Packet. | Keep. |
| 91 | B | Partial range is 2/15 to 8/9. | SUPPORTED | batchnorm_ema 2/15; several 8/9. | Keep. |
| 92 | B | `epistemic_silence` has 6 unscored; `epistemic_type_games` has 4. | SUPPORTED | Packet. | Keep. |
| 93 | B | Remaining unscored belongs to `rd_adaptive_halting`, scored 8/14. | SUPPORTED | Packet. | Keep. |
| 94 | B | Complete environment table values. | SUPPORTED | Every row matches packet lists. | Keep after fixing figure artifact. |
| 95 | B | `ts_*` description is “three sets of four judged cases,” not a difficulty ladder. | SUPPORTED | 4/4, 0/4, 0/4; no shared scale. | Keep. |
| 96 | B | Even 4/4 is a small observed endpoint. | SUPPORTED | Small n = 4. | Keep. |
| 97 | B | `sheaf_schema_sync` 8/9; two sheaf environments 0/9. | SUPPORTED | Packet. | Keep. |
| 98 | B | Grouping all three under “sheaf performance” would discard the contrast. | SUPPORTED | The observed outcomes differ. | Keep. |
| 99 | B | `categorical_lenses` 9/9, `functorial_augmentation` 0/9, `tensor_functor` 6/9. | SUPPORTED | Packet. | Keep. |
| 100 | B | Shared name is unreliable within this archive. | NARROW / SUPPORTED | Supported for cited examples; not a general predictive study. | Keep “within this archive.” |
| 101 | B | Examples do not establish which task property caused pass/fail. | SUPPORTED | No causal controls. | Keep. |
| 102 | B | `glyph` 0/24 is larger all-fail block than four-case `ts_*` endpoints. | CORRECT-ARITHMETIC | 24 > 4. | Keep. |
| 103 | B | `moco` 36/55 = 65.5%, 19 failures. | CORRECT-ARITHMETIC | 55 − 36 = 19. | Keep. |
| 104 | B | `batchnorm_ema` 2/15 = 13.3%, 13 failures. | CORRECT-ARITHMETIC | 15 − 2 = 13. | Keep. |
| 105 | B | Three environments supply **94/405 scored cases** and **56/128 failures**. | CORRECT-ARITHMETIC | 24+55+15=94; 24+19+13=56. | Keep. |
| 106 | B | 94/405 = 23.2%; 56/128 = 43.8%. | CORRECT-ARITHMETIC | Packet confirms both. | Keep, optionally include percentages. |
| 107 | B | This shows pooled result is shaped by where cases were selected. | NARROW | Weighting mathematically affects pooled rate; “shaped” is acceptable if not causal. | Keep with case-weighting wording. |
| 108 | B | It does not show the three share a failure mechanism. | SUPPORTED | No mechanism evidence. | Keep. |
| 109 | B | Unit of pooled rate is a case. | SUPPORTED | Denominator is cases. | Keep. |
| 110 | B | `moco` contributes 55 scored cases = 13.6% of scored campaign. | CORRECT-ARITHMETIC | 55/405 = 13.58%. | Keep. |
| 111 | B | `moco` covers 15 tuples; glyph 24/12; css 18/9; epistemic_games 23/8. | SUPPORTED | Cases-vs-tuples packet. | Keep. |
| 112 | B | 405 cases are not 405 distinct tuples. | SUPPORTED | Multiple examples show cases > tuples. | Keep. |
| 113 | B | “Much less 405 independent tests of general ability.” | NARROW | Dependence is plausible, but within-tuple dependence is not quantified. | Say “independence cannot be assumed from this packet.” |
| 114 | B | Packet does not provide enough information to estimate within-tuple dependence. | SUPPORTED | No dependence model or tuple-level breakdown beyond examples. | Keep. |
| 115 | B | Equal-environment weighting gives mean observed pass fraction ≈ **69.2%**. | CORRECT-ARITHMETIC | Packet explicitly gives unweighted mean ≈69.2%. | Keep. |
| 116 | B | Median = **8/9 = 88.9%**. | CORRECT-ARITHMETIC | Packet explicitly gives median. | Keep. |
| 117 | B | Mean is close to case-weighted 68.4%. | CORRECT-ARITHMETIC | 69.2% vs 68.4%. | Keep. |
| 118 | B | Median hides seven all-fail environments. | SUPPORTED / DESCRIPTIVE | Median alone does not reveal lower tail. | Keep. |
| 119 | B | Either mean hides endpoint frequency. | SUPPORTED | Means summarize, not distribution shape. | Keep. |
| 120 | B | Changing summary changes the question, not preserves map shape. | SUPPORTED CONCEPTUAL | Different weighting answers different question. | Keep. |
| 121 | B | 12 partial environments’ 165 cases are too numerous to treat as noise. | SUPPORTED | 40.7% of scored cases. | Keep. |
| 122 | B | `gnn_message_passing`, `regex_state_machine`, `ssm_parallel_scan` each 5/9. | SUPPORTED | Partial list. | Keep. |
| 123 | B | `sheaf_schema_sync`, `sql_fixed_point`, `transformer_ssm_lift` each 8/9. | SUPPORTED | Partial list. | Keep. |
| 124 | B | Identical fractions do not make environments interchangeable. | SUPPORTED | Packet gives no evidence of equivalence. | Keep. |
| 125 | B | `rd_adaptive_halting` is 8/14 scored + 1 unscored, not 15 judged cases. | CORRECT-ARITHMETIC | 14 scored + 1 unscored = 15 selected. | Keep. |
| 126 | B | Failure labels and counts: 51, 49, 9, 9, 5, 3, 2. | SUPPORTED | Packet. | Keep. |
| 127 | B | First two labels account for 100/128. | CORRECT-ARITHMETIC | 51+49=100. | Keep. |
| 128 | B | Labels are recorded classifications, not observations of internal reasoning. | SUPPORTED | Packet supplies labels only; blueprint rejects cognitive framing. | Keep. |
| 129 | B | Cannot infer internal mechanism from label names. | SUPPORTED | No causal evidence. | Keep. |
| 130 | B | Casing difference is a data-quality flag, not evidence for two runtime failure kinds. | SUPPORTED / CAUTIOUS | Packet has both casings, no definitions or cross-tab. | Keep. |
| 131 | B | Nine-count labels deserve attention because several environments have nine cases. | SUPPORTED | Several 0/9 environments exist. | Keep as inspection trigger. |
| 132 | B | Counts do not match failure modes to environments. | SUPPORTED | Packet gives no cross-tab. | Keep. |
| 133 | B | Nine-count coincidence is not permission to assign harness cause. | SUPPORTED | Correct evidence boundary. | Keep. |
| 134 | B | 189 behavioral_reference + 227 compile_only across 416 selected. | CORRECT-ARITHMETIC | Packet. | Keep. |
| 135 | B | Guarantees are not interchangeable descriptions of what PASS establishes. | NARROW / SUPPORTED | Different judge labels imply different evaluation basis, but packet gives no definitions beyond names. | Keep, avoid over-interpreting judge behavior. |
| 136 | B | Without environment-by-guarantee breakdown, cannot test whether contrasts change under same standard. | SUPPORTED | Required cross-tab absent. | Keep. |
| 137 | B | Calling every perfect-pass environment behaviorally solved outruns evidence. | SUPPORTED | Some PASS may be compile_only; no environment breakdown. | Keep. |
| 138 | B | One seed per selected cell. | SUPPORTED | Packet. | Keep. |
| 139 | B | Source repo dirty at run time. | SUPPORTED | Packet. | Keep. |
| 140 | B | One seed prevents seed-variability estimate. | SUPPORTED | Correct consequence. | Keep. |
| 141 | B | Dirty repo makes exact working-tree state important for reproduction. | SUPPORTED | Correct consequence. | Keep. |
| 142 | B | Neither fact proves a particular score is wrong. | SUPPORTED | They are confounds, not disproof. | Keep. |
| 143 | B | Result is not “environment identity dominates difficulty.” | SUPPORTED | No common difficulty scale. | Keep. |
| 144 | B | Map does not identify model-internal cause for glyph or batchnorm. | SUPPORTED | No causal evidence. | Keep. |
| 145 | B | Map does not say how endpoints survive new seeds, uniform judge, clean source. | SUPPORTED | Those tests absent. | Keep. |
| 146 | B | Recommends environment-by-judge and environment-by-failure-mode cross-tab plus repeated runs. | SUPPORTED AS RECOMMENDATION | Directly addresses missing evidence. | Keep as future work. |
| 147 | B | Keep 68.4% as answer to “fraction of scored selected cases receiving PASS.” | SUPPORTED | Exact denominator. | Keep. |
| 148 | B | More revealing answer is the map with zeros, perfect scores, and 40.7% partial. | SUPPORTED | Distribution facts support this. | Keep. |

## Arithmetic audit

No arithmetic error was found in the core counts. Verified:

- 277 + 128 = **405**
- 405 + 11 = **416**
- 17 + 7 + 12 + 2 = **38**
- 172 + 0 + 165 = **337 scored cases in endpoint + partial groups**; the remaining scored cases are already accounted within those groups, and the table’s PASS rows sum to 277.
- Partial PASS: 2 + 7 + 7 + 5 + 36 + 8 + 5 + 8 + 8 + 5 + 6 + 8 = **105**
- Partial scored: 15 + 9 + 9 + 9 + 55 + 14 + 9 + 9 + 9 + 9 + 9 + 9 = **165**
- Zero-pass scored: 9 + 24 + 9 + 9 + 9 + 4 + 4 = **68**
- Failure labels: 51 + 49 + 9 + 9 + 5 + 3 + 2 = **128**
- Combined exposure: 24 + 55 + 15 = **94 cases**; failures 24 + 19 + 13 = **56**
- 17/36 = **47.2%**, not “half” exactly.
- 24/36 = **66.7%** of scored environments at endpoints.
- 165/405 = **40.7%**
- 172/405 = **42.5%**
- 68/405 = **16.8%**
- 55/405 = **13.6%**
- Unweighted mean ≈ **69.2%** and median = **88.9%** are supplied as packet ground truth and are consistent with Draft B.

## Main unsupported causal inferences to remove or qualify

1. **Draft A**: nine `RUNTIME_ERROR` and nine `source_invalid` labels probably map exactly to 0/9 environments.
   - No environment-by-failure-mode table exists.
   - Action: delete the probability claim; retain “inspect logs.”

2. **Draft A**: casing discrepancy proves disjoint pipelines.
   - It is consistent with inconsistent logging, but not proof.
   - Action: call it a data-quality flag.

3. **Draft A**: dirty repo caused leaked successes or broken failures.
   - Dirty repo is a reproducibility confound, not evidence of either mechanism.
   - Action: state limitation only.

4. **Draft A**: family labels are useless for prediction.
   - The archive shows examples where shared prefixes coexist with very different outcomes.
   - It does not run a predictive validity test.
   - Action: narrow to “unreliable shortcut in these examples.”

5. **Draft A**: “brittle, contextual engine.”
   - Personality/mechanism claim unsupported by counts.
   - Action: delete per blueprint.

6. **Draft B**: equal weighting would “not really fix” the headline.
   - The unweighted mean is close, which supports the descriptive point, but no full alternative analysis is included.
   - Action: keep only with the computed 69.2% mean and explain that it answers a different question.

# Safe claim set

These may be stated without additional qualification, provided the exact denominator is included where relevant:

1. The archive contains **416 selected cases across 38 environments**.
2. **405 cases were scored**: **277 PASS** and **128 FAIL**.
3. The scored-case pass rate is **277/405 = 68.4%**.
4. **11 cases were unscored**: 6 in `epistemic_silence`, 4 in `epistemic_type_games`, and 1 in `rd_adaptive_halting`.
5. The all-selected PASS fraction is **277/416 = 66.6%**; this is not the scored-case pass rate.
6. **36 environments have scored cases**; two environments are unscored-only.
7. **17 environments** have all scored cases passing.
8. **7 environments** have no scored passes.
9. **12 environments** have both passes and failures among scored cases.
10. **24 of 36 scored environments** are observed endpoints: all-pass or all-fail.
11. Perfect-pass environments account for **172 scored cases, all passed**.
12. Zero-pass environments account for **68 scored cases, all failed**.
13. Partial environments account for **165 scored cases**, with **105 passes and 60 failures**, plus **1 unscored case**.
14. Partial environments contain **40.7%** of all scored cases.
15. `glyph` is **0/24**; `moco` is **36/55**; `batchnorm_ema` is **2/15**.
16. `glyph`, `moco`, and `batchnorm_ema` together contain **94 scored cases** and account for **56 failures**.
17. Cases are not evenly distributed across environments.
18. `moco` contains **55 cases from 15 tuples**; `glyph` contains **24 from 12**; `css_state_machine` **18 from 9**; `epistemic_games` **23 from 8**.
19. Recorded failure labels are: underfit 51, overfit_visible_tests 49, `RUNTIME_ERROR` 9, `source_invalid` 9, `invalid_action` 5, `training_failed` 3, and `runtime_error` 2.
20. The first two recorded labels account for **100 of 128 failures**.
21. Judge guarantees total **189 behavioral_reference + 227 compile_only = 416**.
22. Each selected cell was run with **one seed**.
23. The source repository was **dirty at run time**.
24. The unweighted mean of the 36 environment pass fractions is approximately **69.2%**, and the median is **8/9 = 88.9%**.
25. The appropriate high-level description is **endpoint-heavy**, not statistically bimodal.

# Qualified claim set

These require a caveat in the same sentence or paragraph:

1. **Observed outcomes are strongly environment-associated** — but the packet does not establish environment identity as the causal driver.
2. **Shared prefixes were unreliable in this archive** — but the packet does not test their general predictive validity.
3. **The nine-count failure labels warrant investigation** — because no environment-by-failure-mode cross-tab is provided.
4. **The `RUNTIME_ERROR` / `runtime_error` casing is a data-quality flag** — not evidence that there are two distinct runtime mechanisms.
5. **Unequal case density affects the case-weighted 68.4% rate** — without claiming that tuple unrolling alone explains the result.
6. **The 69.2% unweighted environment mean is close to 68.4%** — but it answers an environment-weighted question, not the same case-weighted question.
7. **The median of 88.9% highlights the endpoint-heavy shape** — while concealing the seven zero-pass environments.
8. **Single-seed results provide no seed-variance estimate** — particularly, endpoint labels do not prove stability.
9. **The dirty repo is a reproducibility concern** — not evidence that any particular score was caused by repository state.
10. **`compile_only` and `behavioral_reference` PASSes should not be treated as equivalent** — pending an environment-by-judge breakdown.
11. **A 4/4 endpoint is based on four cases** — it should not be treated as a strong estimate of future performance.
12. **Within-tuple independence cannot be assumed** — because the packet reports cases and tuples separately but provides no dependence model.
13. **The map supports sharp observed contrasts** — but not conclusions about general intelligence, brittleness, or internal cognitive mechanisms.

# Draft-level recommendation

- **Use Draft B as the structural base.** It respects the denominator, uses the endpoint-heavy framing, keeps failure labels as recorded classifications, preserves the unscored column, and avoids most causal overreach.
- **Do not carry forward Draft A’s failure-mapping section, cognitive framing, dirty-repo mechanism speculation, or closing characterization.**
- Before publication:
  1. Replace all `[ac-word]` and `[m-word]` placeholders.
  2. Remove the emoji.
  3. Fix the incomplete figure in Draft B.
  4. Correct “half” to **17/36 = 47%**.
  5. Remove or replace polyfill.io.
  6. Pin MathJax to an exact version.
  7. Plot only the **36 scored environments**, or display the two unscored-only environments separately.

&&&&&&&&&&&&&&&&

opus 5:

# CLAIM KILLER — POST-02 Verification Report
**Target:** Cross-environment outcome map (Mercury-2.5) · Drafts A (Gemini 3.1 Pro) and B (GPT 6 Sol Max)
**Method:** Every number recomputed from the evidence packet; every factual assertion traced to a packet line; every inference tested against what the packet can and cannot establish.

---

## 0. Independent recomputation (packet integrity check — PASSED)

I rebuilt the full 38-environment table from the packet and recomputed everything:

| Quantity | Recomputed | Packet | Status |
|---|---:|---:|---|
| Environments | 38 | 38 | ✓ |
| Selected cases | 416 | 416 | ✓ |
| Scored / unscored | 405 / 11 | 405 / 11 | ✓ |
| PASS / FAIL | 277 / 128 | 277 / 128 | ✓ |
| Pooled scored rate | 0.683951 → 68.4% | 0.684 | ✓ |
| All-selected rate | 0.665865 → 66.6% | 0.666 | ✓ |
| Perfect / zero / partial envs | 17 / 7 / 12 | 17 / 7 / 12 | ✓ |
| Cases in those groups | 172 / 68 / 165 | 172 / 68 / 165 | ✓ |
| Partial passes | 105 | 105 | ✓ |
| Group shares of 405 | 42.47% / 16.79% / 40.74% | 42.5 / 16.8 / 40.7 | ✓ |
| Unweighted mean of 36 env fractions | 0.69208 → 69.2% | ≈69.2% | ✓ |
| Median of 36 env fractions | 0.8889 = 8/9 | 8/9 | ✓ |
| Failure-mode sum | 128 | 128 | ✓ |
| Judge guarantees | 189+227 = 416 | 416 | ✓ |
| glyph+moco+batchnorm | 94 cases / 56 fails = 23.2% / 43.8% | same | ✓ |

**New counterfactuals computed for adjudicating Draft A's weighting claims** (these are not in the packet; I derived them and they are safe to use):
- Pooled rate **excluding moco**: 241/350 = **68.86%** (Δ = +0.47 pt)
- Pooled rate **excluding glyph**: 277/381 = **72.70%** (Δ = +4.31 pt)
- Pooled rate **excluding both**: 241/326 = **73.93%**
- moco counterfactually shrunk to 9 cases at its own 65.5% rate: **≈68.8%** (Δ ≈ +0.4 pt)

These numbers decide two disputed claims below.

---

## 1. Verdict key

| Verdict | Meaning |
|---|---|
| **SUPPORTED** | Directly entailed by the packet; may be stated flat. |
| **CORRECT-ARITHMETIC** | Number recomputed and confirmed exact (including rounding). |
| **NARROW** | True only of this archive / this selection / these judged cases; needs an in-sentence scope limiter. |
| **UNSUPPORTED** | Packet does not establish it; cut or rewrite. |
| **NEEDS-CHECK** | Requires evidence not in the packet (cross-tab, logs, seeds) before it can be stated at all. |
| **ARTIFACT** | Production defect (placeholder, emoji, broken asset, dead script). |

---

## 2. Claim-by-claim verification table

### 2.1 Top-line counts and rates

| # | Claim (verbatim, draft) | Verdict | Evidence source | Required action |
|---|---|---|---|---|
| 1 | A: "a scored pass rate of 0.684" | CORRECT-ARITHMETIC | 277/405 = 0.68395 → 0.684 | Keep. Blueprint: 68.4% is the retained headline. |
| 2 | A: "Out of 405 scored cases, the model passed 277 and failed 128." | SUPPORTED | Packet line 2 | Keep verbatim. |
| 3 | A: "416 selected cases spanning 38 distinct environments (with 11 cases remaining unscored)" | SUPPORTED | Packet line 1 | Keep. |
| 4 | A: "solving roughly two-thirds of what is thrown at it" | NARROW | 0.684 is a share of *scored selected cases*, not of a task universe | Rewrite as "two-thirds of the scored cases in this selection" or cut. |
| 5 | A: "the illusion of a smooth 68.4% capability level shatters" | NARROW | Packet supports dispersion; "capability level" is not measured | Keep dispersion point; drop "capability". |
| 6 | B: "Mercury-2.5 passed 68.4% of the scored cases in this campaign." | CORRECT-ARITHMETIC | 277/405 | Keep. |
| 7 | B: "**416 selected cases in 38 environments**" | SUPPORTED | Packet line 1 | Keep. |
| 8 | B: "405 received a PASS or FAIL judgment: 277 PASS and 128 FAIL" | SUPPORTED | Packet line 2 | Keep. |
| 9 | B: "**277/405, or 68.4%,** is the scored-case pass rate" | CORRECT-ARITHMETIC | 0.68395 | Keep as the precise counting answer (blueprint). |
| 10 | B: "**277/416, or 66.6%,** answers a different question—the share of *all selected cases with an observed PASS*" | CORRECT-ARITHMETIC + SUPPORTED | 0.66587 → 0.666; framing matches packet's two-rate distinction | Keep; this is the correct framing of the 66.6% figure. |
| 11 | B: "It must not be presented as a pass rate that silently turns the 11 unknown outcomes into failures." | SUPPORTED | 11 unscored are unjudged, not FAIL | Keep. |
| 12 | A: "The scored pass rate is rigorously 277/405 (0.684)... the former is the mathematically sound metric" | NARROW | Both rates are arithmetically sound; they answer different questions | Soften to B's framing (two questions, not one correct/one wrong). |

### 2.2 Endpoint structure

| # | Claim | Verdict | Evidence source | Required action |
|---|---|---|---|---|
| 13 | A: "Out of the 36 scored environments, exactly two-thirds reside at the absolute extremes" | CORRECT-ARITHMETIC | 24/36 = 0.6667 exactly | Keep; "exactly two-thirds" is literally exact. |
| 14 | A: "The model achieved flawless performance in 🤬 half the scored environments." | **UNSUPPORTED + ARTIFACT** | 17/36 = 47.2%, not half; emoji is a production artifact | **Blueprint-mandated fix:** replace with "17 of 36 (47%)" and delete the emoji. |
| 15 | A: full 17-environment perfect-pass enumeration (9/9 ×9, 18/18, 15/15 ×2, 23/23, 6/6 ×2, 4/4 ×2) | SUPPORTED | Packet perfect-pass list; sums to 172 | Keep (or defer to B's table). |
| 16 | A: "7 zero-pass environments... 0/9 in functorial_augmentation, monadic_reward, sheaf_invariant_gluing, sheaf_physical_constraints... 0/4 in ts_one_step and ts_trajectory... 0/24 in glyph" | SUPPORTED | Packet zero-pass list; sums to 68 | Keep. |
| 17 | A: "This leaves just 12 partial-pass environments" | SUPPORTED | 36 − 17 − 7 = 12 | Keep. |
| 18 | A: "they represent only a third of the *environments*" | CORRECT-ARITHMETIC | 12/36 = 33.3% | Keep. |
| 19 | A: "exactly 165 out of the 405 scored cases, or 40.7%" | CORRECT-ARITHMETIC | 165/405 = 0.40741 | Keep. |
| 20 | A: "we would expect most environments to cluster around that mean, perhaps following a standard normal distribution" | UNSUPPORTED | Pass fractions are bounded [0,1] small-n ratios; normality is not the right null | Rewrite: "we would expect most environments near 0.68"; delete "standard normal". |
| 21 | A: "The outcomes are intensely endpoint-heavy." | SUPPORTED | 24/36 at endpoints | Keep — matches blueprint ("endpoint-heavy, not bimodal"). |
| 22 | B: "Twenty-four of the 36 environments with scored cases sit at an observed endpoint" | CORRECT-ARITHMETIC | 17+7 = 24 | Keep. |
| 23 | B: "I would call the map *endpoint-heavy*, not declare a statistically bimodal capability." | SUPPORTED | Blueprint decision; packet gives no distributional test | Keep — this is the canonical formulation. |
| 24 | B: "Some endpoints are based on four cases, others on 23 or 24" | SUPPORTED | ts_* 4; epistemic_games 23; glyph 24 | Keep. |
| 25 | B: "the table alone cannot tell us how stable any endpoint would be under new cases or seeds" | SUPPORTED | Single seed per selected cell | Keep. |
| 26 | B: partial environments "range from 2/15 to 8/9" | CORRECT-ARITHMETIC | min 0.133 (batchnorm_ema), max 0.889 (three envs) | Keep. |
| 27 | A: "it represents the arithmetic mean of a landscape where..." | **UNSUPPORTED (arithmetic error)** | 0.684 is the **case-weighted pooled** rate; the arithmetic mean of the 36 env fractions is **69.2%** | **Must fix.** Say "case-weighted pooled rate"; optionally contrast with the 69.2% unweighted mean. |

### 2.3 Group-level table (Draft B's convention — blueprint keeps it)

| # | Claim | Verdict | Evidence source | Required action |
|---|---|---|---|---|
| 28 | B: "Every scored case passed \| 17 \| 172/172 \| 42.5% \| 0" | CORRECT-ARITHMETIC | 172/405 = 0.42469 | Keep. |
| 29 | B: "No scored case passed \| 7 \| 0/68 \| 16.8% \| 0" | CORRECT-ARITHMETIC | 68/405 = 0.16790 | Keep. |
| 30 | B: "Some passed, some failed \| 12 \| 105/165 \| 40.7% \| 1" | CORRECT-ARITHMETIC | 105 partial passes; 165/405 = 0.40741; 1 unscored = rd_adaptive_halting | Keep — including the unscored column (blueprint). |
| 31 | B: "No scored cases \| 2 \| — \| — \| 10" | SUPPORTED | epistemic_silence 6 + epistemic_type_games 4 = 10 | Keep. |
| 32 | B: "**Total** \| **38** \| **277/405** \| **100%** \| **11**" | CORRECT-ARITHMETIC | 42.5+16.8+40.7 = 100.0 | Keep. |
| 33 | B: 36-row per-environment table (all pass / none pass / partial / unscored-only) | SUPPORTED — every row matched | Row-by-row diff against packet: **zero discrepancies** | Adopt wholesale as the article's master table. |
| 34 | B: "`rd_adaptive_halting` \| 8/14 \| 1" and "**8/14 scored, plus one unscored**—not a 15-case judgment with an assumed failure" | SUPPORTED | Packet: 8/14 scored +1 unscored | Keep; this is the model treatment of unscored cases. |
| 35 | A: Figure caption "pass rates across the 38 environments" | UNSUPPORTED (precision) | Only 36 environments have a scored rate | Change to "36 environments with scored cases". |

### 2.4 Family-name claims

| # | Claim | Verdict | Evidence source | Required action |
|---|---|---|---|---|
| 36 | A: "`ts_*` (TypeScript/Tree-Search) family" | **UNSUPPORTED** | Packet never expands the prefix | Delete the gloss; use the literal environment names. |
| 37 | A: "The evidence in this archival campaign **proves that assumption completely false**. Family labels do not predict outcomes." | UNSUPPORTED (overclaim) | Packet shows 3 within-prefix divergences; it cannot establish a general predictive failure | Downgrade to B's formulation: a shared name is an unreliable shortcut *within this archive*. |
| 38 | A/B: ts_parse_only 4/4 vs ts_one_step 0/4 vs ts_trajectory 0/4 | SUPPORTED | Packet lists | Keep. |
| 39 | B: "That is a fair description of these **three sets of four judged cases**. It is not evidence that we have measured a smooth difficulty ladder." | SUPPORTED | 12 judged cases total; no difficulty scale in packet | Keep — this is the correct scope limiter. |
| 40 | A/B: sheaf_schema_sync 8/9 vs sheaf_invariant_gluing 0/9 vs sheaf_physical_constraints 0/9 | SUPPORTED | Packet lists | Keep. |
| 41 | A: "The model performed exceptionally well on `sheaf_schema_sync`... one might assume Mercury-2.5 has a robust grasp of sheaf mechanics" | NARROW | 8/9, single seed, no difficulty scale | Keep only as the hedged hypothetical it is; prefer B's wording. |
| 42 | A: "A shared prefix does not imply shared **cognitive demands** or even a shared evaluation infrastructure." | UNSUPPORTED | "Cognitive demands" is unmeasured; infrastructure differences are not recorded in the packet | Cut "cognitive"; cut the infrastructure half or mark as open question. |
| 43 | B: "`categorical_lenses` passed 9/9, `functorial_augmentation` passed 0/9, and `tensor_functor` passed 6/9" | SUPPORTED | Packet lists | Keep — strongest within-theme contrast available. |
| 44 | B: "They do not establish which task property caused a pass or a failure." | SUPPORTED | No per-case attributes in packet | Keep. |
| 45 | A: "The outcome map is tightly conditioned on the specific environment, not the broad conceptual label" | NARROW | True descriptively for this archive; "conditioned" implies causal structure | Restate descriptively: outcomes vary sharply between similarly named environments. |

### 2.5 Failure modes — the highest-risk section

| # | Claim | Verdict | Evidence source | Required action |
|---|---|---|---|---|
| 46 | A/B: underfit 51, overfit_visible_tests 49, RUNTIME_ERROR 9, source_invalid 9, invalid_action 5, training_failed 3, runtime_error 2 | SUPPORTED | Packet; sums to 128 | Keep the full list. |
| 47 | A: "Together, these 100 cases..." / B: "The first two labels account for 100/128 failures." | CORRECT-ARITHMETIC | 51+49 = 100 | Keep. |
| 48 | A: "the remaining 28 failures" | CORRECT-ARITHMETIC | 9+9+5+3+2 = 28 | Keep the count; see #52 for the surrounding framing. |
| 49 | A: "When **I analyzed the error logs**, I found a sharp divide..." | **UNSUPPORTED (fabricated method)** | Packet contains aggregate label counts only — no logs, no per-case records | Delete. Replace with "the archive records these labels". |
| 50 | A: "These are standard **cognitive failure modes**" | UNSUPPORTED + blueprint violation | Labels are recorded classifications, not observations of internal reasoning | **Blueprint-mandated removal** of "cognitive failure modes" framing. |
| 51 | A: "responsible for the bulk of the attrition in environments like `moco` (where the model dropped 19 cases)" | **MIXED: 19 is CORRECT-ARITHMETIC (55−36); the attribution is UNSUPPORTED** | Packet explicitly states failure modes are **not** matched to environments | Keep "19 failures in moco"; delete the claim that underfit/overfit caused them. |
| 52 | A: "the remaining 28 failures are **deeply suspicious**" | UNSUPPORTED | Packet offers no basis for suspicion beyond the casing duplicate | Cut or reduce to a neutral observation. |
| 53 | A: "these identical counts of 9 act as a **glaring data-quality flag**. It is **highly probable that these failure modes perfectly map to the zero-pass (0/9) environments**." | **UNSUPPORTED — primary blueprint deletion** | Packet: counts do not map modes to environments. 4 of the 7 zero-pass envs are 9-case; glyph is 24, two are 4-case. 9+9=18 ≠ 68 | **Delete the causal speculation** (blueprint). At most: nine-count coincidence warrants inspecting case logs. |
| 54 | A: "we are no longer measuring the model's reasoning capabilities; we are **measuring a broken harness**" | UNSUPPORTED | No harness-state evidence in packet | Delete. |
| 55 | A: "the casing discrepancy... is a classic tell of **disjoint evaluation pipelines**... this is a **parser discrepancy in the logging infrastructure**" | UNSUPPORTED | Casing supports a data-quality flag only; pipeline/parser diagnosis is invented | Reduce to B's line: casing is a data-quality flag, not evidence of two kinds of runtime failure. |
| 56 | A: "I suspect the latter is responsible for at least a portion of the 7 zero-pass environments" | UNSUPPORTED | No evidence links any failure mode to any environment | Delete (blueprint). |
| 57 | A: "infrastructural ghosts" (×2, incl. epistemic-status "harness artifacts") | UNSUPPORTED (rhetorical) | Not established | Delete the framing, including from the epistemic-status block. |
| 58 | B: "They are recorded classifications, however, not observations of Mercury-2.5's internal reasoning. I cannot infer an internal mechanism from their names." | SUPPORTED | Packet gives labels only | Keep — this is the correct replacement for A's §Failure Modes. |
| 59 | B: "I also would not build a story around the difference between `RUNTIME_ERROR` and `runtime_error`. Their casing is a data-quality flag" | SUPPORTED | Packet lists both separately; no semantics given | Keep. |
| 60 | B: "several environments contain nine cases, including all-fail environments. But the counts provided here do **not** match failure modes to environments." | SUPPORTED | Packet explicitly | Keep — load-bearing correction to A. |
| 61 | B: "A nine-count coincidence is reason to inspect case logs... not permission to assign one." | SUPPORTED | Correct epistemic status | Keep as the section's conclusion. |

### 2.6 Case density / weighting

| # | Claim | Verdict | Evidence source | Required action |
|---|---|---|---|---|
| 62 | A/B: moco 55 cases/15 tuples; glyph 24/12; epistemic_games 23/8; css_state_machine 18/9 | SUPPORTED | Packet "Cases vs tuples" | Keep all four pairs. |
| 63 | A: "the 405 scored cases—is not evenly distributed across the 36 scored environments" | SUPPORTED | Case counts range 4–55 | Keep. |
| 64 | A: "Because `moco` contains 55 cases, its 36 passes and 19 failures **heavily dictate** the 68.4% global average." | **UNSUPPORTED (refuted by computation)** | Excluding moco: 241/350 = **68.86%**, a shift of **0.47 pt**. moco is 13.6% of cases and sits near the pooled rate (65.5%) | Replace with the quantified truth: moco is the largest single block (13.6%) but, scoring near the pooled rate, barely moves it. |
| 65 | A: "If `moco` had been a standard 9-case environment, the pooled pass rate would be **demonstrably different**." | **UNSUPPORTED (refuted)** | Same rate at 9 cases → ≈**68.8%** (Δ ≈ 0.4 pt) | Delete or invert. |
| 66 | A: "`glyph`'s 0/24 failure acts as a massive anchor dragging the average down." | NARROW — directionally right, quantify it | Excluding glyph: 277/381 = **72.7%** (Δ = **+4.3 pt**); excluding glyph and moco: 73.9% | Keep but replace "massive anchor" with the computed 68.4% → 72.7% delta. |
| 67 | A: "heavily weighted by **how aggressively the authors decided** to unroll tuples into cases" | UNSUPPORTED (intent attribution) | Packet records counts, not selection intent | Restate as B does: the pooled result is shaped by where cases were selected. |
| 68 | B: "`moco` alone contributes 55 scored cases—**13.6%** of the scored campaign" | CORRECT-ARITHMETIC | 55/405 = 0.13580 | Keep. |
| 69 | B: "these three environments supply **94/405 scored cases but 56/128 failures**" | CORRECT-ARITHMETIC | 24+55+15 = 94 (23.2%); 24+19+13 = 56 (43.8%) | Keep; consider adding the two percentages. |
| 70 | B: "`moco` has 36/55, or 65.5%, with 19 failures. `batchnorm_ema` has 2/15, or 13.3%, with 13 failures." | CORRECT-ARITHMETIC | 0.6545, 0.1333; 55−36 = 19, 15−2 = 13 | Keep. |
| 71 | B: "`glyph` has 0/24: a larger all-fail block than the four-case `ts_*` endpoints." | SUPPORTED | 24 > 4 | Keep. |
| 72 | B: "It does not tell me that the three share a failure mechanism." | SUPPORTED | No cross-tab | Keep. |
| 73 | B: "the 405 cases are not 405 distinct tuples... These aggregates do not give me enough information to estimate within-tuple dependence." | SUPPORTED | Four documented case/tuple mismatches; no per-tuple data | Keep. |
| 74 | B: "the mean of their observed pass fractions is about **69.2%**, close to the case-weighted 68.4%" | CORRECT-ARITHMETIC | Recomputed 0.69208 over 36 envs | Keep. |
| 75 | B: "Their median is **8/9, or 88.9%**." | CORRECT-ARITHMETIC | Median of 36 fractions = 0.88889 | Keep. |
| 76 | B: "The median hides seven all-fail environments; either mean hides how often the scorecard reaches an endpoint." | SUPPORTED | 7 zero-pass; 24/36 endpoints | Keep. |
| 77 | B: "`gnn_message_passing`, `regex_state_machine`, and `ssm_parallel_scan` each have 5/9, while `sheaf_schema_sync`, `sql_fixed_point`, and `transformer_ssm_lift` each have 8/9." | SUPPORTED | Packet partial list | Keep. |
| 78 | B: "Identical fractions do not make those environments interchangeable." | SUPPORTED | No shared scale | Keep. |

### 2.7 Confounds and limits

| # | Claim | Verdict | Evidence source | Required action |
|---|---|---|---|---|
| 79 | A: "11 unscored cases: 6 in `epistemic_silence`, 4 in `epistemic_type_games`, and 1 orphaned case in `rd_adaptive_halting`" | SUPPORTED | Packet | Keep ("orphaned" → neutral wording). |
| 80 | A: "reducing our total scored environment count from 38 to 36" | SUPPORTED | 38 − 2 unscored-only | Keep. |
| 81 | A: "189 cases evaluated via `behavioral_reference` and 227 via `compile_only`" | CORRECT-ARITHMETIC | 189+227 = 416 = selected cases | Keep; state that the sum matches selected cases. |
| 82 | A: "We do not know if `behavioral_reference` is systematically more stringent than `compile_only`." | SUPPORTED | No per-environment breakdown | Keep. |
| 83 | B: "Without an environment-by-guarantee breakdown, I cannot test whether the apparent environment contrasts change when judged to the same standard. Calling every perfect-pass environment behaviorally solved would outrun this evidence." | SUPPORTED | Packet gives totals only | Keep — best statement of the judge caveat. |
| 84 | A: "Each selected cell... was run with a single seed. We have absolutely no insight into variance or stability." | SUPPORTED | Packet: single seed per selected cell | Keep. |
| 85 | A: "Is a 5/9 in `regex_state_machine` the true mean... a different seed would yield a 9/9 or a 1/9?" | SUPPORTED (5/9 correct; question is properly hypothetical) | Packet | Keep. |
| 86 | A: "In the endpoint-heavy environments (the 1.0s and 0.0s), **a single seed is less concerning**" | **UNSUPPORTED** | No variance data at all; a 4/4 or 0/4 endpoint is among the *least* stable observations. Directly contradicts B's correct caution | Delete; adopt B's line that small endpoints are small observed endpoints. |
| 87 | A: "the source repository was 'dirty at run time.' This is a reproducibility nightmare. It implies that uncommitted changes, leftover state, or artifact files were present" | NARROW | Packet states the fact only; the enumeration is inference | Keep the fact; soften to "the exact working-tree state matters for reproduction" (B's wording). |
| 88 | A: "We cannot easily isolate whether the model **relied on leaked state** in the perfect-pass environments, or was **derailed by broken state** in the zero-pass environments." | UNSUPPORTED | Introduces a leakage hypothesis with no supporting evidence | Delete. |
| 89 | B: "each selected cell has **one seed**, and the source repository was **dirty at run time**... Neither fact proves that a particular score is wrong. Both narrow what I can responsibly conclude." | SUPPORTED | Packet | Keep verbatim-equivalent. |
| 90 | B: "An environment-by-judge and environment-by-failure-mode cross-tab, followed by repeated runs, would help distinguish those possibilities." | SUPPORTED (forward-looking) | Identifies the exact missing evidence | Keep as the closing methodological ask. |

### 2.8 Closings and framing

| # | Claim | Verdict | Evidence source | Required action |
|---|---|---|---|---|
| 91 | A: "the model's outcomes are profoundly **environment-conditioned**" (stated "beyond a doubt") | NARROW | Dispersion is real; "beyond a doubt" + causal verb overstate | Restate descriptively; drop "beyond a doubt". |
| 92 | A: "It **proves** that domain names and family prefixes are **useless** for predicting performance." | UNSUPPORTED (overclaim) | Three divergent prefix groups ≠ proof of uselessness | Downgrade to "unreliable within this archive". |
| 93 | A: "We cannot claim that 'environment identity dominates difficulty' because we do not have a shared difficulty scale" | SUPPORTED | No difficulty scale in packet | Keep — A and B agree; retain this. |
| 94 | A: "A 9/9 in `tokenizer_adjunction` and a 0/24 in `glyph` do not mean the model is 'smart' at one and 'dumb' at the other" | SUPPORTED | Counts correct; interpretation correctly withheld | Keep. |
| 95 | A: "Mercury-2.5 not as a uniformly 68.4% capable entity, but as a **brittle, contextual engine**—one whose successes are absolute, whose failures are structural" | **UNSUPPORTED + blueprint violation** | "Structural failures" is exactly the unestablished causal claim; blueprint orders removal | **Delete the closing** (blueprint). |
| 96 | B: "on this archived selection, Mercury-2.5 received **277 PASS judgments among 405 scored cases**, with observed all-pass outcomes in 17 environments, all-fail in seven, mixed in 12, and no scored outcome in two" | SUPPORTED | Packet, fully | Adopt as the article's summary sentence. |
| 97 | B: "The result is *not* that environment identity 'dominates difficulty'" | SUPPORTED | No common scale | Keep. |
| 98 | B: "Nor does this map identify a model-internal cause for `glyph` or `batchnorm_ema`" | SUPPORTED | No mechanism data | Keep. |
| 99 | B: "So I would keep **68.4%** as the answer to a precise counting question" | SUPPORTED + blueprint-aligned | Blueprint: keep 68.4% as precise counting answer | Keep as closing. |
| 100 | B: "especially the zeros, the perfect scores, and the 40.7% of scored cases lying in between" | CORRECT-ARITHMETIC | 165/405 | Keep. |

---

## 3. Production-artifact register (all must be cleared before publication)

| # | Artifact | Location | Action |
|---|---|---|---|
| A1 | `[ac-word]` — occurrence 1 | A, intro: "what Mercury-2.5 [ac-word] did during this campaign" | Resolve to real word; blueprint orders removal |
| A2 | `[ac-word]` — occurrence 2 | A, §Confounds 2: "how much of the environment-conditioned variance is [ac-word] judge-conditioned variance" | Resolve/remove |
| A3 | `[ac-word]` — occurrence 3 | A, §Limits: "what does this cross-environment outcome map [ac-word] tell us" | Resolve/remove |
| A4 | 🤬 emoji | A, perfect-pass bullet | Delete (blueprint) |
| A5 | `[m-word]` — occurrence 1 | B, §Names: "would discard the comparison that [m-word]s" | Resolve/remove |
| A6 | `[m-word]` — occurrence 2 | B, §A case is not a tuple: "Those paired counts [m-word]" | Resolve/remove |
| A7 | Orphan `!` on its own line (broken image markdown — figure missing alt/src) | B, before Figure 2 caption | Restore the figure reference or delete the caption |
| A8 | `polyfill.io` script tag | A, head block | Remove — dead/compromised CDN; MathJax 3 needs no polyfill for target browsers |
| A9 | Single trivial display-math block (`Pass Rate = Passed/Scored`) is the only MathJax use | A, §Gravitational Pull | Either drop MathJax entirely or justify it; one trivial fraction does not warrant two script includes |
| A10 | Figure 2 path `../figures/fig2_lollipop.svg` (relative, untested) | A | Verify asset resolves at build |
| A11 | Caption says "38 environments" for a pass-rate chart | A, Figure 2 caption | Correct to 36 scored environments |
| A12 | Epistemic-status block asserts "revealing underlying harness artifacts" | A, `<dd>` Synthesis | Rewrite — harness artifacts are not established |
| A13 | Two different titles / framings across drafts | A vs B title lines | Pick one; B's title carries the 68.4% + 38-environment frame |
| A14 | Trailing whitespace after several A paragraphs | A, multiple | Clean at build |

---

## 4. Causal-inference register (inferences that outrun the evidence)

| # | Inference | Draft | Why it fails | Disposition |
|---|---|---|---|---|
| C1 | RUNTIME_ERROR(9) and source_invalid(9) map onto the 0/9 environments | A | Packet explicitly does not match modes to environments; 9+9=18 cannot cover 68 zero-pass cases; glyph(24) and two 4-case envs are not 9-case | **DELETE (blueprint)** |
| C2 | Zero-pass environments reflect a broken harness rather than model behavior | A | No harness-state evidence | DELETE |
| C3 | Casing split indicates disjoint pipelines / a parser bug | A | Casing supports only a data-quality flag | Reduce to data-quality flag |
| C4 | underfit/overfit explain moco's 19 failures | A | No environment × mode cross-tab | DELETE attribution; keep the 19 |
| C5 | Possible state leakage explains perfect-pass environments | A | Pure speculation from "dirty repo" | DELETE |
| C6 | moco's size "heavily dictates" the pooled rate | A | Refuted: Δ = 0.47 pt | REPLACE with computed delta |
| C7 | Authors' unrolling choices drive the headline number | A | Intent not recorded | Restate as selection composition |
| C8 | Family prefixes are "proven useless" predictors | A | Three cases ≠ proof | Downgrade to archive-local |
| C9 | Single seed is "less concerning" at endpoints | A | No variance data; small endpoints are the fragile ones | DELETE |
| C10 | Failure labels describe cognition | A | Labels are classifications | DELETE (blueprint) |

Draft B contains **no** causal inferences that outrun the packet. Its failure-mode, judge, seed, and repo sections are all correctly scoped.

---

## 5. Arithmetic / numeric error register

| # | Error | Draft | Correct value |
|---|---|---|---|
| E1 | "flawless performance in half the scored environments" | A | 17/36 = **47.2%** — not half (blueprint-mandated correction) |
| E2 | 0.684 called "the arithmetic mean" of environment outcomes | A | 0.684 is the **case-weighted pooled** rate; the unweighted mean of the 36 env fractions is **69.2%** |
| E3 | moco "heavily dictates" the global average | A | Excluding moco → **68.86%** (Δ 0.47 pt) |
| E4 | "If moco had been 9 cases the rate would be demonstrably different" | A | ≈**68.8%** (Δ ≈ 0.4 pt) |
| E5 | "pass rates across the 38 environments" (figure) | A | **36** environments have a scored rate |
| E6 | "massive anchor" (glyph) — unquantified | A | Quantifiable: excluding glyph → **72.70%** (Δ +4.31 pt). Directionally correct, needs the number |

**Draft B: zero arithmetic errors found.** All 36 table rows, both headline rates, all four group shares, 13.6%, 65.5%, 13.3%, 94/405, 56/128, 69.2%, and 8/9 median verified exact.

---

## 6. SAFE CLAIM SET
*Statable flat, with no in-sentence caveat. Every item recomputed and confirmed.*

1. The archive contains 416 selected cases across 38 environments.
2. 405 cases received a PASS or FAIL judgment; 11 were unscored.
3. 277 PASS and 128 FAIL among the 405 scored cases.
4. The scored-case pass rate is 277/405 = 68.4%.
5. 277/416 = 66.6% is the share of all selected cases with an observed PASS — a different quantity.
6. 36 environments have at least one scored case; 2 have none.
7. 17 environments had every scored case pass (172/172); that is 17 of 36, or 47%.
8. 7 environments had no scored case pass (0/68).
9. 12 environments had mixed outcomes (105/165), with one additional unscored case.
10. 24 of the 36 environments with scored cases sit at an observed endpoint.
11. The three groups hold 42.5%, 16.8%, and 40.7% of the 405 scored cases respectively.
12. The partial environments range from 2/15 to 8/9.
13. The unscored cases are 6 in `epistemic_silence`, 4 in `epistemic_type_games`, 1 in `rd_adaptive_halting`.
14. `rd_adaptive_halting` is 8/14 scored plus one unscored.
15. `ts_parse_only` 4/4; `ts_one_step` 0/4; `ts_trajectory` 0/4.
16. `sheaf_schema_sync` 8/9; `sheaf_invariant_gluing` 0/9; `sheaf_physical_constraints` 0/9.
17. `categorical_lenses` 9/9; `functorial_augmentation` 0/9; `tensor_functor` 6/9.
18. `glyph` 0/24; `moco` 36/55 (65.5%, 19 failures); `batchnorm_ema` 2/15 (13.3%, 13 failures).
19. Those three environments supply 94 of 405 scored cases (23.2%) and 56 of 128 failures (43.8%).
20. `moco` contributes 55 scored cases, 13.6% of the scored campaign.
21. Case/tuple pairs: moco 55/15, glyph 24/12, epistemic_games 23/8, css_state_machine 18/9.
22. The unweighted mean of the 36 environment pass fractions is about 69.2%; the median is 8/9 (88.9%).
23. Failure labels: underfit 51, overfit_visible_tests 49, RUNTIME_ERROR 9, source_invalid 9, invalid_action 5, training_failed 3, runtime_error 2 — summing to 128; the first two account for 100 of 128.
24. The campaign records 189 `behavioral_reference` and 227 `compile_only` judge guarantees, summing to the 416 selected cases.
25. Each selected cell was run with a single seed.
26. The source repository was dirty at run time.
27. The archive does not match failure modes to environments.
28. Excluding `glyph`, the pooled rate is 72.7%; excluding `moco`, 68.9%. *(Derived in §0; arithmetically exact.)*

---

## 7. QUALIFIED CLAIM SET
*May appear only with the stated limiter in the same sentence (blueprint: inline caveats, not batched).*

| Claim | Mandatory in-sentence qualifier |
|---|---|
| The map is endpoint-heavy. | "…**on this archived selection**" — and never "bimodal". |
| Similarly named environments landed far apart. | "…**within this archive**; a shared name is an unreliable shortcut, not a demonstrated non-predictor." |
| The `ts_*` trio reads as a progression. | "…a fair description of **three sets of four judged cases**, not a measured difficulty ladder." |
| Endpoints look decisive. | "…**some rest on four cases**, and a single seed per cell gives no stability estimate." |
| Partial environments carry real weight. | "…**165 of 405 scored cases (40.7%)**, too many to treat as noise — but identical fractions do not make environments interchangeable." |
| Case density shapes the headline. | "…**where cases were selected** shapes it; excluding `glyph` moves 68.4% to 72.7%, while excluding `moco` moves it only to 68.9%." |
| Nine `RUNTIME_ERROR` and nine `source_invalid` labels alongside several nine-case environments. | "…**a reason to inspect case logs**, not a basis for assigning modes to environments." |
| The `RUNTIME_ERROR` / `runtime_error` split. | "…**a data-quality flag**, not evidence of two kinds of runtime failure." |
| underfit and overfit_visible_tests dominate the failures. | "…as **recorded classifications**, not observations of internal reasoning." |
| Perfect-pass environments. | "…**observed all-pass under the judge guarantee applied**; with no environment-by-guarantee breakdown, they cannot be called behaviorally solved." |
| The dirty repo 👹. | "…it makes **the exact working-tree state important for reproduction**; it does not prove any score is wrong." (No leakage hypothesis.) |
| 66.6% may be mentioned. | "…**only as the share of all selected cases with an observed PASS**, never as a pass rate that recodes 11 unknowns as failures." |
| Environment identity and outcomes. | Never "dominates difficulty" — "**there is no common difficulty scale here**." |

---

## 8. Bottom line for the editor

- **Draft B is the numerically clean base.** Zero arithmetic errors, zero causal overreach, correct unscored handling, correct two-rate framing, and the table convention the blueprint retains. Its only defects are production artifacts: two `[m-word]` placeholders and one broken image line.
- **Draft A contributes usable prose only in three places** — the endpoint enumeration (#15–#19), the "no shared difficulty scale" concession (#93–#94), and the confound framing in §Confounds 1–3 (#79–#85), after the flagged sentences are cut.
- **Six numeric corrections (E1–E6) and ten causal deletions (C1–C10) are mandatory**, nine of which the Stage C blueprint already ordered.
- **Fourteen production artifacts (A1–A14) must be cleared**, including three `[ac-word]`, two `[m-word]`, one emoji, one broken image, and a dead polyfill CDN.
