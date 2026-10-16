# Mercury-2.5 cross-environment difficulty analysis — overview

Primary question: How does Mercury-2.5's behaviour vary across environments and difficulty tuples?

## Dimensions
- 38 environments, 340 distinct environment × difficulty-tuple rows, 416 selected cases (405 scored, 11 unscored).
- Difficulty is multi-dimensional per environment (e.g. naming × symptom_mask; hidden_depth × surface_deceptiveness); not a single scalar.
- Outcomes: PASS/FAIL/unscored, failure_mode, score, plus epistemic-game posterior/verdict.

## Key patterns
1. Bimodal environment difficulty: 10 environments at 0.00 pass rate (glyph, functorial_augmentation, monadic_reward, sheaf_*, ts_one_step, ts_trajectory) vs ~12 at 1.00.
2. Failure modes: underfit (51) and overfit_visible_tests (49) dominate; source_invalid (9), runtime (11), invalid_action (5), training_failed (3).
3. Difficulty transitions are non-monotonic in several environments (e.g. MoCo visible-test levels pass/fail/pass).
4. Proxy interventions (visible_proxy, reward_proxy) cut pass rates to 0.30/0.25.
5. Belief computation exact (23/23) while decisions fragile — supporting diagnostic, not headline.

## Visualisations
- environment_difficulty_matrix.csv (340 rows)
- environment_summary_v2.csv (38 rows)
