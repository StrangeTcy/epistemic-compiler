BATTLE WRITER A — R-POST-04: Partial Credit Is Real (Reasoning-Atria)

You are Writer A, an independent candidate producing a complete research essay for the StrangeTcy public site. Writer B will receive the same evidence independently and must not see your draft. Do not reference or incorporate Writer B's work.

ARTICLE SLOT: R-POST-04 — partial scores under FAIL verdicts (Reasoning-Atria).
RESEARCH QUESTION: What does a non-zero score on a FAIL verdict establish about the reported outcome, and what interpretations remain unsupported?

Article:

[
---
title: "Partial Credit Is Real"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic Status**
- **Original ideas:** 4/10 (Building on score distribution observed within the Atria campaign dataset).
- **Synthesis:** 7/10 (Aggregating per-case scores to show that FAIL verdicts carry partial credit).
- **Prose:** 8/10 (First-person, analytical, strictly bound by empirical constraints).
- **Certainty:** High on the reported counts for this specific campaign; limited on generalizing beyond it.
- **Importance:** 5/10 (Relevant for understanding how to interpret benchmark verdicts that binarize partial progress.)

***

When a model fails a reasoning task, we record a `FAIL` verdict. The natural assumption is that a fail means the model got nothing right — score 0.0, no progress, complete failure.

But what if that assumption is wrong? What if a `FAIL` verdict can still carry meaningful partial credit — the model made real headway, just not enough to cross the pass threshold?

This is what I found when I analyzed the `atria_covering_campaign`. The campaign recorded 194 cases across 33 environment families. Of the 62 scored `FAIL` verdicts, many carry non-zero scores. The model is not binary — pass or fail. It is making partial progress on tasks it ultimately fails.

### The Atria Covering Campaign: Strict Judge Guarantees

The campaign successfully recorded 194 cases. To maintain technical rigor, we must strictly divide these cases by the judge guarantee they carry. We cannot stitch these two buckets into a single aggregate pass rate, as doing so would conflate validated results with exploratory signals.

**1. The Behavioral Reference Bucket**
This bucket contains cases carrying a strict, exact-instance oracle guarantee. These are validated model verdicts. Within this gated bucket, the campaign evaluated 72 cases: 56 `PASS` and 16 `FAIL`.

**2. The Compile-Only Bucket**
The remaining cases were graded by judges without a behavioral reference on that exact instance. Compile-only verdicts are purely exploratory. They do not carry the exact-instance oracle guarantee and must not be read as validated model verdicts. Within this bucket, 121 cases were scored: 75 `PASS` and 46 `FAIL`. One additional case was marked as `paused_provider_error`.

*(Contextual note on the pause: The campaign is currently paused due to a provider error. A provider outage lasted approximately 55 minutes — 3300.0 seconds — requiring 8 retries and a final backoff of 600.0 seconds. The campaign paused on the case `ts_trajectory__witness_status=broken_representation=reflective__seed-0`. I mention this purely as context for why the dataset represents exactly 194 cases. The pause does not impact the analysis of the completed, scored cases.)*

### Partial Credit in FAIL Verdicts

A `FAIL` verdict does not uniformly mean a score of 0.0. The records show `FAIL` verdicts carrying non-zero scores: 0.95, 0.714, 0.5, 0.417, 0.286, 0.278, and 0.208.

Here are the specific cases where a `FAIL` verdict carries a non-zero score:

- `moco__naming=easy_distractors=easy_queue_math=easy_temperature=easy_visible_tests=medium_symptom_mask=easy__seed-0`: FAIL, score=0.95
- `ts_parse_only__witness_status=broken_representation=reflective__seed-0`: FAIL, score=0.5
- `ts_one_step__witness_status=valid_representation=flat__seed-0`: FAIL, score≈0.714
- `ts_one_step__witness_status=broken_representation=flat__seed-0`: FAIL, score≈0.286
- `gnn_message_passing`: PASS=0, FAIL=5, average score=0.417
- `sheaf_physical_constraints__medium_implementation_style=easy_notation_mismatch=medium_visible_tests=easy_hidden_context=easy_interaction_depth=easy_investigation_difficulty=easy_symptom_mask=hard__seed-0`: FAIL, score≈0.278
- `regex_state_machine__hard`: FAIL, score≈0.208
- `regex_state_machine__medium`: FAIL, score≈0.208

These are not rounding errors. A score of 0.95 on a FAIL verdict means the model got almost everything right but still failed. A score of 0.5 means it got halfway there. Even 0.208 means it made measurable progress.

### What the Evidence Establishes (And What It Cannot)

The strongest defensible thesis is narrow: a `FAIL` verdict does not mean zero progress. The `atria_covering_campaign` records multiple cases where a failed task still carries substantial partial credit.

The evidence establishes the following concrete facts:

1. **FAIL verdicts carry non-zero scores.** Scores of 0.95, 0.714, 0.5, 0.417, 0.286, 0.278, and 0.208 appear on failed cases.
2. **Near-total progress still fails.** The `moco` case scores 0.95 on a FAIL verdict — the model essentially solved the task but did not pass.
3. **Partial credit is distributed across families.** Non-zero FAIL scores appear in `moco`, `ts_parse_only`, `ts_one_step`, `gnn_message_passing`, `sheaf_physical_constraints`, and `regex_state_machine`.

However, what the evidence cannot establish is just as important:

First, this data does not support the claim that partial credit means "almost passed." A score of 0.208 is partial credit, but it is not close to passing. The range of non-zero FAIL scores spans from near-perfect to minimal.

Second, this data does not support the claim that all FAIL verdicts carry partial credit. Most FAIL verdicts score 0.0. Partial credit exists, but it is not universal.

Third, this dataset cannot tell us why some failures carry credit and others do not. I will not speculate on internal model mechanisms.

Finally, this essay offers no general evaluation prescriptions. This is an analysis of one campaign.

### Limitations

This campaign relied entirely on a single provider (`atria`) in text-only modality. A different provider or modality might yield different score distributions.

The campaign executed a single seed per selected cell, so we cannot calculate confidence intervals.

Compile-only verdicts (122 of 194 cases) are exploratory and lack the exact-instance oracle guarantee.

### Conclusion

When we record a `FAIL` verdict, we tend to treat it as total failure — the model got nothing right. The `atria_covering_campaign` shows that this is not true. A `FAIL` verdict can carry a score of 0.95, 0.5, or 0.208. The model is making progress even when it fails.

But partial credit is not the whole story. Most failures still score 0.0. Some environments are uniformly unsolvable; others are uniformly solved. The existence of partial credit does not change the bimodal landscape — it only complicates it.

The work of understanding what a score means — and how to interpret verdicts that binarize partial progress — continues.
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
- The defensible thesis is narrow: FAIL verdicts can carry non-zero reported scores in the sampled campaign. This does not mean all FAILs carry credit; most failures may still score zero.
- The specified per-case non-zero FAIL scores include 0.95, 0.714, 0.5, 0.286, 0.278, and 0.208. A reported score of 0.417 belongs to `gnn_message_passing` as the environment's average across five FAIL cases; do not present 0.417 as a verified score for one individual FAIL unless an individual case row supports it. Keep case-level scores distinct from environment averages.
- The campaign overall records 131 PASS, 62 FAIL and one paused provider-error case; do not conflate this campaign's 62 FAILs with the different Mercury campaign's 128 FAILs.
- Judge guarantees: 72 scored behavioral_reference cases and 121 scored compile_only cases plus one paused case. Compile_only grades are exploratory, not validated exact-instance verdicts. The packet gives no per-case guarantee for each partial-credit example, so do not imply each partial score has the same guarantee.
- Non-zero scores are score observations, not proof of an internal reasoning process or causal explanation. A score of 0.208 is partial, not “almost passed”; 0.95 is close to full credit by score but the rubric's meaning is not provided.
- One provider, text-only modality, one seed per cell, no confidence intervals, 11 cases unscored/one paused and no independent replication.
- The source article's listing mixes individual cases with one environment mean; correct that distinction. Do not make general evaluation prescriptions.

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
Write a complete research essay for R-POST-04 explaining what non-zero scores on FAIL verdicts show and what they do not show. Distinguish individual scored cases from environment-level averages, keep the score/verdict distinction clear, and put judge-guarantee and sampling caveats next to the claims. Include one compact table or figure with exact labels and caveats. Do not imply that partial credit means a case nearly passed unless the rubric supports that interpretation.

OUTPUT: full article markdown only.
