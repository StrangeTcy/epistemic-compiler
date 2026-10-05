# Mission 02 Council round 1 — compiler cross-critique

**Prepared:** 2026-10-05
**Status:** compiler-authored synthesis of the stored Council responses; not a Council vote, evidence report, or human gate decision.

## Scope and source discipline

This cross-critique addresses Mission 02's current seed (`../seed.yaml`) and the seven stored response bodies:

- Theorist: `theorist.md`
- Experimentalist: `experimentalist.a.md`, `experimentalist.b.md`
- Skeptic: `skeptic.a.md`, `skeptic.b.md`
- Prior-Work Killer: `prior_work_killer.a.md`, `prior_work_killer.b.md`

The human disposition is to keep the separate earlier Arena dialogue out of round 1. Its contents are excluded here; this document uses only the current seed and the four Council roles' responses. No new Arena/model call was made. I did not independently check literature citations, implementation claims, or the role responses' statistical calculations while preparing this synthesis. Preserve each response's own `[V]`, `[S]`, and `[R]` labels as reported; they are not upgraded by appearing in this document. The older responses have incomplete legacy provenance; the Skeptic sidecars record the missing Arena mode, exact Arena-displayed model label, and session time.

## Executive synthesis

**No response supports proceeding with the registered design unchanged.** The responses differ on how much of Q-B survives, but converge on a staged **reuse / narrow / specify / reassess** path—not on running an experiment now.

The strongest shared findings are:

1. **The current Q-A is carrying too many claims.** A formal answer computation, an independently reliable verifier, a faithful English rendering, higher-order dependence, and a novel instance family are separate properties. A successful checker comparison would establish only a portion of that chain. The Council repeatedly asks for reuse and a narrower contribution before building a broad generator.
2. **The current Q-B controls do not isolate every claimed mechanism.** P/L/R/N can compare prompt packages, but do not by themselves show that trigger matching adds value or that obligations prevent misuse. Different proposed controls answer different questions; they should not all be treated as interchangeable.
3. **The text-to-semantics link is a first-order risk.** Independent programs can agree on a formal instance while the rendered English fails to specify it. Conversely, exposing the validity fact in text or in the characterization can make S1/S2 status a cue rather than a test of the card.
4. **The proposed manual-dispatch budget has no settled power basis.** The two Experimentalist samples and Skeptic samples use different definitions and assumptions, and their estimates do not reconcile. A wide interval must not become a retirement decision.
5. **The claim ceiling should remain narrow.** Accuracy on a frozen family would not establish recursive reasoning, theory of mind, or a general retrieval mechanism. Prior-work claims remain to be verified at source level.

The Council has therefore produced useful objections and candidate repairs, but not a single agreed design. This cross-critique does not select one or approve Gate 1.

## Agreement and disagreement map

| Issue | Convergence across roles | Unresolved disagreement / cross-critique |
|---|---|---|
| **Q-A scope and reuse** | Theorist, both Experimentalists, both Skeptics, and both Prior-Work Killers reject a broad novelty claim for generated DEL/ToM tasks, formal ground truth, or “higher-order” as a label. They favor reusing existing artifacts where semantics fit. | Theorist proposes a finite probabilistic-epistemic core with several subfamilies; the Experimentalists sketch DEL and behavior-policy families; the Prior-Work Killers prioritize a narrow game-generated-policy gap; both Skeptics say to start with one audited subfamily. These are alternatives, not one merged specification. The named prior-art claims are not all independently verified here. |
| **Text and verifier validity** | Theorist, Skeptic-a, Skeptic-b, and Prior-Work Killer-b distinguish checking formal computation from checking that English denotes the intended formal object. | Experimentalist-a/b specify independent implementations and checker agreement, but that alone does not answer the text-faithfulness objection. A human reconstruction/audit, its sampling rule, and an ambiguity threshold still need an agreed protocol. |
| **S1/S2 and characterization** | Theorist, both Skeptics, and both Experimentalists recognize that strata and characterization can leak information or become difficult to construct. | Theorist says card-independent validity conditions must be fixed first; Experimentalist-b accepts schema-level characterization that can reveal S1/S2 status to the matcher; Skeptic-b asks for blinded coders and reliability tests. The intended information available to the matcher, solver, and verifier is not yet reconciled. |
| **What Q-B measures** | All roles warn that a positive P-versus-no-text result could be the value of useful instructions, not of retrieval. The prior-work responses also reject generic retrieval as a novelty claim. | Proposed primary contrasts differ: Experimentalist-a/b favor P−L; Skeptic-a asks for P versus all-cards and a fixed recipe; Skeptic-b asks for a yoked/unmatched card and an obligation ablation; Prior-Work Killer-b wants the same card with and without obligations. Each contrast tests a different causal claim. |
| **Power and dispatch** | Both Experimentalists and both Skeptics regard the 60-paste plan as incapable of answering the main efficacy question; all call for an uninformative outcome distinct from a negative result. | Their numerical estimates, sample allocations, solver counts, and accounting units differ. No estimate should be carried into Gate 2 until one estimand and one reproducible calculation are fixed. |
| **Novelty and evidence** | The Prior-Work Killers most directly narrow the novelty language; the Theorist and Skeptic responses independently warn against mechanism claims and unverified leads. | The Prior-Work Killers' literature matrix contains several `[S]`/snippet-level and unchecked claims. The claimed surviving wedges—game-generated policies, obligation efficacy, or the controlled evaluation design—remain hypotheses until targeted source checks establish the gap. |

## Cross-critique by role

### Theorist (P01-T)

**What it contributes.** The response gives concrete well-posedness criteria (unique answers, finite bounds, depth and shortcut certificates), separates semantics from behavior generators, and identifies the danger that card-defined S2 strata can become circular. Its warning that accuracy does not prove a reasoning mechanism is consistent with the more conservative Skeptic and Prior-Work Killer responses.

**What needs challenge.** The proposed “one core semantics, two generators” still spans several substantially different subfamilies; the response's own examples include DEL, common-prior dialogue, level-k policies, dominance, and persuasion. That is a large program, not yet a minimal v1. Its proposed hidden validity labels also leave an operational question: if the feature is omitted from the matcher, how is its status evidenced and independently checked; if it is exposed to the matcher or solver, can it leak the answer or stratum? The proposed fifth generic-enumeration arm and multiple schemata also need to fit a feasible, single-primary design. Finally, the response marks its literature claims `[R]`; they remain leads, not settled facts.

### Experimentalist samples (P02-E-a and P02-E-b)

**What they contribute.** Both specify observable trial records, controls, pilots, and stop conditions more concretely than the seed. Sample **a** makes P−L on S1 its primary contrast and argues for reducing arms; sample **b** adds a detailed dispatch plan, test-retest, surface-feature checks, and an explicit distinction between a pilot and a registered comparison. Both warn that 60 pastes cannot settle H1–H3.

**What needs challenge.** Sample **a** proposes a deterministic API solver, while the seed fixes manual Arena dispatch in R6. That is a change to the target channel, not merely an implementation detail; it would need a human Gate 1/Gate 2 decision. Its section 5 also does not reconcile its stated S1 sample requirement with the smaller S1 count in its 400-trial allocation. Sample **b** likewise needs a single accounting table: its 400-paste allocation describes one primary solver, while the second-solver replication is additional unless explicitly budgeted. Neither P−L nor P−R alone tests the matcher against a fixed recipe/all-card dump, and neither response specifies the same-card/no-obligations contrast needed to attribute an effect to obligations. Sample **b**'s claim that schema-level characterization intentionally reveals stratum status also conflicts with the leakage concerns raised by the Theorist and Skeptics; it needs an explicit threat model, not just a declaration that the leak is intended.

### Skeptic samples (P03-S-a and P03-S-b)

**What they contribute.** Sample **a** emphasizes the English-to-formal-instance gap, missing retrieval controls (all cards and a fixed recipe), inadequate power, and an underpowered-null failure mode. Sample **b** adds schema pseudoreplication, applicability-status cues, obligation ablation, held-out schemas, multiplicity, and a strong generic-method control. Together they explain why an answer-only score cannot establish that a card's obligations were checked.

**What needs challenge.** Their proposed fixes are extensive and costly: extra arms, human audits, multiple coders, oracle pilots, schema holdouts, and several thresholds. The responses do not establish that all those thresholds (for example, classifier AUC or coder-agreement cutoffs) are calibrated or mutually compatible. Skeptic-a's 120–150 paired-instance estimate and the other samples' estimates use assumptions that need a common, reproducible calculation. Skeptic-a's proposed P/A/F pilot and Skeptic-b's yoked-card/obligation controls should not be combined indiscriminately; first decide whether the primary question is retrieval value, fixed-recipe value, or obligation efficacy. Otherwise the “repair” becomes a larger underpowered factorial design.

### Prior-Work Killer samples (P04-PW-a and P04-PW-b)

**What they contribute.** Both reject broad novelty claims and ask for a reuse-first Q-A. Sample **a** leaves a possible narrow, controlled Q-B evaluation; sample **b** stresses that obligations need a same-card ablation and that a general “retrieval helps” claim is already too broad. Both identify the need to distinguish a formal checker from validation of the natural-language rendering, and both set a conservative claim ceiling.

**What needs challenge.** The two samples do not fully agree on the surviving Q-B contribution: a controlled retrieval test, an obligation-specific test, or a game-generated-policy family. That choice must be made before “novelty” can be assessed. Their detailed literature claims include different levels of verification, including search snippets and explicit unchecked leads; this cross-critique has not upgraded them. The claims that a particular paper or artifact “kills” a wedge, and the converse claim that a gap survives, require targeted primary-source review before they are used to amend the seed or justify Gate 2.

## Design tensions that remain unresolved

### 1. The family can make the intervention tautological

Theorist and Skeptic-a point out that if Q-A selects examples specifically because an obvious method fails and the solver must choose another method, then Q-B can reward a prompt that states the selected method. That result would show that useful method text helps on method-sensitive examples; it would not establish trigger matching or the Strategy IR. A family-selection rule should therefore be fixed independently of the desired P effect, and the headline claim should match what the construction actually tests.

### 2. “Independent verifier” has at least three layers

The responses use “independent” for different things. A Gate 1 plan needs to distinguish:

1. independent recomputation of the answer from a frozen formal specification;
2. independent reconstruction of that specification from the rendered text; and
3. independent audit of the assumptions encoded in the specification itself.

Agreement at layer 1 does not establish layers 2 or 3. A text-faithfulness sample and a written semantics review are not replaced by a second implementation of the same hidden parameters.

### 3. Controls should be matched to the claim

The seed's P/L/R/N arms answer some prompt-content questions, but they do not cover all the proposed claims:

- **P versus strong L** asks whether the specific card adds value beyond a genuinely actionable generic method.
- **P versus all cards, fixed recipe, or a yoked card** asks whether trigger-based selection adds value beyond dumping or assigning methods without matching.
- **Full card versus the same card without obligations** asks whether obligations add value.

Those comparisons are not substitutes. The human should select one primary causal question and one primary contrast before considering secondary arms. Random cards drawn from unrelated families risk measuring distraction rather than retrieval.

### 4. S1/S2 may conflate validity with difficulty or a visible cue

If an S2 instance includes a clause that plainly says “private” or “untruthful,” the clause may make S2 easier to classify even if the card is ignored. If that clause is withheld, the solver or matcher may lack the information needed to assess validity. The responses propose minimal pairs, blind characterization, held-out schemas, and audits, but do not yet converge on one procedure. The feature dictionary, what each actor sees, the characterization unit, and the status-labeling rule must be specified together.

### 5. The power arithmetic is not decision-ready

The responses variously count “trials,” “pastes,” paired instances, pilot responses, and solver replications. Their assumed baseline, discordance, effect margin, strata shares, primary contrast, and multiplicity burden differ. Before any solver study, one calculation must state all of these, include the actual feasible dispatch cap, cluster repeated items by base schema, and distinguish an inconclusive interval from evidence against the registered effect. The seed's R9 retirement rule cannot be used as a proxy for adequate power.

## Candidate Gate 1 checklist (not a decision)

For a human Gate 1 disposition, the Council's convergence suggests resolving these items in writing:

1. **Scope:** choose one narrow Q-A family/semantics, or defer Q-A; state what is being reused and what is genuinely missing.
2. **Claim:** state whether Q-B concerns generic method text, trigger matching, obligation efficacy, or a selected subset. Do not bundle these into one result.
3. **Text validity:** specify the formal verifier, the independent text-to-model audit, and how disagreements or ambiguous prose are handled.
4. **Characterization:** fix the unit, feature dictionary, blinding/access boundaries, and a reliability/leakage test before any solver output.
5. **Comparison:** choose one primary contrast and matched controls that identify that claim; set secondary analyses and multiplicity rules separately.
6. **Feasibility:** reconcile the manual-dispatch budget and power calculation; register an explicit “uninformative” outcome if the target precision cannot be reached.
7. **Novelty and claims:** verify the specific prior-art leads required for the chosen wedge and state the narrow claim ceiling.

**Compiler recommendation, not Gate 1 approval:** do not authorize Gate 2 or a paid/solver experiment from the current seed and response set. Request a narrowed, source-checked Gate 1 revision first. Gate 1 remains a human decision; this cross-critique neither approves nor rejects it on the user's behalf.
