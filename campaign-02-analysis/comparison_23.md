opus 5.5:

---
title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>A retrospective look at the archived Mercury-2.5 results, comparing environments and examining how their outcomes are distributed, with no new model runs.</dd>
  <dt>Synthesis</dt><dd>I grouped the 416 selected cases in 38 environments and a 340-row environment × difficulty-tuple matrix to test the pooled pass rate against case counts, endpoints, case density, and the confounds the archive records.</dd>
  <dt>Prose</dt><dd>Written for this article in the first person, with every figure tied to the reported counts.</dd>
  <dt>Certainty</dt><dd>I am fairly confident in the counts, but much less confident about any cause or mechanism, because the archive has a single seed, a dirty source state, unscored cases, two kinds of judge guarantee, and some open discrepancies.</dd>
  <dt>Importance</dt><dd>One pooled benchmark number can hide where its cases sit, how unevenly they are spread, and how little the archive can actually support.</dd>
</dl>

*Revision note: This version replaces the one first published under this title. The headline figure, 68.4%, has not changed. I have corrected several passages, added an environment × difficulty-tuple matrix as an exploratory second layer, and listed the withdrawn and open claims in their own section instead of quietly removing them.*

Mercury-2.5 passed 68.4% of the scored cases in this campaign. What would I expect if I opened one of its environments at random? The `ts_*` results make that question awkward. `ts_parse_only` is 4/4, while `ts_one_step` and `ts_trajectory` are each 0/4. All three count toward the same pooled number. A single pooled pass rate can turn very uneven environment-level results into one tidy figure.

My aim is to understand what that number summarizes, not to replace it with a different slogan. These are outcomes that the campaign's judges assigned to selected cases. They are not repeated measurements of general capability, and an environment name is not a difficulty rating. This is a retrospective analysis of archived results. It was not preregistered. Still, the differences between environments are too large to leave unstated. The 68.4% figure is arithmetically correct, but on its own it describes little. The more useful structure is the endpoint-heavy map underneath it.

## First, count the cases that received a judgment

The archive contains **416 selected cases in 38 environments**. Of these, 405 received a PASS or FAIL judgment: 277 PASS and 128 FAIL. So **277/405, or 68.4%**, is the scored-case pass rate (the case-weighted pooled rate). The other 11 cases are unscored. That is a gap in judge coverage, not a third kind of outcome.

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

![Lollipop chart of pass rates by environment](../figures/fig2_environment_outcome_lollipop.svg)
*Figure: Pass rate by environment for the 36 environments with scored cases. Many environments sit at exactly 1.0 or 0.0. Read each fraction together with its case count.*

## The endpoint-heavy distribution

Out of the 36 scored environments, 24 sit at an endpoint.

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

The `sheaf_*` names set the opposite trap. `sheaf_schema_sync` is 8/9, while `sheaf_invariant_gluing` and `sheaf_physical_constraints` are each 0/9. Combining all three into one "sheaf performance" figure would hide the very contrast that stands out. Category-theory-flavoured names are no more predictive: `categorical_lenses` is 9/9, `functorial_augmentation` is 0/9, and `tensor_functor` is 6/9. A shared name does not imply shared outcomes in this archive, or even shared evaluation infrastructure.

`glyph`, `moco`, and `batchnorm_ema` reinforce the same caution:

- `glyph` is 0/24, a much larger all-fail block than the four-case `ts_*` zeros.
- `moco` is 36/55 (65.5%), with 19 failures.
- `batchnorm_ema` is 2/15 (13.3%), with 13 failures. One of those failures carries the undefined `rejected` disposition.

Together, these three environments contribute **94 of the 405 scored cases but 56 of the 128 failures**. That shows concretely how much the pooled result depends on where cases were selected. It does not show that the three environments share a failure mechanism.

## A second layer: the environment × tuple matrix

Within each environment, cases are organized by difficulty tuples. The archive includes a matrix with one row per environment × tuple: **340 rows** in total. Each environment has between 4 and 15 rows, and six environments have more than 10.

There are **34 difficulty dimension names** across the matrix. The tuples are specific to each environment. A dimension in one environment is not calibrated against a dimension in another. For that reason, I do not pool, rank, or regress tuples across environments, and I do not read any tuple-level pattern as a difficulty effect.

The matrix contains four main facts:

- **Most rows hold a single case.** 296 of 340 rows contain one case. The 44 multi-case rows are all in four environments: `moco` (15 rows, 55 cases), `glyph` (12 rows, 24 cases), `css_state_machine` (9 rows, 18 cases), and `epistemic_games` (8 rows, 23 cases).
- **Most row outcomes are binary.** 329 rows have a pass rate, and 320 of those (97.3%) are exactly 0 or 1. The nine fractional rows are all in `moco`. Since most rows hold one case, a rate of 0 or 1 is mostly unavoidable. It is not evidence of sharp tuple boundaries.
- **Many rows sit in uniform environments.** 214 of 340 rows (63%) belong to environments where every row has the same outcome.
- **Zero-pass tuples are widespread.** 98 individual tuples have no passes, and they occur in 19 environments. That is far more than the seven environments with no passes at all. Many mixed environments contain some zero-pass tuples.

This layer is exploratory. It shows how the cases are arranged, but it does not explain why any tuple passed or failed.

## What a "cell" means

The campaign describes its design as "one seed per cell," and that wording is ambiguous. Every one of the 416 selected cases carries seed 0, and none was re-run under a second seed. If a cell meant a single case, the phrase would add nothing. The row counts suggest the intended meaning: 340 rows hold 416 cases, and 44 rows hold more than one case, all at seed 0. So a cell most plausibly means an environment × tuple row. That is my inference from the arithmetic. The archive does not state it as a convention.

Either way, the 405 scored cases are not 405 distinct tuples, and they are certainly not 405 independent tests of a general ability. `moco` alone supplies 55 scored cases (13.6% of all scored cases) from 15 tuples. The aggregates are not detailed enough to estimate how correlated cases within a tuple are.

Because case density is uneven, a few environments pull hard on the global average:

| Scenario | Pass rate | Change |
|---|---:|---:|
| Exclude `moco` | 241/350 = 68.86% | +0.47 pt |
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

The 11 unscored cases are:

- 6 in `epistemic_silence`
- 4 in `epistemic_type_games`
- 1 in `rd_adaptive_halting`

The first two environments have no scored case at all, which is why the scored-environment count drops from 38 to 36. The unscored `rd_adaptive_halting` case sits at the tuple where all five dimensions are `easy`. The gap is in judge coverage, and that tuple label does not make it evidence about difficulty.

Recoding these 11 cases as failures would put invented outcomes into the denominator. The scored pass rate stays at 277/405. The all-selected figure, 277/416, answers a different question. `rd_adaptive_halting` remains 8/14 scored plus one unscored case. It is not a 15-case judgment with an assumed failure.

## Ten zero-pass environments or seven?

An earlier project summary says there are 10 zero-pass environments. The environment-level count gives 7. I tested one possible explanation: counting environments with at least one zero-pass tuple. That gives 19, so it does not reproduce 10 either. I do not know where the 10 comes from. I use 7 in this article, and the reconciliation remains open.

## What can a FAIL label explain?

The archive assigns these labels to the 128 FAIL outcomes:

| Label | Count |
|---|---:|
| `underfit` | 51 |
| `overfit_visible_tests` | 49 |
| `runtime_error` | 11 |
| `source_invalid` | 9 |
| `invalid_action` | 5 |
| `training_failed` | 3 |
| **Total** | **128** |

The `runtime_error` count combines 9 cases recorded as `RUNTIME_ERROR` and 2 recorded as `runtime_error`. The difference in casing is a data-quality issue, not two kinds of runtime failure.

These are recorded classifications, not observations of Mercury-2.5's internal reasoning. I cannot infer a mechanism from the label names. The counts are also global only. No breakdown by environment is available, so I do not assign any label to any environment. For example, nine `source_invalid` failures and several nine-case all-fail environments are a reason to inspect case logs. They are not grounds for linking the two.

Judge guarantees add a second limit. Across the 416 selected cases, the campaign records **189 `behavioral_reference` and 227 `compile_only`** guarantees, and those totals include unscored cases. The two guarantees check different things, so a PASS under one does not establish what a PASS under the other does. Without a breakdown by environment and guarantee, I cannot test whether the contrasts between environments would hold under a single standard. A PASS records only what that case's judge checked. It does not show that the model understood or solved the task.

## The selection frame

The 416 cases are themselves a selection. Before scoring, **80 cases** were omitted:

| Omission reason | Cases |
|---|---:|
| Intervention-twin omissions | 56 |
| Known-gate calibration failures | 14 |
| Unsupported input modality (all in the `rope` environment) | 10 |

The provenance summary instead gives **24** known-gate omissions, which disagrees with the exclusion record's 14. I report both and do not resolve the conflict.

Two flags apply to cases inside the 416:

- **Ten scored FAIL cases carry the disposition `rejected`:** eight in `monadic_reward`, one in `batchnorm_ema`, and one in `transformer_ssm_lift`. The archive does not define "rejected." All ten stay in the 128 failures.
- **One PASS in `ts_parse_only` is marked performance-ineligible**, and its exclusion note contradicts its verdict. It stays in the 277.

## Confounds I cannot remove

- **Single seed.** Every selected case carries seed 0. I have no variance or stability estimate. A 5/9 in `regex_state_machine` might be typical or unusual, and the archive cannot tell which. The 12 mixed environments, which hold 40.7% of the scored cases, are especially exposed. The endpoints are not protected from this either.
- **Dirty source state.** The campaign's source repository was recorded as dirty. The exact working-tree state [m-word] for reproduction, so I cannot isolate the effect of uncommitted changes on any environment.
- **Selection.** Omissions before scoring, unscored cases, undefined rejections, and uneven case density all shape which outcomes enter the 405. The counts disagree in places (14 vs 24, 10 vs 7).

## What this supports, and what it does not

On this archived selection, Mercury-2.5 received **277 PASS judgments among 405 scored cases**. The judges recorded all-pass outcomes in 17 environments, all-fail outcomes in 7, mixed outcomes in 12, and no scored outcome in 2. Closely named environments sometimes landed far apart. At the tuple level, nearly all rows are binary and most hold a single case. Fractional rows occur only in `moco`.

This analysis does *not* show that environment identity matters more than difficulty, because there is no common difficulty scale to compare against. It does not show a difficulty effect or a ranking within environments. It does not identify a model-internal cause for `glyph` or `batchnorm_ema`. It does not tell us whether the endpoints would hold under other seeds, a uniform judge guarantee, or a cleanly recorded source state. A breakdown of outcomes by environment, judge guarantee, and failure label would be the next useful step.

So I would keep **68.4%** as the answer to one precise question: *What fraction of scored, selected cases received PASS?* I would not let it stand alone as the campaign's outcome. The map beside it says more: the zeros, the all-pass environments, the 40.7% of scored cases in between, and the gaps and disagreements in the archive that limit what any single number can mean.


&&&&&&&&&&&&&&&

gpt 6 luna max:

---
title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
date: 2026-10-16
layout: post
---

*by StrangeTcy*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>I offer a retrospective interpretation of Mercury-2.5’s archived judgments and tuple matrix, with no new model runs.</dd>
  <dt>Synthesis</dt><dd>I bring together selected-case counts, environment outcomes, tuple-row summaries, and documented limitations.</dd>
  <dt>Prose</dt><dd>The article is written in first person and keeps interpretation separate from recorded verdicts.</dd>
  <dt>Certainty</dt><dd>I am confident in the reported arithmetic but cautious about causes or stability because the cases use one seed, omit some judgments, mix judge guarantees, and come from a dirty source state.</dd>
  <dt>Importance</dt><dd>The pooled rate is accurate for its denominator, but cannot show the distribution across environments or the limits of the selected results on its own.</dd>
</dl>

## Revision note

This replaces the earlier version; the headline stays. It adds the environment-by-tuple matrix as an exploratory second layer and states withdrawn claims openly. This is a retrospective analysis of archived results, not a preregistered study; no new runs were performed.

## What the pooled rate says—and leaves out

Judges marked **277 of 405 scored cases** PASS, for a case-weighted rate of **68.4%**. That is a precise answer to a specific counting question. It does not, by itself, describe what happened in any particular environment.

The `ts_*` results make the gap visible: `ts_parse_only` received PASS on 4/4 cases, while `ts_one_step` and `ts_trajectory` each received PASS on 0/4. All three contribute to the same pooled rate. I want to keep that rate while making its parts visible. Environment names are useful labels, not difficulty ratings.

## First, count the cases that received a judgment

The selection contains **416 cases in 38 environments**. Of these, 405 received a PASS or FAIL judgment: 277 PASS and 128 FAIL. The other 11 are unscored because of a judge-coverage gap; they are not a third outcome.

| Environment outcome | Environments | PASS / scored cases | Unscored cases |
|---|---:|---:|---:|
| Every scored case received PASS | 17 | 172/172 | 0 |
| Mixed PASS and FAIL | 12 | 105/165 | 1 |
| No scored case received PASS | 7 | 0/68 | 0 |
| No scored cases | 2 | — | 10 |
| **Total** | **38** | **277/405** | **11** |

The scored-case pass rate is **277/405, or 68.4%**. The fraction **277/416, or 66.6%**, answers a different question: the share of all selected cases with an observed PASS. It should not be read as a pass rate that treats the 11 unknown outcomes as failures.

Of the 36 environments with scored cases, 24 sit at an observed endpoint: every scored case received PASS in 17 environments, and none received PASS in seven. The 12 mixed environments hold 165 of 405 scored cases, or 40.7%. These counts describe the archive’s selected cases; they do not show how any endpoint would hold up under other seeds or cases.

## The endpoint-heavy distribution

The 17 environments in which every scored case received PASS account for 172/172 cases. Nine were 9/9: `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, and `tokenizer_adjunction`. The others were `css_state_machine` (18/18), `rd_gradient_credit` (15/15), `rd_state_carry` (15/15), `epistemic_games` (23/23), `epistemic_announcements` (6/6), `epistemic_nested_knowledge` (6/6), `epistemic_fragmented_observation` (4/4), and `ts_parse_only` (4/4). One PASS in `ts_parse_only` is marked performance-ineligible despite an exclusion note describing a provider-attributed terminal failure; I retain the recorded PASS and return to that inconsistency below.

The seven environments with no scored PASS account for 0/68 cases: `functorial_augmentation` (0/9), `monadic_reward` (0/9), `sheaf_invariant_gluing` (0/9), `sheaf_physical_constraints` (0/9), `ts_one_step` (0/4), `ts_trajectory` (0/4), and `glyph` (0/24). Eight of the nine scored `monadic_reward` cases are marked `rejected`; the archive does not define that label, and all nine remain in the 0/9 tally.

The remaining 12 environments have mixed outcomes: `sheaf_schema_sync` (8/9), `sql_fixed_point` (8/9), `transformer_ssm_lift` (8/9), `compositional_optimizer` (7/9), `equivariant_diagram` (7/9), `tensor_functor` (6/9), `gnn_message_passing` (5/9), `regex_state_machine` (5/9), `ssm_parallel_scan` (5/9), `moco` (36/55), `rd_adaptive_halting` (8/14, plus one unscored case), and `batchnorm_ema` (2/15). Together, these environments contain 105 PASS judgments among 165 scored cases. Their observed fractions differ, but they remain counts from selected cases, not estimates of repeatability.

## Names are handles, not forecasts

The three `ts_*` environments are three sets of four judged cases: 4/4 in `ts_parse_only`, and 0/4 in each of `ts_one_step` and `ts_trajectory`. That is a description of the recorded outcomes, not a controlled progression along a shared scale. The cases were not repeated under another seed, and the names alone do not establish how the environments compare.

The `sheaf_*` results create a similar contrast: `sheaf_schema_sync` is 8/9, while `sheaf_invariant_gluing` and `sheaf_physical_constraints` are each 0/9. Grouping them under one label would hide that difference. Other related names also have distinct recorded results: `categorical_lenses` is 9/9, `functorial_augmentation` is 0/9, and `tensor_functor` is 6/9. A shared label does not establish a shared outcome or judge guarantee.

`glyph` (0/24), `moco` (36/55), and `batchnorm_ema` (2/15) illustrate how case counts and results can differ across environments. Together they contribute 94 of the 405 scored cases and 56 of the 128 FAIL judgments. That concentration is one way the selected cases shape the pooled rate; it does not identify a common failure mechanism.

## A second layer: the tuple matrix

The environment summary compresses cases into 38 outcomes. The environment-by-difficulty-tuple matrix adds 340 rows, with 4 to 15 rows per environment; six environments have more than 10. It uses 34 difficulty-dimension names. Those tuples are environment-specific, so I do not pool, rank, or regress them across environments as though they shared a scale.

The rows are not equivalent to cases. There are 296 single-case rows and 44 multi-case rows. All 44 multi-case rows occur in four environments: `moco` (15 rows, 55 cases), `glyph` (12 rows, 24 cases), `css_state_machine` (9 rows, 18 cases), and `epistemic_games` (8 rows, 23 cases).

Of the 340 rows, 329 carry a pass rate. Of those, 320—97.3%—are exactly 0 or 1; the other nine are fractional, all in `moco`. Also, 214 rows (63%) sit in environments where every row has the same outcome. Separately, 98 individual tuples have zero PASS judgments, across 19 environments. That tuple count does not mean 19 environments have zero PASS across all their scored cases.

### What does a “cell” mean?

All 416 selected cases carry seed 0, and no case was run under a second seed. The wording “one seed per cell” is ambiguous here: some environment-by-tuple rows contain multiple cases. From the row and case counts, I infer that “cell” means an environment-by-tuple row, not a single case. That is an inference from the arithmetic, not a stated convention.

### `moco` is the only environment with fractional tuple rates

Six of `moco`’s 15 rows sit at 0 or 1; the other nine are fractional. The fractional values are 1/6, 1/3, 2/5, 2/3, 3/4, and 5/6. There is no row-by-row key linking each value to its tuple, so I cannot draw the tuple-level shape or connect a particular fraction to a particular tuple. The matrix supports the narrower statement that `moco` is the only environment with fractional row rates.

## Withdrawn and open claims

I withdraw the earlier claim of a non-monotonic difficulty pattern in `css_state_machine`: it is 18/18, and every tuple row is 2/2. The matrix shows no variation in outcomes across those rows.

The reported non-monotonic patterns in `moco` and `sql_fixed_point` remain open, not findings. With one seed and a mostly binary row design, apparent irregularities may arise by chance; the base rate has not been computed. I do not treat those patterns as evidence of a difficulty effect or a ranking.

## Unscored means uncovered, not failed

The 11 unscored cases are six in `epistemic_silence`, four in `epistemic_type_games`, and one in `rd_adaptive_halting`. The `rd_adaptive_halting` case is at the tuple where all five dimensions are `easy`. The first two environments have no scored cases, while `rd_adaptive_halting` has a scored result of 8/14 plus that one unscored case. None of these missing judgments is a FAIL.

## Seven is the environment-level zero count

A project-level account states that 10 environments had zero PASS judgments. The environment-level summary gives seven environments with no scored PASS. Counting environments with at least one zero-PASS tuple gives 19, which does not reproduce 10. I use seven for the environment-level count; the source of the figure 10 remains unexplained.

## Failure labels and judge guarantees

The archive’s global FAIL-label counts are:

| Failure label | Cases |
|---|---:|
| `underfit` | 51 |
| `overfit_visible_tests` | 49 |
| `runtime_error` | 11 |
| `source_invalid` | 9 |
| `invalid_action` | 5 |
| `training_failed` | 3 |
| **Total** | **128** |

The 11 `runtime_error` labels consolidate nine recorded as `RUNTIME_ERROR` and two as `runtime_error`. The counts are global; there is no environment-level breakdown. The two largest labels total 100 of 128 FAIL judgments, but these are recorded classifications, not observations of Mercury-2.5’s internal reasoning or explanations of any particular environment’s results.

The 416 selected cases carry 189 `behavioral_reference` and 227 `compile_only` judge guarantees, including the unscored cases. These guarantees are not interchangeable descriptions of what a PASS establishes. Without an environment-by-guarantee breakdown, I cannot tell whether the observed environment contrasts would change under a common judge standard.

## The selection frame

The 416 cases are not the only cases considered. The exclusion record lists 80 omitted before scoring: 56 intervention-twin omissions, 14 known-gate calibration failures, and 10 unsupported-input-modality cases, all in `rope`. A provenance summary instead gives 24 known-gate omissions. That conflicts with the exclusion record’s 14; I leave the disagreement unresolved rather than substitute one count for the other. The pass rate describes the selected cases, not the omitted ones.

Separately, 10 scored FAIL cases carry the `rejected` disposition: eight of the nine scored `monadic_reward` cases, one `batchnorm_ema` case, and one `transformer_ssm_lift` case. The archive does not define “rejected,” so I keep all 10 in the recorded FAIL and scored-case totals.

One PASS in `ts_parse_only` is marked performance-ineligible. Its exclusion note describes a provider-attributed terminal failure, while its verdict is PASS. I keep it in the 277 PASS judgments and flag the inconsistency rather than recoding it.

## Confounds we cannot remove

The single seed leaves no estimate of variation across seeds: every selected case has seed 0, with no second-seed result. The campaign’s source repository was recorded as dirty, and its exact working-tree state was [m-word] for reproduction. I cannot isolate an effect of uncommitted changes on any environment. The selection omissions and differing judge guarantees also limit what these comparisons can establish.

## What the archive supports

The descriptive result is specific: judges assigned **277 PASS judgments among 405 scored cases**, or **68.4%**, across the selected Mercury-2.5 cases. The environment summary records 17 all-PASS environments, seven with no scored PASS, 12 mixed environments, and two without scored cases. The tuple matrix adds structure, but its environment-specific dimensions and mostly binary, single-seed rows do not provide a common scale or a stability estimate.

This analysis does not show why outcomes differ, what the omitted cases would have received, or how results would change under other seeds, a common judge guarantee, or a cleanly captured source state. I would keep **68.4%** as the answer to the precise question “What fraction of scored, selected cases received PASS?” I would not let it stand alone as the whole outcome.

!

*The chart shows observed pass rates across the 36 environments with scored cases; read each fraction with its case count.*

