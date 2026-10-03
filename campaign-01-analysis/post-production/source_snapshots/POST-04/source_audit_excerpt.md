# Source implementation audit excerpt

## Scope and source identity

The campaign archive points to source commit `d7357092493f311f649a0742889b301d796911b5` and records the campaign repository as dirty. The inspected clean source snapshot has that commit identity; all 33 selected configuration SHA-256 values match the snapshot (`config_hash_audit.csv`). Because the execution records `repository.dirty=true` and the dirty diff/source tree is not part of the evidence ZIP, source statements below are verified against the clean comparator, not proven byte-for-byte statements about every paid run. The source audit does not modify or retroactively adjudicate the frozen Mission 01 or 04 records.

Line references below name paths relative to `rl_eval_generator@d7357092493f311f649a0742889b301d796911b5`. Exact hashes for the selected configuration files are in `config_hash_audit.csv`; the selected case IDs and final-run artifact paths are in `case_results.csv` and `trace_index.csv`.

## What the campaign actually sampled

The result archive covers 33 environments, with one selected run per selected case ID and `seed=0`. Most environments have five cases: an all-easy reference point plus one-factor substitutions for other levels; this permits small, local contrasts but not interactions or population-level estimates. Three recurrent-depth environments have 11 cases each; the `ts_*` trajectory family has three cases per environment; the epistemic task has seven. No environment-level run replicates are recorded. `axis_summary.csv` retains the values of all other axes for each contrast, so it is possible to see whether comparisons are genuinely held fixed.

The `easy`/`medium`/`hard` labels are not a common calibrated difficulty scale. Across tasks they refer to different quantities (names, input size, clue visibility, visible tests, prior, policy-likelihood regime, and judge checks). A reproducible static scan of axis placeholders against all selected environment `files/` templates is saved as `generated/axis_placeholder_audit.csv`. In the clean comparator, ten axis controls across nine category-track environments have no direct placeholder/literal-key reference in those environment files: `architecture_naturality.symptom_mask` (`CHECK_DIM`), `categorical_lenses.symptom_mask` (`STRICT_LAWS`), both `compositional_optimizer` axes (`MODEL_CLASS`, `LR_VAL`), `equivariant_diagram.symptom_mask` (`SYMMETRY_DIM`), `functorial_augmentation.symptom_mask` (`AUG_PARAM`), `monadic_reward.symptom_mask` (`SIDE_EFFECT_CHECK`), `neuro_symbolic_parser.symptom_mask` (`TOLERANCE`), `stochastic_monad.symptom_mask` (`SIGMA_VAL`), and `tokenizer_adjunction.symptom_mask` (`UNICODE_SUPPORT`). `MODEL_FILE` values also have no file-content reference, but remain constant across the levels checked here. This is a static source-template finding, not proof that unarchived dirty files were identical; it does mean that the inspected comparator does not support interpreting those levels as implemented perturbations. Several terminal failures are empty patches, syntax errors, or tool-action errors rather than evidence that a task's underlying mathematical content exceeded the model.

The recorded `ml_debugging` track includes seven `epistemic_games` cases. The latter's files implement a symbolic probability-inference task (`envs/epistemic_games/core.py`, `config.yaml`, and `judge.py`), so the analysis-family table separates these seven cases while preserving the raw label in the case table.

## Family summary, with raw track labels corrected only for analysis

All numbers below are reconstructed from the 194 selected rows. The analysis set excludes the two final results explicitly attributed to provider transients. Modes are the archive's per-case `judge_guarantee` labels, not a judgment that the judge has been independently validated.

| Analysis family | Recorded cases | Eligible cases | PASS | FAIL | Behavioral-reference rows | Compile-only rows | Source-grounded reading |
|---|---:|---:|---:|---:|---:|---:|---|
| `category_theoretic_compositional` | 85 | 84 | 57 | 27 | 5 | 79 | Mixed coding tasks; 79 eligible rows are compile-only |
| `epistemic_games` | 7 | 7 | 7 | 0 | 7 | 0 | Exact Bayesian calculation task as implemented in `core.py`; not recursive strategic ToM |
| `ml_debugging` (source-semantic regrouping) | 30 | 30 | 9 | 21 | 19 | 11 | `batchnorm_ema` 0/11, `glyph` 0/8, `moco` 9/11 |
| `recurrent_depth_behavioral` | 33 | 33 | 31 | 2 | 11 | 22 | `rd_state_carry` 11/11; `rd_gradient_credit` 11/11; `rd_adaptive_halting` 9/11 |
| `trajectory_solver_synthesis` | 9 | 8 | 2 | 6 | 0 | 8 | All eligible rows compile-only; the ninth row is provider-coded |
| `weird_machine` | 30 | 30 | 25 | 5 | 30 | 0 | Six code-repair environments; pass status is limited to each implemented judge |

The archived raw-track summary for `ml_debugging` is 37 cases, 16 PASS and 21 FAIL, because it includes the seven epistemic cases. Do not use that row as an ML-debugging result.

## Post and claim links

- POST-01: `axis_summary.csv`, `environment_summary.csv`, `analysis_family_summary.csv`, `case_results.csv`; findings F-01–F-06 and F-10–F-13.
- POST-02: epistemic case rows and final metrics in `case_results.csv`, `trace_index.csv`, and raw `episodes/<epistemic_case>/<final_run>/final.json`; source `core.py`, `renderer.py`, `config.yaml`, and `judge.py`; finding F-07.
- POST-03: `analysis_family_summary.csv`, category rows in `environment_summary.csv`/`case_results.csv`, `instance_oracles.json`, plus source paths above; findings F-08 and F-15.
- POST-04: `audit.json`, `failure_taxonomy.csv`, `failure_details.csv`, `campaign_exclusions.csv`, `case_results.csv`; findings F-02–F-05 and F-09/F-13.
- POST-05: `axis_summary.csv`, `case_results.csv`, `failure_details.csv`, `trace_index.csv`, and source configs/judges; findings F-06 and F-10/F-15.
