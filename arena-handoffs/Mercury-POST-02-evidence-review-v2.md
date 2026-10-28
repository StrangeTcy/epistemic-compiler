# POST-02 redo — Evidence review of the revised article

This is a self-contained Arena handoff. The article and evidence packet below are quoted verbatim from the pinned repository revision. Do not use repository paths or reconstruct omitted material.

SOURCE COMMIT
- Repository commit: `6ed48cb1c4447d4f902d1fbc8a908a56185e34ed` (`origin/arena/7471eb0f-epistemic-compiler`)
- Article source: `campaign-02-analysis/posts/POST-02-cross-environment-map.md`
- Evidence source: `campaign-02-analysis/post-production/handoffs/POST-02-redo_evidence_packet.md`

## Article “What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments” — verbatim

<BEGIN ARTICLE>
---
title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>A retrospective look at the archived Mercury-2.5 results, comparing environments and examining how their outcomes are distributed, with no new model runs.</dd>
  <dt>Synthesis</dt><dd>I grouped the 416 selected cases in 38 environments and a 340-row environment × difficulty-tuple matrix to set the pooled pass rate against case counts, endpoints, case density, and the confounds the archive records.</dd>
  <dt>Prose</dt><dd>Written for this article in the first person, with every figure tied to the reported counts.</dd>
  <dt>Certainty</dt><dd>I am fairly confident in the counts, but much less confident about any cause or mechanism, because the archive has a single seed, a dirty source state, unscored cases, two kinds of judge guarantee, and some open discrepancies.</dd>
  <dt>Importance</dt><dd>One pooled benchmark number can hide where its cases sit, how unevenly they are spread, and how little the archive can actually support.</dd>
</dl>

*Revision note: This version replaces the one first published under this title. The headline figure, 68.4%, has not changed. I have corrected several passages, added an environment × difficulty-tuple matrix as an exploratory second layer, and listed the withdrawn and open claims in their own section instead of quietly removing them.*

Mercury-2.5 received PASS judgments on 68.4% of the scored cases in this campaign. What would I expect if I opened one of its environments at random? The `ts_*` results make that question awkward. `ts_parse_only` is 4/4, while `ts_one_step` and `ts_trajectory` are each 0/4. All three count toward the same pooled number. A single pooled pass rate can turn very uneven environment-level results into one tidy figure.

My aim is to understand what that number summarizes, not to replace it with a different slogan. These are outcomes that the campaign's judges assigned to selected cases. They are not repeated measurements of general capability, and an environment name is not a difficulty rating. This is a retrospective analysis of archived results. It was not preregistered. Still, the differences between environments are too large to leave unstated. The 68.4% figure is arithmetically correct, but on its own it describes little. The more useful structure is the endpoint-heavy map underneath it.

## First, count the cases that received a judgment

The archive contains **416 selected cases in 38 environments**. Of these, 405 received a PASS or FAIL judgment: 277 PASS and 128 FAIL. So **277/405, or 68.4%**, is the scored-case pass rate (the case-weighted pooled rate). The other 11 cases have no scored result. The archive labels them `infrastructure_unscored` and records no further cause, so I do not describe them as judge gaps or as a third kind of outcome.

![Bar chart from 496 design cells to 277 PASS and 128 FAIL judgments; 80 cases omitted before scoring](../figures/fig8_selection_frame.svg)
*Figure: From the 496 design cells, 80 were omitted before scoring and 416 were selected. Of the 416, 11 have no scored result (the archive's `infrastructure_unscored` status) and 405 were scored: 277 PASS and 128 FAIL. The omitted cases have no score, so they are outside every pass rate in this article. Nine of the 128 scored FAILs carry a disposition label that conflicts with their scored status; the text explains this.*

The fraction **277/416, or 66.6%**, answers a different question: what share of *all selected cases* has an observed PASS? It must not be presented as a pass rate, because doing so silently turns the 11 unknown outcomes into failures.

| Environment outcome | Environments | PASS / scored cases | Share of scored cases | Unscored cases |
|---|---:|---:|---:|---:|
| Every scored case passed | 17 | 172/172 | 42.5% | 0 |
| No scored case passed | 7 | 0/68 | 16.8% | 0 |
| Some passed, some failed | 12 | 105/165 | 40.7% | 1 |
| No scored cases | 2 | — | — | 10 |
| **Total** | **38** | **277/405** | **100%** | **11** |

Of the 36 environments with scored cases, 24 sit at an observed endpoint: every scored case passed or every scored case failed. I call the map *endpoint-heavy*. I am not claiming a capability split into two populations. Some endpoints rest on four cases and others on 23 or 24, and because every case ran under one seed, the table cannot say how stable any endpoint would be.

The mixed environments are not minor exceptions. They hold **165 of the 405 scored cases (40.7%)**, with 105 PASS among those 165 and one additional unscored case. Their results range from 2/15 to 8/9.

Across the 36 scored environments, the unweighted mean of the pass fractions is about 69.2%, and the median is 8/9 (88.9%). Each of these summaries answers a different question, and each still hides the shape of the map.


## The endpoint-heavy distribution

Out of the 36 scored environments, 24 sit at an endpoint.

![Dot plot of pass fraction by environment with 95% Wilson intervals](../figures/fig9_environment_intervals.svg)
*Figure: Each dot is one environment's pass fraction among its scored cases; each bar is a 95% Wilson interval; the dotted vertical line is the pooled 277/405 = 68.4%, and the label beside each bar is PASS/scored. Environments with 4 to 9 cases have wide intervals. The intervals treat each environment's scored cases as a sample under one seed. They do not estimate a population of environments, and they are not a measure of seed-to-seed variation. Environments with no scored cases are not drawn.*

- **17 all-pass environments (rate 1.0), 172/172 scored cases.** That is 17 of 36 scored environments (47%).
  - **9/9:** `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, and `tokenizer_adjunction`.
  - **Larger environments:** `css_state_machine` 18/18, `rd_gradient_credit` 15/15, `rd_state_carry` 15/15, and `epistemic_games` 23/23.
  - **Smaller environments:** `epistemic_announcements` 6/6, `epistemic_nested_knowledge` 6/6, `epistemic_fragmented_observation` 4/4, and `ts_parse_only` 4/4.
  - **Caveat for `ts_parse_only`:** One of its four PASS cases is marked performance-ineligible. Its exclusion note describes a provider-attributed terminal failure, yet its verdict is PASS. I keep it in the 277, but those two records disagree.
- **7 all-fail environments (rate 0.0), 0/68 scored cases.** These are `functorial_augmentation` 0/9, `monadic_reward` 0/9, `sheaf_invariant_gluing` 0/9, `sheaf_physical_constraints` 0/9, `ts_one_step` 0/4, `ts_trajectory` 0/4, and `glyph` 0/24.
  - **Caveat for `monadic_reward`:** 8 of its 9 scored FAIL cases also carry the case disposition `rejected`. The archive does not define that term. I keep all of them in the counts, so this 0/9 may not mean the same thing as the other zeros.

That leaves the 12 mixed environments:

| Environment | PASS / scored |
|---|---:|
| `sheaf_schema_sync` | 8/9 |
| `sql_fixed_point` | 8/9 |
| `transformer_ssm_lift` | 8/9 |
| `compositional_optimizer` | 7/9 |
| `equivariant_diagram` | 7/9 |
| `tensor_functor` | 6/9 |
| `gnn_message_passing` | 5/9 |
| `regex_state_machine` | 5/9 |
| `ssm_parallel_scan` | 5/9 |
| `moco` | 36/55 |
| `rd_adaptive_halting` | 8/14 (+1 unscored) |
| `batchnorm_ema` | 2/15 |

The 68.4% pooled rate therefore sits above a landscape in which most scored environments landed at an endpoint rather than anywhere near 68%.

## Names are useful handles, not forecasts

It is tempting to treat prefixes such as `ts_*` or `sheaf_*` as coherent families and to expect shared outcomes within each one. In this archive, those labels are an unreliable shortcut.

The `ts_*` trio is the clearest small example. `ts_parse_only` is 4/4 (with the ineligibility flag noted above), while `ts_one_step` and `ts_trajectory` are each 0/4. That accurately describes three sets of four judged cases. It is not evidence of a difficulty ladder. There is no shared difficulty scale here, and these are not repeated trials of the same test.

The `sheaf_*` names set the opposite trap. `sheaf_schema_sync` is 8/9, while `sheaf_invariant_gluing` and `sheaf_physical_constraints` are each 0/9. Combining all three into one "sheaf performance" figure would hide the very contrast that stands out. Category-theory-flavoured names are no more predictive: `categorical_lenses` is 9/9, `functorial_augmentation` is 0/9, and `tensor_functor` is 6/9. A shared name does not imply shared outcomes in this archive.

`glyph`, `moco`, and `batchnorm_ema` reinforce the same caution:

- `glyph` is 0/24, a much larger all-fail block than the four-case `ts_*` zeros.
- `moco` is 36/55 (65.5%), with 19 failures.
- `batchnorm_ema` is 2/15 (13.3%), with 13 failures. One of those failures carries the undefined `rejected` disposition.

Together, these three environments contribute **94 of the 405 scored cases but 56 of the 128 failures**. That shows concretely how much the pooled result depends on where cases were selected. It does not show that the three environments share a failure mechanism.

## A second layer: the environment × tuple matrix

Within each environment, cases are organized by difficulty tuples. The archive includes a matrix with one row per environment × tuple: **340 rows** in total. Each environment has between 4 and 15 rows, and six environments have more than 10.

![Grid of 340 environment by difficulty-tuple rows coloured by pass rate](../figures/fig10_tuple_matrix.svg)
*Figure: Each square is one environment × difficulty-tuple row, coloured by its pass rate; grey marks rows with no scored case, and a number marks rows holding more than one case. Most rows hold a single case, so most squares are 0 or 1. The fractional values appear only in moco. The tuples carry environment-specific labels, so columns are not comparable across environments.*

There are **34 difficulty dimension names** across the matrix. The tuples are specific to each environment. A dimension in one environment is not calibrated against a dimension in another. For that reason, I do not pool, rank, or regress tuples across environments, and I do not read any tuple-level pattern as a difficulty effect.

The matrix contains four main facts:

- **Most rows hold a single case.** 296 of 340 rows contain one case. The 44 multi-case rows are all in four environments: `moco` (15 rows, 55 cases), `glyph` (12 rows, 24 cases), `css_state_machine` (9 rows, 18 cases), and `epistemic_games` (8 rows, 23 cases).
- **Most row outcomes are binary.** 329 rows have a pass rate, and 320 of those (97.3%) are exactly 0 or 1. The nine fractional rows are all in `moco`. Since most rows hold one case, a rate of 0 or 1 is mostly unavoidable. It is not evidence of sharp tuple boundaries.
- **Many rows sit in uniform environments.** 204 of 340 rows (60%) belong to environments where every scored row has the same outcome. Adding the 10 rows of the two environments with no scored case gives 214 (63%), but those rows have no outcome, so I do not count them as uniform behaviour.
- **Zero-pass tuples are widespread.** 98 individual tuples have no passes, and they occur in 19 environments. That is far more than the seven environments with no passes at all. All 12 mixed environments contain at least one zero-pass tuple.

This layer is exploratory. It shows how the cases are arranged, but it does not explain why any tuple passed or failed.

## What a "cell" means

The campaign describes its design as "one seed per cell," and that wording is ambiguous. The `seed` column of the per-case records is 0 for all 416 selected cases, and no second-seed rerun is recorded. If a cell meant a single case, the phrase would add nothing. The row counts suggest the intended meaning: 340 rows hold 416 cases, and 44 rows hold more than one case, all at seed 0. So a cell most plausibly means an environment × tuple row. That is my inference from the arithmetic. The archive does not state it as a convention.

Either way, the 405 scored cases are not 405 distinct tuples, and they are certainly not 405 independent tests of a general ability. `moco` alone supplies 55 scored cases (13.6% of all scored cases) from 15 tuples. The aggregates cannot estimate how correlated cases within a tuple are. In `moco`, the only environment whose multi-case rows disagree, there is no row-by-row key. In `glyph`, `css_state_machine` and `epistemic_games`, every multi-case row is unanimous, which is consistent with strong within-row agreement but does not establish it.

Because case density is uneven, a few environments pull hard on the global average:

| Scenario | Pass rate | Change |
|---|---:|---:|
| Exclude `moco` | 241/350 = 68.86% | +0.46 pt |
| Exclude `glyph` | 277/381 = 72.70% | +4.31 pt |
| Exclude both | 241/326 = 73.93% | — |
| Shrink `moco` to 9 cases at its own 65.5% rate | about 68.8% | about +0.4 pt |

These are arithmetic sensitivities, not alternative results. Weighting environments equally does not settle the question either. The unweighted mean (about 69.2%) lands close to the case-weighted rate, while the median (88.9%) hides the seven all-fail environments.

## `moco`: the only fractional rows

`moco` is the only environment whose rows are not all 0 or 1. Of its 15 rows, 6 sit at 0.0 or 1.0, and the other 9 are fractional. The fractional values that appear are 1/6, 1/3, 2/5, 2/3, 3/4, and 5/6.

The archive has no row-by-row key linking each value to its tuple. I therefore cannot draw the shape of `moco` across its difficulty dimensions. I can say that its 36/55 is spread across both endpoint rows and fractional rows. I cannot say how that spread lines up with any dimension.

## Claims withdrawn or left open

**Withdrawn:** An earlier claim of non-monotonic difficulty in `css_state_machine`. That environment is 18/18, so every one of its nine tuple rows is 2/2. There is no variation in it to describe.

**Open, not findings:** Possible non-monotonic patterns in `moco` and in a SQL environment. With a single seed and mostly binary rows, patterns like these can arise by chance. I have not computed how often they would appear by chance, so I treat them as questions, not results.

## Unscored cases are not failures

The 11 cases with no scored result are:

- 6 in `epistemic_silence`
- 4 in `epistemic_type_games`
- 1 in `rd_adaptive_halting`

The first two environments have no scored case at all, which is why the scored-environment count drops from 38 to 36. The unscored `rd_adaptive_halting` case sits at the tuple where all five dimensions are `easy`. The archive records no cause for the gap, and that tuple label does not make the case evidence about difficulty.

Recoding these 11 cases as failures would put invented outcomes into the denominator. The scored pass rate stays at 277/405. The all-selected figure, 277/416, answers a different question. `rd_adaptive_halting` remains 8/14 scored plus one unscored case. It is not a 15-case judgment with an assumed failure.

## Ten zero-pass environments or seven?

An earlier project summary says there are 10 zero-pass environments. The environment-level count gives 7. I tested one possible explanation: counting environments with at least one zero-pass tuple. That gives 19, so it does not reproduce 10 either. I do not know where the 10 comes from. Two readings are untested. Seven all-fail environments plus the two with no scored case give 9. Adding `rope`, which has no row in the 38-environment tables and whose 10 cases were all omitted before scoring, gives 10 only if `rope` is counted as zero-pass. Its cases were never scored, so that count would not mean the same thing as the others. I use 7 in this article, and the reconciliation remains open.

## What can a FAIL label explain?

The archive assigns these labels to the 128 FAIL outcomes:

![Horizontal bar chart of recorded failure labels across all environments](../figures/fig11_failure_labels.svg)
*Figure: Recorded failure labels for all 128 FAIL outcomes combined. These are global counts. The per-environment breakdown is in the table below, built from the same per-case records.*

| Label | Count |
|---|---:|
| `underfit` | 51 |
| `overfit_visible_tests` | 49 |
| `runtime_error` | 11 |
| `source_invalid` | 9 |
| `invalid_action` | 5 |
| `training_failed` | 3 |
| **Total** | **128** |

The `runtime_error` count combines 9 cases recorded as `RUNTIME_ERROR` and 2 recorded as `runtime_error`. The archive normalises both spellings to one label, and I treat the casing difference as a data-quality artefact rather than two kinds of runtime failure.

These are recorded classifications, not observations of Mercury-2.5's internal reasoning. I cannot infer a mechanism from the label names.

The per-case records do carry the environment for each FAIL, so the labels can be broken down by environment. The breakdown is below. It is descriptive only, and it rests on the recorded labels.

| Environment | FAIL | Recorded labels |
|---|---:|---|
| `glyph` | 24 | overfit_visible_tests 22, underfit 1, invalid_action 1 |
| `moco` | 19 | overfit_visible_tests 16, training_failed 2, invalid_action 1 |
| `batchnorm_ema` | 13 | overfit_visible_tests 11, training_failed 1, invalid_action 1 |
| `functorial_augmentation` | 9 | underfit 6, runtime_error 3 |
| `monadic_reward` | 9 | source_invalid 8, invalid_action 1 |
| `sheaf_invariant_gluing` | 9 | underfit 9 |
| `sheaf_physical_constraints` | 9 | underfit 9 |
| `rd_adaptive_halting` | 6 | runtime_error 5, underfit 1 |
| `gnn_message_passing`, `regex_state_machine`, `ssm_parallel_scan`, `ts_one_step`, `ts_trajectory` | 4 each | underfit 17, invalid_action 1, runtime_error 2 |
| `tensor_functor`, `compositional_optimizer`, `equivariant_diagram`, `sheaf_schema_sync`, `sql_fixed_point`, `transformer_ssm_lift` | 3, 2, 2, 1, 1, 1 | underfit 8, runtime_error 1, source_invalid 1 |

The rows above sum to 128. Two patterns stand out. Most `glyph` and `moco` failures carry the overfit label, and the three `sheaf_*` environments with FAIL cases (`sheaf_invariant_gluing` 9, `sheaf_physical_constraints` 9, `sheaf_schema_sync` 1) carry only underfit labels. Both are descriptions of recorded labels. Neither shows why the cases failed.

Nine of the ten `rejected` cases carry the `source_invalid` label (eight in `monadic_reward`, one in `transformer_ssm_lift`). The tenth, in `batchnorm_ema`, carries a different label. The disposition and the label therefore overlap, but they are not the same field.

Judge guarantees add a second limit. Across the 416 selected cases, the campaign records **189 `behavioral_reference` and 227 `compile_only`** guarantees, and those totals include unscored cases. Each environment carries exactly one guarantee: 11 environments are `behavioral_reference` and 27 are `compile_only`. The guarantee is therefore fixed by environment, and I cannot separate a guarantee effect from an environment effect.

By guarantee, the scored results are: `behavioral_reference`, **141/189 (74.6%)** across 11 environments; `compile_only`, **136/216 (63.0%)** across 27 environments, with 11 further unscored cases. These two numbers differ, but the difference is confounded with which environments fall in each group. I do not read it as a judge effect. A PASS under one guarantee does not establish what a PASS under the other does. A PASS records only what that case's judge checked. It does not show that the model understood or solved the task.

## The selection frame

The 416 cases are themselves a selection. Before scoring, **80 cases** were omitted:

| Omission reason | Cases |
|---|---:|
| Intervention-twin omissions | 56 |
| Known-gate calibration failures | 14 |
| Unsupported input modality (all in the `rope` environment) | 10 |

`rope` appears in none of the 38-environment tables. All 10 of its cases were omitted before scoring. The provenance summary instead gives **24** known-gate omissions, which disagrees with the exclusion record's 14. The 14 is the figure that fits the 496-cell frame (56 + 14 + 10 = 80, and 416 + 80 = 496). With 24, the omissions would total 90 and the frame would need 506 design cells. So the 24 cannot coexist with the selection frame as reported, and I leave the conflict open rather than resolve it silently. I report both and do not resolve the conflict.

Three flags apply to cases inside the 416:

- **Ten scored FAIL cases carry the disposition `rejected`:** eight in `monadic_reward`, one in `batchnorm_ema`, and one in `transformer_ssm_lift`. The archive does not define "rejected." All ten stay in the 128 failures.
- **Nine scored FAIL cases carry the disposition `unscored`.** Their status is `scored` and their verdict is FAIL, so the disposition label conflicts with the rest of the record. They are `moco` 3, `batchnorm_ema` 1, `glyph` 1, `monadic_reward` 1, `regex_state_machine` 1, `ts_one_step` 1, and `ts_trajectory` 1. Their recorded labels are `invalid_action` 5, `training_failed` 2, and `runtime_error` 2. I keep them as scored FAILs in the 128. The archive does not define the disposition.
- **One PASS in `ts_parse_only` is marked performance-ineligible**, and its exclusion note contradicts its verdict. It stays in the 277.

## Confounds I cannot remove

- **Single seed.** Every selected case carries seed 0. I have no variance or stability estimate. A 5/9 in `regex_state_machine` might be typical or unusual, and the archive cannot tell which. The 12 mixed environments, which hold 40.7% of the scored cases, are especially exposed. The endpoints are not protected from this either.
- **Dirty source state.** The campaign's source repository was recorded as dirty. The exact working-tree state [m-word] for reproduction, so I cannot isolate the effect of uncommitted changes on any environment.
- **Selection.** Omissions before scoring, unscored cases, undefined rejections, and uneven case density all shape which outcomes enter the 405. The counts disagree in places (14 vs 24, 10 vs 7).

## What this supports, and what it does not

On this archived selection, Mercury-2.5 received **277 PASS judgments among 405 scored cases**. The judges recorded all-pass outcomes in 17 environments, all-fail outcomes in 7, mixed outcomes in 12, and no scored outcome in 2. Closely named environments sometimes landed far apart. At the tuple level, nearly all rows are binary and most hold a single case. Fractional rows occur only in `moco`.

This analysis does *not* show that environment identity matters more than difficulty, because there is no common difficulty scale to compare against. It does not show a difficulty effect or a ranking within environments. It does not identify a model-internal cause for `glyph` or `batchnorm_ema`. It does not tell us whether the endpoints would hold under other seeds, whether the guarantee contrast would survive if guarantees varied within environments (they do not in this archive), or whether the source state was clean. The breakdowns by environment, guarantee, and failure label now exist in the text. The next useful step is evidence the archive cannot give: repeated seeds within environments, so that endpoints can be tested for stability.

So I would keep **68.4%** as the answer to one precise question: *What fraction of scored, selected cases received PASS?* I would not let it stand alone as the campaign's outcome. The map beside it says more: the zeros, the all-pass environments, the 40.7% of scored cases in between, and the gaps and disagreements in the archive that limit what any single number can mean.

<END ARTICLE>

## Evidence packet — verbatim

The evidence packet is the only data source. It contains Tables A–D and Section E chart descriptions. Read the entire packet.

<BEGIN EVIDENCE PACKET>
# POST-02 redo — evidence packet for review

This packet is the only data source for the evidence review. It is generated by `evidence/build_review_packet.py` from the four tables below. Values are copied verbatim. Long free-text fields and case IDs are omitted. Case rows are numbered 1 to 416 in source order. Matrix rows are referenced as `environment#k`, where k numbers the rows of that environment in source order. Section E describes each article chart in text.

Source tables and their SHA-256 hashes (of the full source files, not of this packet):

- `evidence/generated/case_results.csv`: `88bc8fab7f16d494032a81b01fe8ad6d56e71bbf72a17658b2e7caba45bbd567`
- `evidence/generated/campaign_exclusions.csv`: `23629f5b7133631eaeccf654134cdaea6a2e71451f7fb8c19f90a706d828efaa`
- `evidence/generated2/environment_difficulty_matrix.csv`: `a028535fb58dd40d240bd376fd4de3322c08cfa546b03df6c7c16c238827569e`
- `evidence/generated2/environment_summary_v2.csv`: `a4241adbea4653c08366d567b05a2cdcbd669b67f277551225412ea3e42f3082`

## Table A — environment summary (38 environments)

| environment | n_tuples | n_cases | n_scored | n_pass | n_fail | pass_rate |
|---|---|---|---|---|---|---|
| architecture_naturality | 9 | 9 | 9 | 9 | 0 | 1.0 |
| batchnorm_ema | 15 | 15 | 15 | 2 | 13 | 0.13333333333333333 |
| categorical_lenses | 9 | 9 | 9 | 9 | 0 | 1.0 |
| ci_dependency_graph | 9 | 9 | 9 | 9 | 0 | 1.0 |
| compositional_optimizer | 9 | 9 | 9 | 7 | 2 | 0.7777777777777778 |
| css_state_machine | 9 | 18 | 18 | 18 | 0 | 1.0 |
| epistemic_announcements | 6 | 6 | 6 | 6 | 0 | 1.0 |
| epistemic_fragmented_observation | 4 | 4 | 4 | 4 | 0 | 1.0 |
| epistemic_games | 8 | 23 | 23 | 23 | 0 | 1.0 |
| epistemic_nested_knowledge | 6 | 6 | 6 | 6 | 0 | 1.0 |
| epistemic_silence | 6 | 6 | 0 | 0 | 0 |  |
| epistemic_type_games | 4 | 4 | 0 | 0 | 0 |  |
| equivariant_diagram | 9 | 9 | 9 | 7 | 2 | 0.7777777777777778 |
| functorial_augmentation | 9 | 9 | 9 | 0 | 9 | 0.0 |
| glyph | 12 | 24 | 24 | 0 | 24 | 0.0 |
| gnn_message_passing | 9 | 9 | 9 | 5 | 4 | 0.5555555555555556 |
| moco | 15 | 55 | 55 | 36 | 19 | 0.6545454545454545 |
| monadic_reward | 9 | 9 | 9 | 0 | 9 | 0.0 |
| neuro_symbolic_parser | 9 | 9 | 9 | 9 | 0 | 1.0 |
| rd_adaptive_halting | 15 | 15 | 14 | 8 | 6 | 0.5714285714285714 |
| rd_gradient_credit | 15 | 15 | 15 | 15 | 0 | 1.0 |
| rd_state_carry | 15 | 15 | 15 | 15 | 0 | 1.0 |
| regex_state_machine | 9 | 9 | 9 | 5 | 4 | 0.5555555555555556 |
| semiring_unification | 9 | 9 | 9 | 9 | 0 | 1.0 |
| sheaf_invariant_gluing | 9 | 9 | 9 | 0 | 9 | 0.0 |
| sheaf_physical_constraints | 9 | 9 | 9 | 0 | 9 | 0.0 |
| sheaf_schema_sync | 9 | 9 | 9 | 8 | 1 | 0.8888888888888888 |
| spreadsheet_dataflow | 9 | 9 | 9 | 9 | 0 | 1.0 |
| sql_fixed_point | 9 | 9 | 9 | 8 | 1 | 0.8888888888888888 |
| ssm_parallel_scan | 9 | 9 | 9 | 5 | 4 | 0.5555555555555556 |
| stochastic_monad | 9 | 9 | 9 | 9 | 0 | 1.0 |
| template_interpreter | 9 | 9 | 9 | 9 | 0 | 1.0 |
| tensor_functor | 9 | 9 | 9 | 6 | 3 | 0.6666666666666666 |
| tokenizer_adjunction | 9 | 9 | 9 | 9 | 0 | 1.0 |
| transformer_ssm_lift | 9 | 9 | 9 | 8 | 1 | 0.8888888888888888 |
| ts_one_step | 4 | 4 | 4 | 0 | 4 | 0.0 |
| ts_parse_only | 4 | 4 | 4 | 4 | 0 | 1.0 |
| ts_trajectory | 4 | 4 | 4 | 0 | 4 | 0.0 |

## Table B — selected cases (416 rows)

Fields: status, verdict, seed, judge_guarantee, failure_mode_normalized, failure_mode_raw, case_disposition, performance_eligible, environment.

| row | environment | status | verdict | seed | judge_guarantee | failure_mode_normalized | failure_mode_raw | case_disposition | performance_eligible |
|---|---|---|---|---|---|---|---|---|---|
| 1 | architecture_naturality | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 2 | architecture_naturality | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 3 | architecture_naturality | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 4 | architecture_naturality | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 5 | architecture_naturality | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 6 | architecture_naturality | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 7 | architecture_naturality | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 8 | architecture_naturality | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 9 | architecture_naturality | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 10 | batchnorm_ema | scored | FAIL | 0 | compile_only | overfit_visible_tests | overfit_visible_tests | scored | True |
| 11 | batchnorm_ema | scored | FAIL | 0 | compile_only | overfit_visible_tests | overfit_visible_tests | scored | True |
| 12 | batchnorm_ema | scored | FAIL | 0 | compile_only | overfit_visible_tests | overfit_visible_tests | scored | True |
| 13 | batchnorm_ema | scored | FAIL | 0 | compile_only | overfit_visible_tests | overfit_visible_tests | scored | True |
| 14 | batchnorm_ema | scored | FAIL | 0 | compile_only | overfit_visible_tests | overfit_visible_tests | scored | True |
| 15 | batchnorm_ema | scored | FAIL | 0 | compile_only | overfit_visible_tests | overfit_visible_tests | scored | True |
| 16 | batchnorm_ema | scored | FAIL | 0 | compile_only | overfit_visible_tests | overfit_visible_tests | scored | True |
| 17 | batchnorm_ema | scored | FAIL | 0 | compile_only | overfit_visible_tests | overfit_visible_tests | scored | True |
| 18 | batchnorm_ema | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 19 | batchnorm_ema | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 20 | batchnorm_ema | scored | FAIL | 0 | compile_only | training_failed | training_failed | rejected | True |
| 21 | batchnorm_ema | scored | FAIL | 0 | compile_only | overfit_visible_tests | overfit_visible_tests | scored | True |
| 22 | batchnorm_ema | scored | FAIL | 0 | compile_only | overfit_visible_tests | overfit_visible_tests | scored | True |
| 23 | batchnorm_ema | scored | FAIL | 0 | compile_only | overfit_visible_tests | overfit_visible_tests | scored | True |
| 24 | batchnorm_ema | scored | FAIL | 0 | compile_only | invalid_action | invalid_action | unscored | True |
| 25 | categorical_lenses | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 26 | categorical_lenses | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 27 | categorical_lenses | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 28 | categorical_lenses | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 29 | categorical_lenses | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 30 | categorical_lenses | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 31 | categorical_lenses | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 32 | categorical_lenses | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 33 | categorical_lenses | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 34 | ci_dependency_graph | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 35 | ci_dependency_graph | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 36 | ci_dependency_graph | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 37 | ci_dependency_graph | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 38 | ci_dependency_graph | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 39 | ci_dependency_graph | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 40 | ci_dependency_graph | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 41 | ci_dependency_graph | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 42 | ci_dependency_graph | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 43 | compositional_optimizer | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 44 | compositional_optimizer | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 45 | compositional_optimizer | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 46 | compositional_optimizer | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 47 | compositional_optimizer | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 48 | compositional_optimizer | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 49 | compositional_optimizer | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 50 | compositional_optimizer | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 51 | compositional_optimizer | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 52 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 53 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 54 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 55 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 56 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 57 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 58 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 59 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 60 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 61 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 62 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 63 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 64 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 65 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 66 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 67 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 68 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 69 | css_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 70 | epistemic_announcements | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 71 | epistemic_announcements | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 72 | epistemic_announcements | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 73 | epistemic_announcements | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 74 | epistemic_announcements | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 75 | epistemic_announcements | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 76 | epistemic_fragmented_observation | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 77 | epistemic_fragmented_observation | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 78 | epistemic_fragmented_observation | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 79 | epistemic_fragmented_observation | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 80 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 81 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 82 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 83 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 84 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 85 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 86 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 87 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 88 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 89 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 90 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 91 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 92 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 93 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 94 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 95 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 96 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 97 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 98 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 99 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 100 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 101 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 102 | epistemic_games | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 103 | epistemic_nested_knowledge | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 104 | epistemic_nested_knowledge | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 105 | epistemic_nested_knowledge | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 106 | epistemic_nested_knowledge | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 107 | epistemic_nested_knowledge | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 108 | epistemic_nested_knowledge | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 109 | epistemic_silence | infrastructure_unscored |  | 0 | compile_only | unknown |  |  | False |
| 110 | epistemic_silence | infrastructure_unscored |  | 0 | compile_only | unknown |  |  | False |
| 111 | epistemic_silence | infrastructure_unscored |  | 0 | compile_only | unknown |  |  | False |
| 112 | epistemic_silence | infrastructure_unscored |  | 0 | compile_only | unknown |  |  | False |
| 113 | epistemic_silence | infrastructure_unscored |  | 0 | compile_only | unknown |  |  | False |
| 114 | epistemic_silence | infrastructure_unscored |  | 0 | compile_only | unknown |  |  | False |
| 115 | epistemic_type_games | infrastructure_unscored |  | 0 | compile_only | unknown |  |  | False |
| 116 | epistemic_type_games | infrastructure_unscored |  | 0 | compile_only | unknown |  |  | False |
| 117 | epistemic_type_games | infrastructure_unscored |  | 0 | compile_only | unknown |  |  | False |
| 118 | epistemic_type_games | infrastructure_unscored |  | 0 | compile_only | unknown |  |  | False |
| 119 | equivariant_diagram | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 120 | equivariant_diagram | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 121 | equivariant_diagram | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 122 | equivariant_diagram | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 123 | equivariant_diagram | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 124 | equivariant_diagram | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 125 | equivariant_diagram | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 126 | equivariant_diagram | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 127 | equivariant_diagram | scored | FAIL | 0 | compile_only | runtime_error | RUNTIME_ERROR | scored | True |
| 128 | functorial_augmentation | scored | FAIL | 0 | compile_only | runtime_error | RUNTIME_ERROR | scored | True |
| 129 | functorial_augmentation | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 130 | functorial_augmentation | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 131 | functorial_augmentation | scored | FAIL | 0 | compile_only | runtime_error | RUNTIME_ERROR | scored | True |
| 132 | functorial_augmentation | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 133 | functorial_augmentation | scored | FAIL | 0 | compile_only | runtime_error | RUNTIME_ERROR | scored | True |
| 134 | functorial_augmentation | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 135 | functorial_augmentation | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 136 | functorial_augmentation | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 137 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 138 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 139 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 140 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 141 | glyph | scored | FAIL | 0 | behavioral_reference | underfit | underfit | scored | True |
| 142 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 143 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 144 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 145 | glyph | scored | FAIL | 0 | behavioral_reference | invalid_action | invalid_action | unscored | True |
| 146 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 147 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 148 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 149 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 150 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 151 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 152 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 153 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 154 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 155 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 156 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 157 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 158 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 159 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 160 | glyph | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 161 | gnn_message_passing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 162 | gnn_message_passing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 163 | gnn_message_passing | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 164 | gnn_message_passing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 165 | gnn_message_passing | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 166 | gnn_message_passing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 167 | gnn_message_passing | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 168 | gnn_message_passing | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 169 | gnn_message_passing | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 170 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 171 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 172 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 173 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 174 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 175 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 176 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 177 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 178 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 179 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 180 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 181 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 182 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 183 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 184 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 185 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 186 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 187 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 188 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 189 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 190 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 191 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 192 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 193 | moco | scored | FAIL | 0 | behavioral_reference | training_failed | training_failed | unscored | True |
| 194 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 195 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 196 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 197 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 198 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 199 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 200 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 201 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 202 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 203 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 204 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 205 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 206 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 207 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 208 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 209 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 210 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 211 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 212 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 213 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 214 | moco | scored | FAIL | 0 | behavioral_reference | training_failed | training_failed | unscored | True |
| 215 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 216 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 217 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 218 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 219 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 220 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 221 | moco | scored | FAIL | 0 | behavioral_reference | overfit_visible_tests | overfit_visible_tests | scored | True |
| 222 | moco | scored | FAIL | 0 | behavioral_reference | invalid_action | invalid_action | unscored | True |
| 223 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 224 | moco | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 225 | monadic_reward | scored | FAIL | 0 | compile_only | source_invalid | source_invalid | rejected | True |
| 226 | monadic_reward | scored | FAIL | 0 | compile_only | source_invalid | source_invalid | rejected | True |
| 227 | monadic_reward | scored | FAIL | 0 | compile_only | source_invalid | source_invalid | rejected | True |
| 228 | monadic_reward | scored | FAIL | 0 | compile_only | source_invalid | source_invalid | rejected | True |
| 229 | monadic_reward | scored | FAIL | 0 | compile_only | source_invalid | source_invalid | rejected | True |
| 230 | monadic_reward | scored | FAIL | 0 | compile_only | source_invalid | source_invalid | rejected | True |
| 231 | monadic_reward | scored | FAIL | 0 | compile_only | source_invalid | source_invalid | rejected | True |
| 232 | monadic_reward | scored | FAIL | 0 | compile_only | invalid_action | invalid_action | unscored | True |
| 233 | monadic_reward | scored | FAIL | 0 | compile_only | source_invalid | source_invalid | rejected | True |
| 234 | neuro_symbolic_parser | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 235 | neuro_symbolic_parser | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 236 | neuro_symbolic_parser | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 237 | neuro_symbolic_parser | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 238 | neuro_symbolic_parser | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 239 | neuro_symbolic_parser | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 240 | neuro_symbolic_parser | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 241 | neuro_symbolic_parser | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 242 | neuro_symbolic_parser | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 243 | rd_adaptive_halting | infrastructure_unscored |  | 0 | compile_only | unknown |  |  | False |
| 244 | rd_adaptive_halting | scored | FAIL | 0 | compile_only | runtime_error | RUNTIME_ERROR | scored | True |
| 245 | rd_adaptive_halting | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 246 | rd_adaptive_halting | scored | FAIL | 0 | compile_only | runtime_error | RUNTIME_ERROR | scored | True |
| 247 | rd_adaptive_halting | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 248 | rd_adaptive_halting | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 249 | rd_adaptive_halting | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 250 | rd_adaptive_halting | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 251 | rd_adaptive_halting | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 252 | rd_adaptive_halting | scored | FAIL | 0 | compile_only | runtime_error | RUNTIME_ERROR | scored | True |
| 253 | rd_adaptive_halting | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 254 | rd_adaptive_halting | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 255 | rd_adaptive_halting | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 256 | rd_adaptive_halting | scored | FAIL | 0 | compile_only | runtime_error | RUNTIME_ERROR | scored | True |
| 257 | rd_adaptive_halting | scored | FAIL | 0 | compile_only | runtime_error | RUNTIME_ERROR | scored | True |
| 258 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 259 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 260 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 261 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 262 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 263 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 264 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 265 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 266 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 267 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 268 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 269 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 270 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 271 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 272 | rd_gradient_credit | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 273 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 274 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 275 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 276 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 277 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 278 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 279 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 280 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 281 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 282 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 283 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 284 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 285 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 286 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 287 | rd_state_carry | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 288 | regex_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 289 | regex_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 290 | regex_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 291 | regex_state_machine | scored | FAIL | 0 | behavioral_reference | underfit | underfit | scored | True |
| 292 | regex_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 293 | regex_state_machine | scored | FAIL | 0 | behavioral_reference | invalid_action | invalid_action | unscored | True |
| 294 | regex_state_machine | scored | FAIL | 0 | behavioral_reference | underfit | underfit | scored | True |
| 295 | regex_state_machine | scored | FAIL | 0 | behavioral_reference | underfit | underfit | scored | True |
| 296 | regex_state_machine | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 297 | semiring_unification | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 298 | semiring_unification | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 299 | semiring_unification | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 300 | semiring_unification | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 301 | semiring_unification | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 302 | semiring_unification | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 303 | semiring_unification | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 304 | semiring_unification | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 305 | semiring_unification | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 306 | sheaf_invariant_gluing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 307 | sheaf_invariant_gluing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 308 | sheaf_invariant_gluing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 309 | sheaf_invariant_gluing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 310 | sheaf_invariant_gluing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 311 | sheaf_invariant_gluing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 312 | sheaf_invariant_gluing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 313 | sheaf_invariant_gluing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 314 | sheaf_invariant_gluing | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 315 | sheaf_physical_constraints | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 316 | sheaf_physical_constraints | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 317 | sheaf_physical_constraints | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 318 | sheaf_physical_constraints | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 319 | sheaf_physical_constraints | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 320 | sheaf_physical_constraints | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 321 | sheaf_physical_constraints | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 322 | sheaf_physical_constraints | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 323 | sheaf_physical_constraints | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 324 | sheaf_schema_sync | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 325 | sheaf_schema_sync | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 326 | sheaf_schema_sync | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 327 | sheaf_schema_sync | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 328 | sheaf_schema_sync | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 329 | sheaf_schema_sync | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 330 | sheaf_schema_sync | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 331 | sheaf_schema_sync | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 332 | sheaf_schema_sync | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 333 | spreadsheet_dataflow | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 334 | spreadsheet_dataflow | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 335 | spreadsheet_dataflow | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 336 | spreadsheet_dataflow | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 337 | spreadsheet_dataflow | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 338 | spreadsheet_dataflow | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 339 | spreadsheet_dataflow | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 340 | spreadsheet_dataflow | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 341 | spreadsheet_dataflow | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 342 | sql_fixed_point | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 343 | sql_fixed_point | scored | FAIL | 0 | behavioral_reference | underfit | underfit | scored | True |
| 344 | sql_fixed_point | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 345 | sql_fixed_point | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 346 | sql_fixed_point | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 347 | sql_fixed_point | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 348 | sql_fixed_point | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 349 | sql_fixed_point | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 350 | sql_fixed_point | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 351 | ssm_parallel_scan | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 352 | ssm_parallel_scan | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 353 | ssm_parallel_scan | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 354 | ssm_parallel_scan | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 355 | ssm_parallel_scan | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 356 | ssm_parallel_scan | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 357 | ssm_parallel_scan | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 358 | ssm_parallel_scan | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 359 | ssm_parallel_scan | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 360 | stochastic_monad | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 361 | stochastic_monad | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 362 | stochastic_monad | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 363 | stochastic_monad | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 364 | stochastic_monad | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 365 | stochastic_monad | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 366 | stochastic_monad | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 367 | stochastic_monad | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 368 | stochastic_monad | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 369 | template_interpreter | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 370 | template_interpreter | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 371 | template_interpreter | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 372 | template_interpreter | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 373 | template_interpreter | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 374 | template_interpreter | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 375 | template_interpreter | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 376 | template_interpreter | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 377 | template_interpreter | scored | PASS | 0 | behavioral_reference | pass | pass | scored | True |
| 378 | tensor_functor | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 379 | tensor_functor | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 380 | tensor_functor | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 381 | tensor_functor | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 382 | tensor_functor | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 383 | tensor_functor | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 384 | tensor_functor | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 385 | tensor_functor | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 386 | tensor_functor | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 387 | tokenizer_adjunction | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 388 | tokenizer_adjunction | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 389 | tokenizer_adjunction | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 390 | tokenizer_adjunction | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 391 | tokenizer_adjunction | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 392 | tokenizer_adjunction | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 393 | tokenizer_adjunction | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 394 | tokenizer_adjunction | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 395 | tokenizer_adjunction | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 396 | transformer_ssm_lift | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 397 | transformer_ssm_lift | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 398 | transformer_ssm_lift | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 399 | transformer_ssm_lift | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 400 | transformer_ssm_lift | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 401 | transformer_ssm_lift | scored | FAIL | 0 | compile_only | source_invalid | source_invalid | rejected | True |
| 402 | transformer_ssm_lift | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 403 | transformer_ssm_lift | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 404 | transformer_ssm_lift | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 405 | ts_one_step | scored | FAIL | 0 | compile_only | runtime_error | runtime_error | unscored | True |
| 406 | ts_one_step | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 407 | ts_one_step | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 408 | ts_one_step | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 409 | ts_parse_only | scored | PASS | 0 | compile_only | pass | pass | scored | False |
| 410 | ts_parse_only | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 411 | ts_parse_only | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 412 | ts_parse_only | scored | PASS | 0 | compile_only | pass | pass | scored | True |
| 413 | ts_trajectory | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 414 | ts_trajectory | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |
| 415 | ts_trajectory | scored | FAIL | 0 | compile_only | runtime_error | runtime_error | unscored | True |
| 416 | ts_trajectory | scored | FAIL | 0 | compile_only | underfit | underfit | scored | True |

## Table C — pre-scoring omissions (80 rows)

Fields: environment and exclusion_class.

| row | environment | exclusion_class |
|---|---|---|
| 1 | rope | unsupported_provider_input_modality |
| 2 | rope | unsupported_provider_input_modality |
| 3 | rope | unsupported_provider_input_modality |
| 4 | rope | unsupported_provider_input_modality |
| 5 | rope | unsupported_provider_input_modality |
| 6 | rope | unsupported_provider_input_modality |
| 7 | rope | unsupported_provider_input_modality |
| 8 | rope | unsupported_provider_input_modality |
| 9 | rope | unsupported_provider_input_modality |
| 10 | rope | unsupported_provider_input_modality |
| 11 | glyph | known_gate_calibration_failure |
| 12 | glyph | known_gate_calibration_failure |
| 13 | glyph | known_gate_calibration_failure |
| 14 | glyph | known_gate_calibration_failure |
| 15 | glyph | known_gate_calibration_failure |
| 16 | glyph | known_gate_calibration_failure |
| 17 | glyph | known_gate_calibration_failure |
| 18 | glyph | known_gate_calibration_failure |
| 19 | glyph | known_gate_calibration_failure |
| 20 | rope | known_gate_calibration_failure |
| 21 | rope | known_gate_calibration_failure |
| 22 | rope | known_gate_calibration_failure |
| 23 | rope | known_gate_calibration_failure |
| 24 | rope | known_gate_calibration_failure |
| 25 | epistemic_games | intervention_twin_omission |
| 26 | epistemic_games | intervention_twin_omission |
| 27 | epistemic_games | intervention_twin_omission |
| 28 | epistemic_games | intervention_twin_omission |
| 29 | epistemic_games | intervention_twin_omission |
| 30 | epistemic_games | intervention_twin_omission |
| 31 | epistemic_games | intervention_twin_omission |
| 32 | epistemic_games | intervention_twin_omission |
| 33 | epistemic_games | intervention_twin_omission |
| 34 | glyph | intervention_twin_omission |
| 35 | glyph | intervention_twin_omission |
| 36 | glyph | intervention_twin_omission |
| 37 | glyph | intervention_twin_omission |
| 38 | glyph | intervention_twin_omission |
| 39 | glyph | intervention_twin_omission |
| 40 | glyph | intervention_twin_omission |
| 41 | glyph | intervention_twin_omission |
| 42 | glyph | intervention_twin_omission |
| 43 | glyph | intervention_twin_omission |
| 44 | glyph | intervention_twin_omission |
| 45 | glyph | intervention_twin_omission |
| 46 | moco | intervention_twin_omission |
| 47 | moco | intervention_twin_omission |
| 48 | moco | intervention_twin_omission |
| 49 | moco | intervention_twin_omission |
| 50 | moco | intervention_twin_omission |
| 51 | moco | intervention_twin_omission |
| 52 | moco | intervention_twin_omission |
| 53 | moco | intervention_twin_omission |
| 54 | moco | intervention_twin_omission |
| 55 | moco | intervention_twin_omission |
| 56 | moco | intervention_twin_omission |
| 57 | moco | intervention_twin_omission |
| 58 | moco | intervention_twin_omission |
| 59 | moco | intervention_twin_omission |
| 60 | moco | intervention_twin_omission |
| 61 | moco | intervention_twin_omission |
| 62 | moco | intervention_twin_omission |
| 63 | moco | intervention_twin_omission |
| 64 | moco | intervention_twin_omission |
| 65 | moco | intervention_twin_omission |
| 66 | moco | intervention_twin_omission |
| 67 | moco | intervention_twin_omission |
| 68 | moco | intervention_twin_omission |
| 69 | moco | intervention_twin_omission |
| 70 | moco | intervention_twin_omission |
| 71 | moco | intervention_twin_omission |
| 72 | moco | intervention_twin_omission |
| 73 | moco | intervention_twin_omission |
| 74 | moco | intervention_twin_omission |
| 75 | moco | intervention_twin_omission |
| 76 | moco | intervention_twin_omission |
| 77 | moco | intervention_twin_omission |
| 78 | moco | intervention_twin_omission |
| 79 | moco | intervention_twin_omission |
| 80 | moco | intervention_twin_omission |

## Table D — environment × difficulty-tuple matrix (340 rows)

Fields: environment, k (row number within environment), n_dims (number of difficulty keys in the tuple), n_cases, n_scored, n_unscored, n_pass, n_fail, pass_rate, failure_modes, judge_guarantees.

| environment | k | n_dims | n_cases | n_scored | n_unscored | n_pass | n_fail | pass_rate | failure_modes | judge_guarantees |
|---|---|---|---|---|---|---|---|---|---|---|
| architecture_naturality | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| architecture_naturality | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| architecture_naturality | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| architecture_naturality | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| architecture_naturality | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| architecture_naturality | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| architecture_naturality | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| architecture_naturality | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| architecture_naturality | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| batchnorm_ema | 1 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"overfit_visible_tests": 1} | {"compile_only": 1} |
| batchnorm_ema | 2 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"overfit_visible_tests": 1} | {"compile_only": 1} |
| batchnorm_ema | 3 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"overfit_visible_tests": 1} | {"compile_only": 1} |
| batchnorm_ema | 4 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"training_failed": 1} | {"compile_only": 1} |
| batchnorm_ema | 5 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"overfit_visible_tests": 1} | {"compile_only": 1} |
| batchnorm_ema | 6 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"overfit_visible_tests": 1} | {"compile_only": 1} |
| batchnorm_ema | 7 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"overfit_visible_tests": 1} | {"compile_only": 1} |
| batchnorm_ema | 8 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"overfit_visible_tests": 1} | {"compile_only": 1} |
| batchnorm_ema | 9 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"overfit_visible_tests": 1} | {"compile_only": 1} |
| batchnorm_ema | 10 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"overfit_visible_tests": 1} | {"compile_only": 1} |
| batchnorm_ema | 11 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"overfit_visible_tests": 1} | {"compile_only": 1} |
| batchnorm_ema | 12 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"overfit_visible_tests": 1} | {"compile_only": 1} |
| batchnorm_ema | 13 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| batchnorm_ema | 14 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| batchnorm_ema | 15 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"invalid_action": 1} | {"compile_only": 1} |
| categorical_lenses | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| categorical_lenses | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| categorical_lenses | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| categorical_lenses | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| categorical_lenses | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| categorical_lenses | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| categorical_lenses | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| categorical_lenses | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| categorical_lenses | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| ci_dependency_graph | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| ci_dependency_graph | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| ci_dependency_graph | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| ci_dependency_graph | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| ci_dependency_graph | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| ci_dependency_graph | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| ci_dependency_graph | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| ci_dependency_graph | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| ci_dependency_graph | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| compositional_optimizer | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| compositional_optimizer | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| compositional_optimizer | 3 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| compositional_optimizer | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| compositional_optimizer | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| compositional_optimizer | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| compositional_optimizer | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| compositional_optimizer | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| compositional_optimizer | 9 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| css_state_machine | 1 | 2 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| css_state_machine | 2 | 2 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| css_state_machine | 3 | 2 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| css_state_machine | 4 | 2 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| css_state_machine | 5 | 2 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| css_state_machine | 6 | 2 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| css_state_machine | 7 | 2 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| css_state_machine | 8 | 2 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| css_state_machine | 9 | 2 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| epistemic_announcements | 1 | 4 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_announcements | 2 | 4 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_announcements | 3 | 4 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_announcements | 4 | 4 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_announcements | 5 | 4 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_announcements | 6 | 4 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_fragmented_observation | 1 | 3 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_fragmented_observation | 2 | 3 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_fragmented_observation | 3 | 3 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_fragmented_observation | 4 | 3 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_games | 1 | 5 | 3 | 3 | 0 | 3 | 0 | 1.0 | {} | {"behavioral_reference": 3} |
| epistemic_games | 2 | 5 | 3 | 3 | 0 | 3 | 0 | 1.0 | {} | {"behavioral_reference": 3} |
| epistemic_games | 3 | 5 | 4 | 4 | 0 | 4 | 0 | 1.0 | {} | {"behavioral_reference": 4} |
| epistemic_games | 4 | 5 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| epistemic_games | 5 | 5 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| epistemic_games | 6 | 5 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| epistemic_games | 7 | 5 | 4 | 4 | 0 | 4 | 0 | 1.0 | {} | {"behavioral_reference": 4} |
| epistemic_games | 8 | 5 | 3 | 3 | 0 | 3 | 0 | 1.0 | {} | {"behavioral_reference": 3} |
| epistemic_nested_knowledge | 1 | 3 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_nested_knowledge | 2 | 3 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_nested_knowledge | 3 | 3 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_nested_knowledge | 4 | 3 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_nested_knowledge | 5 | 3 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_nested_knowledge | 6 | 3 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| epistemic_silence | 1 | 4 | 1 | 0 | 1 | 0 | 0 |  | {} | {"compile_only": 1} |
| epistemic_silence | 2 | 4 | 1 | 0 | 1 | 0 | 0 |  | {} | {"compile_only": 1} |
| epistemic_silence | 3 | 4 | 1 | 0 | 1 | 0 | 0 |  | {} | {"compile_only": 1} |
| epistemic_silence | 4 | 4 | 1 | 0 | 1 | 0 | 0 |  | {} | {"compile_only": 1} |
| epistemic_silence | 5 | 4 | 1 | 0 | 1 | 0 | 0 |  | {} | {"compile_only": 1} |
| epistemic_silence | 6 | 4 | 1 | 0 | 1 | 0 | 0 |  | {} | {"compile_only": 1} |
| epistemic_type_games | 1 | 3 | 1 | 0 | 1 | 0 | 0 |  | {} | {"compile_only": 1} |
| epistemic_type_games | 2 | 3 | 1 | 0 | 1 | 0 | 0 |  | {} | {"compile_only": 1} |
| epistemic_type_games | 3 | 3 | 1 | 0 | 1 | 0 | 0 |  | {} | {"compile_only": 1} |
| epistemic_type_games | 4 | 3 | 1 | 0 | 1 | 0 | 0 |  | {} | {"compile_only": 1} |
| equivariant_diagram | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| equivariant_diagram | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| equivariant_diagram | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| equivariant_diagram | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| equivariant_diagram | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| equivariant_diagram | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| equivariant_diagram | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| equivariant_diagram | 8 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| equivariant_diagram | 9 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"RUNTIME_ERROR": 1} | {"compile_only": 1} |
| functorial_augmentation | 1 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"RUNTIME_ERROR": 1} | {"compile_only": 1} |
| functorial_augmentation | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| functorial_augmentation | 3 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| functorial_augmentation | 4 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"RUNTIME_ERROR": 1} | {"compile_only": 1} |
| functorial_augmentation | 5 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| functorial_augmentation | 6 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"RUNTIME_ERROR": 1} | {"compile_only": 1} |
| functorial_augmentation | 7 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| functorial_augmentation | 8 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| functorial_augmentation | 9 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| glyph | 1 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"overfit_visible_tests": 2} | {"behavioral_reference": 2} |
| glyph | 2 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"overfit_visible_tests": 2} | {"behavioral_reference": 2} |
| glyph | 3 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"underfit": 1, "overfit_visible_tests": 1} | {"behavioral_reference": 2} |
| glyph | 4 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"overfit_visible_tests": 2} | {"behavioral_reference": 2} |
| glyph | 5 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"invalid_action": 1, "overfit_visible_tests": 1} | {"behavioral_reference": 2} |
| glyph | 6 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"overfit_visible_tests": 2} | {"behavioral_reference": 2} |
| glyph | 7 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"overfit_visible_tests": 2} | {"behavioral_reference": 2} |
| glyph | 8 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"overfit_visible_tests": 2} | {"behavioral_reference": 2} |
| glyph | 9 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"overfit_visible_tests": 2} | {"behavioral_reference": 2} |
| glyph | 10 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"overfit_visible_tests": 2} | {"behavioral_reference": 2} |
| glyph | 11 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"overfit_visible_tests": 2} | {"behavioral_reference": 2} |
| glyph | 12 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"overfit_visible_tests": 2} | {"behavioral_reference": 2} |
| gnn_message_passing | 1 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| gnn_message_passing | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| gnn_message_passing | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| gnn_message_passing | 4 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| gnn_message_passing | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| gnn_message_passing | 6 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| gnn_message_passing | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| gnn_message_passing | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| gnn_message_passing | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| moco | 1 | 6 | 6 | 6 | 0 | 4 | 2 | 0.6666666666666666 | {"overfit_visible_tests": 2} | {"behavioral_reference": 6} |
| moco | 2 | 6 | 3 | 3 | 0 | 2 | 1 | 0.6666666666666666 | {"overfit_visible_tests": 1} | {"behavioral_reference": 3} |
| moco | 3 | 6 | 3 | 3 | 0 | 3 | 0 | 1.0 | {} | {"behavioral_reference": 3} |
| moco | 4 | 6 | 6 | 6 | 0 | 5 | 1 | 0.8333333333333334 | {"training_failed": 1} | {"behavioral_reference": 6} |
| moco | 5 | 6 | 3 | 3 | 0 | 2 | 1 | 0.6666666666666666 | {"overfit_visible_tests": 1} | {"behavioral_reference": 3} |
| moco | 6 | 6 | 6 | 6 | 0 | 1 | 5 | 0.16666666666666666 | {"overfit_visible_tests": 5} | {"behavioral_reference": 6} |
| moco | 7 | 6 | 4 | 4 | 0 | 3 | 1 | 0.75 | {"overfit_visible_tests": 1} | {"behavioral_reference": 4} |
| moco | 8 | 6 | 5 | 5 | 0 | 2 | 3 | 0.4 | {"overfit_visible_tests": 3} | {"behavioral_reference": 5} |
| moco | 9 | 6 | 3 | 3 | 0 | 2 | 1 | 0.6666666666666666 | {"overfit_visible_tests": 1} | {"behavioral_reference": 3} |
| moco | 10 | 6 | 2 | 2 | 0 | 0 | 2 | 0.0 | {"training_failed": 1, "overfit_visible_tests": 1} | {"behavioral_reference": 2} |
| moco | 11 | 6 | 3 | 3 | 0 | 3 | 0 | 1.0 | {} | {"behavioral_reference": 3} |
| moco | 12 | 6 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| moco | 13 | 6 | 4 | 4 | 0 | 4 | 0 | 1.0 | {} | {"behavioral_reference": 4} |
| moco | 14 | 6 | 3 | 3 | 0 | 1 | 2 | 0.3333333333333333 | {"overfit_visible_tests": 1, "invalid_action": 1} | {"behavioral_reference": 3} |
| moco | 15 | 6 | 2 | 2 | 0 | 2 | 0 | 1.0 | {} | {"behavioral_reference": 2} |
| monadic_reward | 1 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"source_invalid": 1} | {"compile_only": 1} |
| monadic_reward | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"source_invalid": 1} | {"compile_only": 1} |
| monadic_reward | 3 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"source_invalid": 1} | {"compile_only": 1} |
| monadic_reward | 4 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"source_invalid": 1} | {"compile_only": 1} |
| monadic_reward | 5 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"source_invalid": 1} | {"compile_only": 1} |
| monadic_reward | 6 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"source_invalid": 1} | {"compile_only": 1} |
| monadic_reward | 7 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"source_invalid": 1} | {"compile_only": 1} |
| monadic_reward | 8 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"invalid_action": 1} | {"compile_only": 1} |
| monadic_reward | 9 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"source_invalid": 1} | {"compile_only": 1} |
| neuro_symbolic_parser | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| neuro_symbolic_parser | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| neuro_symbolic_parser | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| neuro_symbolic_parser | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| neuro_symbolic_parser | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| neuro_symbolic_parser | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| neuro_symbolic_parser | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| neuro_symbolic_parser | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| neuro_symbolic_parser | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_adaptive_halting | 1 | 5 | 1 | 0 | 1 | 0 | 0 |  | {} | {"compile_only": 1} |
| rd_adaptive_halting | 2 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_adaptive_halting | 3 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_adaptive_halting | 4 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"RUNTIME_ERROR": 1} | {"compile_only": 1} |
| rd_adaptive_halting | 5 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| rd_adaptive_halting | 6 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_adaptive_halting | 7 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"RUNTIME_ERROR": 1} | {"compile_only": 1} |
| rd_adaptive_halting | 8 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_adaptive_halting | 9 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"RUNTIME_ERROR": 1} | {"compile_only": 1} |
| rd_adaptive_halting | 10 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_adaptive_halting | 11 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_adaptive_halting | 12 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_adaptive_halting | 13 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"RUNTIME_ERROR": 1} | {"compile_only": 1} |
| rd_adaptive_halting | 14 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_adaptive_halting | 15 | 5 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"RUNTIME_ERROR": 1} | {"compile_only": 1} |
| rd_gradient_credit | 1 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 2 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 3 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 4 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 5 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 6 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 7 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 8 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 9 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 10 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 11 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 12 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 13 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 14 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_gradient_credit | 15 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| rd_state_carry | 1 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 2 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 3 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 4 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 5 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 6 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 7 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 8 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 9 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 10 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 11 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 12 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 13 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 14 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| rd_state_carry | 15 | 5 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| regex_state_machine | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| regex_state_machine | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"behavioral_reference": 1} |
| regex_state_machine | 3 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"behavioral_reference": 1} |
| regex_state_machine | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| regex_state_machine | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| regex_state_machine | 6 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"behavioral_reference": 1} |
| regex_state_machine | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| regex_state_machine | 8 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"invalid_action": 1} | {"behavioral_reference": 1} |
| regex_state_machine | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| semiring_unification | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| semiring_unification | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| semiring_unification | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| semiring_unification | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| semiring_unification | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| semiring_unification | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| semiring_unification | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| semiring_unification | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| semiring_unification | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| sheaf_invariant_gluing | 1 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_invariant_gluing | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_invariant_gluing | 3 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_invariant_gluing | 4 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_invariant_gluing | 5 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_invariant_gluing | 6 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_invariant_gluing | 7 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_invariant_gluing | 8 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_invariant_gluing | 9 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_physical_constraints | 1 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_physical_constraints | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_physical_constraints | 3 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_physical_constraints | 4 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_physical_constraints | 5 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_physical_constraints | 6 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_physical_constraints | 7 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_physical_constraints | 8 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_physical_constraints | 9 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_schema_sync | 1 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| sheaf_schema_sync | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| sheaf_schema_sync | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| sheaf_schema_sync | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| sheaf_schema_sync | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| sheaf_schema_sync | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| sheaf_schema_sync | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| sheaf_schema_sync | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| sheaf_schema_sync | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| spreadsheet_dataflow | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| spreadsheet_dataflow | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| spreadsheet_dataflow | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| spreadsheet_dataflow | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| spreadsheet_dataflow | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| spreadsheet_dataflow | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| spreadsheet_dataflow | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| spreadsheet_dataflow | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| spreadsheet_dataflow | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| sql_fixed_point | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| sql_fixed_point | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| sql_fixed_point | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| sql_fixed_point | 4 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"behavioral_reference": 1} |
| sql_fixed_point | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| sql_fixed_point | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| sql_fixed_point | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| sql_fixed_point | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| sql_fixed_point | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| ssm_parallel_scan | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| ssm_parallel_scan | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| ssm_parallel_scan | 3 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| ssm_parallel_scan | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| ssm_parallel_scan | 5 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| ssm_parallel_scan | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| ssm_parallel_scan | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| ssm_parallel_scan | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| ssm_parallel_scan | 9 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| stochastic_monad | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| stochastic_monad | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| stochastic_monad | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| stochastic_monad | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| stochastic_monad | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| stochastic_monad | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| stochastic_monad | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| stochastic_monad | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| stochastic_monad | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| template_interpreter | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| template_interpreter | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| template_interpreter | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| template_interpreter | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| template_interpreter | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| template_interpreter | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| template_interpreter | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| template_interpreter | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| template_interpreter | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"behavioral_reference": 1} |
| tensor_functor | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tensor_functor | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tensor_functor | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tensor_functor | 4 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| tensor_functor | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tensor_functor | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tensor_functor | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tensor_functor | 8 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| tensor_functor | 9 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| tokenizer_adjunction | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tokenizer_adjunction | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tokenizer_adjunction | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tokenizer_adjunction | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tokenizer_adjunction | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tokenizer_adjunction | 6 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tokenizer_adjunction | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tokenizer_adjunction | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| tokenizer_adjunction | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| transformer_ssm_lift | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| transformer_ssm_lift | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| transformer_ssm_lift | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| transformer_ssm_lift | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| transformer_ssm_lift | 5 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| transformer_ssm_lift | 6 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"source_invalid": 1} | {"compile_only": 1} |
| transformer_ssm_lift | 7 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| transformer_ssm_lift | 8 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| transformer_ssm_lift | 9 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| ts_one_step | 1 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"runtime_error": 1} | {"compile_only": 1} |
| ts_one_step | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| ts_one_step | 3 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| ts_one_step | 4 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| ts_parse_only | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| ts_parse_only | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| ts_parse_only | 3 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| ts_parse_only | 4 | 2 | 1 | 1 | 0 | 1 | 0 | 1.0 | {} | {"compile_only": 1} |
| ts_trajectory | 1 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| ts_trajectory | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"runtime_error": 1} | {"compile_only": 1} |
| ts_trajectory | 3 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |
| ts_trajectory | 4 | 2 | 1 | 1 | 0 | 0 | 1 | 0.0 | {"underfit": 1} | {"compile_only": 1} |

## Section E — what each chart draws

The charts are SVG files that the reviewer cannot render. This section states what each one plots, with the values from the tables above.

**Figure 8 (selection frame).** Three stacked horizontal bars. Bar 1, design cells: 496 = 416 selected + 80 omitted (56 intervention-twin, 14 known-gate, 10 unsupported modality). Bar 2, selected cases: 405 scored + 11 unscored. Bar 3, scored cases: 277 PASS + 128 FAIL. The 80 omitted cases are drawn in pale grey and are in no pass rate. Only segments of 40 or more cases carry a text label; the 11-case unscored segment is unlabelled, and its count appears only in the caption.

**Figure 9 (environment intervals).** One dot per environment with scored cases (36 environments; environments with no scored case are not drawn). The dot is the pass fraction k/n. The bar is the 95% Wilson interval. The label beside each bar is k/n. A dotted vertical line marks the pooled 277/405 = 68.4%. Rows below are in the order drawn, from lowest to highest pass fraction.

| order | environment | k/n | pass fraction | Wilson 95% low | Wilson 95% high | colour class |
|---|---|---|---|---|---|---|
| 1 | ts_one_step | 0/4 | 0.000 | 0.000 | 0.490 | no scored pass |
| 2 | ts_trajectory | 0/4 | 0.000 | 0.000 | 0.490 | no scored pass |
| 3 | functorial_augmentation | 0/9 | 0.000 | 0.000 | 0.299 | no scored pass |
| 4 | monadic_reward | 0/9 | 0.000 | 0.000 | 0.299 | no scored pass |
| 5 | sheaf_invariant_gluing | 0/9 | 0.000 | 0.000 | 0.299 | no scored pass |
| 6 | sheaf_physical_constraints | 0/9 | 0.000 | 0.000 | 0.299 | no scored pass |
| 7 | glyph | 0/24 | 0.000 | 0.000 | 0.138 | no scored pass |
| 8 | batchnorm_ema | 2/15 | 0.133 | 0.037 | 0.379 | mixed |
| 9 | gnn_message_passing | 5/9 | 0.556 | 0.267 | 0.811 | mixed |
| 10 | regex_state_machine | 5/9 | 0.556 | 0.267 | 0.811 | mixed |
| 11 | ssm_parallel_scan | 5/9 | 0.556 | 0.267 | 0.811 | mixed |
| 12 | rd_adaptive_halting | 8/14 | 0.571 | 0.326 | 0.786 | mixed |
| 13 | moco | 36/55 | 0.655 | 0.523 | 0.766 | mixed |
| 14 | tensor_functor | 6/9 | 0.667 | 0.354 | 0.879 | mixed |
| 15 | compositional_optimizer | 7/9 | 0.778 | 0.453 | 0.937 | mixed |
| 16 | equivariant_diagram | 7/9 | 0.778 | 0.453 | 0.937 | mixed |
| 17 | sheaf_schema_sync | 8/9 | 0.889 | 0.565 | 0.980 | mixed |
| 18 | sql_fixed_point | 8/9 | 0.889 | 0.565 | 0.980 | mixed |
| 19 | transformer_ssm_lift | 8/9 | 0.889 | 0.565 | 0.980 | mixed |
| 20 | epistemic_fragmented_observation | 4/4 | 1.000 | 0.510 | 1.000 | all scored passed |
| 21 | ts_parse_only | 4/4 | 1.000 | 0.510 | 1.000 | all scored passed |
| 22 | epistemic_announcements | 6/6 | 1.000 | 0.610 | 1.000 | all scored passed |
| 23 | epistemic_nested_knowledge | 6/6 | 1.000 | 0.610 | 1.000 | all scored passed |
| 24 | architecture_naturality | 9/9 | 1.000 | 0.701 | 1.000 | all scored passed |
| 25 | categorical_lenses | 9/9 | 1.000 | 0.701 | 1.000 | all scored passed |
| 26 | ci_dependency_graph | 9/9 | 1.000 | 0.701 | 1.000 | all scored passed |
| 27 | neuro_symbolic_parser | 9/9 | 1.000 | 0.701 | 1.000 | all scored passed |
| 28 | semiring_unification | 9/9 | 1.000 | 0.701 | 1.000 | all scored passed |
| 29 | spreadsheet_dataflow | 9/9 | 1.000 | 0.701 | 1.000 | all scored passed |
| 30 | stochastic_monad | 9/9 | 1.000 | 0.701 | 1.000 | all scored passed |
| 31 | template_interpreter | 9/9 | 1.000 | 0.701 | 1.000 | all scored passed |
| 32 | tokenizer_adjunction | 9/9 | 1.000 | 0.701 | 1.000 | all scored passed |
| 33 | rd_gradient_credit | 15/15 | 1.000 | 0.796 | 1.000 | all scored passed |
| 34 | rd_state_carry | 15/15 | 1.000 | 0.796 | 1.000 | all scored passed |
| 35 | css_state_machine | 18/18 | 1.000 | 0.824 | 1.000 | all scored passed |
| 36 | epistemic_games | 23/23 | 1.000 | 0.857 | 1.000 | all scored passed |

**Figure 10 (tuple matrix).** One square per environment × difficulty-tuple row: 340 squares, grouped by environment (38 environments, one row of squares each). The colour is the row pass rate (red 0, amber fractional, green 1). Grey marks the 11 rows with no scored case. A number is written in squares that hold more than one case (44 such rows). Fractional rows: 9, all in `moco`. Tuples are environment-specific, so columns are not comparable across environments.

**Figure 11 (failure labels).** A horizontal bar chart of the normalised failure label across all 128 FAIL cases combined. There is no environment split. Counts: underfit 51, overfit_visible_tests 49, runtime_error 11, source_invalid 9, invalid_action 5, training_failed 3.


<END EVIDENCE PACKET>

## Your role

You are an independent Evidence Reviewer. Check every number, count and factual claim in the article against the packet. Produce an adversarial brief. Do not rewrite the article. Do not propose new analyses that need data outside the packet.

## Facts the packet should confirm (check them, do not assume them)

- 416 selected cases; 405 scored (`status = scored`); 11 `infrastructure_unscored`.
- 277 PASS / 128 FAIL; 277/405 = 68.4%; 277/416 = 66.6%.
- 80 omissions: 56 intervention-twin, 14 known-gate, 10 unsupported input modality (all in `rope`).
- 38 environments; 36 with scored cases. Outcome split: 17 all-pass, 12 mixed, 7 all-fail, 2 with no scored case.
- Mixed environments: 165 scored cases, 105 PASS. All 12 contain at least one zero-pass tuple.
- Unweighted mean of environment pass fractions 69.2%; median 88.9%.
- Matrix: 340 rows; 296 single-case; 44 multi-case. 329 rows have a pass rate; 320 of those are exactly 0 or 1; 9 are fractional, all in `moco`. 204 rows sit in environments where every scored row has the same outcome; 214 if the two no-scored environments are added.
- Judge guarantee is fixed per environment: 11 `behavioral_reference` (141/189 scored PASS), 27 `compile_only` (136/216 scored PASS; 11 unscored).
- Failure labels (normalised): underfit 51, overfit_visible_tests 49, runtime_error 11 (9 `RUNTIME_ERROR` and 2 `runtime_error` in the raw column), source_invalid 9, invalid_action 5, training_failed 3.
- Disposition: 10 `rejected` (all FAIL; 9 with label `source_invalid`); 9 scored FAILs with disposition `unscored`.
- One PASS in `ts_parse_only` has `performance_eligible = False`.
- Seed is 0 for all 416 cases.

## Tasks

1. Check each number in the article against the packet. Report each mismatch with the article location, the article value, and the packet value and row.
2. Check each figure caption against Section E of the packet. Report any caption that claims more or less than the chart plots.
3. Check each disclosure beside a claim: the 10 `rejected` FAILs, the 80 omissions, the performance-ineligible PASS, the 9 `unscored`-disposition FAILs, and the 14-vs-24 known-gate conflict.
4. Identify any causal or mechanism claim the packet does not support, and any "cannot" or "does not show" statement that the packet contradicts.
5. Identify any statement that treats a recorded label, disposition or guarantee as a fact about the model rather than a recorded classification.
6. Note any open discrepancy, such as the zero-pass count in `campaign-02-analysis/ANALYSIS_OVERVIEW.md` (stated as 10; the packet gives 7 at environment level and 19 at tuple level).

## Output format

- Verdict: accept / accept with corrections / reject.
- Numbered findings, each with: article location, claim, packet evidence (table and row or column), severity (blocking / correction / note).
- Final line: count of blocking findings and count of corrections.
- Start the response with the "State" line described above (commit read, row counts seen, anything unread).

## Constraints

- No internal finding IDs, trace IDs or draft labels in any suggested public wording.
- Bracketed tokens such as `[m-word]` are intentional replacements, not errors.
- Do not suggest preregistration framing. The analysis is retrospective.
