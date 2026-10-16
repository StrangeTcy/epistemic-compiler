# Implement the Holonomy Engine and three semantically distinct recursive-gluing applications

**Repository:** `StrangeTcy/rl_eval_generator`  
**Assigned branch:** `arena/1ddc930c-e1val-generator` — verify the actual branch name before using it; prior working context identifies `arena/1ddc930c-rl-eval-generator`.  
**Scope:** Four new sibling environments, preserving every existing environment and all campaign state.  
**Execution constraint:** No paid API usage and no external-model campaigns.

## Objective

Add four independently meaningful tasks to the existing recursive-gluing research family:

1. `recursive_holonomy_gluing` — discover latent finite transformations and solve a recursive local-to-global consistency problem.
2. `recursive_compiler_bootstrap` — verify semantic preservation and consistency across recursive compiler/bootstrap stages.
3. `recursive_error_correcting_codes` — recover recursively structured codewords under hidden symbol relabellings and exact parity constraints.
4. `recursive_coarse_graining` — compose finite physical models across scales, derive exact effective descriptions, and test compositional consistency and fixed points.

These are **four different task semantics**, not four names for one CSP. They may reuse repository configuration, prompt-rendering, seed, intervention, provenance, scoring, and reporting infrastructure. Each must have domain-specific instance representations, an independently justified oracle, domain-native witnesses or certificates, and tests that would detect a bug in that domain's semantics.

Preserve the current `recursive_gluing`, `recursive_gluing_discovery`, `recursive_maze_gluing`, `recursive_distributed_gluing`, and `recursive_epistemic_gluing`. Do not replace them, rewrite them, weaken their tests, or infer that they validate the new tasks.

## 0. Mandatory repository audit

Before changing anything, inspect and record:

- `git status --short`
- `git branch --show-current`
- `git rev-parse HEAD`
- `git log --oneline -15`
- `git stash list`
- the current environment registry, shared judge utilities, experiment/intervention configuration, and relevant recursive-gluing implementations and tests.

Verify the branch against the actual checkout; do not assume that the branch name or previous HEAD in this prompt is correct. Preserve existing commits, uncommitted changes, campaign YAML, provider-preflight work, reporters, verdict gates, and running workflows. Do not reset, rebase, force-push, or move work between campaign lineages.

Create a short audit note containing the initial state and the conventions to be reused. Work on top of any existing changes without discarding them.

## 1. Shared research contract

The research target is whether an evaluated model can recover useful latent structure, exploit recursive semantics, and establish global correctness—not merely produce a plausible answer or an explanation that sounds mathematical.

Give each environment:

- a deterministic, seedable instance generator;
- a compact and explicit instance representation where the domain permits both;
- a candidate-facing prompt with exact operational semantics and no leaked answer;
- a reference solver or oracle;
- a judge that independently checks the candidate's submitted answer;
- positive and negative examples where meaningful;
- deterministic baselines, tests, and machine-readable result summaries;
- declared representation and structural interventions, with semantic equivalence checks;
- held-out seeds and transformation variants;
- input-size, explicit-expansion, and oracle-work measurements where applicable.

Use matched experimental conditions when meaningful:

**Structural conditions:** direct control, recursive control, flat consistency/composition control, and recursive composition/gluing target.

**Representation conditions:** hidden/inferred representation, representation supplied/revealed, and explicit expansion when it is a well-defined transformation for that domain.

**Outcome conditions:** satisfiable/obstructed for existence problems; semantically equivalent/non-equivalent for compiler verification; valid/inconsistent codeword or decoding for the code task; exact/inconsistent effective table and fixed-point/non-fixed-point for coarse-graining. Do not force a generic SAT/UNSAT label onto tasks whose natural answer is a different property.

Use existing experiment-arm and overlay conventions where they fit. Keep underlying semantics and task identity matched across representational conditions. Record whether each intervention changes the task, reveals information, or only changes presentation.

**Do not build one universal CSP and merely change its story.** The representation and independent semantic checker for each of the four environments must be recognizably domain-specific. If a shared helper becomes part of the trusted computing base, document it and cross-check its output independently.

## 2. Environment A — `recursive_holonomy_gluing`

### Research question

Can a model infer latent coordinate transformations and exploit a compact recursive description to decide whether locally valid configurations can be assembled into a globally consistent solution?

### Mathematical core

Represent each finite local region \(U_i\) using its own finite state space \(S_i\). On an overlap, an observable transition map transports a local state from one representation to another. A global section is an assignment satisfying all overlap equations.

For a cycle, compose the transitions in a documented order. A globally compatible state must be fixed by the resulting composite map. Generate cases where fixed points exist and cases where none exist, even though every local state space is nonempty and every individual transition map is valid.

Be precise about the sheaf-theoretic interpretation. Unrestricted assignments with ordinary restriction form a genuine sheaf; do not call an UNSAT instance a failure of the sheaf gluing axiom. Describe instead the constrained local-solution structure and prove why it lacks a global section.

### Required exact transformation families

Implement and verify all three:

1. **Finite multiplicative transformations.** Use a finite multiplicative group such as \(\mathbb F_p^\times\), with exact multiplication and composition. On a cycle with composite \(z\mapsto Qz\), verify that a fixed point exists exactly when \(Q=1\). The candidate prompt must not prescribe logarithmic coordinates.
2. **Affine transformations.** Use \(x\mapsto ax+b\pmod p\), \(a\ne0\). Compose exactly and compute the fixed-point set correctly; nonidentity affine maps do not all have the same fixed-point behaviour.
3. **Finite permutations and relabellings.** Compose exact permutations and support arbitrary bijective re-labelling. Include both permutations with fixed points and derangements.

Give enough observable calibration data for intended transformations to be identifiable, or define an output contract that accepts all semantically valid answers when the instance is underdetermined. Never leak generator-only transformation parameters or the target label.

### Recursive semantics and witnesses

Use a compact finite-depth grammar with module types, boundary ports, local overlap structure, and production rules. Parent behaviour must depend on its children's actual boundary behaviour and transformations—not merely on their occurrence count.

Do not just copy the existing two-port relation grammar and rename it. Implement compact composition over the supported finite transformations, and cross-check it against a separately represented explicit solver on exhaustive or broad shallow cases.

Require a machine-checkable global-section witness for positive instances. For negative instances, independently establish the absence of a section or verify a valid obstruction certificate. Never interpret resource exhaustion as proof of UNSAT.

Add the four structural conditions and the inferred/revealed/explicit comparisons when they can be defined without changing the underlying semantics.

## 3. Environment B — `recursive_compiler_bootstrap`

### Research question

Can a model verify meaning across recursively connected compiler stages, infer hidden representation or interface correspondences, and detect an inconsistency in a claimed bootstrap diagram rather than checking each stage in isolation?

This task must use actual executable toy-language semantics, not merely arbitrary variables and equality constraints bearing compiler terminology.

### Finite, executable semantics

Build a small deterministic source language and a small target instruction language with fully specified finite semantics. A suitable choice is a bounded arithmetic language interpreted over a finite value domain and a stack or register bytecode with an exact interpreter. Define each AST/instruction, execution rule, and observation function precisely.

Construct compiler stages and bootstrap paths as maps between representations. Include versioned instruction encodings, boundary conventions or interface representations that can be re-labelled bijectively. Recursively include a compiler artifact being translated or compiled through earlier stages.

A local stage contract must specify:

- its source-program domain;
- its compiler/translation map;
- the source and target interpreters;
- any encoding/decoding map at the interface;
- the exact finite set of programs or all-program domain on which its claim applies.

The semantic oracle must execute or exhaustively interpret the relevant finite programs. It must not accept a result solely because the generator says a stage is valid.

### Crucial consistency requirement

Do **not** manufacture a paradox. If every stage is formally proved to preserve the same semantics for every relevant program under a common, correctly connected semantics, their composition preserves semantics too.

For a meaningful global-obstruction case, make the object under test an explicitly represented set of stage-local contracts plus the shared interface/decoder/bootstrap correspondence claims. A cycle or complete diagram can be locally valid relative to its stated stage contracts but fail to admit one coherent system of interface interpretations, or a bootstrap claim can fail exact observational equivalence. State which property is being tested and why it follows from the finite operational semantics.

A valid positive witness should supply the stage translations and relevant interface correspondences, or a compact certificate for them. The judge independently verifies the commuting equations and observable source-to-target equivalence across the whole path.

A negative witness must identify a checkable contradiction, failed semantic obligation, or incompatible interface condition. Alternatively, the independent exhaustive oracle may establish that no interpretation/correspondence satisfies the declared contract.

### Required controls

Compare stage-local checking with complete-path checking. Where meaningful, contrast an ordinary compilation chain, a recursively bootstrapped chain, and a cyclic/bootstrap consistency task. Provide revealed-interface and inferred-interface variants of the same task.

Use source programs and target instructions, exact interpreters, and compiler-specific output checks throughout. The compiler judge must not simply call the Holonomy Engine judge.

## 4. Environment C — `recursive_error_correcting_codes`

### Research question

Can a model reconstruct a recursively composed codeword under hidden symbol relabellings, satisfy local code constraints, and determine whether a globally consistent decoding exists?

### Domain-specific semantics

Use finite-field arithmetic, such as \(\mathbb F_p\), and explicit linear or affine error-correcting codes. Each code block must have a defined symbol vector, parity-check matrix or generator matrix, and valid encoding/decoding relation. Define exactly how recursive child blocks contribute symbols to parent blocks.

Allow local blocks to use different symbol labels or coordinate orders. The observable instance must specify the relevant boundary/overlap coordinates and provide enough calibration evidence to infer the required permutations. Generate nontrivial permutations rather than only identity maps.

The independent verifier must perform finite-field arithmetic directly. For every asserted local codeword, check the appropriate parity equations. For every child-to-parent or overlap relation, check the declared mapping, including any inferred or submitted relabelling. Check global parity and the full recursive encoding condition independently of the generator.

### Positive and negative tasks

Positive instances require a full codeword or decoding witness that passes every local and global parity condition.

Negative instances must be validly constructed cases in which individual blocks have valid local codewords but their recursive overlap and global parity requirements have no simultaneous solution. Establish this through exact finite-field elimination where the system is linear, or exact enumeration for a bounded non-linear case. On shallow cases, cross-check the chosen oracle against a separate direct enumerator.

Include controlled comparisons where the coordinate transformation is revealed or hidden, and where a recursive code is compared with an explicit expansion. Measure both code specification size and expanded block/symbol count. Do not use an arbitrary generic-CSP verdict as the sole authority.

## 5. Environment D — `recursive_coarse_graining`

### Research question

Can a model derive an exact effective description of a recursively structured finite system, compose local descriptions correctly across scales, and tell an actual fixed point or invariance from an inconsistent or merely apparent one?

### Exact finite physical model

Use a finite statistical-mechanical or factor-graph model with a fully defined state space and exact local weights. A suitable design is a hierarchical finite-spin system whose spins have two or another small number of states, with integer or rational nonnegative local weights.

Represent a region's effective description by an exact boundary table: for each boundary assignment, the table gives the sum of weights of all compatible internal configurations. Compose child-region tables by multiplying local weights and summing over shared/internal states. State the normalization or equivalence relation exactly if one is used.

Avoid floating-point approximations. Do not require transcendental log-partition calculations. Use exact integers/rationals or another rigorously specified exact representation.

The instance may hide permutations of spin labels or boundary-port order; supply calibration data that make the transformations identifiable. Recursively nested regions must be evaluated using the true child boundary tables. Replacing a child by an arbitrary permissive table must change the output on designated test cases.

### Correctness and fixed points

The domain-specific oracle independently derives the effective table from the microscopic model and recursively verifies the composition rules. Compare its result against the submitted table exactly. Define a scale transformation \(T\) over the supported table representation and state whether equality is literal or modulo a declared normalization or relabelling.

Test both:

- an actual fixed point satisfying the specified equation for the exact transformation;
- a near-miss or inconsistent claim that fails under exact composition.

The candidate must provide the effective table and enough evidence for its claimed composition/fixed-point result. The judge must recompute the table from the observable microscopic factors. If the chosen model cannot support a meaningful non-fixed-point claim, report that limitation rather than inventing a binary obstruction.

This must remain a finite coarse-graining task with statistical/partition-function semantics—not a CSP with physical nouns substituted for variables.

## 6. Shared controls without semantic collapse

For each environment, implement the subset of the following controls that is mathematically well-defined, and document any inapplicable condition:

- **A — direct:** no recursive substitution and no difficult global composition;
- **B — recursive:** true recursive structure, but global consistency is guaranteed by construction;
- **C — flat composition:** a non-recursive instance requiring a genuine global composition or consistency check;
- **D — recursive composition:** recursion and nontrivial cross-region/scale/bootstrap consistency both matter.

For existence tasks, include valid and obstructed instances. For semantic equivalence or exact-table tasks, include positive and negative claims in the domain's own terms. Match pairs so that one task-changing intervention alters the correct outcome while a presentation-only relabelling preserves it.

For each task, add as applicable:

- **Inferred:** observable instance and calibration data only;
- **Revealed:** same semantic task with the required representation/correspondence provided;
- **Explicit:** a flattened or fully expanded encoding of the same underlying task.

Verify that transformed witnesses map back correctly, and that task-changing twins genuinely change the independently computed answer.

These controls are for isolating the contribution of recursion, global composition, and representation discovery. They are not evidence that a model has used a particular reasoning process. No external-model campaign is requested.

## 7. Candidate-facing prompt design

Each new environment must have its own `files/prompt.md`. Specify all input fields, finite-state semantics, recursive production rules, transformation/interface rules, required output, and certificate format.

Do not disclose the answer, hidden generator parameters, or a prescribed solution technique. In particular, do not tell Holonomy candidates to use sheaf theory, holonomy, logarithmic coordinates, or a particular group-theoretic method. Compiler prompts must describe executable language and interface semantics rather than announcing the intended diagram defect. Code and coarse-graining prompts must give exact parity/interpreter or weight-table semantics without naming hidden parameters.

Do not confuse secrecy of the solution with underspecification. Candidate-facing operational rules must be complete enough to define a correct answer.

Add tests that inspect rendered prompts after placeholder substitution: no unresolved placeholders, private generator metadata, leaked target labels, or forbidden solution-revealing instructions.

## 8. Independent verification, certification, and trusted components

For every environment, test:

- deterministic generation and reproducibility;
- exact calculations/composition in its native mathematics;
- positive witness acceptance and malformed/incorrect witness rejection;
- negative certificate checking or independent absence proof;
- rejection of an incorrect negative claim when a valid positive solution exists;
- consistency between the public instance and any submitted inferred representation;
- recursively nested boundary/interface semantics;
- invariance under presentation-only relabellings;
- verdict changes under verified task-changing twins;
- exhaustive or independently implemented shallow-oracle agreement;
- held-out seeds and transformations;
- resource limits and malformed output.

A time or memory limit must result in `undetermined` or a judge failure, not UNSAT. Document shared trusted code and add independent cross-checks to avoid an oracle that simply verifies its own answer.

Where applicable, provide compact witnesses for deep instances. Do not claim deep compactness if the witness or judge still expands and enumerates every state assignment. Count the work the implementation fuckingly performs.

## 9. Evaluation evidence and reports

Add deterministic baselines that correspond to real abilities, not straw men. At minimum, where applicable:

- a direct/expanded solver;
- a solver given the latent representation;
- a solver required to infer the representation;
- shallow/truncated recursion and locally-only decision procedures;
- explicit verification of the returned certificate.

Record actual baseline outcomes, negative-case accuracy, errors and limitations. Include instance counts, input bytes, expanded size, local configuration/transition checks, arithmetic or interpreter operations, and resource use where meaningful. Use held-out transformations and a disjoint seed range.

Add a machine-readable report for each environment. Distinguish formal properties, tested implementation behaviour, reference-solver success, and untested claims about model-level discovery. Do not call these environments validated model-reasoning benchmarks until models have fuckingly been evaluated on them.

## 10. Integration and preservation

Register the four environments as distinct siblings using actual repository conventions. If a collision or architectural incompatibility appears, document it explicitly rather than overwriting an existing task or silently merging domains.

Update the family documentation to explain the shared research question and the non-shared semantic oracles. The application environments must remain separate files/configurations with their own prompt, generator, verifier/judge, reference solution, tests, and report.

Keep the existing maze, distributed, and epistemic environments intact. Do not weaken the current recursive-gluing tests. Preserve campaign state, all workflows and preflight infrastructure, and any in-progress work.

No paid API calls; do not launch external-model campaigns.

Run the focused tests for all four environments, prompt-rendering checks, registry/generator smoke tests, explicit-vs-compact oracles where applicable, and the relevant regression suite. Commit on the assigned branch with a descriptive message.

## 11. Required final report

Report:

1. Actual starting and ending branch/HEAD and initial worktree status.
2. Files added/modified and the purpose of each.
3. A separate semantic specification and verifier description for each of the four environments.
4. Worked positive and negative examples for each domain, with their checked results.
5. Which controls and representation interventions are implemented and which are deferred.
6. Exact test commands and outcomes.
7. Compact-versus-expanded or native-domain scaling results, without runtime claims extrapolated solely from object counts.
8. The baselines and measured results.
9. Limitations, partial implementations, or unsupported cases.
10. A claims ledger distinguishing formal results, tested code, baseline/reference performance, and untested model-level discovery.

The deliverable is four semantically distinct, exactly verifiable tasks under one controlled experimental umbrella. The compiler verifier must be a compiler verifier, the code verifier a code verifier, and the coarse-graining verifier a finite physical-model verifier. Shared scaffolding is useful; shared fake semantics are not.
