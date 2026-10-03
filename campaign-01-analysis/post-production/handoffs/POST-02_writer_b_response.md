---
title: "Who Supplied the Speaker's Likelihoods?"
date: 2026-10-03
layout: post
---
{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The distinction among an observation’s diagnostic power, a posterior preference, and the construction of a speaker’s policy; the proposed follow-up is not a performed experiment.</dd>
  <dt>Synthesis</dt>
  <dd>Selected campaign results, an inspected clean-source comparator, and the cited epistemic-evaluation work.</dd>
  <dt>Prose</dt>
  <dd>Model-written in the Arena writing process from supplied evidence and editorial constraints; the site byline is not a claim of sole human composition.</dd>
  <dt>Certainty</dt>
  <dd>High for the recorded judgments on the seven selected cases; qualified for exact executed-code identity and for any generalization beyond them.</dd>
  <dt>Importance</dt>
  <dd>A correct update from a supplied policy is worth recognizing without mistaking it for construction of that policy.</dd>
</dl>

One answer in the archive gives World 1 a probability of three fifths, calls World 1 the more supported world, and says the observed announcement is *indistinguishable* between the two worlds. The judge credits all three answers.

There is no contradiction. The observation did not move the probability to three fifths. It started there.

That small distinction opens a larger one. An agent might correctly update its belief about a speaker while having no part in working out why the speaker would make a particular announcement. The seven selected `epistemic_games` answers are clean successes at the update. They are not, on the evidence available here, a test of whether the model constructed a recursive account of the speaker.

I want to keep three questions apart: **Does this announcement discriminate between the worlds? Which world is more probable after hearing it? Who supplied the account of what each world would announce?** The recorded judge checks answers to the first two. In the inspected clean implementation, the likelihoods needed to answer them are stipulated.

## A world can lead without winning the evidence

The clean-source comparator describes two possible worlds, a prior over them, and the likelihood of an observed announcement under each specified behavior policy. Given those quantities, the update is:

$$
P(W_1\mid o)=
\frac{P(o\mid W_1)P(W_1)}
{P(o\mid W_1)P(W_1)+P(o\mid W_2)P(W_2)}.
$$

It is often easier to see what the observation contributes in odds form:

$$
\frac{P(W_1\mid o)}{P(W_2\mid o)}=
\frac{P(W_1)}{P(W_2)}\cdot
\frac{P(o\mid W_1)}{P(o\mid W_2)}.
$$

The second factor is the observation’s likelihood ratio. If the two worlds produce that announcement with equal likelihood, the factor is one. The posterior then retains the prior. With balanced priors, neither world leads. With a prior favoring World 1, World 1 still leads—but the announcement has done nothing to establish that lead.

Four selected cases make the separation visible. Each uses the paired, bare-table, report presentation; the table gives the judge-credited reference values, not new measurements of speaker behavior.

| Evidence and prior | Posterior for World 1 | Evidence verdict | More-supported world |
| --- | ---: | --- | --- |
| Ambiguous, balanced | $1/2$ | Indistinguishable | Neither |
| Ambiguous, skewed | $3/5$ | Indistinguishable | World 1 |
| Strong, balanced | $1/15$ | Distinguishable | World 2 |
| Weak, balanced | $92/177$ | Weakly distinguishable | World 1 |

The skewed-prior row is the useful snag. “More supported” describes the posterior ranking; “indistinguishable” describes what this observation contributes to that ranking. Someone who changes the evidence verdict merely because the posterior is $3/5$ has conflated two outputs the judge deliberately keeps separate.

The strong and weak rows separate magnitude from direction, too. With balanced priors, the strong case’s posterior of $1/15$ implies odds of $1$ to $14$ for World 1 against World 2. The weak case’s $92/177$ implies odds of $92$ to $85$. Those odds follow from the credited posteriors and balanced priors; they are **not** an independently inferred speaker-policy table. The judge also checks the appropriate likelihood-ratio verdict. I do not need to invent numerical thresholds for its “strong” and “weak” bands to see why the posterior, verdict, and supported-world fields are different questions.

This is a good reason to test them separately. A story about a “genuine” or “strategic” speaker may sound suggestive, but an adjective cannot override a stipulated equal-likelihood observation. Leaving a prior alone when evidence says to leave it alone is a real, checkable success.

## What the seven scores say

In the archived Atria-Dawn-Preview run, all seven selected `epistemic_games` cases are recorded as PASS with score 1.0. Their final results credit the posterior, likelihood-ratio verdict, and most-supported-world answer; they also record the required consistency and provenance checks as passing. These are behavioral-reference judgments on the selected instances, not merely compile-only checks.

The seven are variants, not seven independent draws from a population of strategic situations. Five have ambiguous evidence: the balanced bare-table paired case, its narrative-framing counterpart, a solo presentation, a trap-scenario presentation, and the skewed-prior case. The other two use strong and weak evidence. There is one selected seed per cell. In particular, there is only one selected narrative case, one solo case, and one skewed-prior case.

The environment also has a recorded public Bayesian-oracle behavioral self-test that was executed and passed. That environment-level preflight is separate from the exact-instance calibration and final judgment for each case. It is not an eighth model answer, nor does its existence show that the model used the oracle to produce any answer. The likelihood tables and reference behavior were public in the inspected task design; a passing final response does not disclose the internal procedure that produced it.

I would call the seven results unambiguously correct **as recorded for these selected tasks**. I would not call them an estimate of success across new seeds, new policies, or models. Later editorial or model-role passes over an article about the run do not add experimental replications.

## The calculation the task does not ask for

Where did $P(o\mid W_1)$ and $P(o\mid W_2)$ come from? That is the construct boundary.

In the inspected clean comparator, an evidence table supplies likelihoods for two stipulated behavioral policies. The implementation describes this version as Bayesian inference over those policies, presented through genuine-versus-strategic narratives. It does not implement a fully recursive level-$k$ engine that derives announcements from utilities and repeated belief updates. The model answering a case can therefore solve the posed problem without deriving how either speaker chose an action.

That design choice has a benefit. Supplying the policies isolates the update. If an answer is wrong, the evaluator can inspect its posterior, evidence verdict, and world label rather than wondering whether an unspecified theory of the speaker differed from the evaluator’s. But the same isolation limits the claim. Giving an agent a likelihood table and checking its use of that table is not checking whether it could generate the table from interacting minds.

Nor does the limit imply that Atria-Dawn-Preview *cannot* reason recursively. The archive does not settle that question in either direction. It records correct outputs for this bounded inference problem; it does not reveal whether the model used an explicit calculation, a different reliable procedure, or some other route to the same outputs.

There is a provenance limit alongside the construct limit. The paid campaign recorded its repository as dirty. The selected configurations for all 33 environments matched those in the inspected clean comparator, but matching configurations do not prove byte-for-byte identity of the executed task, helper, and judge code. Thus the seven final judgments are observations from the archive; the account of how the task is implemented comes from a clean comparator, not a certified copy of every executed source file. That qualification belongs beside the implementation claim, rather than disappearing once the results look tidy.

## Seven cases do not become a difficulty scale

It is tempting to read perfect scores across several presentation axes as evidence that framing, presentation, or scenario wording has no effect. The selected comparisons cannot establish that. One narrative case and its bare-table counterpart both passed; one solo case and a paired case both passed. Those observations identify no failure in those particular cells. With one selected seed per cell and sparse, mostly one-factor substitutions, they do not estimate a causal framing effect, test interactions, or measure robustness over a population of stories.

Even the stored track name needs care. The archive labels these seven cases as `ml_debugging`, although the inspected task semantics are Bayesian inference. Under the recorded label, the track has 37 cases, with 16 passes and 21 fails. Separating the seven by task semantics leaves 30 debugging cases with 9 passes and 21 fails, alongside these seven Bayesian passes. That separation changes how a reader describes the cases; it does not change a single run. Other category-themed outcomes in the campaign concern heterogeneous code-repair tasks, not a theorem result or a transferable scalar of category-theoretic ability. None of these sparse, task-specific axes supplies a common difficulty scale or a general model ranking.

The campaign-wide accounting is another place where an attractive fraction could conceal unlike things. The archive has **194 raw result rows** and **24 separately recorded omissions**; the omissions are not 24 additional failed results. Of the raw rows, 72 have behavioral-reference judging, with 56 passes and 16 fails. The other 122 are compile-only, with 75 passes and 47 fails. Two provider-terminal rows belong to that raw compile-only group. Excluding those two gives a 192-row sensitivity set: the same 72 behavioral-reference rows, plus 120 compile-only rows with 75 passes and 45 fails. Compile-only outcomes are exploratory; adding their passes to behavioral-reference passes would not produce a validated behavioral success rate. The seven cases discussed here belong to the behavioral-reference group.

Failure labels also sit at different layers. Elsewhere in the eligible set, 24 failures are labeled `patch_invalid`, 10 `source_invalid`, two `invalid_action`, and three `runtime_error`; 20 are labeled `underfit` and two `overfit_visible_tests`. A rejected submission, an invalid tool action, an execution failure, and a behavioral mismatch do not diagnose the same thing. A failure of judging infrastructure would require its own evidence, not an automatic reinterpretation of any of those labels. None of this downgrades the seven credited answers. It prevents unrelated failures—and weaker compile-only passes—from becoming evidence about their Bayesian task.

## Ask for the missing likelihoods

A follow-up should preserve the present cases as calibration rather than making their success stand in for a different ability. First, it could vary priors and use unseen likelihood tables across multiple selected seeds, while scoring the posterior, likelihood-ratio verdict, and supported world separately. It could put suggestive narrative cues in tension with the supplied numbers. Success there would strengthen the case for reliable conditional inference, including resistance to a misleading description. It would **still** be conditional inference from given policies.

To ask a recursive question, the evaluator would need to specify a mechanism that generates policies: base behavior, utilities, who observes which action, the order of player and observer moves, and rules for belief updates. It could then change one player’s information or incentives while holding other parts of a case fixed. The model would have to predict how the public action distribution changes, derive the resulting observation likelihoods, and only then compute a posterior. A reference implementation would need to check the policy predictions separately from the final update. Otherwise a correct final fraction could hide an incorrect account of the speaker that happened to cancel out.

This would be a proposed experiment, not a retrospective interpretation of the seven passes. It also needs a safeguard against an underspecified story. If the evaluator withholds the likelihood table *and* fails to define how actions are generated, there may be no unique posterior to judge. Making a task harder by removing necessary information is not the same as testing a deeper model of another agent.

There are already distinct ways to make epistemic and social-reasoning questions precise.  uses dynamic epistemic logic for controlled tasks;  targets higher-order recursive beliefs and deception;  uses causal templates to generate social-reasoning evaluations. Those references identify different targets and methods. They do not validate this campaign, and a targeted comparison with them is not an exhaustive novelty claim. They do make it harder to justify calling a supplied-likelihood update a measurement of recursive theory of mind.

Even the stronger proposed test would establish performance on specified outputs, not expose the model’s private reasoning process. That is enough to design a meaningful comparison, provided the scoring keeps policy construction and posterior calculation apart.

The skewed-prior answer is where I would leave the result: World 1 remains at $3/5$; the announcement remains indistinguishable. Atria-Dawn-Preview got that answer, and all six other selected behavioral-reference answers, right as recorded. The evidence licenses a narrow, useful conclusion about Bayesian inference under stipulated policies. It does not license an account of how the model would construct those policies, a causal claim about the presentation changes, or a general ranking of strategic reasoners.
