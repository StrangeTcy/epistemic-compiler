# R-POST-02 — STAGE D: RECONCILER

**Stage D of 4.** You produce the publishable article. You are neither writer: you inherit one draft as the spine, the other as a donor, and a review that says what is broken.

ARTICLE SLOT: R-POST-02 — "Hard" does not reliably make tasks harder.

---

## Inputs

1. `R-POST-02_packet.md` — authoritative evidence base.
2. `drafts/R-POST-02_A.md`
3. `drafts/R-POST-02_B.md`
4. `drafts/R-POST-02_C_review.md` — including its `COMPARATIVE RECOMMENDATION`.

Read the review's **VERDICT** lines first. If it recommends **re-dispatch** for both drafts, stop: do not reconcile, do not salvage. State what the next brief must change and end.

---

## What you are doing

Reconciliation is not averaging and not merging. Adopt the spine the reviewer named, repair everything it flagged, transplant only passages it graded clean, and keep the concessions that cost the article something. Two drafts that disagree factually are not both right — the packet decides.

## Rules, in priority order

1. **The packet decides.** Every number, attribution, and pair outcome comes from `R-POST-02_packet.md`, not from either draft.
2. **Repair every `BLOCKER` and `CORRECTION`.** Where you disagree with a finding, you may not ignore it: either repair it, or state in the change log the packet sentence that refutes it. Silent non-compliance voids this stage.
3. **No new claims, no new numbers.** Delete, compress, reorder, rephrase. Do not add a statistic, an inferred percentage, a reconstructed count, or a "roughly".
4. **Spine, not collage.** One voice, one argument line, one opening, one conclusion, one epistemic-status block.
5. **Keep the minimum concession set.** These may not be compressed into a throwaway sentence and may not move to the end as a formality:
   - 55 of 73 pairs are saturated or floored and carry no directional information;
   - 11 vs 7 with p ≈ 0.48 is not a trend;
   - 9 of the 11 counterintuitive pairs are compile-only;
   - `rd_adaptive_halting` contributes 5 of 11 from one base cell;
   - the flip holds the label string constant, not the rendered task;
   - one seed per cell, one provider, text-only.
6. **Denominators travel with counts; buckets travel with rates.** No pooled pass rate anywhere, including in a summary sentence.
7. **Nothing from `assets/`.** The one `<figure>` is an HTML table with a `<figcaption>` naming the four outcomes and the total 73.
8. **No leakage.** No run folders, snapshots, case IDs, finding IDs, series labels, writer labels, drafting-model names, or TODOs.

## Publishable requirements

- Frontmatter: `title`, `date: 2026-10-21`, `layout: post` — nothing else.
- Byline `_by StrangeTcy_`.
- Five epistemic bullets: Original ideas, Synthesis, Prose, Certainty, Importance. "Prose" states what happened: two independent drafts from one packet, an adjudication, and a reconciliation, with no new campaign run. Honest self-scores only.
- One captioned `<figure>`; body tables as needed; each table carries one line on what its columns are not.
- 1,800–2,800 words.
- A title you would defend publicly. It may come from either draft or be new. The slot is not entitled "inconsistency in difficulty labels". No colon-stacked subtitle, no numerals-only title.
- The opening sentence must be a claim a reader can disagree with.

## Self-check before output

Paste actual values, not ticks:

1. Pairs stated = **73**; both-pass **42**; both-fail **13**; expected **7**; counterintuitive **11**.
2. `73 = 42 + 13 + 7 + 11` verified as arithmetic in the article.
3. Sign test stated as two-sided exact, **p ≈ 0.48**, adjacent to the 11-vs-7 count.
4. Guarantee split of the counterintuitive pairs = **9 compile-only / 2 behavioral**; of the expected = **4 / 3**.
5. `rd_adaptive_halting` described as **5 of 11** from **one base cell**, not five findings.
6. `css_state_machine` identified as carrying the only two counterintuitive pairs under the oracle guarantee.
7. `regex_state_machine` losing at **0.208**.
8. `sheaf_physical_constraints` **0.000 → 0.278** present as the single verdict-identical score move.
9. **18** distinct dimension values; **29 of 33** families contain a `hard` cell.
10. No occurrence of: `0.726`, `0.650`, `0.645`, `131/194`, `193`, `paused`, `provider_error`, `resumable`, "five families", "four families", "near-zero", "unsolvable", "cannot", "hard makes tasks easier", "depends on the environment family".
11. Buckets if mentioned: **72** (56/16, 0.778) and **122** (75/47, 0.615).
12. Word count in range; frontmatter exact; byline present; five fields present; one figure whose caption carries counts and the total.
13. Grep clean: `fuck`, `shit`, `🫣`, `runs/atria_campaign`, `seed-0`, `R-POST`, `Reasoning-Atria`, `Writer A`, `Writer B`, `TODO`, `some model:`.

Fix any failure before producing output. Do not emit a draft that fails its own checklist.

## OUTPUT — exactly this shape

```
<the complete article markdown, starting with --- frontmatter ---, ending with the last sentence>

---
<!-- NOT FOR PUBLICATION — reconciliation log -->
SPINE: draft A | draft B | re-synthesised (one-line justification)
INHERITED FROM SPINE: ...
TRANSPLANTED (clean in review, re-checked): ...
BLOCKERS REPAIRED: one line each, with packet §
CORRECTIONS REPAIRED: one line each
FINDINGS REJECTED (with the packet sentence that refutes them): ...
SELF-CHECK RESULT: 13 lines, actual values
OPEN ISSUES FOR A HUMAN: anything the packet cannot settle and the article now flags
SUGGESTED PUBLICATION PATH: _posts/2026-10-21-<slug>.md
```

Nothing else. No cover note, no summary of the review.
