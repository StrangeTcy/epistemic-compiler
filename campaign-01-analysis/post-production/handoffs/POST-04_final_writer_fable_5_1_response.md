---
title: "One Pass Rate, Six Stopping Points"
date: 2026-10-03
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
<dt>Original ideas</dt><dd>Low to moderate. Splitting a pass rate by pipeline stage is standard practice. What this post adds is one row-level attribution exercise on one frozen campaign archive, with the places where the archive disagrees with itself left visible.</dd>
<dt>Synthesis</dt><dd>Moderate. The work is reconciling a result checkpoint, per-row terminal notes, two judge-mode labels, a campaign report, a clean source comparator, and telemetry counters that do not agree.</dd>
<dt>Prose</dt><dd>Written by a language model inside the Arena writing pipeline, working from an audited evidence packet and an internal source draft. Two candidate drafts and a critique round were revisions of the same analysis. None of that is an independent replication, and none of it re-ran the model.</dd>
<dt>Certainty</dt><dd>High for the archived counts, labels, and terminal notes. Medium for anything that depends on the source comparator, because the archive records its repository as dirty. Low for any claim about why a given output came out the way it did.</dd>
<dt>Importance</dt><dd>Moderate as a reporting method. Low as a statement about model capability: one model, one provider, one configuration, one selected seed per case.</dd>
</dl>

Two rows in this archive carry the label `overfit_visible_tests`. It is the most interesting failure label in the set: a patch that fits the tests it can see instead of the problem. Both rows also record a trusted score of 1.0. Both terminal notes say the same thing in different words: a required companion file is missing.

So the label says the model gamed the tests. The score says the trusted check passed. The note says a file was not where the judge expected it. Three fields on one row, pointing three ways.

That is not a curiosity. If a single row can carry a label that its own note contradicts, then every aggregate built from those labels inherits the contradiction, and no amount of care at the top of the table repairs it. The only place to fix it is the row. This post reads the rows.

## Who gets a row at all

The result checkpoint holds **194 scored cases: 131 PASS and 63 FAIL**. I am not going to edit that. Alongside it the campaign records **24 omissions**: 17 `rope` cases dropped because the provider did not support their input modality, and 7 cases blocked before any provider call by known calibration failures. None of the 24 has a model score. Charging them to the model as failures would score tasks it never saw; crediting them as passes would be absurd in the other direction. They are outside every denominator below.

Then there is a disagreement inside the scored set. The campaign-level outage counter names one provider failure. But two final result files end with a terminal note attributing the failure to a provider transient after bounded retries. Which count do I believe? The archive does not settle it, so I carry all three:

| View | What is removed | PASS / FAIL | What the view represents |
|---|---|---|---|
| Raw checkpoint | nothing | 131 / 63 of 194 | every selected scored row, provider-terminal rows included |
| Report-consistent set | the one outage the report counter names | 131 / 62 of 193 | follows the campaign report's own count |
| Analysis set | both rows whose final notes blame the provider | 131 / 61 of 192 | follows the row-level terminal notes |

The 192-row set is my explicit exclusion, not a corrected campaign figure. The two excluded rows stay in the raw archive, scored, with their original labels. Everything below uses 192 unless I say otherwise.

One caveat applies to every sentence in this post about what a task asked or a judge checked. The archive records its repository as dirty. All 33 selected configuration hashes match a clean source comparator, but matching configs are not byte-level proof that the task, visible-test, judge, and helper code used in the paid run were the clean code. When I describe a judge, I am describing the comparator.

## Six labels are six places to stop

My first plan was to compute a model-attributable failure rate: take the 61 failures, remove the obviously infrastructural ones, divide the remainder by 192.

The plan was wrong, and the way it was wrong is the point.

Each FAIL row names a stopping point along a path: the provider has to return something; the agent has to emit a well-formed action carrying a non-empty patch; the patch has to parse and clear the source validator's import policy; it has to run; and only then does a judge decide whether it is right. The scoreboard applies a projection $\pi : \textsf{Outcome} \to \{0, 1\}$ that forgets which stage produced the zero. Nothing downstream can recover the stage from the bit. So after I strip out infrastructure, what is left is still not one homogeneous quantity; it is several, with different owners.

Here are the 61 failures in the 192-row set, with the judge mode kept visible:

| Recorded label | Count | Behavioral-reference / compile-only | What the record supports |
|---|---:|---:|---|
| `patch_invalid` | 24 | 9 / 15 | every final note says the patch file is empty |
| `underfit` | 20 | 3 / 17 | a judge scored the submission below passing |
| `source_invalid` | 10 | 3 / 7 | syntax error or disallowed import, before execution |
| `runtime_error` | 3 | 0 / 3 | the patch executed and crashed |
| `invalid_action` | 2 | 0 / 2 | action rejected as malformed; see the next section |
| `overfit_visible_tests` | 2 | 1 / 1 | label contradicted by score and note; see the next section |

Compile-only verdicts are exploratory throughout; the campaign report excludes them from any validated aggregate.

The `source_invalid` notes make the layering concrete. Four `monadic_reward` cases were rejected for importing `ast`. One `compositional_optimizer` case was rejected for `weakref`, one `css_state_machine` case for `re`. Three died on syntax: an unterminated triple-quoted string in `sql_fixed_point` and again in `ts_one_step`, and an unexpected indentation in `rd_adaptive_halting`. One of the ten carries no detail at all. The three `runtime_error` rows are an `rd_adaptive_halting` case that used a float tensor as a boolean condition and two `ts_trajectory` cases with no further note.

These are not the same kind of event. A syntax error is plausibly the model's output being broken, and I will not strengthen that beyond "plausibly." A rejected `import ast` is a collision between the output and a validator policy; whether that is the model's error depends on whether the policy was disclosed to the agent, and the archive does not tell me. An empty patch says nothing reached the validator, and from the label I cannot tell whether the agent emitted nothing or something was lost between the agent and the patch file. All of them score zero.

Now the number that changed my mind about the plan. The behavioral-reference slice has 16 failures. Nine are empty patches. Three are source rejections. One is the mislabeled "overfit" row. **Three are `underfit`**, and those three are the only rows in the slice where an independent behavioral judge ran on a submitted patch and found it short. Two of the three have specific notes: `regex_state_machine` outputs of length 66 and 34 where the input had length 32.

So in the slice with the stronger guarantee, three of sixteen failures are the kind a behavioral test is designed to catch. The other thirteen stopped earlier. I am not saying the model is blameless for those thirteen; an empty patch may well be the agent's doing. I am saying the labels do not let me assign it, so the honest move is to leave the attribution open rather than default it to the model.

One more thing the table hides. Seventeen of the twenty `underfit` rows are compile-only. Under compile-only scoring, "underfit" records a shortfall in a mode the report itself calls exploratory; under behavioral-reference scoring, it records a finding by the judge with the stronger guarantee. Same string, two different epistemic objects. And `failure_mode` generally is a campaign/judge label, not a validated taxonomy of mechanisms. It says where a row stopped, not why.

## When the label and the note disagree

Back to the two rows I opened with.

| Environment | Judge mode | Recorded label | Score | Trusted score | Final note |
|---|---|---|---:|---:|---|
| `batchnorm_ema` | compile-only | `overfit_visible_tests` | 0.95 | 1.0 | required companion file missing: `train.py` |
| `moco` | behavioral-reference | `overfit_visible_tests` | 0.95 | 1.0 | required companion file missing: `moco_model.py`; note also mentions `temperature_cancelled` |

Whatever happened on these rows, the notes describe a packaging or contract failure, not overfitting. The label is the only evidence for overfitting, and the label is contradicted by the rest of its own row. The record does not resolve whether the cause sits in the agent's output packaging, the judge's artifact requirements, or some interaction between them. It does establish that these two rows are not straightforward evidence of anything called overfitting.

The two provider-terminal rows are the mirror case. In the raw archive they carry the label `invalid_action`, and read naively that is two instances of the model emitting malformed output. Their final notes say the terminal failure was a provider transient after bounded retries. I hold both facts: the raw label stays, and the note is why the rows sit outside the analysis denominator. What I will not do is describe them as ordinary model-format failures.

That matters because the *other* two `invalid_action` rows, the ones inside the 61, both compile-only, carry no such note. The same raw string appears in two different evidentiary situations, and only the terminal note distinguishes them. A count of `invalid_action` labels, four in the raw checkpoint, would merge events that the archive itself keeps apart.

## Two judges, two promises

The 192 rows were not graded under one contract. **72 are `behavioral_reference`: 56 PASS, 16 FAIL. 120 are `compile_only`: 75 PASS, 45 FAIL.** In the raw 194 the compile-only count is 122 at 75/47; both provider-terminal rows were compile-only.

So 131/192 is not an accuracy. It is a sum across two guarantees, and the campaign report says one of them is exploratory and excluded from any validated aggregate. If you want a validated behavioral figure from this archive, it is 56 of 72, and even that is one selected seed per cell across a handful of environments, not a population estimate. A pass under compile-only scoring is not interchangeable with a pass under a behavioral-reference judge even when both are recorded as 1.

Why does the guarantee matter this much? Because a test only certifies what it executes, and the comparator gives specific reasons for care even where behavioral judges ran. These are comparator observations; the dirty repository means they describe the clean snapshot, not the paid-run code with certainty. With that said: in the comparator, the compositional-optimizer prompt promises nested associativity across multiple steps, while its judge checks tensor shape and one state-isolation chain. The physical-constraints judge enforces a 5:3 ratio the task never states. The categorical-lens hidden judge checks the laws but does not itself assert the coordinate-zero view, though the visible test does. None of this shows that every task is under-specified. It shows that "the judge said FAIL" and "the task was failed" can come apart in both directions, and that a 0/4 in the physical-constraints environment is a fact about a particular judge as much as about a particular model.

The gap has been measured elsewhere. An [empirical study of SWE-bench](https://dl.acm.org/doi/10.1145/3744916.3764576) found that, in its studied SWE-bench Verified setting, 7.8% of plausible patches counted correct by benchmark validation failed the full developer-written test suite. That is a rate for that setting, not for this campaign. I cite it only because it shows the problem is not hypothetical.

## A track label is a tag too

The same thing happens one level up. All seven `epistemic_games` rows are recorded under the `ml_debugging` track. In the comparator, the task's core is Bayesian inference over stipulated policy tables: the agent is handed the policies and asked to update over them. That is a well-posed inference problem, but it is not ML debugging, and it is not recursive theory of mind either. (It is also the only environment with an environment-level behavioral oracle self-test recorded as executed and passed, which is one more way its guarantee differs from its neighbours'.)

The recorded track total stays as recorded: **`ml_debugging`, 37 cases, 16 PASS / 21 FAIL**. As an analysis view, not an edit to the archive, I separate it into the three ML-debugging environments at **9 / 30** and `epistemic_games` at **7 / 7**.

Even the 30 are not one thing. `moco` is 9/11 under behavioral-reference judging, `glyph` is 0/8 under behavioral-reference, `batchnorm_ema` is 0/11 under compile-only. Each of those numbers comes from one selected seed per case, so the contrast between 82% and 0% is an observation about this run, not a stable difference between tasks. The recorded 16/37 blends a perfect inference slice into a debugging slice whose own environments span the whole range under different judges. It describes none of them.

## Counters that will not reconcile

Underneath the results sits the run telemetry, and it does not agree with itself either. The archive has 268 run directories, including earlier and superseded attempts. Retry counts depend on where you look: 3,869 attempts in the selected final manifests, 6,412 in campaign progress, with the API logs and checkpoint rows disagreeing in between. The run configuration says `reasoning_enabled=false`, while usage logs report 325,785 reasoning tokens and 2,710 response rows containing a `reasoning_content` field.

The tempting inference is obvious: the flag was off, the tokens are there, so the model reasoned anyway. I decline it. A field's presence is not its semantics, the cause of the disagreement is unknown, and no reasoning text is reproduced or examined here. What the archive establishes is a metadata discrepancy, full stop. There is also no spend field anywhere in the export, so the archive cannot support a cost estimate and I will not offer one.

## What a pass rate can still be

I do not think the scalar is useless. I think it has to come last.

A row that can answer "whose zero is it?" carries, at minimum: the raw verdict, any exclusion and its reason, the judge mode, whether a valid action and a non-empty patch existed, the validator outcome, the runtime outcome, and the judge's terminal note, with missing required artifacts recorded separately from behavioral misses. Aggregate within documented judge modes before combining them. [HELM](https://arxiv.org/abs/2211.09110) made the broad case for many scenarios and many metrics over one number; it is precedent, not validation of anything here, and the specific layers have to fit the machine being measured. For an agent that edits files and submits them to a validator, the layers above are where it can stop.

What the archive licenses is a descriptive map. Outcomes vary sharply by environment, from 2/8 eligible passes in trajectory synthesis to 31/33 in the recurrent-depth family, under judge guarantees that differ case by case and with no common calibration demonstrated across them. In the 192-row set the 61 failures span at least six recorded stopping points. In the behavioral-reference slice, three of sixteen failures are the `underfit` kind nearest to a behavioral miss. Two "overfit" labels describe missing companion files beside a trusted score of 1.0. Two `invalid_action` rows have notes blaming the provider. One recorded track bundles an unrelated inference task.

What it does not license is a capability ranking, a common difficulty scale, or a causal claim about any task axis: one selected seed per cell, no replication, a dirty repository, two grading contracts in one table with the compile-only half exploratory throughout. Validator rejections, runtime crashes, harness contract misses, judge-label mismatches, and provider outages are failures of different parts of the apparatus, and the thing people want to measure is only one of those parts.

A pass rate can still go at the bottom of the page. It just has to be computed from rows that still carry their tags. In this archive the tags are where the answer lives, and for most of the zeros the answer is still open.
