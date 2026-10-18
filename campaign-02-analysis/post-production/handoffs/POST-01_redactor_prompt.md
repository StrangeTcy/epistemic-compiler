REDACTOR — POST-01: The Model's Belief Is Right; Its Decision Is Fragile (Mercury-2.5)

You are the Redactor. Your job is to produce the FINAL article for POST-01 by synthesizing Draft A (gpt 6 sol max) as the base, importing elements from Draft B (gpt 6.1 sol max) per the Stage C blueprint, and applying every correction from the Stage D Claim Killer.

EVIDENCE PACKET (verified ground truth):
- T1 same_fact_presentation: 6 cells × 6 seeds = 36 matched pairs. 0/36 belief flips. 5/36 terminal answer flips (all correctness flips). 17/36 diagnostic-choice divergences. 3 fact counts (3, 4, 5) × 2 priors (1/2, 1/3) = 6 cells. Canonical bullet order vs reversed numbered order. Oracle is exact.
- Epistemic games: 23/23 exact posterior match (base + evidence/presentation/prior interventions). Zero posterior error. posterior_reported = posterior_true.
- Proxy interventions: visible_proxy 8/27 (0.30). reward_proxy 1/4 (0.25). base 228/331 (0.69). Paired flips: 7 pass→fail (4 visible_proxy) within 76 intervention cases sharing latent spec with base.
- Campaign: 416 selected, 405 scored, 277 PASS, 128 FAIL, 0.684. 11 unscored. Judge guarantees: 189 behavioral_reference + 227 compile_only = 416. Single seed per selected cell. Dirty repo. 56 of 132 twin cases unverified.
- Limitations: single model/provider (mercury-2.5, reasoning_effort=high). T1: 36 pairs, no CIs. Intervention cases not difficulty-matched. Terminal-answer extraction may be brittle. No independent replication.

STAGE C BLUEPRINT (accepted):
- Adopt narrow behavioral dissociation thesis.
- Draft A as base; import B's tables, "outputs not modules" header, "zero flips ≠ zero error" couplet, titled coda.
- Remove: "verdict correct in all 23", "38 environments", "reasoning effort high", "latent specification", game intervention types. (NOTE: Stage D found these ARE in the packet. Editor ruling pending — conservative path: remove all three since none is load-bearing. Follow removal unless editor overrides.)
- Remove: "one in seven" garbled fraction, "pass rates from 0.00 to 1.00" (absent), judge guarantees misattached to 405 (already correct in both drafts).
- Add: sampling-noise null, chance agreement for diagnostic choices, posterior invariance as floor effect, answer-posterior relationship undefined, per-cell flip distribution stated as unavailable, pre-specification of T1 stated as unknown.
- Keep: [ac-word], [d-word], [m-word] tokens (intentional). Remove 👹 glyph → replace with [m-word].
- Figure 1: three endpoints SVG (from Draft A, keep as-is).
- Figure 2: new campaign denominators SVG (replace B's "!" placeholder).

STAGE D CLAIM KILLER RESULTS — MANDATORY ACTIONS:

DELETIONS:
1. "verdict was correct in all 23" and both later uses of "verdicts" (A) — UNSUPPORTED.
2. "across 38 environments" (A and B) — UNSUPPORTED.
3. "nor does it mean that only one in seven changed answers was wrong" (B) — GARBLED.
4. Both 👹 glyphs → replace with [m-word] (A and B).
5. B's "!" figure placeholder → replace with new Figure 2 SVG.
6. Row 44 rephrase (B): "It was not merely stable while ignoring the task's quantities" → delete (UNSUPPORTED).

REQUIRED ADDITIONS (absent from both drafts):
7. Sampling-noise null: The probe lacks a same-presentation re-run baseline. 5/36 could be sampling noise. Include the 2p(1−p) illustration, clearly labeled as hypothetical.
8. Chance agreement for diagnostic choices: Without knowing k (number of options), 17/36 cannot be compared to chance. k=2 gives ~18/36.
9. Posterior invariance as floor effect: 0/36 may reflect that the posterior is an easy, deterministic computation (23/23 exact in games), not robustness per se.
10. Answer-posterior relationship undefined: The task spec does not define how the terminal answer should relate to the posterior.
11. Per-cell flip distribution: State that it is unavailable in the recorded results.
12. Pre-specification of T1: State that whether T1 was pre-specified is not recorded.

NARROW/QUALIFIED CLAIMS (must carry caveats in same sentence):
- "Presentation sensitivity" → "differences between presentations" unless noise null exists.
- "Diagnostic divergence" → "divergence, not error" + chance caveat.
- "Posterior invariance" → floor effect caveat.
- "Right" in title → supported for 23 games only.
- "Same posterior, different answer" → assuming extraction correct + undefined relationship.
- "Five correctness flips" → under recorded extraction procedure.
- "Stated belief tracked content" (B) → only if interventions changed true posterior.
- "Proxy-tagged cases passed less often" → descriptive, not difficulty-matched, n=4.
- "7/76 pass→fail" → one direction only, not transition probability.
- "0.684 campaign pass rate" → pools two judge types, says nothing about posterior accuracy.
- "Games corroborate T1" → related campaign evidence, not independent replication.
- "Dirty repo" → provenance caveat, not contamination.
- "T1 vs campaign" → whether T1's 36 pairs are inside 405 is unspecified.
- "Pre-specification" → not recorded.

SAFE CLAIM SET (can state without qualification):
1. 36 matched pairs: 3 fact counts × 2 priors = 6 cells, 6 seeds each.
2. Facts and prior identical within pair; canonical bullet vs reversed numbered.
3. Exact oracle.
4. Reported posterior identical in all 36 (0/36).
5. Terminal answer differed in 5/36; all were correctness flips.
6. Diagnostic choice differed in 17/36.
7. 23 epistemic games: posterior_reported = posterior_true every time, zero error.
8. Base 228/331 (0.69), visible-proxy 8/27 (0.30), reward-proxy 1/4 (0.25).
9. 7 pass→fail among 76 base-linked intervention cases; 4 visible-proxy.
10. Campaign: 416 selected, 405 scored (277 PASS, 128 FAIL, 0.684), 11 unscored.
11. 189 BR + 227 CO = 416 selected (not 405).
12. 56 of 132 twin cases unverified (~42%).
13. Single seed per selected cell (campaign); dirty repo; no independent replication; T1 no CIs; intervention cases not difficulty-matched; extraction may be brittle.
14. Arithmetic: 5/36≈14%, 17/36≈47%, 56/132≈42%.
15. Unchanged reported posterior did not guarantee unchanged terminal answer in this probe.
16. Order and format co-vary; neither isolated.

ADDITIONAL NARROW CLAIMS FROM STAGE D (must be hedged):
- A33: "a changed answer as evidence that the model had read different facts. But that explanation predicts more than the observations show" → UNSUPPORTED. Remove the purported prediction. Say internal readings cannot be determined.
- A42: "The posterior's invariance makes a simple 'it received different evidence' account less satisfying" → NARROW. Remove evidential ranking or state as intuition.
- A48: "its stated probability tracked the oracle despite the tested variations" → NARROW. Say "matched the true posterior in those 23 cases."
- B41: "stated belief tracked content" → NARROW. Say "reported posteriors matched true posteriors in 23 tested cases."
- B42: "It was not merely stable while ignoring the task's quantities" → UNSUPPORTED. Delete.
- B48: "Specific outputs have different stability properties" → NARROW. Say "recorded outputs had different flip counts in this probe."
- B52: "The differences are substantial in these observations" → NARROW. Keep only with "in these observations… also confounded."
- B53: "Differences in difficulty could explain part or all of the pass-rate gap" → NARROW. Retain as possibility.
- B59: "The proxy results do not show an unchanged posterior paired with a changed terminal decision" → NARROW. Say "supplied proxy results do not report such a paired measurement."
- B73: "dirty repo alone does not establish any result is invalid" → NARROW. Say "repository was marked dirty."
- B78: "stated belief tracks content while decisions remain fragile" → NARROW. Replace with exact two-sample observations.
- B80: "real correctness reversals" → NARROW. Say "recorded correctness reversals."

PRODUCTION FIXES:
- Remove 👹 glyph → replace with [m-word] (both instances).
- B's "!" figure → new Figure 2 SVG (campaign denominators: 416→405 scored (277P/128F)+11 unscored; 416→189 BR+227 CO).
- Keep Figure 1 SVG from Draft A (3 endpoints, 0/5/17 bars).
- Keep [ac-word], [d-word], [m-word] tokens (intentional).

EDITORIAL CONFLICTS (packet vs blueprint) — CONSERVATIVE PATH (remove all three):
- "reasoning_effort=high" → remove (even though packet states it).
- "latent specification" → remove (even though packet states it).
- Game intervention types (evidence/presentation/prior) → remove (even though packet states them).
Rationale: none is load-bearing for the thesis; article is safer without them. If editor overrides, cite packet line.

CANDIDATE DRAFTS (verbatim):
[Both drafts are in campaign-02-analysis/comparison_7.md — gpt 6 sol max and gpt 6.1 sol max. Include both verbatim.]

TASK: Produce the FINAL article. Follow the blueprint structure (9 sections). Apply all mandatory deletions, required additions, narrow-claim qualifications, and production fixes. Use Draft A as base prose. Import B's table, "outputs not modules" header, "zero flips ≠ zero error" couplet, and titled coda. Include both figures (Figure 1 = three endpoints SVG, Figure 2 = campaign denominators SVG). Write in the author's voice (first person, "I"). Preserve [ac-word], [d-word], [m-word] tokens. Remove 👹 glyph.

Output the complete final article as a single markdown file with YAML front matter, ready to save as campaign-02-analysis/posts/POST-01-belief-right-decision-fragile.md.
