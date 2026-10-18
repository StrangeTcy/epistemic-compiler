# POST-02 Source Snapshot — Evidence Extract

## Difficulty Matrix (340 rows)
- File: campaign-02-analysis/evidence/generated2/environment_difficulty_matrix.csv
- 340 rows (environment × difficulty_tuple), 38 environments
- Fields: environment, difficulty_tuple, n_cases, n_scored, n_unscored, n_pass, n_fail, pass_rate, failure_modes, judge_guarantees
- 296 rows have n_cases=1; 44 rows have n_cases>1 (up to 6)
- 329 rows have pass_rate; 11 rows unscored (all n_unscored>0)
- 34 unique difficulty tuple keys across all environments
- Min rows per env: 4; Max: 15
- 6 environments have >10 rows: batchnorm_ema (15), glyph (12), moco (15), rd_adaptive_halting (15), rd_gradient_credit (15), rd_state_carry (15)

## Campaign Totals (F-004)
- 416 selected, 405 scored, 277 PASS, 128 FAIL, 0.684
- 38 environments

## Findings
- F-001 through F-009 (see findings/findings.json)
- F-006: Bimodal environment difficulty (6 named zero-rate + 1 unscored)
- F-007: Failure modes (51 underfit, 49 overfit, 11 runtime, 9 source_invalid, 5 invalid_action, 3 training)
- F-008: Non-monotonic difficulty transitions (MoCo, CSS, SQL)

## Key Observations from Matrix
- 296/340 rows have exactly 1 case (n_cases=1)
- 44/340 rows have multiple cases (n_cases 2-6)
- pass_rate values are discrete: 0.0, 0.167, 0.333, 0.4, 0.667, 0.75, 0.833, 1.0
- 11 unscored rows (all n_unscored > 0, total 11 unscored cases)
- Difficulty axes differ per environment (34 unique keys)
- Some environments have multiple cases per tuple (moco: 55 cases / 15 tuples)
