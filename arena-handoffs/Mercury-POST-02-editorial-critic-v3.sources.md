<BEGIN SOURCE WRITER_PAIR>
gpt 6 luna max:
---
title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>This is a retrospective reading of archived Mercury-2.5 outcomes across environments and tuple rows, not new run results.</dd>
  <dt>Synthesis</dt><dd>I regroup 416 selected cases in 38 environments and add the environment-by-tuple matrix as an exploratory second layer.</dd>
  <dt>Prose</dt><dd>The prose is first-person and exploratory, limited to recorded judgments and their arithmetic.</dd>
  <dt>Certainty</dt><dd>Confidence is high in the counts but limited for causal interpretation by one seed, unscored cases, judge-guarantee differences, selection, and dirty source state.</dd>
  <dt>Importance</dt><dd>The point is to keep the pooled denominator visible while showing how the environment-level distribution changes what it can mean.</dd>
</dl>

**Revision note:** This replaces the earlier version. The headline stays; the tuple matrix is added as an exploratory second layer, and withdrawn or open claims are identified below.

Mercury-2.5 received PASS on **68.4% of 405 scored cases** in this archived campaign. That is a precise case-weighted rate, but it does not describe what happened in each environment. Some environments had PASS judgments for every scored case, some had none, and others mixed PASS and FAIL.

The `ts_*` results make the difference visible: `ts_parse_only` is 4/4, while `ts_one_step` and `ts_trajectory` are each 0/4. Those are descriptions of judgments on small sets of selected cases, not stable estimates. One `ts_parse_only` PASS is also flagged as performance-ineligible despite its PASS verdict; I keep it in the count and return to the conflict below.

These are outcomes assigned by the campaign’s judges to selected cases. They are not repeated measurements of general capability, and an environment name is not a difficulty rating. I want to understand what the pooled number summarizes, rather than replace it with another slogan.

## First, count the cases that received a judgment

The campaign contains **416 selected cases in 38 environments**. Of these, 405 received a PASS or FAIL judgment: 277 PASS and 128 FAIL. Another 11 are unscored because of a judge-coverage gap; they are not a third outcome.

| Environment outcome | Environments | PASS / scored cases | Share of scored cases | Unscored cases |
|---|---:|---:|---:|---:|
| Every scored case passed | 17 | 172/172 | 42.5% | 0 |
| No scored case passed | 7 | 0/68 | 16.8% | 0 |
| Some passed, some failed | 12 | 105/165 | 40.7% | 1 |
| No scored cases | 2 | — | — | 10 |
| **Total** | **38** | **277/405** | **100%** | **11** |

Thus **277/405, or 68.4%**, is the scored-case pass rate. **277/416, or 66.6%**, answers a different question: the share of all selected cases with an observed PASS. It must not be read as a pass rate that treats the unscored cases as failures.

Twenty-four of the 36 environments with scored cases sit at an observed endpoint: every scored case passed or none did. I call this distribution endpoint-heavy, not a stable division in capability. Some endpoints rest on four cases and others on 23 or 24; the counts alone cannot show how they would hold up under other seeds or cases. The mixed environments are not a small remainder: they contain 165 of the 405 scored cases, or 40.7%, with 105 PASS judgments and one additional unscored case.

Across the 36 environments with scored cases, the unweighted mean of their observed pass fractions is approximately 69.2%; the median is 8/9, or 88.9%. Each summary answers a different question, and neither removes the uneven environment-level pattern.

## The endpoint-heavy distribution

The 17 environments in which every scored case passed account for 172/172 cases. Nine are at 9/9: `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, and `tokenizer_adjunction`. The others are `css_state_machine` (18/18), `rd_gradient_credit` (15/15), `rd_state_carry` (15/15), `epistemic_games` (23/23), `epistemic_announcements` (6/6), `epistemic_nested_knowledge` (6/6), `epistemic_fragmented_observation` (4/4), and `ts_parse_only` (4/4).

The seven environments with no scored PASS account for 0/68: `functorial_augmentation` (0/9), `monadic_reward` (0/9), `sheaf_invariant_gluing` (0/9), `sheaf_physical_constraints` (0/9), `ts_one_step` (0/4), `ts_trajectory` (0/4), and `glyph` (0/24). In `monadic_reward`, eight of the nine scored cases carry the disposition `rejected`. The archive does not define that disposition, and all nine cases remain in the 0/9 result and the overall FAIL count.

The 12 mixed environments are:

| Environment | PASS / scored cases |
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
| `rd_adaptive_halting` | 8/14, plus 1 unscored |
| `batchnorm_ema` | 2/15 |

The lone FAIL in `transformer_ssm_lift` also carries the `rejected` disposition and remains in its 8/9 count. Together, the mixed environments contain 165 scored cases, ranging from 2/15 to 8/9. The pooled rate sits above this spread; it does not make the environments interchangeable.

## Names are useful handles, not forecasts

It is tempting to treat prefixes such as `ts_*` or `sheaf_*` as families with a shared outcome. The archive does not support that shortcut.

The `ts_*` trio consists of three sets of four judged cases: `ts_parse_only` is 4/4, while `ts_one_step` and `ts_trajectory` are each 0/4. This is a fair description of those results, but not evidence of an ordering across a shared difficulty scale. The case sets are not repeated trials of an otherwise identical test.

The `sheaf_*` names show the same limit in another way: `sheaf_schema_sync` is 8/9, while `sheaf_invariant_gluing` and `sheaf_physical_constraints` are each 0/9. Grouping them under one label would hide their different recorded outcomes, not explain them. Other broad labels offer no better forecast: `categorical_lenses` is 9/9, `functorial_augmentation` is 0/9, and `tensor_functor` is 6/9.

Case density also gives some environments more weight in the pooled rate. `glyph` contributes 0/24, `moco` 36/55, and `batchnorm_ema` 2/15. Together they contribute 94 of 405 scored cases and 56 of 128 FAILs. That describes where scored cases and FAIL judgments fall in this selection; it does not establish a shared failure mechanism.

## The environment-by-tuple matrix

The second layer contains **340 environment-by-tuple rows**, with between 4 and 15 rows per environment; six environments have more than 10. Most rows are single-case: 296 of 340. The other 44 multi-case rows occur in four environments: `moco` has 15 rows covering 55 cases, `glyph` 12 rows covering 24, `css_state_machine` 9 rows covering 18, and `epistemic_games` 8 rows covering 23.

The 405 scored cases are therefore not 405 distinct tuples, much less 405 independent tests of a general ability. These aggregates do not estimate within-tuple dependence.

Of the 340 rows, 329 carry a pass rate. Of those, 320 (97.3%) are exactly 0 or 1; nine are fractional, all in `moco`. The matrix uses 34 difficulty dimension names, but the tuples are environment-specific. They are not a shared scale and must not be pooled, ranked, or regressed across environments.

A total of 214 rows—63% of the matrix—sit in environments where every row has the same outcome. Separately, 98 individual tuples have zero passes, spread across 19 environments; all 12 mixed environments have at least one such tuple. These are descriptive counts in this matrix, not evidence that a dimension causes an outcome. And with 296 single-case rows, a binary rate can often describe just one judgment; it is not, by itself, evidence of a stable tuple-level result.

### What a “cell” means

All 416 selected cases carry seed 0, and no case was re-run under a second seed. The phrase “one seed per cell” is ambiguous here: the row counts show that a cell must mean an environment-by-tuple row, not a single case. That is an inference from the arithmetic, not a stated convention. Some rows group multiple cases, so the case count and the matrix-row count are not interchangeable.

### `moco`: the only fractional rows

`moco` is the only environment with fractional outcomes in the matrix. Six of its 15 rows sit at 0 or 1; the other nine are fractional, with values of 1/6, 1/3, 2/5, 2/3, 3/4, and 5/6. The available record does not link each fractional value to its tuple key, so I cannot draw the outcome shape across `moco`’s dimensions. Its overall 36/55 rate does not supply that missing mapping.

## Claims withdrawn or left open

I withdraw any earlier suggestion of a non-monotonic outcome pattern in `css_state_machine`: all 18 cases passed, and every tuple row is 2/2. There is no change in recorded outcome across its rows.

I leave apparent non-monotonic patterns in `moco` and the SQL-named `sql_fixed_point` open, not findings. The archived results use one seed, and the mostly binary matrix can show apparent structure by chance; the base rate for such patterns has not been computed. For `moco`, the missing row-by-row tuple key also prevents reconstructing the pattern. None of these observations supports a difficulty effect or a ranking.

## Unscored cases are not failures

The 11 unscored cases are a judge-coverage gap, not failures: six are in `epistemic_silence`, four in `epistemic_type_games`, and one in `rd_adaptive_halting`. The first two environments have no scored cases, so neither has a scored pass fraction. Treating their cases as zero-pass would invent judgments that are not in the record.

The unscored `rd_adaptive_halting` case sits at the tuple where all five dimensions are `easy`. That tuple label does not supply a judgment for the case or turn it into a failure. The environment’s scored result remains 8/14 plus one unscored case.

## Ten zero-pass environments or seven?

A project-level summary states that there are 10 zero-pass environments. The environment-level count here is seven: the environments with at least one scored case and no scored PASS. The tuple matrix gives 98 zero-pass tuples in 19 environments, which also does not reproduce 10. I use the environment-level count of seven and leave the origin of the other figure unresolved; the unscored environments are not zero-pass environments.

## Failure labels and judge guarantees

The 128 FAILs carry these recorded labels:

| Recorded label | FAIL cases |
|---|---:|
| `underfit` | 51 |
| `overfit_visible_tests` | 49 |
| `runtime_error` (spellings consolidated) | 11 |
| `source_invalid` | 9 |
| `invalid_action` | 5 |
| `training_failed` | 3 |
| **Total** | **128** |

The consolidated runtime-error count includes nine cases recorded as `RUNTIME_ERROR` and two as `runtime_error`. These are recorded classifications, not observations of internal reasoning. The counts are global only; they do not show which environments produced which labels or establish a mechanism.

The campaign records 189 `behavioral_reference` and 227 `compile_only` judge guarantees across the 416 selected cases, including the unscored cases.

| Judge guarantee | Selected cases |
|---|---:|
| `behavioral_reference` | 189 |
| `compile_only` | 227 |
| **Total** | **416** |

These guarantees are not interchangeable descriptions of what a PASS establishes. The totals alone do not show how outcomes are distributed by environment and guarantee, so I cannot compare environment results under one common judging standard.

## The selection frame

The 416 selected cases are only part of the campaign’s recorded frame. Another 80 cases were omitted before scoring:

| Omission class | Cases |
|---|---:|
| Intervention-twin omissions | 56 |
| Known-gate calibration failures | 14 |
| Unsupported provider input modality | 10 |
| **Total omitted** | **80** |

All 10 unsupported-input-modality omissions are in `rope`. A provenance summary gives 24 known-gate omissions, which disagrees with the 14 in the exclusion record. I report both figures and leave the discrepancy unresolved. The 80 omitted cases are outside the 416 selected cases and do not enter the scored-case denominator.

There are 10 scored FAIL cases marked with the disposition `rejected`: eight of the nine scored `monadic_reward` cases, one in `batchnorm_ema`, and one in `transformer_ssm_lift`. The archive does not define `rejected`. All 10 remain in the FAIL counts.

There is also one PASS in `ts_parse_only` marked performance-ineligible. Its exclusion note describes a provider-attributed terminal failure, while its verdict is PASS. I keep it in the 277 PASS count and flag the disagreement rather than silently changing the recorded judgment.

## Confounds we cannot ignore

Every selected case has seed 0, and none was run under a second seed. There is no variance or stability estimate here: the observed endpoints and mixed rates describe this seed and selection, not what another seed would produce.

The source repository was recorded as dirty. The exact working-tree state is [m-word] for reproduction, so I cannot isolate the effect of uncommitted changes on any environment.

The 416 cases were selected, while 80 additional cases were omitted before scoring; the disagreement over known-gate omissions adds uncertainty about the selection frame. The reported rate describes the selected, scored cases, not all possible cases. Likewise, the guarantee totals do not show how a uniform judging standard would change the environment comparisons.

## What this supports—and what it does not

The established result is specific: on this archived selection, Mercury-2.5 received **277 PASS judgments among 405 scored cases**. There were observed all-pass outcomes in 17 environments, all-fail outcomes in seven, mixed outcomes in 12, and no scored outcome in two. The matrix adds a second descriptive view of tuple rows, but its environment-specific dimensions do not make a common scale.

This does not show that environment identity outweighs difficulty, because the dimensions cannot be compared across environments on a shared scale. It does not identify an internal cause for the `glyph` or `batchnorm_ema` results, establish how endpoints would hold under other seeds, or show what a uniform judge or cleanly recorded source state would change.

I would keep **68.4%** as the answer to one precise counting question: *What fraction of scored, selected cases received PASS?* I would not let it stand alone as the campaign’s outcome. The environment table and tuple matrix show what that number compresses, while the unscored cases, unequal density, judge guarantees, selection, single seed, and dirty source state limit what the map can establish.

!

*Figure 2: Lollipop chart of observed pass rates across the 36 environments with scored cases. Read each fraction alongside its case count; the chart is not a stability estimate.*

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

opus 5:
---
title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>The structural reading of the Mercury-2.5 archive: how the pooled pass rate decomposes across environments, and now across the environment × difficulty-tuple matrix beneath them.</dd>
  <dt>Synthesis</dt><dd>Aggregation and regrouping of 416 archived cases in 38 environments, plus the 340-row tuple matrix, against exact counts, endpoints, densities, and recorded confounds.</dd>
  <dt>Prose</dt><dd>Written for this article: first person, exploratory, and tied to the arithmetic at every step.</dd>
  <dt>Certainty</dt><dd>High on the counts and tallies; low on anything causal, because every case ran under a single seed, the source tree was dirty, 11 cases are unscored, and judge guarantees differ across environments.</dd>
  <dt>Importance</dt><dd>A pooled benchmark number is easy to mistake for a uniform description of its parts, and this archive shows both how much it hides and how little it can support.</dd>
</dl>

**Revision note.** This version replaces the earlier one under the same title. The headline number is unchanged: 277 of 405 scored cases passed, 68.4%. What is new is a second layer — the 340-row environment × difficulty-tuple matrix — read as exploratory description rather than as a result. One earlier claim is withdrawn outright, two are left open, and the places where the archive's own records disagree with each other are now stated instead of smoothed over.

## The number and the question it answers

Mercury-2.5 passed 68.4% of the scored cases in this campaign. What should I expect if I open one environment at random? The `ts_*` results make that question awkward: `ts_parse_only` is 4/4, while `ts_one_step` and `ts_trajectory` are each 0/4. All three feed the same pooled figure.

I want to know what that figure summarizes, not to replace it with a different slogan. These are verdicts assigned by the campaign's judges to selected cases. They are not repeated measurements of a general ability, and an environment name is not a difficulty rating. The 68.4% is arithmetically correct and descriptively thin; the structure worth looking at is the map underneath it.

## First, count the cases that received a judgment

The archive holds **416 selected cases in 38 environments**. Of those, 405 received a PASS or FAIL verdict: 277 PASS and 128 FAIL. So **277/405 = 68.4%** is the scored-case pass rate. Eleven cases were never scored — a judge-coverage gap, not a third outcome. The fraction **277/416 = 66.6%** answers a different question: the share of all selected cases with an observed PASS. It should never be presented as a pass rate, because that would silently convert 11 unknown outcomes into failures.

| Environment outcome | Environments | PASS / scored cases | Share of scored cases | Unscored cases |
|---|---:|---:|---:|---:|
| Every scored case passed | 17 | 172/172 | 42.5% | 0 |
| No scored case passed | 7 | 0/68 | 16.8% | 0 |
| Some passed, some failed | 12 | 105/165 | 40.7% | 1 |
| No scored cases | 2 | — | — | 10 |
| **Total** | **38** | **277/405** | **100%** | **11** |

Twenty-four of the 36 environments with scored cases sit at an observed endpoint: every case passed, or every case failed. I would call the map *endpoint-heavy* and stop there. Some endpoints rest on four cases, others on 23 or 24, and the table cannot tell me how stable any of them would be under different cases or seeds.

The mixed environments are not a rounding error. They hold **165 of the 405 scored cases**, 40.7%, and range from 2/15 to 8/9. Across the 36 environments with scored cases, the unweighted mean of the observed pass fractions is about 69.2% and the median is 8/9, or 88.9%. Either summary changes the question and still hides the shape.

![Lollipop chart of pass rates by environment](../figures/fig2_environment_outcome_lollipop.svg)
*Figure 2: One dot per environment with at least one scored case, at its observed pass fraction. Read each dot with its case count; the dots at 1.0 and 0.0 rest on anywhere from four to 24 cases.*

## The endpoint-heavy distribution

**17 environments where every scored case passed** (172 cases). Nine are 9/9: `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, `tokenizer_adjunction`. Four are larger: `epistemic_games` 23/23, `css_state_machine` 18/18, `rd_gradient_credit` 15/15, `rd_state_carry` 15/15. Four are smaller: `epistemic_announcements` 6/6, `epistemic_nested_knowledge` 6/6, `epistemic_fragmented_observation` 4/4, `ts_parse_only` 4/4.

**7 environments where no scored case passed** (68 cases): `functorial_augmentation` 0/9, `monadic_reward` 0/9, `sheaf_invariant_gluing` 0/9, `sheaf_physical_constraints` 0/9, `ts_one_step` 0/4, `ts_trajectory` 0/4, and `glyph` 0/24. Eight of the nine scored `monadic_reward` cases also carry a `rejected` disposition, which the archive never defines; I keep all nine in the counts and flag it here rather than quietly dropping them.

**12 mixed environments** (105/165 scored, plus one unscored):

| Environment | Scored | Rate |
|---|---:|---:|
| sheaf_schema_sync | 8/9 | 0.889 |
| sql_fixed_point | 8/9 | 0.889 |
| transformer_ssm_lift | 8/9 | 0.889 |
| compositional_optimizer | 7/9 | 0.778 |
| equivariant_diagram | 7/9 | 0.778 |
| tensor_functor | 6/9 | 0.667 |
| gnn_message_passing | 5/9 | 0.556 |
| regex_state_machine | 5/9 | 0.556 |
| ssm_parallel_scan | 5/9 | 0.556 |
| moco | 36/55 | 0.655 |
| rd_adaptive_halting | 8/14 (+1 unscored) | 0.571 |
| batchnorm_ema | 2/15 | 0.133 |

The single FAIL in `transformer_ssm_lift` carries the same undefined `rejected` disposition, as does one FAIL in `batchnorm_ema`; ten scored FAILs carry it in total, and all ten stay in the 128.

## Names are useful handles, not forecasts

It is tempting to read prefixes like `ts_*` or `sheaf_*` as families with a shared difficulty. In this archive they are an unreliable shortcut.

The `ts_*` trio is the clearest small case: `ts_parse_only` 4/4, `ts_one_step` 0/4, `ts_trajectory` 0/4. That is a fair description of three sets of four judged cases. It is not a difficulty ladder — there is no shared scale here, and these are not repeated trials of one test.

The `sheaf_*` names set the opposite trap: `sheaf_schema_sync` 8/9, while `sheaf_invariant_gluing` and `sheaf_physical_constraints` are each 0/9. Category-flavoured names behave the same way: `categorical_lenses` 9/9, `functorial_augmentation` 0/9, `tensor_functor` 6/9. A shared name does not imply a shared outcome, or even shared evaluation conditions.

`glyph`, `moco`, and `batchnorm_ema` carry more weight. `glyph` is 0/24, a far larger all-fail block than the four-case `ts_*` zeros. `moco` is 36/55 with 19 failures. `batchnorm_ema` is 2/15 with 13. Together these three supply **94 of the 405 scored cases but 56 of the 128 failures**. That shows how much the pooled result depends on where cases were selected. It does not tell me the three share a mechanism.

Density matters for the top line too. Excluding `moco` gives 241/350 = 68.86% (Δ +0.46 pt). Excluding `glyph` gives 277/381 = 72.70% (Δ +4.31 pt). Excluding both gives 241/326 = 73.93%. If `moco` were shrunk to nine cases at its own 65.5%, the pooled figure would sit near 68.8%. The 68.4% is sensitive to how tuples were unrolled into cases for a handful of environments.

## A second layer: the environment × tuple matrix

Beneath the environment summary sits a matrix of **340 rows**, one per environment × difficulty tuple, with 4 to 15 rows per environment and six environments above 10 rows. The matrix names **34 difficulty dimensions**, but they are environment-specific: a tuple in `moco` and a tuple in `glyph` are not two points on one scale. They must not be pooled, ranked, or regressed across environments, and nothing below should be read as a difficulty effect.

What the matrix does show is how thin each row is.

- **296 of 340 rows are single-case.** Only 44 rows hold more than one case, and all 44 sit in four environments: `moco` (15 rows, 55 cases), `glyph` (12 rows, 24 cases), `css_state_machine` (9 rows, 18 cases), `epistemic_games` (8 rows, 23 cases).
- **329 rows carry a pass rate**, and **320 of them (97.3%) are exactly 0 or 1.** Nine rows are fractional, and all nine are in `moco`.
- **214 of 340 rows (63%)** sit in environments where every row has the same outcome.
- **98 individual tuples have zero passes**, spread across 19 environments.

So the matrix mostly repeats the endpoint pattern one level down, which is close to inevitable when nearly nine rows in ten contain a single case. A single-case row can only be 0 or 1. The 98 zero-pass tuples in 19 environments are a count of thin rows, not a ranking of hard ones.

## What a "cell" means

The campaign records one seed per cell. The word "cell" is never defined. The arithmetic forces a reading: 340 rows against 416 cases, with 44 rows holding more than one case, means a cell must be an environment × tuple row rather than a single case. I state that as an inference from the counts, not as a stated convention of the archive. If it is right, then no tuple in this campaign was ever observed under a second seed.

## `moco`: the only fractional rows

`moco` is the one environment whose matrix rows are not all at an endpoint. Six of its 15 rows sit at 0.0 or 1.0; the other nine are fractional, with values 1/6, 1/3, 2/5, 2/3, 3/4, and 5/6. That is the entire fractional population of the matrix.

I cannot draw the shape of `moco` across its dimensions: the fractional values are recorded, but no row-by-row key links each value back to its tuple. So I can say that `moco` is the only environment where outcomes vary within tuples, and I cannot say which tuples those are or how they are arranged.

## Claims withdrawn or left open

One claim from the earlier version is **withdrawn**: a non-monotonic difficulty pattern in `css_state_machine`. The environment is 18/18 over nine rows, so every row is 2/2. There is no pattern there to describe.

Two are **open, and are not findings**: apparent non-monotonic patterns in `moco` and in a SQL-named environment. Under a single-seed design where almost every row is binary, such patterns can arise by chance, and I have not computed the base rate at which they would. I raise them as questions, not results.

## Unscored cases are not failures

Eleven cases were never judged: six in `epistemic_silence`, four in `epistemic_type_games`, one in `rd_adaptive_halting`. The first two environments therefore have no pass fraction at all, which is why the scored-environment count is 36 rather than 38.

The single `rd_adaptive_halting` gap is identified in the matrix at the tuple where all five dimensions are `easy`. Being unscored is a property of the judging pipeline, not of the case's outcome; I will not read it as a hidden failure, and recoding the 11 as failures would inflate the denominator with outcomes nobody observed. The scored rate stays 277/405.

## Ten zero-pass environments or seven?

A project overview states that 10 environments had no passes. The environment-level counts give **seven**. A tuple-level reading — environments with at least one zero-pass tuple — gives 19, so it does not produce 10 either. I have not found the derivation behind the 10. I use seven, and I record the reconciliation as open rather than inventing an account that fits.

## What can a FAIL label explain?

The 128 FAIL verdicts carry six labels, globally:

| Label | Count |
|---|---:|
| underfit | 51 |
| overfit_visible_tests | 49 |
| runtime_error | 11 |
| source_invalid | 9 |
| invalid_action | 5 |
| training_failed | 3 |

The runtime count consolidates nine cases recorded in upper case with two in lower case. I read nothing into the casing, and the counts alone do not establish that the two spellings cover one kind of failure; they only show how the archive consolidated them.

These are global tallies. **No environment-by-label breakdown is available here**, so I cannot say which environments produced the 51 `underfit` labels or the 49 `overfit_visible_tests` ones, and I will not infer a mapping from coincidences of size. The labels are also recorded classifications, not observations of the model's internal reasoning.

There is a second limit on reading PASS labels. The campaign records **189 `behavioral_reference` and 227 `compile_only` judge guarantees** across the 416 selected cases, including the unscored ones. Those guarantees are not interchangeable statements about what a PASS establishes, and without an environment-by-guarantee breakdown I cannot test whether the environment contrasts survive a uniform standard. Describing a 9/9 environment as behaviourally settled would outrun what the judge checked.

## The selection frame

The 416 cases are themselves a selection. **80 further cases were omitted before scoring**: 56 intervention-twin omissions, 14 known-gate calibration failures, and 10 unsupported-input-modality cases, all in the `rope` environment, which has no row in the 38-environment summary.

The archive disagrees with itself here. The provenance summary gives **24** known-gate omissions; the exclusion record gives **14**. I report both and do not resolve the conflict, because nothing available to me says which figure is the correct one.

Two more flags belong beside the counts rather than inside a footnote. Ten scored FAILs carry the undefined `rejected` disposition — eight in `monadic_reward`, one in `batchnorm_ema`, one in `transformer_ssm_lift` — and all ten remain in the 128. And one PASS, in `ts_parse_only`, is marked performance-ineligible, with an exclusion note describing a terminal failure attributed to the provider while the verdict itself reads PASS. I keep it in the 277 and flag the inconsistency rather than adjudicate it.

## Confounds I cannot remove

Every one of the 416 selected cases carries seed 0, and no case was run again under a second seed. There is no variance estimate anywhere in this archive. A 5/9 in `regex_state_machine` may be typical or a single unlucky draw; the endpoints are exposed to the same uncertainty, and the matrix makes it sharper, since 296 rows rest on one case each.

The source repository was recorded as dirty at run time. The exact working-tree state [m-word] for reproduction, so the effect of uncommitted changes on any environment cannot be isolated — only noted.

And the selection frame above sits upstream of everything: 80 omitted cases, a disagreement about 14 versus 24 of them, and an entire environment that never reached scoring.

## What this supports

On this archived selection, Mercury-2.5 received **277 PASS verdicts among 405 scored cases**: all-pass outcomes in 17 environments, all-fail in seven, mixed in 12, and no scored outcome in two. Twenty-four of 36 scored environments sit at an endpoint. The tuple matrix repeats that pattern — 320 of 329 rated rows at 0 or 1, 63% of rows inside environments with a single uniform outcome — largely because most rows hold one case. Closely named environments landed far apart.

What this does not show: any common difficulty scale on which environments could be ranked, so I will not say that environment identity outweighs difficulty. Not a mechanism for `glyph`, `moco`, or `batchnorm_ema`. Not how any endpoint would survive another seed, a uniform judge guarantee, or a clean source tree. An environment-by-guarantee and environment-by-label cross-tab would narrow some of that; nothing in the present archive supplies it.

So I keep **68.4%** as the answer to one precise question: what fraction of scored, selected cases received PASS? I would not let it stand alone. The more informative answer is the map beside it — the zeros, the perfect scores, the 40.7% of scored cases in between, and the honest list of what the archive declines to settle.
<END SOURCE WRITER_PAIR>

<BEGIN SOURCE COMPLETE_EVIDENCE_PACKET>
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


<END SOURCE COMPLETE_EVIDENCE_PACKET>

<BEGIN SOURCE COMPLETE_DIFFICULTY_MATRIX_CSV>
environment,difficulty_tuple,n_cases,n_scored,n_unscored,n_pass,n_fail,pass_rate,failure_modes,judge_guarantees
architecture_naturality,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
architecture_naturality,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
architecture_naturality,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
architecture_naturality,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
architecture_naturality,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
architecture_naturality,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
architecture_naturality,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
architecture_naturality,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
architecture_naturality,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""easy"", ""optimizer_hint"": ""easy"", ""red_herring"": ""easy"", ""symptom_mask"": ""easy"", ""visible_tests"": ""easy""}",1,1,0,0,1,0.0,"{""overfit_visible_tests"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""easy"", ""optimizer_hint"": ""hard"", ""red_herring"": ""easy"", ""symptom_mask"": ""easy"", ""visible_tests"": ""hard""}",1,1,0,0,1,0.0,"{""overfit_visible_tests"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""easy"", ""optimizer_hint"": ""hard"", ""red_herring"": ""hard"", ""symptom_mask"": ""medium"", ""visible_tests"": ""easy""}",1,1,0,0,1,0.0,"{""overfit_visible_tests"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""easy"", ""optimizer_hint"": ""medium"", ""red_herring"": ""easy"", ""symptom_mask"": ""easy"", ""visible_tests"": ""medium""}",1,1,0,0,1,0.0,"{""training_failed"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""easy"", ""optimizer_hint"": ""medium"", ""red_herring"": ""medium"", ""symptom_mask"": ""hard"", ""visible_tests"": ""easy""}",1,1,0,0,1,0.0,"{""overfit_visible_tests"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""hard"", ""optimizer_hint"": ""easy"", ""red_herring"": ""easy"", ""symptom_mask"": ""medium"", ""visible_tests"": ""hard""}",1,1,0,0,1,0.0,"{""overfit_visible_tests"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""hard"", ""optimizer_hint"": ""easy"", ""red_herring"": ""hard"", ""symptom_mask"": ""easy"", ""visible_tests"": ""easy""}",1,1,0,0,1,0.0,"{""overfit_visible_tests"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""hard"", ""optimizer_hint"": ""hard"", ""red_herring"": ""hard"", ""symptom_mask"": ""hard"", ""visible_tests"": ""hard""}",1,1,0,0,1,0.0,"{""overfit_visible_tests"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""hard"", ""optimizer_hint"": ""medium"", ""red_herring"": ""hard"", ""symptom_mask"": ""easy"", ""visible_tests"": ""medium""}",1,1,0,0,1,0.0,"{""overfit_visible_tests"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""hard"", ""optimizer_hint"": ""medium"", ""red_herring"": ""medium"", ""symptom_mask"": ""easy"", ""visible_tests"": ""hard""}",1,1,0,0,1,0.0,"{""overfit_visible_tests"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""medium"", ""optimizer_hint"": ""easy"", ""red_herring"": ""easy"", ""symptom_mask"": ""hard"", ""visible_tests"": ""medium""}",1,1,0,0,1,0.0,"{""overfit_visible_tests"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""medium"", ""optimizer_hint"": ""easy"", ""red_herring"": ""medium"", ""symptom_mask"": ""easy"", ""visible_tests"": ""easy""}",1,1,0,0,1,0.0,"{""overfit_visible_tests"": 1}","{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""medium"", ""optimizer_hint"": ""hard"", ""red_herring"": ""hard"", ""symptom_mask"": ""easy"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""medium"", ""optimizer_hint"": ""hard"", ""red_herring"": ""medium"", ""symptom_mask"": ""easy"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
batchnorm_ema,"{""data_complexity"": ""medium"", ""optimizer_hint"": ""medium"", ""red_herring"": ""medium"", ""symptom_mask"": ""medium"", ""visible_tests"": ""medium""}",1,1,0,0,1,0.0,"{""invalid_action"": 1}","{""compile_only"": 1}"
categorical_lenses,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
categorical_lenses,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
categorical_lenses,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
categorical_lenses,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
categorical_lenses,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
categorical_lenses,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
categorical_lenses,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
categorical_lenses,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
categorical_lenses,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
ci_dependency_graph,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
ci_dependency_graph,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
ci_dependency_graph,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
ci_dependency_graph,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
ci_dependency_graph,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
ci_dependency_graph,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
ci_dependency_graph,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
ci_dependency_graph,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
ci_dependency_graph,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
compositional_optimizer,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
compositional_optimizer,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
compositional_optimizer,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
compositional_optimizer,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
compositional_optimizer,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
compositional_optimizer,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
compositional_optimizer,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
compositional_optimizer,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
compositional_optimizer,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
css_state_machine,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
css_state_machine,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
css_state_machine,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
css_state_machine,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
css_state_machine,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""hard""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
css_state_machine,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""medium""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
css_state_machine,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
css_state_machine,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""hard""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
css_state_machine,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""medium""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
epistemic_announcements,"{""depth"": ""chain"", ""query"": ""factual"", ""scenario"": ""expedition"", ""worlds"": ""four""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_announcements,"{""depth"": ""chain"", ""query"": ""factual"", ""scenario"": ""office"", ""worlds"": ""three""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_announcements,"{""depth"": ""chain"", ""query"": ""nested"", ""scenario"": ""expedition"", ""worlds"": ""four""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_announcements,"{""depth"": ""one"", ""query"": ""factual"", ""scenario"": ""expedition"", ""worlds"": ""four""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_announcements,"{""depth"": ""one"", ""query"": ""nested"", ""scenario"": ""expedition"", ""worlds"": ""three""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_announcements,"{""depth"": ""one"", ""query"": ""nested"", ""scenario"": ""office"", ""worlds"": ""four""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_fragmented_observation,"{""fragment"": ""asymmetric"", ""scenario"": ""expedition"", ""worlds"": ""four""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_fragmented_observation,"{""fragment"": ""asymmetric"", ""scenario"": ""office"", ""worlds"": ""six""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_fragmented_observation,"{""fragment"": ""symmetric"", ""scenario"": ""expedition"", ""worlds"": ""six""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_fragmented_observation,"{""fragment"": ""symmetric"", ""scenario"": ""office"", ""worlds"": ""four""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_games,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",3,3,0,3,0,1.0,{},"{""behavioral_reference"": 3}"
epistemic_games,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""solo"", ""prior"": ""skewed"", ""scenario"": ""trap""}",3,3,0,3,0,1.0,{},"{""behavioral_reference"": 3}"
epistemic_games,"{""evidence"": ""ambiguous"", ""framing"": ""narrative"", ""presentation"": ""solo"", ""prior"": ""balanced"", ""scenario"": ""report""}",4,4,0,4,0,1.0,{},"{""behavioral_reference"": 4}"
epistemic_games,"{""evidence"": ""strong"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""trap""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
epistemic_games,"{""evidence"": ""strong"", ""framing"": ""narrative"", ""presentation"": ""solo"", ""prior"": ""skewed"", ""scenario"": ""report""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
epistemic_games,"{""evidence"": ""weak"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""skewed"", ""scenario"": ""report""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
epistemic_games,"{""evidence"": ""weak"", ""framing"": ""bare_table"", ""presentation"": ""solo"", ""prior"": ""balanced"", ""scenario"": ""report""}",4,4,0,4,0,1.0,{},"{""behavioral_reference"": 4}"
epistemic_games,"{""evidence"": ""weak"", ""framing"": ""narrative"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""trap""}",3,3,0,3,0,1.0,{},"{""behavioral_reference"": 3}"
epistemic_nested_knowledge,"{""order"": ""first"", ""scenario"": ""expedition"", ""worlds"": ""four""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_nested_knowledge,"{""order"": ""first"", ""scenario"": ""office"", ""worlds"": ""six""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_nested_knowledge,"{""order"": ""second"", ""scenario"": ""expedition"", ""worlds"": ""six""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_nested_knowledge,"{""order"": ""second"", ""scenario"": ""office"", ""worlds"": ""four""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_nested_knowledge,"{""order"": ""third"", ""scenario"": ""expedition"", ""worlds"": ""four""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_nested_knowledge,"{""order"": ""third"", ""scenario"": ""office"", ""worlds"": ""six""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
epistemic_silence,"{""observation"": ""message"", ""prior"": ""skewed"", ""protocol"": ""pair"", ""scenario"": ""expedition""}",1,0,1,0,0,,{},"{""compile_only"": 1}"
epistemic_silence,"{""observation"": ""message"", ""prior"": ""skewed"", ""protocol"": ""single"", ""scenario"": ""expedition""}",1,0,1,0,0,,{},"{""compile_only"": 1}"
epistemic_silence,"{""observation"": ""message"", ""prior"": ""uniform"", ""protocol"": ""pair"", ""scenario"": ""expedition""}",1,0,1,0,0,,{},"{""compile_only"": 1}"
epistemic_silence,"{""observation"": ""message"", ""prior"": ""uniform"", ""protocol"": ""single"", ""scenario"": ""office""}",1,0,1,0,0,,{},"{""compile_only"": 1}"
epistemic_silence,"{""observation"": ""silence"", ""prior"": ""skewed"", ""protocol"": ""pair"", ""scenario"": ""office""}",1,0,1,0,0,,{},"{""compile_only"": 1}"
epistemic_silence,"{""observation"": ""silence"", ""prior"": ""uniform"", ""protocol"": ""single"", ""scenario"": ""expedition""}",1,0,1,0,0,,{},"{""compile_only"": 1}"
epistemic_type_games,"{""payoffs"": ""mild"", ""scenario"": ""expedition"", ""types"": ""large""}",1,0,1,0,0,,{},"{""compile_only"": 1}"
epistemic_type_games,"{""payoffs"": ""mild"", ""scenario"": ""office"", ""types"": ""small""}",1,0,1,0,0,,{},"{""compile_only"": 1}"
epistemic_type_games,"{""payoffs"": ""sharp"", ""scenario"": ""expedition"", ""types"": ""small""}",1,0,1,0,0,,{},"{""compile_only"": 1}"
epistemic_type_games,"{""payoffs"": ""sharp"", ""scenario"": ""office"", ""types"": ""large""}",1,0,1,0,0,,{},"{""compile_only"": 1}"
equivariant_diagram,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
equivariant_diagram,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
equivariant_diagram,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
equivariant_diagram,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
equivariant_diagram,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
equivariant_diagram,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
equivariant_diagram,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
equivariant_diagram,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
equivariant_diagram,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""RUNTIME_ERROR"": 1}","{""compile_only"": 1}"
functorial_augmentation,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""RUNTIME_ERROR"": 1}","{""compile_only"": 1}"
functorial_augmentation,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
functorial_augmentation,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
functorial_augmentation,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""RUNTIME_ERROR"": 1}","{""compile_only"": 1}"
functorial_augmentation,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
functorial_augmentation,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""RUNTIME_ERROR"": 1}","{""compile_only"": 1}"
functorial_augmentation,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
functorial_augmentation,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
functorial_augmentation,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
glyph,"{""architecture"": ""easy"", ""data_clue"": ""easy"", ""optimizer"": ""easy"", ""red_herring"": ""easy"", ""symptom_mask"": ""easy"", ""visible_tests"": ""easy""}",2,2,0,0,2,0.0,"{""overfit_visible_tests"": 2}","{""behavioral_reference"": 2}"
glyph,"{""architecture"": ""easy"", ""data_clue"": ""easy"", ""optimizer"": ""hard"", ""red_herring"": ""easy"", ""symptom_mask"": ""hard"", ""visible_tests"": ""hard""}",2,2,0,0,2,0.0,"{""overfit_visible_tests"": 2}","{""behavioral_reference"": 2}"
glyph,"{""architecture"": ""easy"", ""data_clue"": ""easy"", ""optimizer"": ""medium"", ""red_herring"": ""easy"", ""symptom_mask"": ""medium"", ""visible_tests"": ""medium""}",2,2,0,0,2,0.0,"{""underfit"": 1, ""overfit_visible_tests"": 1}","{""behavioral_reference"": 2}"
glyph,"{""architecture"": ""hard"", ""data_clue"": ""easy"", ""optimizer"": ""hard"", ""red_herring"": ""medium"", ""symptom_mask"": ""easy"", ""visible_tests"": ""medium""}",2,2,0,0,2,0.0,"{""overfit_visible_tests"": 2}","{""behavioral_reference"": 2}"
glyph,"{""architecture"": ""hard"", ""data_clue"": ""hard"", ""optimizer"": ""hard"", ""red_herring"": ""hard"", ""symptom_mask"": ""hard"", ""visible_tests"": ""hard""}",2,2,0,0,2,0.0,"{""invalid_action"": 1, ""overfit_visible_tests"": 1}","{""behavioral_reference"": 2}"
glyph,"{""architecture"": ""hard"", ""data_clue"": ""hard"", ""optimizer"": ""medium"", ""red_herring"": ""hard"", ""symptom_mask"": ""medium"", ""visible_tests"": ""medium""}",2,2,0,0,2,0.0,"{""overfit_visible_tests"": 2}","{""behavioral_reference"": 2}"
glyph,"{""architecture"": ""hard"", ""data_clue"": ""medium"", ""optimizer"": ""hard"", ""red_herring"": ""easy"", ""symptom_mask"": ""medium"", ""visible_tests"": ""easy""}",2,2,0,0,2,0.0,"{""overfit_visible_tests"": 2}","{""behavioral_reference"": 2}"
glyph,"{""architecture"": ""medium"", ""data_clue"": ""easy"", ""optimizer"": ""medium"", ""red_herring"": ""hard"", ""symptom_mask"": ""easy"", ""visible_tests"": ""hard""}",2,2,0,0,2,0.0,"{""overfit_visible_tests"": 2}","{""behavioral_reference"": 2}"
glyph,"{""architecture"": ""medium"", ""data_clue"": ""hard"", ""optimizer"": ""medium"", ""red_herring"": ""easy"", ""symptom_mask"": ""hard"", ""visible_tests"": ""easy""}",2,2,0,0,2,0.0,"{""overfit_visible_tests"": 2}","{""behavioral_reference"": 2}"
glyph,"{""architecture"": ""medium"", ""data_clue"": ""medium"", ""optimizer"": ""easy"", ""red_herring"": ""medium"", ""symptom_mask"": ""easy"", ""visible_tests"": ""easy""}",2,2,0,0,2,0.0,"{""overfit_visible_tests"": 2}","{""behavioral_reference"": 2}"
glyph,"{""architecture"": ""medium"", ""data_clue"": ""medium"", ""optimizer"": ""hard"", ""red_herring"": ""medium"", ""symptom_mask"": ""hard"", ""visible_tests"": ""hard""}",2,2,0,0,2,0.0,"{""overfit_visible_tests"": 2}","{""behavioral_reference"": 2}"
glyph,"{""architecture"": ""medium"", ""data_clue"": ""medium"", ""optimizer"": ""medium"", ""red_herring"": ""medium"", ""symptom_mask"": ""medium"", ""visible_tests"": ""medium""}",2,2,0,0,2,0.0,"{""overfit_visible_tests"": 2}","{""behavioral_reference"": 2}"
gnn_message_passing,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
gnn_message_passing,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
gnn_message_passing,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
gnn_message_passing,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
gnn_message_passing,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
gnn_message_passing,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
gnn_message_passing,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
gnn_message_passing,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
gnn_message_passing,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
moco,"{""distractors"": ""easy"", ""naming"": ""easy"", ""queue_math"": ""easy"", ""symptom_mask"": ""easy"", ""temperature"": ""easy"", ""visible_tests"": ""easy""}",6,6,0,4,2,0.6666666666666666,"{""overfit_visible_tests"": 2}","{""behavioral_reference"": 6}"
moco,"{""distractors"": ""easy"", ""naming"": ""easy"", ""queue_math"": ""hard"", ""symptom_mask"": ""medium"", ""temperature"": ""hard"", ""visible_tests"": ""medium""}",3,3,0,2,1,0.6666666666666666,"{""overfit_visible_tests"": 1}","{""behavioral_reference"": 3}"
moco,"{""distractors"": ""easy"", ""naming"": ""easy"", ""queue_math"": ""medium"", ""symptom_mask"": ""hard"", ""temperature"": ""medium"", ""visible_tests"": ""hard""}",3,3,0,3,0,1.0,{},"{""behavioral_reference"": 3}"
moco,"{""distractors"": ""easy"", ""naming"": ""hard"", ""queue_math"": ""hard"", ""symptom_mask"": ""easy"", ""temperature"": ""easy"", ""visible_tests"": ""hard""}",6,6,0,5,1,0.8333333333333334,"{""training_failed"": 1}","{""behavioral_reference"": 6}"
moco,"{""distractors"": ""easy"", ""naming"": ""medium"", ""queue_math"": ""medium"", ""symptom_mask"": ""easy"", ""temperature"": ""easy"", ""visible_tests"": ""medium""}",3,3,0,2,1,0.6666666666666666,"{""overfit_visible_tests"": 1}","{""behavioral_reference"": 3}"
moco,"{""distractors"": ""hard"", ""naming"": ""easy"", ""queue_math"": ""easy"", ""symptom_mask"": ""hard"", ""temperature"": ""hard"", ""visible_tests"": ""easy""}",6,6,0,1,5,0.16666666666666666,"{""overfit_visible_tests"": 5}","{""behavioral_reference"": 6}"
moco,"{""distractors"": ""hard"", ""naming"": ""hard"", ""queue_math"": ""easy"", ""symptom_mask"": ""medium"", ""temperature"": ""easy"", ""visible_tests"": ""medium""}",4,4,0,3,1,0.75,"{""overfit_visible_tests"": 1}","{""behavioral_reference"": 4}"
moco,"{""distractors"": ""hard"", ""naming"": ""hard"", ""queue_math"": ""hard"", ""symptom_mask"": ""hard"", ""temperature"": ""hard"", ""visible_tests"": ""hard""}",5,5,0,2,3,0.4,"{""overfit_visible_tests"": 3}","{""behavioral_reference"": 5}"
moco,"{""distractors"": ""hard"", ""naming"": ""hard"", ""queue_math"": ""medium"", ""symptom_mask"": ""easy"", ""temperature"": ""medium"", ""visible_tests"": ""easy""}",3,3,0,2,1,0.6666666666666666,"{""overfit_visible_tests"": 1}","{""behavioral_reference"": 3}"
moco,"{""distractors"": ""hard"", ""naming"": ""medium"", ""queue_math"": ""medium"", ""symptom_mask"": ""hard"", ""temperature"": ""hard"", ""visible_tests"": ""medium""}",2,2,0,0,2,0.0,"{""training_failed"": 1, ""overfit_visible_tests"": 1}","{""behavioral_reference"": 2}"
moco,"{""distractors"": ""medium"", ""naming"": ""easy"", ""queue_math"": ""easy"", ""symptom_mask"": ""medium"", ""temperature"": ""medium"", ""visible_tests"": ""easy""}",3,3,0,3,0,1.0,{},"{""behavioral_reference"": 3}"
moco,"{""distractors"": ""medium"", ""naming"": ""hard"", ""queue_math"": ""hard"", ""symptom_mask"": ""medium"", ""temperature"": ""medium"", ""visible_tests"": ""hard""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
moco,"{""distractors"": ""medium"", ""naming"": ""medium"", ""queue_math"": ""easy"", ""symptom_mask"": ""hard"", ""temperature"": ""easy"", ""visible_tests"": ""hard""}",4,4,0,4,0,1.0,{},"{""behavioral_reference"": 4}"
moco,"{""distractors"": ""medium"", ""naming"": ""medium"", ""queue_math"": ""hard"", ""symptom_mask"": ""easy"", ""temperature"": ""hard"", ""visible_tests"": ""easy""}",3,3,0,1,2,0.3333333333333333,"{""overfit_visible_tests"": 1, ""invalid_action"": 1}","{""behavioral_reference"": 3}"
moco,"{""distractors"": ""medium"", ""naming"": ""medium"", ""queue_math"": ""medium"", ""symptom_mask"": ""medium"", ""temperature"": ""medium"", ""visible_tests"": ""medium""}",2,2,0,2,0,1.0,{},"{""behavioral_reference"": 2}"
monadic_reward,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""source_invalid"": 1}","{""compile_only"": 1}"
monadic_reward,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""source_invalid"": 1}","{""compile_only"": 1}"
monadic_reward,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""source_invalid"": 1}","{""compile_only"": 1}"
monadic_reward,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""source_invalid"": 1}","{""compile_only"": 1}"
monadic_reward,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""source_invalid"": 1}","{""compile_only"": 1}"
monadic_reward,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""source_invalid"": 1}","{""compile_only"": 1}"
monadic_reward,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""source_invalid"": 1}","{""compile_only"": 1}"
monadic_reward,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""invalid_action"": 1}","{""compile_only"": 1}"
monadic_reward,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""source_invalid"": 1}","{""compile_only"": 1}"
neuro_symbolic_parser,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
neuro_symbolic_parser,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
neuro_symbolic_parser,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
neuro_symbolic_parser,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
neuro_symbolic_parser,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
neuro_symbolic_parser,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
neuro_symbolic_parser,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
neuro_symbolic_parser,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
neuro_symbolic_parser,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""easy""}",1,0,1,0,0,,{},"{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""easy""}",1,1,0,0,1,0.0,"{""RUNTIME_ERROR"": 1}","{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""hard""}",1,1,0,0,1,0.0,"{""RUNTIME_ERROR"": 1}","{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""hard""}",1,1,0,0,1,0.0,"{""RUNTIME_ERROR"": 1}","{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""hard"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""hard"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""hard"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""medium"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""hard""}",1,1,0,0,1,0.0,"{""RUNTIME_ERROR"": 1}","{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""medium"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_adaptive_halting,"{""batching_complexity"": ""medium"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""medium""}",1,1,0,0,1,0.0,"{""RUNTIME_ERROR"": 1}","{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""hard"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""hard"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""hard"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""medium"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""medium"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_gradient_credit,"{""batching_complexity"": ""medium"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
rd_state_carry,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""easy"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""hard"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""hard"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""hard"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""medium"", ""clue_clarity"": ""easy"", ""implementation_obfuscation"": ""hard"", ""recurrence_depth"": ""easy"", ""visible_tests"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""medium"", ""clue_clarity"": ""hard"", ""implementation_obfuscation"": ""easy"", ""recurrence_depth"": ""hard"", ""visible_tests"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
rd_state_carry,"{""batching_complexity"": ""medium"", ""clue_clarity"": ""medium"", ""implementation_obfuscation"": ""medium"", ""recurrence_depth"": ""medium"", ""visible_tests"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
regex_state_machine,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
regex_state_machine,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""behavioral_reference"": 1}"
regex_state_machine,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""behavioral_reference"": 1}"
regex_state_machine,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
regex_state_machine,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
regex_state_machine,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""behavioral_reference"": 1}"
regex_state_machine,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
regex_state_machine,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""hard""}",1,1,0,0,1,0.0,"{""invalid_action"": 1}","{""behavioral_reference"": 1}"
regex_state_machine,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
semiring_unification,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
semiring_unification,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
semiring_unification,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
semiring_unification,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
semiring_unification,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
semiring_unification,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
semiring_unification,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
semiring_unification,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
semiring_unification,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
sheaf_invariant_gluing,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_invariant_gluing,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_invariant_gluing,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_invariant_gluing,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_invariant_gluing,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_invariant_gluing,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_invariant_gluing,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_invariant_gluing,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_invariant_gluing,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_physical_constraints,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_physical_constraints,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_physical_constraints,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_physical_constraints,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_physical_constraints,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_physical_constraints,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_physical_constraints,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_physical_constraints,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_physical_constraints,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_schema_sync,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
sheaf_schema_sync,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
sheaf_schema_sync,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
sheaf_schema_sync,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
sheaf_schema_sync,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
sheaf_schema_sync,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
sheaf_schema_sync,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
sheaf_schema_sync,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
sheaf_schema_sync,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
spreadsheet_dataflow,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
spreadsheet_dataflow,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
spreadsheet_dataflow,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
spreadsheet_dataflow,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
spreadsheet_dataflow,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
spreadsheet_dataflow,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
spreadsheet_dataflow,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
spreadsheet_dataflow,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
spreadsheet_dataflow,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
sql_fixed_point,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
sql_fixed_point,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
sql_fixed_point,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
sql_fixed_point,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""behavioral_reference"": 1}"
sql_fixed_point,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
sql_fixed_point,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
sql_fixed_point,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
sql_fixed_point,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
sql_fixed_point,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
ssm_parallel_scan,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
ssm_parallel_scan,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
ssm_parallel_scan,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
ssm_parallel_scan,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
ssm_parallel_scan,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
ssm_parallel_scan,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
ssm_parallel_scan,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
ssm_parallel_scan,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
ssm_parallel_scan,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
stochastic_monad,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
stochastic_monad,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
stochastic_monad,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
stochastic_monad,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
stochastic_monad,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
stochastic_monad,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
stochastic_monad,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
stochastic_monad,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
stochastic_monad,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
template_interpreter,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
template_interpreter,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
template_interpreter,"{""hidden_depth"": ""easy"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
template_interpreter,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
template_interpreter,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
template_interpreter,"{""hidden_depth"": ""hard"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
template_interpreter,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""easy""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
template_interpreter,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""hard""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
template_interpreter,"{""hidden_depth"": ""medium"", ""surface_deceptiveness"": ""medium""}",1,1,0,1,0,1.0,{},"{""behavioral_reference"": 1}"
tensor_functor,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tensor_functor,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tensor_functor,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tensor_functor,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
tensor_functor,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tensor_functor,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tensor_functor,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tensor_functor,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
tensor_functor,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
tokenizer_adjunction,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tokenizer_adjunction,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tokenizer_adjunction,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tokenizer_adjunction,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tokenizer_adjunction,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tokenizer_adjunction,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tokenizer_adjunction,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tokenizer_adjunction,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
tokenizer_adjunction,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
transformer_ssm_lift,"{""naming"": ""easy"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
transformer_ssm_lift,"{""naming"": ""easy"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
transformer_ssm_lift,"{""naming"": ""easy"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
transformer_ssm_lift,"{""naming"": ""hard"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
transformer_ssm_lift,"{""naming"": ""hard"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
transformer_ssm_lift,"{""naming"": ""hard"", ""symptom_mask"": ""medium""}",1,1,0,0,1,0.0,"{""source_invalid"": 1}","{""compile_only"": 1}"
transformer_ssm_lift,"{""naming"": ""medium"", ""symptom_mask"": ""easy""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
transformer_ssm_lift,"{""naming"": ""medium"", ""symptom_mask"": ""hard""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
transformer_ssm_lift,"{""naming"": ""medium"", ""symptom_mask"": ""medium""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
ts_one_step,"{""representation"": ""flat"", ""witness_status"": ""broken""}",1,1,0,0,1,0.0,"{""runtime_error"": 1}","{""compile_only"": 1}"
ts_one_step,"{""representation"": ""flat"", ""witness_status"": ""valid""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
ts_one_step,"{""representation"": ""reflective"", ""witness_status"": ""broken""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
ts_one_step,"{""representation"": ""reflective"", ""witness_status"": ""valid""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
ts_parse_only,"{""representation"": ""flat"", ""witness_status"": ""broken""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
ts_parse_only,"{""representation"": ""flat"", ""witness_status"": ""valid""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
ts_parse_only,"{""representation"": ""reflective"", ""witness_status"": ""broken""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
ts_parse_only,"{""representation"": ""reflective"", ""witness_status"": ""valid""}",1,1,0,1,0,1.0,{},"{""compile_only"": 1}"
ts_trajectory,"{""representation"": ""flat"", ""witness_status"": ""broken""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
ts_trajectory,"{""representation"": ""flat"", ""witness_status"": ""valid""}",1,1,0,0,1,0.0,"{""runtime_error"": 1}","{""compile_only"": 1}"
ts_trajectory,"{""representation"": ""reflective"", ""witness_status"": ""broken""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"
ts_trajectory,"{""representation"": ""reflective"", ""witness_status"": ""valid""}",1,1,0,0,1,0.0,"{""underfit"": 1}","{""compile_only"": 1}"

<END SOURCE COMPLETE_DIFFICULTY_MATRIX_CSV>

<BEGIN SOURCE CAMPAIGN_PROVENANCE>
# Evidence provenance and reconstruction rules (Mercury)

## 1. Primary archive identity

| Item | Value |
|---|---|
| Archive | `mercury-pairwise-state-38873207827.zip` |
| Git blob SHA-1 | `b96d00d3206929da5089ca63b75b667639e87ebc` (verified) |
| ZIP size | 10,580,748 bytes |
| ZIP SHA-256 | `ece98bcf1cfd53dd24625c43da5e647aa63a5fac645603976c1213bdbd9af389` |
| ZIP members | 5,129 |
| Root-level members | 29 |
| Campaign source commit | `ea827277d42a714d4cd9760f4a4930ab5237e6de` (dirty=true) |
| Model | `mercury-2.5` (reasoning_effort=high, reasoning_enabled=true) |
| Provider | mercury / https://api.inceptionlabs.ai/v1 |

The archive was read in place; no member changed. SHA-256 computed by `reconstruct_campaign.py`.

## 2. Reconstruction

Script: `campaign-02-analysis/evidence/reconstruct_campaign.py` (adapted from Atria's `campaign-01-analysis/evidence/reconstruct_campaign.py`; run_dir prefix changed to `runs/mercury_pairwise_campaign/`, unscored cases handled, Mercury fields `pair_id`, `interventions`, `generation_id` carried).

Generated tables in `evidence/generated/`: archive_inventory.csv, campaign_exclusions.csv, case_results.csv, run_attempts.csv, trace_index.csv, failure_details.csv, environment_summary.csv, track_summary.csv, analysis_family_summary.csv, axis_summary.csv, failure_taxonomy.csv, config_hash_audit.csv, audit.json.

## 3. Scope

- 416 selected case IDs; 405 scored, 11 infrastructure_unscored.
- 189 behavioral_reference (gated), 227 compile_only.
- Omissions: 10 rope cases (provider input modality unsupported), 24 known gate-blocked cases, 56 intervention-twin omissions (unverified).
- Provider outage: one recorded case `ts_parse_only__witness_status=broken_representation=flat__seed-0` (1 retry, 60s).

## 4. Limits

- Source repository dirty at run; config hashes not compared (no clean source snapshot available in this environment) — config_hash_audit.csv has 0 checked.
- Reasoning content not copied (only counts).
- No independent rerun of the campaign; all figures reproduced from archived records.

<END SOURCE CAMPAIGN_PROVENANCE>

<BEGIN SOURCE EARLIER_ANALYSIS_OVERVIEW>
# Mercury-2.5 cross-environment difficulty analysis — overview

Primary question: How does Mercury-2.5's behaviour vary across environments and difficulty tuples?

## Dimensions
- 38 environments, 340 distinct environment × difficulty-tuple rows, 416 selected cases (405 scored, 11 unscored).
- Difficulty is multi-dimensional per environment (e.g. naming × symptom_mask; hidden_depth × surface_deceptiveness); not a single scalar.
- Outcomes: PASS/FAIL/unscored, failure_mode, score, plus epistemic-game posterior/verdict.

## Key patterns
1. Bimodal environment difficulty: 10 environments at 0.00 pass rate (glyph, functorial_augmentation, monadic_reward, sheaf_*, ts_one_step, ts_trajectory) vs ~12 at 1.00.
2. Failure modes: underfit (51) and overfit_visible_tests (49) dominate; source_invalid (9), runtime (11), invalid_action (5), training_failed (3).
3. Difficulty transitions are non-monotonic in several environments (e.g. MoCo visible-test levels pass/fail/pass).
4. Proxy interventions (visible_proxy, reward_proxy) cut pass rates to 0.30/0.25.
5. Belief computation exact (23/23) while decisions fragile — supporting diagnostic, not headline.

## Visualisations
- environment_difficulty_matrix.csv (340 rows)
- environment_summary_v2.csv (38 rows)

<END SOURCE EARLIER_ANALYSIS_OVERVIEW>

<BEGIN SOURCE INELIGIBLE_PASS_CSV_EXCERPT>
case_id,environment,track,analysis_family,track_label_overridden_for_analysis,seed,difficulty_levels,config_path,config_sha256,judge_guarantee,status,verdict,score,failure_mode_raw,failure_mode_normalized,interventions,pair_id,pair_id_basis,generation_id,family,case_disposition,stage_statuses,final_notes,final_metrics,returncode,elapsed_seconds,http_attempts_result,http_attempt_ceiling_result,reasoning_enabled,performance_eligible,exclusion_reason,run_id,run_member_prefix,result_member,final_member,manifest_member,response_member,prompt_tokens_final_run,completion_tokens_final_run,total_tokens_final_run
ts_parse_only__witness_status=broken_representation=flat__seed-0,ts_parse_only,trajectory_solver_synthesis,trajectory_solver_synthesis,False,0,"{""representation"": ""flat"", ""witness_status"": ""broken""}",envs/trajectory_semantics/parse_only/config.yaml,53816a7d544de28c65a50a775f7d42d729f87bf5a0114de03ac6d908212440b8,compile_only,scored,PASS,1.0,pass,pass,[],P965681a0a939d6dd,latent_spec,G6dedadba4e84d060,,scored,"{""behavioral_evaluation"": ""scored_pass"", ""judge_execution"": ""passed"", ""patch_validation"": ""passed"", ""provider_transport"": ""completed_with_errors"", ""required_artifacts"": ""passed"", ""response_parsing"": ""passed"", ""runtime_execution"": ""unknown"", ""source_validation"": ""passed""}",[],"{""query_type"": ""parse_only"", ""track"": ""solver_synthesis_debugging""}",0,46.101,19,240,True,False,campaign report provider-outage case; final result explicitly attributes terminal failure to provider transient after bounded retries,ts_parse_only-20261016T111739Z-40975e49,episodes/ts_parse_only__witness_status=broken_representation=flat__seed-0/ts_parse_only-20261016T111739Z-40975e49/,suite_checkpoint.json#/results/ts_parse_only__witness_status=broken_representation=flat__seed-0,episodes/ts_parse_only__witness_status=broken_representation=flat__seed-0/ts_parse_only-20261016T111739Z-40975e49/final.json,episodes/ts_parse_only__witness_status=broken_representation=flat__seed-0/ts_parse_only-20261016T111739Z-40975e49/manifest.json,episodes/ts_parse_only__witness_status=broken_representation=flat__seed-0/ts_parse_only-20261016T111739Z-40975e49/model_responses.jsonl,11926,12935,24861

<END SOURCE INELIGIBLE_PASS_CSV_EXCERPT>


<BEGIN SOURCE CURRENT_INTERNAL_ARTICLE>
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

<END SOURCE CURRENT_INTERNAL_ARTICLE>

<BEGIN SOURCE HOUSE_STYLE>
# StrangeTcy house style: operational guide for these five research posts

## Source inspected

The source of truth is the public Jekyll site, [`StrangeTcy/strangetcy.github.io`](https://github.com/StrangeTcy/strangetcy.github.io), inspected at commit `bcc89c392920b3be172a27eec10ad205b58d4fa3` on 2026-10-03. This guide is based on the requested post, [“The Diagram Is the Spec”](https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-27-the-diagram-in-the-spec.md), and cross-checks against “Knowing What Kind of Problem You Are In” (2026-09-26), “The Next Question Is Part of the Game” (2026-09-30), “Lying With Truth” (2026-10-01), “A Long Trajectory Is Not Necessarily Deep Reasoning” (2026-09-11), and “Controlling Scheming AIs Giving Strategic Advice” (2026-08-31). These examples were inspected before this guide was written. The last two are useful counterexamples to any claim that there is a single fixed post length or one rigid template.

This is an editorial grammar, not a phrase bank. The new articles should inherit the site's movement between intuition, technical structure, self-correction, and bounded claims; they should not reuse distinctive sentences, metaphors, or openings from the source posts.

## 1. Jekyll frontmatter and includes

The Jekyll site uses the `pages-themes/hacker@v0.2.0` remote theme in `_config.yml`; the recent posts themselves use `layout: post`. They use deliberately spare YAML frontmatter:

```yaml
---
title: "A Sentence-Case or Title-Case Article Title"
date: 2026-10-03
layout: post
---
```

`title`, `date`, and `layout: post` are the recurring fields. The inspected technical posts do not add tags, categories, summaries, or author metadata to frontmatter. Do not invent additional Jekyll fields for these files.

When an article contains inline or display mathematics, put `{% include mathjax.html %}` immediately after the frontmatter and before the byline. This is the include used by the inspected technical posts; `_includes/mathjax.html` is the site's MathJax loader. No other include is needed for the five essays.

The common byline is:

```html
*by <span class="icon-self">StrangeTcy</span>*
```

Recent posts then use an HTML definition list, not a Markdown callout, for epistemic status:

```html
<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>...</dd>
  <dt>Synthesis</dt>
  <dd>...</dd>
  <dt>Prose</dt>
  <dd>...</dd>
  <dt>Certainty</dt>
  <dd>...</dd>
  <dt>Importance</dt>
  <dd>...</dd>
</dl>
```

Preserve the five fields and their order. The HTML block is a compact disclosure about intellectual sources, synthesis/prose, confidence, and why the post matters. In these new drafts, its prose attribution must describe the actual role-separated Arena writing process accurately; it must not imply that two external models or independent human writers participated. Do not turn the disclosure into an internal audit log.

Other inline HTML in the sample includes `<span class="icon-self">`, source/model icon spans, and occasional `<em>`, `<code>`, or `<sup>` elements. Use HTML only where the site's existing styling needs it. There are no custom figure, table, or callout components in the surveyed 2026 research posts.

## 2. Headings and section numbering

- The main body begins without an `Introduction` heading. It opens in prose, often with a short declarative sentence or a compact scene/problem.
- `##` headings mark substantial argumentative turns. They are usually short, specific, and phrased as questions, claims, or objects (“The moving hole”; “What should count as harm?”), not generic report labels.
- Numbered sections are optional, not a house-wide requirement. “The Diagram Is the Spec” uses `## 1 — ...` for a sequence of mathematical examples, but the adjacent posts use unnumbered headings. Use numbering only when the sections really are a sequence of parallel mechanisms; do not number every stage of an essay to make it look systematic.
- `###` is used for subordinate topics or experiment variants. Avoid heading depth beyond that unless the article genuinely needs it.
- The ending usually returns to the central question and states what the idea does and does not license. A “Conclusion” heading is not necessary.

## 3. Length, paragraph density, and pacing

The recent conceptual/research posts are not a fixed word-count format: the inspected set ranges from about 1,800 words (“Lying With Truth”) through roughly 2,800–3,300 words (“The Diagram Is the Spec,” “Knowing What Kind of Problem You Are In,” “The Next Question Is Part of the Game,” and “Controlling Scheming AIs Giving Strategic Advice”) to an intentionally expansive 7,700-word treatment of recurrent depth. The requested target post is about 2,800 words. For these five linked campaign essays, a complete 1,800–2,800-word article fits the observed recent range; longer treatment is warranted where the mechanism needs it. The target's open paragraphing and argumentative development matter more than a threshold. Do not inflate a post to hit a quota.

Paragraphs are visually airy. Most carry one to four sentences; a sentence can stand alone when it marks a conceptual turn. Lists, short equation displays, and occasional one-line contrasts make technical material readable. The rhythm is not “paragraph, citation, paragraph, citation” but a paced alternation between explanation and consequence. A finished piece can be information-dense without reading as a memo.

## 4. Voice and rhetorical moves

The voice is first-person, curious, technically literate, and willing to show its own revision. It is confident about what was inspected and cautious about what the evidence can support. The author can say that an initial idea was wrong, explain why it seemed attractive, and keep the useful part after narrowing the claim. This self-correction is more characteristic than a neutral, impersonal “we evaluate” register.

Rhetorical questions are frequent but purposeful. They open a problem, isolate an ambiguity, or expose a hidden assumption; the next few paragraphs should answer them. Questions such as “what exactly does this measure?” create forward motion. Do not use question marks as a substitute for an argument.

Short contrasts are a recurring device: two variables that sound alike are separated (“rollout length” versus “necessary computation”; “belief displacement” versus “inquiry damage”), then the distinction is given an operational consequence. Use this structure when it clarifies the five topics, not as a repeated formula in every section. Bold is used to mark a thesis or a crucial contrast; italics add local stress rather than substituting for a definition. The author sometimes uses an ampersand in running prose, and occasionally a smiley or emoji as a dry aside. These are recognizable tendencies, not mandatory tokens; use them lightly and do not reproduce a source post's exact line.

Dry humour, self-deprecation, and occasional parenthetical asides are present, but they are intermittent. A small aside can release pressure after a dense point; it should not turn the post into a performance of quirkiness. Profanity exists in some recent writing, including technical prose, but it is an emphatic exception rather than mandatory seasoning. Do not borrow a memorable joke or a distinctive turn of phrase from the source posts.

## 5. Quotations, citations, and links

- Inline Markdown links are the default for papers, named concepts, prior work, and source repositories: `[VarBench](https://...)`.
- Citations are integrated at the point where the source matters. A short “References” section is used when a post has several sources; otherwise a compact inline citation or footnote can suffice. The site does not require a formal author–year style or a numbered bibliography in every post.
- Use blockquotes sparingly for a thesis, a source's consequential formulation, or an experiment's exact claim. The post often quotes a sentence, then interprets it; it does not paste source material as a substitute for analysis.
- Quote only text verified in the linked source. Keep quoted material short and distinguish quotations from paraphrase. Do not cite the blog itself as evidence for campaign results.
- Link to external prior work for conceptual lineage, not as a prestige list. State what each cited item contributes and where it is not a direct comparator.

## 6. Equations, diagrams, and tables

The technical posts use MathJax. Inline expressions use `$...$`; standalone equations use `$$...$$`. The target post frequently expresses commutative diagrams with `\begin{array}` inside display math, then spells out the engineering interpretation in ordinary prose. Other posts use a few equations to make a definition inspectable, not to decorate an assertion.

A diagram must be mathematically and operationally well-typed. State what each symbol means; explain what a failure of the law would look like in code or in the judge. If a full commutative square would overstate the implementation, use a simple equation, a two-column text diagram, or no diagram. The source post's standard is exactness, not ornament.

Tables are occasional and compact. They are useful when they preserve distinctions that a paragraph would blur (e.g., evidence strength by target response, or task claim by actual judge check). They are not the default way to display every result. A table must have explicit row/column meaning and cannot imply a common scale where the campaign did not establish one.

Plain fenced `text` diagrams appear in longer posts for flows or alternative mechanisms. Mermaid, embedded images, and elaborate HTML graphics were not present in the surveyed 2026 research posts; do not add new rendering dependencies.

## 7. Caveats and evidence in the narrative

Caveats appear at the point where an attractive interpretation would otherwise outrun the evidence. The usual move is: state the interesting observation, name the alternative explanation or judge limit immediately, and retain the narrower conclusion. Do not push every limitation into an apologetic final paragraph, and do not interrupt every sentence with a disclaimer.

For this campaign, keep the major constraints close to the evidence they qualify: one selected seed-0 run per cell; mixed `behavioral_reference` and `compile_only` judging; the explicitly exploratory status of compile-only results; two provider-transient terminal rows and the denominator sensitivity; `repository.dirty=true` for all source-comparator claims; implementation/judge defects and static-axis placeholders where relevant; and sequential Council role passes by one Arena model, not independent replications. Do not promote epistemic games to recursive theory of mind, compile checks to behavioral validation, one observed pattern to a causal law, or a task-family count to a general capability score.

The old evidence-marker system remains in its separate traceability files. Public prose must not contain its markers, claim IDs, internal post IDs, editorial notes, or data-extraction instructions.

## 8. A finished post versus an internal memo

An internal memo leads with denominators, evidence tags, source paths, and a list of guardrails. A finished StrangeTcy post begins with an idea a reader can hold in their head, uses a concrete mechanism or example to earn the abstraction, and lets the evidence alter the argument. It still gives exact numbers where they matter, but each number answers a question the essay has already made meaningful. It introduces prior work in relation to the claim rather than stacking references. It uses first-person judgement and self-correction without inventing personal experiences. It ends with a bounded research consequence: what one should test next, what a result would mean, or what the current evidence cannot decide.

For this series the desired progression is: **an intelligible puzzle → the mechanism or mathematical object → a concrete case → what the audited evidence actually says → the strongest counterargument/limitation → the next experiment or research consequence**. Each essay may choose its own order and narrative device. None should read like a benchmark table with prose inserted between rows.

<END SOURCE HOUSE_STYLE>

<BEGIN SOURCE ACTUAL_REFERENCE_POST_EXCERPTS>
# Actual StrangeTcy reference-post excerpts for the post-production workflow

Source repository: [StrangeTcy/strangetcy.github.io](https://github.com/StrangeTcy/strangetcy.github.io)
Source revision: `bcc89c392920b3be172a27eec10ad205b58d4fa3` (checked out for this extraction on 2026-10-03).
The excerpts below are contiguous source text reproduced verbatim, with only the excerpt boundary lines omitted. They are provided as style evidence—not phrases to reuse. Use their structural grammar, paragraph movement, first-person judgment, technical explanation, and claim-bounding; do not copy distinctive wording, examples, or openings.
The original epistemic-status blocks describe the source posts' authorship, not this workflow. Never copy those attribution claims into a new post; use the project-approved attribution in the generated draft.

## The Diagram Is the Spec — Jekyll frame and opening
Source: `2026-09-27-the-diagram-in-the-spec.md`, lines 1–48; full-file SHA-256 `7ae29e22aec58a22f0bdd68b75ddc6012e3beea30c3413d594c24ccd8160d9d4`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-27-the-diagram-in-the-spec.md

```markdown
---

title: "The Diagram Is the Spec"
date: 2026-09-27
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Category theory as a source of implementation constraints rather than vocabulary; the use of algebraic laws as held-out behavioural specifications; sheaf conditions as local-to-global consistency. The packaging into agent environments is mine.</dd>

  <dt>Synthesis</dt>
  <dd><span class="icon-self">StrangeTcy</span></dd>

  <dt>Prose</dt>
  <dd>Several models (<span class="icon-openai">gpt</span>span and <span class="icon-anthropic">claude</span> mostly), from the dialogue &amp; successive rounds of criticism; final edit <span class="icon-self">StrangeTcy</span></dd>

  <dt>Certainty</dt>
  <dd>Confident about the executable design described here &amp; the mathematical laws illustrated below. Exploratory about what frontier models will do on the resulting environments. No model results yet.</dd>

  <dt>Importance</dt>
  <dd>A design post for the <code>cat_theo/*</code> family in <a href="https://github.com/StrangeTcy/rl_eval_generator">rl_eval_generator</a>. Companion to the broader evaluation framing; this post is about the category-theoretic family itself.</dd>
</dl>

I did not build these environments because I wanted agents to recite the [Yoneda lemma](https://en.wikipedia.org/wiki/Yoneda_lemma).

I built them because a large class of ML bugs are **failed diagrams**.

Two computations that ought to be the same composite, traversed two ways, do not agree. A transform that should commute with a symmetry does not. A get/put pair behaves correctly once & breaks on the second update. A parallel scan works on the lengths somebody tested & fails when the tree of compositions changes.

The surface of the code _looks like_ ordinary engineering.

The failure is algebraic.

And that gives me a rather nice way to write an evaluation environment:

> **Make the law the specification, then vary the concrete instance.**

This is one of the reasons I like category theory here. The laws are often small enough to draw.

And the diagrams are pretty :D

That is not entirely a joke.
```

## The Diagram Is the Spec — From principle to equation and judge
Source: `2026-09-27-the-diagram-in-the-spec.md`, lines 69–108; full-file SHA-256 `7ae29e22aec58a22f0bdd68b75ddc6012e3beea30c3413d594c24ccd8160d9d4`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-27-the-diagram-in-the-spec.md

```markdown
## Why diagrams, not unit tests

A unit test says:

> On these inputs, produce these outputs.

A diagram says:

> **These two paths are the same morphism.**

For a natural transformation $\eta:F\Rightarrow G$,

$$
\large
\begin{array}{ccccc}
F(A) & \xrightarrow{\ F(f)\ } & F(B) \\
\big\downarrow{ \eta_A} & & \big\downarrow{ \eta_B} \\
G(A) & \xrightarrow{\ G(f)\ } & G(B)
\end{array}
$$

The square commutes when

$$
\eta_B\circ F(f)=G(f)\circ\eta_A.
$$

That equation does something a unit test does not: it says what should remain true when the concrete objects change.

The evaluator can therefore change the sequence length, the group element, the batching, the chunking, the parenthesisation, or the generated instance without changing the law being tested.

The visible tests are one sample of the diagram.

The held-out judge is another.

```text
surface reading of the code
            ≠
operative law in the judge
```
```

## The Diagram Is the Spec — Bounded ending
Source: `2026-09-27-the-diagram-in-the-spec.md`, lines 698–717; full-file SHA-256 `7ae29e22aec58a22f0bdd68b75ddc6012e3beea30c3413d594c24ccd8160d9d4`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-27-the-diagram-in-the-spec.md

```markdown
## What this is not

It is not a claim that frontier models fail these tasks.

It is not a claim that category theory is necessary for ML engineering.

It is not [a course in category theory](https://www.youtube.com/playlist?list=PLbgaMIhjbmEnaH_LTkxLI7FMa2HsnawM_).

And it is not yet a claim that this suite measures pure law recognition. Some environments hand the law over explicitly. Some hide the terminology. A genuinely clean recognition experiment would require an additional generator axis which removes the law statement itself while leaving the executable problem unchanged.

The claim I can make now is narrower:

> **A useful slice of structural competence can be operationalised as: hold a small diagram constant, vary its concrete instance procedurally, and score the diagram rather than the surface output.**

That is what `cat_theo` is for.

The results will tell me whether the agents can do it.

For now, I mostly wanted the diagrams on the page 😆
```

## Knowing What Kind of Problem You Are In — Conceptual opening and skeptical objection
Source: `2026-09-26-knowing-what-kind-of-problem-you-are-in.md`, lines 1–52; full-file SHA-256 `aed1d48abb3d803bd4db8ec9b1a2435beb6a41a681db19ef95755ec00910c047`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-26-knowing-what-kind-of-problem-you-are-in.md

```markdown
---
title: "Knowing What Kind of Problem You Are In"
date: 2026-09-26
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd> <a href="https://en.wikipedia.org/wiki/Category_theory">Category theory</a> as a source of implementation constraints; <a href="https://gwern.net">Gwern</a> on weird machines; Juan Tamariz on false solutions; recent work on <a href="https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and">recurrent depth</a> &amp; non-verbalised reasoning; a long-standing interest in <a href="https://www.amazon.com/dp/1107008913?lv=shuf&channelId=500&plpRedirect=mhFallback">epistemic games</a>. The synthesis into a single evaluation question came out of a dialogue with <span class="icon-openai">ChatGPT</span> and <span class="icon-anthropic">Claude</span>. 
  </dd>
  <dt>Synthesis</dt>
  <dd><span class="icon-self">StrangeTcy</span></dd>

  <dt>Prose</dt>
  <dd>Several models, from the dialogue &amp; successive rounds of criticism; final edit <span class="icon-self">StrangeTcy</span></dd>

  <dt>Certainty</dt>
  <dd>Confident that solving a problem &amp; identifying what kind of problem one is in are separable abilities, &amp; that current benchmarks mostly measure the first. Exploratory about whether the environments described here measure the second. Predictions at the end are registered before any run.</dd>

  <dt>Importance</dt>
  <dd>A framing post. The generator exists; the numbers do not yet.</dd>
</dl>

Most benchmarks hand the agent its context for free.

Not deliberately. It is what happens when you collect tasks: each one arrives already classified. *This is a Python bug, fix it. This is a competition problem, solve it. This is a paper, reproduce it.* The agent is rarely asked to determine what sort of situation it has walked into before deciding how to act, because the first line of the prompt has already told it.

That gift does more work than we credit. A problem is not just an input paired with an answer; before the solving there is a prior question — which description of the situation should govern the solution? A function can look ordinary while secretly needing to satisfy an invariant. A stylesheet can look like a stylesheet while containing a machine. A training run can look like a familiar optimisation failure while the familiar diagnosis is false. A codebase can contain every tool needed to find the bug while leaving unstated which observation matters. In each case the agent can do something locally reasonable without ever discovering what kind of situation it is in, & everything downstream is fluent, confident & useless.

So the question I have been building environments around is: **can an agent work out what kind of problem it is in, before it starts confidently solving the wrong one?**

Four families ask it from four sides. They share one shape — a plausible surface reading, an operative structure the surface does not state, a locally sensible action that is wrong, & a held-out behavioural test that exposes the difference. What differs is what is hidden: a law, an execution semantics, a causal structure, or the location of the missing evidence.

## First, the objection

The obvious version of this thesis is "strip the vocabulary & the models fall over", & the obvious version is probably wrong. ARC-style tasks already require inducing a rule from object-level instances with nothing to retrieve against, & the scores there do not support a story in which de-naming alone is fatal. If the claim were that removing *monoid* or *equivariant* makes models crater, the counter-evidence exists.

The claim is narrower. [ARC](https://arcprize.org/arc-agi) tells you, by construction, that a rule exists & that finding it is the task. My [environments](https://github.com/StrangeTcy/rl_eval_generator) present a working system whose surface interpretation is perfectly plausible, & ask whether the agent notices that the obvious description is not the operative one — under time pressure, with a runnable test suite offering the constant temptation to stop thinking & start iterating. **Rule induction after being told that a rule is the task is not the same capability as noticing that the situation calls for rule induction.** That distinction is the whole post. If it turns out not to be real, I would like to find that out.

## Which laws does it identify?

The algebraic tasks have [category-theoretic structure underneath](https://github.com/StrangeTcy/rl_eval_generator/tree/main/envs/cat_theo) but do not ask the agent to know any category theory. They ask for an implementation that satisfies a law it was never given. An operation must commute with a group action. A mapping must stay natural as sequence length changes. Two pipelines that should be the same diagram, traversed two ways, must agree. A get/put pair must still behave like a lens once state has been threaded through it. The agent is not tested on whether it knows the name of the law; it is tested on whether it notices the law is there.

The smallest instance: a [CNN](https://en.wikipedia.org/wiki/Convolutional_neural_network) classifies glyphs. It trains, the loss falls, the visible tests pass. The classifier head is spatially sensitive — it works when the glyph sits where the training data put it & fails when the glyph moves. Nothing in the code says *invariant*; nothing in the task says *translation*. The agent has to look at what the task *is* & conclude that the model is obliged to satisfy a symmetry it currently violates. In the harder variant a second fault in the optimiser prevents convergence altogether, so that fixing it makes the model train & feels like progress while leaving the actual problem untouched.

This is why the presentations are de-named. Write [`Monoid`](https://en.wikipedia.org/wiki/Monoid_(category_theory)) on the class or `equivariant` in a comment & you have told the agent which shelf to reach for; useful for many purposes, but not the experiment. Per the objection above, I expect de-naming by itself to be the smaller effect, & the absence of any prompt to look for a law at all to be the larger one. The experiment that separates them is cheap: named, de-named, de-named with irrelevant terminology, same seeds, same judge.

## Which execution semantics does it see?
```

## The Next Question Is Part of the Game — A question-led opening and trajectory model
Source: `2026-09-30-the-next-question-is-part-of-the-game.md`, lines 1–94; full-file SHA-256 `1497b33ec3b79717cf5df4d49caa07aa0cc5fa9a065b9f327af44b821484dc07`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-09-30-the-next-question-is-part-of-the-game.md

```markdown
---

title: "The Next Question Is Part of the Game"
date: 2026-09-30
layout: post
---


{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>
    Evaluating control over another agent's inquiry trajectory rather than only its
    final beliefs; treating magic-style misdirection as a small, experimentally
    tractable instance; separating attention, information acquisition, source trust,
    hypothesis framing, belief revision &amp; opponent modelling instead of arranging
    them into one capability ladder.
  </dd>

  <dt>Synthesis</dt>
  <dd><span class="icon-self">StrangeTcy</span></dd>

  <dt>Prose</dt>
  <dd>
    Developed through dialogues with several models, criticised by further models,
    & edited <span class="icon-self">StrangeTcy</span>.
  </dd>

  <dt>Certainty</dt>
  <dd>
    Confident that the choice of what to investigate next is a strategically important,
    behaviourally observable variable that is poorly represented by final-answer
    accuracy alone. Less confident that any one intervention cleanly identifies an
    internal reasoning mechanism. No model results yet.
  </dd>

  <dt>Importance</dt>
  <dd>
    A research-direction post for the next generation of
    <a href="https://github.com/StrangeTcy/rl_eval_generator">rl_eval_generator</a>.
    The existing suite remains the baseline; this describes what should come after it.
  </dd>
</dl>

Suppose I want you to make the wrong decision.

The stupid way is to lie to you; the more interesting way is to make you run the wrong experiment.

I don't need to convince you that the machine is healthy if I can make you spend
your diagnostic budget measuring the optimiser while the representation collapses.
I don't need to make you believe a particular false proposition if I can determine
which source you consult, which hypothesis you test first, or which anomaly you
dismiss as irrelevant.

The strategic object is no longer just your current answer -- it's your **next question**.

## From false beliefs to epistemic trajectories

The standard toy picture of deception is propositional:

$$
A \longrightarrow \text{false belief }P\text{ in }B.
$$

Alice knows where the object is. Bob does not. Alice sends a misleading signal.
Bob believes the object is in the wrong place.

This is a useful abstraction. It is also a drastic compression of what an
investigator fuckingly does:

An investigator does not normally go straight from observation to answer --  it follows
a trajectory:

$$
\text{observation}
\rightarrow
\text{attention}
\rightarrow
\text{information acquisition}
\rightarrow
\text{hypothesis generation}
\rightarrow
\text{belief revision}
\rightarrow
\text{next investigation}
\rightarrow
\text{action}.
$$

An intervention can affect any of these transitions without immediately determining
the final answer.
```

## Lying With Truth — Visible self-correction and compact contrast table
Source: `2026-10-01-lying-with-truth.md`, lines 1–77; full-file SHA-256 `3ad67e221bfbf5168737bfcc00d53e06bf1dbda59667acc9c741c1056bd2affa`.
URL: https://github.com/StrangeTcy/strangetcy.github.io/blob/bcc89c392920b3be172a27eec10ad205b58d4fa3/_posts/2026-10-01-lying-with-truth.md

```markdown
---

title: "Lying With Truth"
date: 2026-10-01
layout: post
---


{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Treating a bounded, strictly-true intervention chosen to degrade later inquiry as a candidate eval class; separating belief displacement from epistemic damage.</dd>

  <dt>Synthesis</dt>
  <dd><span class="icon-self">StrangeTcy</span></dd>

  <dt>Certainty</dt>
  <dd>Confident that truthfulness ≠ neutrality, and that large belief revision is not itself evidence of harm. Exploratory about whether “desontological attack” is a useful label beyond the terminology described here.</dd>

  <dt>Importance</dt>
  <dd>Defines one truthful-intervention family and the controls it needs, so it cannot quietly turn into “another deception benchmark.”</dd>
</dl>

The first formalisation was wrong.

I modelled a world-model as a graph $G$ & looked for a message $m$ maximising $D\big(G,\mathrm{Update}(G,m)\big)$: the bigger the change, the stronger the attack.

That's backwards.

A short, decisive true observation *should* demolish a bad theory. An excellent reasoner undergoes violent revision on purpose. If a physicist has a beautiful theory and then someone produces a clean experiment that kills it, “the model changed a lot” is not evidence that the experiment was an attack.

It is evidence that the experiment worked.

So there are two different things to measure:

**displacement** — how much the target's beliefs changed;

**damage** — whether the target's subsequent reasoning became worse.

Those are not the same variable.

In the little instrument I am building, the former is essentially blind: the measured displacement statistic $\beth$ stays around $\log_2(8/3)$ across the helpful and adversarial conditions. Whatever it measures, it does not tell us whether the intervention helped or harmed the target.

The interesting question is what happened *after* the change.

## The provocation

There is a useful phrase for the thing I am trying to isolate.

Evgeny Gilbo uses the term **дезонтологическая атака** — literally, a “deontological” or “desontological” attack, in the sense of an intervention aimed not merely at changing a particular belief but at disrupting the opponent's picture of what the world is.

I am using that terminology here as a design prompt, not as established academic terminology.

The striking version of the idea uses information that is completely true.

Tell a Stalinist that Stalin was short and pockmarked.

To a historian, this is trivia. To someone whose image of Stalin is entangled with a heroic or idealised picture of him, the same fact could have a rather different effect.

The proposed mechanism is not:

$\text{true information} \rightarrow \text{false belief}$

It is:

$\text{selected truth} \rightarrow \text{destabilised interpretation} \rightarrow \text{degraded inquiry}$

But *could* is doing almost all the work in that sentence.

A person can learn an embarrassing fact about Stalin and simply continue believing everything they believed before. The example demonstrates a possible lever, not a mechanism.

That gap is exactly what an evaluation is for.

## Truthfulness is not neutrality
```

<END SOURCE ACTUAL_REFERENCE_POST_EXCERPTS>

<BEGIN SOURCE PRIOR_WORK_REFERENCES>
# Prior-work references used in Campaign 01

These sources are cited only for the scope stated here. They do not validate the Atria campaign's own task implementations or results.

1. Percy Liang et al. “Holistic Evaluation of Language Models.” *Transactions on Machine Learning Research*, 2023. [Paper](https://arxiv.org/abs/2211.09110). Used as precedent for broad scenario coverage, multiple metrics, standardized evaluation, and transparency: the paper reports 42 scenarios across 30 models and measures seven metrics for its core scenarios when possible. It is not a direct comparator for this code-repair campaign.
2. Kun Qian et al. “VarBench: Robust Language Model Benchmarking Through Dynamic Variable Perturbation.” *Findings of EMNLP 2024*, pp. 16131–16161. [ACL Anthology](https://aclanthology.org/2024.findings-emnlp.946/) · [DOI](https://doi.org/10.18653/v1/2024.findings-emnlp.946). Used to bound claims of novelty for controlled variable perturbations and repeated dynamic test generation. For variable-based experiments, the paper reports five runs with different sampled values, using random seeds 40–44.
3. Damien Sileo and Antoine Lernould. “MindGames: Targeting Theory of Mind in Large Language Models with Dynamic Epistemic Modal Logic.” *Findings of EMNLP 2023*, pp. 4570–4577. [ACL Anthology](https://aclanthology.org/2023.findings-emnlp.303/) · [DOI](https://doi.org/10.18653/v1/2023.findings-emnlp.303). Used as prior work on controlled epistemic-logic ToM problems and natural-language verbalization.
4. Yufan Wu, Yinghui He, Yilin Jia, Rada Mihalcea, Yulong Chen, and Naihao Deng. “Hi-ToM: A Benchmark for Evaluating Higher-Order Theory of Mind Reasoning in Large Language Models.” *Findings of EMNLP 2023*, pp. 10691–10706. [ACL Anthology](https://aclanthology.org/2023.findings-emnlp.717/) · [DOI](https://doi.org/10.18653/v1/2023.findings-emnlp.717). Used to distinguish this campaign's stipulated Bayesian policies from explicit higher-order recursive belief and deception evaluation.
5. Kanishk Gandhi, J.-Philipp Fränken, Tobias Gerstenberg, and Noah D. Goodman. “Understanding Social Reasoning in Language Models with Language Models.” *NeurIPS 2023 Datasets and Benchmarks*. [Proceedings PDF](https://proceedings.neurips.cc/paper_files/paper/2023/file/2b9efb085d3829a2aadffab63ba206de-Paper-Datasets_and_Benchmarks.pdf). Used as precedent for causal-template-generated ToM evaluations and controlled conditions.
6. You Wang, Michael Pradel, and Zhongxin Liu. “Are ‘Solved Issues’ in SWE-bench Really Solved Correctly? An Empirical Study.” [Publisher page and DOI](https://dl.acm.org/doi/10.1145/3744916.3764576). Used only as a prior caution that test-based patch validation may accept behaviorally incorrect patches in the studied SWE-bench Verified setting: the study reports 7.8% of plausible patches counted correct by benchmark validation failing the full developer-written test suite. Its percentage is not projected onto this campaign.

## Citation discipline

- No “first” or exhaustive-novelty statement is supported by this targeted reference set.
- The SWE-bench study's 7.8% finding is specific to its studied patches and test protocol, not a rate estimate for `rl_eval_generator`.
- MindGames, Hi-ToM, and BigToM differ from `epistemic_games`; their relevance is that controlled epistemic/ToM benchmarking predates this campaign, while the campaign's own source explicitly limits its target to Bayesian inference over stipulated policies.

<END SOURCE PRIOR_WORK_REFERENCES>
