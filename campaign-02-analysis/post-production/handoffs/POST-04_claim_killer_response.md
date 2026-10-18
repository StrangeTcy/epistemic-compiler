# Stage D — Claim Killer Response (POST-04)

Source: Battle Arena, pasted by user 2026-10-17. Output from grok 4.5 (70-row verification table + safe/qualified/forbidden sets + mandatory deletions/additions/production fixes) and gemini 3.1 pro grounding (45-row verification table + similar structure). Preserved in campaign-02-analysis/comparison_19.md (301 lines, 30.4 KB).

Prompt artifact: campaign-02-analysis/post-production/handoffs/POST-04_claim_killer_prompt.md

Status: ACCEPTED as Stage D (Claim Killer). Two independent model outputs.

KEY FINDINGS (both reviewers agree):

1. No arithmetic errors. All F-007 counts sum to 128. 100/128=78.1%, 28/128=21.9%. F-002 rates correct. 7/76 flips correct.

2. MANDATORY DELETIONS (both agree):
- "a difference one would not expect from noise alone" (fable 5.1) — delete.
- "their omission slightly flatters every rate reported here" (fable 5.1) — delete directional claim.
- Emojis 👹 and 🤥 — scrub.
- Wilson intervals (opus 5) — do not import.
- Derived bounds for "several" (3/49 or 20/49) — do not present as evidence-based (gemini flags as unsupported; grok says qualified).

3. MANDATORY ADDITIONS (both agree):
- share_of_eligible_failures caveat (128 = eligible failures, cannot reconcile to 416/331).
- Figure 5 caption: "n=128 eligible failures" (not "128 FAIL verdicts").
- Figure 6 caption: label n=4 reward_proxy as "degenerate".
- 76 shared-specs vs 76 verified twins: flag as unverified coincidence.
- F-009 restatement flag.
- 5-part caveats (judge composition, unscored, twins, single-seed, dirty repo).
- Evidence tiers (quantified / descriptive / not-measured).
- "A note on the title" disclaimer.

4. FORBIDDEN CLAIM SET (both agree):
- "Mostly behavioural, not infrastructural" binary.
- "Usually produces a patch that runs" as fact.
- "Shortcut that the model takes" causal.
- "Failures disappear" as established.
- "Unscored cases flatter rates" directional.
- "Beyond noise" / significance claims for visible-proxy gap.
- Wilson intervals or derived CIs.
- F-009 as replication.
- Cross-tab by judge guarantee (none exists).
- Quantified multi-file/companion-file rate beyond "several".
- Reconciliation of 128 against 416 or 331.
- Causal language around Figure 6.
- Over-precise claims about the 49.

5. SAFE CLAIM SET (both agree): All exact F-007 counts, F-002 rates with denominators, 7/76 flips, judge split 189/227, 11 unscored breakdown, 56/132 unverified twins, evidence conditions (single model/seed/dirty/no-rep), batchnorm_ema example, labels judge-assigned, F-009 restatement, correlational-only framing.

6. QUALIFIED CLAIM SET (both agree): "Several" companion-file cases (bounds illustrative only, 49 = upper bound), multi-file/companion-file/visible-test-heavy as descriptive/hypotheses, visible_proxy association (one unreplicated measurement), flip rate ~9% with caveats, five alternative explanations, success conditions as hypotheses, judge-guarantee composition (no cross-tab), 76 coincidence flag, "patch that runs" as inference only.

7. PRODUCTION FIXES: Emoji scrub (👹, 🤥), figure hygiene (captions cite F-007/F-002, n=128 eligible, n=4 degenerate), preserve bracketed tokens, clean YAML front matter, ~2,200-2,500 words, import checklist (eligible-share, 76-flag, F-009 restatement; NOT Wilson).

8. OVERALL VERDICT: fable 5.1 is correct base. Requires only noise-claim deletion, flatter-claim deletion, emoji scrub, plus three opus imports. After listed fixes, article fully aligned with evidence packet and Stage C blueprint. No remaining blocking unsupported claims.

Full verbatim text in campaign-02-analysis/comparison_19.md.
