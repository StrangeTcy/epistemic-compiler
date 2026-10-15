# Recursive gluing discovery: empirical scaling and benchmark validity

Continue work in `StrangeTcy/rl_eval_generator` on branch `arena/1ddc930c-rl-eval-generator`, starting from commit `ee095ed04c22cd269e1e3e50b58b0d924386c814` or the current branch head if it has advanced. Inspect the branch, working tree, and current tests before changing anything. Preserve work already committed or in progress.

This is a focused validation pass, not a new environment redesign. The current `recursive_gluing_discovery` compact-grammar task and `recursive_gluing` expanded-CSP control are the starting point.

## 1. Objective

Establish, with reproducible measurements, what advantage the compact recursive representation actually provides over explicit unfolding, what it does not provide, and which claims the existing tests support.

The current specification demonstrates exponential growth in the number of expanded occurrences, but depth 12 alone does not establish that expansion is computationally impractical. Furthermore, explicit constraint propagation may solve this particular grammar efficiently on instances whose materialization is still feasible.

Do not conflate these claims:

- **Representation advantage:** a compact grammar and its interface summaries can represent a deep instance without allocating every occurrence.
- **Runtime advantage:** the compact algorithm takes less time than a concrete expanded solver on specified instances.
- **Model-level discovery:** an evaluated model independently finds and implements a useful reusable representation.

Measure the first two. Do not claim the third without running and documenting an actual model evaluation. No external-model runs or API calls are required for this task.

## 2. Build a reproducible scaling experiment

Inspect the existing generator, expansion function, compact oracle, exact CSP solver, and repository testing conventions. Add a standalone script in the repository's appropriate tools or scripts directory, with a deterministic command-line interface.

The script must compare the compact and expanded approaches on matched grammars generated from the same parameters and seeds.

### Compact measurements

For increasing depths, at minimum 3, 6, 12, 24, 48, and 96, record:

- depth and exact number of unfolded occurrences;
- serialized size of the agent-visible grammar;
- time spent generating the grammar;
- compact-oracle runtime;
- number of certificate summary entries and realizable state pairs;
- serialized certificate size;
- peak memory where reliably measurable.

Use the production generator and actual implementation. Do not substitute hard-coded size figures or mock runtimes.

The exact occurrence count is \(2^{d+1}-1\). Validate the formula against actual expansion counts on small instances. Report the dependence of the compact certificate on depth as well as the size of the input grammar: the former grows with the number of summarized depths even though the unfolded tree grows exponentially.

### Expanded measurements

Measure actual materialization at progressively larger feasible depths, starting at 3, 6, 9, and 12. Attempt depth 15 only under a declared memory budget and in an isolated subprocess. Choose safe resource limits based on the existing implementation and environment; do not risk destabilizing the machine or CI.

For each successfully materialized instance, record:

- exact number of occurrences, region/port variables, and overlap constraints;
- serialized expanded size, if serialization is part of the measured operation;
- expansion wall time;
- peak process memory, where supported;
- explicit CSP solver runtime and result for cases that the solver can handle safely.

Do not treat failure to expand under a resource budget as evidence of unsatisfiability. Record it as a resource limit or skipped measurement. Do not use an arbitrarily tiny timeout to manufacture a gap.

Where an instance is too large to materialize safely, report the exact mathematical occurrence and constraint counts separately from empirical measurements. If you extrapolate memory or runtime from measured data, label it explicitly as an estimate and state the assumptions.

Keep the expanded benchmark independent of the compact oracle. The existing shallow expanded solver may be reused as a reference implementation, but it must not call the compact summarization functions to determine its result.

### Measurement methodology

Record the Python version, operating system, measurement method, parameters, and seeds. Use repeated measurements or medians where practical for runtimes. Separate grammar generation, expansion, solving, and certificate verification rather than combining them into one opaque timing.

Timing assertions must not make the test suite flaky across hardware. Tests should enforce semantic and structural invariants; the standalone experiment should report actual performance.

## 3. Report evidence, not just a scaling formula

Add a reproducible scaling report under `docs/decisions/`, updating the existing recursive-gluing design note or creating a dated companion report.

Include a table with measured values for both approaches at every feasible depth, plus exact analytical counts at greater depths. State which cells are measured, skipped, or estimated.

Discuss the results honestly:

- Does the compact grammar remain small relative to the unfolded instance?
- Does the certificate grow linearly with depth for the supported grammar?
- At what measured depth does explicit materialization become meaningfully expensive on the test machine?
- Is the compact algorithm fuckingly faster than the expanded solver on measured cases, or is its demonstrated advantage primarily memory and representation size?
- Which conclusions are robust mathematical properties, and which depend on the implementation and machine?

Do not claim a measured exponential runtime for the explicit solver merely because the number of occurrences grows exponentially. The existing expanded CSP may admit efficient propagation. Distinguish expansion cost from solving cost.

## 4. Strengthen the regression tests

Add focused tests that verify:

1. The exact occurrence-count formula against actual shallow unfoldings.
2. Actual expanded variable and constraint counts agree with formulas derived from the implemented grammar.
3. Compact input size stays substantially below expanded serialized size on matched, measured instances.
4. Compact summaries and certificates have the expected depth-dependent growth and never contain one assignment record per unfolded occurrence.
5. The compact and expanded solvers agree on satisfiability and root interface pairs for shallow instances across all three gluing regimes, both opacity settings, and both ambiguity settings.
6. Presentation-only relabelling preserves the answer.
7. The deep compact oracle completes and produces a valid certificate without materializing the expansion.
8. Expansion budget exhaustion or oracle budget exhaustion is reported as a resource failure, never as `unsat`.
9. The scaling script is deterministic in its inputs, records its configuration, and does not mutate campaign state.

Keep all existing tests. Run the focused discovery suite, v0 suite, generation smoke tests, and relevant integration tests. Report exact commands and outcomes. Do not count a skipped test as a pass.

## 5. Audit experimental claims

While inspecting the code, compare the current implementation with the claims in the design note and repository documentation.

In particular, determine precisely what `label_opacity` changes. The current generator appears to relabel ports by module type; do not describe this as independently relabelling every occurrence unless that is fuckingly implemented and tested. Either implement a compact, semantics-preserving occurrence/rule-level relabelling if it can be done cleanly within the supported grammar, or narrow the documented claim and record per-occurrence relabelling as a remaining limitation. Do not expand the grammar or add complexity just to preserve an inaccurate claim.

Likewise, distinguish the existing implemented tests from future experimental conditions. A written proposal for a canonical-coordinate solver or a model-level evaluation is not evidence that such a condition has been run.

Retain the current supported formal class unless a correctness issue forces a change. If a change is necessary, explain the issue and add corresponding independent correctness tests.

## 6. Scope and repository constraints

- Preserve `envs/cat_theo/recursive_gluing/` as the expanded-CSP control.
- Preserve the existing compact grammar, certificate contract, independent oracle, and agent-facing prompt except where a demonstrated correctness or documentation issue requires a change.
- Do not weaken tests or remove difficult cases to obtain green results.
- Do not modify running campaigns, campaign state, provider-preflight work, reporters, or verdict gates.
- Do not merge, rebase, or cherry-pick onto `main` or another campaign lineage.
- Do not use paid APIs, launch external-model campaigns, or fabricate evidence.
- Commit the results on the assigned branch.

## 7. Final report

Provide:

1. Branch and resulting commit SHA.
2. Files changed and the purpose of each change.
3. Exact test commands and results.
4. The reproducible command for running the scaling experiment.
5. The measured scaling table, clearly separating measurement from analysis or extrapolation.
6. The strongest conclusions supported by the experiment and claims that remain unproven.
7. Any remaining issue with occurrence-level relabelling or other mismatches between the design and implementation.

The deliverable is a more scientifically defensible benchmark with actual scaling evidence. Do not turn this into a larger benchmark, a new theory exercise, or a model campaign.
