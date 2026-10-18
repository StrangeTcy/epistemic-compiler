BATTLE ARENA CLAIM KILLER — POST-04: How Mercury Fails: Observed Failure Patterns in Mercury-2.5

You are an independent Claim Killer. Your job is to verify every factual claim, number, and inference in the two candidate drafts against the verified evidence packet. Produce a claim-by-claim verification table with at least 40 rows, plus safe/qualified/forbidden claim sets.

EVIDENCE PACKET (verified ground truth):
- F-007: 51 underfit, 49 overfit_visible_tests, 11 runtime_error, 9 source_invalid, 5 invalid_action, 3 training_failure = 128 FAIL. share_of_eligible_failures.
- F-002: visible_proxy 8/27 (0.30), reward_proxy 1/4 (0.25) vs base 228/331 (0.69). 7 pass->fail flips within 76 shared latent specs.
- F-009: Same as F-002 (restatement, not replication).
- F-005: 11 unscored (6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting). 56/132 unverified twins.
- Judge guarantees: 189 behavioral_reference, 227 compile_only = 416 selected.
- Single model/provider (mercury-2.5). Single seed per cell. Dirty repo. No replication.
- Failure conditions: proxy channels, visible-test-heavy grading, multi-file edits, companion files.
- Success conditions: single-file specifications, exact oracles (unquantified).
- Overfit: several trusted_score 1.0 but companion file missing (batchnorm_ema/model.py).

STAGE C BLUEPRINT KEY DECISIONS:
- Base: fable 5.1. Import from opus 5: share_of_eligible_failures caveat, 76 coincidence flag, F-009 restatement, emoji scrub.
- Remove: "mostly behavioural" binary, "patch that runs" as fact, "shortcut" causal, "failures disappear" as established, "unscored cases flatter rates" directional claim, "beyond noise" claim for visible-proxy gap, Wilson intervals.
- Qualify: "several" companion-file cases, success conditions as hypotheses, judge-guarantee composition (no cross-tab), visible-test-heavy/multi-file as descriptive.
- Retain: F-007 counts (78.1%/21.9%), F-002 numbers with denominators, 7/76 flips, 5-part caveats, evidence tiers.
- Figure 5: cite F-007, n=128 eligible failures. Figure 6: label n=4 degenerate, no causal language.

CANDIDATE DRAFTS (both in campaign-02-analysis/comparison_17.md):
- opus 5: Summary with resolution table. Noted three additions (share_of_eligible_failures, F-009 restatement, Wilson intervals as own derivation).
- fable 5.1: Full essay (~2,400 words). Title "How Mercury Fails: Observed Failure Patterns in Mercury-2.5". Sections: A note on the title, The shape of the failure set, What "overfit" does and does not mean here, The one quantified intervention pattern, What the proxy pattern does not show, Observed patterns sorted by evidential strength, Caveats (5 items), Summary. Two figures (fig5, fig6). Contains emojis (👹, 🤥) to be scrubbed.

TASK: Produce a claim-by-claim verification table with at least 40 rows covering both drafts. For each claim, mark as SUPPORTED / QUALIFIED / UNSUPPORTED with evidence basis. Then produce:
1. SAFE CLAIM SET: Claims that can appear in the final article without qualification.
2. QUALIFIED CLAIM SET: Claims that can appear but only with explicit hedging.
3. FORBIDDEN CLAIM SET: Claims that must not appear in any form.
4. MANDATORY DELETIONS: Specific phrases/paragraphs to remove.
5. MANDATORY ADDITIONS: Specific caveats/qualifications to add.
6. PRODUCTION FIXES: Emoji scrub, figure hygiene, etc.

IMPORTANT: Bracketed tokens such as [ac-word], [d-word], [m-word] are INTENTIONAL replacements for words the author dislikes. They are NOT production artifacts. Do not flag them for removal.

Output the complete claim verification as a single markdown document.
