# Mission 03 proposal: does matching a strategy to a task's structure matter?

**Status.** Pre-Council proposal, written 2026-10-02. Nothing has been run and no model was called. Two human decisions were recorded on 2026-10-02 (`decisions/human_decisions.yaml`): margin 0.15, pilot on Atria-Dawn-Preview alone. Facts about the two repositories were checked against their files on that date; what was not checked is marked *unknown*. Files: `seed.yaml` (protocol seed), `candidate_measurements.yaml` (measurements, controls, stop conditions, decision regimes, falsification tests), `work_packages/candidates.yaml`, `analysis/power_simulation.py` with `power_table.json`.

## 0. In short

- **Question.** On environments with executable ground truth, does a strategy card chosen because its trigger matches the task raise the pass rate more than a card whose trigger does not hold, and more than length-matched generic advice or nothing?
- **Comparison.** A symmetric crossover: two frozen cards (elimination, counterexample) by two task families (ML debugging, weird-machine solver synthesis). Each card is the matched card in one family and the mismatched card in the other, so card quality and family susceptibility cancel in the primary contrast S. A generic length-matched arm and a direct arm complete the design.
- **Gates before spend.** A blind characterization stage (no solver cost) and a pilot can stop the mission before the roughly 800-episode comparison.
- **Honest limit.** At 100 runs per arm per family a true 15-point S is detected with probability about 0.88; a true 10-point S only about 0.57. The mission can rule out large effects. It cannot reliably see small ones.
- **Recommendation.** Run Stage 0 first. It costs almost nothing and tests the weakest link of the IR. Run the rest only if it passes.

## 1. The question, and what was wrong with the first formulation

The candidate in the brief was: *does explicit, trigger-matched use of a transformation improve problem solving compared with direct solving?* Three problems.

1. **Card versus direct measures any helpful instruction.** A card adds text, a workflow nudge and a spent-steps cost. A gain over direct solving cannot be credited to the transformation.
2. **One card on one family cannot show that selection matters.** The IR's claim is that the right card can be found from the problem's structure. That needs a case where the same card text is applied where its trigger holds and where it does not.
3. **"Trigger-matched" means nothing unless matching was done blind.** If the experimenter decides which card fits, the matching is circular.

The primary contrast is therefore **S = ½ [(own − other) in family 1 + (own − other) in family 2]**, paired by instance, with matching decided by two independent characterizers who never see the cards.

## 2. What in the Strategy IR is testable now

| Component | Status in the repository | Testable now? |
| :--- | :--- | :--- |
| Trigger matching (`retrieve_strategies.py`) | deterministic, unit-tested | Mechanics: done. Whether matches are *useful*: no evidence. This mission. |
| Problem characterization (`problem_state`) | schema and validator; truth of the content is a human or agent judgment | **Yes, cheaply: inter-rater reliability.** No data exist. Stage 0. |
| Feature vocabulary (25 features) | proposed, unvalidated | Partly: Stage 0 shows which features two raters can apply. |
| Cards as hypotheses | 13 candidates, none with evidence | Yes: the crossover tests two. |
| Obligations as guards | the validator checks recorded statuses only | Not here. Needs planted invalid transforms. |
| Composition, episodes, specialization | structural schema; both shipped episodes are illustrative and carry no weight | No. Needs multi-step problems. |
| Promotion policy | a human gate | Not a testable claim. |
| 12-family ontology | one person's first reflection | Not tested. Stage 0 evidence may inform a later revision; none is proposed now. |
| "Problem-solving calculus", runtime, swarm | aspiration, excluded by the brief | Not testable, not tested. |

## 3. Where to test it: what the repository offers

All 34 registry entries were inventoried (`envs/registry.yaml`, the oracle gate's `REFERENCES`, each config, and the prompts of the candidates). The `rl_eval_generator` README and Mission 01's seed say 35; the registry has 34, and their own "12 hardened + 22 compile-only" adds to 34.

| Candidate | Ground truth | Cost per run | What the prompt withholds | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| `moco` | hardened reference; Mission 01: 0 of 5 bypass variants accepted | torch and Docker; 10 epochs on 4,000 samples per training run | the causes (symptom only; "at least two bugs"), plus red herrings and a symptom mask by axis | **Family 1** |
| `regex_state_machine`, `sql_fixed_point`, `css_state_machine`, `spreadsheet_dataflow`, `template_interpreter` | hardened reference; 0 of 5 accepted each | seconds (stdlib or sqlite; the regex judge imports torch) | nothing about the target, which is stated; the visible test is minimal, the hidden test broader | **Family 2** |
| `glyph` | hardened | about 8 minutes per local run (the oracle gate's own comment) | causes | excluded: cost |
| `rope` | hardened | heaviest: several files, paper tools | causes | reserved as a replication family |
| `ci_dependency_graph` | hardened, but a bypass was accepted in Mission 01 | seconds | n/a | excluded: judge fault |
| `epistemic_games` | hardened | seconds | n/a | excluded: the only fitting card is an answer hint (see `strategies/cards/game-policy-likelihood-identifiability.yaml`), and the family belongs to mission-02 |
| `rd_state_carry` | hardened | small torch | the prompt states the invariant | excluded: nothing to select |
| `ts_*`, `batchnorm_ema`, `rd_adaptive_halting`, `rd_gradient_credit`, other `cat_theo` | compile-only judges (no behavioural reference); `ts_*` is small solver writing with horizons up to 510 | n/a | n/a | excluded |
| `categorical_lenses` | hardened, but bypasses accepted in Mission 01 | torch | n/a | excluded |

Two findings from this search shaped the design.

- **The weird-machine prompts state the target computation and the substrate** (checked in all five). Their visible tests have one to five assertions, and every judge randomizes over larger trial sets. The SQL prompt even says that recursion can compute fixed points, and lists cycles and self-loops as requirements that its own visible test (a three-node chain) does not exercise; the CSS visible test ships a rule evaluator, so an exhaustive check over 2^n inputs (n of 3 to 5) is cheap for an agent that thinks to write one. What is hard there is implementation and untested generalization, not recognizing the kind of problem. A card about *diagnosis* should not fit these; a card about *searching for violating inputs* plausibly does.
- **moco withholds the causes.** The agent is told the symptom and that two bugs exist. The README says symptom masks "divert agents into intuitive but wrong fixes". A card about *discriminating between competing causes before patching* plausibly fits.

Both are **hypotheses about where each family's bottleneck lies**. The pilot checks them against the direct arm's own failures.

Not claimed: that these tasks are strategy-sensitive. Baseline pass rates do not exist; `rl_eval_generator/runs/` holds five-case rehearsal smoke runs only.

## 4. The comparison

### 4.1 Cards, families, matching

- Cards: `elimination-discriminating-test-ordering` v1 (E) and `counterexample-minimal-failure` v1 (C). Both were written on 2026-10-01, before any of these prompts were read, are domain-neutral, and are unreviewed candidates. Frozen by hash at Gate 2.
- Matching is **not decided by the compiler**. Two independent characterizers see only the feature vocabulary and each environment's agent-visible text. A feature is present or absent only if both agree. The matcher runs on the consensus: *own* = matched, *other* = blocked by a consensus absence. The compiler's non-blind expectation (moco: E; weird machines: C) is recorded in `candidate_measurements.yaml` so the blind result can be compared with it.
- If the consensus does not give moco and at least three weird-machine environments a clean own/other pair, Stage 0 stops the mission (ABORT-01). That outcome is a finding about the vocabulary.

### 4.2 Arms

| Arm | System prompt gets | Rules out |
| :--- | :--- | :--- |
| A direct | nothing | baseline; floor and ceiling |
| B generic | a content-neutral working-method block, same wrapper and length band as a card block | extra text, verbosity, "think harder" |
| C own card | the block of the card the consensus matches | the treatment |
| D other card | the block of the card the consensus blocks | extra text, card format, random selection, card quality (via the crossover) |
| P (pilot only) | a true, partial, domain-specific hint | an apparatus that cannot see effects |

Card blocks come from one deterministic renderer: name, when it applies, diagnostic questions, the move, obligations, failure modes. The block goes in the **system prompt**: the runner trims history from the oldest message after the system prompt, so a block placed in an early user message would be deleted mid-episode.

### 4.3 Unit, sampling, randomization, runtime

- **Observation:** one episode (instance × arm). **Pairing unit:** the instance, played under all four arms back to back in a seeded random order. **Cluster for intervals:** the instance in moco; the agent-visible (environment, vector) cell in the weird machines, because their prompts do not change with the seed.
- **Sampling:** vectors drawn by a seeded rule from each family, excluding the known gate-blocked vectors; each must pass the instance-oracle gate and match its fingerprint at reset. Pilot seeds are disjoint from Stage 2.
- **Runtime:** the Atria campaign's settings (Atria-Dawn-Preview, temperature 1.0, top_p 0.95, 20 steps, 8192 tokens, Docker). One model is a stated limit.

### 4.4 Measures

- **Primary:** strict judge pass (verdict PASS: score at least 0.85 and the anti-gaming check passed). Failures to submit and API failures count as failures.
- **Secondary:** judge score; judge failure mode (coarse: most failures end as `underfit`); the contrasts Own − Generic, Own − Direct, Generic − Direct, Other − Direct.
- **Trace-derived failure classes (rules, no grading):** no submission; step budget exhausted; invalid-action loop; passed the visible test but failed the judge; edited before any diagnostic; edited only files the reference patch does not touch. Checked: the judge's `overfit_visible_tests` label means the anti-gaming check failed, so the visible-versus-hidden class must come from the trace.
- **Behavioural uptake (never self-reported; the agent is told not to explain):** read-only actions before the first edit and the step of the first edit (for E); a self-authored enumeration or check run before submitting (for C); visible-test runs after the last edit (generic).
- **Cost:** provider tokens (from logged usage), calls, steps, seconds, retries, and window pressure. The block eats part of the 28,000-character window that arm A keeps, so Own − Direct is biased against the card. Own − Other and Own − Generic are not.

### 4.5 Stages and stop rules

| Stage | What | Stops the mission if |
| :--- | :--- | :--- |
| 0 | blind characterization of the 12 hardened environments, matcher run | kappa below 0.6 on any trigger feature of E or C, or no clean own/other pair (ABORT-01) |
| 1 | instance gate, then pilot of about 12 instances per family on arms A–D and P | gate pass rate below 80% (ABORT-02); direct pass rate outside 0.20–0.80 (ABORT-03); hint adds under 0.15 (ABORT-04); card uptake under +15 points or 1.5× direct (ABORT-05) |
| 2 | registered comparison, arms A–D, fixed size, no interim efficacy analysis | call ceiling (ABORT-06) pauses it |

After Stage 2, three falsification tests run: a within-instance label permutation, leave-one-environment-out, and an uptake-split mediation check (`candidate_measurements.yaml`). The claim ceiling is `candidate_claim_ceiling` in `seed.yaml`.

## 5. Trying to kill it

| Attack | Verdict | Answer in the design |
| :--- | :--- | :--- |
| "It is a prompting trick." | True of Own − Direct alone. | The registered primary is S. Own beating Direct with S near zero is reported as structured advice (H2), not as support for trigger matching. |
| "The treatment cannot be operationalized unambiguously." | Mostly answerable. | One deterministic renderer from frozen files, same wrapper and length band in every arm, hashes recorded. Residual: wording. |
| "There is no plausible null." | There are four (H0, H2, H3, H4). | Each has a distinguishing observation. |
| "You cannot tell whether the strategy applied." | Not from the task text by the compiler. | Blind consensus; behavioural uptake from traces. |
| "More tokens or context, not strategy." | The standing confound. | Arm B and arm D carry equal-length text; token use and window pressure are covariates. |
| "One hand-picked task." | Family 1 is one environment. | Family 2 has five task types; leave-one-out; rope reserved. The claim ceiling is limited to the sampled families. |
| "The cards are already native behaviour." | Possible. | The pilot measures the direct arm's own uptake rate (ABORT-05). |
| "Floor or ceiling." | Possible; no baseline exists. | ABORT-03. |
| "The apparatus cannot see an effect." | Possible. | The pilot hint arm (ABORT-04). |
| "The two cards both just mean 'be careful'." | Partly true; it shrinks S and makes a null ambiguous. | Stage 0 requires consensus *absences*; Own − Generic is reported beside S; the ceiling says so. |
| "A null would teach nothing." | False if the gates pass. | It rules out effects of at least the margin for this runtime and these cards. |
| "Forking paths." | Real. The pair and families were chosen by the compiler after reading prompts. | Disclosed (CF14). Margin, size, instance list, arm texts and analysis script are hashed before Stage 2. |

The strongest confound is **relevant advice versus a structural transformation**. A card that fits may help only because it is relevant, careful-sounding advice. The crossover addresses it without eliminating it: the card's generic component appears in both own and other arms and cancels, and arm B measures what a neutral nudge does. It remains possible that E and C overlap enough to shrink S; that makes a null ambiguous, not a positive misleading.

## 6. Power and the margin

From `analysis/power_simulation.py` (all assumptions are in its header and in `power_table.json`; the numbers reproduce with `--check`). Baseline pass rate 0.3 or 0.5 gave nearly identical results.

| Runs per arm per family | detect true S = 0.10 | detect true S = 0.15 | rule out S ≥ 0.15 if S = 0 | false positive if S = 0 |
| ---: | ---: | ---: | ---: | ---: |
| 60 | 0.36–0.38 | 0.68 | 0.69–0.75 | ≤ 0.035 |
| 100 | 0.57–0.59 | 0.88 | 0.89–0.94 | ≤ 0.034 |
| 200 | 0.84 | 0.99 | ≥ 0.995 | ≤ 0.025 |

The simulation is a planning approximation (normal test, cluster-robust error). The registered analysis is a cluster bootstrap.

This is why the proposed margin is **0.15**, not 0.10: it is the smallest round margin for which 100 runs per arm give about a 90% chance of a decision either way (detecting the effect if it is there, ruling it out if it is not). The margin is a human decision at Gate 2. If a graded score has lower paired variance than pass/fail, a single pre-registered switch of the primary metric is allowed, on pilot data that never enter Stage 2.

Cost: about 120 pilot and 800 Stage 2 episodes. At an assumed 15 provider calls each (measured in the pilot) that is about 13,800 calls, 1.4 times the 10,050-call ceiling in `experiments/atria_campaign.yaml`.

## 7. What each outcome would mean

Defined in `candidate_measurements.yaml` (O1–O7). In one line each:

- **Positive on S and Own − Generic, with uptake:** trigger-matched selection added value here. Replicate on a second model and on rope before any card leaves candidate.
- **Own and Other both help equally:** structured advice works; the retrieval claim is unsupported.
- **Interval upper bound below the margin:** effects of that size are ruled out; strategy_ir.md section 10's stop rule applies; extension stops.
- **Own below Direct:** the block costs more than it returns.
- **Interval spans zero and the margin:** inconclusive; at most one pre-registered extension.
- **Any gate fires:** uninformative about strategy value, with the failed prerequisite named.

A null with gates passed is still informative. A null with H4 (no uptake) is not.

## 8. Work packages

Eight candidates in `work_packages/candidates.yaml`: WP-01 arm injection in the runner; WP-02 blind characterization; WP-03 arm texts, leak audit and freeze; WP-04 instance set and schedule; WP-05 trace metrics; WP-06 pilot; WP-07 registered analysis script; WP-08 Stage 2 run. WP-01 is the only change to `rl_eval_generator`: the runner has no hook for a treatment block, and the system prompt is a module constant. Everything else lives here or runs the existing tools.

## 9. Relationship to mission-02, and decisions for a human

- `mission-02/` (unrun) designs an epistemic-games family and gates strategy packs on it. This mission does not depend on it and tests the IR's central claim on tasks that already exist, so it should go first. Mission-02's frozen `game` cards are unused here. The directory is called `mission-03` only because `mission-02/` already exists on this branch, with a freeze record that tests protect.
- **Decisions only a human can make:** the margin; 100 or 60 runs per arm; Atria-Dawn-Preview alone or a second model; whether rope joins as a replication family; who dispatches the two characterizers. Two were confirmed on 2026-10-02 (`decisions/human_decisions.yaml`, M03-HD-1): the margin is **0.15** (HD-1a) and the pilot runs on **Atria-Dawn-Preview alone** (HD-1b), with a second model reserved to the replication branch of a positive result as a new decision. Confirmations are not a Gate 2 freeze. Still open: 100 or 60 runs per arm (the design proposes 100); rope as a replication family; who dispatches the two characterizers.
- **Gate 1 should attack:** the choice of the two cards and the two families (a disclosed degree of freedom); the generic block's text; the claim that E and C are structurally distinct; the margin; the uptake rules.
- **Not verified:** any model behaviour; baseline pass rates; the instance-gate pass rate for sampled vectors; calls and time per episode; whether the provider reports reasoning tokens; the blind characterization result. Mission 01's judge audit is bounded evidence of ground truth, not proof.
