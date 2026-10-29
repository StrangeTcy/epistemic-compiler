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

<BEGIN SOURCE SUPPORTING_LOCAL_SOURCE_CHECK>
# Mercury POST-02 — supporting source check, 2026-10-29

This is local arithmetic and field verification, not an Arena review, a new evaluation run, or a final article validation. The accompanying JSON preserves input hashes, environment aggregates, failure/guarantee cross-tabs, exact flagged case IDs, and omission counts. Source files were read without alteration using PowerShell CSV parsing.

## Verified counts

| Quantity | Verified value |
|---|---:|
| Selected / scored / infrastructure-unscored | 416 / 405 / 11 |
| PASS / FAIL | 277 / 128 |
| Scored-case PASS rate | 68.3951% |
| Selected share with observed PASS | 66.5865% |
| Environments | 38 |
| All-pass / scored zero-pass / mixed / unscored-only environments | 17 / 7 / 12 / 2 |
| Environment-by-tuple rows | 340 |
| Singleton / multi-case rows | 296 / 44 |
| Rows with recorded pass fractions | 329 |
| Endpoint / fractional rows | 320 / 9 |
| Scored zero-pass tuples | 98 |
| Unweighted mean among scored environments | 69.2080% |
| Behavioral-reference scored PASS / scored cases | 141 / 189 |
| Compile-only scored PASS / scored cases | 136 / 216 |
| Distinct omitted case IDs | 80 |

All supplied selected cases have seed 0. Nine scored FAILs carry disposition `unscored`; ten different FAILs carry disposition `rejected`. Their exact case IDs are preserved in the JSON rather than changed or excluded.

Omissions by environment and reason: rope has ten modality omissions and five known-gate omissions; glyph has nine known-gate and twelve intervention-twin omissions; MoCo has 35 intervention-twin omissions; epistemic games has nine intervention-twin omissions. This verifies the detailed rows, not a reconciliation of the historical provenance prose.

## Additional correction for the next review

The drafts describe **214 rows** as belonging to environments where every row has the same outcome. Grouping identical `pass_rate` values reproduces 214 only when blank values are included. The count includes all six `epistemic_silence` rows and all four `epistemic_type_games` rows, which have no scored outcomes.

The supported distinction is **204 rows in environments with uniform scored outcomes, plus ten rows in entirely unscored environments**. Alternatively, 214 can describe a grouping that explicitly includes a shared absence of scored outcomes. It cannot describe 214 observed success/failure outcomes. Trace: complete matrix, all rows in those two environments; the JSON's `uniform_environment_breakdown` and `uniform_scored_environment_rows` retain the calculation.

Carry this to the resumed evidence review and editorial handoff with attribution to this local source check. Do not manufacture an Arena finding or silently modify the preserved candidate responses.

## Scope

The standalone environment-summary CSV was absent from this local snapshot. Environment totals and fractions were therefore derived from the complete tuple matrix. The JSON records this derivation. This check does not verify figure rendering, external sources, raw execution semantics, reviewer completeness, or publication readiness.

<END SOURCE SUPPORTING_LOCAL_SOURCE_CHECK>

<BEGIN SOURCE SUPPORTING_LOCAL_SOURCE_CHECK_JSON>
{
    "stage":  "supporting_source_verification_not_Arena_review",
    "checked_at":  "2026-10-29T13:15:46.7415869Z",
    "source_ref":  "6ed48cb1c4447d4f902d1fbc8a908a56185e34ed",
    "selected":  416,
    "scored":  405,
    "pass":  277,
    "fail":  128,
    "infrastructure_unscored":  11,
    "seed_values":  [
                        "0"
                    ],
    "environment_count":  38,
    "matrix_rows":  340,
    "singleton_rows":  296,
    "multi_case_rows":  44,
    "rated_rows":  329,
    "endpoint_rows":  320,
    "fractional_rows":  9,
    "uniform_environment_rows_including_unscored":  214,
    "uniform_environment_breakdown":  [
                                          {
                                              "Name":  "architecture_naturality",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "categorical_lenses",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "ci_dependency_graph",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "css_state_machine",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "epistemic_announcements",
                                              "Count":  6
                                          },
                                          {
                                              "Name":  "epistemic_fragmented_observation",
                                              "Count":  4
                                          },
                                          {
                                              "Name":  "epistemic_games",
                                              "Count":  8
                                          },
                                          {
                                              "Name":  "epistemic_nested_knowledge",
                                              "Count":  6
                                          },
                                          {
                                              "Name":  "epistemic_silence",
                                              "Count":  6
                                          },
                                          {
                                              "Name":  "epistemic_type_games",
                                              "Count":  4
                                          },
                                          {
                                              "Name":  "functorial_augmentation",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "glyph",
                                              "Count":  12
                                          },
                                          {
                                              "Name":  "monadic_reward",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "neuro_symbolic_parser",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "rd_gradient_credit",
                                              "Count":  15
                                          },
                                          {
                                              "Name":  "rd_state_carry",
                                              "Count":  15
                                          },
                                          {
                                              "Name":  "semiring_unification",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "sheaf_invariant_gluing",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "sheaf_physical_constraints",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "spreadsheet_dataflow",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "stochastic_monad",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "template_interpreter",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "tokenizer_adjunction",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "ts_one_step",
                                              "Count":  4
                                          },
                                          {
                                              "Name":  "ts_parse_only",
                                              "Count":  4
                                          },
                                          {
                                              "Name":  "ts_trajectory",
                                              "Count":  4
                                          }
                                      ],
    "scored_zero_pass_tuples":  98,
    "scored_zero_pass_environments":  7,
    "failure_cross_tab":  [
                              {
                                  "Name":  "batchnorm_ema, overfit_visible_tests",
                                  "Count":  11
                              },
                              {
                                  "Name":  "batchnorm_ema, training_failed",
                                  "Count":  1
                              },
                              {
                                  "Name":  "batchnorm_ema, invalid_action",
                                  "Count":  1
                              },
                              {
                                  "Name":  "compositional_optimizer, underfit",
                                  "Count":  2
                              },
                              {
                                  "Name":  "equivariant_diagram, underfit",
                                  "Count":  1
                              },
                              {
                                  "Name":  "equivariant_diagram, RUNTIME_ERROR",
                                  "Count":  1
                              },
                              {
                                  "Name":  "functorial_augmentation, RUNTIME_ERROR",
                                  "Count":  3
                              },
                              {
                                  "Name":  "functorial_augmentation, underfit",
                                  "Count":  6
                              },
                              {
                                  "Name":  "glyph, overfit_visible_tests",
                                  "Count":  22
                              },
                              {
                                  "Name":  "glyph, underfit",
                                  "Count":  1
                              },
                              {
                                  "Name":  "glyph, invalid_action",
                                  "Count":  1
                              },
                              {
                                  "Name":  "gnn_message_passing, underfit",
                                  "Count":  4
                              },
                              {
                                  "Name":  "moco, overfit_visible_tests",
                                  "Count":  16
                              },
                              {
                                  "Name":  "moco, training_failed",
                                  "Count":  2
                              },
                              {
                                  "Name":  "moco, invalid_action",
                                  "Count":  1
                              },
                              {
                                  "Name":  "monadic_reward, source_invalid",
                                  "Count":  8
                              },
                              {
                                  "Name":  "monadic_reward, invalid_action",
                                  "Count":  1
                              },
                              {
                                  "Name":  "rd_adaptive_halting, RUNTIME_ERROR",
                                  "Count":  5
                              },
                              {
                                  "Name":  "rd_adaptive_halting, underfit",
                                  "Count":  1
                              },
                              {
                                  "Name":  "regex_state_machine, underfit",
                                  "Count":  3
                              },
                              {
                                  "Name":  "regex_state_machine, invalid_action",
                                  "Count":  1
                              },
                              {
                                  "Name":  "sheaf_invariant_gluing, underfit",
                                  "Count":  9
                              },
                              {
                                  "Name":  "sheaf_physical_constraints, underfit",
                                  "Count":  9
                              },
                              {
                                  "Name":  "sheaf_schema_sync, underfit",
                                  "Count":  1
                              },
                              {
                                  "Name":  "sql_fixed_point, underfit",
                                  "Count":  1
                              },
                              {
                                  "Name":  "ssm_parallel_scan, underfit",
                                  "Count":  4
                              },
                              {
                                  "Name":  "tensor_functor, underfit",
                                  "Count":  3
                              },
                              {
                                  "Name":  "transformer_ssm_lift, source_invalid",
                                  "Count":  1
                              },
                              {
                                  "Name":  "ts_one_step, runtime_error",
                                  "Count":  1
                              },
                              {
                                  "Name":  "ts_one_step, underfit",
                                  "Count":  3
                              },
                              {
                                  "Name":  "ts_trajectory, underfit",
                                  "Count":  3
                              },
                              {
                                  "Name":  "ts_trajectory, runtime_error",
                                  "Count":  1
                              }
                          ],
    "guarantee_outcome_cross_tab":  [
                                        {
                                            "Name":  "compile_only, scored, PASS",
                                            "Count":  136
                                        },
                                        {
                                            "Name":  "compile_only, scored, FAIL",
                                            "Count":  80
                                        },
                                        {
                                            "Name":  "behavioral_reference, scored, PASS",
                                            "Count":  141
                                        },
                                        {
                                            "Name":  "compile_only, infrastructure_unscored, ",
                                            "Count":  11
                                        },
                                        {
                                            "Name":  "behavioral_reference, scored, FAIL",
                                            "Count":  48
                                        }
                                    ],
    "environment_guarantee_cross_tab":  [
                                            {
                                                "Name":  "architecture_naturality, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "batchnorm_ema, compile_only",
                                                "Count":  15
                                            },
                                            {
                                                "Name":  "categorical_lenses, behavioral_reference",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "ci_dependency_graph, behavioral_reference",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "compositional_optimizer, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "css_state_machine, behavioral_reference",
                                                "Count":  18
                                            },
                                            {
                                                "Name":  "epistemic_announcements, compile_only",
                                                "Count":  6
                                            },
                                            {
                                                "Name":  "epistemic_fragmented_observation, compile_only",
                                                "Count":  4
                                            },
                                            {
                                                "Name":  "epistemic_games, behavioral_reference",
                                                "Count":  23
                                            },
                                            {
                                                "Name":  "epistemic_nested_knowledge, compile_only",
                                                "Count":  6
                                            },
                                            {
                                                "Name":  "epistemic_silence, compile_only",
                                                "Count":  6
                                            },
                                            {
                                                "Name":  "epistemic_type_games, compile_only",
                                                "Count":  4
                                            },
                                            {
                                                "Name":  "equivariant_diagram, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "functorial_augmentation, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "glyph, behavioral_reference",
                                                "Count":  24
                                            },
                                            {
                                                "Name":  "gnn_message_passing, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "moco, behavioral_reference",
                                                "Count":  55
                                            },
                                            {
                                                "Name":  "monadic_reward, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "neuro_symbolic_parser, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "rd_adaptive_halting, compile_only",
                                                "Count":  15
                                            },
                                            {
                                                "Name":  "rd_gradient_credit, compile_only",
                                                "Count":  15
                                            },
                                            {
                                                "Name":  "rd_state_carry, behavioral_reference",
                                                "Count":  15
                                            },
                                            {
                                                "Name":  "regex_state_machine, behavioral_reference",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "semiring_unification, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "sheaf_invariant_gluing, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "sheaf_physical_constraints, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "sheaf_schema_sync, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "spreadsheet_dataflow, behavioral_reference",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "sql_fixed_point, behavioral_reference",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "ssm_parallel_scan, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "stochastic_monad, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "template_interpreter, behavioral_reference",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "tensor_functor, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "tokenizer_adjunction, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "transformer_ssm_lift, compile_only",
                                                "Count":  9
                                            },
                                            {
                                                "Name":  "ts_one_step, compile_only",
                                                "Count":  4
                                            },
                                            {
                                                "Name":  "ts_parse_only, compile_only",
                                                "Count":  4
                                            },
                                            {
                                                "Name":  "ts_trajectory, compile_only",
                                                "Count":  4
                                            }
                                        ],
    "scored_fail_unscored_disposition":  [
                                             {
                                                 "case_id":  "batchnorm_ema__optimizer_hint=medium_red_herring=medium_visible_tests=medium_data_complexity=medium_symptom_mask=medium__seed-0",
                                                 "environment":  "batchnorm_ema",
                                                 "failure_mode_raw":  "invalid_action"
                                             },
                                             {
                                                 "case_id":  "glyph__architecture=hard_optimizer=hard_red_herring=hard_visible_tests=hard_data_clue=hard_symptom_mask=hard__seed-0",
                                                 "environment":  "glyph",
                                                 "failure_mode_raw":  "invalid_action"
                                             },
                                             {
                                                 "case_id":  "moco__naming=hard_distractors=easy_queue_math=hard_temperature=easy_visible_tests=hard_symptom_mask=easy__reward_proxy__seed-0",
                                                 "environment":  "moco",
                                                 "failure_mode_raw":  "training_failed"
                                             },
                                             {
                                                 "case_id":  "moco__naming=medium_distractors=hard_queue_math=medium_temperature=hard_visible_tests=medium_symptom_mask=hard__seed-0",
                                                 "environment":  "moco",
                                                 "failure_mode_raw":  "training_failed"
                                             },
                                             {
                                                 "case_id":  "moco__naming=medium_distractors=medium_queue_math=hard_temperature=hard_visible_tests=easy_symptom_mask=easy__visible_proxy__seed-0",
                                                 "environment":  "moco",
                                                 "failure_mode_raw":  "invalid_action"
                                             },
                                             {
                                                 "case_id":  "monadic_reward__naming=medium_symptom_mask=hard__seed-0",
                                                 "environment":  "monadic_reward",
                                                 "failure_mode_raw":  "invalid_action"
                                             },
                                             {
                                                 "case_id":  "regex_state_machine__surface_deceptiveness=hard_hidden_depth=medium__seed-0",
                                                 "environment":  "regex_state_machine",
                                                 "failure_mode_raw":  "invalid_action"
                                             },
                                             {
                                                 "case_id":  "ts_one_step__witness_status=broken_representation=flat__seed-0",
                                                 "environment":  "ts_one_step",
                                                 "failure_mode_raw":  "runtime_error"
                                             },
                                             {
                                                 "case_id":  "ts_trajectory__witness_status=valid_representation=flat__seed-0",
                                                 "environment":  "ts_trajectory",
                                                 "failure_mode_raw":  "runtime_error"
                                             }
                                         ],
    "rejected_failures":  [
                              {
                                  "case_id":  "batchnorm_ema__optimizer_hint=medium_red_herring=easy_visible_tests=medium_data_complexity=easy_symptom_mask=easy__seed-0",
                                  "environment":  "batchnorm_ema",
                                  "failure_mode_raw":  "training_failed"
                              },
                              {
                                  "case_id":  "monadic_reward__naming=easy_symptom_mask=easy__seed-0",
                                  "environment":  "monadic_reward",
                                  "failure_mode_raw":  "source_invalid"
                              },
                              {
                                  "case_id":  "monadic_reward__naming=easy_symptom_mask=hard__seed-0",
                                  "environment":  "monadic_reward",
                                  "failure_mode_raw":  "source_invalid"
                              },
                              {
                                  "case_id":  "monadic_reward__naming=easy_symptom_mask=medium__seed-0",
                                  "environment":  "monadic_reward",
                                  "failure_mode_raw":  "source_invalid"
                              },
                              {
                                  "case_id":  "monadic_reward__naming=hard_symptom_mask=easy__seed-0",
                                  "environment":  "monadic_reward",
                                  "failure_mode_raw":  "source_invalid"
                              },
                              {
                                  "case_id":  "monadic_reward__naming=hard_symptom_mask=hard__seed-0",
                                  "environment":  "monadic_reward",
                                  "failure_mode_raw":  "source_invalid"
                              },
                              {
                                  "case_id":  "monadic_reward__naming=hard_symptom_mask=medium__seed-0",
                                  "environment":  "monadic_reward",
                                  "failure_mode_raw":  "source_invalid"
                              },
                              {
                                  "case_id":  "monadic_reward__naming=medium_symptom_mask=easy__seed-0",
                                  "environment":  "monadic_reward",
                                  "failure_mode_raw":  "source_invalid"
                              },
                              {
                                  "case_id":  "monadic_reward__naming=medium_symptom_mask=medium__seed-0",
                                  "environment":  "monadic_reward",
                                  "failure_mode_raw":  "source_invalid"
                              },
                              {
                                  "case_id":  "transformer_ssm_lift__naming=hard_symptom_mask=medium__seed-0",
                                  "environment":  "transformer_ssm_lift",
                                  "failure_mode_raw":  "source_invalid"
                              }
                          ],
    "omission_count":  80,
    "distinct_omitted_case_ids":  80,
    "omission_cross_tab":  [
                               {
                                   "Name":  "rope, unsupported_provider_input_modality",
                                   "Count":  10
                               },
                               {
                                   "Name":  "glyph, known_gate_calibration_failure",
                                   "Count":  9
                               },
                               {
                                   "Name":  "rope, known_gate_calibration_failure",
                                   "Count":  5
                               },
                               {
                                   "Name":  "epistemic_games, intervention_twin_omission",
                                   "Count":  9
                               },
                               {
                                   "Name":  "glyph, intervention_twin_omission",
                                   "Count":  12
                               },
                               {
                                   "Name":  "moco, intervention_twin_omission",
                                   "Count":  35
                               }
                           ],
    "scored_pass_fraction":  0.68395061728395057,
    "selected_observed_pass_share":  0.66586538461538458,
    "environment_unweighted_mean":  0.69207952541285889,
    "environment_rows_derived_from_matrix":  [
                                                 {
                                                     "Name":  "architecture_naturality",
                                                     "n_scored":  9,
                                                     "n_pass":  9
                                                 },
                                                 {
                                                     "Name":  "batchnorm_ema",
                                                     "n_scored":  15,
                                                     "n_pass":  2
                                                 },
                                                 {
                                                     "Name":  "categorical_lenses",
                                                     "n_scored":  9,
                                                     "n_pass":  9
                                                 },
                                                 {
                                                     "Name":  "ci_dependency_graph",
                                                     "n_scored":  9,
                                                     "n_pass":  9
                                                 },
                                                 {
                                                     "Name":  "compositional_optimizer",
                                                     "n_scored":  9,
                                                     "n_pass":  7
                                                 },
                                                 {
                                                     "Name":  "css_state_machine",
                                                     "n_scored":  18,
                                                     "n_pass":  18
                                                 },
                                                 {
                                                     "Name":  "epistemic_announcements",
                                                     "n_scored":  6,
                                                     "n_pass":  6
                                                 },
                                                 {
                                                     "Name":  "epistemic_fragmented_observation",
                                                     "n_scored":  4,
                                                     "n_pass":  4
                                                 },
                                                 {
                                                     "Name":  "epistemic_games",
                                                     "n_scored":  23,
                                                     "n_pass":  23
                                                 },
                                                 {
                                                     "Name":  "epistemic_nested_knowledge",
                                                     "n_scored":  6,
                                                     "n_pass":  6
                                                 },
                                                 {
                                                     "Name":  "epistemic_silence",
                                                     "n_scored":  0,
                                                     "n_pass":  0
                                                 },
                                                 {
                                                     "Name":  "epistemic_type_games",
                                                     "n_scored":  0,
                                                     "n_pass":  0
                                                 },
                                                 {
                                                     "Name":  "equivariant_diagram",
                                                     "n_scored":  9,
                                                     "n_pass":  7
                                                 },
                                                 {
                                                     "Name":  "functorial_augmentation",
                                                     "n_scored":  9,
                                                     "n_pass":  0
                                                 },
                                                 {
                                                     "Name":  "glyph",
                                                     "n_scored":  24,
                                                     "n_pass":  0
                                                 },
                                                 {
                                                     "Name":  "gnn_message_passing",
                                                     "n_scored":  9,
                                                     "n_pass":  5
                                                 },
                                                 {
                                                     "Name":  "moco",
                                                     "n_scored":  55,
                                                     "n_pass":  36
                                                 },
                                                 {
                                                     "Name":  "monadic_reward",
                                                     "n_scored":  9,
                                                     "n_pass":  0
                                                 },
                                                 {
                                                     "Name":  "neuro_symbolic_parser",
                                                     "n_scored":  9,
                                                     "n_pass":  9
                                                 },
                                                 {
                                                     "Name":  "rd_adaptive_halting",
                                                     "n_scored":  14,
                                                     "n_pass":  8
                                                 },
                                                 {
                                                     "Name":  "rd_gradient_credit",
                                                     "n_scored":  15,
                                                     "n_pass":  15
                                                 },
                                                 {
                                                     "Name":  "rd_state_carry",
                                                     "n_scored":  15,
                                                     "n_pass":  15
                                                 },
                                                 {
                                                     "Name":  "regex_state_machine",
                                                     "n_scored":  9,
                                                     "n_pass":  5
                                                 },
                                                 {
                                                     "Name":  "semiring_unification",
                                                     "n_scored":  9,
                                                     "n_pass":  9
                                                 },
                                                 {
                                                     "Name":  "sheaf_invariant_gluing",
                                                     "n_scored":  9,
                                                     "n_pass":  0
                                                 },
                                                 {
                                                     "Name":  "sheaf_physical_constraints",
                                                     "n_scored":  9,
                                                     "n_pass":  0
                                                 },
                                                 {
                                                     "Name":  "sheaf_schema_sync",
                                                     "n_scored":  9,
                                                     "n_pass":  8
                                                 },
                                                 {
                                                     "Name":  "spreadsheet_dataflow",
                                                     "n_scored":  9,
                                                     "n_pass":  9
                                                 },
                                                 {
                                                     "Name":  "sql_fixed_point",
                                                     "n_scored":  9,
                                                     "n_pass":  8
                                                 },
                                                 {
                                                     "Name":  "ssm_parallel_scan",
                                                     "n_scored":  9,
                                                     "n_pass":  5
                                                 },
                                                 {
                                                     "Name":  "stochastic_monad",
                                                     "n_scored":  9,
                                                     "n_pass":  9
                                                 },
                                                 {
                                                     "Name":  "template_interpreter",
                                                     "n_scored":  9,
                                                     "n_pass":  9
                                                 },
                                                 {
                                                     "Name":  "tensor_functor",
                                                     "n_scored":  9,
                                                     "n_pass":  6
                                                 },
                                                 {
                                                     "Name":  "tokenizer_adjunction",
                                                     "n_scored":  9,
                                                     "n_pass":  9
                                                 },
                                                 {
                                                     "Name":  "transformer_ssm_lift",
                                                     "n_scored":  9,
                                                     "n_pass":  8
                                                 },
                                                 {
                                                     "Name":  "ts_one_step",
                                                     "n_scored":  4,
                                                     "n_pass":  0
                                                 },
                                                 {
                                                     "Name":  "ts_parse_only",
                                                     "n_scored":  4,
                                                     "n_pass":  4
                                                 },
                                                 {
                                                     "Name":  "ts_trajectory",
                                                     "n_scored":  4,
                                                     "n_pass":  0
                                                 }
                                             ],
    "uniform_scored_environment_rows":  204,
    "uniform_rows_caveat":  "214 includes ten blank pass-rate rows in epistemic_silence and epistemic_type_games. Only 204 rows lie in environments with a uniform recorded scored outcome. A shared absence of scored outcomes must not be described as an observed success/failure outcome.",
    "input_hashes":  [
                         {
                             "Path":  "C:\\Users\\hatgu\\epistemic-compiler\\arena-handoffs\\Mercury-POST-02-redo-writer-revision-v2.sources\\campaign-02-analysis\\evidence\\generated\\case_results.csv",
                             "Hash":  "88BC8FAB7F16D494032A81B01FE8AD6D56E71BBF72A17658B2E7CABA45BBD567"
                         },
                         {
                             "Path":  "C:\\Users\\hatgu\\epistemic-compiler\\arena-handoffs\\Mercury-POST-02-redo-writer-revision-v2.sources\\campaign-02-analysis\\evidence\\generated\\campaign_exclusions.csv",
                             "Hash":  "23629F5B7133631EAECCF654134CDAEA6A2E71451F7FB8C19F90A706D828EFAA"
                         },
                         {
                             "Path":  "C:\\Users\\hatgu\\epistemic-compiler\\arena-handoffs\\Mercury-POST-02-redo-writer-revision-v2.sources\\campaign-02-analysis\\evidence\\generated2\\environment_difficulty_matrix.csv",
                             "Hash":  "A028535FB58DD40D240BD376FD4DE3322C08CFA546B03DF6C7C16C238827569E"
                         }
                     ],
    "failure_labels_case_sensitive":  [
                                          {
                                              "Name":  "overfit_visible_tests",
                                              "Count":  49
                                          },
                                          {
                                              "Name":  "training_failed",
                                              "Count":  3
                                          },
                                          {
                                              "Name":  "invalid_action",
                                              "Count":  5
                                          },
                                          {
                                              "Name":  "underfit",
                                              "Count":  51
                                          },
                                          {
                                              "Name":  "RUNTIME_ERROR",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "source_invalid",
                                              "Count":  9
                                          },
                                          {
                                              "Name":  "runtime_error",
                                              "Count":  2
                                          }
                                      ],
    "all_pass_environments":  17,
    "mixed_environments":  12,
    "unscored_only_environments":  2
}
<END SOURCE SUPPORTING_LOCAL_SOURCE_CHECK_JSON>

<BEGIN SOURCE CURRENT_V3_EVIDENCE_REVIEW_PAIR>
grok 4.5:
I will now assemble the full evidence review from all four parts, beginning with required Web Search checks on provenance and any external claims.State. Pinned commit 6ed48cb1c4447d4f902d1fbc8a908a56185e34ed (StrangeTcy/epistemic-compiler). Read in full: WRITER_PAIR (both drafts verbatim), COMPLETE_EVIDENCE_PACKET (Table A 38 env rows, Table B 416 case rows, Table C 80 omission rows, Table D 340 matrix rows, Section E chart descriptions), COMPLETE_DIFFICULTY_MATRIX_CSV (340 rows with full difficulty_tuple keys), CAMPAIGN_PROVENANCE, EARLIER_ANALYSIS_OVERVIEW, INELIGIBLE_PASS_CSV_EXCERPT, and the 2026-10-29 supporting local check. Web Search accessed Inception Labs/OpenRouter/etc. pages confirming Mercury-2.5 existence and specs (no campaign data or public StrangeTcy/epistemic-compiler repo/commit retrieved; limitation noted, embedded sources used exclusively). Calculations performed: row sums (277 PASS/128 FAIL/405 scored/11 unscored; 17/7/12/2 env split; 172/68/165; omission 56+14+10; failure-label totals; 296/44/329/320/9/98 matrix; unweighted mean ≈69.2%; 214 vs 204+10 uniform; moco fractions and keys; guarantee 189/227; rejected/unscored disposition counts). Unverifiable/unread: actual SVG binary renders (descriptions only), exact dirty working-tree state, clean-source comparison, public origin of overview’s “10”, any external campaign data.

1. Draft gpt 6 luna max
Verdict: accept with corrections

Confirmed-arithmetic table (matches Tables A/B/C/D + local check):

Quantity	Value
Selected / scored / unscored	416 / 405 / 11
PASS / FAIL	277 / 128
277/405	68.4%
277/416	66.6%
Env split (all-pass / zero-pass scored / mixed / unscored-only)	17 (172) / 7 (68) / 12 (105/165 +1) / 2 (10)
Matrix rows / singleton / multi	340 / 296 / 44
Rows with rate / endpoint / fractional	329 / 320 / 9 (all moco)
Zero-pass tuples	98 (19 env)
Unweighted mean / median (36 scored env)	~69.2% / 8/9 = 88.9%
Failures (underfit / overfit_visible_tests / runtime consolidated / source_invalid / invalid_action / training_failed)	51 / 49 / 11 / 9 / 5 / 3
Guarantees	189 behavioral_reference / 227 compile_only
Omissions	80 (56 twin / 14 known-gate / 10 modality all rope)
Rejected FAILs	10 (8 monadic_reward +1 batchnorm_ema +1 transformer_ssm_lift)

Numbered findings:

Location: moco subsection / “Claims withdrawn…”. Claim: “The available record does not link each fractional value to its tuple key, so I cannot draw the outcome shape across moco’s dimensions.” Evidence: COMPLETE_DIFFICULTY_MATRIX_CSV supplies full difficulty_tuple JSON keys for all 15 moco rows (e.g. distractors/naming/queue_math/… mapped to 1/6, 1/3, 2/5, 2/3, 3/4, 5/6 etc.). Compact Table D omits the strings; complete matrix does not. Verdict: incorrect (keys exist). Severity: correction. Action: Replace with statement that keys are present in the complete matrix and optionally list the nine fractional mappings; do not claim unavailability.

Location: “The environment-by-tuple matrix” (214 rows). Claim: “A total of 214 rows—63% of the matrix—sit in environments where every row has the same outcome.” Evidence: Local check + matrix: 214 only when blanks (unscored) are treated as uniform; supported split is 204 rows in environments with uniform scored outcomes + 10 rows in the two fully unscored environments (epistemic_silence 6 + epistemic_type_games 4). Verdict: imprecise. Severity: correction. Action: Narrow to “204 rows in uniform-scored-outcome environments + 10 in fully unscored environments (or 214 if shared absence of scored outcomes is grouped)”.

Location: “Ten zero-pass environments or seven?” + overview cross-ref. Claim: Correctly uses 7 scored zero-pass and leaves “10” unresolved. Evidence: Table A shows exactly 7 (functorial_augmentation, monadic_reward, sheaf_invariant_gluing, sheaf_physical_constraints, ts_one_step, ts_trajectory, glyph); overview states 10; tuple view yields 19. Unscored-only envs are not zero-pass. Verdict: correct handling. Severity: note. Action: Retain; do not reconcile.

Location: Omission / provenance. Claim: Reports both 14 (exclusion record) and 24 (provenance) known-gate; leaves open; does not present 14+10=24 as verified. Evidence: Table C = 14 known-gate (9 glyph +5 rope) +10 modality +56 twin; provenance prose “24 known gate-blocked”. Verdict: correct. Severity: note. Action: Keep both figures and open status.

Location: Failure labels / dispositions. Claim: Global tallies only; runtime consolidated 9+2; 10 rejected kept in FAIL; archive undefined. Also notes unscored dispositions implicitly via counts. Evidence: Table B + local check: labels sum 128; exactly 10 rejected; 9 scored-FAIL with disposition unscored. Verdict: correct on globals and rejected; slightly incomplete on the 9. Severity: note. Action: Optionally flag the 9 scored/FAIL/unscored disposition cases explicitly as recorded but undefined operationally.

Location: ts_parse_only / ineligible. Claim: Keeps the PASS in 277; flags performance-ineligible and provider-attributed terminal failure vs PASS verdict. Evidence: INELIGIBLE_PASS_CSV_EXCERPT + Table B row 409: verdict PASS, performance_eligible=False, exclusion_reason provider-outage/transient. Verdict: correct; attribution is the recorded field, not independent causation. Severity: note. Action: Retain flag; do not elevate exclusion_reason to proven cause.

Location: Figure 2 caption. Claim: Lollipop of observed pass rates across 36 scored envs; read fraction with case count; not stability. Evidence: Section E describes related interval/lollipop-style env plot (Fig 9) with Wilson intervals and same 36; drafts’ Fig 2 path/units match data but numbering/caption differ from packet’s 8–11. No SVG rendered here. Verdict: substantively aligned, numbering mismatch. Severity: note. Action: Align caption/number to packet or note descriptive match only; do not claim rendered SVG content beyond description.

Location: Seed / dirty / selection / guarantees. Claims: All seed 0, no second seed, dirty source [m-word], 80 omitted, guarantees not interchangeable, no env-by-guarantee cross-tab. Evidence: Table B all seed=0; provenance dirty=true, no clean snapshot; Table C 80; guarantees 189/227 total only. Verdict: correct limits. Severity: note. Action: None beyond retaining.

Location: Public prose / brackets. Claim: Uses [m-word]; no accidental paths, broken MD, or ungrounded authorship. Evidence: Intentional per rules; required fig URLs absent or clean. Verdict: clean. Severity: note.

Blocking-finding count: 0
Correction count: 2 (moco keys; 214 wording)
Note count: 7

2. Draft opus 5
Verdict: accept with corrections

Confirmed-arithmetic table: Identical to the table above (all core denominators, splits, matrix stats, labels, guarantees, omissions, rejected match Tables A–D + local check). Additional verified sensitivities (ex-moco 241/350≈68.86%, ex-glyph 277/381≈72.70%, etc.) are pure arithmetic on existing rows, not new analysis.

Numbered findings:

Location: moco subsection. Claim: “the fractional values are recorded, but no row-by-row key links each value back to its tuple. So I can say that moco is the only environment where outcomes vary within tuples, and I cannot say which tuples those are…” Evidence: COMPLETE_DIFFICULTY_MATRIX_CSV provides the exact keys for every moco row (including the nine fractionals). Verdict: incorrect (keys exist). Severity: correction. Action: Same as gpt #1 — acknowledge complete-matrix keys and map if desired; drop “cannot”.

Location: Matrix section (214 / 63%). Claim: “214 of 340 rows (63%) sit in environments where every row has the same outcome.” Evidence: Same local-check distinction (204 uniform-scored + 10 fully unscored). Verdict: imprecise. Severity: correction. Action: Identical narrowing as gpt #2.

Location: “Ten zero-pass…”. Claim: Uses 7; leaves 10 open; tuple view 19. Evidence: Table A =7; overview =10. Verdict: correct. Severity: note. Action: Retain.

Location: Selection frame / provenance. Claim: 14 vs 24 known-gate both reported, unresolved; 10 modality all rope; does not treat 14+10 as verified reconciliation. Evidence: Table C vs provenance. Verdict: correct. Severity: note. Action: Keep.

Location: Failure labels. Claim: Globals only; “No environment-by-label breakdown is available here”; runtime casing consolidated without over-reading; 10 rejected kept. Evidence: Packet supplies globals; complete matrix has per-row failure_modes but no pre-aggregated env×label table in compact form. Local check notes 9 scored/FAIL/unscored disposition. Verdict: mostly correct (globals accurate; “no breakdown” is true for compact packet, overstated if complete matrix counts are allowed). Severity: correction (mild). Action: Soften to “no pre-built env-by-label cross-tab in the compact packet; per-row modes exist in matrix for counting if needed”; explicitly note the 9 disposition cases.

Location: ts_parse_only ineligible + guarantees. Claim: Keeps in 277, flags inconsistency; guarantees not interchangeable, no env-by-guarantee. Evidence: Excerpt + totals. Verdict: correct. Severity: note. Action: Retain.

Location: Density/sensitivity arithmetic. Claim: Excluding moco/glyph etc. shifts. Evidence: Direct from Table A (55 moco, 24 glyph). Verdict: supported verification. Severity: note. Action: Keep as arithmetic illustration only.

Location: Figure caption / embed. Claim: Markdown image to ../figures/fig2_environment_outcome_lollipop.svg + caption matching 36 scored envs, fractions + counts. Evidence: Section E Fig-style data match; path is required figure URL (not leakage); no binary render. Verdict: acceptable reference. Severity: note. Action: Confirm path resolves in final; caption OK.

Location: Seed/dirty/selection/confounds / [m-word]. Claims: Accurate limits; intentional bracket. Evidence: Matches provenance/Table B. Verdict: clean. Severity: note.

Blocking-finding count: 0
Correction count: 3 (moco keys; 214; mild env-by-label availability)
Note count: 6

3. Shared unresolved source discrepancies

Bounded by supplied records: 14 (Table C) vs 24 (provenance) known-gate omissions — both figures exist; Table C rows detail 9 glyph +5 rope; no row-level support for 24 inside the exclusion CSV. 7 scored zero-pass env (Table A) vs overview “10” — overview list enumerates only the 7; origin of 10 unreconciled here (not the 2 unscored-only, not the 19 tuple envs). 214 uniform rows — resolvable as 204+10 once blanks included (local check). moco keys — available in complete CSV, absent from compact Table D. 9 scored/FAIL/unscored disposition cases + 10 rejected — exact IDs in local JSON/Table B; definitions absent.
Cannot be reconciled here: Exact dirty working-tree state or causal effect; clean-source counterfactual; seed-variance (only seed 0); whether overview “10” derives from an earlier filter; any env×label or env×guarantee controlled comparison beyond raw counts that can be tallied from matrix; base rate of apparent non-monotonicity; independent causation behind exclusion_reason text (recorded attribution only). Arithmetic coincidences (e.g. 14+10) are not documented explanations.

4. Handoff for the editorial critic
Exact corrections to carry:

Both drafts: Insert that complete difficulty-matrix CSV supplies difficulty_tuple keys for all rows (including moco’s nine fractionals); remove or rewrite any “no key / cannot map / unavailable” claim. Optionally publish the nine mappings as descriptive.
Both: Re-word 214/63% to distinguish 204 uniform-scored-outcome rows + 10 fully-unscored-environment rows (or explicitly define inclusion of blank pass_rate).
Opus (and optionally gpt): Soften “no environment-by-label breakdown” to reflect that per-row failure_modes exist for aggregation; note the 9 scored/FAIL/disposition=unscored cases alongside the 10 rejected.
Retain: 277/405=68.4% as scored pass rate; 7 (not 10) scored zero-pass envs; dual 14/24 known-gate reporting as open; ineligible ts_parse_only PASS kept in numerator with flag; all seed-0 / dirty / selection / guarantee / single-seed limits; no causal or common-scale claims; intentional [m-word].
Newly available fields for critic: full tuple keys, per-row failure_modes/judge_guarantees, exact disposition flags (9+10), local-check uniform split, INELIGIBLE exclusion_reason text, matrix-derived env totals.
Evidence limits: No new model fits, no causal estimates, no imported campaigns, no SVG pixel claims, no fabrication of missing clean snapshot or second seeds. Overview vs Table A “10 vs 7” and provenance vs Table C “24 vs 14” stay open. Web Search found no public archive contradicting the pinned embedded records.

No prose rewrite, no winner choice, no claim that later stages are complete.

&&&&&&&&

claude fable 5.1:
Both drafts and all source blocks are now assembled; before writing the review I will verify the arithmetic against the supplied tables and run the required Web Search for provenance.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
# Mercury POST-02 — evidence review of gpt 6 luna max and opus 5

State. Pinned commit 6ed48cb1c4447d4f902d1fbc8a908a56185e34ed in StrangeTcy/epistemic-compiler. Read in full: WRITER_PAIR (both drafts, verbatim order); COMPLETE_EVIDENCE_PACKET — Table A (38 rows), Table B (416 rows), Table C (80 rows), Table D (340 rows), Section E (Figures 8–11); COMPLETE_DIFFICULTY_MATRIX_CSV (340 rows with difficulty_tuple keys, raw failure labels, judge guarantees); CAMPAIGN_PROVENANCE; EARLIER_ANALYSIS_OVERVIEW; INELIGIBLE_PASS_CSV_EXCERPT (1 row); and the 2026-10-29 supporting local check. Calculations performed in Python from Table A and the env-level guarantee assignment in Table B/D: denominators, group totals, shares, unweighted mean/median, tuple-row sums, sensitivity scenarios, Wilson intervals, guarantee cross-tabs (all reproduced below). Web Search accessed: the repository landing page https://github.com/StrangeTcy/epistemic-compiler exists and is public; search results could not retrieve the pinned commit, the four CSVs, or their hashes, so file-level provenance remains verified only against the embedded sources. External context: Mercury 2.5 is a publicly announced Inception model (https://www.baseten.co/library/mercury-25/, https://www.businesswire.com/news/home/20260908593295/en/Inception-Launches-Mercury-2.5-the-Next-Tier-of-Intelligence-for-Diffusion-LLMs); none of the campaign's numbers are checked against those pages. Unverifiable: no SVG was rendered; Section E describes Figures 8–11 only, and neither draft's "Figure 2" lollipop chart is described there. No evidence/generated/environment_summary.csv or the supporting check's JSON was supplied.

Confirmed arithmetic (both drafts, identical numbers)
Claim	Derivation / source	Status
416 selected / 405 scored / 11 unscored; 277 PASS / 128 FAIL	Table A sums; Table B statuses	✓
277/405 = 68.4%; 277/416 = 66.6%	68.395%, 66.587%	✓
17 all-pass (172/172, 42.5%); 7 zero-pass (0/68, 16.8%); 12 mixed (105/165, 40.7%, +1 unscored); 2 no-scored (10 unscored)	Table A grouping; 42.47/16.79/40.74	✓
24 of 36 scored environments at an endpoint; endpoints rest on 4 to 23/24 cases	17+7; ts_* n=4, epistemic_games 23, glyph 24	✓
Unweighted mean ≈ 69.2%; median 8/9 = 88.9%	69.208%; sorted positions 18–19 both 0.889	✓
All environment fractions listed in both drafts (incl. 9 envs at 9/9; mixed table)	Table A	✓
glyph+moco+batchnorm_ema = 94/405 cases, 56/128 FAILs	24+55+15; 24+19+13	✓
340 tuple rows; 4–15 per env; six envs >10; 296 singleton / 44 multi-case in moco 15/55, glyph 12/24, css 9/18, epistemic_games 8/23	Table A n_tuples sum = 340; Table D	✓
329 rows with pass rate; 320 (97.3%) at 0/1; 9 fractional, all moco; moco 6 endpoint rows; distinct values 1/6, 1/3, 2/5, 2/3, 3/4, 5/6	Table D moco#1–15	✓
34 difficulty dimension names	counted in full matrix	✓
98 zero-pass tuples in 19 environments; all 12 mixed envs have ≥1	Table D (13+2+2+9+12+4+1+9+6+4+9+9+1+1+4+3+1+4+4)	✓
css_state_machine 9 rows all 2/2	Table D	✓
Unscored: 6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting; latter at all-easy tuple	Table B 109–118, 243; full matrix rd_adaptive_halting row 1	✓
Failure labels 51/49/11/9/5/3 = 128; runtime = 9 RUNTIME_ERROR + 2 runtime_error	Table B/D raw labels	✓
189 behavioral_reference / 227 compile_only across 416	Table B; provenance §3	✓
10 rejected FAILs: 8 monadic_reward (225–231, 233), batchnorm_ema 20, transformer_ssm_lift 401	Table B	✓
Omissions 56/14/10 = 80; all 10 modality omissions in rope; provenance says 24 known-gate	Table C; provenance §3	✓ (discrepancy correctly reported)
All 416 cases seed 0; source dirty; no clean snapshot	Table B; provenance §1, §4	✓
ts_parse_only row 409 PASS, performance_eligible False, exclusion note attributes terminal failure to provider	Table B; INELIGIBLE_PASS_CSV_EXCERPT	✓
opus only: 241/350 = 68.86% (+0.46), 277/381 = 72.70% (+4.31), 241/326 = 73.93%, moco→9 cases ≈ 68.8%	recomputed	✓
1. Draft gpt 6 luna max — verdict: accept with corrections

Section "moco: the only fractional rows". Claim: "The available record does not link each fractional value to its tuple key, so I cannot draw the outcome shape across moco's dimensions." Also "Claims withdrawn": "the missing row-by-row tuple key also prevents reconstructing the pattern." Evidence: COMPLETE_DIFFICULTY_MATRIX_CSV, all 15 moco rows carry a full difficulty_tuple (e.g. the 1/6 row is distractors=hard, naming=easy, queue_math=easy, symptom_mask=hard, temperature=hard, visible_tests=easy). Verdict: false as a statement about the record. Severity: blocking. Action: replace with "the compact packet omits the keys; the complete matrix records them." The keys' existence does not license a difficulty-effect reading — keep the moco pattern "open".

Section "Failure labels and judge guarantees". Claim: "The counts are global only; they do not show which environments produced which labels." Evidence: Table D failure_modes and Table B give per-environment labels (e.g. all 9 source_invalid are monadic_reward ×8 + transformer_ssm_lift ×1; all 5 RUNTIME_ERROR in rd_adaptive_halting). Verdict: unsupported "cannot". Severity: correction. Action: state the breakdown is recorded; keep the separate, valid point that labels are classifications, not mechanisms.

Same section. Claim: "The totals alone do not show how outcomes are distributed by environment and guarantee, so I cannot compare environment results under one common judging standard." Evidence: Table D judge_guarantees — every environment has a single guarantee; BR 141/189 scored, CO 136/216 scored. Verdict: first half unsupported (the cross-tab exists); second half supportable only because guarantee is confounded with environment (no within-environment variation), not because the data are missing. Severity: correction. Action: reword to the confound.

Section "The environment-by-tuple matrix" (and conclusion). Claim: "A total of 214 rows—63% of the matrix—sit in environments where every row has the same outcome." Evidence: uniform-scored environments hold 148 (all-pass) + 56 (zero-pass) = 204 rows; the 214 includes the 10 rows of epistemic_silence/epistemic_type_games, which have no outcome (supporting check, uniform_scored_environment_rows). Verdict: arithmetic reproducible only by counting blank pass rates as an "outcome". Severity: correction. Action: "204 of 340 (60%) in environments with a uniform scored outcome, plus 10 in entirely unscored environments."

Final figure block. Text: a bare "!" line followed by "Figure 2: Lollipop chart of observed pass rates across the 36 environments…". Evidence: Section E describes Figures 8, 9, 10, 11 only; the nearest match is Figure 9 (dots + 95% Wilson bars + pooled line, 36 environments). Verdict: broken image embed (malformed Markdown) and unverifiable chart number/type; caption omits the interval bars and reference line if Figure 9 is the intended asset. Severity: correction. Action: repair the embed; either reference a Section-E-described figure with a caption matching its contents (fractions, Wilson 95% intervals and their binomial-independence assumption, pooled 68.4% line, no unscored environments drawn) or supply a verifiable description for "Figure 2."

Section "What a 'cell' means". Claim: 'The phrase "one seed per cell" is ambiguous here'. Evidence: the phrase appears in no supplied source (provenance, overview, packet). Verdict: unattributed quotation. Severity: correction. Action: attribute or drop the quotation marks; the all-seed-0 fact stands on Table B alone.

Sections "First, count…" and "Unscored cases are not failures". Claim: unscored cases are "a judge-coverage gap". Evidence: recorded status is infrastructure_unscored; failure_mode_normalized is unknown. Verdict: label promoted into an explanation. Severity: correction. Action: use the recorded status label.

Section "The selection frame" (omission). The draft reports the 10 rejected FAILs but not the nine scored FAILs whose case_disposition is unscored (Table B rows 24, 145, 193, 214, 222, 232, 293, 405, 415; labels: all 5 invalid_action, 2 training_failed, both lowercase runtime_error). Table A counts them in n_scored. Severity: correction. Action: add the parallel flag; unscored as a disposition is undefined in the record and must not be equated with infrastructure_unscored status.

Section "Ten zero-pass environments or seven?" Correct as stated. Note only: the overview also says "~12 at 1.00" against Table A's 17; worth recording alongside the 10-vs-7 gap. Severity: note.

gpt 6 luna max: 1 blocking, 7 corrections, 1 note.

2. Draft opus 5 — verdict: accept with corrections

Section "What can a FAIL label explain?" and "What this supports". Claims: "No environment-by-label breakdown is available here, so I cannot say which environments produced the 51 underfit labels"; "An environment-by-guarantee and environment-by-label cross-tab would narrow some of that; nothing in the present archive supplies it." Evidence: Table D failure_modes and judge_guarantees columns, Table B per-row fields (e.g. underfit: sheaf_invariant_gluing 9, sheaf_physical_constraints 9, functorial_augmentation 6, gnn 4, ssm 4, …). Verdict: false about the record, repeated three times and carried into the conclusion. Severity: blocking. Action: delete the "not available" statements; the per-environment counts may be reported as recorded cross-tabs, with the separate caveat that they are not controlled comparisons.

Section "moco: the only fractional rows". Claim: "no row-by-row key links each value back to its tuple." Evidence: as gpt finding 1 — all 15 moco tuple keys are in the complete matrix. Severity: blocking. Action: same as gpt finding 1.

Same section as 1. Claim: "without an environment-by-guarantee breakdown I cannot test whether the environment contrasts survive a uniform standard." Evidence: breakdown exists; guarantee is constant within each environment, so the limit is confounding, not absence. Severity: correction. Action: reword to the confound.

Same section. Claim: "Describing a 9/9 environment as behaviourally settled would outrun what the judge checked." Evidence: four 9/9 environments are behavioral_reference (categorical_lenses, ci_dependency_graph, spreadsheet_dataflow, template_interpreter); six are compile_only. Verdict: over-general. Severity: correction. Action: say which guarantee each 9/9 carries, or restrict the sentence to compile-only environments.

Section "A second layer" bullet and "What this supports". Claim: "214 of 340 rows (63%) sit in environments where every row has the same outcome"; "63% of rows inside environments with a single uniform outcome." Evidence/action: as gpt finding 4 (204 + 10).

Figure after "First, count…". Embed ../figures/fig2_environment_outcome_lollipop.svg with caption "Figure 2: One dot per environment … the dots at 1.0 and 0.0 rest on anywhere from four to 24 cases." Evidence: Section E has no Figure 2; the content matches Figure 9 (36 envs, k/n dots) but the caption omits the Wilson bars, pooled line, and the interval assumptions. Verdict: unverifiable chart number/path; caption incomplete if the asset is Figure 9. Severity: correction. Action: as gpt finding 5. (A figure URL is not path leakage.)

Section "What a 'cell' means". Claim: "The campaign records one seed per cell." Evidence: not in any supplied source. Severity: correction. Action: attribute or remove; Table B's seed column already establishes all seed 0.

Sections "First, count…" / "Unscored cases are not failures". Claims: "a judge-coverage gap"; "Being unscored is a property of the judging pipeline." Evidence: status infrastructure_unscored. Severity: correction. Action: use the recorded label; do not assign the cause to the judge.

Section "The selection frame" (omission). Nine scored FAILs with disposition unscored not mentioned. As gpt finding 8. Severity: correction.

Section "Names are useful handles". Claim: "The 68.4% is sensitive to how tuples were unrolled into cases for a handful of environments." Evidence: arithmetic scenarios are correct; "unrolled" implies a design mechanism not described in any source. Severity: note. Action: phrase as sensitivity to selected case density.

opus 5: 2 blocking, 7 corrections, 1 note.

3. Shared unresolved source discrepancies
Known-gate omissions, 14 vs 24. Bounded by the record: Table C holds exactly 14 (glyph 9, rope 5); the provenance prose says 24. 14 + 10 modality = 24 is an arithmetic coincidence; neither draft asserts it as a reconciliation (correct), and this review does not either. Origin cannot be resolved here.
Zero-pass environments, 10 vs 7; all-pass "~12" vs 17. Table A gives 7 and 17; the overview's parenthetical list enumerates at most 7 names. Neither draft notes the "~12" side. Cannot be reconciled from supplied material.
Provider-outage case. Provenance: "1 retry, 60s"; CSV row: http_attempts_result 19, elapsed_seconds 46.101, provider_transport: completed_with_errors. The fields may count different things; unresolved. The exclusion_reason is the archive's own attribution, not independent causation.
Tuple-level vs case-level counts (98 zero-pass tuples in 19 envs; 7 zero-pass envs; 10 "overview" envs) count different categories and must not be merged.
Overview claims 3–5 (non-monotonic MoCo transitions, proxy-intervention rates 0.30/0.25, 23/23 belief computation) are not supported by any supplied table except the 23/23; outside this review.
4. Handoff for the editorial critic

Carry forward, with attribution to the supplied matrix and the 2026-10-29 local check (not to an Arena finding):

Newly available fields (both drafts wrongly say absent): full difficulty_tuple keys for all 340 rows including the 15 moco rows and the all-easy unscored rd_adaptive_halting tuple; per-environment failure_modes (raw spelling) and judge_guarantees. Keys enable description only — no shared scale, no difficulty effect, no ranking.
Recorded cross-tabs that may be stated as observations: guarantee is uniform within every environment; BR 141/189 scored PASS (74.6%), CO 136/216 (63.0%) — a confounded contrast, not a judged comparison. The two lowercase runtime_error cases (ts_one_step 405, ts_trajectory 415) are both disposition unscored; the nine RUNTIME_ERROR are disposition scored — recorded coincidence, no documented explanation.
Fix 214 → "204 rows in uniformly-scored environments + 10 rows in entirely unscored environments" (62.9% only if the unscored ten are counted).
Add the nine unscored-disposition FAILs beside the ten rejected; both dispositions are undefined; all 19 remain in the 128 and in Table A's n_scored.
Figures: repair gpt's broken "!" embed; for both, reconcile "Figure 2" with Section E (Figure 9 is the only matching description: 36 environments, k/n dots, 95% Wilson bars, pooled 68.4% line, unscored environments omitted). Captions must name the interval and its independence assumption, or the figure must be independently verified before publication.
Remove or attribute "one seed per cell"; replace "judge-coverage gap"/"judging pipeline" with the recorded infrastructure_unscored.
Keep unresolved: 14 vs 24; 10 vs 7 and ~12 vs 17; provider-retry field mismatch; rejected/unscored disposition meanings; ts_parse_only row 409 PASS vs provider-attributed exclusion note (recorded attribution, not established cause).
Preserve [m-word]-style replacements, the verbatim draft order, and the single-seed/dirty-source/selection limits; do not convert seed 0 into a variance estimate or 80 omissions into a sampling frame.
<END SOURCE CURRENT_V3_EVIDENCE_REVIEW_PAIR>
<BEGIN SOURCE CURRENT_EDITORIAL_BLUEPRINT_PAIR>
claude fable 5.1:
# Mercury POST-02 — editorial critic blueprint, v3 (internal review and handoff)

Status of this document: internal editorial report and claim-check handoff. It does not choose a prose winner, merge the drafts, write the article, dispatch a stage, publish anything, or assert that the claim killer, final writer, local validator, or human review has passed. Candidate labels `gpt 6 luna max` and `opus 5` are used here for attribution only and must not enter the public article.

---

## 1. State and evidence-review disposition

### 1.1 Inputs received and read (through the final END marker)

| Block | Read | Notes |
|---|---|---|
| Governing instructions (POST-02 critic blueprint v3) | Yes | Contract, boundaries, exclusions |
| `WRITER_PAIR` — `gpt 6 luna max`, `opus 5` | Yes, complete | Verbatim order preserved |
| `COMPLETE_EVIDENCE_PACKET` — Tables A (38), B (416), C (80), D (340), Section E | Yes, complete | Section E is the only figure description available |
| `COMPLETE_DIFFICULTY_MATRIX_CSV` (340 rows with `difficulty_tuple`) | Yes, complete | Supplies the tuple keys the drafts call absent |
| `CAMPAIGN_PROVENANCE` | Yes | Source of "24 known gate-blocked", dirty=true, "1 retry, 60s" |
| `EARLIER_ANALYSIS_OVERVIEW` | Yes | Source of "10 environments at 0.00" and "~12 at 1.00" |
| `INELIGIBLE_PASS_CSV_EXCERPT` (row 409) | Yes | `exclusion_reason`, `performance_eligible=False`, attempt/time fields |
| `CURRENT_INTERNAL_ARTICLE` | Yes, complete | Already carries four figures and the env-by-label/guarantee tables; introduces new boundary errors (§6) |
| `HOUSE_STYLE`, `ACTUAL_REFERENCE_POST_EXCERPTS` | Yes | Voice/structure guidance only; historical attribution/process text not imported |
| `PRIOR_WORK_REFERENCES` (Campaign 01) | Yes | Not campaign evidence; links unverified here |
| `SUPPORTING_LOCAL_SOURCE_CHECK` (.md) and companion `.json` | Yes, both supplied | Attributed as local verification, not an Arena verdict |
| `CURRENT_V3_EVIDENCE_REVIEW_PAIR` — `grok 4.5`, `claude fable 5.1` | Yes, complete | Both rated "Both are bad" by orchestration; findings rechecked row by row below |
| `ORCHESTRATION_CAPTURE_NOTE` | Yes | Clipboard Markdown not claimed; DOM archived locally |
| Supporting reconciliation note (R1–R4) | Yes | Checked against supplied rows; all four findings reproduce |

Not supplied / not readable here: the SVG files themselves (captions below are checked against Section E text only, not a rendering); the earlier claim-killer/redactor handoffs (described as obsolete; their Figure 2 and bracket-removal instructions do not apply); the standalone `environment_summary.csv` (the local check derived environment totals from the matrix; Packet Table A supplies them and agrees); the exact dirty working-tree state; any public copy of the pinned commit.

### 1.2 Mode and external access

- Arena Web Search mode: required enabled for this stage. The setting is not observable from this document; orchestration must record the observed value. An enabled mode is not evidence that any source was read.
- External sources accessed by this stage: none. Every claim below rests on the supplied blocks.
- Both reviewers assert web access (Inception/Baseten/BusinessWire pages, repository landing page). Per the capture note, those access claims are recorded as asserted, not independently established, and none of them touches campaign numbers.

### 1.3 Recorded review verdicts (as stated by the reviewers)

| Reviewer | `gpt 6 luna max` | `opus 5` |
|---|---|---|
| `grok 4.5` | accept with corrections — 0 blocking, 2 corrections, 7 notes | accept with corrections — 0 blocking, 3 corrections, 6 notes |
| `claude fable 5.1` | accept with corrections — 1 blocking, 7 corrections, 1 note | accept with corrections — 2 blocking, 7 corrections, 1 note |
| Orchestration rating | "Both are bad" (substantive review defects) | "Both are bad" |

These verdicts are not acceptance of either candidate and are not carried forward as such.

### 1.4 Reviewer disagreements and reviewer errors (rechecked against rows)

| Point | `grok 4.5` | `claude fable 5.1` | Row check | Disposition |
|---|---|---|---|---|
| `moco` tuple keys "absent" | correction | blocking | Complete matrix: all 15 `moco` rows carry full keys | Correction required in both drafts and in the current internal article; severity label is editorial — treat as must-fix |
| Env-by-label / env-by-guarantee "unavailable" | softened to "no prebuilt table" for `opus 5`; accepted for `gpt 6 luna max` | blocking (`opus 5`), correction (`gpt`) | Table B and Table D carry environment, labels, guarantees; JSON cross-tabs and reconciliation R4 reproduce | `claude fable 5.1` supported; `grok 4.5` understated (R4). Unresolved disagreement preserved, resolved by rows |
| 9/9 environments by guarantee | not addressed | "four behavioral_reference; six compile_only" | 4 BR (`categorical_lenses`, `ci_dependency_graph`, `spreadsheet_dataflow`, `template_interpreter`) + 5 CO (`architecture_naturality`, `neuro_symbolic_parser`, `semiring_unification`, `stochastic_monad`, `tokenizer_adjunction`) = 9 | `claude fable 5.1` miscounted (R1). Carry 4 + 5 |
| "one seed per cell" quotation | not flagged | correction: unattributed | Phrase appears in no supplied source; only Figure 8's bar label "design cells" exists | `claude fable 5.1` supported |
| "judge-coverage gap" | not flagged | correction | Recorded status is `infrastructure_unscored`; `failure_mode_normalized` = `unknown` | `claude fable 5.1` supported |
| Figure 2 path | "required figure URL (not leakage)" | "unverifiable chart number/path" | The four required URLs are fig8–fig11; `fig2_environment_outcome_lollipop.svg` is not among them and Section E does not describe it | `grok 4.5` wrong; replace Figure 2 in both drafts |
| 214 uniform rows | correction (204 + 10) | correction (204 + 10) | 148 all-pass rows + 56 zero-pass rows = 204; +10 unscored-environment rows = 214 | Agreed; current internal article already correct |
| Overview "~12 at 1.00" vs 17 | not noted | noted | Table A: 17 all-pass environments, 172/172 | Add to open-claims list (R2) |
| Provider "1 retry, 60s" vs row 409 fields | not noted | noted | `http_attempts_result` 19, `elapsed_seconds` 46.101, `provider_transport` `completed_with_errors` | Preserve as field contrast, no unit conversion (R3) |

### 1.5 Missing or unverifiable material (explicit gaps)

- No rendering of any SVG was inspected; caption checks are against Section E prose.
- No second seed, clean source snapshot, config-hash comparison, or base rate for apparent non-monotonic patterns exists in the record; none may be invented.
- The origin of the overview's "10" and "~12", and of the provenance's "24", cannot be determined from supplied material.
- The operational meaning of dispositions `rejected` and `unscored` is undefined in the record.
- Links in `PRIOR_WORK_REFERENCES` are not verified usable from this stage.

### 1.6 Arithmetic rechecked here (from Tables A–D and the complete matrix)

416 / 405 / 11; 277 / 128; 277/405 = 68.395%; 277/416 = 66.587%. Environments 17 (172/172) / 7 (0/68) / 12 (105/165, +1 unscored) / 2 (10 unscored). Unweighted mean of 36 scored-environment fractions 69.21%; median 8/9. Matrix 340 rows; 296 single-case, 44 multi-case (`moco` 15/55, `glyph` 12/24, `css_state_machine` 9/18, `epistemic_games` 8/23); 329 rated, 320 at 0 or 1, 9 fractional (`moco` rows #1, 2, 4, 5, 6, 7, 8, 9, 14; values 2/3 ×4, 5/6, 1/6, 3/4, 2/5, 1/3); 6 `moco` endpoint rows (#3, 10, 11, 12, 13, 15). 98 zero-pass tuples in 19 environments; all 12 mixed environments contain at least one. 34 distinct difficulty-key names. Labels 51/49/11 (9 `RUNTIME_ERROR` + 2 `runtime_error`)/9/5/3 = 128. Guarantees: 11 BR environments, 189 cases, 141/189 scored PASS, 48 FAIL; 27 CO environments, 227 cases, 136/216 scored PASS, 80 FAIL, 11 `infrastructure_unscored` all CO. Dispositions: 10 `rejected` FAILs (rows 20, 225–231, 233, 401; 9 `source_invalid` + 1 `training_failed`); 9 `unscored`-disposition FAILs with status `scored` (rows 24, 145, 193, 214, 222, 232, 293, 405, 415; 5 `invalid_action`, 2 `training_failed`, 2 lowercase `runtime_error`). Omissions: `moco` 35 twin; `glyph` 9 gate + 12 twin = 21; `rope` 10 modality + 5 gate = 15; `epistemic_games` 9 twin; totals 56/14/10 = 80; 416 + 80 = 496. Sensitivities: 241/350 = 68.86%; 277/381 = 72.70%; 241/326 = 73.93%. The single `sql_fixed_point` FAIL: `hidden_depth=hard`, `surface_deceptiveness=easy`. The unscored `rd_adaptive_halting` row: all five keys `easy`. Environments within five points of 68.4%: only `moco` (65.5%) and `tensor_functor` (66.7%).

---

## 2. Seven-dimension comparison

### 2.1 Argument and structure

Concrete question the article answers: what does the scored pass rate 277/405 = 68.4% summarize, and what does the recorded environment and tuple structure permit a reader to conclude from it?

Strongest source-supported thesis: the pooled figure is an exact answer to one counting question, but it is a value almost no environment takes — 24 of 36 scored environments sit at an endpoint, the 12 mixed environments hold 40.7% of scored cases, and the 340-row map beneath is 87% single-case rows — so the record supports a descriptive map of where judged outcomes fell and does not support a difficulty ranking, a mechanism, or a stability estimate.

Structures of the two drafts:

- `gpt 6 luna max` is a linear audit: counts → endpoint list → names → matrix → cell → `moco` → withdrawn → unscored → 10-vs-7 → labels/guarantees → selection → confounds → conclusion. Thirteen headed blocks for roughly 2,300 words; the reader meets findings in sequence rather than an argument. Its sections "Unscored cases are not failures", "Ten zero-pass environments or seven?", and "Confounds we cannot ignore" repeat caveats stated earlier.
- `opus 5` uses the same skeleton but opens with a reader's question ("What should I expect if I open one environment at random?") and adds a density/sensitivity passage and a sharper matrix reading ("the matrix mostly repeats the endpoint pattern one level down, which is close to inevitable when nearly nine rows in ten contain a single case"). It is still a sequence of audit blocks, and its conclusion imports a false limit ("nothing in the present archive supplies it").

What to move, combine, shorten, remove:

- Combine "Unscored cases are not failures" into the counting section (where the 405 vs 416 denominators are introduced) rather than a standalone block.
- Combine "The selection frame" with the counting section, because Figure 8 is the selection frame and the omissions table belongs beside it.
- Move the sensitivity table (currently under "What a cell means" in the internal article) to the density discussion.
- Shorten the three enumerations of 9/9 environments to one compact table or one line.
- Remove the Figure 2 lollipop in both drafts (contract forbids substitution for Figures 8–11).
- Merge "Confounds I cannot remove" into local caveats and a short bounded ending; a separate confounds section is the "ending disclaimer" pattern the house style warns against.
- Progression to enforce: intelligible problem (the average nobody has) → counting result and frame → environment map → what the tuple map adds (and does not) → what labels/guarantees record → withdrawn/open → bounded consequence.

### 2.2 Opening

- `gpt 6 luna max`: "Mercury-2.5 received PASS on **68.4% of 405 scored cases** in this archived campaign. That is a precise case-weighted rate, but it does not describe what happened in each environment." Specific, flat; the limit (judged outcomes, selected cases, one seed) arrives in paragraph three; no tension beyond the `ts_*` contrast.
- `opus 5`: "What should I expect if I open one environment at random?" Creates tension quickly; limit arrives in paragraph two ("These are verdicts assigned by the campaign's judges to selected cases"). Its closing line of the opening — "descriptively thin; the structure worth looking at is the map underneath it" — is a thesis sentence, reusable in meaning.
- Both openings use the identical `ts_*` 4/4, 0/4, 0/4 contrast, as does the current internal article. A fresh device is proposed in §3.

### 2.3 Examples and technical depth

Selected examples (all source-supported):

- The two largest endpoint blocks: `epistemic_games` 23/23 and `glyph` 0/24 (Table A). Both are `behavioral_reference`, which lets the article say the guarantee does not by itself separate them.
- Near-pooled environments: only `moco` 36/55 and `tensor_functor` 6/9 land within five points of 68.4% (Table A; Figure 9 order 13–14).
- `ts_*` and `sheaf_*` name contrasts (Table A) — keep, but as a second-level example, not the opening.
- `css_state_machine` nine rows all 2/2 (matrix) — the withdrawn claim.
- `sql_fixed_point` single FAIL at `hidden_depth=hard`, `surface_deceptiveness=easy` (matrix) — the "one observation" example.
- `moco` row #6: six cases, 1/6, five `overfit_visible_tests`, key `distractors=hard, naming=easy, queue_math=easy, symptom_mask=hard, temperature=hard, visible_tests=easy` — one descriptive example that the keys exist; no shape claim.
- Row 409 `ts_parse_only` PASS with `performance_eligible=False` and the recorded `exclusion_reason`.

Tables/figures and their roles:

| Element | Role | Keep/compact |
|---|---|---|
| Figure 8 (selection frame) | Shows 496 → 416 → 405 → 277/128; omitted cases outside every rate | Keep; caption must carry the unlabelled 11 |
| Four-way environment table (17/7/12/2) | Replaces three enumerations with parallel counts | Keep |
| Figure 9 (intervals) | Shows endpoint-heaviness and interval width by n | Keep; caption states Wilson/binomial convention |
| Mixed-environment table (12 rows) | Preserves distinct fractions and the +1 unscored | Keep; add a flags column for `rejected`/ineligible rows |
| Omissions table (class × environment) | Connects selection concentration to interpretation | Keep, compact (4 environments × 3 classes) |
| Sensitivity table (exclude `moco`/`glyph`) | Arithmetic illustration of density | Keep, three rows; label as arithmetic |
| Figure 10 (tuple matrix) | Shows single-case dominance and the 9 amber `moco` rows | Keep |
| Figure 11 + global label table + env-by-label table | Shows labels are recorded classifications with an environment breakdown | Keep; rebuild env-by-label rows so each environment is identifiable |
| Guarantee table (BR/CO: environments, PASS, FAIL, scored, unscored) | Shows the confound | Keep, two rows |

Do not add: mathematics (no `$`), a shared difficulty scale, a `moco` heat map by dimension, Mermaid or any new rendering dependency, Wilson arithmetic in prose.

### 2.4 Prose and tone

Faults with exact quotations:

- Stock transitions: `gpt 6 luna max` "Thus **277/405, or 68.4%**, is the scored-case pass rate"; "Together, the mixed environments contain…"; `opus 5` "So the matrix mostly repeats…", "So I keep **68.4%**…" (serviceable individually, formulaic cumulatively).
- Empty emphasis: `gpt 6 luna max` bolds "**416 selected cases in 38 environments**", "**277/405, or 68.4%**", "**277/416, or 66.6%**", "**340 environment-by-tuple rows**" — bold on every number dilutes the thesis marker the house style reserves bold for.
- Repetitive caveats: `gpt 6 luna max` states the one-seed limit in the opening, under "What a cell means", and again under "Confounds we cannot ignore"; `opus 5` repeats "I keep all nine in the counts" / "all ten stay in the 128" / "all ten remain in the 128".
- Overlong setup: `gpt 6 luna max` lists all 17 all-pass names in running prose and again partially in the "endpoint-heavy" section.
- Unsupported superlatives/mechanism words: `opus 5` "The 68.4% is sensitive to how tuples were unrolled into cases" ("unrolled" implies a design step no source describes); `opus 5` "Being unscored is a property of the judging pipeline" (cause assigned).
- Mechanical benchmark-report prose: `gpt 6 luna max` "The campaign records 189 `behavioral_reference` and 227 `compile_only` judge guarantees across the 416 selected cases, including the unscored cases." followed by a two-row totals table that adds nothing to the sentence.
- Invented first-person experience: none found that asserts a personal act beyond reading records. `opus 5` "I have not found the derivation behind the 10" is acceptable as a statement about the record. Heading "Confounds we cannot ignore" (`gpt 6 luna max`) breaks the first-person voice.
- Author's wording exclusions present in candidates (internal quotation preserved; must not enter public prose): `opus 5` "Density matters for the top line too."; `opus 5` "the honest list of what the archive declines to settle". The current internal article also contains two: "environment identity matters more than difficulty" and "how little the archive can actually support" (Importance field).

Calibration against reference excerpts: the reference posts open on a short declarative or a self-correction, move in one-to-four-sentence paragraphs, mark one thesis in bold, and attach the limit where the attractive reading would overrun. Adopt that movement. Do not reuse their metaphors, jokes, emoji, or formulations ("failed diagrams", "the first formalisation was wrong", etc.). No numerical prose ratings are assigned here.

### 2.5 Transitions and caveat placement

| Limit | Attach to |
|---|---|
| Selected-case denominator (405 vs 416) | Counting section, the sentence introducing 66.6% |
| Unknown outcomes (11 `infrastructure_unscored`) | Same paragraph; recorded label, no cause |
| One-seed scope (seed 0 in all supplied records) | First appearance of an endpoint or interval; Figure 9 caption; not a separate section |
| Selection and dependence | Omissions table (concentration in `moco`/`glyph`/`rope`/`epistemic_games`) and the multi-case-row paragraph |
| Judge-guarantee/environment confound | Guarantee table, immediately after 141/189 vs 136/216 |
| Undefined dispositions | Mixed table flags column and `monadic_reward` 0/9 line; one sentence in labels section |
| Provider-note conflict (row 409) | Beside `ts_parse_only` 4/4 wherever first cited |
| Dirty source / no clean comparator | Beside any reproduction or "would a clean tree change this" sentence, in the bounded ending |

Consolidation: state each limit once in full at its anchor; later references are a clause, not a paragraph. The ending summarizes what is open; it does not introduce new limits.

### 2.6 Claim support and traceability

Full table in §6. Headline items: both drafts and the current internal article wrongly state that `moco` tuple keys are unavailable; both drafts wrongly state env-by-label and env-by-guarantee breakdowns are unavailable; both drafts quote "one seed per cell" without a source; both call unscored cases a "judge-coverage gap"; both use a Figure 2 that the contract forbids (`gpt 6 luna max`'s embed is also broken: a bare "!" line). The current internal article adds two boundary violations ("the 24 cannot coexist with the selection frame"; casing treated as "a data-quality artefact") and one unsupported quotation. Overclaims and unsupported "unavailable" claims are both flagged; editorial preferences are labelled separately in §6.3.

### 2.7 Public-site fit

- Frontmatter: all three texts carry the exact contracted title/date/layout. Keep.
- Byline: present and exact in all three.
- Epistemic-status `<dl>`: five fields in order in all three. Prose field in both drafts ("first-person and exploratory"; "Written for this article") discloses nothing about process; a neutral AI-assisted statement is permissible and recommended. No field may claim human verification or replication. Remove "actually" from the Importance field of the current internal article.
- MathJax: no inline or display mathematics is needed; plain fractions and "×" do not require the loader. Omit `{% include mathjax.html %}` unless `$` appears; if it does, place it immediately after the frontmatter and before the byline; no external scripts.
- Figures: both drafts lack all four required figures and use `fig2_environment_outcome_lollipop.svg`; the current internal article carries fig8–fig11 in sensible positions. Alt text and captions must match Section E (see §7).
- Markdown/HTML: `gpt 6 luna max` has a malformed image line ("!" alone). Tables render as GFM; the current internal article's env-by-label table has two rows that bundle several environments with a "3, 2, 2, 1, 1, 1" cell — hard to read; rebuild.
- Internal provenance: no candidate exposes source paths, case IDs, or stage terminology. The current internal article's label `infrastructure_unscored` is a recorded field value, acceptable. Keep `[m-word]` where its passage remains. Headings such as "Claims withdrawn or left open" are fine; avoid "handoff", "packet", "reviewer", "Arena" in public prose.
- Reading flow: the current internal article runs over the 2,800-word target; trimming must come from enumerations and repeated caveats, not from evidence tables.

---

## 3. Original thesis, reader question, opening strategy

Thesis (to be stated once, in bold, early): 277/405 = 68.4% is the exact answer to one counting question, and in this campaign it is a value almost no environment took — the record supports a map of where judged outcomes fell, not a difficulty ranking, a mechanism, or a stability estimate.

Reader question: when a single pass rate is reported for a model across many environments, what should a reader expect from any one environment, and what would they need to know before trusting that expectation?

Opening device (described, not drafted): begin with the mismatch between the pooled value and the per-environment values — only two of 36 scored environments land within five points of 68.4%, while 24 landed at exactly all or exactly none — stated as a prediction problem the reader can hold in mind before any table appears. Within the first three paragraphs, name the three limits that govern every later number: judged verdicts on selected cases, seed 0 throughout the supplied records, two kinds of judge guarantee fixed by environment. Then a one-sentence revision note that the earlier version is replaced and that one claim is withdrawn below. This follows the reference-post grammar of a short declarative problem followed immediately by the bound on what it can mean, without copying either candidate's `ts_*` opening or any reference-post phrasing. The `ts_*` contrast is retained later as the smallest illustration of the name problem.

---

## 4. Section-by-section blueprint (target 2,000–2,800 words, excluding tables)

### 4.0 Frame
- Frontmatter exactly as contracted; byline; `<dl class="epistemic-status">` with five fields making supportable disclosures (retrospective reading of archived judgments; regrouping of 416 cases/38 environments/340 rows; drafting and revision AI-assisted; confidence high in counts and low in causal readings; why a pooled number needs its map). No MathJax include unless math appears.
- Revision note, one or two sentences: replaces the earlier version; headline unchanged; tuple layer added as description; one claim withdrawn, several left open, listed in their own section.

### 4.1 Opening (no heading, ~250 words)
- Purpose: pose the prediction problem and bound it.
- Progression: pooled value → how few environments sit near it → what the verdicts are and are not (judged outcomes, selected cases, seed 0, two guarantees) → thesis in bold.
- Evidence: Table A (two environments within five points; 24 endpoints).
- Caveat: PASS/FAIL labels do not establish understanding or general capability; an environment name is not a difficulty rating.
- Transition: "count first" — what the denominators are.

### 4.2 Counting the judged cases and the frame around them (~450 words)
- Purpose: fix 416/405/277/128/11 and the 496 frame; separate 68.4% from 66.6%.
- Progression: 416 selected → 405 scored → 277/128 → 11 `infrastructure_unscored` (recorded label, no recorded cause) → 277/416 answers a different question and must not be read as a rate that treats unknowns as failures → the 80 omissions before selection.
- Figure 8 here, caption carrying the 11-count and the note that the nine conflicting-disposition FAILs are not drawn.
- Omissions table: `moco` 35 twin; `glyph` 9 gate + 12 twin; `rope` 10 modality + 5 gate; `epistemic_games` 9 twin; totals 56/14/10. One sentence: the provenance summary says 24 known-gate omissions against the 14 in the detailed rows; both are reported; unresolved.
- Caveats attached: the 496 frame counts case IDs and is not the 340-row matrix; "design cells" is a chart label, not a definition; selection was not random and concentrated in three environments, which bears on how the map is read without establishing a causal effect.
- Transition: with the denominator fixed, how are the 405 distributed across environments?

### 4.3 An endpoint-heavy map (~500 words)
- Purpose: show the shape the pooled value compresses.
- Progression: four-way table (17/7/12/2) → 24 of 36 at an endpoint, resting on 4 to 24 cases → the 12 mixed environments hold 165 cases, 2/15 to 8/9 → one sentence on unweighted mean 69.2% and median 8/9 as different questions.
- Figure 9 here; caption names the 95% Wilson interval, its binomial sampling convention, that it is not seed variation, pooled line at 68.4%, and that environments with no scored case are not drawn.
- Mixed table with a flags column: `transformer_ssm_lift` 8/9 (lone FAIL `rejected`); `batchnorm_ema` 2/15 (one `rejected`, one `unscored`-disposition); `rd_adaptive_halting` 8/14 + 1 unscored; `moco` 36/55 (three `unscored`-disposition FAILs).
- Endpoint flags in prose: `monadic_reward` 0/9 with eight `rejected`; `ts_parse_only` 4/4 with one performance-ineligible PASS whose `exclusion_reason` describes a provider-attributed terminal failure — recorded attribution that conflicts with the verdict, not proof of cause; it stays in the 277. If space allows, one clause that the provenance's "1 retry, 60s" and the row's 19 attempts / 46.1 s are not reconciled.
- Caveats: one seed; within-environment agreement does not establish independence; dispositions undefined.
- Transition: names and density — why "the map" is not a set of families.

### 4.4 Names, density, and what moves the number (~400 words)
- Purpose: block two shortcuts — reading prefixes as families and reading the pooled rate as representative.
- Progression: `ts_*` (4/4, 0/4, 0/4) and `sheaf_*` (8/9, 0/9, 0/9) and `categorical_lenses`/`functorial_augmentation`/`tensor_functor` (9/9, 0/9, 6/9) → `glyph`, `moco`, `batchnorm_ema` supply 94/405 cases and 56/128 FAILs → sensitivity table (exclude `moco` 68.86%; exclude `glyph` 72.70%; both 73.93%) labelled as arithmetic on recorded rows → link back to the omissions concentration in the same environments.
- Caveat: shared names do not imply shared conditions; sensitivity is to selected case density, not to any described design step; no shared failure mechanism is implied.
- Transition: what sits beneath each environment number.

### 4.5 Beneath the environments: 340 rows (~450 words)
- Purpose: show what the tuple layer adds (thinness, uniformity) and what it cannot (scale, effect, ranking).
- Progression: 340 rows, 4–15 per environment → 296 single-case, 44 multi-case in four environments → 329 rated, 320 at 0 or 1, 9 fractional all in `moco` → 204 rows in environments with a uniform scored outcome plus 10 rows in two environments with no scored outcome (214 only if shared absence is grouped) → 98 zero-pass tuples in 19 environments, all 12 mixed environments included; a different count from the 7 zero-pass environments.
- Figure 10 here; caption: 340 squares, grey for 11 unscored rows, numbers on 44 multi-case rows, amber only in `moco`, columns not comparable across environments.
- "Cell" paragraph without the unattributed quotation: the supplied records show seed 0 for all 416 selected cases and record no second seed; 44 rows hold more than one case; the inference that a planning unit is a row rather than a case is the writer's reading of the arithmetic, not a recorded convention.
- `moco` paragraph corrected: the complete matrix records a tuple key for every row, including the nine fractional ones; one example row (#6, 1/6) is described; 34 key names are environment-specific, so no cross-environment scale, dimension effect, or ranking is read. The unscored `rd_adaptive_halting` row at all-`easy` is a recorded field, not a cause.
- Caveat: multi-case rows do not estimate within-row dependence; single-case rows can only be 0 or 1.
- Transition: what the labels on the 128 FAILs record.

### 4.6 What the labels and guarantees record (~400 words)
- Purpose: present recorded breakdowns as recorded, and the confound that prevents a judge-effect reading.
- Progression: Figure 11 + global table (51/49/11/9/5/3) → casing: 9 `RUNTIME_ERROR` and 2 `runtime_error` are normalised to one bucket as an analysis convention; uppercase cases carry disposition `scored`, lowercase `unscored`; recorded association, no explanation → env-by-label table (one environment per row where counts differ; small environments may share a row only if each environment's own labels stay legible) → dispositions: 10 `rejected` (8 `monadic_reward`, 1 `batchnorm_ema`, 1 `transformer_ssm_lift`) and 9 `unscored`-disposition FAILs with status `scored`; the disposition value "unscored" is not the status `infrastructure_unscored` → guarantee table: BR 11 environments 141/189, CO 27 environments 136/216 with all 11 unscored cases → each environment carries one guarantee, so the contrast is confounded with environment.
- Caveats: labels are classifications, not mechanisms; a compile-only PASS is not behavioral validation; a 9/9 under `compile_only` (five environments) records what that judge checked; the four BR 9/9 environments are named if the point is made.
- Transition: what the earlier version claimed and what the record leaves open.

### 4.7 Withdrawn and open (~250 words)
- Withdrawn: `css_state_machine` non-monotonic variation — all nine rows 2/2.
- Open, not findings: apparent non-monotonic patterns in `moco`; the single `sql_fixed_point` FAIL at `hidden_depth=hard`, `surface_deceptiveness=easy` is one observation and establishes no effect; no base rate computed.
- Source disagreements preserved: 7 scored zero-pass environments vs the overview's 10; 17 all-pass vs the overview's "~12"; 14 vs 24 known-gate omissions; dispositions undefined; provider note vs recorded fields for row 409.
- Caveat: no reconciliation is asserted; 14 + 10 = 24 may be mentioned once as an unverified possibility or omitted.

### 4.8 What this supports (~250 words)
- Restate: 277/405; 17/7/12/2; 24 endpoints; 320 of 329 rated rows binary because most rows hold one case; near-pooled environments are two.
- Does not show: a common difficulty scale or ranking; a mechanism for `glyph`, `moco`, `batchnorm_ema`; how endpoints behave under another seed; what a uniform guarantee or a clean source tree would change (source recorded dirty; no clean config-hash comparison).
- Bounded consequence: the next evidence the record cannot supply — repeated seeds within environments and guarantees varied within an environment — and what each would and would not settle.
- End on the counting question 68.4% answers, without a new caveat paragraph.

---

## 5. Retention and reconstruction decisions

### 5.1 Useful elements from `gpt 6 luna max` (reasons)
- The four-way environment table and the mixed-environment table — exact and compact.
- "Treating their cases as zero-pass would invent judgments that are not in the record." — the right meaning for the 11 unknowns; reuse the meaning, not the sentence.
- Keeping the ineligible PASS in the 277 with the conflict stated, and reporting 14 and 24 without reconciling.
- The clear statement that the tuples "are not a shared scale and must not be pooled, ranked, or regressed across environments."

### 5.2 Useful elements from `opus 5` (reasons)
- A question-led opening and the thesis meaning "arithmetically correct and descriptively thin".
- The reasoning that single-case rows force binary rates, so the matrix "mostly repeats the endpoint pattern one level down".
- The sensitivity arithmetic and "94 of the 405 scored cases but 56 of the 128 failures".
- The principle that flags "belong beside the counts rather than inside a footnote".
- The revision-note framing of the tuple layer as "exploratory description rather than as a result".
- "Closely named environments landed far apart." as a summary meaning.

### 5.3 Elements to remove or narrow (both drafts unless noted)
- Figure 2 lollipop and its captions (both); the bare "!" line (`gpt 6 luna max`).
- "one seed per cell" as a quotation (both; also current internal article).
- "judge-coverage gap" / "property of the judging pipeline" (both).
- `moco` "no row-by-row key" (both; also current internal article).
- "No environment-by-label breakdown is available here" and "nothing in the present archive supplies it" (`opus 5`); "The counts are global only; they do not show which environments produced which labels" and "I cannot compare environment results under one common judging standard" (`gpt 6 luna max`).
- "Describing a 9/9 environment as behaviourally settled would outrun what the judge checked." (`opus 5`) — narrow to the five compile-only 9/9 environments.
- "unrolled into cases" (`opus 5`).
- "no case was re-run under a second seed" / "no case was run again under a second seed" (both) — narrow to "the supplied records show seed 0 for every selected case and record no second seed".
- Guarantee totals-only table (`gpt 6 luna max`) — replace with the two-row guarantee table carrying environments/PASS/FAIL/unscored.
- Excluded wording: "Density matters…", "the honest list…" (`opus 5`); "matters more than difficulty", "actually support" (current internal article).
- Current internal article: "So the 24 cannot coexist with the selection frame as reported"; "I treat the casing difference as a data-quality artefact"; the speculative 7 + 2 + `rope` derivation; the duplicated "I report both and do not resolve the conflict."

### 5.4 Problems neither draft handles adequately
- Neither draft uses any of the four required figures.
- Neither distinguishes the disposition value `unscored` (9 FAILs with status `scored`) from the status `infrastructure_unscored` (11 cases).
- Neither connects omission concentration (`moco` 35, `glyph` 21, `rope` 15, `epistemic_games` 9) to the environments that dominate the FAIL count, which is the one place selection bears directly on reading the map.
- Neither names the `sql_fixed_point` FAIL tuple; both obscure the environment name.
- Neither records the overview's "~12 at 1.00" against 17.
- Neither states that both `epistemic_games` 23/23 and `glyph` 0/24 carry `behavioral_reference`, which is the compact way to show the guarantee does not sort the endpoints.
- Neither says what `epistemic_games` tests if it is mentioned beyond a count; if discussed, keep the bounded description (Bayesian inference over stipulated policies, not recursive theory of mind) and do not import the overview's "belief computation exact while decisions fragile".

---

## 6. Claim-check handoff

### 6.1 Evidence corrections (factual)

| ID | Candidate quotation / location | Source citation | v3 attribution | Required action | Remaining limit |
|---|---|---|---|---|---|
| CC-01 | `gpt 6 luna max`, "`moco`: the only fractional rows": "The available record does not link each fractional value to its tuple key, so I cannot draw the outcome shape across `moco`'s dimensions."; "Claims withdrawn": "the missing row-by-row tuple key also prevents reconstructing the pattern." `opus 5`, same section: "no row-by-row key links each value back to its tuple." Current internal article: "The archive has no row-by-row key linking each value to its tuple." | Complete matrix, all 15 `moco` rows with `difficulty_tuple` (e.g., 1/6 row: distractors hard, naming easy, queue_math easy, symptom_mask hard, temperature hard, visible_tests easy) | `grok 4.5` correction; `claude fable 5.1` blocking; local check | Replace with: keys are recorded for every row; description available; pattern remains open | No isolated dimension effect, no scale, one seed, no base rate; within-row dependence not estimated |
| CC-02 | Both: "214 rows—63% of the matrix—sit in environments where every row has the same outcome." / "214 of 340 rows (63%) sit in environments where every row has the same outcome."; `opus 5` ending: "63% of rows inside environments with a single uniform outcome" | Matrix: 148 all-pass rows + 56 zero-pass rows = 204; `epistemic_silence` 6 + `epistemic_type_games` 4 = 10 blank | Both reviewers; local check `uniform_scored_environment_rows` 204 | 204 in uniform-scored environments plus 10 in entirely unscored environments; 214 only when shared absence of scored outcomes is grouped | Uniform outcome is not stability |
| CC-03 | `gpt 6 luna max`: "The counts are global only; they do not show which environments produced which labels or establish a mechanism." `opus 5`: "**No environment-by-label breakdown is available here**"; "nothing in the present archive supplies it." | Table B (environment, `failure_mode_raw`); Table D `failure_modes`; JSON `failure_cross_tab`; reconciliation R4 | `claude fable 5.1` (blocking/correction); `grok 4.5` understated per R4 | State breakdown as recorded (e.g., `glyph` overfit 22; `sheaf_*` zero-pass environments underfit 9 each; `rd_adaptive_halting` RUNTIME_ERROR 5; `source_invalid` 8 + 1) | Labels are classifications, not mechanisms |
| CC-04 | `gpt 6 luna max`: "The totals alone do not show how outcomes are distributed by environment and guarantee, so I cannot compare environment results under one common judging standard." `opus 5`: "without an environment-by-guarantee breakdown I cannot test whether the environment contrasts survive a uniform standard." | Table D `judge_guarantees`; JSON cross-tabs; R4: BR 11 envs 141/189; CO 27 envs 136/216 + 11 unscored | `claude fable 5.1`; R4 | Reword to the confound: one guarantee per environment, so the contrast cannot be read as a judge effect | No within-environment variation in guarantee |
| CC-05 | `opus 5`: "Describing a 9/9 environment as behaviourally settled would outrun what the judge checked." | Table B/D: 4 BR 9/9 environments, 5 CO 9/9 environments | `claude fable 5.1` correction (its "six compile_only" is wrong); R1 | Restrict to the five compile-only 9/9 environments or name guarantees | BR PASS still records only what that judge checked |
| CC-06 | `gpt 6 luna max`: 'The phrase "one seed per cell" is ambiguous here'; `opus 5`: "The campaign records one seed per cell."; current internal article: 'The campaign describes its design as "one seed per cell"' | Absent from provenance, overview, packet; only Figure 8 bar label "design cells" | `claude fable 5.1` correction | Drop quotation and attribution; seed 0 rests on Table B; present any row-as-unit reading as the writer's inference | "design cells" is not a definition of "cell" |
| CC-07 | Both: "a judge-coverage gap"; `opus 5`: "Being unscored is a property of the judging pipeline, not of the case's outcome." | Table B rows 109–118, 243: status `infrastructure_unscored`, verdict blank, `failure_mode_normalized` `unknown` | `claude fable 5.1` correction | Use the recorded status; record no cause | None recorded |
| CC-08 | Both drafts omit the nine FAILs with status `scored` and disposition `unscored` | Table B rows 24, 145, 193, 214, 222, 232, 293, 405, 415; JSON `scored_fail_unscored_disposition` | Both reviewers; local check | Add beside the 10 `rejected`; keep all 19 in the 128 and in `n_scored` | Dispositions undefined; do not equate with `infrastructure_unscored` |
| CC-09 | `gpt 6 luna max`: bare "!" line + "*Figure 2: Lollipop chart…*"; `opus 5`: `![…](../figures/fig2_environment_outcome_lollipop.svg)` + "*Figure 2: One dot per environment…*" | Section E describes Figures 8–11 only; contract requires fig8–fig11 and forbids Figure 2 | Both reviewers; `grok 4.5` wrongly treated fig2 as required | Remove Figure 2; place the four required figures with Section-E-checked captions | SVGs not rendered here |
| CC-10 | Both: "no case was re-run under a second seed" / "no case was run again under a second seed" | Table B seed column; boundary: absence of repeated-seed data establishes nothing archive-wide | — | "the supplied records show seed 0 for every selected case and record no second seed" | Not a variance estimate |
| CC-11 | Current internal article: "So the 24 cannot coexist with the selection frame as reported" | Table C 14 (9 `glyph` + 5 `rope`); provenance "24"; Section E Figure 8 496 frame | Governing boundary; both reviewers kept 14/24 open | Remove the impossibility claim; report both; at most note 14 + 10 = 24 once as unverified | Origin of 24 unknown |
| CC-12 | Current internal article: "I treat the casing difference as a data-quality artefact rather than two kinds of runtime failure." | Table B rows 127, 128, 131, 133, 244, 246, 252, 256, 257 (`RUNTIME_ERROR`, disposition `scored`); rows 405, 415 (`runtime_error`, disposition `unscored`) | `claude fable 5.1` handoff ("recorded coincidence, no documented explanation") | Describe normalisation as an analysis convention; state the disposition association; no cosmetic or mechanistic explanation | None documented |
| CC-13 | Current internal article: "Seven all-fail environments plus the two with no scored case give 9. Adding `rope`… gives 10 only if `rope` is counted as zero-pass." | Table A; boundary: combining unscored environments and omitted `rope` does not verify the overview's definition | — | Trim to "unresolved"; if kept, label as not a verification | Overview's rule unknown |
| CC-14 | Neither draft; overview: "vs ~12 at 1.00" | Table A: 17 all-pass environments, 172/172 | `claude fable 5.1` note; R2 | Add to open-claims list beside 10 vs 7 | No explanation available |
| CC-15 | Both: "exclusion note describes a provider-attributed terminal failure" (acceptable); provenance "1 retry, 60s" | Row 409 / excerpt: `http_attempts_result` 19, `elapsed_seconds` 46.101, `provider_transport` `completed_with_errors`, `performance_eligible` False | `claude fable 5.1`; R3 | Attribute description to the recorded `exclusion_reason`; keep PASS in 277; if the provenance figures are mentioned, present the field contrast without unit conversion | Attribution is recorded, not established cause |
| CC-16 | Both obscure the environment: "the SQL-named `sql_fixed_point`" / "a SQL-named environment"; current internal article: "a SQL environment" | Matrix: `sql_fixed_point` FAIL at `hidden_depth=hard`, `surface_deceptiveness=easy`; 8/9 | — | Name the environment and the tuple; one observation establishes no non-monotonic effect | One seed; no base rate |
| CC-17 | `opus 5`: "The 68.4% is sensitive to how tuples were unrolled into cases for a handful of environments." | No source describes an unrolling step; Table A n_tuples/n_cases | `claude fable 5.1` note | "sensitive to selected case density" | Density is recorded, mechanism is not |

### 6.2 Open questions referred to the claim-check stage (no answers invented)
- Origin of the overview's "10" and "~12"; origin of the provenance's "24".
- Operational meaning of `rejected` and `unscored` dispositions.
- Whether "1 retry, 60s" and the row-409 fields count the same quantities.
- Whether any public source link (e.g., prior-work references) is verified usable before it appears in the article; none is required.
- Whether the four SVGs render as Section E describes (captions here are text-checked only).

### 6.3 Editorial preferences (not evidence corrections)
- Open with the "value almost no environment takes" device rather than `ts_*`.
- One compact table instead of three enumerations of all-pass environments.
- Drop the unweighted mean/median to a single sentence.
- Place the sensitivity table in the density section.
- Add a flags column to the mixed table rather than scattered sentences.
- Mention one `moco` row as an example rather than listing nine keys.
- Omit external citations unless verified; the article stands on the record.
- Prose field: a neutral AI-assisted statement; Certainty field without the word "actually".
- Prefer first-person headings over "we".
- Reduce bold to the thesis and the two denominators.

---

## 7. Final writer checklist

Frame
- [ ] Frontmatter exactly: `title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"`, `date: 2026-10-16`, `layout: post`; no extra fields.
- [ ] `{% include mathjax.html %}` only if `$`/`$$` appears, placed after frontmatter and before byline; no external scripts.
- [ ] Byline `*by <span class="icon-self">StrangeTcy</span>*`.
- [ ] `<dl class="epistemic-status">` with Original ideas, Synthesis, Prose, Certainty, Importance, in order; supportable disclosures; neutral AI-assisted statement permitted; no claimed human verification, replication, or author experiences.
- [ ] Concise revision note; a "withdrawn and open" section with `css_state_machine` withdrawn, `moco`/`sql_fixed_point` open, 10 vs 7, ~12 vs 17, 14 vs 24, dispositions, row-409 field contrast.

Figures (positions and captions checked against Section E; no claim of visual inspection)
- [ ] `../figures/fig8_selection_frame.svg` in the counting section. Caption: three stacked bars; 496 recorded case IDs = 416 selected + 80 omitted (56 intervention-twin, 14 known-gate, 10 unsupported input modality); 416 = 405 scored + 11 `infrastructure_unscored` (the 11-case segment is unlabelled in the image, so the count is given here); 405 = 277 PASS + 128 FAIL; omitted cases in pale grey enter no pass rate; the nine scored FAILs with a conflicting disposition are not drawn separately. Alt text describes bars, not "cells" as a definition.
- [ ] `../figures/fig9_environment_intervals.svg` in the map section. Caption: one dot per environment with scored cases (36; the two unscored environments are not drawn) at PASS/scored; bars are 95% Wilson intervals under a binomial sampling convention — not measured seed variation; dotted line at 277/405 = 68.4%; label beside each bar is k/n; colour classes no scored pass / mixed / all scored passed; selection and possible dependence limit interpretation.
- [ ] `../figures/fig10_tuple_matrix.svg` in the rows section. Caption: 340 squares, one per environment × tuple row, grouped by environment; colour is row pass rate (red 0, amber fractional, green 1); grey marks the 11 rows with no scored case; numbers mark the 44 rows holding more than one case; the 9 fractional rows are all `moco`; tuples are environment-specific, so columns are not comparable across environments.
- [ ] `../figures/fig11_failure_labels.svg` in the labels section. Caption: normalised failure label for all 128 FAILs combined (underfit 51, overfit_visible_tests 49, runtime_error 11 — consolidating 9 upper-case and 2 lower-case spellings — source_invalid 9, invalid_action 5, training_failed 3); no environment split in the image; environment breakdown in the adjacent table.
- [ ] No Figure 2; no other image paths.

Numbers and boundaries
- [ ] 416 / 405 / 277 / 128 / 11 distinct; 277/405 = 68.4% is the scored-case rate; 277/416 = 66.6% is the share of selected cases with an observed PASS; unknowns receive no judgment; compile-only PASS is not behavioral validation.
- [ ] 496 case-ID frame separate from 340 rows; "design cells" not used as a definition; seed 0 stated as a property of the supplied records only; no variance or correlation claims.
- [ ] Omissions: `moco` 35, `glyph` 21 (9 + 12), `rope` 15 (10 + 5), `epistemic_games` 9; classes 56/14/10; 14 vs 24 open; no impossibility claim; 14 + 10 = 24 at most once as unverified.
- [ ] 7 scored zero-pass environments; overview's 10 and ~12 recorded as unresolved; 98 zero-pass tuples in 19 environments stated as a different count; no derivation offered as reconciliation.
- [ ] Matrix: 340; 296/44; 329/320/9; 204 + 10 (214 only with shared absence stated); 34 key names environment-specific; keys recorded for all rows including `moco`; no scale, effect, trend, or ranking; `rd_adaptive_halting` all-easy row is a recorded field, not a cause.
- [ ] `css_state_machine` withdrawn (nine rows 2/2); `sql_fixed_point` FAIL named with its tuple; one observation ≠ effect.
- [ ] Guarantees: 11 BR environments 141/189; 27 CO environments 136/216 with all 11 unscored; one guarantee per environment; confound stated; four BR and five CO among the 9/9 environments if that point is made.
- [ ] Runtime casing: normalisation as convention; uppercase ↔ `scored`, lowercase ↔ `unscored` disposition stated without explanation.
- [ ] 9 `unscored`-disposition FAILs (5 `invalid_action`, 2 `training_failed`, 2 lowercase `runtime_error`) and 10 `rejected` FAILs (8 `monadic_reward`, 1 `batchnorm_ema`, 1 `transformer_ssm_lift`) visible; caveats beside affected comparisons (`monadic_reward` 0/9, `transformer_ssm_lift` 8/9, `batchnorm_ema` 2/15); no disposition definitions invented.
- [ ] `ts_parse_only` ineligible PASS attributed to its recorded `exclusion_reason`; conflict stated; PASS kept in 277.
- [ ] Retrospective, single-campaign scope; source recorded dirty; no clean config-hash comparison; no Atria or other-post numbers; no random-selection assumption; `epistemic_games`, if discussed, described as Bayesian inference over stipulated policies.

Prose
- [ ] Local caveats at their anchors (§2.5); no ending disclaimer paragraph; no repeated one-seed paragraphs.
- [ ] Keep `[ac-word]`, `[d-word]`, `[m-word]` where their passages remain; remove transcript debris (e.g., stray "!" lines) and malformed text.
- [ ] Author's wording exclusions honoured in all public prose and proposed wording; the exclusion notation itself does not appear.
- [ ] No internal paths (other than the four figure URLs), case/trace/finding IDs, internal post IDs, Arena/reviewer/model labels, extraction instructions, or stage terminology; no blueprint citations copied into the article.
- [ ] First-person, curious, technically literate; bold reserved for the thesis and key denominators; no numerical self-ratings; no copied reference-post phrases or personal claims.
- [ ] Length about 2,000–2,800 words with compact tables; required evidence retained even if the count runs over.

---

Scope statement: this blueprint is internal editorial work on one archived campaign. It performed no new evaluation, model fitting, causal estimation, web access, SVG rendering, or code execution; the arithmetic in §1.6 is a recheck of supplied rows. The current review verdicts remain as recorded and rated; the local source check and the reconciliation note are attributed as supporting local verification, not Arena verdicts. Nothing here constitutes acceptance by the claim killer, final writer, local validator, or human review.

&&&&&&&&

grok 4.5:
Markdown
# Mercury POST-02 — Editorial Critic Blueprint (v3)
**Internal report only. Not the article. Not a winner selection. Not a stitch job.**

## 1. State and evidence-review disposition

**Inputs read (complete):**
- Writer pair: `gpt 6 luna max` and `opus 5` (full drafts).
- COMPLETE_EVIDENCE_PACKET (Tables A–D, Section E Figs 8–11 descriptions).
- COMPLETE_DIFFICULTY_MATRIX_CSV (340 rows with full `difficulty_tuple` keys).
- CAMPAIGN_PROVENANCE, EARLIER_ANALYSIS_OVERVIEW, INELIGIBLE_PASS_CSV_EXCERPT.
- CURRENT_INTERNAL_ARTICLE.
- HOUSE_STYLE + ACTUAL_REFERENCE_POST_EXCERPTS + PRIOR_WORK_REFERENCES.
- SUPPORTING_LOCAL_SOURCE_CHECK + JSON (2026-10-29).
- CURRENT_V3_EVIDENCE_REVIEW_PAIR (`grok 4.5`, `claude fable 5.1`).
- ORCHESTRATION_CAPTURE_NOTE + supporting reconciliation note.
- Pinned commit `6ed48cb1c4447d4f902d1fbc8a908a56185e34ed`.

**Arena Web Search mode:** Enabled per orchestration; reviews report access to public Mercury-2.5/Inception pages and repo landing page. No campaign CSVs, hashes, or StrangeTcy commit content retrieved externally. All factual claims rest on embedded sources. No fabrication of additional access.

**Current review verdicts (as recorded):**
- Both: “accept with corrections.”
- `grok 4.5`: 0 blocking / 2–3 corrections (moco keys, 214 wording; mild label availability) + notes.
- `claude fable 5.1`: 1–2 blocking (moco keys; “no env-by-label/guarantee breakdown”) + several corrections (214, cell phrase, judge-coverage language, 9 disposition cases, Fig 2, etc.).
- Orchestration note: both rated “Both are bad” for substantive defects. Reviewer A retained false source-availability limits; Reviewer B had inconsistent 9/9 guarantee counts and unestablished execution claims. **Useful findings preserved only after recheck against rows; neither response is acceptance or publication clearance.**

**Unresolved reviewer disagreements / gaps:**
- Strength of “unavailable” language for env×label and env×guarantee (stronger correction in claude + local reconciliation supported; breakdowns aggregable from Table B/D).
- Exact 9/9 guarantee split: local reconciliation R1 corrects to 4 behavioral_reference + 5 compile_only (not 4+6).
- Fig 2 vs Section E Figs 8–11 (neither draft’s “Figure 2” matches packet numbering; content nearest Fig 9).
- “One seed per cell” attribution (phrase not in supplied sources).
- “Judge-coverage gap” / “judging pipeline” causal language vs recorded `infrastructure_unscored`.

**Missing / unverifiable:**
- Actual SVG binary renders (Section E text descriptions only; captions/alt must not claim visual inspection).
- Exact dirty working-tree state; clean config-hash comparison (0 checked).
- Origin of overview “10” zero-pass and “~12 at 1.00”.
- Operational definitions of `rejected` / `unscored` dispositions.
- Independent causation for `ts_parse_only` exclusion_reason (recorded attribution only).
- Base rate of apparent non-monotonicity; seed variance; any new runs.

**Local verification attribution (not Arena verdict):** Supporting check + JSON + reconciliation confirm core arithmetic (416/405/11; 277/128; 17/7/12/2; 340/296/44; 329/320/9; 98 zero-pass tuples; 204 uniform-scored rows + 10 fully unscored; omission cross-tab; guarantee 141/189 vs 136/216; 9 scored-FAIL + disposition unscored; 10 rejected). 214 only when blanks included; must not be described as 214 observed success/failure outcomes.

**Handoff gap:** No fresh independent claim-killer or final human validation of these candidates beyond the supplied v3 pair + local checks. Missing current clean review of the exact pair must remain explicit.

---

## 2. Seven-dimension comparison

### 1. Argument and structure
**Reader question:** What does the single 68.4% scored-case pass rate compress, and what do the environment map + tuple matrix add (and still cannot establish)?

**Strongest source-supported thesis:** On this archived seed-0 selection of 416 cases (405 scored), Mercury-2.5 received 277 PASS / 128 FAIL (68.4%). The distribution is endpoint-heavy (17 all-pass 172/172, 7 scored zero-pass 0/68, 12 mixed 105/165 +1 unscored, 2 fully unscored). The 340-row environment×tuple matrix is mostly singleton/binary (296/340 single-case; 320/329 rated rows exactly 0 or 1; 9 fractionals all in `moco`); dimensions are environment-specific (no shared scale). Selection (80 omissions), single seed, dirty source, guarantee/environment confound, undefined dispositions, and open 14-vs-24 / 7-vs-10 discrepancies bound every causal or general-capability reading.

**Structures:**
- `gpt 6 luna max`: Cleaner linear count → endpoints → names-as-handles → matrix → withdrawn/open → unscored → 7-vs-10 → labels/guarantees → selection → confounds → supports/does-not. Slightly more compressed; ends with broken “!” + Figure 2.
- `opus 5`: Similar skeleton with stronger density/sensitivity arithmetic early, more explicit “what this does not show,” and a live Fig 2 embed. Slightly more rhetorical framing of the pooled number as “descriptively thin.”

**Move/combine/shorten/remove:**
- Progress: intelligible pooled-rate problem → exact counts + selection frame (Fig 8) → endpoint map (Fig 9) → density/names caution → tuple matrix (Fig 10) → failure labels (Fig 11) + guarantee confound → withdrawn/open + unresolved discrepancies → bounded consequence.
- Avoid audit-findings-as-essay. Shorten repeated caveat lists into point-of-use attachments. Remove any “no breakdown available” claims. Do not sequence every local-check row as prose.

### 2. Opening
**gpt:** Direct 68.4% + ts_* contrast; solid but report-like.
**opus:** “What should I expect if I open one environment at random?” + ts_*; better tension, still close to internal article.

**Proposed fresh strategy (do not draft full opening or copy either):** Open on a concrete, source-supported contrast that makes the pooled rate feel immediately insufficient—e.g., the three `ts_*` environments (4/4 vs 0/4 vs 0/4) or the sheaf split (8/9 vs 0/9 vs 0/9)—then state that 277/405 = 68.4% is the precise answer to one counting question and the rest of the piece maps what that number hides and cannot support. Ground in supplied example; establish single-seed/selected/retrospective limit within first screen. No slogan replacement; no imported reference-post scene.

### 3. Examples and technical depth
**Keep exact supported examples:**
- ts_* trio; sheaf_* split; categorical_lenses 9/9 vs functorial_augmentation 0/9 vs tensor_functor 6/9.
- Density: glyph 0/24, moco 36/55, batchnorm_ema 2/15 → 94/405 cases, 56/128 FAILs.
- css_state_machine all 2/2 (withdraw variation claim).
- sql_fixed_point single FAIL at hidden_depth=hard, surface_deceptiveness=easy (one observation; no non-monotonic effect).
- moco: 15 rows, 6 endpoint + 9 fractional (values 1/6, 1/3, 2/5, 2/3, 3/4, 5/6); complete matrix supplies keys—descriptive mapping only, no difficulty effect/ranking/scale.
- rd_adaptive_halting unscored at all-easy five-dimension tuple (missing outcome ≠ easy-case failure).
- 10 rejected FAILs (8 monadic_reward source_invalid, 1 batchnorm_ema, 1 transformer_ssm_lift); 9 scored-FAIL + disposition unscored (all 5 invalid_action, 2 training_failed, 2 lowercase runtime_error).
- ts_parse_only row performance_eligible=False PASS kept in 277; exclusion_reason = recorded provider-attribution conflict.

**Tables/figures (roles):**
- Compact env-outcome summary table (17/7/12/2).
- Mixed-env rate table (or integrate into Fig 9 reading).
- Optional compact omission table (56/14/10) + dual 14/24 note.
- Optional sensitivity arithmetic (ex-moco/ex-glyph) as illustration only.
- Fig 8 (selection frame): 496 → 80 omitted + 416; 405 scored + 11 unscored; 277+128. Caption must state 11-case segment unlabelled on image; does not plot 9 conflicting-disposition cases.
- Fig 9 (env intervals): 36 scored envs, k/n dots, 95% Wilson (binomial sampling convention, not seed variance), pooled 68.4% line; selection/dependence limit.
- Fig 10 (tuple matrix): 340 squares, 11 grey, 44 multi-case numbered; columns not comparable; 9 amber fractionals in moco.
- Fig 11 (failure labels): global 51/49/11/9/5/3; env breakdown in article table (aggregable from records).
- No new math, shared difficulty scale, or rendering dependency. Prefer parallel counts over long enumerations.

### 4. Prose and tone
**Faults to excise:** Stock transitions (“Thus,” “So I keep”); empty emphasis; repetitive global caveat dumps; mechanical benchmark-report cadence; unsupported superlatives; invented first-person experiential claims; “judge-coverage gap” causal promotion; unattributed “one seed per cell”; “no key/no breakdown available” overclaims; any excluded fragments (“If you want”, “matters”, “but wait”, “actually”, “honest”, “Let me”).

**Strengths to calibrate (not copy):** Both drafts’ first-person exploratory voice tied to arithmetic; willingness to withdraw/leave open; dry precision. Match house-style curious technically-literate judgment and self-correction (reference excerpts) without distinctive metaphors, openings, or personal claims from those posts. Epistemic-status must disclose AI-assisted drafting/revision neutrally; no invented independent human verification or dual-model authorship.

### 5. Transitions and caveat placement
Attach limits at point of interpretation:
- Selected-case denominator + 80 omissions + 14-vs-24 → with selection frame / Fig 8.
- 11 infrastructure_unscored (not failures; recorded status) + 277/416 ≠ pass rate → with first counts.
- One-seed scope / no variance → with endpoints, matrix, and any stability language.
- Selection + possible dependence → with Fig 9 Wilson reading and matrix aggregates.
- Guarantee/environment confound (each env one guarantee; 11 BR / 27 CO; 141/189 vs 136/216) → beside any guarantee contrast; not a measured judge effect.
- Undefined dispositions (10 rejected + 9 scored/FAIL/unscored) → beside affected counts/comparisons (incl. monadic_reward 0/9, transformer_ssm_lift 8/9).
- Provider-note conflict on ts_parse_only → at its PASS mention; keep in 277.
- Dirty source + no clean config-hash → beside any reproduction claim ([m-word]).
- Compile-only PASS ≠ behavioral validation; PASS/FAIL ≠ understanding/mechanism/general capability.
- Epistemic_games: bounded Bayesian inference over stipulated policies, not recursive ToM (if mentioned).
Consolidate repetition; no ending-disclaimer dump that hides qualifications.

### 6. Claim support and traceability
(See §6 Claim-check handoff for full table. Key corrections both drafts share:)
- moco keys **exist** in COMPLETE_DIFFICULTY_MATRIX_CSV (both claimed unavailable).
- 214 → 204 uniform-scored-outcome rows + 10 fully-unscored-environment rows (local check).
- Env×label and env×guarantee breakdowns **aggregable** from Table B/D (remove “not available”).
- 9 scored-FAIL + disposition=unscored must be visible alongside 10 rejected.
- Fig numbering/captions must align to packet Figs 8–11 (or descriptive match only).
- Overview 10 vs Table A 7; provenance 24 vs Table C 14; overview ~12 vs 17 all-pass: preserve as open.
Distinguish editorial preference (pacing, example order) from evidence correction.

### 7. Public-site fit
- Frontmatter exact: title/date/layout as contracted.
- Byline + five-field `<dl class="epistemic-status">` (Original ideas, Synthesis, Prose, Certainty, Importance) with supportable disclosures; neutral AI-assisted OK.
- MathJax include only if inline/display math used (plain fractions do not require it).
- Four figure URLs only: fig8_selection_frame, fig9_environment_intervals, fig10_tuple_matrix, fig11_failure_labels. No earlier Fig 2 substitution.
- Captions/alt checked against Section E / SVG descriptions (unread render ≠ visually inspected).
- Intentional tokens `[ac-word]`, `[d-word]`, `[m-word]` retained where passages remain.
- No internal paths, case/trace/finding IDs, Arena/reviewer/model labels, stage terminology, or blueprint citations in public prose.
- Clean Markdown/HTML; repair any broken embeds (gpt “!”).
- ~2,000–2,800 words; retain required evidence over mechanical length.
- Concise revision note + substantive withdrawn/open-claims disclosure.

---

## 3. Original thesis and opening strategy

**Thesis (source-supported):** The 68.4% (277/405) scored-case pass rate on this archived Mercury-2.5 campaign is arithmetically exact for one question and descriptively thin: environment outcomes are endpoint-heavy, case density is uneven, the 340-row tuple matrix is mostly single-case binary with environment-specific dimensions, and selection, single-seed, dirty-source, guarantee confound, undefined dispositions, and open record discrepancies sharply limit causal, stability, or general-capability claims.

**Reader question:** What does 68.4% hide about where the cases sit, and what can the environment + tuple maps actually support?

**Opening device:** Concrete mini-contrast (ts_* 4/4 vs 0/4 vs 0/4, or equivalent supplied split) that makes “open one environment at random” immediately awkward, then name the precise counting question the 68.4% answers and signal that the piece maps the compression and its bounds. No copied candidate/reference opening; no full draft here.

---

## 4. Section-by-section blueprint

**Frontmatter + byline + epistemic-status + revision note**  
Exact YAML. Byline. Five-field dl (retrospective archive reading; regrouping 416 + 340 matrix; first-person exploratory tied to recorded arithmetic; high on counts, low on causal given seed/dirty/unscored/guarantees/selection; importance = pooled number hides distribution and support limits). Revision note: replaces earlier version; headline 68.4% unchanged; matrix added as exploratory layer; withdrawn/open listed explicitly.

**Opening (no heading)**  
Device above. Establish 416 selected / 405 scored / 277 PASS / 68.4%; 11 infrastructure_unscored; retrospective, not new runs; environment name ≠ difficulty.

**## First, count the cases that received a judgment**  
Purpose: Fix denominators.  
Evidence: Table A/B; 277/405 vs 277/416; summary table 17/7/12/2; unweighted mean ~69.2%, median 8/9.  
Fig 8 + caption (11 unlabelled on image; 9 conflicting-disposition not plotted).  
Local caveat: unscored ≠ FAIL; selected denominator.  
Transition → map shape.

**## The endpoint-heavy distribution**  
Purpose: Show 24/36 endpoints without capability-population claim.  
Evidence: 17 all-pass list (9×9/9 + largers/smallers); 7 zero-pass; mixed table; monadic_reward 8/9 rejected; transformer_ssm_lift rejected FAIL; ts_parse_only ineligible PASS flag.  
Fig 9 + caption (Wilson binomial convention; not seed variance; selection/dependence).  
Caveat: small-n endpoints; one seed.  
Transition → names unreliable.

**## Names are useful handles, not forecasts**  
Purpose: Kill prefix-family and density misreadings.  
Evidence: ts_*, sheaf_*, category-flavoured splits; glyph/moco/batchnorm_ema density (94 cases / 56 FAILs); optional sensitivity arithmetic as illustration.  
Caveat: no shared mechanism inferred.  
Transition → tuple layer.

**## A second layer: the environment × tuple matrix**  
Purpose: Exploratory description of arrangement, not difficulty effects.  
Evidence: 340 rows; 296 singleton / 44 multi (moco/glyph/css/epistemic_games); 329 rated / 320 endpoint / 9 fractional (moco); 34 dim names environment-specific; 98 zero-pass tuples in 19 envs; **204 uniform-scored rows + 10 fully unscored** (or 214 only if shared absence explicit).  
Fig 10 + caption.  
### What a “cell” means: all seed 0; cell ≈ env×tuple row by arithmetic inference (do not quote unattributed “one seed per cell”); no within-tuple dependence estimate.  
### moco: only fractionals; keys exist in complete matrix—optional compact descriptive map of 9 fractionals; no shape/effect claim; overall 36/55.  
Caveat: single-case rows make 0/1 unsurprising; no cross-env scale/ranking/regression.  
Transition → withdrawn/open.

**## Claims withdrawn or left open**  
Withdraw css_state_machine non-monotonic (all 2/2).  
Open: apparent moco / sql_fixed_point patterns (single seed, mostly binary, no base rate); sql one FAIL location noted without effect claim.  
Disclose 7 vs overview 10; 17 vs ~12; 14 vs 24 known-gate (identity 14+10=24 possible but unverified).  

**## Unscored cases are not failures**  
11 = 6 epistemic_silence + 4 epistemic_type_games + 1 rd_adaptive_halting (all-easy tuple). Recorded status infrastructure_unscored. rd remains 8/14 +1.  

**## Failure labels and judge guarantees**  
Fig 11 global + article env-breakdown table (aggregable; descriptive only; labels ≠ mechanisms). Runtime 9 RUNTIME_ERROR (scored) + 2 runtime_error (unscored disposition)—convention, no cosmetic mechanism.  
9 disposition=unscored FAILs + 10 rejected visible; undefined; stay in 128.  
Guarantees: 189 BR / 227 CO; per-env constant (11/27); scored 141/189 vs 136/216 +11 unscored in CO; **confound, not judge effect**. Compile-only PASS ≠ behavioral validation.  

**## The selection frame**  
80 = 56 twin + 14 known-gate + 10 modality (all rope); totals by env 35 moco / 21 glyph / 15 rope / 9 epistemic_games. Dual 14/24 open. rope absent from 38. Flags: rejected, unscored-disposition, ineligible PASS.  

**## Confounds that remain**  
Single seed 0; dirty source [m-word]; selection/dependence; guarantee confound; undefined dispositions; open discrepancies. No Atria/other-campaign numbers.  

**## What this supports—and what it does not**  
Restate 277/405, 17/7/12/2, matrix descriptive facts.  
Does not: common difficulty scale or env-vs-difficulty ranking; mechanisms for glyph/moco/batchnorm; seed stability; uniform-judge counterfactual; clean-source effect; understanding/general capability.  
Keep 68.4% for the precise counting question; map + bounds are the informative answer.  
Optional bounded next step (repeated seeds) without new-run claim.

**Withdrawn/open disclosure** already integrated; ensure visible.

---

## 5. Retention and reconstruction decisions

**Useful from gpt 6 luna max:** Tight count-first progression; clear withdrawn/open section; restrained tone; good endpoint/mixed separation; intentional [m-word].  
**Remove/narrow:** Broken “!”/Fig 2; moco “no key”; 214 unglazed; “judge-coverage gap”; light treatment of 9 disposition cases; global-only label implication.

**Useful from opus 5:** Density/sensitivity arithmetic; stronger “what this does not show”; live figure attempt; explicit thinness of pooled number; good monadic_reward/rejected handling.  
**Remove/narrow:** moco “no key”; repeated “no breakdown available”; 214; “unrolled” mechanism language; Fig 2 path/caption mismatch with packet; over-general “behaviourally settled.”

**Neither handles adequately (blueprint must supply):**
- Exact 204+10 uniform distinction with shared-absence language.
- Visibility of both 10 rejected and 9 scored/FAIL/unscored disposition.
- Aggregation-available env×label and env×guarantee stated as recorded cross-tabs + confound limit.
- moco keys present → descriptive option without effect claim.
- Fig 8–11 alignment + caption fidelity to Section E (Wilson convention, unlabelled 11, grey 11, etc.).
- Overview ~12 vs 17 noted beside 10 vs 7.
- Guarantee split on 9/9 envs (4 BR + 5 CO) if discussed.
- Provider field contrast (prose 1 retry/60s vs http_attempts 19 / 46.1s) left unresolved.
- Clean public voice free of internal labels while preserving every numerical boundary.

Do not stitch quoted paragraphs. Reconstruct argumentatively from evidence.

---

## 6. Claim-check handoff

| Candidate quotation / location | Source / v3 finding | Required action | Remaining limit |
|---|---|---|---|
| Both: moco “no row-by-row key / cannot draw shape / missing key” | COMPLETE_DIFFICULTY_MATRIX_CSV all 15 moco keys; grok #1, claude #1 (blocking) | Replace: keys present in complete matrix; optional descriptive fractional map; pattern stays open | No difficulty effect, ranking, or shared scale |
| Both: “214 of 340 (63%) … same outcome” | Local check: 204 uniform-scored + 10 fully unscored; grok/claude + reconciliation | Reword to 204+10 (or 214 only with explicit shared-absence) | Blanks ≠ observed success/failure |
| opus (strong): “No environment-by-label breakdown is available”; “nothing … supplies” env×guarantee/label | Table B/D fields; local failure_cross_tab / guarantee tabs; claude blocking + R4 | Delete unavailability; report aggregated descriptive counts | Not controlled comparison; labels ≠ mechanisms; guarantee confounded with env |
| gpt: “counts are global only; do not show which environments…” | Same | Soften; supply breakdown table | Same |
| Both (implicit/light): 10 rejected only | Table B + JSON: also 9 scored+FAIL+disposition unscored | Make both visible; undefined; stay in 128 | No operational definitions |
| Both: “judge-coverage gap” / “judging pipeline” | status=`infrastructure_unscored` | Use recorded status label | Cause not established |
| Both: “one seed per cell” (quoted or as campaign record) | Phrase absent from supplied sources; all seed=0 in Table B | Drop unattributed quote; state all selected seed 0 | No variance estimate |
| Both Fig 2 lollipop / broken embed | Section E = Figs 8–11; nearest content = Fig 9 | Align to fig9 (or 8–11 set); caption = Wilson, pooled line, binomial convention, no unscored envs; repair MD | Unread SVG ≠ visual inspection |
| Both: 7 zero-pass vs overview 10 | Table A=7; overview=10; tuple=19 | Keep 7; leave 10 open | Do not invent filter |
| Add: overview “~12 at 1.00” vs 17 | Table A/Matrix=17 (172/172); R2 | Note unresolved beside 10-vs-7 | No invented rule |
| Both: 14 vs 24 known-gate | Table C=14 (9 glyph+5 rope); provenance=24 | Report both; open; 14+10=24 unverified | Do not double-count or assert coexistence impossibility beyond frame arithmetic |
| Both: ts_parse_only ineligible PASS | Excerpt + row 409: PASS, eligible=False, exclusion_reason provider-attribution | Keep in 277; flag conflict; recorded attribution only | Not independent proof of cause; retry/time fields unresolved (R3) |
| gpt/opus guarantees “cannot compare under common standard” because totals only | Per-env constant; 141/189 vs 136/216 | Reword to confound (no within-env variation) | Not measured judge effect |
| Optional 9/9 guarantee split | R1: 4 BR + 5 CO | If mentioned, use 4+5=9 | — |
| css non-monotonic | All rows 2/2 | Withdrawn | — |
| sql_fixed_point / moco non-monotonic | One FAIL location; moco fractionals | Open, not findings | Single seed, no base rate |
| Runtime casing | 9 upper scored + 2 lower unscored disp. | Normalize to 11 for display; note association | No cosmetic/mechanism claim |
| Epistemic_games (if used) | Task evidence | Bayesian stipulated policies, not recursive ToM | — |
| Dirty source / reproduction | Provenance dirty=true; 0 clean hashes | [m-word]; no clean comparison | — |

**Editorial preferences (not evidence corrections):** Opening contrast choice (ts_* vs sheaf); whether to print full 9 moco fractional key table vs prose summary; exact sensitivity rows; heading wording; length within 2–2.8k while retaining evidence.

**Refer to next claim-check:** Any residual SVG pixel-level caption match; final public-link verification; unresolved overview/provenance origins if new primary sources appear. Do not invent answers.

---

## 7. Final writer checklist

- [ ] Frontmatter exact:  
  ```yaml
  ---
  title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
  date: 2026-10-16
  layout: post
  ---
 {% include mathjax.html %} only if real math used (immediately after frontmatter).
 Byline: *by <span class="icon-self">StrangeTcy</span>*
 <dl class="epistemic-status"> five fields in order, supportable text; neutral AI-assisted drafting/revision OK; no invented human verification or dual external authorship.
 Concise revision note + substantive withdrawn/open disclosure.
 Figures only:
../figures/fig8_selection_frame.svg
../figures/fig9_environment_intervals.svg
../figures/fig10_tuple_matrix.svg
../figures/fig11_failure_labels.svg
Captions/alt match Section E (11 unlabelled; Wilson binomial ≠ seed var; 340/11 grey/44 multi; global labels + table breakdown).
 Intentional tokens [ac-word], [d-word], [m-word] preserved; accidental debris gone.
 Numerical boundaries: 416/405/11; 277/128; 68.4% (277/405) vs 66.6% (277/416); 17/7/12/2; 172/68/165; 340/296/44/329/320/9; 98 tuples/19 envs; 204+10 uniform; 51/49/11/9/5/3; 189/227; 141/189 & 136/216; 80=56+14+10; dual 14/24; 10 rejected + 9 unscored-disp; ts_parse_only PASS kept; all seed 0; 7 (not 10) scored zero-pass; css all 2/2 withdrawn; moco keys usable descriptively; no shared scale/ranking/causal/seed-variance/clean-hash.
 Local caveats at point of use (selection, seed, dirty [m-word], confound, dispositions, open discrepancies, compile-only limit).
 No excluded word fragments in public prose.
 No internal paths, IDs, Arena/reviewer/model labels (gpt 6 luna max/opus 5 etc.), stage terms, or blueprint citations in public text.
 Public citations only verified usable links supporting adjacent claim (prior-work list discipline).
 ~2,000–2,800 words; evidence retained over word-count pressure.
 Clean Markdown/HTML; no broken embeds; house-style voice/pacing without copied distinctive phrases.
 Retrospective single-campaign scope only; no new evals, fitted models, or cross-campaign imports.

End of blueprint. Do not produce the article, dispatch stages, or claim claim-killer / final-writer / local-validator / human-review passage.
<END SOURCE CURRENT_EDITORIAL_BLUEPRINT_PAIR>
<BEGIN SOURCE SUPPORTING_REVIEW_RECONCILIATION>
# Mercury POST-02 — supporting reconciliation of current review claims

Checked 2026-10-29 against the pinned local sources. This note is local row and field verification for the subsequent claim check. It is not an Arena verdict, a replacement review, a prose revision, or final-article validation. The saved candidate and reviewer responses remain unchanged. No browser, Python, or new evaluation run was used.

The review being checked is `Mercury-POST-02-redo-evidence-check-v3.retry-1.responses.md`, labelled `grok 4.5` and `claude fable 5.1`. Its SHA-256 at inspection was `2af1df655f53f29d726b54ec5d8da3e81b3492d6a5997bc0fc5739cf7911ef93`. Citations below use its saved line numbers and section descriptions.

Source identifiers below are relative to `arena-handoffs/Mercury-POST-02-redo-writer-revision-v2.sources/campaign-02-analysis/`, pinned to `6ed48cb1c4447d4f902d1fbc8a908a56185e34ed`:

- **Packet:** `post-production/handoffs/POST-02-redo_evidence_packet.md`, Tables A, B, D.
- **Matrix:** `evidence/generated2/environment_difficulty_matrix.csv`; grouped by `environment`, summing `n_scored` and `n_pass`.
- **Cases:** `evidence/generated/case_results.csv`; grouped by `environment`, `judge_guarantee`, `status`, `verdict`, and `failure_mode_raw` as relevant.
- **Overview:** `ANALYSIS_OVERVIEW.md`, Key patterns 1.
- **Provenance:** `evidence/PROVENANCE.md`, Scope.

PowerShell `Import-Csv`, grouping, and numerical sums were used. The five source hashes were reread and match the corresponding entries in `Mercury-POST-02-editorial-critic-v3.sources.record.json`.

## R1 — nine 9/9 environments; four behavioral-reference and five compile-only

**CORRECTION_REQUIRED in one reviewer sentence.** The matrix contains exactly nine environments with `n_pass = n_scored = 9`. Both candidates' nine-name enumerations are supported, as is the `claude fable 5.1` confirmed-arithmetic row at review line 131. Its later statement at line 176, “four 9/9 environments are behavioral_reference ...; six are compile_only,” has the wrong compile-only count.

| Recorded guarantee | 9/9 environments | Count |
|---|---|---:|
| `behavioral_reference` | `categorical_lenses`, `ci_dependency_graph`, `spreadsheet_dataflow`, `template_interpreter` | 4 |
| `compile_only` | `architecture_naturality`, `neuro_symbolic_parser`, `semiring_unification`, `stochastic_monad`, `tokenizer_adjunction` | 5 |

Source: Packet Table A, the nine named environment rows; Matrix, all rows for those environments; Cases, all selected records for those environments and their `judge_guarantee` fields. Carry **four plus five equals nine** into the next claim check; preserve the original review verbatim.

## R2 — historical “~12 at 1.00” versus 17 all-pass environments

**SUPPORTED historical discrepancy; UNRESOLVED explanation.** The `claude fable 5.1` additions at review lines 164 and 194 are supported. Overview Key patterns 1 says “vs ~12 at 1.00.” Packet Table A and Matrix instead yield 17 environments with positive `n_scored` and no FAILs.

The grouping is nine at 9/9, one at 18/18, two at 15/15, one at 23/23, two at 6/6, and two at 4/4: **17 environments and 172/172 scored cases**. The two environments with no scored outcomes do not enter this count. No rule in the supplied overview explains its approximate twelve. Record this alongside the already identified historical ten versus seven scored zero-pass environments; do not invent a historical filtering rule or replace the source text.

## R3 — provider prose and recorded attempt/time fields

**SUPPORTED field contrast; UNRESOLVED equivalence of units.** The `claude fable 5.1` claim at review line 195 accurately transcribes the available values. Provenance Scope calls `ts_parse_only__witness_status=broken_representation=flat__seed-0` a provider-outage case with “1 retry, 60s.” Its Cases row, also supplied as the complete ineligible-PASS excerpt, records:

| Field | Recorded value |
|---|---|
| `http_attempts_result` | 19 |
| `http_attempt_ceiling_result` | 240 |
| `elapsed_seconds` | 46.101 |
| `stage_statuses.provider_transport` | `completed_with_errors` |
| `status` / `verdict` | `scored` / `PASS` |
| `performance_eligible` | `False` |

Packet Table B identifies this as row 409. The full Cases row's `exclusion_reason` is “campaign report provider-outage case; final result explicitly attributes terminal failure to provider transient after bounded retries.” Its `final_notes` is empty and `final_metrics` supplies task labels, without a reconciliation of the attempt/time quantities.

The supplied records do not establish whether “1 retry” means the same unit as an HTTP attempt or whether “60s” denotes the measured elapsed duration. Therefore, retain an unresolved prose-versus-field contrast, not an asserted conversion or mechanism. These fields do not independently prove provider causation or authorize removing the recorded PASS.

## R4 — failure and guarantee breakdowns are available

**The stronger availability correction is supported.** In `grok 4.5`, review lines 40 and 65 accept unavailable environment-by-guarantee claims; line 63 says “Packet supplies globals” and softens the failure-breakdown correction to absence of a prebuilt table. Those conclusions understate the supplied packet. Packet Table B explicitly includes environment, verdict, guarantee, and both failure-label fields. Table D explicitly includes environment, `failure_modes`, and `judge_guarantees` (field descriptions at packet lines 57 and 567). An environment-level display table need not already exist for these recorded breakdowns to be available by aggregation.

The corresponding `claude fable 5.1` corrections at review lines 150–152 and 170–174 are supported. Cases produces exactly one guarantee per environment, with these totals:

| Guarantee | Environments | PASS | FAIL | Scored | Infrastructure-unscored |
|---|---:|---:|---:|---:|---:|
| `behavioral_reference` | 11 | 141 | 48 | 189 | 0 |
| `compile_only` | 27 | 136 | 80 | 216 | 11 |

The reviewer’s failure-breakdown examples also match the case rows: `source_invalid` is eight `monadic_reward` plus one `transformer_ssm_lift`; `rd_adaptive_halting` has five uppercase `RUNTIME_ERROR` FAILs; underfit counts include nine in each of the two zero-pass sheaf environments, six in `functorial_augmentation`, and four each in `gnn_message_passing` and `ssm_parallel_scan`.

Thus, remove evidence-unavailability claims from the factual handoff. Preserve the separate limit: guarantee is constant within each environment, so those counts do not supply a controlled within-environment comparison or a measured judge effect. Failure-label counts likewise do not identify mechanisms. Distinguish a missing preformatted display from missing source data.

No other review claims were audited in this note.

<END SOURCE SUPPORTING_REVIEW_RECONCILIATION>
<BEGIN SOURCE SUPPORTING_BLUEPRINT_RECONCILIATION>
Supporting orchestration findings (not an Arena verdict): Editorial A, claude fable 5.1, section 4.2 says selection was not random and concentrated in three environments. Non-randomness is not established; omission rows cover FOUR environments (moco 35, glyph 21, rope 15, epistemic_games 9). Its section 4.4 links the moco/glyph/batchnorm failure-density trio to omissions in the same environments; batchnorm has no omission rows. It says single-case rows can only be 0 or 1; qualify SCORED singleton rows: 285 scored + 11 unscored = 296. Its planning-unit inference is unsupported. Editorial B, grok 4.5, similarly proposes cell approximately equals environment-by-tuple row by arithmetic inference; the contract prohibits inferring that technical definition. It often joins shared paraphrases as quotations in its handoff; verify exact wording separately against each candidate. Both blueprints were rated Both are bad. They are completed reports with material defects, not acceptance. Evidence-review pair was also rated Both are bad; source evidence controls every conclusion. The evidence pair is complete rendered text, HTML preserved. Editorial A is exact Markdown code-block text; B is complete rendered text after its nested fence closed early. Capture labels or code-fence debris are not public prose. Recheck all findings independently against supplied rows; do not infer missing evidence merely because a prior review was poor.
<END SOURCE SUPPORTING_BLUEPRINT_RECONCILIATION>
<BEGIN SOURCE SUPPORTING_SVG_SOURCE_CHECK>
{
  "schema_version": 1,
  "checked_on": "2026-10-29",
  "scope": "Supporting inspection of existing SVG source; not an Arena verdict or final-article validation.",
  "method": "Read-only PowerShell and .NET XML parsing with external XML resolution disabled; source geometry, text nodes, counts and SHA-256 inspected.",
  "source_result": "PASS",
  "visual_rendering": "NOT_PERFORMED",
  "modifications": "Only this supporting JSON report was created.",
  "figure_directory": "C:/Users/hatgu/epistemic-compiler/arena-handoffs/Mercury-POST-02-pipeline-resources/campaign-02-analysis/figures",
  "source_description": "arena-handoffs/Mercury-POST-02-redo-writer-revision-v2.sources/campaign-02-analysis/post-production/handoffs/POST-02-redo_evidence_packet.md, Section E",
  "figures": [
    {
      "file": "fig8_selection_frame.svg",
      "existence": "PRESENT",
      "bytes": 5994,
      "sha256": "1adc919e00bd4af48a39f7df40bf60bf51daf193b075c496db702ad300d5a98d",
      "xml_parse": "PASS",
      "checks": {
        "stacked_bars": {
          "status": "PASS",
          "observed": 3,
          "evidence": "Eight clipped segment paths, patch_3 through patch_10, occupy three distinct horizontal bands: y=201.486281, 135.578589 and 69.670897. Text labels: Scored cases, Selected cases, Design cells."
        },
        "eleven_case_segment": {
          "status": "PASS",
          "observed": 11,
          "evidence": "Grey patch_6 is adjacent to the 405 scored segment. Its width ratio to patch_5 times 405 equals 11 to six decimals. Section E identifies it as unscored."
        },
        "eleven_numeric_label": {
          "status": "ABSENT_AS_EXPECTED",
          "evidence": "All 12 text elements were read. None labels the grey segment with 11. The caption must supply the count."
        },
        "visible_count_labels": [
          "277 PASS",
          "128 FAIL",
          "405 scored",
          "416 selected",
          "56 intervention-twin, 14 known-gate,",
          "10 unsupported input modality (rope)"
        ],
        "disposition_conflicts": {
          "status": "NOT_PLOTTED",
          "evidence": "The three bars encode scored outcomes, selected status and omissions. No separate segment or label describes the nine conflicting dispositions."
        }
      },
      "caption_limits": "The source title uses design cells for 496; this label does not define a technical unit. Retain the eleven-case caption count and the selected/scored distinction."
    },
    {
      "file": "fig9_environment_intervals.svg",
      "existence": "PRESENT",
      "bytes": 46798,
      "sha256": "fab530a275cb51b6ba2102c449b033cae0a270f5f89104433ca2a5b999244bc3",
      "xml_parse": "PASS",
      "checks": {
        "interval_label": {
          "status": "PASS",
          "exact_text": "Pass fraction among scored cases (dot); 95% Wilson interval (bar)"
        },
        "environment_intervals": {
          "status": "PASS",
          "observed": 36,
          "color_groups": {
            "no_scored_pass": 7,
            "mixed": 12,
            "all_scored_passed": 17
          },
          "evidence": "Direct clipped interval paths under axes_1, grouped by red, amber and green stroke, excluding the one dashed pooled reference path."
        },
        "pooled_reference": {
          "status": "PASS",
          "label": "pooled 68.4%",
          "dashed_paths": 1
        },
        "wilson_endpoint_spot_checks": {
          "status": "PASS",
          "method": "Mapped SVG endpoint coordinates onto axis ticks 0 and 1; compared with Wilson formula using z=1.959963984540054.",
          "zero_of_four_upper": {
            "svg": 0.48989084,
            "computed": 0.489890836
          },
          "nine_of_nine_lower": {
            "svg": 0.700854948,
            "computed": 0.700854952
          },
          "limit": "Two distinct endpoint calculations checked; not a recomputation of every interval."
        }
      },
      "caption_limits": "Use a binomial sampling convention with selection and possible dependence qualifications. These intervals do not measure seed variation. Two entirely unscored environments are outside the 36 plotted environments."
    },
    {
      "file": "fig10_tuple_matrix.svg",
      "existence": "PRESENT",
      "bytes": 99887,
      "sha256": "d3811935a4000fe7fbb57ff52799ae5c4d0593878d9b441ec81e2f95d5198b5e",
      "xml_parse": "PASS",
      "checks": {
        "data_glyphs": {
          "status": "PASS",
          "observed": 340,
          "evidence": "Clipped patch paths directly under axes_1, excluding axes/background and legend patches. Source title: Each square is one environment x difficulty-tuple row (340 rows). Paths are rectangular cell glyphs."
        },
        "environment_rows": {
          "status": "PASS",
          "observed": 38,
          "evidence": "38 environment text nodes under matplotlib.axis_2."
        },
        "unscored_glyphs": {
          "status": "PASS",
          "observed": 11,
          "evidence": "11 data paths use fill #9e9e9e; the legend identifies grey as unscored."
        },
        "scored_glyphs": {
          "pass_rate_one": 222,
          "pass_rate_zero": 98,
          "fractional": 9
        },
        "multicase_numbers": {
          "status": "PASS",
          "observed": 44,
          "label_frequencies": {
            "2": 27,
            "3": 9,
            "4": 4,
            "5": 1,
            "6": 3
          },
          "evidence": "44 direct text annotations under axes_1 use font-size 6px; the title says Numbers mark rows with several cases; most rows hold one."
        }
      },
      "caption_limits": "Columns represent environment-specific tuples and are not comparable across environments. Eleven unscored matrix rows are distinct from the ten rows belonging to entirely unscored environments."
    },
    {
      "file": "fig11_failure_labels.svg",
      "existence": "PRESENT",
      "bytes": 10345,
      "sha256": "bf74789998f679b7d272c74a8a1e125369ca8fc1c028149c1bf25de030ce1187",
      "xml_parse": "PASS",
      "checks": {
        "failure_total": {
          "status": "PASS",
          "observed": 128,
          "exact_axis_label": "FAIL outcomes (n = 128)"
        },
        "bars": {
          "status": "PASS",
          "observed": 6
        },
        "labels_and_counts": {
          "underfit": 51,
          "overfit_visible_tests": 49,
          "runtime_error": 11,
          "source_invalid": 9,
          "invalid_action": 5,
          "training_failed": 3
        },
        "count_sum": 128,
        "aggregation": {
          "status": "PASS",
          "exact_title": "Recorded failure labels, all environments combined",
          "exact_footer": "Global counts across all 128 FAIL outcomes; the per-environment breakdown is in the article text."
        }
      },
      "caption_limits": "The SVG contains global failure counts, with no environment split. The final article must supply its environment breakdown separately. Runtime aggregation is an analysis convention."
    }
  ],
  "recommended_candidate": {
    "path": "C:/Users/hatgu/epistemic-compiler/arena-handoffs/Mercury-POST-02-pipeline-resources/campaign-02-analysis/posts/POST-02-cross-environment-map-v3-final.md",
    "parent_directory": "PRESENT",
    "proposed_file_at_inspection": "ABSENT",
    "action_taken": "NONE; location recommendation only.",
    "relative_links": [
      "../figures/fig8_selection_frame.svg",
      "../figures/fig9_environment_intervals.svg",
      "../figures/fig10_tuple_matrix.svg",
      "../figures/fig11_failure_labels.svg"
    ],
    "resolution": "All four paths were resolved from the existing posts directory to the inspected original SVG files.",
    "preservation": "A new filename in posts preserves the current internal article and original SVG files."
  },
  "limits": [
    "No visual rendering, browser inspection or publication check was performed.",
    "SVG source inspection confirms labels and encoded shapes, not final page layout or readability.",
    "Two Wilson endpoint spot checks passed; all 36 interval values were not independently recomputed."
  ]
}

<END SOURCE SUPPORTING_SVG_SOURCE_CHECK>
