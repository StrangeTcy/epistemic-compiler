---
title: "A Red Square Is Not One Result"
date: 2026-10-03
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The frame is an interpretation of this archive, not a new empirical result.</dd>
  <dt>Synthesis</dt>
  <dd>The observations describe one paid campaign and a source-comparator audit; the audit does not establish the exact source tree used in the paid runs.</dd>
  <dt>Prose</dt>
  <dd>This is a reading guide to the archived records, not an additional campaign run or replication.</dd>
  <dt>Certainty</dt>
  <dd>High for recorded counts and terminal notes; low for causal claims or exact identity between the clean comparator and the dirty paid-run tree.</dd>
  <dt>Importance</dt>
  <dd>Moderate as a way to read this archive; not a general model-capability ranking.</dd>
</dl>

The same numerator appears three times: 131 out of 194, 131 out of 193, and 131 out of 192. The passes do not move. The denominator does, because each fraction handles the campaign’s provider failures differently. A green square can look like a simple result; the number beneath it is already answering a question about what counts.

That matters because the grid invites a second question: which tasks were easy, which were hard, and what does the pattern say about capability? The archive is useful, but its colors collapse distinctions that have to be restored before that question can be answered. What changed in the task? What could the judge check? Where did the attempt stop? Without those details, a red cell is not one result, and “hard” is not one scale.

## The denominator changes with the question

The raw checkpoint contains 194 scored selected results: 131 PASS and 63 FAIL. The archive separately accounts for 24 cases that never became scored results. Seventeen were omitted because the provider could not accept their input modality; seven were gate-blocked before provider access for known calibration failures. They are not passes or failures. Adding them to either side would make up outcomes the campaign never recorded.

Two of the 194 scored results carry final notes attributing the terminal failure to provider transients after bounded retries. The campaign-level outage counter names one episode; an archive audit found a second final result with the same kind of terminal note. It is useful to keep the three scopes visible:

| Scope | PASS / total | FAIL | What it counts |
|---|---:|---:|---|
| Raw checkpoint | 131 / 194 | 63 | All scored selected results |
| Exclude only the report-listed transient | 131 / 193 | 62 | The campaign report’s single listed episode removed |
| Exclude both provider-coded terminal rows | 131 / 192 | 61 | A performance-analysis sensitivity set |

The last row is a defensible analysis choice, not a replacement for the raw checkpoint or a revision of the campaign report. Both provider-coded rows sit in the compile-only pool, which affects the next comparison. Whatever fraction is used, its denominator needs to travel with it.

## Green does not mean the same thing in both pools

After those two provider-coded rows are set aside, the 192-case performance set combines 72 cases with an instance-specific behavioral reference (56 PASS / 16 FAIL) and 120 compile-only cases (75 PASS / 45 FAIL). The campaign report calls compile-only verdicts exploratory and excludes them from a validated behavioral aggregate.

A behavioral-reference verdict checks a submission against the correct behavior recorded for that particular instance. A compile-only verdict checks a narrower contract: the submission builds and clears the available checks, without an instance-specific behavioral reference. A green in one pool is not interchangeable with a green in the other. Reporting their counts side by side is more informative than averaging them into a single rate that sounds more uniform than the judges were. The archive also records a passing public Bayesian-oracle preflight for the `epistemic_games` environment. That test is an environment-level setup check, not a reference for each scored instance; it cannot upgrade the compile-only pool into behavioral evaluation.

There is a further boundary around claims about how a task was implemented. The archive records the campaign repository as dirty. All 33 selected configuration hashes match a clean comparator of the recorded commit, which is evidence about those configurations. It is not byte-for-byte proof that the paid runs used the same task templates, visible tests, judge code, or helper files. Descriptions of what an axis does are therefore descriptions of the inspected comparator, not a verified transcript of the paid-run source tree.

## “Easy” and “hard” name different things in different tasks

Consider the regex state-machine environment. Its “hidden depth” axis is input-string length: 32, 128, or 512 characters. At the easy surface label, the selected run passes all three lengths. Hold the input at 32 characters and sweep the surface label, however, and the medium and hard cases fail: the recorded output lengths are 34 and 66 rather than 32. That is a clear contrast in these selected cases. It is not yet evidence for a general surface effect. In the clean comparator, the surface labels also change class names, and the hard prompt includes an extra performance hint. The campaign’s dirty-repository flag means those comparator details cannot establish exactly what the paid run saw; the sweep also has one selected seed per cell.

CSS gives “depth” another meaning: a bit count. At easy surface, the selected cases over 3, 4, and 5 bits yield a partial score of 0.416667, a source-validation rejection because the submission imported a disallowed `re`, and a pass. The surface-label sweep at fixed three-bit input produces a failure followed by two passes. Its 3/5 environment total therefore hides different things: partial credit, a validator stop, and behavioral outcomes. SQL uses graph-chain length instead. At easy surface, lengths 6 and 25 pass; the 12-node case stops at source validation because of an unterminated triple-quoted string. A validator rejection is not the same observation as code that ran and failed a behavioral reference.

These examples do not establish a shared unit called “difficulty.” Length, bit count, and graph size are different quantities; the nominal labels sometimes bundle a name or hint with the size change; and each contrast comes from one selected seed. The evidence licenses descriptions of these cases, not a causal account of surface form, string length, bit width, or recurrence depth.

## A red cell can stop at several layers

The 61 eligible failures also separate into terminal labels. The two provider-coded failures remain in the raw 63 but are outside this taxonomy:

| Terminal label | Count | Behavioral-reference / compile-only |
|---|---:|---|
| `patch_invalid` (empty patch) | 24 | 9 / 15 |
| `underfit` | 20 | 3 / 17 |
| `source_invalid` | 10 | 3 / 7 |
| `runtime_error` | 3 | 0 / 3 |
| `invalid_action` | 2 | 0 / 2 |
| `overfit_visible_tests` | 2 | 1 / 1 |

An empty patch is a non-answer. A rejected import or syntax error stops before behavior is tested; a runtime crash is different again. The 20 rows labeled `underfit` are closer to the familiar picture of an attempted solution missing a score threshold, but the judge split matters: 17 of those rows are compile-only and only three carry a behavioral reference. Calling all 20 proven behavioral misses would overstate what the judge could establish.

The labels need scrutiny too. Both rows labeled `overfit_visible_tests` have a trusted score of 1.0 and notes about a missing required file; the MoCo record names `moco_model.py`. That conflicts with the applied label, but it does not establish whether the cause belongs to the submission, the task, or the judging pipeline. The careful claim is that the archived score and terminal note do not support a straightforward diagnosis of behavioral overfitting. A grid that paints an empty file, a rejected source, a crash, a missing companion file, and a judged miss the same red is hiding information, not summarizing it.

## Family totals are descriptions, not a ranking

The recurrent-depth family records 31 passes in 33 eligible cases; trajectory/synthesis records 2 in 8. The gap is striking, but the totals do not compare calibrated versions of one construct. Recurrent depth itself mixes `rd_state_carry` at 11/11 under behavioral reference, `rd_gradient_credit` at 11/11 under compile-only, and `rd_adaptive_halting` at 9/11 under compile-only. The last environment’s misses include an unexpected-indentation syntax error and a runtime error. A large part of the family’s passes therefore comes from the exploratory judge, and not every failure is a behavioral miss.

The three ML-debugging environments make the same point in another direction: `batchnorm_ema` is 0/11 under compile-only, `glyph` is 0/8 under behavioral reference, and MoCo is 9/11 under behavioral reference, including the missing-file row. Those labels cover different tasks, sizes, tests, and judge modes. The family counts describe the selected campaign; they do not rank general reasoning ability. They can still help choose cases for closer inspection, provided the family totals stay attached to the task and judge mix that produced them. A large ratio is a lead for an audit, not a level on a capability scale.

A static scan of the clean comparator also found ten advertised control or variable axes across nine category environments with no implementation reference in those templates. That scan is evidence about the comparator, not proof that the paid runs inherited the same placeholders. It is worth investigating, but it should not be counted as a demonstrated flaw in the paid artifacts.

## Keep the map; do not turn it into a ladder

A useful report would let a reader recover at least four facts from each cell: the input change that actually rendered, the judge mode and availability of an instance-specific reference, the terminal layer, and the displayed verdict. The “easy” or “hard” label alone cannot carry that information. In practice, a cell could be accompanied by a compact record:

| Record | Question it answers |
|---|---|
| Rendered input change | What changed in the task, beyond its surface label? |
| Judge mode and reference | What could the judge verify on this instance? |
| Terminal layer | Did the attempt reach behavioral evaluation? |
| Verdict and scope | Which result is counted, under which denominator? |

This is a reporting principle rather than a new one: [HELM](https://arxiv.org/abs/2211.09110) is a precedent for broad scenario coverage with multiple metrics, while [VarBench](https://aclanthology.org/2024.findings-emnlp.946/) perturbs task variables and repeats variable-based experiments across five sampled values. Neither validates this campaign; both help explain why a score should say what it measured and why a contrast should be repeated before it is called an effect.

This archive is one paid campaign with one selected seed per cell, mixed judge guarantees, sparse contrasts, and a source identity that remains uncertain because the repository was dirty. It shows heterogeneous outcomes and several non-monotone patterns. It does not estimate an intervention effect, make “hard” mean the same thing across environments, or rank general capability.

A stronger follow-up would first verify that each rendered axis changes the task. It would separate labels from class names and performance hints, run more than one seed per cell, and report outcomes split by judge guarantee and stopping layer. Until then, the grid is best read as an index of cases and implementations worth inspecting. It is a map of where the questions are—not a leaderboard of who is good at what.
