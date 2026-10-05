# Source note: the 2026-09-29/30 epistemic-games dialogue and Arena round

**Status.** The compiler agent's reading of material the user pasted on 2026-10-02, after the Mission 02 kickoff commit (`312bc80`) and the card freeze (`426d693`). The compiler had not seen it when it wrote the seed, the four Council prompts, or the five `game` cards. **The dialogue itself is not stored here.** It is long (about 90 KB) and re-typing it risks silent edits; the user holds the original, and this note refers to messages by model label and order. It is **not shown to the Council in round 1**. Nothing in it is evidence for or against any hypothesis in `../seed.yaml`. Statements below are unverified unless a row in section 3 says otherwise.

**Human disposition (2026-10-05).** Keep this dialogue separate from Mission 02 Council round 1. The compiler-prepared cross-critique uses only round 1 Council responses; no amendment to the current seed or prompts is made by this decision. Gate 1 remains a separate human decision.

## 1. What the material is

A ChatGPT conversation (message times 17:12 to 21:25 on 2026-09-29) that moves from epistemic game theory to "control of another agent's epistemic process", stage-magic misdirection, Pelevin's MI-13 and Gilbo's «дезонтологическая атака». The user then ran the conversation through several Arena models (GPT-6 Astra Max, GPT-5.6 Luna, Gemini 3.1 Pro, GPT-6 Sol Max, Opus 5, GPT-5.6 Sol xhigh, Opus 4.8); those outputs are undated. The `knowledge/` graph comes from the same lineage: it has nodes for `alon-2023`, `dbos-2026`, `lying-with-truths-2026`, `potemkin-2026`, `epistemic-process-control`, `pelevin-mi13` and `lefebvre-reflexive`.

## 2. Where the Arena round ended up

"Epistemic Trajectories v0.1", a proposed new Arena track in `rl_eval_generator`:

- A hidden mechanism, a budget of diagnostic tests with known outcome partitions, and a presenter that may reorder and emphasise the *same* atomic facts. The defender's first test is the observable.
- Metrics kept separate: inquiry regret ΔQ (value of the best test minus value of the chosen test), final belief error ΔB (Brier score), terminal loss ΔR. No pooled score.
- Arms: canonical, neutral, helpful, adversarial order, adversarial emphasis, each aware or unaware. A scripted exact-Bayesian defender is the null and must show zero effect.
- Ladder: PR1 domain and oracle; PR2 runner and CLI; PR3 a 50-episode infrastructure pilot; PR4 a preregistered defender experiment; PR5 a model presenter; PR6 recovery and opponent-model ablations.
- Claims discipline: a changed next question is a behavioural effect and does not show that any update rule changed. (Opus 5's formulation: the policy is one function and the conditions are two inputs to it.)
- Rejected inside the dialogue: a capability ladder from belief to recursive control; displacement as damage (`max_m D(G, Update(G, m))`); KL divergence as the inquiry metric; calling order and emphasis effects "attention"; decorative notation.

## 3. What was checked (2026-10-02)

| Claim | From | Status | How |
| :--- | :--- | :--- | :--- |
| `rl_eval_generator` has specialised benchmarks in `arena/trajectory.py`, `trajectory_plan.py`, `trajectory_runner.py`, wired into `arena.py` | Sol xhigh | **verified** | files present on `main` (e1b038a); `arena.py` contains `trajectory-plan` |
| The helpers the v0.1 spec reuses exist: `ProviderClient`, `resolve_credentials`, `resolve_api_base`, `provider_metadata`, `append_jsonl`, `write_json`, `sanitize`, `utc_now`, `enforce_call_guard` | Sol xhigh | **verified** | found by grep in `arena/providers.py`, `arena/artifacts.py`, `arena/trajectory_runner.py` |
| "PR1 shipped": `arena/epistemic.py`, `tests/test_epistemic.py` | Opus 4.8 | **not supported** | absent from `main` and from all 14 `arena/*` branches, as is `docs/epistemic_trajectories_v0.md`. The model may have run code in its own sandbox |
| Pilot numbers. Opus 5: +0.1486 bits, +11.8 pp, frozen-schedule gap exactly 0. Opus 4.8: +0.30 bits and +27.9 pp at budget 1, +0.35 pp at budget 3, about 31% surviving a frozen schedule | Opus 5, Opus 4.8 | **quarantined** | no code or artifacts reached the compiler. Both describe the same shape of pilot (8 hypotheses, 6 tests, budget 3) and disagree |
| Published posts | blog repo | **checked** | `_posts/2026-09-30-the-next-question-is-part-of-the-game.md` and `_posts/2026-10-01-lying-with-truth.md` exist. The first says "No model results yet"; neither contains the unaudited numbers |
| QuestBench; K-Level Reasoning; Kuhn et al. 2014 | several | **exist** | search results, abstracts only |
| LOLA; machine teaching; Bloedel and Segal; Alon 2023; D-BOS; Potemkin; Lying with Truths; Hypergame Rationalisability; AmongUs-X | several | **not checked** | |
| OpenAI's Navier-Stokes post; GPT-6.1 Astra withheld; whether these concern the same model | user, ChatGPT, Astra Max | **out of scope, not checked** | Astra Max notes the sources do not establish that they are the same model |
| Gilbo's definition of «дезонтологическая атака» | user | **the user's own statement; no primary source** | |

## 4. How it bears on Mission 02

1. **The seed does not contain the user's family.** The candidate semantics (a) to (f) in `../seed.yaml` cover specified policies, dynamic epistemic logic, type spaces, level-k, rationalizability and signalling. None is inquiry selection under matched presentation, which is what this material is about. A Council run on the current prompts explores a different family.
2. **Things in the repository the Arena models did not see.** `tools/epistemic_probe.py` already grades answer sources, including graded scripted positive controls (`framing_sensitive_q10/q20/q30`, described as a power check). That is the same idea as the scripted "bounded target" and the natural pattern for the pilot's scripted defenders. `envs/epistemic_games` already has a `framing` axis (narrative versus bare table), a presentation-susceptibility axis for belief inference.
3. **The nearest prior art for a presentation effect lies outside the epistemic literature.** LLM sensitivity to option order and position is documented: Pezeshkpour and Hruschka (arXiv 2308.11483; NAACL Findings 2024) report sensitivity gaps of up to 75% in zero-shot settings, and Zheng et al. (ICLR 2024), "Large Language Models Are Not Robust Multiple Choice Selectors", report selection bias. That a presentation change moves a defender's test choice is the null to rule out first. No model in the paste raised it. Seen only as search results.
4. **Defender-only precedent.** QuestBench (arXiv 2503.22674) already evaluates whether a model identifies the right question to ask. Novelty for the new track would have to rest on the presenter, the matched-fact control and the recovery measures, not on question selection. Seen only as a search result.
5. **A level-k design criterion.** arXiv 2608.21296 (2026) formalises a "level-K distinguishability" condition for evaluating strategic depth with novel game structures. Relevant to semantics (d) in the seed. Seen only as a search result.
6. **The flat belief-displacement result is built into the toy target.** A scripted defender that holds exactly three live hypotheses with a uniform posterior has KL(posterior ‖ uniform prior over 8) = log2(8/3) = 1.415 bits whatever the presentation (computed here). A constant ΔG in that setup follows from the target's definition. It is not evidence that belief-change metrics are blind in general, as the Opus 4.8 draft argues.
7. **The strategy-pack gate has a natural first subject.** Using a characterization written by the compiler after reading the dialogue (so not blind), the real matcher returns exactly one match for the diagnostic device: `elimination-discriminating-test-ordering`. That card was written on 2026-10-01 before this material was seen, and its trigger features (`competing_hypotheses_remain`, `cheap_discriminating_test_available`) describe the device. The five frozen `game` cards do not fire (three blocked by declared absences, two not retrieved). This shows the triggers behave as designed, not that the card helps. The spec's `aware` text ("the ordering may be adversarial; it is not evidence") is itself generic non-strategy prose, a ready-made control for the length-matched arm.
8. **Where code would live.** The generator is a different repository, and this session can push only to its own branch here. A v0.1 implementation would have to be delivered from this repository as files (an independent implementation would also serve as the independent verifier that Q-A asks for) or be built in `rl_eval_generator` by the user.

## 5. Proposed amendment to the seed (not applied; needs the user's decision)

- Q-A becomes: is Epistemic Trajectories v0.1 a valid, informative and novel eval design, and what must change before PR1? Keep semantics (a) to (f), add (g) matched-presentation inquiry selection, presented as a proposal under attack together with the Arena critiques.
- H0 for Q-A: any presentation effect on test choice is known option-order or format sensitivity, not something about inquiry. Add prior-work leads: QuestBench, K-Level Reasoning, Kuhn 2014, the two order-sensitivity papers, arXiv 2608.21296, and LOLA, machine teaching and Bloedel-Segal as the user's models cited them.
- Q-B names its first subject: `elimination-discriminating-test-ordering`, with the spec's `aware` text as the generic-prose arm. The frozen `game` cards stay frozen and unused unless the Council widens the scope.
- Regenerate the four prompts and the hashes in `../council/README.md`. If round 1 on the current prompts has already been run, keep it: it is the one place where unled models either rediscover this framing or do not.
