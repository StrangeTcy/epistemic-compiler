# Research-valid v1: recursive gluing with latent-structure discovery

Work in `StrangeTcy/rl_eval_generator`, continuing from the assigned branch `arena/1ddc930c-rl-eval-generator` and the existing commit `93cc8dc567302238000deae082493bbce1350be6`, unless inspection shows the branch has moved. Check the current branch and working tree first.

This is a research-design revision followed by implementation. Do not stop at a proposal. Produce a running, registered environment with an exact judge, regression tests, and a commit on the assigned branch.

## 1. Preserve v0 as a control

The existing `envs/cat_theo/recursive_gluing/` is useful as a baseline: it has a finite CSP, an independently implemented oracle, a cyclic obstruction, opaque labels, and a valid generation/scoring path.

Do not delete it or weaken its tests.

The strategic limitation is that v0 provides an explicit, expanded set of regions and binary overlap tables. Its largest configured task has only 15 regions, and its overlap relations are bijections derived from a finite carrier. A generic CSP solver can propagate assignments around the graph and detect inconsistent cycles without recovering the hidden generative representation.

Do not attempt to repair this research limitation merely by increasing domain size or recursive depth while keeping the same observable problem.

Build a distinct sibling environment, provisionally named:

`envs/cat_theo/recursive_gluing_discovery/`

Register it separately. Retain v0 as the expanded-CSP control against which the new environment can be compared.

## 2. Research hypothesis

Test whether a model can implement a general solver that exploits a compact, recursively defined structure to solve problems whose fully expanded form is exponentially larger than the description.

The target abilities are:

1. Recover useful correspondences between locally relabelled components.
2. Reuse a solution to a recurring subproblem across differently transformed instances.
3. Compose local solutions across recursive boundaries and cross-links.
4. Detect global obstructions that are invisible to individual components and selected neighbouring pairs.
5. Generalize the inferred representation to held-out transformations, depths, and seeds.

Do not equate a correct answer with proof that a model discovered the hidden structure. The environment must make structure-aware computation useful, and its design must support later experiments comparing models and baselines.

## 3. New input representation: compact recursive constraint grammar

Define a small, precise class of finite-domain problems that are supplied as a compact grammar rather than a pre-expanded graph.

The exact schema is yours to design, but it must contain the following elements.

### Reusable module definitions

Each module type describes a local constraint problem, including finite-domain variables, internal restrictions, boundary/interface variables, and the constraints governing their compatibility.

Production rules recursively instantiate module types. Each rule may create multiple children and attach their interfaces to the parent and to one another.

The same finite collection of module definitions is reused at every recursive level. The instance specifies the root and a finite expansion depth.

### Local coordinate frames

Different occurrences must use different local labels for structurally corresponding states. Production rules apply explicit finite relabelling/transport tables; the solver must have enough observable information to determine valid correspondences, but must not be given a canonical global labelling or a named mathematical solution.

The presentation may use arbitrary tokens and permutations. Do not encode the answer in region names, state labels, generation order, comments, or other superficial cues.

### Global overlap structure

Local modules must include constraints that couple the interfaces of multiple children and the parent. Generate cycles and cross-level dependencies through recurring rules, so that global consistency is not equivalent to solving each child independently.

Include both:

- globally satisfiable cyclic instances; and
- globally unsatisfiable instances whose local domains and individual overlap relations are nonempty and locally compatible.

The obstruction must be a property of the composed constraint system, not an empty local domain, an empty relation table, a malformed instance, or a trivial contradiction planted in plain sight.

Do not implement a disguised flat CSP with a recursive-looking file format. Recursive substitution must materially determine the semantics of the problem.

### Exponential expansion

Choose depth levels where the explicit unfolded problem grows exponentially while the recursive description grows only modestly. For example, a binary expansion can produce approximately (2^{d+1}-1) module occurrences at depth (d).

Include depths large enough that naive full materialization becomes an unreasonable strategy, while a solver using a compact representation and bounded interface state remains practical.

Report both serialized input size and unfolded instance size. Demonstrate the scaling empirically in tests.

Keep the supported mathematical class narrow enough that its semantics and exact solvability can be justified. Do not quietly broaden it to arbitrary recursive CSPs if the proposed oracle or algorithm is only complete for a restricted grammar.

## 4. Require a compact solution certificate

The candidate solver must not need to emit one independent assignment for every occurrence in an exponentially large expansion.

Define a deterministic output contract that distinguishes `sat` from `unsat` and uses a compact certificate for either result.

For satisfiable instances, the certificate should encode a reusable assignment rule over the finite recursive structure and interface/context states. Its size should depend on the grammar, interface size, finite transport/context state, and depth—not on the full number of unfolded occurrences.

For unsatisfiable instances, require a machine-checkable certificate or complete finite summary establishing that no compatible root solution exists.

You may use a lookup table, finite-state strategy, or another compact representation, provided its semantics are explicit and the judge can verify it without trusting the candidate's prose.

A certificate is not acceptable merely because it matches a few visible instances. It must cover all recursively reachable contexts required by the instance.

## 5. Exact independent oracle

Implement an oracle that does not import or invoke the candidate solver.

The natural approach may be bottom-up summaries of boundary/interface possibilities, memoization over equivalent recursive contexts, and finite-state closure under the available transports. Choose the algorithm appropriate to the supported grammar, but document the exact mathematical justification.

The oracle must establish:

- soundness: every accepted certificate denotes a globally valid assignment or a valid proof of unsatisfiability;
- completeness: every satisfiable instance in the supported class admits an accepted witness, and every unsatisfiable instance is correctly rejected;
- correspondence with the fully expanded semantics.

For shallow instances, implement an independent expanded reference oracle or another extensional checker. Cross-check the compact oracle against it across many seeds and all relevant regimes.

Do not reuse the candidate solver, its internal summaries, or its hidden generation metadata to decide the answer. A timeout or resource-budget overrun is an explicit judge failure, never an unsatisfiability verdict.

If your chosen formal class does not support an efficient independent exact oracle and compact certificate, revise the class before proceeding to implementation.

## 6. Controlled experimental conditions

The new environment should have independent axes that correspond to real, documented changes.

At minimum:

- **Recursive depth:** shallow cases suitable for expanded cross-checking; medium cases that test reuse; deep cases where explicit expansion is impractical.
- **Interface/domain complexity:** vary the actual size of the local state spaces and interfaces, while keeping the exact oracle within a specified resource budget.
- **Gluing regime:** compatible acyclic cases, globally satisfiable cyclic cases, and globally obstructed cyclic cases.
- **Label opacity:** transparently aligned state labels versus independently relabelled occurrences. This must preserve the answer when treated as a presentation intervention.
- **Structural ambiguity:** include decoy module types or near-matching local patterns in some conditions, where treating merely similar components as identical would be incorrect. This must be declared as a real task change, not as label opacity.

Generate matched instances wherever possible. A transparent and an opaque presentation of the same underlying instance must have equivalent answers. SAT and UNSAT variants must differ semantically in ways the oracle can demonstrate.

Do not claim an intervention is supported unless it is implemented, tested, and registered under the repository's intervention conventions.

## 7. Baselines and evidence of a useful representation

The point is not to demonstrate that a recursive data structure can be parsed. Establish that using a compact structural representation is useful.

Include, at minimum:

1. The current v0 explicit-CSP environment as the baseline for ordinary global-consistency solving.
2. A reference algorithm operating on shallow expanded instances.
3. A straightforward full-expansion or explicit-solver baseline for a bounded set of larger instances, used to quantify expansion costs where it is feasible.
4. The compact reference oracle/solver for the new grammar.

In tests and an environment-design note, report the number of occurrences after expansion, compact input size, state/interface summary size, and runtime for increasing depths. Avoid fabricated or selectively chosen measurements.

The design must establish a resource gap between the explicit representation and the compact representation on the hard instances, without making the task depend on hardware accidents or an arbitrarily tiny timeout.

The coding environment's hidden judge should score correctness, certificate validity, transformation invariance, generalization to held-out instances, and compliance with resource limits. Do not award credit for explanations that merely name a plausible mathematical concept.

A later model evaluation can then compare:

- an ordinary explicit CSP solver;
- a solver given a canonicalized/revealed representation;
- a solver that must work with opaque local frames and the compact grammar.

Keep these as distinct experimental conditions. Do not claim that the environment alone proves a model can discover latent structure.

## 8. Agent-facing task prompt

Write a clear `files/prompt.md` describing the observable input format, output/certificate contract, and correctness requirements.

The benchmark prompt must not give away the intended solution algorithm or name the precise mathematical trick. In particular, do not instruct the evaluated agent to use sheaf theory, holonomy, group actions, a particular canonicalization algorithm, or a particular dynamic-programming strategy.

It must still provide enough information about the format and finite semantics to make a correct implementation possible. The challenge is to discover and exploit the recurring structure, not to guess undocumented input fields.

Keep the development task prompt and the benchmark's agent-facing prompt distinct: this research specification may name the intended scientific hypothesis; the evaluated agent's prompt must not provide its solution.

## 9. Tests and integration

Add dedicated tests for the new environment. Include:

- configuration, registry, layout, and generated-tree validation;
- deterministic generation and reproducible seeds;
- correct semantic variation for every difficulty axis;
- SAT and UNSAT cases with nonempty domains and nonempty local relations;
- cross-checks between expanded and compact semantics on shallow instances;
- correctness under independently relabelled local frames;
- held-out transformations, module arrangements, and recursive depths;
- certificate soundness and rejection of malformed certificates;
- oracle completeness on exhaustive small cases;
- an explicit demonstration that the naïve full expansion grows exponentially;
- a practical runtime/resource test for deep compact instances;
- baseline failure and reference-solver success;
- proof that a presentation-only intervention changes labels but preserves the answer.

Use the existing generator, judge framework, provenance rules, scoring interface, and latent-factor conventions. Generated files must compile after placeholder substitution. Preserve campaign state.

Write a short research-design note before or alongside the implementation. It must state the hypothesis, supported formal class, semantics of the compact certificate, oracle-completeness argument, expected scaling, and the competing explanations this design can distinguish. Then finish the implementation; do not stop for approval.

## 10. Repository constraints and final report

- Preserve `recursive_gluing` v0 as an untouched control apart from any strictly necessary shared registration/documentation changes.
- Do not edit running campaigns, their state, reporters, verdict gates, or provider-preflight work.
- Do not merge, rebase, or cherry-pick onto `main` or another campaign lineage. Work only on the assigned branch.
- No paid API usage and no external-model campaign runs.
- Prefer a small, correct, fully tested research-valid slice over a sprawling design with unverified semantics.

Run the focused tests, generation smoke tests at shallow and deep settings, exact-oracle cross-checks, and relevant repository tests. Report actual commands and outcomes; do not turn warnings or skipped tests into claims of success.

Commit on the assigned branch and report:

1. branch and commit SHA;
2. files changed;
3. mathematical semantics and completeness justification;
4. concrete SAT and locally compatible but globally unsatisfiable examples;
5. measured input-size/expansion/runtime scaling;
6. baseline comparison results;
7. known limitations and the next experiment needed to establish genuine model-level discovery.

The desired outcome is not “a larger recursive CSP.” It is a controlled, exactly checkable environment where solving the problem through reusable structure is like a 𝖒𝖔𝖙𝖍𝖊𝖗𝖋𝖚𝖈𝖐𝖊𝖗 different from expanding it and treating every occurrence independently.
