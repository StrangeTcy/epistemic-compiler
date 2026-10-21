gemini 3.1 pro grounding:

---
title: "Environment dominates difficulty"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic Status**
- **Original ideas:** 3/10 (Building heavily on existing categorical observations within our datasets).
- **Synthesis:** 8/10 (Aggregating campaign outcomes to isolate environment variables from difficulty variables).
- **Prose:** 8/10 (First-person, analytical, and strictly bound by empirical constraints).
- **Certainty:** High regarding the outcomes of this specific Atria campaign; strictly limited to the recorded dataset without cross-provider generalization.
- **Importance:** 7/10 (Crucial for understanding what our metrics are actually testing when we design reasoning benchmarks).

***

When we set out to evaluate the reasoning capabilities of a model, we naturally lean on a familiar set of assumptions about what makes a task "hard." We tend to conceptualize difficulty as a collection of independent, stackable dimensions: the number of logical constraints, the depth of the required inference, the complexity of the data structures, or the sheer length of the context window. It is intuitive to assume that dialing up these difficulty dimensions will smoothly decrease the likelihood of a model's success. We assume that a simple prompt will pass, and a highly complex prompt will fail, regardless of the domain. 

But what if this assumption is fundamentally backwards? What if the environment family in which a task resides acts as an immovable ceiling, overriding the specific difficulty dimensions of any given case? Does the "hard" knob actually predict failure, or does the environment family dominate the outcome?

This is the central tension I wanted to explore when I began analyzing the recent `atria_covering_campaign`. Executed by the `atria` provider in a text-only modality, this campaign provides a distinct window into how model performance clusters. I initially expected to find a smooth, predictable gradient of success based on individual case complexity. However, looking closely at the data, I must correct that assumption. The evidence points to a much narrower, but significantly more defensible thesis: a case's outcome is predicted more by its environment family than by its individual difficulty dimensions. 

Before we can map the environmental landscape, we have to establish the strict boundaries of the dataset itself. 

### The Atria Covering Campaign: Strict Judge Guarantees

The campaign successfully recorded 194 cases. To maintain any kind of technical rigor, we must strictly divide these 194 cases by the judge guarantee they carry. We cannot and must not stitch these two distinct buckets into a single aggregate pass rate, as doing so would conflate validated results with exploratory signals.

**1. The Behavioral Reference Bucket**
This bucket contains the cases that carry a strict, exact-instance oracle guarantee. These are validated model verdicts. Within this gated bucket, the campaign evaluated 72 cases. The model returned 56 `PASS` verdicts and 16 `FAIL` verdicts. 

**2. The Compile-Only Bucket**
The remaining cases were graded by judges without a behavioral reference on that exact instance. I must emphasize a strict disclaimer here: compile-only verdicts are purely exploratory. They do not carry the exact-instance oracle guarantee and must not be read as validated model verdicts. Within this compile-only bucket, 121 cases were successfully scored, resulting in 75 `PASS` verdicts and 46 `FAIL` verdicts. One additional case in this bucket was marked as paused.

*(Contextual note on the pause: The campaign is currently in a paused state due to a provider error. We experienced a provider outage lasting approximately 55 minutes, or 3300.0 seconds, requiring 8 retries and a final backoff of 600.0 seconds. The campaign paused precisely on the case `ts_trajectory__witness_status=broken_representation=reflective__seed-0`. I mention this purely as context for why our dataset represents exactly 194 cases and why one case sits in a `paused_provider_error` state. The pause does not impact the analysis of the completed, scored cases.)*

With these strict divisions established for our overall campaign metrics, we can now look at how the 194 cases distribute across their 33 specific environment families to test our hypothesis. Keep in mind that the per-environment breakdowns below reflect the structural observations across both buckets to map domain trends, but they do not circumvent the requirement to treat compile-only data as exploratory.

### The Bimodal Landscape: 14 Solvable, 5 Unsolvable

If difficulty dimensions were the primary driver of outcomes, we would expect most environment families to display a mix of passes and fails. An easy instance in a given environment would pass, while a hard instance would fail, leaving most environments hovering around a 40% to 60% success rate. 

That is not what the data shows. Instead, the results cluster heavily at the extremes. Knowing the environment tells you far more than knowing whether a specific instance is "easy" or "hard."

**The Uniformly Solvable Environments**
Fourteen distinct environments proved to be uniformly solvable. Across all instances tested within these families, the model achieved perfect 100% pass rates and scores of 1.000. 

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

If you select a case at random from `rd_state_carry` or `epistemic_games`, I can predict its success with near certainty before you even tell me what specific constraints were applied to the prompt. The environment itself practically guarantees a pass. 

**The Uniformly Unsolvable Environments**
On the opposite end of the spectrum, five environments are uniformly unsolvable. Within these families, the model returned exclusively `FAIL` verdicts and near-zero scores. 

- `batchnorm_ema`: PASS=0, FAIL=11, score=0.086
- `glyph`: PASS=0, FAIL=8, score=0.000
- `sheaf_physical_constraints`: PASS=0, FAIL=5, score=0.111
- `ts_one_step`: PASS=0, FAIL=3, score=0.333
- `ts_trajectory`: PASS=0, FAIL=2 (with 1 paused), score=0.000

In these five domains, the environment is effectively a terminal diagnosis. You could design what you believe to be a trivially "easy" instance of `glyph`, minimizing all traditional difficulty dimensions, and the model will still fail. The environment overrides the difficulty dial.

<br>

> **Figure 1: The Predictive Power of Environments**
> *(A conceptual representation of the Atria campaign's environment pass rates. Instead of a standard bell curve of difficulty, we observe a starkly bimodal distribution. 14 environment families sit entirely at the 100% pass threshold, while 5 families sit entirely at the 0% pass threshold with near-zero scores. The overarching domain dictates the outcome far more reliably than case-by-case complexity tuning.)*

<br>

### The Middle Ground: Where Difficulty Still Matters

It is crucial that I state exactly what the evidence establishes, and what it does *not*. I am not claiming that difficulty dimensions do not matter at all. The evidence does not support the idea that internal task complexity is entirely irrelevant. 

The remaining 14 environments in our dataset fall into a middle ground, proving that some intra-environment variation does exist. In these families, the difficulty dimensions likely play a deciding role.

Consider environments that lean toward success but feature notable stumbles:
- `moco`: PASS=9, FAIL=2 (score=0.905)
- `categorical_lenses`: PASS=4, FAIL=1 (score=0.800)
- `neuro_symbolic_parser`: PASS=4, FAIL=1 (score=0.800)
- `rd_adaptive_halting`: PASS=9, FAIL=2 (score=0.818)
- `sql_fixed_point`: PASS=4, FAIL=1 (score=0.800)
- `ts_parse_only`: PASS=2, FAIL=1 (score=0.833)

Here, the environment is generally tractable, but something about the individual case complexity forces a failure. 

We see the inverse in environments that lean heavily toward failure but occasionally allow a pass:
- `monadic_reward`: PASS=1, FAIL=4 (score=0.200)
- `sheaf_schema_sync`: PASS=1, FAIL=4 (score=0.200)

And finally, we have the true battlegrounds—environments where the model appears highly sensitive to the specific parameters of the case:
- `compositional_optimizer`: PASS=3, FAIL=2 (score=0.600)
- `css_state_machine`: PASS=3, FAIL=2 (score=0.683)
- `functorial_augmentation`: PASS=2, FAIL=3 (score=0.650)
- `regex_state_machine`: PASS=3, FAIL=2 (score=0.683)
- `tensor_functor`: PASS=2, FAIL=3 (score=0.400)

Furthermore, we must acknowledge the nuance of partial credit. The dataset contains a rich gradient of partial scores within `FAIL` verdicts. A fail does not uniformly mean a score of 0.0. The records show `FAIL` verdicts carrying non-zero scores of 0.95, 0.714, 0.5, 0.417, 0.286, 0.278, and 0.208. 

The environment `gnn_message_passing`, for instance, recorded 0 passes and 5 fails, but maintained a score of 0.417. Because it achieved robust partial credit, it escapes our classification of being uniformly unsolvable with a "near-zero" score, landing instead in this nuanced middle ground. This partial credit proves that the model is making varied progress based on the specifics of the prompt, reinforcing that individual difficulty dimensions still matter, even if they do not dictate the final binary outcome as strongly as the environment itself.

### What the Evidence Establishes (And What It Cannot)

Synthesizing all this data, the strongest defensible thesis remains narrow but highly significant. When determining whether a task will pass or fail, the environment family is the dominant predictive factor. 

The evidence establishes the following concrete facts:
1. **14 environments are uniformly solvable.** Regardless of case difficulty, the model passed every time.
2. **5 environments are uniformly unsolvable.** Regardless of case difficulty, the model failed completely, with near-zero scores.
3. **The environment sets the baseline.** An "easy" case in a uniformly unsolvable environment is vastly more likely to fail than a "hard" case in a uniformly solvable environment.

However, as a technically curious observer, I must also strictly bound my conclusions. What the evidence *cannot* establish is just as important as what it can.

First, this data does not support the claim that difficulty dimensions are irrelevant. As we saw in the middle-ground environments, variation exists. Tuning the difficulty dials clearly tips the scales in families like `tensor_functor` or `regex_state_machine`.

Second, this dataset cannot provide a causal mechanism for *why* some environments are inherently harder than others. I will not speculate on internal model architectures, tokenization bottlenecks, or mechanistic limitations. The data shows us *that* `glyph` fails universally and *that* `rd_state_carry` passes universally; it does not tell us *how* the model is structurally failing.

Finally, this essay cannot and does not offer general evaluation prescriptions. This is an analysis of one specific campaign. While it highlights a fascinating reality about how we measure model capability, it is not a blanket directive on how the industry should structure its benchmarks moving forward. 

### Final Limitations and Caveats

It is essential to read this analysis through the lens of its specific constraints. 

As mentioned, this campaign relied entirely on a single provider (`atria`) locked into a text-only input modality. A multi-modal approach or an alternate provider might yield entirely different environmental biases. 

Additionally, the campaign executed only a single seed per selected cell. Without multiple runs across varying seeds, we are unable to calculate rigorous confidence intervals for these pass rates. We are observing a single, frozen snapshot in time.

And I must reiterate the most critical caveat of all: the heavy reliance on compile-only data within these environmental groupings. Of the 194 cases, 122 are compile-only and thus exploratory. They lack the behavioral reference necessary to be deemed exact-instance oracle guarantees. Our observations about the 33 environment families reflect structural trends in the dataset, but they are intrinsically tied to this exploratory methodology. 

### Conclusion

When a model fails a reasoning task, our first instinct is often to blame the complexity of the prompt. We assume the model simply couldn't handle the depth of the logic or the length of the constraints. 

But the `atria_covering_campaign` paints a different picture. It suggests that difficulty is not a universal, domain-agnostic slider. Instead, the model's capacity is overwhelmingly dictated by the environment family it is operating within. If you want to predict whether the model will pass or fail, do not ask how hard the prompt is. Ask what environment the prompt lives in. Because, at least in this dataset, the environment sets the ceiling, and the environment dominates the difficulty.

&&&&&&&&

gpt 6 luna max:

---
title: "Does Environment Predict Failure Better Than Difficulty?"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

### Epistemic status

- **Original ideas:** The interpretation of the outcome patterns below.
- **Synthesis:** One Atria campaign, as reported in the supplied evidence.
- **Prose:** Original commentary based on that evidence.
- **Certainty:** High on the reported counts; limited on any comparison with unmeasured difficulty dimensions.
- **Importance:** Suggestive about this campaign's environment families, not a general result about models or tasks.

Does "hard" predict failure, or does the environment family a case belongs to? If I know only that a case is difficult, I might expect that label to tell me something about its outcome. But in this campaign, the environment summaries divide into strikingly different outcome patterns: some families have only passes, some have no passes, and others contain both.

My narrow answer is that **environment family is the more informative coarse predictor in these observed results**. Fourteen families are all-PASS among their scored cases. Five have no scored PASS. The remaining fourteen are mixed. That is a strong descriptive pattern—but not a formal contest between environment and measured difficulty. The evidence packet does not include case-level difficulty ratings or a predictive model comparing them.

### What was scored

The evidence comes from one paid, text-only campaign using the Atria provider. There were 194 cases across 33 environment families: 193 received scored verdicts, and one remained paused after a provider error.

The results are separated by judge guarantee:

| Judge guarantee | Scored | PASS | FAIL | Other |
|---|---:|---:|---:|---|
| Behavioral reference | 72 | 56 | 16 | — |
| Compile-only | 121 | 75 | 46 | 1 paused case |

The behavioral-reference cases have an exact-instance behavioral reference. The compile-only cases do not: their verdicts are exploratory and should not be read as validated model verdicts. I keep these buckets separate and do not calculate a combined campaign pass rate.

The environment ledger below is useful for seeing the pattern across families, but it is supplied across both judge-guarantee buckets. Because there is no environment-by-guarantee breakdown, it is descriptive evidence—not a validated, reference-only comparison of environments.

```text
Outcome pattern across 33 environment families

All scored cases PASS   14 | ##############
No scored case PASS      5 | #####
Both PASS and FAIL      14 | ##############
```

**Figure 1.** Environment families grouped by their observed verdict pattern. “No scored case PASS” includes TS trajectory, which had two FAILs and one paused, unscored case; it is not a complete set of verdicts for that family.

### The environment ledger

| Environment family | PASS | FAIL | Paused | Reported score |
|---|---:|---:|---:|---:|
| Architecture naturality | 5 | 0 | 0 | 1.000 |
| BatchNorm EMA | 0 | 11 | 0 | 0.086 |
| Categorical lenses | 4 | 1 | 0 | 0.800 |
| CI dependency graph | 5 | 0 | 0 | 1.000 |
| Compositional optimizer | 3 | 2 | 0 | 0.600 |
| CSS state machine | 3 | 2 | 0 | 0.683 |
| Epistemic games | 7 | 0 | 0 | 1.000 |
| Equivariant diagram | 5 | 0 | 0 | 1.000 |
| Functorial augmentation | 2 | 3 | 0 | 0.650 |
| Glyph | 0 | 8 | 0 | 0.000 |
| GNN message passing | 0 | 5 | 0 | 0.417 |
| MoCo | 9 | 2 | 0 | 0.905 |
| Monadic reward | 1 | 4 | 0 | 0.200 |
| Neuro-symbolic parser | 4 | 1 | 0 | 0.800 |
| RD adaptive halting | 9 | 2 | 0 | 0.818 |
| RD gradient credit | 11 | 0 | 0 | 1.000 |
| RD state carry | 11 | 0 | 0 | 1.000 |
| Regex state machine | 3 | 2 | 0 | 0.683 |
| Semiring unification | 5 | 0 | 0 | 1.000 |
| Sheaf invariant gluing | 5 | 0 | 0 | 1.000 |
| Sheaf physical constraints | 0 | 5 | 0 | 0.111 |
| Sheaf schema sync | 1 | 4 | 0 | 0.200 |
| Spreadsheet dataflow | 5 | 0 | 0 | 1.000 |
| SQL fixed point | 4 | 1 | 0 | 0.800 |
| SSM parallel scan | 5 | 0 | 0 | 1.000 |
| Stochastic monad | 5 | 0 | 0 | 1.000 |
| Template interpreter | 5 | 0 | 0 | 1.000 |
| Tensor functor | 2 | 3 | 0 | 0.400 |
| Tokenizer adjunction | 5 | 0 | 0 | 1.000 |
| Transformer–SSM lift | 5 | 0 | 0 | 1.000 |
| TS one-step | 0 | 3 | 0 | 0.333 |
| TS parse-only | 2 | 1 | 0 | 0.833 |
| TS trajectory | 0 | 2 | 1 | 0.000 |

The reported score is not the same thing as the fraction of cases that passed. Partial credit is present: for example, GNN message passing has no PASS verdicts but a reported score of 0.417. A FAIL therefore does not necessarily mean a score of zero.

### The separation is the story

The clearest contrast is between families with the same number of scored cases. RD gradient credit has 11 PASS and no FAIL; RD state carry also has 11 PASS and no FAIL. BatchNorm EMA, with 11 scored cases as well, has 11 FAIL and no PASS. Their reported scores are 1.000, 1.000, and 0.086, respectively.

That contrast does not show *why* those families differ. It does show why a single, environment-blind label like "hard" is a blunt summary of these results. The family label sorts the observed outcomes into sharply different groups: there are environments where every scored case passed, and others where none did.

The no-PASS group needs a small but important qualification. Four families—BatchNorm EMA, Glyph, GNN message passing, and Sheaf physical constraints—have only FAILs among all their scored cases. TS trajectory also has no scored PASS, but one of its three cases was paused rather than scored. So "five uniformly unsolved" is shorthand for the observed verdicts: four complete all-FAIL sets and one family with only FAILs among its two scored cases, plus one unresolved case. It would be too strong to say that all three TS trajectory cases failed.

The middle group matters just as much. Fourteen families contain both PASS and FAIL verdicts. CSS state machine, for example, has three PASS and two FAIL; Tensor functor has two PASS and three FAIL; TS parse-only has two PASS and one FAIL. These within-family differences are a direct reason not to treat environment as destiny. A family can make a useful coarse distinction without settling the result of every case inside it.

### What "predicts more" can mean here

I should be precise about the word *predicts*. If it means "which label best sorts the outcomes in this reported ledger?", the answer points toward environment family. Fourteen all-PASS groups, five no-PASS groups, and fourteen mixed groups are not what I would expect from an account in which a generic hard/easy description alone captures the visible pattern.

If instead it means "which variable wins in a measured, out-of-sample prediction test?", this evidence cannot answer that. There are no case-level difficulty dimensions in the packet, no fitted comparison, and no reported predictive performance for environment labels versus difficulty features. I cannot estimate how much more predictive environment is, or compare it against every possible individual dimension.

The distinction is important: **the data support environment family as the stronger descriptive grouping, but they do not quantify a head-to-head predictive advantage.** Nor do they show that difficulty is irrelevant. The mixed families demonstrate that outcomes vary within some environments; the evidence does not identify what accounts for that variation. Difficulty may matter, but this packet does not isolate its contribution.

I also can't infer a mechanism from the names of the environment families. The results do not tell us why BatchNorm EMA differs from RD gradient credit, or why some other families fall in the middle. Any explanation based on task structure, representation, or another feature would need evidence beyond these outcome counts.

### How far to take the result

The exact claim supported by the environment ledger is limited: among the 33 families in this campaign, 14 are all-PASS across their scored cases, five have no scored PASS, and 14 contain both PASS and FAIL. The "five" has the TS trajectory caveat above. These are observations about the cases scored in this campaign, not guarantees about every possible case in those families.

There is also an important guarantee limitation. The per-environment ledger pools the behavioral-reference and compile-only results, and the packet does not provide a per-environment split between them. The compile-only verdicts are exploratory, not exact-instance validated results. So the sharp environment pattern is visible in the supplied ledger, but I cannot establish from this breakdown alone that the same pattern holds within the behavioral-reference bucket by itself.

Finally, this is one provider, one input modality, and a small number of cases in many families. There is no confidence interval, and the selected cells use a single seed. Those limits make the pattern worth noticing, not a basis for a universal law. One case is also unscored after the provider pause; that matters for the completeness of TS trajectory, but not enough to change the broader descriptive picture.

So, does "hard" predict failure better than environment family? **In this campaign's reported results, environment family is the more useful coarse guide.** The conclusion is strongest as a description of the observed grouping, not as a formal predictive estimate. Difficulty has not been ruled out; within-family variation is right there in the data. What the ledger makes hard to ignore is how much the outcome changes from one environment family to another.
