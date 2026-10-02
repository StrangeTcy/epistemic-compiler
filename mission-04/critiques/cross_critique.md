# Mission 04 — Council round 1 cross-critique

**Status:** Compiler synthesis after the four named roles were collected. This is not another independent Council response, not a vote, not a design revision, and not Gate 1 sign-off. It preserves disagreements and flags what must be settled before Gate 2. The response records and source checks are in `../council/`; in particular, see `../council/intake_log.md` for audits, limits and follow-up references.

**Inputs:** `../seed.yaml`, `../design.md`, Theorist samples a/b, Experimentalist, Skeptic, and Prior-Work Killer (P04-PW v1). The four roles are represented by five response files because Theorist has two independent samples.

## Cross-critique items

### CR01 — The registered label and the v1 task do not match

All roles, despite different recommendations, identify a construct mismatch: the seed/title says “common-knowledge neglect,” but design §3 scripts Bob's policy and discloses it to Alice. In the current model Alice is asked to infer whether a known automaton received the terminal message and compare that probability to a payoff threshold. That is a first-order posterior/decision task under a scripted partner, not an endogenous game in which both players reason strategically about a hierarchy of beliefs. P04's high-level reframe is supported; the response's more specific claim that this is “the seed's headline hypothesis” must be qualified because S04 itself distinguishes H1 from H2 and explicitly labels the scripted-partner limitation.

### CR02 — The current CHAIN oracle removes the advertised dose-response

The independent finite-tree enumeration reported by Theorist b and Skeptic agrees: under the literal ping-pong protocol, for even k Bob can receive `m_k` only at Alice's maximal receipt count, where the conditional completion probability is `1−ε`; below that, the chain has already stopped. For odd k Bob cannot receive the odd-indexed `m_k`. Thus the oracle does not have the interior cutoff `q(n)=(1−ε)^(k−n′)` used in design §3; there is no graded chain-depth region to separate H1 from H2 as currently hypothesized. This is a protocol/model failure, not a small arithmetic adjustment. Theorist a's “directionally” increasing-tail account does not survive the literal stopping rule; its own section says the mapping requires explicit enumeration, which is the safer rule. Any repair must freeze timing, parity, who receives each message, Alice's observation, termination observability, and the posterior before generating cells.

### CR03 — PUBLIC changes the partner rule unless explicitly repaired

The chain prompts state “Bob chooses X iff he received the k-th confirmation.” A public announcement of G does not imply Bob received that message. The design nevertheless sets PUBLIC's q to 1 and action to X. Unless PUBLIC has a distinct rule or a carefully specified public event that changes Bob's information while preserving his policy, the treatment arms do not hold the model fixed. The model can read the rule rather than reason about public versus private information. This converges with both Theorist samples and Skeptic; the Experimentalist independently catches a related leak in S04-R1's PUBLIC wording, which says the board reveals Bob's action itself.

### CR04 — The proposed repairs test different constructs; none is yet an approved fix

- **Experimentalist S04-R1:** Its completion probability and cutoff are coherent under its *new* timing/protocol assumptions. It measures completion-risk or threshold reasoning with a scripted partner. It does not restore higher-order beliefs or establish common-knowledge neglect. The listed sample/run totals also need the intake-log corrections before a Gate 2 spec.
- **Theorist b's T-EC:** A nested epistemic-condition rule could provide a finite-order inference task. It remains a prescribed/scripted partner policy, not endogenous strategic rationalizability. The proposed closed-form beliefs and boundary cells must be independently formalized and exhaustively enumerated before reliance; the response itself asks that the enumerator check the derivation. Title and claim ceiling would need to say what is actually being measured.
- **Endogenous v2:** This is the most direct route to a strategic common-knowledge question, but the unbounded Rubinstein result cannot simply be copied to a finite capped type space. Theorist b and Skeptic find multiplicity or knife-edge cases for some capped profiles. Specify terminal types, stopping observations, priors/payoffs and strict-versus-weak deletion; then implement and independently check the full finite solution. Theorist a's blanket uniqueness statement is not established for the current cap.

### CR05 — Prior work kills a broad “new phenomenon” claim, not automatically the narrow instrument

The Council's strongest prior-work point is sound at a broad level: human finite-order/common-knowledge effects are reported by Bolander et al. (arXiv preprint first submitted 2020) and De Freitas et al. (PNAS 2019); the LLM preprint EAST (Rocca et al., July 2026) reports private-versus-mutual epistemic-tracking failures. The compiler's follow-up found still closer adjacent work: a peer-reviewed 2026 dynamic-epistemic benchmark with 2,784 Muddy Children/Cheryl's Birthday answer-prediction and role-playing samples; Galanis's 2026 arXiv study of LLM prediction markets across four increasingly complex private-information structures; and MT-PingEval's 2026 multi-turn private-information games. MT-PingEval's “level-k” specifically counts dialogue turns needed to reach a score threshold, not epistemic belief order. CRAFT/“Flout at Your Own Risk” adds a genuinely interactive partial-observability task: three Directors with private views coordinate through messages and a shared board with a Builder over 20 turns, evaluated by task progress and diagnostic graders. This is a strong prior for epistemic-asymmetry coordination, but it has no lossy-message or public-versus-chain treatment; its pragmatic “mind modeling” is not common knowledge as an experimental variable. These works differ materially from the exact S04 chain/public/payoff construction, but foreclose claims that LLMs have never been tested on recursive knowledge, private information, or epistemic asymmetry. Details and source-status qualifiers are logged in `../council/intake_log.md`.

The narrow candidate gap—one-shot, parameterized lossy confirmation depth with an explicit public comparison and a registered cutoff oracle—was not found in this limited follow-up. That is “not found,” not proof of novelty. P04's own search was incomplete, and the required 2026 industry-artifact search remains light. Do not write “first,” “novel,” or “no benchmark” until targeted follow-up is complete.

### CR06 — Correct P04's own checkable errors before reusing its conclusions

The Prior-Work Killer correctly flags the BMS DOI in `knowledge/nodes.yaml` as unresolved: the supplied DOI returns “DOI Not Found,” while the ACM TARK '98 record identifies the paper and proceedings pages 43–56. Its distinction between nodes existing in `knowledge/nodes.yaml` and not being retrieved into `context/shared.md` is also correct. The graph's `rubinstein-1989 — empirically-tests — common-knowledge` edge is inappropriate for Rubinstein's theoretical game-theoretic paper; the duplicate edge 003/081 and L07's “Morris & Robins” citation need correction or source identification.

Two P04 flags are not supported: (i) seed L04 names TMGBench and the separately quoted MathAI 2026 “Strategic Reasoning in Large Language Models” paper, with the OpenReview URL following the latter; PW-K08's alleged attachment of that URL to TMGBench is false as written (separate citation formatting could be clearer); (ii) “fuckingly” is absent from the current seed, design and all four role prompts. Also correct P04's PNAS author order to De Freitas, Thomas, DeScioli and Pinker, and distinguish an arXiv preprint from an established publication. Its MathAI example shows reference/benchmark-optimal scoring, not necessarily the same exhaustive deterministic oracle architecture as S04.

### CR07 — Keep useful controls, but separate constructs and harmonize rules

The Skeptic's arithmetic-twin task is a useful proposed control for computational load versus information-structure effects; it is not already part of the frozen design. The Council also identifies transcript leaks/shortcut cues, exact comprehension keys, two-sided action discrimination, payoff/ε mobility, padding balance, strict margin exclusions, and consistent gate/abort thresholds as matters for a measurement specification. The Experimentalist's arithmetic/counting discrepancies (51 listed depths, 153 base cells, not 49/147) and selected pilot scaffold cells belong in Gate 2, not in a claim that the current protocol has passed. The Skeptic's threshold critique must distinguish stratum accuracy from `ρ=P(X | oracle Y)`: always-Y can exploit an oracle-Y-only stratum but gives ρ=0.

### CR08 — Recommended Gate 1 disposition: REFRAME; do not advance the current design

As written, the protocol does not support the registered H1/H2 contrast. The prior-work record supports reframing the broad phenomenon as known human/LLM territory, while the specific LLM delivery-chain instrument remains only a candidate extension. The current Gate 1 acceptance conditions are not all met: no valid current oracle/dose-response, no completed targeted prior-work search, and only indirect support for runtime feasibility because the `rl_eval_generator` source repository is absent here. The design/source note makes local extension plausible, but the relevant interfaces cannot be independently rechecked in this workspace. A Gate 1 reframe should define a new sharp question and scope before any Gate 2 work. No Council vote or human Gate 1 decision is implied here.

## Decision points to carry forward

1. Choose the target construct: first-order completion-risk instrument; finite-order epistemic-condition task; or endogenous strategic game. Do not blend their claims.
2. For that construct, replace the current formal protocol and independently enumerate the oracle on every rendered state, including PUBLIC and tie/margin handling.
3. Update H0/H1/H2/H3 so at least two hypotheses make distinct predictions under the corrected model; use a two-sided human/LLM prior where evidence permits.
4. Complete a focused literature search for lossy/communication-failure coordination, public/private delivery contrasts, and 2026 preprints/industry-track items before asserting a novelty wedge.
5. Resolve the BMS DOI, L07 author string and edge 081 in the source record at a deliberate revision point; do not cite graph edge IDs as primary literature evidence.

No Mission 04 seed/design change, Mission 02/03 edit, or Atria campaign analysis has been made by this cross-critique.
