# Epistemic Trajectories — Proposed Evaluation Design

**Status:** working proposal only. This document is not an approved protocol, preregistration, implementation, or experimental result. The proposed track boundary is recorded separately in [`epistemic_trajectories_scope.md`](epistemic_trajectories_scope.md).

**Scope of this draft:** one narrow interactive pilot. It does not define the entire research object, settle a formal theory, or replace the 15-question portfolio. The broader sequence of deception → belief manipulation → epistemic-process manipulation is provisionally adopted as a testable organizing hypothesis in the [evaluation-proposal record](../mission-02/sources/epistemic_games_genre_v5_02_evaluation_experiment_proposals.md); this pilot alone cannot establish that sequence or its transfer claims. The original source passage remains there, and a related minimal-test proposal is in [`epistemic_games_proposed_minimal_test.md`](../mission-02/sources/epistemic_games_proposed_minimal_test.md).

## Candidate question

Under a fixed world and a fixed, engine-validated fact set, does changing the **order or emphasis** of a presentation causally change the target’s subsequent **observable** choices of tests, queries, or sources? Can the target recover after independently supplied corrective evidence?

This pilot measures a presentation effect and its task consequences. It does not by itself show that an internal inquiry policy, update rule, attention mechanism, or world model changed.

## Episode outline

- **World:** hidden state \(\theta\), generated from a declared prior; ground truth remains in the trusted engine.
- **Target/defender:** receives a declared test or inspection budget, chooses actions, observes their outcomes, and makes a final decision.
- **Presenter:** can use only the intervention allowed by the condition. In the matched-presentation condition, it cannot condition its choice on the hidden \(\theta\).
- **Engine:** validates facts and interventions, returns test outcomes, and scores the final decision.
- **Event history:** records the case, condition, presented fact IDs, test requests, returned observations, final decision, and score so the run can be replayed.

A trajectory here means the recorded sequence of events and choices. It is not a claim that a black-box target’s hidden cognitive process has been observed.

## Initial condition proposal

The most specified narrow comparison in the source material is **same-fact presentation**: every arm receives the same semantic fact set and truth conditions; only order or emphasis varies. The presenter’s allowed output should be engine-validated against canonical fact IDs. A neutral condition is the comparator; helpful presentation and no-presenter conditions can test whether the effect is adversarial-specific or caused merely by having a presenter.

Keep these candidate conditions separate:

| Condition | What changes | Boundary |
|---|---|---|
| Neutral presentation | Nothing beyond the standard order | Baseline |
| Adversarial presentation | Order/emphasis of the fixed fact set | Same facts; no added evidence |
| Helpful presentation | Order/emphasis selected to support the better test | Separate positive control |
| No presenter | Standard fact sheet, no presenter | Detects presenter-presence effects |

A truthful-subset condition changes what information is available and therefore is **not** the same-information comparison. Observation budgets, source cues, causal-attribution cues, and attacker/defender awareness are separate candidate factors; they are not silently included in this first condition.

## Task template status

The earlier four-mechanism/three-test diagnostic device can serve as an oracle-transparency fixture, but a later assistant proposal in [`epistemic_games_genre_v5_05_implementation_generator_specifications.md`](../mission-02/sources/epistemic_games_genre_v5_05_implementation_generator_specifications.md) notes that a constant best test invites a shallow “choose the most outcomes” heuristic. That proposal suggests an `exclusion_8x6` template for a primary test. Neither choice is established by results here. Before selecting a primary template, verify that the best test varies across cases and relevant histories, and that the oracle and simple baselines behave as expected.

## Candidate outcomes

For history \(h_t\), define the ex-ante value of available test \(q\) as \(V(q\mid h_t)\), using only the prior, evidence available to the target, declared costs, and value of the eventual decision. One proposed inquiry measure is test-choice regret:

\[
r_t=\max_{q\in Q_t}V(q\mid h_t)-V(q_t\mid h_t).
\]

A candidate primary contrast is the paired difference in mean regret between adversarial and neutral presentation. The following should remain distinct outcomes when measured:

- first-test choice and cumulative test-choice regret;
- final decision loss;
- elicited probability forecasts, scored separately with a proper scoring rule;
- recovery after independently supplied corrective evidence;
- intervention-validity rate.

The source materials use symbols such as \(\Delta_G\), \(\Delta_Q\), and \(\Delta_R\) inconsistently. Keep outcome names in words until each quantity, sign, baseline, and measurement procedure is settled. Do not use a single “epistemic damage” score. A model-change measure is unavailable for a black-box target unless an explicit, instrumented representation exists; even then, model change alone is not harm.

## Controls and validity checks

Before treating a contrast as interpretable, specify and check:

1. Same world, prior, test costs, and verified semantic fact set in matched-presentation arms.
2. No added facts, omitted facts, covert instructions, or dependence on hidden \(\theta\) in the presenter’s permitted transform.
3. Randomized or counterbalanced condition order and paired seeds/cases.
4. A trusted oracle that computes test values and outcomes independently of the target’s explanation.
5. An optimal scripted target as a null check, plus simple heuristic baselines to detect a trivial winning rule.
6. Replayable event logs from which scores can be recomputed.
7. Separate treatment of belief elicitation: asking for a belief after every step may itself change later behavior.

The test should be challenged with alternatives such as extra information, better advice, a shallow heuristic, reward effects, or prompt injection. Such challenges are a future review method, not an authorization to call Arena/Battle models.

## Attacker-model conditions: later option

The proposed \(A_0\), \(A_1\), and \(A_2\) conditions—no opponent model, a model of opponent beliefs, and a model of opponent inquiry dynamics—may be considered as a later ablation. They are not part of the initial matched-presentation condition and should not be treated as a validated global capability ladder. Specify the information each condition gives the attacker and test it independently.

## Implementation boundary and open decisions

The source proposal describes a new interactive track with constrained actions, a trusted engine, and replayable artifacts. That is a proposed extension, not a claim about the current CLI or a request to implement it here. Before a pilot is approved, decide:

- which task template is primary and which is only an infrastructure fixture;
- the exact primary endpoint, budget, pairing, seed range, and exclusions;
- the semantic fact-matching and intervention-validation procedure;
- whether helpful/no-presenter controls are required in the first pilot;
- which outcome definitions and symbols, if any, are retained;
- whether attacker-model access is deferred to a later experiment.

No model calls, code changes, or runs are implied by this design note.
