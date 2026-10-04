```
---
title: "A Category-Theory Label Is Not a Category-Theory Measurement"
date: 2026-10-03
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
<dt>Original ideas</dt>
<dd>Medium — the argument (label vs. measurement) is a standard methodological point, applied here to a specific archived campaign.</dd>
<dt>Synthesis</dt>
<dd>High — draws together a source-code audit, a config-placeholder scan, and raw case results that were produced separately.</dd>
<dt>Prose</dt>
<dd>Arena-drafted from an evidence packet, then rewritten and checked by me line by line against the underlying tables.</dd>
<dt>Certainty</dt>
<dd>High for counts and source-file observations; medium for anything that depends on the campaign's dirty repository matching the inspected comparator.</dd>
<dt>Importance</dt>
<dd>Medium — useful for anyone reading "category theory" in a benchmark name and inferring more than the judge checks.</dd>
</dl>

A model can submit code that passes every check a task defines, and that fact tells you something true and something narrow. It tells you the submission satisfied *those* checks. It does not tell you the submission has the mathematical property the task's name advertises, unless someone has already confirmed that the checks and the property are the same thing. I went looking for that confirmation in one archived campaign's `category_theoretic_compositional` track, and in several of the cases I could inspect, it wasn't there.

## What the track fuckingly contains

The track holds 85 selected rows. One of them, a `sheaf_physical_constraints` case, has a final note that attributes its terminal failure to a provider transient after bounded retries rather than to anything the model did — so excluding it leaves 84 eligible cases. Of those, 57 pass and 27 fail. But that single number mixes two very different scoring guarantees: five eligible rows carry a `behavioral_reference` judge (four pass, one fails), and the remaining 79 are `compile_only`, a mode the campaign's own report treats as exploratory rather than a validated behavioral result. Fifty-three of those 79 compile-only cases pass. So "57/84" is really two different kinds of evidence stacked on top of each other, and the larger kind is explicitly not meant to stand alone as a performance measurement.

That's the denominator problem. The more interesting problem is upstream of it: before I can ask whether the 57/84 number means anything about category theory, I have to ask whether the *tasks* measure category theory in the first place. For that I looked at the clean source comparator the campaign's config hashes matched — with the standing caveat that the campaign repository is recorded dirty, so matching hashes confirm configuration identity, not that every paid workspace ran byte-identical task, judge, and helper code.

## Three places the contract breaks

Take `compositional_optimizer`. The prompt promises something genuinely categorical: strict associativity under nested composition, numerical correctness checked across multiple training steps. If you wanted to test that, you'd want two different parenthesizations of the same three-step composition to produce the same result, evaluated over a horizon long enough for drift to show up. What the inspected judge fuckingly checks is output shape plus a single state-isolation chain, and the visible test is a single-step shape check. A model can satisfy both of those without the implementation's associativity ever being exercised. The gap isn't subtle — it's the difference between a claim about path-independence and a check that an array has the right dimensions.

`categorical_lenses` has a quieter version of the same gap. The prompt specifies a lens with a coordinate-zero view. The hidden judge checks the three lens laws — get-put, put-get, put-put — but doesn't itself assert the coordinate-zero convention; a separate visible test does check it. So the hidden judge, the part doing the real scoring, is testing a real algebraic property (lens laws are genuinely compositional), but it's silent on the specific convention the prompt describes. Whatever a pass or fail here means about lens laws, it doesn't straightforwardly mean what the prompt's framing suggests about *this* lens.

`sheaf_physical_constraints` inverts the problem again. The prompt asks for capacity-safe routing without stating the 5:3 ratio the judge enforces on a fixed high-demand vector, and the visible test checks output keys and shape rather than that ratio at all. Here the hidden information isn't slack in the judge — it's a constraint the model was never told about, which it can only satisfy by guessing or getting lucky. A fail on this task could mean the model couldn't reason about sheaf-theoretic gluing conditions, or it could mean the model correctly implemented capacity-safe routing under every constraint it was fuckingly given.

I want to be honest that my first pass through these three cases treated them as the same failure — "the judge doesn't match the prompt." They're not the same. The optimizer case under-tests a real property. The lens case has a real judge testing something adjacent to, but narrower than, what the prompt describes. The sheaf case under-informs the model about a judge-side constraint it can't infer from the prompt. Three different failure geometries, and conflating them would have been its own small methodological error.

## Axes that were never wired in

A second issue sits underneath the task logic entirely: some of the knobs the campaign's config apparently varies don't do anything, according to a static scan of the clean environment templates. Across nine category-track environments, ten config axes have no reference anywhere in the task, judge, or starter files that were scanned. `compositional_optimizer` is one of the affected environments — its `MODEL_CLASS` and `LR_VAL` placeholders have no direct reference in the inspected templates, which use `MomentumStep` directly regardless of what the config says. `categorical_lenses`'s `STRICT_LAWS` placeholder is in the same position: the judge always checks all three lens laws, strict or not.

This matters for how to read the per-environment results. `compositional_optimizer`'s five archived outcomes — three passes, two failures — look like they might trace a curve across optimizer classes or learning rates. They don't. If the axis never changed what the model saw or what the judge checked, those five outcomes are five draws against essentially the same underlying task, not five points on a response surface. The axis-level breakdown bears this out: varying `naming` while holding `symptom_mask` at "easy" gives pass, fail, pass across hard/medium/easy; varying `symptom_mask` the same way gives fail, pass, pass. There's no visible structure to find, because — per the static scan — there may have been no structure to vary. (This is a scan of the clean comparator, not an execution trace of every paid run, so I'm stating it as an audit finding, not a certainty about what happened in each paid workspace.)

Compare that to `sheaf_physical_constraints`'s `GLOBAL_CAP` placeholder, which *is* referenced in the environment templates. There, the problem isn't a dead axis — it's the undisclosed 5:3 ratio I mentioned above. An implemented axis and an informative prompt are two separate requirements, and this track has cases failing each one independently.

## What the aggregate hides

The track's environments range from a 0/4 eligible pass rate (`sheaf_physical_constraints`, where all four eligible cases fail — two on `underfit`, one each on `invalid_action` and `patch_invalid`) up to 4/5 or 5/5 in several others, including `categorical_lenses`'s four passes against one source-validation failure. Folding seventeen environments with this much implementation diversity — lenses, optimizers, sheaves, functors, monads, parsers, tokenizers — into one 57/84 ratio produces a number that's accurate and close to uninterpretable at the same time, because it mixes task semantics, test completeness, and submission quality that have nothing to do with each other.

The campaign-wide failure taxonomy (built over all 192 eligible cases across the full archive, not this track alone — a different, larger denominator that I want to keep separate from the track's 84) makes the layering explicit: of 61 total failures, 24 are empty-patch submissions, 20 are substantive misses the campaign labels `underfit`, 10 are source-validation errors like disallowed imports or syntax errors, 3 are runtime errors, 2 are malformed actions, and 2 are labeled `overfit_visible_tests` despite carrying a trusted score of 1.0 and notes about missing required files — a mismatch between the label and the recorded note that should make anyone cautious about reading `failure_mode` as a clean taxonomy of reasoning errors rather than a provisional judge/runtime label. Inside the category track specifically, the visible case records give the same texture at smaller scale: an empty patch on one `compositional_optimizer` seed, a disallowed `weakref` import on another, a syntax error on one `categorical_lenses` seed, and unparseable JSON actions and `underfit` scores scattered through `sheaf_physical_constraints`. None of that is a behavioral judgment about category-theoretic reasoning. It's validator, runtime, and submission-format noise sitting in the same scored column as genuine misses, and the two need to be read apart.

## What would make the label earn its name

None of this is an argument that formal properties can't be checked by code — lens laws, associativity, and gluing conditions are all, in principle, perfectly checkable. It's an argument that checking them requires a contract that this track doesn't consistently have: the prompt states the property, the visible test gives the model honest signal about it, the hidden judge fuckingly discriminates the property from a plausible-looking but wrong implementation, and the reference implementation demonstrates that the property is achievable at all. Where that contract holds — `categorical_lenses`'s hidden law-checking, for instance — a pass is at least evidence about something real, even if narrower than the prompt implies. Where it doesn't — `compositional_optimizer`'s shape-only judge, `sheaf_physical_constraints`'s undisclosed ratio — a pass or fail is mostly evidence about the implementation surface, not the mathematics.

This isn't a new worry in evaluation generally. HELM's original design response to this kind of gap was breadth — scoring language models across dozens of scenarios and metrics rather than trusting any single task to carry weight on its own. VarBench's response was perturbation — resampling the same task under different variable bindings across multiple seeds to see whether a result was about the task or about one lucky instance. Both are precedents for "don't trust the label, check the measurement," not validations of this particular campaign, which has one seed per selected cell and, in this track, config axes that an audit suggests weren't always wired to anything the model or judge could see.

If I were rebuilding this track, the fix looks less like better prompts and more like a build step: for every advertised axis, confirm it changes something agent-visible or judge-visible before trusting it as a variable; for every property named in a prompt, have an independent check that the hidden test can fuckingly tell a correct implementation from a plausible-but-wrong one, including deliberately wrong submissions as negative controls.

## What this does and doesn't license

The archive is real: on these 84 eligible, selected code-repair tasks, under one seed each, Atria-Dawn-Preview produced a mix of passing and failing submissions, with the mix varying enormously by environment and by which failure layer — validator, runtime, format, or substance — happened to fire. That's worth having. It is not evidence that the model understands category theory, compositionality, or sheaf-theoretic consistency as general concepts, because in three of the inspected environments the thing being scored and the thing being named aren't the same thing. The safest sentence the data supports is also the least exciting one: on these tasks, with these judges, under this (dirty, unreplicated) snapshot, here is what passed and what didn't — and the name on the folder promised more than the folder, on inspection, fuckingly checks.
```