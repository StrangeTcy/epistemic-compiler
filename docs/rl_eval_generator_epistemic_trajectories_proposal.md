# `rl_eval_generator`: Epistemic Trajectories Implementation Proposal

**Status:** proposed, unverified, and not authorized as an implementation plan. This note concerns the separate `rl_eval_generator` project—not the `epistemic-compiler` repository that contains this document. No target-repository code was inspected or changed for this note.

The implementation suggestions originated in §4 of [`epistemic_games_genre_v5_02_evaluation_experiment_proposals.md`](../mission-02/sources/epistemic_games_genre_v5_02_evaluation_experiment_proposals.md), which now points to the extracted evaluation design and this proposal. The implementation details remain separate from the evaluation-design draft in [`epistemic_trajectories.md`](epistemic_trajectories.md).

## Proposal from the source passage

If the evaluation is approved and the target repository supports it, add an interactive track—illustratively, a module such as `arena/epistemic_trajectories/` and a corresponding `arena.py` command. These are proposed paths, not confirmed existing files or supported commands.

The proposed state machine uses constrained actions such as:

- `present` — emit an engine-validated presentation;
- `inspect(test_id)` — request an available diagnostic test;
- `final(decision)` — submit a terminal decision.

Ground truth, allowed presentation transforms, test outcomes, and scoring remain in trusted engine code. Each episode records the condition, presented fact IDs, inspection actions, returned observations, final decision, and enough seed/configuration data to replay the score.

## Reuse candidates, not verified repository facts

The source passage suggests reusing provider adapters, event-artifact conventions, seed discipline, and deterministic generation. It also says the existing generator has seeded substitution and an opt-in deterministic renderer. These are **claims to verify in the actual `rl_eval_generator` checkout** before designing against them. They are not claims about `epistemic-compiler`.

## Gate before implementation

1. Inspect the actual `rl_eval_generator` repository and record its revision, CLI entry points, provider interfaces, artifact formats, and seed/rendering behavior.
2. Confirm the interactive episode semantics and oracle independently of any model-generated messages.
3. Map the proposed actions and event record to the target repository’s existing abstractions; do not add a configuration subtype and assume that this makes the current runner interactive.
4. Specify and test the condition invariants, replay behavior, validation failures, and scoring before making any model calls.

Until those checks are done, this file is an implementation hypothesis only. It does not establish that the proposed directory or command exists, and it does not authorize code changes or model review.
