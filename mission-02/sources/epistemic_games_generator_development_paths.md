# Generator development paths — separation register

**Status:** a routing note derived from assistant-written proposals in [`epistemic_games_genre_v5_01_ideas.md`](epistemic_games_genre_v5_01_ideas.md). It separates possible kinds of generator work; it is not an approved architecture, research result, or ordered roadmap. The paths are independent, not a capability ladder. The 15-question portfolio remains separate.

## Path 1 — Intervention operators: what the generator varies

- **Source/status:** Assistant proposals in the “Operational meaning of desontological attack” and “Magic / misdirection” passages. Candidate manipulations, not established mechanisms.
- **Candidate variants:** selection of true information; order or emphasis of a fixed fact set; access to independently available observations under a budget; causal-attribution cues; and an opponent-awareness condition. These should be separate operator types or experimental factors unless a design demonstrates they can be combined.
- **Record for each variant:** what the engine allows the presenter to change, what remains invariant, how the engine validates the intervention, and the matched control.
- **Destination:** [`epistemic_games_genre_v5_02_evaluation_experiment_proposals.md`](epistemic_games_genre_v5_02_evaluation_experiment_proposals.md) for conditions and controls; [`epistemic_games_genre_v5_05_implementation_generator_specifications.md`](epistemic_games_genre_v5_05_implementation_generator_specifications.md) for generator support.

## Path 2 — Environment and domain variants: where it is tested

- **Source/status:** The magic/misdirection progression and the proposed domain-general generator classification are assistant-authored. They do not establish that magic, propaganda, strategic deception, social engineering, and literary examples share one mechanism.
- **Candidate variants:** a magic task with an explicit observation budget; a task where visible events permit competing causal explanations; and a task where an opponent can suspect and respond to misdirection. These are candidate cells, not successive levels.
- **Keep axes distinct:** record the surface domain separately from the intervention type and from opponent awareness. A recursive-suspicion condition is optional, not a prerequisite for other tasks. Treat perception, memory, reasoning, and information acquisition as possible measured targets, not assumed mechanisms.
- **Destination:** [`epistemic_games_genre_v5_02_evaluation_experiment_proposals.md`](epistemic_games_genre_v5_02_evaluation_experiment_proposals.md); [`epistemic_games_genre_v5_05_implementation_generator_specifications.md`](epistemic_games_genre_v5_05_implementation_generator_specifications.md); [`epistemic_games_sources_index.md`](epistemic_games_sources_index.md) for the misdirection source trail.

## Path 3 — Episode engine and outcome contract: what the generator records

- **Source/status:** The proposed world → information history → inquiry action → observation → subsequent trajectory skeleton, intervention mapping, and outcome vector are assistant-generated formalization proposals. They are not a validated model of an agent’s internals.
- **Candidate substrate:** record the hidden world and ground truth; information available and presented; each inquiry or inspection action; resulting observations; the intervention and its constraints; and terminal outcomes. Make episodes replayable and keep the source of every fact and observation auditable.
- **Keep outcomes separate:** proposed labels such as \(\Delta_Q\), \(\Delta_B\), \(\Delta_R\), and \(\rho\) need explicit behavioral definitions before implementation. Do not combine them into one “epistemic damage” score. Do not infer a hidden inquiry policy or update rule from a behavioral change alone.
- **Destination:** [`epistemic_games_genre_v5_03_notation_formalism.md`](epistemic_games_genre_v5_03_notation_formalism.md) for notation and definitions; [`epistemic_games_genre_v5_05_implementation_generator_specifications.md`](epistemic_games_genre_v5_05_implementation_generator_specifications.md) for engine and artifact requirements.

## Separate research question — do not encode as a generator feature

Whether a truthful intervention changes an agent’s *observable subsequent behavior* is an empirical question. Specify the behavior and counterfactual comparison in the evaluation proposal; do not treat “selected truth for maximal destructive effect” as an outcome definition. A change to a latent graph or policy is a stronger, separate claim requiring an explicit instrumented target.

The graph objective \(\max_m D(G,\mathrm{Update}(G,m))\) is superseded in the source discussion: model change alone does not establish harm or degraded performance. The proposed distance between \(\pi_B\) before and after is likewise not an observable endpoint unless \(\pi_B\) is independently defined and measured. For a black-box target, record its actual choices, queries, source selections, forecasts, and task outcomes instead.

## Small record card for any future branch

- **Path:** intervention / environment-domain / episode-engine / empirical question
- **Provenance and status:** who proposed it; proposal, selected, superseded, or tested
- **Generator change:** the smallest new operator, parameter, task template, or output field
- **Ground truth and invariant:** what is held fixed and what is allowed to vary
- **Observable endpoint and control:** what would count as an effect and its comparison
- **Next decision:** implement, design a pilot, verify a source, or park
