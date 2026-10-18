# POST-02 redo — Stage B2 (Writer revision) prompt

You are the Writer for a research post on the archived Mercury-2.5 campaign. Write one complete article in Markdown. Output only the article: front matter, byline, epistemic-status block, body, and an optional image link. No notes, reviewer commentary, change logs, or metadata outside the article.

## 1. Task

Revise the cross-environment map article so it matches the verified facts in section 3 and fixes the errors in section 4. Keep the environment table as the headline. Treat the 340-row environment × difficulty-tuple matrix as a second, exploratory layer, not a replacement for the headline.

## 2. Scope and standing rules

- Analysis of archived evidence only. No new runs, no provider calls, no claim that any run was repeated.
- Mercury-2.5 is the subject. Do not import denominators, exclusions, categories, or conclusions from any Atria campaign. Atria posts are method precedent only.
- Do not describe any plan as preregistration.
- Public copy must not contain internal file paths, finding IDs (F-###), trace IDs, draft labels, or the words "packet", "evidence packet", "source analysis", "overview document", or "working notes".
- Bracketed tokens such as [ac-word], [d-word], [m-word] are intentional replacements. Keep them exactly as they appear in the instructions below; do not expand, remove, or flag them.
- Every number and strong factual claim must be traceable to a figure in section 3. Put the limitation beside the claim it qualifies.
- Do not state any number that is not in section 3. If a figure you want is missing, leave the claim out.

## 3. Verified facts (use these; they were recomputed from the archived tables)

Headline counts (from the case-level table):
- 416 selected cases in 38 environments.
- 405 scored; 277 PASS, 128 FAIL; 11 unscored (judge-coverage gap, not a third outcome).
- Scored pass rate 277/405 = 68.4%. The fraction 277/416 = 66.6% answers a different question (share of all selected cases with a PASS) and must be labelled as such.

Environment outcomes (38 environments):
- 17 environments: every scored case passed (172/172).
- 12 environments: mixed (105/165 scored; 1 unscored).
- 7 environments: every scored case failed (0/68).
- 2 environments: no scored cases (10 unscored: `epistemic_silence` 6, `epistemic_type_games` 4).

Perfect-pass environments and their counts: 9/9 in `architecture_naturality`, `categorical_lenses`, `ci_dependency_graph`, `neuro_symbolic_parser`, `semiring_unification`, `spreadsheet_dataflow`, `stochastic_monad`, `template_interpreter`, `tokenizer_adjunction`; 18/18 `css_state_machine`; 15/15 `rd_gradient_credit`, `rd_state_carry`; 23/23 `epistemic_games`; 6/6 `epistemic_announcements`, `epistemic_nested_knowledge`; 4/4 `epistemic_fragmented_observation`, `ts_parse_only`.

Zero-pass environments (7): `functorial_augmentation` 0/9, `monadic_reward` 0/9, `sheaf_invariant_gluing` 0/9, `sheaf_physical_constraints` 0/9, `ts_one_step` 0/4, `ts_trajectory` 0/4, `glyph` 0/24.

Mixed environments with counts: `sheaf_schema_sync` 8/9, `sql_fixed_point` 8/9, `transformer_ssm_lift` 8/9; `compositional_optimizer` 7/9, `equivariant_diagram` 7/9; `tensor_functor` 6/9; `gnn_message_passing` 5/9, `regex_state_machine` 5/9, `ssm_parallel_scan` 5/9; `moco` 36/55; `rd_adaptive_halting` 8/14 scored (1 unscored); `batchnorm_ema` 2/15.

Outcome spread: 24 of 36 scored environments sit at an endpoint (all pass or all fail). The 12 mixed environments hold 165 of 405 scored cases (40.7%).

340-row matrix (one row per environment × difficulty-tuple):
- 340 rows; 4–15 rows per environment; 6 environments have more than 10 rows.
- 296 rows have exactly one case; 44 rows have 2–6 cases.
- The 44 multi-case rows lie in exactly four environments: `moco` 15 rows (55 cases), `glyph` 12 rows (24 cases), `css_state_machine` 9 rows (18 cases), `epistemic_games` 8 rows (23 cases). Those totals equal each environment's full case count.
- 329 rows carry a pass rate. 320 (97.3%) take exactly 0 or 1. The 9 non-binary rows are all in `moco`.
- 214 of 340 rows (63%) sit in environments where every row has the same outcome.
- 34 difficulty dimension names occur across the matrix. Tuples are environment-specific and must not be pooled, ranked, or regressed across environments.
- 98 individual tuples have zero passes, spread over 19 environments.

`moco` detail: 15 rows, 36/55 PASS (65.5%). Six rows are at 0.0 or 1.0 (for example 3/3 and 2/0). Nine rows are fractional, with values 1/6, 1/3, 2/5, 2/3, 3/4, 5/6. The archive does not give a row-by-row key linking each fraction to a tuple; do not draw a shape.

`css_state_machine` detail: 18/18 PASS across 9 tuple rows, each 2/2.

Unscored rows (11): `epistemic_silence` 6 rows; `epistemic_type_games` 4 rows; `rd_adaptive_halting` 1 row. The `rd_adaptive_halting` unscored tuple is `{"batching_complexity": "easy", "clue_clarity": "easy", "implementation_obfuscation": "easy", "recurrence_depth": "easy", "visible_tests": "easy"}`. Its scored total 8/14 is unchanged.

Failure labels (global counts only; no environment breakdown is available): `underfit` 51; `overfit_visible_tests` 49; `runtime_error` 11 (9 `RUNTIME_ERROR` and 2 `runtime_error` consolidated); `source_invalid` 9; `invalid_action` 5; `training_failed` 3. Total 128.

Judge guarantees (global counts only): 189 `behavioral_reference`; 227 `compile_only`. A behavioral PASS and a compile-only PASS are different claims.

Selection frame (outside the 416 selected cases):
- 80 cases were omitted before scoring: 56 intervention-twin omissions; 14 known-gate calibration failures; 10 unsupported provider input-modality cases (all in `rope`). Per exclusion-record row, by environment: `moco` 35, `glyph` 21, `rope` 15, `epistemic_games` 9. All 80 rows lie outside the 416 selected cases.
- Discrepancy, unresolved: the provenance summary gives 24 known-gate omissions and 10 `rope` omissions. The exclusion record gives 14 and 10. State that the figures differ and that the origin is unresolved. Use the exclusion-record figure and say which one it is.
- 10 scored FAIL cases carry the `rejected` disposition: `monadic_reward` 8 (of its 9 scored cases), `batchnorm_ema` 1, `transformer_ssm_lift` 1. The archive does not define "rejected". Keep all 10 in the counts. State beside the `monadic_reward` zero-pass result that 8 of its 9 scored cases carry this disposition.
- One PASS, `ts_parse_only__witness_status=broken_representation=flat__seed-0`, is marked performance-ineligible. Its exclusion note describes a provider-attributed terminal failure, but its verdict is PASS. Keep it in the 277 count. Flag the inconsistency; do not resolve it.

Other limitations to state where relevant:
- Every case carries seed 0. Each selected case was run once. No variance or stability estimate exists at either environment or tuple level.
- The campaign's source repository was recorded as dirty. The exact working-tree state [m-word] for reproduction; the effect cannot be isolated.
- The archive supplies no definition of "cell". The row-level arithmetic indicates an environment × tuple row. State this as an inference.

10-versus-7 zero-pass environments:
- The case-level count supports 7 (listed above).
- An overview document states 10. Adding the two fully unscored environments gives 9, and they are a coverage gap, not zero-pass results.
- The tuple-level explanation was tested: counting environments with at least one zero-pass tuple gives 19, not 10. The origin of 10 is unexplained.
- Use 7 throughout. Say the figure of 10 is not reproduced and its origin is open.

## 4. Errors that must not appear in the output

1. "314 of 329" or "95.4%" for binary rows. Correct: 320 of 329, 97.3%.
2. "Every moco row is mixed" or "all 15 non-binary rows". Correct: 9 non-binary rows, all in `moco`; 6 `moco` rows sit at 0.0 or 1.0.
3. Any claim that the 10 zero-pass environments come from a tuple-level count. Correct: that count gives 19.
4. Any claim that the `rd_adaptive_halting` unscored tuple cannot be identified. Correct: it is identified (section 3).
5. Any non-monotonic claim for `css_state_machine`. It is withdrawn: 18/18 forces every row to 2/2.
6. Any "difficulty effect", monotone ladder, or ranking of difficulty labels. Not supported.
7. Any failure-by-environment cross-tabulation or judge-by-environment cross-tabulation. Not available; state that the archive gives global counts only.
8. Any figure, simulation result, or base rate not in section 3. Do not invent a chance-monotone base rate; if relevant, say it has not been computed.
9. Any mention of Atria figures or a comparison to another campaign.

## 5. Structure (target 2,000–2,500 words)

1. Front matter: title "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"; date 2026-10-16; layout post.
2. Byline: *by StrangeTcy*.
3. Epistemic-status block with five entries (Original ideas, Synthesis, Prose, Certainty, Importance). Describe the work without referring to any "packet".
4. A short revision note stating that the article replaces the 2026-10-16 version, that the tuple matrix was added as a second layer, and that claims which did not survive the cross-check are corrected or withdrawn in the open. No finding IDs.
5. Body sections, in this order:
   a. Counting cases with a judgment (headline table: environment outcome × environments × PASS/scored × share × unscored).
   b. The endpoint-heavy distribution (perfect-pass list; zero-pass list with the `monadic_reward` caveat; mixed list).
   c. Names as handles, not forecasts.
   d. The 340-row matrix: what it adds and what it does not (singletons, binary share, 34 dimension names, 214 homogeneous rows, 98 zero-pass tuples).
   e. What "cell" means here (inference, with limitation).
   f. `moco`: the only fractional environment.
   g. Two difficulty claims that do not hold up (CSS withdrawn; MoCo and SQL open, no effect language).
   h. Judge-coverage gap: 11 unscored, including the identified `rd_adaptive_halting` tuple.
   i. The 10-versus-7 discrepancy.
   j. Failure labels (global counts only).
   k. Judge guarantees (global counts only).
   l. The selection frame and its disclosures (80 omitted; known-gate discrepancy; 10 `rejected`; one performance-ineligible PASS).
   m. Confounds (single seed, dirty source, selection).
   n. What the post supports (short).
   o. Figure: `![Lollipop chart of pass rates by environment](../figures/fig2_environment_outcome_lollipop.svg)`.
   p. What the post does not show.

## 6. Tone

First-person, plain, exploratory and conservative. Short declarative sentences where a claim is firm; explicit hedges where it is not. No hype, no rhetorical flourish, no "the packet says". Name the limitation in the same paragraph as the claim.

## 7. Output checklist (verify before returning)

- [ ] Every number appears in section 3.
- [ ] 320/329 and 97.3% (not 314 or 95.4%).
- [ ] 7 zero-pass environments, with the 10 figure described as unexplained.
- [ ] `rd_adaptive_halting` unscored tuple given.
- [ ] CSS claim withdrawn.
- [ ] No Atria figures; no cross-campaign comparison.
- [ ] No forbidden words from section 2.
- [ ] [m-word] kept as written.
- [ ] Figure link present.
- [ ] Output is the article only.
