REDactor — POST-02: Cross-environment outcome map (Mercury-2.5)

You are the Redactor. Your job is to produce the FINAL, publication-ready article markdown for POST-02, applying every correction and decision from the accepted pipeline stages (Evidence Reviewer, Writer Candidates, Editorial Critic, Claim Killer). This is the last stage before human review.

INPUTS
1. Evidence packet (verified ground truth) — see below.
2. Editorial blueprint (accepted Stage C) — see below.
3. Claim-killer verdicts (accepted Stage D) — see below.
4. Two candidate drafts (A=gemini, B=gpt sol max) — see below.
5. House style reference — see below.

EVIDENCE PACKET (verified ground truth)
- 38 environments total; 416 selected cases; 405 scored; 11 unscored.
- 277 PASS / 128 FAIL (sum 405).
- 17 perfect-pass (rate 1.0): architecture_naturality 9/9, categorical_lenses 9/9, ci_dependency_graph 9/9, css_state_machine 18/18, epistemic_announcements 6/6, epistemic_fragmented_observation 4/4, epistemic_games 23/23, epistemic_nested_knowledge 6/6, neuro_symbolic_parser 9/9, rd_gradient_credit 15/15, rd_state_carry 15/15, semiring_unification 9/9, spreadsheet_dataflow 9/9, stochastic_monad 9/9, template_interpreter 9/9, tokenizer_adjunction 9/9, ts_parse_only 4/4.
- 7 zero-pass (rate 0.0): functorial_augmentation 0/9, glyph 0/24, monadic_reward 0/9, sheaf_invariant_gluing 0/9, sheaf_physical_constraints 0/9, ts_one_step 0/4, ts_trajectory 0/4.
- 12 partial: batchnorm_ema 2/15 (0.133), compositional_optimizer 7/9 (0.778), equivariant_diagram 7/9 (0.778), gnn_message_passing 5/9 (0.556), moco 36/55 (0.655), rd_adaptive_halting 8/14 (0.571, +1 unscored), regex_state_machine 5/9 (0.556), sheaf_schema_sync 8/9 (0.889), sql_fixed_point 8/9 (0.889), ssm_parallel_scan 5/9 (0.556), tensor_functor 6/9 (0.667), transformer_ssm_lift 8/9 (0.889).
- 2 unscored-only: epistemic_silence (6 cases), epistemic_type_games (4 cases).
- Scored pass rate: 277/405 = 0.684. All-selected: 277/416 = 0.666.
- Judge guarantees: 189 behavioral_reference + 227 compile_only = 416.
- Failure modes: underfit 51, overfit_visible_tests 49, RUNTIME_ERROR 9, source_invalid 9, invalid_action 5, training_failed 3, runtime_error 2 (sum 128).
- Cases vs tuples: css_state_machine 18/9, epistemic_games 23/8, glyph 24/12, moco 55/15.
- Single seed per selected cell. Source repo dirty at run time.
- 11 unscored: 6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting.
- 36 environments have scored cases (38 - 2 unscored-only). 24 of 36 are at endpoints (17 + 7). 12 partial.
- Partial environments hold 165/405 scored cases = 40.7%.
- Zero-pass environments hold 68 scored cases. 0/68.
- Perfect-pass environments hold 172 scored cases. 172/172.
- Mixed environments: 105/165 + 1 unscored.
- Combined exposure: glyph (24) + moco (55) + batchnorm_ema (15) = 94 cases; failures 24+19+13 = 56.
- Unweighted mean of 36 env pass fractions ≈ 69.2%. Median = 8/9 = 88.9%.
- Counterfactuals (derived, arithmetically exact): excluding moco → 241/350 = 68.86% (Δ +0.47 pt); excluding glyph → 277/381 = 72.70% (Δ +4.31 pt); excluding both → 241/326 = 73.93%; moco shrunk to 9 cases at its own 65.5% rate → ≈68.8% (Δ ≈ +0.4 pt).

EDITORIAL BLUEPRINT (accepted Stage C) — key decisions
- Thesis: The 68.4% top-line pass rate is arithmetically accurate but descriptively hollow; it acts as a "statistical blanket" obscuring an endpoint-heavy (not bimodal) landscape, uneven case density, and infrastructural questions demanding environment-level analysis.
- Opening: Draft B's ts_* cold-open + one sentence of Draft A's "blanket" metaphor. State 68.4% and thesis.
- Structure: 11 sections (see editorial critic response).
- Retain from Draft A: "statistical blanket" metaphor, endpoint enumeration, near-miss examples, unscored breakdown, lollipop figure reference (corrected caption).
- Retain from Draft B: cold-open ts_* hook, summary tables, "endpoint-heavy not bimodal" sentence, unweighted mean/median, 3-example family contrast, 94/405 stat, refusal to infer environment-level failure-mode mapping, closing frame.
- Reject: Draft A's causal speculation, "cognitive failure modes", "brittle contextual engine" closing, [ac-word]/[m-word] placeholders, emoji, 38-row table (collapse to figure + short table), Draft B's 36-row table in argumentative path (move to appendix or collapse).
- Figure: fig2_lollipop.svg after denominator table. Correct caption to "36 scored environments."
- Inline caveats (not batched).
- Keep 68.4% as precise counting answer.
- Endpoint-heavy, not bimodal.
- Keep Draft B's epistemic-status dl (calibrated) with Draft A's fuller field coverage.

CLAIM-KILLER VERDICTS (accepted Stage D) — mandatory corrections
1. Remove [ac-word] (3 instances in Draft A).
2. Remove [m-word] (2 instances in Draft B).
3. Remove stray emoji (🤬).
4. Fix "half the scored environments" → "17 of 36 (47%)".
5. Remove "0.684 is the arithmetic mean" → "case-weighted pooled rate" (contrast with 69.2% unweighted mean).
6. Remove "moco heavily dictates" → quantified: excluding moco → 68.86% (Δ +0.47 pt).
7. Remove "If moco had been 9 cases, demonstrably different" → ≈68.8% (Δ ≈ +0.4 pt).
8. Quantify "glyph massive anchor" → excluding glyph → 72.70% (Δ +4.31 pt).
9. Remove "authors' unrolling choices" intent attribution → "where cases were selected."
10. Remove "single seed less concerning at endpoints" → "endpoint labels do not eliminate seed uncertainty."
11. Remove "dirty repo caused leaked/broken state" → "exact working-tree state matters for reproduction."
12. Remove "family labels useless" → "unreliable shortcut within this archive."
13. Remove "ts_* (TypeScript/Tree-Search)" gloss.
14. Remove "When I analyzed the error logs."
15. Remove "proves completely false."
16. Remove "cognitive demands."
17. Remove "environment-conditioned" causal → descriptive.
18. Remove "profoundly" / "beyond a doubt."
19. Remove "proves domain names useless."
20. Remove "brittle, contextual engine" closing.
21. Remove "infrastructural ghosts" framing (including epistemic-status).
22. Remove "standard cognitive failure modes."
23. Remove causal speculation: RUNTIME_ERROR(9)+source_invalid(9) map to 0/9 environments.
24. Remove "disjoint evaluation pipelines" / "parser discrepancy" → "data-quality flag."
25. Remove "I suspect test failed to run for at least a portion."
26. Remove "measuring a broken harness."
27. Remove "infrastructural ghosts" from epistemic-status.
28. Remove polyfill.io script tag.
29. Remove MathJax scripts (one trivial fraction doesn't warrant two script includes; write formula inline).
30. Fix figure caption: "36 scored environments" not "38."
31. Fix incomplete image markup in Draft B (bare `!`).
32. Fix epistemic-status "harness artifacts" → neutral.
33. Add counterfactuals (excluding moco/glyph) — arithmetically exact, safe to use.

HOUSE STYLE
- Jekyll frontmatter: title, date, layout: post. No extra fields.
- Byline: *by <span class="icon-self">StrangeTcy</span>*
- Epistemic-status <dl> with five fields: Original ideas, Synthesis, Prose, Certainty, Importance.
- First-person, curious, technically literate, self-correcting.
- Concrete cases, exact counts, caveats beside claims.
- No internal file paths, finding IDs, trace IDs, draft labels in public copy.
- No generic "environment matters more than difficulty" without supporting comparisons.
- Target ~1800-2800 words. Do not inflate.
- No paid API calls; no external publishing.

CANDIDATE DRAFTS (verbatim, for reference)
gemini 3.1 pro grounding:

---
title: "POST-02: Cross-environment outcome map (Mercury-2.5)"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>Analyzing the specific structural variance and outcome distribution in the Mercury-2.5 archival campaign.</dd>
  <dt>Synthesis</dt><dd>Aggregating 416 selected cases across 38 distinct environments to deconstruct the pooled top-line pass rate, revealing underlying harness artifacts and data imbalances.</dd>
  <dt>Prose</dt><dd>Exploratory but rigorously grounded in exact case counts; first-person analytical; cautious regarding causal assumptions.</dd>
  <dt>Certainty</dt><dd>High on the descriptive statistics and failure mode counts; necessarily cautious on causal attribution due to documented archival confounds.</dd>
  <dt>Importance</dt><dd>Crucial for understanding how top-line evaluation metrics can obscure structural evaluation failures, uneven data density, and highly localized model outcomes.</dd>
</dl>

<!-- MathJax Include -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

When I first look at a new model run, I find myself fighting an ingrained habit: the urge to look at the single, aggregated top-line number and nod. In the archived campaign for Mercury-2.5, that number is a scored pass rate of 0.684. Out of 405 scored cases, the model passed 277 and failed 128. 

It is a comfortable, respectable number. It suggests a model that is generally capable, perhaps a bit rough around the edges, solving roughly two-thirds of what is thrown at it. But a single pooled pass rate is often a mirage. It acts as a statistical blanket, smoothing out a jagged landscape of absolute triumphs, catastrophic failures, and deeply unequal testing conditions. 

To understand what Mercury-2.5 [ac-word] did during this campaign, we have to pull back the blanket. We have 416 selected cases spanning 38 distinct environments (with 11 cases remaining unscored). When we map the outcomes across these environments, the illusion of a smooth 68.4% capability level shatters. Instead, we find an outcome map that is heavily environment-conditioned, dominated by endpoint extremes, and plagued by infrastructural ghosts.

### The Endpoint-Heavy Distribution

If Mercury-2.5 had a uniform capability level of 0.684, we would expect most environments to cluster around that mean, perhaps following a standard normal distribution. We see nothing of the sort. The outcomes are intensely endpoint-heavy. 

Out of the 36 scored environments, exactly two-thirds reside at the absolute extremes of the scoring spectrum:
- **17 perfect-pass environments (rate 1.0):** The model achieved flawless performance in almost half the scored environments. It went 9/9 in `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, and `tokenizer_adjunction`. It scored 18/18 in `css_state_machine`, 15/15 in both `rd_gradient_credit` and `rd_state_carry`, and swept `epistemic_games` with a massive 23/23. Smaller environments like `epistemic_announcements` (6/6), `epistemic_nested_knowledge` (6/6), `epistemic_fragmented_observation` (4/4), and `ts_parse_only` (4/4) were similarly cleared with zero errors.
- **7 zero-pass environments (rate 0.0):** On the opposite end, the model entirely flatlined in seven environments. It scored 0/9 in `functorial_augmentation`, `monadic_reward`, `sheaf_invariant_gluing`, and `sheaf_physical_constraints`. It went 0/4 in both `ts_one_step` and `ts_trajectory`. Most dramatically, it suffered a 0/24 complete failure in `glyph`.

This leaves just 12 partial-pass environments sitting in the vast middle ground. However, one must not mistake this for a trivial minority of the data. While they represent only a third of the *environments*, these 12 partial environments hold an immense share of the actual evaluation weight: exactly 165 out of the 405 scored cases, or 40.7% of the scored dataset. 

In this chunky middle, outcomes are highly variable. We see near-misses like `sheaf_schema_sync`, `sql_fixed_point`, and `transformer_ssm_lift` (all 8/9, or 0.889), and compositional tasks like `compositional_optimizer` and `equivariant_diagram` (both 7/9, 0.778). The model achieved a 0.655 pass rate (36/55) in the massive `moco` environment, while struggling heavily in `batchnorm_ema` with a meager 2/15 (0.133). 

This is the first great deception of the 0.684 pooled average: it represents the arithmetic mean of a landscape where the model is far more likely to either perfectly solve or completely fail a given environment than to achieve exactly a 68% pass rate within it.

![Lollipop chart of pass rates by environment](../figures/fig2_lollipop.svg)
*Figure 2: Lollipop chart illustrating the endpoint-heavy distribution of pass rates across the 38 environments. Notice the dense clustering of environments at exactly 1.0 and 0.0.*

### Deceptive Family Ties

When reviewing categorized benchmarks, it is tempting to look at prefix labels—such as `ts_*` or `sheaf_*`—and treat them as coherent "families" of difficulty. One might hypothesize that an LLM would possess a generalized proficiency (or deficiency) for a given conceptual domain. The evidence in this archival campaign proves that assumption completely false. Family labels do not predict outcomes. 

Let us look at the `ts_*` (TypeScript/Tree-Search) family. If Mercury-2.5 were generally capable or incapable of `ts_*` logic, we would expect consistent scoring. Instead, the model perfectly cleared `ts_parse_only` (4/4). Yet, when faced with `ts_one_step` and `ts_trajectory`, the model crashed, scoring 0/4 in both. 

The Category Theory and sheaf-theoretic (`sheaf_*`) environments provide an even starker example of this internal variance. The model performed exceptionally well on `sheaf_schema_sync`, passing 8 out of 9 cases (0.889). Based on that, one might assume Mercury-2.5 has a robust grasp of sheaf mechanics in this evaluation harness. But looking further down the table, `sheaf_invariant_gluing` and `sheaf_physical_constraints` are both zero-pass environments (0/9). 

What does this tell us? It tells us that we cannot rely on shared nomenclature to infer a shared difficulty scale. A shared prefix does not imply shared cognitive demands or even a shared evaluation infrastructure. The outcome map is tightly conditioned on the specific environment, not the broad conceptual label slapped on the directory folder. 

### Failure Modes and Infrastructure Ghosts

To truly understand the 128 recorded failures, we must look at the specific failure modes. When I analyzed the error logs, I found a sharp divide between genuine model shortcomings and what appear to be catastrophic infrastructural ghosts.

The majority of failures fall into classic generalization gaps:
- **underfit:** 51 cases
- **overfit_visible_tests:** 49 cases

Together, these 100 cases represent the expected friction of an LLM grappling with partial environments. The model either failed to capture the core logic of the task (`underfit`) or successfully solved the visible prompt but failed the holdout evaluation (`overfit_visible_tests`). These are standard cognitive failure modes, responsible for the bulk of the attrition in environments like `moco` (where the model dropped 19 cases). 

But the remaining 28 failures are deeply suspicious. Consider these specific modes:
- **RUNTIME_ERROR:** 9 cases
- **source_invalid:** 9 cases
- **invalid_action:** 5 cases
- **training_failed:** 3 cases
- **runtime_error:** 2 cases

Notice the counts for `RUNTIME_ERROR` (9) and `source_invalid` (9). In an evaluation dataset built heavily on standard 9-case environments (such as `functorial_augmentation`, `monadic_reward`, `sheaf_invariant_gluing`), these identical counts of 9 act as a glaring data-quality flag. It is highly probable that these failure modes perfectly map to the zero-pass (0/9) environments. If an entire 9-case environment throws a `RUNTIME_ERROR` or a `source_invalid` flag, we are no longer measuring the model's reasoning capabilities; we are measuring a broken harness. 

Furthermore, the casing discrepancy between `RUNTIME_ERROR` (9) and `runtime_error` (2) is a classic tell of disjoint evaluation pipelines. This is not a model failing in two distinct ways; this is a parser discrepancy in the logging infrastructure. When an environment completely flatlines, we must ask whether the model failed the test, or the test failed to run. Given these exact 9-case artifacts, I suspect the latter is responsible for at least a portion of the 7 zero-pass environments.

### The Gravitational Pull of Unequal Density

If infrastructural artifacts skew the failures, unequal data density skews the successes. 

The pooled pass rate calculation is elegantly simple: 
$$ \text{Pass Rate} = \frac{\text{Passed Cases}}{\text{Scored Cases}} $$

However, the denominator—the 405 scored cases—is not evenly distributed across the 36 scored environments. Some environments exert a massive gravitational pull on the global average due to cases vs. tuples mismatches. 

In a perfectly balanced dataset, each environment would contribute an equal number of cases, ensuring that the model's performance in one domain doesn't mathematically overwhelm another. That is not what happened in this archival campaign. Let's look at the case bloat:
- `moco`: 55 cases generated from just 15 tuples.
- `glyph`: 24 cases generated from 12 tuples.
- `epistemic_games`: 23 cases generated from 8 tuples.
- `css_state_machine`: 18 cases generated from 9 tuples.

Because `moco` contains 55 cases, its 36 passes and 19 failures heavily dictate the 68.4% global average. If `moco` had been a standard 9-case environment, the pooled pass rate would be demonstrably different. Conversely, `glyph`'s 0/24 failure acts as a massive anchor dragging the average down. The 0.684 top-line number is therefore heavily weighted by how aggressively the authors decided to unroll tuples into cases for specific environments, rather than a balanced reflection of cross-domain capability.

### Methodological Confounds We Cannot Ignore

Beyond unequal density and broken harnesses, there are several methodological confounds in this archival packet that force us to remain cautious. We can state exactly what this evidence establishes, but we must be equally rigorous about what it cannot.

**1. The Unscored Cases Are Not Failures**
There are 11 unscored cases in this dataset: 6 in `epistemic_silence`, 4 in `epistemic_type_games`, and 1 orphaned case in `rd_adaptive_halting`. Crucially, the two epistemic environments were entirely unscored, reducing our total scored environment count from 38 to 36. It is an analytical sin to recode unscored cases as failures to inflate the denominator. The scored pass rate is rigorously 277/405 (0.684). If we look at the all-selected rate, we get 277/416 (0.666), but the former is the mathematically sound metric for performance on *evaluated* tasks.

**2. Untested Judge Guarantees**
The packet relies on two different judge guarantees: 189 cases evaluated via `behavioral_reference` and 227 via `compile_only`. We do not have cross-over tests. We do not know if `behavioral_reference` is systematically more stringent than `compile_only`. Without controlled, pairwise testing of the same outputs against both judges, we cannot determine how much of the environment-conditioned variance is [ac-word] judge-conditioned variance.

**3. The Single Seed Vulnerability**
Each selected cell in this dataset was run with a single seed. We have absolutely no insight into variance or stability. Is a 5/9 in `regex_state_machine` the true mean of the model's capability? Or did it just get unlucky on a single run, and a different seed would yield a 9/9 or a 1/9? In the endpoint-heavy environments (the 1.0s and 0.0s), a single seed is less concerning, but in the 12 partial environments holding 40.7% of the data, the lack of variance bounds is a glaring blind spot.

**4. The Dirty Source Repo**
Finally, the archival notes indicate that the source repository was "dirty at run time." This is a reproducibility nightmare. It implies that uncommitted changes, leftover state, or artifact files were present during evaluation. We cannot easily isolate whether the model relied on leaked state in the perfect-pass environments, or was derailed by broken state in the zero-pass environments.

### The Limits of the Map

So, what does this cross-environment outcome map [ac-word] tell us about Mercury-2.5? 

It establishes, beyond a doubt, that the model's outcomes are profoundly environment-conditioned. It establishes that the 0.684 global pass rate conceals a landscape polarized by perfect sweeps and total failures, bridged only by a set of massive, heavily weighted partial environments. It proves that domain names and family prefixes are useless for predicting performance. 

But we must resist the urge to draw a single, unified theory of Mercury-2.5's internal intelligence from this map. We cannot claim that "environment identity dominates difficulty" because we simply do not have a shared difficulty scale across these distinct, highly localized harnesses. A 9/9 in `tokenizer_adjunction` and a 0/24 in `glyph` do not mean the model is "smart" at one and "dumb" at the other; it means the specific interaction between the model, the task definition, the unrolled tuples, and the infrastructure succeeded in one directory and collapsed in the other. 

Evaluating an LLM through a massive benchmarking campaign is an exercise in managing noise. As researchers, our job is not just to report the aggregated signal, but to map the noise itself. By pulling apart the 416 cases in this archive, we see Mercury-2.5 not as a uniformly 68.4% capable entity, but as a brittle, contextual engine—one whose successes are absolute, whose failures are structural, and whose aggregate score is largely a product of how the map was drawn.

&&&&&&&&&&&&

gpt 6 sol max:

---
title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>The comparisons and interpretation here; no new model runs.</dd>
  <dt>Synthesis</dt><dd>Archived, reconstructed case counts grouped by environment.</dd>
  <dt>Prose</dt><dd>Written for this article.</dd>
  <dt>Certainty</dt><dd>High for the reported arithmetic; limited for explanations of the outcomes.</dd>
  <dt>Importance</dt><dd>A pooled benchmark number is easy to mistake for a description of its parts.</dd>
</dl>

Mercury-2.5 passed 68.4% of the scored cases in this campaign. What would I expect if I opened one of its environments at random? The `ts_*` results make that question awkward: `ts_parse_only` is 4/4, while `ts_one_step` and `ts_trajectory` are each 0/4. All three contribute to the same pooled number.

I want to know what that number summarizes, rather than replace it with a different slogan. These are outcomes assigned by the campaign’s judges to selected cases. They are not repeated measurements of general capability, and an environment name is not a difficulty rating. Still, the cross-environment variation is too large to leave implicit.

## First, count the cases that received a judgment

The archive contains **416 selected cases in 38 environments**. Of those, 405 received a PASS or FAIL judgment: 277 PASS and 128 FAIL. Thus **277/405, or 68.4%,** is the scored-case pass rate. Another 11 cases were unscored. The fraction **277/416, or 66.6%,** answers a different question—the share of *all selected cases with an observed PASS*. It must not be presented as a pass rate that silently turns the 11 unknown outcomes into failures.

| Environment outcome | Environments | PASS / scored cases | Share of scored cases | Unscored cases |
|---|---:|---:|---:|---:|
| Every scored case passed | 17 | 172/172 | 42.5% | 0 |
| No scored case passed | 7 | 0/68 | 16.8% | 0 |
| Some passed, some failed | 12 | 105/165 | 40.7% | 1 |
| No scored cases | 2 | — | — | 10 |
| **Total** | **38** | **277/405** | **100%** | **11** |

Twenty-four of the 36 environments with scored cases sit at an observed endpoint: every case passed or every case failed. I would call the map *endpoint-heavy*, not declare a statistically bimodal capability. Some endpoints are based on four cases, others on 23 or 24; the table alone cannot tell us how stable any endpoint would be under new cases or seeds. Nor are the partial environments negligible exceptions. They contain **165 of the 405 scored cases**, or 40.7%, and range from 2/15 to 8/9.

The two environments with no scored outcome are `epistemic_silence` (six unscored cases) and `epistemic_type_games` (four). The remaining unscored case belongs to `rd_adaptive_halting`, whose scored result is 8/14. There is no scored pass fraction to plot for the first two environments.

!

*Figure 2. The per-environment view exposes endpoints that a pooled fraction averages together. Read each fraction with its case count; an unscored-only environment has no scored rate.*

Here is the complete case-level map. “PASS / scored” excludes unscored cases; the last column keeps them visible.

| Outcome | Environment | PASS / scored | Unscored |
|---|---|---:|---:|
| All pass | `architecture_naturality` | 9/9 | 0 |
| All pass | `categorical_lenses` | 9/9 | 0 |
| All pass | `ci_dependency_graph` | 9/9 | 0 |
| All pass | `css_state_machine` | 18/18 | 0 |
| All pass | `epistemic_announcements` | 6/6 | 0 |
| All pass | `epistemic_fragmented_observation` | 4/4 | 0 |
| All pass | `epistemic_games` | 23/23 | 0 |
| All pass | `epistemic_nested_knowledge` | 6/6 | 0 |
| All pass | `neuro_symbolic_parser` | 9/9 | 0 |
| All pass | `rd_gradient_credit` | 15/15 | 0 |
| All pass | `rd_state_carry` | 15/15 | 0 |
| All pass | `semiring_unification` | 9/9 | 0 |
| All pass | `spreadsheet_dataflow` | 9/9 | 0 |
| All pass | `stochastic_monad` | 9/9 | 0 |
| All pass | `template_interpreter` | 9/9 | 0 |
| All pass | `tokenizer_adjunction` | 9/9 | 0 |
| All pass | `ts_parse_only` | 4/4 | 0 |
| None pass | `functorial_augmentation` | 0/9 | 0 |
| None pass | `glyph` | 0/24 | 0 |
| None pass | `monadic_reward` | 0/9 | 0 |
| None pass | `sheaf_invariant_gluing` | 0/9 | 0 |
| None pass | `sheaf_physical_constraints` | 0/9 | 0 |
| None pass | `ts_one_step` | 0/4 | 0 |
| None pass | `ts_trajectory` | 0/4 | 0 |
| Partial | `batchnorm_ema` | 2/15 | 0 |
| Partial | `compositional_optimizer` | 7/9 | 0 |
| Partial | `equivariant_diagram` | 7/9 | 0 |
| Partial | `gnn_message_passing` | 5/9 | 0 |
| Partial | `moco` | 36/55 | 0 |
| Partial | `rd_adaptive_halting` | 8/14 | 1 |
| Partial | `regex_state_machine` | 5/9 | 0 |
| Partial | `sheaf_schema_sync` | 8/9 | 0 |
| Partial | `sql_fixed_point` | 8/9 | 0 |
| Partial | `ssm_parallel_scan` | 5/9 | 0 |
| Partial | `tensor_functor` | 6/9 | 0 |
| Partial | `transformer_ssm_lift` | 8/9 | 0 |
| Unscored only | `epistemic_silence` | — | 6 |
| Unscored only | `epistemic_type_games` | — | 4 |

## Names are useful handles, not forecasts

My first temptation on seeing the `ts_*` trio is to tell a progression story: parsing worked; taking a step or sustaining a trajectory did not. That is a fair description of these **three sets of four judged cases**. It is not evidence that we have measured a smooth difficulty ladder. We have no shared difficulty scale here, and these are not repeated trials of an otherwise identical test. Even the seemingly reassuring 4/4 is a small observed endpoint.

The `sheaf_*` names create the opposite trap. `sheaf_schema_sync` passed 8/9, while `sheaf_invariant_gluing` and `sheaf_physical_constraints` each passed 0/9. Grouping all three under “sheaf performance” would discard the comparison that [m-word]s. Similarly, a category-theory-flavored name does not settle the outcome: `categorical_lenses` passed 9/9, `functorial_augmentation` passed 0/9, and `tensor_functor` passed 6/9. These examples show that a shared name is an unreliable shortcut *within this archive*. They do not establish which task property caused a pass or a failure.

`glyph`, `moco`, and `batchnorm_ema` put more weight behind that caution. `glyph` has 0/24: a larger all-fail block than the four-case `ts_*` endpoints. `moco` has 36/55, or 65.5%, with 19 failures. `batchnorm_ema` has 2/15, or 13.3%, with 13 failures. Taken together, these three environments supply **94/405 scored cases but 56/128 failures**. That is one concrete way the pooled result is shaped by where cases were selected. It does not tell me that the three share a failure mechanism.

## A case is not necessarily a new tuple

The unit of the pooled rate is a *case*, and case density differs markedly. `moco` alone contributes 55 scored cases—13.6% of the scored campaign. Its archive entries cover 15 tuples. `glyph` has 24 cases over 12 tuples; `css_state_machine` has 18 over nine; `epistemic_games` has 23 over eight. Those paired counts [m-word] because the 405 cases are not 405 distinct tuples, much less 405 demonstrated independent tests of a general ability. These aggregates do not give me enough information to estimate within-tuple dependence.

Would weighting environments equally fix the headline? Not really. Across the **36 environments with scored cases**, the mean of their observed pass fractions is about **69.2%**, close to the case-weighted 68.4%. Their median is **8/9, or 88.9%**. The median hides seven all-fail environments; either mean hides how often the scorecard reaches an endpoint. Changing the single-number summary changes the question, but does not preserve the shape of the map.

That is why I find the 12 partial environments especially informative. Their 165 cases are too numerous to treat as noise between “solved” and “unsolved” groups. Yet a partial result also resists a one-line account: `gnn_message_passing`, `regex_state_machine`, and `ssm_parallel_scan` each have 5/9, while `sheaf_schema_sync`, `sql_fixed_point`, and `transformer_ssm_lift` each have 8/9. Identical fractions do not make those environments interchangeable. And `rd_adaptive_halting` remains **8/14 scored, plus one unscored**—not a 15-case judgment with an assumed failure.

## What can a FAIL explain?

The archive assigns the 128 FAIL outcomes these labels: `underfit` (51), `overfit_visible_tests` (49), `RUNTIME_ERROR` (9), `source_invalid` (9), `invalid_action` (5), `training_failed` (3), and `runtime_error` (2). The first two labels account for 100/128 failures. They are recorded classifications, however, not observations of Mercury-2.5’s internal reasoning. I cannot infer an internal mechanism from their names.

I also would not build a story around the difference between `RUNTIME_ERROR` and `runtime_error`. Their casing is a data-quality flag, not evidence for two kinds of runtime failure. The nine `RUNTIME_ERROR` labels and nine `source_invalid` labels deserve attention because several environments contain nine cases, including all-fail environments. But the counts provided here do **not** match failure modes to environments. A nine-count coincidence is reason to inspect case logs for a possible harness or source problem, not permission to assign one.

There is a second limit on comparing PASS labels. The campaign records **189 `behavioral_reference` and 227 `compile_only` judge guarantees** across the 416 selected cases. Those guarantees are not interchangeable descriptions of what a PASS establishes. Without an environment-by-guarantee breakdown, I cannot test whether the apparent environment contrasts change when judged to the same standard. Calling every perfect-pass environment behaviorally solved would outrun this evidence.

Finally, each selected cell has **one seed**, and the source repository was **dirty at run time**. The first prevents a seed-variability estimate from these outcomes; the second makes the exact working-tree state important for reproduction. Neither fact proves that a particular score is wrong. Both narrow what I can responsibly conclude from it.

## Keep the map; keep the denominator

The established result is specific and useful: on this archived selection, Mercury-2.5 received **277 PASS judgments among 405 scored cases**, with observed all-pass outcomes in 17 environments, all-fail outcomes in seven, mixed outcomes in 12, and no scored outcome in two. Closely named environments sometimes landed far apart. Case counts, tuple counts, missing judgments, and judge guarantees all affect how much weight I would put on those contrasts.

The result is *not* that environment identity “dominates difficulty”: there is no common difficulty scale here on which to make that comparison. Nor does this map identify a model-internal cause for `glyph` or `batchnorm_ema`, or tell us how the endpoints would survive new seeds, a uniform judge, and a cleanly captured source state. An environment-by-judge and environment-by-failure-mode cross-tab, followed by repeated runs, would help distinguish those possibilities.

So I would keep **68.4%** as the answer to a precise counting question: *What fraction of scored, selected cases received PASS?* I would not let it stand alone as the campaign’s outcome. The more revealing answer is the map beside it—especially the zeros, the perfect scores, and the 40.7% of scored cases lying in between.


TASK: Produce the FINAL article markdown. Apply every correction listed above. Use Draft B as the structural base, with Draft A's usable prose (endpoint enumeration, "no shared difficulty scale" concession, confound framing) integrated. Write the complete article — not an outline, not a summary. Every number must be traceable to the evidence packet. Every strong claim must have a caveat in the same sentence. No placeholders, no emoji, no broken markup, no MathJax scripts, no polyfill.

OUTPUT: the full article markdown only. No preamble, no commentary.
