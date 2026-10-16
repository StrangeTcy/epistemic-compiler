# Task: Establish that recursive local-to-global reasoning is necessary, not cosmetic

Repository: `StrangeTcy/rl_eval_generator`

Assigned branch: `arena/1ddc930c-rl-eval-generator`

The latest reported commit hashes conflict across prior reports. Inspect the actual branch and current HEAD. Do not assume either `c50f128e0ab4c3e51e5cca14a1851d67be82c561` or `d365d9e407b29ea4a5764cca0fe87e7f4d53c861` is current.

## Objective

The research target is recursive local-to-global reasoning, grounded in the sheaf-theoretic perspective. The current environments may already implement valid tasks and judges, but that does not establish that the intended reasoning is necessary to solve them.

This pass must mechanically establish whether shallow methods can solve the current distributions and, for one selected environment, construct and verify cases that separate:

1. local solvability from global solvability;
2. pairwise compatibility from the existence of a global solution;
3. ordinary global solving from reasoning over recursively nested subproblems;
4. a correct judge from an accurate but potentially shortcut-prone benchmark.

Do not redesign all three environments. Do not add new environments or build a shared generic solver. Audit the existing three, then make a bounded, evidence-driven improvement to one.

No paid APIs, external-model runs, campaign changes, or speculative claims about model capabilities.

## Phase 0 — mandatory repository audit

Perform this phase before modifying environment code.

### 0.1 Preserve and identify the repository state

Run and record:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git log --oneline -15
git stash list
```

Preserve existing uncommitted changes. Do not reset, discard, or overwrite work to restore a previously reported commit. Work on top of the actual branch state.

Read the relevant files in full:

- `envs/cat_theo/recursive_maze_gluing/`
- `envs/cat_theo/recursive_distributed_gluing/`
- `envs/cat_theo/recursive_epistemic_gluing/`
- `envs/cat_theo/recursive_gluing/` and `envs/cat_theo/recursive_gluing_discovery/` as read-only controls
- `docs/decisions/2026-10-16-sheaf-recursive-reasoning.md`
- the environment registry and `envs/interventions.yaml`
- the applicable environment tests and shared judge implementation.

Adapt paths to the actual repository layout. If a named file does not exist, report that fact rather than silently substituting a different file.

Write `docs/audits/2026-10-16-recursive-gluing-necessity-audit.md`, or a dated successor if the name already exists. Include file and line references and actual commands or test outputs. Separate verified findings from hypotheses.

### 0.2 Test the current environments

For each of the three domain environments, generate at least 200 deterministic instances using the existing default configuration, or the largest reproducible sample the actual harness permits. Record the exact sample size and any limitations.

Measure these baselines against the ground truth determined by the environment's precise domain semantics:

**B0 — local-only solver.** Predict SAT exactly when every local subproblem has at least one admissible solution.

**B1 — pairwise-compatibility solver.** Predict SAT according to the environment's pairwise overlap or interface-compatibility conditions, without checking higher-order or global constraints.

**Bflat — recursion-flattening solver.** Replace each nested subproblem's behaviour with the permissive boundary approximation defined for that domain, then solve the resulting task. Implement this as an actual baseline, not an informal guess.

**Bk — bounded-depth solver.** Truncate recursive reasoning at depths 0, 1, and 2 wherever those truncations are well-defined for the environment. Record when a baseline cannot be meaningfully defined.

**M — metadata and surface-feature probes.** Measure the strongest single-feature predictors available from public instance data: instance ID, seed-related fields if exposed, domain size, depth, counts, label statistics, twist parity, or other relevant scalar features. Do not use hidden judge metadata as agent-visible input.

For each environment, record SAT/UNSAT counts, accuracy on the full sample, accuracy on UNSAT instances, balanced accuracy when applicable, Bflat's agreement with ground truth, and the smallest concrete counterexample found for each failed baseline.

A baseline's answer accuracy and its agreement rate with ground truth are distinct measurements. Report both. Never exclude failed cases to improve a score.

### 0.3 Audit judge independence

For every environment, establish from the actual source whether the judge:

- recomputes answers from domain semantics;
- uses generator-only metadata or precomputed ground-truth labels;
- imports or calls the reference solver to decide correctness;
- rejects malformed outputs and invalid witnesses;
- treats timeout, crash, or resource exhaustion as failure or `undetermined`, never as evidence that a task is UNSAT.

Write explicit findings with file and line references. Add mechanical tests for important independence claims.

If any judge has a demonstrated correctness or independence defect, **fix that defect first in the affected environment and stop this implementation pass after regression tests and a final report**. Do not build a more ambitious benchmark on top of a defective judge.

### 0.4 Audit the mathematical claims

Read the existing design note. Correct any assertion that describes an unsatisfiable instance as a failure of the sheaf gluing axiom without justification.

The correct distinction is essential:

- Let \(A(U)\) be the assignments to variables or configurations on region \(U\), with ordinary restriction maps. Under the usual assignment semantics, compatible local assignments glue uniquely.
- Let \(S(U)\subseteq A(U)\) be the assignments satisfying the constraints whose scopes are wholly contained in \(U\). If the cover localizes every constraint, compatible locally admissible assignments glue to a globally admissible assignment.
- Therefore, a nontrivial UNSAT instance is not automatically a failure of the sheaf axiom. It can be the **absence of a global section** of the relevant constrained solution structure, even when all local solution spaces are nonempty.

Where the instance includes transports or accumulated state, formalize how those transports compose. A nontrivial twist around a cycle may be described using holonomy or a finite local system when the construction mathematically warrants it. Do not attach cohomological language to a task without defining the mathematical object and proving the claimed correspondence.

Append corrections to the existing note or add a clearly linked addendum. Preserve the history.

## Phase 0 decision rule

After committing or otherwise preserving the audit, choose the next action by this fixed rule:

1. If a judge correctness defect was found, fix only that defect, add regression tests, and stop.
2. Otherwise, select the environment with the highest B1 accuracy on its UNSAT sample, because this is the environment whose supposedly global negatives are most susceptible to pairwise reasoning. Break ties by higher Bflat agreement with ground truth; then use the fixed order maze, distributed, epistemic.
3. Record the selection and the measurements that determined it. Apply the following implementation requirements only to the selected environment. Leave the other two read-only.
4. If all three already establish the intended distinctions with mechanical evidence, do not invent a weakness. Add the audit and appropriate regression guards, report the result, and stop.

## Phase 1 — mathematical contract for the selected environment

Before changing its generator, write a domain-specific decision note explaining the formal model, the sheaf-theoretic interpretation, the operational semantics, the global solution criterion, the exact verifier, and the evidence required to establish that recursion and global interaction matter.

Use the actual data structures found in the source. Do not blindly retrofit the following descriptions onto an environment whose present semantics differ.

### If the maze environment is selected

The intended model is a collection of recursively nested grid-maze module types. Each module has traversable corridors, boundary ports, and slots that may contain copies of other module types. Each slot has a port mapping. Corridors may carry a binary twist \(t\in\mathbb Z/2\).

Operational state is a stack of nested module occurrences, a current cell, and the accumulated twist. Entering a child pushes the stack; exiting through a child port returns to the corresponding parent boundary and pops it. A valid route begins at the root start with an empty stack and twist zero, and reaches the designated root goal with an empty stack and twist zero.

A route is a concrete sequence of legal moves. The evaluated agent must return a route for SAT, not merely name a boundary pair.

Formally, let \(\Sigma_M\) denote the least set of realizable boundary-to-boundary traversals of module type \(M\), including entry/exit ports and accumulated twist. It satisfies a recursive closure equation:

\[
\Sigma_M=\operatorname{lfp}(\Phi_M),
\]

where \(\Phi_M\) composes the actual corridor transitions with the behaviour of every nested slot, using its port mapping. State the fixed-point construction precisely for the existing implementation. The root instance is SAT exactly when its start-to-goal traversal with final twist zero belongs to the root's realizable relation.

The raw local assignment or route-fragment structure should have a precise restriction and compatibility semantics. Demonstrate the gluing property for that raw structure. Define the constrained substructure that enforces the required boundary state, and explain why it may have no global section even though the unconstrained route structure glues correctly.

A useful obstruction construction has all of these properties:

- each local module admits at least one traversal;
- all local tables and port mappings are nonempty;
- forgetting the twist makes the root start-to-goal task solvable;
- every globally possible start-to-goal route has final twist one;
- requiring final twist zero therefore makes the complete task UNSAT;
- neutralizing any one twist on a declared obstruction support spanning at least two module types restores SAT.

The judge must mechanically verify these properties. An empty local domain or malformed slot is not a nontrivial global obstruction.

The state space and route depth must have an explicit resource contract. Use bounded product-state exploration for independent checks; never infer UNSAT from budget exhaustion.

### If the distributed-computation environment is selected

Use the actual program, processor, channel, lock, message, and sub-system semantics. A global witness must be a valid distributed execution, schedule, or protocol trace.

Precisely define local traces, restrictions to shared channels or locks, compatibility of sends and receives, resource ownership, termination, and how recursively invoked sub-systems affect the parent's possible inputs, outputs, and resources held on return.

Include instances where workers have locally valid traces and selected pairs of workers are compatible, but there is no globally valid execution. At least one recursive obstruction must depend on a sub-system retaining a resource or returning a constrained result; a flattened sub-system that returns immediately with arbitrary allowed output must produce the wrong verdict.

The judge must simulate or exhaustively explore the global transition system independently of the reference scheduler. Specify a state-count budget, and treat an exceeded budget as `undetermined`, never UNSAT.

Do not reduce the task to recognizing a syntactic lock cycle unless that cycle is sufficient and necessary under the actual operational semantics.

### If the epistemic environment is selected

Use the actual possible-world model, observation relations or partitions, propositions, and modal query language.

For agent \(a\), define \(K_a\varphi\) at world \(w\) by requiring \(\varphi\) to hold at every world observationally indistinguishable to \(a\) from \(w\). Nested modalities must be evaluated recursively under this semantics.

Distinguish an actual fact from an agent's knowledge of that fact, and distinguish \(K_aK_b\varphi\) from \(K_a\varphi\). Include held-out instances where truncating nested knowledge changes the answer, and where each agent's local report is consistent but the proposed joint situation has no admissible world or valuation.

Explain how the selected task relates to local solution structures and global sections. If it only instantiates a finite constraint-presheaf view of information states rather than a stronger sheaf-theoretic invariant, say that explicitly. Do not relabel ordinary model checking as a cohomological obstruction without a formal argument.

The independent judge must evaluate the modal formula over the specified model or enumerate the bounded model space directly. It must not use hidden labels or the reference solver as the source of truth.

## Phase 2 — construct a matched test distribution

Build deterministic, seeded instance classes for the selected environment. Use the following classes as the conceptual target; adapt names and serialization to the existing repository conventions.

**POS-plain:** SAT, and replacing recursive subproblems by the permissive boundary approximation preserves the verdict.

**POS-recursive:** SAT with an accepted witness that genuinely descends into a nested subproblem at depth at least two. The flattening baseline's proposed witness must be invalid under the real semantics, or its verdict must differ from ground truth.

**NEG-local:** UNSAT because at least one local problem is unsatisfiable. This is an explicit trivial control, not evidence for a global obstruction.

**NEG-pairwise:** locally nonempty, but incompatible local sections already expose the contradiction at a pairwise level. This is another explicit control.

**NEG-deep:** each local region is solvable; the stipulated pairwise compatibility test holds; compatibility also holds for every compatible combination over three cover elements, but no global section exists. This class does not need recursion to create the obstruction.

**NEG-recursive:** each local problem is solvable and satisfies the selected pairwise compatibility criterion, but no globally admissible solution exists because of the semantic behaviour of nested subproblems. The flattening baseline incorrectly predicts SAT or proposes a witness rejected by the true verifier.

**FLIP pairs:** each selected NEG-recursive task has a minimal task-changing twin differing in a declared rule or nested constraint, where the correct verdict flips. It also has a presentation-only twin—renaming types or labels or reordering entries—that preserves the verdict and transforms any witness to another valid witness.

For each class, specify which exact properties must hold and implement code that checks membership. Do not classify an instance according to the generator's intended label alone.

Generate a reproducible development set with at least 30 instances per feasible class. Use a held-out seed range not used in development, tests, or examples. Run the same class checks on the held-out set at report time.

A class may be marked unsupported only after documenting the precise semantic or resource reason. Do not silently omit difficult classes or replace them with weaker ones.

## Phase 3 — establish that the target reasoning matters

Implement deterministic baseline solvers as ordinary test or analysis code, not as part of the judge. Include:

- B0: constant majority predictor;
- B1: the local-only and pairwise baselines from Phase 0;
- Bflat: the domain-specific recursion-flattening baseline;
- Bk: depth-truncated baselines for supported depths;
- a metadata-only predictor trained on development data and evaluated on the held-out split.

The principal requirement is not that every baseline scores exactly chance by construction. It is that its actual accuracy and failure modes are measured, and that each claimed hard class provably defeats the shortcut it is designed to defeat.

Require the reference solver and independent judge to agree on all generated cases. For NEG-recursive, the flattening baseline must demonstrably fail on every accepted member of the class. For POS-recursive, its claimed witness must be rejected by the full semantics where the intended contrast requires it.

Use a balanced SAT/UNSAT distribution for the overall held-out classification comparison, with minimal matched pairs wherever feasible. Report per-class and per-factor metrics so the balanced aggregate cannot hide trivial failures.

Report failures honestly. If a baseline performs well, determine why and either refine the task with a meaningful semantic intervention or leave the result as evidence against the hypothesis. Never tweak labels, seed correlations, scoring, or hidden metadata to force a desired accuracy.

Do not run external-model campaigns. This phase establishes what the deterministic controls can solve, not what any model has learned.

## Phase 4 — independent judge and certificates

The judge must verify SAT witnesses from domain semantics.

For SAT, reject illegal moves or transitions, invalid stack or call/return behaviour, mismatched messages or resources, invalid modal valuations, violated constraints, overlong witnesses, malformed JSON, and any other domain-specific contract violation.

For UNSAT, use a complete independent decision procedure within a declared state-space bound. Where appropriate, allow a private certificate that the judge can verify without importing the generator or reference solver.

For the maze, one useful certificate is a family of module relations closed under the recursive rules, containing every base traversal and closed under \(\Phi_M\). Because the least fixed point is contained in every closed superset, if the root target is absent from such a certificate, the target traversal is unreachable. Prove the details for the actual transition system before relying on this argument.

Add tests that monkeypatch the reference solver to fail and confirm that the judge remains able to decide the result independently. Add an AST-based import check where useful.

Malformed outputs, crashes, and resource exhaustion must never count as correct UNSAT claims. The instance generator must discard instances exceeding its generation budget rather than falsely labelling them UNSAT.

## Phase 5 — agent-facing prompt and leakage tests

Keep the development specification separate from the evaluated agent's prompt.

The evaluated agent must receive all operational rules, the instance format, the output contract, and sufficient information to determine correctness. Its prompt must not prescribe the intended solution algorithm.

Do not use the terms `sheaf`, `presheaf`, `section`, `gluing`, `glue`, `holonomy`, `monodromy`, `cohomology`, `Čech`, `local system`, `fixed point`, or descriptions that explicitly instruct the model to construct per-module transfer summaries.

These terms belong in the developer-facing mathematical note, not the evaluated prompt.

The generated prompt must be linted after placeholder substitution; checking only the template file is insufficient. Include environment paths where the harness exposes them, and document any unavoidable terminology leak from fixed directory names.

Check that type names, instance IDs, seed fields, field order, grid size, label statistics, and filenames do not reveal the answer. Presentation transformations must preserve correct outputs; task-changing transformations must change semantics in a judge-verified manner.

Implement explicit and revealing evaluation conditions only if the existing overlay machinery supports them cleanly. Define their exact distinction from the inference condition, but do not run models.

## Phase 6 — tests and preservation

Include tests for:

1. Deterministic generation and byte-identical output for identical parameters and seeds.
2. Independent verification of reference witnesses.
3. Completeness of the bounded exact judge on exhaustive small cases.
4. Each instance class's defining properties.
5. The smallest hand-written NEG-deep and NEG-recursive examples, with their actual solver and judge outcomes.
6. A minimal FLIP pair and an inert presentation twin.
7. Recursion necessity under Bflat and Bk.
8. Local solvability and pairwise compatibility of the claimed nontrivial obstructions.
9. Correctness after renaming or reordering.
10. Judge independence from the reference solver and generator metadata.
11. Budget exhaustion, invalid certificates, malformed output, and overlong witnesses.
12. Prompt terminology lint after full rendering.
13. Held-out sample metrics and metadata-probe reports.

Avoid wall-clock assertions. Use reproducible state-count and search budgets. Keep existing tests intact and run the relevant repository integration suite.

Preserve both `recursive_gluing` and `recursive_gluing_discovery` byte-for-byte, along with campaigns, campaign state, workflows, reporters, verdict gates, provider-preflight code, and the two non-selected recursive environments. Do not add environments, alter shared scoring semantics, merge or rebase onto `main`, force-push, or use paid APIs.

## Phase 7 — final report

Commit on the assigned branch with a descriptive commit message. Report:

1. Actual starting and final HEADs, branch, starting worktree state, and `git diff --stat`.
2. The Phase 0 audit and the decision rule outcome, with numeric evidence.
3. The selected environment and the reason for selecting it.
4. The local-to-global formalization, including the sheaf-theoretic object and its gluing behaviour. Explicitly distinguish absence of a global section from failure of the sheaf axiom.
5. The exact judge's correctness argument and resource contract.
6. The smallest NEG-deep and NEG-recursive examples, one FLIP pair, and one presentation-only twin, with actual witnesses or certificates and judge results.
7. Test commands and real results.
8. Baseline metrics for development and held-out data, the metadata audit, and the evidence for or against each research hypothesis.
9. Unsupported classes, known limitations, and follow-up work for the two non-selected environments.

Maintain a claims ledger that tags every claim as one of `[formal]`, `[tested]`, `[reference-solver only]`, or `[requires model runs — not done]`.

The final report must distinguish three accomplishments: an implemented task, a verified reference solver and judge, and demonstrated model capability. This pass can establish the first two. It must not claim the third.
