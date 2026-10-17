grok 4.5:

```html
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

The `sheaf_*` names create the opposite trap. `sheaf_schema_sync` passed 8/9, while `sheaf_invariant_gluing` and `sheaf_physical_constraints` each passed 0/9. Grouping all three under a single “sheaf performance” discards the comparison that matters. Category-theory-flavored names are no more predictive: `categorical_lenses` passed 9/9, `functorial_augmentation` passed 0/9, and `tensor_functor` passed 6/9. These examples show that a shared name does not imply shared outcomes, shared cognitive demands, or even shared evaluation infrastructure inside this packet. The outcome map is tightly conditioned on the specific environment, not the broad conceptual label.

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

Finally, the source repository was dirty at run time. The exact working-tree state matters for reproduction. We cannot isolate whether any perfect-pass environment benefited from leaked state or any zero-pass environment was derailed by broken state; we can only note the confound.

## Keep the map; keep the denominator

The established result is specific and useful: on this archived selection, Mercury-2.5 received **277 PASS judgments among 405 scored cases**, with observed all-pass outcomes in 17 environments, all-fail outcomes in seven, mixed outcomes in 12, and no scored outcome in two. Closely named environments sometimes landed far apart. Case counts, tuple counts, missing judgments, judge guarantees, single seeds, and dirty source state all affect how much weight any contrast can bear.

The result is *not* that environment identity “dominates difficulty”: there is no common difficulty scale here on which to make that comparison. Nor does this map identify a model-internal cause for `glyph` or `batchnorm_ema`, or tell us how the endpoints would survive new seeds, a uniform judge, and a cleanly captured source state. An environment-by-judge and environment-by-failure-mode cross-tab, followed by repeated runs, would help distinguish those possibilities.

So I would keep **68.4%** as the answer to a precise counting question: *What fraction of scored, selected cases received PASS?* I would not let it stand alone as the campaign’s outcome. The more revealing answer is the map beside it—especially the zeros, the perfect scores, the 40.7% of scored cases lying in between, and the concrete ways unequal density and archival confounds shape what any single number can mean.
```


&&&&&&&&&&&


gpt 6.1 sol max:

---
title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>The comparisons and interpretation here; no new model runs.</dd>
  <dt>Synthesis</dt><dd>Archived counts covering 416 selected cases across 38 environments, with outcomes, tuple exposure, missing judgments, judge guarantees, and failure labels kept distinct.</dd>
  <dt>Prose</dt><dd>First-person analysis written for this article, separating descriptive results from possible explanations.</dd>
  <dt>Certainty</dt><dd>High for the reported counts and arithmetic; limited for causal explanations, seed stability, and comparisons across judging standards.</dd>
  <dt>Importance</dt><dd>A pooled benchmark rate answers a useful counting question, but cannot describe its constituent environments on its own.</dd>
</dl>

Mercury-2.5 passed **68.4% of the scored cases** in this archived campaign. What would I expect if I opened one of its environments at random? The `ts_*` results make that question awkward: `ts_parse_only` is 4/4, while `ts_one_step` and `ts_trajectory` are each 0/4. All three contribute to the same pooled number, with only four scored cases apiece.

The arithmetic is right, but as a stand-alone description of this selection, 68.4% acts as a statistical blanket over an endpoint-heavy map, uneven case density, and unresolved evaluation questions.

I want to know what that number summarizes, rather than replace it with a different slogan. These are judgments on selected cases, not repeated measurements of general capability. An environment name is not a difficulty rating. The useful next step is to keep the headline while exposing its parts.

## First, keep the denominators straight

The archive contains **416 selected cases in 38 environments**. Of those, 405 received a PASS or FAIL judgment: **277 PASS and 128 FAIL**. The scored-case pass rate is therefore **277/405, or 68.4%** after rounding.

The fraction **277/416, or 66.6%**, answers a different question: what share of *all selected cases* received an observed PASS? It must not silently turn the 11 unscored cases into failures.

Those missing judgments are six cases in `epistemic_silence`, four in `epistemic_type_games`, and one in `rd_adaptive_halting`. The first two environments have no scored cases, leaving **36 environments with scored outcomes**.

| Environment outcome | Environments | PASS / scored cases | Share of scored cases | Unscored cases |
|---|---:|---:|---:|---:|
| Every scored case passed | 17 | 172/172 | 42.5% | 0 |
| No scored case passed | 7 | 0/68 | 16.8% | 0 |
| Some passed, some failed | 12 | 105/165 | 40.7% | 1 |
| No scored cases | 2 | — | — | 10 |
| **Total** | **38** | **277/405** | **100%** | **11** |

!

*Figure 2. Pass fractions across the 36 scored environments. Each fraction describes the observed scored cases, not stability under new cases or seeds; the two unscored-only environments have no scored rate to plot.*

## Endpoint-heavy, not bimodal

Twenty-four of the 36 scored environments—exactly two-thirds—sit at an observed endpoint. Every scored case passed in **17 of 36 environments (47%)**; none passed in seven.

I would call this map **endpoint-heavy, not bimodal**: the description stays with the observed fractions rather than asserting two underlying capability populations.

The 17 perfect-pass environments break down as follows:

- **Nine at 9/9:** `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, and `tokenizer_adjunction`.
- **Four larger blocks:** `css_state_machine` at 18/18, `epistemic_games` at 23/23, and `rd_gradient_credit` and `rd_state_carry` at 15/15 each.
- **Four smaller blocks:** `epistemic_announcements` and `epistemic_nested_knowledge` at 6/6 each, and `epistemic_fragmented_observation` and `ts_parse_only` at 4/4 each.

Together, those environments contribute **172 PASS judgments in 172 scored cases**.

At the other endpoint, `functorial_augmentation`, `monadic_reward`, `sheaf_invariant_gluing`, and `sheaf_physical_constraints` are each 0/9. `ts_one_step` and `ts_trajectory` are each 0/4, while `glyph` is 0/24. These seven environments contribute **0 PASS judgments in 68 scored cases**.

“Perfect-pass” and “zero-pass” are labels for these observed selections, not declarations that an environment is permanently solved or unsolvable. Their case counts differ, and endpoint labels do not eliminate seed uncertainty.

## The middle holds 40.7% of the scored cases

The remaining 12 scored environments have mixed outcomes. Although they are only one-third of the scored environments, they contain **165/405 scored cases, or 40.7%**. Their combined result is **105/165**, with one additional unscored case.

The near-misses are `sheaf_schema_sync`, `sql_fixed_point`, and `transformer_ssm_lift`, each at **8/9, or 88.9%**. `compositional_optimizer` and `equivariant_diagram` are both 7/9. `gnn_message_passing`, `regex_state_machine`, and `ssm_parallel_scan` each have 5/9, while `tensor_functor` has 6/9.

The other mixed results widen the range: `moco` is **36/55, or 65.5%**; `batchnorm_ema` is **2/15, or 13.3%**; and `rd_adaptive_halting` is **8/14 scored, plus one unscored**.

I would not treat this middle as noise between “solved” and “unsolved” groups, because it holds a substantial share of the selected evidence. Nor would I treat matching fractions as evidence of matching mechanisms: three environments at 5/9 need not have failed for the same reason.

## Names are handles, not forecasts

The opening `ts_*` contrast invites a progression story: `ts_parse_only` passed 4/4, while `ts_one_step` and `ts_trajectory` passed 0/4 each. But these are distinct selected sets, not repeated measurements along an established difficulty ladder.

The `sheaf_*` results create a similar temptation. `sheaf_schema_sync` passed 8/9, while `sheaf_invariant_gluing` and `sheaf_physical_constraints` each passed 0/9. A single “sheaf performance” label would obscure those differences within this archive, without explaining which task property produced them.

A third contrast appears among category-theory-flavored names: `categorical_lenses` passed 9/9, `functorial_augmentation` passed 0/9, and `tensor_functor` passed 6/9. Again, that is an outcome comparison, not a controlled test of a shared conceptual ability.

These examples make family labels an **unreliable shortcut within this archive**, not proof that naming conventions never carry information. There is no shared difficulty scale here, so I cannot turn the contrasts into a claim that environment identity “dominates difficulty.”

## Three environments account for 56 failures

`glyph`, `moco`, and `batchnorm_ema` make the distinction between environment counts and case counts concrete:

- `glyph`: 24 scored cases, 24 failures.
- `moco`: 55 scored cases, 19 failures.
- `batchnorm_ema`: 15 scored cases, 13 failures.

Together, they supply **94/405 scored cases but 56/128 failures**—a concentration in this selection, not evidence of a common failure mechanism.

This is one way the pooled result reflects where cases were selected. Counting these as merely three environments would discard their case-level exposure; treating their 56 failures as one explanatory category would discard differences the aggregate counts cannot resolve.

## A case is not necessarily a new tuple

The unit of the pooled rate is a *case*. The archive’s tuple counts show that cases and tuples are not interchangeable.

| Environment | Cases | Tuples |
|---|---:|---:|
| `css_state_machine` | 18 | 9 |
| `epistemic_games` | 23 | 8 |
| `glyph` | 24 | 12 |
| `moco` | 55 | 15 |

`moco`, for example, contributes 55 scored cases across 15 tuples. That gives it more case-level weight than an environment with nine scored cases, but does not establish that its cases provide proportionally more independent evidence.

The 405 scored cases are not 405 distinct tuples, much less 405 demonstrated independent tests of general ability. These aggregates also do not provide enough information to estimate within-tuple dependence.

Unequal case counts are not inherently an error; they mean that the headline is a **case-weighted pooled rate**, rather than an equally weighted average across environments.

## How much does case weighting change the headline?

Large case counts do not automatically imply large leverage on the pooled percentage. Arithmetic exclusions make that distinction visible:

| Scored selection retained | PASS / scored cases | Pooled pass rate |
|---|---:|---:|
| All scored cases | 277/405 | 68.4% |
| Excluding `moco` | 241/350 | 68.86% |
| Excluding `glyph` | 277/381 | 72.70% |
| Excluding both | 241/326 | 73.93% |

Excluding `moco` shifts the rate upward by less than half a percentage point—about **0.47 points**—whereas excluding `glyph` shifts it by **4.31 points**; these are sensitivities of the existing selection, not results from new evaluations.

The difference is arithmetic: `moco`’s own 65.5% rate is close to the pooled rate, while `glyph` contributes a 0/24 block. Volume and pass fraction both matter to the effect of an exclusion.

A second weighting check reaches the same limited conclusion. Reducing `moco`’s weight from 55 cases to nine, while holding its observed 36/55 pass fraction fixed, produces a pooled rate of approximately **68.8%**, about **0.4 percentage points** higher. This is a fractional-weight calculation, not a prediction that an actual nine-case subset would reproduce that fraction.

I would use these checks to understand the headline’s sensitivity, not to choose a more flattering replacement selection.

## Equal environment weights do not recover the map

Across the **36 environments with scored cases**, the unweighted mean of their observed pass fractions is approximately **69.2%**. That is close to the case-weighted 68.4%, but the similarity does not make either number representative of every environment.

The median environment pass fraction is **8/9, or 88.9%**. That higher summary still leaves seven zero-pass environments in the same map.

The pooled rate weights environments by their scored case counts; the unweighted mean gives each scored environment equal weight. Those answer different aggregation questions, but neither preserves the endpoint-heavy shape.

This is why I do not think the problem is solved by finding the “right” single number. For this archive, the zeros, perfect scores, mixed outcomes, and case counts remain relevant even when two averages happen to be close.

## Failure labels are not environment-level explanations

The 128 FAIL judgments carry these recorded labels:

| Failure label | Count |
|---|---:|
| `underfit` | 51 |
| `overfit_visible_tests` | 49 |
| `RUNTIME_ERROR` | 9 |
| `source_invalid` | 9 |
| `invalid_action` | 5 |
| `training_failed` | 3 |
| `runtime_error` | 2 |
| **Total** | **128** |

The first two labels account for **100/128 failures**, but their names alone do not establish a model-internal mechanism. They are recorded classifications, not direct observations of Mercury-2.5’s reasoning.

The casing difference between `RUNTIME_ERROR` and `runtime_error` is a **data-quality flag**, not evidence of separate evaluation pipelines or a particular parser problem. I would preserve both categories until their definitions and provenance were checked.

Likewise, nine `RUNTIME_ERROR` labels and nine `source_invalid` labels cannot be assigned to particular nine-case environments from these totals. The matching counts invite inspection, but do not supply an environment-by-failure-mode mapping.

Before attributing any zero-pass block to a source, runtime, or harness problem, I would need that cross-tab and the relevant case records. The aggregate table identifies questions to investigate, not their answers.

## What the judges and archive derp! claim

The campaign records **189 `behavioral_reference` and 227 `compile_only` judge guarantees**, totaling all 416 selected cases—not just the 405 scored cases.

Those are different recorded guarantees, so I cannot assume that every PASS establishes the same kind of validation without knowing how they were applied. The aggregates here provide neither an environment-by-guarantee breakdown nor a controlled comparison of the same outputs under both guarantees. Calling every perfect-pass environment “behaviorally solved” would therefore outrun this evidence.

Each selected cell also has **a single seed**. These outcomes do not provide a repeated-seed variability estimate for a selected cell, and the observed endpoints are not exempt from that limitation. A 4/4, 9/9, or 0/24 label describes this run’s selected cases, not its stability across reruns.

Finally, the source repository was **dirty at run time**, making the exact working-tree state important for reproduction without establishing that any particular judgment was wrong.

These limitations narrow the interpretation of the map; none, by itself, licenses recoding a PASS, FAIL, or unscored case.

## Keep the map; keep the denominator

The established result is specific: Mercury-2.5 received **277 PASS judgments among 405 scored cases**, with observed all-pass outcomes in 17 environments, all-fail outcomes in seven, mixed outcomes in 12, and no scored outcome in two.

The contrasts are substantial within this selection, but they do not identify a common difficulty scale or a model-internal cause for `glyph`, `batchnorm_ema`, or any other environment. Nor do they tell us how the endpoints would change under new seeds, common judging standards, or a precisely reproduced source state.

An environment-by-judge cross-tab, an environment-by-failure-mode cross-tab, repeated-seed runs, and a captured working tree would help assess those questions; they would be additional evidence, not retroactive explanations.

So I would keep **68.4%** as the answer to a precise counting question: *What fraction of scored, selected cases received PASS?* I would not let it stand alone as the campaign’s outcome. The more revealing answer is the map beside it—especially the zeros, the perfect scores, and the **40.7% of scored cases** lying in between.
