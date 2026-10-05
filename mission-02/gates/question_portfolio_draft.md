# Mission 02 — Gate 1 question portfolio (working draft)

**Status:** non-decisional working draft. **Human scope decision:** keep all 15 listed candidates (E1–E8, S1–S4, V1–V3) for further development; develop them serially rather than in one Arena Battle prompt. This retains the candidates but does not select a primary question, approve Gate 1, authorize a reframe, proceed to Gate 2, or authorize an experiment. The current Gate 1 status remains pending.

## How to use this portfolio

At the human's direction, this draft preserves all candidates rather than collapsing the program to one question. Treat them as individually assessed branches sharing some validation infrastructure—not as one bundled scientific claim. The protocol uses “the research question” in the singular, so the formal Gate 1 artifact should explicitly explain this portfolio structure and how each retained branch is assessed. Do not bundle distinct questions into one claim: each candidate below has its own contrast, observable, hypotheses, nearest prior-work collision, and feasibility needs. A branch may be tagged as an anchor, source-check-needed, blocked, or ready for Gate 1 review without being deleted from the retained portfolio.

The candidate sentences make the empirical contrasts explicit; they are starting formulations, not registered protocols. A question that is actually retained must still pass the four criteria in `research_protocol/protocol.md` §3.1: sharp empirical discrimination, genuinely competing plausible hypotheses, adequate source-level prior-work differentiation, and accessibility in an existing or locally extensible architecture.

**Limited source-check note (2026-10-05):** a read-only spot check confirms MindGames describes controlled DEL problem generation, English verbalizations, and public code/data ([arXiv:2305.03353](https://arxiv.org/abs/2305.03353)). The newly surfaced *Beyond Memorization* paper describes a DEL-puzzle benchmark varying narrative familiarity and inference complexity, including asymmetric observations ([arXiv:2603.21350](https://arxiv.org/html/2603.21350)). These are confirmed close collision leads for parts of the portfolio, not a full prior-art review; the exact verifier independence, text-fidelity controls, and overlap with the strategy-card questions remain to be checked.

## A. Candidate questions about epistemic reasoning

### E1 — Updating from a supplied behavior policy

**Question:** Across finite two-world instances with an explicitly supplied behavior table, do specified language models' posterior estimates track changes in prior odds and likelihood ratios more accurately than a prior-only or surface-cue baseline?

- **Discriminator / outcome:** posterior score or a predeclared posterior band as prior odds and likelihood ratio vary; compare against exact Bayesian ground truth.
- **Competing predictions:** evidence-sensitive Bayesian updating versus prior neglect, likelihood neglect, or cue-based answers.
- **Nearest collision / status:** Mission 02's v0 already instantiates an answer-only version. Treat this as a reuse baseline or a question about a clearly added factor—not as novelty merely because the task is epistemic.
- **Feasibility issue:** separate policy inference from policy application; v0 supplies the policy and is not a recursive level-k engine.

### E2 — Sequential public-announcement updates

**Question:** In formally matched dynamic-epistemic instances that differ only in the number or order of truthful public announcements, how does exact truth-classification accuracy change with update depth?

- **Discriminator / outcome:** exact classification of a registered knowledge proposition after each update, by depth, against a matched one-step/factual control.
- **Competing predictions:** correct sequential state updates versus depth-related update loss or a final-sentence/surface heuristic.
- **Nearest collision / status:** MindGames already generates DEL problems with English verbalizations; the 2026 DEL literature is a close lead. Any novelty claim needs a specific regime not already tested.
- **Feasibility issue:** freeze the event model, truth conditions, and text rendering rule before measuring model answers.

### E3 — Information carried by silence

**Question:** Under a fully specified partner policy that sends a message in some states but not others, do models update beliefs correctly when the expected public message is absent, compared with matched trials where the message is observed?

- **Discriminator / outcome:** posterior or knowledge classification after an explicit non-announcement versus the matched announcement condition.
- **Competing predictions:** treating silence as informative under the known policy versus treating silence as missing/no information.
- **Nearest collision / status:** classical signalling and dynamic epistemic reasoning are obvious prior-work leads; the seed's graph leads are not source verification.
- **Feasibility issue:** the protocol must specify when a message would have been sent. Silence is not informative without that policy and observability assumption.

### E4 — Nested knowledge order

**Question:** On matched finite epistemic models with the same narrative and first-order facts but different truth values for registered nested-knowledge formulas, how does model accuracy vary from first- through higher-order propositions?

- **Discriminator / outcome:** exact truth classification for formula families such as `K_i p`, `K_i K_j p`, and a bounded higher-order extension, with formula depth as the varying factor.
- **Competing predictions:** tracking the nested accessibility structure versus relying on first-order facts, familiar puzzle templates, or wording cues.
- **Nearest collision / status:** Hi-ToM directly covers higher-order ToM orders; MindGames also includes higher-order DEL problems. “Higher-order” alone is not a novelty wedge.
- **Feasibility issue:** use a bounded, explicit formal model; do not claim finite-order results establish common knowledge or a general theory of mind.

### E5 — Asymmetric or fragmented observation

**Question:** Holding narrative and underlying rules fixed, do models' truth judgments track changes in a registered observation matrix as agents' views become more asymmetric or fragmented?

- **Discriminator / outcome:** exact knowledge/posterior accuracy across symmetric and asymmetric observation structures, with matched narrative variants.
- **Competing predictions:** tracking each agent's observation relation versus treating the story as a familiar symmetric puzzle.
- **Nearest collision / status:** *Beyond Memorization* is a particularly close lead: it studies DEL-style puzzles while varying narrative familiarity and inference complexity, including asymmetric observations. MindGames is another near-prior. This candidate likely needs a narrower regime to survive.
- **Feasibility issue:** define the observation matrix, the task unit, and the semantics of every queried proposition before generating English items.

### E6 — Finite type spaces and common priors

**Question:** In finite common-prior games with fixed payoffs and different information partitions, do models' predicted action profiles track the independently enumerated Bayesian-Nash equilibrium when the games are restricted to instances with a unique equilibrium?

- **Discriminator / outcome:** predicted action profile compared with the unique, independently enumerated equilibrium under each type partition.
- **Competing predictions:** partition-sensitive reasoning versus payoff-only or surface-based choice.
- **Nearest collision / status:** classical epistemic game theory is a necessary prior-work base; benchmark and LLM claims require a focused source search. The knowledge graph is only a lead source.
- **Feasibility issue:** specify types, common prior, information partitions, solution concept, and tie/multiplicity rules; the oracle cannot be inferred from an uncapped textbook result.

### E7 — Level-k versus a competing solution concept

**Question:** In preregistered finite games selected so that bounded level-k predictions differ from a stated alternative solution concept, which prediction best describes models' actions as game depth or payoff parameters vary?

- **Discriminator / outcome:** action agreement with the separately enumerated level-k and alternative prediction sets across designed divergence cases.
- **Competing predictions:** stable alignment with level-k, alignment with the alternative, or neither.
- **Nearest collision / status:** game-theoretic LLM benchmarks such as GTBench are close; existing claims about strategic reasoning methods do not establish this narrower discrimination.
- **Feasibility issue:** choose one level-0 policy and one alternative solution concept; prove the selected finite games actually make distinct predictions.

### E8 — Belief and action in a signalling game

**Question:** In finite signalling games with a unique registered equilibrium outcome, do models' receiver-belief estimates and resulting actions change as priors and signal costs cross the precomputed pooling/separating boundary?

- **Discriminator / outcome:** belief and action correctness relative to an enumerated equilibrium, on matched games on either side of the boundary.
- **Competing predictions:** belief/action changes tracking the formal incentive threshold versus narrative or signal-salience heuristics.
- **Nearest collision / status:** signalling is named in the seed and classical literature; empirical LLM prior work and exact novelty need source checks.
- **Feasibility issue:** restrict to instances with an unambiguous solution or register how multiple equilibria are scored.

## B. Candidate questions about strategy packs

These are distinct causal questions. A positive answer to one does not imply a positive answer to the others.

### S1 — Value of method text beyond generic advice

**Question:** On one frozen, formally specified task family, does an actionable strategy card improve verified accuracy over a strong, length- and format-matched generic method instruction?

- **Discriminator / outcome:** paired correctness difference between the card and the generic-method condition.
- **Competing predictions:** card-specific content adds value versus generic explicit modelling being sufficient.
- **Nearest collision / status:** Self-Discover, Buffer of Thoughts, and other reasoning-template work are leads against a broad “method text helps” novelty claim; exact contrasts need source review.
- **Scope limit:** this tests card content against generic advice, not the value of trigger-based selection.

### S2 — Incremental value of trigger matching

**Question:** On the same frozen family and with card count, format, and exposure controlled, does selecting a card by a pre-solver structural trigger outperform assigning a yoked, non-matching same-family card?

- **Discriminator / outcome:** paired verified-accuracy difference between trigger-matched and yoked-card assignments.
- **Competing predictions:** trigger matching improves selection versus arbitrary same-family selection performing similarly.
- **Nearest collision / status:** generic retrieval systems are near-priors, but the exact trigger-matched contrast remains unverified. This is closest to the registered title's “trigger-matched strategy packs improve solving” claim.
- **Feasibility issue:** define the trigger from information available before solver output and prevent the card or matcher from seeing the answer or validity label.

### S3 — Incremental effect of obligations

**Question:** On trigger-present but move-invalid instances, does adding a card's explicit validity obligations reduce invalid method application relative to the otherwise identical card with obligation text removed?

- **Discriminator / outcome:** invalid-application or wrong-answer rate under a same-card, with-versus-without-obligations contrast.
- **Competing predictions:** obligations reduce misuse versus having no effect (or increasing errors through distraction).
- **Nearest collision / status:** the exact obligation mechanism is not established by the cited retrieval work, but it needs its own targeted search and its own observable.
- **Scope limit:** this cannot by itself show that retrieval or trigger matching improves solving.

### S4 — Transfer across epistemic families

**Question:** Does a strategy card whose trigger was authored on one epistemic family improve verified accuracy on a held-out family with the same declared structural feature, relative to a family-specific or no-card control?

- **Discriminator / outcome:** accuracy on the held-out family, with transfer defined before outcomes.
- **Competing predictions:** the structural transformation transfers versus the card's value being family-specific.
- **Nearest collision / status:** broad transfer claims are not registered in the current seed and would need a new prior-work and feasibility check.
- **Scope limit:** exploratory candidate; do not add it silently to the current seed.

## C. Supporting validation questions (not automatically scientific outcomes)

### V1 — Faithfulness of English renderings

**Question:** Given an instance's English text without generator metadata or answer, how often do independent annotators reconstruct the registered formal state and queried proposition exactly?

- **Outcome:** agreement with the frozen formal specification, ambiguity rate, and error type.
- **Role:** measurement-validity evidence. It is not evidence that an LLM reasons epistemically.
- **Needed rule:** predefine sampling, annotation access, adjudication, and treatment of ambiguous items.

### V2 — Reliability and leakage of problem characterization

**Question:** Given only the solver-visible text, do blinded characterizers independently assign the registered structural trigger features reliably, without access to generator parameters, answers, or outcome labels?

- **Outcome:** agreement/reliability plus a predeclared leakage audit.
- **Role:** a precondition for interpreting a trigger-matching study; it is not itself evidence that strategy packs help.

### V3 — Feasibility of independent verification

**Question/check:** Can the chosen family support a verifier that does not share the generator implementation, and can the intended local extension be described within the available architecture?

- **Role:** Gate 1 testability evidence and an engineering feasibility check, not a scientific hypothesis about solver behavior. Gate 1 need not require building the full verifier or running an experiment.

## Dependency-first serial development plan

All 15 candidates are retained by human direction, but **they are not to be developed in parallel in one Arena Battle**. Develop one question card at a time, following prerequisites rather than finishing every E-card before starting any S-card. This is portfolio development—not 15 separate seed rewrites and not a Gate 1 reframe. The protocol's one-reseed limit still applies only to a formal reframe after a Gate 1 failure. Serial development also does **not** require 15 Arena sessions: do local specification and source work first; request model critique selectively, one candidate at a time.

### Proposed dependency path (order is provisional; nothing is pruned)

1. **Establish one substrate family:** start with E1 as the v0 anchor because it is the existing, specified implementation. Develop its exact question and identify any factor beyond v0. If it adds none, keep E1 explicitly as a baseline/anchor rather than presenting the unchanged v0 task as a novel contribution.
2. **Check that substrate:** assess V3 (independent-verifier feasibility) and V1 (English-to-formal fidelity) for that family. These are local/source/feasibility checks, not a requirement to build the full verifier or conduct an Arena Battle.
3. **Check the retrieval precondition:** assess V2 (characterization reliability and leakage) using the selected substrate before claiming a trigger-matching test is feasible.
4. **Develop S2, then S3 on that substrate:** S2 tests incremental value from trigger matching; S3 separately tests the effect of obligations. Give each its own question card and contrast. Neither result stands in for the other.
5. **Continue the epistemic branches one at a time:** E2–E8 all remain in the queue. E3 (informative silence) is a reasonable early follow-up for targeted prior-work checking; E2, E4, and E5 have especially close DEL/ToM benchmark collisions; E6–E8 need their own formal solution/oracle checks. This order does not imply that any candidate is accepted or dropped.
6. **Develop S1 and S4:** S1 (method text versus strong generic advice) remains separate from S2; S4 (cross-family transfer) comes after at least two family cards have stable semantics and supporting checks.
7. **Repeat V1/V3 where a new family changes the formal or language-generation assumptions.** V2 is repeated only if the trigger vocabulary or characterization procedure changes materially.

For each card, record the target family and assumptions, manipulated contrast, observable, competing hypotheses, closest source-checked prior work, and family-specific feasibility. Use statuses such as `queued`, `in development`, `baseline/anchor`, `source check needed`, `blocked`, or `ready for Gate 1 review`; **these statuses track progress without removing any of the 15 retained candidates**.

Only if the human wants another model critique, prepare **one question-specific prompt for one Battle session** after the corresponding local card is ready, and preserve each returned answer separately. No additional Arena prompt or call is authorized by this plan.

## Gate 1 handling proposal

1. Keep all 15 candidates in the portfolio for serial development; this is not a promise to execute all of them. Do not force a single family or question merely to satisfy the word “sharp.”
2. Apply the four Gate 1 criteria **to each retained question**. Record the strongest prior-work collision and the narrow unestablished regime, if any, for that question separately.
3. Mark infrastructure and measurement-validity items (V1–V3) as supporting checks or engineering preconditions, not as LLM outcome hypotheses.
4. After the question cards have been developed, prepare the formal `gates/gate1_question.md` with the retained question portfolio, per-question hypotheses, prior-work differentiation, and explicit novelty statements. There are currently no pruned candidates; record that explicitly. Any later pruning requires a separate human decision. The existing `gate1_review_prompt.md` and response bundles are advisory materials, not that artifact.
5. Detailed controls, sample size, power, and execution remain Gate 2 or later. The user's decision to retain all candidates is a scope choice, not Gate 1 approval or experiment authorization.
