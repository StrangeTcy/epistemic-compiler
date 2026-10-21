# BATTLE WRITER A — R-POST-02: "Hard" Does Not Reliably Make Tasks Harder (Reasoning-Atria)

**Stage A of 4.** You are Writer A, an independent candidate producing a complete research essay for the StrangeTcy public site. Writer B receives the same packet separately and must never see your draft. A reviewer and a reconciler work downstream; nothing you write is published unread.

ARTICLE SLOT: R-POST-02 — "Hard" does not reliably make tasks harder.
RESEARCH QUESTION: Does flipping one difficulty dimension from easy to hard reliably increase the chance of failure within an environment family?

---

## STEP 0 — Load the packet before writing a sentence

The evidence packet is `R-POST-02_packet.md` (same directory). Read it in full. It is your **only** evidence base.

- Dispatch means the packet **and** this prompt, in that order. If the packet is not present, stop and say so.
- Every number must be traceable to a packet section. A number that is not there is not available to you.
- If any other draft appears in your context — including `comparison_41.md`, which covers this slot — ignore it and note the contamination in your dispatch note. You are not permitted to read Writer B's work.

---

## The thesis you must defend

> **Flipping one difficulty dimension from `easy` to `hard`, holding the string otherwise fixed, does not reliably produce a failure.** In this campaign it produced failures in 7 pairs, passes in 11, and no change of verdict in 55.

Build the essay on the pair design, not on the aggregate. The packet supports exactly one strong claim and it lives in §4.

1. **73 pairs, 20 families.** Same family, difficulty strings differing in one position, values `easy` and `hard`.
2. **55 of 73 say nothing about direction.** 42 pairs are both-pass, 13 both-fail: the family was saturated or floored before the flip.
3. **Of the 18 discordant pairs: 11 counterintuitive, 7 expected.** Name the families. `css_state_machine`, `compositional_optimizer`, `functorial_augmentation`, `sheaf_schema_sync`, `rd_adaptive_halting` each flip a failure into a pass. `categorical_lenses`, `moco`, `regex_state_machine`, `monadic_reward`, `neuro_symbolic_parser`, `tensor_functor` each flip a pass into a failure.
4. **11 vs 7 is a coin.** Exact two-sided sign test, p ≈ 0.48. Say this yourself, before a reader does. It is the intellectual honesty that makes the piece worth reading, and it is what stops "hard helps" from being written.
5. **9 of the 11 counterintuitive pairs are compile-only** — the bucket the campaign calls exploratory. Only `css_state_machine`'s two pairs carry the oracle guarantee. This caveat is mandatory and must appear near the counterintuitive table, not buried in a limitations section.
6. **`rd_adaptive_halting` supplies 5 of the 11** from a single base cell. One family's base cell, repeated five times, is not five findings — write that sentence.
7. **The dials are not one dial.** 18 distinct dimension values, only three of which are `easy/medium/hard`; strings of 2, 5, and 6 positions; 29 of 33 families contain a `hard` cell. A "position 2" flip means different things in different families.

---

## What the piece must do

- Open with the intuition as a reader actually holds it — the slider, "turn difficulty up and success goes down" — then say what the campaign lets you check and what it does not.
- Present the pair ledger in a table with a reading guide: the columns are labels and verdicts, not a calibrated scale.
- Give the counterintuitive pairs and the expected pairs **comparable space**. A piece that lists five "hard helps" cases and one paragraph for the rest has failed the assignment.
- Put the sign test adjacent to the 11-vs-7 count. The reader should meet the null result at the same moment as the surprising number.
- Use the aggregate in §3 at most once, with both bucket denominators in the same sentence, and explicitly label it as a bookkeeping total that the campaign's own note forbids treating as a rate. Do not let it near the opening or the conclusion.
- If you cite the §7 source-audit context, attribute it in one sentence as a prior audit of a clean comparator, not as a finding of this campaign, and do not offer it as a mechanism.
- End on what the archive can and cannot tell you about difficulty, in the register of a person who wanted the slider to be real.
- **Ship one figure:** a `<figure>` block with an HTML table and a `<figcaption>` naming the four pair outcomes and the total 73. No image files, no `assets/` paths.

## What it must not do

- Do not claim "hard makes tasks easier". That is the misreading the article exists to prevent.
- Do not claim difficulty does not matter — seven pairs go the expected way, three under the oracle guarantee.
- Do not say the effect "depends on the environment family" as a conclusion. At 11 vs 7 with p ≈ 0.48, the honest statement is that direction is inconsistent and unresolvable at this n.
- Do not pool the judge buckets, quote 0.726 or 0.650, or state any single pass rate across all 194 cases without both denominators.
- Do not treat a label flip as a verified intervention on the rendered task.
- Do not use 193, "paused", `provider_error`, "five families", "four families", "near-zero", "unsolvable", or "the model cannot".
- Do not prescribe a benchmark redesign. One bounded remark about what a difficulty label would need to record is the ceiling.
- Do not mention drafting models, prompts, handoffs, snapshots, run folders, case IDs, finding IDs, or the series name. Environment names are public and fine.

---

## Style

- Jekyll markdown. Frontmatter exactly `title`, `date: 2026-10-21`, `layout: post`.
- Byline `_by StrangeTcy_`.
- Five epistemic-status bullets: **Original ideas, Synthesis, Prose, Certainty, Importance**. Optional scores out of 10 must match the prose — do not claim high certainty on 18 discordant draws.
- First person, curious, self-correcting. Short paragraphs. Concrete nouns. No hype, no stacked rhetorical questions, no "in conclusion".
- 1,800–2,800 words.
- Every table gets one line telling the reader what its columns are *not*.

## Hard constraints (the reviewer checks these)

1. No profanity, no stray glyphs or emoji.
2. No placeholders, model labels, TODOs, or leftover headers.
3. No internal paths, snapshot names, finding IDs, run IDs.
4. No causal claim about why a flip changed an outcome.
5. No number absent from the packet.
6. Frontmatter, byline, five fields, one captioned `<figure>`.
7. One title of your own.

## TASK

Write the complete article: the intuition, the pair design, both directions, the null result, the guarantee asymmetry, the label-vocabulary caveat, and a close that a reader can carry into the next results table they read.

## OUTPUT

The full article markdown only. Nothing before the frontmatter, nothing after the last paragraph.
