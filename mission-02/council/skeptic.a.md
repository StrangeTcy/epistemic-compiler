## 1. Kill attempt (P03-S-1)

**The mission, as framed, is a machine for producing a positive result on Q-B that means nothing, and a negative result on Q-B that means nothing either. Both failure modes are built into the design, not into the execution.**

Three legs.

**(a) The instance family is specified to satisfy the intervention's success condition.** Q-A(iii) asks for "instances on which the obvious reading is systematically wrong, so that the method the solver chooses decides correctness." Q-B then asks whether supplying a method helps. These are the same sentence read twice. If Q-A succeeds by its own criterion, Q-B's S1 result is determined before any solver is run: on problems engineered so that not knowing the method is fatal, text stating the method will help. That is not a finding about trigger-matched retrieval, about the Strategy IR, or about cards. It is a finding about instance construction. The seed's own framing ("the method the solver chooses decides correctness") is leading wording and I flag it under Rule 2.

**(b) The arms in R4 do not contain the contrast that the Strategy IR is actually on trial for.** The IR's claim is about *matching* — that characterizing a problem beforehand and retrieving by trigger produces something better than the alternatives. R4's controls are L (generic prose), R (random cards), N (nothing). All three are controls for *content relevance*. None is a control for *retrieval*. The two arms that would isolate retrieval are missing: **A** = give the solver the whole frozen card set concatenated (no matching, no characterization, just dump the library), and **F** = one fixed hand-written recipe per subfamily (named in `known_alternatives` and then not made an arm). If P beats L and R but A or F ties P, the matcher is decorative and the library can be replaced by a constant string. Under the current design that outcome is invisible, and R9 would record "the gate passed" and authorize expanding the library. This is the single cheapest way the mission produces a confidently wrong decision.

**(c) The gate is almost certainly underpowered, and R9 converts underpowering into a retirement decision.** R6 fixes manual copy-and-paste dispatch. I computed exact-binomial McNemar power in-session for paired strict-correctness: for a 15-percentage-point true difference with a 35% discordance rate you need roughly 120–150 paired instances; for 10pp, roughly 300; for 5pp, more than 800. S1 alone at 150 instances × 4 arms × 2 solver families = 1,200 pastes, before S2 and S3. The realistic study is ~3,000+ manual dispatches, which `known_unknowns` already concedes may be infeasible. The predictable compromise is n ≈ 30–60 per cell, which can only detect effects above ~25pp. Then R9 fires: "does not beat its controls by the margin → extension stops, cards retired." H5 gives an "uninformative, not no-effect" escape hatch for *floor/ceiling* but there is **no equivalent clause for insufficient power**. As written, the protocol's own stop rule will retire cards on the basis of a study that could never have detected them.

I tried to find a framing under which (a) is not fatal and failed to find one inside Q-A as stated: any family satisfying Q-A(iii) is a family where the S1 comparison is near-tautological. The repair is not to abandon the mission but to **invert the order**: fix the instance family by an external criterion (difficulty, verifiability, depth), *not* by "the method decides correctness," and make the primary contrast P vs A and P vs F rather than P vs N.

---

## 2. Primary critiques

**S-CR01 — Target: R1, CF05, Q-A(ii). The "independent verifier" does not verify the thing that can be wrong.**
Flaw: the verifier re-derives the answer from the *structured* instance (worlds, policies, events). The solver reads *English*. The generator alone controls the map from structure to English. Nothing in R1 audits that map. The realistic bug is not "Bayes computed wrong" (trivial, both implementations will agree) but "the verbalization does not entail the semantics the ground truth assumes" — e.g. whether "nobody spoke up" is common knowledge among all agents or only observed by some; whether an announcement is truthful by construction; whether agents know the behaviour table. Two independent implementations of the *same* spec agree perfectly and both are wrong relative to the text. Worse, this inflates arm effects: a pack that tells the solver which reading to assume ("treat announcements as public and truthful") converts verbalization ambiguity into points, and the gain gets reported as method-selection benefit.
Severity: **fatal to Q-A's headline claim**, serious for Q-B.
Repair: add a text-faithfulness check that is not a program — ≥2 human solvers (or a solver family excluded from the study) blind to generator parameters answer a random 30-instance sample from the text alone; report the disagreement rate with the generator. Pre-register that >10% disagreement voids the subfamily. Also require a "restate the structure" probe: ask solvers to emit the world set and update sequence they inferred, and score structure-recovery separately from the answer.

**S-CR02 — Target: R4/R9, Q-B. No arm isolates retrieval (see 1b).** Severity: **fatal**. Repair: add arms A (all cards) and F (fixed recipe). Primary contrast becomes P−A and P−F; P−N and P−L become secondary. If pastes are scarce, drop N (the least informative arm: nobody doubts that relevant method text beats nothing on method-sensitive problems).

**S-CR03 — Target: R6/R7/R9. Power and the stop rule.** Severity: **serious**. Repair: pre-register a minimum detectable effect from the feasible n, computed before Gate 2; add **S-ABORT05** below: if achievable n is below the n required for the registered margin at 80% power, the study is reported as *uninformative* and R9's retirement clause does not fire. Also: with 2 contrasts × 3 strata × 2 solver families there are 12 registered tests; fix one primary (P−A on S1) and label the rest exploratory, or the "margin fixed in advance" is a multiplicity illusion.

**S-CR04 — Target: H2, R9, and the obligations mechanism. "Obligation checks firing" is not observable in an answer-only task.** The v0 output is a literal `ANSWER` dict. If obligations are to be observed, the solver must emit a checks field — but requiring that field in the P arm and not in others makes the arms non-comparable (CF01 in a new guise: the P arm gets an extra output-format instruction). If the field is required in all arms, the N arm is no longer "no added text."
Severity: **serious**. Repair: identical output schema across all arms including a `preconditions_checked` list; measure obligations *only* via (i) S2 accuracy and (ii) rate of explicit refusal-to-apply, both scored from the same schema. Pre-register that unparsable checks count as "not fired."

**S-CR05 — Target: R2 and CF03. Characterization leakage is structural, not procedural.** R2 forbids writing the problem state from generator parameters or the answer. It does not forbid the *feature vocabulary itself* from encoding the method. A feature like "public truthful announcement present: yes" is the method hint. Whoever designs the feature set after knowing the subfamilies has already done the method selection by hand; the matcher then performs a lookup that a human performed earlier and off the record.
Severity: **serious**. Repair: (i) the feature checklist is authored and hashed *before* the instance family spec exists, by a party that has not read the cards; (ii) ≥2 independent characterizers per unit, report Cohen's κ; pre-register that κ < 0.6 voids the characterization and therefore the gate; (iii) report what fraction of instances the matcher maps to the same pack — if ≥90% of S1 maps to one pack, state plainly that the matcher is a constant function on this family and that the study tests card content, not matching.

**S-CR06 — Target: the freezing order in `repo_context`. Anti-tuning runs the wrong way.** Cards are frozen before the Council responds so the family cannot be tuned to the cards. But the family does not exist yet and will be designed *after* the cards, by agents with access to the card families and to the 12-family taxonomy. The protective order should be: family spec hashed first, cards written against it blind — or cards first, family designed by someone who has not read them. Currently the cards are frozen *and* the family designer can read them, which is the worst of both.
Severity: **serious**. Repair: name, in the commit, who wrote the family spec and whether they had read the cards; if yes, Q-B is exploratory, not registered.

**S-CR07 — Target: Q-A's "higher-order" framing. Depth is confounded with bookkeeping load.** Nesting depth, number of agents, number of events and text length move together in every generator of this kind. [S] Hi-ToM reports accuracy declining with order and that chain-of-thought prompting gave no substantial improvement in their setting (seen in the PDF snippet, not the full text). A decline with order is equally explained by working-memory/bookkeeping load. If the family's difficulty axis is depth, the study measures tracking capacity and calls it epistemic reasoning.
Severity: **serious**. Repair: minimal-pair construction — hold entities, events and token count fixed; vary only the nesting depth of the *query* over the same event log. Pre-register the depth×length decomposition.

**S-CR08 — Target: H5 and `known_unknowns` on ceiling. The headroom test is the wrong headroom test.** H5 checks that the N arm is off floor and ceiling. The binding quantity is different: the maximum effect any pack could have, which is bounded by (oracle-hint accuracy − N accuracy). If a plainly-stated correct recipe buys 6pp, no card can beat the controls by a 10pp margin, and the study is dead regardless of floor/ceiling.
Severity: **serious**. Repair: add an oracle-hint arm to the pilot (S-FALS02) and pre-register an abort if the oracle gain is below the registered margin.

**S-CR09 — Target: H0/H3 and the interpretation of L. The L arm is not a weak control; it is the hypothesis.** A "length-matched generic prose" control that mentions explicit modelling is, by construction, H3. If L is deliberately made contentless to protect the P−L contrast, the contrast becomes P vs filler (i.e. CF01 only). The design must state which L it is and accept the consequence. If L contains "enumerate the states and update on each event" — which is nearly the entire content of any valid DEL card — then P−L is a test of *card specificity*, and I expect it to be near zero.
Severity: **serious**, and it is the most likely true outcome. Repair: run both L-generic-modelling (L_m) and L-filler (L_f); report both.

**S-CR10 — Target: known_alternatives / CF07 / R6. Tool access makes the whole comparison contingent.** Modern arena sessions may run code or extended reasoning without the dispatcher knowing. "Sampling settings and tool access are recorded where observable" is an admission that they may not be observable. If a solver can enumerate Kripke models in Python, a method hint is moot and P−N → 0 for reasons unrelated to the IR.
Severity: **serious**. Repair: pre-register tool-use as an exclusion criterion with an observable proxy (ask the solver to declare tool use in the output schema; exclude declared-tool trials from the primary analysis and report them separately). If unobservable, report the whole study as tool-status-unknown and lower the claim ceiling accordingly.

**S-CR11 — Target: the "build a v1" premise of Q-A.** [S] MindGames has a public code repository and a HuggingFace dataset (I saw the GitHub repo page listing generation code for epistemic-logic problems and a dataset link; I did not run it). If an existing generator plus an existing model checker covers the public-announcement subfamily, the marginal value of a v1 is verbalization control and S2 construction only. Building a generator is the most expensive, least informative part of this mission and is where all the schedule will go.
Severity: **minor-to-serious** (resource argument). Repair: make Q-A's first deliverable a *reuse report* with a run of the external generator, not a new spec.

**S-CR12 — Target: CF04/contamination.** Muddy children, drinking logicians and Cheryl's birthday are in training data in many paraphrases. A generated variant inherits the canonical *answer shape*. Severity: **serious**. Repair: include "perturbed-canonical" instances where the standard answer is wrong by construction (e.g. one agent cannot hear the announcement) and report accuracy on canonical vs perturbed as a contamination index; if models do worse than chance on perturbed variants, every other number is about memorization.

---

## 3. Confound and circularity register

**S-CF12 — Topic-match masquerading as trigger-match.** The R arm draws random cards from a library of ~8 cards in 6 non-game families. Those cards will be visibly off-topic. P−R then measures "on-topic text beats off-topic text," which is CF01 with extra steps. *In data:* P−R ≫ P−L, and R ≤ N (off-topic text actively distracts). *Control:* draw R from within the game family (a game card whose trigger is absent in this instance), and add arm A (all cards).

**S-CF13 — Hedging placebo.** Obligation prose may reduce S2 errors by inducing caution generally, not by being checked. *In data:* S2 improvement accompanied by increased abstention/low-confidence answers on S1 too, and by improvement on S2 instances whose planted violation is unrelated to the stated obligation. *Control:* an obligation-placebo arm — same card with obligations replaced by irrelevant-but-cautious conditions; pre-register the S2-by-violation-type breakdown.

**S-CF14 — S2 is a difficulty stratum, not a validity stratum.** For invalidity to be detectable at all, the text must state the violating fact; that fact adds a clause and a reasoning step. S1 and S2 then differ in difficulty. *In data:* N-arm accuracy differs between S1 and S2; a surface classifier separates them. *Control:* minimal-pair S1′/S2 generation (identical text except the violating clause, with a neutral filler clause in S1′), plus S-FALS01's classifier gate.

**S-CF15 — Incomplete blinding of the human dispatcher.** The arm key is withheld but arms are recognizable by eye (length, card formatting). The dispatcher chooses session, order, and whether to retry a malformed response. *In data:* arm effects correlated with session order or time-of-day; retry counts differing by arm. *Control:* automated API harness if at all possible; otherwise all four arms of an instance dispatched in one randomized block, zero retries permitted, timestamps and session ids logged, and a post-hoc test that arm is not predicted by dispatch order.

**S-CF16 — Cross-trial carryover within an arena session.** A session that saw a pack earlier carries the method into a later N trial, biasing *against* the pack. *Control:* one fresh session per prompt, verified; pre-register exclusion of any trial sharing a session with another trial.

**S-CF17 — Independence theater between generator and verifier.** Two implementations of one spec by one author share the spec's errors (distinct from CF05, which is about shared code). *In data:* zero disagreements — which R1 will read as success and which is also what you see when both are wrong. *Control:* differential testing against a *pre-existing external* checker (a published DEL model checker or L01's released code), plus brute-force enumeration from an independently written semantics, plus S-CR01's human gold sample. Pre-register that zero-disagreement with a sibling implementation is *not* evidence of correctness and must be reported as such.

**S-CF18 — Format-compliance confound.** R7 counts format failures as errors. Packs contain structured text and may raise schema compliance independent of reasoning. *In data:* P's advantage shrinks to zero when the analysis is restricted to parseable responses. *Control:* report accuracy-among-parseable and format-failure rate separately as co-primary; add a structure-only pack arm (card skeleton with method content removed).

**S-CF19 — Answer-space asymmetry.** With a small verdict band set (as in v0: three bands) and a posterior field, strict correctness is dominated by whichever field has the fewest degrees of freedom; a hint that fixes the *format* of the posterior (exact fraction vs decimal) can move strict correctness several points. *Control:* field-wise scoring reported alongside strict correctness; tolerance rules for numeric fields fixed before Gate 2.

---

## 4. Three executable falsification experiments

**S-FALS01 — Surface-feature audit of the family (LOCAL, 0 model calls).**
On the full generated instance pool, fit three cheap classifiers on bag-of-words + length features with held-out splits: (i) text → ground-truth answer; (ii) text → stratum (S1 vs S2); (iii) prompt text → arm label.
*Pass/fail, fixed in advance:* FAIL and rebuild the family if (i) beats the majority-class base rate by >5pp, or (ii) reaches AUC > 0.65, or (iii) reaches accuracy > 0.5 on the P/L/R three-way (indicating arms are trivially distinguishable, relevant to blinding). FAIL on (ii) specifically voids all H2 conclusions.
*Why it can end the mission:* if planted invalidity is surface-detectable, S2 cannot test obligations at all.

**S-FALS02 — Headroom and intervention ceiling (MODEL RUNS: 96 pastes = 24 pilot instances × 2 arms × 2 solver families).**
Arms: N and ORACLE (a plainly written, correct solution recipe for that subfamily — not a card, no retrieval). Pilot instances never enter the registered set (R8).
*Pass/fail:* ABORT Q-B on this family if N accuracy > 0.85 or < 0.15 in both families (H5 fails → uninformative, per the seed's own clause). ABORT Q-B if (ORACLE − N) < the margin to be registered at Gate 2 — no pack can exceed an explicit correct recipe, so this bounds the best case. PROCEED only if headroom exists *and* the oracle gain exceeds the margin by at least a factor of two.

**S-FALS03 — Retrieval-necessity probe (MODEL RUNS: 144 pastes = 24 pilot S1 instances × 3 arms × 2 solver families).**
Arms: P-sim (the trigger-matched card alone), A (entire frozen card set concatenated), F (one fixed generic recipe reused for all instances).
*Pass/fail:* if A ≥ P-sim − 3pp **or** F ≥ P-sim − 3pp on pooled pilot accuracy, declare the trigger matcher non-necessary and either (a) cancel Q-B as framed, or (b) re-register with P−A and P−F as the primary contrasts. Only if P-sim exceeds both A and F does the registered study measure anything about matching.
*Why it can end the mission:* this is the cheapest direct test of the Strategy IR's actual claim, and the current design never performs it.

(If only one can be run: S-FALS03. It costs 144 pastes and can retire the premise.)

---

## 5. Claim ceiling and abort conditions (P03-S-2)

The study **cannot justify**:
- …that trigger matching, characterization, or the Strategy IR contributed anything, unless arms A and F are run and P exceeds both. Without them the maximum claim is "relevant method text helped on instances built to require that method."
- …that the ground truth is correct, only that two implementations of one spec agree — unless an external checker and a human gold sample are included (S-CR01, S-CF17).
- …any statement about recursive reasoning, level-k depth, theory of mind, or mechanism. Accuracy is not mechanism; the seed already concedes this and the concession must survive into the write-up's title.
- …that a null result means the cards are useless, unless power for the registered margin is demonstrated.
- …that obligations work or fail, unless obligation-firing is observable in a uniform output schema across arms (S-CR04).
- …any generalization beyond the one family, the named card versions, the named models, the arena dispatch channel, and the tool-access status actually observed.

**S-ABORT01** H5 fails (floor/ceiling in both solver families on pilot) → stop; report "uninformative," not "no effect."
**S-ABORT02** Oracle-hint gain (S-FALS02) below the registered margin → stop Q-B; the family cannot host the question.
**S-ABORT03** Any disagreement between the generator and the external/human verification path that is not traced to a single identified bug under the pre-written exclusion rule → suspend Q-A claims for that subfamily; do not silently drop instances.
**S-ABORT04** S1/S2 separable by surface classifier at AUC > 0.65 → H2 is untestable; report S2 results as uninterpretable.
**S-ABORT05** Feasible paired n below the n required for the registered margin at 80% power → report uninformative; **R9's retirement clause does not fire**. (This clause does not currently exist and must be added at Gate 2.)
**S-ABORT06** Contamination index indicates canonical-answer transfer (accuracy on perturbed canonicals at or below chance while canonical accuracy is high) → restrict the registered set to non-canonical subfamilies.
**S-ABORT07** Declared or detected tool use in >10% of trials and not suppressible → report the comparison as tool-contaminated; primary contrasts become exploratory.
**S-ABORT08** Characterizer κ < 0.6, or the matcher maps >90% of registered instances to a single pack → the "retrieval" factor is degenerate; report as such and do not claim a retrieval effect in either direction.

---

## 6. Attack on the strategy-pack idea itself (P03-S-3)

**Why trigger matching may be meaningless here.** With ~8 existing cards plus a first small `game` set, the matcher's output space on a single instance family is tiny and probably constant. A function that returns the same pack for every instance in the registered set is not retrieval; it is a constant string with a ceremony attached. The experiment would then be a comparison of two fixed prompts, and every sentence in the write-up about triggers, characterization and matching would be unsupported by the data. The matcher's degeneracy is measurable before any solver runs (S-ABORT08) and must be reported.

**Why it may be harmful.** Three concrete mechanisms. (1) *Authority override on S2*: a confidently phrased card supplies a procedure; models tend to execute supplied procedures. On move-invalid instances the pack's main effect may be to suppress a correct instinct. (2) *Obligations as prose are weak*: a caveat buried in card text competes with an explicit transformation instruction; prose conditions are not checks. R9 anticipates this but calls it a negative result for "the obligation mechanism" — it is really a negative result for *prose-form* obligations, which is a narrower and less interesting finding, and the seed's own `possible_future_research_on_failure` already names the fix, which means the registered study is partly pre-conceded. (3) *Characterization cost*: in any real use the human must characterize the problem first; nothing in R1–R10 measures that cost, so even a positive result does not establish net benefit over "just tell the model to enumerate states."

**What a fair negative result looks like.** Headroom demonstrated by an oracle-hint arm; power sufficient for the registered margin; arms A, F, L_m, L_f present; κ reported; format failures reported separately; tool status known; and P fails to exceed A and F by the registered margin on S1. That result would be genuinely informative about the IR and I would accept it.

**What would make a positive result untrustworthy even with every registered control in place.** (i) The family was designed by someone who had read the cards (S-CR06). (ii) The verbalization was never checked by anything that reads English (S-CR01) — the pack may simply be disambiguating the generator's prose. (iii) A and F absent (S-CR02). (iv) One instance family, one subfamily, one card set: an effect at n=1 family is a property of that family. (v) The effect is carried by format compliance (S-CF18). Any one of these makes a positive P result uninterpretable, and the current design permits all five simultaneously.

---

## 7. Outcome forecast (P03-S-4) — subjective, hostile priors declared

All probabilities are my subjective credences, not estimates from data.

- **H0 (null/artifactual) partially correct, ~55%.** I expect P−N to be positive and P−L_m to be within ±5pp, i.e. H3 holds: the gain is "be explicit, enumerate states, update," and the card adds nothing specific.
- **P vs A (all cards) ties, ~60%.** The library is small enough that dumping it costs little and matching buys little. This is my single highest-value prediction and the current design cannot test it.
- **H1 as stated (P beats L and R by a pre-registered margin on S1), ~20%** — and conditional on it happening, ~70% that it is explained by S-CF12 (R is off-topic) or S-CF18 (format), not by matching.
- **H2 (packs hurt on S2), ~35% for a detectable harm; ~70% that obligation-firing is observed in <10% of S2 trials**, which is R9's negative result for the obligation mechanism and the most likely concrete finding of the whole mission.
- **H4 (independent verification achievable), ~80% for the *answer computation*, ~25% for the *text→semantics* map.** The easy half will be done and reported as if it were the whole.
- **H5 (headroom), ~45% on canonical-style DEL instances with current strong models, higher (~70%) on perturbed/non-canonical and depth-≥3 instances. Expect ceiling on muddy-children clones.**
- **Feasibility: ~70% that the manual-dispatch budget forces n below the power requirement**, producing a null that R9 misreads as a decision.

**What would change my mind.** A pilot showing P-sim beating A *and* F by ≥10pp on 24 instances across two solver families (S-FALS03) would overturn my "matching is decorative" prior immediately. A human gold panel agreeing with the generator on 30/30 text-only instances would overturn S-CR01. An oracle-hint gain above 25pp would show real headroom and make the whole Q-B exercise worth its cost. Absent those three, I would not spend the dispatch budget.

**Cut for length:** a fourth falsification experiment (verbalization-ambiguity probe), detailed numbers for the multiplicity correction, and a proposed re-framing of Q-A around difficulty-by-construction rather than method-sensitivity.
