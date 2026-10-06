# Proposed Minimal Test

**Status:** extracted and organized from the assistant-generated proposal in §3 of [`epistemic_games_genre_v5_02_evaluation_experiment_proposals.md`](epistemic_games_genre_v5_02_evaluation_experiment_proposals.md) (source log: response 16). This is a candidate design, not an approved protocol, preregistration, or result. The full design is organized here rather than duplicated in §3 of the genre proposal.

## Candidate question

Under a fixed world and evidence set, can otherwise matched messages change a target’s subsequent **observable** information-seeking or test choices? If so, do those effects differ by the attacker’s access to an opponent model?

This is a narrow candidate test, not a definition of the full research object or a replacement for the 15-question portfolio.

## Keep three outcomes distinct

The source proposal separates:

- **\(\Delta G\):** magnitude of model change.
- **\(\Delta Q\):** change in the quality of subsequent inquiry.
- **\(\Delta R\):** change in eventual task performance or recovery.

These labels still need operational definitions, direction conventions, and controls. Do not combine them into one score. For a black-box target, a change in behavior does not reveal a hidden world model or update rule; \(\Delta G\) requires an explicit, instrumented representation. Observable inquiries, tests, source choices, forecasts, and task outcomes should be recorded directly.

## Candidate message conditions

The proposed comparison uses:

\[
M_{\mathrm{helpful}},\qquad M_{\mathrm{neutral}},\qquad M_{\mathrm{adversarial}}.
\]

The intended contrast is: same world, same evidence, same literal facts, but different subsequent observable inquiry. Truthfulness and message length are proposed matching constraints; token-level information content is mentioned as a possible further constraint.

**Still unresolved:** token counts do not establish semantic equivalence. The condition generator needs an auditable rule for holding the underlying fact set fixed, validating each message, and distinguishing a presentation effect from added advice or changed evidence. A truthful-subset condition changes the target’s information set and should not be treated as the same-information comparison.

## Opponent-model conditions

The proposal also suggests crossing message condition with:

- **\(A_0\):** no opponent model;
- **\(A_1\):** a model of the opponent’s beliefs;
- **\(A_2\):** a model of the opponent’s inquiry dynamics.

Treat these as proposed experimental conditions or ablations, not as an established global capability ladder. Specify exactly what information each condition gives the attacker and hold the rest of the task fixed before interpreting differences.

## Decisions needed before a pilot

1. Define a measurable inquiry-quality outcome for \(\Delta Q\), and specify the relevant task outcomes for \(\Delta R\).
2. Decide whether \(\Delta G\) is available only for an instrumented target or excluded from the black-box analysis.
3. Specify the semantic-matching and truth-validation procedure for the three message conditions.
4. Choose controls that distinguish matched presentation from extra information, ordinary advice, deception, shallow heuristics, or reward effects.
5. Decide whether attacker-model access is part of this pilot or a later ablation; do not assume \(A_0\), \(A_1\), and \(A_2\) form a monotone scale.

No Arena/Battle review or model call has been made or is implied by this note.
