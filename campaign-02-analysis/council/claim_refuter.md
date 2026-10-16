# Claim Refuter (Mercury)

## F-006 (bimodal difficulty)
- Claim: "7 environments score 0.00, 17 score 1.00, 2 unscored, 12 partial."
- Evidence: environment_summary_v2.csv (recomputed from case_results.csv).
- Counterevidence: none; counts reconcile. But "bimodal" is an interpretation; 12 partial environments break strict bimodality.
- Verdict: narrow — state counts exactly; avoid "bimodal" as a statistical claim.

## F-008 (non-monotonic transitions)
- Claim: MoCo/CSS/SQL show non-monotonic outcomes.
- Evidence: case_results.csv single cells.
- Counterevidence: single seed per cell; no replication; labels change different task properties.
- Verdict: narrow — describe as observed single-seed pattern, not established transition.

## F-009 (proxy interventions)
- Claim: visible_proxy 0.30, reward_proxy 0.25 vs base 0.69.
- Evidence: case_results.csv.
- Counterevidence: intervention cases not difficulty-matched; small denominators (4 reward_proxy).
- Verdict: narrow — observed association, not causal.

## F-001 (belief/decision dissociation)
- Claim: 0/36 belief flips, 5/36 terminal flips.
- Evidence: t1_same_fact_presentation.json.
- Counterevidence: 36 pairs; terminal extraction may be brittle; single model.
- Verdict: survives as observed pattern, scope narrowed to single model/probe.
