---
title: "Whose Zero Is It?"
date: 2026-10-03
layout: post
---
{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
<dt>Original ideas</dt><dd>Low to moderate. Breaking a pass rate down by pipeline stage is standard practice. What this post adds is one specific attribution exercise on one frozen archive.</dd>
<dt>Synthesis</dt><dd>Moderate. Most of the work is reconciling row labels, terminal notes, judge modes, and telemetry counters that don't fully agree.</dd>
<dt>Prose</dt><dd>A language model wrote this in the Arena pipeline, working from an audited evidence packet and an earlier source draft. Later editorial and model passes are revisions of one analysis. They are not independent replications of it.</dd>
<dt>Certainty</dt><dd>High for the archived counts, labels, and notes quoted here. Low for anything about why a given output was produced.</dd>
<dt>Importance</dt><dd>Moderate as a reporting lesson. Low as a statement about model capability. The data is one campaign with one seed per cell.</dd>
</dl>

Here's a question I couldn't answer about a campaign I thought I understood: of the cases that failed, how many failed because of the model?

That should be easy. The archive is a completed paid run with a result checkpoint, a failure label on every row, and a campaign report on top. But the more carefully I read it, the less the question meant. A FAIL row isn't a statement about the model. It says that *something*, somewhere between the provider's API and the hidden judge, didn't reach the end. Which something it was is recorded, if at all, in a free-text note that no summary table ever reads.

So this post isn't about the pass rate. It's about **attribution**: for each zero, whose zero is it?

## First, who gets a row at all

Before attribution there's admission. The checkpoint holds **194 scored cases: 131 PASS, 63 FAIL.** That's the raw record, and I'm not going to edit it.

There are also **24 cases that never got a row.** Seventeen `rope` cases were dropped because the provider didn't support their input modality. Seven were blocked before any provider call because of known calibration failures. None of these cases were scored. Counting them as failures would charge the model for tasks it never saw. Counting them as passes would be absurd in the other direction. They sit outside every denominator below.

Then there's a disagreement inside the scored set. The campaign-level outage counter names one provider failure, but two final result files carry the terminal note that the failure came from a provider transient after bounded retries. Where should those two rows go?

I don't think the archive settles it, so I keep all three readings:

| View | What's removed | PASS / FAIL |
|---|---|---|
| Raw checkpoint | nothing | 131 / 63 of 194 |
| Report-consistent sensitivity set | the one outage the report counter names | 131 / 62 of 193 |
| Analysis set | both rows with provider-terminal notes | 131 / 61 of 192 |

The 192 set is my explicit exclusion, not a corrected campaign report. The two excluded rows stay scored in the raw archive with their original labels. Everything below uses 192 unless I say otherwise.

One more admission caveat applies to every sentence about task or judge code in this post. The archive records `repository.dirty=true`. All 33 selected config hashes match a clean source comparator, but matching configs aren't proof that the executed task, test, and judge code were the clean code. When I describe what a judge checks, I'm describing the comparator.

## FAIL is a sum type that got cast to a bool

My first plan was to compute a "model-attributable failure rate": take the 61 failures, drop the obviously infrastructural ones, and divide what's left by 192.

That plan was wrong, and the reason it was wrong is the point of this post.

Each failure label really names a variant of a tagged union, something like

$$
\textsf{Outcome} \;=\; \textsf{ProviderDied} + \textsf{NoPatch} + \textsf{RejectedSource} + \textsf{Crashed} + \textsf{JudgeSaidNo}(s) + \textsf{Pass},
$$

and the scoreboard applies $\textsf{isPass} : \textsf{Outcome} \to \{0,1\}$, which throws away the tag. You can't recover the tag from the bool. Worse, the two judge modes in this archive (more on them below) mean $\textsf{JudgeSaidNo}$ isn't one variant but two, with different guarantees. So even after I strip out the infrastructure failures, what's left isn't one homogeneous quantity I can divide by 192.

So let me read the tags instead.

## Walking the gates

In the 192-case set, the 61 failures carry these recorded labels:

| Recorded label | Count | Behavioral-reference | Compile-only | Where it stopped |
|---|---:|---:|---:|---|
| `patch_invalid` | 24 | 9 | 15 | patch file was empty (every final note says so) |
| `underfit` | 20 | 3 | 17 | judge scored the submission below passing |
| `source_invalid` | 10 | 3 | 7 | syntax error or disallowed import, before execution |
| `runtime_error` | 3 | 0 | 3 | executed and crashed |
| `invalid_action` | 2 | 0 | 2 | action rejected as malformed |
| `overfit_visible_tests` | 2 | 1 | 1 | see next section; the label doesn't match the note |

Read the last column top to bottom and you get a pipeline. Something has to come back from the provider. The agent has to emit a well-formed action carrying a non-empty patch. The patch has to parse and pass the source validator's import policy. It has to run. Only then does a judge decide whether it's *right*.

The `source_invalid` notes make the layering concrete. Four `monadic_reward` cases were rejected for importing `ast`. One `compositional_optimizer` case was rejected for `weakref`, and one `css_state_machine` case for `re`. Others died on syntax: an unterminated triple-quoted string (once in `sql_fixed_point`, once in `ts_one_step`) and an unexpected indentation in `rd_adaptive_halting`. The `runtime_error` rows include an `rd_adaptive_halting` case that used a float tensor as a boolean condition, plus two `ts_trajectory` runtime failures.

These events aren't all the same kind. A syntax error is plausibly the model's output being broken. A rejected `import ast` is a collision between the output and a validator policy. Whether that counts as a model error depends on whether the policy was stated to the agent, and this archive doesn't answer that. An empty patch says nothing reached the validator. From the label alone I can't tell whether the agent emitted nothing or something got lost between the agent and the patch file. All of them score 0, but they belong to different owners.

Now the number that changed my mind. **The behavioral-reference slice has 16 failures. Nine are empty patches, three are source rejections, one is the mislabeled "overfit" case, and only three are `underfit`.** Those three are the only rows where an independent behavioral judge ran on a submission and found it wanting. The notes on two of them are specific: `regex_state_machine` outputs of length 66 and 34 where the input had length 32.

So in the slice with the strongest judge guarantee, three of sixteen failures look like what people mean by "the model got the task wrong." The other thirteen stopped earlier. I'm not claiming the model is blameless for those thirteen. An empty patch may well be the agent's doing. But I can't say that from these labels, so the honest move is to leave the attribution open rather than default it to the model.

The `underfit` label is also less uniform than it looks. Seventeen of its twenty rows are compile-only, which means "underfit" there means something different (next section but one). And `failure_mode` is a campaign/judge label, not a validated taxonomy of cognitive mechanisms. It tells you where a row stopped, not why.

## When the tag itself is wrong

Two rows go further. Their labels don't just hide the event; they point at the wrong event.

**The two "overfits."** `overfit_visible_tests` sounds like the most interesting failure in the set: a model fitting the visible tests rather than the problem. Both rows so labeled have `trusted_score=1.0`. Both final notes say a required companion file is missing: `train.py` in one `batchnorm_ema` case, `moco_model.py` in one `moco` case (the latter note also mentions `temperature_cancelled`). Whatever happened there, the notes describe a packaging or contract failure, not overfitting. The label is the only evidence for overfitting, and the label is contradicted by its own row.

**The two provider-terminal rows.** These are the rows I removed to get from 194 to 192. In the raw archive, both are labeled `invalid_action`. Read naively, that's two cases of the model emitting malformed output. Their final notes say the terminal failure was a provider transient after bounded retries. So I hold both facts at once: the raw label is `invalid_action`, and it stays. The terminal note points to the provider, and that's why the rows sit outside the analysis denominator. What I won't do is describe them as ordinary model-format failures. (The *other* two `invalid_action` rows, both compile-only, are inside the 61 and have no such note. They're a separate pair.)

If a single row can carry a label that inverts its own note, then any aggregate built from labels inherits the inversion. That can't be fixed at the top of the stack, only row by row.

## Two judges, two promises

The 192 rows weren't graded under one contract. **72 are `behavioral_reference`: 56 PASS, 16 FAIL. 120 are `compile_only`: 75 PASS, 45 FAIL.** The campaign report itself calls compile-only verdicts exploratory and excludes them from any validated aggregate. (In the raw 194, compile-only is 122 rows at 75/47. Both provider-terminal rows were compile-only.)

So "131/192" isn't an accuracy. It's a sum across two guarantees, and one of them is explicitly not validated behavior. If you want a validated behavioral figure from this archive, it's 56 of 72. Even that is one seed per cell across a handful of environments, not a population estimate.

Why does the guarantee matter so much? Because a test only certifies what it executes. The comparator gives specific reasons to be careful even where judges did run. In the comparator, the compositional-optimizer prompt promises nested associativity across multiple steps, but its judge checks shape and one state-isolation chain. The physical-constraints judge enforces a 5:3 ratio the task never states. The categorical-lens hidden judge checks the laws but doesn't itself assert the coordinate-zero view, though the visible test does. These are comparator observations from a dirty-repo campaign, so they don't prove what the paid run executed, and they don't show that every category task is under-specified. They do show that "the judge said FAIL" and "the task was failed" can come apart in both directions.

Outside this archive, the gap has been measured. A [SWE-bench empirical study](https://dl.acm.org/doi/10.1145/3744916.3764576) found that, in its studied SWE-bench Verified setting, 7.8% of plausible patches counted as correct by benchmark validation failed the full developer-written test suite. That's a fact about that setting, not a rate for this campaign. I cite it only to show the problem isn't hypothetical.

## Tracks are tags too

The same attribution problem shows up one level up. All seven `epistemic_games` rows are recorded under the `ml_debugging` track. In the comparator, that task's core is Bayesian inference over stipulated policy tables. That's a well-defined inference problem, but it isn't ML debugging, and it isn't recursive theory of mind either.

The recorded track total stays as recorded: `ml_debugging` has **37 cases, 16 PASS / 21 FAIL.** As a separate analysis view, not an edit to the archive, I split it:

- the three ML-debugging environments: **9 PASS / 21 FAIL of 30**
- `epistemic_games`: **7 / 7 PASS**

Even the 30 aren't one thing. `moco` is 9/11 under behavioral-reference judging, `glyph` is 0/8 under behavioral-reference, and `batchnorm_ema` is 0/11 under compile-only. The recorded 16/37 blends a perfect inference slice into a debugging slice whose own environments range from 0% to 82% under different judges. The blended number describes none of them.

## Telemetry that won't settle on one number

Below the results sits the run telemetry, and it doesn't reconcile either. The archive has 268 run directories, including superseded attempts. Retry counts depend on where you look: 3,869 attempts in the selected final manifests, 6,412 in campaign progress, with API logs and checkpoint rows disagreeing in between. The run configuration says `reasoning_enabled=false`, while usage logs report 325,785 reasoning tokens and 2,710 response rows containing a `reasoning_content` field.

I treat all of this as **metadata discrepancy**: counters and flags that disagree across export scopes, cause unknown. It's not evidence about what the model did internally. I reproduce no reasoning text and infer nothing from the field's presence. There's also no spend field anywhere in the export, so the archive can't support a cost estimate, and I won't make one.

## What a row should carry

If the question is "whose zero is it?", then a row needs enough structure to answer it. The minimum for a code-agent pipeline like this one looks like:

```
provider:  usable response?          → else infrastructure
action:    valid action, non-empty patch?  → else agent/harness (needs artifact to split)
source:    parses, passes import policy?   → else output vs. stated policy
runtime:   executes?                  → else output (usually)
judge:     which guarantee, which verdict, which note?
```

Alongside that, the row keeps the raw verdict, any explicit exclusion and its reason, the scoring mode, the judge's note, and the artifact itself. Nothing here is new as a principle. [HELM](https://arxiv.org/abs/2211.09110) made the broad argument for many scenarios and many metrics over a single number. But the specific layers have to match the machine being measured, and for an agent that edits files and submits them to a validator, these are where it can stop.

## What this licenses

The archive supports a **descriptive map**. Results vary sharply by environment, from 2/8 eligible passes in trajectory synthesis to 31/33 in the recurrent-depth family, under judge guarantees that differ case to case. In the 192-case set, the 61 failures span at least six recorded stopping points. In the behavioral-reference slice, only 3 of 16 failures are the `underfit` kind closest to a behavioral miss. Two "overfit" labels describe missing companion files with a trusted score of 1.0. Two `invalid_action` rows have terminal notes blaming the provider. One recorded track bundles an unrelated inference task.

It does **not** support a general capability ranking, a common difficulty scale across environments, or causal claims about any difficulty axis. There's one selected seed per cell and no replication. The repository was dirty. Two grading contracts are stitched into one table, and the compile-only half is exploratory throughout. Validator rejections, runtime crashes, harness contract misses, judge-label mismatches, and provider outages are failures of different parts of the apparatus. I've tried to keep each one apart from the thing people actually want to measure.

A pass rate can still go at the bottom of the page. It just has to be computed last, from rows that still carry their tags. In this archive the tags are where the answer is, and for most of the zeros, the answer to "whose zero is it?" is still open.
