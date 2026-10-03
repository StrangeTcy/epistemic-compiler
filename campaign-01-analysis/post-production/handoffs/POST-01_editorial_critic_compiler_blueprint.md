# POST-01 editorial blueprint

*Compiler synthesis of the two supplied Battle critic reviews. They disagree about which draft to prefer and both answer a winner-selection question rather than fully satisfying the requested blueprint. Treat their recommendations as evidence to inspect, not as a vote. This document is the actionable editorial response for the final-writer stage; it does not select A or B as the winning draft.*

## Proposed thesis

The campaign’s green and red cells do not sit on one calibrated difficulty scale. A displayed outcome compresses several distinct facts: what input or task axis changed, what the judge could actually check (including whether an instance-specific behavioral reference was available), and where the attempt stopped. The denominator and scoring mode matter too. The useful product is a case map with those distinctions visible—not a universal ranking or causal estimate.

Keep the four-question intuition from B as an organizing aid, but do not treat `c = π(x, g, r, t)` as a validated measurement model. In particular, define judge guarantee and reference availability separately if both symbols remain; they are related and could look redundant. A compact “read this cell” table may be clearer and safer than formal notation.

## Opening and working title

Open on the concrete puzzle that the same 131 passes can be reported as 131/194 (raw), 131/193 (excluding only the report-listed transient), or 131/192 (excluding both provider-coded terminal rows). Explain those scopes immediately; do not imply that the 24 pre-scoring omissions are failures. Use the puzzle to ask what the colored grid does—and does not—measure. Do not invent a personal origin story such as “I came wanting one number” unless the author confirms that it is literally true.

Possible title directions: **“A Red Square Is Not One Result”** (concrete, covers judge and stopping layers) or **“The Grid Is Not a Difficulty Scale”** (states the main limit). A’s denominator title is vivid but narrower than the full argument; B’s four-question title is apt but abstract. Choose a final title only after the through-line is set.

## Section-by-section plan

1. **Start with the denominator puzzle.** State the raw 194 selected results: 131 PASS, 63 FAIL. Keep the 24 unscored omissions separate (17 unsupported input modality; 7 gate-blocked before provider access). Show the three fractions and what each excludes. Say that the primary performance sensitivity removes both provider-attributed terminal rows, while retaining the raw report count. The official outage counter lists one; the archive audit found a second terminal note. Do not silently convert an analysis exclusion into a change to the campaign report.

2. **Explain what a green cell guarantees.** Put the post-exclusion split beside the claim: 72 behavioral-reference cases (56 PASS / 16 FAIL) and 120 compile-only cases (75 PASS / 45 FAIL). The report calls compile-only exploratory; do not blend the two into one validated behavioral rate. If mentioning the `epistemic_games` preflight, state that it is an environment-level self-test, not a case-level judge guarantee; it is optional and probably not needed in this post.

3. **Show why “easy / medium / hard” is not a common unit.** Use a small number of concrete contrasts, not a tour of every environment. The regex example is vivid: “hidden depth” is input length (32/128/512), while the surface sweep at length 32 changes the returned length to 34 and 66 for the medium/hard labels. Immediately qualify that the comparator bundles class-name changes and a hard-level performance hint; dirty repository status prevents treating comparator code as proof of the paid-run implementation. CSS and SQL are useful counterexamples because selected “difficulty” cases stop at source validation (`import re` / unterminated triple-quoted string), rather than testing behavior. Keep the CSS partial score (0.416667, or clearly rounded to 0.42) distinct from pass/fail. Every contrast is one selected seed, not an intervention estimate.

4. **Separate terminal layers.** Use one compact table for the 61 eligible failures, split by judge mode if space permits: `patch_invalid` 24 (9 behavioral-reference / 15 compile-only), `underfit` 20 (3 / 17), `source_invalid` 10 (3 / 7), `runtime_error` 3 (0 / 3), `invalid_action` 2 (0 / 2), and `overfit_visible_tests` 2 (1 / 1). Make clear this taxonomy excludes the two provider-coded raw failures. Explain that an empty patch, rejected source, crash, invalid action, missing required companion file, and judged behavioral miss are not interchangeable observations. Do not present the campaign’s labels as a validated psychological taxonomy of model reasoning.

5. **Use the suspicious “overfit” rows carefully.** The evidence packet supports that both rows labeled `overfit_visible_tests` have a trusted score of 1.0 and missing-required-file notes; the MoCo row names `moco_model.py`. This is a real task/judge mismatch worth flagging. It does **not** establish “the model’s code was fine” or prove that the harness alone caused the outcome. Say that the archived score and terminal note conflict with the label, and keep responsibility unresolved unless the primary trace supports more.

6. **Treat family totals as a tempting but uncalibrated summary.** If retaining recurrent-depth 31/33 versus trajectory/synthesis 2/8, decompose the recurrent total immediately: its environments mix behavioral-reference and exploratory compile-only judgments, and its remaining misses include syntax/runtime terminations. Keep the comparison descriptive of these selected tasks only. Do not turn the ratio into “recurrence is easier” or a model-capability ranking. This section can be short; drop the family comparison if it crowds out the denominator/judge/termination argument.

7. **Close with the map and the next experiment.** Propose a per-cell record that exposes (a) the rendered input change, not just the label; (b) judge mode/guarantee and instance-reference status; (c) terminal layer; and (d) the displayed verdict. Then name the next work that would justify stronger claims: verify each axis actually changes the task, unbundle labels from hints, repeat across seeds, and report by judge guarantee and stopping layer. End by stating that this archive is useful for locating cases and implementation questions, not for a general ranking or causal estimate.

## A/B material to retain, and material to repair

- From A, retain the concrete denominator hook, exact axis details (especially regex output lengths), the visible scope boundaries, and the insistence that the archive licenses observations rather than causal claims. Distribute those caveats beside the relevant numbers instead of collecting them all in a long final disclaimer.
- From B, retain the through-line that a cell hides more than one question, the clean sequence from denominator to judge to axis to stopping layer, the compact failure table, and the map/not-leaderboard ending. Use the tuple only as a mnemonic unless its coordinates are rigorously distinguished.
- Neither draft should be copied paragraph-for-paragraph. Neither should claim that the model’s code was “fine” or that the harness was solely at fault for the MoCo row. Avoid an oversized inventory of every family/environment; the essay should remain an argument, not a benchmark report.
- Remove the repeated “fuckingly” wording from both drafts. The house-style packet treats profanity as an emphatic exception, and this exact unusual turn appears in the supplied reference material; repeating it risks borrowing a distinctive phrase rather than establishing voice.

## Claim and citation audit

- **Supported in the attached packet:** the raw/sensitivity denominators; 24 omissions and their two categories; two provider-coded terminal rows versus one in the official outage counter; post-exclusion judge split; compile-only exploratory status; one selected seed per cell; dirty-repository/comparator limitation; regex/CSS/SQL examples; eligible failure counts; and the missing-file evidence for the two mislabeled `overfit_visible_tests` rows.
- **Keep adjacent caveats:** a 33/33 selected-config hash match is not byte-for-byte proof of paid-run task/judge source identity. The inspected clean comparator is not the proven dirty paid-run tree. Static placeholder-axis counts, if used, are a scan of that comparator, not proof that the paid runs inherited those no-ops.
- **No causal or ranking language:** the archive supports local observed contrasts, not a causal surface effect, a shared difficulty unit, or a general capability ordering. Role-separated writing passes are not independent campaign replications.
- **Prior work:** HELM and VarBench are scoped precedents for broad scenario/metric coverage and repeated variable perturbations; they do not validate this campaign. The packet’s references do support the SWE-bench 7.8% statistic for the study’s own patches and test protocol, but it is tangential. Prefer omitting it unless the final article makes a clear, bounded point about test coverage; if retained, cite the listed study and explicitly say the percentage is not transferable to this campaign.
- **First-person/process claims:** do not assert a personal search, a rerun, or a specific authoring process unless the author verifies it. The epistemic-status block can follow the site’s five fields and order, but its attribution must use the project-approved wording and must not imply two independent human writers or independent model replications. Do not expose model labels in public prose.

## Public-site and style checklist

- Jekyll frontmatter: specific title, `date: 2026-10-03`, `layout: post`; if displaying math, put `{% include mathjax.html %}` immediately after frontmatter and before the byline.
- Use the site byline convention. If present, the epistemic-status definition list uses the five fields in this order: Original ideas, Synthesis, Prose, Certainty, Importance. Keep authorship/process language accurate and do not copy attribution claims from reference posts.
- Begin directly in prose; use short, argumentative `##` headings. Favor airy paragraphs and a deliberate alternation of mechanism, evidence, and consequence. Keep tables compact and explicitly scoped; do not imply a common scale.
- Inline links are appropriate for HELM/VarBench and any retained external study. Cite at the point of use, state what each source contributes, and do not present prior work as evidence for Atria outcomes.
- Keep raw counts, denominator choices, judge mode, terminal layer, one-seed scope, and dirty-source caveat traceable. Put each caveat next to the claim it limits.
- Public copy contains no evidence IDs, internal paths, editorial labels, or unsupported authorship/process claims. No causal claim, leaderboard, unresolved TODO, or borrowed distinctive phrase.
- Target the project’s 1,800–2,800-word range without padding. Do not draft the article in this blueprint.
