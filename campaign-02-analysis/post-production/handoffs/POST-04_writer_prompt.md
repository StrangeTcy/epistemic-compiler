BATTLE WRITER — POST-04: How Mercury Fails: Recurring Failure Modes and Their Conditions (Mercury-2.5)

You are an independent candidate producing a complete research essay for the StrangeTcy public site. You receive the evidence packet, the evidence reviewer's adversarial brief, and the existing draft stub below. Produce a complete, publication-ready essay.

EVIDENCE PACKET (verified ground truth):
- F-007: Failure modes dominated by underfit and visible-test overfit. Of 128 FAIL verdicts: 51 underfit, 49 overfit_visible_tests, 11 runtime_error, 9 source_invalid, 5 invalid_action, 3 training_failure. (51+49+11+9+5+3 = 128.)
- F-002: Proxy-channel interventions sharply reduce pass rates. visible_proxy 8/27 (0.30), reward_proxy 1/4 (0.25) vs base 228/331 (0.69). 7 pass->fail flips within 76 shared latent specs.
- F-009: Proxy interventions reduce pass rates (same as F-002, restated — NOT an independent replication).
- F-005: 11 unscored cases (6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting). 56 of 132 twin cases unverified.
- Failure taxonomy: failure_mode_normalized, count, share_of_eligible_failures, case_ids, judge_guarantees.
- Overfit cases: several have trusted_score 1.0 but marked failed because required companion file missing (e.g., batchnorm_ema missing model.py).
- Proxy interventions: visible_proxy cases pass at 0.30, reward_proxy at 0.25.
- Failure conditions: proxy channels, visible-test-heavy grading, multi-file edits, companion files.
- Success conditions: single-file specifications, exact oracles.
- Judge guarantees: 189 behavioral_reference, 227 compile_only = 416 selected.
- Single model/provider (mercury-2.5). Single seed per cell. Dirty repo. No replication.

EVIDENCE REVIEWER BRIEF (Stage A — blocking issues):
1. "Mostly behavioural, not infrastructural" is an overclaim. The taxonomy labels are not classified as behavioral/infrastructural in the data. 28/128 = 21.9% are mechanical errors. Replace with quantified statement.
2. "Model usually produces a patch that runs" is unsupported. F-007 gives failure-mode labels, not execution-status data. Cannot assume the 108 non-runtime/non-source-invalid failures ran.
3. "Overfit ≠ gaming in every case" is correct but under-quantified. "Several" trusted_score 1.0 companion-file cases is not quantified (could be 3/49 or 20/49). State uncertainty explicitly.
4. Proxy numbers (0.30/0.25/0.69) are numerically correct. But n=4 (reward_proxy) is too small for stable estimate. Missing denominator: 7 flips within 76 shared latent specs (~9% flip rate).
5. "Shortcut that the model takes" is unsupported causal/intentional claim. Data only shows correlational pass-rate differences. Multiple alternative explanations cannot be ruled out.
6. "Conditions under which failures disappear" (single-file/exact oracle) is unsupported. No pass-rate data cited. Risk of circularity. Present as hypothesis at most.
7. "Visible-test-heavy grading" and "multi-file edits" as general conditions are overgeneralized from single example (batchnorm_ema).
8. Missing caveats: 11 unscored cases (F-005), 56/132 unverified twins (42%), judge guarantee composition (189 behavioral_reference vs 227 compile_only), single seed per cell, dirty repo, no replication. 132-56=76 numerical coincidence with shared latent specs needs verification.
9. Title "Recurring Failure Modes and Their Conditions" promises causal/conditional claims. Soften or caveat up front.

EXISTING DRAFT STUB (to be replaced, not patched):
[See campaign-02-analysis/posts/POST-04-failure-modes.md]

HOUSE STYLE: See campaign-02-analysis/post-production/source_snapshots/shared/house_style.md and style_reference_material.md.

TASK: Produce a complete, publication-ready essay. The reviewer's blocking issues must be addressed, not ignored. Key reframing requirements:
- Replace "mostly behavioural, not infrastructural" with a quantified statement about the two dominant labels (100/128, 78.1%) alongside the mechanical-error share (28/128, 21.9%).
- Do not claim the model "usually produces a patch that runs" — flag as inference.
- Quantify the companion-file artifact uncertainty ("several" of 49, fraction unknown).
- Add n=4 caveat for reward_proxy; add 76-spec denominator for flips.
- Replace "shortcut that the model takes" with correlational language and list alternative explanations.
- Present success conditions as unquantified hypotheses, not established facts.
- Separate conditions by evidential strength (quantified vs. anecdotal/descriptive).
- Expand caveats to include all five limitations (judge-label composition, unscored cases, unverified twins, single-seed/no-replication, dirty repo).
- Soften title/framing: "conditions" → "observed patterns" or caveat up front.
- Every number must be traceable to the evidence packet. Include appropriate caveats in the same sentence as qualified claims.

IMPORTANT: Bracketed tokens such as [ac-word], [d-word], [m-word] are INTENTIONAL replacements for words the author dislikes. They are NOT production artifacts. Do not flag them for removal.

Output the complete article as a single markdown file with YAML front matter, ready to save as campaign-02-analysis/posts/POST-04-failure-modes.md.
