sonnet 5:

---
title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
date: 2026-10-17
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<p class="editorial-note"><em>Revision note: this post replaces the version published 2026-10-16. The original worked entirely from environment-level aggregates. This version keeps that structure as the headline and adds a second, more granular layer — a 340-row environment × difficulty-tuple matrix — as an exploratory cross-check, not a replacement. Several claims from the original packet's internal findings (F-006, F-008) did not survive that cross-check and are corrected or retracted below, in the open, rather than quietly dropped.</em></p>

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>The comparisons, the structural reading of variance, and the reconciliation between the environment-level aggregates and the 340-row difficulty-tuple matrix; no new model runs.</dd>
  <dt>Synthesis</dt><dd>Aggregating the 416 selected cases across 38 environments, then cross-checking that picture against a finer-grained matrix of 340 environment × difficulty-tuple rows, to see which claims the finer grain actually supports and which it only appears to support.</dd>
  <dt>Prose</dt><dd>Written for this article; first-person, exploratory, and deliberately conservative about what a single-seed, 340-row matrix with 296 one-case rows can and cannot say.</dd>
  <dt>Certainty</dt><dd>High on the descriptive statistics, pass/fail counts, and row counts as reported; low on anything resembling a "difficulty effect," a monotonic difficulty ladder, or a cross-environment ranking, because the finer-grained matrix is mostly single-case rows under a single seed, spread across 34 incommensurable difficulty keys.</dd>
  <dt>Importance</dt><dd>A finer-grained table is easy to mistake for a stronger table. Here, moving from 38 environment aggregates to 340 tuple rows is mostly a move toward more rows of less information per row — useful for a few specific questions, dangerous as a general upgrade.</dd>
</dl>

Mercury-2.5 passed 68.4% of the scored cases in this campaign. What would I expect if I opened one of its environments at random? The `ts_*` results make that question awkward: `ts_parse_only` is 4/4, while `ts_one_step` and `ts_trajectory` are each 0/4. All three contribute to the same pooled number. A single pooled pass rate is a statistical blanket, smoothing a jagged landscape of absolute triumphs, total failures, and unequal testing conditions into one comfortable figure.

For this redo I also have a second table: 340 rows, one per environment × difficulty-tuple combination, covering the same 38 environments. It is tempting to treat that as a finer lens on the same question — surely more rows means more insight? Mostly, no. Of the 340 rows, 296 report exactly one case. Pushing from 38 environment aggregates (each built from a handful to two dozen cases) down to 329 scored rows (median one case each) is a move *down* the information ladder for most of the matrix, not up it. A handful of environments are the exception, and I treat them as one.

## First, count the cases that received a judgment

The archive contains **416 selected cases in 38 environments**. Of those, 405 received a PASS or FAIL judgment: 277 PASS and 128 FAIL. Thus **277/405, or 68.4%**, is the scored-case pass rate (the case-weighted pooled rate). The remaining 11 cases were never scored — a judge-coverage gap, addressed in its own section below, not a third outcome bucket. The fraction **277/416, or 66.6%**, answers a different question — the share of *all selected cases with an observed PASS* — and must not be presented as a pass rate that silently turns 11 unknown outcomes into failures.

| Environment outcome | Environments | PASS / scored cases | Share of scored cases | Unscored cases |
|---|---:|---:|---:|---:|
| Every scored case passed | 17 | 172/172 | 42.5% | 0 |
| No scored case passed | 7 | 0/68 | 16.8% | 0 |
| Some passed, some failed | 12 | 105/165 | 40.7% | 1 |
| No scored cases | 2 | — | — | 10 |
| **Total** | **38** | **277/405** | **100%** | **11** |

Twenty-four of the 36 environments with scored cases sit at an observed endpoint: every case passed, or every case failed. This is an *endpoint-heavy* map, not a claim of statistical bimodality — some endpoints rest on 4 cases, others on 23 or 24, and the table alone cannot say how stable any endpoint would be under new cases or seeds. The 12 partial environments are not negligible exceptions; they hold **165 of the 405 scored cases**, or 40.7%, ranging from 2/15 to 8/9.

## The endpoint-heavy distribution

Out of the 36 scored environments, 24 sit at the absolute extremes:

- **17 perfect-pass environments (rate 1.0):** flawless performance across 9/9 in `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, and `tokenizer_adjunction`; 18/18 in `css_state_machine`; 15/15 in both `rd_gradient_credit` and `rd_state_carry`; 23/23 in `epistemic_games`; and 6/6, 6/6, 4/4, 4/4 in `epistemic_announcements`, `epistemic_nested_knowledge`, `epistemic_fragmented_observation`, and `ts_parse_only`. These 17 environments hold 172 of the 405 scored cases (172/172).

- **7 zero-pass environments (rate 0.0):** a complete flatline across seven environments holding 68 scored cases (0/68) — 0/9 in `functorial_augmentation`, `monadic_reward`, `sheaf_invariant_gluing`, and `sheaf_physical_constraints`; 0/4 in `ts_one_step` and `ts_trajectory`; and 0/24 in `glyph`.

- **12 partial-pass environments:** `sheaf_schema_sync`, `sql_fixed_point`, and `transformer_ssm_lift` at 8/9 (0.889); `compositional_optimizer` and `equivariant_diagram` at 7/9 (0.778); `tensor_functor` at 6/9 (0.667); `gnn_message_passing`, `regex_state_machine`, and `ssm_parallel_scan` at 5/9 (0.556); `moco` at 36/55 (0.655); `rd_adaptive_halting` at 8/14 (0.571, plus one unscored case); and `batchnorm_ema` at a low 2/15 (0.133).

- **2 unscored environments:** `epistemic_silence` (6 unscored cases) and `epistemic_type_games` (4 unscored cases) — no scored outcome at all.

The 0.684 pooled average sits atop a landscape where an environment is far more likely to land at an endpoint than to land near 68% inside itself.

## Names are useful handles, not forecasts

Prefix labels like `ts_*` or `sheaf_*` invite a reading of shared difficulty. Within this archive they are an unreliable shortcut. `ts_parse_only` cleared 4/4 while `ts_one_step` and `ts_trajectory` each scored 0/4. `sheaf_schema_sync` passed 8/9 while `sheaf_invariant_gluing` and `sheaf_physical_constraints` each passed 0/9. `categorical_lenses` passed 9/9, `functorial_augmentation` passed 0/9, and `tensor_functor` passed 6/9. A shared name does not imply a shared outcome, or even shared evaluation infrastructure, inside this packet.

`glyph`, `moco`, and `batchnorm_ema` put more weight behind the same caution: `glyph` has 0/24, `moco` has 36/55 with 19 failures, and `batchnorm_ema` has 2/15 with 13 failures. Together these three supply 94 of the 405 scored cases but 56 of the 128 failures — a concrete way the pooled result is shaped by where cases were selected, not evidence that the three share a failure mechanism.

## A second layer: what the 340-row difficulty matrix adds — and what it doesn't

Underneath the 38 environments sits a finer table: **340 rows, one per environment × difficulty-tuple combination, spanning 34 unique difficulty keys.** Every environment contributes between 4 and 15 rows; 6 environments contribute more than 10. This is the layer this redo adds. Three facts about its shape have to be stated before any of its content is used.

**It is mostly singletons.** 296 of the 340 rows report exactly one case; only 44 rows report more than one (up to 6). A "pass_rate" computed from one case is not a rate — it is a single binary outcome wearing a rate's clothing. Across the 329 rows that carry a pass_rate at all, 314 (95.4%) take the value 0 or 1 exactly. I treat those as **outcomes** (✓/✗), not rates, and I do not plot them on a continuous axis.

**Its 34 difficulty keys are not one scale.** They are environment-specific labels, not points on a shared difficulty ladder. There is no basis in this packet for pooling tuples across environments, ranking difficulty keys against each other, or fitting any regression across the matrix. What the matrix supports is 12 separate, within-environment descriptive maps — one per environment worth examining individually — read on their own axes, never compared against each other's axis.

**Most of it repeats what the environment aggregate already says.** 214 of the 340 rows (63%) sit in an environment where every row shares the same outcome as every other row in that environment — carrying zero *within*-environment information beyond the aggregate already reported above. This is expected: the 17 perfect-pass and 7 zero-pass environments (24 of 38) are, by construction, homogeneous at the case level, so their rows are necessarily homogeneous too. The matrix's genuine new information is concentrated in the environments that are *not* already endpoints — and even there, mostly in the four environments where more than one case was run per tuple.

### Resolving what "one seed per cell" means

The evidence packet states a single seed per selected cell, but "cell" is ambiguous between "one case" and "one environment × difficulty-tuple row." The row-level counts resolve this. The 44 rows with more than one case are confined to exactly four environments — `moco` (15 rows, 55 cases), `css_state_machine` (9 rows, 18 cases), `glyph` (12 rows, 24 cases), and `epistemic_games` (8 rows, 23 cases) — and these counts are each environment's *entire* case total (55, 18, 24, and 23 respectively match the environment-level totals already cited above). That means, for these four environments, **every** difficulty-tuple row carries multiple cases; for the other 34 environments, every row carries exactly one. Summing the remaining single-case rows (296) and the cases inside the 44 multi-case rows (120) gives 296 + 120 = 416, exactly the total selected-case count.

The best-supported reading, then, is: **a "cell" is an environment × difficulty-tuple row**, not a single case. "Single seed per cell" describes the row, not every case inside it — a row with `n_cases` > 1 holds multiple distinct selected cases sharing one difficulty tuple, each still run once, with no case re-run under a second seed (consistent with "no replication" in the packet). I flag this as the reading the arithmetic supports, not as something stated explicitly in the source documentation — the packet itself does not define "cell" directly, and a different internal convention cannot be ruled out from the evidence available here.

## Only `moco` shows the shape of a gradient

Of the four multi-case environments, three are already endpoints at the environment level — `css_state_machine` (18/18), `glyph` (0/24), `epistemic_games` (23/23) — and an environment that is uniformly 1.0 or uniformly 0.0 cannot contain an internally varying row: every row inside it necessarily shares that same extreme outcome. That leaves `moco` as the **only** environment in the entire 340-row matrix where multi-case rows can and do land on values other than 0 or 1. This matches the reported pass_rate value set directly — {0.0, 0.167, 0.333, 0.4, 0.667, 0.75, 0.833, 1.0} — where 0.167 ≈ 1/6, 0.333 ≈ 2/6, 0.4 = 2/5, 0.667 ≈ 4/6, 0.75 = 3/4, and 0.833 ≈ 5/6: fractions whose denominators (3 through 6) match the reported range of cases per multi-case row.

`moco`'s 15 rows sum to 55 cases and an overall 36/55 (65.5%), consistent with its environment-level figure above. What I do *not* have from this packet is a row-by-row key: which of moco's 34-key-space difficulty tuples produced 5/6 versus 1/6, for instance. The evidence packet supplies the achievable value set and the row/case totals, not a tuple-indexed listing. I can say moco's within-environment picture has real gradation — it is the one environment in the archive where "difficulty tuple" outcomes are genuinely fractional rather than binary — but I cannot draw its shape, and I am not going to simulate one.

## Two claims from the difficulty layer that don't survive contact with the arithmetic

The source analysis asserted non-monotonic difficulty transitions in three environments — MoCo, CSS, and SQL. Two of these claims need to be flagged plainly rather than repeated.

**The CSS claim is arithmetically impossible, and I retract it.** `css_state_machine` scored 18/18 — every one of its scored cases passed. As shown above, an environment at that extreme cannot contain an internally varying row: each of its 9 difficulty-tuple rows must itself read 1.0 (2/2, in a 9-row/18-case split), because any row below 1.0 would have produced at least one FAIL and broken the environment's perfect record. A sequence where every value is identical is trivially monotone (constant sequences satisfy both non-decreasing and non-increasing definitions); it cannot be *non*-monotonic. The claim as stated cannot be reconciled with `css_state_machine`'s own scored total, and I am dropping it rather than patching it.

**The MoCo and SQL claims need a different caveat, not a retraction.** These environments are not pinned to an extreme, so internal variation across difficulty tuples is possible in principle. But under a single-seed, mostly-binary design, non-monotonicity across a small grid of difficulty tuples is close to the *default* expectation rather than a discovery: only a small minority of simple two-axis grids with binary single-seed outcomes come out monotone in both axes by chance alone. Observing a non-monotonic pattern in `moco` or in a SQL environment's tuples is therefore weak evidence of anything about "difficulty" specifically — it is close to what a random binary grid produces anyway, absent replication to check whether the pattern is stable. I report this as an open, unresolved claim, not as a confirmed effect, and I do not build any "difficulty effect" language on top of it.

## The judge-coverage gap: 11 unscored rows

Eleven rows in the 340-row matrix carry no pass_rate at all, because the judge never scored them. All six rows belonging to `epistemic_silence` are unscored; all four rows belonging to `epistemic_type_games` are unscored; and one single row belonging to `rd_adaptive_halting` is unscored, alongside that environment's other rows which *did* receive scores (summing to its reported 8/14 scored total).

This maps cleanly onto the two environment-level "no scored cases" rows in the headline table: `epistemic_silence` and `epistemic_type_games` are entirely unscored at *every* difficulty tuple, not merely under-sampled, which is why they contribute zero scored cases rather than a low pass fraction. That is a coverage gap in the judging pipeline for those two environments specifically — I have no basis for treating it as a model result, and it should not be silently folded into either a pass or a fail count.

The eleventh unscored row, in `rd_adaptive_halting`, cannot be identified further from this packet. I know it is exactly one row out of that environment's total, and I know it accounts for the "plus one unscored" already noted against its 8/14 scored figure — but the packet does not specify *which* of `rd_adaptive_halting`'s difficulty-tuple keys that row corresponds to. I flag this explicitly as an open item rather than guessing a tuple label: the environment-level fact (one row unscored, scored total unaffected) is solid; the tuple-level identity is not resolvable from the evidence available here.

## A documentation discrepancy: 10 vs. 7 zero-pass environments

The project's `ANALYSIS_OVERVIEW.md` states 10 zero-pass environments. The case-level evidence above supports exactly **7**: `functorial_augmentation`, `monadic_reward`, `sheaf_invariant_gluing`, `sheaf_physical_constraints`, `ts_one_step`, `ts_trajectory`, and `glyph` — each with 0 PASS among its scored cases. I cannot reconstruct 10 from any combination of environment-level facts in this packet: adding the two fully-unscored environments (`epistemic_silence`, `epistemic_type_games`) to the 7 gets to 9, not 10, and those two are a coverage gap, not a zero-pass result, so adding them at all would conflate two different things.

My best working hypothesis is that `ANALYSIS_OVERVIEW.md`'s count was built at the *tuple* level rather than the *environment* level — i.e., it may have counted every environment containing at least one zero-pass row in the 340-row matrix, including some of the 12 partial environments that could plausibly contain an individual zero-pass tuple without the environment's overall case total reaching zero. I cannot confirm this from the data in hand, because the packet does not give me row-level environment attribution beyond the four multi-case environments already discussed. I am flagging the 10-vs-7 gap as **unresolved** rather than silently picking a number: the 7 figure is the one directly supported by the scored-case arithmetic above, and it is the figure I use throughout this piece; the 10 figure in the overview document should be corrected or its methodology published before it is cited again.

## What can a FAIL explain?

The archive assigns the 128 FAIL outcomes to six labels: `underfit` (51), `overfit_visible_tests` (49), `runtime_error` (11), `source_invalid` (9), `invalid_action` (5), and `training_failure` (3). This is a correction from the original post, which had split `runtime_error` into two case-sensitive variants (`RUNTIME_ERROR` and `runtime_error`, 9 and 2) as though they were distinct categories; the underlying packet consolidates these into a single 11-count label, confirming the earlier split was a casing artifact rather than two kinds of runtime failure, exactly as flagged at the time.

`underfit` and `overfit_visible_tests` together account for 100 of the 128 failures. These are recorded classifications, not observations of Mercury-2.5's internal reasoning, and I cannot infer a mechanism from their names. I also cannot break this tally down by environment: the evidence packet supplies only the global counts above, with no environment-level or row-level attribution of which failure mode occurred in which environment. An environment × failure-mode cross-tabulation was on the recommended structure for this piece, and I am not including one, because it is not computable from the data available to me — presenting one would mean inventing the missing linkage. That gap should be closed in the underlying data before the cross-tab is attempted.

## Judge guarantees, and the cross-tab I don't have either

The campaign records **189 `behavioral_reference` and 227 `compile_only` judge guarantees** across the 416 selected cases (189 + 227 = 416, covering scored and unscored cases alike). These guarantees are not interchangeable descriptions of what a PASS establishes, and a behaviorally-referenced PASS is not the same claim as a compile-only PASS.

As with failure modes, I want an environment × guarantee cross-tab — exactly what Stage A review asked for — and the packet does not support one. Only the grand totals are given; there is no environment-level split of behavioral_reference versus compile_only cases provided here. I cannot test whether the 17 perfect-pass environments lean toward one guarantee type, or whether the 7 zero-pass environments were judged to a different standard than the 12 partial ones. Calling every perfect-pass environment "behaviorally solved" would outrun this evidence regardless; the missing cross-tab makes that caution concrete rather than rhetorical.

## Methodological confounds we cannot ignore

Several further confounds bear on both layers of this map.

The 11 unscored cases are a judge-coverage gap, not a third outcome and not a quiet failure: 6 in `epistemic_silence`, 4 in `epistemic_type_games`, 1 in `rd_adaptive_halting`. Recoding them as failures would inflate the denominator illegitimately. The scored pass rate remains rigorously 277/405 (0.684); the all-selected figure 277/416 (0.666) answers a different question.

Each selected cell — read here as an environment × difficulty-tuple row, per the reconciliation above — was run once. We have no variance or stability estimate, at either the environment level or the tuple level. A 5/9 in `regex_state_machine`, or any individual tuple's single-case outcome inside the 340-row matrix, might be near the model's typical performance or an unlucky draw; a different seed could move it substantially. Endpoint labels do not eliminate this uncertainty, and neither does a finer row count — 296 of the 340 rows are single-case outcomes, which carry exactly as much seed uncertainty as the coarser environment figures, just presented with more apparent precision.

Finally, the source repository was dirty at run time. The exact working-tree state [m-word] for reproduction, and we cannot isolate its effect on any individual environment or tuple — only note the confound at both levels of this report.

## Keep the map; add the layer, don't replace it

The established result is specific and useful: on this archived selection, Mercury-2.5 received **277 PASS judgments among 405 scored cases**, with observed all-pass outcomes in 17 environments, all-fail outcomes in 7, mixed outcomes in 12, and no scored outcome in 2. The 340-row difficulty-tuple matrix sitting underneath that map mostly confirms it rather than extending it: 63% of its rows carry zero information beyond their environment's aggregate, 95.4% of its scored rows are binary, and its 34 difficulty keys cannot be pooled, ranked, or regressed against each other. The one place the finer grain earns its keep is `moco`, the single environment where multi-case rows produce genuinely fractional, non-endpoint outcomes — and even there, the packet supports describing the range of outcomes, not drawing their shape.

Two claims that looked like findings in the difficulty layer did not survive contact with the arithmetic: CSS cannot show non-monotonic tuple transitions while sitting at a perfect 18/18, and I have retracted that claim outright rather than patch it. The 10-vs-7 zero-pass-environment discrepancy remains open, flagged rather than silently resolved in either direction, with 7 as the figure directly supported by scored-case counts. The identity of `rd_adaptive_halting`'s single unscored tuple is likewise an open item, not a guess.

So I would keep **68.4%** as the answer to a precise counting question: *what fraction of scored, selected cases received PASS?* I would not let it stand alone, and I would not let a finer-grained table stand in for it either. The more revealing picture is still the environment-level map — the zeros, the perfect scores, the 40.7% of scored cases lying in between — with the tuple matrix read alongside it as a narrow, mostly-confirmatory, occasionally-correcting second layer: useful exactly where it has more than one case per row, and silent everywhere else.

&&&&&&&&&&&&&&&&&

opus 5.5:

I've written the full replacement essay, about 3,500 words. The environment table is still the headline, with the 340-row tuple matrix added as a second, exploratory layer. Two of the four gating items are settled in the text. The other two can't be answered from the evidence packet, so the essay says so openly. Two caveats come first:

- **House style not applied.** No house style files or matrix data were uploaded, so I didn't check against `house_style.md` or `style_reference_material.md`. I copied the original post's format (front matter, byline, epistemic-status block, first person). Please run a style pass.
- **Tables not filled in.** Without the matrix rows I couldn't build the two cross-tabs (environment × failure mode, environment × judge guarantee) or the tuple-by-tuple ✓/✗ maps.

**How the gating items are handled:**
1. **Cell/case/seed meaning: flagged as unknown.** The essay shows why it 👹: every one of moco's 15 tuples has a mixed result. If a "cell" is a single case, that looks like seed sensitivity. If a cell is a whole row, it's just different problems at the same point. The essay picks the cautious reading (the fractions are plain counts, not variance or replication).
2. **10 vs 7 zero-pass environments: settled at 7.** Only the 7 named environments make the totals add up (0/68, then 277/405 overall). None of the 12 partial environments has fewer than two passes, and adding the 2 unscored environments only gets to 9. The overview's "10" is marked unsupported, with its source unknown. F-006's "6" is noted but not explained.
3. **F-008's CSS claim: withdrawn.** `css_state_machine` is 18/18, so its results are flat and can't be non-monotonic. The SQL part comes down to the position of one failure, and the moco part is within normal noise.
4. **The unscored rd_adaptive_halting tuple: flagged as unknown.** Its 8/14 is reported as 8 of 14 judged cases.

**Numbers I worked out from the packet (all checked):**
- 285 single-case rows plus 29 multi-case rows where every case agreed make the 314 rows scored exactly 0 or 1.
- So all 15 non-binary rows are moco's, and every moco row is mixed.
- The 214 rows with no variation inside their environment break down as 148 + 56 + 10.
- The 11 partial environments with one case per tuple total 69 ✓, 41 ✗ and 1 unscored.
- The packet's failure-mode counts close to 128, and the judge-guarantee counts close to 416.

**Things to check:**
- **The reviewer's 2.4% figure.** I couldn't reproduce it. My own count is that 20 of 512 possible 3×3 pass/fail grids (3.9%) are monotone at a 50% pass chance, and about 8% at 68.4%. The essay uses my figures and mentions the difference.
- **Failure-mode labels.** I used the packet's names (`runtime_error` 11, `training_failure` 3). The original post had split runtime errors by capitalization (9 + 2) and called the last label `training_failed`.
- **Figure.** The figure link `../figures/fig2_lollipop.svg` is carried over from the original post. Please confirm the file still exists.
- **Date.** I kept the original 2026-10-16.

Files are in /tmp/outputs:
- POST-02-cross-environment-map.md
