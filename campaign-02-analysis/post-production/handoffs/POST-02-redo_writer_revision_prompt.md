# POST-02 redo — Stage B2 Writer prompt (self-contained)

## Your task

Write one research article about the archived Mercury-2.5 evaluation campaign. The article is a revision of an earlier post. Its headline claim is the pooled pass rate, and it should show what that rate hides across environments. You receive every fact you need below. Do not assume anything about the campaign beyond these facts. Output only the article, as one Markdown document, with front matter. Do not include notes, commentary, or a list of changes.

## Non-negotiable rules

1. Analysis of archived results only. Do not suggest that any run was repeated or that new model runs were performed.
2. Mercury-2.5 is not Atria. Do not use numbers, labels, or conclusions from any other campaign.
3. Do not present this as preregistered. It is a retrospective analysis.
4. Public copy must not contain file paths, finding IDs (such as F-006), trace IDs, draft labels, or the words "packet", "evidence packet", "source analysis", "overview document", or "working notes".
5. Keep bracketed tokens exactly as written: [ac-word], [d-word], [m-word]. They are intentional replacements, not placeholders.
6. Every number must come from the facts below. State a limitation beside each claim it limits.
7. Do not describe any tuple-level pattern as a difficulty effect, a monotonic ladder, or a ranking. The evidence does not support those.

## Verified facts

**Campaign and selection**
- 416 selected cases in 38 environments. 405 scored: 277 PASS, 128 FAIL. 11 unscored (judge-coverage gap, not a third outcome).
- Scored pass rate: 277/405 = 68.4%. All-selected fraction 277/416 = 66.6% answers a different question and must be labelled as such.
- All 416 selected cases carry seed 0. No case was re-run under a second seed.
- Judge guarantees: 189 behavioral_reference, 227 compile_only (these totals include unscored cases).
- Omitted before scoring (outside the 416): 80 cases, namely 56 intervention-twin omissions, 14 known-gate calibration failures, 10 unsupported-input-modality cases (all in the `rope` environment). The provenance summary gives 24 known-gate omissions. This disagrees with the exclusion record's 14. State the disagreement; do not resolve it.
- 10 scored FAIL cases carry case_disposition `rejected`: 8 of the 9 scored `monadic_reward` cases, 1 `batchnorm_ema`, 1 `transformer_ssm_lift`. The archive does not define "rejected". Keep all 10 in the counts and say so beside the `monadic_reward` claim.
- One PASS, `ts_parse_only__witness_status=broken_representation=flat__seed-0`, is marked performance-ineligible. Its exclusion note describes a provider-attributed terminal failure while its verdict is PASS. Keep it in the 277 count and flag the inconsistency.

**Environment outcomes (environment-level, from the 38-row summary)**
- 17 environments: every scored case passed (172/172 total). Nine at 9/9: architecture_naturality, categorical_lenses, ci_dependency_graph, neuro_symbolic_parser, semiring_unification, spreadsheet_dataflow, stochastic_monad, template_interpreter, tokenizer_adjunction. Then css_state_machine 18/18; rd_gradient_credit 15/15; rd_state_carry 15/15; epistemic_games 23/23; epistemic_announcements 6/6; epistemic_nested_knowledge 6/6; epistemic_fragmented_observation 4/4; ts_parse_only 4/4.
- 7 environments: no scored case passed (0/68 total): functorial_augmentation 0/9, monadic_reward 0/9, sheaf_invariant_gluing 0/9, sheaf_physical_constraints 0/9, ts_one_step 0/4, ts_trajectory 0/4, glyph 0/24.
- 12 mixed environments (105/165 scored; one unscored case in rd_adaptive_halting): sheaf_schema_sync 8/9, sql_fixed_point 8/9, transformer_ssm_lift 8/9, compositional_optimizer 7/9, equivariant_diagram 7/9, tensor_functor 6/9, gnn_message_passing 5/9, regex_state_machine 5/9, ssm_parallel_scan 5/9, moco 36/55, rd_adaptive_halting 8/14 (plus 1 unscored), batchnorm_ema 2/15.
- 2 environments with no scored case: epistemic_silence (6 unscored), epistemic_type_games (4 unscored).
- 24 of the 36 environments with scored cases sit at an endpoint (all pass or all fail). Mixed environments hold 165 of the 405 scored cases (40.7%).

**The 340-row environment × difficulty-tuple matrix**
- 340 rows; 4 to 15 rows per environment; 6 environments have more than 10 rows.
- 34 difficulty dimension names. Tuples are environment-specific and must not be pooled, ranked, or regressed across environments.
- 296 rows are single-case. 44 rows are multi-case, all in four environments: moco (15 rows, 55 cases), glyph (12 rows, 24 cases), css_state_machine (9 rows, 18 cases), epistemic_games (8 rows, 23 cases).
- 329 rows carry a pass rate. Of these, 320 (97.3%) are exactly 0 or 1. Nine rows are fractional, all in moco.
- moco: 6 of its 15 rows sit at 0.0 or 1.0. The other 9 are fractional. Fractional values: 1/6, 1/3, 2/5, 2/3, 3/4, 5/6. No row-by-row key links each value to a tuple.
- 214 of 340 rows (63%) sit in environments where every row has the same outcome.
- 98 individual tuples have zero passes, in 19 environments.
- The "one seed per cell" wording is ambiguous. The row counts show a cell must mean an environment × tuple row, not a single case. This is an inference from the arithmetic, not a stated convention.

**Unscored cases (11)**
- epistemic_silence: 6. epistemic_type_games: 4. rd_adaptive_halting: 1, at the tuple where all five dimensions are `easy` (this tuple is identified in the matrix).

**Failure labels (global counts only; no environment breakdown is available)**
- underfit 51, overfit_visible_tests 49, runtime_error 11 (9 recorded as RUNTIME_ERROR plus 2 as runtime_error, consolidated), source_invalid 9, invalid_action 5, training_failed 3. Total 128.

**Ten-versus-seven discrepancy**
- A project overview document states 10 zero-pass environments. The environment-level count gives 7. A tuple-level explanation (environments with at least one zero-pass tuple) gives 19, so it does not reproduce 10. The origin of 10 is unexplained. Use 7 and state that the reconciliation is open.

**Claims withdrawn or open**
- Withdrawn: non-monotonic difficulty in css_state_machine. It is 18/18, so every tuple row is 2/2.
- Open, not findings: non-monotonic patterns in moco and in a SQL environment. Under a single-seed, mostly binary design such patterns may arise by chance. The base rate has not been computed.

**Source state**
- The campaign's source repository was recorded as dirty. The exact working-tree state [m-word] for reproduction, so the effect of uncommitted changes on any environment cannot be isolated.

## Structure (approximately 2,000–2,500 words)

1. Front matter: title, date 2026-10-16, layout post. Byline "by StrangeTcy".
2. Short epistemic-status block: original ideas, synthesis, prose, certainty, importance. Keep each entry to one sentence.
3. Short revision note: this replaces the earlier version, the headline stays, the tuple matrix is added as an exploratory second layer, and withdrawn claims are stated openly.
4. Opening: the 68.4% figure and why one pooled rate can hide the environment-level picture.
5. Counting scored cases: the outcome table (17 / 12 / 7 / 2) and the 277/405 vs 277/416 distinction.
6. The endpoint-heavy distribution, with the environment lists above.
7. Names as handles, not forecasts: the ts_* and sheaf_* examples, and glyph/moco/batchnorm_ema.
8. The 340-row matrix: what it adds, the binary and singleton facts, the 34 non-comparable dimensions, the 214 homogeneous rows, and the 98 zero-pass tuples in 19 environments.
9. The meaning of a cell (inference, stated as such).
10. moco as the only environment with fractional outcomes, with the limit that its shape cannot be drawn.
11. Claims withdrawn or left open (CSS withdrawn; MoCo and SQL open).
12. Unscored cases: the coverage gap, the rd_adaptive_halting tuple, and why they are not failures.
13. The 10-versus-7 discrepancy.
14. Failure labels and judge guarantees, global counts only, with the interpretive limits.
15. The selection frame: 80 omitted cases and the 14-vs-24 disagreement; the 10 rejected cases; the one performance-ineligible PASS.
16. Confounds: single seed, dirty source, selection.
17. What this supports, and what it does not show.
18. Figure: `../figures/fig2_environment_outcome_lollipop.svg` with alt text "Lollipop chart of pass rates by environment".

## Style

- First person, plain, exploratory, conservative. Short paragraphs, direct sentences.
- Tables where the data are tabular. Lists only where the content is a list.
- Do not use the words "bimodal" or "significant" unless you define them and show they apply.
- Do not claim that a pass means a model "understood" or "solved" anything. Describe what the judge checked.

## Output

One Markdown document. Front matter, then the article. Nothing before or after it.
