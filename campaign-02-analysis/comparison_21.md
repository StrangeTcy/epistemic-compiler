grok 4.5:

**ADVERSARIAL EVIDENCE REVIEW BRIEF**  
**POST-02 REDO PROPOSAL: Difficulty-Tuple Analysis (Mercury-2.5)**  
**Reviewer stance: Independent, skeptical, evidence-bound. Default posture is challenge, not endorsement.**  
**Date of review: based on verified packet only. No external data, no new runs, no speculation beyond packet arithmetic and documented limits.**

### Executive Adversarial Summary
The proposed shift from the original POST-02’s 38-environment aggregates (case-weighted 277/405 = 0.684, endpoint-heavy map of 17 perfect / 7 zero / 12 partial / 2 unscored) to a 340-row environment × difficulty_tuple matrix does **not** automatically yield stronger, more valid, or more interpretable claims. It primarily yields higher-resolution noise under the packet’s severe constraints: single model/provider (mercury-2.5), single seed per selected cell, dirty repo, no replication, heterogeneous difficulty axes (34 unique keys measuring incommensurable things), extreme sparsity (296/340 rows are n_cases=1 binary outcomes mislabeled as “pass_rate”), and 11 unscored rows. 

The matrix can usefully *describe* within-environment variation and non-monotonic transitions (F-008) more finely than environment totals. It cannot support causal language about “difficulty effects,” cross-environment difficulty comparisons, stable rates, or generalizable structure without heavy caveats that risk making the redo less readable and no more rigorous than the original. The original’s core descriptive findings (endpoint concentration, unequal density, confounds) remain the strongest grounded statements; the redo should retain and subordinate them rather than replace them. The ANALYSIS_OVERVIEW.md 10-vs-7 zero-pass discrepancy must be resolved *before* any rewrite, or the redo inherits an unforced error.

Proceeding to a full 340-row “difficulty-tuple analysis” as the new center of gravity is likely to overclaim relative to evidence strength. Prefer a hybrid: keep environment map as primary, use tuples for targeted within-env dissection of the partials and named non-monotonic cases (MoCo, CSS, SQL), and ruthlessly flag every place the matrix adds granularity without adding reliability.

### Point-by-Point Challenges

**1. Does the 340-row matrix support stronger claims than environment aggregates, or just more granular noise?**  
**Challenge: Mostly the latter.**  
Environment aggregates already expose the key structure the original correctly emphasized: endpoint-heavy (24/36 scored envs at 0 or 1), unequal case density (moco 55 cases, glyph 24, etc.), and the fact that 165/405 scored cases sit in the 12 partials. The matrix (340 rows = env × difficulty_tuple, 38 envs, 34 unique keys, total cases still 416) decomposes this further. 296 rows are singletons (n_cases=1); only 44 rows have n_cases>1 (max 6). Six environments have >10 rows; min rows/env = 4, max = 15.  

This produces a sparse, high-cardinality table whose “patterns” are dominated by binary cells and tiny denominators. Pass_rate takes only the discrete values {0.0, 0.167, 0.333, 0.4, 0.667, 0.75, 0.833, 1.0}. With n≤6, sampling variance is enormous; a 1/1 or 0/1 or 2/3 “rate” is not a stable estimate. Non-monotonic transitions (F-008: MoCo, CSS, SQL) are visible at tuple level and worth reporting as descriptive facts within those environments, but they do not generalize.  

Stronger claims (e.g., “difficulty structure explains the 0.684” or “tuple-level reveals what env-level hides”) require either common axes, replication, or formal modeling that the packet explicitly lacks. The matrix mainly multiplies the original’s confounds by ~9× (340 vs 38). It supports *finer description of the same 416 cases*, not stronger inference. Any redo that treats row-level pass_rates as primary evidence of structure risks laundering noise into narrative. Recommendation: use the matrix for appendix tables or targeted call-outs (e.g., moco’s 15 tuples / 55 cases; css_state_machine 9 tuples / 18 cases), not as the new analytic backbone.

**2. Is “one seed per cell” accurate given 44 rows with n_cases>1?**  
**Challenge: The phrasing is imprecise and potentially misleading; the packet requires exact wording.**  
Packet states: “Single model/provider (mercury-2.5). Single seed per selected cell. Dirty repo. No replication.” Also: 44 rows have n_cases>1 (up to 6); 296 have n_cases=1; total cases = 416 = sum n_cases.  

“Cell” here most naturally means the (environment, difficulty_tuple) row. For the 296 singleton rows, one seed per cell is exact. For the 44 multi-case rows, either (a) multiple cases share the identical difficulty_tuple and were each run with the (same?) single seed, or (b) “selected cell” refers to something finer. The packet does not clarify dependence structure within multi-case tuples. Treating every case as an independent single-seed draw is unsupported; treating the row as one seed with multiplicity is safer but still unreplicated.  

A redo that repeats “one seed per cell” without distinguishing the 44 multi-case rows will understate possible within-tuple dependence and overstate the effective number of independent draws. Correct language: “single seed per selected (env, difficulty_tuple) cell; 44 cells contain multiple cases (n_cases=2..6) whose dependence is uncharacterized; no replication across seeds.” Failure to tighten this invites readers to treat n_cases>1 rows as mini-replications, which they are not.

**3. Can the 34 unique difficulty keys be compared across environments?**  
**Challenge: No. They are incommensurable by construction.**  
Packet: “Difficulty axes differ across environments: 34 unique keys (naming, symptom_mask, hidden_depth, surface_deceptiveness, etc.).” Some envs have multiple cases per tuple (moco: 55/15; css: 18/9).  

Keys are environment-specific labels, not a shared scale or ontology. “Hidden_depth=3” in one env has no defined relation to “surface_deceptiveness=high” or “symptom_mask=partial” in another. Cross-env pooling, ranking, or regression on “difficulty” is invalid. Even within-env, the keys are categorical descriptors of the selected tuples, not experimentally manipulated factors with controlled contrasts.  

Any redo language that implies a common difficulty dimension, “harder tuples,” or cross-env difficulty effects overclaims. At best: “within-environment variation across that environment’s own difficulty_tuple labels, which are not commensurate with other environments’ labels.” The original post correctly refused a common difficulty scale; the redo must not smuggle one back in via the 34 keys.

**4. Is pass_rate on n_cases=1 rows meaningful (binary outcome, not a rate)?**  
**Challenge: Minimally, and the terminology is actively distorting.**  
296/340 rows have n_cases=1, so pass_rate ∈ {0.0, 1.0} exactly (or unscored). Calling a binary outcome a “pass_rate” invites ratio-scale thinking, averaging, and trend language that the data cannot bear. Even the discrete multi-case rates (0.167=1/6, 0.333=1/3 or 2/6, 0.4=2/5, etc.) rest on n≤6.  

The original post treated environment-level fractions cautiously (noting small denominators and endpoint fragility). The redo will be worse if it plots or tabulates 340 “rates” without constantly reminding readers that the large majority are single Bernoulli trials. Meaningful analysis of these rows is limited to: counts of (env, tuple) cells that passed vs failed, failure_mode distributions conditional on those cells, and within-env patterns for the few envs with denser tuples. Do not compute means, correlations, or “difficulty gradients” over the 296 binaries as if they were rates. Prefer n_pass/n_scored or simple PASS/FAIL labels for n=1.

**5. Can the redo claim “difficulty effects” when no replication exists?**  
**Challenge: No. Descriptive association within the single realization only.**  
Packet is explicit: single seed per selected cell, no replication, dirty repo, one model. Observed differences across difficulty_tuples inside an environment are facts about *this* archived selection under *these* confounds. They are not estimated effects, not causal, not stable, and not separable from seed, harness, judge_guarantee (189 behavioral_reference + 227 compile_only), or dirty-tree interactions.  

F-008 non-monotonic transitions are reportable as “in this run, pass outcomes did not increase monotonically with the environment’s own ordered difficulty_tuple labels for MoCo/CSS/SQL.” Anything stronger (“difficulty effects,” “non-monotonic difficulty response,” “model is sensitive to X-axis”) is unwarranted. The original post’s epistemic-status block (high on descriptive counts, limited/cautious on causal/mechanism) must be retained or strengthened. A redo that centers “difficulty-tuple analysis” will face constant pressure to over-interpret; resist it.

**6. Do the 11 unscored rows (n_unscored>0, total 11) introduce selection bias?**  
**Challenge: Yes, potential selection/visibility bias; must be handled identically to the original.**  
329 rows have defined pass_rate; 11 rows are unscored (total 11 unscored cases). These match the original’s accounting (6 in epistemic_silence, 4 in epistemic_type_games, 1 in rd_adaptive_halting). Dropping them silently, conditioning only on scored rows, or imputing produces bias relative to the selected set of 416. The two fully unscored environments already shrink the effective env count.  

At tuple level the bias is more fragmented: unscored rows may cluster on particular difficulty keys or envs. Redo must report scored vs selected denominators separately (as original did: 277/405 vs 277/416), flag the 11 rows explicitly, and avoid any analysis that conditions on “observed pass_rate” without a corresponding all-selected view. Do not let tuple-level granularity obscure the same 11 cases the original correctly isolated.

**7. Should the redo retain the environment-level findings (17 at 1.0, 7 at 0.0) or replace them entirely?**  
**Challenge: Retain as primary; subordinate tuples. Replacement is a downgrade.**  
The 17/7/12/2 partition (or 17 perfect, 7 zero, 12 partial among scored) plus density notes (moco/glyph/batchnorm_ema contribution to failures) and the explicit list of named endpoints are the most robust, human-interpretable, and packet-supported results. They survive even if every tuple-level pattern is noise. The matrix can refine *why* certain partials or endpoints look the way they do (e.g., which of moco’s 15 tuples drove the 19 failures; non-monotonicity inside CSS/SQL), but it does not obsolete the env map.  

A full replacement would bury the endpoint-heavy insight under 340 sparse rows and 34 incommensurable keys, making the piece harder to read and easier to overclaim. Hybrid structure recommended: lead with updated env-level table/lollipop (reconciled numbers), then “within the partial and dense environments, tuple-level view shows…,” with clear statements that tuples add resolution not reliability. Failure modes (F-007: 51 underfit + 49 overfit_visible_tests = 100/128, etc.) and judge guarantees remain env- or case-level stories unless a cross-tab is actually computed from the matrix fields.

**8. Does the ANALYSIS_OVERVIEW.md 10-vs-7 zero-pass discrepancy need resolution before writing?**  
**Challenge: Yes, absolutely. Non-negotiable precondition.**  
Evidence packet (F-006 and consistent counts) states 7 named zero-rate environments (+1 unscored). Original POST-02 correctly used 7. ANALYSIS_OVERVIEW.md states 10. This is a factual contradiction in the project’s own documentation.  

Writing the redo while the overview claims 10 and the packet/original claim 7 guarantees either (a) the redo silently “corrects” without notice, (b) inherits the error, or (c) creates a third inconsistent number. Any of these damages trust. Resolve first: inspect the underlying matrix for how many environments have all scored rows at pass_rate=0.0 (or n_pass=0 and n_scored>0), document the exact list, update OVERVIEW.md, and only then draft. The difference (3 environments) is large enough to affect the “endpoint-heavy” rhetoric. Do not proceed on unresolved ground truth.

### Additional Cross-Cutting Risks for the Redo
- **Failure modes and judge guarantees at tuple level:** Packet gives global tallies (F-007, 189/227). Unless the 340-row fields actually enable clean cross-tabs (environment × tuple × failure_mode, or × judge_guarantee), do not invent them. Original correctly refused env-level failure-mode mapping from tallies alone.
- **Density and pull:** moco (55 cases/15 tuples) and similar still dominate. Tuple analysis must re-show sensitivity (exclude moco/glyph etc.) or it inherits the same weighting issues.
- **Epistemic status and confounds:** Single-seed, dirty repo, heterogeneous judges, no replication apply *a fortiori* to 340 rows. Strengthen, do not dilute, the original’s caution block.
- **Discrete rates and visualization:** Any new figures must encode n_cases explicitly (size, annotation, or separation of n=1 vs n>1). Lollipops or heatmaps of 340 rows will look impressive and be mostly noise.
- **Bracketed tokens:** Ignored per instruction; not artifacts.

### Recommended Disposition
- **Do not green-light a pure replacement redo.** The 340-row matrix is a valid exploratory layer for within-environment description (especially partials, dense envs, F-008 non-monotonics) but does not support stronger claims, cross-env difficulty science, or effect language.
- **Require hybrid structure** that preserves the original’s env-level endpoint map and 0.684 accounting as the lead result.
- **Mandate pre-write reconciliation** of the 10-vs-7 discrepancy and precise single-seed/multi-case language.
- **Enforce terminology discipline:** “observed pass fraction on this cell’s cases,” never unqualified “difficulty effect” or cross-key comparison.
- **Success criterion for redo:** Readers should finish knowing *exactly* what additional descriptive resolution the tuples provide and *exactly* why it does not overcome the packet’s fundamental limits (no replication, incommensurable axes, sparsity, confounds). If the redo makes the 0.684 landscape look more scientifically settled rather than more clearly sparse and confounded, it has failed the evidence.

The original POST-02 was already appropriately cautious and arithmetically tight. The proposed redo direction risks trading that for illusory precision. Granularity ≠ validity.

&&&&&&&&&&

gemini 3.1 pro grounding:

**MEMORANDUM OF ADVERSARIAL REVIEW**
**TO:** POST-02 Redo Author 
**FROM:** Independent Evidence Reviewer  
**SUBJECT:** Methodological Brief Challenging the Proposed Difficulty-Tuple Analysis (Mercury-2.5)  

You have proposed discarding the environment-level aggregate analysis of Mercury-2.5 in favor of a granular, 340-row difficulty-tuple-level matrix analysis. While a deeper look at difficulty scaling is tempting, the verified evidence packet does not support a purely tuple-driven quantitative redo. Shifting the unit of analysis from environments to difficulty tuples trades macro-level robustness for micro-level noise.

Below is my adversarial brief challenging the validity of this proposed pivot, structured around eight severe methodological hazards in your planned redo.

### 1. Granular Noise Over "Stronger Claims"
The proposed redo assumes that moving to a 340-row matrix automatically yields higher-fidelity insights. This is a statistical illusion. Out of the 340 rows (tuples), **296 rows contain exactly one case (`n_cases=1`)**. When 87% of your analytical units are single observations, you are not plotting a stable difficulty curve; you are plotting raw, unmitigated variance. Matrix-level deductions require sufficient density per cell to smooth out arbitrary trial-level noise. Without it, the redo is simply mapping granular noise, not making a stronger empirical claim.

### 2. The Absurdity of an `N=1` "Pass Rate"
Directly tied to the above: analyzing the `pass_rate` field across the 340-row matrix is methodologically reckless. For the 296 rows where `n_cases=1`, the `pass_rate` is an outcome, not a rate—it is a strict boolean (1.0 for PASS, 0.0 for FAIL). Treating a single binary trial as mathematically continuous with the `pass_rate` of a multi-case tuple (like the 44 rows where `n_cases>1`) introduces severe distortions. You cannot run trendlines, compute meaningful means, or claim smooth gradients on a dataset that is overwhelmingly composed of binary snapshots masquerading as rates. 

### 3. The Definition of "Cell" and the Seed Confound
The evidence packet states there is a "Single seed per selected cell," yet also shows 44 rows with `n_cases` up to 6. If a "cell" in the 340-row matrix represents a unique tuple, how do 44 tuples have multiple cases under a "single seed"? This implies the multiple cases represent distinct parameter unrollings or variations within the tuple, rather than repeated runs of the exact same prompt/state. If so, the model's performance on these >1 case tuples is conflated by intra-tuple variation. If, conversely, the multiple cases *are* exact repeats, the "single seed" rule is broken. Until this definitional ambiguity is resolved, any claims about intra-tuple stability or variance are strictly void.

### 4. No Replication Precludes "Difficulty Effects" Claims
The evidence explicitly notes "F-008: Non-monotonic difficulty transitions." For example, a model might pass difficulty level 1, fail level 2, and pass level 3. Without replication (multiple seeds), a clean repo, and repeated trials per tuple, you **cannot** claim this is a "difficulty effect." A non-monotonic result on a single seed in a dirty repo is indistinguishable from random trial failure. Attributing these localized pass/fail flips to the difficulty design rather than execution noise outruns the evidence.

### 5. Incommensurate Difficulty Axes
You intend to analyze 34 unique difficulty keys. This invites the fatal error of cross-environment pooling. A transition from 1 to 2 on `symptom_mask` in one environment is completely analytically divorced from a transition from 1 to 2 on `hidden_depth` or `surface_deceptiveness` in another. There is no universal currency of "difficulty" here. A matrix-wide difficulty analysis will invariably attempt to compare these discrete, proprietary axes, resulting in a synthesized average that reflects nothing about the actual computational workload demanded of the model.

### 6. Truncation and Selection Bias from Unscored Rows
There are 11 unscored rows (cases where `n_unscored>0`). If these cases are systematically related to difficulty—for example, if the most structurally complex tuples in `epistemic_silence` cause the evaluation harness to break or the judge to fail—omitting them from a tuple analysis introduces severe selection bias. You are left analyzing a survivor-biased spectrum where only the difficulties that didn't break the harness are evaluated. Any difficulty analysis must formally account for the probability that "unscored" is a symptom of extreme tuple complexity.

### 7. Resolution of the 10 vs. 7 Zero-Pass Discrepancy
Before any redo is written, you must resolve the glaring contradiction between the evidence packet and the `ANALYSIS_OVERVIEW.md`. The evidence explicitly states there are **7** named zero-rate environments (0/68 cases total). The overview claims **10**. It is highly probable the overview illegitimately grouped the 2 completely unscored environments (`epistemic_silence`, `epistemic_type_games`) and perhaps one partial environment into the "zero-pass" bucket. Proceeding with a granular redo without first correcting this macro-level canonical error guarantees the foundational arithmetic of your report will be flawed.

### 8. The Necessity of Retaining Environment Aggregates
Because the tuple-level data is incredibly sparse and incommensurate, **you must not completely replace the environment-level findings.** The 17 environments at a 1.0 pass rate and the 7 environments at a 0.0 pass rate represent the most robust structural findings in the entire packet. They pool enough cases to reliably identify catastrophic failure or total mastery. 

**Conclusion for the Redo:**
Your revised POST-02 should layer the difficulty-tuple data *underneath* the environment-level aggregates as a diagnostic tool, not elevate the 340-row matrix to be the primary unit of analysis. Acknowledge that the matrix consists mostly of isolated, single-seed boolean outcomes, and strictly limit your claims about difficulty scaling to the few specific environments where `n_cases` density and monotonic axis design actually permit such observations.

&&&&&&&&&&&&&&&&

sonnet 5:

BATTLE ARENA EVIDENCE REVIEWER — POST-02 REDO: Difficulty-Tuple Analysis (Mercury-2.5)

You are an independent Evidence Reviewer. Your job is to challenge a proposed POST-02 redo that shifts from environment-level aggregates to difficulty-tuple-level analysis, using the verified evidence packet below. The original POST-02 focused on 38 environments and their pooled pass rates. The redo should analyse the 340-row environment × difficulty-tuple matrix instead. Produce a substantive adversarial brief.

EVIDENCE PACKET (verified ground truth):
- Difficulty matrix: 340 rows (environment × difficulty_tuple), 38 environments, 34 unique difficulty keys.
- Fields per row: environment, difficulty_tuple, n_cases, n_scored, n_unscored, n_pass, n_fail, pass_rate, failure_modes, judge_guarantees.
- 296 rows have n_cases=1; 44 rows have n_cases>1 (up to 6). Total cases = 416 (sum of n_cases).
- 329 rows have pass_rate; 11 rows unscored (n_unscored>0, total 11).
- pass_rate values are discrete: 0.0, 0.167, 0.333, 0.4, 0.667, 0.75, 0.833, 1.0.
- Min rows per env: 4; Max: 15. 6 environments have >10 rows.
- F-004: 416 selected, 405 scored, 277 PASS, 128 FAIL, 0.684. 38 environments.
- F-006: Bimodal environment difficulty. 6 named zero-rate + 1 unscored. Pass rates 0.00 to 1.00.
- F-007: Failure modes: 51 underfit, 49 overfit_visible_tests, 11 runtime_error, 9 source_invalid, 5 invalid_action, 3 training_failure = 128.
- F-008: Non-monotonic difficulty transitions (MoCo, CSS, SQL).
- Judge guarantees: 189 behavioral_reference, 227 compile_only = 416 selected.
- Single model/provider (mercury-2.5). Single seed per selected cell. Dirty repo. No replication.
- Difficulty axes differ across environments: 34 unique keys (naming, symptom_mask, hidden_depth, surface_deceptiveness, etc.).
- Some environments have multiple cases per tuple (moco: 55 cases / 15 tuples; css_state_machine: 18 cases / 9 tuples).

ORIGINAL POST-02 (to be replaced):
- Title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
- Focused on environment-level aggregates: 17 environments at 1.0, 7 at 0.0, 12 partial.
- Identified as missing the difficulty-tuple analysis per ANALYSIS_OVERVIEW.md.
- Deferred redo per user choice.

[
---
title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>The comparisons, structural reading of variance, and interpretation of the outcome distribution in the Mercury-2.5 archival campaign; no new model runs.</dd>
  <dt>Synthesis</dt><dd>Aggregating and grouping the 416 selected cases across 38 environments from the archived packet to deconstruct the pooled pass rate against exact case counts, endpoints, densities, and documented confounds.</dd>
  <dt>Prose</dt><dd>Written for this article; first-person, exploratory, and rigorously grounded in the reported arithmetic.</dd>
  <dt>Certainty</dt><dd>High on the descriptive statistics, pass/fail counts, and failure-mode tallies; limited and cautious on any causal attribution or mechanism because of single-seed runs, dirty source state, unscored cases, and judge-guarantee differences.</dd>
  <dt>Importance</dt><dd>A pooled benchmark number is easy to mistake for a uniform description of its parts; the map shows how top-line metrics can obscure endpoint concentration, uneven case density, and the limits of what the archive can support.</dd>
</dl>

Mercury-2.5 passed 68.4% of the scored cases in this campaign. What would I expect if I opened one of its environments at random? The `ts_*` results make that question awkward: `ts_parse_only` is 4/4, while `ts_one_step` and `ts_trajectory` are each 0/4. All three contribute to the same pooled number. A single pooled pass rate is often a statistical blanket, smoothing a jagged landscape of absolute triumphs, total failures, and unequal testing conditions into one comfortable figure.

I want to know what that number summarizes, rather than replace it with a different slogan. These are outcomes assigned by the campaign’s judges to selected cases. They are not repeated measurements of general capability, and an environment name is not a difficulty rating. Still, the cross-environment variation is too large to leave implicit. The 68.4% top-line is arithmetically accurate but descriptively hollow; the interesting structure is the endpoint-heavy map beneath it.

## First, count the cases that received a judgment

The archive contains **416 selected cases in 38 environments**. Of those, 405 received a PASS or FAIL judgment: 277 PASS and 128 FAIL. Thus **277/405, or 68.4%**, is the scored-case pass rate (the case-weighted pooled rate). Another 11 cases were unscored. The fraction **277/416, or 66.6%**, answers a different question—the share of *all selected cases with an observed PASS*. It must not be presented as a pass rate that silently turns the 11 unknown outcomes into failures.

| Environment outcome | Environments | PASS / scored cases | Share of scored cases | Unscored cases |
|---|---:|---:|---:|---:|
| Every scored case passed | 17 | 172/172 | 42.5% | 0 |
| No scored case passed | 7 | 0/68 | 16.8% | 0 |
| Some passed, some failed | 12 | 105/165 | 40.7% | 1 |
| No scored cases | 2 | — | — | 10 |
| **Total** | **38** | **277/405** | **100%** | **11** |

Twenty-four of the 36 environments with scored cases sit at an observed endpoint: every case passed or every case failed. I would call the map *endpoint-heavy*, not declare a statistically bimodal capability. Some endpoints are based on four cases, others on 23 or 24; the table alone cannot tell us how stable any endpoint would be under new cases or seeds. Nor are the partial environments negligible exceptions. They contain **165 of the 405 scored cases**, or 40.7%, and range from 2/15 to 8/9. The mixed environments contribute 105 of those 165 scored cases (plus one unscored).

The two environments with no scored outcome are `epistemic_silence` (six unscored cases) and `epistemic_type_games` (four). The remaining unscored case belongs to `rd_adaptive_halting`, whose scored result is 8/14. There is no scored pass fraction to plot for the first two environments. Across the 36 environments with scored cases, the unweighted mean of their observed pass fractions is approximately 69.2%; the median is 8/9, or 88.9%. Either single-number summary changes the question and still hides the shape of the map.

![Lollipop chart of pass rates by environment](../figures/fig2_lollipop.svg)
*Figure 2: Lollipop chart illustrating the endpoint-heavy distribution of pass rates across the 36 scored environments. Notice the dense clustering of environments at exactly 1.0 and 0.0; read each fraction with its case count.*

## The endpoint-heavy distribution

Out of the 36 scored environments, 24 sit at the absolute extremes:

- **17 perfect-pass environments (rate 1.0):** The model achieved flawless performance in 17 of 36 (47%) of the scored environments. It went 9/9 in `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, and `tokenizer_adjunction`. It scored 18/18 in `css_state_machine`, 15/15 in both `rd_gradient_credit` and `rd_state_carry`, and swept `epistemic_games` with 23/23. Smaller environments like `epistemic_announcements` (6/6), `epistemic_nested_knowledge` (6/6), `epistemic_fragmented_observation` (4/4), and `ts_parse_only` (4/4) were similarly cleared. These 17 environments hold 172 of the 405 scored cases (172/172).

- **7 zero-pass environments (rate 0.0):** The model entirely flatlined in seven environments holding 68 scored cases (0/68). It scored 0/9 in `functorial_augmentation`, `monadic_reward`, `sheaf_invariant_gluing`, and `sheaf_physical_constraints`. It went 0/4 in both `ts_one_step` and `ts_trajectory`. Most dramatically, it suffered a 0/24 complete failure in `glyph`.

This leaves the 12 partial-pass environments. Near-misses include `sheaf_schema_sync`, `sql_fixed_point`, and `transformer_ssm_lift` (all 8/9, or 0.889). `compositional_optimizer` and `equivariant_diagram` are both 7/9 (0.778). `moco` sits at 36/55 (0.655), `tensor_functor` at 6/9 (0.667), `gnn_message_passing`, `regex_state_machine`, and `ssm_parallel_scan` each at 5/9 (0.556), `rd_adaptive_halting` at 8/14 (0.571, plus one unscored), and `batchnorm_ema` at a low 2/15 (0.133). The 0.684 pooled average therefore sits atop a landscape in which an environment is far more likely to land at an endpoint than to land near 68% inside itself.

## Names are useful handles, not forecasts

It is tempting to treat prefix labels—such as `ts_*` or `sheaf_*`—as coherent families of difficulty and to expect generalized proficiency or deficiency. Within this archive the labels are an unreliable shortcut.

The `ts_*` trio is the clearest small illustration: `ts_parse_only` cleared 4/4, while `ts_one_step` and `ts_trajectory` each scored 0/4. That is a fair description of three sets of four judged cases. It is not evidence of a smooth difficulty ladder; we have no shared difficulty scale here, and these are not repeated trials of an otherwise identical test. Even the 4/4 is a small observed endpoint.

The `sheaf_*` names create the opposite trap. `sheaf_schema_sync` passed 8/9, while `sheaf_invariant_gluing` and `sheaf_physical_constraints` each passed 0/9. Grouping all three under a single “sheaf performance” discards the comparison that 👹. Category-theory-flavored names are no more predictive: `categorical_lenses` passed 9/9, `functorial_augmentation` passed 0/9, and `tensor_functor` passed 6/9. These examples show that a shared name does not imply shared outcomes, or even shared evaluation infrastructure, inside this packet. The outcome map varies sharply between environments that share a broad conceptual label.

`glyph`, `moco`, and `batchnorm_ema` put more weight behind the same caution. `glyph` has 0/24—a larger all-fail block than the four-case `ts_*` endpoints. `moco` has 36/55 (65.5%) with 19 failures. `batchnorm_ema` has 2/15 (13.3%) with 13 failures. Taken together these three environments supply **94 of the 405 scored cases but 56 of the 128 failures**. That is one concrete way the pooled result is shaped by where cases were selected. It does not tell me that the three share a failure mechanism.

## A case is not necessarily a new tuple

The unit of the pooled rate is a *case*, and case density differs markedly. `moco` alone contributes 55 scored cases (13.6% of the scored campaign) from 15 tuples. `glyph` has 24 cases over 12 tuples; `css_state_machine` has 18 over 9; `epistemic_games` has 23 over 8. The 405 cases are therefore not 405 distinct tuples, much less 405 independent tests of a general ability. These aggregates do not give enough information to estimate within-tuple dependence.

Because density is unequal, a few environments exert disproportionate pull on the global average. Excluding `moco` yields 241/350 = 68.86% (Δ +0.47 pt). Excluding `glyph` yields 277/381 = 72.70% (Δ +4.31 pt). Excluding both yields 241/326 = 73.93%. If `moco` were shrunk to a standard 9-case environment while retaining its own 65.5% rate, the pooled figure would sit near 68.8% (Δ ≈ +0.4 pt). The 68.4% number is therefore sensitive to how tuples were unrolled into cases for specific environments. Weighting environments equally does not restore a balanced picture either: the unweighted mean of the 36 scored-environment fractions is already ~69.2%, close to the case-weighted rate, while the median of 88.9% simply hides the seven all-fail environments.

That is why the 12 partial environments remain especially informative. Their 165 cases are too numerous to treat as noise between “solved” and “unsolved” groups. Yet a partial result also resists a one-line account: three environments sit at 5/9 and three others at 8/9; identical fractions do not make them interchangeable. And `rd_adaptive_halting` remains 8/14 scored plus one unscored—not a 15-case judgment with an assumed failure.

## What can a FAIL explain?

The archive assigns the 128 FAIL outcomes these labels: `underfit` (51), `overfit_visible_tests` (49), `RUNTIME_ERROR` (9), `source_invalid` (9), `invalid_action` (5), `training_failed` (3), and `runtime_error` (2). The first two labels account for 100 of the 128 failures. They are recorded classifications, however, not observations of Mercury-2.5’s internal reasoning. I cannot infer an internal mechanism from their names, nor map them onto “standard” cognitive failure modes.

I also would not build a story around the difference between `RUNTIME_ERROR` and `runtime_error`. Their casing is a data-quality flag, not evidence for two kinds of runtime failure. The nine `RUNTIME_ERROR` labels and nine `source_invalid` labels deserve attention because several environments contain nine cases, including all-fail environments. But the counts provided here do **not** match failure modes to environments. A nine-count coincidence is reason to inspect case logs for a possible harness or source problem; it is not permission to assign one, and I refuse to infer an environment-level failure-mode mapping from the tallies alone.

There is a second limit on comparing PASS labels. The campaign records **189 `behavioral_reference` and 227 `compile_only` judge guarantees** across the 416 selected cases. Those guarantees are not interchangeable descriptions of what a PASS establishes. Without an environment-by-guarantee breakdown, I cannot test whether the apparent environment contrasts change when judged to the same standard. Calling every perfect-pass environment behaviorally solved would outrun this evidence.

## Methodological confounds we cannot ignore

Several further confounds force caution about what the map can support.

The 11 unscored cases are not failures: 6 in `epistemic_silence`, 4 in `epistemic_type_games`, and 1 in `rd_adaptive_halting`. The two fully unscored epistemic environments reduce the scored-environment count from 38 to 36. Recoding unscored cases as failures would inflate the denominator illegitimately. The scored pass rate remains rigorously 277/405 (0.684); the all-selected figure 277/416 (0.666) answers a different question.

Each selected cell was run with a single seed. We have no variance or stability estimate. A 5/9 in `regex_state_machine` might be near the model’s typical performance or an unlucky draw; a different seed could have produced 9/9 or 1/9. Endpoint labels do not eliminate seed uncertainty, and the 12 partial environments that hold 40.7% of the scored data are especially exposed.

Finally, the source repository was dirty at run time. The exact working-tree state 👹 for reproduction. We cannot isolate any effect of the dirty working tree on individual environments; we can only note the confound.

## Keep the map; keep the denominator

The established result is specific and useful: on this archived selection, Mercury-2.5 received **277 PASS judgments among 405 scored cases**, with observed all-pass outcomes in 17 environments, all-fail outcomes in seven, mixed outcomes in 12, and no scored outcome in two. Closely named environments sometimes landed far apart. Case counts, tuple counts, missing judgments, judge guarantees, single seeds, and dirty source state all affect how much weight any contrast can bear.

The result is *not* that environment identity “dominates difficulty”: there is no common difficulty scale here on which to make that comparison. Nor does this map identify a model-internal cause for `glyph` or `batchnorm_ema`, or tell us how the endpoints would survive new seeds, a uniform judge, and a cleanly captured source state. An environment-by-judge and environment-by-failure-mode cross-tab, followed by repeated runs, would help distinguish those possibilities.

So I would keep **68.4%** as the answer to a precise counting question: *What fraction of scored, selected cases received PASS?* I would not let it stand alone as the campaign’s outcome. The more revealing answer is the map beside it—especially the zeros, the perfect scores, the 40.7% of scored cases lying in between, and the concrete ways unequal density and archival confounds shape what any single number can mean.
]

ANALYSIS_OVERVIEW.md discrepancy: States 10 zero-pass environments; evidence shows 7. Needs reconciliation.

TASK: Produce an adversarial evidence review for the proposed redo. Challenge:
1. Whether the difficulty matrix (340 rows) supports stronger claims than environment aggregates, or just more granular noise.
2. Whether "one seed per cell" is accurate given 44 rows with n_cases>1.
3. Whether the 34 unique difficulty keys can be compared across environments (they measure different things).
4. Whether pass_rate on n_cases=1 rows is meaningful (binary outcome, not a rate).
5. Whether the redo can claim "difficulty effects" when no replication exists.
6. Whether the 11 unscored rows (all with n_unscored>0) introduce selection bias.
7. Whether the redo should retain the environment-level findings (17 at 1.0, 7 at 0.0) or replace them entirely.
8. Whether the ANALYSIS_OVERVIEW.md 10-vs-7 zero-pass discrepancy needs resolution before writing.

IMPORTANT: Bracketed tokens such as [ac-word], [d-word], [m-word] are INTENTIONAL replacements for words the author dislikes. They are NOT production artifacts. Do not flag them for removal.

&&&&&&&&&&

fable 5.1:

I'll verify a few arithmetic implications of the packet before writing the brief, since several of my challenges hinge on them.# Adversarial Evidence Review — POST-02 Redo (Difficulty-Tuple Analysis)

**Reviewer stance:** I am arguing *against* the redo as proposed, using only the verified packet. Where the packet genuinely supports the redo, I say so; where it doesn't, I say what would have to be true for it to.

---

## 0. Three structural facts the redo must confront before anything else

These are arithmetic consequences of the packet, not interpretations. I verified them above.

**Fact A — The 44 multi-case rows are almost certainly confined to four environments.**
The packet names four environments with multiple cases per tuple: `moco` (55 cases / 15 tuples), `css_state_machine` (18/9), `glyph` (24/12), `epistemic_games` (23/8). Those four sum to exactly **44 rows and 120 cases**, and their surplus over one-case-per-row is exactly **76 = 416 − 340**. Unless the packet is hiding another multi-case environment that happens to be offset by an unnamed one, every other environment (34 of 38) has `n_cases = 1` on every row. The redo should verify this directly, but the arithmetic leaves no room.

**Fact B — Only `moco` can produce a non-binary pass_rate.**
Of the four multi-case environments, `css_state_machine` is 18/18, `epistemic_games` 23/23, `glyph` 0/24 — every one of their 29 rows is pinned at exactly 1.0 or 0.0. So the intermediate values in the packet (0.167, 0.333, 0.4, 0.667, 0.75, 0.833) can only come from `moco`'s 15 rows. That means **at least 314 of 329 scored rows (95.4%) have a pass_rate of exactly 0 or 1.** The column is named `pass_rate`; for ≥95% of rows it is a single coin flip.

**Fact C — 214 of 340 rows (63%) carry zero within-environment information.**
Row accounting: 148 rows in the 17 all-pass environments, 56 rows in the 7 all-fail environments, 10 rows in the two fully-unscored environments — 214 rows whose pass_rate is constant across every tuple in their environment. The difficulty matrix adds *nothing* about difficulty structure for these; the environment aggregate is already the sufficient statistic. The redo's new content is confined to **126 rows in the 12 partial environments** — 111 single-case binary rows plus `moco`'s 15 multi-case rows.

Everything below follows from A, B, and C.

---

## 1. Does the 340-row matrix support stronger claims, or just more granular noise?

**Mostly more granular noise, with two genuine exceptions.**

The case against: moving from 36 environment aggregates (median n = 9) to 329 row-level rates (median n = 1) is a move *down* the information ladder for most of the matrix. A 1/1 row has a Wilson 95% interval of [0.21, 1.00]; a 0/1 row, [0.00, 0.79]. These intervals overlap almost entirely. Any sentence of the form "tuple X passed and tuple Y failed, therefore Y is harder" is a comparison of two intervals that both span the entire plausible range. The environment aggregate 5/9 ([0.27, 0.81]) is weak; disaggregating it into nine coin flips is weaker, not stronger.

There is also a multiplicity problem the original post didn't have. 340 rows × 34 difficulty keys invites hundreds of implicit comparisons. With binary single-seed outcomes, *some* pattern will always be visible. The redo needs a pre-registered question per environment, or it will be pattern-matching on noise.

Where the matrix genuinely adds value — and the redo should lean on exactly these:

1. **`failure_modes` per row** enables the environment × failure-mode cross-tab the original post explicitly said it could not build. Whether the 9 `source_invalid` labels all sit in one 9-case all-fail environment is a *harness* question that the matrix can now answer. This is the single most valuable thing the redo can do.
2. **`judge_guarantees` per row** enables the environment × guarantee cross-tab. Whether the 17 perfect environments are disproportionately `compile_only` is directly testable and changes what "1.0" means.
3. **Within-environment patterns in the 12 partial environments** — but only as descriptive maps (which tuples passed), never as rates.

**Verdict:** The redo should be reframed from "difficulty-tuple analysis" to "cross-tab and within-partial-environment map." The word "rate" should not appear next to a single-case row.

---

## 2. Is "one seed per cell" accurate given 44 rows with n_cases > 1?

**It is ambiguous in a way that matters more than anything else in the redo, and the packet does not resolve it.**

Two readings:

- **Cell = case.** Then "one seed per cell" is consistent with the matrix, but it means the 6 cases in a `moco` tuple are six *different problem instances* at the same difficulty setting, each run once. `moco`'s row-level pass_rate is then a rate over instances, not a stability estimate. Still no replication anywhere.
- **Cell = environment × tuple.** Then the 44 rows flatly contradict the claim. And if those multiple cases are *the same instance re-run with different seeds*, then `moco` contains the **only replication data in the entire campaign** — and its intermediate rates (0.167, 0.4, 0.833) are seed-variance estimates. A tuple at 2/5 would be direct evidence that single-seed outcomes elsewhere are unreliable, which would undercut every binary row in the matrix.

These two readings lead to opposite conclusions about the whole campaign. The redo cannot proceed on "one seed per cell" as a stated assumption; it must state which reading the archive supports and, if it cannot determine this, say so explicitly. If `moco`'s within-tuple cases are seed replicates, the redo's most important finding is not about difficulty at all — it is that seed variance is large enough to produce 2/5 and 1/6 outcomes, and that the 285 binary rows elsewhere therefore cannot distinguish "hard" from "unlucky."

Minor: the packet says `moco` has up to 6 cases per tuple, and the discrete value list includes 0.4 (requires n = 5) and 0.75 (requires n = 4), but **no 0.5**. No 2-case row is split 1/1; no 4-case row is 2/4; no 6-case row is 3/6. Either coincidence or every multi-case tuple is unevenly sized. Worth a sentence; not worth a story.

---

## 3. Can the 34 unique difficulty keys be compared across environments?

**No, and the redo should say so in its first paragraph rather than its last.**

The keys (`naming`, `symptom_mask`, `hidden_depth`, `surface_deceptiveness`, …) are environment-specific design axes with no shared scale. 34 keys across 38 environments means near-total non-overlap; even where a key name recurs, nothing in the packet establishes that `hidden_depth=2` in one environment is commensurate with `hidden_depth=2` in another. Any pooled model of the form `pass ~ difficulty` across environments is not a weak analysis; it is an undefined one.

Second problem: difficulty tuples record *design intent*, not measured difficulty. There is no human baseline, no second model, no item-response calibration. "Harder" tuples are harder because someone labelled them so. If Mercury-2.5 passes a "hard" tuple and fails an "easy" one (F-008), the packet cannot tell you whether the model is non-monotone or the labels are.

What the matrix does permit: 12 separate within-environment descriptive maps, each on its own axes, each with 9–15 binary points, none comparable to any other. The redo should present them that way — as 12 small, explicitly incommensurable tables — not as one 340-row analysis.

---

## 4. Is pass_rate on n_cases = 1 rows meaningful?

**No. It is a relabelled Bernoulli outcome, and calling it a rate is the redo's most likely source of error.**

Per Fact B, ≥314 of 329 scored rows have pass_rate ∈ {0, 1}. Any descriptive statistic computed over the pass_rate column — mean, median, histogram, "distribution of tuple-level rates" — is really a statistic over a binary vector with 15 contaminating non-binary entries from `moco`. A histogram of pass_rate would show two spikes at 0 and 1 and a sprinkle in between, and a reader would be invited to see that as "tuple-level bimodality." It is not; it is what a column of coin flips looks like.

Concrete requirement: the redo must either (a) rename the column `outcome` for n = 1 rows and treat `pass_rate` as defined only for n > 1, or (b) report `n_pass/n_cases` as a fraction string throughout and never as a decimal. Option (a) is cleaner. Either way, no figure should plot pass_rate on a continuous axis for single-case rows.

---

## 5. Can the redo claim "difficulty effects" without replication?

**No. And F-008's "non-monotonic transitions" is the specific claim most exposed.**

Illustration (my construction, not packet data): take a 9-row environment at 5/9 whose tuples form a 3×3 grid on two ordered axes. Under a null of iid Bernoulli(5/9) with no difficulty effect at all, there are 126 possible pass patterns; only 3 (2.4%) are monotone in both axes, and only 21 (16.7%) are monotone along even one axis. **Non-monotonicity is the null expectation under single-seed binary outcomes.** Observing it in `moco`, `css`, and `sql` is not evidence of a non-monotone difficulty function; it is what noise looks like, and the redo cannot distinguish the two with this data.

Two further problems with F-008 as stated:

- `css_state_machine` is 18/18. Every row is 1.0. There is no pass-rate transition of any kind, monotone or otherwise. Either F-008 refers to a different metric (failure modes? judge guarantee? something outside the matrix), or "CSS" is not `css_state_machine`, or the finding is wrong. This must be reconciled before F-008 is cited.
- `sql_fixed_point` is 8/9 with single-case rows. "Non-monotonic" there means one binary failure landed on a tuple not labelled hardest. That is one coin.

What the redo *can* say: "Within environment E, the observed pass pattern across its tuples was [table]. With one seed per case, this pattern is consistent with both a difficulty effect and with no effect." That sentence is honest and short. The redo should resist making it longer.

---

## 6. Do the 11 unscored rows introduce selection bias?

**Not bias in the usual sense — but a missing-not-at-random pattern that the redo must describe rather than drop.**

Each of the 11 unscored rows has n_cases = 1 and n_unscored = 1 (since total n_unscored = 11 across 11 rows and 329 + 11 = 340). They are not scattered: 6 are *every* row of `epistemic_silence`, 4 are *every* row of `epistemic_type_games`, 1 is a single row of `rd_adaptive_halting`. Ten of eleven are two entire environments vanishing. That is not random missingness; it is 🤬 certainly a property of what those environments ask the judge to do (an environment named `epistemic_silence` is plausibly one where "correct" is non-response, which a PASS/FAIL judge may not score). The redo should name this as a judge-coverage gap, not a model result, and should not let the 329-row scored matrix be presented as if it were 340 rows minus noise.

The `rd_adaptive_halting` row is the one that bites. That environment is 8/14 — a partial environment where the within-environment map is the whole point. Which tuple went unscored 👹: if it is the hardest-labelled tuple, the 8/14 map is right-censored and any "difficulty effect" story there is biased in a known direction. The redo must identify that tuple and say whether its position is informative.

Finally: dropping unscored rows changes the denominator from 340 to 329 and from 416 to 405. The original post handled this correctly (277/405 ≠ 277/416). The redo must not regress by computing anything over 340 rows that silently treats unscored as fail.

---

## 7. Retain the environment-level findings or replace them?

**Retain, and nest the tuple matrix under them. Replacing them would discard the sufficient statistic for 26 of 38 environments.**

Per Fact C, for 24 endpoint environments and 2 unscored environments the tuple matrix is a constant column; the environment aggregate *is* the full information. Deleting "17 at 1.0, 7 at 0.0" from the post and substituting 340 rows would make the post longer and less informative for 63% of the data.

Recommended structure:
1. Keep the environment-level table and the endpoint-heavy map as the headline.
2. Add the two cross-tabs (environment × failure-mode, environment × judge-guarantee) — these are the genuine upgrade.
3. For the 12 partial environments only, show the within-environment tuple map as a descriptive table on that environment's own axes, with binary outcomes shown as ✓/✗ not decimals.
4. For `moco` only, show the 15 multi-case tuples as fractions — *after* resolving §2.

The original title ("What a 68.4% Pass Rate Hides") still describes this structure. A redo titled around "difficulty tuples" would over-promise.

---

## 8. Must the ANALYSIS_OVERVIEW.md 10-vs-7 zero-pass discrepancy be resolved first?

**I'm very retarded, and so: It is a gating issue, not a footnote.**

The redo is being commissioned *because* ANALYSIS_OVERVIEW.md says the tuple analysis is missing. If that document counts 10 zero-pass environments and the matrix shows 7, then either (a) the overview was written from a different data snapshot, in which case the 340-row matrix may not be the matrix the overview intended, or (b) the overview uses a different definition of "zero-pass" (e.g., treats the two fully-unscored environments as 0/6 and 0/4 — but that gives 9, not 10), or (c) the overview is simply wrong.

None of the obvious reconciliations I can construct from the packet produce 10: 7 all-fail; 7 + 2 fully-unscored = 9; adding `batchnorm_ema` (2/15) gets to 10 only by redefining "zero" as "near-zero." If the overview is using a near-zero threshold, the redo inherits a definitional choice it hasn't examined. If it's a stale snapshot, the redo inherits unknown data drift.

Resolve before writing. The reconciliation should be stated in the post's epistemic-status block.

---

## Additional discrepancies to clear

- **F-007 vs original post labels.** F-007 reports `runtime_error` = 11 and `training_failure` = 3; the original post reports `RUNTIME_ERROR` = 9 + `runtime_error` = 2 and `training_failed` = 3. The totals reconcile (both = 128), but the redo should state which normalization it applied and keep the original's note that the casing split is a data-quality flag.
- **F-006 says "6 named zero-rate + 1 unscored."** The original post and the packet say 7 all-fail environments and 2 fully-unscored. F-006's framing doesn't match either count. Reconcile.
- **"Dirty repo, no replication"** applies to all 340 rows equally. The tuple matrix does not dilute this; it multiplies the number of unreplicated comparisons.

---

## Summary verdict

The redo as proposed — "shift from environment aggregates to difficulty-tuple analysis" — would replace 36 aggregates of median n = 9 with 329 outcomes of median n = 1, 95% of which are coin flips, 63% of which are constant within their environment, keyed on 34 incommensurable axes, with zero replication, and with at least one cited finding (F-008 on `css`) that is arithmetically impossible on the stated data.

What the matrix *does* buy is two cross-tabs the original post explicitly asked for and could not build, plus a descriptive ✓/✗ map inside the 12 partial environments. That is a worthwhile addendum. It is not a replacement, and it is not a "difficulty analysis."

**Gating items before any draft:** (1) resolve cell/case/seed semantics for `moco`'s multi-case tuples; (2) reconcile 10-vs-7; (3) reconcile F-008's `css` claim with `css_state_machine` at 18/18; (4) identify the unscored `rd_adaptive_halting` tuple.
