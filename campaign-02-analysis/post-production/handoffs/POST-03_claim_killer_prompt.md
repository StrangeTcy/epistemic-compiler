CLAIM KILLER — POST-03: Where Mercury Breaks: Non-Monotonic Difficulty Transitions (Mercury-2.5)

You are the Claim Killer. Your job is to verify every number, strong factual claim, and inferred conclusion in the two candidate drafts against the evidence packet. Produce a claim-by-claim verification table with verdicts.

EVIDENCE PACKET (verified ground truth):
- F-008: Non-monotonic difficulty transitions. MoCo visible-test levels yield pass/fail/pass; CSS state machine easy-surface cases over 3/4/5 bits yield partial score/source-validation failure/pass; SQL fixed points pass at graph-chain lengths 6 and 25 but fail source validation at length 12.
- F-006: Bimodal environment difficulty. 7 environments score 0.00 (6 named: glyph, functorial_augmentation, monadic_reward, sheaf_invariant, ts_one_step, ts_trajectory; +1 unscored: epistemic_silence/type_games). Pass rates range 0.00 to 1.00. Count discrepancy: 6 named + 1 unscored = 7 claimed.
- F-004: Overall campaign 416 selected, 405 scored, 277 PASS, 128 FAIL, 0.684. 38 environments.
- Environment difficulty matrix: 340 rows (environment x difficulty_tuple), n_cases/n_scored/n_pass/n_fail/pass_rate/failure_modes/judge_guarantees.
- Single seed per selected cell (seed-0). Dirty repo. No replication.
- Difficulty axes: MoCo visible-test level changes test coverage; CSS surface labels change class names and bit counts; SQL changes graph-chain length; regex changes input-string length (32/128/512).

EDITORIAL BLUEPRINT (accepted Stage C) key decisions:
- Base: Draft B (gpt 6.1 sol max). Import from Draft A: figures, epistemic-status block, selection-rule sentence, "no direction" argument, closing cadence.
- 7-section structure. Two figures.
- Remove: "fuckingly" artifacts, regex pass claim, SQL surface qualifier, CSS axis mis-description, "hardest label" framing, partial-score reconciliation, F-006 count discrepancy.
- Qualify: 21.6% (and 14.8%) as illustrative not calibrated; axis definitions unverified; F-006 tally discrepancy; judge guarantees as audit item.
- Retain: [d-word] ×2 in Draft 2 untouched. No other bracketed tokens.
- Acceptance criteria: 9 items (no calibrated null claim, no prevalence claim, denominator hygiene, sequence asymmetry, source-validation distinction, no unsupported causal explanation, axis construct validity, provenance/replication limits, no invented evidence).

CANDIDATE DRAFTS (verbatim):
[Both drafts are in campaign-02-analysis/comparison_12.md — gpt 6 sol max and gpt 6.1 sol max. Include both verbatim.]

TASK: Produce a claim-by-claim verification table. For every number, strong factual claim, and inferred conclusion in BOTH drafts, provide:
- Claim (as written, with draft attribution A or B)
- Verdict: SUPPORTED / UNSUPPORTED / NARROW / CORRECT-ARITHMETIC / NEEDS-CHECK
- Evidence source (which part of the packet supports or contradicts it)
- Required action for the final article

Be exhaustive. Include at least 40 rows. Flag every causal inference that outruns the evidence. Flag every arithmetic error. Flag every unsupported interpretation. Flag every unverified detail.

IMPORTANT: Bracketed tokens such as [ac-word], [d-word], [m-word] are INTENTIONAL replacements for words the author dislikes. They are NOT production artifacts. Do NOT flag them for removal.

Also produce a short "safe claim set" — the exact list of claims the final article may make without qualification, and a "qualified claim set" — claims that require a caveat in the same sentence.
