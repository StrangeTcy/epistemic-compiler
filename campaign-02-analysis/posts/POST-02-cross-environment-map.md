---
title: "Mercury-2.5 Across 38 Environments: A Bimodal Capability Map"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The cross-environment structure and the claim that environment identity dominates difficulty labels.</dd>
  <dt>Synthesis</dt>
  <dd>Role-separated analysis over the archived Mercury evidence; final writer reconciled contested claims.</dd>
  <dt>Prose</dt>
  <dd>Final-writer draft; independent battle drafts pending manual execution.</dd>
  <dt>Certainty</dt>
  <dd>Observed on one model/provider; mixed judge guarantees; one seed per cell.</dd>
  <dt>Importance</dt>
  <dd>Shows that aggregate pass rates hide a sharp environment split.</dd>
</dl>

Mercury-2.5 does not have one difficulty. Across 38 environments and 405 scored cases, its overall pass rate is 0.684, but that average conceals a sharp split: seven environments score 0.00, seventeen score 1.00, two are entirely unscored, and twelve are partial. The environment matters more than any difficulty label.

![Radial environment overview](../figures/fig1_radial_environment_overview.svg)

*Figure 1. Radial overview of all 38 environments by pass rate (green = perfect, red = zero, amber = partial, grey = unscored only). Spoke length encodes pass rate; labels include scored denominators. Not a calibrated capability scale.*

The seven zero-pass environments are glyph, functorial_augmentation, monadic_reward, sheaf_invariant_gluing, sheaf_physical_constraints, ts_one_step, and ts_trajectory. The seventeen perfect-pass environments include categorical_lenses, ci_dependency_graph, css_state_machine, epistemic_games, rd_gradient_credit, rd_state_carry, semiring_unification, spreadsheet_dataflow, stochastic_monad, template_interpreter, tokenizer_adjunction, ts_parse_only, neuro_symbolic_parser, epistemic_announcements, epistemic_fragmented_observation, epistemic_nested_knowledge, and architecture_naturality. Two environments — epistemic_silence and epistemic_type_games — have no scored cases at all (11 infrastructure-unscored cases total).

This is not a ranking of reasoning ability. The environments differ in task type, judge guarantee (189 behavioral-reference, 227 compile-only), and scoring. What the split shows is that Mercury's competence is sharply environment-dependent: some task families are reliably solvable, others reliably not, with little middle ground.

![Environment outcome lollipop](../figures/fig2_environment_outcome_lollipop.svg)

*Figure 2. Per-environment pass proportions with exact numerators and denominators.*

The failure modes reinforce this. Of 128 FAIL verdicts, 51 are underfit and 49 are overfit_visible_tests. Source-invalid (9), runtime errors (11), invalid actions (5), and training failures (3) are the minority. The dominant failures are not crashes but partial solutions and visible-test gaming — a behavioural signature, not an infrastructure one.

The implication for evaluation: report per-environment and per-judge-guarantee, never a single score. A 0.684 average is accurate and misleading at the same time.

Caveats: single model and provider; mixed judge guarantees; one seed per cell; source repository dirty at run time; no replication.
