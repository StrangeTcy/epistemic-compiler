---
title: "Two Output Lengths, One Unanswered Question"
date: 2026-10-03
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The central reading is that a sharp local contrast can be useful without establishing its cause. It is an interpretation of saved results, not a new experiment.</dd>
  <dt>Synthesis</dt>
  <dd>This post reads the regex results alongside the other tasks in the same track, the available source comparison, and prior evaluation work.</dd>
  <dt>Prose</dt>
  <dd>This essay organizes saved campaign results and source-comparison notes. No additional cases were run.</dd>
  <dt>Certainty</dt>
  <dd>High for the recorded outcomes and notes. Lower for claims about the exact code used in the campaign run, because the record says some working files had uncommitted changes. The saved results do not identify a cause for the two output-length mismatches.</dd>
  <dt>Importance</dt>
  <dd>A descriptive result from one model, one answer service, and one evaluation setup. Each selected task setting was run once, so this is a clue for a better experiment, not a general score.</dd>
</dl>

In one saved code-repair campaign, two versions of a regular-expression task began with 32-character inputs and produced outputs of 34 and 66 characters. Both results are marked **FAIL**. Three other versions of the same task are marked **PASS**, including one with a 512-character input. That is a sharp contrast—and a small one.

The campaign’s results table has one row for each selected task setup. Here, a *case* means one combination of a task and its settings, not every retry or saved folder. The track discussed in this post contains 30 such cases across six task types. The campaign tested one model, Atria-Dawn-Preview, using one answer service and one set of evaluation settings. Each case used one seed: the randomization setting was 0, and the same setup was not run again. For cases that reach behavioral testing, a *judge* is the software that checks the submitted code against expected task behavior. These details matter because the table’s cases are different settings, not repeated tries at the same problem.

The campaign groups these tasks under the label “weird machine.” I use that name only for the track: six small code-repair tasks built around unusual ways of describing or implementing a computation. The label does not show that a model recognized a general kind of machine. The regex task is the clearest place to see both what the saved results show and where they stop.

## The regex pattern is clear; its cause is not

The task asks the model to implement an update of a cellular automaton: a line of binary cells, or zeros and ones, changes according to a rule about neighboring cells. The model had to express that update using regular expressions, or *regex*: text patterns that can find and replace parts of a string. The task’s judge checks that the solution uses regex instead of an explicit loop over the string, matches a known example, preserves output length, and agrees with expected results on a set of test strings. Passing means passing those specific checks, not that the program works for every possible input or for repeated updates. This one-step result is not evidence of Turing completeness—the formal ability to carry out any computation a general-purpose computer can perform.

The saved results for the five selected regex cases are:

| Surface setting | Input length | Result | Saved judge note |
|---|---:|---|---|
| easy | 32 | PASS | No failure note recorded |
| easy | 128 | PASS | No failure note recorded |
| easy | 512 | PASS | No failure note recorded |
| medium | 32 | FAIL | Length mismatch: 32 in, 34 out |
| hard | 32 | FAIL | Length mismatch: 32 in, 66 out |

“Surface setting” means the task’s label and framing—in this case, easy, medium, or hard—not the size of the input string. At first glance, the table invites a simple story: the model handled the longer inputs under the easy label, but stumbled on two altered labels at the shortest input length. The tempting conclusion is that the surface mattered more than size.

The table cannot establish that. Each setting has one run, so the three easy-label passes do not show that performance is stable at larger sizes. A new run could pass or fail. The two altered-label outcomes also do not show that the names, the instructions, or any particular feature of the task caused the errors. The notes tell us the output lengths did not match; they do not explain why.

There are two comparisons tucked into the table. Changes in input length appear only under the easy surface, while the medium and hard labels appear only at the shortest input. The missing combinations matter: we do not know how either altered version behaves at longer lengths. A pass on the longest easy case is not a direct comparison with a hard-label case at that same size. That unfilled part of the table is a question for another experiment, not a gap the current results can answer.

There is another complication in the task code. I inspected a clean copy of the source repository as a comparison. In that copy, the surface labels use different class names, and the hard version adds a performance hint to the prompt. The proposed “surface” change therefore bundles at least two things: a name change and an extra instruction. If those details also appeared in the paid run, either could matter; the saved results cannot isolate them.

The source record adds a limit to that comparison. It marks the campaign repository as “dirty,” meaning some working files had changes not represented by the recorded commit. All 33 selected configuration files match the clean comparison copy. That is useful, but it does not prove that the exact task text, starter code, tests, grading rules, and helper files used in the recorded run were identical. The class-name and hint observations are findings about the comparison copy, not proof of every file the model saw. Matching the setting files is like confirming the recipe’s settings, not every ingredient and tool used that day. The task text, starter code, checks, and helper code may still differ. Because the dirty changes are not preserved in the archive, the clean copy is a guide to the likely setup, not a verified reconstruction.

So I can report the pattern precisely: easy-label cases passed at the three selected lengths, and the medium- and hard-label cases failed at length 32 with the recorded output mismatches. I cannot turn that into “the model was fooled by the names,” “the hint caused the errors,” or “length did not matter.” The results are a reason to test those possibilities separately, not a result that settles them.

## Five failures stopped in different places

All 30 cases in this track were assigned a judge designed to compare a repair with the task’s expected behavior. But a submitted program can be rejected before the judge gets to test that behavior. A *source check* is a preliminary check for issues such as invalid syntax or a disallowed import. If it rejects the code, the result tells us the submission did not get through that gate; it does not tell us whether the code would have behaved correctly.

The five recorded failures break down this way. The partial CSS score means the submitted program was judged but fell short; the other two code-gate failures never reached a behavior check. That difference is not a technicality: a broken program file and a program that runs but gives a wrong answer are different evidence about what happened.

| Task setting | Where it stopped | What the saved record says |
|---|---|---|
| Regex, medium label, input 32 | Behavior check | Output was 34 characters instead of 32 |
| Regex, hard label, input 32 | Behavior check | Output was 66 characters instead of 32 |
| CSS task, 3 bits | Behavior check | Partial score: 0.416667 |
| CSS task, 4 bits | Before behavior check | A top-level Python `re` import was disallowed |
| SQL task, chain length 12 | Before behavior check | A triple-quoted string was left unfinished |

The CSS task uses styling rules for web pages to test parity—whether a count is odd or even—while changing the number of 0/1 input values. Its easy-label cases receive a partial score at 3 bits, are rejected by the source check at 4 bits, and pass at 5 bits. At 3 bits, the easy, medium, and hard surface settings go fail, pass, pass—the opposite direction from the regex contrast. The rejected import is Python’s regular-expression library; the campaign’s source check did not allow that import at the top level. This is a code-policy rejection, not a test of whether the model understood the parity rule.

The SQL task uses a database query to follow a chain of states. It passes at chain lengths 6 and 25, while the length-12 submission is rejected because a quoted string in the code was never closed. Again, that failure happened before a behavior test. These uneven outcomes are worth reporting, but the labels easy, medium, and hard do not correspond to one shared measure of difficulty across tasks. The campaign calls its size setting “hidden depth,” but that label points to different things here: input-string length in regex, bit count in CSS, and chain length in SQL. It is not a common scale.

## Twenty-five of thirty is a count, not a capability score

The track contains five selected cases for each of six different tasks: the regex update; the CSS parity test; the SQL query; a spreadsheet task where formulas pass values between cells; a CI, or continuous-integration, task about dependencies in automated software checks; and a small program that interprets templates. The saved results show 25 PASS and 5 FAIL. By task, the counts are CI 5/5, spreadsheet 5/5, template interpreter 5/5, SQL 4/5, CSS 3/5, and regex 3/5.

Those totals describe this set of rows. They are not a measure of general code ability. The tasks ask for different things and use different tests: a 512-character string, a five-bit input, a 25-step query chain, and a larger spreadsheet are not interchangeable units of computational difficulty. Even within a task, the same FAIL label can describe a behavior mismatch or a program that was stopped before its behavior was tested. Adding the pass counts is accurate arithmetic; treating the sum as one calibrated score would imply more comparability than the experiment provides.

This is why I keep the local regex result separate from the 25/30 total. The other tasks give useful context, but they do not replicate the regex conditions or explain the output lengths. They make the report broader, not the cause clearer.

## A better sweep would separate the changes

The next experiment can be designed around the uncertainty in this one. First, vary class names and the performance hint independently: keep the name fixed while adding or removing the hint, then change names without changing the hint. Cross those choices with the three input lengths. That would show whether either manipulation tracks with the output mismatch, rather than changing both at once.

One run per setting is not enough to tell a stable pattern from run-to-run variation. I would generate multiple equivalent task instances for each combination, use several seeds, and randomize the order of the runs. Before sending each task to the model, I would compare the exact prompt, starter code, visible tests, and grading program across settings. Those are the materials that determine what the model is asked to do and what the judge later accepts.

The reporting should keep the steps separate too: was a code patch saved, did it pass the source check, did it run, and did its behavior pass the task-specific tests? A single PASS or FAIL is convenient, but it hides where an attempt stopped. The five failures here show why that detail is worth keeping.

There are precedents for pieces of this design. [HELM](https://arxiv.org/abs/2211.09110) reports language-model results across 42 scenarios and multiple measures. [VarBench](https://aclanthology.org/2024.findings-emnlp.946/) dynamically changes task values and, in its variable-based experiments, runs five evaluations with different sampled values. These are context for broad reporting and repeated sampling, not evidence about this campaign or a claim that its design is new.

The useful conclusion is modest. One archived run shows three passing easy-label regex cases at lengths 32, 128, and 512, alongside two length-32 failures under altered labels, with outputs of 34 and 66 characters. The clean source comparison reveals that names and a performance hint changed together, while the uncommitted source changes prevent me from treating that copy as a verified account of every file used in the run. This result does not show that “surface deception beats hidden depth,” or that the model recognizes weird machines in general. It does show exactly what a better experiment should separate next.