BATTLE ARENA EVIDENCE REVIEWER — POST-03: Where Mercury Breaks: Non-Monotonic Difficulty Transitions (Mercury-2.5)

You are an independent Evidence Reviewer. Your job is to challenge the existing draft for POST-03 against the verified evidence packet below. Produce a substantive adversarial brief that identifies overclaims, unsupported inferences, missing caveats, and factual errors.

EVIDENCE PACKET (verified ground truth):
- F-008: Non-monotonic difficulty transitions. Several environments show non-monotonic outcomes across difficulty levels: MoCo visible-test levels yield pass/fail/pass; CSS state machine easy-surface cases over 3/4/5 bits yield partial score/source-validation failure/pass; SQL fixed points pass at graph-chain lengths 6 and 25 but fail source validation at length 12.
- F-006: Bimodal environment difficulty. 7 environments score 0.00 (glyph, functorial_augmentation, monadic_reward, sheaf_invariant, ts_one_step, ts_trajectory, epistemic_silence/type_games unscored). Pass rates range 0.00 to 1.00.
- F-004: Overall campaign 416 selected, 405 scored, 277 PASS, 128 FAIL, 0.684. 38 environments.
- Environment difficulty matrix: 340 rows (environment x difficulty_tuple), n_cases/n_scored/n_pass/n_fail/pass_rate/failure_modes/judge_guarantees.
- Single seed per selected cell (seed-0). Dirty repo. No replication.
- Difficulty axes differ across environments: MoCo visible-test level changes test coverage; CSS surface labels change class names and bit counts; SQL changes graph-chain length; regex changes input-string length (32/128/512).

EXISTING DRAFT (POST-03 stub):
---
title: "Where Mercury Breaks: Non-Monotonic Difficulty Transitions"
...
Difficulty labels are not a staircase. In several Mercury environments, the outcome across difficulty levels is non-monotonic: the middle level is harder than both ends, or the hardest label passes while an easier one fails.

In MoCo, visible-test levels yield pass, fail, pass. In CSS state machines, easy-surface cases over 3, 4, and 5 bits yield a partial score, a source-validation failure, and a pass. In SQL fixed points, easy-surface cases pass at graph-chain lengths 6 and 25 but fail source validation at length 12. These are not smooth degradations; they are qualitatively different failure layers at adjacent levels.

The reason is that "difficulty" changes different things in different environments. In regex state machines, hidden depth means input-string length (32, 128, 512 characters) and the model passes all three at the easy surface label. In MoCo, visible-test level changes test coverage. In CSS and SQL, surface labels change class names and graph sizes. The labels are not commensurable across environments, and sometimes not within one.

This matters for two reasons. First, a non-monotonic result is a signal that the manipulation is not isolating a single latent difficulty — it is changing the task. Second, single-seed cells cannot distinguish a real transition from noise. The campaign records one seed-0 run per selected cell, so every transition claim is provisional.

The strongest defensible statement: in this archived run, several environments show non-monotonic outcomes across their difficulty axes, and the axes themselves change different task properties. Whether those are real thresholds or seed-specific accidents requires replication.

Caveats: single seed per cell; dirty source repository; mixed judge guarantees.
---

TASK: Produce an adversarial evidence review. Challenge every claim in the draft. Identify overclaims, unsupported inferences, missing caveats, and factual errors. Be specific about which evidence supports or contradicts each claim. Note any numbers that need verification. Flag any causal inference that outruns the evidence.

IMPORTANT: Bracketed tokens such as [ac-word], [d-word], [m-word] are INTENTIONAL replacements for words the author dislikes. They are NOT production artifacts. Do not flag them for removal.
