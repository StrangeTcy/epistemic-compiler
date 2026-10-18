# Evidence extract (POST-04)

- F-007: Failure modes dominated by underfit and visible-test overfit. Of 128 FAIL verdicts: 51 underfit, 49 overfit_visible_tests, 11 runtime_error, 9 source_invalid, 5 invalid_action, 3 training_failure.
- F-002: Proxy-channel interventions sharply reduce pass rates. visible_proxy 8/27 (0.30), reward_proxy 1/4 (0.25) vs base 228/331 (0.69). 7 pass->fail flips within 76 shared latent specs.
- F-009: Proxy interventions reduce pass rates (same as F-002, restated).
- F-005: 11 unscored cases (6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting). 56 of 132 twin cases unverified.
- Failure taxonomy: failure_mode_normalized, count, share_of_eligible_failures, case_ids, judge_guarantees.
- Overfit cases: several have trusted_score 1.0 but marked failed because required companion file missing.
- Proxy interventions: visible_proxy cases pass at 0.30, reward_proxy at 0.25.
- Failure conditions: proxy channels, visible-test-heavy grading, multi-file edits, companion files.
- Success conditions: single-file specifications, exact oracles.
