BATTLE WRITER — POST-03: Where Mercury Breaks: Non-Monotonic Difficulty Transitions (Mercury-2.5)

You are an independent candidate producing a complete research essay for the StrangeTcy public site. You receive the evidence packet, the evidence reviewer's adversarial brief, and the existing draft stub below. Produce a complete, publication-ready essay.

EVIDENCE PACKET (verified ground truth):
- F-008: Non-monotonic difficulty transitions. Several environments show non-monotonic outcomes across difficulty levels: MoCo visible-test levels yield pass/fail/pass; CSS state machine easy-surface cases over 3/4/5 bits yield partial score/source-validation failure/pass; SQL fixed points pass at graph-chain lengths 6 and 25 but fail source validation at length 12.
- F-006: Bimodal environment difficulty. 7 environments score 0.00 (glyph, functorial_augmentation, monadic_reward, sheaf_invariant, ts_one_step, ts_trajectory, epistemic_silence/type_games unscored). Pass rates range 0.00 to 1.00. (Count discrepancy: 6 named + 1 unscored = 7 claimed.)
- F-004: Overall campaign 416 selected, 405 scored, 277 PASS, 128 FAIL, 0.684. 38 environments.
- Environment difficulty matrix: 340 rows (environment x difficulty_tuple), n_cases/n_scored/n_pass/n_fail/pass_rate/failure_modes/judge_guarantees.
- Single seed per selected cell (seed-0). Dirty repo. No replication.
- Difficulty axes differ across environments: MoCo visible-test level changes test coverage; CSS surface labels change class names and bit counts; SQL changes graph-chain length; regex changes input-string length (32/128/512).

EVIDENCE REVIEWER BRIEF (Stage A — blocking issues):
1. NULL HYPOTHESIS: At campaign pass rate 0.684, ~21.6% of three-level sweeps produce non-monotonic patterns by chance. Three out of ~40 eligible triples is below the noise floor. The headline finding must be reframed as methodological, not empirical.
2. SELECTION EFFECT: No enumeration procedure stated. How were the three triples selected from 340 matrix rows?
3. SOURCE-VALIDATION FAILURES: Two of three showcase cases (CSS 4-bit, SQL-12) are source-validation failures, not task failures. The truncation/length hypothesis must be addressed.
4. CAUSAL OVERREACH: "The reason is that difficulty changes different things" is a non sequitur. Cross-environment heterogeneity doesn't explain within-environment non-monotonicity.
5. LATENT DIFFICULTY: "Manipulation is not isolating a single latent difficulty" is unsupported for n=1 binary outcomes.
6. FACTUAL ERRORS: Regex pass claim unsupported; "easy-surface" qualifier on SQL unsupported; CSS axis mis-described; "hardest label" framing conflates axes; "partial score" unreconciled with binary accounting; F-006 count discrepancy.
7. MISSING CAVEATS: Bimodality context, 11 unscored cases as MNAR, dirty-repo implication, judge-guarantee confound, sparse SQL sampling, model/harness provenance.

EXISTING DRAFT STUB (to be replaced, not patched):
[The existing stub from campaign-02-analysis/posts/POST-03-difficulty-transitions.md]

HOUSE STYLE: See campaign-02-analysis/post-production/source_snapshots/shared/house_style.md and style_reference_material.md.

TASK: Produce a complete, publication-ready essay. The reviewer's blocking issues must be addressed, not ignored. The thesis must be reframed: the real finding is that difficulty labels are not a validated ordinal scale, that axes mean different things in different environments, and that one seed per cell buys no power to detect a threshold. The three recorded non-monotonic sequences should be reported as observations, not as evidence of a difficulty curve. Every number must be traceable to the evidence packet. Include appropriate caveats in the same sentence as qualified claims.

IMPORTANT: Bracketed tokens such as [ac-word], [d-word], [m-word] are INTENTIONAL replacements for words the author dislikes. They are NOT production artifacts. Do not flag them for removal.

Output the complete article as a single markdown file with YAML front matter, ready to save as campaign-02-analysis/posts/POST-03-difficulty-transitions.md.
