# Evidence extract (POST-03)

- F-008: Non-monotonic difficulty transitions. Several environments show non-monotonic outcomes across difficulty levels: MoCo visible-test levels yield pass/fail/pass; CSS state machine easy-surface cases over 3/4/5 bits yield partial score/source-validation failure/pass; SQL fixed points pass at graph-chain lengths 6 and 25 but fail source validation at length 12.
- F-006: Bimodal environment difficulty. 7 environments score 0.00 (glyph, functorial_augmentation, monadic_reward, sheaf_invariant, ts_one_step, ts_trajectory, epistemic_silence/type_games unscored). Pass rates range 0.00 to 1.00.
- F-004: Overall campaign 416 selected, 405 scored, 277 PASS, 128 FAIL, 0.684. 38 environments.
- Environment difficulty matrix: 340 rows (environment x difficulty_tuple), n_cases/n_scored/n_pass/n_fail/pass_rate/failure_modes/judge_guarantees.
- Single seed per selected cell (seed-0). Dirty repo. No replication.
- Difficulty axes differ across environments: MoCo visible-test level changes test coverage; CSS surface labels change class names and bit counts; SQL changes graph-chain length; regex changes input-string length (32/128/512).
