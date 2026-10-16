---
title: "The Model's Belief Is Right; Its Decision Is Fragile"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The dissociation framing and the specific claim that belief invariance plus decision sensitivity is the campaign's most informative result.</dd>
  <dt>Synthesis</dt>
  <dd>Role-separated analysis (theorist, experimentalist, skeptic, prior-work killer) over the archived Mercury evidence, then a single final writer.</dd>
  <dt>Prose</dt>
  <dd>Drafted by the final writer from the evidence dossier, two candidate drafts, and an editorial blueprint; not an independent second author.</dd>
  <dt>Certainty</dt>
  <dd>Observed on one model and provider; small sample (36 matched pairs); no confidence intervals. Interpretation, not mechanism.</dd>
  <dt>Importance</dt>
  <dd>Argues that scoring stated belief alone overstates reliability; decision behavior needs its own audit.</dd>
</dl>

A model can know the right answer and still act on the wrong one. In a controlled probe of 36 matched pairs, Mercury-2.5's stated posterior never changed with the order in which the same facts were presented, but its terminal decision changed in 5 of those pairs, and every one of those 5 changes was a correctness flip. Diagnostic choices diverged in 17 of 36. The belief layer is order-invariant; the behavior is not.

That is the most informative result I can defend from the archived Mercury campaign. The campaign is large — 416 selected cases across 38 environments, 405 of them scored — but size is not the point. The point is a dissociation: belief computation and decision selection can come apart, and a benchmark that scores only the former will miss it.

## The probe

The probe is `t1_same_fact_presentation`: six cells crossing three fact counts (3, 4, 5) with two priors (1/2 and 1/3), six seeds each, 36 matched pairs in total. Each pair presents the same facts in two orders — a canonical bullet order and a reversed numbered order — and asks for an elicited belief, a terminal answer, and a pair of diagnostic choices. The oracle is exact, so correctness is not in dispute.

The result is lopsided in a revealing way. Across all 36 pairs, the elicited posterior was identical in both orders: zero belief flips. The terminal answer flipped in 5 of 36 pairs, and all 5 flips were correctness flips — the model was right in one order and wrong in the other. Diagnostic choices (which evidence to inspect or request next) diverged in 17 of 36.

Read that again: the model's number did not move, but its action did. If you only read the posterior, the model looks perfectly stable. If you read the decision, it is presentation-sensitive in roughly one in seven pairs, and wrong in one in seven of those.

## Why this is not a parsing story

The natural first explanation is that presentation changes parsing, and parsing changes the effective evidence. That would make the belief flip too, since the belief is computed from the same parsed facts. It did not. The posterior is invariant to order while the decision is not, which pushes the locus of fragility downstream of belief computation — into whatever maps a correct posterior into an answer and a choice.

I am deliberately not calling this a "decision layer" in the architectural sense. The probe measures endpoints, not internals. The honest claim is behavioral: on this task, with this model, correct belief and correct action are not the same achievement.

## The broader suite agrees about belief

The same exactness shows up in the epistemic-game suite: all 23 cases — base scenarios plus evidence, presentation, and prior interventions — produced zero posterior error and the correct verdict. Whatever Mercury-2.5 is doing with explicit likelihoods, it is doing it reliably across intervention variants. Belief tracks content.

## Where it breaks: proxy channels

The decision side breaks under a different manipulation. Intervention cases that introduce a visible-proxy channel pass at 0.30 (8 of 27), and a reward-proxy channel at 0.25 (1 of 4), against a 0.69 base pass rate (228 of 331 scored base cases). Within paired groups sharing a latent specification, 7 of 76 intervention cases flipped a passing base case to a failure, 4 of them under the visible-proxy tag.

These are not difficulty-matched experiments — the intervention cases often differ in their difficulty levels — so I treat the proxy effect as an observed association, not a causal claim. But the direction is consistent and the within-pair flips are hard to explain by difficulty alone.

## What this means for evaluation

Two consequences follow, and both are modest.

First, a correct posterior is not a correct action. Evaluating a model on its stated belief alone overstates reliability. Belief and decision should be scored as separate endpoints, and a benchmark that collapses them into one will hide exactly this kind of fragility.

Second, presentation is a variable. If the same facts in a different order change the answer, then any evaluation that fixes one presentation and reports one number is measuring a presentation, not just a capability. The T1 probe exists precisely to make that visible; the broader campaign does not control for it.

## What the campaign cannot show

The limits are as important as the result. This is one model on one provider configuration (mercury-2.5, reasoning effort high). The probe has 36 pairs and no confidence intervals. The intervention cases are not difficulty-matched. Terminal-answer extraction may be brittle, and a parsing difference could in principle masquerade as a decision flip — though the belief invariance makes that less likely. There is no independent replication, and the source repository was dirty at run time, so exact source identity is unresolved.

The campaign also cannot support a general claim about "reasoning." The 405 scored cases span environments with pass rates from 0.00 to 1.00, and the judge guarantees differ (189 behavioral-reference, 227 compile-only). Collapsing those into one number would be a category error. The 11 infrastructure-unscored cases and 56 unverified twin groups are further reasons to keep the claims narrow.

## A bounded conclusion

What I can say: on this probe, with this model, belief computation is presentation-invariant and content-sensitive, while terminal decisions are presentation- and proxy-sensitive. That is a dissociation worth measuring for, not a diagnosis of an internal mechanism. Whether it survives replication, difficulty matching, and a second model is the experiment that would actually settle it.
