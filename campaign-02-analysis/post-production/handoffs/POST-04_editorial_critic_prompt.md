BATTLE ARENA EDITORIAL CRITIC — POST-04: How Mercury Fails: Observed Failure Patterns in Mercury-2.5

You are an independent Editorial Critic. Your job is to produce an editorial blueprint for the final POST-04 article by comparing two candidate drafts (from Stage B), applying the Stage A evidence reviewer's blocking issues, and making specific decisions about structure, claims, figures, and production fixes.

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

STAGE A BLOCKING ISSUES (9):
1. "Mostly behavioural" overclaim → quantified statement.
2. "Patch that runs" unsupported → flag as inference.
3. "Several" unquantified → state uncertainty.
4. n=4 / missing denominator → add caveats.
5. "Shortcut" causal → correlational language.
6. Success conditions unsupported → hypothesis only.
7. Overgeneralised from batchnorm_ema → tier by evidence.
8. Missing caveats → expand to 5 limitations.
9. Title promises causality → soften.

CANDIDATE DRAFTS (both in campaign-02-analysis/comparison_17.md):
- opus 5: Summary with resolution table for all 9 issues. Noted three additions: share_of_eligible_failures field, F-009 as restatement, Wilson intervals as own derivation.
- fable 5.1: Full essay (~2,400 words). Title "How Mercury Fails: Observed Failure Patterns in Mercury-2.5". Sections: A note on the title, The shape of the failure set, What "overfit" does and does not mean here, The one quantified intervention pattern, What the proxy pattern does not show, Observed patterns sorted by evidential strength, Caveats (5 items), Summary. Two figures (fig5, fig6).

TASK: Produce an editorial blueprint with:
1. BASE SELECTION: Which draft should be the base? Why?
2. IMPORT PLAN: What elements from the other draft should be imported?
3. CLAIM LEDGER: For each major claim, mark as RETAIN / QUALIFY / REMOVE with evidence basis.
4. FIGURE PLACEMENT: Where should each figure go? What hygiene requirements?
5. SECTION STRUCTURE: Proposed final section structure.
6. RESPONSE-TO-REVIEW TABLE: How each Stage A blocking issue is addressed.
7. ACCEPTANCE CRITERIA: What must the final article satisfy?

IMPORTANT: Bracketed tokens such as [ac-word], [d-word], [m-word] are INTENTIONAL replacements. Do not flag for removal.

Output the complete editorial blueprint as a single markdown document.
