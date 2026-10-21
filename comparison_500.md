fable 5.1:

---
title: "Does Hard Make Tasks Harder?"
date: 2026-10-21
layout: post
---

_by StrangeTcy_

**Epistemic Status**
- **Original ideas:** 4/10 (The question is old; the within-environment pairing is the only new move.)
- **Synthesis:** 7/10 (Pulls case-level verdicts from one campaign into matched easy-vs-hard pairs and reads them against the aggregate.)
- **Prose:** 8/10 (First-person, analytical, with caveats placed next to the claims they qualify.)
- **Certainty:** High on the counts reported here; low on anything that generalizes past this one campaign, one provider, one modality.
- **Importance:** 6/10 (If "hard" labels do not predict failure within an environment, they are a weaker instrument than most benchmark designs assume.)

***

I want to start with the assumption I had going in, because the whole point of this post is that I had to give it up.

When you build a reasoning benchmark, you usually build in a difficulty axis. Each case carries a string of dimension values — `easy,easy`, `easy,hard`, `easy,easy,easy,easy,hard` — and the implicit model is that each dimension is a dial. Turn one from easy to hard and the case gets harder. Turn several and it gets harder still. Pass rates should slope downward as you turn, and the shape of that slope is supposed to tell you something about how much reasoning the model can sustain before it breaks.

That is a clean picture. It is also a testable one, and I had a dataset where I could test it directly: a campaign of 194 cases across 33 environment families, every case tagged with a difficulty string, every scored case carrying a PASS or FAIL verdict. If the dial works, then within a single environment, holding every dimension fixed except one and flipping that one from easy to hard should push cases from PASS toward FAIL. It should never push them the other way.

It pushes them the other way about as often as it pushes them the expected way.

### The dataset, and the line I will not cross

Before the difficulty question, a word on what the 194 cases [ac-word] are, because the campaign records two kinds of verdict and they are not interchangeable.

Some cases were graded against a behavioral reference — an exact-instance oracle for that specific case. These are the validated verdicts. There are 72 of them: 56 PASS, 16 FAIL.

The rest were graded compile-only. The judge had no behavioral reference on that exact instance, so the verdict reflects what the judge could establish without one. These are exploratory. They are not validated model verdicts and I will not treat them as such. There are 122 compile-only cases: 121 scored (75 PASS, 46 FAIL) and one that never received a verdict because the campaign paused on a provider error while it was in flight. The outage lasted about 55 minutes with 8 retries before the run paused in a resumable state. That is the only reason the campaign is 194 cases and not more, and it is the last I will say about it — the pause does not touch any of the scored cases, and this post is not about the pause.

The important discipline is that I will not add 56 + 75 and call it a pass rate. The two buckets carry different guarantees, and a single blended number would quietly launder exploratory signal into validated signal. Where I do pool cases below — and I do, once, for a descriptive tally — I say so and I say what the number can and cannot bear.

### First look: the aggregate goes the wrong way

The cheapest test of the dial is to split all scored cases by whether their difficulty string contains at least one `hard` and compare pass counts. Across the 193 scored cases:

- Cases with at least one `hard` dimension: PASS=53, FAIL=20. That is a pass fraction of 0.726.
- Cases with no `hard` dimension at all: PASS=78, FAIL=42. That is a pass fraction of 0.650.

Cases containing `hard` passed more often than cases that did not.

Two caveats belong directly beside that result, not in a footnote. First, this tally pools gated and compile-only verdicts, so it is a descriptive count over the whole campaign, not a validated aggregate — read it as a sanity check on direction, not as a measurement with a guarantee attached. Second, it is confounded by environment: environments differ enormously in their pass rates (several are 5/5 or 11/11 PASS; `glyph` is 0/8 and `batchnorm_ema` is 0/11), and if `hard`-tagged cases happen to concentrate in easier environments, the aggregate would tilt upward for reasons that have nothing to do with the dial.

So the aggregate is suggestive and nothing more. It told me the naive picture was in trouble, but it could not tell me why. For that I had to go inside environments.

### Second look: matched pairs inside a single environment

The right comparison is the one a controlled experiment would make. Take two cases from the same environment family whose difficulty strings are identical except for the last dimension — easy in one, hard in the other — and compare their verdicts. The environment is held fixed, the other dimensions are held fixed, and the only thing that moved is the dial.

Under the naive picture there is exactly one permitted kind of disagreement between the two verdicts: easy PASS, hard FAIL. The reverse — easy FAIL, hard PASS — should not occur. If it does, the dial is not doing what the label says.

The campaign records nine such pairs where the verdict changed between easy and hard. They split almost evenly.

**Easy passes, hard fails** — the direction the dial is supposed to turn:

- `categorical_lenses`: `easy,easy` = PASS, `easy,hard` = FAIL
- `moco`: `easy,easy,easy,easy,easy,easy` = PASS, `easy,easy,easy,easy,easy,hard` = FAIL
- `monadic_reward`: `easy,easy` = PASS, `easy,hard` = FAIL
- `tensor_functor`: `easy,easy` = PASS, `easy,hard` = FAIL

**Easy fails, hard passes** — the direction the dial is not supposed to turn:

- `css_state_machine`: `easy,easy` = FAIL, `easy,hard` = PASS
- `compositional_optimizer`: `easy,easy` = FAIL, `easy,hard` = PASS
- `functorial_augmentation`: `easy,easy` = FAIL, `easy,hard` = PASS
- `sheaf_schema_sync`: `easy,easy` = FAIL, `easy,hard` = PASS
- `rd_adaptive_halting`: `easy,easy,easy,easy,easy` = FAIL, `easy,easy,easy,easy,hard` = PASS

Four pairs in the intuitive direction. Five in the counterintuitive direction. Same environment, same other dimensions, one label flipped.

And there is a third category that the nine pairs leave out but the environment table makes visible. Several families pass everything — `rd_gradient_credit` (11/0), `rd_state_carry` (11/0), `epistemic_games` (7/0), and a run of 5/0 environments including `architecture_naturality`, `ci_dependency_graph`, `semiring_unification`, `spreadsheet_dataflow`, and `tokenizer_adjunction`. Others fail everything — `glyph` (0/8), `batchnorm_ema` (0/11), `gnn_message_passing` (0/5), `sheaf_physical_constraints` (0/5). Whatever mix of difficulty labels those environments contain, no easy→hard flip inside them changed a verdict, because there was no verdict variation to change. In those families the dial, whatever it is labeled, turned nothing.

<br>

> **Figure 1. Within-environment easy→hard flips, by direction of verdict change.**
>
> | Direction of change | Environment | Easy string → verdict | Hard string → verdict |
> |---|---|---|---|
> | PASS → FAIL (intuitive) | `categorical_lenses` | `easy,easy` → PASS | `easy,hard` → FAIL |
> | PASS → FAIL (intuitive) | `moco` | `easy,easy,easy,easy,easy,easy` → PASS | `easy,easy,easy,easy,easy,hard` → FAIL |
> | PASS → FAIL (intuitive) | `monadic_reward` | `easy,easy` → PASS | `easy,hard` → FAIL |
> | PASS → FAIL (intuitive) | `tensor_functor` | `easy,easy` → PASS | `easy,hard` → FAIL |
> | FAIL → PASS (counterintuitive) | `css_state_machine` | `easy,easy` → FAIL | `easy,hard` → PASS |
> | FAIL → PASS (counterintuitive) | `compositional_optimizer` | `easy,easy` → FAIL | `easy,hard` → PASS |
> | FAIL → PASS (counterintuitive) | `functorial_augmentation` | `easy,easy` → FAIL | `easy,hard` → PASS |
> | FAIL → PASS (counterintuitive) | `sheaf_schema_sync` | `easy,easy` → FAIL | `easy,hard` → PASS |
> | FAIL → PASS (counterintuitive) | `rd_adaptive_halting` | `easy,easy,easy,easy,easy` → FAIL | `easy,easy,easy,easy,hard` → PASS |
>
> *Each row is a pair of cases from the same environment family with identical difficulty strings except for the final dimension. Four flips move a case from PASS to FAIL, as the difficulty label would predict. Five move a case from FAIL to PASS, which the label cannot explain. Environments that pass or fail uniformly (not shown) contribute flips with no change at all. Pairs may include compile-only verdicts, which are exploratory; see Limitations.*

<br>

### Checking myself

When I first saw the five counterintuitive pairs I assumed I had misread the difficulty strings — maybe the hard case was in a different environment, or the other dimensions were not [ac-word] held constant. They are, and they were. The pairing rule is strict: same family, same string except the last position.

The second thing I checked was whether the counterintuitive pairs were all living in low-pass-rate environments where verdicts are noisy anyway. Some are: `sheaf_schema_sync` is 1/5 overall, `functorial_augmentation` is 2/5, `compositional_optimizer` and `css_state_machine` are 3/5. But `rd_adaptive_halting` is 9/11, one of the stronger families in the campaign, and its flip still went the wrong way. Meanwhile the intuitive pairs are not confined to strong environments either: `monadic_reward` is 1/5 and `tensor_functor` is 2/5, and both produced the textbook PASS→FAIL. There is no clean split where the dial works in good environments and misfires in bad ones.

The third thing I checked was whether partial credit was hiding something. Some FAIL verdicts in this campaign carry non-zero scores — values like 0.95, 0.714, 0.5, 0.417 appear — so a FAIL is not always a blank. This matters for the per-environment score column (which is why `gnn_message_passing` can be 0/5 on verdicts and 0.417 on score), but it does not rescue the dial. The pair analysis is on verdicts, and the verdicts flipped. A FAIL at 0.95 and a FAIL at 0.0 are both FAIL for the purposes of asking whether "hard" predicts failure.

Having checked those three things, I am left with the result as stated: within a single environment, holding everything else fixed, flipping the last dimension from easy to hard produced a failure in four pairs, produced a pass in five pairs, and produced nothing in the uniform environments.

### What the evidence establishes

I want to be precise about the claim, because it is narrow and it is easy to overstate.

**Established:** Flipping a difficulty dimension from `easy` to `hard` does not reliably produce a failure. Within the same environment family, with all other dimensions held constant, the campaign contains easy→hard flips that go PASS→FAIL (four), flips that go FAIL→PASS (five), and flips that change nothing. "Hard," as a label, is not a reliable predictor of failure in this dataset.

**Established:** The direction of the effect varies by environment family. The same operation — flip the last dimension — helped in `css_state_machine`, `compositional_optimizer`, `functorial_augmentation`, `sheaf_schema_sync`, and `rd_adaptive_halting`, and hurt in `categorical_lenses`, `moco`, `monadic_reward`, and `tensor_functor`. Knowing which environment you are in tells you more about which way the flip will go than the label does.

**Established, with the pooling caveat:** Across all 193 scored cases, those containing at least one `hard` dimension passed at 0.726 and those with none passed at 0.650. This pools the validated and exploratory buckets and is confounded by environment composition, so it is a direction check rather than a measurement.

### What the evidence cannot establish

**Not established: that difficulty dimensions do not matter.** Four flips went exactly the way the label predicts. `moco` is 9/11 overall and its one hard-flipped case failed. `categorical_lenses` is 4/5 and the flip found the one failure. Difficulty labels are doing something in those families; the problem is that they are not doing the same thing everywhere.

**Not established: that "hard" makes tasks easier.** Five counterintuitive pairs against four intuitive ones is not a trend, it is a near-even split, and the aggregate tilt toward `hard`-tagged cases is confounded. If I had seen nine FAIL→PASS pairs and zero PASS→FAIL I would be writing a different post. I did not see that.

**Not established: why.** I have verdicts and labels. I do not have anything that would let me say what about an `easy,hard` case in `sheaf_schema_sync` made it tractable when `easy,easy` was not, or what about `easy,hard` in `monadic_reward` made it fail. It would be easy to reach for stories here — that "hard" variants add structure that constrains the search, or that "easy" variants are underspecified — and every such story would be invented. The data does not contain a mechanism and I am not going to supply one.

**Not established: anything prescriptive beyond this campaign.** This is one provider, one input modality, one seed per cell. Whether this pattern holds for a different model or a different family of environments is an open question that this dataset cannot answer. The most I will say is that if you are reading pass rates sliced by difficulty label and treating the slope as meaningful, this is one concrete instance where that slope would have misled you.

### Limitations

The campaign used a single provider, `atria`, in text-only modality. Nothing here speaks to other providers or modalities.

Each selected cell ran once. There are no repeated seeds, so there are no confidence intervals, and any individual verdict could be sensitive to sampling in ways I cannot measure. A flip that reads as FAIL→PASS on one seed might not replicate on another. This cuts both ways — the intuitive pairs are equally single-seed — but it means every pair should be read as one observation, not as a settled fact about that environment.

The within-environment pairs vary only the last difficulty dimension. The other dimensions were held constant across each pair but were not independently varied, so I cannot say whether flipping an earlier dimension would behave the same way.

Of the 194 cases, 122 are compile-only: 121 scored without a behavioral reference and one unscored at the pause. Compile-only verdicts are exploratory. The pair-level results above are drawn from the campaign's case-level verdicts without regard to bucket, and from the summary I am working from I cannot assign each pair cleanly to the gated or compile-only bucket, so the pairs inherit the compile-only caveat wherever it applies. The 72 gated cases (56 PASS, 16 FAIL) are the only validated verdicts in the campaign.

Partial credit exists. Some FAIL verdicts carry scores well above zero, so per-environment score and per-environment verdict count can diverge. The pair analysis uses verdicts only.

### Conclusion

I went in expecting that "hard" would be a dial, and that turning it would push cases from PASS to FAIL in a direction I could count on. Inside this campaign, it is not a dial. It is a label whose effect depends on which environment the case lives in: in four families it did what it said, in five it did the opposite, and in the uniform families it did nothing at all.

That is a narrow finding and I want to keep it narrow. It does not say difficulty is irrelevant — it plainly is not in `moco` or `monadic_reward`. It does not say hard is secretly easy. It does not say why the split exists. What it says is that if your question is "will this case fail?", the answer "it's tagged hard" is not a reliable one. You have to ask which environment the case is in first, because in this dataset the environment decides what "hard" means — and sometimes it decides that "hard" means nothing at all.

&&&&&&&&&&&&&&&&&&

gpt 6.1 sol max:

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

The 72 `behavioral_reference` cases carry the campaign’s strict, exact-instance oracle guarantee. These are the validated verdicts under that gate.

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
<figcaption><strong>Figure 1. The same difficulty-label change accompanies opposite verdict changes.</strong> All non-final difficulty coordinates remain fixed at easy. These are the nine listed discordant pairs, not a complete count of all matched pairs. The available pair summary does not specify each case’s judge guarantee; the plotted outcomes are recorded verdicts, not a claim that every comparison is oracle-validated.</figcaption>
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

There is also an important resolution limit here. “Unchanged” means unchanged **verdict**, not necessarily unchanged performance on every measure.

Some failures in the campaign receive nonzero partial-credit scores, including scores such as 0.95 and 0.5. Two cases labeled `FAIL` therefore need not have performed equally well. Conversely, a verdict transition does not by itself tell me the size of the numerical score change.

This essay concerns the ordering of binary verdicts. It does not establish that every stable verdict represents identical performance, or that every changed verdict represents a large deterioration or improvement.

## The aggregate reversal—and why I do not turn it into a validated rate

The campaign summary contains another counterintuitive observation: among scored cases, the group containing at least one `hard` dimension has a higher recorded pass share than the group containing no `hard` dimension.

That is the reported direction of the pooled difficulty comparison. It is not a validated aggregate result.

The comparison combines `behavioral_reference` and `compile_only` verdicts. Reproducing its pooled pass rates as model-success rates would cross the judge-guarantee boundary established above. I therefore do not report those combined rates or use the pooled reversal to strengthen the oracle-supported evidence.

The missing information is the intersection of difficulty status and judge guarantee. The summary supplies totals by guarantee and a separate pooled difficulty comparison. It does not supply the `hard`-containing and no-`hard` counts separately inside each guarantee bucket.

Consequently, I cannot determine from these summaries whether hard-containing cases pass more often within `behavioral_reference`, within `compile_only`, within both, or within neither. The pooled direction alone does not answer those questions.

Even apart from the guarantee problem, this aggregate comparison asks a different question from the matched pairs.

“No `hard` dimension” is not synonymous with “all dimensions easy”; it can include medium settings. The groups also contain cases from different environment families, which contribute different numbers of recorded cases. An across-case difference is therefore not equivalent to changing one coordinate while holding the environment and remaining coordinates fixed.

My initial temptation is to treat the aggregate reversal as the headline: hard cases pass more often. On inspection, that is too strong. The defensible account is that the supplied mixed-guarantee tally has that direction, while a guarantee-separated difficulty comparison is unavailable.

The within-environment contrasts remain interesting without borrowing authority from an inadmissible pooled rate.

## How much does “not reliable” [ac-word] mean?

There are several claims I need to keep apart.

**First, the recorded outcomes are not uniformly monotonic in the difficulty label.** The listed pairs establish that directly: the same final-coordinate change accompanies both `FAIL`-to-`PASS` and `PASS`-to-`FAIL` transitions. Other recorded settings retain the same verdict.

**Second, that does not establish that difficulty has zero predictive value.** A probabilistic predictor can have exceptions. Counterexamples to a perfect ordering do not prove the absence of an average relationship.

This is where the opening question needs a careful answer. If “does hard make failure more likely?” means “does every such change worsen the recorded outcome?”, these cases answer no. If it means “what is the change in conditional failure probability?”, the available summaries do not provide a reliable estimate.

I use “not reliable” in the narrower sense: the label alone does not consistently order these observed comparisons. I am not reporting a fitted predictive model, a calibrated failure probability, or a statistical demonstration of no association.

**Third, the direction varies across the listed environment families, but that does not make environment identity a proven replacement predictor.** The record shows heterogeneity. It does not establish that the family name determines what a difficulty change will do.

It would be easy to replace one overstatement with another: first assuming that difficulty controls the outcome, then concluding that environment controls it instead. Neither causal claim follows from this summary.

Several limits keep the interpretation local.

The campaign used one provider and text-only inputs. These observations do not establish the same pattern for another provider or modality.

Each selected cell has a single seed. The record therefore does not characterize run-to-run stability within a cell. I report no confidence intervals or estimates of how often each listed verdict would recur under repeated executions.

The displayed comparisons change only the last difficulty coordinate. They do not test every coordinate independently, and they do not establish what happens when several coordinates change together.

Finally, matching configuration labels is not the same as identifying a causal effect. The summary gives me no basis for explaining why a particular hard-side case passed when its easy-side counterpart failed. I cannot infer a mechanism from the direction of a verdict change.

These limits do not erase the observed contrasts. They determine what those contrasts can support.

## What survives the caveats

The result is smaller than “difficulty does not matter,” but more concrete.

In five listed within-environment comparisons, the hard-side case passes while the easy-side case fails. In four, the easy-side case passes while the hard-side case fails. Other recorded settings retain their verdicts. A separate pooled summary points toward a higher pass share among hard-containing cases, but it mixes judge guarantees and cannot serve as a validated aggregate comparison.

I can therefore reject a simple reading of this campaign in which `hard` consistently pushes recorded outcomes toward failure. I cannot conclude that difficulty is irrelevant, that difficulty helps, or that I know why the contrasts reverse.

For this Atria record, `hard` is an intended setting—not a dependable ordering of observed success and failure. That is the correction I can [d-word] without turning a small empirical inconsistency into a universal theory.
