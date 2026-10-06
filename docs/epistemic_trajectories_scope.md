# Epistemic Trajectories — Scope and Status

## Status

`epistemic_trajectories` is a **proposed working name** for a possible evaluation track. It is not yet an approved project rename, implemented benchmark, run experiment, or result. The proposal is to continue alongside `epistemic_games`, not replace or rename it. Separately, the broader sequence from deception through belief manipulation to epistemic-process manipulation has been provisionally adopted as a testable organizing hypothesis in the [evaluation-proposal record](../mission-02/sources/epistemic_games_genre_v5_02_evaluation_experiment_proposals.md). That hypothesis does not validate an ordering or replace the 15-question portfolio.

The source proposal describes `epistemic_games` as a static belief-inference task and says a multi-turn presenter/defender experiment would require additional interaction machinery. Those are claims from the dialogue; they have not been verified against the separate `rl_eval_generator` repository in this checkout. This `docs/` directory is new in `epistemic-compiler`; the local `rl_eval_generator/` directory is empty. Treat this note as research documentation, not as evidence that the target implementation repository has been modified.

## Boundary

- The proposed track concerns interactive episodes with a trusted engine, constrained interventions, recorded actions and observations, and explicit controls.
- The first proposed pilot is one narrow evaluation condition, not a definition of the whole research object or a replacement for the 15-question portfolio.
- A behavioral effect does not establish a change to a hidden policy, update rule, attention mechanism, or world model. Stronger mechanism claims require independently instrumented targets.
- No Arena/Battle review, model call, code implementation, or preregistration is authorized by this scope note.

## Source and companion document

Section 4 of [`epistemic_games_genre_v5_02_evaluation_experiment_proposals.md`](../mission-02/sources/epistemic_games_genre_v5_02_evaluation_experiment_proposals.md) now points to the extracted companion documents; its detailed body is not duplicated there. The separate working design is [`epistemic_trajectories.md`](epistemic_trajectories.md); target-repository implementation suggestions are in [`rl_eval_generator_epistemic_trajectories_proposal.md`](rl_eval_generator_epistemic_trajectories_proposal.md). The broader source archive remains available for attribution and comparison.
