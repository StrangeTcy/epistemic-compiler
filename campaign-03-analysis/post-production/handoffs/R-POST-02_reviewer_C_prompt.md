# R-POST-02 — STAGE C: ADJUDICATOR / REVIEWER

**Stage C of 4.** Two independent writers produced a draft of the same article from the same packet. Find every claim either draft cannot support, then recommend a spine.

ARTICLE SLOT: R-POST-02 — "Hard" does not reliably make tasks harder.

You do **not** write the article and you do not rewrite paragraphs. You quote, check, and rank. Stage D writes.

---

## Inputs

1. `R-POST-02_packet.md` — authoritative. Any number not in it is, by definition, unsupported.
2. `drafts/R-POST-02_A.md`
3. `drafts/R-POST-02_B.md`

You are not told which draft is preferred, and no draft is. Do not assume A is the baseline because it came first.

---

## Job 1 — Claims ledger

One row per factual claim, in document order, per draft. Merge duplicates inside a draft; do not merge across drafts.

| # | Draft | Verbatim claim (≤25 words, quoted) | Packet ref | Verdict | Severity |
|---|---|---|---|---|---|

**Verdict:** `match` · `overreach` (right number, unsupported inference) · `mismatch` (number or attribution wrong) · `outside packet` · `unverifiable`.

**Severity:** `BLOCKER` (false, or unsupported in a way that changes the thesis, or a number contradicting the packet) · `CORRECTION` (misstates the evidence, fixable without changing the argument) · `NOTE` (omission or phrasing that invites a stronger reading) · `CLEAN`.

## Job 2 — Mandatory spot checks (both drafts)

A wrong value here is a `BLOCKER` even in a peripheral sentence.

| Check | Required value | Packet § |
|---|---|---|
| Single-position easy↔hard pairs | **73** | 4 |
| Both PASS | **42** | 4 |
| Both FAIL | **13** | 4 |
| Expected direction (easy passes → hard fails) | **7** | 4 |
| Counterintuitive (easy fails → hard passes) | **11** | 4 |
| Discordant pairs | **18** | 4 |
| Sign test | two-sided exact, p ≈ **0.48** | 4, App. A |
| Counterintuitive pairs by guarantee | **9 compile-only, 2 behavioral** | 4.1 |
| Expected pairs by guarantee | **4 compile-only, 3 behavioral** | 4.2 |
| Families with a counterintuitive pair | **5** | 4.2 |
| Families with an expected pair | **6** | 4.2 |
| `rd_adaptive_halting` share | **5 of 11**, one base cell | 4.1 |
| Score-shifted, verdict-identical pairs | **1** (`sheaf_physical_constraints`, 0.000 → 0.278) | 4.3 |
| `regex_state_machine` failing score | **0.208** | 4.2 |
| Distinct dimension values | **18** | 6 |
| Families containing a `hard` cell | **29 of 33** | 6 |
| Buckets | **72** (56/16, 0.778) and **122** (75/47, 0.615) | 2 |
| Pooled any-hard / no-hard | 73/53 (0.726) and 121/78 (0.645) — *context only, §3* | 3 |

## Job 3 — Slot-specific traps

Each of these is a `BLOCKER` unless marked otherwise.

- **Pooled rate.** Any pass rate spanning both guarantee buckets: 0.726, 0.650, 0.645, "131/194", "68% overall", or a single accuracy figure. The campaign's own aggregate note forbids it. `CORRECTION` only if the sentence names both denominators and labels itself a bookkeeping total.
- **"Hard makes tasks easier."** Any sentence asserting or implying that raising difficulty improved outcomes, or that the counterintuitive pairs are a trend or pattern.
- **Ratio without the null.** Stating 11 vs 7 (or "more often") without the sign test in the same passage. `BLOCKER` if the sentence reads as evidence; `CORRECTION` if p ≈ 0.48 appears nearby but the sentence overstates.
- **`rd_adaptive_halting` counted as five findings.** Any phrasing that treats the five pairs as five independent anomalies.
- **A label flip as an intervention.** Asserting that the rendered task changed in exactly the flipped dimension.
- **Mechanism.** Any causal story for a flip: task design, harness behaviour, model internals, "the model was confused by the harder prompt".
- **Guarantee asymmetry omitted.** A draft that presents the 11 counterintuitive pairs without noting that 9 are compile-only. `BLOCKER` for Writer A and B both — it is the slot's central caveat.
- **Saturation/floor omitted.** A draft that reports 73 pairs without saying 55 cannot speak to direction.
- **Stale numbers:** `193`, `paused`, `provider_error`, `resumable`, `0.650`, "five counterintuitive families", "four intuitive families", "near-zero", "unsolvable", "the model cannot".
- **Design-critique overreach.** More than one bounded remark about what a difficulty label should record is a `CORRECTION`; a full evaluation-proposal section is a `BLOCKER`.
- **§7 misuse.** Citing the clean-comparator source audit as a cause of the flips rather than as attributed context.

## Job 4 — Claim discipline (one paragraph per draft)

- Is the thesis limited to the pair design, with the aggregate kept out of the opening and the conclusion?
- Does the draft give the expected-direction cases comparable space to the counterintuitive ones, or does it list one side and paragraph the other?
- Does the sign test appear adjacent to the 11-vs-7 count, and does the prose actually concede the null result?
- Does it state what the archive cannot show, unprompted, matching packet §5 and §8?
- Does every count carry a denominator, and every rate a bucket?
- Does it avoid using single-seed limits as a shield for a claim it made anyway?

## Job 5 — Compliance

Report the result of each:

1. Frontmatter exactly `title`, `date: 2026-10-21`, `layout: post`.
2. Byline `_by StrangeTcy_`.
3. Five epistemic fields in order: Original ideas, Synthesis, Prose, Certainty, Importance. Flag any self-score contradicting the prose (e.g. certainty 9/10 on 18 discordant draws).
4. One `<figure>` with a `<figcaption>` stating the four outcome counts and the total 73.
5. No `<img>`, no `assets/` path.
6. Word count 1,800–2,800 (`wc -w` minus frontmatter); report actual.
7. Profanity / glyphs: `fuck`, `shit`, `damn`, `🫣`, emoji in prose. Quote the line.
8. Leakage: `runs/atria_campaign`, `seed-0`, `coverage.json`, `state-62`, `R-POST`, `Reasoning-Atria`, `Writer A`, `Writer B`, `TODO`, `some model:`, snapshot names, finding IDs. Quote each hit.
9. Meta text addressed to an editor.
10. Family names spelled correctly and attributed to the right guarantee.

## Job 6 — Comparative recommendation (not optional)

Five axes, two sentences each, one-word winner per axis:

| Axis | What you are weighing |
|---|---|
| Evidence density | how much of the 73-pair ledger survives into prose without becoming a list |
| Structure | does the funnel/argument make the reader feel the evidence shrink |
| Honesty about limits | quality of the concessions, especially the sign test and the compile-only concentration |
| Readability | would a competent reader finish it |
| Originality of framing | is the opening a thought or a throat-clearing |

Then:

1. **Spine:** which draft Stage D builds on, ≤80 words.
2. **Transplants:** 3–5 passages from the other draft, quoted with a locating phrase; none graded `BLOCKER` or `CORRECTION`.
3. **Must not change:** qualities a reconciler will be tempted to sand off (usually the concession that costs the argument most).
4. **Word budget:** where to cut without losing the sign test, the guarantee asymmetry, or the saturation point.

## Rules

- A finding without a verbatim quote is not a finding.
- No severity inflation, and none of the reverse: `CLEAN` where clean.
- No new numbers, no new claims.
- A defect present in both drafts: state once, mark `SHARED`, rank it first.
- If both drafts are unpublishable on the same blocker, recommend **re-dispatch** and say exactly which part of the packet or brief must change.

## OUTPUT

```
VERDICT — Draft A: accept | accept with corrections | reject   (one sentence)
VERDICT — Draft B: accept | accept with corrections | reject   (one sentence)
BLOCKERS (ordered by damage)
CORRECTIONS
NOTES
SPOT-CHECK TABLE (both drafts, pass/fail per row)
CLAIMS LEDGER (both drafts)
CLAIM DISCIPLINE
COMPLIANCE
COMPARATIVE RECOMMENDATION (spine / transplants / must-not-change / word budget)
HANDOFF TO STAGE D (≤120 words, imperative)
```

No rewriting, no sample paragraphs, no praise section.
