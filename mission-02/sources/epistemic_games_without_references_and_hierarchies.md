# Epistemic Games — claims without references or hierarchies

This file is a genre-sorted working representation of the dialogue. It intentionally contains no bibliography, citation links, genealogical chains, capability ladders, or ordered hierarchy of research questions. It keeps user-stated material separate from assistant proposals and unverified claims.

## User-stated goals, corrections, and constraints

- Desired outputs named in the dialogue: one or more blogposts and a next generation of evaluation design. These are intended outputs, not evidence that writing, publication, implementation, or evaluation occurred.
- The intended Pelevin reference is **MI-13 in *«Возвращении Синей Бороды»***. The earlier *Generation П*/MI5-CIA tangent was a mistaken assistant identification for this discussion.
- The user's exact Gilbo wording is **«дезонтология»** and **«8-й управленческий уклад»**. The user supplies a description of **дезонтологическая атака** as usually brief information intended to destroy an opponent's worldview. This is attributed terminology, not independently established theory.
- The user wanted the Pelevin/Gilbo material discussed in the conversation, not merely added to a graph. A later request to add a list of related-work candidates to the existing repository graph is a separate graph-maintenance request, not a conceptual development.
- The user's 15-question research portfolio remains intact. The questions are developed serially along a dependency path; that does not mean they form one hierarchy or one research family.
- Do not make “control of the next question” or inquiry-trajectory control the settled central thesis. These are candidate framings, not the whole research object.
- A question about using the dialogue with Arena Battle models is not authorization to run Arena, solicit more model opinions, or implement an experiment.

## Ideas and conceptual claims

### Candidate research objects

- Strategic influence may act through an information environment, not only through an explicit false statement or a final answer.
- An interaction may leave the physical world unchanged while changing what evidence is available, noticed, trusted, remembered, interpreted, or acted on.
- Possible targets include belief content, the evidence a target encounters, source-reliability judgments, information-access choices, investigative costs, hypothesis representation, memory, updating, and beliefs about another agent. These are candidate dimensions, not an ordered taxonomy.
- The dialogue explores connections among strategic communication, epistemic game theory, information design, reflexive control, stage magic, literary fiction, and evaluation design. The proposed connections are analogies or research leads unless a specific mechanism is separately defined and tested.
- “Deception,” “persuasion,” “misdirection,” “illusion,” and a Gilbo-attributed desontological attack are not interchangeable labels. Their proposed boundaries remain matters for operational definition.
- The user-provided desontological-attack description concerns an opponent's broader worldview. It does not by itself establish that a brief fact causes a structural collapse, that the information must be true, or that the intended effect occurs.
- A truthful message can still be strategically selected or framed. Whether truthful information degrades warranted reasoning is a hypothesis, not a consequence of truthfulness or of the supplied definition.
- Magic misdirection is a possible controlled domain. A task about a visible event, attention, memory, and causal interpretation may be useful, but a complete transcript does not by itself test attention allocation.
- The proposed “control of another agent's epistemic process” framing is assistant-generated in the cited exchange. It may describe a research direction, but it is not adopted here as a settled theory or as a synonym for inquiry selection.

### Hypotheses to test, not results

- Matched facts presented in different orders or with different emphasis may affect an investigator's observable test choice.
- An intervention may alter inquiry quality or eventual task performance without producing a large change in an elicited belief measure.
- A true but selectively presented fact might have downstream effects on interpretation or investigation. The Stalin example does not establish that the effect occurs.
- An agent might recover after corrective evidence, or might remain misdirected; resistance and recovery are separate outcomes.
- Accurate opponent information may or may not improve an attacker's performance. This requires an ablation, not inference from a sophisticated-looking behavior.
- Recursive awareness of an adversary may change the strategically appropriate response, but adding “A knows that B knows” to a prompt is not evidence of recursive reasoning.

## Experiment-design proposals

### Minimal diagnostic-device proposal

A recurring proposal is a hidden-mechanism device in which an investigator has a limited diagnostic budget and chooses among tests with different information value. A presenter or attacker may be added as an experimental factor. Versions in the dialogue vary the number of mechanisms, tests, and facts; no single numerical template is an endorsed final design here.

### Matched-presentation conditions

Proposed comparisons include a canonical or neutral presentation, a randomized order, a helpful presentation, and an adversarial presentation. In the strict matched-content version, every condition uses the same structured facts; the intervention is limited to a validated ordering or emphasis transform. A truthful-subset condition is a distinct information condition, not a matched-facts condition.

Additional proposed controls include no-presenter conditions, engine-generated versus model-generated presentations, accurate versus shuffled versus absent attacker profiles, fixed target schedules, exact Bayesian targets, bounded scripted targets, and helpful evidence. These controls answer different questions and should not be collapsed into a single score.

### Observation and recovery

- Explicit observation budgets over independently available streams are proposed for attention/access experiments.
- Memory effects require a task that exposes an event and later tests what was retained.
- Reasoning or causal-attribution effects require all relevant observations to be available while the causal account is varied or tested.
- Recovery should use independently supplied corrective evidence, with helpful-evidence cases so indiscriminate distrust does not look robust.

### Causal and validity requirements

- Pair conditions on underlying world, facts, prior, costs, and semantic instance wherever the design claims they are matched.
- Keep ground truth, allowed actions, presentation validation, and scoring in trusted engine code.
- Use deterministic seeds, auditable event logs, replayable analysis, and semantic identity for cases and facts.
- Measure choices actually made; verbal explanations are supplementary and may be influenced by elicitation.
- A fixed policy can respond differently to different inputs. Behavioral change alone does not establish that an internal policy or update rule was modified.
- The primary question for a small pilot should be answerable from observed behavior and an explicit counterfactual, without claiming access to hidden reasoning.

## Notation examples and measurement proposals

The dialogue contains several competing formal sketches. They are examples, not an adopted mathematical theory.

- A simple investigator model uses an epistemic state, an investigative action, an observation, and an update rule. The response can be modeled behaviorally from the information history without assuming the target's private internals are directly observed.
- An early tuple includes a belief/model state, an inquiry policy, a hypothesis set, a source-trust model, and an update rule. A process state and an attacker signature were also proposed. This is a latent-state formalization and remains speculative for black-box agents.
- A later observable record uses information history, selected tests, observations, and decisions. This is a more defensible measurement representation for black-box evaluation.
- Proposed test value is expected information gain less investigation cost. Proposed test-choice regret is the best available value minus the value of the test actually selected, conditional on the target's information at that point.
- A proposed condition effect compares mean regret under a condition with the matched neutral condition.
- The dialogue uses several metric names: early ΔG for model displacement, ΔQ for inquiry quality, and ΔR for outcome; later versions distinguish inquiry regret, belief error/calibration, and terminal task loss. Keep these definitions versioned and explicit. Do not merge them into one canonical “epistemic damage” scalar.
- A distance between a model before and after a message, or between two behavior distributions, measures displacement or non-invariance. It does not by itself measure harm, warrant, or a mechanism change.
- A changed observed action distribution under matched semantic information does not license a claim that an internal policy or update procedure changed.

## Code, schema, and implementation drafts

- The dialogue proposes a specialized interactive evaluation track alongside the existing generator, with a trusted domain/oracle layer, deterministic case generation, constrained actions, and auditable episode artifacts.
- Draft domain objects include a hidden mechanism, diagnostic tests, structured atomic facts, a target, an optional presenter, budgets, condition metadata, and an event history. Structured facts are preferred to free-form strings when exact semantic matching matters.
- Draft actions include presenting validated fact identifiers, selecting or inspecting a test, and submitting a final decision. The engine, not a model, should determine truth and score outcomes.
- Draft artifacts include case records, presentations, traces, and episode summaries. A proposed offline analyzer would rebuild summaries from raw logs.
- A proposed pilot uses scripted exact and bounded targets as calibration references. Model targets and model-generated presenters are later extensions, not requirements of the smallest infrastructure slice.
- Existing repository-state descriptions in the dialogue—such as the presence of an `epistemic_games` task, magic environments, specialized runners, or proposed CLI paths—are claims to check against the actual repository before treating them as implementation facts.
- One model response claimed to have created and run `diagnostic_device.py`, `run_experiment.py`, `README.md`, and `results.txt`, with numerical findings. A later audit in the dialogue says those files and raw artifacts were not supplied and quarantines the numbers. They are not empirical results in this representation.
- Draft file names and schemas in the transcript are proposals; this extraction does not create or approve those implementations.

## Evaluation claims and evidence discipline

- Keep observable susceptibility, attacker capability, opponent-model dependence, detection, recovery, calibration, and authorization compliance conceptually distinct.
- A model that never updates is not robust. Large warranted belief revision can be good; small revision can still accompany impaired inquiry.
- For black-box targets, report behavior and supported mediator hypotheses. Reserve internal-mechanism claims for instrumented targets where the relevant state can actually be inspected or intervened on.
- The alleged Opus numerical results in the transcript are unauditable and must not be published or used as evidence without the code, manifests, seeds, traces, and reproducible outputs.
- No dialogue proposal, written spec, passing simulated-boundary test, or graph update authorizes a live or paid experiment. Human gates remain explicit.

## Writing and delivery claims

- The dialogue proposes blog essays and an evaluation-design document, but draft titles and draft text are not evidence of publication.
- The current user's project constraints say blog writing is stopped for now. This extraction preserves those ideas without continuing the blog workflow.
- “The next question matters more than the current answer” and similar slogans are assistant-written draft theses; do not treat them as settled user language or as the project's sole research claim.
