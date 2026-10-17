EVIDENCE REVIEWER — POST-02: Cross-environment outcome map (Mercury-2.5)

You are the Evidence Reviewer for a research essay about Mercury-2.5's behaviour across environments and difficulty tuples in the archived Mercury campaign.

Your job is to produce an evidence-led editorial brief, NOT a finished article. Challenge the existing draft; do not validate it by default.

INPUTS
- Campaign: Mercury pairwise-state, model mercury-2.5, reasoning_effort=high, provider mercury.
- Archive: mercury-pairwise-state-38873207827.zip (SHA-256 ece98bcf1cfd53dd24625c43da5e647aa63a5fac645603976c1213bdbd9af389), 5129 members.
- Reconstructed evidence: campaign-02-analysis/evidence/generated/ and generated2/.
- Findings register: campaign-02-analysis/findings/findings.json (F-001..F-009).
- Figures: campaign-02-analysis/figures/ (7 SVGs, see README).
- Style reference: StrangeTcy house style (Jekyll, layout: post, byline, epistemic-status dl).
- Reference essay: "A Category-Theory Label Is Not a Category-Theory Measurement" (strangetcy.github.io).

ENVIRONMENT SUMMARY (38 environments; 416 selected cases; 405 scored; 11 unscored)
architecture_naturality: cases=9 scored=9 pass=9 fail=0 rate=1.0 tuples=9
batchnorm_ema: cases=15 scored=15 pass=2 fail=13 rate=0.13333333333333333 tuples=15
categorical_lenses: cases=9 scored=9 pass=9 fail=0 rate=1.0 tuples=9
ci_dependency_graph: cases=9 scored=9 pass=9 fail=0 rate=1.0 tuples=9
compositional_optimizer: cases=9 scored=9 pass=7 fail=2 rate=0.7777777777777778 tuples=9
css_state_machine: cases=18 scored=18 pass=18 fail=0 rate=1.0 tuples=9
epistemic_announcements: cases=6 scored=6 pass=6 fail=0 rate=1.0 tuples=6
epistemic_fragmented_observation: cases=4 scored=4 pass=4 fail=0 rate=1.0 tuples=4
epistemic_games: cases=23 scored=23 pass=23 fail=0 rate=1.0 tuples=8
epistemic_nested_knowledge: cases=6 scored=6 pass=6 fail=0 rate=1.0 tuples=6
epistemic_silence: cases=6 scored=0 pass=0 fail=0 rate=NA (unscored) tuples=6
epistemic_type_games: cases=4 scored=0 pass=0 fail=0 rate=NA (unscored) tuples=4
equivariant_diagram: cases=9 scored=9 pass=7 fail=2 rate=0.7777777777777778 tuples=9
functorial_augmentation: cases=9 scored=9 pass=0 fail=9 rate=0.0 tuples=9
glyph: cases=24 scored=24 pass=0 fail=24 rate=0.0 tuples=12
gnn_message_passing: cases=9 scored=9 pass=5 fail=4 rate=0.5555555555555556 tuples=9
moco: cases=55 scored=55 pass=36 fail=19 rate=0.6545454545454545 tuples=15
monadic_reward: cases=9 scored=9 pass=0 fail=9 rate=0.0 tuples=9
neuro_symbolic_parser: cases=9 scored=9 pass=9 fail=0 rate=1.0 tuples=9
rd_adaptive_halting: cases=15 scored=14 pass=8 fail=6 rate=0.5714285714285714 tuples=15
rd_gradient_credit: cases=15 scored=15 pass=15 fail=0 rate=1.0 tuples=15
rd_state_carry: cases=15 scored=15 pass=15 fail=0 rate=1.0 tuples=15
regex_state_machine: cases=9 scored=9 pass=5 fail=4 rate=0.5555555555555556 tuples=9
semiring_unification: cases=9 scored=9 pass=9 fail=0 rate=1.0 tuples=9
sheaf_invariant_gluing: cases=9 scored=9 pass=0 fail=9 rate=0.0 tuples=9
sheaf_physical_constraints: cases=9 scored=9 pass=0 fail=9 rate=0.0 tuples=9
sheaf_schema_sync: cases=9 scored=9 pass=8 fail=1 rate=0.8888888888888888 tuples=9
spreadsheet_dataflow: cases=9 scored=9 pass=9 fail=0 rate=1.0 tuples=9
sql_fixed_point: cases=9 scored=9 pass=8 fail=1 rate=0.8888888888888888 tuples=9
ssm_parallel_scan: cases=9 scored=9 pass=5 fail=4 rate=0.5555555555555556 tuples=9
stochastic_monad: cases=9 scored=9 pass=9 fail=0 rate=1.0 tuples=9
template_interpreter: cases=9 scored=9 pass=9 fail=0 rate=1.0 tuples=9
tensor_functor: cases=9 scored=9 pass=6 fail=3 rate=0.6666666666666666 tuples=9
tokenizer_adjunction: cases=9 scored=9 pass=9 fail=0 rate=1.0 tuples=9
transformer_ssm_lift: cases=9 scored=9 pass=8 fail=1 rate=0.8888888888888888 tuples=9
ts_one_step: cases=4 scored=4 pass=0 fail=4 rate=0.0 tuples=4
ts_parse_only: cases=4 scored=4 pass=4 fail=0 rate=1.0 tuples=4
ts_trajectory: cases=4 scored=4 pass=0 fail=4 rate=0.0 tuples=4

FAILURE MODES (128 FAIL verdicts)
underfit: 51
overfit_visible_tests: 49
RUNTIME_ERROR: 9
source_invalid: 9
invalid_action: 5
training_failed: 3
runtime_error: 2

KEY FACTS
- 7 zero-pass environments: functorial_augmentation, glyph, monadic_reward, sheaf_invariant_gluing, sheaf_physical_constraints, ts_one_step, ts_trajectory.
- 17 perfect-pass environments (listed above).
- 2 unscored-only: epistemic_silence (6 cases), epistemic_type_games (4 cases); plus 1 unscored rd_adaptive_halting case.
- 12 partial-pass environments.
- Judge guarantees: 189 behavioral_reference, 227 compile_only.
- Overall: 277 PASS / 128 FAIL / 11 unscored among 416 selected.
- Difficulty is multidimensional and environment-specific; one seed per selected cell; source repo dirty at run time.

EXISTING DRAFT (to challenge, not validate)
Title: "Mercury-2.5 Across 38 Environments: A Bimodal Capability Map"
Current thesis: environment identity dominates difficulty labels; 0.684 average conceals sharp split.

REQUIRED OUTPUT FORMAT
Produce a structured evidence-led brief with these sections:
1. Empirical question the post can answer.
2. Strongest candidate thesis and competing interpretations.
3. Precise observations and comparisons supporting it (with exact counts/denominators).
4. Cases and tuple dimensions that matter (name specific environments and axes).
5. Strongest counterexamples and known confounds.
6. Which visualisations make the evidence easier to understand (reference the 7 figures).
7. Boundaries between observation, interpretation, and hypothesis.
8. Claims that are NOT currently defensible.

Be adversarial: challenge the existing draft's thesis, its "bimodal" framing, and any claim that environment identity alone explains outcomes. Identify what the evidence cannot support.
