opus 5:

I'll assemble the final article with all Stage D corrections, build the new Figure 2 SVG, and save the file.Final article saved and exported to `campaign-02-analysis/posts/POST-01-belief-right-decision-fragile.md` (~3,450 words, both figures inline).

## Compliance summary

**Deletions applied (Stage D 1–6):** "verdict correct in all 23" and both downstream "verdicts" uses removed (games section now says only `posterior_reported = posterior_true`, zero error); "across 38 environments" struck from the campaign section; B's garbled "one in seven" sentence deleted; both 👹 glyphs replaced with `[m-word]`; B's `!` placeholder replaced with a real Figure 2 SVG; B's row-44 "not merely stable while ignoring the task's quantities" deleted.

**Required additions (7–12):** new subsection "The null this probe does not have" carries the sampling-noise null with the 2p(1−p) illustration explicitly labeled hypothetical (p=0.08 → ~5.3/36), the chance-agreement caveat for diagnostic choices (k unrecorded; k=2 → ~18/36), and the pre-specification-not-recorded statement. Posterior invariance is framed as a possible floor effect; the undefined answer-to-posterior relationship is stated plainly; the per-cell flip distribution is stated as unavailable.

**Narrow-claim hedging:** "presentation sensitivity" → "differences between presentations"; 17/36 → "divergence, not error" with chance caveat; five flips always "under the recorded extraction procedure"; A33 rewritten so internal readings are declared undeterminable (no purported prediction); A42 demoted to a labeled intuition; A48/B41 → "matched the true posterior in those 23 cases"; B48 → "recorded outputs had different flip counts"; proxy numbers descriptive with n=4 and difficulty caveats; 7/76 flagged one-directional, not a transition probability; 0.684 flagged as pooling two judge types; games labeled related campaign evidence, not replication; dirty repo stated as provenance only; T1-inside-405 stated as unspecified.

**Conservative editorial path taken:** `reasoning_effort=high`, "latent specification" (→ "base-linked"), and the game intervention types are all removed. Flag for editor: all three are in the packet, so override is available if you want them restored.

**Imports from B:** three-endpoint table, "The dissociation is between outputs, not modules" header, the "zero flips ≠ zero error" couplet, and the titled coda "A bounded answer." Figure 1 (A's three-endpoint SVG) kept as-is; Figure 2 is new, with both bar rows on one 416-case scale so the 189+227=416 vs. 405 distinction is visually unambiguous. `[ac-word]`, `[d-word]`, `[m-word]` preserved (1/2/2 occurrences).

<okay, this is unintentionally pretty funny>

&&&&&&&&&&&&&&&&

fable 5.1:

---
title: "The Model's Belief Is Right; Its Decision Is Fragile"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The paired-presentation result is most useful as a narrow dissociation between a stated posterior and the other responses recorded alongside it.</dd>
  <dt>Synthesis</dt>
  <dd>Draws on the archived paired probe, the epistemic games, the proxy-intervention results, and campaign coverage. These are treated as distinct measurements and are not pooled.</dd>
  <dt>Prose</dt>
  <dd>Written from verified aggregate results, without access to individual prompt-and-response transcripts for this essay.</dd>
  <dt>Certainty</dt>
  <dd>The reported counts are specific; the interpretation is bounded by 36 matched pairs with no confidence intervals, no same-presentation re-run baseline, possible extraction errors, one model and provider configuration, and no independent replication.</dd>
  <dt>Importance</dt>
  <dd>A stable probability report did not guarantee a stable answer in this probe. That is a reason to examine both readouts, not a general theory of how the model decides.</dd>
</dl>

If a model gives the same probability after seeing the same facts in two presentations, should it also give the same answer? I would have expected so, at least in a task with an exact oracle. Mercury-2.5 did not always oblige. In 36 matched pairs, its reported posterior was identical across the two presentations in every pair. Its terminal answer differed in five pairs, and each of those five differences was also a correctness difference under the recorded extraction procedure: one presentation elicited the right answer and the other the wrong one. Its choice of what evidence to inspect or request next differed in 17 pairs.

There is an important restraint hidden in the title. *Belief* means the posterior the model stated, not an internal state I can inspect. *Right* is established by a related set of 23 oracle-scored epistemic games, in which every reported posterior matched the true posterior; it is supported for those 23 cases and nowhere else. The aggregate evidence does **not** tell me that the stated posterior was oracle-correct in each of the five paired-presentation trials whose answers flipped. In the paired probe, the direct finding is invariance of the reported number alongside variability of the answer. I want to keep that finding intact rather than strengthen it by quietly merging two sets of results. Keeping the measurements separate is essential to understanding what the campaign [ac-word] tells us.

## Hold the facts fixed; change their presentation

The paired probe crosses three fact counts—three, four, and five—with two priors, 1/2 and 1/3. That makes six cells, each tested with six seeds: 36 matched pairs. Within a pair, the facts and prior stay the same. One prompt puts the facts in a canonical bullet order; the other reverses them in a numbered list. The model is asked for a posterior, a terminal answer, and a diagnostic choice about which evidence to inspect or request next. The oracle for the posterior is exact.

Consider what a single cell specifies. With four facts and a prior of 1/3, each of its six pairs compares two presentations of those same four facts. The per-cell distribution of the five answer flips is not available in the recorded results, so I cannot say whether any flip occurred in that particular cell. It would be easy to invent a vivid example of one; it would not be evidence.

The manipulation also has a small but consequential complication. It changes **both sequence and format**: canonical bullets become reversed numbered items. The two features co-vary and neither is isolated. "Differences between presentations" is therefore the [d-word] description. The probe cannot, by itself, assign the difference specifically to position in the list rather than numbering, or to an interaction between them.

Two further things are not recorded. Whether this probe was pre-specified before the campaign ran, or designed after other results were in hand, is not stated in the materials available to me. And whether its 36 pairs sit inside the 405 scored campaign cases or were run alongside them is unspecified.

## Three endpoints, counted by pair

| Endpoint | Pairs with a difference | What the difference establishes |
|---|---:|---|
| Reported posterior | 0/36 | No observed difference in the reported number between the paired presentations |
| Terminal answer | 5/36 | Five correctness reversals under the recorded extraction procedure |
| Diagnostic choice | 17/36 | Different evidence-selection choices, not necessarily worse ones |

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

The five answer flips warrant particular precision. In each flipped pair, one answer was right and one was wrong according to an exact oracle, as recorded by the extraction procedure. That does **not** tell us the model's total answer accuracy across all 72 presentations. It does not tell us whether the canonical or reversed version was more often correct. The other 31 pairs might contain two right answers or two wrong ones; answer stability alone cannot distinguish those possibilities.

There is a null I cannot reject with this design. The probe has no same-presentation re-run baseline: nobody ran the canonical prompt twice with the same seed configuration and counted how often the answer differed from itself. Without that baseline, five differences out of 36 could be sampling noise rather than anything about the presentation. As a purely hypothetical illustration: if a single presentation produced the correct answer independently with probability *p* on each run, two draws would disagree with probability 2*p*(1−*p*). At *p* = 0.9 that is 0.18, or roughly six or seven disagreements in 36 pairs; at *p* = 0.93 it is about 0.13, or roughly five. The observed 5/36 is consistent with such a noise process at plausible accuracy levels. I have no estimate of the actual *p*, and the illustration is not a claim about the model. It is a reason to describe the result as "differences between presentations" rather than "presentation sensitivity."

A similar caution applies to the diagnostic column. The recorded results do not state *k*, the number of diagnostic options the model chose among. Without *k*, 17 of 36 cannot be compared to chance agreement. If, hypothetically, there were two options chosen independently and uniformly, two draws would differ about half the time—roughly 18 of 36—and 17 would be unremarkable. With more options, chance disagreement would be higher still. The packet does not establish that either choice in a divergent pair was wrong, or that only one choice could be good. I take this column as evidence of **divergence, not error**, and I cannot say whether the divergence exceeds what chance would produce.

## The dissociation is between outputs, not modules

My first impulse was to treat a changed answer as evidence that the model had read different facts. The recorded outputs cannot determine what the model read internally; nothing in the packet reaches that level. What the outputs do show is that across all 36 pairs the *elicited posterior* did not move, even when the answer or diagnostic choice did. At minimum, the answer was not determined by the reported posterior in a presentation-invariant way in this probe. The two endpoints need not travel together.

Two caveats attach directly to that sentence. First, the task specification does not define how the terminal answer should relate to the posterior. If there is no stated rule mapping a probability to an answer, then "same posterior, different answer" is a description of two recorded outputs, not a violation of a specified contract. Second, the posterior's invariance may be a floor effect. In the 23 epistemic games the model reported the exact oracle posterior every time, which suggests that computing this posterior is an easy, effectively deterministic task for it. A number that is easy to get exactly right will also be easy to get identically twice. Zero flips out of 36 may therefore reflect the ease of the computation rather than robustness in any broader sense.

It would be a mistake to turn the observation into a map of the model's internals. Identical reported posteriors do not prove identical parsing, identical intermediate calculations, or a discrete "belief module" followed by a defective "decision module." Different processing paths could produce the same stated number. A probability report may also conceal distinctions that matter to a later answer. This experiment records outputs; it does not locate a failure inside the computation.

There is a second, more prosaic concern. Terminal-answer extraction may be brittle. An exact oracle tells us which answer is correct **if the recorded answer is what the model gave**. It cannot guarantee that a parser captured the intended answer faithfully in both presentation conditions. Without the individual transcripts here, I cannot adjudicate that possibility for the five flipped pairs. My intuition is that an unchanged posterior sits awkwardly with a simple "it received different evidence" story, but the data do not rank that account against readout artifacts, sampling noise, or subtler presentation effects, and I will not pretend they do.

## Where "right posterior" is directly observed

Zero posterior flips is not the same as zero posterior error. A model could report the same incorrect probability twice.

The accuracy evidence comes instead from the epistemic games. In 23 cases, including base scenarios and intervention variants, `posterior_reported` equaled `posterior_true` every time. Posterior error was zero in all 23. On those cases, Mercury-2.5's stated probability matched the true posterior in those 23 cases—and that is the full extent of what "right" in the title means. I can say that reported posteriors matched true posteriors in 23 tested cases; I cannot say that stated belief tracked content in general, because the packet does not tell me which interventions changed the true posterior and which left it fixed.

That is a substantial local success. It also makes the main puzzle sharper without solving it: the campaign contains evidence that this model can report exactly correct posteriors in a related task, and separate paired evidence that an unchanged posterior report can accompany a changed answer.

But the two findings must not be silently substituted for each other:

- The presentation probe establishes posterior **invariance** alongside answer and diagnostic-choice differences.
- The epistemic games establish posterior **accuracy** across their 23 tested cases.

Invariance alone does not establish that every posterior in the presentation probe was correct. I cannot treat the 23 games as an independent replication of the 36 pairs; they are related campaign evidence from the same model and provider configuration. The evidence supplied for this essay does not establish that their cases or procedures are disjoint. More importantly, they answer different questions. Adding their denominators would manufacture a single experiment that was never run. The 23 exact matches neither erase the five paired answer flips nor certify the posteriors in those specific five pairs.

What remains is less sweeping than "the model knows but cannot act," but more informative than "the model is inconsistent": the recorded outputs had different flip counts in this probe, and those counts can be reported separately.

## A separate observation about proxy interventions

Another part of the campaign tested cases tagged with proxy channels. These results are tempting to enlist as an explanation for the presentation finding, because they too involve weaker outcomes under a changed condition. I do not think they permit that move.

| Case category | Passing / scored | Pass fraction |
|---|---:|---:|
| Base | 228/331 | 0.69 |
| Visible proxy | 8/27 | 0.30 |
| Reward proxy | 1/4 | 0.25 |

The differences are large in these observations, and they are also confounded. Intervention and base cases are **not difficulty-matched**; differences in difficulty could, as a live possibility, explain part or all of the gap. Four reward-proxy cases are too few to support a fine comparison with the visible-proxy tag. I read the table as descriptive: cases carrying these labels passed less often in this campaign.

There is a more closely linked comparison. Among 76 intervention cases linked to a base case, seven were recorded as a passing base case becoming a failing intervention case. Four of those seven carry the visible-proxy tag. The seven count one direction only, pass→fail; the packet does not provide a corresponding fail→pass count or the number of linked base cases that passed. Seven out of 76 is therefore not a transition probability, and being linked to a base case does not by itself hold difficulty constant.

Most importantly, these pass/fail outcomes are not the presentation probe's belief-and-answer measurements. The supplied proxy results do not report a paired measurement of an unchanged posterior alongside a changed terminal answer. A pass on a proxy-intervention case is not interchangeable with a stable posterior, a terminal-answer flip, or a diagnostic-choice divergence. I cannot use the proxy results to identify what produced the five flips. The intervention taxonomy is also incomplete in the evidence available here: the labels and counts do not specify a uniform construction for every proxy case, characterize all other intervention types, or provide a crosswalk between the category totals and the 76-case linked subset.

The lower observed pass fractions are worth following up. They are not, on their own, a causal estimate of a proxy's effect, and they are not a second measurement of the paired-probe dissociation. Calling them further evidence for one fragile "decision layer" would make the narrative smoother by making the evidence less faithful.

## How much weight can the campaign bear?

The wider Mercury-2.5 campaign selected 416 cases. Of those, 405 were scored: 277 PASS and 128 FAIL, for a recorded pass fraction of 0.684. Eleven were unscored. That aggregate pools two kinds of judge and says nothing about posterior accuracy or presentation robustness; it describes coverage.

The judge guarantees make that distinction concrete. The campaign records 189 *behavioral-reference* cases and 227 *compile-only* cases. Those categories sum to **416 selected cases**, not 405 scored cases. I should not attach the guarantee split to the scored denominator, and I should not read one pooled PASS fraction as though every case had the same kind of check.

<figure>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 210" role="img" aria-labelledby="campaign-figure-title campaign-figure-description" style="max-width: 100%; height: auto;">
    <title id="campaign-figure-title">Campaign denominators: 416 selected cases split two ways</title>
    <desc id="campaign-figure-description">Top bar: of 416 selected cases, 405 were scored, comprising 277 PASS and 128 FAIL, and 11 were unscored. Bottom bar: the same 416 selected cases comprise 189 behavioral-reference and 227 compile-only judge guarantees. The judge split partitions selected cases, not scored cases.</desc>
    <rect x="0" y="0" width="760" height="210" fill="#ffffff"/>
    <text x="8" y="24" font-size="15" fill="#203040">Scoring outcome (416 selected)</text>
    <rect x="80" y="36" width="399.5" height="30" fill="#226b99"/>
    <rect x="479.5" y="36" width="184.6" height="30" fill="#7fa7c4"/>
    <rect x="664.1" y="36" width="15.9" height="30" fill="#c8c8c8"/>
    <text x="90" y="57" font-size="14" fill="#ffffff">277 PASS</text>
    <text x="490" y="57" font-size="14" fill="#ffffff">128 FAIL</text>
    <text x="684" y="57" font-size="13" fill="#203040">11</text>
    <text x="80" y="86" font-size="13" fill="#203040">405 scored (0.684 PASS)</text>
    <text x="620" y="86" font-size="13" fill="#203040">11 unscored</text>
    <text x="8" y="124" font-size="15" fill="#203040">Judge guarantee (416 selected)</text>
    <rect x="80" y="136" width="272.6" height="30" fill="#3f6f55"/>
    <rect x="352.6" y="136" width="327.4" height="30" fill="#9bbfa9"/>
    <text x="90" y="157" font-size="14" fill="#ffffff">189 behavioral-reference</text>
    <text x="362" y="157" font-size="14" fill="#203040">227 compile-only</text>
    <text x="80" y="190" font-size="13" fill="#203040">0</text>
    <text x="600" y="190" font-size="13" fill="#203040">416 selected</text>
  </svg>
  <figcaption><strong>Figure 2.</strong> Campaign denominators. Of 416 selected cases, 405 were scored (277 PASS, 128 FAIL) and 11 were unscored. The 189 behavioral-reference and 227 compile-only judge guarantees partition the 416 selected cases, not the 405 scored ones.</figcaption>
</figure>

The available results also leave 56 of 132 twin cases unverified—about 42%. These are cases, not groups, and I cannot treat them as fully checked replications.

Provenance and sampling further limit the reach of the result. The main campaign used a single seed per selected cell, so campaign-wide results do not establish run-to-run stability. The dedicated paired-presentation probe instead used six seeds in each of its six cells; neither description should overwrite the other, and the probe's 36 pairs should not be treated as 36 representative draws from the 405 scored cases. The source repository was marked dirty at run time. That is a provenance caveat—a commit identifier alone may not reconstruct the exact working tree—and I do not read it as evidence of contamination. All of this concerns one model and one provider configuration, mercury-2.5, with no independent replication.

None of these qualifications makes the five paired correctness flips disappear. They specify the scale at which I can describe them.

## The next test I would run

I would start with a same-presentation re-run baseline, because without it the sampling-noise null stands. Run each presentation against itself under the same seed configuration and count how often the terminal answer disagrees with itself. If that rate is near 14%, the five flips carry no information about presentation; if it is near zero, they do.

Then I would go to the five flipped pairs. Preserve each raw response, check the terminal-answer extraction by hand without knowing which presentation produced it, and compare that pair's stated posterior with the oracle. That would test the strongest reading of the title on the very examples where it [m-word]: *Was the reported probability both unchanged and correct when the answer changed?* It would also require a stated rule for how an answer should follow from a posterior, which the current task specification does not supply.

Then I would separate the two components of the prompt swap. Reverse the facts while keeping bullets; change bullets to numbers while keeping fact order; and test their combination. For the diagnostic endpoint, record *k* and a chance baseline. Repeating those comparisons across more seeds would show whether the current five flips persist and whether one component accounts for them. A second model or provider configuration would test whether this is peculiar to Mercury-2.5. For the proxy cases, the follow-up is different: match difficulty, specify the intervention taxonomy and scoring rules, report both directions of paired pass/fail change, and elicit both a posterior and an answer in the same controlled comparison. Those are distinct experiments because the present measurements are distinct.

## A bounded answer

Does Mercury-2.5's stated belief track content while its decisions remain fragile?

The answer I can [d-word] now is narrower than that question. Two observations, from two samples, stand on their own. In 23 related oracle-scored games, the reported posterior matched the true posterior every time. In a 36-pair presentation probe, the reported posterior was the same in every pair, the terminal answer differed in five pairs—each a correctness reversal under the recorded extraction procedure—and the diagnostic choice differed in 17, a count I cannot compare to chance.

The proxy interventions add a separate, confounded association with lower pass fractions, not another measurement of that dissociation.

The finding I would keep is behavioral and local: in this probe, an unchanged reported posterior did not guarantee an unchanged terminal answer, and a posterior-only summary would have omitted recorded correctness reversals. The invariance may be a floor effect; the flips may be noise; the extraction may be brittle; the task never said how an answer should follow from a posterior. That is enough to make the result worth replicating with the controls it currently lacks. It is not enough to tell me which internal mechanism, if any, failed.
