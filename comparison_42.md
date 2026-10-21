---
title: "Epistemic Games Are 100% Solved"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic Status**
- **Original ideas:** 3/10 (Building on outcome patterns observed within the Atria campaign dataset).
- **Synthesis:** 8/10 (Aggregating per-environment pass rates to identify uniformly solved families).
- **Prose:** 8/10 (First-person, analytical, strictly bound by empirical constraints).
- **Certainty:** High on the reported counts for this specific campaign; limited on generalizing beyond it.
- **Importance:** 5/10 (Relevant for understanding which reasoning tasks current models have already mastered.)

***

When we evaluate reasoning models, we tend to assume that every task family contains some cases the model will fail. The intuition is that no benchmark is fully solved — there is always headroom, always a frontier where the model breaks down.

But what if some environment families are already fully solved? What if, for certain classes of reasoning tasks, the model passes every single case with a perfect score?

This is what I found when I analyzed the `atria_covering_campaign`. The campaign recorded 194 cases across 33 environment families. Fourteen of those families are uniformly solvable — every case passes with a score of 1.000. One of them, `epistemic_games`, stands out not just because it is fully solved, but because of what it is: a suite of reasoning tasks designed to test whether a model can track evidence, update beliefs, and resist misleading presentations. And the model passed all 7 cases with perfect scores.

### The Atria Covering Campaign: Strict Judge Guarantees

The campaign successfully recorded 194 cases. To maintain technical rigor, we must strictly divide these cases by the judge guarantee they carry. We cannot stitch these two buckets into a single aggregate pass rate, as doing so would conflate validated results with exploratory signals.

**1. The Behavioral Reference Bucket**
This bucket contains cases carrying a strict, exact-instance oracle guarantee. These are validated model verdicts. Within this gated bucket, the campaign evaluated 72 cases: 56 `PASS` and 16 `FAIL`.

**2. The Compile-Only Bucket**
The remaining cases were graded by judges without a behavioral reference on that exact instance. Compile-only verdicts are purely exploratory. They do not carry the exact-instance oracle guarantee and must not be read as validated model verdicts. Within this bucket, 121 cases were scored: 75 `PASS` and 46 `FAIL`. One additional case was marked as `paused_provider_error`.

*(Contextual note on the pause: The campaign is currently paused due to a provider error. A provider outage lasted approximately 55 minutes — 3300.0 seconds — requiring 8 retries and a final backoff of 600.0 seconds. The campaign paused on the case `ts_trajectory__witness_status=broken_representation=reflective__seed-0`. I mention this purely as context for why the dataset represents exactly 194 cases. The pause does not impact the analysis of the completed, scored cases.)*

### The Uniformly Solvable Environments

Fourteen distinct environments proved to be uniformly solvable. Across all instances tested within these families, the model achieved perfect 100% pass rates and scores of 1.000:

- `architecture_naturality`: PASS=5, FAIL=0
- `ci_dependency_graph`: PASS=5, FAIL=0
- `epistemic_games`: PASS=7, FAIL=0
- `equivariant_diagram`: PASS=5, FAIL=0
- `rd_gradient_credit`: PASS=11, FAIL=0
- `rd_state_carry`: PASS=11, FAIL=0
- `semiring_unification`: PASS=5, FAIL=0
- `sheaf_invariant_gluing`: PASS=5, FAIL=0
- `spreadsheet_dataflow`: PASS=5, FAIL=0
- `ssm_parallel_scan`: PASS=5, FAIL=0
- `stochastic_monad`: PASS=5, FAIL=0
- `template_interpreter`: PASS=5, FAIL=0
- `tokenizer_adjunction`: PASS=5, FAIL=0
- `transformer_ssm_lift`: PASS=5, FAIL=0

If you select a case at random from any of these 14 families, I can predict its success with near certainty before you even tell me what specific constraints were applied to the prompt. The environment itself practically guarantees a pass.

### Epistemic Games: 7 Out of 7

`epistemic_games` deserves special attention. This family contains 7 cases, all passing with perfect scores:

- `report_evidence=ambiguous_presentation=paired_prior=balanced_framing=bare_table`: PASS, score=1.0
- `trap_evidence=ambiguous_presentation=paired_prior=balanced_framing=bare_table`: PASS, score=1.0
- `report_evidence=strong_presentation=paired_prior=balanced_framing=bare_table`: PASS, score=1.0
- `report_evidence=weak_presentation=paired_prior=balanced_framing=bare_table`: PASS, score=1.0
- `report_evidence=ambiguous_presentation=solo_prior=balanced_framing=bare_table`: PASS, score=1.0
- `report_evidence=ambiguous_presentation=paired_prior=skewed_framing=bare_table`: PASS, score=1.0
- `report_evidence=ambiguous_presentation=paired_prior=balanced_framing=narrative`: PASS, score=1.0

Every case passes. Every score is 1.0. The model handles ambiguous evidence, strong evidence, weak evidence, trap evidence, solo and paired priors, balanced and skewed framing, bare tables and narrative formats — all without a single failure.

This is not a case of "the model mostly gets it right." This is a case of the model getting it right every time, across varied presentations and evidence conditions.

### What the Evidence Establishes (And What It Cannot)

The strongest defensible thesis is narrow: `epistemic_games` is uniformly solved in this campaign — all 7 cases pass with perfect scores. The same is true for 13 other environment families.

The evidence establishes the following concrete facts:

1. **`epistemic_games`: 7/7 PASS, all scores 1.000.** No failures across any variant.
2. **13 other environments are also uniformly solvable**, each with perfect pass rates.
3. **The solved families span diverse task types** — epistemic games, state carry, gradient credit, semantic unification, spreadsheet dataflow, and more.

However, what the evidence cannot establish is just as important:

First, this data does not support the claim that epistemic games are "easy" in any general sense. The 7 cases cover varied scenarios (ambiguous vs. strong vs. weak evidence, trap vs. report, solo vs. paired priors, balanced vs. skewed framing, bare table vs. narrative). The model passes them all, but that says nothing about harder variants not included in the campaign.

Second, this data does not support the claim that all reasoning is solved. Five environments are uniformly unsolvable (all FAIL), and 14 more are mixed. Solved families coexist with unsolved ones in the same campaign.

Third, this dataset cannot provide a causal mechanism for why epistemic games are solved while other families fail. I will not speculate on internal model architectures or representations.

Finally, this essay offers no general evaluation prescriptions. This is an analysis of one campaign.

### Limitations

This campaign relied entirely on a single provider (`atria`) in text-only modality. A different provider or modality might yield different results.

The campaign executed a single seed per selected cell, so we cannot calculate confidence intervals.

Compile-only verdicts (122 of 194 cases) are exploratory and lack the exact-instance oracle guarantee.

### Conclusion

When we evaluate reasoning models, we often assume there is always a frontier where the model fails. The `atria_covering_campaign` shows that for some task families, that frontier does not exist — at least not within the cases tested. `epistemic_games` is 7 out of 7, all perfect scores. The model does not fail these tasks.

But this is not a declaration of victory. It is an observation about one campaign, one provider, one set of cases. Some environments are solved; others are not. The work of understanding why — and of building benchmarks that capture what remains unsolved — continues.
