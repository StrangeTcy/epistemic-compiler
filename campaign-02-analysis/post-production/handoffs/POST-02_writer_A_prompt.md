BATTLE WRITER A — POST-02: Cross-environment outcome map (Mercury-2.5)

You are Writer A, an independent candidate producing a complete research essay for the StrangeTcy public site. You receive the evidence packet and reviewer brief below. Writer B will receive the same packet separately and must not see your draft.

ARTICLE SLOT: POST-02 — Cross-environment outcome map (primary comparative article).
RESEARCH QUESTION: How does Mercury-2.5's judged outcome vary across the 38 environments in this archived campaign, and how much does a single pooled pass rate conceal?

EVIDENCE PACKET (verified against reconstructed tables)

Environment outcomes (38 environments; 416 selected cases; 405 scored; 11 unscored):
- 17 perfect-pass (rate 1.0): architecture_naturality (9/9), categorical_lenses (9/9), ci_dependency_graph (9/9), css_state_machine (18/18), epistemic_announcements (6/6), epistemic_fragmented_observation (4/4), epistemic_games (23/23), epistemic_nested_knowledge (6/6), neuro_symbolic_parser (9/9), rd_gradient_credit (15/15), rd_state_carry (15/15), semiring_unification (9/9), spreadsheet_dataflow (9/9), stochastic_monad (9/9), template_interpreter (9/9), tokenizer_adjunction (9/9), ts_parse_only (4/4).
- 7 zero-pass (rate 0.0): functorial_augmentation (0/9), glyph (0/24), monadic_reward (0/9), sheaf_invariant_gluing (0/9), sheaf_physical_constraints (0/9), ts_one_step (0/4), ts_trajectory (0/4).
- 12 partial: batchnorm_ema 2/15 (0.133), compositional_optimizer 7/9 (0.778), equivariant_diagram 7/9 (0.778), gnn_message_passing 5/9 (0.556), moco 36/55 (0.655), rd_adaptive_halting 8/14 (0.571, +1 unscored), regex_state_machine 5/9 (0.556), sheaf_schema_sync 8/9 (0.889), sql_fixed_point 8/9 (0.889), ssm_parallel_scan 5/9 (0.556), tensor_functor 6/9 (0.667), transformer_ssm_lift 8/9 (0.889).
- 2 unscored-only: epistemic_silence (6 cases), epistemic_type_games (4 cases).
- Overall: 277 PASS / 128 FAIL / 11 unscored; scored pass rate 277/405 = 0.684; all-selected 277/416 = 0.666.
- Judge guarantees: 189 behavioral_reference, 227 compile_only (sum 416).
- Failure modes: underfit 51, overfit_visible_tests 49, RUNTIME_ERROR 9, source_invalid 9, invalid_action 5, training_failed 3, runtime_error 2 (sum 128).
- Cases vs tuples mismatch: css_state_machine 18 cases/9 tuples, epistemic_games 23/8, glyph 24/12, moco 55/15.
- Single seed per selected cell; source repo dirty at run time; 11 unscored cases (10 in two epistemic environments + 1 rd_adaptive_halting).
- Figures (7 SVGs in campaign-02-analysis/figures/): fig1 radial overview, fig2 lollipop, fig3 difficulty heatmap (6 envs), fig4 controlled single-axis transitions, fig5 failure modes, fig6 pairwise intervention, fig7 coverage. Embed via relative paths ../figures/figN_*.svg.

REVIEWER BRIEF (accepted Stage A) — key points to respect:
- The strongest thesis is NOT "bimodal capability" or "environment identity dominates difficulty labels." Those are too strong.
- Recommended framing: outcomes are endpoint-heavy and environment-conditioned; a single pooled rate conceals variation; family labels (ts_*, sheaf_*, CT-named) do NOT predict outcomes (ts_parse_only 4/4 vs ts_one_step/trajectory 0/4; sheaf_schema_sync 8/9 vs sheaf_invariant_gluing/physical_constraints 0/9).
- Confounds to address: judge-strength (behavioral vs compile_only) untested; harness failures in all-fail environments (RUNTIME_ERROR/source_invalid counts equal 9-case environment sizes); dirty source repo; single seed per cell; unequal case density (moco 55, glyph 24); unscored cases (11) must not be recoded as failures.
- The 12 partial environments hold 165/405 scored cases (40.7%) and span 0.133–0.889.
- "RUNTIME_ERROR" (9) vs "runtime_error" (2) casing is a data-quality flag, not two distinct modes.

STYLE REFERENCE
- Jekyll frontmatter: title, date, layout: post. No extra fields.
- Byline: *by <span class="icon-self">StrangeTcy</span>*
- Epistemic-status <dl> with five fields: Original ideas, Synthesis, Prose, Certainty, Importance.
- mathjax include if math used.
- First-person, curious, technically literate, self-correcting. Concrete cases, exact counts, caveats beside claims. No generic "environment matters more than difficulty" without supporting comparisons.
- Target ~1800-2800 words. Do not inflate.

TASK
Write a complete, independently structured research essay (not an outline, not a summary) for POST-02. Lead with a real question or tension. Explain concrete cases (ts_*, sheaf_*, glyph, moco, batchnorm_ema). Make quantitative structure inspectable (tables/figures). State exactly what the evidence establishes and what it cannot. Embed at least one figure with a caption. Place caveats where needed. Do not claim bimodality as a statistical fact; do not claim environment identity dominates difficulty (no shared difficulty scale exists). Do not imply internal mechanisms.

OUTPUT: the full article markdown only.
