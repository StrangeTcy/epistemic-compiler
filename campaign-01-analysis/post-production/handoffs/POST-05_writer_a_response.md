---
title: Length Holds, Names Break — What One Sweep of Surface and Size Actually Shows
date: 2026-10-03
layout: post
---
*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Local contrast between length-stable regex passes under one surface and length-mismatched failures under renamed surfaces in a single-seed pilot; explicit separation of source-validator events from behavioral underfit.</dd>
  <dt>Synthesis</dt>
  <dd>Heterogeneous code-task outcomes from one paid campaign archive, read against a clean-source comparator and prior multi-scenario/perturbation work, without claiming a shared depth scale or causal surface effect.</dd>
  <dt>Prose</dt>
  <dd>First-person technical narrative written from the Arena campaign evidence packet and style constraints.</dd>
  <dt>Certainty</dt>
  <dd>High on the recorded cell outcomes, failure notes, and dirty-repository flag; low on any isolated cause or general weird-machine detection claim.</dd>
  <dt>Importance</dt>
  <dd>Medium for measurement hygiene in code-agent evaluation; low as a capability ranking.</dd>
</dl>

I keep returning to five cells. Three of them look almost boring: the same model, seed 0, produces a regular-expression encoding of one Rule 110 update that preserves length on input strings of 32, 128, and 512 characters. The other two, still at length 32, collapse. One emits length 34; the other emits length 66. The judge records both as underfit. The only advertised change between the passing trio and the failing pair is the surface label—easy versus medium or hard.

That contrast is sharp enough to feel like a finding. It is also exactly the kind of pattern that evaporates once you ask what else moved with the label. This note stays inside the archive: one selected seed per cell, a dirty repository flag, and a clean-source comparator that is not proof of the paid-run workspace. The question is not whether the model “sees weird machines.” The question is what these particular cells license, and what they carefully do not.

## The track is six programs, not one depth axis

The weird-machine family in the archive contains six environments: a regex cellular-automaton step, a CSS parity selector, an SQL fixed-point chain, a spreadsheet dataflow, a CI dependency graph, and a small template interpreter. Thirty eligible selected cases; twenty-five pass under behavioral_reference judges. That fraction is a description of these implementations and this run. It is not a calibrated score of hidden-depth competence.

Each environment defines its own size parameter and its own success criteria. Regex checks output length plus a handful of fixed seeded strings. CSS checks parity behavior while the bit count moves from 3 to 4 to 5. SQL runs a fixed-point query whose chain length is varied. Spreadsheets check dataflow over class-name and grid-length contrasts. CI checks a dependency graph. The template interpreter checks a miniature language. A 512-character string, a 5-bit selector, a 25-node chain, and a larger grid are not interchangeable units of computational demand. Adding the passes therefore mixes distinct programs, distinct judges, and distinct notions of “larger.”

The same non-monotonicity appears inside single environments. Under the easy surface the CSS cases score a partial 0.416667 at 3 bits, a source-invalid zero at 4 bits (disallowed top-level import of `re`), and a clean pass at 5 bits. The surface sweep at 3 bits is fail/pass/pass. SQL passes at chain lengths 6 and 25 yet fails source validation at length 12 with an unterminated triple-quoted string. The spreadsheet, CI, and template environments pass all five of their selected cells. These are heterogeneous code-repair outcomes. They do not form a theorem, a scalar difficulty scale, or evidence that the model detected an underlying machine in any general sense.

One Rule 110 update encoded in regex does not establish Turing completeness, arbitrary iteration, or that the model internally represented a “weird machine.” The judge only ever saw length preservation and fifteen seeded strings. Passing those checks is local.

## The regex contrast is real and confounded

Hold the surface at easy and the three length cells all pass. Hold length at 32 and switch the surface to medium or hard: both fail with length mismatches (34 and 66). The failure notes are explicit morphisms collapsed on length. That is the cleanest surface-versus-size pattern the track contains.

It is also confounded by construction. In the clean-source comparator the surface levels correspond to different class names. The hard prompt additionally inserts an implementation-performance hint. A name change can alter retrieval or coding conventions even when the underlying transition rule is unchanged; an extra hint changes the instruction itself. The design therefore bundles at least two surface factors with the nominal label. There is one seed-0 run per selected cell. No factorial separation, no repeated sampling, no population of equivalent task instances. The archive supports the exact response pattern that was observed. It does not support the causal claim that class names fooled the model, that the performance note distracted it, or that input length was irrelevant.

A plausible and still-untested hypothesis is that the renamed classes or the added hard-level hint mattered more than string length for these two failures. The present sweep cannot distinguish that hypothesis from ordinary sampling variation or from their interaction. I am stating it as speculation, not as an inferred effect.

## Failure layers are not interchangeable

Across the broader eligible set the scalar PASS/FAIL label conceals different terminal events: empty patches, source-validation failures, runtime errors, malformed actions, and behavioral underfit. In the weird-machine track itself the two regex failures are underfit (length mismatch after a patch was produced). The CSS medium-depth cell is source_invalid because of a disallowed import. The SQL medium-depth cell is source_invalid because of a syntax error in a triple-quoted string. Those validator rejections occurred before any behavioral test of parity or fixed-point semantics. They are not evidence that the model failed to grasp the intended computation; they are evidence that the produced source did not clear the static gate.

I keep the layers distinct on purpose. A source-invalid or runtime failure is a different kind of miss from an underfit that reaches the judge and then mismatches length or parity. Collapsing them into a single “fail” rate erases exactly the diagnostic information the archive still contains. Provider-terminal rows sit outside the main taxonomy denominator entirely; they are recorded but not folded into the behavioral counts used here.

All thirty weird-machine cells carry the behavioral_reference judge guarantee. There are no compile-only outcomes inside this family to misread as validated behavior. The 25/30 figure is therefore a behavioral-reference pass count under the stated eligibility rules, nothing more.

## One seed, dirty tree, comparator only

Every selected cell is a single seed-0 draw. Subsequent editorial or model-role passes are not independent replications. Most contrasts are sparse one-factor substitutions around a baseline rather than full factorials or interaction tests. That design is enough to surface interesting local patterns; it is not enough to estimate cell-level variance or to claim robustness.

The campaign archive records the repository as dirty. All thirty-three selected configuration hashes match the clean comparator snapshot, yet exact identity of the task, starter, visible-test, and judge code that actually ran remains unresolved. Observations drawn from the clean source—class-name differences, the hard-level performance note, the absence of direct template references for certain advertised axes in the wider category track—are therefore comparator findings. They do not establish the precise paid-run workspaces. I treat them as such.

The same caution applies to the adjacent source-audit result that several nominal axes in the broader category track left no direct reference in the inspected templates. That is useful benchmark QA. It is not direct evidence about the regex surface manipulation, and the dirty flag still attaches.

## What the measurement tradition already knew

None of the methodological worries are new. Dynamic variable perturbation and repeated sampling already appear in VarBench; broad multi-scenario, multi-metric evaluation is the point of HELM. Other lines of work have examined epistemic-logic tasks, higher-order belief, causal templates for theory-of-mind, and the gap between plausible patches and full developer test suites. The contribution of this sweep is narrower: a concrete local pattern (length-stable passes under one regex surface, length-mismatched failures under the others) plus an explicit source-comparator audit that flags the name-plus-hint confound. Because the repository was dirty, even that audit stops short of proving exact runtime identity.

I am not claiming priority. I am claiming that the archive makes the confound visible and that the right response is to keep the claim local.

## A cleaner separation would look different

If the goal is to isolate surface from size, the next design writes the factors apart. Fix the class name and vary only the implementation hint; then vary names while holding the hint constant. Generate multiple equivalent task instances at each input size, randomize order, and draw multiple seeds. Before any model call, diff the rendered prompt, starter code, visible tests, and judge inputs across levels; block any advertised axis that changes no relevant artifact. Score exact behavioral match separately from patch validity and from source/runtime clearance. Only then does a length-invariance claim or a surface-sensitivity claim become estimable rather than anecdotal.

The present data cannot run that experiment retroactively. They can only show where the entanglement lives.

## What the evidence licenses

In one archived, single-seed sweep the model produced length-preserving regex updates for strings of 32, 128, and 512 characters under the easy surface label, and produced length-mismatched outputs (34 and 66) under the medium and hard surface labels at length 32. The surface manipulation bundled class-name changes and, at hard, an extra performance hint. Four other environments contributed additional passes and a pair of source-validation failures; two more environments passed every selected cell. The aggregate 25/30 is a heterogeneous count across six distinct programs and judges, not a shared depth metric.

These observations do not establish that the model detects computational weirdness in general, that surface deception systematically beats hidden depth, that input length is irrelevant, or that any particular factor caused the two regex failures. They do not yield a common difficulty scale, a capability ranking, or a Turing-completeness result. They do show, concretely, that surface labels, size parameters, validators, and task semantics must be disentangled before anyone treats the cells as evidence about “what the model saw.” The useful residue is the map of where those distinctions failed in this run, and the reminder that a dirty tree plus one seed per cell is a pilot, not a proof.
