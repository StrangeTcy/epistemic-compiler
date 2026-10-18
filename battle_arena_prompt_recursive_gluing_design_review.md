# Battle Arena prompt: adversarial design review of recursive gluing environments

Use the attached `recursive_gluing_research_brief_2026-10-18.md` as the statement of research intent. Inspect the actual repository code before proposing solutions:

- Repository: https://github.com/StrangeTcy/rl_eval_generator
- Branch: `arena/1ddc930c-rl-eval-generator`
- Recent four-app correction: `0dcb51cbfa35598fa843905c3384d93a5fc95a71`
- Main starting point: `envs/cat_theo/recursive_maze_gluing/`
- Compact recursive comparison: `envs/cat_theo/recursive_gluing_discovery/`
- Expanded constraint control: `envs/cat_theo/recursive_gluing/`
- Candidate sibling tasks to critique, not assume are replications: `recursive_holonomy_gluing`, `recursive_compiler_bootstrap`, `recursive_error_correcting_codes`, `recursive_coarse_graining`.

## Mission

Conduct a skeptical, technically grounded research-design review. The goal is to build a deliberately nasty self-similar task in which a model must recover an inferable but non-obvious generating mechanism and discover why naive local gluing fails globally. Do not drift into a generic suite of four compositional puzzles or assume that the common use of recursion makes several tasks replications of one construct.

The motivating shape is the recursive maze: locally feasible routes and tiles can look innocent, but state changes across recursive nesting (for example, orientation transforms, child entry/return, exit sealing, and edge-use constraints) mean that local solvability does not imply a globally valid route. The right compositional summary must preserve the information the parent needs; a Boolean “child is solvable” is inadequate when it discards relevant boundary behaviour.

The prompt shown to the evaluated model must not name the underlying mathematical theory or reveal the intended abstraction / algorithm. Merely replacing terms like “sheaf” and “global section” with synonyms is not enough. However, the task must remain identifiable: the mechanism must be recoverable from actual public evidence available to the agent, not depend on guessing evaluator internals or an unstated rule.

## Work in adversarial rounds

### Round 1 — independent reconstructions

Each reviewer should first state, in their own words, the intended construct and what would count as evidence for it. Separate at least:

1. solving an explicitly specified finite problem;
2. generalizing a compact compositional algorithm across depths and instances;
3. recovering a latent generating mechanism from examples / interactions / traces;
4. transferring the principle to a different representation or domain;
5. making claims about internal model concepts (which task accuracy alone cannot establish).

Explicitly identify any ambiguity in whether the task should infer a hidden generator, infer an algorithm for a specified recursive object, or test both in separate phases. Recommend a clean operationalization rather than silently merging these.

### Round 2 — red-team the current repository

Inspect generator, agent-facing prompt, judge/oracle, grade cases, tests and configuration. Cite exact file paths and relevant functions in every material claim.

In particular, assess:

- `recursive_maze_gluing`: what is genuinely recursive and consequential today? What does the agent prompt already tell it about the mechanism? What can a generic BFS/DFS or simple parity shortcut solve? Do the configured depths 1–3 actually force composition, or merely permit it? Does the current grade suite separate local feasibility from global obstruction in a way that tests the target claim?
- `recursive_gluing_discovery`: it has depth up to 12 and a compact grammar, but explicitly gives the recurrence semantics and requires a realizable-boundary-pair certificate. What does it test, and what does it not test? Could it serve as a positive control or as one phase in a stronger task?
- `recursive_gluing`: does its expanded CSP version offer a valid control for any specific claim?
- The four sibling applications: are there meaningful construct-level reasons to use them, or would treating them as replications be unjustified? Do not recommend keeping them merely because they exist.

Test the strongest plausible null explanations, including small-instance enumeration, explicit BFS/DFS, local-only gluing, ignoring orientation/state, fixed route templates, shallow-depth memorization, answer-polarity heuristics, label leakage, and seed/generator leakage. Distinguish shortcuts that are valid general algorithms from shortcuts that only exploit the present test distribution.

### Round 3 — propose a stronger design

Propose the smallest coherent revised experiment, not the largest list of new environments. It should specify:

- the central falsifiable hypothesis;
- exactly what the agent sees and can query, and what remains hidden;
- how examples / tool interactions / generated instances make the mechanism inferable;
- the state/interface information that must be preserved across recursion, and why a naive local summary fails;
- paired instances with matched local components but different global outcome, where feasible;
- transformations that preserve task identity (opaque relabelling, rule-preserving changes) separately from interventions that alter the actual global constraint;
- meaningful depth scaling with no silent caps or saturated difficulty settings;
- held-out seeds and, preferably, held-out production patterns rather than only replays of one template;
- reference, shortcut and complexity baselines;
- output certificates that are checked independently;
- metrics: route / certificate validity, SAT and UNSAT errors separately, per-depth generalization, resource/interaction cost, and uncertainty;
- explicit go/no-go criteria for model calls.

A particularly useful candidate invariant to examine is the set/relation of boundary behaviours each recursive component can realize, indexed by remaining depth and any genuinely necessary finite state. But do not prescribe it as correct without checking it against the maze's route semantics. Prove or test that the proposed summary is sufficient and complete. If there is an even better summary, defend it.

Crucial: don't conflate “mechanism not named” with “mechanism hidden.” Don't claim the model has discovered a sheaf-theoretic concept because it succeeds on a task whose observable behaviour is compatible with that interpretation. State the strongest operational claim the evidence would support, and its limits.

### Round 4 — criticism and convergence

Each reviewer should attack the strongest proposal from another reviewer. Require concrete counterexamples: ways an apparently successful design could still be passed by brute force, leakage, a simple heuristic, or a memorized general solver. Then produce a synthesis that records:

- points of agreement;
- substantive disagreements that remain;
- recommended primary design and rejected alternatives;
- priority-ordered code changes;
- the tests / adversarial instances required for each change;
- what should be deferred;
- why the first model pilot would be informative if the go/no-go gate passes.

Do not settle on vague recommendations such as “increase difficulty,” “hide the concepts,” or “add more tests.” Every recommendation must name the code or contract to change, the intended effect, a test that could refute the claim, and an observed result that would count as success or failure.

## Guardrails

- No Astra or other model API calls in this review.
- Do not treat `174 passed, 0 skipped` in the sibling-task audit as evidence of model capability or construct validity.
- Do not call direct-vs-recursive an isolated recursion contrast when other dimensions change.
- Do not turn the four sibling tasks into cross-domain replications without an explicit shared hypothesis and evidence.
- Do not remove useful mechanics merely to make the prompt cryptic; preserve enough observable information for the intended inference to be possible.
- Do not edit unrelated maze / distributed / epistemic / v0 / discovery environments without explaining the causal link to the primary design. The discovery environment may be discussed as a candidate architecture, but changes to it must be justified against the maze-centered objective.
- Prefer one coherent task with strong controls and an explicit validation argument over a broad suite with ambiguous meaning.
- You may run local generator / oracle scripts and tests to inspect the present design, but no model scoring or paid endpoint use. Keep every empirical statement traceable to a reproducible command, test, or inspected code.

## Required final deliverable

Produce a design-review report with:

1. a concise reconstruction of the target capability;
2. the strongest criticisms of the current environment(s);
3. an experiment matrix separating factors, controls and confounds;
4. the minimal redesign recommendation and concrete code-level changes;
5. adversarial regression tests and baselines;
6. a pre-model go/no-go checklist;
7. a short section titled **“What a successful pilot would not prove.”**

If implementing a code patch is part of the Arena session, first agree on the design and scope. Make a small, reviewable patch with tests and a diff; don't quietly replace the research question with a generic solver benchmark. The user will decide when to run the improved environment against Astra.
