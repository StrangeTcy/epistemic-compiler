Conduct a scientific-design audit of the compositional reasoning experiments
in StrangeTcy/rl_eval_generator.

Primary research objective:
Test whether language-model agents can discover and use compact compositional
representations to solve local-to-global constraint problems under recursive
composition, hidden/relabelled representations, and global obstructions—not
merely solve small instances by brute force or exploit surface heuristics.

Review:
1. recursive_gluing_discovery (the primary candidate);
2. recursive_gluing (expanded-CSP control);
3. recursive_holonomy_gluing;
4. recursive_compiler_bootstrap;
5. recursive_error_correcting_codes;
6. recursive_coarse_graining.

Restate the intended structural solution explicitly:
For each module type and remaining depth, compute the relation of realizable
boundary states. Initialize leaf relations from local constraints; recursively
compose child relations through the wiring/transport constraints; apply the
root-closing condition. A global obstruction exists when no realizable root
pair satisfies closure, even though local relations may be nonempty.
This is a proposed algorithmic target, not a claim about model internals.

For each candidate experiment, specify:
- the exact hypothesis and observable evidence that would support or falsify it;
- the competing explanations: brute force, generic solver synthesis, memorized
  domain algorithms, surface cues, and genuine compositional generalization;
- paired contrasts and whether they isolate the intended variable;
- positive and negative baselines, including an exhaustive baseline where
  feasible and a compact compositional reference solver;
- held-out generalization tests and a depth/size scaling analysis;
- exact metrics, including certificate correctness, false SAT/UNSAT results,
  and resource use;
- threats to construct validity, confounds, ceiling/floor effects, and
  what conclusions would remain unjustified;
- a concrete go/no-go criterion for spending model calls on a pilot.

Explicitly distinguish:
A. implementing a known formal algorithm;
B. generalizing a compositional algorithm to new instances;
C. transferring a structural principle across task domains;
D. discovering a sheaf-theoretic interpretation or internal concept.

Do not imply that success at A–C establishes D.
Do not treat removal of theory vocabulary as evidence that the underlying
structure is hidden.
Do not call direct-vs-recursive an isolated structural contrast when other
factors change.
Do not call the four-app suite one coherent construct without evidence.

No model calls, API calls, environment changes, or new tests in this task.
Inspect existing artifacts and produce a review at
docs/audits/2026-10-18-compositional-experiment-design.md.

End with a concrete recommended experiment matrix, the remaining blockers
that affect validity (not just logistics), and the smallest [d-word] pilot.
