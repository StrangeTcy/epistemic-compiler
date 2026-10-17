# Evidence Reviewer Response — POST-02 (Mercury-2.5 Cross-Environment Outcome Map)

Source: Battle Arena (two independent model responses), pasted by user 2026-10-17.
Prompt artifact: campaign-02-analysis/post-production/handoffs/POST-02_evidence_reviewer_prompt.md
Status: ACCEPTED (substantive; factual counts verified against environment_summary_v2.csv and case_results.csv)

--- BEGIN PASTED RESPONSE ---

unknown model:

# Evidence Reviewer Brief — POST-02 (Mercury-2.5 Cross-Environment Outcome Map)

**Scope note on evidence access:** My toolset is web search only; I have no direct read access to the zip archive, `findings.json`, or the actual SVG figures. Everything below is derived from the aggregated summary tables supplied in this task. Any reference to F-001–F-009 or to specific figure contents must be independently verified against the source files before publication — I flag this as a hard boundary throughout, not a formality.

## 1. Empirical question the post can answer

With the data available, the [d-word] question is narrow: **"Across the 38 environments and 416 selected (tuple × environment) cases that were [ac-word] run, how is mercury-2.5's pass/fail outcome distributed, and does knowing only the environment name let you predict the outcome?"**

It is *not*: "why does mercury-2.5 fail at category theory / sheaves / epistemic reasoning" (no mechanism data given), and it is not "how does difficulty scale" (no per-tuple breakdown provided — only environment-level aggregates). The post should be scoped to outcome distribution and predictability, not causal explanation.

## 2. Strongest candidate thesis and competing interpretations

**Draft thesis:** environment identity dominates difficulty labels; the 0.684 average conceals a sharp pass/fail split.

This is a reasonable first-order observation but is **not the strongest available thesis**, and "bimodal" is doing more rhetorical work than the numbers support. Competing/better-supported framings:

- **(A) Environment identity dominates (draft).** Partially true: 24/38 environments (63%) are perfectly consistent (17 at rate 1.0, 7 at rate 0.0). But this only resolves 63% of environments — it says nothing about the other 32% (12 partial environments), which is where most of the interesting variance lives.
- **(B) Task-*type* (static/parse vs. dynamic/execution) cuts across named environment families and predicts outcome better than environment identity.** The `ts_*` family splits 0% / 0% / 100% (ts_one_step, ts_trajectory vs. ts_parse_only) and the `sheaf_*` family splits 0% / 0% / 88.9% (sheaf_invariant_gluing, sheaf_physical_constraints vs. sheaf_schema_sync). Same naming family, opposite outcomes — this directly undercuts "environment identity" as the operative variable and points instead to something about what kind of task is being asked (parse/sync vs. simulate/predict-forward).
- **(C) Sampling-design artifacts (cases ≠ tuples) inflate the apparent determinism of some environments.** moco has 55 cases but only 15 tuples; css_state_machine has 18 cases vs. 9 tuples; epistemic_games 23 vs. 8; glyph 24 vs. 12. The "rate" for these environments is not a simple one-seed-per-tuple statistic as claimed elsewhere ("one seed per selected cell") — multiple cases map to the same tuple for at least four environments, which needs explanation before the headline rate can be trusted as a clean difficulty signal.
- **(D) Failure mode composition (underfit vs. overfit_visible_tests) may track judge guarantee type (behavioral_reference vs. compile_only), not environment per se.** This is a plausible but currently *untested* hypothesis — no cross-tab of guarantee type × failure mode × environment is in the summary.

The strongest [d-word] thesis for the post is a hybrid: **environment identity is a strong but incomplete predictor — fully determinative for roughly two-thirds of environments, but inside the same named family, task type (static analysis vs. dynamic execution) produces a bigger swing than the environment label implies.**

## 3. Precise observations and comparisons supporting it

- Overall: **277 PASS / 128 FAIL / 11 unscored of 416 selected** (405 scored); scored pass rate = 277/405 ≈ **0.684**.
- **17/38 environments at exactly 1.0** (architecture_naturality 9/9, categorical_lenses 9/9, ci_dependency_graph 9/9, css_state_machine 18/18, epistemic_announcements 6/6, epistemic_fragmented_observation 4/4, epistemic_games 23/23, epistemic_nested_knowledge 6/6, neuro_symbolic_parser 9/9, rd_gradient_credit 15/15, rd_state_carry 15/15, semiring_unification 9/9, spreadsheet_dataflow 9/9, stochastic_monad 9/9, template_interpreter 9/9, tokenizer_adjunction 9/9, ts_parse_only 4/4).
- **7/38 environments at exactly 0.0** (functorial_augmentation 0/9, glyph 0/24, monadic_reward 0/9, sheaf_invariant_gluing 0/9, sheaf_physical_constraints 0/9, ts_one_step 0/4, ts_trajectory 0/4).
- That is **24/38 (63.2%) of environments showing zero internal variance** — this is the real empirical anchor for any "environment [m-word]s a lot" claim.
- But the **remaining 12/38 (31.6%) partial environments span rates from 0.133 (batchnorm_ema, 2/15) to 0.889** (sheaf_schema_sync 8/9, sql_fixed_point 8/9, transformer_ssm_lift 8/9) — a continuous spread, not a second mode. Computing an unweighted mean across the 36 scored environments gives ≈0.692, close to but not identical to the case-weighted 0.684 — the two averages are similar enough here that weighting is not a major distortion, but this check needed to be done rather than assumed.
- Failure modes are dominated by two categories: **underfit (51) and overfit_visible_tests (49)**, together 100/128 = **78% of all failures**. Infrastructure/process failures (RUNTIME_ERROR 9 + runtime_error 2 + source_invalid 9 + invalid_action 5 + training_failed 3 = 28) account for only **~22%** of failures. This [m-word]s for the post's framing: most failures look like genuine capability misses (wrong fit to spec), not environment breakage — but see §5 on the RUNTIME_ERROR/runtime_error case-split as a taxonomy flag.

## 4. Cases and tuple dimensions that [m-word]

- **Family-internal splits are the sharpest evidence against pure environment-identity framing:**
  - `ts_*`: ts_one_step (0/4), ts_trajectory (0/4) vs. ts_parse_only (4/4, 100%). Same domain, opposite outcome by task type (static parse vs. dynamic prediction/trajectory).
  - `sheaf_*`: sheaf_invariant_gluing (0/9), sheaf_physical_constraints (0/9) vs. sheaf_schema_sync (8/9, 88.9%). Again, "gluing/constraints" (structural invariant-preservation) fails completely while "schema_sync" mostly passes.
  - `epistemic_*`: four scored sub-environments are all 100% (announcements, fragmented_observation, games, nested_knowledge), but **epistemic_silence (6 cases) and epistemic_type_games (4 cases) are entirely unscored** — the family cannot be called "solved" as a whole; 10 cases have no verdict at all.
- **Cases-vs-tuples mismatch** is a dimension the post must address directly: moco (55 cases / 15 tuples), css_state_machine (18/9), epistemic_games (23/8), glyph (24/12) all have more cases than tuples, meaning the per-environment rate is not a uniform one-seed-per-tuple statistic. moco alone contributes 55/405 ≈ 13.6% of all scored cases and 36/277 ≈ 13% of all passes — any environment-identity narrative needs to account for why moco is sampled so much more densely than, say, architecture_naturality (9 cases/9 tuples).
- **Judge guarantee split (189 behavioral_reference / 227 compile_only)** is a case-level dimension not currently cross-tabulated against environment or failure mode in the summary. Given that overfit_visible_tests is nearly as common as underfit, this is the single most promising unexplored axis for the post — but it cannot be asserted without the actual cross-tab.
- **rd_adaptive_halting has 15 cases, 14 scored, 1 unscored** — the only partial environment with an internal unscored case, distinct from the two wholly-unscored environments. This should not be folded into "11 unscored" as if homogeneous.

## 5. Strongest counterexamples and known confounds

- **Counterexample to "environment identity dominates":** the `ts_*` and `sheaf_*` family splits (§4) are the strongest available evidence that something other than the coarse environment label — likely task type (static/structural vs. dynamic/behavioral) — is doing the predictive work. The draft thesis needs to either absorb this (task-type as a sub-dimension of "environment") or concede it's a separate, more powerful axis.
- **Confound: dirty source repo at run time.** This is stated as a known condition, not a hypothesis. It directly threatens the interpretability of the 28 infrastructure-adjacent failures (RUNTIME_ERROR, runtime_error, source_invalid, invalid_action, training_failed) — some zero-pass environments could in principle owe part of their 0% rate to environment/repo state rather than model incapability. Without a per-environment failure-mode breakdown, this cannot be ruled out, and the post should not claim the 7 zero-pass environments are "genuine capability floors" without checking this.
- **Confound: inconsistent failure-mode casing.** RUNTIME_ERROR (9) and runtime_error (2) appear as separate categories in the register. This is very likely a logging/taxonomy artifact (same underlying condition, inconsistent capitalization) rather than two distinct failure types, and it should be flagged as a data-quality issue rather than silently merged or silently kept separate in any figure.
- **Confound: single seed per cell.** With one seed per selected cell, none of the partial-pass rates (e.g., batchnorm_ema's 2/15) can be distinguished from high-variance/noisy single-draws versus a true smooth difficulty gradient. A 0.133 rate could be "this environment is hard" or "this environment is bimodal at the tuple level with one seed landing badly" — the aggregate cannot distinguish these, which undercuts any claim about *why* the partial band exists.
- **Confound: unequal case density across environments weakens the "bimodal" visual.** Because glyph (24 cases) and moco (55 cases) carry outsized weight in any case-weighted histogram, a naive pass-rate histogram will visually exaggerate the modes at 0 and 1 relative to an environment-equal-weighted view. Both weightings should be shown, not just one.

## 6. Which visualisations make the evidence easier to understand

(Caveat: exact figure titles/contents cannot be confirmed from here — this is a recommendation list to check against the actual README/SVGs, not a report of what they show.)

- A **histogram of the 36 scored environments' pass rates** (not case-weighted) is the single most important check on "bimodal" — it would show whether the 12 partial environments cluster near 0.5 (true second mode) or skew high (0.55–0.89, as the raw numbers suggest), which materially changes the thesis.
- A **family-grouped bar chart** (ts_*, sheaf_*, epistemic_*, rd_*) placing same-prefix environments adjacent would visually make the §4 counterexamples (ts_parse_only vs. ts_one_step/trajectory; sheaf_schema_sync vs. the other two sheaf_* environments) immediately legible — this is probably the most persuasive single figure against the pure environment-identity draft thesis.
- A **cases-vs-tuples scatter or table** (environment on x-axis, cases/tuples ratio on y-axis) would expose the sampling-density confound (moco, css_state_machine, epistemic_games, glyph) before readers take the headline rate at face value.
- A **stacked failure-mode bar per environment** (underfit/overfit_visible_tests/infrastructure) would let readers see whether zero-pass environments fail for "capability" reasons (underfit/overfit) or "infrastructure" reasons (RUNTIME_ERROR/source_invalid), directly addressing the dirty-repo confound.
- If one of the 7 SVGs already is a guarantee-type (behavioral_reference/compile_only) breakdown, that should be the figure used to test the overfit_visible_tests hypothesis in §5 — this would be the most novel content in the post if it exists.

## 7. Boundaries between observation, interpretation, and hypothesis

- **Observation (directly countable from the summary):** 277/405 scored pass; 17 environments at 1.0; 7 at 0.0; 12 partial with rates 0.133–0.889; underfit (51) and overfit_visible_tests (49) are the two dominant failure modes; ts_* and sheaf_* families split internally.
- **Interpretation (reasonable reading, not proven):** that the 63%/37% split constitutes "environment identity as primary predictor"; that the ts_*/sheaf_* splits indicate task-type (static vs. dynamic) as a competing predictor; that the partial band skews toward "mostly reliable" rather than "coin flip."
- **Hypothesis (not supported by the data in hand, needs further cross-tabs):** that overfit_visible_tests correlates with compile_only judge guarantees; that infrastructure failure modes explain any part of the zero-pass environments' 0% rate; that the partial-band variance reflects a real difficulty gradient rather than single-seed noise.

The draft currently presents its central claim as settled observation when at least two load-bearing pieces (bimodality's shape, and environment-identity-as-sole-driver) sit in the interpretation/hypothesis zone, not the observation zone.

## 8. Claims that are NOT currently [d-word]

- **"Environment identity dominates difficulty labels"** as a universal claim — contradicted by the ts_* and sheaf_* within-family splits (§4, §5). At most this holds for the 24/38 environments with 0% or 100% rates; it explicitly does not hold for the 12 partial environments, which is a third of the dataset.
- **"Bimodal" as a precise statistical description of the full distribution** — true only if you restrict to 24/38 environments; the 12 partial-environment rates (0.133–0.889) do not cluster near 0.5 and instead form a right-skewed spread, which is a different shape than "bimodal" implies.
- **Any claim about *why* the 7 zero-pass environments fail (pure capability floor vs. infrastructure artifact)** — cannot be supported without per-environment failure-mode breakdown, which is not in the summary, and the dirty-repo caveat specifically threatens this inference.
- **Any claim about difficulty-tuple axes driving the partial-pass band** — no per-tuple pass/fail data is available here; single-seed-per-cell design means the partial rates could be noise, not a smooth difficulty gradient.
- **Any claim linking overfit_visible_tests to compile_only judge guarantees, or underfit to behavioral_reference guarantees** — plausible but entirely unverified; no cross-tab is provided.
- **Treating epistemic_* as a "fully solved" family** — two of six sub-environments (epistemic_silence, epistemic_type_games) are wholly unscored; "100% pass" claims about the family must be scoped to the four scored sub-environments only.
- **Any numeric claim attributed to F-001–F-009 or to specific figure content** — not independently verified in this review; must be checked against the actual files before the post cites them.

&&&&&&&&&&&&&&&

opus 5.5:

I couldn't open any of the referenced files. The archive, `findings.json`, `generated/` and `generated2/`, and the 7 SVGs are not in my sandbox. The input directory is empty. So this brief works only from the environment summary, failure-mode counts and key facts in your message. I re-checked the arithmetic and ran some tests on those numbers myself. I can't tell you what's in findings F-001..F-009 or in any specific figure. Anything that needs per-tuple or per-judge data is listed below as a check to run, not a finding.

# POST-02 Evidence Brief: Mercury-2.5 cross-environment outcome map

## 1. What the post can answer

**What it can answer:** In this Mercury-2.5, `reasoning_effort=high`, provider-`mercury` campaign, how did judged outcomes vary across the 38 selected environments, and how much does the pooled pass rate conceal variation among those environments?

**What it can't answer yet:** Whether *environment identity outweighs difficulty labels*, which is the draft's thesis. The difficulty axes are different in each environment, so there's no shared difficulty scale to compare against. In the 24 environments where every case passed or every case failed, difficulty has no variance at all, so "environment explains everything" is true there automatically. The question can only be tested inside the 12 partial-pass environments, and only with per-tuple data, which I don't have.

## 2. Strongest thesis and competing readings

**Recommended thesis ([d-word]):** *Outcomes differ far more between environments than a single 68% rate suggests. 24 of 36 scored environments are all-pass or all-fail. But a third are partial, and three known confounds have to be ruled out before this reads as a capability map: judge strength, harness failures and small-sample saturation.*

**Why I'd drop "bimodal":** The differences between environments are real. A chi-square test across the 36 scored environments gives χ² ≈ 257 (df = 35, p ≈ 1e-35). If every case had the same 0.684 pass chance, you'd expect about 1.8 all-pass and 0.04 all-fail environments; we see 17 and 7. But calling it "bimodal" claims two clusters of underlying ability, and the data doesn't show that:
- 12 of 36 environments (33%) are partial, and they hold **165 of 405 scored cases (40.7%)**.
- Most environments have only 4–9 cases, which pushes results toward 0% and 100%. An environment with a true pass rate of 0.9 would still show 9/9 about 39% of the time (0.9⁹ ≈ 0.39).

**Competing readings the post must address:**

| # | Reading | What would support it | Can we check it now? |
|---|---|---|---|
| A | Real capability differences between environments (the draft) | Splits survive stratifying by judge type and removing harness failures | Partly |
| B | **Judge-strength artifact.** 227/416 (54.6%) cases are compile_only | All-pass environments concentrated in compile_only | **No.** Needs a judge × environment cross-tab |
| C | **Harness/infrastructure artifact** in all-fail environments | One failure mode per all-fail environment; source_invalid or runtime errors | Partly (see §5) |
| D | **Task stage:** parsing/structure succeeds, execution/training fails | Contrasts inside families (ts, sheaf) | Suggestive; small samples |
| E | **Small-sample saturation** | 0% or 100% rates with wide confidence intervals | Yes: 4-case environments can't tell 0.5 from 1.0 |

## 3. Observations with exact counts

- **Headline rate:** 277/405 = **0.684** counts scored cases only. Counting all selected cases gives 277/416 = **0.666**. The post has to say which denominator it uses. Averaging the 36 environment rates gives 0.692, so the case-weighted headline isn't driven by the bigger environments.
- **Where the cases sit (405 scored):**
  - 17 all-pass environments: **172 PASS**
  - 7 all-fail environments: **68 FAIL**
  - 12 partial environments: **105 PASS / 60 FAIL**
  - 240/405 (59.3%) of scored cases are in all-or-nothing environments.
- **The partial group isn't one thing:**
  - Near the top: sheaf_schema_sync, sql_fixed_point and transformer_ssm_lift (8/9 each); compositional_optimizer and equivariant_diagram (7/9 each).
  - Near the bottom: batchnorm_ema 2/15.
  - Genuinely mid-range: gnn_message_passing, regex_state_machine and ssm_parallel_scan (5/9 each); tensor_functor 6/9; rd_adaptive_halting 8/14; moco 36/55.
  - So the [h-word] picture is a range of rates with heavy piles at 0% and 100%, not two clean groups.
- **Where failures concentrate:** glyph (24), moco (19) and batchnorm_ema (13) produce **56/128 (43.8%)** of all FAILs. Glyph alone is 18.75%.
- **Failure modes:**
  - underfit + overfit_visible_tests = 100/128 (78.1%), the substantive behavioural failures.
  - RUNTIME_ERROR 9 + runtime_error 2 + source_invalid 9 + invalid_action 5 + training_failed 3 = **28/128 (21.9%)**. These may be harness failures or ambiguous, rather than capability failures.
- **Confidence intervals (Wilson 95%):**
  - 4/4 → [0.51, 1.00] and 0/4 → [0.00, 0.49]
  - glyph 0/24 → [0.00, 0.14]
  - moco 36/55 → [0.52, 0.77]
  - gnn_message_passing 5/9 → [0.27, 0.81]

## 4. Cases and dimensions that [m-word]

**Contrasts within a family are the most useful evidence (my computation):**
- **ts:** parse_only 4/4 vs one_step 0/4 vs trajectory 0/4. Fisher exact test, parse vs one_step: p ≈ 0.029 (two-sided). This is the cleanest "task stage" contrast, but it rests on n = 4 per cell.
- **sheaf:** schema_sync 8/9 vs invariant_gluing 0/9 and physical_constraints 0/9 (p < 0.001 against each). Same family label, opposite outcomes.
- **rd:** gradient_credit 15/15 and state_carry 15/15 vs adaptive_halting 8/14, plus 1 unscored case.
- **epistemic:** 4 scored environments are 45/45 pass, but **epistemic_silence (6) and epistemic_type_games (4) are unscored**. You can't say the family is perfect.
- **Category-theory-named environments:**
  - All pass: categorical_lenses, stochastic_monad, tokenizer_adjunction, semiring_unification, architecture_naturality (9/9 each).
  - All fail: functorial_augmentation 0/9 and monadic_reward 0/9.
  - Partial: tensor_functor 6/9.
  - This links directly to the reference essay: the CT label doesn't predict the outcome. That point is stronger than "environment identity dominates."

**Cases ≠ tuples:** css_state_machine (18 cases / 9 tuples), epistemic_games (23/8), glyph (24/12) and moco (55/15) together hold 120/405 scored cases. This sits uneasily with "one seed per selected cell." The post needs to say what the extra dimension is (variant? turn? prompt?). Otherwise cases in those environments aren't independent, and every count based on them overstates the evidence.

**Difficulty axes:** I can't name them, because they're in the generated evidence I couldn't access. Tuple-level analysis is only informative for the 12 partial environments; moco (15 tuples) and batchnorm_ema (15) are the best candidates.

## 5. Strongest counterexamples and confounds

1. **Judge type.** 189 behavioral_reference vs 227 compile_only. If the all-pass environments are mostly compile_only, "perfect" just means "compiles." overfit_visible_tests (49) implies hidden tests, which suggests those failures come from behavioural judging. Failures may be concentrated where the judge is stronger. **This could invert the post's reading and must be checked first.**
2. **Harness failures in all-fail environments.** The 9 source_invalid and 9 RUNTIME_ERROR counts each equal a 9-case environment's size. That *could* mean whole environments failed for one harness reason. It's a hypothesis to check, not a finding. "RUNTIME_ERROR" and "runtime_error" appearing as separate labels suggests more than one harness code path.
3. **Source repo was dirty at run time.** Environment code may differ from any commit. This hits all-fail environments hardest.
4. **Small samples:** 4-case environments (ts_*, epistemic_fragmented_observation) can't support "perfect" or "impossible."
5. **Unscored cases (11).** If they're missing for reasons linked to failure, all rates are biased upward and the epistemic family looks better than it is.
6. **One seed per cell.** Run-to-run variance is unknown, so a 5/9 vs 7/9 gap may be noise.
7. **Draft vs. counterexample:** sheaf and ts show that environments sharing a family label can go opposite ways. That undercuts "environment identity" as a level of explanation: the useful unit is the task's demands, not the environment's name.

## 6. Visualisations

I couldn't see the 7 SVGs or the README. Match these needs to the existing figures and flag any figure that doesn't meet them:
1. **Per-environment dot plot** sorted by rate, with Wilson intervals and n marked. This is the main replacement for any "bimodal" histogram. Unscored environments should be shown separately, not as 0.
2. **Environment × judge type** (stacked bars or a matrix). Required for confound 1.
3. **Failure-mode composition per environment**, especially for the 7 all-fail environments and for glyph, moco and batchnorm_ema.
4. **Family small multiples** (ts, sheaf, rd, epistemic, CT-named). This is the strongest story.
5. **Tuple heatmaps for partial environments only.** Heatmaps of all-pass or all-fail environments carry no information.
6. **Avoid** an environment-rate histogram without n. It creates bimodality visually by pooling 4-case and 55-case environments.

## 7. Observation, interpretation, hypothesis

- **Observation:** the counts and rates above; χ² heterogeneity; 17/7/12 split; failure-mode totals; the ts and sheaf contrasts within families.
- **Interpretation (stated with hedging):** outcomes depend strongly on the environment; one aggregate rate is misleading; family labels (including CT names) don't predict outcomes.
- **Hypothesis (needs checks):** a static/structural vs execution/training split (ts, sheaf, ML-training environments); all-pass environments overlapping with compile_only; some all-fail environments being harness failures.

## 8. Claims that aren't [d-word] now

- "Bimodal capability": the partial environments hold 40.7% of scored cases, and the extremes are partly small-sample saturation.
- "Environment identity dominates difficulty labels": there's no shared difficulty scale, it's trivially true where outcomes are saturated, and it's untested where they aren't.
- "Mercury-2.5 cannot do glyph / sheaf gluing / ts stepping": this would need harness failures ruled out and the dirty-repo state recorded.
- "Mercury-2.5 has mastered the epistemic family": 10 cases are unscored, and the judge type is unknown.
- Any claim about capability in general: this is one model, one setting, one seed and one campaign.
- Any 0.684 figure without its denominator (405 scored vs 416 selected).
- Treating the 405 cases as independent in multi-case-per-tuple environments.

**Suggested retitle:** "Mercury-2.5 Across 38 Environments: One Pass Rate, Many Stories."

**Checks to run, in order:**
1. Judge type × environment cross-tab.
2. Failure mode × environment for the 7 all-fail environments.
3. What separates cases that share a tuple.
4. Per-tuple results for moco and batchnorm_ema.
5. Check the findings in F-001..F-009 against the points above.

--- END PASTED RESPONSE ---
