```markdown
---
title: "The Name of a Task Is Not the Operation It Runs"
date: 2026-10-03
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Low. The central move is a reading discipline, not a new result: separate what a benchmark is called from what its source fuckingly computes.</dd>
  <dt>Synthesis</dt>
  <dd>Medium. I reconcile seven perfect task-level scores with an implementation note that disclaims the capability the task's name implies.</dd>
  <dt>Prose</dt>
  <dd>Drafted and revised in the Arena against a frozen paid-run archive and a clean-source comparator. The comparator is outside the archive ZIP; the campaign repository was recorded dirty, so I argue only to what that evidence licenses.</dd>
  <dt>Certainty</dt>
  <dd>High on the recorded outcomes and the source-described target; low on any generalization beyond seven seed-0 instances.</dd>
  <dt>Importance</dt>
  <dd>Moderate. The error it guards against — promoting a calculation to a cognition — is common and cheap to make.</dd>
</dl>

Here is a small experiment in reading. I will give you a task named `epistemic_games`, tell you it has a condition labeled "strategic," hand you a transcript where a model answers every instance perfectly, and ask what you now believe about that model. If your first instinct is that something was demonstrated about strategic reasoning — about a mind modeling another mind — then the name did its work before the arithmetic got a turn. That is the thing I want to pull apart, because the archive I am looking at contains both the perfect scores *and* a line of source code that declines the interpretation the name invites.

So the question is not "did it pass?" It passed. The question is what the pass is a measurement *of*.

## What the seven cases fuckingly are

The archived Atria-Dawn-Preview run clears all seven selected `epistemic_games` instances, each scored 1.0. In every case the judge records an exact posterior credit, the correct likelihood-ratio verdict, the correct most-supported world, `provenance_ok=true`, and `all_correct=true`. The exact posterior values that show up across the selected set include $1/2$, $3/5$, $1/15$, and $92/177$ — and the reported numbers match the oracle not loosely but at full precision, down to `0.519774` against a true $92/177 \approx 0.5198$.

That is worth stating plainly: on these seven, the model is not approximately right. It reproduces the reference posteriors exactly and attaches the correct discrete labels to them.

But hold the denominators steady. This is seven instances, one seed (seed-0), one model and one configuration. Within those seven there is exactly one `solo` presentation and exactly one `skewed` prior; everything else is `paired` and `balanced`. The axis table sweeps five factors — `evidence`, `framing`, `presentation`, `prior`, `scenario` — but each sweep is a one-factor substitution against a fixed base cell, not an interaction grid and not a population estimate. Seven green cells is a real outcome. It is not a distribution.

## The math is honest; the label is ambitious

Here is what the task computes. The source defines two hypotheses $W_1, W_2$, a prior over them, an observed announcement $o$, and a likelihood table giving $P(o \mid W_i)$ for each stipulated behavior policy. The posterior is the ordinary two-hypothesis Bayes update:

$$
P(W_1 \mid o) = \frac{P(o \mid W_1)\,P(W_1)}{P(o \mid W_1)\,P(W_1) + P(o \mid W_2)\,P(W_2)}
$$

The judge then checks that the submitted number equals this posterior and that the accompanying verdict and most-supported-world label are internally consistent with it. That is a well-specified calculation with a public oracle, and the answers are correct on the selected cases.

Now the part the name hides. The inspected `core.py` says, in its own words, that v0 does **not** implement a fully recursive level-k engine with utilities and recursive belief updates. It supplies the likelihoods directly through an evidence table. Its design description frames the target as Bayesian inference over two specified behavioral policies, dressed in genuine-versus-strategic narratives. The narrative motivates the inference; it does not make the likelihood table an output of the model's own strategic reasoning. The numbers $P(o \mid W_i)$ arrive pre-computed. Nobody in the loop recursively modeled anybody.

I should flag the provenance caveat right next to that, because it is load-bearing. These implementation statements come from the *clean* comparator source. The campaign records `repository.dirty=true`, and the comparator is a snapshot that lives outside the archive ZIP. All 33 selected config hashes match the comparator, which is reassuring — but matching config hashes are not byte-for-byte proof that the exact task, judge, or helper code executed in the paid run is the code I read. So: the source I can inspect disclaims recursion; the source that fuckingly ran is probably the same, but "probably" is the honest word.

With that in hand, the distinction sharpens. A model can compute what an observation implies about two possible worlds without ever representing what one agent believes another agent believes. The first is a conditional-probability update. The second is theory of mind. The task name borrows the connotations of the second to describe an instance of the first.

## The ambiguous case is where the reading gets tested

The most informative cell is the one designed to have no winner. In the ambiguous-evidence condition, both worlds produce the observation with equal likelihood, so the ratio is $1$ and — under a balanced prior — the posterior sits at $1/2$. The correct behavior there is to report non-identifiability, not to pick whichever narrative sounds more convincing. The model does report it: $P(W_1)=0.5$, verdict `indistinguishable`, support `neither`.

Two neighboring cells pressure this from different sides. The `skewed`-prior ambiguous case returns $3/5$ — the likelihoods still cancel, so the posterior is the prior, and the model correctly reports `world1` as better supported while keeping the verdict `indistinguishable`. That pairing matters: it separates "the evidence discriminates" from "my belief leans," which is exactly the confusion a narrative framing is built to induce. And the `trap` scenario — same balanced ambiguous setup, different story wrapper — also returns $1/2$ with `neither`. The wrapper changed; the arithmetic did not; the answer tracked the arithmetic.

On the discriminating end, the `strong` case returns $1/15 \approx 0.0667$ with verdict `distinguishable` and support `world2`, and the `weak` case returns $92/177$ with verdict `weakly_distinguishable`. For these the judge checks the posterior value *and* whether the evidence lands in the right likelihood-ratio band — two guarantees, not one, which is why I keep calling the labels "discrete": they are a separate thing to get right on top of the number.

This is genuinely good behavior on the thing being measured. It is also, precisely, Bayesian inference over stipulated policies. The model resists the narrative pull in the trap case; it does not thereby demonstrate that it modeled a strategist, because there was no strategist to model — only a table.

## Keep the layers of the archive separate

A perfect sub-score is easy to over-read when the surrounding campaign is messy, so it helps to name the layers the seven cases sit inside and keep them from blurring.

First, the scoring-guarantee split. The campaign carries two different guarantee groups, and the report excludes compile-only results from any validated behavioral aggregate. The raw counts: 72 `behavioral_reference` rows at 56 PASS / 16 FAIL, and 122 `compile_only` rows at 75 PASS / 47 FAIL. After dropping two provider-coded terminal rows, compile-only becomes 120 rows (75/45) while behavioral-reference stays at 72 (56/16). All seven `epistemic_games` cases are `behavioral_reference`; none are compile-only. Compile-only outcomes are exploratory probes, not a validated behavioral number, and I am not folding them into the same bucket.

Second, `epistemic_games` is the one environment with an environment-level `public_bayes_oracle` behavioral self-test recorded as executed and passed. That preflight is a *different* mechanism from the exact-instance per-case calibration the judge applies to each answer. Both being satisfied is why I trust the seven numbers as recorded; it is not a reason to trust anything outside the seven.

Third, a labeling wrinkle worth not sweeping away. In the raw archive, all seven `epistemic_games` cases are filed under the `ml_debugging` track, even though the inspected task core implements symbolic Bayesian inference. The source-semantic regrouping pulls them out — `ml_debugging` drops to 30 cases at 9 PASS / 21 FAIL once the seven are separated to their own 7/7 — but I want to be explicit that this regrouping is an editorial override; the raw track label is preserved unchanged. I am not quietly rewriting the archive; I am reading its recorded track one way and its source semantics another, and reporting that they disagree.

Fourth, and most important for not confusing competence with its opposite: the failure taxonomy of this campaign is dominated by modes that are not behavioral misses at all. Of the eligible failures, the largest shares are `patch_invalid` (24) and `underfit` (20), followed by `source_invalid` (10), `runtime_error` (3), `invalid_action` (2), and `overfit_visible_tests` (2). A validator rejecting a patch, a runtime crashing, a tool producing an invalid action — these are failures of the plumbing or the submission, not evidence that a model reasoned incorrectly. If you mix them into a single "accuracy" figure you will both flatter and slander different models at once. The seven `epistemic_games` passes are clean behavioral passes; most of the campaign's failures are not clean behavioral failures; neither fact should be read through the other.

## What a test of the thing the name promises would need

None of this is an argument that epistemic evaluation is a dead end — the opposite. The live field is specific about what it measures. [MindGames](https://aclanthology.org/2023.findings-emnlp.303/) uses dynamic epistemic logic to isolate controlled theory-of-mind problems; [Hi-ToM](https://aclanthology.org/2023.findings-emnlp.717/) targets higher-order recursive beliefs and deception; [BigToM](https://proceedings.neurips.cc/paper_files/paper/2023/file/2b9efb085d3829a2aadffab63ba206de-Paper-Datasets_and-Benchmarks.pdf) generates social-reasoning items from causal templates. Those are distinct constructs with distinct machinery. Their relevance here is only this: a seven-item Bayesian-calculation result should not be dressed up as a new recursive-ToM benchmark, because that would claim to have measured a construct these lines of work define far more carefully. (This is a targeted precedent check, not a literature survey, and it supports no claim of being first.)

If someone wanted the harder thing, the current seven make a fine calibration floor, and the extension is a design problem, not a rhetorical one. Keep the Bayesian cases as the sanity layer. Then specify, separately, a recursive task: base policies, utilities, observer/player alternation, explicit belief-update rules, and a mapping from beliefs to public actions. Make the likelihood tables *unseen* rather than supplied. Run multiple seeds, not one. Build counterfactual cases where the narrative cue actively contradicts the supplied evidence — the trap case is a gesture at this, but with the table still handed over. And crucially, score the final inference *separately* from any evidence that the model reconstructed the policy or ran the recursion, so a correct number earned by shortcut is distinguishable from a correct number earned by the intended procedure. A pass tells you the output matched; it never tells you which internal process produced it.

## What the seven cases license

So, back to the reading experiment I opened with. Here is what I think the evidence supports, kept narrow on purpose.

Atria-Dawn-Preview answered all seven selected `epistemic_games` instances correctly — exact posteriors, correct verdicts, correct supported-world labels, provenance checks passing — under the policies the task implementation stipulates. That is competence on a small, public, deterministic family of two-hypothesis Bayesian updates with a reference table and a public oracle, including the cases engineered for non-identifiability. It is a clean behavioral result, and I am happy to call it a good one.

What it does not license: that the model inferred the policy table, generated an opponent model, or recursively updated beliefs over multiple strategic agents. That these seven establish a difficulty scale, a capability ranking, or a causal effect of any axis — seven seed-0 cells, read against a dirty-repository provenance and a comparator that only probably matches what ran, cannot carry that weight. And that "strategic" in a condition label means strategy was exercised rather than merely narrated.

The name said *games*. The code computed a posterior and checked it against an oracle. Both of those are true, and the honest headline is the smaller one.
```
