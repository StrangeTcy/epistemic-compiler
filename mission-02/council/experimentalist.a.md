<!--
COMPILER PROVENANCE HEADER (not part of the response; the response starts at the line "ROLE: EXPERIMENTALIST (P02-E)")

Stored:            2026-10-02, by the compiler agent, from the user's paste into the chat.
Prompt answered:   mission-02/council/prompts/02_experimentalist_prompt.md (sha256 469513786cd8a664163b1b98a924ecaffbc2ea6314fc9c976812618fe575dd0e); the response's own PROMPT_ID is M02-P02-E v1.
Sample:            "a" of two answers to the same prompt that were pasted together; "b" is experimentalist.b.md.
Arena mode:        not stated; two answers from two named models suggest battle mode.
Model as shown:    "opus 4.6" (the label the user put on the paste). The response self-reports "Claude (Anthropic, 2025-2026 generation)", which is not reliable.
Session date/time: not supplied.
Tools in session:  not supplied. The response self-reports browsing yes, code execution no.
Text integrity:    preserved exactly as pasted. The user's label line and the separator between the two answers are not part of the response and are dropped.
Order of events:   the five game-family cards were frozen in commit 426d693, before this response was stored.
-->

ROLE: EXPERIMENTALIST (P02-E)
PROMPT_ID: M02-P02-E v1
SELF-REPORTED MODEL (may be wrong): Claude (Anthropic, 2025–2026 generation)
TOOLS: browsing yes; code execution no
SAW OTHER ROLES' OUTPUT: no

---

## 1. Kill attempt (P02-E-1)

**Strongest argument that Q-B cannot be answered as registered by manual dispatch, or that the likely result is uninformative.**

The kill argument is statistical, not conceptual. Q-B asks whether a trigger-matched pack *improves verified accuracy relative to controls*. With manual copy-and-paste dispatch into arena sessions, the experiment has four arms (P, L, R, N) × three strata (S1, S2, S3) × at least two solver families = 24 cells. The primary contrast is P vs. L on S1. A single trial is one (instance, arm, solver) tuple. With 60 trials total that is ≈2.5 observations per cell—far below the minimum needed for any frequentist or Bayesian inference that can come out either way. Even with 400 trials that is ≈17 per cell. At plausible baseline accuracies (30–70%), the smallest detectable effect at 80% power with n = 17 paired observations is above 25 percentage points (McNemar or paired exact test). Any real effect of a method hint is likely in the 5–15pp range, based on the literature: existing reasoning models "exhibit a 20–30% drop in accuracy on more complex tasks", and "advanced reasoning methods are not always beneficial" per GTBench [S]. A method-hint effect smaller than the within-cell noise floor is indistinguishable from zero, so the experiment is biased toward H0 by design.

Second: the confound structure is nearly untreatable at manual-dispatch scale. CF08 (session variance, model drift, unknown sampling settings) means each paste is drawn from a non-stationary distribution. Arena platforms may silently change model versions, temperature, system prompts, or rate limits between sessions. Without API access, these cannot even be measured, let alone controlled. The blinding key (R6) is fragile: the human dispatcher sees the prompt text and can plausibly distinguish which arm contains a strategy card even under opaque ids if the card text uses distinctive vocabulary.

Third: if the MindGames [V] or L02 [S] generators already produce instances with published independent verifiers and code, building a new v1 is unnecessary for Q-A. MindGames' code generates "epistemic reasoning problems (akin to muddy children or drinking logicians) using modal logic" and is publicly available with datasets. The problems "necessitate tracking multiple agents' beliefs and reasoning about higher-order beliefs." Similarly, L02 synthesizes muddy children and Cheryl's birthday puzzles requiring "recursive reasoning about agents' knowledge through sequential information exchanges" with 2,784 samples. If both already supply generator + verifier, the strongest variant of Q-A is answered by running their code, making a new family a novelty claim without novelty (see L01–L03).

**What I tried and why it only partly succeeded.** I tried to argue that Q-B is conceptually vacuous (a method hint is just a more specific prompt, so the experiment reduces to a prompt-engineering comparison). This fails because the seed explicitly distinguishes triggered retrieval (with validity obligations) from generic prompting, and the obligation mechanism (H2, S2 stratum) is a distinct testable claim not covered by prompt-engineering studies. The experiment *does* have a conceptually separable question—it just cannot answer it at the proposed scale.

**Net assessment:** The mission can proceed, but only if (a) the 400-trial budget is the minimum, (b) the arm count is reduced from 4 to 3 (merge R and N into a single control, or drop one), and (c) at least one solver is used via a deterministic API rather than arena paste. Without (c), CF08 alone can mask or fabricate any effect.

---

## 2. Registered comparison (P02-E-2)

### Arms

| Arm | Code | Content added to prompt |
|---|---|---|
| Pack | **P** | Trigger-matched strategy cards from frozen library, rendered in full (trigger, transformation, obligations, failure modes). |
| Length-matched prose | **L** | Generic epistemic-reasoning advice of the same token count as the pack, composed once per schema (not per instance), containing no trigger-specific vocabulary. Example: "Consider what each agent can observe; update beliefs after each event; check your conclusion against the stated evidence." |
| No added text | **N** | Bare instance only. |

I recommend **dropping the random-card arm (R)**. At this trial budget, R and L together ask two separate questions about placebo content and neither can be answered with power. L already controls CF01 (length/format). R can be added only if budget exceeds 600.

### Strata

| Stratum | Code | Definition | Min instances |
|---|---|---|---|
| Trigger-present, move-valid | **S1** | Instance schema matches at least one card trigger; card's validity obligations hold for this instance. | ≥ 40% of registered set. |
| Trigger-present, move-invalid | **S2** | Instance schema matches at least one card trigger; at least one obligation fails, by construction (e.g. announcement is private not public, or behaviour policy must be inferred). Invalidity confirmed by independent verifier. | ≥ 15% of registered set. |
| Trigger-absent | **S3** | No card trigger matches the schema features. | ≥ 15% of registered set. |

### Unit of observation

The **instance-solver pair**. Each instance is dispatched once per arm per solver. The unit of analysis is the instance (paired across arms within solver).

### Solver pool

Two solver families, identities recorded at Gate 2. I assume at least one frontier-class model (e.g. GPT-class or Claude-class, 2026 vintage) and one mid-tier open-weight model (e.g. Llama or Qwen family). If tool access is available in the arena, record it; design for no tool access.

### Replicates

At 400 trials total: 3 arms × 2 solvers × n instances. With n distributed across strata, this gives roughly 66 instances, each appearing in all 6 (arm × solver) conditions = 396 dispatches. At 60 trials total: 3 arms × 1 solver × 20 instances = 60 dispatches (only 1 solver; see §5).

### Randomization

The compiler agent generates all prompts in advance, assigns each a random opaque alphanumeric id (e.g. `X7k3qP`), and produces a dispatch manifest ordering them in a random permutation. The human dispatches in manifest order. The arm key mapping opaque id → (instance, arm, solver) is stored in a sealed file the human does not open until all dispatches are complete.

### Pack rendering

The matched cards are appended after the instance text under a header "## Reference strategies (may or may not apply to this problem)". Each card shows: trigger summary, transformation, expected effect, obligations. No card contains an answer or answer shape. The obligations are rendered as a checklist the solver is asked to evaluate before using the card.

### Length-matching rule

For each schema, measure the token count of the rendered pack (P arm). The L arm's generic prose is padded or trimmed to within ±10% of that count, using a fixed library of generic epistemic-reasoning sentences. The same L text is used for all instances sharing a schema.

### Problem characterization production

**Unit: schema** (not instance). Each schema (defined by subfamily, evidence level, depth, and announcement type) gets one problem-state declaration, written by the compiler agent from the schema definition text alone, never from the generator's parameters, the ground-truth answer, or any solver output. The characterization is committed (with content hash) before any solver output exists.

**Leakage guard:** The problem state declares only structural features (e.g. "public announcement: present", "sequential updates: ≥2", "behaviour policy: given vs. inferred"). It never names the correct method, the answer, or the difficulty.

---

## 3. Measurements (E-M01 to E-M05)

**E-M01: Primary metric — strict accuracy.** Binary: solver's answer matches ground truth on all required fields (posterior direction, verdict band, and identified world). Format failures or unparseable outputs count as incorrect. Reported per stratum × arm × solver.

**E-M02: Secondary metric — graded score.** If the family defines a graded rubric (e.g. posterior within ε, correct verdict but wrong posterior), report it. Never substitute E-M02 for E-M01 in the primary contrast.

**E-M03: Format-failure rate.** Fraction of trials where the solver's output could not be parsed into the required answer schema. Reported per arm. If P's format-failure rate differs significantly from N's, the pack may be interfering with compliance rather than reasoning.

**E-M04: Obligation-check rate (S2 only).** On S2 instances in arm P: did the solver's trace explicitly evaluate the card's obligations and conclude they do not hold? Binary per trial. The proportion is the obligation-mechanism test (H2).

**E-M05: Failure-mode classification.** Each incorrect answer is classified using the v0 taxonomy (wrong_direction, verdict_miscalibration, prior_neglect, etc.) or the v1 taxonomy if different. This is diagnostic only—not used in the primary contrast.

**Per-trial record schema:**

| Field | Type | Source |
|---|---|---|
| `dispatch_id` | string | manifest |
| `instance_id` | string | generator |
| `schema_id` | string | generator |
| `arm` | P/L/N | sealed key |
| `solver_id` | string | recorded |
| `stratum` | S1/S2/S3 | characterization |
| `timestamp_paste` | ISO 8601 | human log |
| `timestamp_response` | ISO 8601 | human log |
| `session_id` | string | arena URL or session token |
| `raw_output` | text | paste-back |
| `parsed_answer` | dict or null | compiler agent |
| `ground_truth` | dict | generator |
| `strict_correct` | bool | compiler agent |
| `graded_score` | float | compiler agent |
| `format_failure` | bool | compiler agent |
| `obligation_checked` | bool or null | compiler agent (S2/P only) |
| `failure_mode` | string or null | compiler agent |
| `prompt_token_count` | int | compiler agent |
| `tool_access_observed` | bool | human |
| `notes` | text | human |

---

## 4. Controls (E-CTRL01 to E-CTRL06)

**E-CTRL01 (→ CF01, prompt length/format).** The L arm is length-matched to P within ±10% tokens. Any residual arm difference between P and L cannot be attributed to extra reasoning budget alone.

**E-CTRL02 (→ CF02, answer leakage).** Before freezing the card set, run an automated check: for every (card, instance) pair, search the card text for any substring of the ground-truth answer, any numeric value in the posterior, or any verdict-band keyword that matches this instance's truth. Any hit → card is revised or instance is excluded.

**E-CTRL03 (→ CF03, characterization leakage).** The problem state is written from the schema definition only, which does not contain the ground-truth answer. The procedure is: (1) the compiler agent reads the schema text, (2) declares features, (3) commits. No solver output, generator parameter, or answer is available at step 2.

**E-CTRL04 (→ CF04, contamination).** Use only novel instances from the v1 generator, never canonical puzzle texts (no "muddy children", "blue eyes" verbatim). Vary surface names, locations, and narrative framing. Include a contamination probe: embed 5 recognizable canonical puzzles in the pilot (never registered) set and compare accuracy to novel instances of matched difficulty.

**E-CTRL05 (→ CF05, generator/verifier circularity).** R1 requires the verifier to be independent. The verifier must be a second implementation (different language, author, or algorithm) that takes the instance specification and returns ground truth. Report the agreement rate on 100% of instances before any solver is run. Any disagreement → instance excluded (rule written in advance, counted, and reported).

**E-CTRL06 (→ CF08, session variance).** Record session id, timestamp, and any observable model-version string. Interleave arms within a dispatch session (do not block all P trials, then all L trials). Randomization (§2) handles this. Report a sensitivity analysis dropping the first and last decile of dispatches by timestamp.

---

## 5. Sample size (P02-E-3)

**Assumptions:**
- Baseline (N arm) accuracy on S1: 45% (chosen to be mid-range; if pilot shows <20% or >80%, adjust family difficulty per §6).
- Minimum meaningful effect: 15 pp improvement (P arm accuracy = 60% vs. N = 45%). Smaller effects are real but not actionable for the strategy-IR gate.
- Within-instance correlation across arms: ρ ≈ 0.3 (easy instances are easy in all arms).
- McNemar-like paired test, two-sided α = 0.05.

**Derivation (paired binary):** Under McNemar, the relevant quantity is the number of discordant pairs (one arm right, other wrong). With baseline 45% and treatment 60%, and correlation 0.3, the expected discordant fraction is roughly 0.38. To detect an odds ratio of ~2.0 among discordants at 80% power requires ≈40 discordant pairs, implying ≈105 instances in S1. With S1 comprising 60% of instances, total ≈175 instances × 3 arms × 1 solver = 525 dispatches. For 2 solvers: 175 × 3 × 2 = 1,050.

**400-trial design:** Use 1 solver only. 133 instances × 3 arms = 399 dispatches. S1 gets ≈80 instances → ≈30 discordant pairs → power ≈ 65% for a 15 pp effect, ≈80% for a 20 pp effect. This is marginal but informative. Report the achieved power and the confidence interval width.

**60-trial design:** 20 instances × 3 arms × 1 solver = 60. S1 gets ≈12 instances. **This cannot detect any plausible effect.** The 60-trial design can only serve as a logistics pilot: checking for floor/ceiling (H5), verifying the dispatch pipeline, and measuring format-failure rate. It cannot answer Q-B and should not be used for the registered contrast.

**What the 60-trial design can decide:** (a) Whether headroom exists (H5). (b) Whether the dispatch pipeline works end-to-end. (c) Whether format-failure rates differ by arm. **What it cannot decide:** Any hypothesis H0–H3.

---

## 6. Pilot and headroom (P02-E-4)

**Procedure:**
1. Select 15–20 instances spanning all subfamilies and all difficulty levels. These never enter the registered set. Mark them `pilot_only` in the manifest.
2. Dispatch them in arm N (no added text) to both solvers. Record accuracy per solver × difficulty level.
3. If accuracy is >85% on the hardest stratum for both solvers: increase difficulty (add depth, more agents, harder evidence). If accuracy is <15% on the easiest stratum: decrease difficulty or simplify framing.
4. Iterate at most once. Re-pilot with adjusted instances if needed.

**Rules:**
- Pilot outputs may be used only for: (a) checking floor/ceiling, (b) verifying the parser works, (c) measuring format-failure rate, (d) estimating baseline accuracy for power calculation.
- Pilot outputs may **not** be used for: (a) comparing arm effects, (b) selecting which instances enter the registered set based on "interestingness", (c) tuning card text, (d) adjusting the margin.

---

## 7. Acceptance tests (E-T01 to E-T08)

**E-T01: Generator determinism.** Run the generator twice on the same (template, evidence, prior, presentation, seed) tuple. Output must be byte-identical. Repeat for 20 tuples.

**E-T02: Known-answer cases.** For each subfamily, construct 3 instances whose ground truth is trivially verifiable by hand (e.g. only one world is consistent with the evidence). Verify the generator and independent verifier both return the expected answer.

**E-T03: Generator/verifier agreement.** Run both on 100% of registered instances. Record and report the number of disagreements. Disagreeing instances are excluded. If disagreement rate exceeds 5%, halt: the family is not ready.

**E-T04: Verifier independence.** The verifier must not import, call, or share any module with the generator beyond the instance specification format. Document the dependency graph of both.

**E-T05: Judge mutation tests.** For 20 instances, produce 5 mutated answers each (wrong posterior direction, wrong verdict band, correct posterior but wrong justification, etc.). Verify the judge marks each as incorrect and assigns the expected failure mode.

**E-T06: Pack leakage test.** For every (card, instance) pair in the registered set: (a) no substring of the ground-truth answer appears in the card; (b) removing the card from the prompt does not change the answer that a string-match oracle would give; (c) the card does not name the specific instance schema or parameters.

**E-T07: Instance-text leakage test.** The instance text must not contain the ground-truth answer, the verdict band, or the posterior value in any explicit form. Check by regex on 100% of instances.

**E-T08: S2 invalidity confirmation.** For every S2 instance: (a) the independent verifier confirms that applying the card's method as written produces a wrong answer (or is undefined), and (b) the obligation that fails is identified and documented.

---

## 8. Dispatch protocol and logging (P02-E-5)

### Compiler agent (runs locally, before dispatch)

1. Generate all instances. Run E-T01–E-T08.
2. Produce problem states per schema. Freeze and commit with hash.
3. Run the trigger matcher against the frozen card library. Record matches.
4. Render all prompts (instance text + arm-specific content) under opaque ids. Emit the dispatch manifest (ordered random permutation).
5. Store the sealed key file mapping opaque id → (instance_id, arm, solver_id, stratum). Hash and commit.
6. Output a dispatch log template: one row per manifest entry, with columns for `dispatch_id`, `timestamp_paste`, `timestamp_response`, `session_id`, `raw_output`, `tool_access_observed`, `notes`.

### Human (manual dispatch)

1. Open an arena session for the designated solver. Record the session URL/id and any visible model-version string, system prompt, or tool-access indicator.
2. Take the next entry from the manifest. Copy the prompt text. Paste into the arena session. Wait for the complete response.
3. Copy the full response text. Paste into the `raw_output` column of the dispatch log. Fill `timestamp_paste`, `timestamp_response`, `session_id`, `tool_access_observed`, `notes`.
4. Do **not** read or interpret the response. Do not re-dispatch or edit. If the response is truncated, note it and move on.
5. After every 20 dispatches, start a new session (to limit session-context contamination). Record the new session id.
6. Continue in manifest order until complete. Commit the dispatch log.

### Compiler agent (post-dispatch)

7. Parse each `raw_output` into the answer schema. Record `parsed_answer`, `format_failure`.
8. Score each parsed answer against ground truth. Record `strict_correct`, `graded_score`, `failure_mode`.
9. For S2/P trials: check whether the solver's trace mentions the obligation and concludes it fails. Record `obligation_checked`.
10. Compute per-cell statistics. Run the pre-registered tests. Output the decision per E-O01–E-O05.

### What changes with tool access

If the solver has code execution: the method hint may be moot (CF07). Record this. If tool access is present for some sessions and not others, those sessions are not comparable—flag and exclude or report separately. If tool access is universal, add a note that Q-B's relevance is conditional on no-tool settings.

---

## 9. Decision rules (E-O01 to E-O05)

**E-O01: Primary (H1).** On S1, if P's accuracy exceeds L's accuracy by ≥ the pre-registered margin δ (set at Gate 2; I recommend δ = 12 pp), with the lower bound of a 90% CI above 0: **H1 supported**. If the CI includes 0: **H1 not supported; stop rule applies**. Report the point estimate and the CI regardless.

**E-O02: Misapplication (H2).** On S2, if P's error rate exceeds L's error rate and the difference is in the predicted direction (more wrong answers, not just more format failures): **H2 supported (pack hurts)**. If additionally E-M04 shows <50% of S2/P trials have `obligation_checked = true`: **obligation mechanism failed**. If obligation-check rate is >80% and P's error rate is not elevated: **obligations may protect**.

**E-O03: Generic modelling (H3).** If L's accuracy on S1 is within δ of P's: **H3 not refuted**; the specific trigger match adds nothing beyond explicit-modelling nudge.

**E-O04: Headroom (H5).** From pilot (§6): if baseline accuracy on the hardest S1 instances is >85% or <15% for both solvers, and difficulty adjustment fails to move it: **H5 fails; Q-B is uninformative; record and stop**. This is not a negative result for the pack; it is a design failure.

**E-O05: Verifier agreement (H4).** From E-T03: if disagreement rate is 0% on all subfamilies tested: **H4 supported** for those subfamilies. If >0% but ≤5%: **H4 partially supported**; report which subfamilies disagree. If >5%: **H4 not supported; family is not ready; do not proceed to Q-B**.

**Uninformative outcomes (recorded, not interpreted as null):**
- H5 failure (floor/ceiling).
- Fewer than 20 S1 instances dispatched (insufficient data).
- Format-failure rate >30% in any arm (the solver cannot engage with the task).
- Session-level confounds detected (e.g., model version changed mid-experiment).

---

## 10. Critique of the draft gate (P02-E-6)

1. **No sample-size commitment.** The gate says "register and run one comparison" but specifies no minimum number of instances, no power calculation, and no minimum detectable effect. A comparison with n = 5 technically satisfies the gate while having zero statistical informativeness. The gate must specify a minimum n and a margin δ.

2. **No solver specification.** "Problems with known ground truth" and "a control receiving prose of comparable length" are under-specified. The gate does not say how many solvers, whether they must differ in capability, or how dispatch is done. Different solvers may produce opposite results.

3. **"Beat its controls" is undefined.** Beat by what metric, by what margin, by what statistical test, at what significance level? The gate needs a registered test and a one-sentence decision criterion.

4. **No independent-verification requirement.** The gate mentions "known ground truth" but does not require the truth to be independently verified (R1). If the generator and judge share code (as in v0), the comparison cannot rule out a semantic bug that both share.

5. **"Obligation checks that never fail on planted invalid transforms" is necessary but incomplete.** The gate should also specify what happens if obligations fire but the solver ignores them—this is a different failure mode (the card is honest but the solver is not responsive to warnings).

6. **No contamination or leakage check.** The gate does not mention checking whether the cards leak answers (CF02), whether instances are memorized (CF04), or whether the characterization leaks the stratum (CF03).

7. **No pilot / headroom check.** The gate does not require H5 to be checked before the registered comparison. If the family is at floor or ceiling, the comparison is uninformative regardless of outcome, and the stop rule would incorrectly trigger a negative result.

8. **No time limit or staleness clause.** The gate does not say when the comparison expires—if card library, models, or instance families change, should the gate be re-run? A staleness clause (e.g., "results are valid for 6 months or until the card library changes, whichever is sooner") would prevent indefinite reliance on one snapshot.

---

*Word count: ≈3,400. Nothing cut.*
