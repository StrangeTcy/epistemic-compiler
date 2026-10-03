---
title: "A Red Square Is Not One Result"
date: 2026-10-03
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The framing that a displayed cell compresses distinct facts about input change, judge guarantee, reference availability, and termination layer, and that the useful product is therefore a case map rather than a scalar ranking. The underlying observations come from one archived campaign.</dd>
  <dt>Synthesis</dt>
  <dd>Written from an audited evidence packet for this post: a frozen archive of one paid Atria-Dawn-Preview campaign, finding records with stated confidence levels, a source-comparator audit, and a targeted (not systematic) prior-work check. No cases were re-run.</dd>
  <dt>Prose</dt>
  <dd>Argument structure and wording are mine; counts, terminal notes, and scope boundaries are taken directly from the packet.</dd>
  <dt>Certainty</dt>
  <dd>High for recorded counts, judge-mode splits, and terminal notes; low for any causal reading of the nominal axes and low for exact identity between the inspected clean comparator and the paid-run tree, because the repository was recorded dirty.</dd>
  <dt>Importance</dt>
  <dd>Moderate as a reading guide for this archive; modest as a general point, because the general point is already established in prior evaluation work.</dd>
</dl>

The same 131 passes can be written three ways. Raw checkpoint: 131 PASS and 63 FAIL among 194 scored selected results. Exclude only the single provider-transient episode named in the campaign-level outage counter and the fraction becomes 131/193. Exclude both final results that carry explicit terminal notes attributing failure to provider transients after bounded retries and it becomes 131/192. The numerator never moves. Only the denominator does, and each choice quietly changes what the number claims to measure.

That is the opening puzzle of this archive. A colored grid invites a difficulty ranking or a capability score. Once the stopping layers and judge guarantees are kept visible, the grid stops looking like either.

## Three denominators, and twenty-four cases that never entered them

Before any model call, 24 cases were already outside the scored set. Seventeen were omitted because the provider did not support the required input modality; seven were gate-blocked before provider access for known calibration failures. Together with the 194 scored results they make 218 case IDs the campaign accounts for. Those 24 have no model score. They are neither passes nor failures; they are cases the campaign never asked.

Of the 194 that were scored, the raw split is 131 PASS / 63 FAIL. Two of the failures carry final-result notes that attribute the terminal outcome to provider transients after bounded retries. The campaign’s own outage counter tracks only one episode; the archive audit finds a second terminal note. Removing both is an analysis choice for asking about model performance, not a rewrite of the campaign report. I work primarily from the 192-case sensitivity set (131 PASS / 61 FAIL) while keeping the raw counts on the page. The two excluded rows happen to sit in the compile-only pool, which matters for the next cut.

## What a green cell fuckingly guarantees

The 192 eligible cases were judged under two different guarantees that the grid renders identically. Seventy-two carried an instance-specific behavioral reference: the judge knew the correct behavior for that particular task instance (56 PASS / 16 FAIL). One hundred and twenty were compile-only (75 PASS / 45 FAIL). The campaign report itself calls the compile-only verdicts exploratory and keeps them out of any validated aggregate.

A green behavioral-reference cell and a green compile-only cell are not the same observation. One says the submission matched the instance reference on behavior the model could not see. The other says it built and cleared an exploratory check. Averaging them produces a number that answers no single question. Any honest map therefore reports the two pools side by side.

The families grouped into tracks mix the guarantees unevenly. The weird-machine environments are entirely behavioral-reference (30 eligible cases). The recurrent-depth family mixes 11 behavioral-reference with 22 compile-only. The three ML-debugging environments split 19 and 11. Color alone erases that distinction.

A standing caveat sits under every source-level claim that follows. The archive points at a specific commit and records the working tree as dirty. All 33 selected configuration hashes match a clean comparator snapshot of that commit. Matching config hashes are reassuring about the configs; they are not byte-for-byte proof that the task templates, visible tests, judge code, or helper files used in the paid runs were exactly the inspected clean files. Every description of what an axis “does” is a statement about the comparator, not a proven transcript of the paid artifacts.

## “Easy / medium / hard” measures different quantities in different rooms

The labels look like a staircase. They are not a common calibrated unit.

In the regex state-machine environment the “hidden depth” axis is input-string length: 32, 128, or 512 characters. With the surface label held at easy, the selected run (one seed per cell) passes all three lengths. Hold length at 32 and sweep the surface label, and the medium and hard variants fail. The notes record length mismatch: input 32, output 34 for medium; input 32, output 66 for hard. Length preservation is the core requirement of the task, so these are behavioral misses under a behavioral reference.

Is the contrast a clean surface effect? In the clean comparator the surface levels also change class names, and the hard prompt carries an extra performance hint absent from the easy prompt. The manipulation is therefore a bundle. With the repository dirty, the comparator details do not prove the exact paid-run files. The contrast is sharp for the cases that exist; it does not isolate a general surface cause.

CSS makes the word travel worse. There “hidden depth” is a bit count. At easy surface over 3, 4, and 5 bits the selected outcomes are a partial score of 0.416667, a source-validation failure (the validator rejected a disallowed `import re`), and a pass. Hold the bits fixed and sweep the surface label and the pattern is failure followed by two passes. The environment total of 3/5 silently folds a partial-credit behavioral outcome, a validator stop, and clean passes into one fraction.

SQL repeats the shape with a third physical quantity. The depth axis is graph-chain length. At easy surface the length-6 and length-25 cases pass; the length-12 case fails source validation on an unterminated triple-quoted string. The environment total of 4/5 hides that the single red cell never reached a behavioral test.

Other families produce still different profiles. The five selected spreadsheet cases pass at their tested class-name and grid-length levels. The six weird-machine environments together record 25 passes out of 30 eligible cases. In the MoCo debugging task the visible-test levels produce pass, fail, pass; the middle case carries a trusted test score of 1.0 yet is marked failed because a required companion file is missing. In adaptive-recurrence halting the easy-depth case is a syntax error (unexpected indentation), while the medium- and hard-depth cases pass. None of these patterns is a clean measure of one shared latent difficulty.

Every contrast above is one selected seed per cell. Most are sparse one-factor substitutions around a single baseline, not factorial designs or population estimates. They license local description, not causal claims about surface form, string length, bit width, or recurrence depth.

## A red square is not one kind of failure

Among the 61 eligible failures the terminal labels break down as follows (the two provider-coded raw failures sit outside this taxonomy):

| Terminal label | Count | Behavioral-reference / compile-only |
|---|---:|---|
| patch_invalid (empty patches) | 24 | 9 / 15 |
| underfit | 20 | 3 / 17 |
| source_invalid | 10 | 3 / 7 |
| runtime_error | 3 | 0 / 3 |
| invalid_action | 2 | 0 / 2 |
| overfit_visible_tests | 2 | 1 / 1 |

Nearly 40 % of the red cells are empty patches—the submission produced nothing. Another ten never passed the source validator; three crashed at runtime; two were malformed actions. Only the 20 underfit cases are the plain behavioral miss: running code that the judge scored below threshold.

The labels themselves are campaign and judge artifacts, not a validated taxonomy of cognitive mechanisms. Both rows labeled `overfit_visible_tests` carry a trusted score of 1.0 and a note that a required companion file was missing (the MoCo case names `moco_model.py`). The archived score and terminal note conflict with the applied label. Responsibility for the mismatch is unresolved on the available evidence; what is clear is that the label does not describe a demonstrated behavioral overfit.

An empty file, a rejected import, a crash, a missing companion file, and a running-but-wrong program are five different observations. A grid that paints them the same red answers a question nobody asked.

## Family totals look like a ranking; they are not calibrated to one

Recurrent-depth records 31 passes in 33 eligible cases; trajectory/synthesis records 2 in 8. The contrast is descriptive of these selected tasks, prompts, judges, and one-seed runs. It is not evidence that recurrence is intrinsically easier than synthesis, nor a ranking of general capabilities.

The recurrent-depth total itself mixes guarantees and termination layers: `rd_state_carry` is 11/11 under behavioral reference, `rd_gradient_credit` is 11/11 under compile-only, and `rd_adaptive_halting` is 9/11 under compile-only. One of the two misses is the unexpected-indentation syntax error at easy depth; another is a runtime error from using a float tensor as a boolean condition. A large share of the family’s green comes from the exploratory judge, and two of its reds are not judged behavioral misses.

The ML-debugging environments sit at 9/30 overall, but the internal split is extreme: BatchNorm EMA 0/11 (compile-only), glyph 0/8 (behavioral reference), MoCo 9/11 (behavioral reference, including the missing-file mislabel). The family labels cover different code tasks, sizes, tests, and score modes. Nothing calibrates them to a shared construct.

A static scan of the clean comparator finds ten advertised control or variable axes across nine category environments with no reference in the environment templates (both axes of the compositional-optimizer environment among them). The finding is inferred from the comparator, not observed in the paid runs; the dirty flag prevents treating it as proof of what executed. If the paid runs inherited those placeholders, nominal coverage overstates the number of distinct interventions. Columns can look like experiments without being experiments.

## Draw a map, not a ladder

None of this makes the campaign worthless. It makes the right product a map that keeps the compressed facts visible. Concretely, every cell should expose at least four things separately:

- the rendered input change (not merely the easy/medium/hard label),
- the judge mode and whether an instance-specific behavioral reference was available,
- the terminal layer (empty patch, source validation, runtime, invalid action, missing required file, or judged behavioral outcome),
- the displayed verdict.

This is not a new evaluation principle. HELM already treats broad scenario coverage with multiple metrics as the expected shape of a serious evaluation. VarBench dynamically perturbs task variables and, for variable-based experiments, repeats across five sampled seeds rather than trusting a single draw. The modest lesson each carries is the same: expose what each score means and where a manipulation fuckingly changed the task. Against that bar this campaign is one selected seed per cell, mostly one-factor substitutions, with manipulations that sometimes bundle names and hints, mixed judge guarantees, and a source identity left unresolved by a dirty repository. That is enough to say the outcomes are heterogeneous and some nominal contrasts are non-monotone. It is not enough to estimate an intervention effect, to make “hard” mean one thing across environments, or to rank general capability.

What would license stronger claims is also clear. Verify that each rendered axis fuckingly changes the task. Hold class names and performance hints constant while moving one quantity. Run more than one seed per cell. Report everything split by judge guarantee and by stopping layer. Until then the archive is most useful as an index—a pointer to specific cases and specific implementations that need inspection: the two mislabeled missing-file rows, the ten source-validator stops, the twenty-four empty patches, the regex name-and-hint bundle, the axes the comparator cannot find.

The evidence licenses a descriptive map of task-specific result and failure patterns under one model, one provider, these prompts, and these judges. It does not license a universal difficulty scale, a causal story about surface form, a validated aggregate that folds compile-only verdicts into behavioral ones, or a leaderboard. The single number I might have wanted was never in the grid to begin with; the interesting information is in the layers the color discards.
