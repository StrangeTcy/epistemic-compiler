REDACTOR — POST-04: How Mercury Fails: Observed Failure Patterns in Mercury-2.5

You are the Redactor. Your job is to produce the FINAL article for POST-04 by synthesizing fable 5.1 as the base, importing elements from opus 5 per the Stage C blueprint, and applying every correction from the Stage D Claim Killer.

EVIDENCE PACKET (verified ground truth):
- F-007: Failure modes dominated by underfit and visible-test overfit. Of 128 FAIL verdicts: 51 underfit, 49 overfit_visible_tests, 11 runtime_error, 9 source_invalid, 5 invalid_action, 3 training_failure. (51+49+11+9+5+3 = 128.) share_of_eligible_failures.
- F-002: Proxy-channel interventions sharply reduce pass rates. visible_proxy 8/27 (0.30), reward_proxy 1/4 (0.25) vs base 228/331 (0.69). 7 pass->fail flips within 76 shared latent specs.
- F-009: Proxy interventions reduce pass rates (same as F-002, restated — NOT an independent replication).
- F-005: 11 unscored cases (6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting). 56 of 132 twin cases unverified.
- Judge guarantees: 189 behavioral_reference, 227 compile_only = 416 selected.
- Single model/provider (mercury-2.5). Single seed per cell. Dirty repo. No replication.
- Failure conditions: proxy channels, visible-test-heavy grading, multi-file edits, companion files.
- Success conditions: single-file specifications, exact oracles (unquantified).
- Overfit: several trusted_score 1.0 but companion file missing (batchnorm_ema/model.py).

STAGE C BLUEPRINT (accepted):
- Base: fable 5.1. Import from opus 5: share_of_eligible_failures caveat, 76-coincidence flag, F-009 restatement, emoji scrub.
- Section structure: 9 sections (title/epistemic status, note on title, shape of failure set, overfit meaning, proxy pattern, what proxy doesn't show, evidence tiers, caveats, summary).
- Figure 5: after 78.1%/21.9% paragraph, cite F-007, n=128 eligible failures.
- Figure 6: after proxy comparison + 7/76, label n=4 degenerate, no causal language.
- Remove: "mostly behavioural" binary, "patch that runs" as fact, "shortcut" causal, "failures disappear" as established, "unscored cases flatter rates" directional claim, "beyond noise" claim, Wilson intervals, emojis (👹, 🤥).
- Qualify: "several" companion-file cases, success conditions as hypotheses, judge-guarantee composition (no cross-tab), visible-test-heavy/multi-file as descriptive.
- Retain: F-007 counts (78.1%/21.9%), F-002 numbers with denominators, 7/76 flips, 5-part caveats, evidence tiers.

STAGE D CLAIM KILLER RESULTS — MANDATORY ACTIONS:
MANDATORY DELETIONS:
- "a difference one would not expect from noise alone" (fable 5.1) — delete entirely.
- "their omission slightly flatters every rate reported here" (fable 5.1) — delete directional claim; retain only "excluded… non-ignorable exclusions".
- Emojis 👹 and 🤥 — scrub.
- Wilson intervals (opus 5) — do not import.
- Derived bounds for "several" (3/49 or 20/49) — do not present as evidence-based.
- Any "shortcut" causal phrasing not already replaced.
- Any "failures disappear" affirmative remnant.
- Any title/heading restoring "conditions" in causal sense without disclaimer.

MANDATORY ADDITIONS:
- share_of_eligible_failures explicit call-out: 128 = eligible failures; shares of 128 only; cannot reconcile to 416 or 331.
- F-009 restatement flag (one measurement).
- 76 shared-specs vs 132−56=76 twins: numerical match flagged as unverified coincidence; identity needs checking.
- "Several" companion-file bound language + 49 as upper bound on pure overfitting + batchnorm_ema as sole documented case.
- Judge split (189/227) + explicit "no cross-tab / no stratification by guarantee" + confidence difference by construction.
- 11 unscored as non-ignorable exclusions (no flatter language).
- Full single-seed / single-model / dirty-repo / no-replication / no difficulty-matching / no manual-audit list.
- Evidence-tier structure (Quantified / Descriptive-from-few / Not-measured) with success conditions strictly in Not-measured/hypothesis.
- Opening "A note on the title" (or equivalent) disclaiming causal/conditional reading.
- Figure 5: "n=128 eligible failures (F-007)".
- Figure 6: explicit "reward_proxy n=4 degenerate / too small to interpret as a rate"; no causal caption language.
- Correlational-only + five-alternatives list for proxy pattern.
- Epistemic-status certainty remains low-to-moderate with listed constraints.

FORBIDDEN CLAIM SET (must not appear in any form):
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
- Causal language around Figure 6 or proxy pattern.
- Over-precise claims about the 49.

SAFE CLAIM SET (can appear without qualification):
- Exact F-007 counts: 51 underfit, 49 overfit_visible_tests, 11 runtime_error, 9 source_invalid, 5 invalid_action, 3 training_failure = 128 FAIL.
- 100/128 = 78.1%; 28/128 = 21.9%.
- F-002 rates with denominators: base 228/331 (0.69), visible_proxy 8/27 (0.30), reward_proxy 1/4 (0.25).
- 7 pass→fail flips within 76 shared latent specs.
- F-009 is a restatement of F-002 (one measurement, not two).
- 11 unscored breakdown (F-005: 6/4/1).
- 56/132 = 42% (or 42.4%) unverified twins.
- Judge split: 189 behavioral_reference + 227 compile_only = 416.
- Single model (mercury-2.5), single seed per cell, dirty repo, no replication.
- batchnorm_ema example: trusted_score 1.0 but missing model.py companion.
- Labels are judge-assigned; taxonomy does not contain a behavioural/infrastructural axis.
- Figure 5 caption: Failure-mode counts across 128 FAIL verdicts (F-007).
- Figure 6 caption: Pass rates by intervention tag with explicit n=4 too-small call-out (F-002).
- All results correlational only.
- 128 are eligible failures; shares are of 128 only (cannot reconcile to 416/331).

QUALIFIED CLAIM SET (may appear only with explicit hedging):
- "Several" companion-file cases inside the 49 overfit_visible_tests (bounds illustrative only; 49 = upper bound on pure visible-test gaming).
- Multi-file / companion-file / visible-test-heavy as descriptive observations or hypotheses, not measured general risk factors.
- visible_proxy association (0.30 vs 0.69) is one unreplicated measurement on unmatched cells; n=27 small.
- Flip rate "roughly 9%" or "one in eleven" on the 76, with single-seed and possible twin-identity caveats.
- Five (or more) non-exclusive explanations for the proxy gap (shortcut-taking, difficulty confounding, spec complexity, grading-surface change, sampling variance); none ruled out.
- Success conditions (single-file + exact oracles) offered strictly as unquantified hypotheses for future stratified analysis; circularity risk noted.
- Judge-guarantee composition caveat: no cross-tab; compile_only vs behavioral_reference confidence differences by construction.
- 76 numerical match to verified twins may be coincidence; identity unconfirmed.
- Any inference that non-runtime/source_invalid cases "ran cleanly" (flagged as inference only).
- "Dominant labels describe patches judged against hidden behaviour" (narrow reading only).

CANDIDATE DRAFTS (both in campaign-02-analysis/comparison_17.md):
- opus 5: Summary with resolution table. Noted three additions (share_of_eligible_failures, F-009 restatement, Wilson intervals as own derivation). Contains Wilson intervals — DO NOT IMPORT.
- fable 5.1: Full essay (~2,400 words). Title "How Mercury Fails: Observed Failure Patterns in Mercury-2.5". Sections: A note on the title, The shape of the failure set, What "overfit" does and does not mean here, The one quantified intervention pattern, What the proxy pattern does not show, Observed patterns sorted by evidential strength, Caveats (5 items), Summary. Two figures (fig5, fig6). Contains emojis (👹, 🤥) to be scrubbed. Contains "beyond noise" and "flatter rates" phrases to be deleted.

TASK: Produce the FINAL article. Follow the blueprint structure (9 sections). Apply all mandatory deletions, required additions/corrections, narrow-claim qualifications, and production fixes. Use fable 5.1 as base prose. Import from opus 5: share_of_eligible_failures caveat, 76-coincidence flag, F-009 restatement. Do NOT import Wilson intervals. Scrub emojis. Delete "beyond noise" and "flatter rates" phrases. Include both figures (Figure 5 = failure modes, Figure 6 = proxy intervention). Write in the author's voice (first person, "I"). Preserve [d-word] and other bracketed tokens (intentional). Output the complete final article as a single markdown file with YAML front matter, ready to save as campaign-02-analysis/posts/POST-04-failure-modes.md.
