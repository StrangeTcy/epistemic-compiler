---
title: "Same Numerator, Three Denominators"
date: 2026-10-03
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>The framing of a campaign archive as a stack of stopping layers, and the claim that a pass rate is only legible once you say which layer it was taken from. The underlying evidence is one archived campaign; nothing here is a new evaluation principle.</dd>
  <dt>Synthesis</dt><dd>Written from an audited evidence packet prepared for this post in the Arena pipeline: a frozen archive of one paid Atria-Dawn-Preview campaign, finding records with stated confidence, a source-comparator audit, and a targeted (not systematic) prior-work check. I did not re-run any cases.</dd>
  <dt>Prose</dt><dd>Drafted in one pass from the packet; the argument structure is mine, the numbers are the packet's.</dd>
  <dt>Certainty</dt><dd>High for recorded counts and terminal notes; low for any causal reading of the difficulty axes, and low for the identity between the inspected source and what fuckingly ran, because the repository was recorded dirty.</dd>
  <dt>Importance</dt><dd>Moderate as a reading guide for this archive; modest as a general point, since the general point is old.</dd>
</dl>

I was handed the number 131 three times before I noticed it was the same number.

The first time it was 131 out of 194. The second time, 131 out of 193. The third, 131 out of 192. The passes never moved. Only the thing they were being divided by moved, and each division was quietly a different claim about what the campaign had measured.

That is the whole essay, really. A benchmark archive is not a scoreboard with some footnotes attached. It is a stack of places where a case can stop, and the number you report depends on which of those places you decided to stop counting at. Once I started reading the archive that way, most of the apparently interesting "difficulty" patterns in it turned into something else — not less interesting, but differently interesting, and much less flattering to the word *hard*.

## Where a case can stop

Let me lay out the stack as the archive records it, from the outside in.

Before any model was called, 24 cases were already out. Seventeen were omitted because the provider did not support the input modality those cases needed; seven were omitted before provider access because their calibration was already known to fail. Together with the 194 that were scored, that makes 218 case IDs the campaign accounts for. Those 24 have no model score. They are not failures, and they are not passes; they are cases the campaign never asked the question of.

Of the 194 that were scored, 131 passed and 63 failed. That is the raw checkpoint and it stays the raw checkpoint; I am not rewriting it.

Two of the 63 failures carry final-result notes attributing the terminal outcome to provider transients after bounded retries. Here the archive disagrees with itself in a small way: the campaign-level outage counter names only one episode, but two final rows carry the note. If you remove the one the report names, you get 131/193. If you remove both, you get 131/192. I use 192 below, and I want to be honest that it is an analysis choice layered on top of the report, not the report itself. My first instinct was to put 192 in a headline. It is the better denominator for asking about the model, but it is already an editorial act, and the point of this piece is that such acts should be visible.

Now the 61 remaining failures. The archive labels each with a failure mode, and the labels are worth reading literally rather than psychologically:

| Terminal label | Count | What the notes fuckingly say |
|---|---:|---|
| patch_invalid | 24 | every one an empty patch |
| underfit | 20 | ran, was judged, scored below threshold |
| source_invalid | 10 | rejected by the source validator before execution |
| runtime_error | 3 | crashed during execution |
| invalid_action | 2 | malformed action |
| overfit_visible_tests | 2 | trusted score of 1.0; a required companion file was missing |

Those last two rows are the ones that made me stop. The label says the submission overfit the visible tests. The note says the trusted test score was perfect and a required file was absent. Whatever happened there, "overfit" is not what the recorded evidence describes. I take this as a reminder that `failure_mode` is a campaign label, applied by a judge pipeline, and not a validated taxonomy of what the model was doing. It is a stopping layer with a name attached.

So of 61 failures, 24 never produced anything, 10 never got past a syntax or import check, 3 crashed, 2 were malformed, and 2 are mislabelled by their own notes. That leaves 20 cases where a program ran, was judged, and was judged wrong. Twenty is the number of behavioural misses in the plain sense of the phrase. The other 41 are something, but they are not that.

## Two judges wearing one colour

There is a second seam in the stack that the raw pass rate hides entirely. The 192 eligible cases were judged under two different guarantees. Seventy-two had an instance-specific behavioural reference — the judge knew what this particular task's correct behaviour was. One hundred and twenty were compile-only, and the campaign report itself calls those verdicts exploratory and keeps them out of any validated aggregate.

The split in outcomes: behavioural-reference cases went 56 pass, 16 fail. Compile-only cases went 75 pass, 45 fail (47 before removing the two provider-terminal rows).

Why does this matter beyond bookkeeping? Because the families the archive groups into "tracks" mix the two guarantees unevenly. The weird-machine track is entirely behavioural-reference: all 30 of its eligible cases. The recurrent-depth family is 11 behavioural-reference and 22 compile-only. The three ML-debugging environments split 19 and 11. A green cell in one track and a green cell in another are not the same observation. One says *the judge checked this instance's behaviour and it was right*. The other says *it compiled and cleared an exploratory check*. Colouring them the same shade is not a lie, exactly, but it is a design decision that makes the map harder to read than the data underneath it.

Within the compile-only families the point sharpens. The gradient-credit environment went 11 for 11 and the BatchNorm EMA environment went 0 for 11, both compile-only. I genuinely do not know how to compare those two numbers to the MoCo environment's 9 of 11 under behavioural reference, and I think the correct response to not knowing is to not pretend.

## What the difficulty knobs fuckingly turn

With the layers in view, I can look at the part of the archive that invites the most tempting story: the easy/medium/hard axes.

The regex state-machine environment is where the pattern looks cleanest, so start there. Its "hidden depth" axis is input-string length: 32, 128, or 512 characters. With the surface label held at easy, the selected run passes all three lengths. Hold length at 32 instead and sweep the surface label, and medium and hard both fail — underfit, same partial score, with the notes recording that the output came back 34 and 66 characters long against a 32-character input. Length preservation is the whole game in a Rule-110-style task, so those are real behavioural misses, judged against a behavioural reference.

That looks like a surface effect. Is it? The clean source comparator says the surface levels also change class names, and the hard prompt carries an extra performance hint the easy prompt does not. So the manipulation is a bundle: label, name, hint. There is one seed-0 run per cell. And the archive records the repository as dirty at the time of the run, which means the comparator I just described is a comparator, not a transcript of what ran. The contrast is sharp and it is real for these cases. It does not isolate a cause.

CSS is where the layers really earn their keep. Sweep hidden depth at easy surface and you get, over 3, 4, and 5 bits: a partial score of about 0.42, a zero, and a pass. Read as a difficulty curve it is non-monotone and strange. Read by layer it dissolves: the zero at 4 bits is a source-validator rejection because the submission imported `re`, which was disallowed. That is not the model failing to solve a four-bit state machine. It is the model never being allowed to try. The 3-bit case *is* a judged behavioural miss; the 4-bit case is a validator stop; the 5-bit case passed. Three different layers, one row of a table.

SQL repeats the shape. At easy surface, chain lengths 6 and 25 pass; length 12 fails. The length-12 failure is an unterminated triple-quoted string caught by the source validator. Whatever one wants to say about a model that produces an unterminated string literal, "the medium-depth SQL task was harder" is not supported by this row.

The recurrent-depth adaptive-halting environment does the same thing from the other side. The easy-depth case fails and medium and hard pass — exactly backwards from the staircase story — but the easy-depth failure is an unexpected-indentation syntax error. Another failure in that environment is a runtime error from using a float tensor as a boolean condition. Those are failures. They are not depth-related failures in any sense the axis name promises.

And MoCo's visible-test axis goes pass, fail, pass, where the middle fail is the case I described above: trusted score 1.0, required companion file missing, labelled overfit.

So when I sort the selected axis sweeps by what fuckingly stopped each failing case, I get this:

- Regex surface sweep at length 32: two behavioural misses (length drift), confounded by name and hint changes.
- CSS depth sweep: one behavioural miss, one validator stop, one pass.
- CSS surface sweep at 3 bits: one behavioural miss, two passes.
- SQL depth sweep: one validator stop, two passes.
- Adaptive-halting depth sweep: one validator stop, two passes.
- MoCo visible-test sweep: one mislabelled missing-file case, two passes.
- Spreadsheet, both sweeps: six passes.

Of the apparently non-monotone contrasts, most are non-monotone at the validator or packaging layer, not at the judge. That is not nothing — a model that cannot terminate its string literals is telling you something — but it is a different something from "hidden depth medium is harder than hidden depth hard," and the environment-level totals (CSS 3/5, SQL 4/5, adaptive halting 9/11) flatten the distinction entirely.

## The comparator is not the source

I have been leaning on the clean comparator to explain what the axes do, so I should say plainly how much weight it bears.

The archive points at a specific commit and records the working tree as dirty. All 33 selected configuration hashes match the clean snapshot of that commit. That is reassuring about the configs. It is not evidence about the task templates, visible tests, judge code, or helper files, any of which could have differed in the working tree without touching a config hash. Every time I wrote "the comparator shows" above, read it as "the clean version of the code shows, and I cannot confirm the paid run used the clean version."

There is a further complication in the category track, which I have mostly left alone here because its outcomes are heterogeneous code-repair results rather than anything a single number summarises. A static scan of the clean comparator found ten advertised control or variable axes across nine category environments with no reference in the environment templates — both axes of the compositional-optimizer environment among them. If that scan is right about what ran, then some of the nominal design cells differ from their neighbours in name only, and the count of distinct interventions is smaller than the manifest implies. The finding is inferred, not observed: the scan did not execute generation or inspect every rendered bundle, and the dirty flag means it is a statement about the comparator. But it is one more reason not to read the axis grid as a grid of experiments.

## What the sampling can bear

One selected seed per cell. No cell-level replication. Most contrasts are single-factor substitutions around one baseline, not factorial designs. Later passes over the archive — editorial, analytic, the one that produced this essay — reread the same 194 rows; none of them are new draws.

Under those conditions, what are the family totals? Recurrent depth: 31 of 33. Trajectory synthesis: 2 of 8. Weird machine: 25 of 30. ML debugging: 9 of 30, carried almost entirely by MoCo, with the glyph environment at 0 of 8 under behavioural reference and BatchNorm EMA at 0 of 11 compile-only.

Those are descriptions of what this model, under this provider, with these prompts and judges, did on these selected cases once. The families are collections of different code tasks at different sizes with different tests and different scoring modes. Nothing calibrates them to a shared construct, and a 94% next to a 25% is not a measurement of how much easier recurrence is than synthesis. It is two measurements of two different things that happen to share a page.

None of this is a new complaint. HELM made broad scenario coverage with multiple reported metrics the expected shape of a serious evaluation ([Liang et al., 2023](https://arxiv.org/abs/2211.09110)). VarBench perturbs task variables dynamically and reports variable-based experiments across five sampled seeds rather than one ([Qian et al., 2024](https://aclanthology.org/2024.findings-emnlp.946/)). I cite them as precedent for the modest version of the lesson — report what each score means, and replicate before calling a contrast an effect — not as validation of anything in this archive. The prior-work check behind this post was targeted, not exhaustive, and supports no claim of novelty.

## What the archive licenses

Here is what I think the evidence fuckingly permits.

It permits saying that in this one campaign, 131 of 194 scored selected cases passed; that 24 further cases were never scored and are neither; that two of the 63 failures are provider-terminal and can be defensibly set aside to give 131 of 192; and that any of those three fractions is fine so long as it travels with its denominator.

It permits saying that the 61 eligible failures stop at at least five different layers, that only about twenty of them are behavioural misses in the judged sense, and that two carry labels their own notes contradict.

It permits saying that the regex surface contrast is sharp for the cases that exist, that several of the other non-monotone axis sweeps are non-monotone at the validator rather than at the judge, and that the easy/medium/hard labels name different quantities in different environments and share no common scale.

It does not permit a claim that surface form, string length, bit width, or recurrence depth *caused* any of these outcomes. It does not permit treating compile-only passes as a validated behavioural aggregate. It does not permit a ranking of this model's capabilities across families, or a ranking of the families by difficulty. And it does not permit treating the clean comparator as the source that ran.

What it does give, and what I think is worth keeping, is a list of specific cases and specific implementations that need to be looked at: the two mislabelled missing-file rows, the ten source-validator stops, the twenty-four empty patches, the regex name-and-hint bundle, the ten axes the comparator cannot find. The useful follow-up is not a bigger sweep. It is to verify what each axis renders, unbundle the names from the hints, run more than one seed per cell, and then — only then — report pass rates by judge guarantee and by stopping layer, so that the next person who is handed 131 three times knows, each time, what it is 131 of.
