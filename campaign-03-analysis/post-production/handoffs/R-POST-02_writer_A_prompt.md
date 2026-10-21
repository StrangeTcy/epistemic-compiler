BATTLE WRITER A — R-POST-02: “Hard” Does Not Reliably Make Tasks Harder (Reasoning-Atria)

You are Writer A, an independent candidate producing a complete research essay for the StrangeTcy public site. Writer B will receive the same evidence independently and must not see your draft. Do not reference or incorporate Writer B's work.

ARTICLE SLOT: R-POST-02 — difficulty-dimension transitions (Reasoning-Atria).
RESEARCH QUESTION: Does flipping a difficulty dimension from easy to hard reliably increase failure within an environment?

Article:

[
---
title: "Does Hard Make Tasks Harder?"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic Status**
- **Original ideas:** 4/10 (Building on outcome patterns observed within the Atria campaign dataset).
- **Synthesis:** 7/10 (Aggregating within-environment case pairs to test whether difficulty dimensions predict failure).
- **Prose:** 8/10 (First-person, analytical, strictly bound by empirical constraints).
- **Certainty:** High on the reported counts; limited on generalizing beyond this single campaign.
- **Importance:** 6/10 (Relevant for understanding whether "difficulty" labels are meaningful predictors in reasoning benchmarks).

***

When we design a reasoning benchmark, we tend to treat "difficulty" as a dial we can turn. Easy tasks pass, hard tasks fail, and the slope between them tells us something about a model's reasoning capacity. It is intuitive to assume that dialing up the difficulty dimensions of a case — more logical constraints, deeper inference, more complex data structures — will smoothly decrease the likelihood of success.

But what if that assumption is wrong? What if flipping a case from "easy" to "hard" sometimes makes it easier, sometimes makes it harder, and sometimes changes nothing at all?

This is the central tension I wanted to explore when I analyzed the `atria_covering_campaign`. The campaign recorded 194 cases across 33 environment families, each case carrying a difficulty string of dimension values (easy, medium, hard). I initially expected to find that harder cases fail more often within the same environment. The data says otherwise.

Before testing the difficulty dial, we have to establish the boundaries of the dataset.

### The Atria Covering Campaign: Strict Judge Guarantees

The campaign successfully recorded 194 cases. To maintain technical rigor, we must strictly divide these cases by the judge guarantee they carry. We cannot stitch these two buckets into a single aggregate pass rate, as doing so would conflate validated results with exploratory signals.

**1. The Behavioral Reference Bucket**
This bucket contains cases carrying a strict, exact-instance oracle guarantee. These are validated model verdicts. Within this gated bucket, the campaign evaluated 72 cases: 56 `PASS` and 16 `FAIL`.

**2. The Compile-Only Bucket**
The remaining cases were graded by judges without a behavioral reference on that exact instance. Compile-only verdicts are purely exploratory. They do not carry the exact-instance oracle guarantee and must not be read as validated model verdicts. Within this bucket, 121 cases were scored: 75 `PASS` and 46 `FAIL`. One additional case was marked as `paused_provider_error`.

*(Contextual note on the pause: The campaign is currently paused due to a provider error. A provider outage lasted approximately 55 minutes — 3300.0 seconds — requiring 8 retries and a final backoff of 600.0 seconds. The campaign paused on the case `ts_trajectory__witness_status=broken_representation=reflective__seed-0`. I mention this purely as context for why the dataset represents exactly 194 cases. The pause does not impact the analysis of the completed, scored cases.)*

### The Difficulty Dial Does Not Turn the Way We Expect

If "hard" reliably predicted failure, we would expect to see a consistent pattern: within any given environment, flipping a dimension from "easy" to "hard" should move a case from PASS to FAIL. The data does not show this.

Across all 194 cases, those containing at least one "hard" dimension actually passed *more* often than those with no "hard" at all:

- Cases with at least one "hard" dimension: PASS=53, FAIL=20 (pass rate 0.726)
- Cases with no "hard" dimension: PASS=78, FAIL=42 (pass rate 0.650)

The aggregate is already counterintuitive. But the within-environment comparison is where the story really breaks down.

### Within-Environment Easy-vs-Hard Pairs

I looked at pairs of cases within the same environment family where every difficulty dimension was held constant except the last one, flipped from "easy" to "hard." If difficulty predicted failure, the hard case should fail whenever the easy case passes — or at least never pass when the easy case fails.

That is not what happens.

**Hard passes while easy fails** — counterintuitive cases where increasing difficulty appears to help:

- `css_state_machine`: easy,easy=FAIL | easy,hard=PASS
- `compositional_optimizer`: easy,easy=FAIL | easy,hard=PASS
- `functorial_augmentation`: easy,easy=FAIL | easy,hard=PASS
- `sheaf_schema_sync`: easy,easy=FAIL | easy,hard=PASS
- `rd_adaptive_halting`: easy,easy,easy,easy,easy=FAIL | easy,easy,easy,easy,hard=PASS

**Easy passes while hard fails** — the intuitive cases, but they are not the whole story:

- `categorical_lenses`: easy,easy=PASS | easy,hard=FAIL
- `moco`: easy,easy,easy,easy,easy,easy=PASS | easy,easy,easy,easy,easy,hard=FAIL
- `monadic_reward`: easy,easy=PASS | easy,hard=FAIL
- `tensor_functor`: easy,easy=PASS | easy,hard=FAIL

In some environments, hard makes failure more likely. In others, it makes failure less likely. In still others, it changes nothing. The difficulty dial does not turn in one direction.

<br>

> **Figure 1: The Difficulty Dial Is Not Monotonic**
> *(Within-environment easy-vs-hard pairs where only the last difficulty dimension changes. In `css_state_machine`, `compositional_optimizer`, `functorial_augmentation`, `sheaf_schema_sync`, and `rd_adaptive_halting`, flipping a dimension from easy to hard converts a FAIL into a PASS. In `categorical_lenses`, `moco`, `monadic_reward`, and `tensor_functor`, the same flip converts a PASS into a FAIL. The direction of the effect depends on the environment family, not on the difficulty label itself.)*

<br>

### What the Evidence Establishes (And What It Cannot)

The strongest defensible thesis is narrow: flipping a difficulty dimension from "easy" to "hard" does not reliably produce a failure. Within the same environment, holding all other dimensions constant, some easy→hard flips cause pass→fail, some cause fail→pass, and some cause no change. "Hard" is not a reliable failure predictor.

The evidence establishes the following concrete facts:

1. **Cases containing "hard" pass more often overall** — 0.726 vs 0.650 pass rate.
2. **Within some environments, hard makes failure more likely** — `categorical_lenses`, `moco`, `monadic_reward`, `tensor_functor`.
3. **Within other environments, hard makes failure less likely** — `css_state_machine`, `compositional_optimizer`, `functorial_augmentation`, `sheaf_schema_sync`, `rd_adaptive_halting`.
4. **The effect direction depends on the environment family**, not on the difficulty label alone.

However, what the evidence cannot establish is just as important:

First, this data does not support the claim that difficulty dimensions never matter. Some easy→hard flips do cause failures. Difficulty has not been ruled out as a factor.

Second, this data does not support the claim that "hard" reliably makes tasks easier either. The effect is inconsistent across environments. The five counterintuitive cases are interesting, but they do not establish a general rule.

Third, this dataset cannot provide a causal mechanism for why flipping a dimension helps in some environments and hurts in others. I will not speculate on internal model architectures or mechanistic limitations.

Finally, this essay offers no general evaluation prescriptions. This is an analysis of one campaign, one provider, one modality.

### Limitations

This campaign relied entirely on a single provider (`atria`) in text-only modality. A different provider or modality might yield different patterns.

The campaign executed a single seed per selected cell, so we cannot calculate confidence intervals.

The within-environment pairs only flip the last difficulty dimension; not all dimensions were independently varied.

Compile-only verdicts (122 of 194 cases) are exploratory and lack the exact-instance oracle guarantee.

### Conclusion

When a model fails a reasoning task, our instinct is to blame the difficulty of the prompt. We assume the model couldn't handle the depth of the logic or the length of the constraints.

The `atria_covering_campaign` suggests a different picture. Difficulty is not a universal, domain-agnostic slider. Whether "hard" makes a task harder depends on the environment family the task lives in. If you want to predict whether the model will pass or fail, asking whether the prompt is "hard" is not enough. You have to ask what environment it lives in — because the environment shapes what difficulty even means.
]

EVIDENCE PACKET (verified against the Reasoning-Atria campaign record)

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

REVIEWER BRIEF — required corrections
- The narrow thesis is that flipping the last recorded difficulty dimension from easy to hard does not reliably lead to failure in this dataset. Five listed pairs change FAIL→PASS; four change PASS→FAIL. These do not establish that hard helps, that difficulty is irrelevant, or that the direction of effect is statistically associated with environment.
- Cases with at least one hard dimension: PASS=53, FAIL=20, pass rate 0.726. Cases with no hard dimensions: PASS=78, FAIL=42, pass rate 0.650. These categories total 193 scored cases; one additional recorded case is paused, not scored. Treat the aggregate as descriptive; do not infer a causal effect of “hard.”
- Within-environment pairs hold other listed dimensions constant and flip the last dimension. Five hard-pass/easy-fail cases: `css_state_machine`, `compositional_optimizer`, `functorial_augmentation`, `sheaf_schema_sync`, `rd_adaptive_halting`. Four easy-pass/hard-fail cases: `categorical_lenses`, `moco`, `monadic_reward`, `tensor_functor`.
- The packet does not enumerate outcome-identical pairs or provide a denominator of all eligible pairs; do not assert a measured “no change” category unless you can substantiate it from the evidence included.
- Do not claim one universal difficulty scale across environment-specific axes. Only the last dimension was flipped in the listed paired comparisons; not all dimensions were independently varied.
- Do not merge behavioral_reference and compile_only cases in a validated aggregate; compile_only results are exploratory.
- Limitations: one Atria provider, text-only, one seed per selected cell, no confidence intervals, a paused provider-error case, partial credit on some FAILs. No causal mechanism or general evaluation prescriptions.


STYLE REFERENCE
- Jekyll front matter: title, date, layout: post. No extra fields.
- Byline: _by StrangeTcy_
- Epistemic-status section with exactly five fields: Original ideas, Synthesis, Prose, Certainty, Importance.
- First-person, curious, technically literate, self-correcting.
- Concrete cases, exact counts, caveats beside claims.
- No internal file paths, finding IDs, trace IDs, or draft labels in public copy.
- Approximately 1,800–2,800 words; do not inflate.
- Include at least one meaningful figure or table with a caption. It must reflect the reported data, not imply a statistical test that was not performed.
- This is the Reasoning-Atria campaign, not the already-published plain-Atria blog posts. Keep the dataset identity explicit and do not import results from plain-Atria posts.


TASK
Write a complete research essay for R-POST-02. Lead with the question “Does dialling up hard predict failure?” Use the aggregate rates and the nine listed within-environment flips, keeping their denominators and limitations explicit. Correct any source-draft claim that goes beyond the packet, including unsupported assertions about unchanged pairs. State what the comparisons establish and what they cannot establish. Include at least one figure/table and a precise caption.

OUTPUT: full article markdown only.
