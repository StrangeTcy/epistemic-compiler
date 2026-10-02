# Mission 04 design: common-knowledge neglect under finite confirmation chains

**Status.** Pre-Council proposal, written 2026-10-02 from the revised Arena instruction pasted by the
user (`mission-02/sources/raw/2026-10-02_instruction_revision.gpt_5.6_luna.md`), adapted: its TENTH
section names `mission-02/` artifacts, but that directory exists on this branch under a freeze
(`tests/test_mission_02_freeze.py`), so this mission is `mission-04`. Nothing has been run and no model
was called. The `rl_eval_generator` runtime repository is **not present in this workspace** (empty
placeholder directory); every statement about it is a specification or is sourced to
`mission-02/sources/2026-09-29_arena_round_note.md` section 3, which verified it against that
repository's `main` at `e1b038a` on 2026-10-02. Facts from the epistemic-games literature carry
evidence tags: [V] verified, [S] seen this session (search snippets), [R] recalled, unverified.

Files: `seed.yaml` (S04, protocol schema), `context/` (compiled Mindcluster packs, retrieval id
`2f65c211684ee6ec`), this design, and `tests/test_mission_04_seed.py`. `mission-01/harvest.md` carries
the durable Mission 01 methodology this design reuses.

## 1. Mindcluster search (FIRST) and candidate phenomena (SECOND)

The graph (`knowledge/`, 118 nodes, 301 edges) was searched for clusters with a formal mechanism, an
AI failure mode, a natural game construction, and matched controls. Six clusters were considered:

| Cluster | Graph anchors | Verdict |
| :--- | :--- | :--- |
| **Common knowledge and its failure under private chains** | `common-knowledge`, `rubinstein-1989`, `aumann-1976`, `baltag-moss-solecki-1998`, `lewis-1969`; edges 002, 003, 008, 076, 081, 164, 207 | **Selected.** Exact discontinuity theorem, executable as a parameterized decision task, exact oracle, facts-hold-fixed manipulation built in. |
| Level-k / cognitive hierarchy | `level-k`, `zhang-klevel`, `camerer-ho-chong-2004`, `nagel-1995`; edges 004–007, 077 | Rejected for v1: prior work is dense (guessing games already benchmarked on LLMs [R]; GTBench-adjacent play batteries, L04 in `seed.yaml`), and ground truth needs a model of the opponent's reasoning level, weakening the oracle. |
| Signalling / strategic information transmission | `signalling`, `spence-1973`, `kamenica-gentzkow-2011` | Strong runner-up. Rejected here because sender-incentive manipulations confound message *content* with delivery; keep as the next seed if S04 lands. Edge 039 (`level-k -- applies --> signalling`) noted. |
| Deception / lying with truths / Potemkin | `lying-with-truths-2026`, `potemkin-2026`, `strategic-deception`, `belief-state-shaping` | Rejected for v1: the presenter side needs a second model or a scripted presenter with many free parameters; overlaps the Epistemic Trajectories v0.1 proposal recorded in the sources note. |
| Reflexive control / epistemic process control | `reflexive-control`, `lefebvre-reflexive`, `epistemic-process-control`, `pelevin-mi13` | Rejected: no minimal ground-truthable game identified; stays in `knowledge/` as direction, not mission. |
| Attention manipulation / endogenous attention | `attention-manipulation`, `nguyen-attention-2026`, `rational-inattention` | Rejected: needs an attention-budget mechanic that the current runtime does not obviously provide; unknown, not assumed. |

Selection criteria applied (THIRD): novelty (no benchmark found that manipulates delivery structure
with facts held fixed; section 9), tractability (single-decision episodes, exhaustive instance space),
evaluator reliability (deterministic oracle, no LLM judge on the primary outcome), separability
(H0–H3 make different dose-response predictions), reusability (a parameterized family, not one puzzle),
infrastructure fit (one new environment family; mission-01's hardening method applies), and null value
(section 8).

**Selected phenomenon.** Finite-depth private confirmation is not common knowledge, yet models trained
on corroborated-text corpora may treat them alike. The electronic mail game [R][L01] makes the contrast
exact: the same signal, the same protocol knowledge, the same payoffs — delivered publicly or through a
lossy private chain — change the correct action.

## 2. Research question and mechanistic hypotheses

From `seed.yaml`: for a fixed runtime, on instances where the factual content is held fixed and only
delivery varies (public announcement vs private chain of depth k with loss probability ε), does the
model's choice track the exact oracle, or does the chain arm behave like the public arm?

- **H0 surface.** Length/wording drive everything; length-matched padding kills the gap.
- **H1 common-knowledge neglect.** Chain-arm choices jump to the public-arm policy; the empirical cutoff
  depth sits near the public arm's, far from the oracle's.
- **H2 bounded iteration.** Graded or interior-step depth response; intermediate depths pass where H1
  predicts public-like behaviour.
- **H3 comprehension artifact.** Errors come from misreading the transcript; controls fail; a scaffold
  removes most of the effect.

H1 and H2 are both "real epistemic failure" stories; they are separated by the shape of the
dose-response, which is why the design samples all depths rather than two arms.

## 3. Formal environment definition

**Epistemic model M(P, k, ε).** Two players, Alice (the model under test) and Bob (scripted). State
θ ∈ {N, G}, prior Pr(G) = 1/2. If θ = G the coordinator sends message m₁ to Alice; on receiving mᵢ a
player sends mᵢ₊₁ to the other; each in-transit message is lost with probability ε, independently, and
the protocol stops after a loss or after k messages. If θ = N nothing is ever sent. Payoff profile
P = (G, L): if both choose action X then +G each when θ = G and −G each when θ = N; if Alice chooses X
and Bob does not, Alice gets −L (same for Bob); Y pays 0. Bob's rule is stated verbatim in every
prompt: *Bob chooses X if and only if he received the k-th confirmation.* All of this is common
knowledge and rendered in the prompt.

**Histories.** Alice's observation is the number n of messages she received (0…⌈k/2⌉); it determines the
realized chain length. The instance space per profile is therefore finite and small: the public arm
(announcement of G, or silence) plus k+2 chain histories.

**Oracle (closed form, derivable in three lines).** For n ≥ 1, θ = G with probability 1 (no messages in
N), and Bob plays X with probability q(n) = (1−ε)^{k−n′} where n′ is the delivered chain length implied
by n; for n = 0, q = 0. The oracle action is X iff q ≥ L/(G+L), i.e. iff the delivered depth exceeds
the cutoff n\*(P, k, ε) = k − ⌊log(L/(G+L)) / log(1−ε)⌋ (with the boundary cases computed exactly by
the oracle module, not by this sketch). **Public arm:** announcement ⇒ q = 1 ⇒ X; silence ⇒ Y.

**The manipulation, exactly.** Pick parameters with an interior cutoff (worked example: ε = 0.1,
k = 10, G = 100, L = 90 ⇒ q\* ≈ 0.474 ⇒ n\* = 3). On chain instances with n < n\* the oracle says Y
while the "treat the chain as public" heuristic says X; on n ≥ n\* both agree. Same facts, same
protocol text, same payoffs across arms: only delivery differs. **Known limitation:** with Bob's rule
fixed in the prompt, the task is strategic-uncertainty reasoning about Bob's information, not unbounded
belief iteration; the endogenous (fully two-player) email game, where the unique rationalizable outcome
is Y at every finite depth [R][L01], is held out as variant v2 (section 10) with its own oracle by
iterated dominance over the finite type space.

**Cover stories.** Three registered renderings of the identical formal model (no war/conflict wording;
abstract actions X/Y labelled per story, e.g. LAUNCH-HOLD for a sensor calibration task). Cover 3 is
held out from the pilot and appears only in FALS-03, to bound CF03/CF08.

## 4. Treatment and control conditions

| Condition | Prompt receives | Purpose | Rules out |
| :--- | :--- | :--- | :--- |
| PUBLIC | public announcement or silence | upper reference; correct action obvious | floor effects; task incomprehension |
| CHAIN(n) | private transcript at sampled depth n | the treatment | — |
| PADDED | CHAIN + length-matched neutral coordinator log | length/verbosity control | CF01 |
| COMPREHENSION | same transcript, factual questions (depths, who needs what) | reading gate | CF02/CF07 contamination of the main contrast |
| BELIEF | same transcript, "probability Bob chooses X" | first-order belief probe; calibrates secondary measure | separates belief from decision |
| LABEL-SWAP | CHAIN with X/Y labels permuted | wording-asymmetry probe | CF05 |
| SCAFFOLD (pilot only) | CHAIN + instruction to tabulate histories before deciding | H3 test | comprehension vs epistemic failure |

Every arm shares one deterministic renderer from frozen template files; arm texts and hashes are
recorded at freeze (Gate 2), following the CTRL11 pattern of `mission-03/candidate_measurements.yaml`.

## 5. Sampling and runtime

- **Instances:** exhaustive over depths per profile (the space is small; no Monte Carlo over histories).
  Profiles: three seen (cutoffs shallow/mid/deep) + two unseen until FALS-03. ε ∈ {0.05, 0.1, 0.2},
  k ∈ {8, 10, 12}, payoffs chosen so n\* spans the range; exact registered values fixed at Gate 2.
- **Repetitions:** m = 8 draws per instance at the campaign's temperature if the runtime samples;
  m = 3 if deterministic decoding is used. Pilot seeds disjoint from registered seeds.
- **Order:** seeded; action-label swap balanced across depths; cover story balanced across profiles.
- **Runtime:** same settings convention as mission-03 (a campaign config in the runtime repository);
  single-turn decision episodes; structured JSON answer `{action, probability?, reason?}`; `reason` is
  collected as secondary evidence and never scored on the primary outcome.
- **Cost:** 5 profiles × ~12 chain depths × 3 covers × 8 draws ≈ 1,440 chain episodes + arms ≈ under
  2,500 single-turn episodes total. Cheap relative to mission-03's budget.

## 6. Measures

- **Primary.** Strict correctness versus the oracle action per arm. Primary contrasts, all paired by
  instance within profile: (a) **neglect rate** ρ = P(model says X | CHAIN, oracle says Y); (b)
  PUBLIC − CHAIN accuracy on the disagreement stratum; (c) empirical cutoff ñ (deepest n where the
  model still says Y with ≥ 50% probability mass) versus theoretical n\*.
- **Secondary.** Calibration of `probability` against q(n) (Brier); dose-response curve shape (H1:
  step at ñ ≈ n\* of the public arm; H2: graded); BELIEF-arm probability versus decision consistency;
  token/cost statistics.
- **Tertiary (never primary).** Coded explanations; treated as hints about mechanism only, per the
  instruction's SIXTH point.

Decision regimes (qualitative, to be quantified in `spec/draft.yaml` at Gate 2): O1 ρ high with
controls at ceiling ⇒ H1; O2 graded depth response, intermediate depths pass ⇒ H2; O3 padding kills the
gap ⇒ H0; O4 controls fail ⇒ H3, epistemic interpretation blocked; O5 everything near ceiling
including unseen variants ⇒ capability result, family ships as an instrument.

## 7. Oracle specification (SIXTH)

- **Implementation:** pure deterministic module `oracle.py`: (profile, arm, history) → (posterior, q,
  EU, action, n\*). No LLM anywhere in the primary verdict. State-transition/payoff verification only:
  the oracle recomputes the finite message tree by explicit enumeration in a second module
  (`oracle_crosscheck.py`), and the two must agree on **all** instances of all registered profiles at
  build time — exhaustive, not sampled. This applies the Mission 01 lesson that two checkers sharing a
  code path validate nothing (`mission-01/harvest.md`, item 2).
- **Renderer independence:** the prompt renderer and the oracle share no function that computes
  beliefs; the renderer consumes only (profile, history, cover) and template text.
- **Hardening:** before any model run, the environment gets the Mission 01 bypass-variant treatment:
  a fixed set of degenerate policies (always-X, always-Y, copy-the-example, ignore-transcript) must
  score exactly as the oracle predicts across 50 seeds (harvest item 1).
- **Anti-gaming:** single-decision structured output leaves nothing to game beyond answering; the
  parser is deterministic and parse failures count as failures (CF07 monitored separately).

## 8. Value of each outcome

H1 confirmed ⇒ a named, bounded behavioural failure (delivery-structure neglect) with a reusable
instrument; feeds the epistemic-games programme a concrete empirical object and `rl_eval_generator` a
family. H2 confirmed ⇒ a depth-frontier measurement worth publishing on its own. H0 ⇒ the family is a
surface-robustness diagnostic; still a shipped capability. H3 ⇒ transcript-faithfulness becomes the
next seed. O5 ⇒ positive capability evidence and the family becomes a standing regression test for
future models. No branch is empty-handed, which the brief required.

## 9. Prior work and the surviving wedge

Checked this session by web search on 2026-10-02 [S], plus items inherited from the mission-02
prior-work records: game-play batteries (GTBench [V-inherited], TMGBench, GameBench [S];
LLM-Coordination [S]; MultiAgent-Bench [S]; elimination_game [S]) evaluate play quality or coordination
*outcomes* in natural-language games; none holds facts fixed while varying delivery structure, and none
uses an exact epistemic oracle on the primary outcome (MultiAgent-Bench scores with an LLM judge [S]).
DEL puzzle QA (MindGames, Hi-ToM [V-inherited from `mission-02/council/prior_work_killer.b.md`]) is
question-answering, not payoff-based decisions. The mechanism itself is classical [R][L01][L02][L07];
no novelty is claimed for it. **Surviving wedge:** the public-vs-chain delivery manipulation with an
exact oracle and dose-response, as an LLM behavioural instrument. Residual collision risk: an
unpublished 2026 artifact doing exactly this; the Council's Prior-Work Killer should attack with the
compiled pack in `context/prior_work_killer.md`.

## 10. Evolution of rl_eval_generator (EIGHTH)

Specified, not implemented (the runtime repo is absent from this workspace):

- `envs/epistemic_depth/` — generator + sampler + renderer (frozen templates); config schema for
  profile, arm, cover, depth; registry entry with `REFERENCES`-style hardening from day one.
- `oracle.py` + `oracle_crosscheck.py` (closed form vs exhaustive enumeration) and the all-instance
  agreement test.
- Adversarial variants: misleading framing sentences that do not change the epistemic model (register
  at freeze); held-out variants: unseen profiles, cover 3, endogenous-game v2 where the oracle computes
  the rationalizable profile by iterated dominance over the finite type space.
- Metrics module: ρ, paired contrasts, cutoff estimation, Brier; episode artifact schema compatible
  with the arena's JSONL logging (per the sources note's verified plumbing).
- Docs and tests: 50-seed determinism, parser tests, degenerate-policy hardening, label-swap symmetry.

## 11. TRY TO KILL IT (NINTH)

| Attack | Answer in the design |
| :--- | :--- |
| Memorized email-game text (CF03/CF08) | Three covers, one held out; unseen parameters in FALS-03; abstract action labels; if cover 3 behaves differently, the finding is bounded and says so. |
| Surface length/wording (CF01/CF05) | PADDED arm, LABEL-SWAP arm; H0 is an explicit outcome, not a threat. |
| Numeracy, not epistemics (CF02) | COMPREHENSION gate at a registered threshold before any epistemic claim. |
| Sampling noise (CF06) | m draws per instance; paired intervals by instance; no point estimates in the claim set. |
| Parser/judge artifact (CF07) | Deterministic parser with tests; parse failures reported separately, never silently rescored. |
| Accidental asymmetry | LABEL-SWAP plus symmetric profile pairs (swap G/L roles across profiles). |
| One game construction | v2 endogenous variant + global-game-style payoff profiles registered as follow-on, not claimed here. |
| One model family | Registered limit; replication runtimes are a Gate-2 decision, and the claim ceiling in `seed.yaml` says runtime-specific. |
| Reward hacking | No learned judge, single decision, structured output; nothing to hack. |
| Oracle wrong | Exhaustive cross-check at build; mission-01's lesson that shared-dispatcher agreement is worthless is applied structurally, not rhetorically. |
| Training-data contamination of the *mechanism description* in the prompt | The protocol is rendered from frozen templates with neutral vocabulary; FALS-03 rephrases it. |

**Falsification experiments (registered, max 3 per protocol §).**
- **FALS-01 (surface):** PADDED and LABEL-SWAP arms. Kill condition for H1: the neglect rate on the
  disagreement stratum drops by at least half under padding.
- **FALS-02 (comprehension):** COMPREHENSION and BELIEF arms. Kill condition for any epistemic claim:
  comprehension accuracy below 0.9 on the same instances.
- **FALS-03 (transfer/memorization):** unseen profiles + cover 3 + rephrased protocol. Kill condition
  for rule-use claims: neglect rate on unseen variants inconsistent with seen ones beyond registered
  intervals; also probes the endogenous v2 oracle on a subsample.

## 12. Claim ceiling (restated from the seed)

Behavioural, runtime-specific, family-specific delivery-structure sensitivity, surviving padding,
comprehension gating, one unseen-parameter and one novel-cover variant. Nothing about representations,
deployments, untested models, training causes, or mathematical novelty. Full list in `seed.yaml`.

## 13. Connection to the Strategy IR (SEVENTH, secondary)

The five frozen `game` cards of Mission 02 (`mission-02/freeze/game_cards.freeze.yaml`) were written
for this family; three of them name this mechanism directly: `game-public-announcement-world-elimination`
(trigger: public announcements eliminating worlds), `game-common-knowledge-reachability`, and
`game-level-k-recursion`. If the primary result lands, a natural secondary experiment is whether the
matched card shifts ñ on the CHAIN arm — but that is `mission-03`'s trigger-matching design applied to
this family, and is **future research**, not part of this mission's registered claims. No strategy card
is injected into this mission's arms; the IR stays a secondary object per the brief.

## 14. Not verified / unknown

Any model behaviour; baseline rates on any arm; the current contents of `rl_eval_generator` beyond the
sources note's verified list; whether the arena supports the single-decision episode shape without a
live partner (assumed yes for v1; v3 live protocol play is deferred); all [R] literature statements,
which the Council should check; and whether the ε-independent-message idealization survives rendering
in natural language without leaking cues (a pilot check, FALS-01 adjacent).
