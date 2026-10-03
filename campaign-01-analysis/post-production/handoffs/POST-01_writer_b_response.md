```markdown
---
title: Every Cell Hides Four Questions
date: 2026-10-03
layout: post
---
{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Low. The reframing is mine; the facts are an archive's.</dd>
  <dt>Synthesis</dt>
  <dd>High. The point is almost entirely about how to read numbers that already exist.</dd>
  <dt>Prose</dt>
  <dd>Medium. One extended metaphor, carried as far as it holds and no further.</dd>
  <dt>Certainty</dt>
  <dd>High for the recorded outcomes; low for any claim about why they happened.</dd>
  <dt>Importance</dt>
  <dd>Moderate. It is a reading hygiene argument, not a result.</dd>
</dl>

I came to this archive wanting one number. I had a frozen snapshot of a completed paid campaign — call it the Atria-Dawn-Preview run — a grid of environments and conditions, each ending in a green or a red square. The obvious thing to do with a grid like that is to sort it: which tasks are easy, which are hard, how does this model rank. I spent an afternoon trying, and the grid would not let me.

Not because the numbers were missing. Because each square turned out to be a lossy compression of several unrelated questions, and once I decompressed a few of them the "difficulty" axis I was looking for stopped existing.

## What a square fuckingly stores

Write the displayed outcome of one cell as a projection. Each green or red square $c$ is

$$c = \pi\,(x,\; g,\; r,\; t)$$

where $x$ is the input manipulation the campaign applied, $g$ is the judge's guarantee, $r$ is whether the judge held an instance-specific behavioral reference, and $t$ is how the submission terminated. The grid shows you $c$ and throws away the tuple. My whole argument is that the tuple is where the information lives, and that no two of its coordinates are commensurable across environments.

Before any of that, though, the denominator deserves the same scrutiny, because the aggregate is the first thing a square tempts you to compute.

## The denominator is not one number either

The raw checkpoint holds 194 scored selected results: 131 PASS and 63 FAIL. Separately — and this separation matters — the archive lists 24 cases that never became scored results at all: 17 omitted because the provider could not accept their input modality, and 7 gate-blocked before provider access for known calibration failures. Those 24 are neither passes nor failures. Counting them as either would be inventing data. The full bookkeeping records 218 case IDs as scored or explicitly omitted; only 194 are scores.

Inside the 194, two final results attribute their terminal failure to provider transients after bounded retries. The campaign's own outage counter tracks only one of them. So there are three defensible denominators, and I will keep them visibly distinct rather than pick one and hide the rest:

| What you remove | PASS / total | FAIL |
|---|---|---|
| Nothing (raw) | 131 / 194 | 63 |
| Only the report-listed transient | 131 / 193 | 62 |
| Both provider-coded terminal rows | 131 / 192 | 61 |

For performance analysis I work from the 192-case set, because terminal provider failures are not the model missing a problem — they are the infrastructure refusing to let it try. But the raw 63 stays on the page. The exclusion is an analysis choice, not a rewrite of the campaign report, and both provider-coded rows happen to sit in the compile-only pool, which matters for the next cut.

## Two judges wearing the same color

The 192 eligible cases split by judge guarantee into two groups that the grid renders identically and that mean entirely different things. There are 72 behavioral-reference cases (56 PASS / 16 FAIL) and 120 compile-only cases (75 PASS / 45 FAIL). A behavioral-reference verdict checks an instance-specific reference; a compile-only verdict checks that the submission builds and runs its visible tests. The campaign report itself calls the compile-only verdicts **exploratory** — not a validated behavioral aggregate.

This is the $g$ and $r$ coordinates, and it is the single most important thing the color strips away. A green compile-only square and a green behavioral-reference square are not the same evidence. One says "this ran"; the other says "this did what the task required on a reference it could not see." Averaging them produces a number that answers no question. So any honest aggregate has to report these two pools side by side, not fold them into one pass rate.

One environment, epistemic_games, carries an environment-level behavioral self-test that was recorded as executed and passed. That is a preflight on the environment, not a per-case guarantee, and the two mechanisms should not be conflated — an oracle that confirms the environment is wired correctly is a different object from a reference that scores an individual submission.

A standing caveat under all of this: the archive points at a source commit but records the repository as **dirty**. All 33 selected config hashes match a clean source comparator, which is reassuring, but matching config hashes are not byte-for-byte proof that the task, visible-test, judge, and helper code in the paid runs were exactly the inspected clean files. Every source-level description below is a statement about the comparator, not a proven statement about the paid artifacts.

## "Difficulty" is a different physical quantity in each room

Now the $x$ coordinate — the thing the campaign calls difficulty. The labels `easy`, `medium`, `hard` look like a staircase. They are not even measuring the same building.

In the regex state-machine environment (a Rule 110 construction — which tells you nothing about Turing completeness, only that the task is phrased that way), the "hidden depth" knob is literally input-string length: 32, 128, 512 characters. Hold the surface label at easy and the selected run passes all three lengths. But hold the length at 32 and sweep the surface label, and the medium and hard variants fail — the output grows to 34 and then 66 characters instead of preserving length. A sharp contrast. Except in the clean comparator those surface labels also rename classes, and the hard prompt carries an extra performance hint. So the "surface" manipulation bundles at least three changes, and with the repository dirty I cannot even confirm those bundled changes are what the paid run saw. One seed per cell. This is an observation about two specific cases, not an isolated surface effect.

CSS makes the word travel even worse. There "hidden depth" is a bit count. At easy surface over 3, 4, and 5 bits the selected run scores a partial 0.416667, then a source-validation failure (the validator rejected an `import re`), then a clean pass. Hold the bits at the baseline and sweep the surface label and you get a failure followed by two passes. The environment total is 3/5 — a number that silently contains a partial credit, a validator rejection, and three genuine behavioral outcomes, all flattened into "three green, two red."

SQL does it again with a third quantity. The depth knob is graph-chain length; easy and hard (6 and 25 nodes) pass, while the 12-node middle case fails source validation on an unterminated triple-quoted string. Its environment total, 4/5, hides that the one red square is a syntax error, not a wrong algorithm.

Three environments, three incompatible meanings of "deeper," and in two of them the failure at the "harder" level is the validator refusing the file before any behavior was tested. Whatever `hidden_depth` is, it is not one scale.

## A red square is not a red square

That brings me to $t$, the termination type, which the grid compresses most brutally of all. Among the 61 eligible failures:

| Terminal event | Count | Behavioral-ref / compile-only |
|---|---:|---|
| patch_invalid (empty patch) | 24 | 9 / 15 |
| underfit | 20 | 3 / 17 |
| source_invalid | 10 | 3 / 7 |
| runtime_error | 3 | 0 / 3 |
| invalid_action | 2 | 0 / 2 |
| overfit_visible_tests | 2 | 1 / 1 |

Nearly 40% of the red squares are empty patches — the agent submitted nothing. That is not a wrong algorithm; it is a non-answer. Another ten are source-validation rejections and three are runtime crashes: the submission never reached a behavioral test. Only the 20 "underfit" cases are unambiguously the thing people picture when they say a model failed a hard problem — it produced running code that got the behavior wrong.

And the labels are not even internally trustworthy. The two `overfit_visible_tests` failures both carry a trusted score of 1.0 and a note that a required companion file was missing — in the MoCo case, `moco_model.py`. The model's code was fine; the harness could not assemble the task. Calling that "overfitting the visible tests" describes a cognitive failure that did not occur. These labels are campaign and judge artifacts, not a validated taxonomy of reasoning failures, and here two of them point the wrong way.

So the rule I want is simple and unglamorous: an empty file, a rejected import, a crash, a missing companion file, and a running-but-wrong program are **five different observations**. A results grid that paints them all the same red is answering a question nobody asked.

## The family totals look like a ranking. They aren't.

Zoom out and the temptation returns in a new costume. The recurrent-depth family passes 31 of 33 eligible cases; the trajectory/synthesis family passes 2 of 8. It is almost irresistible to read that as "recurrence is easier than synthesis for this model."

It isn't, for reasons that are now familiar. The recurrent-depth 31/33 is itself a mixture: `rd_state_carry` is 11/11 under behavioral reference, `rd_gradient_credit` is 11/11 under compile-only, and `rd_adaptive_halting` is 9/11 under compile-only — where one of the two misses is a syntax error (unexpected indentation at the easy depth) and the other is a runtime crash (a float tensor used as a boolean). A large share of that family's green comes from the exploratory judge, and two of its reds are not reasoning misses at all. The ML-debugging environments, by contrast, sit at 9/30, but inside that: `batchnorm_ema` 0/11 under compile-only, `glyph` 0/8 under behavioral reference, `moco` 9/11 under behavioral reference — with one of MoCo's two reds being the missing-file mislabel above. These family names cover different code, different sizes, different tests, and different score modes. They are not calibrated to a shared construct, so the 31/33-versus-2/8 contrast describes these selected tasks and prompts, not an intrinsic ordering of reasoning abilities.

There is also a quieter inflation worth flagging. A static scan of the comparator found ten control or variable axes, spread across nine category environments, that appear to have no implementation behind them — placeholders that render as distinct "interventions" but do nothing. With the repository dirty I cannot prove the paid runs inherited those no-ops, but if they did, the nominal coverage overstates how many genuinely different things were varied. Columns can look like experiments without being experiments.

## So draw a map, and stop drawing a ladder

None of this says the campaign is worthless. It says the right output is a map with the tuple visible, not a scalar with the tuple discarded. Concretely, every cell should display four things separately: what input changed ($x$), what the judge checked and whether it had an instance-specific reference ($g, r$), and how the submission terminated ($t$) — with empty-patch, validator, runtime, and behavioral-test outcomes kept in their own columns.

This is not a new principle. [HELM](https://arxiv.org/abs/2211.09110) built broad coverage out of 42 scenarios reported under multiple metrics rather than one headline. [VarBench](https://aclanthology.org/2024.findings-emnlp.946/) perturbs task variables and, crucially, repeats across sampled values — five seeds — instead of trusting a single draw. And the coverage worry has teeth elsewhere too: an empirical study of SWE-bench found that 7.8% of patches counted as correct failed the full developer test suite in its setting. The lesson each of these carries is modest and the same: expose what a score means and where a manipulation fuckingly changed the task.

Against that bar this campaign is a single seed per cell, mostly one-factor substitutions around one baseline, with manipulations that bundle several changes at once and a source identity left unresolved by a dirty repository. That is enough to say the outcomes are heterogeneous and some nominal contrasts are non-monotone. It is not enough to estimate an intervention effect, to make "hard" mean one thing across rooms, or to rank general capability.

What would license more is also clear: verify each rendered axis fuckingly does something, hold names and hints constant while moving one quantity, run multiple seeds, and report everything split by judge guarantee and failure layer. Until someone does that, the most useful thing this grid can be is an index — a pointer to which specific cases and which specific implementations deserve a closer look. It is a good map of where to inspect. It is not a leaderboard, and the single number I walked in wanting was never in there to find.
```
