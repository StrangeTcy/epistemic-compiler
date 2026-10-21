fable 5.1:

---
title: "Does Hard Make Tasks Harder?"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic Status**
- **Original ideas:** 4/10 (The question is old; the within-environment pairing is the only novel move here.)
- **Synthesis:** 7/10 (Counts pulled from one campaign snapshot and arranged to test a single prediction.)
- **Prose:** 7/10 (First-person, deliberately narrow, corrects itself where the data forces it to.)
- **Certainty:** High on every number quoted; low on anything that generalizes past this one campaign.
- **Importance:** 6/10 (If difficulty labels do not predict failure, a lot of benchmark design rests on a weaker floor than it assumes.)

***

Here is a prediction I would have made before looking at any data. Take a reasoning task. Keep everything about it fixed — the environment family, the seed, every difficulty dimension but one — and flip that last dimension from `easy` to `hard`. The model should fail more often on the hard version. Not always. But on net, and reliably enough that the label "hard" would be a useful thing to know before you see the verdict.

That prediction is the quiet assumption behind most difficulty-stratified benchmarks. We build a dial, we turn it, and we read the slope. The slope is supposed to tell us something about reasoning capacity.

I wanted to know whether the dial actually turns. So I took one campaign where the difficulty labels were explicit, the environment families were fixed, and the case grid let me hold everything else constant, and I asked the narrowest version of the question I could: when only the last dimension flips from easy to hard, what happens to the verdict?

The short answer is that it depends on the environment, and not in a direction you can predict from the label.

### What was measured

The campaign in question is the `atria_covering_campaign`: one provider (`atria`), paid execution, text-only input. It recorded 194 cases across 33 environment families. Each case carries a difficulty string — a comma-separated list of dimension values drawn from `easy`, `medium`, and `hard` — and each case resolves to a verdict of `PASS` or `FAIL`, along with a numeric score.

Before I touch the difficulty question, I need to separate the cases by what kind of judge produced the verdict, because the two kinds are not interchangeable.

**Behavioral-reference cases** were graded against an exact-instance oracle: the judge had a behavioral reference for that specific instance. These are the validated verdicts. There are 72 of them: 56 `PASS`, 16 `FAIL`.

**Compile-only cases** were graded by judges without a behavioral reference on that exact instance. These verdicts are exploratory. They do not carry the oracle guarantee and should not be read as validated model verdicts. There are 122 such cases; 121 were scored (75 `PASS`, 46 `FAIL`) and one is marked `paused_provider_error`.

| Judge guarantee | Scored | PASS | FAIL | Other |
|---|---|---|---|---|
| behavioral_reference | 72 | 56 | 16 | — |
| compile_only | 121 | 75 | 46 | 1 paused |

I am not going to combine these two rows into a single campaign-wide pass rate. Doing so would launder exploratory verdicts into the validated bucket, and nothing in this post depends on a stitched number. Where I do quote a pooled count later, I flag it as a pooled count and explain what that costs.

One piece of housekeeping: the campaign is currently in a paused state after a provider outage (roughly 55 minutes of waiting, eight retries, a final backoff of ten minutes). The single paused case is `ts_trajectory__witness_status=broken_representation=reflective__seed-0`. That is why the denominator is 194 recorded with 193 scored. The pause has no bearing on the scored cases, and I will not mention it again.

### The direct test: hold everything, flip the last dimension

The cleanest test of the difficulty dial is a within-environment pair. Two cases from the same environment family, with identical difficulty strings except that the final dimension is `easy` in one and `hard` in the other. If `hard` is a failure predictor, the pattern we should see across such pairs is simple: when the verdicts differ, the easy case passes and the hard case fails. We might tolerate some pairs where both pass or both fail. What we should essentially never see is the reverse — the easy case failing while its hard sibling passes.

The campaign contains nine such pairs where the verdict actually changes. Here they are.

> **Figure 1. Within-environment easy→hard flips that changed the verdict.**
>
> | Environment | Easy case (string → verdict) | Hard case (string → verdict) | Direction |
> |---|---|---|---|
> | `css_state_machine` | `easy,easy` → FAIL | `easy,hard` → PASS | hard helps |
> | `compositional_optimizer` | `easy,easy` → FAIL | `easy,hard` → PASS | hard helps |
> | `functorial_augmentation` | `easy,easy` → FAIL | `easy,hard` → PASS | hard helps |
> | `sheaf_schema_sync` | `easy,easy` → FAIL | `easy,hard` → PASS | hard helps |
> | `rd_adaptive_halting` | `easy,easy,easy,easy,easy` → FAIL | `easy,easy,easy,easy,hard` → PASS | hard helps |
> | `categorical_lenses` | `easy,easy` → PASS | `easy,hard` → FAIL | hard hurts |
> | `moco` | `easy,easy,easy,easy,easy,easy` → PASS | `easy,easy,easy,easy,easy,hard` → FAIL | hard hurts |
> | `monadic_reward` | `easy,easy` → PASS | `easy,hard` → FAIL | hard hurts |
> | `tensor_functor` | `easy,easy` → PASS | `easy,hard` → FAIL | hard hurts |
>
> *Each row is a pair of cases from the same environment family where every difficulty dimension is identical except the last, which is flipped from `easy` to `hard`. Five of the nine verdict-changing flips go the "wrong" way: the easy case fails and the hard case passes. Four go the expected way. The direction is a property of the environment, not of the label.*

Five pairs where hard passes and easy fails. Four pairs where easy passes and hard fails. If I had been handed the environment name and the fact that the flip changed the verdict, and asked to guess which direction, I would have been slightly better off guessing "hard helps" than "hard hurts." That is not what a difficulty predictor is supposed to look like.

I want to sit with the five counterintuitive rows for a moment, because they are the whole reason this post exists. In `css_state_machine`, the all-easy case failed and the case with one hard dimension passed. Same for `compositional_optimizer`, `functorial_augmentation`, and `sheaf_schema_sync`. In `rd_adaptive_halting` the string is five dimensions long, four held at `easy`, and flipping only the fifth to `hard` moved the verdict from `FAIL` to `PASS`. These are not edge cases from environments that pass everything anyway. `sheaf_schema_sync` passed one case out of five in the whole campaign — and the one it passed was the hard one.

The four intuitive rows deserve equal weight. `categorical_lenses`, `monadic_reward`, and `tensor_functor` all show the two-dimension version of the expected pattern: `easy,easy` passes, `easy,hard` fails. `moco` shows it on a six-dimension string. These are real. Difficulty did something here, in the direction we expected.

So the honest summary of Figure 1 is not "hard doesn't matter." It is "hard matters, in both directions, and the environment decides which."

### The third outcome: nothing changes

There is a third class of pair that Figure 1 cannot show, because it has no verdict change to display: flips where the easy and hard cases get the same verdict.

I cannot enumerate those pairs from the counts I have, but I can bound them. Fourteen of the 33 environment families have zero `FAIL` verdicts across every case they contain (`architecture_naturality`, `ci_dependency_graph`, `epistemic_games`, `equivariant_diagram`, `rd_gradient_credit`, `rd_state_carry`, `semiring_unification`, `sheaf_invariant_gluing`, `spreadsheet_dataflow`, `ssm_parallel_scan`, `stochastic_monad`, `template_interpreter`, `tokenizer_adjunction`, `transformer_ssm_lift` — 84 passes between them). Six more have zero `PASS` verdicts (`batchnorm_ema`, `glyph`, `gnn_message_passing`, `sheaf_physical_constraints`, `ts_one_step`, `ts_trajectory` — 34 fails plus the paused case). That is 20 of 33 environments in which every scored case landed on the same side.

Any easy→hard pair that lives inside one of those 20 environments is, by construction, a no-change pair. I do not know how many such pairs exist, because I have not broken those environments down by difficulty string. But I know that whatever difficulty labels those 118 cases carry, flipping among them never moved a verdict, because there was no other verdict to move to.

That gives us the full menu. Flip the last dimension from easy to hard and one of three things happens: the verdict goes from pass to fail (four observed pairs), the verdict goes from fail to pass (five observed pairs), or the verdict stays where it was (an unknown but non-trivial number of pairs, concentrated in the 20 single-verdict environments). "Hard" does not pick out one of those three outcomes.

### The pooled count, and what it costs to quote it

There is a cruder way to ask the question: ignore environments entirely and just split cases by whether their difficulty string contains `hard` anywhere.

- Cases with at least one `hard` dimension: 53 `PASS`, 20 `FAIL` — a pass rate of 0.726.
- Cases with no `hard` dimension: 78 `PASS`, 42 `FAIL` — a pass rate of 0.650.

Cases that contain "hard" pass more often than cases that do not.

I quote this number because it is the one people will ask for, and because it points the same direction as Figure 1. But I need to be clear about what it is. These 193 cases span both judge-guarantee buckets — the 72 validated behavioral-reference verdicts and the 121 exploratory compile-only verdicts. The split by `hard` is therefore a descriptive count of verdict labels across the whole scored set. It is not a validated model pass rate, and it should not be cited as one. I do not have the per-bucket breakdown of the `hard` split, so I cannot tell you whether the 0.726-versus-0.650 gap survives restriction to the 72 gated cases. It might. It might reverse. The pooled number cannot settle that.

What the pooled count can do is rule out the strong version of the original prediction. If "hard" were a reliable failure predictor, you would expect it to show up even in a crude pooled split. It does not. The sign is wrong.

It is also worth saying what the pooled count does not do: it does not show that hard makes tasks easier. The gap is 0.076 on a single seed per cell with no confidence intervals, and it is computed across environments with wildly different base rates. Environment composition alone could produce it. The pooled number is a sanity check on the within-environment pairs, not an independent finding.

### Verdict is not score

One more thing the counts make visible, because it affects how you should read `FAIL`.

The campaign reports both a binary verdict and a numeric score per case, and the two can come apart. `gnn_message_passing` is 0 `PASS`, 5 `FAIL`, and yet its score is 0.417. `batchnorm_ema` is 0 for 11 with a score of 0.086. `ts_one_step` is 0 for 3 at 0.333. Some `FAIL` verdicts in the campaign carry partial-credit scores as high as 0.95.

I have been working with verdicts throughout, because the question I asked is about verdicts: does flipping to `hard` make the case fail. But a `FAIL` at 0.95 and a `FAIL` at 0.0 are very different outcomes, and the nine pairs in Figure 1 are reported at the verdict level only. It is possible that some of the counterintuitive flips are near-misses on the easy side — a 0.95 `FAIL` turning into a `PASS` — rather than a clean reversal. I do not have the per-case scores for those pairs, so I cannot say. The verdict-level finding stands; the score-level story might be softer or sharper, and I will not guess which.

### What the evidence establishes

I think the following claims are supported, and I would defend each of them with the specific rows above.

1. **Flipping the last difficulty dimension from `easy` to `hard` does not reliably produce a failure.** Of nine within-environment pairs where the flip changed the verdict, five went fail→pass and four went pass→fail.
2. **In some environments, `hard` makes failure more likely.** `categorical_lenses`, `moco`, `monadic_reward`, `tensor_functor`.
3. **In other environments, `hard` makes failure less likely.** `css_state_machine`, `compositional_optimizer`, `functorial_augmentation`, `sheaf_schema_sync`, `rd_adaptive_halting`.
4. **In at least 20 of 33 environments, no flip could have changed the verdict,** because every scored case in those environments landed on the same side.
5. **Pooled across both judge buckets, cases containing `hard` passed more often than cases without it** — 0.726 versus 0.650 — with the caveat that this is a descriptive count over mixed-guarantee verdicts, not a validated rate.
6. **The direction of the effect is a property of the environment family, not of the label.**

### What the evidence cannot establish

The limits are at least as important as the findings, and I want to state them as plainly.

**It does not show that difficulty is irrelevant.** Four pairs went the expected way. In `moco`, five easy dimensions plus one hard one was enough to turn a pass into a fail. Difficulty has not been ruled out as a factor; it has been ruled out as a *reliable* one.

**It does not show that difficulty helps.** Five counterintuitive pairs out of nine is not a general rule. It is a demonstration that the rule does not run the other way either. If I had found nine fail→pass pairs and zero pass→fail, I would be writing a different and much stranger post. I did not.

**It does not explain why.** I have no account of why `sheaf_schema_sync` passes its hard case and fails its easy one, or why `tensor_functor` does the opposite. Nothing in this dataset reaches inside the model, and I am not going to speculate about what the difficulty dimensions are doing to its processing. The honest statement is that the environment family determines the sign of the effect, and the reason is outside the scope of what was measured.

**It does not license general prescriptions.** This is one campaign, one provider, one input modality, one seed per cell. I am not going to tell you how to build your benchmark on the basis of nine pairs.

### Limitations

- **Single provider, single modality.** Every case ran on `atria` with text-only input. A different provider or modality could produce a different pattern — including, possibly, the intuitive one.
- **Single seed per cell.** No confidence intervals are possible. Each of the nine pairs is a single comparison, and a flaky case on either side would flip its row.
- **Only the last dimension was varied.** The pairs hold all other dimensions at their values and flip the final one. I cannot say whether flipping the first dimension, or two at once, behaves the same way.
- **Judge guarantee is mixed.** 122 of the 194 cases are compile-only and carry exploratory verdicts. I do not have the gated/compile-only split for the nine pairs, so I cannot say how many of them rest on validated verdicts.
- **Partial credit is invisible at the verdict level.** Some `FAIL` verdicts carry scores of 0.95, 0.714, 0.5, 0.417, 0.286, 0.278, or 0.208. A verdict flip may conceal a near-miss rather than a reversal.
- **The no-change class is bounded, not counted.** I know 20 environments could not show a flip effect; I do not know how many easy→hard pairs they actually contain.

### Conclusion

I started with a prediction that felt too obvious to test: turn the difficulty dial up, and the model fails more. The within-environment pairs say the dial does not turn that way. Five flips to `hard` rescued a failing case. Four sank a passing one. Across most of the campaign, the flip would not have moved anything.

What this leaves me with is not "difficulty is meaningless" but something more specific and, I think, more useful: the label `hard` on its own does not tell you whether a case will fail. The environment family does most of the work. `sheaf_schema_sync` fails almost everything, `rd_gradient_credit` passes everything, and inside the mixed environments the difficulty label points whichever way that environment happens to point.

If you want to know whether a model will pass a case, the question "is it hard?" is not enough. You have to ask what environment it lives in. In this campaign, at least, that is where the answer was.


&&&&&&&&&&&&&&&&

opus 5.5:

---
title: 'Does "Hard" Make Tasks Harder?'
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic Status**
- **Original ideas:** 4/10 (Mostly a careful reading of outcome patterns in one campaign. The question isn't new.)
- **Synthesis:** 7/10 (Combines per-environment results, matched easy-vs-hard pairs and one aggregate split into a single argument.)
- **Prose:** 8/10 (First person, kept close to the counts.)
- **Certainty:** High on the reported counts. Moderate on the narrow thesis. Low on anything beyond this one campaign.
- **Importance:** 6/10 (Matters if you use difficulty labels as a stand-in for how likely a model is to fail.)

***

I came into this analysis with an assumption I had never really checked. When a reasoning benchmark tags a case as "hard," I took that to mean the model is more likely to fail it. Difficulty works like a dial: turn it up and the pass rate goes down. Most of us build benchmarks this way. We add constraints, deepen the inference chain, make the structure more tangled, and expect the scores to fall.

So here's the question. **If you take a case and flip one of its difficulty dimensions from "easy" to "hard," leaving everything else the same, does the model fail more often?**

I looked at this using the `atria_covering_campaign`, a run of 194 cases across 33 environment families. Every case has a difficulty string, which is a list of dimension values, each one easy, medium or hard. I expected to find at least a rough downward slope. What I found was messier. In some families, "hard" goes along with failure. In others it goes along with *success*. And when I group cases simply by whether they contain "hard" at all, the hard group comes out ahead.

Before getting to that, I need to set out what kind of evidence this is, because the dataset is split in a way that limits what can be claimed.

### Two kinds of verdict

The campaign recorded 194 cases, and they don't all carry the same guarantee.

**Behavioral-reference cases (72).** These were judged against a behavioral reference on the exact instance the model saw. That's the strict guarantee. These are the only verdicts I'd call validated. Of the 72, **56 passed and 16 failed**.

**Compile-only cases (122).** These were graded by judges that had no behavioral reference for that exact instance. They don't carry the exact-instance oracle guarantee, so they shouldn't be read as validated model verdicts. They're exploratory signal. Of the 122, **121 were scored (75 passed, 46 failed)**, and one case is marked `paused_provider_error`.

I won't combine these into a single pass rate. Adding 56 to 75 and calling it the model's score would put validated and exploratory results on the same footing, and they aren't.

A brief note on that one unscored case. The campaign is formally paused after a provider outage. The provider was unavailable for about 55 minutes (3300 seconds) across 8 retries, with a final backoff of 600 seconds, and the case in flight at that point was never scored. That's the only reason one of the 194 has no verdict. All the episodes in the manifest ran, and the outage has nothing to do with the question here.

### A first look by environment

Before getting to difficulty, it's worth seeing how widely the 33 families vary on their own. Pooling both buckets, and **for description only**, here are the extremes:

- Thirteen families passed every case. `rd_gradient_credit` and `rd_state_carry` went 11/11, `epistemic_games` went 7/7, and ten more went 5/5.
- Five families passed nothing. `batchnorm_ema` went 0 for 11, `glyph` 0 for 8, `gnn_message_passing` and `sheaf_physical_constraints` 0 for 5 each, and `ts_one_step` 0 for 3.
- The rest fall in between: `moco` 9–2, `rd_adaptive_halting` 9–2, `monadic_reward` 1–4, `sheaf_schema_sync` 1–4, `tensor_functor` 2–3.

So the family a case belongs to already says a lot about how it will turn out. The question is whether the difficulty label adds anything once you account for the family.

### The aggregate looks backwards

The simplest test splits cases by whether their difficulty string contains at least one "hard":

| Group | PASS | FAIL | Pass rate |
|---|---|---|---|
| At least one "hard" dimension | 53 | 20 | 0.726 |
| No "hard" dimension | 78 | 42 | 0.650 |

If "hard" predicted failure, the top row should have the lower pass rate. It has the higher one.

I don't want to make too much of this table, and I have three reasons.

First, it's computed over all 193 scored cases, which means it **mixes the behavioral-reference and compile-only buckets**. I only have this split in pooled form. So it's a descriptive pattern in mixed-guarantee data, not a validated aggregate, and I can't tell you whether it holds within the validated bucket alone.

Second, a gap of 0.076 between two groups from a single seed per cell, with no confidence intervals, isn't something I'd stake much on.

Third, and most important, the aggregate can be skewed by *which families* end up in each group. Families have different numbers of difficulty dimensions (some cases carry two, others five or six), so some families have more chances to include a "hard" somewhere. If those families also happen to be ones the model does well on, the hard group would look better without "hard" helping anything. I haven't broken this down by family composition, so I'm raising it as a possibility, not stating it as the explanation.

All of which means the aggregate is suggestive at most. It would be easy to misread "hard cases pass more often" as "hardness helps," and the table can't support that. What it does show is that, at the coarsest level, there's no sign of the dial working as expected.

To get past the confound of which family a case comes from, I need comparisons *inside* a single family.

### Matched pairs: same family, one dimension flipped

The cleaner test uses pairs of cases from the same family that are identical in every difficulty dimension except the last, which goes from "easy" to "hard." If the dial idea is right, there's a prediction: when the easy version fails, the hard version shouldn't pass. The hard version might fail too, or the easy version might pass, but the hard case should never do better than its easier twin.

That prediction breaks in five families.

**Hard passes, easy fails:**

- `css_state_machine`: easy,easy = FAIL; easy,hard = PASS
- `compositional_optimizer`: easy,easy = FAIL; easy,hard = PASS
- `functorial_augmentation`: easy,easy = FAIL; easy,hard = PASS
- `sheaf_schema_sync`: easy,easy = FAIL; easy,hard = PASS
- `rd_adaptive_halting`: easy,easy,easy,easy,easy = FAIL; easy,easy,easy,easy,hard = PASS

And it holds in four families.

**Easy passes, hard fails:**

- `categorical_lenses`: easy,easy = PASS; easy,hard = FAIL
- `moco`: easy,easy,easy,easy,easy,easy = PASS; easy,easy,easy,easy,easy,hard = FAIL
- `monadic_reward`: easy,easy = PASS; easy,hard = FAIL
- `tensor_functor`: easy,easy = PASS; easy,hard = FAIL

<br>

> **Figure 1: One flip, two directions**
>
> | Environment family | Dims | All-easy | Last dim → hard | Direction |
> |---|---|---|---|---|
> | `css_state_machine` | 2 | FAIL | PASS | hard did better |
> | `compositional_optimizer` | 2 | FAIL | PASS | hard did better |
> | `functorial_augmentation` | 2 | FAIL | PASS | hard did better |
> | `sheaf_schema_sync` | 2 | FAIL | PASS | hard did better |
> | `rd_adaptive_halting` | 5 | FAIL | PASS | hard did better |
> | `categorical_lenses` | 2 | PASS | FAIL | hard did worse |
> | `moco` | 6 | PASS | FAIL | hard did worse |
> | `monadic_reward` | 2 | PASS | FAIL | hard did worse |
> | `tensor_functor` | 2 | PASS | FAIL | hard did worse |
>
> *Matched within-family pairs where only the last difficulty dimension changes from easy to hard. In five families the flip goes with a FAIL becoming a PASS. In four it goes with a PASS becoming a FAIL. Each row is one pair from a single seed. The verdicts in this table are pooled across judge-guarantee buckets and shouldn't be read as validated verdicts unless the underlying cases are behavioral-reference cases. The figure shows that the direction isn't consistent. It doesn't show how big any effect is.*

<br>

That's the core of the post. The same move, easy to hard on the last dimension with everything else fixed, goes with failure in some families and with success in others. Five go one way and four go the other. On these pairs, knowing that a dimension went to "hard" doesn't tell you which way the verdict moved.

### And sometimes nothing changes

The third outcome, no change at all, is easy to miss because it doesn't show up as an interesting pair. But it follows directly from the per-family results. Thirteen families passed every case and five failed every case. If any of those families has a matched easy-vs-hard pair, the two verdicts have to be the same: PASS/PASS in `rd_gradient_credit` or `epistemic_games`, FAIL/FAIL in `batchnorm_ema` or `glyph`. In those families the difficulty flip makes no visible difference to the binary verdict, because the family has already settled the outcome.

I'll be precise about what that inference covers. I'm reasoning from the family totals, not from a list of unchanged pairs, so the claim is conditional: *wherever* such pairs exist in those families, they can't show a change. That's enough to show that "no change" is a real third outcome next to the other two, and not a rare one.

### Where my reading needed correcting

When I first lined up the five counterintuitive pairs against the four intuitive ones, I briefly started telling myself a story: maybe "hard" helps more often than it hurts. That's the wrong lesson. Five against four is close to a coin flip, it rests on one seed per cell, and the five aren't a sample from anything bigger. They're the pairs this campaign happened to produce. Reading them as "hard makes things easier" would repeat the original mistake in reverse, swapping one universal slope for another.

I also caught myself treating each pair as a clean experiment. It isn't, quite. A few things get in the way:

- **Partial credit sits behind the binary verdicts.** Some FAIL verdicts in this campaign carry non-zero scores (values such as 0.95, 0.714, 0.5, 0.417, 0.286, 0.278 and 0.208 appear). A flip from FAIL to PASS might be a big jump or a small move across a threshold. `css_state_machine`, for example, went 3–2 on verdicts with a family score of 0.683. That's consistent with near-misses, but I can't tell from the summary which pair cases scored what. The binary flip is real, but how large it is remains unknown.
- **Only the last dimension is flipped.** No dimension other than the last was varied on its own in these pairs, so I can't say whether flipping the first dimension, or two at once, would behave the same way.
- **"Hard" doesn't mean the same thing across families.** The last dimension of `moco` (one of six) and the last dimension of `tensor_functor` (one of two) are different knobs on different tasks. Calling both "hard" is a labeling convention, not a shared unit. That's part of why I'm wary of comparing pairs across families at all.

### What the evidence establishes

Holding to what the data actually supports, here's what I'm prepared to say:

1. **Flipping a difficulty dimension from easy to hard doesn't reliably produce a failure in this campaign.** Within the same family, with the other dimensions fixed, the flip went with pass→fail in four families, fail→pass in five, and, by inference from families with uniform results, no change wherever such pairs exist.
2. **There are matched pairs where hard passes and easy fails:** `css_state_machine`, `compositional_optimizer`, `functorial_augmentation`, `sheaf_schema_sync` and `rd_adaptive_halting`.
3. **There are matched pairs where easy passes and hard fails:** `categorical_lenses`, `moco`, `monadic_reward` and `tensor_functor`.
4. **In the pooled, mixed-guarantee data, cases containing "hard" passed more often** (0.726) than cases without it (0.650). That's a descriptive pattern, not a validated aggregate.
5. **Family membership tells you more than the label.** Thirteen families passed everything and five failed everything, regardless of the difficulty strings inside them.

### What it can't establish

The other half matters just as much.

**It doesn't show that difficulty is irrelevant.** Four families show the intuitive direction. In `categorical_lenses`, `moco`, `monadic_reward` and `tensor_functor`, the hard twin failed where the easy one passed. Difficulty hasn't been ruled out as a factor. It just isn't a reliable *one-way* predictor.

**It doesn't show that "hard" makes tasks easier.** The direction isn't consistent across families, the counts are small, and the aggregate that seems to favor "hard" is mixed-guarantee and open to composition effects.

**It doesn't explain the inconsistency.** I have no causal account of why a flip goes one way in `sheaf_schema_sync` and the other way in `monadic_reward`. The data records inputs and verdicts, nothing about what happens in between, and I'm not going to invent a story about model internals to fill the gap.

**It doesn't validate the pair verdicts beyond their bucket.** The pair verdicts are reported pooled across both buckets. Any pair whose cases are compile-only is exploratory evidence, not a validated model verdict.

**It doesn't generalize past this campaign.** One provider (`atria`), text-only input, a single seed per selected cell, and no confidence intervals. A different provider, a different modality or more seeds could change any individual pair.

### Limitations, gathered in one place

- Single provider, text-only modality.
- One seed per selected cell, so there's no estimate of verdict variance and no confidence intervals.
- 122 of 194 cases are compile-only. Their verdicts are exploratory.
- The hard/no-hard aggregate and the pair verdicts are pooled across judge-guarantee buckets, and I don't have the per-bucket breakdown for them.
- Matched pairs only vary the last difficulty dimension.
- Binary verdicts hide partial credit, so the size of a flip is unknown.
- One case went unscored because of a provider error during the pause. It doesn't affect any of the pairs discussed here.

### Conclusion

I started with a simple picture: turn difficulty up and the pass rate goes down. Within this campaign, that picture doesn't hold. The same easy→hard flip, with everything else fixed, went with failure in four families, with success in five, and with no visible change wherever a family's outcome was already uniform. And the crudest aggregate, hard versus no hard, points the "wrong" way, though in data too mixed to put weight on.

The narrow conclusion is the one I trust: **in this campaign, the label "hard" isn't a reliable predictor of failure.** It sometimes lines up with failure, sometimes with success, and sometimes with nothing. Which of those you see depends on the environment family, and this dataset can't tell me why. I'll stop there and not draw a general lesson about benchmark design.

What I'll take into the next analysis is a habit more than a rule. Before reading a FAIL as "the task was too hard," I'll check whether its easy twin in the same family actually passed. In this campaign, it often didn't.
