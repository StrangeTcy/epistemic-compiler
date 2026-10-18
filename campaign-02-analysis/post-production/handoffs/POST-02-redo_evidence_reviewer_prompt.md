BATTLE ARENA EVIDENCE REVIEWER — POST-02 REDO: Difficulty-Tuple Analysis (Mercury-2.5)

You are an independent Evidence Reviewer. Your job is to challenge a proposed POST-02 redo that shifts from environment-level aggregates to difficulty-tuple-level analysis, using the verified evidence packet below. The original POST-02 focused on 38 environments and their pooled pass rates. The redo should analyse the 340-row environment × difficulty-tuple matrix instead. Produce a substantive adversarial brief.

EVIDENCE PACKET (verified ground truth):
- Difficulty matrix: 340 rows (environment × difficulty_tuple), 38 environments, 34 unique difficulty keys.
- Fields per row: environment, difficulty_tuple, n_cases, n_scored, n_unscored, n_pass, n_fail, pass_rate, failure_modes, judge_guarantees.
- 296 rows have n_cases=1; 44 rows have n_cases>1 (up to 6). Total cases = 416 (sum of n_cases).
- 329 rows have pass_rate; 11 rows unscored (n_unscored>0, total 11).
- pass_rate values are discrete: 0.0, 0.167, 0.333, 0.4, 0.667, 0.75, 0.833, 1.0.
- Min rows per env: 4; Max: 15. 6 environments have >10 rows.
- F-004: 416 selected, 405 scored, 277 PASS, 128 FAIL, 0.684. 38 environments.
- F-006: Bimodal environment difficulty. 6 named zero-rate + 1 unscored. Pass rates 0.00 to 1.00.
- F-007: Failure modes: 51 underfit, 49 overfit_visible_tests, 11 runtime_error, 9 source_invalid, 5 invalid_action, 3 training_failure = 128.
- F-008: Non-monotonic difficulty transitions (MoCo, CSS, SQL).
- Judge guarantees: 189 behavioral_reference, 227 compile_only = 416 selected.
- Single model/provider (mercury-2.5). Single seed per selected cell. Dirty repo. No replication.
- Difficulty axes differ across environments: 34 unique keys (naming, symptom_mask, hidden_depth, surface_deceptiveness, etc.).
- Some environments have multiple cases per tuple (moco: 55 cases / 15 tuples; css_state_machine: 18 cases / 9 tuples).

ORIGINAL POST-02 (to be replaced):
- Title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
- Focused on environment-level aggregates: 17 environments at 1.0, 7 at 0.0, 12 partial.
- Identified as missing the difficulty-tuple analysis per ANALYSIS_OVERVIEW.md.
- Deferred redo per user choice.

ANALYSIS_OVERVIEW.md discrepancy: States 10 zero-pass environments; evidence shows 7. Needs reconciliation.

TASK: Produce an adversarial evidence review for the proposed redo. Challenge:
1. Whether the difficulty matrix (340 rows) supports stronger claims than environment aggregates, or just more granular noise.
2. Whether "one seed per cell" is accurate given 44 rows with n_cases>1.
3. Whether the 34 unique difficulty keys can be compared across environments (they measure different things).
4. Whether pass_rate on n_cases=1 rows is meaningful (binary outcome, not a rate).
5. Whether the redo can claim "difficulty effects" when no replication exists.
6. Whether the 11 unscored rows (all with n_unscored>0) introduce selection bias.
7. Whether the redo should retain the environment-level findings (17 at 1.0, 7 at 0.0) or replace them entirely.
8. Whether the ANALYSIS_OVERVIEW.md 10-vs-7 zero-pass discrepancy needs resolution before writing.

IMPORTANT: Bracketed tokens such as [ac-word], [d-word], [m-word] are INTENTIONAL replacements for words the author dislikes. They are NOT production artifacts. Do not flag them for removal.
