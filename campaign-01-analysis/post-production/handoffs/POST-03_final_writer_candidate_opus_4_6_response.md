---
title: "A Category-Theory Label Is Not a Category-Theory Measurement"
date: 2026-10-03
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
<dt>Original ideas</dt>
<dd>Low-to-moderate — the distinction between a label and a measurement is standard methodology; applying it line-by-line to this archive's source comparator is my contribution.</dd>
<dt>Synthesis</dt>
<dd>High — draws together a frozen paid-run archive, a static placeholder scan, and a clean source comparator that sits outside the archive.</dd>
<dt>Prose</dt>
<dd>Arena-drafted from an evidence packet, then restructured and checked by me against the underlying tables and source audit.</dd>
<dt>Certainty</dt>
<dd>High for counts and source-file observations; medium for any claim that depends on the dirty repository matching the inspected comparator.</dd>
<dt>Importance</dt>
<dd>Modest but practical — a worked example of a general failure: inferring a capability from a track name instead of from the check that produced each verdict.</dd>
</dl>

See `category_theoretic_compositional` in a results table and your mind fills in the rest: the model was tested on functors, on naturality, on the way morphisms compose. That reflex is the problem I want to examine. The name is a promise made by whoever assembled the tasks. The artifact that produced each PASS or FAIL is a judge script and a set of visible tests — code that touched the submission — and if I want to know what was measured I have to read *them*, not the folder they sit in.

I spent time doing that for one archived track of one paid campaign, and in several of the environments I could inspect, the judge and the label are not testing the same thing. This post is a record of what I found and a case for why the distinction matters.

## The number everyone would quote, and why they shouldn't

The track holds 85 recorded rows from a completed paid run of a model the campaign calls Atria-Dawn-Preview, tied to a specific source commit. One row has a final note attributing its terminal failure to a provider transient after bounded retries — nothing to do with the model — so I set it aside as an analysis exclusion, leaving 84 eligible cases. Of those, 57 pass and 27 fail: a rate near 0.68.

That single ratio is the thing I least want anyone to walk away with, because it averages over two scoring guarantees that the campaign's own report treats differently:

| Mode | Eligible | Pass | Fail | What a pass certifies |
|---|---:|---:|---:|---|
| `behavioral_reference` | 5 | 4 | 1 | Output checked against a reference behavior |
| `compile_only` | 79 | 53 | 26 | Submission built and cleared its checks |

The campaign report calls compile-only results **exploratory**. They are not a validated behavioral aggregate. So the honest description of this track is not "68 % category-theory competence." It is: a heterogeneous set of code-repair tasks, overwhelmingly graded in an exploratory mode, spanning 17 environments whose per-environment pass rates run from zero to perfect — with one selected seed per cell and no within-cell replications.

One more boundary before I look at the source code. The campaign repository is recorded as **dirty**. The clean source I inspect is a comparator: all 33 selected config hashes match it, but a matching config hash is not byte-for-byte proof that every task file, visible test, and judge used in the paid run was identical. Every source-level observation below is a statement about that comparator, not a guarantee about what executed in each paid workspace.

## A prompt that promises associativity, a judge that checks shape

Take `compositional_optimizer`. The prompt in the clean comparator describes strict associativity under nested composition — numerical correctness carried across multiple training steps. That is a real categorical claim. Associativity says

$$(f \circ g) \circ h \;=\; f \circ (g \circ h)$$

for every parenthesization. The interesting version here is that the two groupings should still agree *after several optimizer steps*, not just on the first forward pass.

The inspected judge checks output shape and a single state-isolation chain. The visible test is a single-step shape check. Neither artifact is structurally capable of catching the property the prompt advertises: a shape comparison on one step cannot tell you whether two parenthesizations of a three-operation composite stay equal across a multi-step horizon. The gap is the distance between a claim about path-independence and a check that an array has the right dimensions. A model can pass this environment while the implementation quietly violates the law its name invokes.

## A law checked, a convention not

`categorical_lenses` is the one environment here graded under `behavioral_reference`, and it fares better — four passes, one failure. It is also where the mismatch runs in the opposite direction, which I find clarifying.

The prompt describes a lens with a coordinate-zero view. The hidden judge checks the three lens laws — get-put, put-get, put-put — and always checks all three regardless of the config's `STRICT_LAWS` placeholder, which has no reference in the clean environment templates. But the hidden judge does not itself assert the coordinate-zero convention the prompt describes; only a visible test anchors that convention. Prompt, visible test, and hidden judge each carry a different slice of the specification, and none carries all of it.

The single failure is revealing about *kinds* of failure. Its final note is a `source_invalid` verdict: a syntax error, an un-indented block after a function definition. That is not a model that misunderstands lenses; it is a model that emitted code the parser rejected. Four passes and one syntax error are exact outcomes under these checks — not a general referendum on lens theory.

## Zero out of four is not "cannot do sheaves"

`sheaf_physical_constraints` has the starkest headline: zero passes among four eligible rows. Read as a capability score, that says the model cannot reason about sheaf consistency. Read as the checks that ran, it says something smaller and more specific.

The prompt asks for capacity-safe routing but never states the 5:3 ratio the inspected judge enforces on a fixed high-demand vector. The visible test checks output keys and shape, not that ratio. A model can fail here by not inferring a constraint it was never told about — a reasonable miss, and not obviously a category-theory deficit.

More important, the four eligible failures are not the same event:

| Cell | Score | Failure mode | What happened |
|---|---|---|---|
| easy / hard | 0.28 | underfit | Ran, scored partial credit, missed the target |
| medium / easy | 0.28 | underfit | Ran, scored partial credit, missed the target |
| easy / medium | 0.00 | patch\_invalid | Patch file was empty — nothing submitted |
| hard / easy | 0.00 | invalid\_action | Harness could not parse a valid JSON action |

Only the two `underfit` rows are plausibly behavioral misses: the model submitted something, it ran, and it fell short of the hidden ratio. The empty patch is a submission-pipeline event. The unparseable action is a harness-format event. Collapsing a tooling failure, a submission failure, and a partial behavioral miss into one "0/4" erases the distinction a reader needs most.

My first pass through these three environments treated them as the same kind of flaw — "the judge doesn't match the prompt." They are not. The optimizer case under-tests a real property. The lens case has a real judge testing something adjacent to, but narrower than, what the prompt describes. The sheaf case under-informs the model about a judge-side constraint it cannot infer from the prompt. Three different failure geometries, and conflating them would have been its own small methodological error.

## Axes that change nothing

Underneath the task-logic mismatches sits a configuration problem. Each environment advertises intervention axes — `naming`, `symptom_mask` — rendered at easy/medium/hard levels. Five cells per environment then look like a response curve. But a static scan of the clean comparator finds that across nine category-track environments, ten advertised axes have no reference anywhere in the task, judge, or starter files.

`compositional_optimizer` is one of the affected environments: its `MODEL_CLASS` and `LR_VAL` placeholders appear nowhere in the inspected templates, which use `MomentumStep` directly regardless of config. Its five outcomes — three passes, two failures — are therefore not five points on a curve over optimizer classes or learning rates. They are, as far as the comparator can tell, five draws of roughly the same task. (Since the repository was dirty, I file this as observed about the source files and inferred about the executed runs.) The same pattern holds for `categorical_lenses`'s `STRICT_LAWS` placeholder and several others. Nominal coverage can overstate the number of genuinely distinct interventions.

## Failure labels are also claims

That the four `sheaf_physical_constraints` failures are different events is not unique to one environment. Across the full 192-case eligible archive — a larger denominator than this track's 84, and one I want to keep strictly separate — the campaign records 61 failures: 24 empty-patch submissions, 20 substantive `underfit` misses, 10 source-validation errors (disallowed imports, syntax errors), 3 runtime errors, 2 malformed actions, and 2 cases labeled `overfit_visible_tests`.

Those last two are worth pausing on: both carry a trusted score of 1.0 and notes about a missing required companion file, which is not what "overfit the visible tests" means. The label and the evidence disagree. If the taxonomy's own labels can be wrong about the mechanism in a handful of rows, I should not treat any single `failure_mode` tag as a direct window into cognition. Empty patches are facts about the submission pipeline. Disallowed-import rejections are facts about a validator rule. The behavioral signal lives in the `underfit` partial scores and the genuine reference checks — a thinner slice than the raw pass count suggests.

## What would make the label earn its name

None of this is an argument that formal properties cannot be evaluated through code. Lens laws, associativity, and gluing conditions are all, in principle, perfectly checkable. The argument is that checking them requires a contract between five things that currently drift apart: the mathematical claim, the prompt, the visible tests, the hidden judge, and the reference implementation.

For each task, the authors would need to state the property under test, supply counterexamples and valid alternatives, and have an independent oracle confirm that the hidden tests can discriminate a correct implementation from a plausible-but-wrong one — including deliberately wrong submissions as negative controls. Pair that with a build-time assertion that every advertised axis changes something agent-visible or judge-visible, and the name starts to mean something a reader can rely on.

There is precedent for wanting the contract to be explicit rather than averaged away. Holistic multi-scenario evaluation (HELM, Liang et al., TMLR 2023) responded to single-score fragility with breadth — dozens of scenarios and metrics rather than one number. Dynamic variable perturbation (VarBench, Qian et al., Findings of EMNLP 2024) responded with resampling across multiple seeds to separate task signal from instance luck. Both are precedents for "do not trust the label, check the measurement," not validations of this particular campaign, which has one seed per selected cell and — in this track — config axes that an audit suggests were not always wired to anything the model or judge could see.

## What this does and does not license

The archive is real. On these 84 eligible, selected code-repair tasks, under one seed each and almost entirely in an exploratory compile-only mode, Atria-Dawn-Preview produced a mix of passing and failing submissions — with the mix varying by environment and by which failure layer (validator, runtime, format, or substance) happened to fire. The per-environment spread runs from a clean zero to a perfect score.

What the evidence does **not** license is the inference the folder name invites: a claim that the model understands category theory, or a general compositional-reasoning score, or a difficulty ordering across environments. There is no demonstrated common calibration that would let a `hard` sheaf cell and an `easy` lens cell sit on one axis. The results can help improve the benchmark — they point at exactly which prompts, axes, and judges to repair first. They cannot be promoted into a capability claim, because in three of the inspected environments the property being scored and the property being named are not the same thing, and the archive provides no independent replication to distinguish a robust finding from one seed's luck.
