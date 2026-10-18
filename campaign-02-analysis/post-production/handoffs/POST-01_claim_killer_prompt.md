CLAIM KILLER — POST-01: The Model's Belief Is Right; Its Decision Is Fragile (Mercury-2.5)

You are the Claim Killer. Your job is to verify every number, strong factual claim, and inferred conclusion in the two candidate drafts against the evidence packet. Produce a claim-by-claim verification table with verdicts.

EVIDENCE PACKET (verified ground truth):
- T1 same_fact_presentation: 6 cells × 6 seeds = 36 matched pairs. 0/36 belief flips. 5/36 terminal answer flips (all correctness flips). 17/36 diagnostic-choice divergences. 3 fact counts (3, 4, 5) × 2 priors (1/2, 1/3) = 6 cells. Canonical bullet order vs reversed numbered order. Oracle is exact.
- Epistemic games: 23/23 exact posterior match (base + evidence/presentation/prior interventions). Zero posterior error. posterior_reported = posterior_true.
- Proxy interventions: visible_proxy 8/27 (0.30). reward_proxy 1/4 (0.25). base 228/331 (0.69). Paired flips: 7 pass→fail (4 visible_proxy) within 76 intervention cases sharing latent spec with base.
- Campaign: 416 selected, 405 scored, 277 PASS, 128 FAIL, 0.684. 11 unscored. Judge guarantees: 189 behavioral_reference + 227 compile_only = 416. Single seed per selected cell. Dirty repo. 56 of 132 twin cases unverified.
- Limitations: single model/provider (mercury-2.5, reasoning_effort=high). T1: 36 pairs, no CIs. Intervention cases not difficulty-matched. Terminal-answer extraction may be brittle. No independent replication.

EDITORIAL BLUEPRINT (accepted Stage C) key decisions:
- Adopt narrow behavioral dissociation thesis.
- Draft A (gpt 6 sol max) as base; import B's tables, "outputs not modules" header, "zero flips ≠ zero error" couplet, titled coda.
- Remove: "verdict correct in all 23" (unverified), "38 environments" (unverified), "reasoning effort high" (unverified), "latent specification" (unverified), game intervention types (unverified).
- Remove: "one in seven" garbled fraction, "pass rates from 0.00 to 1.00" (fabricated), judge guarantees misattached to 405.
- Add: sampling-noise null, chance agreement for diagnostic choices, posterior invariance as floor effect, answer-posterior relationship undefined, per-cell flip distribution, pre-specification of T1.
- Keep: [ac-word], [d-word], [m-word] tokens (intentional). Remove 👹 glyph.
- Figure 1: three endpoints SVG. Figure 2: campaign denominators SVG (new).

CANDIDATE DRAFTS (verbatim):
gpt 6 sol max:

---
title: "The Model's Belief Is Right; Its Decision Is Fragile"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The paired-presentation result is most useful as a narrow dissociation between a stated posterior and the responses given alongside it.</dd>
  <dt>Synthesis</dt>
  <dd>Draws on the archived paired probe, epistemic games, proxy-intervention results, and campaign coverage. These are treated as distinct measurements.</dd>
  <dt>Prose</dt>
  <dd>Written from verified aggregate results, without access to individual prompt-and-response transcripts for this essay.</dd>
  <dt>Certainty</dt>
  <dd>The reported counts are specific; the interpretation is bounded by 36 matched pairs, possible extraction errors, and no independent replication.</dd>
  <dt>Importance</dt>
  <dd>A stable probability report did not guarantee a stable answer in this probe. That is a reason to examine both readouts, not a general theory of how the model decides.</dd>
</dl>

If a model gives the same probability after seeing the same facts in two presentations, should it also give the same answer? I would have expected so, at least in a task with an exact oracle. Mercury-2.5 did not always oblige. In 36 matched pairs, its reported posterior was identical across the two presentations in every pair. Its terminal answer changed in five pairs. Each of those five changes was also a correctness change: one presentation elicited the right answer and the other the wrong one. Its choice of what evidence to inspect or request next differed in 17 pairs.

There is an important restraint hidden in the title. *Belief* means the posterior the model stated, not an internal state I can inspect. *Right* is established by a related set of 23 oracle-scored epistemic games, in which every reported posterior matched the true posterior. The aggregate evidence does **not** tell me that the stated posterior was oracle-correct in each of the five paired-presentation trials whose answers flipped. In the paired probe, the direct finding is invariance of the reported number alongside variability of the answer. I want to keep that finding intact rather than strengthen it by quietly merging two sets of results.

## Hold the facts fixed; change their presentation

The paired probe crosses three fact counts—three, four, and five—with two priors, 1/2 and 1/3. That makes six cells, each tested with six seeds: 36 matched pairs. Within a pair, the facts and prior stay the same. One prompt puts the facts in a canonical bullet order; the other reverses them in a numbered list. The model is asked for a posterior, a terminal answer, and a diagnostic choice about which evidence to inspect or request next.

Consider what a single cell specifies. With four facts and a prior of 1/3, each of its six pairs compares two presentations of those same four facts. The results available to me do not say whether any of the five answer flips occurred in that particular cell. It would be easy to invent a vivid example of one; it would not be evidence.

The manipulation also has a small but consequential complication. It changes **both sequence and format**: canonical bullets become reversed numbered items. “Presentation sensitivity” is therefore the [d-word] description. The probe cannot, by itself, assign the difference specifically to position in the list rather than numbering, or to an interaction between them.

<figure>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 176" role="img" aria-labelledby="paired-figure-title paired-figure-description" style="max-width: 100%; height: auto;">
    <title id="paired-figure-title">Different outputs across two presentations of the same facts</title>
    <desc id="paired-figure-description">Of 36 matched pairs, zero had different reported posteriors, five had different terminal answers, and seventeen had different diagnostic choices. All five answer changes changed correctness.</desc>
    <rect x="0" y="0" width="760" height="176" fill="#ffffff"/>
    <text x="8" y="32" font-size="16" fill="#203040">Reported posterior</text>
    <rect x="275" y="14" width="360" height="24" fill="#dce5ec"/>
    <text x="650" y="32" font-size="16" fill="#203040">0/36</text>
    <text x="8" y="77" font-size="16" fill="#203040">Terminal answer</text>
    <rect x="275" y="59" width="360" height="24" fill="#dce5ec"/>
    <rect x="275" y="59" width="50" height="24" fill="#226b99"/>
    <text x="650" y="77" font-size="16" fill="#203040">5/36</text>
    <text x="8" y="122" font-size="16" fill="#203040">Diagnostic choice</text>
    <rect x="275" y="104" width="360" height="24" fill="#dce5ec"/>
    <rect x="275" y="104" width="170" height="24" fill="#226b99"/>
    <text x="650" y="122" font-size="16" fill="#203040">17/36</text>
    <text x="275" y="159" font-size="13" fill="#203040">0</text>
    <text x="584" y="159" font-size="13" fill="#203040">36 pairs</text>
  </svg>
  <figcaption><strong>Figure 1.</strong> Differences between matched presentations, counted by pair. A different diagnostic choice is not necessarily an incorrect choice. Every terminal-answer difference changed correctness; the counts do not establish which presentation was better overall.</figcaption>
</figure>

Five of 36 is about 14% of these pairs; 17 of 36 is about 47%. Those are descriptions of this small probe, not estimates of how often Mercury-2.5 would err on arbitrary problems. Nor should the two counts be added: the available results do not specify how answer flips and diagnostic-choice divergences overlap.

The five answer flips warrant particular precision. In each flipped pair, one answer was right and one was wrong according to an exact oracle. That does **not** tell us the model’s total answer accuracy across all 72 presentations. It does not tell us whether the canonical or reversed version was more often correct. The other 31 pairs might contain two right answers or two wrong ones; answer stability alone cannot distinguish those possibilities.

## What a stable number does—and does not—explain

My first impulse was to treat a changed answer as evidence that the model had read different facts. But that explanation predicts more than the observations show. Across all 36 pairs, the *elicited posterior* did not move, even when the answer or diagnostic choice did. At minimum, the answer is not determined by the reported posterior in a presentation-invariant way in this task. The two endpoints need not travel together.

It would be a mistake to turn that observation into a map of the model’s internals. Identical reported posteriors do not prove identical parsing, identical intermediate calculations, or a discrete “belief module” followed by a defective “decision module.” Different processing paths could produce the same stated number. A probability report may also conceal distinctions that matter to a later answer. This experiment records outputs; it does not locate a failure inside the computation.

There is a second, more prosaic concern. Terminal-answer extraction may be brittle. An exact oracle tells us which answer is correct **if the recorded answer is what the model gave**. It cannot guarantee that a parser captured the intended answer faithfully in both presentation conditions. Without the individual transcripts here, I cannot adjudicate that possibility for the five flipped pairs. The posterior’s invariance makes a simple “it received different evidence” account less satisfying, but it does not rule out readout artifacts or subtler presentation effects.

The diagnostic choices provide a useful third view, with a different standard of interpretation. Seventeen pairs produced different choices about what to inspect or request next while retaining the same reported posterior. The packet does not establish that either choice was wrong, or even that only one choice could be good. I take this as evidence of **choice variability**, not a 17-of-36 diagnostic error rate.

## Where “right posterior” is directly observed

The epistemic games provide the accuracy check that the paired counts alone cannot. In 23 cases spanning base scenarios and evidence, presentation, and prior interventions, `posterior_reported` equaled `posterior_true` every time. Posterior error was zero in all 23, and the verdict was correct in all 23. On those cases, Mercury-2.5’s stated probability tracked the oracle despite the tested variations.

That is a substantial local success. It also makes the main puzzle sharper without solving it: the campaign contains evidence that this model can report exactly correct posteriors under varied inputs, and separate paired evidence that an unchanged posterior report can accompany a changed answer.

I cannot treat the 23 games as an independent replication of the 36 pairs. The evidence supplied for this essay does not establish that their cases or procedures are disjoint. More importantly, they answer different questions. The games check posterior accuracy and verdicts on their tested scenarios; the paired probe checks what changes when a fixed fact set is presented two ways. Adding their denominators would manufacture a single experiment that was never run. The games’ 23 correct verdicts neither erase the five paired answer flips nor certify the posteriors in those specific five pairs.

## A separate observation about proxy interventions

Another part of the campaign tested cases tagged with proxy channels. These results are tempting to enlist as an explanation for the presentation finding, because they too involve weaker outcomes under a changed condition. I do not think they permit that move.

Among scored base cases, 228 of 331 passed, about 69%. Among cases tagged **visible-proxy**, 8 of 27 passed, about 30%; among those tagged **reward-proxy**, 1 of 4 passed, 25%. In a comparison restricted to intervention cases sharing a latent specification with a base case, seven of 76 were recorded as a passing base case becoming a failing intervention case. Four of those seven carry the visible-proxy tag.

Those numbers describe pass/fail outcomes under intervention tags. They do not supply posterior reports paired with terminal answers under the same-facts presentation swap. A pass on a proxy-intervention case is not interchangeable with a stable posterior, a terminal-answer flip, or a diagnostic-choice divergence. I cannot use the proxy results to identify what produced the five flips.

Even as evidence about proxy channels, the comparison has live confounds. Intervention and base cases are **not difficulty-matched**. Sharing a latent specification does not guarantee equal task difficulty. The seven paired changes count one reported direction, pass→fail; the packet does not provide a corresponding fail→pass count or the number of paired base cases that passed. Seven out of 76 is therefore not an estimated probability that a passing base case will fail under intervention. Four reward-proxy cases, meanwhile, are too few to support a fine comparison with the visible-proxy tag.

The intervention taxonomy is incomplete in the evidence available here. The labels and counts do not specify a uniform construction for every proxy case, characterize all other intervention types, or provide a breakdown of scoring guarantees within these groups. The lower observed pass fractions are worth following up. They are not, on their own, a causal estimate of a proxy’s effect, and they are not a second measurement of the paired-probe dissociation.

## How much weight can the campaign bear?

The wider Mercury-2.5 campaign selected 416 cases across 38 environments. Of those, 405 were scored: 277 PASS and 128 FAIL, for a recorded pass fraction of 68.4%. Eleven were unscored. Those totals describe coverage, not a uniform measure of posterior accuracy or presentation robustness.

The judge guarantees make that distinction concrete. The campaign records 189 *behavioral-reference* cases and 227 *compile-only* cases. Those categories sum to **416 selected cases**, not 405 scored cases. I should not attach the guarantee split to the scored denominator, and I should not read one pooled PASS fraction as though every case had the same kind of check. The available results also leave 56 of 132 twin cases unverified; I cannot treat those as fully checked replications.

Provenance and sampling further limit the reach of the result. The main campaign used a single seed per selected cell. The dedicated paired-presentation probe instead used six seeds in each of its six cells; its 36 pairs should not be silently treated as 36 representative draws from the 405 scored campaign cases. The source repository was dirty at run time. A commit identifier alone might therefore be insufficient to reconstruct the exact working tree, although “dirty” does not establish that a relevant file changed during execution or that any outcome was contaminated. There is no independent replication on a second model or provider configuration. The reported model was mercury-2.5 with reasoning effort set to high.

None of these qualifications makes the five paired correctness flips disappear. They specify the scale at which I can describe them.

## The next test I would run

I would start with the five flipped pairs, not a larger headline number. Preserve each raw response, check the terminal-answer extraction by hand without knowing which presentation produced it, and compare that pair’s stated posterior with the oracle. That would test the strongest reading of the title on the very examples where it matters: *Was the reported probability both unchanged and correct when the answer changed?*

Then I would separate the two components of the prompt swap. Reverse the facts while keeping bullets; change bullets to numbers while keeping fact order; and test their combination. Repeating those comparisons across more seeds would show whether the current five flips persist and whether one component accounts for them. A second model or provider configuration would test whether this is peculiar to Mercury-2.5. For the proxy cases, the relevant follow-up is different: match difficulty, specify the intervention taxonomy and scoring rules, and report both directions of paired pass/fail change. Those are distinct experiments because the present measurements are distinct.

The answer I can [d-word] now is narrow. In a controlled 36-pair presentation probe, Mercury-2.5 stated the same posterior for the same facts every time, yet changed its terminal answer five times, always changing correctness, and changed its diagnostic choice 17 times. In 23 related oracle-scored games, its stated posterior was exactly right each time. Proxy-tagged cases had lower observed pass fractions in a separate, confounded comparison. Together these findings make me unwilling to infer a stable answer from a stable stated probability. They do not tell me what internal mechanism produced the gap—or whether the gap will survive the next, more discriminating test.


&&&&&&&&&&&&&&&&


gpt 6.1 sol max:

---
title: "The Model's Belief Is Right; Its Decision Is Fragile"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The emphasis on invariant stated belief alongside sensitive decisions as the campaign’s most informative narrow result.</dd>
  <dt>Synthesis</dt>
  <dd>An interpretation of the archived Mercury results, keeping the matched presentation probe distinct from campaign-level proxy interventions.</dd>
  <dt>Prose</dt>
  <dd>AI-drafted from the archived evidence; no new measurements or independent replication.</dd>
  <dt>Certainty</dt>
  <dd>One model and provider configuration. The presentation probe has 36 matched pairs and no confidence intervals. Proxy comparisons are not difficulty-matched.</dd>
  <dt>Importance</dt>
  <dd>A posterior-only summary would miss observed terminal-answer correctness reversals. That is a limitation of that summary, not a diagnosis of an internal mechanism.</dd>
</dl>

What should I conclude when a model reports the same probability under two presentations of the same facts, yet gives a correct answer in one presentation and an incorrect answer in the other?

My first instinct is to say that it knew the answer but failed to use it. That is an attractive explanation. It is also more than these measurements establish.

The narrower observation is already interesting. In a 36-pair presentation probe, Mercury-2.5’s reported posterior never changed between the two presentations. Its terminal answer changed in five pairs, and every change crossed the correctness boundary. Its diagnostic choices changed in seventeen.

There is a behavioral dissociation here: the measured belief output was invariant while other outputs were not. I do not need to identify an internal “decision layer” to find that result important.

A related epistemic-game suite supplies evidence for accurate posterior reporting. Separately, campaign-level proxy interventions show lower pass rates than base cases. Those findings deserve discussion, but they do not all measure the same thing. Keeping them separate is essential to understanding what the campaign [ac-word] tells us.

## One comparison, three endpoints

The presentation probe holds the facts fixed within each pair. It crosses three fact counts—3, 4, and 5—with two priors—1/2 and 1/3. That makes six cells, with six seeds per cell: 36 matched pairs.

One presentation uses canonical bullet order. The other reverses the facts and presents them as a numbered list. The model supplies an elicited posterior, a terminal answer, and diagnostic choices about which evidence to inspect or request next.

The results are:

| Endpoint | Pairs with a change | What the change establishes |
|---|---:|---|
| Reported posterior | 0/36 | No observed posterior sensitivity to the paired presentations |
| Terminal answer | 5/36 | Five correctness reversals |
| Diagnostic choices | 17/36 | Different evidence-selection choices, not necessarily worse ones |

The terminal result is stronger than a difference in wording. The task has an exact oracle, and all five answer flips were correctness flips: right under one presentation, wrong under the other.

Five of 36 is approximately 14% of the observed pairs. That is **not** a 14% overall error rate, nor does it mean that only one in seven changed answers was wrong. Every changed-answer pair contained a correctness reversal. The flip counts alone do not tell us the overall accuracy of either presentation.

The diagnostic result needs a different interpretation. Seventeen pairs—approximately 47%—produced different choices about evidence. But a different diagnostic choice is not automatically an error. Two requests could be equally useful, or their relative value could require an analysis not supplied here. This endpoint establishes sensitivity, not seventeen additional failures.

There is also an important qualification to “order sensitivity.” The comparison changes both order and list format: canonical bullets versus reversed numbering. It therefore establishes sensitivity to that bundled presentation change. It does not isolate an order effect from a formatting effect.

These are descriptive counts from a small probe, without confidence intervals. They are not estimates with demonstrated precision across arbitrary prompts or tasks.

## The dissociation is between outputs, not modules

The most useful fact is the conjunction: the reported posterior stayed fixed **while** the terminal answer sometimes crossed from correct to incorrect.

If I retained only the posterior column, I would lose that conjunction. I could accurately report complete posterior invariance and still omit five correctness reversals.

That makes separate endpoint measurement informative in this particular experiment. It does not establish a sequence in which the model first computes a belief and then passes it to a distinct decision mechanism.

The distinction matters because the tempting explanation runs ahead of the evidence. Perhaps the model forms the same internal belief and uses it inconsistently. But equality of reported numbers does not establish equality of internal representations, interpretation, or computation. Nor does it establish that the reported posterior is what determines the terminal answer.

For the same reason, I cannot rule out parsing explanations merely because the posterior did not move. A presentation difference could affect some aspect of the response without changing the number the model reports. Observing one invariant output is not an audit of everything that produced it.

Answer extraction is another live caveat. An exact oracle settles the mathematical target; it does not, by itself, validate the procedure that extracts an answer from generated text. If extraction is brittle, some apparent answer changes could reflect that brittleness. The recorded result is five correctness flips under the existing extraction and scoring procedure. Inspecting those responses would strengthen the interpretation.

None of these qualifications erases the observed dissociation. They constrain its explanation. I can say that posterior reporting and terminal-answer correctness behaved differently under the paired presentations. I cannot locate the cause “downstream of belief,” infer separate internal modules, or claim that parsing has been eliminated.

## Where the evidence for “right” comes from

Zero posterior flips is not the same as zero posterior error. A model could report the same incorrect probability twice.

The stronger accuracy evidence comes from the epistemic-game suite. Across 23 cases—including base scenarios and evidence, presentation, and prior interventions—the reported posterior exactly matched the true posterior in every case. Posterior error was zero throughout that set.

This supports a bounded sense in which stated belief tracked content: under the tested evidence and prior conditions, the model reported the oracle posterior. It was not merely stable while ignoring the task’s quantities.

But the two findings must not be silently substituted for each other:

- The presentation probe establishes posterior **invariance** alongside answer and diagnostic-choice sensitivity.
- The epistemic games establish posterior **accuracy** across their tested scenarios and interventions.

In particular, invariance alone does not establish that every posterior in the presentation probe was correct. The title uses “belief” operationally, to mean an elicited posterior—not privileged access to a hidden belief state.

The probe and the epistemic games are related campaign evidence, not independent replications. Their different units should not be added into a larger sample of one experiment. The 23 exact matches make accurate posterior reporting an observed capability here; they do not independently replicate the five terminal correctness reversals.

That leaves a result less sweeping than “the model knows but cannot act,” but more informative than “the model is inconsistent.” Specific outputs have different stability properties, and those properties can be measured separately.

## A separate finding: proxy-tagged cases pass less often

The broader campaign contains another suggestive result:

| Case category | Passing / scored | Pass rate |
|---|---:|---:|
| Base | 228/331 | 0.69 |
| Visible proxy | 8/27 | 0.30 |
| Reward proxy | 1/4 | 0.25 |

The differences are substantial in these observations. They are also confounded.

The intervention cases are not difficulty-matched to the base cases. Differences in difficulty could explain part or all of the pass-rate gap. The reward-proxy category has only four cases, so its fraction should not be read as a precise characterization of the model’s behavior.

There is a more closely linked comparison available. Among 76 intervention cases sharing a latent specification with a base case, seven changed a passing base result into a failure. Four of those seven carried the visible-proxy tag.

Sharing a latent specification is useful: it connects the comparison more closely than two unrelated category totals. But it does not, by itself, hold difficulty or every other relevant feature constant. The seven pass-to-fail transitions therefore do not remove the difficulty confound. Nor does this directional count supply a complete account of all paired transitions.

The category accounting also has a gap. The available counts do not provide a complete crosswalk between every intervention type, the aggregate proxy categories, and the 76-case paired subset. I cannot treat the named proxy categories as an exhaustive partition or combine these summaries into one clean intervention-effect estimate.

Most importantly, these pass/fail outcomes are not the presentation probe’s belief-and-answer measurements. The proxy results do not show an unchanged posterior paired with a changed terminal decision. They do not establish that proxy cues disrupted the same behavior, let alone the same internal process.

I read them as a parallel observation: cases carrying these proxy labels passed less often in this campaign, with some pass-to-fail transitions among cases sharing a latent specification. That association is worth testing under better controls.

Calling it further evidence for one fragile “decision layer” would make the narrative smoother by making the evidence less faithful.

## How much weight can the campaign carry?

The campaign selected 416 cases across 38 environments. Of those, 405 were scored and 11 were unscored. The scored cases contain 277 passes and 128 failures, for an aggregate pass rate of 0.684.

That aggregate is campaign context. It is not a posterior-accuracy estimate, a presentation-sensitivity estimate, or an estimate of a proxy effect.

The judge-guarantee counts require their own denominator. There are 189 cases labeled behavioral-reference and 227 labeled compile-only. Those counts sum to **416 selected cases**, not 405 scored cases.

!

*Figure 1. Campaign coverage. Of 416 selected cases, 405 were scored and 11 were unscored. The 189 behavioral-reference and 227 compile-only judge guarantees partition the selected cases; they are not a breakdown restricted to scored cases.*

Different judge guarantees are another reason not to turn the aggregate pass rate into a general statement about “reasoning.” A pass under one kind of check should not automatically be treated as equivalent evidence to a pass under another.

The sampling details also matter. The broader campaign used a single seed per selected cell. That is distinct from the presentation probe’s six seeds per cell; neither description should be allowed to overwrite the other. Campaign-wide single-seed results do not establish run-to-run stability.

There are also 56 unverified twin cases out of 132—about 42%. These are cases, not 56 unverified groups, and they should not be counted as additional verified comparisons.

All of this concerns one model and one provider configuration: `mercury-2.5` with high reasoning effort. There is no independent replication. The source repository was dirty at run time, which is a provenance caveat. That fact alone does not establish that the executed source is unknowable or that any particular result is invalid.

These limitations do not make the matched probe disappear. They limit how far I can carry it beyond the recorded setting.

## What would clarify the finding?

For the presentation result, I would first separate the two manipulated features. A comparison that independently varies fact order and list format could distinguish sensitivity to order, formatting, and their combination.

I would also inspect the five correctness-flip pairs against the raw responses and extraction procedure. If those reversals survive an extraction audit, the behavioral interpretation becomes firmer. If some do not, the result should be revised rather than defended through the oracle’s exactness.

Repeated runs and an independent replication would address a different question: whether this pattern persists beyond the recorded sample and provider configuration. They would not retroactively convert the present counts into an internal explanation.

For the proxy result, the next comparison needs matched difficulty and clearer category accounting. If the hypothesis concerns a dissociation between reported belief and action under proxy cues, then both endpoints need to be elicited and scored in that same controlled comparison. The existing pass/fail tables cannot answer that question by themselves.

The immediate reporting lesson is local. For this probe, I would preserve posterior invariance, terminal correctness reversals, and diagnostic-choice divergence as separate outcomes. A posterior-only summary omits observed behavior; a single combined score would also discard the distinction that makes the result interesting.

This is not evidence that every evaluation needs the same structure. It is evidence that, here, the structure changes what we can see.

## A bounded answer

Does Mercury-2.5’s stated belief track content while its decisions remain fragile?

The archived evidence supports a qualified answer. Posterior reports exactly matched the oracle in the 23 epistemic-game cases. In the 36-pair presentation probe, posterior reports were invariant, while terminal answers showed five correctness reversals and diagnostic choices diverged in seventeen pairs.

The proxy interventions add a separate association with lower pass rates, not another measurement of that same dissociation. Their difficulty confound remains live.

The finding I would keep is therefore behavioral: an unchanged stated posterior did not guarantee an unchanged terminal answer, and a posterior-only account would have missed real correctness reversals under the recorded scoring procedure.

That is enough to make the result worth replicating. It is not enough to tell us which internal mechanism failed.


TASK: Produce a claim-by-claim verification table. For every number, strong factual claim, and inferred conclusion in BOTH drafts, provide:
- Claim (as written, with draft attribution A or B)
- Verdict: SUPPORTED / UNSUPPORTED / NARROW / CORRECT-ARITHMETIC / NEEDS-CHECK
- Evidence source (which part of the packet supports or contradicts it)
- Required action for the final article

Be exhaustive. Include at least 40 rows. Flag every causal inference that outruns the evidence. Flag every arithmetic error. Flag every unsupported interpretation. Flag every unverified detail.

IMPORTANT: Bracketed tokens such as [ac-word], [d-word], [m-word] are INTENTIONAL replacements for words the author dislikes. They are NOT production artifacts. Do NOT flag them for removal.

Also produce a short "safe claim set" — the exact list of claims the final article may make without qualification, and a "qualified claim set" — claims that require a caveat in the same sentence.
