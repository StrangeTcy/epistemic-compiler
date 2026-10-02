# Task, configuration, and judge implementation audit

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

## Source-specific findings relevant to the posts

### Epistemic games: exact Bayesian inference over stipulated policies

- `envs/epistemic_games/files/core.py:18–34` explicitly says v0 does not implement a fully recursive level-k engine with utilities and recursive belief updates. The behavioral policies are specified directly by `EVIDENCE_TABLE`; the code describes the task as Bayesian inference over two specified policies and warns that a pass is not evidence of three-level recursive reasoning.
- `core.py:38–51` defines the posterior from two likelihoods and priors, and likelihood-ratio labels for indistinguishable/weak/strong evidence. `core.py:89–122` provides the two priors, evidence tables, and presentation subfamilies. The selected cases use one seed and a seven-row one-factor design.
- `config.yaml:14–18` declares a no-provider `public_bayes_oracle` self-test. The archived `oracle_preflight.json` records that self-test passed for `epistemic_games`; the task's `judge.py:10–20` independently re-derives the case from its seed and scores a literal answer as data rather than executing it.
- The seven selected final results all report score 1.0, exact posterior credit, correct likelihood-ratio verdict, correct supported world, and all correctness checks true. The exact posterior fractions and case IDs are in their final result JSONs, linked from `case_results.csv`/`trace_index.csv`.

**Claim ceiling:** the model returned correct answers on these seven deterministic, specified-policy Bayesian items. It does not show recursively generated strategic reasoning, general theory of mind, or social behavior.

### Category-theoretic/compositional track: broad task names, uneven and mixed judges

- The 17 registered environments in this track span lens laws, optimizer modules, message passing, functorial data augmentation, state-space models, sheaf-inspired synchronization/routing, and other code repairs. They are not one homogeneous formal category-theory test. The generated environment table provides the full task-by-task outcome and mode split.
- `envs/cat_theo/categorical_lenses/files/prompt.md:5–14` states the three lens laws. `judge.py:32–60` samples one state and two values from a fixed seed and evaluates the laws; it does not directly assert that `view(s)` is coordinate zero. The agent-visible `files/visible_tests.py:3–5` does assert `view((1,2)) == 1.0`, so the intended first projection is visible even though the hidden judge's own law checks would admit alternate lawful projections. `config.yaml:15–23` declares a `symptom_mask` axis through `%%STRICT_LAWS%%`, but that placeholder is not referenced by the inspected prompt, judge, visible tests, or starter source: the judge always checks the same three laws. Therefore that axis does not implement its advertised masking perturbation in this comparator.
- `envs/cat_theo/compositional_optimizer/files/prompt.md:5–8` promises strict associativity under nested composition and numerical correctness across multiple training steps. `judge.py:40–58, 70–83` checks output shape and one two-module update chain against a state-isolation reference; it does not compare the two parenthesizations of a three-operation composition or a multi-step horizon. The visible test (`files/visible_tests.py:4–9`) is a single-step shape check. The `naming`/`MODEL_CLASS` placeholder and `symptom_mask`/`LR_VAL` placeholder are both absent from the inspected source templates; the starter code, visible test, and judge instead name `MomentumStep` directly. Neither advertised axis changes the task/judge in this comparator. The five archived rows (3 PASS/2 FAIL) are therefore not five levels of an associativity manipulation; under the clean snapshot they are repeated runs against the same task template, with failures including an empty patch and a disallowed `weakref` import.
- `envs/cat_theo/sheaf/sheaf_physical_constraints/files/prompt.md:5–11` requires capacity-safe routing but does not state the judge's 5:3 proportionality target. `judge.py:45–68` checks a 5:3 ratio on one fixed high-demand vector; lines 72–100 add fixed local/global constraints and symmetry checks. The visible test (`files/visible_tests.py:3–8`) checks output keys/shape, not the ratio. The `GLOBAL_CAP` substitution changes a hidden judge constructor/check value, while the prompt leaves the numerical global cap unspecified. This is a task/judge specification mismatch, not evidence of an internal sheaf contradiction.
- The archive records category-family results as 57/85 before exclusions, 57/84 after excluding the provider-coded physical-constraints row; the eligible mode split is 4/5 PASS in `categorical_lenses` (`behavioral_reference`) and 53/79 PASS in the rest of the eligible compile-only cases. `sheaf_physical_constraints` has 0/4 eligible cases; the fifth final row is provider-coded. Several other tasks include empty-patch or source-validation failures, not direct tests of category-theoretic reasoning.

**Claim ceiling:** these are source-grounded code-repair outcomes under heterogeneous implementations. Do not describe 57/84 as a validated category-theory capability score or as a measurement of a sheaf theorem.

### Nominal axes with no source-template reference in the category comparator

The static scan's no-reference results are easiest to interpret alongside their selected-case outcomes. They are not causal comparisons for those controls. The `axis_placeholder_audit.csv` rows list config path, source revision, placeholder, and any environment-template references.

| Environment | No-reference control | Selected rows | PASS/FAIL in primary set | Boundary |
|---|---|---:|---:|---|
| `architecture_naturality` | `symptom_mask` / `CHECK_DIM` | 5 | 5 / 0 | Compile-only; dimension control has no direct source-template reference |
| `categorical_lenses` | `symptom_mask` / `STRICT_LAWS` | 5 | 4 / 1 | Hidden judge always checks the laws; the advertised mask has no direct reference |
| `compositional_optimizer` | `naming` / `MODEL_CLASS`; `symptom_mask` / `LR_VAL` | 5 | 3 / 2 | Both controls are unreferenced; judge and visible test use `MomentumStep` |
| `equivariant_diagram` | `symptom_mask` / `SYMMETRY_DIM` | 5 | 5 / 0 | Compile-only; no direct source-template reference |
| `functorial_augmentation` | `symptom_mask` / `AUG_PARAM` | 5 | 2 / 3 | Compile-only; no direct source-template reference |
| `monadic_reward` | `symptom_mask` / `SIDE_EFFECT_CHECK` | 5 | 1 / 4 | Compile-only; no direct source-template reference |
| `neuro_symbolic_parser` | `symptom_mask` / `TOLERANCE` | 5 | 4 / 1 | Compile-only; no direct source-template reference |
| `stochastic_monad` | `symptom_mask` / `SIGMA_VAL` | 5 | 5 / 0 | Compile-only; no direct source-template reference |
| `tokenizer_adjunction` | `symptom_mask` / `UNICODE_SUPPORT` | 5 | 5 / 0 | Compile-only; no direct source-template reference |

This does not imply that all other axes are clean causal controls: class-name variants can change prompt cues, task-size parameters can change multiple properties, and the archive has no per-cell replication. It establishes a narrower point: the listed values do not appear in any of the clean comparator's environment files, so no task/judge alteration can be attributed to those values from that source snapshot. Exact executed-source identity remains unresolved because the campaign recorded a dirty repository.

### Weird-machine tasks: a controlled but one-case-per-cell pilot

The relevant configs are under `envs/weird_machine/`:

- `regex_state_machine/config.yaml:2–26` maps the surface label to class names (`RegexAutomaton`, `PatternTransducer`, `StringValidator`) and changes the hard prompt with an extra performance comment. Its `hidden_depth` values actually set input-string length to 32/128/512. The task asks for one Rule 110 cellular-automaton update using regex (`files/prompt.md:7–25`). The judge uses four equal boolean checks (regex mechanism/no explicit string loops, one basic known input, length preservation, and exact equality on 15 seeded strings; `files/judge.py:34–68, 71–113, 132–156`). At surface `easy`, all three lengths pass. At fixed easy length, the easy class passes and medium/hard classes fail with output lengths 34 and 66 for input length 32 (`failure_details.csv`). The medium/hard class names and hard performance hint are confounded with the purported surface-deception manipulation.
- `css_state_machine/config.yaml:2–23` uses class names to reframe a parity-selector task and changes number of input bits from 3 to 4 to 5; these are size/complexity changes, not hidden recursive depth. In its five selected one-factor cases, the all-easy case is partial (`0.416667`), the easy-surface/medium-size result is source-invalid (disallowed `re` import), the easy-surface/hard-size result passes, and the two non-easy surface labels at easy size pass. The nonmonotone pattern is real in the archived cases, but one point is a source-validator failure.
- `sql_fixed_point/config.yaml:2–23` changes class name and graph-chain length (6/12/25). The easy-size surface sweep passes for all three names; the medium chain-length case is `source_invalid` due an unterminated triple-quoted string; easy and hard lengths pass.
- `spreadsheet_dataflow/config.yaml:2–23` changes the class name and grid length 8/15/30. All five selected cases pass.
- `ci_dependency_graph` and `template_interpreter` also have 5/5 passing selected cases. Across the six five-case environments in this track, 25/30 selected rows pass.

`case_results.csv`, `axis_summary.csv`, `failure_details.csv`, and the source configs/judges establish these cells. Because each cell has one seed-0 run and multiple axes use class names or extra hints, the observed contrast is a pilot response pattern—not causal proof that deceptive surface form, hidden depth, or a general computational substrate drove the output.

### Recurrent depth and task/code errors

- `rd_adaptive_halting/config.yaml` maps recurrence-depth easy/medium/hard to train/hidden depths 4/8, 16/32, and 32/64. The one-factor selected recurrence-depth cases are easy `source_invalid` (unexpected indentation), medium PASS, and hard PASS. At the all-easy point, the failure is source syntax; a separate medium implementation-obfuscation case fails at runtime because `torch.where` receives a float condition. It would be invalid to say that easy recurrence is harder than deep recurrence based on those three terminal labels.
- `rd_gradient_credit` is 11/11 PASS but all compile-only in the archived guarantee field. `rd_state_carry` is 11/11 PASS and all behavioral-reference. Across the family, the 31/33 result therefore mixes validation modes and includes syntax/runtime failures; the depth axis does not isolate a general recurrence law.

### ML-debugging task outputs and failure-label checks

- After separating the epistemic label, `batchnorm_ema` records 0/11 PASS, `glyph` 0/8, and `moco` 9/11. The `batchnorm_ema` cases are compile-only; glyph/MoCo are behavioral-reference cases under the per-instance campaign label.
- All 8 `glyph` and 9 `batchnorm_ema` `patch_invalid` rows have archived final notes `Patch file is empty`. Across all environments, all 24 eligible `patch_invalid` rows have the same empty-patch note.
- The two rows labeled `overfit_visible_tests` instead have `trusted_score=1.0` plus notes that a required cross-context file was missing (`train.py` for one BatchNorm row; `moco_model.py` for one MoCo row). The label therefore should not be presented as observed test overfitting without further audit.
- All 10 `source_invalid` rows are source validator outcomes (syntax failures or disallowed imports). The `failure_details.csv` records each exact case and final note. This is distinct from an algorithmic test failure.

## Post and claim links

- POST-01: `axis_summary.csv`, `environment_summary.csv`, `analysis_family_summary.csv`, `case_results.csv`; findings F-01–F-06 and F-10–F-13.
- POST-02: epistemic case rows and final metrics in `case_results.csv`, `trace_index.csv`, and raw `episodes/<epistemic_case>/<final_run>/final.json`; source `core.py`, `renderer.py`, `config.yaml`, and `judge.py`; finding F-07.
- POST-03: `analysis_family_summary.csv`, category rows in `environment_summary.csv`/`case_results.csv`, `instance_oracles.json`, plus source paths above; findings F-08 and F-15.
- POST-04: `audit.json`, `failure_taxonomy.csv`, `failure_details.csv`, `campaign_exclusions.csv`, `case_results.csv`; findings F-02–F-05 and F-09/F-13.
- POST-05: `axis_summary.csv`, `case_results.csv`, `failure_details.csv`, `trace_index.csv`, and source configs/judges; findings F-06 and F-10/F-15.
