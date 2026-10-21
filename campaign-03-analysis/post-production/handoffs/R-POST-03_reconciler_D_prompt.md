# R-POST-03 — STAGE D: RECONCILER

**Stage D of 4.** You produce the publishable article. You are neither writer: you inherit one draft as the spine, the other as a donor, and a review that tells you what is broken.

ARTICLE SLOT: R-POST-03 — a zero-pass-rate environment family is not a capability verdict.

---

## Inputs

1. `R-POST-03_packet.md` — authoritative evidence base.
2. `drafts/R-POST-03_A.md` — Writer A.
3. `drafts/R-POST-03_B.md` — Writer B.
4. `drafts/R-POST-03_C_review.md` — the adjudicator's report, including its `COMPARATIVE RECOMMENDATION`.

Read the review's **VERDICT** lines first. If it recommends **re-dispatch** for both drafts, stop: do not reconcile, do not salvage. Say what the next brief must change and end.

---

## What you are doing

Reconciliation is not averaging and not merging. It is: adopt the spine the reviewer named, repair everything it flagged, transplant only passages it graded clean, and keep the concessions that cost the article something. Two drafts that disagree factually are not both wrong — the packet decides.

## Rules, in priority order

1. **The packet decides.** Any number, attribution, or layer-split fact comes from the packet, not from either draft. If both drafts are wrong, the review will have marked it `SHARED`; fix it once.
2. **Every BLOCKER and CORRECTION from the review must be repaired.** Where you disagree with a finding, you do not get to ignore it — you either repair it or state, in the change log, the packet sentence that refutes the finding. Silent non-compliance is the one failure mode that voids this stage.
3. **No new claims and no new numbers.** You may delete, compress, reorder, and rephrase. You may not add a fact that is absent from the packet, including a "safe" summary statistic, an inferred percentage, or a reconstructed total.
4. **Spine, not collage.** One voice, one argument line. Do not alternate between the two writers' sensibilities; do not keep two openings, two conclusions, or two epistemic-status blocks.
5. **Keep the minimum viable concession set.** At least: the single-seed / one-provider / text-only limits; the fact that the archive records the layer and not the cause; and the record conflict on the 0.95 row. These are not decoration and may not be compressed into one throwaway sentence.
6. **Denominators travel with counts.** Every stated count carries its total in the same sentence, or sits in a table whose caption carries it.
7. **Nothing from `assets/`.** The one `<figure>` is an HTML table with a `<figcaption>` naming counts and total.
8. **No leakage.** No run folders, snapshots, case IDs, finding IDs, series labels, writer labels, drafting-model names, or TODOs.

## Publishable requirements

- Frontmatter: `title`, `date: 2026-10-21`, `layout: post` — nothing else.
- Byline `_by StrangeTcy_`.
- Five epistemic-status bullets: Original ideas, Synthesis, Prose, Certainty, Importance. "Prose" must now say what actually happened: two independent drafts, an adjudication, and a reconciliation — and that no new campaign was run. Honest self-scores only.
- One captioned `<figure>`; body tables as needed; each table gets a one-line note on what its columns are not.
- 1,800–2,800 words.
- A title you would defend in public. It may come from either draft or be new. No colon-stacked subtitles, no numerals-only titles, no "On the…".
- One-sentence opening a reader can disagree with.

## Self-check before you output

Run this list and paste the result into your change log, with the actual value found, not a tick:

1. Count of zero-pass families stated = **6**.
2. Their cases = **35**; failures = **35 of 63**; share of cases = **35 of 194**.
3. Layer split present and summing to **35**: 18 + 4 + 1 + 2 + 9 + 1.
4. The words **25** (stopped before behavioural scoring) and **10** (judged) both appear correctly.
5. `glyph` described with **8** cases, **0.0000**, **behavioural-reference**.
6. `gnn_message_passing` described with **5** cases at **0.4167** and the word "identical" or equivalent.
7. `ts_one_step` **0.7143** present as the highest judged score in a zero family.
8. The 0.95 row appears with `trusted_score` **1.0** and the missing file, and the disagreement is stated rather than resolved.
9. No occurrence of: `paused`, `provider_error`, `193`, `131/194` without bucket split, `0.726`, `0.650`, `five families`, `near-zero`, "unsolvable", "cannot", "gave up".
10. Bucket split if mentioned: **72** (56/16) and **122** (75/47).
11. Word count in range; frontmatter exact; byline present; five fields present; one figure with a caption containing counts.
12. Grep clean for: `fuck`, `shit`, `🫣`, `runs/atria_campaign`, `seed-0`, `R-POST`, `Reasoning-Atria`, `Writer A`, `Writer B`, `TODO`, `some model:`.

If any check fails, fix it before producing output. Do not output a draft that fails its own checklist.

## OUTPUT — exactly this shape

```
<the complete article markdown, starting with --- frontmatter ---, ending with the last sentence of the article>

---
<!-- NOT FOR PUBLICATION — reconciliation log -->
SPINE: draft A | draft B | re-synthesised (justify in one line)
INHERITED FROM SPINE: ...
TRANSPLANTED (quoted in C, clean on re-check): ...
BLOCKERS REPAIRED: one line each, with the packet §
CORRECTIONS REPAIRED: one line each
FINDINGS REJECTED (with the packet sentence that refutes them): ...
SELF-CHECK RESULT: 12 lines, actual values
OPEN ISSUES FOR A HUMAN: anything the packet cannot settle and the article now flags as open
SUGGESTED PUBLICATION PATH: _posts/2026-10-21-<slug>.md
```

Nothing else. No cover note, no summary of the review.
