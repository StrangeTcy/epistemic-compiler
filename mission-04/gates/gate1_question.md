# Mission 04 — Gate 1: Question & Novelty Gate (DRAFT)

- **Mission:** `mission-04`
- **Seed:** `S04`, currently titled *“Common-knowledge neglect: do frontier models treat deep private confirmation chains as public announcements?”*
- **Status:** **Draft retained under user-directed HOLD — NOT approved.** Recommended disposition remains **REFRAME**, but no reframed direction was selected. Gate 2, experiment implementation, model calls, and seed/design edits are not authorized.
- **Inputs audited:** `../seed.yaml`, `../design.md`; all four Council roles (Theorist a/b, Experimentalist, Skeptic, Prior-Work Killer); `../critiques/cross_critique.md`; `../council/intake_log.md`; `../../research_protocol/protocol.md` §3.1; `../../mission-01/gates/gate1_question.md` as an artifact-format example.

## 1. Decision summary

The v1 proposal names a meaningful and important general topic, but it does **not** pass Gate 1 as currently framed. The formal chain oracle does not support the claimed interior depth cutoff under the literal ping-pong rule, and the PUBLIC arm does not preserve the disclosed scripted-Bob policy. H1 (“common-knowledge neglect”) and H2 (“bounded iteration”) therefore do not make the advertised distinct predictions. Separately, P04 and the follow-up audit establish substantial human and LLM prior art for finite-order/common-knowledge effects, dynamic epistemic evaluation, private-information games, and epistemic-asymmetry coordination. They do not establish an exact replication of S04's proposed lossy-chain/public/payoff-cutoff task, but the narrow gap is not yet verified by an exhaustive targeted search.

**Recommendation:** reframe around one explicitly chosen construct and narrow contribution. Do not advance the current seed unchanged and do not claim novelty. Whether a reframed question satisfies Gate 1 is a human decision after the choices below and a revised, independently checked question/model.

## 2. Gate 1 acceptance checklist (protocol §3.1)

| Acceptance condition | Draft assessment | Basis / what remains |
|---|---|---|
| 1. Sharp empirical discrimination problem | **Partially met as prose; fails as an executable question in v1.** The question is explicit, but its current oracle and public comparison do not match the written protocol. | `CR02`–`CR04`; rebuild the question around a frozen, valid event model. |
| 2. At least two genuinely competing, a priori plausible hypotheses | **Not met for the current design.** H1/H2 are intended to differ by dose-response, but the literal message rule collapses the response to a parity/terminal-cell check. | Define new, observably distinct hypotheses after the human chooses a construct; Gate 2 will test their measurement separation. |
| 3. Prior-work collision checked and exact contribution verified or narrowed | **Broad novelty is rejected; narrow contribution remains provisional.** Human work and several LLM evaluations are established. The checked follow-up did not find an exact S04 match, but search coverage is incomplete and absence is not proof. | Intake log §“Compiler follow-up search”; complete targeted search for delivery-structure, lossy-channel, public/private, and 2026 industry/preprint work; state a claim ceiling of “not found in this limited audit” until then. |
| 4. Testable within existing or locally extensible architecture | **Plausible, not independently verified from runtime source in this workspace.** The design describes a new `epistemic_depth` family and the cited Mission 02 source note reports relevant runtime plumbing, but the `rl_eval_generator` repository itself is absent here. | Before Gate 2, inspect the runtime or obtain the relevant version/source; confirm episode, oracle, logging, and local-extension interfaces. This is an unresolved feasibility check, not evidence that the research question is impossible. |

## 3. What the Council and audit support

### Formal and construct failures

1. Under the literal alternating ping-pong chain, Bob can receive the even-indexed `m_k` only at Alice's maximal receipt count for even `k`; at lower counts the chain has already stopped. For odd `k`, Bob cannot receive `m_k`. This contradicts the design's interior tail formula and removes the H1/H2 dose-response as specified. The independent enumeration and assumptions are recorded in the intake log.
2. PUBLIC does not specify how the same “Bob chooses X iff he received `m_k`” rule applies when a public announcement replaces the chain. Setting `q=1` for PUBLIC is not derived from that rule. In Experimentalist S04-R1, the proposed PUBLIC wording additionally states Bob's action directly.
3. With Bob scripted, the task is at most an inference/decision problem about a known partner policy. It is not endogenous common-knowledge reasoning. T-EC (Theorist b) and an endogenous finite-type game are different possible constructs, not approved repairs.
4. The user-visible original v1 title and the high-level research interest can be preserved only if the model and measurement are replaced to actually instantiate the claimed construct. Do not silently relabel the current score as evidence of higher-order belief.

### Prior-work differentiation

- **Classical mechanism:** Rubinstein's Electronic Mail Game is the mechanism source, not an empirical LLM result. The graph edge saying Rubinstein “empirically-tests” common knowledge is inaccurate; do not use that edge as evidence.
- **Human evidence:** De Freitas et al. (PNAS 2019) and Bolander, Engelhardt & Nicolet (2020 arXiv preprint, current v3 revised in 2025; three experiments, N=802) study common/finite-order shared knowledge. Their tasks and contribution differ from an LLM delivery-chain benchmark. See the primary-record checks in `../council/intake_log.md`.
- **LLM dynamic epistemic reasoning:** EAST is a 2026 arXiv preprint on epistemic tracking in a one-shot shared-word task. Li, Luo & Liao's peer-reviewed 2026 *Knowledge-Based Systems* paper evaluates recursive updates in Muddy Children/Cheryl's Birthday puzzles using 2,784 answer-prediction and role-playing samples. These defeat a broad “LLMs have not been tested on dynamic or higher-order epistemic reasoning” claim, but do not test S04's payoff-linked lossy chain.
- **LLM private-information and multi-turn coordination:** Galanis's 2026 arXiv preprint evaluates prediction markets with private signals and increasingly complex information structures; MT-PingEval evaluates multi-turn collaboration with private information, where “level-k” counts turns rather than nested belief order; CRAFT/“Flout at Your Own Risk” evaluates three private-view Directors coordinating with a Builder via a public board over 20 turns. These are substantial near-priors for interaction, private information and pragmatic/epistemic asymmetry, while differing from the proposed exact public-versus-lossy-chain cutoff task.
- **Communication/system robustness:** AgentComm-Bench and ProtocolBench test channel or protocol failures, but the inspected materials do not operationalize epistemic order or the S04 belief construct. A blanket “no communication-failure coordination benchmarks” statement would be unsafe.
- **Narrow surviving candidate:** The limited follow-up did not find a direct match to a one-shot LLM task that combines a parameterized lossy confirmation chain, a public-announcement comparison with the other model facts held fixed, and a closed-form payoff cutoff. This is a candidate gap only—not a novelty finding. P04's incomplete search and the follow-up scope are documented in the intake log.

P04's BMS DOI warning and its correction of graph-versus-retrieved-pack distinctions are supported. Two other P04 criticisms are not: seed L04 separately names TMGBench and the MathAI 2026 paper (the OpenReview link follows the latter), and the alleged “fuckingly” text is absent from the current seed/design/prompts. These corrections remain in the audit; they do not remove the need to expand the prior-work search.

## 4. Human choice: which question, if any, should be reframed?

The following are **candidate directions**, not approved seed text or settled Council consensus. Choose one construct; do not combine their claims.

### A. Bounded first-order completion-risk instrument — simplest executable path

Candidate question: *When the state and a scripted partner policy are disclosed, do tested LLM runtimes estimate the probability of terminal delivery success and choose according to a payoff cutoff across relay depth, loss probability, and payoffs, relative to a matched no-partner arithmetic task?*

This is the closest to Experimentalist S04-R1 and the Skeptic's proposed arithmetic twin. It explicitly drops “common knowledge,” “higher-order belief,” and a public-versus-chain claim unless a coherent matched public condition is separately derived. It would study a bounded decision/computation behavior, not whether models treat chains as public.

### B. Finite-order epistemic-condition task — preserves explicit nesting, not equilibrium

Candidate question: *Can a model map an agent's finite private-message history to the truth or probability of a specified nested-knowledge condition, and how does accuracy vary with nesting order after controlling for translation, surface length, and first-order arithmetic?*

This is closest to Theorist b's T-EC proposal. The scripted condition may permit a well-defined finite-order task, but it does not test endogenous strategic rationalizability or common-knowledge equilibrium. The formula, event model, role-specific indices, public condition, rendered observations, and full oracle require independent derivation and enumeration first.

### C. Endogenous strategic communication game — only direction that could retain a common-knowledge/equilibrium claim

Candidate question: *In a fully specified finite noisy-communication game with endogenous player actions and a registered solution concept, do tested LLM agents' action profiles track the independently enumerated solution set as information depth, noise, and payoffs vary?*

This requires replacing the scripted partner, specifying terminal observations/types and the capped game, and solving every instance before measurement design. Existing council checks find multiplicity and knife-edge profiles under some capped settings; do not assume the uncapped Rubinstein result yields a unique finite oracle. It is the most expensive direction and its exact prior-work gap remains unverified.

### D. Pause or stop

Pause for additional prior-work/runtime verification, or close S04 if none of the three constructs matches the research objective. A Gate 1 stop is a valid outcome under protocol §3.1; it is not a failure of the process.

## 5. Reframing requirements before Gate 1 can be approved

1. Record the human's chosen direction and the intended claim ceiling. If direction A or B is chosen, remove unsupported “common-knowledge neglect” and “public-versus-chain” wording unless the new formal task actually tests those constructs. If C is chosen, keep the common-knowledge claim conditional on the endogenous model and solution concept.
2. Rewrite one sharp research question and a coherent model from the rendered protocol backward. Specify timing, state, private/public events, who observes what and when, message recipients, stopping, partner policy (if scripted), priors/payoffs, exact tie rule, and the target estimand.
3. Independently derive and exhaustively enumerate all histories/types and actions for every arm, including the comparison arm. Have a checker start from the frozen prompt semantics, not copy the closed form. Remove parity, terminal-cell, tie, and policy inconsistencies before sampling any hypotheses.
4. Replace H0–H3 with at least two plausible, distinguishable hypotheses for the chosen target. Include a boring computation/surface alternative; specify what measured pattern would discriminate them. Detailed likelihoods and expected-information-gain table belong in the Gate 2 draft.
5. Complete the focused literature searches noted above. Maintain a source table distinguishing peer-reviewed papers, arXiv preprints, benchmarks, and adjacent system-level work. Report the exact scope and date of any absence search.
6. Verify runtime feasibility against the actual `rl_eval_generator` revision or obtain the source artifacts that establish its extension interfaces. No model run or implementation is authorized by this draft.

## 6. Requested human decision and decision log

**Requested:** choose A, B, C, or D from §4; optionally state the claim ceiling and whether the proposed reframing matches the original research intent. If choosing a reframe, this is not yet approval of the final Gate 1: the revised formal question, oracle, competing hypotheses, and targeted prior-work search must be returned for review.

- **Draft recommendation:** `REFRAME` (choose one direction; no current v1 pass).
- **Human verdict:** `HOLD` (the user selected option D, then clarified “pause/hold” in the follow-up decision).
- **Chosen direction:** `NONE`; A/B/C were not selected.
- **Mission status:** `PAUSED` pending further user direction.
- **Gate 2 authorization:** `NOT AUTHORIZED`.
- **Decision date:** `2026-10-02` (Arena decision UI; no time supplied).
- **Seed/design changes:** none made.
- **Model runs:** none made.
- **Mission 02 / Mission 03:** untouched. Atria campaign analysis remains deferred and separate.
