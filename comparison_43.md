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
