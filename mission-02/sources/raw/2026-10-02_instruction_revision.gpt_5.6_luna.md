<!--
COMPILER PROVENANCE HEADER (not part of the response; the response starts at the line "You're right.")

Stored:            2026-10-02, by the compiler agent, from the user's paste into the chat.
Prompt answered:   not supplied by the user; not one of the four Mission 02 Council prompts (P01-P04). From the response's first line it answers a critique of the respondent's own earlier Arena-instruction draft. No sha256 recorded.
Sample:            single paste; no side-by-side companion was supplied.
Arena mode:        not stated.
Model as shown:    "gpt 5.6 luna" (the label the user put on the paste). The sources note for the 2026-09-29 round lists GPT-5.6 Luna among the models used there.
Session date/time: not supplied.
Tools in session:  not supplied.
Text integrity:    preserved exactly as pasted, including its nested code fences and the fenced instruction block. The user's label line is not part of the response and is dropped.
Order of events:   stored after the Mission 02 freeze (M02-FREEZE-1), the Mission 02 Council round (three of four roles in), the Mission 03 proposal and its decision record (M03-HD-1). The response refers to creating mission-02/seed.yaml, which already exists and is protected by tests/test_mission_02_freeze.py; it predates that state.
-->

You're right. I collapsed “the epistemic-games research direction is too broad to be a single mission” into “don't study epistemic games.” That was wrong.

The epistemic-games / strategic-reasoning cluster should probably be one of the **central research domains** of the programme. The point is not to replace it with generic “strategy” research. The point is to use it to generate **specific empirical questions** that can be turned into `rl_eval_generator` environments.

In fact, the architecture is more interesting this way:

```text
epistemic-games mindcluster
        ↓
research concepts / mechanisms
        ↓
candidate phenomenon
        ↓
formalization
        ↓
controlled environment family
        ↓
frontier-model evaluation
        ↓
new empirical result
        ↓
new rl_eval_generator capability
        ↓
expanded epistemic-games research
```

And this gives the mindcluster a job that is much stronger than “background context.”

For example, the existing graph contains things like higher-order belief, common knowledge, signalling, recursive opponent modelling, cognitive hierarchy, dynamic epistemic logic, deception, belief shaping, endogenous attention, epistemic drift, cognitive collusion, etc. Those are exactly the sorts of mechanisms from which you can derive benchmark families.

The research question could be something like:

> Do frontier models fuckingly exploit higher-order epistemic structure when it matters, or do they solve superficially similar tasks using shallower heuristics?

Or:

> At what level of recursive belief reasoning do frontier models fail, and can we construct environments that distinguish genuine level-k / recursive reasoning from pattern matching?

Or:

> Can agents manipulate another agent's epistemic state without changing the underlying facts, and can evaluators distinguish ordinary persuasion from belief-state manipulation?

Or:

> Does strategic reasoning degrade when the information environment itself is adversarial?

Those are very much **epistemic-games questions**, and `rl_eval_generator` is potentially an excellent laboratory for them.

The Strategy IR then becomes complementary rather than substitutive:

```text
EPISTEMIC-GAMES MEMORY
"What mechanisms are interesting?"

STRATEGY MEMORY
"What problem-solving transformations might apply?"

EPISTEMIC COMPILER
"Which mechanism + transformation can be turned into a controlled experiment?"

RL_EVAL_GENERATOR
"Can we build the damn experiment?"
```

That is the architecture I should have given you.

I would therefore revise the Arena instruction substantially. The agent should be told that **epistemic games is a priority research domain**, while still refusing to accept “study epistemic games” as a sufficiently specified mission.

Work on:

* `https://github.com/StrangeTcy/epistemic-compiler`
* `https://github.com/StrangeTcy/rl_eval_generator`

The goal is to advance a research programme at the intersection of:

1. epistemic games / strategic reasoning;
2. frontier-model evaluation;
3. reusable problem-solving strategies;
4. research infrastructure that evolves as the empirical programme advances.

IMPORTANT: epistemic games / strategic reasoning is a CORE RESEARCH DOMAIN, not background material to be discarded.

The imported Mindcluster in `knowledge/` is a cumulative research memory containing work on higher-order beliefs, common knowledge, signalling, recursive reasoning, cognitive hierarchy, dynamic epistemic logic, strategic information transmission, deception, belief shaping, attention manipulation, epistemic drift, cognitive collusion, opponent modelling, and related mechanisms.

We do NOT want a vague mission called “study epistemic games.”

We DO want to use this research memory to discover a precise, experimentally tractable epistemic phenomenon that can become a new `rl_eval_generator` benchmark family.

MISSION 01 IS FROZEN.

Do not modify its preregistration, approved spec, raw results, or claim set.

However, mine Mission 01 for reusable methodology and infrastructure where appropriate.

YOUR JOB

Design the next research mission around a concrete phenomenon from the epistemic-games / strategic-reasoning research direction.

The mission must satisfy all of the following:

* genuinely concerns epistemic or strategic reasoning;
* is not merely a generic prompting experiment;
* admits a precise falsifiable hypothesis;
* can be instantiated as executable environments in `rl_eval_generator`;
* has an independent oracle/evaluator;
* supports meaningful controls;
* can distinguish shallow heuristic success from the target epistemic mechanism as far as practical;
* would produce a reusable benchmark capability if the phenomenon is interesting;
* remains scientifically interesting even if the main hypothesis is falsified.

FIRST: SEARCH THE MINDCLUSTER

Use the actual contents of `knowledge/`, especially nodes, edges, sources, and the retriever.

Find several clusters where there is:

* a well-defined formal mechanism;
* an identifiable failure mode or open empirical question for AI systems;
* a natural game/environment construction;
* a possibility of constructing matched controls.

Examples of directions worth investigating include, but are not limited to:

* higher-order belief vs shallow inference;
* common knowledge vs merely shared information;
* level-k / recursive reasoning depth;
* signalling and strategic information transmission;
* deception and belief manipulation;
* epistemic effects of truthful-but-selectively-presented information;
* opponent modelling;
* dynamic belief updates under public/private observations;
* endogenous attention;
* epistemic drift under adversarial information environments;
* cognitive collusion between agents.

Do not assume these examples are the best choices. Use the Mindcluster to discover stronger ones.

SECOND: GENERATE CANDIDATE PHENOMENA

For each promising cluster, formulate a concrete phenomenon in the form:

mechanism
→ minimal environment
→ target capability
→ predicted failure
→ discriminating manipulation
→ measurable outcome

Reject anything that remains merely philosophical.

A good candidate should admit tiny environments in which changing one epistemic variable changes the correct action.

THIRD: SELECT ONE MISSION

Choose ONE candidate, using explicit criteria:

* scientific novelty / interestingness;
* experimental tractability;
* evaluator reliability;
* ability to separate competing explanations;
* benchmark reusability;
* connection to existing `rl_eval_generator` infrastructure;
* value of null results.

Do not give me a generic roadmap. Pick one.

FOURTH: DESIGN THE BENCHMARK

Design a minimal environment family.

The benchmark should ideally contain controlled variants in which the underlying world can remain nearly identical while epistemic structure changes.

For example, depending on the chosen phenomenon:

* same physical state, different knowledge state;
* same facts, different common-knowledge structure;
* same objective, different information partition;
* same interaction, different recursive belief depth;
* same evidence, different strategic presentation.

Be extremely careful not to confuse “different prompt wording” with “different epistemic state.”

Define the latent variables formally enough that the evaluator can know the ground truth.

FIFTH: DESIGN THE CONTROLS

Explicitly separate:

* direct factual competence;
* ordinary planning;
* generic reasoning;
* the target epistemic mechanism.

Use matched control environments whenever possible.

A particularly valuable design is one where a shallow heuristic succeeds on ordinary cases but fails on a controlled epistemic manipulation.

SIXTH: DESIGN THE ORACLE

The oracle must evaluate the actual game-theoretic / epistemic ground truth, not whether the model's explanation sounds sophisticated.

Prefer state-transition or payoff-based verification.

Where explanations are requested, treat them as secondary evidence.

SEVENTH: CONNECT TO STRATEGY IR

Treat the Strategy IR as a SECONDARY research object.

Ask whether the target epistemic problem also exposes reusable problem-solving transformations such as:

* representation change;
* meta-level reasoning;
* counterexample construction;
* invariant discovery;
* decomposition;
* adversarial perspective-taking;
* game modelling.

Do not force this connection if it is not real.

If a strategy appears relevant, specify the trigger and transformation explicitly.

EIGHTH: EVOLVE RL_EVAL_GENERATOR

The mission should leave behind something reusable.

Specify exactly what would be added to `rl_eval_generator`:

* environment family;
* configuration schema;
* oracle;
* adversarial variants;
* held-out variants;
* metrics;
* documentation;
* tests.

The permanent benchmark should encode the scientific phenomenon, not merely the prompt used in this experiment.

NINTH: TRY TO KILL IT

Attack the proposal.

In particular ask whether apparent success could be explained by:

* memorized textual patterns;
* surface cues;
* additional context;
* longer inference;
* general planning ability;
* reward hacking;
* evaluator artifacts;
* accidental asymmetries;
* one particular model family;
* one particular game construction.

Construct explicit falsification variants wherever possible.

TENTH: CREATE THE RESEARCH ARTIFACT

Create:

`mission-02/seed.yaml`

plus the minimum supporting files needed by the existing protocol.

Also create:

`mission-02/design.md`

containing:

* research question;
* mechanistic hypothesis;
* formal environment definition;
* treatment/control conditions;
* sampling;
* primary and secondary metrics;
* oracle specification;
* confounds;
* falsification experiments;
* claim ceiling;
* expected `rl_eval_generator` additions.

Also create:

`mission-01/harvest.md`

containing only durable, evidence-backed methodological or benchmark objects that should be carried forward from Mission 01. Do not rewrite its scientific conclusions.

Do not implement a general strategy engine.
Do not build an agent swarm runtime.
Do not modify frozen Mission 01 artifacts.
Do not create a giant theoretical framework before identifying the minimal executable phenomenon.

The objective is:

EPISTEMIC-GAMES THEORY
↓
specific mechanism
↓
minimal executable game
↓
controlled frontier-model experiment
↓
scientific result
↓
new reusable evaluation capability
↓
better epistemic-games research

The result should make both sides stronger: a real contribution to the epistemic-games / strategic-reasoning research programme AND a concrete evolution of `rl_eval_generator`.

Prefer one sharp phenomenon over a broad survey.

And I'd go one step further: **the mindcluster should eventually become a generator of candidate benchmark mechanisms.** That's the really attractive loop.

Your graph contains centuries of ideas about knowledge, belief, information, signalling, recursive reasoning and strategic manipulation. The exciting possibility is to systematically ask:

> “What is the smallest executable game that isolates this concept, and what do frontier models fuckingly do on it?”

Then every interesting answer expands `rl_eval_generator`, and every new benchmark result feeds back into the epistemic-games research.

That is a much better reason for the mindcluster to exist than merely stuffing it into a council context window.
