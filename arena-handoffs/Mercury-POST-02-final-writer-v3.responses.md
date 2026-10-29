claude fable 5.1:
---
title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>A retrospective reading of one archived Mercury-2.5 campaign: what a pooled pass rate compresses once its cases are regrouped by environment and by difficulty tuple. No new runs.</dd>
  <dt>Synthesis</dt><dd>Recorded verdicts for 416 cases in 38 environments, an 80-case omission record, and a 340-row environment × difficulty-tuple matrix, read against the conflicts the records themselves carry.</dd>
  <dt>Prose</dt><dd>Drafted and revised with AI assistance from the archived records. No independent human verification or replication of the campaign is claimed.</dd>
  <dt>Certainty</dt><dd>High for the counts, which are arithmetic on recorded rows. Low for anything causal: one seed, a source tree recorded as dirty, eleven unscored cases, judge guarantees fixed by environment, and places where the records disagree with each other.</dd>
  <dt>Importance</dt><dd>A pooled benchmark number is easy to read as a description of its parts. This one is not, and the records show both how uneven the parts are and how little they can settle.</dd>
</dl>

*Revision note: this version replaces the one first published under this title. The headline, 277 of 405 scored cases, is unchanged. The tuple matrix is now read as description rather than result, one earlier claim is withdrawn, and the open questions get their own section instead of being smoothed over.*

Mercury-2.5 received a PASS verdict on 68.4% of the scored cases in this campaign. Suppose I pick one of its environments without looking. What pass rate should I expect?

Not 68.4%. Of the 36 environments with at least one scored case, only two land within five points of the pooled figure: `moco` at 36/55 (65.5%) and `tensor_functor` at 6/9 (66.7%). Twenty-four sit at an exact endpoint: every scored case passed, or none did. The pooled number is a precise answer to one question, and it is a value the environments almost never take.

Three limits govern everything below, so I state them once. These are verdicts the campaign's judges assigned to selected cases, not repeated measurements of a general ability, and an environment name is not a difficulty rating. Every selected record carries seed 0, and no second seed is recorded. And each environment was judged under exactly one of two guarantees, `behavioral_reference` or `compile_only`, which do not establish the same thing when they say PASS.

**The thesis is narrow: 277/405 = 68.4% is the exact answer to one counting question, and the records beneath it support a map of where judged outcomes fell, not a difficulty ranking, a mechanism, or a stability estimate.**

## Counting the judged cases, and the frame around them

The campaign selected **416 cases in 38 environments**. Of these, 405 received a verdict: 277 PASS and 128 FAIL. The other 11 carry the recorded status `infrastructure_unscored`; the records state no cause, and I do not supply one.

So 277/405 = 68.4% is the share of *scored* cases with a PASS. The fraction 277/416 = 66.6% answers a different question, the share of all *selected* cases with an observed PASS, and must not be presented as a pass rate, because that would quietly book eleven unknown outcomes as failures.

![Three stacked bars: 496 recorded case IDs split into 416 selected and 80 omitted; 416 split into 405 scored and 11 unscored; 405 split into 277 PASS and 128 FAIL](../figures/fig8_selection_frame.svg)
*Figure 8. The top bar, which the chart labels "design cells", holds 496 recorded case IDs: 80 omitted before scoring (56 intervention-twin, 14 known-gate, 10 unsupported input modality, the last all in `rope`) and 416 selected. The 416 split into 405 scored and 11 `infrastructure_unscored`; the 11-case segment carries no number in the image, so this caption supplies it. The 405 split into 277 PASS and 128 FAIL. Omitted cases, in grey, enter no pass rate. Nine scored FAILs whose disposition field conflicts with their status are not drawn separately. "Design cells" is the chart's label, not a definition of a sampling unit.*

The 416 are themselves a selection. The 80 omitted cases fall in four environments:

| Environment | Intervention-twin | Known-gate | Input modality | Total |
|---|---:|---:|---:|---:|
| `moco` | 35 | — | — | 35 |
| `glyph` | 12 | 9 | — | 21 |
| `rope` | — | 5 | 10 | 15 |
| `epistemic_games` | 9 | — | — | 9 |
| **Total** | **56** | **14** | **10** | **80** |

`rope` never reached scoring and has no row in the 38-environment tables. One disagreement sits here: the campaign's provenance summary gives 24 known-gate omissions where the detailed rows give 14. I report both; nothing in the records says which was intended, and the coincidence that 14 plus the 10 modality cases equals 24 is not a reconciliation. The records say nothing about how selection was done, so I assume neither random nor targeted selection. What the table does show is that omissions concentrate in `moco` and `glyph`, two environments that weigh heavily on the pooled figure.

## An endpoint-heavy map

| Environment outcome | Environments | PASS / scored | Share of scored | Unscored |
|---|---:|---:|---:|---:|
| Every scored case passed | 17 | 172/172 | 42.5% | 0 |
| No scored case passed | 7 | 0/68 | 16.8% | 0 |
| Some passed, some failed | 12 | 105/165 | 40.7% | 1 |
| No scored case | 2 | — | — | 10 |
| **Total** | **38** | **277/405** | **100%** | **11** |

Twenty-four of the 36 scored environments are at an endpoint. I call the map endpoint-heavy and stop there: an endpoint on four cases and one on 24 are both single-seed observations, and the table cannot say how either would hold under other cases or seeds.

![Dot plot of pass fraction by environment with 95% Wilson intervals and a dotted line at the pooled 68.4%](../figures/fig9_environment_intervals.svg)
*Figure 9. One dot per environment with scored cases (36; the two environments with no scored case are not drawn), placed at PASS/scored and labelled k/n. Bars are 95% Wilson intervals under a binomial sampling convention; they are not measured seed-to-seed variation, and selection and possible dependence among cases limit what they mean. The dotted line is the pooled 277/405. Colours mark no scored pass (7), mixed (12), and all scored passed (17).*

The 17 all-pass environments are nine at 9/9 (`architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, `tokenizer_adjunction`), plus `epistemic_games` 23/23, `css_state_machine` 18/18, `rd_gradient_credit` and `rd_state_carry` 15/15, `epistemic_announcements` and `epistemic_nested_knowledge` 6/6, `epistemic_fragmented_observation` and `ts_parse_only` 4/4. One of the four `ts_parse_only` PASSes is marked performance-ineligible: its recorded exclusion field attributes a terminal failure to a provider transient after bounded retries, while the verdict reads PASS. The two fields conflict; I keep the case among the 277 and alter nothing.

The seven zero-pass environments are `functorial_augmentation`, `monadic_reward`, `sheaf_invariant_gluing` and `sheaf_physical_constraints` at 0/9, `ts_one_step` and `ts_trajectory` at 0/4, and `glyph` at 0/24. Eight of the nine `monadic_reward` FAILs also carry the disposition `rejected`, a term the records do not define, so its 0/9 may not mean what the other zeros mean.

The mixed twelve:

| Environment | PASS / scored | Recorded flags |
|---|---:|---|
| `sheaf_schema_sync` | 8/9 | |
| `sql_fixed_point` | 8/9 | |
| `transformer_ssm_lift` | 8/9 | lone FAIL has disposition `rejected` |
| `compositional_optimizer` | 7/9 | |
| `equivariant_diagram` | 7/9 | |
| `tensor_functor` | 6/9 | |
| `moco` | 36/55 | three FAILs have disposition `unscored` |
| `rd_adaptive_halting` | 8/14 | plus one `infrastructure_unscored` case |
| `gnn_message_passing` | 5/9 | |
| `regex_state_machine` | 5/9 | one FAIL has disposition `unscored` |
| `ssm_parallel_scan` | 5/9 | |
| `batchnorm_ema` | 2/15 | one FAIL `rejected`, one disposition `unscored` |

These hold 165 of the 405 scored cases, 40.7%, and run from 2/15 to 8/9. Averaging the 36 environment fractions without weighting gives about 69.2%; the median is 8/9. Each answers a different question; neither recovers the shape.

## Names and density

Prefixes invite a shortcut: read `ts_*` or `sheaf_*` as a family, expect a family outcome. The records refuse it. `ts_parse_only` is 4/4; `ts_one_step` and `ts_trajectory` are 0/4. `sheaf_schema_sync` is 8/9; `sheaf_invariant_gluing` and `sheaf_physical_constraints` are 0/9. `categorical_lenses` is 9/9, `functorial_augmentation` 0/9, `tensor_functor` 6/9. These are outcomes attached to distinct environment labels, not positions on a shared scale.

Density pulls the other way. `glyph` (0/24), `moco` (36/55) and `batchnorm_ema` (2/15) supply 94 of the 405 scored cases and 56 of the 128 FAILs. That is where the pooled rate gets its weight, and arithmetic on the recorded rows shows how much:

| Arithmetic on recorded rows | Rate |
|---|---:|
| All scored cases | 277/405 = 68.4% |
| Without `moco` | 241/350 = 68.9% |
| Without `glyph` | 277/381 = 72.7% |
| Without both | 241/326 = 73.9% |

These illustrate sensitivity to selected case density. They are not alternative results, and they say nothing about why those environments failed or whether they share a mechanism.

## Beneath the environments: 340 rows

Each environment's cases sit on difficulty tuples, and the records hold one row per environment × tuple: 340 rows, 4 to 15 per environment, six environments above ten. This is a different object from the 496 case-ID frame.

![Grid of 340 squares, one per environment × difficulty-tuple row, coloured by pass rate](../figures/fig10_tuple_matrix.svg)
*Figure 10. One square per row, grouped by environment. Colour is the row's pass rate: red 0, amber fractional, green 1. Grey marks the 11 rows with no scored case: ten in the two entirely unscored environments and the one unscored `rd_adaptive_halting` row. Numbers mark the 44 rows holding more than one case. The nine amber rows are all in `moco`. Tuples are environment-specific, so columns are not comparable across environments.*

Four facts:

- **296 of 340 rows hold one case** (285 scored, 11 unscored). The 44 multi-case rows sit in four environments: `moco` (15 rows, 55 cases), `glyph` (12, 24), `css_state_machine` (9, 18), `epistemic_games` (8, 23).
- **329 rows carry a pass rate, and 320 of them (97.3%) are exactly 0 or 1.** A scored single-case row can be nothing else, so the matrix repeats the endpoint pattern one level down largely by construction. The nine fractional rows are all in `moco`.
- **204 rows lie in environments whose scored outcome is uniform**: 148 in all-pass and 56 in zero-pass environments. Ten more lie in the two environments with no scored outcome. The figure 214 is reachable only by grouping that shared absence with the observed outcomes, and I do not describe those ten rows as outcomes.
- **98 tuples have zero passes, across 19 environments**, including all 12 mixed ones. That is a different count from the seven zero-pass environments and does not reduce to it.

The matrix uses 34 distinct difficulty keys in total, but each environment uses its own small set. There is no common scale, so I do not pool, rank, or regress tuples across environments, and nothing in this layer is read as a difficulty effect.

A note on units. The records define no sampling "cell", and I do not infer one from the arithmetic: 340 rows hold 416 cases, 44 rows hold more than one, all at seed 0. The 405 scored cases are not 405 distinct tuples, and the records neither establish independence among cases in a row nor estimate dependence. A unanimous multi-case row shows agreement, not repeatability.

`moco` is the one environment whose rows vary. Six of its 15 rows are at 0 or 1; the other nine are fractional (2/3 four times, 5/6, 3/4, 2/5, 1/3, 1/6), summing with the rest to 36/55. Every row has a recorded tuple key, so a descriptive map is possible. The 1/6 row, for instance, is `distractors=hard, naming=easy, queue_math=easy, symptom_mask=hard, temperature=hard, visible_tests=easy`: six cases, five labelled `overfit_visible_tests`. The keys permit description only; under one seed, with six-key tuples and two to six cases per row, they establish no isolated dimension effect and no trend.

The single unscored `rd_adaptive_halting` case sits at the row where all five keys read `easy`. That is a recorded field, not an explanation; it does not turn a missing verdict into a failure.

## What the labels and guarantees record

![Horizontal bar chart of recorded failure labels for all 128 FAIL outcomes combined](../figures/fig11_failure_labels.svg)
*Figure 11. Recorded failure labels across all 128 FAILs: underfit 51, overfit_visible_tests 49, runtime_error 11, source_invalid 9, invalid_action 5, training_failed 3. The 11-case runtime bar consolidates nine cases recorded as `RUNTIME_ERROR` and two as `runtime_error`, an analysis convention. The image has no environment split; the table below supplies it.*

The labels are recorded classifications, not observations of what the model did. By environment:

| Environment | Recorded FAIL labels |
|---|---|
| `glyph` | overfit_visible_tests 22, underfit 1, invalid_action 1 |
| `moco` | overfit_visible_tests 16, training_failed 2, invalid_action 1 |
| `batchnorm_ema` | overfit_visible_tests 11, training_failed 1, invalid_action 1 |
| `functorial_augmentation` | underfit 6, RUNTIME_ERROR 3 |
| `monadic_reward` | source_invalid 8, invalid_action 1 |
| `sheaf_invariant_gluing` | underfit 9 |
| `sheaf_physical_constraints` | underfit 9 |
| `rd_adaptive_halting` | RUNTIME_ERROR 5, underfit 1 |
| `gnn_message_passing` | underfit 4 |
| `ssm_parallel_scan` | underfit 4 |
| `regex_state_machine` | underfit 3, invalid_action 1 |
| `ts_one_step` | underfit 3, runtime_error 1 |
| `ts_trajectory` | underfit 3, runtime_error 1 |
| `tensor_functor` | underfit 3 |
| `compositional_optimizer` | underfit 2 |
| `equivariant_diagram` | underfit 1, RUNTIME_ERROR 1 |
| `sheaf_schema_sync` | underfit 1 |
| `sql_fixed_point` | underfit 1 |
| `transformer_ssm_lift` | source_invalid 1 |

The rows sum to 128. The two lowercase runtime labels belong to cases whose disposition is `unscored`; all nine uppercase ones belong to cases whose disposition is `scored`. I record that alignment and offer no account of it.

Two disposition groups need to stay visible. Ten scored FAILs carry the disposition `rejected`: eight in `monadic_reward` and one in `transformer_ssm_lift`, all labelled `source_invalid`, plus one `training_failed` in `batchnorm_ema`. Nine other scored FAILs carry the disposition `unscored`: three in `moco` and one each in `batchnorm_ema`, `glyph`, `monadic_reward`, `regex_state_machine`, `ts_one_step` and `ts_trajectory`, labelled five `invalid_action`, two `training_failed`, two `runtime_error`. That disposition is a different field from the status `infrastructure_unscored`, and the records define neither term. All 19 stay in the 128.

Then the guarantees. Each environment was judged under exactly one:

| Judge guarantee | Environments | PASS / scored | Unscored |
|---|---:|---:|---:|
| `behavioral_reference` | 11 | 141/189 = 74.6% | 0 |
| `compile_only` | 27 | 136/216 = 63.0% | 11 |

The two rates differ, and the difference cannot be read as a judge effect, because guarantee and environment are confounded: no environment was judged both ways. Nor does the guarantee sort the endpoints on its own; `epistemic_games` (23/23) and `glyph` (0/24) are both `behavioral_reference`. Of the nine 9/9 environments, four are behavioral-reference and five compile-only. A compile-only PASS records that a compile check succeeded; it is not behavioral validation. A behavioral-reference PASS records what that judge checked and no more. For `epistemic_games`, the bounded reading is that the task asks for Bayesian inference over stipulated policies; a 23/23 there is not evidence of recursive reasoning about other minds.

## Withdrawn and open

**Withdrawn.** The earlier version suggested non-monotonic variation across difficulty in `css_state_machine`. All 18 cases passed; each of its nine tuple rows is 2/2. There is nothing to describe.

**Open, not findings.** Apparent non-monotonic patterns in `moco` remain a question. The single `sql_fixed_point` FAIL sits at `hidden_depth=hard, surface_deceptiveness=easy`; one observation under one seed establishes no difficulty trend, and I have not computed how often such patterns would arise by chance in a mostly binary matrix.

**Where the records disagree with themselves.** An earlier project overview counts 10 environments at zero and "~12" at 1.0; the rows give 7 and 17, and the 19 environments containing a zero-pass tuple do not reproduce the 10 either. The provenance summary's 24 known-gate omissions stand against 14 detailed rows. The ineligible `ts_parse_only` PASS carries exclusion wording that contradicts its verdict. The dispositions `rejected` and `unscored` are undefined. I leave each as stated.

## What this supports

On this archived selection, Mercury-2.5 received 277 PASS verdicts among 405 scored cases: all-pass in 17 environments, all-fail in 7, mixed in 12, no verdict in 2. Only two environments sit near the pooled rate. Beneath them, 320 of 329 rated tuple rows are binary, mostly because they hold one case; the only fractional rows are in `moco`. Closely named environments landed far apart.

What it does not support: a common difficulty scale, so no ranking of environments and no claim that environment identity outweighs difficulty; a mechanism behind `glyph`, `moco`, or `batchnorm_ema`; how an endpoint would hold under a second seed; or what a uniform judge would show. Reproduction is bounded too. The source repository was recorded as dirty at run time, and no clean configuration-hash comparison exists, so the exact working-tree state is [m-word] for anyone trying to rerun this.

The next useful evidence is the kind this record cannot give: repeated seeds within environments, and guarantees varied within an environment rather than fixed by it. The first would show which endpoints are stable; the second, whether 74.6% against 63.0% is about judges or about environments.

Until then, 68.4% keeps its one precise job, the share of scored, selected cases with a PASS, and the map beside it does the rest.

&&&&&&&&

grok 4.5:
---
title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>A retrospective reading of archived Mercury-2.5 judgments across environments and the environment-by-tuple matrix beneath them; no new model runs.</dd>
  <dt>Synthesis</dt>
  <dd>Regrouping of 416 selected cases in 38 environments and 340 tuple rows against exact counts, endpoints, density, recorded labels, guarantees, and open record discrepancies.</dd>
  <dt>Prose</dt>
  <dd>First-person exploratory prose written for this article; drafting and revision were AI-assisted.</dd>
  <dt>Certainty</dt>
  <dd>High on the recorded counts and tallies; low on causal or stability readings, given one seed across the supplied selected records, a dirty source state, unscored cases, guarantee fixed by environment, selection, and unresolved summary discrepancies.</dd>
  <dt>Importance</dt>
  <dd>A pooled benchmark number is easy to mistake for a uniform description of its parts; this archive shows both how much the number compresses and how little it can support.</dd>
</dl>

**Revision note.** This replaces the earlier version under the same title. The headline figure is unchanged: 277 of 405 scored cases passed, 68.4%. What is new is an exploratory second layer — the 340-row environment × difficulty-tuple matrix — read as description rather than result. One earlier claim is withdrawn, several are left open, and places where the archive’s own records disagree are stated rather than smoothed over.

Mercury-2.5 received PASS on 68.4% of the scored cases in this archived campaign. What should a reader expect from any one environment? Only two of the 36 environments with scored cases land within five points of that pooled value — `moco` at 36/55 (65.5%) and `tensor_functor` at 6/9 (66.7%). Twenty-four of those 36 sit at an observed endpoint: every scored case passed, or none did. The rest of the piece maps what 68.4% compresses, and what the record still cannot establish.

These are verdicts the campaign’s judges assigned to selected cases. They are not repeated measurements of general capability, and an environment name is not a difficulty rating. Every supplied selected-case record carries seed 0; no second seed is recorded. Two kinds of judge guarantee are fixed by environment. The aim is to keep the pooled number visible while showing the map underneath it.

## First, count the cases that received a judgment

The archive holds **416 selected cases in 38 environments**. Of those, 405 received a PASS or FAIL verdict: 277 PASS and 128 FAIL. So **277/405 = 68.4%** is the scored-case pass rate. Eleven cases carry the recorded status `infrastructure_unscored`; the records state no cause. They are not a third outcome and must not be treated as failures.

![Three stacked bars from 496 recorded case IDs through selected and scored cases to 277 PASS and 128 FAIL](../figures/fig8_selection_frame.svg)
*Figure: Selection frame. Three stacked bars. The top bar is labelled “design cells” in the image and shows 496 recorded case IDs = 416 selected + 80 omitted (56 intervention-twin, 14 known-gate, 10 unsupported input modality, all ten modality cases in `rope`). The middle bar is selected cases: 405 scored + 11 `infrastructure_unscored` (the 11-case segment has no numeric label in the image; the count is given here). The bottom bar is scored cases: 277 PASS + 128 FAIL. Omitted cases enter no pass rate. Nine scored FAILs carry a disposition that conflicts with their scored status; those conflicts are not drawn as a separate segment.*

The fraction **277/416 = 66.6%** answers a different question: the share of all selected cases with an observed PASS. It must not be read as a pass rate that assigns outcomes to the 11 unknowns.

| Environment outcome | Environments | PASS / scored cases | Share of scored cases | Unscored cases |
|---|---:|---:|---:|---:|
| Every scored case passed | 17 | 172/172 | 42.5% | 0 |
| No scored case passed | 7 | 0/68 | 16.8% | 0 |
| Some passed, some failed | 12 | 105/165 | 40.7% | 1 |
| No scored cases | 2 | — | — | 10 |
| **Total** | **38** | **277/405** | **100%** | **11** |

Twenty-four of the 36 environments with scored cases sit at an observed endpoint. Some rest on four cases, others on 23 or 24. The mixed environments are not a remainder: they hold 165 of the 405 scored cases (40.7%), ranging from 2/15 to 8/9. Across the 36 scored environments, the unweighted mean of the environment-level pass fractions is about 69.2%; the median is 8/9 (88.9%). Each summary answers a different question; neither removes the shape.

Before scoring, 80 cases were omitted: 56 intervention-twin, 14 known-gate calibration failures, and 10 unsupported input-modality cases. By environment the omissions are concentrated: `moco` 35 (all twin), `glyph` 21 (9 gate + 12 twin), `rope` 15 (10 modality + 5 gate), `epistemic_games` 9 (all twin). A provenance summary instead states 24 known-gate omissions against the 14 in the detailed rows. Both figures are reported; the discrepancy is unresolved. The identity 14 + 10 = 24 is a possible aggregation reading and is not verified. The 80 omitted cases sit outside the 416 and outside every pass rate below. The 496 figure counts recorded case IDs; it is not the 340-row matrix, and “design cells” is the chart’s label, not a technical unit.

## The endpoint-heavy map

![Dot plot of pass fraction by environment with 95% Wilson intervals](../figures/fig9_environment_intervals.svg)
*Figure: Environment intervals. One dot per environment with scored cases (36; the two environments with no scored case are not drawn) at its PASS/scored fraction; each bar is a 95% Wilson interval under a binomial sampling convention — not measured seed variation; the dotted vertical line is the pooled 277/405 = 68.4%; the label beside each bar is k/n. Colour classes: no scored pass, mixed, all scored passed. Selection and possible dependence constrain interpretation. Endpoints rest on anywhere from four to 24 cases.*

**17 environments where every scored case passed** (172/172). Nine are 9/9: `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, `tokenizer_adjunction`. Larger: `epistemic_games` 23/23, `css_state_machine` 18/18, `rd_gradient_credit` 15/15, `rd_state_carry` 15/15. Smaller: `epistemic_announcements` 6/6, `epistemic_nested_knowledge` 6/6, `epistemic_fragmented_observation` 4/4, `ts_parse_only` 4/4. One of the four `ts_parse_only` PASS cases is marked performance-ineligible; its recorded exclusion note attributes a terminal failure to a provider transient, while the verdict is PASS. The PASS stays in the 277; the field conflicts with the verdict and is not independent proof of cause.

**7 environments where no scored case passed** (0/68): `functorial_augmentation` 0/9, `monadic_reward` 0/9, `sheaf_invariant_gluing` 0/9, `sheaf_physical_constraints` 0/9, `ts_one_step` 0/4, `ts_trajectory` 0/4, `glyph` 0/24. Eight of the nine scored `monadic_reward` FAILs also carry the disposition `rejected`, which the archive does not define; all nine remain in the 0/9 and in the 128.

**12 mixed environments** (105/165 scored, plus one unscored):

| Environment | PASS / scored | Flags |
|---|---:|---|
| `sheaf_schema_sync` | 8/9 | — |
| `sql_fixed_point` | 8/9 | — |
| `transformer_ssm_lift` | 8/9 | lone FAIL carries `rejected` |
| `compositional_optimizer` | 7/9 | — |
| `equivariant_diagram` | 7/9 | — |
| `tensor_functor` | 6/9 | — |
| `gnn_message_passing` | 5/9 | — |
| `regex_state_machine` | 5/9 | one FAIL disposition `unscored` |
| `ssm_parallel_scan` | 5/9 | — |
| `moco` | 36/55 | three FAILs disposition `unscored` |
| `rd_adaptive_halting` | 8/14 (+1 unscored) | — |
| `batchnorm_ema` | 2/15 | one FAIL `rejected`, one disposition `unscored` |

The pooled rate therefore sits above a landscape in which most scored environments landed at an endpoint rather than near 68%. Closely named environments sometimes landed far apart: the `ts_*` trio is 4/4, 0/4, 0/4; the `sheaf_*` names are 8/9, 0/9, 0/9; among category-flavoured names, `categorical_lenses` is 9/9, `functorial_augmentation` 0/9, `tensor_functor` 6/9. Shared prefixes are handles, not forecasts.

Case density pulls on the top line. `glyph`, `moco`, and `batchnorm_ema` together supply 94 of 405 scored cases and 56 of 128 FAILs. Excluding `moco` gives 241/350 = 68.86%; excluding `glyph` gives 277/381 = 72.70%; excluding both gives 241/326 = 73.93%. These are arithmetic illustrations of selected case density, not alternative results, and they establish no shared failure mechanism.

## Beneath the environments: 340 rows

![Grid of 340 environment-by-tuple rows coloured by pass rate](../figures/fig10_tuple_matrix.svg)
*Figure: Tuple matrix. Each square is one environment × difficulty-tuple row (340 total), grouped by environment. Colour is the row pass rate (red 0, amber fractional, green 1). Grey marks the 11 rows with no scored case (distinct from the ten rows belonging to the two entirely unscored environments). Numbers mark the 44 rows holding more than one case. The nine fractional rows are all in `moco`. Tuples are environment-specific, so columns are not comparable across environments.*

The matrix has between 4 and 15 rows per environment; six environments have more than 10. **296 of 340 rows are single-case**; the 44 multi-case rows sit in four environments only: `moco` (15 rows, 55 cases), `glyph` (12/24), `css_state_machine` (9/18), `epistemic_games` (8/23). Of 329 rows with a pass rate, **320 (97.3%) are exactly 0 or 1**; the nine fractional rows are all in `moco`. A scored single-case row can only be 0 or 1; eleven single-case rows have no scored outcome at all.

**204 rows** lie in environments with a uniform scored outcome (every scored row the same). **Ten more** lie in the two entirely unscored environments (`epistemic_silence` 6, `epistemic_type_games` 4). Grouping those as a shared absence of scored outcomes yields 214; they are not 214 observed success/failure outcomes. Separately, **98 individual tuples have zero passes**, spread across 19 environments — a different count from the seven environments with no scored PASS — and all 12 mixed environments contain at least one such tuple.

The complete matrix records a difficulty-tuple key for every row, including all 15 `moco` rows. Six of those sit at 0 or 1; the other nine are fractional (values 1/6, 1/3, 2/5, 2/3, 3/4, 5/6). One example: the 1/6 row has six cases under `distractors=hard`, `naming=easy`, `queue_math=easy`, `symptom_mask=hard`, `temperature=hard`, `visible_tests=easy`, with five `overfit_visible_tests` labels. Across the matrix there are 34 distinct difficulty-key names; they are environment-specific. Keys support description only. They do not establish an isolated dimension effect, a monotonic trend, a common calibrated scale, or a ranking, and the apparent `moco` pattern stays open.

The supplied records show seed 0 for every selected case and record no second seed. Forty-four rows hold more than one case. The records do not define a technical sampling unit called a “cell,” and they do not estimate within-tuple dependence. The unscored `rd_adaptive_halting` row sits at the tuple where all five dimensions are `easy`; that label supplies no judgment and does not turn the gap into an easy-case failure. The environment remains 8/14 scored plus one unscored case.

## What the labels and guarantees record

![Horizontal bar chart of recorded failure labels across all 128 FAIL outcomes](../figures/fig11_failure_labels.svg)
*Figure: Global failure labels for all 128 FAIL outcomes combined (underfit 51, overfit_visible_tests 49, runtime_error 11 — consolidating nine uppercase `RUNTIME_ERROR` and two lowercase `runtime_error` spellings as an analysis convention — source_invalid 9, invalid_action 5, training_failed 3). No environment split in the image; the breakdown is in the table below.*

| Environment | FAIL labels |
|---|---|
| `glyph` | overfit_visible_tests 22, underfit 1, invalid_action 1 |
| `moco` | overfit_visible_tests 16, training_failed 2, invalid_action 1 |
| `batchnorm_ema` | overfit_visible_tests 11, training_failed 1, invalid_action 1 |
| `functorial_augmentation` | underfit 6, RUNTIME_ERROR 3 |
| `monadic_reward` | source_invalid 8, invalid_action 1 |
| `sheaf_invariant_gluing` | underfit 9 |
| `sheaf_physical_constraints` | underfit 9 |
| `rd_adaptive_halting` | RUNTIME_ERROR 5, underfit 1 |
| `gnn_message_passing` | underfit 4 |
| `ssm_parallel_scan` | underfit 4 |
| `ts_one_step` | underfit 3, runtime_error 1 |
| `ts_trajectory` | underfit 3, runtime_error 1 |
| `tensor_functor` | underfit 3 |
| `compositional_optimizer` | underfit 2 |
| `equivariant_diagram` | underfit 1, RUNTIME_ERROR 1 |
| `regex_state_machine` | underfit 3, invalid_action 1 |
| `sheaf_schema_sync` | underfit 1 |
| `sql_fixed_point` | underfit 1 |
| `transformer_ssm_lift` | source_invalid 1 |

These are recorded classifications, not observations of internal reasoning. The uppercase/lowercase runtime split aligns with disposition `scored` versus disposition `unscored`; that association is recorded, and no explanation is offered.

Two disposition groups sit inside the 128 and must stay visible. **Ten scored FAILs carry disposition `rejected`:** eight in `monadic_reward`, one in `batchnorm_ema`, one in `transformer_ssm_lift` (nine of the ten carry `source_invalid`; the tenth carries `training_failed`). **Nine other scored FAILs carry disposition `unscored`** while status remains `scored`: three in `moco`, and one each in `batchnorm_ema`, `glyph`, `monadic_reward`, `regex_state_machine`, `ts_one_step`, `ts_trajectory` (labels: five `invalid_action`, two `training_failed`, both lowercase `runtime_error`). The archive defines neither disposition. Disposition `unscored` is not the status `infrastructure_unscored`. The flags qualify the affected comparisons — especially `monadic_reward` 0/9, `transformer_ssm_lift` 8/9, and `batchnorm_ema` 2/15 — without removing any case from the counts.

Judge guarantees are fixed by environment: **11 environments** are `behavioral_reference` (189 selected cases, **141/189 scored PASS**, 48 FAIL); **27** are `compile_only` (227 selected, **136/216 scored PASS**, 80 FAIL, and all 11 unscored cases). Among the nine 9/9 environments, four are behavioral-reference and five are compile-only. Because each environment carries exactly one guarantee, the rate contrast is confounded with environment and is not a measured judge effect. A compile-only PASS is not behavioral validation. A PASS under either guarantee records only what that case’s judge checked; it does not show that the model understood or solved the task. Both `epistemic_games` 23/23 and `glyph` 0/24 are behavioral-reference, so the guarantee alone does not sort the endpoints. If `epistemic_games` is described beyond its count, the target is Bayesian inference over stipulated policies, not recursive theory of mind.

## Claims withdrawn or left open

**Withdrawn:** non-monotonic variation in `css_state_machine`. The environment is 18/18 over nine rows; every row is 2/2. There is no variation to describe.

**Open, not findings:** apparent non-monotonic patterns in `moco`; the single FAIL in `sql_fixed_point` at `hidden_depth=hard`, `surface_deceptiveness=easy`. Under one seed and mostly binary rows, such patterns can arise by chance; no base rate has been computed. One observation establishes no difficulty effect.

**Unresolved source discrepancies, preserved rather than closed:**

- Scored zero-pass environments: the rows give **seven**; an earlier overview states **10**. The 19 environments that contain a zero-pass tuple are a different unit and do not reproduce 10. Fully unscored environments and omitted `rope` do not verify the overview’s rule.
- All-pass environments: the rows give **17** (172/172); the overview says “~12 at 1.00.” No supplied rule explains the approximate twelve.
- Known-gate omissions: detailed rows give **14**; provenance states **24**. Both are reported; 14 + 10 = 24 is an unverified possible aggregation, not a reconciliation.
- Dispositions `rejected` and `unscored` remain undefined.
- The ineligible `ts_parse_only` PASS keeps its recorded exclusion wording in conflict with its verdict; provenance’s “1 retry, 60s” and the row’s attempt/time fields are not reconciled.

The source repository was recorded as dirty at run time. The exact working-tree state is [m-word] for reproduction; no clean config-hash comparison is supplied. That limit sits beside any claim about what another tree would change.

## What this supports

On this archived selection, Mercury-2.5 received **277 PASS judgments among 405 scored cases**. Judges recorded all-pass outcomes in 17 environments, all-fail in 7, mixed in 12, and no scored outcome in 2. Twenty-four of 36 scored environments sit at an endpoint. Only two land near the pooled value. The tuple matrix mostly repeats the endpoint pattern one level down — 320 of 329 rated rows at 0 or 1, 204 rows in environments with a uniform scored outcome, plus 10 in entirely unscored environments — largely because most rows hold one case. Fractional rows occur only in `moco`. Closely named environments landed far apart. Labels and guarantees are available as descriptive cross-tabs; neither yields a mechanism or a controlled judge comparison.

This does not show a common difficulty scale on which environments could be ranked, so it does not show that environment identity outweighs difficulty. It does not identify a mechanism for `glyph`, `moco`, or `batchnorm_ema`. It does not say how any endpoint would hold under another seed, a uniform guarantee varied within environments, or a clean source tree. The next evidence the record cannot supply is repeated seeds within environments and guarantees that vary inside an environment; each would narrow stability and confound questions without turning a single campaign into a general capability score.

So **68.4%** remains the answer to one precise question: what fraction of scored, selected cases received PASS? It should not stand alone. The more informative answer is the map beside it — the zeros, the perfect scores, the 40.7% of scored cases in between, the thin tuple rows, and the gaps the archive declines to settle.