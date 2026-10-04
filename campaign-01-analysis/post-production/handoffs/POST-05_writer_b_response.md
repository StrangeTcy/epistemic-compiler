---
title: "Thirty-Four Characters Out of Thirty-Two"
date: 2026-10-03
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Moderate. Two ideas here are new: reading the regex contrast as a map of where failures happen rather than as a result, and a design that tests the two bundled manipulations separately. The general principle of perturbing variables and controlling for them comes from earlier work.</dd>
  <dt>Synthesis</dt>
  <dd>Combines one archived paid evaluation campaign (one model, one configuration, one seed per cell), an audit of a clean source comparator for a repository recorded as dirty, and two published benchmark papers used only for context.</dd>
  <dt>Prose</dt>
  <dd>A language model drafted this in an Arena writing pass, working from a compiled evidence packet of archive tables, audit findings, and limitations. It is published under this byline. No outside authors contributed.</dd>
  <dt>Certainty</dt>
  <dd>High for the recorded case outcomes. Low for any causal reading of them. The one causal hypothesis below is labelled speculative and was not tested.</dd>
  <dt>Importance</dt>
  <dd>Modest. The post is about experimental design for one small task family, not about model capability.</dd>
</dl>

Suppose you rename a class and the model's regex stops preserving string length.

What did you learn? The obvious answer is that the model was paying attention to the name. A more careful answer is that you learned something about the name and about whatever else changed when the name changed. If you can't say what else changed, you have learned less than the obvious answer claims.

This post is about one small cluster of results that looks at first like it answers a good question: *can a model see the computation underneath an unfamiliar surface?* I want to show why it doesn't answer that yet, and why the way it falls short is still useful.

## The task family

The campaign archive has a track of six "weird machine" code tasks. Each one hides a computation inside a substrate that wasn't built for it:

- a regex that has to carry out a cellular-automaton step
- CSS selectors that compute parity
- a SQL fixed-point query
- spreadsheet dataflow
- a CI dependency graph
- a small template interpreter

Each task has two nominal axes, `surface_deceptiveness` and `hidden_depth`, each labelled easy, medium, or hard.

The design isn't a full grid. Each environment has five selected cells:

- the easy/easy baseline
- two cells that change depth while surface stays easy
- two cells that change surface while depth stays easy

That's a one-factor-at-a-time cross around a single baseline. Each cell has exactly one seed-0 run. Every one of the 30 cases is graded by a behavioral reference judge, not compile-only. All 30 were recorded and all 30 count toward the score: no exclusions and no provider-terminal rows in this track.

25 of the 30 pass. I'll come back to why that number means less than it seems.

## The cross in the regex task

The regex task asks for a single update of Rule 110, written as regular-expression machinery. "Hidden depth" here means only the length of the input string: 32, 128, or 512 characters.

Here are the five cells:

| surface | input length | verdict | score | judge note |
|---|---|---|---|---|
| easy | 32 | PASS | 1.0 | — |
| easy | 128 | PASS | 1.0 | — |
| easy | 512 | PASS | 1.0 | — |
| medium | 32 | FAIL | 0.208333 | length mismatch, in=32, out=34 |
| hard | 32 | FAIL | 0.208333 | length mismatch, in=32, out=66 |

Laid out like that, it looks like a clean story. Under the easy label, the model's solution holds up as the input grows sixteenfold. At the smallest input, changing the surface label breaks it. Surface beats depth.

I believed that for about one paragraph of the first draft. Then I looked at what the surface label actually controls.

## Two changes made at once

In the clean source comparator, the surface levels map to different class names. The hard level also adds an implementation-performance hint to the prompt.

So moving from easy to hard surface changes two things together:

1. **A name.** A class name changes nothing about the computation, but it can change which conventions and memorised patterns the model reaches for.
2. **The instruction.** The extra hint is new content. It asks for something, or at least suggests something, that the easy prompt doesn't.

The medium cell changes only the name (as far as the comparator shows). The hard cell changes the name and adds the hint. Both fail. Because each cell has one run, I can't separate the following:

- the name mattered
- the hint mattered
- both mattered, or they interacted
- seed 0 happened to land badly on two of five draws

There's another caveat. The comparator is *clean*, while the paid campaign recorded its repository as dirty. All 33 selected config hashes match the clean snapshot. But matching configs isn't byte-level proof that the prompts, visible tests, or judge code the model actually saw were the same. So even "the hard prompt contained a performance hint" is an observation about the comparator, not a certainty about the paid run.

Here is the hypothesis I'd bet on, and I'm labelling it plainly as speculation. **In this particular regex task and this particular run, the changed names or the added hint probably mattered more than input length.** The archive can't separate that from sampling noise. Nothing in it estimates an effect.

## What the numbers 34 and 66 tell us

The judge's notes give a little more than a verdict, and they're tempting to over-read.

On a 32-character input, the medium-surface output was 34 characters: the input plus two. The hard-surface output was 66 characters: a bit more than double. A Rule 110 update should map a string to a string of the same length. Both failures broke that invariant, and the judge stopped at the mismatch. Its note says it "collapsed on length mismatch".

My first instinct was to diagnose. +2 looks like a boundary-padding slip that never got trimmed. ~2× looks like something duplicating or interleaving the string. Those are plausible stories. But the archive records only the lengths, and I'd be making up a mechanism from two integers. What I can say is narrower: both failures are behavioral misses of the same kind. The code ran and produced output, and that output violated a structural property the task requires. They weren't crashes or validator rejections.

That distinction matters, because the passes need a caveat too. The regex judge checks four specific criteria, including 15 seeded strings and length preservation. Passing those checks shows the expression behaved correctly on those checks. It doesn't prove the regex is correct in general.

It also says nothing about the more romantic claim nearby. Rule 110 is famously Turing complete when iterated. This task asks for *one update*. A model that writes a correct single step hasn't shown that it represented a universal machine, that the expression can iterate arbitrarily, or anything at all about Turing completeness. The weird-machine framing is a reason to build the task. It isn't something the task measures.

## Five failures, three layers

Now widen the view. The track has five failures across 30 cases, and they don't all happen at the same stage:

| environment | condition | score | where it stopped |
|---|---|---|---|
| regex | surface=medium, depth=easy | 0.208333 | behavioral: length mismatch (32→34) |
| regex | surface=hard, depth=easy | 0.208333 | behavioral: length mismatch (32→66) |
| CSS | surface=easy, depth=easy | 0.416667 | behavioral: partial credit, labelled underfit |
| CSS | surface=easy, depth=medium | 0.0 | source validator: disallowed `import re` |
| SQL | surface=easy, depth=medium | 0.0 | source validator: unterminated triple-quoted string |

Three are behavioral misses: the program ran and got things wrong. Two never reached a behavioral test. The CSS medium-depth patch imported a module that isn't on the allowlist. The SQL medium-depth patch had a syntax error. Both validators reject before any semantics are checked. The validator's own note says it is not a security sandbox. Whatever it is, it's a gate, and these two cases stopped at the gate.

That changes how the "depth" rows read. CSS uses a parity-selector implementation, and depth there means bit count:

| CSS, surface=easy | 3 bits | 4 bits | 5 bits |
|---|---|---|---|
| outcome | FAIL 0.416667 (behavioral) | FAIL 0.0 (source-invalid) | PASS |

SQL's depth is the length of a graph chain:

| SQL, surface=easy | chain 6 | chain 12 | chain 25 |
|---|---|---|---|
| outcome | PASS | FAIL 0.0 (source-invalid) | PASS |

Both rows are non-monotone as archived outcomes. In SQL the middle value fails and the largest passes. In CSS the smallest has the only behavioral failure and the largest passes. But in both, the failure in the middle row is a validator rejection. That's not evidence the model couldn't handle 4 bits or a 12-node chain. It's evidence that on that draw the model wrote a patch that didn't get through the gate. Whether a validator failure is "really" a reasoning failure is a fair question, but the archive can't answer it. Folding these into a depth curve would bury the question.

The CSS surface sweep at 3 bits runs fail, pass, pass for easy, medium, hard. That's the opposite direction from regex. I'm not going to make a pattern out of that either. One run per cell, different task, different judge.

The other three environments are uneventful in this run. Spreadsheet dataflow, the CI dependency graph, and the template interpreter each pass all five selected cells.

For scale: across the whole campaign, the taxonomy has 61 failures among 192 eligible cases, and two provider-coded final rows fall outside that denominator. The labels there hide similar mixtures. Empty patches, source rejections, runtime errors, and malformed actions all show up as FAIL. Two cases labelled "overfit to visible tests" actually have full trusted scores and missing-companion-file notes. The weird-machine track is cleaner than that because everything in it is behaviorally judged and nothing is excluded. But a clean track can still mix failures from different layers.

## Why 25/30 isn't a number about anything in particular

Per environment, the track breaks down as follows:

| environment | eligible | pass |
|---|---|---|
| CI dependency graph | 5 | 5 |
| spreadsheet dataflow | 5 | 5 |
| template interpreter | 5 | 5 |
| SQL fixed point | 5 | 4 |
| CSS state machine | 5 | 3 |
| regex state machine | 5 | 3 |

The pooled 25/30 is accurate bookkeeping. It's a poor *measurement*, because the rows have nothing in common except the axis labels:

- They are different programs.
- Each has its own judge: length preservation and seeded strings for regex, parity behavior for CSS, a fixed-point computation for SQL, dataflow for spreadsheets, a dependency graph for CI, a small language for the template interpreter.
- "Hidden depth" means a 512-character string in one, a 5-bit selector in another, a 25-node chain in a third, and a larger grid in a fourth.

Nothing says those are equally hard, or even hard along the same dimension.

So easy/medium/hard aren't points on a common difficulty scale. They're ordinal labels inside each environment, and a few cells show the labels don't even order outcomes reliably there. Averaging over them gives a number with units of "whatever these six tasks happen to be". It's not a weird-machine capability score, and with one model and one configuration it's certainly not a ranking.

The underlying move isn't new. HELM's case for [broad scenario coverage and multiple metrics](https://arxiv.org/abs/2211.09110) (42 scenarios) is largely an argument against reading a single pooled score this way. [VarBench](https://aclanthology.org/2024.findings-emnlp.946/) already does dynamic variable perturbation, with repeated sampling (five seeds) for its variable-based experiments. I'm citing these as context for the design, not as validation of this campaign. This post doesn't do anything those papers haven't, beyond looking closely at one archive.

## What the source audit adds, and what it doesn't

The useful contribution here is small and specific. Comparing the archived outcomes with the source comparator found the name-plus-hint bundling in the regex surface axis. Without the comparator, "surface deceptiveness" would look like one intervention. With it, we can see it's at least two.

A related audit covered the separate category track, a set of heterogeneous code-repair tasks. A static scan of the clean comparator found ten advertised control or variable axes, across nine category environments, that the environment templates never directly reference. Where that holds, the nominal axis count overstates the number of distinct interventions: a cell labelled "hard" may differ from "easy" only in its label. That finding isn't about the regex task, and it doesn't make the category-track outcomes a theorem or a score. They're still a collection of code-repair results. I mention it because it's the same kind of problem as the regex finding: the label promises a manipulation, and the artifacts may not deliver that manipulation cleanly.

Both audit findings carry the dirty-repository caveat. They describe what the clean source does. They show only by inference what the paid runs saw.

## The experiment I'd fuckingly want

If the question is "does the surface or the depth decide the outcome?", the design has to give each its own handle:

1. **Split the bundled surface manipulation.** Hold the class name fixed and toggle only the performance hint. Then hold the hint fixed (present or absent) and vary only the name. That's a 2×2 on the surface side, not three ordered levels.
2. **Replicate cells.** Generate several equivalent task instances at each input size, randomise their order, and run multiple seeds per cell. With five draws per cell, a 0-for-5 means something that a 0-for-1 can't.
3. **Diff the rendered artifacts before any model sees them.** For every pair of levels, compare the rendered prompt, starter code, visible tests, and judge inputs. If an advertised axis changes no relevant artifact, block it from the sweep. If it changes more than one, record each change as its own factor.
4. **Score layers separately.** Report patch created, source valid, runs without error, and behaviorally correct as distinct outcomes. A validator rejection at 4 bits and a wrong parity answer at 3 bits shouldn't share a column.
5. **Make the regex judge report more than lengths.** Even when length preservation fails, a per-position comparison on the seeded strings would let "+2 characters" become a diagnosis instead of a guess.

Even with all that, the result would be about these task implementations under this judge, not about an abstract ability to detect computational weirdness.

## What this licenses

The archive supports one narrow claim:

> In one archived sweep, with one seed per cell, this model passed the regex Rule 110 task at all three input lengths under the easy surface label and failed both altered-surface variants at the shortest length, where the altered variants change class names and, at the hard level, add an implementation hint.

It also supports a few small descriptive facts:

- Three of the track's five failures are behavioral misses and two are source-validator rejections.
- Three environments passed everything they were given.
- The depth axes measure different quantities in different environments.

It doesn't license:

- a causal claim that names fooled the model
- a claim that depth didn't matter
- a law that surface beats depth
- a calibrated difficulty scale
- a capability ranking
- any statement about Turing completeness

The most interesting thing in the archive is still the pair of integers 34 and 66. I'd just rather find out what produced them than write as if I already know.
