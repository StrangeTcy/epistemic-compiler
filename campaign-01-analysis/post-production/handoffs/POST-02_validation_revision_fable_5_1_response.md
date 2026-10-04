---
title: "A Correct Posterior Is Not a Model of the Speaker"
date: 2026-10-03
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The argument here is a reading discipline. It separates three questions: what an observation tells you, which world you now favour, and who supplied the speaker's behaviour. The recursive follow-up is a proposal. It has not been run.</dd>
  <dt>Synthesis</dt>
  <dd>Seven selected case records from one archived evaluation campaign, an inspected clean-source comparator for the task, and three prior epistemic-reasoning papers cited only as precedent.</dd>
  <dt>Prose</dt>
  <dd>Language models wrote this through a role-separated Arena process: two separate drafts, an editorial critique, and a final synthesis, all working from a supplied evidence dossier. It is published under the site byline. These writing passes are not replications of the experiment, and none of them executed the model under test.</dd>
  <dt>Certainty</dt>
  <dd>High for the recorded judgments on the seven selected cases. Unresolved for whether the executed task code exactly matches the source I inspected. None for any generalisation past these seven items.</dd>
  <dt>Importance</dt>
  <dd>Moderate. Treating a calculation as a capability costs little to do and a lot to undo.</dd>
</dl>

One answer in the archive gives World 1 a probability of three fifths. It names World 1 as the better-supported world. It also says the observation is *indistinguishable* between the two worlds. The judge credits all three parts.

Is that a contradiction?

No. The observation never moved anything to three fifths. The probability started there.

That small accounting point leads to a bigger one. A model can update correctly on what a speaker said without having worked out *why* the speaker would say it. The task this answer comes from is called epistemic games. Its narratives talk about "genuine" and "strategic" speakers. But in the source I could inspect, the speakers' behaviour is not derived by anyone. It is given in a table.

So I want to keep three questions apart throughout:

1. **Does this observation discriminate between the worlds?**
2. **Which world is more probable after seeing it?**
3. **Who supplied the account of what each world would produce?**

The judge scores answers to the first two. In the inspected implementation, the answer to the third is "the task did". That implementation says explicitly that this version does not implement a fully recursive level-$k$ engine with utilities and recursive belief updates. Its own design description calls the target Bayesian inference over two specified behavioural policies, presented through genuine-versus-strategic narratives.

That description has a caveat attached, and it belongs here rather than in a footnote. I read the clean comparator source, not a certified copy of the code that ran. The paid campaign recorded its repository as dirty, so the exact paid-run source identity remains unresolved: the clean comparator is a comparator, not proof of which source executed. All 33 selected configuration hashes match the clean comparator. Matching configurations are still not byte-for-byte proof that the executed task, judge or helper code was identical. Exactly which source ran is unresolved.

Within those limits the result is clean. Atria-Dawn-Preview passed all seven selected cases with score 1.0. Each final result credits the posterior, the likelihood-ratio verdict and the most-supported world, and records the consistency and provenance checks as passing.

This is a real success, but it is a Bayesian one. It is not evidence of recursive theory of mind.

## Three fields, three questions

The inspected task gives the model two hypotheses, $W_1$ and $W_2$, a prior over them, an observed announcement $o$, and a likelihood for that announcement under each stipulated behavioural policy. The update is ordinary two-hypothesis Bayes:

$$
P(W_1 \mid o) = \frac{P(o \mid W_1)\,P(W_1)}{P(o \mid W_1)\,P(W_1) + P(o \mid W_2)\,P(W_2)}
$$

The numerator asks how plausible World 1 was to begin with, and how likely World 1 would be to produce this announcement. The denominator applies the same question to both worlds, so the result is a proper probability.

The odds form is easier to read, because it separates the two contributions:

$$
\frac{P(W_1 \mid o)}{P(W_2 \mid o)} = \frac{P(W_1)}{P(W_2)} \cdot \frac{P(o \mid W_1)}{P(o \mid W_2)}
$$

The first factor on the right is where you stood before the observation. The second factor is the likelihood ratio: what the observation itself contributes. The task's evidence verdict is about the second factor. The most-supported-world label is about the left-hand side.

Now the three-fifths case makes sense. In the ambiguous-evidence condition, both worlds produce the announcement with equal likelihood. The likelihood ratio is 1 and the observation contributes nothing. With a balanced prior, the posterior stays at $1/2$ and neither world leads. With the skewed prior in the selected case, the posterior stays at the prior: $3/5$, which is odds of 3 to 2 for World 1. World 1 leads, but the announcement did nothing to put it in front.

"More supported" and "indistinguishable" are answers to different questions. Someone who changes the evidence verdict because the posterior isn't one half has merged two outputs that the judge deliberately keeps apart.

## What was answered

Four of the selected cases show the separation. All four use paired presentation, bare-table framing and the "report" scenario. The values are the judge-credited reference answers. They are not new measurements of how any speaker behaves.

| Evidence, prior | Posterior for World 1 | Evidence verdict | More-supported world |
| --- | ---: | --- | --- |
| Ambiguous, balanced | $1/2$ | Indistinguishable | Neither |
| Ambiguous, skewed | $3/5$ | Indistinguishable | World 1 |
| Strong, balanced | $1/15$ | Distinguishable | World 2 |
| Weak, balanced | $92/177$ | Weakly distinguishable | World 1 |

A note on precision. The model reported decimals rather than fractions. The judge credited those decimals against the exact reference fractions $92/177$ and $1/15$. "Exact" here describes the reference the judge checks against. It does not mean the model printed a fraction.

The strong and weak rows separate *how much* the evidence moves things from *which way* it moves them. With a balanced prior, the prior odds are 1. The posterior odds therefore equal the likelihood ratio, and I can read them straight off the credited posteriors:

- In the strong case, $1/15$ leaves World 1 far behind. The posterior odds, and so the likelihood ratio, run heavily against it; the observation favours World 2 heavily.
- In the weak case, $92/177$ sits just above one half. The odds lean only slightly towards World 1.

Both ratios are derived from the posteriors and priors. They are not a speaker-policy table that anyone inferred. For these two cases the judge checks the posterior value and, separately, whether the evidence falls in the correct likelihood-ratio band. I don't know the band thresholds and won't invent them. I don't need them to see that a near-coin-flip posterior and a "weakly distinguishable" verdict are distinct claims, and that the model got both right.

The other three selected cases are all balanced, ambiguous-evidence variants:

- one with narrative framing instead of a bare table;
- one with solo presentation instead of paired;
- one in the scenario labelled "trap", still with bare-table framing.

All three returned $1/2$, "indistinguishable" and "neither", as the arithmetic requires. I have only the recorded levels and outputs for these cases. I'm not going to describe what the trap scenario's story contained, or what its designers meant it to provoke.

## Where did the likelihoods come from?

This is where the task's boundary sits.

Every row above depends on two numbers: $P(o \mid W_1)$ and $P(o \mid W_2)$. In a recursive strategic setting, those numbers would be the hard part. A speaker who knows a listener is watching chooses what to announce based on what they expect the listener to infer. The listener knows that, and the speaker knows the listener knows. The likelihood of an announcement comes out of that regress, together with whatever utilities drive it.

In the inspected comparator, that regress is not present. An evidence table supplies the likelihoods for two stipulated policies. The genuine-versus-strategic narrative explains *why* a speaker might announce one thing rather than another, but it doesn't generate the table. Bayesian inference is performed on numbers that arrive already computed.

I don't think this is a flaw in the task. Supplying the policies isolates the update, and that is valuable. If an answer is wrong, you can tell whether the posterior, the verdict or the label went wrong. You don't have to wonder whether the model's theory of the speaker simply differed from the evaluator's. The task is well specified and has a unique answer, and the environment carries a public Bayesian-oracle behavioural self-test that was recorded as executed and passed.

The same isolation limits what a pass can mean. Giving a reasoner a likelihood table and checking that it uses the table correctly is a different test from checking whether it could build that table from interacting minds.

It matters which way this limit runs. The archive doesn't show that Atria-Dawn-Preview *cannot* reason recursively. It shows nothing in either direction about that. A passing final answer doesn't reveal the procedure behind it. The model might have done explicit arithmetic, used some other reliable route, or something else. The archive contains no evidence that the model inferred a policy table, built an opponent model or updated beliefs recursively over several strategic agents. The task never asked it to.

The oracle self-test also needs to stay in its own box. It is an environment-level check that the task's reference machinery behaves as intended. It is separate from the per-case calibration and final judgment on each answer. It isn't an eighth model answer, and its existence says nothing about how the model produced its seven.

## Seven green cells are not a robustness curve

It is tempting to read perfect scores across five axes (evidence, framing, presentation, prior and scenario) as showing that framing doesn't matter, that presentation doesn't matter, or that the model resists narrative pull in general. The design can't support any of those conclusions.

There is **one selected seed per case**. There is one model and one configuration. The axis comparisons are sparse substitutions of one factor at a time around a fixed base cell, not an interaction grid. Exactly one case uses narrative framing, one uses solo presentation and one uses a skewed prior. When the narrative case and its bare-table counterpart both pass, all we learn is that neither of those two cells failed. That is not a framing effect of zero, and it is certainly not a robustness estimate over a population of stories.

These seven cases are also not seven independent draws from "strategic situations". They are hand-varied neighbours of each other. Five of the seven share ambiguous evidence, where the correct move is to leave the prior alone.

One more boundary concerns how these cases sit inside the wider campaign. All seven were judged in the behavioural-reference mode, which scores answers against a reference. The campaign also contains compile-only results, which the report treats as exploratory and excludes from any validated behavioural aggregate. None of the seven is compile-only, and none of the campaign's other outcomes says anything about this task. I mention the split only so that nobody adds these seven passes into a larger fraction where they would sit next to results judged under weaker guarantees.

Rereading or redrafting an article about the run doesn't change any of this. Several role-separated writing passes looked at these seven records, but there is still one run per cell. Editorial attention is not replication.

## What a recursive test would have to specify

If someone wants to measure what the task's name suggests, the seven current cases make a good calibration floor. They check that the update itself is sound. A recursive layer above them would be a different and separately specified experiment. I am proposing it here, not reporting it.

At a minimum, it would need:

- **Base policies and utilities**, so that a speaker's choice of announcement follows from what they want rather than from a table.
- **An information structure**: who observes what, in what order, and how player and observer moves alternate.
- **Belief-update rules**, so the regress has a defined depth and a defined fixed point, or at least a defined truncation.
- **A mapping from beliefs to public actions**, so that the likelihood of an announcement is something the model must *derive*.

The model would then predict how each world's speaker acts, turn that into observation likelihoods, and only then compute the posterior.

The scoring has to keep those stages apart. If only the final fraction is judged, an incorrect speaker model could produce a correct posterior through errors that happen to cancel. The policy predictions need a reference check of their own.

The design would also need unseen policy structures and likelihoods rather than public ones, multiple seeds per cell, and perturbations that change one player's information or incentives while holding everything else fixed. A natural stress test would put a narrative cue in tension with the generated evidence. That would be a new condition. I don't claim the current trap case did this.

There is one trap in the design itself. If the evaluator withholds the likelihood table without fully defining how actions are generated, the problem may no longer have a unique posterior. Removing necessary information makes a task underdetermined, which is not the same as making it test a deeper model of another agent.

Other researchers have already made social and epistemic reasoning precise in other ways. [MindGames](https://aclanthology.org/2023.findings-emnlp.303/) uses dynamic epistemic logic to build controlled theory-of-mind problems. [Hi-ToM](https://aclanthology.org/2023.findings-emnlp.717/) targets higher-order recursive beliefs and deception. [BigToM](https://proceedings.neurips.cc/paper_files/paper/2023/file/2b9efb085d3829a2aadffab63ba206de-Paper-Datasets_and_Benchmarks.pdf) uses causal templates to generate social-reasoning evaluations. These target different constructs with different machinery. They don't validate anything in this campaign, and this targeted comparison is not a novelty claim. Their relevance is simple: careful work already exists on the construct that the name "epistemic games" points to. A seven-item supplied-likelihood update should not be presented as a new benchmark of it.

Even the stronger version would measure performance on specified outputs. It would still not reveal the model's private reasoning. It would only place the scored outputs closer to the capability people fuckingly want to talk about.

## What the three-fifths answer licenses

Back to where I started. World 1 sits at $3/5$, and the announcement is indistinguishable between the worlds. Atria-Dawn-Preview got that right. It also got the six other selected behavioural-reference cases right, as recorded.

**The evidence licenses this:** on seven selected single-seed instances, the model returned answers credited as correct for the posterior, the likelihood-ratio verdict and the most-supported world, with consistency and provenance checks passing. This was Bayesian inference over two behavioural policies stipulated by the task. It includes the cases where the right move is to let an uninformative observation leave the prior where it was. That is a narrow result, and a good one.

**The evidence does not license these claims:**

- that the model can build the policies it was given, or did build them;
- that it models opponents recursively, or has theory of mind in any general sense;
- that framing, presentation or scenario wording has no effect;
- a difficulty scale or a ranking of strategic reasoners;
- any statement about the procedure the model used internally.

All of this rests on one run per cell and on paid-run source identity that remains unresolved because the repository was recorded as dirty. The task's name is about games. What the evidence shows is a correctly computed posterior on given inputs.
