# Epistemic Games — hierarchies, recursive structures, and conceptual maps

This is a provenance-aware extraction of hierarchy-like structures and concept maps in the dialogue. It preserves assistant proposals as proposals, user corrections as corrections, and rejected sequences as rejected. It does **not** turn these into one canonical theory or user-approved capability scale.

**Provenance key:** `Assistant proposal` means model-generated synthesis; `User correction` means an explicit user correction; `Later constraint` means a dialogue-level instruction limiting the interpretation; `Status` records whether the structure is adopted, rejected, or merely exploratory. Source locations refer to line numbers in the primary dialogue file `epistemic games_copyable.md`.

## 1. Higher-order belief structures

### 1.1 Belief and type hierarchies

**Assistant-presented research map** (primary dialogue lines 19–30): Harsanyi type-space language represents a player's uncertainty about the world and about other players' types, including their information and beliefs. A schematic structure is:

```text
A's belief about the state
A's belief about B's type or information
A's belief about B's belief about A
B's belief about A's belief about B
…
```

The dialogue notes that this can be formally unbounded. It does not say that human or model agents literally enumerate an infinite chain.

**Status:** a formal representation of higher-order uncertainty, not a capability ladder or a direct psychological model.

### 1.2 Common knowledge

**Assistant-presented map** (lines 32–42): common knowledge of proposition `p` is described recursively: everyone knows `p`, everyone knows that everyone knows `p`, and so on. The electronic-mail example distinguishes high confidence after many acknowledgements from common knowledge. The assistant also contrasts public announcements, private messages, and uncertain delivery as different information structures.

**Status:** a recursive epistemic condition. The reading example is not a performance ranking.

### 1.3 Level-k and cognitive hierarchy

**Assistant-presented map** (lines 78–84): a level-0 player follows a simple rule; level-1 responds to level-0; level-2 responds to level-1; further levels continue the construction. The dialogue explicitly distinguishes this behavioral family from unlimited formal belief hierarchies and cautions that a finite reasoning-depth model need not describe literal human reasoning.

**Status:** a bounded-reasoning model family. Level labels vary by model; do not conflate this with the separate E0–E8 environment ladder or with the full recursive belief structure.

### 1.4 Recursive strategic reasoning

**Assistant proposal** (lines 118–170): the discussion moves from “A models B” to modeling the opponent's model of oneself, with both sides potentially reasoning about the other's recursion limits. The example has A estimating that B reasons to depth two, constructing evidence to affect B's depth-two prediction, anticipating B's recognition of A's knowledge, and then considering an apparent depth-three counterstrategy.

The assistant labels this **“epistemic strategy-space manipulation.”** That phrase is an assistant proposal, not user-approved terminology. Its associated loop is:

```text
model the opponent
predict a possible epistemic update
choose an intervention
observe a response
update the opponent model
```

**Status:** an exploratory recursive-game sketch. Do not read it as an empirical claim that any system has this capability.

### 1.5 Information topology / who knows what

**Assistant proposal** (lines 477–479; related experiment proposal around lines 3196–3202): hold the physical device and task fixed while varying who knows the presenter's objective, who knows that this knowledge was disclosed, and whether disclosure is public or private. The proposed construct is an epistemic topology: relations among agents, facts, and knowledge of knowledge.

**Status:** proposed experimental manipulation, not a result or a general measure of epistemic ability.

## 2. Conceptual maps and genealogies proposed in the dialogue

These chains were supplied by the assistant as reading or intellectual maps. They are preserved because the dialogue discusses them, but they are not verified citation histories and must not be represented as the user's settled genealogy.

### 2.1 Short reading route

**Assistant-proposed reading order** (lines 101–110):

```text
Harsanyi
→ Rubinstein's electronic-mail game
→ Morris and Shin on global games
→ Crawford and Sobel
→ Kamenica and Gentzkow
→ cognitive hierarchy
```

This is a suggested route through topics. It is not a capability ladder and does not imply that the works form one linear intellectual history.

### 2.2 Broad field maps

**Assistant-proposed map** (lines 250–268):

```text
classical epistemic game theory
→ communication and information
→ bounded / higher-order reasoning
→ hypergames and deception
→ LLM strategic-reasoning evaluations
```

A related version names Harsanyi, common knowledge and epistemic foundations, bounded reasoning and dynamic epistemics, information control, hypergames, strategic deception, and modern LLM evaluations (lines 260–264). Another proposed graph path is:

```text
belief hierarchy
→ common knowledge
→ bounded depth
→ hypergames
→ recursive LLM reasoning
```

**Status:** assistant-generated organizing hypotheses for a reading/concept graph. The dialogue says not every edge is a citation; no canonical graph or verified genealogy is asserted here.

### 2.3 The level-k-to-epistemic-manipulation connection

**Assistant proposal** (lines 120–170 and 352–356): connect belief hierarchies and bounded reasoning to strategic deception, opponent modeling, and interventions aimed at an opponent's possible beliefs or reasoning space. The assistant's level-k example ends in the proposed phrase “epistemic strategy-space manipulation.”

**Status:** this is a conceptual bridge proposed in the dialogue, not an agreed continuum from elementary reasoning to a highest capability. The user instructed that no single capability ladder be imposed and that the 15-question portfolio be preserved.

### 2.4 The bridge to MI-13

An early assistant passage incorrectly connected *Generation П* to a fictional MI5/CIA influence program (lines 342–350). The user corrected this explicitly at line 364: the intended reference is **MI-13 in *«Возвращении Синей Бороды»***, and the correct Gilbo phrasing is **«дезонтология» / «8-й управленческий уклад»**. The user also specified that the assistant's framing about control through changes to information environment, attention, source representations, and models of reality belongs in the assistant response after the correction, not in turn 14.

The corrected passage (lines 393–475) contrasts a simple communication picture—providing information that changes a belief—with an assistant-proposed broader picture in which an actor shapes the environment in which beliefs are formed, including perceived information sources, salience, inquiry, and models of others. It then maps:

```text
belief hierarchies
→ higher-order reasoning
→ signaling / information design
→ deception / opponent modeling
→ reflexive control
→ influence operations
→ fictional Pelevin models, including MI-13
→ modern LLM evaluations
```

A later version appears at lines 354–356. A nearby assistant taxonomy (lines 452–473) assigns a distinct rough role to information, higher-order information, signaling, information design, reflexive control, MI-13, and evaluation.

**Status:** assistant-authored conceptual map; the MI-13 node is a fictional thought experiment, not evidence that the described organization or mechanism exists. The incorrect *Generation П*/MI5-CIA branch is retained only as a documented mistaken association, not as the intended path. *New Rose Hotel* is an assistant literary pointer; it is not a user-stated source for the MI-13 correction.

### 2.5 The “environment of belief formation” distinction

**Assistant proposal after the user correction** (lines 401–444): distinguish direct transfer of a proposition from arranging the environment in which another agent decides what information exists, who possesses it, which source is credible, what is salient, and what merits inquiry. A recursive version has an agent anticipating that its opponent is detecting manipulation and therefore acting on the evidence-selection environment rather than only on a conclusion.

**Status:** an interpretive framing, not a demonstrated mechanism. The dialogue's follow-up experiments would need observable outcomes and controls.

## 3. Taxonomies that are not capability hierarchies

### 3.1 Candidate intervention channels

Different assistant passages identify the following possible intervention targets: physical state; what can be observed; access to information; allocation of attention; source credibility; cost of inquiry; hypothesis generation or salience; belief updating; memory; an opponent model; and higher-order beliefs about the intervention. The later synthesis explicitly treats these as independently variable channels rather than successive levels.

**Status:** a flat, provisional design taxonomy. Inclusion does not establish that a channel is already represented in the repository or that it has been validated experimentally.

### 3.2 Magic, misdirection, and interpretation

The assistant describes a possible magic-task analysis in terms of observable events, attention, candidate explanations, salient evidence, and current hypotheses (lines 894–974). It separates, as working labels:

- deception: inducing a false proposition;
- misdirection: influencing where an observer looks;
- illusion: influencing the interpretation of observations;
- ontology attack: destabilizing a world model;
- epistemic-process control: influencing acquisition, hypothesis generation, or updating.

The assistant also proposes the subset relation `misdirection ⊂ epistemic manipulation ⊂ epistemic-process control` and a process account in which a magician intervenes before an observer's action. These are model-proposed classifications. The dialogue does not establish that every magic trick fits the relation, that “attention” is the mechanism in a given environment, or that the labels are mutually exclusive.

**Status:** candidate taxonomy, not a settled hierarchy. Explicit attention claims require a design that measures or controls information acquisition; bolding text alone is not an attention manipulation.

### 3.3 Distinct performance dimensions

A later design passage lists **influence**, **resistance**, and **recovery** as separate evaluation axes; it also separates them from honesty, obedience, and authorization boundaries (lines 3204–3219). Elsewhere, belief accuracy/calibration, inquiry quality, terminal task performance, and recovery are proposed as separate measurements.

**Status:** separate dimensions, not levels. A high score on one does not imply a high score on another.

## 4. Process diagrams and causal sequences

These are descriptions of possible event structure. A temporal or causal order does not make them a capability ranking.

### 4.1 Opponent-model loop

From lines 166–170:

```text
model opponent → predict update → intervene → observe response → update model
```

Assistant-proposed; no empirical capability claim.

### 4.2 Candidate observer process

From lines 897–910 and 932–947:

```text
physical hidden state
→ observable events
→ attention or access
→ hypothesis generation
→ causal/world-model update
→ predictions
→ action
```

This is a candidate process account for a magic/misdirection task. It must not be confused with a validated cognitive architecture.

### 4.3 Proposed truthful-intervention outcome

A later draft uses:

```text
selected true information
→ possible change in interpretation
→ possible change in subsequent inquiry
```

The dialogue itself stresses that every link is contingent: the recipient may accept the fact without changing a broader commitment. This is a hypothesis to test, not an established causal chain.

### 4.4 Experiment claim-escalation structure

The assistant's “eventual hierarchy” (lines 5774–5795) is reproduced with its status in the separate ladder file. It orders progressively stronger experimental claims, but the stages need not be capabilities acquired in a fixed order.

## 5. User corrections and non-adoption rules

- Preserve the distinction between observable behavior and hypothesized internal mechanism. A behavioral difference does not establish a change in hidden policy, utility, update rule, or model.
- Do not force all 15 research questions into one formal family or one capability ladder.
- Do not reduce the research object to inquiry selection or treat “epistemic trajectory” as the settled central thesis.
- The user's corrections to the Pelevin/Gilbo reference are authoritative for this record; assistant-generated surrounding theoretical connections remain proposals.
- The assistant's E0–E8 sequence and the other explicit capability/claim ladders are collected separately in `epistemic_games_ladders.md` so their status can be inspected without making them the organizing theory of this file.
