# Editorial blueprint — POST-05

## 1. Conceptual structure and thesis

**The real argument** (which both drafts gesture at but neither fully centers): A one-seed sweep produced a visually sharp contrast — length invariance under one surface label, length-mismatched failures under two others at the shortest length — but the manipulation bundles at least two factors (class name + hard-level hint), the five failures occur at *different stages of the pipeline* (behavioral vs. source-validator), and the aggregate 25/30 is a bookkeeping total over six incomparable programs. The piece is about why that archive *cannot* answer the question it looks like it answers, and what a design that could would need.

**Structural divergence:**
- **A** moves linearly from aggregate (25/30) → regex contrast → failure layers → design caveats → prior work → cleaner experiment → what the evidence licenses. It is tight but withholds the regex table and never shows the reader the 34/66 numbers in their visual context until near the end.
- **B** opens question-first, uses two tables early (regex 5-cell grid; failure stratification), and does the layer-separation argument *before* the aggregate critique. This ordering is stronger: the reader sees the shape of the data before being told what to make of it.

**Recommended shape for the final piece:**
1. Open on the two integers (34, 66) or on the renamed-class puzzle — concrete, not aggregate.
2. Lay out the task family and the 5-cell-per-environment design so the reader knows what "25/30" is made of.
3. Show the regex table and admit the confound in the *same* section.
4. Separate behavioral miss from source-invalid before pooling anything.
5. Explain why 25/30 is bookkeeping, not measurement.
6. State the comparator-vs-dirty-tree boundary explicitly, once, where it bites.
7. Describe the cleaner experiment.
8. Close with a precise license statement.

**Cut from source draft / A:**
- The "weird-machine benchmark asks whether a model can infer…" opener (abstract definition before specifics).
- The paragraph that reintroduces the regex contrast *after* the aggregate — avoid two passes at the same material.
- A's "What the measurement tradition already knew" is slightly defensive; fold the HELM/VarBench reference into the aggregate-critique section as context, not a standalone turn.

**Move:**
- Failure-layer separation (currently buried in A, well-placed in B) should sit immediately after the regex table so the reader learns early that FAIL ≠ FAIL.

## 2. Opening

**Comparison:**
- Source draft opens with abstract definition. Low tension, high setup cost.
- **A** opens on "I keep returning to five cells" — specific, first-person, states the puzzle in two sentences. Good tension, limit stated by paragraph two.
- **B** opens with a conditional: "Suppose you rename a class and the model's regex stops preserving string length." This is the style-reference register (question-led, cf. "Suppose I want you to make the wrong decision"). Fastest to tension and to limit.

**Fresh opening strategy (do not copy either):** Open on the asymmetry a reader can hold in their head *before* any framing — a concrete scene of three passing lengths and two failing renamed cells, stated as what-happened, followed immediately by the limit: single seed, dirty repo, comparator-only. The opener should name what the post refuses to claim (a general weird-machine detector, a surface-beats-depth law) before it discusses what it does claim. Do not define "weird machine" in the opener; let the examples do the definitional work.

## 3. Examples and technical depth

**Keep (exact, source-grounded, useful):**
- Regex table (B's five-row table). This is the central exhibit; it must appear.
- Explicit numbers: 32/128/512 input lengths; outputs 34 and 66 at input 32; CSS 0.416667 / 0 / 1.0 at 3/4/5 bits; SQL passes at chain 6 and 25, source-invalid at 12; CSS validator rejected `import re`; SQL unterminated triple-quoted string.
- Per-environment pass counts (B's second summary table: CI 5/5, spreadsheet 5/5, template 5/5, SQL 4/5, CSS 3/5, regex 3/5).
- Failure stratification table (B's "three layers" table). Useful because it visually enforces the behavioral/source-invalid distinction.

**Cut / avoid:**
- Equations: none needed. Rule 110 is referenced, not derived. Do **not** introduce an equation; it would be decorative here. (The style reference uses math only when the formalism itself is the subject.)
- Diagrams: not needed. The two tables carry the argument. A pipeline-stage diagram would be decorative given the small failure count.
- Do not add a `{% include mathjax.html %}` block — there is no math in this post.

**Judge criteria depth:** State once that the regex judge checks length preservation plus 15 seeded strings (four criteria total). That's the right level of detail; do not elaborate beyond it.

**Rule 110 handling:** B's half-paragraph on "Rule 110 is Turing complete when iterated; this task asks for one update" is exactly right and should be retained in substance. A mentions it only glancingly.

## 4. Generic AI prose and benchmark-report tone

**Issues to eliminate:**
- "That contrast is sharp enough to feel like a finding" (A) is good — keep that register but do not multiply it.
- A has mild score-led tone in the "The track is six programs, not one depth axis" opening sentences; prefer B's question-first framing of the same material.
- Avoid stock transitions: "Furthermore," "Importantly," "It is worth noting." Neither draft overuses these; keep that discipline.
- Avoid empty superlatives: "sharp," "clean," "cleanest" are used sparingly in both — fine, but do not let them stack.
- **Both drafts contain the literal token "fuckingly"** in multiple places (A: once; B: three times). This is a sanitized remnant of findings-text expletives in the evidence packet. Strip it everywhere. The findings text itself used it as emphasis; it must not appear in public prose.
- Do not report 0.8333333333333334 as a percentage with that precision; "25 of 30" is the readable form. Avoid "83.3%" framing because the pooled rate is specifically what the post argues against.
- Avoid "the model passed/failed" when "the recorded cell passed/failed" would be more honest — this is a running tone issue in benchmark writing. Both drafts mostly handle it; keep the discipline.

## 5. Transitions and caveat placement

Each limitation must sit beside its claim:

- **Dirty-source / comparator caveat**: attach it specifically to the sentence that says the surface levels differ in class names *and* the hard prompt adds a performance hint. Do not relegate it to a late methodology paragraph.
- **Judge-mode / defect**: when stating 25/30, immediately note that all 30 are behavioral_reference-judged (so the number is not inflated by compile-only). This is a *supportive* caveat and must not be omitted even though it strengthens the number — the point is that even clean grading does not make the count a capability measure.
- **One-seed boundary**: attach to any sentence that could be read as an effect estimate. Especially the regex contrast and the "non-monotone" CSS/SQL rows.
- **Provider/exclusion**: the weird-machine track has no excluded rows and no provider-terminal rows. State this once, briefly, when introducing the 30-case denominator. Do not import the broader 192/61 taxonomy except as a one-sentence scale check — B uses it well; A omits it.
- **Speculative hypothesis**: the name-or-hint-mattered-more-than-length claim must stay explicitly flagged as speculation (both drafts handle this; keep B's plainer "I'm labelling it plainly as speculation" register).

**Specific placement fixes:**
- Do not let the comparator caveat and the dirty-tree caveat drift into separate paragraphs; they are one point and should be stated once, where it bites hardest (the moment the "class name + hint" bundle is named).
- The "clean comparator shows X about the category track" aside (ten no-reference axes) should be brief and clearly marked as *adjacent* evidence — B handles this well; A buries it.

## 6. Unsupported claims and claim traceability

**Statements to remove or narrow:**
- Any phrasing that treats the regex failures as caused by surface deception. The data support a response pattern, not a cause.
- Any framing of the aggregate 25/30 that reads as a capability number. Both drafts avoid this; the final must as well.
- "Length invariance" as a property of the model: narrow to "three passes at three lengths under one surface label, which is not an invariance estimate."
- "The model represented a weird machine": do not assert; the judge saw length + 15 seeded strings.
- Do not claim Turing completeness, arbitrary iteration, or general regex correctness were demonstrated.
- Do not describe the clean-source observations as facts about the paid run.
- Do not claim novelty against HELM/VarBench. Cite them for context only; the targeted prior-work check supports no "first" or exhaustive-novelty claim.

**Substantiate:**
- Every table number must trace to the evidence packet exactly. Allowed numeric vocabulary includes: 30, 25, 5, 3, 4, 32, 34, 66, 128, 512, 6, 12, 25, 0.416667, 0.208333, 0.0, 1.0, 15, 110, 33, 42, 192, 61, 10, 9. Do not round 0.416667 or 0.208333 in table cells.
- When citing HELM "42 scenarios" and VarBench "five seeds," keep those exact figures from the references.

**Do not invent:**
- Mechanistic stories for +2 or ~2× length (B wisely refuses this; A doesn't attempt it — keep the refusal).
- Any seed count other than 1 per cell.
- Any claim about what the paid-run source actually contained beyond what the comparator shows.
- Any author identity beyond the stated byline and the honest "written in an Arena pass from a compiled evidence packet" framing. Do not invent collaborators or external reviewers.

## 7. Public-site fit

**Jekyll frontmatter:**
- `title:` — avoid colons unless quoted; B wisely quotes "Thirty-Four Characters Out of Thirty-Two." Pick a title that is specific and non-grandiose; both A and B are acceptable models. Avoid "weird machine" in the headline since the post argues against treating it as measured.
- `date: 2026-10-03` (exact).
- `layout: post`.
- **No** `{% include mathjax.html %}` — no math in this post.

**Byline and epistemic status:**
- Exact byline: `*by <span class="icon-self">StrangeTcy</span>*`.
- `<dl class="epistemic-status">` with the five dt/dd pairs in order: Original ideas, Synthesis, Prose, Certainty, Importance. B's content is better calibrated (explicit "modest," "low for any causal reading," honest Arena-pass note). A's is adequate but slightly over-polished.
- Prose field: honestly describe the Arena writing pass from the compiled evidence packet; do not invent an author process beyond that; do not copy author-process claims from the style reference posts.

**Voice fit against StrangeTcy excerpts:**
- The style reference favors: short declarative openers that set a scene, visible self-correction, questions that move the argument, airy paragraphs, first-person.
- B is closer to the reference register ("I believed that for about one paragraph of the first draft" is pure style-reference voice; cf. "The first formalisation was wrong").
- A is more measured but slightly closer to benchmark-report register in its middle sections.
- The final piece should allow at least one visible self-correction moment and at least one question that genuinely moves the argument, not a rhetorical one.

**Links/Markdown:**
- Cite HELM and VarBench inline where they're mentioned (B does this correctly). Links go where they matter, not in a bibliography block.
- Tables use standard Markdown pipes; both drafts' table syntax is fine.
- Do not include editorial markers, evidence IDs, finding IDs, SHA hashes, or claim IDs in public prose.
- Do not include an "Editor's note" footer referencing internal CSVs (source draft does this; strip it).

**Layout mismatches to avoid:**
- No `## Introduction` heading. Open in prose.
- Keep headings short, argumentative turns (`## The regex contrast is real and confounded` works; `## Background` does not).
- Target 1,800–2,800 words. A ≈ 1,500 (short); B ≈ 2,400 (within range). Final should land ~2,000–2,400.

## A/B elements worth retaining

**From A:**
- The disciplined "What the evidence licenses" closing register — a bulletless, prose statement of what is and is not supported. Use this *as* the closing section's spine, but keep B's enumerated "licenses / does not license" lists for scannability.
- The crisp "I keep the layers distinct on purpose" principle statement about not collapsing failure types.
- The one-sentence framing that comparator findings are not paid-run identity.

**From B:**
- The question-led opener style (not the exact words).
- Both tables (regex 5-cell; failure stratification by layer) — these are the piece's most informative artifacts.
- The explicit per-environment pass table.
- The honest refusal to invent a mechanism for 34 and 66.
- The one-paragraph aside on the broader 192/61 taxonomy for scale, with the "overfit_visible_tests" mislabel noted briefly.
- The "experiment I'd want" numbered list — cleaner than A's prose version.
- The Rule 110 / Turing-completeness disclaimer paragraph.

## Elements neither draft handles well

- **Why the depth axes aren't commensurable as units of work.** Both state it; neither gives the reader a one-line intuition. A single sentence like "a 512-character string is not twice the computational demand of a 25-node chain" would land it.
- **The judge's four criteria for regex** are mentioned (15 seeded strings + length) but the full count of four criteria is underused; stating "the judge checks four things, and three passes mean those four held on seed 0" would sharpen the "local" claim.
- **The CSS surface sweep at 3 bits (fail/pass/pass) runs opposite to the regex surface sweep.** B notes this; A doesn't. Final piece should give it one sentence as a check against overgeneralization *from the regex contrast itself*.
- **The adjacent category-track axis-placeholder audit** is mentioned by both but the connection to the regex finding (same class of problem: labels promise manipulations that artifacts may not deliver) is explicit only in B. Keep B's framing.
- **Explicit statement that no compile-only cases exist in this track** — A has it, B does not. Include it; it defuses a plausible reader objection.

## Exact evidence boundaries

**In-bounds:**
- All numbers in the allowed-numbers list, used in their exact packet context.
- The dirty-repository flag.
- 33/33 config-hash match with the clean comparator (as comparator-level evidence, not run-identity proof).
- The regex judge criteria (four, including 15 seeded strings and length preservation).
- Failure modes exactly as labeled: underfit, source_invalid.
- HELM: 42 scenarios. VarBench: dynamic variable perturbation, five seeds for variable-based experiments.
- Broader campaign: 61 fails of 192 eligible; the two mislabeled overfit_visible_tests cases.

**Out-of-bounds:**
- Any seed count > 1.
- Any causal attribution for the two regex failures.
- Any claim about paid-run source identity beyond "comparator shows X."
- Any Turing-completeness / arbitrary-iteration claim.
- Any novelty claim against prior work.
- Any mechanism for +2 or +34 output-length discrepancies.
- Any inference about model capability from the aggregate 25/30.

## Final quality checklist

- [ ] Frontmatter: title, `date: 2026-10-03`, `layout: post`. No mathjax include.
- [ ] Exact byline present; epistemic-status `<dl>` with five fields in order.
- [ ] Opens in prose (no `## Introduction`); limit stated within first two paragraphs.
- [ ] Regex 5-cell table present with exact scores 1.0, 0.208333 and the length-mismatch notes.
- [ ] Failure-layer stratification table present; behavioral vs. source-invalid distinction visible before any pooling.
- [ ] Per-environment pass table present.
- [ ] Comparator / dirty-repository caveat placed at the moment the name+hint bundle is first named.
- [ ] One-seed caveat placed beside the regex contrast and beside any non-monotone pattern.
- [ ] Behavioral-reference judge-mode noted when the 25/30 is first stated.
- [ ] No-exclusions / no-provider-terminal note included once for this track.
- [ ] Rule 110 single-update vs. Turing-completeness disclaimer present.
- [ ] Speculative hypothesis (name-or-hint > length) explicitly marked speculative.
- [ ] HELM (42 scenarios) and VarBench (five seeds) cited as context only, with inline links; no novelty claim.
- [ ] Category-track axis-placeholder audit (10 axes / 9 environments) mentioned briefly as adjacent, with dirty-repo caveat.
- [ ] Visible self-correction moment present at least once.
- [ ] "What the evidence licenses / does not license" closing with explicit lists.
- [ ] Word count 1,800–2,800.
- [ ] No "fuckingly," no evidence IDs, no SHA hashes, no claim IDs, no "Editor's note" with internal file references.
- [ ] No equation, no `{% include mathjax.html %}`.
- [ ] All numerics drawn from the allowed vocabulary and used in packet context.
- [ ] No invented authors, no invented reviewers, no author-process claims copied from style-reference posts.
