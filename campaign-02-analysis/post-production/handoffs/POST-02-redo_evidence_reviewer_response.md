# Stage A — Evidence Reviewer Response (POST-02 Redo)

Source: Battle Arena, pasted by user 2026-10-17. Output from grok 4.5 and fable 5.1 (plus sonnet 5 echoing the prompt). Preserved in campaign-02-analysis/comparison_21.md (417 lines, 53 KB).

Prompt artifact: campaign-02-analysis/post-production/handoffs/POST-02-redo_evidence_reviewer_prompt.md

Status: ACCEPTED as Stage A (Evidence Reviewer). Two independent model outputs (grok 4.5, fable 5.1).

KEY FINDINGS (both reviewers agree):

1. GRANULAR NOISE, NOT STRONGER CLAIMS: The 340-row matrix does not support stronger claims than environment aggregates. 296/340 rows are singletons (n_cases=1). Moving from 36 aggregates (median n=9) to 329 outcomes (median n=1) is a move DOWN the information ladder. The matrix adds resolution, not reliability.

2. "ONE SEED PER CELL" IS AMBIGUOUS: 44 rows have n_cases>1 (up to 6). Two readings: (a) cell=case (different instances, each run once — no replication), or (b) cell=env×tuple (multi-case rows contradict "one seed per cell" — and if they're seed replicates, moco contains the only replication data in the campaign). The packet does not resolve this. Must state which reading is supported or say it's unknown.

3. 34 DIFFICULTY KEYS ARE INCOMMENSURABLE: Environment-specific design axes with no shared scale. Cross-env pooling/ranking/regression on "difficulty" is invalid. 12 separate within-environment descriptive maps only.

4. PASS_RATE ON N=1 ROWS IS BINARY: ≥314 of 329 scored rows have pass_rate ∈ {0, 1}. Calling it a "rate" invites ratio-scale thinking. Rename to "outcome" for n=1 rows or report as fraction strings.

5. "DIFFICULTY EFFECTS" NOT CLAIMABLE: No replication. Non-monotonicity is the null expectation under single-seed binary outcomes (only 2.4% of 3×3 grids are monotone in both axes). F-008's CSS claim is arithmetically impossible (css_state_machine is 18/18, all pass). Must reconcile before citing.

6. 11 UNSCORED ROWS = NON-RANDOM MISSINGNESS: 6 are ALL rows of epistemic_silence, 4 are ALL rows of epistemic_type_games, 1 is a single row of rd_adaptive_halting. This is a judge-coverage gap, not random noise. Must describe, not drop. The rd_adaptive_halting unscored tuple must be identified (right-censoring risk).

7. RETAIN ENVIRONMENT-LEVEL FINDINGS: 63% of rows (214/340) carry zero within-environment information (constant within environment). The tuple matrix is the sufficient statistic for these. Replace environment aggregates with tuple matrix = downgrade. Hybrid structure: env-level headline + cross-tabs + within-partial descriptive maps.

8. 10-VS-7 DISCREPANCY IS GATING: Must resolve before writing. 7 all-fail + 2 fully-unscored = 9, not 10. No obvious reconciliation produces 10. Could be stale snapshot, different definition, or error.

ADDITIONAL FINDINGS:
- 44 multi-case rows confined to 4 environments: moco (15 rows/55 cases), css (9/18), glyph (12/24), epistemic_games (8/23). Sum = 44 rows, 120 cases, surplus = 76 = 416-340.
- 95.4% of rows (314/329) have binary pass_rate (0 or 1). Only moco produces intermediate values.
- 63% of rows (214/340) carry zero within-environment information.
- The matrix's genuine value: (a) failure_modes cross-tab (env × failure mode), (b) judge_guarantees cross-tab (env × guarantee), (c) within-partial-environment descriptive maps.
- F-006 discrepancy: "6 named zero-rate + 1 unscored" doesn't match 7 all-fail + 2 fully-unscored.
- F-007 vs original post: runtime_error 11 vs 9+2 casing split; totals reconcile.
- No 0.5 in discrete values (no 2-case row split 1/1, no 4-case row 2/4, no 6-case row 3/6) — possibly coincidence or uneven tuple sizes.
- Non-monotonicity is null expectation under single-seed binary outcomes (only 2.4% of 3×3 grids are monotone in both axes).
- css_state_machine is 18/18 — F-008's CSS claim is arithmetically impossible on stated data.
- sql_fixed_point is 8/9 — "non-monotonic" means one binary failure on a non-hardest tuple.
- The 10-vs-7 discrepancy: no obvious reconciliation produces 10 (7 all-fail; 7+2 unscored=9; +batchnorm_ema near-zero=10 only by redefining "zero").
- Gating items before any draft: (1) resolve cell/case/seed semantics for moco, (2) reconcile 10-vs-7, (3) reconcile F-008's CSS claim, (4) identify unscored rd_adaptive_halting tuple.

RECOMMENDED DISPOSITION:
- Do NOT green-light a pure replacement redo. The 340-row matrix is a valid exploratory layer for within-environment description (especially partials, dense envs, F-008 non-monotonics) but does not support stronger claims, cross-env difficulty science, or effect language.
- Require hybrid structure: env-level headline + cross-tabs + within-partial descriptive maps.
- Mandate pre-write reconciliation of 10-vs-7 and precise single-seed/multi-case language.
- Enforce terminology discipline: "observed pass fraction on this cell's cases," never unqualified "difficulty effect" or cross-key comparison.
- Success criterion: Readers should finish knowing exactly what additional descriptive resolution the tuples provide and exactly why it does not overcome the packet's fundamental limits.

Full verbatim text in campaign-02-analysis/comparison_21.md.
