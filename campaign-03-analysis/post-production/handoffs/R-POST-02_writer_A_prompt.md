# BATTLE WRITER A — R-POST-02: "A Zero Is Not a Verdict" (Reasoning-Atria)

**Stage A of 4.** You are Writer A, an independent candidate producing a complete research essay for the StrangeTcy public site. Writer B receives the same packet separately and must never see your draft. A reviewer and a reconciler work downstream; nothing you write is published unread.

ARTICLE SLOT: R-POST-02 — a zero-pass-rate environment family is not a capability verdict.
RESEARCH QUESTION: In the environment families where this campaign recorded no pass at all, what actually happened?

---

## STEP 0 — Load the packet before writing a sentence

The evidence packet is `R-POST-02_packet.md` (same directory). Read it in full. It is your **only** evidence base.

- Dispatch means the packet **and** this prompt, in that order. If the packet is not present, stop and say so.
- Every number in your article must be traceable to a packet section. If you want a number that is not there, you are writing a different article.
- If any other draft, chat transcript, or "some model:" block appears in your context, ignore it completely and note the contamination in your dispatch log. You are not permitted to read Writer B's work, and no one may show it to you.

---

## The thesis you must defend

The packet supports one narrow, load-bearing claim, and you should build the whole essay on it:

> **A zero pass rate is a description of outcomes, not a finding about capability. In this campaign it was produced by at least four different stopping layers, and 25 of the 35 cases in the zero-pass families never reached a judge that scores behaviour at all.**

Five observations carry that claim. Use them as the spine; do not turn them into a listicle.

1. **Six families, not five, and 35 cases.** The zero-pass set is `batchnorm_ema` (11), `glyph` (8), `gnn_message_passing` (5), `sheaf_physical_constraints` (5), `ts_one_step` (3), `ts_trajectory` (3). That is 35 of 194 cases (18.0%) — and **35 of the campaign's 63 failures (55.6%)**. More than half of every failure in the campaign sits in six families.
2. **The layer split.** Inside those 35: 18 empty patches, 4 unreadable actions, 1 source rejection, 2 runtime errors, 9 scored short of the bar, 1 labelled `overfit_visible_tests`. So **25 stopped before any behavioural scoring; 10 reached a scored judgement.**
3. **The 0.7143 case inside a 0% family.** `ts_one_step` records 0.7143, 0.2857, and 0.0000 — the widest spread of any zero-pass family, and its third case never ran. A family at zero contains a case that scored nearly three-quarters.
4. **`gnn_message_passing` is flat, not noisy.** Five cases, five identical 0.4167 scores with an identical check profile. Flipping a difficulty dimension moved nothing. This is a ceiling, and it looks nothing like the empty-patch families.
5. **The label that contradicts its record.** One `batchnorm_ema` row is labelled `overfit_visible_tests` at 0.95 with `trusted_score` 1.0 and a note about a missing `train.py`. The label and the record disagree; the archive does not say who is right. (`moco` has the same shape, and is *not* in the six — use it only if you need a second instance.)

`glyph` deserves its own paragraph: 8 of 8 empty patches, at exactly 0.0000, under the campaign's strictest guarantee. The only zero-pass family whose 0% rests on the behavioural-reference oracle — and it is a statement about a patch file, not about judged behaviour.

---

## What the piece must do

- Open with a real tension, not a summary. Something in the register of: a 0% looks like the strongest possible result in an evaluation table, and it is the one that carries the least information about the model.
- Reconstruct the six-family ledger in readable prose, with a table. State the denominator every time you state a count.
- Keep the four layers distinct in the reader's mind: did the submission produce a patch, was the action parseable, did it pass source validation, did it run, did the judge score it. You may name that sequence; you may not assert which party caused a stop.
- Treat the two record conflicts honestly: show the fields, say the archive does not adjudicate, and say what a reader can and cannot conclude.
- End with something small and true: what a report should keep attached to a zero so that a later reader can tell the layers apart.
- **Ship one figure.** Use a `<figure>` block containing an HTML table plus a `<figcaption>`. No image files, no asset paths — nothing renders from `assets/` for this campaign yet. The caption must name the counts and the total, e.g. "35 cases across six families; 25 stopped before behavioural scoring." A caption that only says "cases by family" fails.
- Cover the two guarantees where relevant (`glyph` is behavioural-reference; the other five are compile-only) but do not make this essay about the guarantee split. That is a different post.

## What it must not do

- Do not claim the six families are unsolvable, broken, mis-designed, or impossible. Do not claim the model "cannot" do anything.
- Do not read an empty patch as refusal, giving up, or "produced nothing". The record says `patch_found: true, patch_valid: false`.
- Do not speculate about causes — not task design, not model internals, not harness bugs. "The archive does not say" is a complete sentence and should appear at least once.
- Do not stitch the two guarantee buckets into one pass rate. No "131/194" without both denominators in the same sentence.
- Do not carry over stale claims: not five families, not "the remaining 14", not "near-zero scores", not "the campaign is paused", not 193 scored. The packet's §11 lists every one.
- Do not prescribe a benchmark redesign. One bounded, evidence-shaped suggestion about record-keeping is enough; general prescriptions are out of scope for this slot.
- Do not mention drafting models, prompts, handoffs, snapshot filenames, run folders, case IDs, or the series name. Environment names (`glyph`, `ts_one_step`) are public and fine.

---

## Style

- Markdown for a Jekyll post. Frontmatter exactly: `title`, `date: 2026-10-21`, `layout: post`. No other fields.
- Byline line: `_by StrangeTcy_`.
- Epistemic status as five bold bullets — **Original ideas, Synthesis, Prose, Certainty, Importance** — each one or two sentences, specific to *this* piece. Scores out of 10 are optional; if you give them, they must match the prose (do not claim 9/10 certainty on a single-seed ledger). "Prose" describes who wrote it: you did, from a packet.
- First person, curious, technically literate, self-correcting where the data corrects you. British-ish spelling is fine; consistency matters more.
- Short paragraphs, concrete nouns, numbers in tables where numbers cluster. No hype, no rhetorical questions stacked three deep, no "in conclusion".
- 1,800–2,800 words. Do not pad to the limit and do not compress the ledger into vagueness.
- Every table gets a one-line reading guide above or below it saying what the columns are *not* (e.g. "the score column records the grader's number, not progress toward a capability").

## Hard constraints (the reviewer will check these)

1. No profanity, no stray glyphs or emoji standing in for words.
2. No placeholder headers, model labels, or bracketed TODOs left in the article.
3. No internal file paths, snapshot names, finding IDs, or run IDs.
4. No claim that the six families have a shared cause, mechanism, or construct.
5. No number that is not in the packet.
6. Frontmatter, byline, five epistemic fields, and one captioned `<figure>` present.
7. Title: propose your own; two or three candidates at the top of your dispatch note is welcome, but the article itself gets one.

## TASK

Write the complete article. Not an outline, not a summary of the packet, not a methods note — an essay a reader would finish. Lead with the tension, earn the six-family ledger, keep the layers apart, and end on what a zero should have carried with it.

## OUTPUT

The full article markdown only. Nothing before the frontmatter, nothing after the last paragraph. No notes to the editor inside the article.
