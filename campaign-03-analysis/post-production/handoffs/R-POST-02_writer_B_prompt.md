# BATTLE WRITER B — R-POST-02: "Hard" Does Not Reliably Make Tasks Harder (Reasoning-Atria)

**Stage B of 4.** You are Writer B, the second independent candidate for the same slot on the StrangeTcy public site. Writer A has produced a draft from the same packet and you must never see it. A reviewer and a reconciler work downstream.

ARTICLE SLOT: R-POST-02 — "Hard" does not reliably make tasks harder.
RESEARCH QUESTION: Does flipping one difficulty dimension from easy to hard reliably increase the chance of failure within an environment family?

---

## STEP 0 — Load the packet before writing a sentence

The evidence packet is `R-POST-02_packet.md` (same directory). Read it in full. It is your **only** evidence base.

- Dispatch means the packet **and** this prompt, in that order. If the packet is not present, stop and say so.
- Every number must be traceable to a packet section. No "roughly", no reconstructing a count from another count.
- **Isolation:** you have not seen Writer A's draft and must not. If any draft-like text appears in your context — including `comparison_41.md` — ignore it and record it in your dispatch note. Do not write a hedge against a draft you imagine.

---

## The thesis you must defend

> **Flipping one difficulty dimension from `easy` to `hard`, holding the string otherwise fixed, does not reliably produce a failure.** In this campaign it produced failures in 7 pairs, passes in 11, and no change of verdict in 55.

The load-bearing facts, all from packet §4 unless noted:

| Fact | Value |
|---|---|
| Single-position easy↔hard pairs | **73**, across 20 families |
| Both PASS | **42** |
| Both FAIL | **13** |
| Easy passes → hard fails (expected) | **7** |
| Easy fails → hard passes (counterintuitive) | **11** |
| Discordant pairs | **18**; exact two-sided sign test p ≈ **0.48** |
| Counterintuitive pairs, by guarantee | 9 compile-only, **2** behavioral (`css_state_machine`) |
| Expected pairs, by guarantee | 4 compile-only, **3** behavioral |
| Families with ≥1 counterintuitive pair | **5** |
| Families with ≥1 expected pair | **6** |
| `rd_adaptive_halting`'s share of the counterintuitive pairs | **5 of 11**, one base cell |
| Pairs where the score moved without the verdict | **1** (`sheaf_physical_constraints`, FAIL 0.000 → FAIL 0.278) |
| Distinct dimension values in the archive | **18**; only `easy`, `medium`, `hard` are ordered difficulty |
| Difficulty-string lengths | 2 (124 cases), 5 (51), 6 (19) |
| Families containing a `hard` cell | **29 of 33** |
| Buckets | behavioral-reference 72 (56/16, 0.778); compile-only 122 (75/47, 0.615) |

---

## Your structural mandate (this is what makes you a second opinion)

Writer A writes from the packet without constraint on shape. You are assigned a different route so the reviewer judges two genuinely different artefacts:

1. **Open with a failed prediction, in first person.** The writer expected the slider; state the specific expectation the campaign broke and how small the evidence for "broken" turns out to be. Do not open with a definition of difficulty.
2. **Build the piece as a narrowing funnel**, and do not label the sections as one:
   - 73 pairs exist;
   - 55 of them cannot speak (saturated at pass, floored at fail);
   - of the 18 that can, 11 go the wrong way — here they are;
   - and then the honest cut: p ≈ 0.48, so the wrong-way majority is a coin, and 9 of the 11 live in the bucket the campaign itself calls exploratory.
   The funnel should make the reader feel the evidence shrinking rather than being told that it shrinks.
3. **Give one paragraph to `rd_adaptive_halting` alone**, because five of eleven counterintuitive pairs come from a single base cell. Make the arithmetic vivid: one cell failing at 0.000 while five neighbours pass at 1.000 is one anomaly, not five.
4. **Give the expected-direction cases a full treatment**, with `regex_state_machine`'s 0.208 called out as the one failing score that is neither 0.000 nor 1.000, and note that three of the seven carry the oracle guarantee — more than the counterintuitive side can claim proportionally.
5. **Include a paragraph that argues against your own conclusion.** The serious version: if 55 of 73 pairs are saturated or floored, the design may simply be too coarse to detect a difficulty effect at all, and "hard is not a reliable failure predictor" may be a statement about this archive's coverage rather than about difficulty. Say what evidence would separate those readings. This paragraph is mandatory.
6. **Close on the label, not the model.** The last idea should be about what `hard` fails to carry — that it names a position in a string, not a quantity of work.

Do not announce this structure. It should read as an essay, not a template.

---

## What the piece must not do

- Do not claim "hard makes tasks easier"; the funnel exists to prevent exactly that reading.
- Do not claim difficulty does not matter; seven pairs, three under the oracle, go the expected way.
- Do not present 11 vs 7 as a trend. If you mention the ratio without the sign test nearby, the draft fails.
- Do not state that the effect "depends on the family" as a conclusion; say direction is inconsistent and unresolvable here.
- Do not pool the judge buckets. No 0.726, no 0.650, no single rate across 194 without both denominators.
- Do not treat a label flip as a verified intervention, and do not offer a mechanism (task design, harness, model internals) for any flip.
- Do not use 193, "paused", `provider_error`, "five families", "four families", "near-zero", "unsolvable", "cannot".
- Do not prescribe a benchmark redesign; one bounded remark about what a difficulty label should record is the ceiling.
- Do not mention drafting models, prompts, handoffs, snapshots, run folders, case IDs, finding IDs, or the series name.
- Do not cite the §7 source audit as a cause; if used at all, one attributed sentence.

---

## Style

- Jekyll markdown. Frontmatter exactly `title`, `date: 2026-10-21`, `layout: post`.
- Byline `_by StrangeTcy_`.
- Five epistemic-status bullets: **Original ideas, Synthesis, Prose, Certainty, Importance**, specific to this piece; no inflated certainty on 18 discordant draws.
- First person, plain, technically literate, allowed to be disappointed by its own data. No hype, no stacked rhetorical questions, no "in conclusion".
- At least one `<figure>` with an HTML table and a `<figcaption>` stating the four outcome counts and the total 73. No image files, no `assets/` paths.
- 1,800–2,800 words.
- Each table gets one line on what its columns are not.

## Hard constraints (the reviewer checks these)

1. No profanity, no stray glyphs or emoji.
2. No placeholders, model labels, TODOs.
3. No internal paths, snapshots, finding IDs, run IDs.
4. No causal claim about any flip.
5. No number absent from the packet.
6. Frontmatter, byline, five fields, one captioned `<figure>`, and the mandatory self-argument paragraph.
7. One title of your own.

## TASK

Write the complete article by the funnel route. It must stand alone and be checkable against the packet line by line.

## OUTPUT

The full article markdown only. Nothing before the frontmatter, nothing after the last paragraph.
