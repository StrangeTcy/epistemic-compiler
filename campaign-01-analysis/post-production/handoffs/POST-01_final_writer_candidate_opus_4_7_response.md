```markdown
---
title: "A Benchmark Grid Is Not a Difficulty Scale"
date: 2026-10-03
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt><dd>Modest. The reframing — that a colored cell in a benchmark grid compresses a denominator choice, a judge guarantee, and a stopping layer into one symbol — is mine for this archive. The general lesson that evaluations should expose what each score means is old.</dd>
  <dt>Synthesis</dt><dd>From an audited evidence packet prepared for this essay: a frozen snapshot of a single completed paid campaign (one model, one provider, one configuration), per-case finding records, a source-comparator audit, and a targeted prior-work check. I did not re-run any cases, and nothing here is an independent replication.</dd>
  <dt>Prose</dt><dd>Drafted in one pass from the packet. The argument structure is mine; the counts are the archive's.</dd>
  <dt>Certainty</dt><dd>High for the recorded counts, terminal notes, and the config-hash match. Low for any causal reading of a "difficulty" axis. Low for identity between the inspected comparator and the code that fuckingly produced the paid results, because the campaign repository was recorded as dirty.</dd>
  <dt>Importance</dt><dd>Moderate as a reading guide for this archive and others like it. Low as a general methodological point, which has been made before.</dd>
</dl>

I was handed the number 131 three times before I noticed it had not moved.

The first time it was 131 out of 194. The second time, 131 out of 193. The third, 131 out of 192. The passes stayed where they were. Only what they were being divided by changed, and each division was quietly a different claim about what the campaign had measured.

That is the whole essay, in a sense. A benchmark archive is not a scoreboard with footnotes. It is a stack of places where a case can stop — before provider access, inside the source validator, in the runtime, inside the judge — and the number you quote depends on which of those places you decide to stop counting at. Once I read this archive that way, most of the apparently interesting "difficulty" patterns in it stopped being about difficulty.

## Three defensible denominators

Before any model was called, 24 cases were already out. Seventeen were omitted because the provider could not accept their input modality; seven were gate-blocked before provider access for known calibration failures. Together with the 194 that did get scored, the campaign accounts for 218 case IDs. Those 24 have no model score. Counting them as either passes or failures would be inventing data.

Of the 194 that were scored, 131 passed and 63 failed. That is the raw checkpoint, and I am not rewriting it.

Two of the 63 failures carry final-result notes attributing the terminal outcome to provider transients after bounded retries. Here the archive disagrees with itself, mildly: the campaign-level outage counter names one such episode, but two final rows carry the terminal provider note. There are therefore three defensible denominators, and I will keep them visibly distinct:

| Exclusion | PASS / total | FAIL |
|---|---|---|
| None (raw checkpoint) | 131 / 194 | 63 |
| Only the report-listed transient | 131 / 193 | 62 |
| Both provider-coded terminal rows | 131 / 192 | 61 |

For performance analysis I work from the 192-case set, because a terminal provider failure is not the model missing a problem; it is the infrastructure refusing to let it try. But that choice is an analysis layered on top of the campaign report, not the report itself, and I would rather name it as such than hide it behind a headline. Both of the provider-coded rows happen to sit in the compile-only pool, which matters for the next cut.

## Two judges wearing the same color

The 192 eligible cases split under two different judge guarantees that the grid renders identically and that mean entirely different things.

There are 72 cases with an instance-specific behavioral reference, which went 56 PASS / 16 FAIL. There are 120 compile-only cases, which went 75 PASS / 45 FAIL (47 before the two provider exclusions). A behavioral-reference verdict checks the submission against a reference for *this* task's correct behavior. A compile-only verdict checks that the submission builds and clears visible checks; the campaign report itself calls these verdicts *exploratory* and does not fold them into a validated behavioral aggregate.

So any honest aggregate from this archive reports those two pools side by side. A green compile-only cell says *this ran and cleared an exploratory check*. A green behavioral-reference cell says *this did what the task required against a reference the model did not see*. Averaging them produces a number that answers no question. One environment, the epistemic-games track, additionally carries an environment-level behavioral self-test that was recorded as executed and passing; that is a preflight for the environment, not a per-case guarantee, and the two should not be conflated.

A standing caveat sits under all of this. The archive points at a specific source commit and records the working tree as dirty. All 33 selected configuration hashes match a clean comparator of that commit, which is reassuring about configs — and only about configs. It is not byte-for-byte proof that the task templates, visible tests, judge code, or helper files in the paid runs were exactly the inspected clean versions. Every statement below of the form *the source does X* should be read as *the clean comparator does X, and I cannot confirm the paid run used the clean comparator*.

## "Difficulty" is a different quantity in each room

With denominator and judge in view, I can look at the part of the archive that most invites a story: the `easy` / `medium` / `hard` axes. They look like a staircase. They are not even measuring the same building.

In the regex state-machine environment — a Rule-110-flavored construction, which I mention only to describe the task, not to imply anything about general computation — the "hidden depth" knob is literally input-string length: 32, 128, or 512 characters. Hold the surface label at easy and the selected run passes all three lengths. Hold the length at 32 instead and sweep the surface label, and the medium and hard variants fail: the returned string grows to 34 and then 66 characters against a 32-character input. Length preservation is the whole game in a task like this, so those are real behavioral misses, judged against a behavioral reference. One seed per cell.

Is that a *surface* effect? The clean comparator says the surface labels also rename classes, and that the hard-level prompt carries an extra performance hint the easy prompt does not. So the manipulation is a bundle of at least three changes — label, name, hint — and with the repository dirty I cannot even confirm the paid run saw that bundle. The contrast is sharp. It does not isolate a cause.

CSS makes the word travel worse. There "hidden depth" is a bit count. At easy surface, over 3, 4, and 5 bits, the selected run scores a partial 0.42, then a 0, then a 1. Read as a difficulty curve it is non-monotone and strange. Read by stopping layer it dissolves: the 0 at 4 bits is a source-validator rejection, because the submission imported `re`, which was disallowed. That is not the model failing a 4-bit state machine. It is the model never being allowed to try. The environment total of 3/5 silently contains one partial-credit behavioral case, one validator rejection, one validator-related zero, and clean passes — all painted as "three green, two red."

SQL does it again with a third physical quantity. The depth knob is graph-chain length. At easy surface, chain lengths 6 and 25 pass; length 12 fails. The length-12 failure is an unterminated triple-quoted string caught by the source validator before anything behavioral was tested. Whatever one wants to say about a model that emits an unterminated string literal, "the medium-depth SQL task was harder" is not what this row shows.

The adaptive-halting environment, under recurrent depth, inverts the staircase outright: the easy-depth case fails and medium and hard pass. The easy-depth failure is an unexpected-indentation syntax error. The environment's other miss is a runtime crash from using a float tensor as a boolean condition. Both are failures. Neither is depth-related in any sense the axis name promises.

Three environments, three incompatible meanings of *deeper*, and in several of them the "harder" red cell is the validator or the runtime refusing the submission before any behavior was reached. Whatever `hidden_depth` is here, it is not one scale.

## A red cell is not one observation

The point sharpens when you look at the 61 eligible failures by terminal layer:

| Terminal event | Count | Behavioral-ref / compile-only |
|---|---:|---|
| `patch_invalid` (empty patch) | 24 | 9 / 15 |
| `underfit` | 20 | 3 / 17 |
| `source_invalid` | 10 | 3 / 7 |
| `runtime_error` | 3 | 0 / 3 |
| `invalid_action` | 2 | 0 / 2 |
| `overfit_visible_tests` | 2 | 1 / 1 |

Roughly 40% of the red cells are empty patches: the agent submitted nothing. Ten more are source-validation rejections; three are runtime crashes; two are malformed actions. The 20 `underfit` cases are the ones that match the common mental picture of a model failing — running code that was judged against its target behavior and got that behavior wrong.

These labels are not interchangeable observations about reasoning. They are campaign and judge artifacts: a non-answer, a rejected build, a crash, a malformed call, and a running-but-wrong program are five different things, and the grid paints them one color. The labels are also not internally trustworthy. Both rows marked `overfit_visible_tests` carry a trusted score of 1.0 together with notes that a required companion file was missing — in the MoCo row, `moco_model.py`. The archived score and terminal note contradict the label. I do not know from the archive alone whether to assign that mismatch to the submission, to the harness, or to the judging pipeline, and I would rather leave the responsibility unresolved than invent a story about it. What is clear is that `failure_mode` is not a validated taxonomy of cognitive failures, and here, at least twice, it points the wrong way.

## Family totals look like a ranking

Zoom out and the temptation returns in a new costume. The recurrent-depth family passes 31 of 33 eligible cases. The trajectory-synthesis family passes 2 of 8. It is almost irresistible to read that as "recurrence is easier than synthesis for this model."

It isn't, for reasons that are by now familiar. The recurrent-depth 31/33 is itself a mixture: `rd_state_carry` went 11/11 under behavioral reference; `rd_gradient_credit` went 11/11 under compile-only; `rd_adaptive_halting` went 9/11 under compile-only, where one of the two misses was the unexpected-indentation syntax error above and the other was the float-tensor runtime crash. A large share of the family's green comes from the exploratory judge mode, and two of its reds are not behavioral misses. The ML-debugging grouping, by contrast, sits at 9/30, but inside that: `batchnorm_ema` 0/11 under compile-only, `glyph` 0/8 under behavioral reference, `moco` 9/11 under behavioral reference — with one of MoCo's two reds being the missing-file mislabel discussed above. These family labels cover different code, different sizes, different tests, and different scoring modes. Nothing calibrates them to a shared construct. A 94% next to a 25% here is two measurements of two different things that happen to share a page.

There is a quieter inflation worth flagging, with its own caveats. A static scan of the clean comparator found ten control or variable axes — spread across nine category environments, including both axes of the compositional-optimizer environment — with no reference in the environment templates. If the paid runs inherited those no-ops, then some of the nominal design cells differ from their neighbors in name only, and the count of distinct interventions is smaller than the manifest implies. That finding is inferred, not observed: the scan did not execute generation or inspect every rendered task bundle, and the dirty-repository flag means it is a statement about the comparator rather than about what ran. It is one more reason not to read the axis grid as a grid of experiments.

## What this archive can bear

One selected seed per cell. No cell-level replication. Most contrasts are one-factor substitutions around a single baseline, not factorial designs. Later passes over the archive — the editorial pass, the analytic pass, the one that produced this essay — all reread the same 194 rows. None of them are new draws.

None of this is a new complaint. [HELM](https://arxiv.org/abs/2211.09110) made broad scenario coverage with multiple metrics the expected shape of a serious evaluation; it reports 42 scenarios rather than a headline score. [VarBench](https://aclanthology.org/2024.findings-emnlp.946/) perturbs task variables dynamically and reports its variable-based experiments across five sampled seeds rather than one. I cite both as precedent for the modest version of the lesson — expose what each score means, and replicate before calling a contrast an effect — not as validation of anything in this campaign. The prior-work check behind this essay was targeted, not systematic, and supports no novelty claim.

Against that modest bar, this archive is one model under one provider with one configuration, one seed per cell, prompts and judges that bundle several changes per nominal step, and a source identity left unresolved by a dirty repository. That is enough to say that the outcomes are heterogeneous and that several of the nominal contrasts are non-monotone at the validator or runtime rather than at the judge. It is not enough to estimate an intervention effect, to make `hard` mean one thing across environments, or to rank general capability.

Here is what I think the evidence does license. In this one campaign, 131 of 194 scored selected cases passed, 24 further case IDs were never scored and are neither passes nor failures, two of the 63 failures are provider-terminal and can defensibly be set aside to give 131 of 192, and any of those three fractions is fine so long as it travels with its denominator. The 61 remaining eligible failures stop at at least five different layers; roughly 20 are behavioral misses in the judged sense; two carry labels their own notes contradict. The 72 behavioral-reference and 120 compile-only cases should be reported side by side, not folded. The sharp regex contrast exists for the exact cases it exists for and bundles name and hint changes with the surface label. Several other "difficulty" sweeps turn non-monotone the moment you distinguish a validator stop from a judged miss.

What this archive does not license is a ranking of this model's capabilities across families, a ranking of the families by difficulty, a causal statement about surface form or hidden depth, a treatment of compile-only passes as a validated behavioral aggregate, or an identification of the clean comparator with the code that produced the paid results.

What it does give is an index: a list of specific cases and specific implementations that need to be looked at. The two mislabeled missing-file rows. The ten source-validator stops. The twenty-four empty patches. The regex name-and-hint bundle. The ten axes the comparator cannot find. A useful follow-up is not a wider sweep. It is to verify that each rendered axis fuckingly changes the task, to unbundle names and hints from labels, to run more than one seed per cell, and then — only then — to report pass rates split by judge guarantee and by stopping layer, so that the next person handed 131 three times knows, each time, what it is 131 of.
```
