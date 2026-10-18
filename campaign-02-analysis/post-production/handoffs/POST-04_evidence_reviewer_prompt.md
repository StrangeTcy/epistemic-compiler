BATTLE ARENA EVIDENCE REVIEWER — POST-04: How Mercury Fails: Recurring Failure Modes and Their Conditions (Mercury-2.5)

You are an independent Evidence Reviewer. Your job is to challenge the existing draft for POST-04 against the verified evidence packet below. Produce a substantive adversarial brief that identifies overclaims, unsupported inferences, missing caveats, and factual errors.

EVIDENCE PACKET (verified ground truth):
- F-007: Failure modes dominated by underfit and visible-test overfit. Of 128 FAIL verdicts: 51 underfit, 49 overfit_visible_tests, 11 runtime_error, 9 source_invalid, 5 invalid_action, 3 training_failure. (51+49+11+9+5+3 = 128.)
- F-002: Proxy-channel interventions sharply reduce pass rates. visible_proxy 8/27 (0.30), reward_proxy 1/4 (0.25) vs base 228/331 (0.69). 7 pass->fail flips within 76 shared latent specs.
- F-009: Proxy interventions reduce pass rates (same as F-002, restated).
- F-005: 11 unscored cases (6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting). 56 of 132 twin cases unverified.
- Failure taxonomy: failure_mode_normalized, count, share_of_eligible_failures, case_ids, judge_guarantees.
- Overfit cases: several have trusted_score 1.0 but marked failed because required companion file missing (e.g., batchnorm_ema missing model.py).
- Proxy interventions: visible_proxy cases pass at 0.30, reward_proxy at 0.25.
- Failure conditions: proxy channels, visible-test-heavy grading, multi-file edits, companion files.
- Success conditions: single-file specifications, exact oracles.
- Judge guarantees: 189 behavioral_reference, 227 compile_only = 416 selected.
- Single model/provider (mercury-2.5). Single seed per cell. Dirty repo. No replication.

EXISTING DRAFT (POST-04 stub):
---
title: "How Mercury Fails: Recurring Failure Modes and Their Conditions"
...
Mercury's failures are mostly behavioural, not infrastructural. Of 128 FAIL verdicts, 100 are either underfit (51) or overfit_visible_tests (49). Source-invalid (9), runtime errors (11), invalid actions (5), and training failures (3) are the minority. The model usually produces a patch that runs; it just does not solve the task.

The two dominant modes have different signatures. Underfit cases produce partial solutions — the code runs but misses hidden checks. Overfit-visible-tests cases pass the visible tests but fail hidden ones; several of these have a trusted score of 1.0 yet are marked failed because a required companion file is missing. The label "overfit" is therefore not direct evidence of visible-test gaming in every case.

Proxy interventions make the failure mode sharper. Cases that introduce a visible-proxy channel pass at 0.30 (8 of 27) and a reward-proxy channel at 0.25 (1 of 4), against a 0.69 base pass rate. Within paired groups sharing a latent specification, seven interventions flipped a passing base case to a failure. The proxy channel appears to offer a shortcut that the model takes.

The conditions under which failures appear are therefore: proxy channels, visible-test-heavy grading, and environments where the task requires multi-file edits or companion files. The conditions under which they disappear: environments with clear single-file specifications and exact oracles.

Caveats: judge-assigned labels; intervention cases not difficulty-matched; single model.
---

TASK: Produce an adversarial evidence review. Challenge every claim in the draft. Identify overclaims, unsupported inferences, missing caveats, and factual errors. Be specific about which evidence supports or contradicts each claim. Note any numbers that need verification. Flag any causal inference that outruns the evidence. Pay particular attention to:
1. Whether "behavioural, not infrastructural" is supported (runtime errors are 11/128 = 8.6%, which is not negligible).
2. Whether "the model usually produces a patch that runs" is supported.
3. Whether "the proxy channel appears to offer a shortcut that the model takes" is a causal claim beyond the evidence.
4. Whether "conditions under which failures disappear" is supported (no evidence for single-file specifications leading to success).

IMPORTANT: Bracketed tokens such as [ac-word], [d-word], [m-word] are INTENTIONAL replacements for words the author dislikes. They are NOT production artifacts. Do not flag them for removal.
