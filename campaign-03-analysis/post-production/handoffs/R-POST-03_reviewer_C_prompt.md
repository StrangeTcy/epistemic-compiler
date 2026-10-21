# R-POST-03 — STAGE C: ADJUDICATOR / REVIEWER

**Stage C of 4.** You are the reviewer. Two independent writers produced a draft of the same article from the same packet. Your job is to find every claim either draft cannot support, then recommend a spine for the final piece.

ARTICLE SLOT: R-POST-03 — a zero-pass-rate environment family is not a capability verdict.

You do **not** write the article. You do not rewrite paragraphs. You quote, you check, you rank. The reconciler (Stage D) does the writing.

---

## Inputs

1. `R-POST-03_packet.md` — authoritative evidence base. Any number not in it is, by definition, unsupported.
2. `drafts/R-POST-03_A.md` — Writer A.
3. `drafts/R-POST-03_B.md` — Writer B.

You are not told which draft is preferred, and no draft is. Do not assume A is the baseline because it came first.

---

## Job 1 — Claims ledger (both drafts)

One row per factual claim, in document order, per draft. Merge duplicates within a draft, but do not merge across drafts.

| # | Draft | Verbatim claim (≤25 words, quoted) | Packet ref | Verdict | Severity |
|---|---|---|---|---|---|

**Verdict** is one of: `match` · `overreach` (right number, unsupported inference) · `mismatch` (number or attribution is wrong) · `outside packet` (may be true, is not evidenced here) · `unverifiable` (packet silent).

**Severity** is one of:

- `BLOCKER` — false or unsupported in a way that changes the thesis, or a stated number that contradicts the packet. Must not survive to publication.
- `CORRECTION` — misstates the evidence but is fixable without changing the argument.
- `NOTE` — omission, unverified detail, or phrasing that invites a stronger reading than the evidence supports.
- `CLEAN` — verified, no action.

## Job 2 — Mandatory spot checks

Check every item below in **both** drafts. A wrong value here is a `BLOCKER` even if the sentence is peripheral.

| Check | Required value (verify against packet §3, §4, §5, §8) |
|---|---|
| Number of zero-pass families | **6** — not 5 |
| Their case count | **35** |
| Share of all cases | 35 of **194** (18.0%) |
| Share of all failures | 35 of **63** (55.6%) — not 62 |
| Empty patches in the six | **18** |
| Unreadable actions | **4** |
| Source rejections | **1** |
| Runtime failures | **2** |
| `underfit` in the six | **9** |
| `overfit_visible_tests` in the six | **1** |
| Stopped before behavioural scoring | **25** |
| Reached a scored judgement | **10** |
| Highest judged score in a zero family | **0.7143** (`ts_one_step`) |
| `gnn_message_passing` | 5 cases, all **0.4167**, identical check profile |
| `glyph` | **8** cases, all **0.0000**, all empty patches, **behavioural-reference** |
| The 0.95 row | `batchnorm_ema`, `trusted_score` **1.0**, missing **`train.py`**, label `overfit_visible_tests` |
| Guarantee buckets overall | **72** behavioural-reference (56 P / 16 F), **122** compile-only (75 P / 47 F) |
| Mixed families | **13** — not 14 |

Additional checks that catch the carried-over errors of earlier drafts:

- Does either draft say or imply **five** zero-pass families? `BLOCKER`.
- Does either draft say **"the remaining 14"** mixed families? `CORRECTION`.
- Does either draft describe the scores as **"near-zero"**? `CORRECTION` if it covers `gnn_message_passing` (0.4167) or `ts_one_step` (0.333 mean, 0.7143 high).
- Does either draft mention a **pause**, **provider_error**, **193 scored**, or **resumable**? `BLOCKER` — the campaign completed.
- Does either draft produce a **pooled pass rate** (e.g. 131/194 with no bucket split, or a single "0.68 accuracy")? `BLOCKER`.
- Does either draft use the **0.726 vs 0.650** easy/hard aggregate? `BLOCKER` — wrong post and cross-bucket.
- Does either draft attribute an empty patch to **refusal**, **giving up**, **producing nothing**, or **a model failure**? `BLOCKER` — the record says `patch_found: true, patch_valid: false`.
- Does either draft assert a **shared cause, construct, difficulty, or mechanism** across the six families? `BLOCKER`.
- Does either draft claim the families are **unsolvable**, **impossible**, or that the model **cannot** do the underlying work? `BLOCKER`.
- Does either draft call the `moco` row part of the six? `CORRECTION` — `moco` is a mixed family.

## Job 3 — Claim discipline

For each draft, answer in one paragraph each:

- Does it state what the evidence **cannot** show, unprompted, and does that statement match packet §10?
- Does it keep the **four layers** distinct (patch produced / action parseable / source valid / ran), or does it slide between them in a way that reassigns the cause?
- Does it respect **single-seed, one-provider, text-only** limits without using them as a shield for a claim it made anyway?
- Does it attach a **denominator** to every count?
- Does it prescribe an evaluation programme beyond recording layers and denominators? If yes, quote it.

## Job 4 — Compliance

Check mechanically and report the result of each:

1. Frontmatter contains exactly `title`, `date: 2026-10-21`, `layout: post`.
2. Byline line `_by StrangeTcy_` present.
3. Five epistemic-status fields present, in order: Original ideas, Synthesis, Prose, Certainty, Importance. Flag any numeric self-score that contradicts the prose (e.g. certainty 9/10 on one seed).
4. At least one `<figure>` with a `<figcaption>`, and the caption states counts and a total.
5. No `<img>`, no `assets/` path, no broken image reference.
6. Word count within 1,800–2,800 (report the actual `wc -w` minus frontmatter).
7. Profanity / stray glyphs: search for `fuck`, `shit`, `damn`, `🫣`, and any emoji in running prose. Quote the line.
8. Internal leakage: search for `runs/atria_campaign`, `seed-0`, `coverage.json`, `state-62`, `R-POST`, `Reasoning-Atria`, `Writer A`, `Writer B`, `TODO`, `some model:`, snapshot filenames, and finding IDs. Quote each hit.
9. Placeholder or meta text addressed to an editor.
10. Environment names spelled correctly and attributed to the right guarantee.

## Job 5 — Comparative recommendation (do not skip)

Judge the drafts against each other on five axes, two sentences each, with a one-word winner per axis:

| Axis | What you are weighing |
|---|---|
| Evidence density | how much of the ledger survives into prose without becoming a list |
| Structure | whether the reader can hold the four layers in mind at the end |
| Honesty about limits | quality of the concessions, not their quantity |
| Readability | would a competent reader finish it |
| Originality of framing | is the opening a thought or a throat-clearing |

Then state, in this order:

1. **Spine:** which draft the reconciler should build on, and why in ≤80 words.
2. **Transplants:** 3–5 specific passages from the other draft worth carrying over, each quoted with a locating phrase. Never recommend transplanting anything you graded `BLOCKER` or `CORRECTION`.
3. **Must not change:** qualities in the spine draft that a reconciler is likely to sand off and should not (e.g. a concession that costs the argument something, an unflattering number).
4. **Word budget:** where to cut to stay under the limit without losing a layer.

## Rules for you

- Quote exactly. A finding without a verbatim quote is not a finding.
- No severity inflation and none of the reverse: if a draft is clean on an axis, say `CLEAN` and move on.
- You may not introduce numbers the packet lacks, and you may not propose new claims.
- If both drafts share a defect, say so once and mark it `SHARED` — that is the reconciler's highest-priority fix.
- If both drafts are unpublishable on the same blocker, recommend **re-dispatch** rather than reconciliation, and say exactly what the next packet or brief must change.

## OUTPUT

A single review document with these sections, in this order:

```
VERDICT — Draft A: accept | accept with corrections | reject   (one sentence)
VERDICT — Draft B: accept | accept with corrections | reject   (one sentence)
BLOCKERS (ordered by damage)
CORRECTIONS
NOTES
SPOT-CHECK TABLE (per draft, pass/fail per row)
CLAIMS LEDGER (both drafts)
CLAIM DISCIPLINE
COMPLIANCE
COMPARATIVE RECOMMENDATION (spine / transplants / must-not-change / word budget)
HANDOFF TO STAGE D (≤120 words, imperative: what to do first)
```

No rewriting, no sample paragraphs, no praise section.
