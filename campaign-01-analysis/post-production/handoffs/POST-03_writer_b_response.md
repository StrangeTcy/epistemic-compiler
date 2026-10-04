```
---
title: "The Checks That Actually Ran"
date: 2026-10-03
layout: post
---
{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
<dt>Original ideas</dt>
<dd>Low-to-moderate. The reframing — treat the judge and visible tests as the real specification and read the track name as a claim to be audited — is mine; the underlying numbers are not.</dd>
<dt>Synthesis</dt>
<dd>Moderate. I am stitching together one frozen paid-run archive, a static placeholder scan, and a clean source comparator that sits outside that archive.</dd>
<dt>Prose</dt>
<dd>Drafted through the usual Arena back-and-forth and then edited down by hand; the arguments and the caveats are mine to own.</dd>
<dt>Certainty</dt>
<dd>High for counts and source-comparator observations; lower for anything about executed paid code, because the campaign recorded a dirty repository.</dd>
<dt>Importance</dt>
<dd>Modest but practical. It is a worked case of a general failure: inferring a capability from a name instead of from the check.</dd>
</dl>

Hand me the name of a benchmark track and I will give you, without thinking, a guess about what it measures. `category_theoretic_compositional` — so the model is being tested on functors, naturality, the way morphisms compose. That reflex is the whole problem. The name is a promise made by whoever assembled the tasks. The thing that fuckingly produced each `PASS` and `FAIL` is a judge script and a set of visible tests, and those are the only artifacts that touched the submission. If I want to know what was measured, I have to read *them*, not the folder they live in.

So this post is an attempt to read the checks instead of the label, for one archived track of one paid campaign, and to be honest about how much daylight sits between the two.

## What the track is, counted carefully

The archive I am looking at is a completed paid run of a model the campaign calls Atria-Dawn-Preview, tied to a specific source commit, and — this matters for everything downstream — the repository was recorded as **dirty**. The clean source I inspect is a *comparator*, not a proof of what the paid workspace executed. All 33 selected config hashes match that comparator, but a matching config hash is not byte-for-byte evidence that every task file, visible test, and judge used in the paid run was identical. Keep that qualifier attached to every source-level claim I make.

The track holds **85** recorded rows. One of them ends in a terminal failure that its own final note attributes to a provider transient after bounded retries, so I set it aside from any performance reading — not by rewriting the raw score, but as an explicit analysis exclusion. That leaves **84 eligible** rows, of which **57 pass and 27 fail**, a rate near 0.68.

That single number is the one I least want you to walk away with, because it averages over two different scoring guarantees:

| Mode | Eligible | Pass | Fail | What a pass certifies |
|---|---:|---:|---:|---|
| `behavioral_reference` | 5 | 4 | 1 | output checked against a reference behavior |
| `compile_only` | 79 | 53 | 26 | submission built and cleared its checks |

The campaign report explicitly calls the compile-only mode **exploratory**. It is not a validated behavioral aggregate. So the honest description of this track is not "68% category-theory competence." It is: a heterogeneous set of code-repair tasks, overwhelmingly graded in an exploratory mode, spanning 17 environments whose per-environment outcomes run all the way from zero passes to perfect scores. The scalar hides that spread, and the spread is the real content.

## Example one: a promise the judge never verifies

Take `compositional_optimizer`. In the clean comparator, the prompt talks about strict associativity under nested composition and numerical correctness carried across multiple training steps. That is a genuine categorical claim. Associativity is the statement that

$$(f \circ g) \circ h = f \circ (g \circ h)$$

for every way you parenthesize a composite, and the interesting version of it here is that the two groupings should still agree *after several optimizer steps*, not just on the first.

Now read the judge. In the comparator it checks output **shape** and a single state-isolation chain; the visible test is a single-step shape check. Those are reasonable programming checks. They are also structurally incapable of catching the thing the prompt advertised: a single-step shape comparison cannot tell you whether two parenthesizations of a three-operation composite stay equal across a multi-step horizon. The property is stated in the prompt and then simply not asserted anywhere that grades the answer. A model can pass this environment while quietly violating the exact law its name invokes.

The environment's five outcomes — three passes, two failures, all compile-only — therefore do not certify associativity. And because the repository was dirty, even this is a statement about the inspected snapshot, not a guarantee about the code that fuckingly ran in the paid workspace.

## Example two: the axes that change nothing

The same environment surfaces a second, quieter problem. Each config advertises two intervention axes — a `naming` axis and a `symptom_mask` axis — rendered at easy/medium/hard levels, which is what lets five cells read like a little response curve. But a static scan of the comparator finds that `compositional_optimizer`'s placeholders for both axes, `MODEL_CLASS` and `LR_VAL`, have **no reference** in the environment's file templates.

If the placeholder for an axis never appears in anything the agent or the judge sees, then moving that axis from easy to hard may change nothing downstream. The five cells stop being a curve over optimizer classes and learning rates and become five draws of roughly the same task. This is not unique to one environment: the scan reports ten such no-reference control/variable axes across nine category environments. The scan is static — it does not execute generation or diff every rendered bundle — so I file this as *inferred* about the executed runs and *observed* about the source files. But the direction is clear: nominal coverage can overstate how many genuinely distinct interventions were run.

The cleanest fix I can imagine is a build-time assertion that every advertised axis measurably changes at least one agent-visible or judge-visible artifact. An axis that moves nothing should fail to build, not silently inflate the count.

## Example three: a law checked, a convention not

`categorical_lenses` is the one environment here graded as `behavioral_reference`, and it does better — four passes, one failure. It is also where the misalignment runs in the opposite direction, which I find clarifying.

The prompt describes a lens with a coordinate-zero view. The hidden judge faithfully checks the three lens laws — and *always* checks all three, regardless of the `STRICT_LAWS` placeholder, which again has no reference in the clean templates. But the hidden judge does not itself assert the coordinate-zero convention the prompt describes. A visible test does anchor that convention. So the thing the prose emphasizes is enforced only by the sample test the agent can read, while the thing the judge guards is the law suite. Prompt, visible test, and hidden judge each carry a different slice of the specification, and none carries all of it.

The one failure in this environment is instructive about *kinds* of failure. Its note is a `source_invalid` verdict: a syntax error — an un-indented block after a function definition in `lenses.py`. That is not a model that misunderstands lenses. That is a model that emitted code which would not parse. Four passes and one syntax error are exact outcomes under these particular checks; they are not a general referendum on lens theory.

## Example four: zero out of four is not "cannot do sheaves"

`sheaf_physical_constraints` is the environment I would most want someone to misread, because its headline is a clean **0** — zero passes among four eligible rows. Read as a capability score, that says the model cannot reason about sheaf consistency. Read as checks-that-ran, it says something much smaller and more interesting.

Start with the specification gap. The prompt asks for capacity-safe routing but never states the 5:3 ratio that the inspected judge enforces on a fixed high-demand vector. The visible test checks output keys and shape, not that ratio. So a model can fail here purely by not inferring an unstated numerical constraint — which is a reasonable thing to miss, and not obviously a category-theory deficit.

Then look at *why* each of the four eligible rows failed, because they did not fail the same way:

| Cell | Verdict | Normalized failure | What fuckingly happened |
|---|---|---|---|
| easy / hard | FAIL (0.28) | underfit | ran, partial score, missed the target |
| medium / easy | FAIL (0.28) | underfit | ran, partial score, missed the target |
| medium / easy (naming) | FAIL (0.00) | patch_invalid | patch file was empty |
| hard / easy | FAIL (0.00) | invalid_action | could not parse a valid JSON action |

(The fifth cell is the provider-transient row I excluded.)

Only the two `underfit` rows are plausibly a behavioral miss — the model submitted something, it ran, and it scored partial credit against the hidden ratio. The other two are not about sheaves at all: one is an **empty patch** (nothing was submitted to grade) and one is a **malformed action** the harness could not parse. Collapsing a tooling failure, a submission failure, and a partial behavioral miss into one `0/4` erases exactly the distinction a reader needs. A validator failure, a runtime failure, a tool-parsing failure, and a conceptual miss are four different events wearing the same `FAIL`.

## The label on the failure is also a claim

That last point generalizes, and it is worth stating plainly: `failure_mode` is a campaign-and-judge label, not a validated taxonomy of what went wrong inside the model. Across the broader eligible campaign set (192 cases, a denominator I am keeping distinct from this track's 27 fails), the recorded modes include 24 `patch_invalid` rows that are all empty patches, 20 `underfit`, 10 `source_invalid`, 3 `runtime_error`, 2 `invalid_action`, and 2 rows labeled `overfit_visible_tests`. Those last two are the tell: both carry a trusted score of 1.0 and notes about a missing required companion file, which is not what "overfit the visible tests" means. The label and the evidence disagree in at least those two cases. If the label can be wrong about the mechanism twice in a handful of rows, I should not treat any single failure-mode tag as a direct window into cognition.

So when I see a large block of `patch_invalid`-as-empty-patch, I read it as "the agent, in this harness, sometimes submitted nothing," which is a fact about the submission pipeline. When I see `source_invalid` from a disallowed `import weakref`, I read it as a validator rule the model tripped, not a theorem it failed to grasp. The behavioral signal is the `underfit` partial scores and the genuine reference checks — a much thinner slice than the 57 passes make it look.

## What a benchmark would need to earn the label

None of this says formal mathematics can't be evaluated through code. It says the evaluation needs a contract, and the contract has to connect five things that currently drift apart: the mathematical claim, the prompt, the visible tests, the hidden judge, and the reference implementation. Concretely, for each task I would want the authors to state the property under test, supply counterexamples and valid alternatives, and have an independent oracle confirm that the hidden tests fuckingly discriminate the intended property from merely plausible code that happens to compile. Pair that with the build-time axis check from earlier — every advertised intervention must move a visible or judge-visible artifact — and the name starts to mean something a reader can rely on.

There is prior art for wanting the contract to be explicit rather than averaged away. Holistic multi-scenario, multi-metric evaluation and dynamic variable-perturbation benchmarks both exist precisely because a single scalar over heterogeneous tasks hides too much. I cite them only as precedent for the shape of the worry, not as validation of this campaign.

## What this licenses, and what it doesn't

Here is the narrowest claim the evidence supports. On these selected tasks, under these particular judges and visible tests, and almost entirely in an exploratory compile-only mode, Atria-Dawn-Preview produced a mixed bag: 57 of 84 eligible rows passed, the per-environment spread ran from a clean zero to perfect, and a meaningful share of the failures were empty patches, syntax errors, disallowed imports, and unparseable actions rather than conceptual misses. All of that is a statement about the inspected source comparator and one dirty-repository archive with a single seed per cell — no replications, no byte-for-byte proof of the executed code.

What it does **not** license is the thing the folder name invites: a claim that the model understands category theory, or a general compositional-reasoning score, or a difficulty ordering across these environments. There is no demonstrated common calibration that would let a `hard` sheaf cell and an `easy` lens cell sit on one axis. The results can genuinely improve the benchmark — they point at exactly which prompts, axes, and judges to repair first. They cannot be promoted into a capability ranking, and the moment I let the label do my reading for me, I've measured the folder instead of the model.
```