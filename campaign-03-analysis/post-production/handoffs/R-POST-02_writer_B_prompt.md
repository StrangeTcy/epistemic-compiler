BATTLE WRITER B — R-POST-02: "Hard" Does Not Reliably Make Tasks Harder (Reasoning-Atria)

You are Writer B, an independent candidate producing a complete research essay for the StrangeTcy public site. You receive the evidence packet and reviewer brief below. Writer A will receive the same packet separately and you must not see Writer A's draft. Do not reference, react to, or incorporate Writer A's work.

ARTICLE SLOT: R-POST-02 — "Hard" does not reliably make tasks harder (Reasoning-Atria).

Article:

[
---
title: "Does Hard Make Tasks Harder?"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic Status**
- **Original ideas:** 4/10 — An interpretation of outcome patterns in the Atria campaign, not a new theory of difficulty.
- **Synthesis:** 7/10 — Comparing matched difficulty settings while separating recorded verdicts from oracle-supported results.
- **Prose:** 8/10 — First-person, analytical, and bounded by the available evidence.
- **Certainty:** High on the reported counts and listed verdict contrasts; limited on predictive strength, causal interpretation, and generalization.
- **Importance:** 6/10 — A concrete test of whether intended difficulty labels order observed reasoning outcomes.

***

If I change one task setting from `easy` to `hard`, should I expect the model to fail more often?

My first instinct is yes. Otherwise, what is the difficulty setting doing? A benchmark need not produce a failure on every hard instance, but I would expect its labels to provide some direction: increasing difficulty should generally move performance downward, not unpredictably between success and failure.

The `atria_covering_campaign` complicates that expectation. Its recorded comparisons include easy cases that fail while their hard counterparts pass. Other comparisons run in the expected direction: easy passes, hard fails. Elsewhere, the recorded verdict does not change across difficulty settings.

The narrow finding is that **`hard` does not impose a consistent ordering on these recorded outcomes**.

That is not the same as proving that difficulty has no statistical relationship with failure. Nor does a passing hard case prove that increasing difficulty helped the model. Those stronger interpretations require evidence this campaign summary does not provide.

There is another distinction I need to make before examining the cases. Here, `hard` is a configuration label. I am testing whether that label orders observed verdicts—not measuring an intrinsic quantity of difficulty experienced by the model.

## First, which verdicts carry which guarantee?

The campaign record contains 194 cases across 33 environment families, using the `atria` provider with text-only inputs. Each selected cell was executed with a single seed.

Those cases do not all have the same evidential status.

| Judge guarantee | Recorded cases | Scored cases | `PASS` | `FAIL` | Unscored provider-error case |
|---|---:|---:|---:|---:|---:|
| `behavioral_reference` | 72 | 72 | 56 | 16 | 0 |
| `compile_only` | 122 | 121 | 75 | 46 | 1 |

The 72 `behavioral_reference` cases carry the campaign's strict, exact-instance oracle guarantee. These are the validated verdicts under that gate.

The `compile_only` cases were graded without a behavioral reference on the exact instance. Their verdicts are exploratory. A `PASS` in this bucket must not be read as an oracle-validated demonstration of correct behavior; a `FAIL` likewise does not become a validated model verdict merely because it appears in the same campaign.

I therefore keep the buckets separate. There is no combined validated pass rate in this essay.

The progress snapshot updated on October 2, 2026 records the campaign as paused after a provider error. One compile-only case has no scored verdict. That explains the unscored row; I do not count the interruption as a model failure.

A further limitation applies to the comparisons below: the available pair summary does not identify the judge guarantee for each member. I can report the recorded contrasts, but I cannot present all nine pairs as oracle-validated behavioral comparisons. That caveat belongs beside the evidence, not only in a limitations section at the end.

## The same label change, opposite outcomes

The most useful comparisons are within an environment family, with all difficulty coordinates held fixed except the last, which changes from `easy` to `hard`.

This is more controlled than comparing an arbitrary easy case from one family with a hard case from another. It is still a comparison between recorded cases, however. Matching the other difficulty labels does not establish that every other property of the task instances was identical.

Seven of the listed pairs have two difficulty coordinates:

`easy,easy` versus `easy,hard`.

The remaining two use longer strings:

- `rd_adaptive_halting`: `easy,easy,easy,easy,easy` versus `easy,easy,easy,easy,hard`.
- `moco`: `easy,easy,easy,easy,easy,easy` versus `easy,easy,easy,easy,easy,hard`.

In every row of Figure 1, then, the preceding coordinates remain `easy`. Only the final difficulty label changes.

<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 440" width="720" height="440" role="img" aria-labelledby="difficulty-pairs-title difficulty-pairs-desc" style="max-width:100%;height:auto;">
  <title id="difficulty-pairs-title">Opposite verdict changes under the same easy-to-hard label change</title>
  <desc id="difficulty-pairs-desc">Five listed environment pairs change from FAIL on easy to PASS on hard. Four change from PASS on easy to FAIL on hard. Only the final difficulty coordinate changes in each pair.</desc>
  <g fill="currentColor" font-family="sans-serif" font-size="16" font-weight="bold">
    <text x="20" y="35">Environment</text>
    <text x="430" y="35">Final: easy</text>
    <text x="590" y="35">Final: hard</text>
  </g>
  <path d="M20 52H700 M20 250H700" stroke="currentColor" stroke-opacity="0.3"/>
  <g fill="currentColor" font-family="monospace" font-size="14">
    <text x="20" y="90">css_state_machine<tspan x="430">FAIL</tspan><tspan x="590">PASS</tspan></text>
    <text x="20" y="125">compositional_optimizer<tspan x="430">FAIL</tspan><tspan x="590">PASS</tspan></text>
    <text x="20" y="160">functorial_augmentation<tspan x="430">FAIL</tspan><tspan x="590">PASS</tspan></text>
    <text x="20" y="195">sheaf_schema_sync<tspan x="430">FAIL</tspan><tspan x="590">PASS</tspan></text>
    <text x="20" y="230">rd_adaptive_halting<tspan x="430">FAIL</tspan><tspan x="590">PASS</tspan></text>
    <text x="20" y="290">categorical_lenses<tspan x="430">PASS</tspan><tspan x="590">FAIL</tspan></text>
    <text x="20" y="325">moco<tspan x="430">PASS</tspan><tspan x="590">FAIL</tspan></text>
    <text x="20" y="360">monadic_reward<tspan x="430">PASS</tspan><tspan x="590">FAIL</tspan></text>
    <text x="20" y="395">tensor_functor<tspan x="430">PASS</tspan><tspan x="590">FAIL</tspan></text>
  </g>
</svg>
<figcaption><strong>Figure 1. The same difficulty-label change accompanies opposite verdict changes.</strong> All non-final difficulty coordinates remain fixed at easy. These are the nine listed discordant pairs, not a complete count of all matched pairs. The available pair summary does not specify each case's judge guarantee; the plotted outcomes are recorded verdicts, not a claim that every comparison is oracle-validated.</figcaption>
</figure>

Five listed pairs run against the intuitive ordering. In `css_state_machine`, for example, `easy,easy` receives `FAIL`, while `easy,hard` receives `PASS`. The same contrast appears in `compositional_optimizer`, `functorial_augmentation`, and `sheaf_schema_sync`.

The longer configuration in `rd_adaptive_halting` does not remove the reversal: four preceding coordinates remain easy, the final coordinate changes to hard, and the recorded verdict changes from failure to success.

These are concrete counterexamples to a simple rule that moving toward `hard` must worsen the recorded verdict. They are not evidence that the hard cases demanded less computation or that the model benefited from difficulty. I have verdicts, not a measurement of either proposition.

The four pairs in the other direction matter just as much. `categorical_lenses`, `moco`, `monadic_reward`, and `tensor_functor` all show an easy-side `PASS` and a hard-side `FAIL`.

I cannot use the five reversals to announce that difficulty is irrelevant while ignoring these four. The record contains exactly the kind of worsening that difficulty labels are intended to anticipate—just not consistently across the listed environments.

Nor is five against four a meaningful contest over whether difficulty helps more often than it hurts. These are nine listed changing pairs. Without a complete inventory of comparable pairs, including unchanged outcomes, that count is not an estimate of the probability that a difficulty increase improves performance.

## A third possibility: the verdict stays put

A difficulty-setting change need not cross the `PASS`/`FAIL` boundary at all.

The family summaries include groups with no recorded verdict variation. `architecture_naturality` has five `PASS` verdicts and no `FAIL` verdicts. `rd_gradient_credit` has eleven `PASS` verdicts and no `FAIL` verdicts. In the opposite direction, `glyph` has eight `FAIL` verdicts and no `PASS` verdicts.

These are recorded-label summaries, subject to the same judge-guarantee caution. They show the unchanged-outcome side of the campaign: different selected settings can retain the same verdict. The available summary does not enumerate the unchanged last-coordinate pairs individually, so I cannot give their number or infer their frequency from Figure 1.

There is also an important resolution limit here. "Unchanged" means unchanged **verdict**, not necessarily unchanged performance on every measure.

Some failures in the campaign receive nonzero partial-credit scores, including scores such as 0.95 and 0.5. Two cases labeled `FAIL` therefore need not have performed equally well. Conversely, a verdict transition does not by itself tell me the size of the numerical score change.

This essay concerns the ordering of binary verdicts. It does not establish that every stable verdict represents identical performance, or that every changed verdict represents a large deterioration or improvement.

## The aggregate reversal—and why I do not turn it into a validated rate

The campaign summary contains another counterintuitive observation: among scored cases, the group containing at least one `hard` dimension has a higher recorded pass share than the group containing no `hard` dimension.

That is the reported direction of the pooled difficulty comparison. It is not a validated aggregate result.

The comparison combines `behavioral_reference` and `compile_only` verdicts. Reproducing its pooled pass rates as model-success rates would cross the judge-guarantee boundary established above. I therefore do not report those combined rates or use the pooled reversal to strengthen the oracle-supported evidence.

The missing information is the intersection of difficulty status and judge guarantee. The summary supplies totals by guarantee and a separate pooled difficulty comparison. It does not supply the `hard`-containing and no-`hard` counts separately inside each guarantee bucket.

Consequently, I cannot determine from these summaries whether hard-containing cases pass more often within `behavioral_reference`, within `compile_only`, within both, or within neither. The pooled direction alone does not answer those questions.

Even apart from the guarantee problem, this aggregate comparison asks a different question from the matched pairs.

"No `hard` dimension" is not synonymous with "all dimensions easy"; it can include medium settings. The groups also contain cases from different environment families, which contribute different numbers of recorded cases. An across-case difference is therefore not equivalent to changing one coordinate while holding the environment and remaining coordinates fixed.

My initial temptation is to treat the aggregate reversal as the headline: hard cases pass more often. On inspection, that is too strong. The defensible account is that the supplied mixed-guarantee tally has that direction, while a guarantee-separated difficulty comparison is unavailable.

The within-environment contrasts remain interesting without borrowing authority from an inadmissible pooled rate.

## How much does "not reliable" mean?

There are several claims I need to keep apart.

**First, the recorded outcomes are not uniformly monotonic in the difficulty label.** The listed pairs establish that directly: the same final-coordinate change accompanies both `FAIL`-to-`PASS` and `PASS`-to-`FAIL` transitions. Other recorded settings retain the same verdict.

**Second, that does not establish that difficulty has zero predictive value.** A probabilistic predictor can have exceptions. Counterexamples to a perfect ordering do not prove the absence of an average relationship.

This is where the opening question needs a careful answer. If "does hard make failure more likely?" means "does every such change worsen the recorded outcome?", these cases answer no. If it means "what is the change in conditional failure probability?", the available summaries do not provide a reliable estimate.

I use "not reliable" in the narrower sense: the label alone does not consistently order these observed comparisons. I am not reporting a fitted predictive model, a calibrated failure probability, or a statistical demonstration of no association.

**Third, the direction varies across the listed environment families, but that does not make environment identity a proven replacement predictor.** The record shows heterogeneity. It does not establish that the family name determines what a difficulty change will do.

It would be easy to replace one overstatement with another: first assuming that difficulty controls the outcome, then concluding that environment controls it instead. Neither causal claim follows from this summary.

Several limits keep the interpretation local.

The campaign used one provider and text-only inputs. These observations do not establish the same pattern for another provider or modality.

Each selected cell has a single seed. The record therefore does not characterize run-to-run stability within a cell. I report no confidence intervals or estimates of how often each listed verdict would recur under repeated executions.

The displayed comparisons change only the last difficulty coordinate. They do not test every coordinate independently, and they do not establish what happens when several coordinates change together.

Finally, matching configuration labels is not the same as identifying a causal effect. The summary gives me no basis for explaining why a particular hard-side case passed when its easy-side counterpart failed. I cannot infer a mechanism from the direction of a verdict change.

These limits do not erase the observed contrasts. They determine what those contrasts can support.

## What survives the caveats

The result is smaller than "difficulty does not matter," but more concrete.

In five listed within-environment comparisons, the hard-side case passes while the easy-side case fails. In four, the easy-side case passes while the hard-side case fails. Other recorded settings retain their verdicts. A separate pooled summary points toward a higher pass share among hard-containing cases, but it mixes judge guarantees and cannot serve as a validated aggregate comparison.

I can therefore reject a simple reading of this campaign in which `hard` consistently pushes recorded outcomes toward failure. I cannot conclude that difficulty is irrelevant, that difficulty helps, or that I know why the contrasts reverse.

For this Atria record, `hard` is an intended setting—not a dependable ordering of observed success and failure. That is the correction I can make without turning a small empirical inconsistency into a universal theory.
]

EVIDENCE PACKET (verified against source snapshots and findings register)

Campaign identity:
- Event: atria_covering_campaign
- Provider: atria
- Execution mode: paid
- Case manifest sha256: c08e3637b50da84f8a02e47be96c0b18ec2792b0ccf109ba6b07ec00e699872d
- Recorded at: 2026-09-29T13:34:39.345679Z

Campaign status:
- Status: paused
- Pause reason: provider_error
- Resumable: true
- Recorded cases: 194
- Episodes completed: 194 / 194
- Current case: null
- Phase: episodes
- Progress updated at: 2026-10-02T04:55:06.143150Z

Gate:
- Gate carried: true
- Gated case count: 72
- Compile-only case count: 122

Results by judge guarantee:
- behavioral_reference: scored 72, verdict_pass 56, verdict_fail 16
- compile_only: scored 121, verdict_pass 75, verdict_fail 46, paused_provider_error 1

Provider outage:
- Waited seconds: 3300.0 (~55 minutes)
- Retries: 8
- Last backoff seconds: 600.0
- Last case ID: ts_trajectory__witness_status=broken_representation=reflective__seed-0
- Updated at: 2026-10-02T04:31:37.148365Z

Compatibility:
- Status: passed
- Attempts: 1
- Waited seconds: 0.0

Aggregate note:
- Report per judge_guarantee bucket only; compile_only verdicts are exploratory and excluded from any validated aggregate

Compile-only disclaimer:
- Compile_only rows are graded by judges without a behavioral reference on that exact instance; they do not carry the exact-instance oracle guarantee and must not be read as validated model verdicts

All environment results (194 cases, 193 scored + 1 paused_provider_error):

architecture_naturality: PASS=5 FAIL=0 score=1.000
batchnorm_ema: PASS=0 FAIL=11 score=0.086
categorical_lenses: PASS=4 FAIL=1 score=0.800
ci_dependency_graph: PASS=5 FAIL=0 score=1.000
compositional_optimizer: PASS=3 FAIL=2 score=0.600
css_state_machine: PASS=3 FAIL=2 score=0.683
epistemic_games: PASS=7 FAIL=0 score=1.000
equivariant_diagram: PASS=5 FAIL=0 score=1.000
functorial_augmentation: PASS=2 FAIL=3 score=0.650
glyph: PASS=0 FAIL=8 score=0.000
gnn_message_passing: PASS=0 FAIL=5 score=0.417
moco: PASS=9 FAIL=2 score=0.905
monadic_reward: PASS=1 FAIL=4 score=0.200
neuro_symbolic_parser: PASS=4 FAIL=1 score=0.800
rd_adaptive_halting: PASS=9 FAIL=2 score=0.818
rd_gradient_credit: PASS=11 FAIL=0 score=1.000
rd_state_carry: PASS=11 FAIL=0 score=1.000
regex_state_machine: PASS=3 FAIL=2 score=0.683
semiring_unification: PASS=5 FAIL=0 score=1.000
sheaf_invariant_gluing: PASS=5 FAIL=0 score=1.000
sheaf_physical_constraints: PASS=0 FAIL=5 score=0.111
sheaf_schema_sync: PASS=1 FAIL=4 score=0.200
spreadsheet_dataflow: PASS=5 FAIL=0 score=1.000
sql_fixed_point: PASS=4 FAIL=1 score=0.800
ssm_parallel_scan: PASS=5 FAIL=0 score=1.000
stochastic_monad: PASS=5 FAIL=0 score=1.000
template_interpreter: PASS=5 FAIL=0 score=1.000
tensor_functor: PASS=2 FAIL=3 score=0.400
tokenizer_adjunction: PASS=5 FAIL=0 score=1.000
transformer_ssm_lift: PASS=5 FAIL=0 score=1.000
ts_one_step: PASS=0 FAIL=3 score=0.333
ts_parse_only: PASS=2 FAIL=1 score=0.833
ts_trajectory: PASS=0 FAIL=2 paused_provider_error=1 score=0.000

Overall: PASS=131 FAIL=62 paused_provider_error=1

Aggregate difficulty vs no-difficulty comparison:
- Cases with at least one "hard" dimension: PASS=53 FAIL=20 pass_rate=0.726
- Cases with no "hard" dimension: PASS=78 FAIL=42 pass_rate=0.650
- Counterintuitive: cases containing "hard" pass MORE often than cases with no "hard" at all

Within-environment easy-vs-hard pairs (same environment, last dimension flipped easy→hard, all other dims held constant):

Hard PASSES while easy FAILS (counterintuitive — "hard" makes it easier):
- css_state_machine: easy,easy=FAIL | easy,hard=PASS
- compositional_optimizer: easy,easy=FAIL | easy,hard=PASS
- functorial_augmentation: easy,easy=FAIL | easy,hard=PASS
- sheaf_schema_sync: easy,easy=FAIL | easy,hard=PASS
- rd_adaptive_halting: easy,easy,easy,easy,easy=FAIL | easy,easy,easy,easy,hard=PASS

Easy PASSES while hard FAILS (intuitive):
- categorical_lenses: easy,easy=PASS | easy,hard=FAIL
- moco: easy,easy,easy,easy,easy,easy=PASS | easy,easy,easy,easy,easy,hard=FAIL
- monadic_reward: easy,easy=PASS | easy,hard=FAIL
- tensor_functor: easy,easy=PASS | easy,hard=FAIL

Limitations:
- Single provider (atria), text_only input modality
- Campaign paused at provider_error; one case (ts_trajectory__broken_reflective) marked paused_provider_error
- Compile_only verdicts are exploratory, not validated model verdicts
- No confidence intervals; single seed per selected cell
- Partial credit exists: some FAIL verdicts carry non-zero scores (0.95, 0.714, 0.5, 0.417, 0.286, 0.278, 0.208)
- Within-environment pairs only flip the last difficulty dimension; not all dimensions independently varied

REVIEWER BRIEF (accepted Stage A) — key points to respect:

- The strongest defensible thesis is narrow: flipping a difficulty dimension from "easy" to "hard" does not reliably produce a failure. Within the same environment, holding all other dimensions constant, some easy→hard flips cause a pass→fail, some cause a fail→pass, and some cause no change. "Hard" is not a reliable failure predictor.
- NOT defensible: claiming that difficulty dimensions never matter — some easy→hard flips do cause failures (categorical_lenses, moco, monadic_reward, tensor_functor).
- NOT defensible: claiming that "hard" reliably makes tasks easier — the effect is inconsistent across environments.
- NOT defensible: stitching behavioral_reference and compile_only buckets into one aggregate pass rate. Report per bucket only.
- NOT defensible: treating compile_only verdicts as validated model verdicts.
- NOT defensible: general evaluation prescriptions beyond what the evidence supports.
- The post is about the unreliability of "hard" as a failure predictor, not about the campaign being paused or unfinished. Mention the pause only as context for partial data; do not dwell on it.
- Tone: remove profanity, stray glyphs, and unsupported mechanistic language.

STYLE REFERENCE

- Jekyll frontmatter: title, date, layout: post. No extra fields.
- Byline: _by StrangeTcy_
- Epistemic-status with five fields: Original ideas, Synthesis, Prose, Certainty, Importance.
- First-person, curious, technically literate, self-correcting.
- Concrete cases, exact counts, caveats beside claims.
- No internal file paths/finding IDs/trace IDs/draft labels in public copy.
- Target ~1800-2800 words. Do not inflate.

TASK

Write a complete, independently structured research essay (not an outline, not a summary) for R-POST-02. Lead with a real question or tension: if you dial up "hard," does the model fail more often? Present the within-environment easy-vs-hard pairs as evidence that the answer is no — sometimes hard passes while easy fails, sometimes easy passes while hard fails, and sometimes nothing changes. State exactly what the evidence establishes (the counterintuitive pairs where hard passes but easy fails; the intuitive pairs where easy passes but hard fails; the aggregate showing hard-containing cases pass more often) and what it cannot (no claim that difficulty is irrelevant, no claim that difficulty helps, no causal mechanism for the inconsistency). Embed at least one figure with a caption. Place caveats where needed. Do not imply internal mechanisms. Do not make general evaluation prescriptions beyond what the evidence supports. Do not focus on the campaign being unfinished — focus on the unreliability of difficulty as a predictor.

OUTPUT: the full article markdown only.