<!--
COMPILER PROVENANCE HEADER (not part of the response; the response starts at the line "ROLE: EXPERIMENTALIST (P02-E)")

Stored:            2026-10-02, by the compiler agent, from the user's paste into the chat.
Prompt answered:   mission-02/council/prompts/02_experimentalist_prompt.md (sha256 469513786cd8a664163b1b98a924ecaffbc2ea6314fc9c976812618fe575dd0e); the response's own PROMPT_ID is M02-P02-E v1.
Sample:            "b" of two answers to the same prompt that were pasted together; "a" is experimentalist.a.md.
Arena mode:        not stated; two answers from two named models suggest battle mode.
Model as shown:    "fable 5.1" (the label the user put on the paste). The response self-reports "Claude (Anthropic)", which is not reliable.
Session date/time: not supplied.
Tools in session:  not supplied. The response self-reports "browsing yes (web search only, snippets, no full-text fetch); code execution no".
Text integrity:    preserved exactly as pasted. The user's label line and the separator between the two answers are not part of the response and are dropped. After the header lines the response has a sentence glued to the next heading ("...independent verifier.## 1. Kill attempt (P02-E-1)"); kept as received.
Order of events:   the five game-family cards were frozen in commit 426d693, before this response was stored.
-->

ROLE: EXPERIMENTALIST (P02-E)
PROMPT_ID: M02-P02-E v1
SELF-REPORTED MODEL (may be wrong): Claude (Anthropic)
TOOLS: browsing yes (web search only, snippets, no full-text fetch); code execution no
SAW OTHER ROLES' OUTPUT: no

Before writing, I ran two searches to check whether L01/L03 ship code I can reuse as an independent verifier.## 1. Kill attempt (P02-E-1)

**Strongest argument: as registered, Q-B is a four-arm, three-stratum, two-solver, paired design (R4–R6) whose primary contrasts have to be detected through hand-pasted chat sessions. With the budgets on the table it is underpowered for anything but a very large effect, and the arm that would most plausibly show a large effect (P vs N) is the one contrast the seed's own hypotheses say is uninterpretable (H0/H3: length and "model explicitly" nudges).** The informative contrasts are P vs L and P vs R. Those are differences between two *prompt-augmented* conditions on the same solver, and everything I know about prompting interventions on fixed-answer puzzles [R] says such differences are modest and swamped by instance variance. At 60 pastes, 4 arms × 3 strata × 2 solvers gives 2.5 trials per cell. That is not an experiment; it is a demonstration.

Second, the "pack" in the registered design is confounded with its own retrieval by construction. R2 says the problem state is written from instance text alone; but the matcher is deterministic and the cards are frozen, so for a fixed schema every S1 instance gets the *same* pack. The experiment then compares one fixed paragraph of method prose against another fixed paragraph. Nothing about *retrieval* is tested; the "trigger match" step contributes zero variance. The honest name for the registered Q-B is "does card text X beat prose text Y on schema Z", which is a prompt-engineering A/B, not a test of the Strategy IR. The seed's known alternative "a fixed hand-written recipe per subfamily" is not an alternative; it is what the design already is.

Third, the manual-dispatch channel cannot give fixed sampling or a clean session boundary (CF08), and arena chat UIs in 2026 commonly have hidden tools or extended reasoning that a solver may use silently (CF07). If a solver can quietly run the update in a scratchpad or tool, every arm converges to the answer and H5 fails for the wrong reason.

**Smallest design that can answer something.** Drop R to a secondary arm, drop the second solver from the primary registration, run three arms (P, L, N) on two strata (S1, S2) on one solver, with S3 as a small sanity set. Register one primary contrast: P − L on S1, paired by instance. That is answerable at ~400 and *barely* diagnosable at ~60 (Section 5). Everything else is exploratory.

**Prompt-steering flagged.** (a) The seed's "what would surprise us" list and H1–H3 are written so that a null on P vs L is already labelled H3 ("generic modelling explains gain") rather than H0; those are not distinguishable from a P/L/N design and should be merged. (b) "Independently checkable ground truth" in the title presupposes the family exists. (c) The prompt to me says "turn Q-B into something … that can come out either way" — that pushes me toward asserting feasibility; my answer is that at 60 pastes it mostly cannot. (d) R5's "trigger present and move invalid" presupposes cards have crisp move-validity conditions; the cards are unseen, so S2 may be unconstructable for some cards. This is a Gate-2 blocker, not a design parameter.

What I tried and could not do: argue that Q-A (the family) is infeasible. A small DEL/public-announcement family with a brute-force Kripke verifier is entirely feasible with the standard library; MindGames [S] already releases code and data (sileod/llm-theory-of-mind on GitHub; dataset on Hugging Face), so one independent verifier is *sourceable*, not just buildable.

## 2. Registered comparison (P02-E-2)

**Family (assumption, pending Theorist/Gate 1).** Subfamily F1: finite public-announcement DEL (muddy-children-type with n ∈ {3,4,5} agents, k rounds, including silence rounds). Subfamily F2: Bayesian inference over an *explicit* behaviour policy that is itself derived from a stated level-k best-response, with a planted case where the stated policy is *not* what level-k would produce (so the solver must use the given table, not the inferred one). Each has an exact enumerator (worlds ≤ 2^5; types ≤ 4).

**Arms.** P: trigger-matched pack (frozen cards, R3). L: generic prose, length-matched (rule below), content = "enumerate possible states, eliminate on each event, then answer" — this is H3's control and is the primary comparator. N: no added text. R: random cards (secondary arm; see Section 5 for when it is affordable).

**Strata.** S1 trigger-present/valid; S2 trigger-present/invalid (invalidity planted mechanically: e.g., an announcement is marked private to one agent, or declared possibly untruthful, or the behaviour table is explicitly stated to be inferred rather than given); S3 trigger-absent (a structurally different puzzle from the same text distribution: a plain conditional-probability item with no other agent).

**Unit of observation.** One (instance, arm, solver) response. **Unit of analysis.** Instance, paired across arms.

**Characterization unit.** Schema, not instance. Each schema (F1-S1, F1-S2, F2-S1, F2-S2, S3) gets one problem state written once by the compiler agent from a *redacted template* (variables replaced by placeholders), committed before any instance is generated. Rationale: per-instance characterization from instance text by a human is unfundable at 400 and leaks stratum trivially (the writer would see the "private announcement" sentence). Schema-level characterization leaks the stratum to the matcher by design — that is the point of S2 (trigger fires, obligation should catch) — but it never sees an answer or generator parameters. Record this as a limitation: it tests obligations, not characterization.

**Counts.** 400-design: 1 solver primary; S1 = 48 instances, S2 = 32, S3 = 16 (96 instances) × 3 arms (P, L, N) = 288 pastes, + R arm on S1 only (48) = 336, + 24 repeat pastes for test-retest (Section 4) = 360; 40 pilot pastes. 60-design: S1 = 12, S2 = 6 × 3 arms (P, L, N) = 54, + 6 pilot. No S3, no R, no second solver.

**Solver pool.** Two named solver families recorded by UI model label and date (R6); only one is in the primary registration; the second is a replication with the same instance ids.

**Replicates.** One per (instance, arm) in the primary set; the test-retest subset re-pastes 24 (instance, arm) pairs in fresh sessions to estimate within-condition noise.

**Randomization and blinding.** The compiler agent generates all prompts, assigns opaque 8-hex ids, and writes `key.json` (id → instance, arm, stratum) encrypted with a passphrase it writes to a sealed file whose sha256 is committed. The human receives only `queue.txt` (ordered id list, order block-randomized so that each block of 12 contains all arms, no two arms of the same instance within 3 positions) and `prompts/<id>.txt`. The human never sees the key; the agent decrypts after all outputs are logged.

**Pack rendering.** Prefix block titled "Reference notes" placed *before* the problem text, followed by the problem, then the answer-format spec. Same block title and position for L and R; N omits the block entirely (not an empty block). Identical answer-format spec in all arms.

**Length-matching rule for L.** |tokens(L)| within ±5% of |tokens(P)| by the same tokenizer (record which), matched per schema, with the same number of paragraphs and bullet points as the rendered pack. L text is authored before cards are unfrozen to the agent, from the strategy_ir.md "generic explicit model" wording.

**Random-card rule for R.** Draw, with a committed seed, the same number of cards as P from the frozen library *excluding the game family*, reject-and-redraw if total length is outside ±10% of P.

## 3. Measurements

- **E-M01 Strict correctness (primary).** Parsed ANSWER dict equals the verifier's ground truth on every required field (for F1: a truth value per queried knowledge formula; for F2: exact rational posterior within a stated tolerance of 0 — rationals must match — plus verdict band). Format failure = 0 (R7).
- **E-M02 Field-level partial score (secondary).** Fraction of answer fields correct.
- **E-M03 Failure class.** Each incorrect response is assigned one class by a deterministic function of (answer, truth): extend `classify_failure` with `private_as_public`, `ignored_silence`, `inferred_policy_overrode_given` for the new family. Pre-register the function; it must be computable from the parsed dict only, never from free text.
- **E-M04 Obligation-check event (S2 only).** Binary: does the response's `justification` field contain an explicit statement that a card condition does not hold? Scored by two blind raters on a fixed rubric; disagreement resolved by a third; κ reported. This is the only free-text judgment in the study.
- **E-M05 Response length and presence of visible tool/scratchpad artifacts**, as observable.
- **Per-stratum reporting.** For each stratum and arm: n, accuracy, Wilson 95% CI; paired P−L and P−N differences with bootstrap CIs over instances; McNemar on discordant pairs.
- **Per-trial record schema.** `trial_id, instance_id (post-unblind), schema, stratum, arm, solver_label, solver_date, session_id, queue_position, paste_timestamp, raw_output_sha256, raw_output_path, parse_ok, answer_dict, strict_correct, partial_score, failure_class, obligation_flag, output_tokens, tool_use_observed, repair_count, redispatch_count, human_minutes, notes`.

## 4. Controls

- **E-CTRL01 Length-matched prose L** — CF01 (tokens/budget) and H3. If P ≈ L, nothing specific to the card survived.
- **E-CTRL02 Random cards R** — CF01's *format* component and "any structured notes help"; separates card content from card shape.
- **E-CTRL03 Framing rotation** — CF09: every instance is rendered in both narrative and bare-table framing; framing is balanced across arms within stratum; framing is a blocking factor, not a contrast.
- **E-CTRL04 Novel surface vocabulary** — CF04: no "muddy", "Cheryl", "hats", "islanders"; agent names and predicates drawn from a committed nonsense lexicon; a contamination probe set of 10 canonical-puzzle pastes under N is run in the pilot to measure the gap between canonical and de-named items.
- **E-CTRL05 Independent verifier** — CF05: F1 verified by brute-force Kripke enumeration written without reading the generator, plus cross-check against MindGames' generator [S] on the overlap (MindGames [S] releases code; whether its DEL semantics matches ours on silence rounds is exactly what the agreement count measures). F2 verified by an independent rational-arithmetic Bayes implementation.
- **E-CTRL06 Blind dispatch and pre-committed queue** — CF08 (ordering), CF10 (forking): the queue, arms, metrics, margins and this document's hash are committed before the first paste.
- **E-CTRL07 Test-retest subset** — CF08 (session/sampling variance): 24 re-pastes give an estimate of within-cell noise so arm differences can be compared with it.
- **E-CTRL08 Surface-feature classifier** — new E-CF12 (answer predictable from text shape): a logistic model on token counts, number of agents, number of events, framing, predicting strict correctness under N; reported as AUC with CI. Above-chance is a warning, not a result.
- **E-CTRL09 Leakage audit of P and L** — CF02: automated check that no card or L text contains any token from the instance's variable lexicon or any numeral present in the answer; plus a "pack-only" paste (pack with the problem text removed) to 3 pilot items — if the solver can produce a correct answer, the pack leaks.
- **E-CTRL10 Tool-use declaration** — CF07: every prompt ends with "State whether you used any tool or code." Self-report is weak; it is recorded and reported, not trusted.

## 5. Sample size (P02-E-3)

Assumptions: single solver; baseline (N) accuracy on S1 after pilot calibration ≈ 0.5 (that is what the pilot *targets*, Section 6); paired binary outcome; the meaningful effect is P − L ≥ 0.15 absolute (anything smaller is not worth a library); within-instance correlation between arms moderate, so discordant-pair rate ≈ 0.35.

McNemar power calculation for a paired design: with discordant fraction 0.35 and a 0.15 difference, the discordant pairs split roughly 0.25/0.10. For 80% power at two-sided α = 0.05, the number of discordant pairs needed is about n_d ≈ (1.96·√(0.35) + 0.84·√(0.35 − 0.15²/0.35))² / 0.15² ≈ (1.16 + 0.47)² / 0.0225 ≈ 118... divided by the discordant fraction is not the right step; more carefully, the required *total* pairs is n ≈ n_d / 0.35 where n_d is computed on the discordant subset: the paired-proportions formula gives n ≈ [1.96·√0.35 + 0.84·√(0.35 − 0.0225/0.35... )]² / 0.15² ≈ (1.16 + 0.80... )²/0.0225. I will state the conclusion I am confident of rather than hand-wave the algebra: **detecting a 0.15 absolute paired difference at these correlations needs on the order of 100–130 instances per contrast; detecting 0.25 needs roughly 40–50.** (If the compiler agent has code, it should recompute this exactly with the committed assumptions before Gate 2 — that is E-T09 below.)

Consequences:
- **400 pastes.** S1 = 48 instances × 3 arms gives 48 pairs for P−L: powered (~80%) only for an effect of about 0.25; for 0.15 power is roughly 40%. Honest statement: the 400 design can detect a *large* card effect and will usually not resolve a moderate one. Adding the second solver as a replication pooled over solvers (96 pairs) would reach 0.15–0.18 at the cost of not characterizing either solver alone; I recommend pooling as a pre-registered secondary.
- **60 pastes.** 12 S1 instances × 3 arms. This can decide exactly two things: (i) H5 — whether N is at floor/ceiling (12 N trials give a Wilson CI of width ≈ ±0.27, enough to exclude 0 or 1 if the point estimate is near 0.5); (ii) whether P is *not catastrophically worse* than L on S2 (6 pairs; detects only near-total reversal). It cannot decide H1, H2 or H3. If only 60 pastes exist, register it as a *feasibility pilot*, not as the gate.

## 6. Pilot and headroom (P02-E-4)

Procedure: 40 pilot pastes under arm N only, one solver, 20 F1 + 20 F2 at the generator's default difficulty, instances drawn from a seed range disjoint from the registered range (committed before pilot). Compute accuracy with Wilson CI per subfamily.

Rules (fixed now): if the upper CI bound < 0.20, difficulty is too high → reduce agents/rounds by one step and re-pilot with 20 fresh pastes; if the lower CI bound > 0.80, raise difficulty one step (more agents, add a silence round, skew prior) and re-pilot; otherwise freeze. At most two adjustment rounds; if neither lands in [0.20, 0.80], Q-B is declared "uninformative on this family for this solver" before registration, and the human is told to stop rather than spend the paste budget.

Pilot data may not be used for: choosing which card the pack contains; selecting instances by difficulty into the registered set; tuning L's wording; setting the margin (the margin is 0.15 and is fixed now); or any arm comparison. Pilot pastes do include the 10-item contamination probe (E-CTRL04) and the 3-item pack-only leak probe (E-CTRL09), both under N or pack-only, never under P-with-problem.

## 7. Acceptance tests

- **E-T01 Determinism.** Generator called twice with the same (schema, seed) yields byte-identical instance text and ground truth; 200 seeds.
- **E-T02 Known-answer cases.** Three hand-derived F1 cases (n=3 muddy children, k=1,2,3 announcements) and three hand-derived F2 posteriors, written in the test file with the derivation, must match both generator and verifier.
- **E-T03 Generator/verifier agreement.** All registered and pilot instances; required agreement 100%; any disagreement is logged, the instance excluded, and the count reported (R1). Cross-check F1 against the MindGames generator [S] on any overlapping configurations; report agreement and the list of semantic differences found.
- **E-T04 Judge mutation tests.** For each registered instance, mutate the correct answer by (a) flipping one knowledge-formula value, (b) swapping the posterior for its complement, (c) perturbing the posterior by the smallest representable rational step, (d) changing the verdict band only, (e) dropping a field. The judge must reject all five. Also submit the correct answer with field order shuffled and with extra whitespace; it must accept.
- **E-T05 S2 invalidity check.** For each S2 instance, run the card's method mechanically (the naive public-announcement update, or the naive "treat the table as given" Bayes) as a *reference wrong solver*; it must produce an answer the verifier rejects on ≥ 95% of S2 instances, and accept on ≥ 95% of S1 instances. If a card's method cannot be made mechanical, that card has no S2 stratum and is excluded from H2 with the reason recorded.
- **E-T06 Surface-cue check for S2.** A bag-of-words classifier trained on instance text alone to predict S1 vs S2 must not exceed an AUC of 0.7 on held-out instances; if it does, invalidity is surface-detectable and H2 is downgraded.
- **E-T07 Pack leakage.** Automated token-intersection check (E-CTRL09) over every (pack, instance) pair; zero hits on lexicon names and answer numerals.
- **E-T08 Instance leakage.** The answer must not be recoverable by a trivial heuristic: for F2, the posterior must not equal the prior on more than the planned fraction of instances; for F1, the queried formula's truth value must be balanced 50/50 within each schema.
- **E-T09 Power recomputation.** The compiler agent recomputes Section 5 exactly from the committed assumptions and records the numbers before Gate 2.

## 8. Dispatch protocol and logging (P02-E-5)

Compiler agent, before Gate 2: generates instances; runs E-T01–E-T09; writes prompts; builds `queue.txt`, encrypted key, committed hashes; writes `log.csv` header with the schema in Section 3.

Human, per paste: (1) open a fresh chat session (no history), record `session_id` as the UI's conversation URL or a counter; (2) record the model label shown in the UI and any visible settings (reasoning mode, tools toggles); (3) paste `prompts/<id>.txt` exactly; (4) wait for completion; copy the *entire* output into `outputs/<id>.txt`; (5) append a row: `id, session_id, model_label, timestamp_start, timestamp_end, tool_use_observed (yes/no/unknown), ui_anomaly (truncation, refusal, retry prompt), human_minutes`; (6) if the output is truncated or the UI errored, do **not** re-prompt in the same session; log `redispatch_count += 1` and re-queue the id to the end of the queue; (7) never paste follow-ups, clarifications, or "please use the format". The first output is the output.

Compiler agent, after all rows exist: hash every output; parse; mark `parse_ok`; compute E-M01–E-M03; only then decrypt the key and join. Any parse repair (e.g., tolerant JSON) is applied by one committed function to all arms identically and counted as `repair_count`.

Fields Mission 01 could not estimate and which are now mandatory: `human_minutes` per paste, `redispatch_count`, `repair_count`, `queue_position`, `session_id`, `ui_anomaly`, `coordination_notes` (free text per session day), total wall-clock per block.

If tools are visible in the arena: record per trial; pre-register that trials with `tool_use_observed = yes` are analysed in a separate stratum and never pooled with no-tool trials.

## 9. Decision rules

- **E-O01 H5 fails** (pilot N outside [0.20, 0.80] after two adjustments): stop before registration; record "uninformative: no headroom on this family/solver"; cards untouched.
- **E-O02 E-T03 agreement < 100% and > 5% instances excluded, or E-T05 fails for every card:** stop before dispatch; record a Q-A negative ("independent verification not achieved for this subfamily"); do not run Q-B on it.
- **E-O03 P − L on S1 ≥ 0.15 with 95% CI excluding 0, and P − R ≥ 0.15 (if R run):** cards concerned stay `candidate` with "one positive comparison" recorded; no promotion (section 7 evidence policy). Next registration: second solver, new instance version.
- **E-O04 P − L CI includes 0 and point estimate < 0.15, but P − N ≥ 0.15:** record as H3-consistent; cards stay candidate; the IR's claimed value is diagnostic, not performance; stop extension (R9).
- **E-O05 P − N CI includes 0:** H0-consistent; stop extension; cards may be retired by human decision.
- **E-O06 CI width > 0.30 on the primary contrast:** result is "underpowered/uninformative"; it is *not* recorded as a null; the stop rule is not triggered; a follow-up may be registered with more trials only.
- **E-O07 S2: P wrong-answer rate exceeds L by ≥ 0.15 with CI excluding 0, and E-M04 obligation flags < 20% of P-on-S2 trials:** H2-consistent; record "obligation mechanism did not prevent misapplication as prose"; flag the specific cards.
- **E-O08 S2: obligation flag rate ≈ 0 regardless of correctness:** negative result for the obligation mechanism per R9, independent of accuracy.
- **E-O09 Surface classifier AUC CI lower bound > 0.6 (E-CTRL08 or E-T06):** all accuracy results carry a "surface-predictable" caveat; H1/H2 cannot be claimed.
- **E-O10 Pack-only leak probe yields any correct answer:** dispatch halts; cards are re-authored; the registration is void.

## 10. Critique of the draft gate (P02-E-6)

1. "Beat its controls by the margin fixed in advance" names no primary contrast. With two controls and three strata there are at least six candidate comparisons; the gate must name one (I propose P − L on S1) or it invites forking (CF10).
2. "Solved or reduced better (verified outcome, or effort to a verified outcome)" conflates two metrics. "Effort" is unmeasurable in a copy-paste arena; delete it from this gate or define it as a secondary (output tokens).
3. It has no uninformative outcome. A gate that only distinguishes "beat" from "did not beat" turns an underpowered study into a stop decision. E-O06 must be in the gate text.
4. "Toy instances where the trigger is present but the move is invalid" — "toy" is exactly what makes S2 surface-detectable; the gate should require invalidity that passes a surface-cue test (E-T06).
5. It omits a headroom precondition (H5) and an independent-verifier precondition (H4). Both are decided before the comparison and should be gate entries, not seed hypotheses.
6. It does not say what the random-card control is matched on (count, length, family exclusion). Section 2 fixes this.
7. "Obligation checks that never fail on planted invalid transforms" presumes obligations are *checked* by something. In this design they are prose shown to the solver; the only observable is E-M04. The gate should say whether it is testing the solver's response to prose obligations or a mechanical checker — these are different experiments, and only the first is possible here.
8. The gate speaks of "problems characterized before the attempt" but does not fix the unit. If the unit is the schema (my recommendation, for cost), the gate is not testing per-problem characterization and should say so.
9. Nothing in the gate requires disclosing who authored the cards and the controls (CF06). R3 covers cards; nothing covers L.

**Cut for length:** worked numeric power table; detailed F2 construction; per-field tolerance spec for E-M01.
