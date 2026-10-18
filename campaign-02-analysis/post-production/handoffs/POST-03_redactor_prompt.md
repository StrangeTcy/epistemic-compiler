REDACTOR — POST-03: Where Mercury Breaks: Non-Monotonic Difficulty Transitions (Mercury-2.5)

You are the Redactor. Your job is to produce the FINAL article for POST-03 by synthesizing Draft B (gpt 6.1 sol max) as the base, importing elements from Draft A (gpt 6 sol max) per the Stage C blueprint, and applying every correction from the Stage D Claim Killer.

EVIDENCE PACKET (verified ground truth):
- F-008: Non-monotonic difficulty transitions. MoCo visible-test levels yield pass/fail/pass; CSS state machine easy-surface cases over 3/4/5 bits yield partial score/source-validation failure/pass; SQL fixed points pass at graph-chain lengths 6 and 25 but fail source validation at length 12.
- F-006: Bimodal environment difficulty. 6 named zero-rate environments (glyph, functorial_augmentation, monadic_reward, sheaf_invariant, ts_one_step, ts_trajectory) + 1 unscored (epistemic_silence/type_games). Pass rates range 0.00 to 1.00. Count discrepancy: 6 + 1 unscored = 7 claimed.
- F-004: Overall campaign 416 selected, 405 scored, 277 PASS, 128 FAIL, 0.684. 38 environments.
- Environment difficulty matrix: 340 rows (environment x difficulty_tuple), n_cases/n_scored/n_pass/n_fail/pass_rate/failure_modes/judge_guarantees.
- Single seed per selected cell (seed-0). Dirty repo. No replication.

STAGE C BLUEPRINT (accepted):
- Base: Draft B. Import from Draft A: figures, epistemic-status block, selection-rule sentence, "no direction" argument, closing cadence.
- 7-section structure + closing. Two figures.
- Remove: "fuckingly" artifacts (×3), regex pass claim, SQL surface qualifier, CSS axis mis-description, "hardest label" framing, partial-score reconciliation paragraphs, F-006 count discrepancy (cut to one sentence).
- Qualify: 21.6% (and 14.8%) as illustrative not calibrated; axis definitions unverified; F-006 tally discrepancy; judge guarantees as audit item.
- Retain: [d-word] ×2 in Draft B untouched.
- Acceptance criteria: 9 items.

STAGE D CLAIM KILLER RESULTS — MANDATORY ACTIONS:

DELETIONS:
1. "fuckingly" ×3 (A ×2, B ×1) — artifact, not bracketed token.
2. B's regex "all-pass" clause — phantom claim.
3. B's SQL surface sentence — unsupported qualifier.
4. B's CSS axis bullet — rewrite in packet terms.
5. Partial-score reconciliation paragraphs (both drafts) — keep one clause.
6. B's two-paragraph F-006 discussion — cut to one sentence.
7. "Hardest label" framing — not present, ensure not introduced.

REQUIRED ADDITIONS/CORRECTIONS:
8. Add 14.8% (PASS-FAIL-PASS only) alongside 21.6%, both labelled illustrative.
9. Add A's explicit selection-rule sentence to §3.
10. Add A's "no direction" argument under MoCo.
11. Add A's closing cadence.
12. Rewrite CSS axis: "CSS surface labels change class names and bit counts; the F-008 sequence varies bit count (3/4/5) within easy-surface cases."
13. Add axis attribution sentence: "per the packet's axis descriptions, not verified against task templates."
14. Add "mixed guarantees" audit-item framing (not assertion of variation).
15. Add Figure 1 and Figure 2 (built from matrix, not broken placeholders).
16. Add epistemic-status block from Draft A (five-field format).

NARROW/QUALIFIED CLAIMS (must carry caveats in same sentence):
- "MoCo visible-test level changes test coverage" → "as the packet describes the axis; not verified against executed source."
- "CSS varies class names and bit counts" → "surface labels change class names and bit counts; F-008 sequence varies bit count within easy-surface."
- "SQL varies graph-chain length" → "an ordered parameter whose relation to success probability is uncalibrated."
- Regex lengths 32/128/512 → "per packet; unit unspecified; no outcome sequence."
- Judge guarantees → "recorded per row; whether they vary is unverified; audit item."
- F-006 "bimodal" → "as F-006 labels it; no distribution supplied."
- F-006 zero tally → "six named + one unscored; not seven measured zeros."
- 0.684 → "among scored cases; 11 unscored outside denominator."
- 21.6% / 14.8% → "illustrative, not calibrated null."
- Truncation hypothesis → "one untested hypothesis among several."
- Source-validation failure as legitimate benchmark failure → "if valid source is part of contract, which packet doesn't specify."
- Non-monotonic "reversal" → "recorded sequence of single outcomes, not estimated response curve."
- "Mercury-2.5" → "one campaign under that label; no checkpoint/harness manifest."
- MoCo level ordering → "level values and spacing not supplied."
- Figures → "built from selected matrix rows; grey = unscored not zero; not an enumeration of eligible sweeps."

SAFE CLAIM SET (can state without qualification):
1. Campaign selected 416 cases across 38 environments; scored 405: 277 PASS, 128 FAIL.
2. 11 selected cases unscored (416−405). Not failures.
3. Matrix has 340 rows: n_cases, n_scored, n_pass, n_fail, pass_rate, failure_modes, judge_guarantees.
4. Single seed (seed-0) per selected cell; no replication.
5. Dirty repo at run time.
6. Environment pass rates range 0.00 to 1.00.
7. MoCo: PASS → FAIL → PASS across visible-test levels.
8. CSS: partial score → source-validation failure → PASS at 3/4/5 bits.
9. SQL: PASS → source-validation failure → PASS at lengths 6/12/25.
10. Two middle failures (CSS, SQL) are source-validation failures, not behavioral/semantic.
11. Three sequences are those F-008 identifies; no exhaustive enumeration or prespecified selection rule.
12. No generated submissions, output lengths, budgets, or validator diagnostics.
13. Monotonically declining success probabilities can produce non-monotonic single-outcome sequences.
14. Archive does not validate difficulty labels as ordinal scale; does not locate threshold.

FORBIDDEN CLAIM SET (must not appear):
- Reversals frequent/rare/enriched over chance.
- 21.6%/14.8% as null model/baseline/expected rate.
- Truncation/output limits/dirty repo/changing judge guarantees CAUSED any failure.
- Seven environments scored 0.00.
- Regex produced all-pass (or any) outcome sequence.
- SQL had a surface-label setting.
- CSS swept surface labels in F-008 sequence.
- Middle setting is "hardest label."
- 0.684 as unconditional success probability.
- Mercury-2.5 capability "breaks" at located threshold.

CANDIDATE DRAFTS (verbatim):
[Both drafts are in campaign-02-analysis/comparison_12.md — gpt 6 sol max and gpt 6.1 sol max. Include both verbatim.]

TASK: Produce the FINAL article. Follow the blueprint structure (7 sections + closing). Apply all mandatory deletions, required additions/corrections, narrow-claim qualifications, and production fixes. Use Draft B as base prose. Import from Draft A: figures, epistemic-status block, selection-rule sentence, "no direction" argument, closing cadence. Include both figures (Figure 1 = matrix overview, Figure 2 = three sequences). Write in the author's voice (first person, "I"). Preserve [d-word] ×2 (intentional). Remove "fuckingly" artifacts. Output the complete final article as a single markdown file with YAML front matter, ready to save as campaign-02-analysis/posts/POST-03-difficulty-transitions.md.
