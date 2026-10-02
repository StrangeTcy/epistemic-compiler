<!--
COMPILER PROVENANCE HEADER (not part of the response; the response starts at the line "ROLE: THEORIST (P01-T)")

Stored:            2026-10-02, by the compiler agent, from the user's paste into the chat.
Prompt answered:   mission-02/council/prompts/01_theorist_prompt.md (sha256 f668ecf81a355a52c73daae656e88605fb9f5777d3ec1292b31e0c9ebcccc6f0); the response's own PROMPT_ID is M02-P01-T v1.
Arena mode:        not supplied.
Model as shown:    not supplied. The response self-reports "Claude (Anthropic); exact version unknown to me", which is not reliable.
Session date/time: not supplied.
Tools in session:  not supplied. The response self-reports browsing and code execution available but not used.
Text integrity:    preserved exactly as pasted; the code fence around the paste was dropped. One word in T-A09
                   ("fuckingly") reads as an insertion artifact: the same word appears at odd places in other pasted
                   text this project has received. Its origin (model or paste pipeline) is unknown. Kept as received.
Order of events:   the five game-family cards were frozen in commit 426d693, before this response was stored.
-->

ROLE: THEORIST (P01-T)
PROMPT_ID: M02-P01-T v1
SELF-REPORTED MODEL (may be wrong): Claude (Anthropic); exact version unknown to me
TOOLS: browsing available but not used this session; code execution available but not used. Every external claim below is therefore [R], recalled from memory and not checked. I have no access to L02, which is dated 2026, so I make no claims about its content.
SAW OTHER ROLES' OUTPUT: no

---

## 1. Kill attempt (P01-T-1)

**Where it fails: the S1/S2/S3 strata cannot be defined without the cards, but the cards are hidden.** S2 means "trigger present, move invalid". That is defined relative to a specific card's trigger and obligations. Those are agent-authored, still unwritten as far as the Council knows, and deliberately withheld. That leaves three options:

- **(a) Design the family without the cards and assign strata later by running the matcher.** The strata are then whatever the cards happen to carve out. Planting invalidity "by construction" (R5) is impossible, because nobody knew what to plant against.
- **(b) The card author reads the family and writes cards to fit it.** That is CF06, authorship circularity.
- **(c) Define strata by validity conditions of standard methods that are independent of the cards.** Only this one is coherent. But then S2 exists for a card only if that card's obligations happen to match one of the conditions I declare.

**There is also a set-theoretic constraint.** S2 for a card c is the set {trigger(c) ∧ ¬obligation(c)}. It is non-empty only if the obligation does not follow from the trigger. Both are written in terms of features of the problem state that can be read from the text (R2). If the person writing the problem state honestly records the feature that decides validity (for example "the announcement is heard by all agents"), there are two outcomes:

- The matcher already sees that feature. Then the S1/S2 split is just a label sitting in the problem state, which is CF03 leakage in reverse.
- The trigger is coarser than the obligation. Then S2 measures how coarse the trigger is, not whether obligations work.

Either way, Q-B's S2 contrast is defined by the cards and has no independent content.

**Second failure: Q-A's clause (iii) mixes two different properties.** "The obvious reading is systematically wrong" is a property of resistance to narrative and shortcuts. v0 already tests that. "The method the solver chooses decides correctness" is a different property. On any finite explicit semantics there is a method that is always valid: enumerate the model and apply the stated update rule. So "method choice" can only mean choosing a shortcut that is invalid on some instances.

The obligation of any sensible card then reduces to "check that the instance satisfies the semantics the shortcut assumes". A generic "enumerate states and update" prose control already contains that. **H3 is therefore close to true by construction** unless the cards encode shortcuts that pay off on S1. Q-B, as designed, mostly tests whether shortcut cards beat full enumeration in token-limited arena sessions. That is a question about bookkeeping capacity, not about epistemics.

**Third failure: much of Q-A may already be solved.** As I recall, MindGames (L01) generates DEL problems and labels them with a model checker (SMCDEL). That covers clauses (i) and (ii) for public-announcement subfamilies [R]. Hi-ToM (L03) covers "higher-order" up to order 4 [R]. The only part of Q-A that could be new is clause (iii) combined with a certificate that the instance genuinely requires higher-order reasoning. That is a design property of instances, not a choice of semantics.

**Leading wording in the prompt and seed:**
- The title's "independently checkable ground truth" presents a goal as if it were a feature.
- "Higher-order" is used as a selling point; L03 already has this.
- Candidate semantics (a) to (f) all come from the graph's epistemic-game-theory cluster. That frames the problem as game theory when it may be a state-tracking problem.
- Q-B is worded as "improve", which presumes the direction of effect.
- "Instances on which the obvious reading is systematically wrong, so that the method decides correctness" assumes that the "so that" holds.
- The surprise list treats "existing generator suffices" as a surprise. It should be the default.

**Verdict.** Do not proceed as framed. Proceed in this reframed form:

- **Q-A′:** a single finite probabilistic-epistemic semantics (§3).
- **Instance validity:** each instance must carry (i) a *depth certificate* and (ii) a *shortcut-failure certificate* against a baseline of naive programs registered in advance.
- **Strata:** S2 is defined by validity conditions declared now and independent of the cards (§4). Each card is then mapped onto those conditions at Gate 2. A card whose obligation matches no declared condition gets no S2 cell, and that is reported.
- **Reuse:** reuse L01 as a source of instances and of a verifier for pure public-announcement problems, if its artifacts exist.

## 2. Selection criteria (P01-T-2)

| # | Property | How tested |
|---|---|---|
| C1 | Unique answer | The verifier enumerates all answers allowed by the semantics. The instance is kept only if exactly one remains, with exact rational arithmetic and no ties at verdict-band boundaries. |
| C2 | Finite and decidable | The verifier terminates within a fixed size bound (\|W\| ≤ 64 worlds, ≤ 6 events); otherwise the instance is rejected. |
| C3 | Independent verifiability | A second implementation in a different paradigm, written by a different author working from the text spec (§6), agrees on 100% of instances. Disagreements are logged and the instance is excluded. |
| C4 | Text-sufficiency | A parser or human annotator given only the rendered text rebuilds a formal spec that is isomorphic to the generator's (bisimilar, for epistemic models). Instances that fail this are bugs in the verbalization. |
| C5 | Depth certificate | The generator outputs a witness model M′ that is (k−1)-bisimilar to M but has ans(M′) ≠ ans(M). The verifier checks both the bisimulation and the answers. See below. |
| C6 | Shortcut-failure certificate | A registered set of naive programs B (§4) is run. An instance counts as "trap" only if every program in B that applies gives a wrong answer. |
| C7 | Separable difficulty knobs | Modal depth k and bookkeeping load (\|W\| × events) are varied factorially, so that the two can be told apart (T-H6). |
| C8 | Memorization resistance | No instance is isomorphic to a canonical puzzle (muddy children with symmetric sight, Cheryl's birthday). Checked by canonical-form hashing against a small list of canonical models, plus a probe that asks the solver to name the puzzle. |
| C9 | Reading agreement | Two humans read 30 instances and agree on the formal spec. Anything below full agreement on a subfamily marks that subfamily as ambiguous. |
| C10 | Checkable answer format | The answer is a literal (set, rational, round number). The v0 parse-as-data judge is reused. |

**What the depth certificate means.** The *depth* of an instance is the smallest k such that the answer is fixed by the formulas of modal depth ≤ k that are true at the actual world. "Higher-order" is then a checkable claim about the model, rather than a property of the story.

## 3. Framework assessment (P01-T-3)

**Main recommendation: one core semantics, two generators feeding it.** The core is the *finite probabilistic epistemic model* (PEM): worlds W, an actual world, a partition Π_i for each agent, an explicit prior μ (common or per-agent), and public or semi-public events with an observability specification. (a), (b) and (c) are fragments of the PEM. (d) and (e) are *generators* of behaviour or strategy tables, not ground-truth semantics in their own right.

**(a) Bayesian inference over specified policies (v0)**
- (i) Computation: posterior = μ(w)·P(o|w) normalized, in exact rationals.
- (ii) Unique answer: unique whenever P(o) > 0. Bands need a tie rule at R = 3.
- (iii) Cannot represent: anything higher-order. The policies are given, so no agent reasons about another agent.
- (iv) Pitfall: labels such as "level-3 strategic" claim a depth the tables do not encode. The v0 docstring admits this.
- (v) **ADOPT WITH RESTRICTION:** use it as the observation layer of the PEM only, never as evidence of higher-order reasoning.

**(b) Possible worlds / DEL with public (non-)announcements**
- (i) Computation: an S5 Kripke model, restricted on each truthful public announcement to the worlds where it holds. Non-announcement ("nobody stepped forward") is an announcement of ¬K formulas, and is valid *only under a protocol that is common knowledge*.
- (ii) Unique answer requires:
  - S5 (knowledge, not belief);
  - announcements that are truthful (otherwise the update is undefined or empty);
  - a speaking protocol stated explicitly;
  - synchronous rounds.
- (iii) Cannot represent: probabilities, false belief, lying, private or semi-private events. Those need action models (Baltag–Moss–Solecki product update) [R].
- (iv) Pitfalls:
  - Moore-type sentences become false after being announced ("unsuccessful updates") [R].
  - Cheryl's birthday had disputed readings of "I don't know" versus "I knew you wouldn't know" [R].
  - Inference from silence silently assumes the protocol.
- (v) **ADOPT WITH RESTRICTION:**
  - S5 only;
  - truthful public announcements, plus action models limited to "event E observed by subset G, and it is common knowledge that G observed it";
  - the protocol stated in the text;
  - \|W\| ≤ 64.

**(c) Partitional type spaces, common prior, common knowledge**
- (i) Computation: the meet of the partitions gives the common-knowledge cells. The Geanakoplos–Polemarchakis dialogue (alternating public posterior announcements, each refining the partitions by level sets) converges in finitely many rounds to agreement [R].
- (ii) Unique answer: exact rationals; prior stated explicitly. Without a common prior, posteriors are still computable but the agreement results do not apply [R].
- (iii) Cannot represent: action choice or incentives.
- (iv) Pitfalls: Aumann 1976 assumes common knowledge of *posteriors* and a common prior; applying "rational agents can't agree to disagree" without both is the textbook misuse [R]. The email game shows that "almost common knowledge" differs sharply from common knowledge [R].
- (v) **ADOPT**, merged with (b) into the PEM. It supplies the cleanest S2 lever: drop the common prior.

**(d) Level-k / cognitive hierarchy**
- (i) Computation: specify L0 explicitly; L_k best-responds to L_{k−1} (or, in CH, to a Poisson mixture of lower levels [R]).
- (ii) Unique answer only with an explicit L0, utilities, a tie-breaking rule and a stated level.
- (iii) As a ground truth for "what the agent does", level-k is a behavioural *model*. The "correct answer" is a modelling choice. Asking "what does a level-3 player do" is computable, but measures whether the solver can execute a recursion, not whether it can reason correctly about the agent.
- (iv) Pitfalls: results are highly sensitive to the L0 specification [R].
- (v) **REJECT as semantics; ADOPT as a generator** of the behaviour table that feeds (a). This turns v0's hand-written table into a computed one, which is exactly what the v0 docstring asks for.

**(e) Rationalizability / iterated dominance**
- (i) Computation: iterated elimination of strategies that are strictly dominated, *including by mixed strategies* (an LP at each step).
- (ii) Unique answer: the surviving set is unique and independent of elimination order for strict dominance [R]. With two players it equals rationalizability; with n ≥ 3, independent and correlated versions can differ [R], so one must be stated.
- (iii) Cannot represent: information structure (unless written in Bayesian-game form), or equilibrium selection.
- (iv) Pitfall: pure-strategy dominance checks miss strategies dominated only by mixtures. That is a natural S2 case.
- (v) **ADOPT WITH RESTRICTION:** two players, at most 5×5 strategies, strict dominance with mixtures, set-valued answers.

**(f) Signalling / persuasion**
- (i) Computation:
  - Signalling equilibria (Spence, Crawford–Sobel) have many equilibria, and the answer depends on the refinement chosen [R].
  - Bayesian persuasion with commitment, binary state: the sender-optimal value is the concavification of the sender's value as a function of the receiver's posterior, which is unique. The receiver's posterior under a committed signal is just (a).
- (ii) Unique answers exist for KG value questions; questions about which equilibrium is played are not well posed.
- (iii) Cannot represent: without commitment, no unique prediction.
- (iv) Pitfalls: confusing cheap talk with commitment; refinement disputes (for example the intuitive criterion) [R].
- (v) **REJECT equilibrium questions. ADOPT WITH RESTRICTION** for the commitment case: binary state, posterior or value questions. The commitment/no-commitment distinction is a good S2 lever.

**(g, added) Belief (KD45) with false beliefs and revision**
- **REJECT for v1.** The update after a surprise depends on a choice of revision policy, so there is no unique answer without extra specification that is hard to verbalize.

**(h) None / keep v0**
- v0 is correctly sized *for its own stated claim* (respecting evidence despite narratives).
- **KEEP** it as the S3/control subfamily and as the narrative-framing axis. Do not relabel it as higher-order.

## 4. Instance schemata (P01-T-4)

**Registered naive program set B, used for the shortcut certificate (C6):**
- B1: take messages at face value;
- B2: ignore the prior;
- B3: "k muddy ⇒ k rounds";
- B4: "rational agents agree immediately / eventually agree";
- B5: dominance checked against pure strategies only;
- B6: treat every announcement as public.

**SCH-1: Asymmetric-sight muddy agents (PEM, DEL fragment)**
- Parameters:
  - n ≤ 5 agents;
  - a directed "sees" graph G;
  - actual mud vector;
  - initial public announcement ("at least one");
  - a protocol: each round, all agents who know their own state step forward at the same time, and this is common knowledge.
- Answer: for each agent, the round in which it steps forward (or "never"). Computed by enumerating 2^n worlds, with each agent's partition given by G, then a public restriction per round.
- Naive reading: B3 gives "round = number of muddy agents".
- Valid method: enumerate worlds and delete those inconsistent with each round's public silence or step-forward.
- S2: one agent did not hear the initial announcement, and the others know this. The announcement is then semi-public: the condition "public and commonly known" fails. The correct answer, computed by action-model update, is typically "never" for some agents, which B6 gets wrong.
- S3: every agent is told its own state directly. The answer is round 1, and no epistemic structure is involved.

**SCH-2: Posterior dialogue (PEM, partitional)**
- Parameters:
  - \|Ω\| ≤ 12 states;
  - prior μ, either common or one per agent;
  - partitions Π_A and Π_B;
  - event E;
  - actual state.
- A and B alternately announce their exact posterior of E in public.
- Question: the posterior at round t, the round at which they agree, and the final values.
- Computation: Geanakoplos–Polemarchakis refinement (each announcement reveals the level-set cell).
- Naive reading: B4 says they agree at round 1, or average the two posteriors.
- Valid method: refine the partitions after each announcement.
- S2: the agents' priors differ (stated in the text), so the common-prior condition fails. The correct answer is persistent disagreement, which B4 gets wrong.
- S3: E is measurable with respect to both partitions from the start, so both know E. The answer is immediate and trivial.

**SCH-3: Strategic reporter with a generated behaviour table (d → a)**
- Parameters:
  - sender types θ ∈ {honest-incentive, deceptive-incentive};
  - explicit utilities;
  - L0 sender reports truthfully;
  - L1 receiver best-responds;
  - L2 sender best-responds to L1, with deterministic tie-breaking;
  - the observer's prior over types, and the stated level.
- Answer: the observer's posterior over θ after the message, in exact rationals, from the computed table.
- Naive reading: B1 (face value), or the narrative-driven "suspect the deceiver".
- Valid method: compute the recursion, then apply Bayes.
- S2: the narrative strongly suggests a motive to deceive, but the stated utilities are aligned. The "discount suspicious messages" move is then invalid; the failing condition is that there is no incentive to deviate. The correct posterior equals the face-value posterior.
- S3: the message comes from a sensor with a stated error rate, so the problem is plain v0-style Bayes.

**SCH-4: Dominance with a mixed-only dominator (e)**
- Parameters: a two-player game of at most 4×4 with rational payoffs; common knowledge of rationality is stated.
- Answer: the set of surviving strategy profiles under iterated strict dominance with mixtures, via LP.
- Naive reading: B5, or "pick the Nash equilibrium the story suggests".
- Valid method: iterated elimination with a check against mixed strategies.
- S2: a strategy is dominated only by a mixture. Pure-only elimination is then invalid (the failing condition is "pure dominance is enough"), and the survivor sets differ.
- S3: each player has a strictly dominant strategy at step 1, so only one level of reasoning is needed.

**Rule applying to all schemata:** every S2 instance is paired with an S1 *twin* that differs only in the one validity-deciding clause. This controls for length and vocabulary (CF09), and the clause difference is verified (§6).

## 5. Text-observable structure (P01-T-5)

| Property | Diagnostic question | Leak? |
|---|---|---|
| Publicness | Is every event observed by every agent, and is it common knowledge that it was observed? | **LEAKS the stratum** (S1/S2 in SCH-1) |
| Truthfulness | Can any statement be false? | Leaks the stratum if it is the lever |
| Protocol | Is it commonly known *when* agents must speak, so that silence carries information? | Leaks the stratum in silence variants |
| Prior | Is there one prior shared by all agents? | **LEAKS the stratum** (SCH-2) |
| Incentive alignment | Do the stated utilities give any agent a reason to misreport? | **LEAKS the stratum and nearly the answer** (SCH-3) |
| Commitment | Is the information policy fixed before the state is known? | Leaks the stratum (f) |
| Policy status | Are behaviours given, or must they be derived from utilities? | Safe |
| Dominance type | Is mixed-strategy dominance relevant? | Leaks the answer; it requires solving |
| Knowledge vs belief | Can agents be mistaken? | Safe (all v1 instances are S5) |
| Size | How many worlds and events? | Safe; it is a difficulty knob |

**Consequence for R2.** The problem state must declare *trigger-level* features (for example "agents announce posteriors in public") and must **leave the leaking validity features undeclared**, recording them as unknown. Otherwise S2 is empty by construction (§1). The leaking features belong only in the verifier's hidden labels.

## 6. Independent verification (P01-T-6)

**Building the verifier:**

1. **Different representation.** The generator works on explicit worlds in Python. The verifier should be one of:
   - a symbolic model checker, for example SMCDEL (BDD-based) [R] or DEMO [R], if available;
   - or an ASP/SMT encoding;
   - or an LP solver, for SCH-4.
2. **Different input.** The verifier consumes a formal spec *rebuilt from the rendered text* by a separate parser or annotator, never the generator's parameters. This catches verbalization bugs, which I expect to be the largest class of errors.
3. **Different author**, working from a written semantics document and not from `core.py`.
4. **Metamorphic checks.** The answer must not change when:
   - agents or worlds are relabelled;
   - bisimilar duplicate worlds are added;
   - irrelevant events are added.

   The verifier also independently re-checks the depth certificate (M, M′).
5. **Twin check.** Each S1/S2 pair differs in exactly one validity clause, and the verifier confirms that the two answers differ.

**What counts as independent enough:** points 1, 2 and 3 all hold, plus 100% agreement on at least 200 instances for each subfamily. Any disagreement is logged and its cause classified before the instance is excluded (R1).

**What it cannot catch:**
- Shared *specification-level* mistakes, for example both sides assuming that silence is informative when the text never states a protocol. C9 human-reading agreement is the only guard.
- Real ambiguity in natural language.
- Whether a depth-k distinction matters cognitively.
- Contamination.

## 7. Claim ceiling for Q-A (P01-T-7)

**Accuracy on these instances may show:**
- that the solver produced the answer required by the stated semantics, on these verbalizations, at the certified depth k and load L;
- with paired twins, whether the solver is sensitive to the specific validity clause;
- through the B-baseline, whether the solver beat specific registered shortcuts.

**It may not show:**
- theory of mind, recursive reasoning or level-k cognition, because a memorized algorithm or a bookkeeping procedure gives the same outputs;
- that errors are epistemic rather than parsing or arithmetic, unless the parse is probed separately (ask for the formal spec first, score it, and condition on it);
- that the solver reasons at depth k, if any program in B with depth below k scores as well;
- any generalization beyond S5/PEM. Belief, lying and revision are excluded.

## 8. Hidden assumptions and sharper hypotheses (P01-T-8)

**Hidden assumptions**

| ID | Assumption |
|---|---|
| T-A01 | Strata can be defined independently of the cards. They cannot, unless conditions are declared ahead of the cards (§1). |
| T-A02 | Obligations are not implied by triggers; otherwise S2 is empty. |
| T-A03 | The text fully determines the formal model (C4/C9). |
| T-A04 | Difficulty comes from modal depth, not bookkeeping load. Untested. |
| T-A05 | In arena sessions, solvers lack code execution (CF07). If they have it, Q-B reduces to "does the solver write the enumerator". |
| T-A06 | The "obvious reading" is shared across solver families. It may differ by model. |
| T-A07 | The unit of characterization can be the *schema × stratum*, not the instance. I recommend this: it reduces CF03, and twins share a problem state. |
| T-A08 | L01/L03 artifacts are not usable. Unverified. |
| T-A09 | The B baseline approximates what solvers fuckingly do wrong. |
| T-A10 | Card text is read as method, not as an answer hint. For SCH-3, "check incentive alignment" practically hands over the S2 answer (CF02). |

**Sharper hypotheses**

- **T-H0 (null):** for each S1/S2 twin, P, L, R and N differ by less than the Gate-2 margin δ in paired strict accuracy.
  - Falsifier: the interval for (P − L) on S1 excludes 0 and exceeds δ.
- **T-H1:** on S1, P beats L and R by at least δ, *and* the gain is concentrated where load is high.
  - Prediction: the gain rises with \|W\|×events.
  - Falsifier: the gain is flat across load levels or absent.
- **T-H2:** on S2, P's wrong-answer rate exceeds L's, *and* those errors match the B-program output the card licenses.
  - Falsifier: S2 errors under P are unrelated to the card's shortcut, which would mean they come from general confusion.
- **T-H3:** a generic enumeration control G (to be added as a fifth arm) matches P on S1 and beats P on S2.
  - Falsifier: P beats G on S1 by at least δ with no loss on S2.
- **T-H4:** for at least two schemata, the §6 verifier agrees on 100% of instances, *and* S2 twins are confirmed.
  - Falsifier: any unexplained disagreement in a subfamily.
- **T-H5 (headroom):** in arm N, the strongest solver's S1 accuracy lies in [0.2, 0.8] on high-load cells.
  - Falsifier: the pilot falls outside this range, in which case the result is "uninformative".

**Competing hypotheses the seed omits**

- **T-H6 (load, not depth):** accuracy is predicted better by log(\|W\|×events) than by certified depth k, comparing out-of-sample deviance on the factorial grid.
  - Falsifier: k adds predictive power after controlling for load.
- **T-H7 (any warning helps):** on S2, a control that states the validity clause without a method ("check whether everyone heard the announcement") matches P.
  - If true, the obligation text is doing the work and retrieval is not.
- **T-H8 (L01 suffices):** an existing DEL generator plus a model checker reproduces SCH-1-type headroom and twins.
  - If true, build only SCH-2 to SCH-4.

## 9. Relation audit (P01-T-9)

All ten are tagged [R].

1. `bernheim-1984 --formalizes--> level-k`: this is rationalizability, which assumes common knowledge of rationality (unbounded depth). Level-k comes from later bounded-depth models (Nagel, Stahl–Wilson).
2. `pearce-1984 --formalizes--> level-k`: same objection. Also, the Pearce node shares Bernheim's JSTOR link (1911391), which looks like a data error.
3. `belief-hierarchies --extends--> level-k`: wrong relation. Level-k is a behavioural truncation model, not an extension of Harsanyi/Mertens–Zamir hierarchies. At most "loosely parallels".
4. `strategic-reasoning --specializes--> level-k`: the direction is reversed. Level-k specializes strategic reasoning.
5. `baltag-moss-solecki-1998 --formalizes--> belief-hierarchies`: BMS formalizes action models and product update, not type-space belief hierarchies.
6. `carlsson-vandamme-1993 --formalizes--> information-design`: global games is about equilibrium selection under noisy private signals. Information design is later work and differs in kind.
7. `rubinstein-1989 --empirically-tests--> common-knowledge`: the email game is a theoretical paper, not an empirical test.
8. `spence-1973 --extends--> information-design`: anachronistic, and signalling without commitment is not information design.
9. `crawford-sobel-1982 --extends--> information-design`: cheap talk has no commitment, which is exactly what separates it from Kamenica–Gentzkow.
10. `aumann-1976 --extends--> belief-hierarchies`: Aumann uses partitions with a common prior, not belief hierarchies. The `formalizes common-knowledge` edge is fine.

**Also noted:**
- `plaza-2007` carries the date of a reprint; the original is around 1989. That makes `BMS-1998 extends plaza-2007` look anachronistic, even though the direction is correct.
- The Gemini 4 Argon nodes have nothing to do with this mission and look like retrieval noise.

**Cut for length:** formal definitions of the action-model update, and a size and power estimate for the paired twins.
