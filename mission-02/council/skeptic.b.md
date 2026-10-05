## 1. Kill attempt (P03-S-1)

**Do not proceed with Q-A and Q-B as one build-and-test package.** The cheapest way this design produces a misleading positive is: encode a narrow puzzle family and its answers, give a matched card a procedure tailored to that family, then show that the procedure changes answer accuracy. That would establish that extra instructions can affect scores on those items. It would not establish that the trigger matcher adds value, that the natural-language instances really specify the formal semantics, or that the solver used higher-order reasoning.

An independent program can agree perfectly with the generator while both implement the same mistaken or unstated interpretation of the story. And answer-only scoring cannot reveal whether the solver checked a card’s obligations, ignored them, or guessed correctly. A negative result is also easy to misread if the no-pack models are at floor or ceiling. The right first step is a **narrow, reusable-family audit**, not a broad v1 plus a four-arm efficacy study.

The wording itself is leading: “obvious reading is systematically wrong,” “method the solver chooses decides correctness,” and the H1/H2 framing invite the Council to assume that traps and useful cards exist. I treat those as hypotheses, not findings. The v0 facts and Mission 01 counts do not establish either proposition; the seed itself notes that Mission 01’s oracle shared a dispatcher with the grader.

## 2. Primary critiques

**S-CR01 — Target: Q-A, “minimal specification.”**  
**Flaw:** “Minimal” has no criterion, and the candidate formalisms are not interchangeable. A public-announcement update, inference over supplied behavior policies, level-k recursion, rationalizability, and signaling can define different objects and answer rules. Choosing one does not validate the others. **Severity: serious.** **Repair:** Choose one formalism and state its ontology, update rules, answer predicate, and uniqueness conditions. If the claim is about strategic policy generation, specify policies, incentives and tie-breaking; otherwise do not call a fixed-table inference task strategic reasoning.

**S-CR02 — Target: Q-A’s “higher-order” and “obvious reading”; H1.**  
**Flaw:** Answer accuracy alone does not establish that an answer *depends* on higher-order information or method choice. A cue, answer prior, or template could do the work. “Obvious reading” is not a specified baseline. **Severity: serious.** **Repair:** Require matched instances in which changing only a higher-order information/update condition changes the formal answer, then test a named simple baseline on them. If the answer-only format remains, limit the claim to accuracy on those items, not reasoning mechanism.

**S-CR03 — Target: Q-A’s reuse and novelty question.**  
Several close precedents reduce the case for building a new generator before an artifact audit. *MindGames* generates controlled DEL problems, verbalizes them in English, and states that its code and datasets are public [V].  *Hi-ToM* directly evaluates higher-order ToM through order four; it reports falling accuracy at higher order and no substantial benefit from its chain-of-thought prompting variant, with some drops on deceptive-communication items [V].  The L02 article page/abstract I could inspect describes a 2,784-sample DEL benchmark, but I could not verify its released artifacts from that material [S].  A further direct lead omitted from L01–L08 is *DEL-ToM*: its ACL abstract describes a DEL simulator and a process-belief verifier, and says code is available [S].   
**Severity: serious. Repair:** Make reuse the default. Identify the precise unmet requirement—perhaps text-to-semantics auditing or an obligation-ablation experiment—and show that existing artifacts cannot meet it before building another family.

**S-CR04 — Target: R1 and H4.**  
**Flaw:** A separate implementation is not necessarily an independent semantic check. It may consume the same hidden parameters and repeat the same interpretation; it may verify arithmetic while never checking that the rendered text entails those parameters. Excluding disagreements under a prewritten rule is safer than ad hoc exclusion, but disagreement still signals that the family is not yet reliably specified. H4’s “two subfamilies” is also an arbitrary gate if the claim is only about one narrow family. **Severity: serious. Repair:** Separate three checks: independently recompute answers from a frozen formal specification; independently reconstruct the formal instance from the rendered text; and have a blinded reviewer audit edge cases. Report disagreements on the full original denominator. Require a second subfamily only if making a broader scope claim.

**S-CR05 — Target: R2 and the trigger matcher.**  
**Flaw:** “From text alone” does not specify who codes states, how disagreements are resolved, or how to prevent knowledge of schema and answers leaking into feature labels. If a trigger cannot be reliably identified from the text, the retrieval intervention is not operational. **Severity: serious. Repair:** Freeze a feature dictionary and coding procedure; have two blinded coders independently record present/absent/unknown; publish their agreement and all adjudications. Choose one unit in advance: instance-level if testing instance retrieval, schema-level if testing a fixed schema recipe. Do not switch after seeing results.

**S-CR06 — Target: H0–H3 and R3–R4.**  
**Flaw:** The arms do not yet isolate trigger-matching. A matched card may contain a more useful algorithm than L’s “generic prose”; R may be actively distracting; and neither comparison alone distinguishes a good procedure from correct assignment of that procedure to the right instance. H3 is testable only if L is explicitly defined as the generic explicit-state procedure. **Severity: serious. Repair:** Specify L as a strong, actionable generic state-update control; add a **yoked/unmatched-card** control using the same cards and format on nonmatching instances; and match output budget and formatting. Freeze the exact texts. Define the primary H1 contrast and an equivalence criterion for H0 before the trial.

**S-CR07 — Target: H2 and R5.**  
**Flaw:** Final correctness cannot show whether obligations prevented misapplication. A correct answer might be a guess; an incorrect answer might arise elsewhere. R4 also lacks a method-only versus method-plus-obligations contrast. **Severity: fatal to the obligation claim as written. Repair:** Add a structured applicability response (yes/no/unknown for each obligation, before the answer) and compare the full card with the same card minus obligations. Construct matched S1/S2 items with the validity-relevant facts available in text but without an easy status cue. If those changes are out of scope, drop the claim about obligations and report only final-answer effects.

**S-CR08 — Target: R6–R7.**  
**Flaw:** Opaque IDs do not blind the dispatcher to the semantic contents of each prompt. Manual copy-paste also leaves ordering, fresh-session state, model-version drift, and tool/system settings as possible treatment confounds. “Paired by instance” does not solve dependence among paraphrases from the same schema. **Severity: serious. Repair:** Use logged, stateless, fresh sessions; randomize dispatch order; pin versions/settings where possible; record unavailable settings rather than implying control. Set inference at the schema/base-puzzle cluster level, and calculate sample size for the fixed primary contrast—not merely the number of generated rows.

**S-CR09 — Target: R8 and H5.**  
**Flaw:** “Strongest feasible solvers” is not a selection rule. Raising difficulty after a floor/ceiling pilot can become task tuning. **Severity: serious. Repair:** Name the primary and replication solvers before the pilot, set explicit headroom thresholds, and keep pilot schemas disjoint. If changing the family after seeing pilot outcomes, re-register and use a new pilot set.

**S-CR10 — Target: R9 and the H0/H2 conclusions.**  
**Flaw:** “Does not beat the margin” is a sensible stop rule, but a wide interval is not evidence of equivalence. Nor does an obligation check that never fails show obligations are ineffective if the solver never attempted the move. **Severity: serious. Repair:** Pre-register the effect interval and a rule separating “evidence against the target margin” from “inconclusive.” Score applicability decisions separately; otherwise stop the obligation subquestion as unmeasured.

**S-CR11 — Target: R10 and the candidate claim ceiling.**  
**Flaw:** The ceiling is appropriately conservative about generalization, but even a clean accuracy gain would not show recursive reasoning, actual method selection, or a general trigger-matching benefit. **Severity: minor if respected; serious if later overstated. Repair:** State that results concern the frozen prompt packages, formal family, model versions, and accuracy metric only. Treat mechanism and transfer claims as outside scope.

## 3. Confound and circularity register

- **S-CF12 — Schema pseudoreplication.** Many seeds or paraphrases may share one underlying puzzle structure. It would appear as tight item-level intervals but unstable results when whole schemas are held out. **Address:** Hold out schemas and cluster inference/resampling at the base-puzzle level; R7’s instance pairing alone is insufficient.
- **S-CF13 — Common-mode semantic error.** Generator and verifier can be separate codebases yet share an incomplete interpretation of announcement, silence, or observation rules. It would appear as perfect code agreement alongside reviewer disagreement or ambiguous renderings. **Address:** Independent text-to-semantics audit and hand-checked edge cases, not just R1 implementation separation.
- **S-CF14 — Applicability-status cue confounding.** S1 and S2 may differ in obvious wording that labels a card valid or invalid. It would appear as strong S1/S2 performance differences even when the card is ignored. **Address:** Matched minimal pairs, randomized names/order, and the obligation-ablation/checklist design in S-CR07.
- **S-CF15 — Cross-arm carryover.** The same solver may see the same base puzzle in multiple arms and reuse an earlier answer or method. It would appear as performance varying with dispatch order. **Address:** Fresh stateless sessions, randomized order, and no repeated item in a shared conversation.
- **S-CF16 — Serialization/parser artifact.** A card may change answer formatting, causing strict-scoring failures unrelated to reasoning. It would appear as arm-specific malformed-output rates. **Address:** Identical answer schema and parser across arms; report parse failures separately as well as counting them as errors.
- **S-CF17 — Multiple-comparison inflation.** Four arms, three strata, two solver families, and several outcomes create many possible favorable contrasts. It would appear as one striking subgroup result among mostly null comparisons. **Address:** One primary contrast and outcome; pre-register a hierarchy or multiplicity correction.
- **S-CF18 — Card-to-family co-design.** Frozen cards can still be tailored to a known family by their authors. It would appear as gains confined to the schemas whose features inspired the card. **Address:** Hold out entire schemas from card authorship or evaluation, and test the frozen cards on those held-out schemas.

## 4. Three executable falsification experiments (S-FALS01–S-FALS03)

**S-FALS01 — LOCAL: bounded semantics/oracle challenge.**  
Pick one subfamily only: for example, finite possible-world models with explicit observation partitions and truthful public announcements. Freeze its formal specification. Independently implement the verifier and exhaustively compare it with the generator on all models in a bounded domain (two agents, two-to-four worlds, up to three announcements); independently audit 20 rendered edge cases without access to answers. If silence is included, its event semantics must be explicit; otherwise exclude silence from this subfamily.  
**Pass:** exact agreement on every bounded case and 20/20 texts judged to specify one formal instance. **Fail:** any unresolved disagreement or ambiguous text; stop or narrow this subfamily before solver testing.

**S-FALS02 — LOCAL: trigger-reliability and surface-shortcut audit.**  
Create 400 balanced instances, including 200 matched counterfactual pairs, with schemas held out between training and test. Two blind coders assign problem states from text alone. A preregistered shallow classifier uses only style/position/length/name-order cues—not relational or update computation—to predict the answer.  
**Pass:** coder agreement κ ≥ 0.80, unknown trigger status ≤ 10%, and held-out classifier accuracy ≤ 55%. **Fail:** revise the family or matcher; do not interpret a pack effect as evidence for trigger matching until this test passes.

**S-FALS03 — MODEL RUNS: no-pack headroom pilot.**  
Use two named solver families, 24 disjoint pilot S1 items per solver, and two independent fresh-session runs per item: **96 pastes total**. Run only the no-added-text arm; use outputs only for the R8 headroom decision, not for treatment-effect comparisons.  
**Pass:** both preselected solvers score between 20% and 80% on strict correctness. **Fail:** if either is outside the band, reshape/re-register the family or stop Q-B; do not call a later null a card failure.

## 5. Claim ceiling and abort conditions (P03-S-2)

**The study cannot justify** that a solver used recursive reasoning, level-k reasoning, or theory of mind; that the task family measures epistemic reasoning generally; that a card is validated for other models or domains; or that obligations prevent misuse without the S-CR07 ablation and observable applicability measure. It also cannot justify that trigger matching itself adds value unless matched cards beat the yoked/unmatched-card and generic-method controls.

- **S-ABORT01:** Stop the affected subfamily if the independent verifier/text audit leaves any semantic disagreement or underdetermined instance unresolved.
- **S-ABORT02:** Stop the “higher-order” claim if no matched counterfactual shows the answer changing because of a higher-order information/update condition.
- **S-ABORT03:** Stop Q-B if trigger coding fails the preregistered reliability threshold or uses answer/schema information unavailable in the text.
- **S-ABORT04:** Stop the obligation subquestion if validity status cannot be inferred from the text, or if obligations are not compared against the same move without obligations.
- **S-ABORT05:** Report Q-B as uninformative if headroom fails for the preregistered solver set, or if session/model conditions cannot be recorded well enough to interpret arm contrasts.
- **S-ABORT06:** If intervals are too wide to distinguish the registered margin from no meaningful effect, report inconclusive and stop expansion under R9; do not relabel that result as evidence for H0.

## 6. Attack on the strategy-pack idea itself (P03-S-3)

A trigger matcher is a classification rule, not evidence that its labels identify when a strategy helps. If the instance taxonomy and card triggers are designed together, the matcher may merely attach a hand-selected recipe to a known puzzle type. A positive P-versus-N result could then be the value of receiving an explicit algorithm, not the value of retrieval. Even P-versus-L is uninformative if L is weak or less specific; even P-versus-R is uninformative if random cards are distracting.

Reusable reasoning structures and retrieval already have close precedents: *Self-Discover* describes composing reasoning modules [S], and *Buffer of Thoughts* describes retrieving thought templates [S].  The plausible narrower contribution is validity-aware matching—not the existence of a card library. Prior results also caution against assuming that more explicit reasoning instructions help: *GTBench* reports that advanced prompting methods do not always help [V]. 

**A fair negative result:** with adequate headroom and power, P fails to beat the strong generic procedure and yoked-card controls by the registered margin on held-out schemas; the interval rules out the target benefit. For obligations, the full card fails to improve applicability decisions or S2 accuracy over the same move without obligations. That would be a negative for these cards and this matcher—not proof that every retrieval system is useless. A wide interval is inconclusive, not a fair null.

**A positive result I would still distrust:** P wins only against weak prose/random-card controls; the gain disappears on held-out schemas; S1/S2 validity is signaled by surface wording; or the apparent benefit comes from output-format changes. I would also distrust an obligation claim if accuracy changes but applicability decisions are not measured. In any of those cases, the registered comparison may be real while the interpretation “trigger matching/obligations worked” is not.

## 7. Outcome forecast (P03-S-4)

These are subjective priors, not findings. The literature is consistent with difficulty increasing on higher-order items without guaranteeing that prompting repairs it: *Hi-ToM* reports order-related declines and limited prompting gains [V], while *GTBench* reports that advanced reasoning prompts do not always help [V]. 

| Regime | Subjective expectation | What would change my mind |
|---|---|---|
| **H0** | The strict all-arms-equal null is possible, but I expect any explicit procedure may beat N on some hard items. I expect little or no reliable **P-over-strong-L** gain. | A well-powered, held-out comparison showing P beats both strong L and yoked cards by the registered margin. |
| **H1** | Low-to-moderate chance of benefit over N; lower chance of a trigger-specific benefit over a strong generic method. | Replicated P-over-L and P-over-yoked gains on held-out schemas in both solver families. |
| **H2** | Packs may hurt in S2 if the move is over-applied; I doubt prose obligations alone will reliably prevent that. | Full-card versus method-only results showing fewer precondition violations and fewer wrong answers in S2, without a matching surface cue. |
| **H3** | Most likely explanation for a positive result: generic explicit state-update instructions account for much of the gain. | P consistently beats an equally actionable generic state-update control. |
| **H4** | Likely achievable for one narrow finite semantics; unlikely to hold for the seed’s entire menu of formalisms without further assumptions. | Independent implementations plus blinded text audits agree exactly on all registered cases and edge cases. |
| **H5** | Likely mixed: simple/canonical items may be at ceiling while genuinely difficult items may be at floor. | The disjoint no-pack pilot places both preregistered solvers inside the headroom band. |
