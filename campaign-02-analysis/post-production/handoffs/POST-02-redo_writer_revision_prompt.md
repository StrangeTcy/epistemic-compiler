# POST-02 redo — Stage B2 Writer prompt (self-contained)

## Your task

Improve the original article quoted below. It is the Mercury-2.5 cross-environment post as first published on 2026-10-16. Use the revisions and corrections in section 4 to fix every passage that conflicts with them. Keep what is correct, and extend the article only where the verified facts support it. Do not add claims that are not in section 4 or in the article itself. Output only the revised article, as one Markdown document, with front matter. Do not include notes, commentary, or a list of changes.

## Non-negotiable rules

1. Analysis of archived results only. Do not suggest that any run was repeated or that new model runs were performed.
2. Mercury-2.5 is not Atria. Do not use numbers, labels, or conclusions from any other campaign.
3. Do not present this as preregistered. It is a retrospective analysis.
4. Public copy must not contain file paths, finding IDs (such as F-006), trace IDs, draft labels, or the words "packet", "evidence packet", "source analysis", "overview document", or "working notes".
5. Keep bracketed tokens exactly as written: [ac-word], [d-word], [m-word]. They are intentional replacements, not placeholders.
6. Every number must come from the facts below. State a limitation beside each claim it limits.
7. Do not describe any tuple-level pattern as a difficulty effect, a monotonic ladder, or a ranking. The evidence does not support those.

## Original article (verbatim)

The article below is quoted exactly as first published. Revise it; do not treat it as a summary of what to write.

````markdown
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

The `sheaf_*` names create the opposite trap. `sheaf_schema_sync` passed 8/9, while `sheaf_invariant_gluing` and `sheaf_physical_constraints` each passed 0/9. Grouping all three under a single “sheaf performance” discards the comparison that matters. Category-theory-flavored names are no more predictive: `categorical_lenses` passed 9/9, `functorial_augmentation` passed 0/9, and `tensor_functor` passed 6/9. These examples show that a shared name does not imply shared outcomes, or even shared evaluation infrastructure, inside this packet. The outcome map varies sharply between environments that share a broad conceptual label.

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

Finally, the source repository was dirty at run time. The exact working-tree state matters for reproduction. We cannot isolate any effect of the dirty working tree on individual environments; we can only note the confound.

## Keep the map; keep the denominator

The established result is specific and useful: on this archived selection, Mercury-2.5 received **277 PASS judgments among 405 scored cases**, with observed all-pass outcomes in 17 environments, all-fail outcomes in seven, mixed outcomes in 12, and no scored outcome in two. Closely named environments sometimes landed far apart. Case counts, tuple counts, missing judgments, judge guarantees, single seeds, and dirty source state all affect how much weight any contrast can bear.

The result is *not* that environment identity “dominates difficulty”: there is no common difficulty scale here on which to make that comparison. Nor does this map identify a model-internal cause for `glyph` or `batchnorm_ema`, or tell us how the endpoints would survive new seeds, a uniform judge, and a cleanly captured source state. An environment-by-judge and environment-by-failure-mode cross-tab, followed by repeated runs, would help distinguish those possibilities.

So I would keep **68.4%** as the answer to a precise counting question: *What fraction of scored, selected cases received PASS?* I would not let it stand alone as the campaign’s outcome. The more revealing answer is the map beside it—especially the zeros, the perfect scores, the 40.7% of scored cases lying in between, and the concrete ways unequal density and archival confounds shape what any single number can mean.
````

## Revisions and corrections (verified facts)

**Campaign and selection**
- 416 selected cases in 38 environments. 405 scored: 277 PASS, 128 FAIL. 11 unscored (judge-coverage gap, not a third outcome).
- Scored pass rate: 277/405 = 68.4%. All-selected fraction 277/416 = 66.6% answers a different question and must be labelled as such.
- All 416 selected cases carry seed 0. No case was re-run under a second seed.
- Judge guarantees: 189 behavioral_reference, 227 compile_only (these totals include unscored cases).
- Omitted before scoring (outside the 416): 80 cases, namely 56 intervention-twin omissions, 14 known-gate calibration failures, 10 unsupported-input-modality cases (all in the `rope` environment). The provenance summary gives 24 known-gate omissions. This disagrees with the exclusion record's 14. State the disagreement; do not resolve it.
- 10 scored FAIL cases carry case_disposition `rejected`: 8 of the 9 scored `monadic_reward` cases, 1 `batchnorm_ema`, 1 `transformer_ssm_lift`. The archive does not define "rejected". Keep all 10 in the counts and say so beside the `monadic_reward` claim.
- One PASS, `ts_parse_only__witness_status=broken_representation=flat__seed-0`, is marked performance-ineligible. Its exclusion note describes a provider-attributed terminal failure while its verdict is PASS. Keep it in the 277 count and flag the inconsistency.

**Environment outcomes (environment-level, from the 38-row summary)**
- 17 environments: every scored case passed (172/172 total). Nine at 9/9: architecture_naturality, categorical_lenses, ci_dependency_graph, neuro_symbolic_parser, semiring_unification, spreadsheet_dataflow, stochastic_monad, template_interpreter, tokenizer_adjunction. Then css_state_machine 18/18; rd_gradient_credit 15/15; rd_state_carry 15/15; epistemic_games 23/23; epistemic_announcements 6/6; epistemic_nested_knowledge 6/6; epistemic_fragmented_observation 4/4; ts_parse_only 4/4.
- 7 environments: no scored case passed (0/68 total): functorial_augmentation 0/9, monadic_reward 0/9, sheaf_invariant_gluing 0/9, sheaf_physical_constraints 0/9, ts_one_step 0/4, ts_trajectory 0/4, glyph 0/24.
- 12 mixed environments (105/165 scored; one unscored case in rd_adaptive_halting): sheaf_schema_sync 8/9, sql_fixed_point 8/9, transformer_ssm_lift 8/9, compositional_optimizer 7/9, equivariant_diagram 7/9, tensor_functor 6/9, gnn_message_passing 5/9, regex_state_machine 5/9, ssm_parallel_scan 5/9, moco 36/55, rd_adaptive_halting 8/14 (plus 1 unscored), batchnorm_ema 2/15.
- 2 environments with no scored case: epistemic_silence (6 unscored), epistemic_type_games (4 unscored).
- 24 of the 36 environments with scored cases sit at an endpoint (all pass or all fail). Mixed environments hold 165 of the 405 scored cases (40.7%).

**The 340-row environment × difficulty-tuple matrix**
- 340 rows; 4 to 15 rows per environment; 6 environments have more than 10 rows.
- 34 difficulty dimension names. Tuples are environment-specific and must not be pooled, ranked, or regressed across environments.
- 296 rows are single-case. 44 rows are multi-case, all in four environments: moco (15 rows, 55 cases), glyph (12 rows, 24 cases), css_state_machine (9 rows, 18 cases), epistemic_games (8 rows, 23 cases).
- 329 rows carry a pass rate. Of these, 320 (97.3%) are exactly 0 or 1. Nine rows are fractional, all in moco.
- moco: 6 of its 15 rows sit at 0.0 or 1.0. The other 9 are fractional. Fractional values: 1/6, 1/3, 2/5, 2/3, 3/4, 5/6. No row-by-row key links each value to a tuple.
- 214 of 340 rows (63%) sit in environments where every row has the same outcome.
- 98 individual tuples have zero passes, in 19 environments.
- The "one seed per cell" wording is ambiguous. The row counts show a cell must mean an environment × tuple row, not a single case. This is an inference from the arithmetic, not a stated convention.

**Unscored cases (11)**
- epistemic_silence: 6. epistemic_type_games: 4. rd_adaptive_halting: 1, at the tuple where all five dimensions are `easy` (this tuple is identified in the matrix).

**Failure labels (global counts only; no environment breakdown is available)**
- underfit 51, overfit_visible_tests 49, runtime_error 11 (9 recorded as RUNTIME_ERROR plus 2 as runtime_error, consolidated), source_invalid 9, invalid_action 5, training_failed 3. Total 128.

**Ten-versus-seven discrepancy**
- A project overview document states 10 zero-pass environments. The environment-level count gives 7. A tuple-level explanation (environments with at least one zero-pass tuple) gives 19, so it does not reproduce 10. The origin of 10 is unexplained. Use 7 and state that the reconciliation is open.

**Claims withdrawn or open**
- Withdrawn: non-monotonic difficulty in css_state_machine. It is 18/18, so every tuple row is 2/2.
- Open, not findings: non-monotonic patterns in moco and in a SQL environment. Under a single-seed, mostly binary design such patterns may arise by chance. The base rate has not been computed.

**Source state**
- The campaign's source repository was recorded as dirty. The exact working-tree state [m-word] for reproduction, so the effect of uncommitted changes on any environment cannot be isolated.

## Structure (approximately 2,000–2,500 words; keep the original structure where it is correct)

1. Front matter: title, date 2026-10-16, layout post. Byline "by StrangeTcy".
2. Short epistemic-status block: original ideas, synthesis, prose, certainty, importance. Keep each entry to one sentence.
3. Short revision note: this replaces the earlier version, the headline stays, the tuple matrix is added as an exploratory second layer, and withdrawn claims are stated openly.
4. Opening: the 68.4% figure and why one pooled rate can hide the environment-level picture.
5. Counting scored cases: the outcome table (17 / 12 / 7 / 2) and the 277/405 vs 277/416 distinction.
6. The endpoint-heavy distribution, with the environment lists above.
7. Names as handles, not forecasts: the ts_* and sheaf_* examples, and glyph/moco/batchnorm_ema.
8. The 340-row matrix: what it adds, the binary and singleton facts, the 34 non-comparable dimensions, the 214 homogeneous rows, and the 98 zero-pass tuples in 19 environments.
9. The meaning of a cell (inference, stated as such).
10. moco as the only environment with fractional outcomes, with the limit that its shape cannot be drawn.
11. Claims withdrawn or left open (CSS withdrawn; MoCo and SQL open).
12. Unscored cases: the coverage gap, the rd_adaptive_halting tuple, and why they are not failures.
13. The 10-versus-7 discrepancy.
14. Failure labels and judge guarantees, global counts only, with the interpretive limits.
15. The selection frame: 80 omitted cases and the 14-vs-24 disagreement; the 10 rejected cases; the one performance-ineligible PASS.
16. Confounds: single seed, dirty source, selection.
17. What this supports, and what it does not show.
18. Figure: `../figures/fig2_environment_outcome_lollipop.svg` with alt text "Lollipop chart of pass rates by environment".

## Style

- First person, plain, exploratory, conservative. Short paragraphs, direct sentences.
- Tables where the data are tabular. Lists only where the content is a list.
- Do not use the words "bimodal" or "significant" unless you define them and show they apply.
- Do not claim that a pass means a model "understood" or "solved" anything. Describe what the judge checked.

## Output

One Markdown document. Front matter, then the article. Nothing before or after it.
