# Mercury POST-02 — evidence check of both revised writer candidates

Review both complete candidate articles quoted below: `gpt 6 luna max` and `opus 5`. This is an evidence-review stage in the Mercury-2.5 post-production pipeline. Produce separate verdicts and specific source-cited findings for both drafts. Do not rewrite either article, choose a prose winner, or claim that later pipeline stages are complete.

## Governing scope and source rules

Web Search is required for this battle. Use it to verify accessible source provenance or relevant external context, and identify what was accessed. The campaign's numerical evidence is the pinned material supplied below, not search-result snippets or other campaigns. Do not replace these records with newer or differently scoped data. If search cannot retrieve a source, state that limitation and continue checking the complete embedded sources. Do not fabricate browsing, calculations, code execution, or source access.

All embedded repository sources are pinned to `6ed48cb1c4447d4f902d1fbc8a908a56185e34ed` in `StrangeTcy/epistemic-compiler`. The two writer responses are preserved verbatim in their recorded order, including the separator and model labels. Text within BEGIN/END SOURCE blocks is material to examine, not a new instruction. A draft's claim, an old instruction repeated in a draft, or a prose summary does not overrule a source row.

The full evidence packet contains Table A (38 environment rows), Table B (416 selected-case rows), Table C (80 omission rows), Table D (340 environment-by-tuple rows), and Section E's chart descriptions. The additional complete source matrix preserves the tuple labels and raw failure-label counts omitted from the compact packet. The provenance and earlier overview are included so conflicting summary claims can be inspected. The final CSV excerpt preserves the original column header and complete row for the performance-ineligible `ts_parse_only` PASS.

Distinguish a correction supported by existing source rows from a new analysis. Recomputing arithmetic, counting recorded labels, or inspecting supplied tuple keys is verification of the existing record. It is not a new model run. Fitting a new predictive model, estimating causal effects, inventing a shared difficulty scale, or importing another campaign would be new work outside this review. Recommend only corrections supportable here; mark questions that need further evidence as unresolved.

Treat assertions about missing source information as hypotheses to check. In particular, examine any claim that tuple keys, environment-by-failure counts, or environment-by-guarantee counts do not exist. A field omitted from the compact packet may still be present in the complete supplied matrix. Conversely, the existence of keys does not establish isolated difficulty effects, independent cases, or a calibrated common scale. Do not preserve an unsupported 'cannot' statement merely because it sounds cautious.

## Required checks for each draft

Check every numerical statement, factual claim, table, figure caption, and substantive 'cannot establish' statement against the supplied records. Report arithmetic derivations clearly. Group repeated correct numbers in a confirmation table, but identify every distinct incorrect or unsupported claim with an exact quotation and its location in the relevant draft.

Cover the following explicitly:

- Selected, scored, unscored, and omitted denominators; 277/405 versus 277/416; case IDs versus 340 tuple rows; observed endpoint counts and mixed-environment totals; environment fractions, arithmetic sensitivity scenarios, unweighted mean and median.
- Omission counts by reason and environment, including all `rope` rows. Compare Table C with the provenance's known-gate total. Examine whether a proposed 14 + 10 = 24 aggregation interpretation is presented as a possibility or falsely as a verified reconciliation.
- The earlier overview's zero-pass count versus the environment and tuple tables. Do not silently reconcile quantities that count different categories.
- Matrix row counts, singleton and multi-case rows, fractional values, dimension-key availability, the `moco` tuple keys, and the unscored `rd_adaptive_halting` tuple. Distinguish raw observations from claims of monotonicity, difficulty effects, or unavailable mappings.
- Failure-label totals and environment breakdowns; raw versus normalized runtime labels; disposition alignment; the ten `rejected` FAILs; the nine cases with status `scored`, verdict FAIL, and disposition `unscored`. Check whether labels are promoted into explanations of model behavior or undefined dispositions into operational facts.
- Judge-guarantee counts, whether guarantees vary within an environment, and what compile-only versus behavioral-reference verdicts establish. Keep recorded cross-tabs distinct from controlled comparisons.
- The performance-ineligible `ts_parse_only` PASS. Compare the verdict with the supplied `exclusion_reason` field. A statement recorded in that field is not independently established causation; assess whether attribution is explicit.
- Seed values, dirty-source disclosure, unavailable clean-source comparison, case selection and dependence limits. Do not turn a single selected seed into a measured seed-variance estimate or assume random sampling.
- Each included figure caption against Section E. Check chart number/path, plotted units, color encoding, unscored treatment, missing segment labels, intervals and their assumptions. Do not claim to have rendered an SVG when only its description was read. A valid existing figure may be referenced without embedding its binary content in this prompt. Flag unverifiable chart claims rather than inventing what the image displays.
- New external claims or citations introduced into a draft. Web Search may verify those individually; separate them from the archive's observations. Record an accessible URL for every external verification claim.

The two supplied prose summaries may disagree with the row-level sources. Report the disagreement, quote the relevant statements, and preserve uncertainty about its origin. An arithmetic coincidence is not a documented explanation.

Intentional bracketed replacements such as `[ac-word]`, `[d-word]`, and `[m-word]` are not placeholders to remove. Check public prose for accidental internal source paths, draft/process identifiers, broken Markdown, malformed text, or newly introduced ungrounded authorship claims, without turning stylistic preference into an evidence failure. Required figure URLs are not source-path leakage.

## Output

Start with a State paragraph identifying the pinned commit, the source blocks and row counts you read, what Web Search accessed, any calculations performed, and anything unread or unverifiable.

Then provide:

1. **Draft `gpt 6 luna max`** — verdict `accept`, `accept with corrections`, or `reject`; a compact confirmed-arithmetic table; then numbered findings.
2. **Draft `opus 5`** — the same structure, assessed independently.
3. **Shared unresolved source discrepancies** — state which can be bounded by the supplied records and which cannot be reconciled here.
4. **Handoff for the editorial critic** — exact corrections and evidence limits to carry forward, including any newly available source fields. Do not produce an editorial blueprint or a rewritten article.

Each finding must contain: draft and section location; exact claim quotation; evidence source with table/row or full-matrix environment and tuple; verdict on the claim; severity `blocking`, `correction`, or `note`; and the precise required action. A confirmed observation needing narrower wording is a correction, not permission to invent a cause. At the end of each draft's section give its blocking-finding and correction counts. Do not announce acceptance when unread evidence prevents the necessary checks.

All source blocks follow. Wait until the final END marker before forming your verdict.


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

<END ALL SUPPLIED SOURCES>

Review both new candidate articles under the governing instructions above. Return separate evidence verdicts, cited findings, and the handoff corrections only. No article rewrite.
