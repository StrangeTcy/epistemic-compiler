# Research brief: Nasty self-similarity and recursive gluing failures

**Date:** 2026-10-18  
**Status:** Working research intent for adversarial review. Not a validated benchmark specification.

## 1. The point of the project

The target is a deliberately nasty, self-similar reasoning environment in which an agent must recover and use a non-trivial generating mechanism. The visible pieces should make local solutions look plausible, while their recursive composition can make a global objective impossible. Naively solving each local piece and “gluing” the answers together should fail for a principled reason, not because of a typo, arbitrary hidden rule, or missing information.

The desired capability is not merely to implement a familiar finite solver. It is to discover the structural invariant that makes the recursively generated system work, derive a reusable account of what each subproblem can do at its interface, and use that account to predict whether the whole construction admits a valid solution.

The environment should present an unfamiliar concrete problem, not announce the mathematical abstraction. Do not name “sheaves,” “global sections,” “holonomy,” “monodromy,” “cohomology,” or “recursive gluing” in the agent-facing prompt. Simply deleting those words is not enough: the prompt must not give away the key abstraction or the intended algorithm in ordinary language either.

At the same time, this must be a fair, identifiable problem. The operational rules required to act on the environment cannot be secretly withheld. If the agent is expected to infer a generating mechanism, the instance, examples, tool interactions, traces, or other public evidence must actually make the mechanism recoverable. The objective is latent but inferable structure, not a guessing game about hidden evaluator code.

## 2. The original motivating shape: the recursive maze

The recursive maze is the concrete prototype and should remain the center of design, not just one member of a supposed family of cross-domain replications.

Its important ingredients are:

- Rooms and corridors are local to tile types; a room name in one tile does not mean the same room in another.
- Walking a corridor or entering a child can change a state bit (the current implementation uses XOR orientation flips).
- Tiles may contain shafts into child tiles. At deeper levels, a repeated child type is used, so the same local pattern is encountered recursively.
- A tile's exit can be sealed until the walker has descended and returned; directed edges within a particular nested copy cannot simply be reused at will.
- A child tile may have a locally valid entrance-to-exit walk, yet choosing and composing local routes can leave the parent in the wrong state, or make the root goal impossible.
- The target is to expose the failure of the naive inference “every local part has a solution, therefore the whole recursively assembled object has a solution.”

The general mechanism need not be orientation XOR specifically. Orientation is a useful small state space for the first prototype, but the design goal is a robust family of recursively composed state transformations / boundary behaviours. The important feature is that the state needed to compose subproblems is richer than a Boolean “child solvable” flag. A correct abstract summary might encode which entry/exit states are mutually realizable, along with whichever finite history or resource state is genuinely needed.

A strong instance should make each local component look reasonable and locally feasible while producing a global obstruction only after the recursively repeated transformations, compatibility conditions, and root goal are considered together. Paired instances should make the source of the difference inspectable: change a carefully selected condition while preserving as much of the local structure as possible.

## 3. What the current repository already contains

Repository: `StrangeTcy/rl_eval_generator`  
Relevant branch: `arena/1ddc930c-rl-eval-generator`  
Recent four-app design correction: commit `0dcb51cbfa35598fa843905c3384d93a5fc95a71`.

### `envs/cat_theo/recursive_maze_gluing/`

This is the closest concrete prototype. Its generator uses `keep`, `inner_keep`, `crypt`, and an optional `pit` decoy. The `inner_keep` tile is recursively reused at deeper levels. The regime toggles a corridor flip; the solver must respect nesting, orientation, exit sealing, and edge-use constraints. The reference oracle uses BFS over state including the tile stack, room, orientation, cleared status, and used edges.

Its current configuration only selects depths 1, 2, and 3. The agent prompt explicitly explains the operational rules for nesting, XOR orientation, sealing, and edge reuse, then asks for an explicit route. Grade cases include a visible one-corridor case, the configured case, known SAT/UNSAT cases, an opaque relabelled twin, a decoy case, and deterministic behaviour.

This is a useful starting task and correctness harness. However, as currently written, it appears closer to “solve a fully specified small recursive maze” than “recover a hidden non-trivial generating mechanism.” The prompt describes much of the critical mechanism, the available depths are small, and a generic explicit search can plausibly solve these instances. The design review must test this diagnosis against the code, not just accept it.

### `envs/cat_theo/recursive_gluing_discovery/`

This has a compact recursive grammar and depths 3, 6, and 12. Its judge builds an independent bottom-up reference summary: for every module type and remaining depth, it computes all realizable boundary pairs, then applies the root-closing constraint. It avoids materializing the complete exponentially unfolded tree in the oracle.

This is a valuable formalization of the compact-composition target and may provide useful controls or oracle machinery. But the prompt explicitly specifies the grammar, recursive production rules, the complete realizable-pair certificate, and how to decide root satisfiability. It therefore tests implementation of a known compositional algorithm more directly than discovery of the algorithm or its generating mechanism. Treat that as a distinction to investigate, not a flaw to paper over.

### `envs/cat_theo/recursive_gluing/`

This is the expanded constraint-network / CSP formulation. It may be a useful explicit control against a compact recursive representation, but a control relationship must be demonstrated experimentally and not assumed from the names.

### Four sibling applications

`recursive_holonomy_gluing`, `recursive_compiler_bootstrap`, `recursive_error_correcting_codes`, and `recursive_coarse_graining` have made progress on generator correctness and shortcut-resistance. The current readiness audit correctly says their model performance is unmeasured and that their contrasts are not all clean. They should not automatically be called cross-domain replications of the main construct. Treat them as candidate mechanisms or analogies only if the review establishes exactly what common capability they test and what independent evidence would validate that claim.

## 4. Separate the claims we might test

Avoid treating “the model solved it” as one undifferentiated conclusion. Distinguish at least these levels:

1. **Explicit solving:** The agent can produce a valid route / assignment on a fully specified finite instance.
2. **Compositional generalization:** The agent recovers a reusable summary or recurrence and applies it to held-out instances, structures, and depths.
3. **Generating-mechanism recovery:** The agent infers the non-obvious rule that explains why the recursive construction behaves as it does, using available evidence rather than simply reading the rule in the prompt.
4. **Structural transfer:** The agent carries the principle into a genuinely different presentation or domain. Similar-looking tasks do not establish this automatically.
5. **Claims about internal concepts:** Successful behaviour does not, by itself, prove that the model internally represents a sheaf-theoretic concept. Such a claim would require separate evidence.

The central research target is levels 2 and 3, grounded by level 1. Level 4 may be a later research program. Level 5 is not established by task accuracy alone.

## 5. Design constraints and failure modes

### A. The latent mechanism must be inferable

- Do not tell the model the target theory, the intended invariant, or the algorithm to implement.
- Do provide enough public evidence—through the instance structure, examples, safe tool access, observed runs, or deliberately selected demonstrations—that a competent agent could distinguish the intended mechanism from plausible alternatives.
- Do not confuse naming opacity with conceptual opacity. Renaming `door` to `qxjvm` tests less than hiding the compositional invariant.
- If an interaction protocol is necessary to infer the mechanism, explicitly model it as part of the task rather than silently assuming a single static prompt is enough.

### B. Self-similarity must be consequential

- Recursive structure should recur at multiple depths and affect the reachable states of higher levels.
- A valid summary for a child must not collapse to the Boolean “solvable.” It must preserve exactly the interface behaviour that parent composition needs.
- Locally feasible pieces should coexist with globally incompatible compositions in at least some cases.
- A depth increase should be a real increase in recursive work, not a configuration number that saturates or changes a different variable.
- Decoys should be locally plausible and distinguishable by evidence, not arbitrary distractions.

### C. Controls must isolate the variable named in a claim

- Pair satisfiable/unsatisfiable examples with identical or maximally matched local components where feasible; make the global difference explicit in the hidden design and available through the input evidence.
- Change depth while holding generating rules, label mode, and answer polarity fixed when estimating scaling.
- Change label/presentation while preserving the exact latent task when estimating invariance.
- Distinguish “same local components, different closing condition” from “a different local generator.”
- Do not call a contrast “nesting” if it also changes polarity or several structural features.
- Keep test and demonstration instances separate from held-out cases; prevent seed leakage and file/path/metadata leakage.

### D. Brute force is a competing explanation to measure

An exact search solver may be perfectly legitimate at small sizes. The issue is whether the benchmark's intended claim survives when explicit enumeration is not a viable explanation for performance.

Compare against, as appropriate:

- constant/label heuristics and “local pieces imply SAT” baselines;
- local-only recursive glue that ignores orientation or the required state interface;
- shallow-depth, first-child, trust-the-claim, or similar shortcut baselines;
- straightforward unfolded BFS/DFS / generic CSP solving at small sizes;
- a compact dynamic-programming reference based on a sufficient interface summary.

Do not rig the benchmark so correct general-purpose search is unfairly penalized. Instead, establish the size/depth range where brute force is feasible and where compact compositional reasoning becomes necessary, and measure resources as well as correctness.

### E. Validation requires more than unit tests

Generator/oracle tests establish that the task is generated and scored as specified. Leakage tests establish that unintended answers are not handed to the agent. Neither establishes construct validity. Construct validity needs evidence that the task differentiates the target capability from its competing explanations.

Measure at least correct SAT/UNSAT or route outcomes, invalid purported solutions, false SAT versus false UNSAT, held-out generalization, performance by depth, and compute / interaction cost. Preserve raw model traces and outputs for diagnosis. Treat all internal-reasoning interpretations as hypotheses, not observations.

## 6. Questions the Arena design review must resolve

1. Is the main task supposed to infer a generative mechanism from examples / interaction, infer a compact structural algorithm from a recursive instance, or explicitly test both in separate phases? Which is the cleanest operationalisation of the intent?
2. What exactly is the invariant needed for correct recursive composition in the maze? Is the current interface summary sufficient, or must it preserve orientation, edge-use, sealed-exit state, nesting/return state, or other information? Prove the proposed summary sound and complete against the exact route semantics.
3. Can a generic BFS/DFS, simple parity trick, static template, or shallow-depth lookup solve the current grade instances? Demonstrate the strongest plausible shortcuts against the actual generator and judge.
4. Does current recursive maze generation produce sufficiently deep, nontrivial, self-similar obstruction cases—or does the visible structure give away a small one-off puzzle?
5. How can two instances be made maximally matched locally while differing in global satisfiability due to recursive composition?
6. How can we design held-out cases where the generating rule must transfer beyond seen seeds and a single hand-authored maze template?
7. What is the smallest defensible experiment that would distinguish local gluing from genuine compositional generalization and mechanism recovery?
8. Which code changes should be made first, and what tests would demonstrate that each change improved the scientific design rather than merely adding complexity?

## 7. Definition of a good outcome

A good outcome is not “more environments” or “all tests pass.” It is a task whose intended construct is operationally precise; whose mechanism is latent but recoverable from legitimate evidence; whose locally valid components can produce a provable global obstruction only after the relevant recursive interactions are composed; whose difficulty and controls are meaningful; whose strongest shortcut explanations have been tested; and whose results can be interpreted without overclaiming.

The immediate deliverable should be a candid adversarial review of the existing design and a prioritized proposal for changing the code. Do not run model calls until that review identifies a defensible hypothesis, clean contrasts, strong baselines, held-out tests, and go/no-go criteria.
