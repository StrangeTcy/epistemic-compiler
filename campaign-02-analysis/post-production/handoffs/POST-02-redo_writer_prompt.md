BATTLE WRITER — POST-02 REDO: What a 68.4% Pass Rate Hides (Mercury-2.5)

You are an independent candidate producing a complete research essay for the StrangeTcy public site. This is a REDO of POST-02, which originally focused on environment-level aggregates. The redo should use the 340-row difficulty-tuple matrix as an exploratory layer while retaining the environment-level findings as the primary structure.

EVIDENCE PACKET (verified ground truth):
- Difficulty matrix: 340 rows (environment × difficulty_tuple), 38 environments, 34 unique difficulty keys.
- 296 rows have n_cases=1; 44 rows have n_cases>1 (up to 6). Total cases = 416.
- 329 rows have pass_rate; 11 rows unscored (n_unscored>0, total 11).
- pass_rate values: 0.0, 0.167, 0.333, 0.4, 0.667, 0.75, 0.833, 1.0.
- Min rows per env: 4; Max: 15. 6 environments have >10 rows.
- F-004: 416 selected, 405 scored, 277 PASS, 128 FAIL, 0.684. 38 environments.
- F-006: Bimodal environment difficulty. 6 named zero-rate + 1 unscored. Pass rates 0.00 to 1.00.
- F-007: Failure modes: 51 underfit, 49 overfit_visible_tests, 11 runtime_error, 9 source_invalid, 5 invalid_action, 3 training_failure = 128.
- F-008: Non-monotonic difficulty transitions (MoCo, CSS, SQL). NOTE: CSS claim is arithmetically impossible (css_state_machine is 18/18). Must reconcile.
- Judge guarantees: 189 behavioral_reference, 227 compile_only = 416 selected.
- Single model/provider (mercury-2.5). Single seed per selected cell. Dirty repo. No replication.
- 44 multi-case rows confined to 4 environments: moco (15 rows/55 cases), css (9/18), glyph (12/24), epistemic_games (8/23). Sum = 44 rows, 120 cases, surplus = 76.
- 95.4% of rows (314/329) have binary pass_rate (0 or 1). Only moco produces intermediate values.
- 63% of rows (214/340) carry zero within-environment information (constant within environment).
- 11 unscored rows: 6 epistemic_silence (all rows), 4 epistemic_type_games (all rows), 1 rd_adaptive_halting (single row).
- F-009 restates F-002 (not replication).
- ANALYSIS_OVERVIEW.md says 10 zero-pass environments; evidence shows 7. Discrepancy unresolved.

EVIDENCE REVIEWER BRIEF (Stage A — blocking issues):
1. The 340-row matrix does NOT support stronger claims than environment aggregates. Mostly more granular noise. 296/340 singletons. Moving from 36 aggregates (median n=9) to 329 outcomes (median n=1) is a move DOWN the information ladder.
2. "One seed per cell" is ambiguous. 44 rows have n_cases>1. Two readings (cell=case vs cell=env×tuple) lead to opposite conclusions. Must state which is supported or say unknown.
3. 34 difficulty keys are incommensurable. Cross-env pooling/ranking/regression invalid. 12 separate within-environment descriptive maps only.
4. pass_rate on n_cases=1 rows is binary, not a rate. ≥314/329 rows have pass_rate ∈ {0,1}. Rename to "outcome" or report as fraction strings. No continuous-axis plots for single-case rows.
5. "Difficulty effects" not claimable without replication. Non-monotonicity is null expectation under single-seed binary outcomes (only 2.4% of 3×3 grids monotone in both axes). F-008 CSS claim arithmetically impossible.
6. 11 unscored rows = non-random missingness. 6 all rows of epistemic_silence, 4 all rows of epistemic_type_games, 1 single row of rd_adaptive_halting. Judge-coverage gap, not model result. Must describe, not drop.
7. RETAIN environment-level findings. 63% of rows carry zero within-environment information. Hybrid structure: env-level headline + cross-tabs + within-partial descriptive maps.
8. 10-vs-7 discrepancy is GATING. Must resolve before writing.

RECOMMENDED STRUCTURE (from Stage A):
1. Keep environment-level table and endpoint-heavy map as headline.
2. Add two cross-tabs: (a) environment × failure-mode, (b) environment × judge-guarantee.
3. For 12 partial environments only: within-environment tuple map as descriptive table on own axes, binary outcomes as ✓/✗ not decimals.
4. For moco only: 15 multi-case tuples as fractions (after resolving cell/case/seed semantics).
5. Title should remain "What a 68.4% Pass Rate Hides" — not "difficulty tuples."

GATING ITEMS (must resolve before writing):
1. Cell/case/seed semantics for moco's multi-case tuples.
2. 10-vs-7 zero-pass discrepancy.
3. F-008's CSS claim vs css_state_machine 18/18.
4. Unscored rd_adaptive_halting tuple identification.

ORIGINAL POST-02 (to be replaced, not patched):
[See campaign-02-analysis/posts/POST-02-cross-environment-map.md — 92 lines, ~3,000 words]

HOUSE STYLE: See campaign-02-analysis/post-production/source_snapshots/shared/house_style.md and style_reference_material.md.

TASK: Produce a complete, publication-ready essay. The reviewer's blocking issues must be addressed, not ignored. Key reframing requirements:
- Retain environment-level findings as primary structure (17 at 1.0, 7 at 0.0, 12 partial, 2 unscored).
- Add tuple matrix as exploratory layer, NOT replacement.
- Use "observed pass fraction on this cell's cases" terminology, never unqualified "difficulty effect."
- No cross-key comparison or pooled difficulty model.
- No "rate" language for single-case rows.
- Include failure_modes cross-tab and judge_guarantees cross-tab if computable from matrix.
- Handle 11 unscored rows as judge-coverage gap, not model result.
- Resolve or explicitly flag the 10-vs-7 discrepancy.
- Resolve or explicitly flag F-008's CSS claim.
- Resolve or explicitly flag cell/case/seed semantics.
- Every number must be traceable. Include appropriate caveats.

IMPORTANT: Bracketed tokens such as [ac-word], [d-word], [m-word] are INTENTIONAL replacements for words the author dislikes. They are NOT production artifacts. Do not flag them for removal.

Output the complete article as a single markdown file with YAML front matter, ready to save as campaign-02-analysis/posts/POST-02-cross-environment-map.md.
