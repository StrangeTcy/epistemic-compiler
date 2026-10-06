# Epistemic Games — ladder and progression proposals

This file isolates the dialogue's explicitly ordered ladders, sequences, and escalation plans. It is a historical record, **not an approved capability taxonomy**. Most rows below are assistant-generated; the user did not approve a single ladder, asked that all 15 research questions be preserved, and explicitly rejected forcing them into one capability scale.

The source locations below point into `epistemic games_copyable.md`. `Assistant proposal` identifies model-authored material. `Rejected / superseded` means the dialogue later disputes the ordering or the claim. A progression in experimental claims or implementation work is not automatically a progression in an agent's capability.

## 1. E0–E8 environment-family ladder (assistant-proposed; unapproved)

**Source:** primary dialogue lines 840–890, after the assistant proposes using a model debate and adversarial criticism to generate evaluation environments.

```text
E0  ordinary decision problem
E1  hidden information
E2  deceptive signalling
E3  higher-order belief
E4  belief-state shaping
E5  attention manipulation
E6  hypothesis-space manipulation
E7  opponent-model manipulation
E8  recursive epistemic-process manipulation
```

The assistant says to keep task structure matched while altering epistemic conditions, then asks whether capability transfers monotonically across the sequence or has qualitative discontinuities.

**Status and limitations:** this is a model-generated environment-family ordering, not a user-approved research roadmap, validated measurement scale, or demonstrated monotonic capability ladder. The user asked about using Arena Battle models but did not authorize running them. No Arena/model review was initiated for this extraction. Later dialogue also warns against treating an apparent behavioral effect as attention or process control without the corresponding controls.

## 2. Level-k reasoning and “epistemic strategy-space manipulation”

**Source:** lines 134–170.

The assistant begins with a recursive-belief example:

```text
A models B
A models B's model of A
B models A's model of B
both may reason about the other's finite recursion depth
```

Its constructed example has A estimate that B usually reasons to depth 2; A presents evidence intended to induce a depth-2 prediction; A anticipates that B knows A understands this; A then considers an apparent depth-3 counterstrategy; B considers whether A is exploiting that recognition.

The assistant calls the result **“epistemic strategy-space manipulation.”**

**Status:** an illustrative assistant-authored sequence, not an observed capability, user-approved label, or universal extension of level-k theory. It is included because it is the dialogue's clearest “level-k to epistemic manipulation” passage.

## 3. Belief-to-process ladder (explicitly rejected as one ascending ladder)

**Source:** lines 1240–1268.

An assistant response first writes the following as an apparent ascent:

```text
belief
→ attention
→ hypothesis generation
→ opponent model
→ recursive epistemic control
```

The same response immediately says to **stop treating it as one ascending ladder**: these are different variables. A changed test choice after learning that a source is unreliable does not prove that the underlying inquiry procedure changed. It replaces the single ladder with an intervention-to-outcome diagram whose possible targets are observations, source beliefs, attention allocation, information acquisition, hypothesis space, update policy, and opponent model, with subsequent inquiry and outcomes measured separately.

**Status:** the ascending interpretation is rejected in the dialogue. Preserve the components as independently testable dimensions, not successive rungs.

## 4. Other assistant-proposed conceptual progressions

### 4.1 Deception to process intervention

Several passages present variations on a conceptual movement from changing a proposition or belief toward influencing how another agent forms, tests, or updates beliefs. One version compares ordinary persuasion, higher-order beliefs about the persuader, and redirecting the target toward a different question (lines 393–444). Another distinguishes deception, misdirection, illusion, ontology attack, and epistemic-process control (lines 911–974).

**Status:** these are explanatory contrasts and candidate categories, not an agreed strict ordering. Their definitions can overlap, and the dialogue does not operationalize every rung.

### 4.2 Cross-field path to MI-13 and LLM evaluations

**Source:** lines 352–356 and 452–473.

```text
belief hierarchies
→ higher-order reasoning
→ signaling / information design
→ deception / opponent modeling
→ reflexive control
→ influence operations
→ Pelevin's fictional models, including MI-13
→ modern LLM strategic-reasoning evaluations
```

The assistant offered this as the intended conceptual bridge. An earlier attempt substituted *Generation П* and an MI5/CIA tangent; the user corrected it to **MI-13 in *«Возвращении Синей Бороды»*** and corrected the Gilbo phrase to **«дезонтология» / «8-й управленческий уклад»**. The model's chain remains an assistant-authored map, not a verified intellectual genealogy or capability ladder. The fictional node is not evidence about real-world mechanisms.

### 4.3 Hidden state to agent action

**Source:** lines 932–974.

```text
physical hidden state
→ observable events
→ attention allocation
→ hypothesis generation
→ causal/world-model update
→ prediction
→ action
```

The assistant uses this as a candidate process description for magic and misdirection, then suggests that an intervention could occur upstream. It is a proposed process diagram, not a demonstrated architecture or capability scale. The later design critique says an explicit attention claim needs an acquisition-budget manipulation; supplying a complete event transcript does not establish attention control.

### 4.4 Recursive misdirection

**Source:** lines 948–961.

```text
A misdirects B
→ B suspects misdirection
→ A models that suspicion
→ A chooses a second-order misdirection
```

This is an assistant-authored game sketch. It identifies a possible recursive structure; it is not a result about models or a prescribed ordering of research questions.

## 5. Attacker ablation conditions (A0–A2; not a maturity ladder)

**Source:** lines 1306–1338.

```text
A0  no opponent model
A1  belief model of opponent
A2  model of opponent's inquiry dynamics
```

The assistant proposes these as experimental conditions for testing whether attacker performance depends on opponent-model information.

**Status:** ablation labels, not a claim that every attacker must develop through these stages. A comparison requires matched conditions and actual outcomes. Later dialogue distinguishes attacker ability, target susceptibility, and model dependence rather than treating a sophisticated behavior as proof of opponent modeling.

## 6. “Eventually” escalated experiment claims

**Source:** lines 5667–5795, especially 5774–5793.

The assistant labels this an “eventual hierarchy”:

```text
an intervention exists
→ target is behaviorally susceptible
→ attacker can construct an effective intervention
→ attacker benefits from modeling the target
→ target detects the intervention and recovers
→ recursive attacker/defender game
```

The surrounding text associates different claims with separate experiments: an initial matched-presentation effect; a presenter that constructs a validated intervention; a comparison of accurate, shuffled, or absent target profiles; and later detection/recovery or recursive interaction.

**Status:** assistant-proposed claim-escalation framework. The stages mark what evidence might license increasingly specific claims; they do not establish a fixed capability order, and the later stages are not prerequisites for all 15 questions. Black-box behavioral evidence does not license internal-mechanism claims.

## 7. PR / implementation order (engineering sequence, not science hierarchy)

The dialogue contains several non-identical implementation plans. Preserve their changes rather than silently combining them.

### 7.1 Initial six-PR proposal

**Source:** lines 5602–5650.

```text
PR1  pure domain and oracle
PR2  runner and analysis
PR3  infrastructure pilot (50 episodes; no model-evidence claim)
PR4  preregistered defender experiment
PR5  model presenter with constrained fact IDs and emphasis
PR6  opponent-model ablation and recovery
```

The dialogue describes the PR5 presenter as emitting only ordered fact IDs and emphasis choices. The PR6 comparison is accurate profile versus shuffled profile versus no profile, followed by corrective evidence.

### 7.2 Revised sequence in the later actionable-spec draft

**Source:** lines 6045–6066.

```text
PR1    domain and oracle
PR1.5  offline scripted pilot and validity checks
PR2    plan / runner / CLI / artifacts
PR3    infrastructure pilot; no scientific claims
PR4    preregistered defender experiment
PR5    model presenter (named v0.2 in that draft)
PR6    recovery (named v0.3 in that draft)
```

That draft specifies an `exclusion_8x6` primary template, three budgets, four validity checks, and separate reporting for inquiry, belief, and outcome measures. These are design proposals from the transcript, not evidence that the described files, tests, results, or PRs exist. In particular, the draft's statement that PR1 had shipped must be checked against the repository, not accepted solely because it appears in the dialogue.

**Status:** implementation planning, not a capability hierarchy and not an instruction to implement or run the plan in this extraction.

## 8. Version labels and proposed blog series

The conversation variously labels an initial track v0.1, a model presenter v0.2, and recovery v0.3. These are version-scope proposals, not a theory of increasing intelligence.

A proposed three-post order appears at lines 5388–5397 and 6382–6388:

```text
“The Next Question Is Part of the Game”
→ “Lying With Truth”
→ “The Presenter and the Investigator”
```

This is an assistant-generated editorial sequence. Draft titles and text are not proof of publication or user approval. The current user instruction says blog writing is stopped for now; this list is preserved as dialogue history only.

## 9. Research, analysis, and reproducibility sequences (not capability ladders)

### 9.1 Baseline-to-next-generation workflow

**Source:** lines 979–1004. In response to the user's then-current Atria-Dawn run and possible future writing/spec work, the assistant proposes:

```text
Atria-Dawn baseline run
→ results, failures, anomalies
→ blogpost
→ formal specification
→ new environment families
→ Arena model generation and adversarial review
→ next generator version
```

This is an assistant's proposed workflow, not a theory hierarchy. Later user constraints say blog writing is stopped and the question about Arena Battle did not authorize calls, so this sequence must not be treated as current authorization.

### 9.2 Corpus-to-environment pipeline

**Source:** lines 840–859. The assistant suggests a pipeline from conversation/research corpus, through model-vs-model debate and candidate formalizations, to candidate environment families, adversarial criticism, minimal distinguishing environments, implementation, automated validation, and the generator's environment zoo.

**Status:** unexecuted assistant proposal. The user's question did not authorize Arena review or external model calls.

### 9.3 Measurement-to-abstraction proposal

**Source:** lines 5680–5690.

```text
observable behavior
→ measurement
→ formal abstraction
→ stronger intervention families
```

This is a model-proposed research-development principle, not a guarantee that the final item follows from the earlier items.

### 9.4 Reproducibility/identity sequence

**Source:** lines 5744–5755.

```text
canonical environment
→ stable semantic identity
→ reproducible trajectory
→ cross-run comparison
```

This is an engineering rationale for deterministic semantic IDs, not a theory of agent ability.

## 10. Standing interpretation rules

- Do not adopt the E0–E8 sequence as the user's framework.
- Do not turn the level-k example into a universal ladder from simple reasoning to epistemic manipulation.
- Do not reinstate `belief → attention → hypotheses → recursive control` as a single scale; the dialogue explicitly rejects that reading.
- Keep observations, source/access effects, attention, hypotheses, updating, opponent models, resistance, influence, recovery, and task outcomes separately defined.
- The user preserves a 15-question portfolio; no sequence in this file supersedes it.
- Distinguish observable behavior from hypothesized internal mechanisms throughout.
