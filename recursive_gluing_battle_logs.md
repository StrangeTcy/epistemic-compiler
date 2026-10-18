some model:

Here is the adversarial design review and recommended minimal redesign for the recursive gluing environment, structured precisely to the requested final deliverable format.

***

# Adversarial Design Review: Recursive Gluing Environments

## 1. A concise reconstruction of the target capability
The core construct is the ability of an agent to do two distinct things in sequence:
1. **Generating-mechanism recovery:** Deduce an unstated, stateful recursive invariant (the rules governing how properties like orientation, exit sealing, and edge-reuse transform across recursive tile boundaries) strictly from observable evidence, such as logs of valid and invalid paths on small instances. 
2. **Compositional generalization:** Formulate a structurally sound strategy (e.g., a bottom-up summary of realizable boundary-state pairs, or a memoized recursive solver) that correctly predicts global satisfiability for deeply nested structures (depths 6+). 

Success means the agent recognizes that naive "gluing" (assuming that locally solvable child tiles imply a solvable parent) fails due to state mismatches, and successfully applies a compositional algorithm to instances where explicit flat search (BFS/DFS) is computationally intractable.

## 2. The strongest criticisms of the current environment(s)
*   **`recursive_maze_gluing` fails mechanism hiding and scaling:** The agent prompt explicitly hands the model the rules ("nesting, XOR orientation, sealing"). This reduces the task to reading comprehension and basic search. Furthermore, at depths 1–3, the state space does not strictly require a compositional summary; a generic, unfolded BFS/DFS can easily solve it, failing to distinguish brute force from compositional reasoning.
*   **`recursive_gluing_discovery` fails mechanism hiding:** While it successfully scales to depth 12 and forces a compositional approach, the prompt explicitly specifies the grammar, the recurrence semantics, and the exact boundary-pair certificate format. It tests the ability to *implement* a mathematically specified algorithm, not the *discovery* of the recursive invariant.
*   **Sibling tasks are unearned confounds:** `recursive_holonomy_gluing`, `compiler_bootstrap`, etc., cannot be treated as cross-domain replications without empirical evidence that they isolate the exact same capability. Keeping them active in the initial validation phase adds noise, introduces uncontrolled variables, and distracts from validating the core recursive maze construct.

## 3. An experiment matrix separating factors, controls, and confounds
To rigorously prove the capability, the benchmark must separate the following dimensions in a 2-phase experiment (Discovery -> Test):

*   **Factor 1: Depth (Scale Control)**
    *   *Small (Depths 1-2):* Used strictly for providing observable trace logs. Flat search is viable here.
    *   *Deep (Depths 6-10):* Used for evaluation. Unfolded trees grow exponentially; flat search must provably timeout or OOM.
*   **Factor 2: Instance Pairing (Global Obstruction Control)**
    *   *SAT / UNSAT Pairs:* At deep levels, test cases must be generated in pairs. Both instances use the exact same base tiles and nesting structure, differing by only a single edge in a deep child that preserves local pathing but flips the global return-state parity (rendering the root UNSAT). 
*   **Factor 3: Competitor / Confound Baselines**
    *   *Naive Local Gluing:* Returns SAT if every unique tile type has at least one valid internal path.
    *   *Context / Brute-force Limit:* A generic Python BFS solver. 
    *   *Trivial Heuristics:* "Always SAT", "Always UNSAT", "Random".

## 4. The minimal redesign recommendation and concrete code-level changes
**Recommendation:** Merge the implicit mechanism of `recursive_maze_gluing` with the depth scaling of `recursive_gluing_discovery`. We will use a **Trace-to-Solver** architecture. 

**Priority-ordered code changes:**
1.  **Modify `recursive_maze_gluing` prompts:** Strip all explicit mentions of XOR, orientation, and sealing. Replace the prompt with a purely operational goal: *"Write a Python function `evaluate_maze_sat(maze_spec)` that returns True/False."*
2.  **Build a Trace Logger (Phase 1 Evidence):** Create a script that generates a text file of "Explorer Logs." These logs show step-by-step traces of agents successfully navigating—and fatally failing—in depths 1 and 2 mazes. The model must read these traces to infer the hidden state constraints.
3.  **Upgrade the Generator for Matched Deep Pairs:** Modify the `recursive_maze_gluing` generator to output depths 6, 8, and 10. Write an adversarial pairing function that takes a SAT instance, isolates a critical edge, and toggles it to break global parity without breaking local tile pathing.
4.  **Quarantine sibling applications:** Exclude the four sibling environments from the Arena pipeline until the core maze construct passes validation. 

## 5. Adversarial regression tests and baselines
Before evaluating an LLM, the environment must automatically run these tests against its own generated test sets:
*   **The Brute-Force Rejection Test:** Run an explicit flat BFS against depths 6, 8, and 10. *Success criterion:* It must deterministically hit a compute/timeout limit, proving the instance cannot be solved by a lazy LLM writing a generic search script.
*   **The Naive Local Glue Rejection Test:** Run a solver that checks only if `start -> end` exists in each isolated tile type. *Success criterion:* It must predict SAT for both halves of the paired instances, scoring exactly 50% on the evaluation set. 
*   **The Reference Oracle Test:** Ensure the repository's provided bottom-up boundary-pair algorithm evaluates depths 6, 8, and 10 correctly in under 2 seconds.
*   **Leakage Scan:** Grep the final prompt and trace logs to ensure terms like `orientation`, `XOR`, `parity`, `sheaf`, and the test-set random seeds are entirely absent.

## 6. A pre-model go/no-go checklist
Do not execute Astra API calls until these conditions are met locally:
- [ ] Are depths 1–3 entirely removed from the testing/evaluation phase?
- [ ] Are test instances generated in strictly matched SAT/UNSAT pairs based on a single localized recursive obstruction?
- [ ] Does a standard flat-BFS script definitively fail/timeout on the evaluation test set?
- [ ] Can a human engineer logically deduce the sealing/orientation mechanics strictly by reading the Phase 1 trace logs, without looking at the Python generator code?
- [ ] Is the model forced to output a runnable Python script (enabling exact evaluation of their generalized algorithm) rather than just guessing "SAT" or "UNSAT"?

## 7. What a successful pilot would not prove
If the model correctly infers the rules from the traces, synthesizes a dynamic-programming solver, and achieves high accuracy on depth 10 paired instances:
*   It **would not prove** that the model has an internal representation of sheaf theory, global sections, or algebraic topology. 
*   It **would not prove** that the model can structurally transfer this compositional reasoning to mathematically homologous but functionally distinct domains (like error-correcting codes). 
*   It **would prove only** that the model possesses highly advanced in-context deductive reasoning to infer a discrete, stateful recursive invariant from raw trace data, and possesses the algorithmic synthesis capabilities to implement a memoized solution for an exponentially unfolding structure.


&&&&&&&&&&&&&&&&&&&&&&&


some other model:

I'll start by inspecting the repository structure and the key environment code referenced in the brief.I'll inspect the specified branch and the cat_theo recursive environments next.Focusing on the recursive maze and related gluing environments' file structure and core code.Fetching the core maze and discovery source files now.Fetching the remainder of maze `network.py` and the discovery environment sources.Continuing with generator logic and the sibling/control environments.Examining maze tests and analyzing the obstruction mechanism in detail.# Design-review report: recursive gluing / nested-tile environments

**Branch:** `arena/1ddc930c-rl-eval-generator` @ `cc945530…`  
**Primary code:** `envs/cat_theo/recursive_maze_gluing/`  
**Comparators:** `recursive_gluing_discovery/`, `recursive_gluing/`, four sibling apps  
**Recent audit:** `docs/audits/2026-10-17-four-apps-evaluation-readiness.md` (commit `0dcb51cb…`)  
**No model API calls; claims trace to inspected sources and tests.**

---

## 1. Concise reconstruction of the target capability

### Intended construct (own words)

An agent faces a **concrete, self-similar nested system** whose local pieces look solvable. Correct behavior requires recovering a **non-Boolean interface summary**: which boundary behaviours a recursive component can realize (entry/exit states, orientation or other finite state, sealing/history, edge-use if binding), then composing those summaries so that **local feasibility does not imply global feasibility**. The failure of naive “glue every local solution” must be **principled and inspectable**, not a hidden rule or typo.

### Capability levels (must stay separate)

| Level | Claim | What counts as evidence |
|------|--------|-------------------------|
| **1. Explicit solving** | Produce a valid route/assignment on a fully specified finite instance | Independent replay/oracle accepts certificate |
| **2. Compositional generalization** | Recover a reusable recurrence/summary and apply it at held-out depths/structures | Depth scaling + held-out production patterns; compact cert preferred over unfolded search |
| **3. Generating-mechanism recovery** | Infer the non-obvious rule that explains recursive behaviour from public evidence | Success after **withholding** the algorithm/invariant while providing recoverable evidence (examples, tools, structured instances) |
| **4. Structural transfer** | Same principle in a genuinely different presentation/domain | Only with an explicit shared hypothesis and matched controls—not “also recursive” |
| **5. Internal concepts** | Model “has” sheaf/holonomy/etc. | **Not** established by task accuracy |

### Ambiguity in the current suite (must not be silently merged)

Three different tasks are currently conflated:

1. **Specified recursive object → implement solver** (`recursive_maze_gluing` prompt fully states nesting, XOR, sealing, edge-use; agent returns a route).
2. **Specified compositional algorithm → emit DP certificate** (`recursive_gluing_discovery` prompt defines productions, wiring, and the exact realizable-pair certificate).
3. **Latent mechanism recovery** (research brief target)—**not operationalized** anywhere as a distinct phase.

**Clean operationalization (recommendation):**

- **Primary program:** maze-centered **Level 1 + Level 2**, with a **thin Level-3 probe** only after Level 2 is hard enough that brute force is not the dominant explanation.
- **Do not** claim Level 3 from the current maze or discovery prompts: both **name the operational rules and the intended compositional form**.
- **Use discovery** as a **positive control / oracle architecture** (compact summary soundness, depth scaling), not as the discovery task.
- **Defer Level 4** (siblings) until one maze construct is validated; do not treat siblings as replications.
- **Never** claim Level 5 from accuracy.

**Falsifiable central hypothesis for the redesign:**

> *H₁:* Agents that only locally glue (Boolean “child solvable,” ignore orientation/interface, copy leaf tables upward, or unfold-BFS only at small depth) fail on matched SAT/UNSAT pairs whose difference is a **recursive interface obstruction**, while agents that maintain a sufficient boundary relation succeed at depths where unfolded search is resource-dominated.

---

## 2. Strongest criticisms of the current environment(s)

### 2.1 `recursive_maze_gluing` — useful harness, wrong scientific claim

**Files:**  
`envs/cat_theo/recursive_maze_gluing/config.yaml`, `files/prompt.md`, `files/network.py` (`generate_maze`, `shortest_route`, `replay_route`, `build_grade_mazes`, `arm_ignore_orientation`), `files/judge.py`, `files/solver.py`, `tests/test_recursive_maze_gluing.py`.

#### A. Prompt already gives the mechanism (blocks Level 3)

`files/prompt.md` explicitly teaches:

- local room names  
- XOR orientation on edges/shafts  
- descend/ascend and `nesting["deeper"]`  
- root exit sealed until one child completed  
- directed edges used at most once per nested copy  
- sat/unsat route format  

That is **Level 1 specification**, not latent-mechanism recovery. Renaming “holonomy” away is already done; the **algorithmic content remains in ordinary language**.

#### B. The global obstruction is not recursive composition

In `generate_maze` (`network.py`):

```text
cycle_flip = 1 if regime == CYCLIC_UNSAT else 0
keep path (cyclic): dock → ra → rb(flip=cycle_flip) → rc → door
inner_keep: always tree edges, all flip 0
crypt: flip 0
start_orientation = goal_orientation = 0 always
```

For `CYCLIC_UNSAT`, the unique entrance→exit corridor on **root `keep`** has XOR parity 1, so exit orientation ≠ goal. Nesting only enforces **sealing** (must descend once); child walks do not flip. So:

- Local tiles “have edges” (test `test_regimes_and_local_tiles_walkable` only checks nonempty rooms/edges).
- UNSAT is **root path parity**, not “composed child interfaces fail to close.”
- Depth 1/2/3 changes nest count, **not** the nature of the obstruction.

This fails the brief’s core target: *naive local gluing fails for a principled recursive reason*.

#### C. Depths 1–3 do not force compositional reasoning

- Config: easy/medium/hard → depth 1/2/3 only (`config.yaml`).
- Oracle: BFS over `(stack, room, orientation, cleared, used edges)` with `max_nodes=50_000` (`shortest_route`).
- Tile graphs are tiny (≤5 rooms, few edges, one primary shaft line).

A generic explicit search that mirrors the prompt **is the intended correct algorithm at these sizes**. That is fine for Level 1, fatal for claims of Level 2/3 necessity.

#### D. Grade suite does not isolate “local SAT, global UNSAT via recursion”

`build_grade_mazes`:

| Check | What it actually tests |
|--------|-------------------------|
| `local_visible` | Trivial one-corridor maze (`example_visible_maze`) |
| `configured` | One seed of the axis combo |
| `assembled_sat` / `assembled_unsat` | Regime flip on **same generator family**, not matched recursive interface pair |
| `opaque_twin` | Relabel of configured (presentation) |
| `decoy_heldout` | Extra `pit` shaft (local distractor with flip 1 on pit path) |
| `deterministic` | Double call |

Missing:

- Paired instances with **identical child tiles** and **identical parent topology**, differing only in a recursive closing/composition constraint that creates SAT vs UNSAT.
- Held-out **production patterns** (only one hand template: keep / inner_keep / crypt [/pit]).
- Depth sweep with fixed regime/labels.
- Resource metrics (nodes, steps, time).
- Separation of false-SAT vs false-UNSAT in scoring (accuracy over 7 binary checks only).

#### E. Baselines present but weak relative to the claim

- Stub `solver.py`: first-edge heuristic; passes visible tests only.
- `arm_ignore_orientation`: zeros flips, then BFS — correctly fails `assembled_unsat` (`test_grade_reference_beats_baseline`).
- **No** baseline that implements full prompt-faithful BFS (would pass everything at d≤3).
- **No** “Boolean child-solvable glue” baseline that is the brief’s main foil.
- **No** measurement of where BFS becomes infeasible.

#### F. Self-similarity is thin

- Only `inner_keep` repeats; structure is a **spine of nested keeps**, not a branching self-similar family with nontrivial interface algebra.
- `cleared` is a single root bit (one descend anywhere unseals)—not per-copy sealing history that interacts with recursion depth.
- Edge-use is tracked but the generator barely stresses it (almost unique paths).

**Diagnosis (agrees with brief, confirmed in code):** closest prototype and solid correctness harness; **closer to “solve a fully specified small recursive maze” than “recover a hidden generating mechanism.”** Depths permit composition; they do not force it; obstruction is not the intended recursive one.

---

### 2.2 `recursive_gluing_discovery` — excellent compact control, not discovery

**Files:** `files/prompt.md`, `files/network.py` (`generate_grammar`, `compact_summaries`, `compose_branch`, `build_grade_grammars`, `arm_copy_leaf_upward`, `measure_scaling`).

**What it tests well (Level 2 implementation):**

- Compact grammar; depths 3/6/12; unfolded size \(2^{d+1}-1\).
- Oracle never materializes the tree; bottom-up realizable pairs (`compact_summaries`) — sound/complete **for this serial binary grammar** (stated in docstring).
- Certificate demands **exact** realizable tables + root closing (`verify_certificate`).
- Naive foil `arm_copy_leaf_upward` exists.
- `heldout_twist` (`mid_delta=1`) and scaling harness exist.
- Expanded CSP cross-check capped at depth 4 (`MAX_EXPAND_DEPTH`).

**What it does *not* test:**

- Mechanism recovery: prompt **defines** leaf/branch, productions, wiring, closing, and the full certificate shape.
- Maze-shaped route semantics (no sealing, edge-use, walk replay).
- Name “discovery” is misleading relative to the brief.

**Role:** keep as **positive control** and **oracle/DP reference pattern** for a maze redesign; optional Phase-B “implement the summary you inferred” only after a true inference phase. Do not call it the main nasty self-similar task.

---

### 2.3 `recursive_gluing` (expanded CSP)

**Prompt:** region domains + overlap pair tables; nested ids cosmetic.

**Valid control only for:** “same underlying constraint network, expanded vs compact presentation” **if** instances are **literally dual** to discovery (or maze) grammars. Today it is a **sibling CSP env**, not a demonstrated dual of the maze.  
**Do not assume** control relationship from the name. Use it only after a generator emits matched expanded/compact pairs and tests prove answer identity.

---

### 2.4 Four sibling apps — not replications of the maze construct

From prompts + readiness audit (`docs/audits/2026-10-17-four-apps-evaluation-readiness.md`):

| Env | Surface problem | Shared with maze? |
|-----|-----------------|-------------------|
| `recursive_holonomy_gluing` | Fixed point of composed finite maps on cycle | Finite state + composition; **not** nested route sealing/edge-use |
| `recursive_compiler_bootstrap` | Compile/recode equivalence claim | Pipeline composition; confounded direct/recursive |
| `recursive_error_correcting_codes` | Local kernels + glues + parent check | Local-vs-global linear constraints |
| `recursive_coarse_graining` | Integer series tables + fixed under doubling | Bottom-up summary; 2-spin toy |

Audit already records: **model performance unmeasured**; `direct` vs `recursive` confounds structure with polarity; `recursive` vs `recursive_composition` is polarity on matched shape; `flat` not selectable; compiler depth saturates at 2; coarse depth honesty issues.

**Construct-level verdict:** useful as **analogies** for “local OK, global fail,” **not** cross-domain replications of recursive maze gluing. **Do not expand them in this redesign.** Prefer one coherent maze experiment.

**Note:** `174 passed` is generator/oracle/shortcut unit evidence only—audit says so; do not treat as capability.

---

## 3. Experiment matrix (factors, controls, confounds)

| Factor | Levels | Isolates | Confound if mixed |
|--------|--------|----------|-------------------|
| **F1 Depth** | 1,2,3,4,6,(8+) | Recursive work / need for summary | Changing regime or template with depth |
| **F2 Regime / polarity** | SAT twin / UNSAT twin | Global obstruction | Different local generators |
| **F3 Presentation** | transparent / opaque relabel | Label invariance | Different edges/flips |
| **F4 Ambiguity** | clean / decoy child | Distractor discrimination | Polarity change |
| **F5 Interface richness** | orient only vs orient+edge-use vs multi-bit state | Summary sufficiency | Graph size explosion |
| **F6 Evidence regime** | full ops prompt vs ops+examples vs interaction tools | Level 1 vs 3 | Hiding rules without recoverable evidence |
| **F7 Certificate type** | route steps vs compact boundary tables | Search vs composition | Requiring both without phase split |

**Primary contrasts (clean):**

1. **Matched-local SAT/UNSAT:** same tiles/edges/shafts; only recursive closing or interface composition differs → global SAT flips.  
2. **Depth ladder:** fixed generator rules, fixed polarity family, measure accuracy **and** cost.  
3. **Opaque twin:** same latent maze, relabelled rooms.  
4. **Summary ablation baselines:** ignore orientation; Boolean child-sat glue; copy-local-route; full BFS; compact DP reference.

**Confounds to forbid in claims:**

- `assembled_unsat` that only flips one root edge parity (current maze).  
- Scoring depth while changing regime.  
- Calling siblings “transfer” without shared interface hypothesis.  
- Prompt that states the DP recurrence while claiming “discovery.”

---

## 4. Minimal redesign recommendation and concrete code-level changes

### 4.1 Primary design (one coherent task)

**Name (internal):** strengthen `recursive_maze_gluing` only.  
**Agent-facing:** keep “nested tile routes” framing; **no** sheaf/holonomy/gluing theory words (already mostly clean).

**Phase structure (smallest coherent experiment):**

1. **Phase M (main grade):** Fully specified operational rules (current style) + **harder recursive obstruction** + depth where BFS cost diverges from compact summary. Certificate = **route** (Level 1) **and/or** optional compact interface table checked independently (Level 2).  
2. **Phase I (optional, later):** Same generator; withhold composition recipe; give small worked examples / probe tool; require mechanism-consistent behaviour on held-out depths (Level 3). **Not** in first pilot.

**Do first:** fix obstruction + depth + matched pairs + baselines on Phase M.  
**Do not first:** four new envs, cryptic prompt without evidence, or sibling “replications.”

### 4.2 What must be preserved in the interface summary (checked against route semantics)

Exact route state in oracle today:

`state = (tile_stack, room, orientation ∈ Z/2, cleared_root, used_edges)`

A **sound complete compact summary** for composition is **not** Boolean solvable. Minimally, for each tile type and remaining depth \(k\):

> **Realizable boundary behaviours**  
> \( R(t,k) \subseteq \)  
> (entry_orient × exit_orient × cleared_needed? × …)  
> subject to edge-use **within** one copy.

More precisely, propose and **prove against `replay_route`**:

- For a copy of type \(t\) entered with orientation \(o_{in}\), remaining depth \(k\),  
  the set of achievable \((o_{out}, \mathsf{did\_clear\_child}, \mathsf{edge\text{-}multiset\ constraint})\) when standing at exit ready to ascend (or at root exit).

**Why Boolean fails:** parent needs a specific exit orientation (and sealing). A child may be entrance→exit walkable yet only realize \(o \mapsto o\oplus 1\), breaking parent goal; or edge-use in parent may forbid the only child entry that realizes the needed map.

**Current generator does not stress this:** children are orientation-identity; only root flip breaks SAT. **Must change generator**, not only prompt.

**Sufficiency test (code):**  
Implement `compact_maze_summaries(maze)` and assert for many seeds:

`grammar_sat_from_summaries == maze_satisfiable`  
and every summary-predicted root witness extends to a `replay_route`-valid path (or unsat both sides).

If edge-use within small tiles makes pure orient-pair summaries incomplete, **either** enlarge state in summary **or** redesign tiles so edge-use is non-binding at the interface (document which).

### 4.3 Generator redesign (core)

**File:** `envs/cat_theo/recursive_maze_gluing/files/network.py` → `generate_maze`

**Replace single root `cycle_flip` obstruction with recursive interface obstruction**, e.g. one of:

**Preferred minimal mechanism (keep Z/2):**

- Every **leaf** (`crypt`) realizes a fixed nontrivial map \(o \mapsto o \oplus 1\) (or a configurable leaf_delta).  
- Each nested `inner_keep` must descend exactly once (sealing) before exit; shaft flip 0; parent path otherwise identity.  
- Root goal \(o_{out}=o_{in}\).  
- Then total flip count = number of leaf visits along the forced spine = depth (or \(2^{d}\) if branching).  
- **SAT regime:** goal matches parity of forced leaf count; **UNSAT:** goal mismatches **or** closing requires even parity while depth forces odd.  
- **Matched pair:** identical tiles/edges/shafts; only `goal_orientation` (or one closing constraint) differs → SAT vs UNSAT. Locals unchanged.

**Stronger (still small):** branching shafts (two children) with different leaf maps; parent mid-corridor requires composing left then right maps; UNSAT when composition ≠ required holonomy, while each child alone is walkable.

**Keep:** decoy `pit` with different flip table; opaque relabel; sealing; edge-use.

**Depth axis:** extend config to **1,2,3,4,6** (hard ≥6). Measure oracle BFS nodes vs compact summary time (mirror discovery’s `measure_scaling`).

**Held-out production:** at least two templates (spine vs binary branch) with **disjoint seeds** for grade vs visible demos; one held-out pattern only in judge.

### 4.4 Prompt / certificate (Phase M)

**File:** `files/prompt.md`

- Keep operational rules (fair Level 1).  
- Strengthen “what correct means”: every child can have an entrance→exit walk while root still fails **because composed orientation/sealing constraints conflict**—without naming theory.  
- Optional second output mode (config flag): require `interfaces` tables per type/depth (discovery-style) **in addition to** or **instead of** full route at high depth—checked by independent compact oracle.

**Do not** strip rules until Phase I; stripping without examples = guessing game (brief forbids).

### 4.5 Judge / grade

**Files:** `files/judge.py`, `build_grade_mazes`

Replace/extend checks:

1. `local_visible` — trivial (keep)  
2. `configured`  
3. `matched_sat` / `matched_unsat` — **identical locals**, polarity twin  
4. `depth_heldout` — depth not equal to configured (e.g. configured 3, held-out 6) same rules  
5. `opaque_twin`  
6. `decoy_heldout`  
7. `pattern_heldout` — second template  
8. `deterministic`  
9. Metrics: `false_sat`, `false_unsat`, `bfs_nodes_ref`, `agent_step_count` if exposed  

Scoring: report SAT-error and UNSAT-error separately; do not only average 7 booleans.

### 4.6 Baselines (must land in `network.py` + tests)

| Arm | Expected |
|-----|----------|
| `arm_reference` BFS | all pass (until depth budget) |
| `arm_compact_summary` | all pass; scales past BFS |
| `arm_ignore_orientation` | fails matched_unsat |
| `arm_boolean_child_sat` | fails matched_unsat / depth cases |
| `arm_first_edge` (stub) | only local_visible |
| `arm_local_route_template` | fails decoy / opaque / held-out pattern |

### 4.7 Discovery / CSP / siblings

| Component | Action |
|-----------|--------|
| `recursive_gluing_discovery` | **Keep unchanged** as compact-oracle control; optionally import summary ideas into maze judge; **no** claim it is discovery |
| `recursive_gluing` | Defer; only wire as expanded dual if maze summaries expand to CSP with proof of equivalence |
| Four siblings | **No code changes** for this program; audit already sufficient; not in pilot matrix |

### 4.8 Priority-ordered code changes

| Pri | Change | Intended effect | Refutation test | Success look like |
|-----|--------|-----------------|-----------------|-------------------|
| **P0** | Rewrite `generate_maze` obstruction to recursive interface parity/composition; add `matched_sat/unsat` builders | Global fail only after composition | `test_matched_pair_identical_locals`; boolean-glue arm fails unsat, ref passes | Locals equal; SAT differs; ignore-orient or boolean-glue fails |
| **P0** | Prove/test compact summary vs `maze_satisfiable` / `replay_route` | Sound interface invariant | Random seeds d=1..6, both regimes | Exact agreement; witness routes replay |
| **P1** | Depth levels 1..6 in `config.yaml`; `measure_scaling_maze` | Force composition vs BFS | BFS hits `OracleBudgetExceeded` or huge nodes at d≥6 while compact finishes | Clear crossover depth |
| **P1** | Grade matrix + false SAT/UNSAT metrics in judge | Interpretable outcomes | Unit test on foil arms | Foils fail the right cells |
| **P2** | Second held-out tile template | Template non-memorization | Agent/oracle with only template A fails pattern B if hardcoded | Ref passes both |
| **P2** | Optional interface certificate path | Level-2 signal | Exact match to compact oracle | Discovery-like cert without renaming maze |
| **P3** | Phase I evidence protocol (examples tool) | Level 3 | Withhold rules; only examples; still recoverable | Documented recovery procedure passes human pilot |
| **Defer** | Sibling edits, CSP dual, theory-name games | — | — | — |

---

## 5. Adversarial regression tests and baselines

Add to `tests/test_recursive_maze_gluing.py` (and keep existing depth-guard tests):

1. **`test_unsat_is_not_root_only_parity`**  
   For matched UNSAT, zeroing only root edge flips still UNSAT **or** document that obstruction lives in leaf/composition counts—not a single root flip.

2. **`test_matched_pair_same_tiles`**  
   Deep equality on `tiles`/`nesting`; only goal or closing differs; SAT xor.

3. **`test_each_local_tile_entrance_exit_walk_exists`**  
   Stronger than nonempty edges: each type has some entrance→exit walk ignoring parent goal (BFS in isolation).

4. **`test_boolean_glue_fails_matched_unsat`**

5. **`test_compact_summary_agrees_with_bfs`** for d≤4 and compact-only for d≥6.

6. **`test_bfs_budget_grows_with_depth`** / crossover.

7. **`test_ignore_orientation_false_sat_on_unsat`**

8. **`test_opaque_preserves_sat_and_route_replay`**

9. **`test_decoy_pit_not_required_on_sat_spine`** (already partially there)

10. **`test_no_theory_tokens_in_workspace`** (extend like four-app audit to all selectable axis combos)

11. **`test_grade_seed_not_in_visible_tests`**

12. **Shortcut: static template** hardcode depth-1 crypt route → must fail d=3/6 and held-out pattern.

**Null explanations to kill before any model pilot:**

- Small-instance BFS (measure crossover).  
- Parity of a single visible root edge (redesign obstruction).  
- “All cyclic_unsat → unsat” regime keyword leakage (judge-only strings; agent payload has no regime name—verify `public_maze` keys only).  
- Seed/path leakage (`generation.json` not in agent image—confirm like audit).  
- Label heuristics (opaque twin).  
- Memorized one template (second pattern).

---

## 6. Pre-model go/no-go checklist

Do **not** run Astra/model scoring until **all** of the following are true:

- [ ] **H₁** written in repo doc pointing at maze only; siblings excluded from claim.  
- [ ] Matched SAT/UNSAT pairs: identical locals; composition-level obstruction; unit tests green.  
- [ ] Compact summary proven/tested sound & complete vs route semantics for the generator family.  
- [ ] Depth ladder includes ≥ one depth where reference BFS exceeds budget or \(>10\times\) compact cost; compact still correct.  
- [ ] Baselines: boolean-glue, ignore-orient, stub, template — **fail** the cells theory says they must fail; reference **passes**.  
- [ ] Grade matrix separates false-SAT / false-UNSAT; held-out depth + held-out pattern + opaque.  
- [ ] Agent workspace: no regime/SAT labels, no theory tokens, no `%%` leftovers, public keys only (`PUBLIC_KEYS`).  
- [ ] Visible tests ≠ judge seeds/templates.  
- [ ] Prompt still states **operational** move/descend rules (fairness) but does **not** hand the compact recurrence or “compute realizable pairs” recipe unless Phase-2 cert is explicit.  
- [ ] Human dry-run: author can solve one hard instance with summary reasoning and exhibit a boolean-glue failure case.  
- [ ] No credentialed model call used to “tune” the benchmark.

**Go:** pilot on Phase M only, small N, log traces, compare to baseline arms’ expected failure profile.  
**No-go:** if BFS still solves all grade depths cheaply **and** obstruction is still single-edge parity.

---

## 7. What a successful pilot would not prove

- That the model **recovered a sheaf / holonomy / cohomology concept**—only that it produced routes or summaries compatible with a compositional interface discipline on this generator.  
- That it **discovered a latent generating mechanism** if the prompt still fully specifies nesting, XOR, sealing, and edge-use (Level 1–2 at best).  
- That success is **not** “implemented the BFS described in the prompt” unless depth/cost controls show BFS is non-viable and/or compact cert is required.  
- **Transfer** to compilers, codes, coarse-graining, or holonomy apps.  
- That **unit-test green** or **174 passed** equals model capability or construct validity.  
- That opaque labels equal conceptual difficulty.  
- That UNSAT answers reflect understanding rather than refusal/heuristic without false-SAT pressure from matched twins.  
- Any claim about internal representations without separate probing.

---

## Round-style synthesis

### Points of agreement (with the research brief, confirmed on code)

- Maze should stay center; siblings are not automatic replications.  
- Current maze is a correctness harness, not a mechanism-recovery benchmark.  
- Discovery is compositional-algorithm implementation, valuable as control.  
- Boolean child-sat is the right conceptual foil; depths must matter; matched locals matter.  
- No model calls until design gate passes.

### Substantive tensions resolved here

| Tension | Resolution |
|---------|------------|
| Infer mechanism vs implement specified solver | **Phase M first** (specified ops, hard composition); Phase I later |
| Route cert vs pair cert | Routes for semantics fidelity; add compact interface cert when depth kills BFS |
| Hide names vs hide concepts | Keep ops explicit; hide **invariant/algorithm**, not the physics of move/descend |
| Use four apps? | **No** for primary validity |

### Recommended primary design

**One env: hardened `recursive_maze_gluing`** with recursive interface obstruction, matched SAT/UNSAT, depth crossover, compact-summary oracle, adversarial baselines.  
**Rejected:** multi-env expansion; discovery-as-main; cryptic prompt without evidence; treating four apps as the construct.

### Deferred

Phase I interaction-based mechanism recovery; CSP dual; sibling unification; multi-bit non-Z/2 state families beyond what’s needed for H₁.

### Why the first pilot is informative if the gate passes

If boolean-glue and ignore-orient fail matched UNSAT while models pass only at low depth and collapse where BFS is impossible unless they emit correct interface behaviour, you get a **clean Level 1–2 measurement**. If models pass high depth with short traces and correct compact structure, you get a signal worth a Phase I redesign. If they pass via prompt-faithful BFS at all graded depths, the gate failed and you raise depth/branching before any claim.

---

### Immediate next engineering step (when you authorize a patch)

Single reviewable PR scoped to **P0+P1 only**:

1. `network.py`: new `generate_maze` + matched pair + compact summary + baselines + scaling.  
2. `config.yaml`: deeper depth levels.  
3. `judge.py` / `build_grade_mazes`: new checks + error split metrics.  
4. `tests/test_recursive_maze_gluing.py`: tests in §5.  
5. Short `docs/audits/…-maze-redesign.md` stating H₁ and non-claims.

**No** sibling edits; **no** model scoring in that PR.

---

**Bottom line:** The repository already has a serious oracle/judge skeleton and an honest four-app audit. The maze’s scientific failure mode is specific and fixable: **the prompt specifies the mechanics, the depths are BFS-trivial, and the UNSAT bit is a root XOR, not recursive interface composition.** Fix that obstruction and the evaluation matrix before any Astra run; keep discovery as the compact-reasoning control; leave the four siblings out of the primary claim.


&&&&&&&&&&&&&&&&&&&


some model #3:

I'll start by inspecting the repository structure and the key environment code on the specified branch.Fetching the repository tree and key paths on the target branch.Exploring the cat_theo environments and the recursive maze gluing code.Inspecting `recursive_maze_gluing` and related environment files.Fetching core maze gluing source files and configs.Pulling the maze implementation files next.Fetching the remainder of `network.py` and the discovery environment sources.Inspecting discovery prompt/network and sibling environments.Gathering more implementation details, tests, and sibling-task structure.Examining generator regimes, tests, and whether maze SAT/UNSAT pairs are locally matched.Checking maze tests and whether orientation obstruction depends on depth.# Adversarial design review: recursive gluing / nested-tile environments

**Branch:** `arena/1ddc930c-rl-eval-generator`  
**Primary code reviewed:**  
`envs/cat_theo/recursive_maze_gluing/`, `recursive_gluing_discovery/`, `recursive_gluing/`, sibling four-apps + `docs/audits/2026-10-17-four-apps-evaluation-readiness.md`  
**Commit context:** four-app correction `0dcb51cbfa35598fa843905c3384d93a5fc95a71` (does not change maze/discovery).

No model API calls. Claims below are from inspected generators, prompts, judges, oracles, and unit tests.

---

## 1. Concise reconstruction of the target capability

### Intended construct (in operational terms)

An agent faces a **self-similar, recursively nested concrete system** (centered on the recursive maze) in which:

- every local piece can look walkable / table-nonempty;
- composing those pieces under nesting, state transport, sealing, and a root goal can still make a global solution impossible;
- a Boolean “child solvable” summary is **incomplete**;
- the right reusable account is a **finite interface relation** (which entry/exit boundary behaviours a component can realize, indexed by remaining depth and any necessary finite state);
- that account is **inferable from public evidence**, not named as sheaf/holonomy/gluing theory and not handed over as “implement this DP.”

### Five claim levels (must stay separated)

| Level | Claim | What counts as evidence |
|---|---|---|
| **1. Explicit solving** | Produce a valid route/assignment on a fully specified finite instance | Route replay / assignment check against independent semantics |
| **2. Compositional generalization** | Recover a reusable interface summary/recurrence; apply across depths and held-out instances | Correct compact certificates + depth scaling where unfold/BFS fails; held-out seeds/patterns |
| **3. Generating-mechanism recovery** | Infer the non-obvious rule explaining recursive behaviour from instances/examples/tools/traces—not from a recipe in the prompt | Success after rules are under-specified *as algorithm*, with enough interaction/evidence; failure of “read the prompt and code the stated recurrence” |
| **4. Structural transfer** | Same principle in a genuinely different presentation/domain | Cross-format transfer with matched latent task; **not** “also has recursion” |
| **5. Internal concepts** | Model “has” sheaf/holonomy concepts | **Not** established by task accuracy; needs separate probes |

### Ambiguity in the current suite — and a clean operationalization

| Environment | What it actually tests today |
|---|---|
| `recursive_maze_gluing` | **Level 1 only**: fully specified nested-maze route finding |
| `recursive_gluing_discovery` | **Level 2 as implementation**: prompt states grammar + exact realizable-pair certificate + closing rule |
| `recursive_gluing` | **Level 1 CSP**: expanded region/overlap assignment |
| Four siblings | Separate small algebraic/compiler/code/coarse toys; **not** maze replications |

**Recommendation (do not merge silently):**  
Center on the **maze**. Use a **two-phase** contract:

1. **Phase L1 (calibration):** operational walk semantics stated; agent returns routes on small depths.  
2. **Phase L2/L3 (target):** same semantics; agent must **discover** that a compact boundary summary (e.g. realizable \((o_\text{in}, o_\text{out})\) pairs per tile type × remaining depth, plus sealing/edge constraints as needed) decides root SAT/UNSAT and scales; **do not** name the certificate format or the bottom-up algorithm in the agent prompt. Evidence = multiple public instances, optional validate-route tool, optional shallow demos—not hidden evaluator code.

Discovery’s compact oracle is a **positive control / judge backend**, not the agent-facing “discovery” task as written.

---

## 2. Strongest criticisms of the current environment(s)

### 2.1 `recursive_maze_gluing` — primary

**Files:**  
`envs/cat_theo/recursive_maze_gluing/files/{prompt.md,network.py,judge.py,solver.py,visible_tests.py}`, `config.yaml`, `tests/test_recursive_maze_gluing.py`.

#### A. Prompt already hands over the mechanism (not latent)

`prompt.md` states:

- XOR orientation on edges/shafts;
- shaft descend / ascend at child exit;
- `nesting["deeper"]` when remaining depth ≥ 2;
- root exit **sealed** until descend+ascend;
- directed edges used at most once per nested copy;
- SAT = explicit route; UNSAT = no walk.

That is a complete operational specification of a finite graph search. Banned theory words are absent (good), but **conceptual opacity is near zero**. A competent agent is asked to implement BFS/DFS with the stated state—not to recover a hidden generating rule.

#### B. “Recursive obstruction” is mostly a single root flip

In `generate_maze` (`network.py`):

```text
cycle_flip = 1 if regime == CYCLIC_UNSAT else 0
```

- `CYCLIC_*`: root `keep` gets cycle edges with that flip on `ra→rb`.  
- **`inner_keep` always gets `tree_edges` (all flip 0)** even in cyclic regimes.  
- Leaf `crypt` has flip 0; decoy `pit` has a local flip 1.

So SAT vs UNSAT is decided by **one root corridor flip + goal orientation 0**, not by monodromy accumulated through recursive composition. Nesting mainly enforces **sealing** (must descend once). Depth does not deepen the orientation obstruction.

**Self-similarity is not consequential for the polarity contrast.** That fails research-brief §2 and §5.B.

#### C. Depths 1–3 do not force composition

`config.yaml`: depth easy/medium/hard = 1/2/3.  
Oracle: BFS over `(stack, room, orientation, cleared, used edges)` with `max_nodes=50_000` (`shortest_route`).  
Tile graphs are tiny (≈3–5 rooms, few edges). Depth 3 is trivial for generic search.

Grade suite (`build_grade_mazes`): `local_visible`, `configured`, `assembled_sat`, `assembled_unsat`, `opaque_twin`, `decoy_heldout` + determinism.  
`assembled_sat` / `assembled_unsat` differ by regime and **different seeds** (`seed+11` vs `seed+13`), so opaque labels are not matched twins. Transparent mode is closer to a polarity pair, but still not a recursive-composition pair.

#### D. Fixed hand template, not a generative family

Always `keep` / `inner_keep` / `crypt` (+ optional `pit`). Same topology; axes only flip depth, one edge flip, labels, decoy.  
`config.yaml` latent_factors honestly say:

> `causal_mechanism: unavailable: fixed hand-authored template code`

No held-out **production patterns**—only seed/label variation of one maze.

#### E. Shortcuts the design already partially measures

| Shortcut | Behaviour on current grade |
|---|---|
| Stock `solver.py` | One-corridor + first-edge; fails most checks (`test_grade_reference_beats_baseline`) |
| `arm_ignore_orientation` | Zeros flips; **fails `assembled_unsat`** (correctly) |
| Generic BFS with full state | **Solves all current instances** (same as oracle) |
| “Local tiles have edges ⇒ SAT” | Fails UNSAT if agent returns sat without route check; unsat-guessing can luck into UNSAT cases |
| Shallow template “descend crypt then walk to door” | Works on TREE/CYCLIC_SAT transparent; fails decoy if it always picks pit; fails UNSAT |

**Strongest null for any pilot on current maze: “agent implemented the prompt’s BFS.”** That is Level 1 success, not Levels 2–3.

#### F. Judge metrics are coarse

7 binary checks → accuracy; no separate false-SAT vs false-UNSAT rates, no node/time budgets on the candidate, no depth curves, no interface-certificate track.

---

### 2.2 `recursive_gluing_discovery` — misnamed relative to intent

**Files:** `recursive_gluing_discovery/files/{prompt.md,network.py,...}`, `tests/test_recursive_gluing_discovery.py`.

**What works well (as engineering):**

- Compact grammar; depths 3/6/12; unfolded size \(2^{d+1}-1\).  
- `compact_summaries` + `compose_branch` is a sound complete interface DP; cross-checked vs expanded CSP for shallow depths.  
- UNSAT via `leaf_delta=1` + identity `closing` while local tables stay nonempty—**true compositional obstruction**.  
- Baselines: `arm_copy_leaf_upward` fails decoy/opaque/twist/unsat; good.  
- `measure_scaling` shows compact stays small while expansion blows up.

**What it does *not* test:**

- Prompt **specifies** productions, wiring, exact `realizable[type][depth]` certificate, and closing rule.  
- Name “discovery” is false advertising: it tests **implement the stated compositional algorithm** (Level 2 coding), not mechanism recovery (Level 3).  
- Still one stem/tip/(weed) family; heldout_twist only flips `mid_delta`.

**Role going forward:** judge/oracle machinery and Level-2 **positive control**, not the primary agent-facing discovery task.

---

### 2.3 `recursive_gluing` (expanded CSP)

Prompt: regions + overlap pair tables → assignment. Depths 1–3, domain 3/5/7.  
Valid **representation control** only if the **same latent instance** is shown compact vs expanded. Today generators are related in spirit but not proven instance-identical to maze or discovery. Do not claim “CSP control for maze composition” without a shared generator bridge.

---

### 2.4 Four sibling apps

From configs + audit `docs/audits/2026-10-17-four-apps-evaluation-readiness.md`:

| Env | Actual construct | Why not a maze replication |
|---|---|---|
| `recursive_holonomy_gluing` | Finite maps; fixed-point of cycle | Map algebra, not nested route gluing |
| `recursive_compiler_bootstrap` | Compile/recode equivalence | Stage claims, depth capped at 2 |
| `recursive_error_correcting_codes` | Block overlaps over \(\mathbb F_5\) | Linear constraints |
| `recursive_coarse_graining` | 2-spin projector toy | Not physics; weak depth |

Audit correctly: **174 passed ≠ model capability or construct validity**; `direct` vs `recursive` confounds structure with other factors; polarity contrasts are the clean ones; model performance **unmeasured**.

**Recommendation:** do not treat as cross-domain replications. Defer entirely until maze L2/L3 is solid. Keep only if a later program states an explicit shared hypothesis (e.g. “interface monodromy”) and builds matched transfer items.

---

## 3. Experiment matrix (factors, controls, confounds)

### Central falsifiable hypothesis (H1)

> On nested-tile instances whose **local components are matched** but whose **recursively composed boundary behaviours** disagree on the root goal, agents that only use local solvability / ignore orientation–nesting interface state will show elevated **false SAT** (or invalid routes). Agents that recover a **sufficient interface summary** (realizable boundary behaviours by tile type and remaining depth) will match the oracle on held-out depths and seeds where naive unfold/BFS is resource-bounded—and will do so **without** the prompt naming that summary or algorithm.

Secondary:

- **H2 (L1):** With full walk semantics, generic search solves small depths; L1 accuracy alone ≠ H1.  
- **H3 (presentation):** Opaque relabel preserves H1 for agents with the right invariant; copy-label heuristics fail.  
- **H4 (not claimed):** Success ⇏ internal sheaf concept.

### Factor matrix

| Factor | Levels | Isolates | Confound if mixed |
|---|---|---|---|
| **Polarity** | SAT vs UNSAT | Global obstruction | Changing topology at the same time |
| **Depth** | 1,2,3, then 4,6,8+ | Scaling / need for compact summary | Changing regime or template |
| **Obstruction locus** | Root-only flip vs **accumulated nested transform** | Whether recursion matters | Current maze: root-only |
| **Presentation** | transparent / opaque | Label invariance | Seed-coupled relabel on polarity pairs |
| **Ambiguity** | clean / decoy shaft | Evidence-based child choice | Decoy that also flips polarity |
| **Evidence regime** | full opspec vs opspec+demos vs tool traces | L1 vs L3 | Withholding rules with no recovery path |
| **Output** | route vs compact interface cert vs both | L1 vs L2 | Scoring only status bit |
| **Representation** | maze route vs compact grammar vs expanded CSP | Transfer / control | Different generators per format |

### Required paired contrasts

1. **Matched local, different global (primary):** identical tile graphs and shafts; only nested state-transport / closing differs so local walks exist on both, root SAT differs. Same seed for labels.  
2. **Depth ladder:** fixed generator rules & polarity; depth varies.  
3. **Opaque twin:** `relabel_*` of same maze; answer preserved.  
4. **Decoy:** extra locally plausible child with different flip/boundary; oracle prefers the compatible child.  
5. **Negative control:** Boolean-child-solvable / ignore-orientation / copy-leaf-upward / first-shaft baselines must fail polarity or decoy items.

### Confounds to forbid in claims

- Calling depth a recursion contrast when polarity or template also changes.  
- Calling siblings “replications” without shared H1 items.  
- Treating unit-test green or reference BFS success as model structural reasoning.  
- Seed leakage / `meta` / regime strings in agent workspace (four-app audit pattern should apply to maze too).

---

## 4. Minimal redesign recommendation and concrete code-level changes

**Principle:** one coherent maze-centered task + strong controls; discovery oracle as backend; siblings deferred.

### 4.1 Design sketch (smallest coherent experiment)

**Agent sees**

- Concrete maze grammar (rooms, edges with numeric side-effects, shafts, depth, nesting, start/goal bits)—**operational walk rules stated once** (fairness: acting rules are not secret).  
- **Not** told: “compute realizable orientation pairs,” “dynamic programming,” theory names, or regime labels.  
- Multiple grade instances; optional `validate_route(maze, steps) -> ok/reason` tool (no SAT oracle).  
- Optional 2–3 **demonstration** mazes with gold routes (shallow), held out from grading seeds.

**Hidden**

- `meta.regime`, expected SAT, generator seed policy for held-out patterns.  
- Compact summary algorithm (judge-only).

**Interface invariant to implement in the judge (prove against route semantics)**

Define for each tile type \(t\) and remaining depth \(k\):

\[
S(t,k) \subseteq \{0,1\}\times\{0,1\}
\]

= set of \((o_{\mathrm{in}}, o_{\mathrm{out}})\) such that there exists a walk from entrance@\(o_{\mathrm{in}}\) to exit@\(o_{\mathrm{out}}\) obeying edge-use, sealing (if shafts), and child calls using \(S(\mathrm{child}, k')\).

**Soundness/completeness sketch (must be tested, not only asserted):**

- Leaf, no shafts: \(S\) = XOR sums along simple paths respecting edge-use (small graphs: enumerate).  
- With shafts: a descend at shaft with flip \(f\) into child type \(c\) contributes transitions that quantify over \((o',o'')\in S(c,k_{\mathrm{child}})\).  
- Sealing: root (or any tile with shafts) may not take exit edge until a successful child return in that copy—encode as mode in the local NFA or as two-phase summary if needed.  
- Edge-use: if graphs stay small, fold used-edge sets into local state; if that blows up, **redesign tiles** so edge-use is unnecessary for the intended obstruction (prefer orientation + sealing only) so \(S\) stays tiny.

**Critical generator change:** put **stateful flips on the recursively reused tile** (`inner_keep`), not only on root `keep`, so depth multiplies obstruction. Example family:

- Each nested copy applies a fixed orientation transport \(\tau \in \{0,1\}\) on the mandatory child round-trip;  
- Root requires total parity \(d\cdot\tau \equiv g \pmod 2\);  
- Local path always exists; global fails iff parity wrong.  
- SAT/UNSAT pair: same tiles, flip \(\tau: 0\leftrightarrow 1\) or goal bit—**matched locals**.

That makes recursion consequential; Boolean “child sat” still true on both.

**Outputs**

- L1 items: route certificates (`replay_route`).  
- L2 items (harder depths / held-out): either routes **or** agent-proposed interface tables checked against judge \(S\) (exact match or sat-equivalent closure)—format described as “optional compact proof” only after L1, or scored in a second solve API without prescribing DP.

**Depth:** config hard ≥ 6–8 once compact oracle exists; keep L1 grade depths 1–3 for calibration. Candidate resource budget in judge so pure unfold BFS times out on deep items while compact oracle stays fast (mirror discovery’s pattern).

### 4.2 Priority-ordered code changes

| P | Change | File/contract | Intended effect | Refuting test | Success criterion |
|---|---|---|---|---|---|
| **P0** | Document claim levels in env README/comment; stop implying discovery | `recursive_maze_gluing/` + brief pointer in discovery prompt header (internal) | Honest construct | — | Review sign-off |
| **P1** | **Recursive obstruction generator:** flip/transport on `inner_keep` (and nested path), matched SAT/UNSAT same seed | `network.py` `generate_maze` | Polarity from composition | `test_obstruction_is_nested_not_root_only`: root-only flip disabled still UNSAT at depth≥2 when nested τ=1 | Nested τ drives SAT; local leaf walks nonempty on UNSAT |
| **P2** | Matched polarity twins API | `paired_mazes(seed, depth, ...)` | Clean H1 contrast | Twins equal after zeroing the one transport bit | `public` graphs equal except that bit / goal |
| **P3** | Compact maze interface oracle \(S(t,k)\) + agree with BFS on depths ≤4 | `network.py` new `compact_maze_summaries`, `maze_satisfiable_compact` | L2 backend; scale | Cross-check vs `shortest_route`; disagree ⇒ fail | 100% agree shallow; deep compact finishes & BFS budget-exceeds |
| **P4** | Grade matrix: depth ladder, matched sat/unsat, opaque twin same seed, decoy, held-out **pattern id** | `build_grade_mazes` | Separable metrics | Leakage: pattern id not in agent payload | Checks named; metrics split SAT/UNSAT errors |
| **P5** | Baselines: ignore orientation; local-sat⇒global-sat; always-crypt; BFS with node cap; compact reference | `arm_*` | Nulls for H1 | Caps: BFS fails deep; local-sat fails unsat | Reference 1, nulls 0 on H1 items |
| **P6** | Prompt: keep walk opspec; **remove** recipe-like “what correct means” that spoils L3; add that deep instances may need a reusable account of what a nested tile can do to the orientation bit—**without** specifying tables | `prompt.md` | L3 space without unfair hidden rules | Banned-token test; “realizable pair” / “dynamic programming” absent | Still solvable from opspec + search on small; deep favors summary |
| **P7** | Judge metrics: false SAT, false UNSAT, per-depth, optional candidate node_count if instrumented | `judge.py` | Interpretable pilot | — | JSON metrics present |
| **P8** | Discovery: mark as `compact_grammar_control`; optional bridge `maze_to_grammar` later | discovery config/docs only first | No false “discovery” claim | — | Docs match tests |
| **P9** | Defer siblings from primary pilot | suite inventory | Focus | — | Pilot JSON = maze only |

**Do not do first:** more sibling envs, cryptic renames without matched twins, deleting sealing/XOR (they are the right mechanics), or requiring sheaf vocabulary.

### 4.3 On the proposed interface summary

Candidate \(S(t,k)\subseteq\{0,1\}^2\) (orientation in/out) is **necessary** given XOR semantics and goal orientation.  
**Not automatically sufficient** if:

- sealing is not folded in (need “cleared” mode or exit enabled flag in the summary);  
- edge-use creates path-history dependence beyond orientation;  
- multiple shaft choices (crypt vs pit) need existential choice inside \(S\), not a single Boolean.

**Proof obligation (code):** for all generator outputs with depth≤4,  
`maze_satisfiable(m) == ( (start,goal) ∈ S(root,depth) with sealing )`, and every BFS route’s boundary pair ∈ \(S\). If edge-use breaks small \(S\), **simplify edge-use** in the generator (e.g. allow reuse, or unique paths) so the intended invariant stays finite and tight—better than an incomplete summary.

Discovery’s enter/leave label pairs are the right **abstract** cousin; maze should keep **orientation bits** as the concrete state so the agent-facing world stays a maze, not a grammar worksheet.

---

## 5. Adversarial regression tests and baselines

Add under `tests/test_recursive_maze_gluing.py` (names indicative):

1. `test_nested_transport_drives_polarity` — depth 2/3; nested τ toggles SAT; locals nonempty.  
2. `test_matched_sat_unsat_identical_public_topology` — only transport/goal differs.  
3. `test_compact_summary_agrees_bfs_depth_le_4` — all regimes × opacity × ambiguity grid.  
4. `test_compact_scales_where_bfs_budget_fails` — depth 8, BFS max_nodes small raises `OracleBudgetExceeded`; compact returns.  
5. `test_arm_local_sat_implies_global_fails_unsat` — new baseline.  
6. `test_arm_ignore_orientation_fails_nested_unsat`.  
7. `test_opaque_twin_same_seed_pair`.  
8. `test_heldout_pattern_not_in_training_template_family` — at least one second topology family (e.g. two shafts in series) in grade, absent from visible demos.  
9. `test_agent_workspace_no_regime_meta_leak` — mirror four-app workspace lint.  
10. `test_prompt_forbids_algorithm_giveaway` — no “realizable”, “for each depth compute”, “dynamic programming”, theory tokens.  
11. `test_false_sat_scored_separately` — judge metric path.  
12. Discovery: `test_docs_claim_level_is_algorithm_implementation` (documentation regression only).

**Baselines to ship and always report**

| Arm | Expected on H1 UNSAT |
|---|---|
| `arm_reference_compact` | pass |
| `arm_reference_bfs` | pass only under budget |
| `arm_ignore_orientation` | fail |
| `arm_local_nonempty_implies_sat` | fail (false SAT) |
| `arm_first_shaft_template` | fail decoy / some unsat |
| `arm_copy_child_route_ignore_flip` | fail |
| Stock stub solver | fail |

---

## 6. Pre-model go/no-go checklist

Do **not** run Astra/model pilots until:

- [ ] **G1** Nested transport obstruction implemented; unit test shows depth-dependent polarity with matched locals.  
- [ ] **G2** Compact summary ↔ BFS agreement on full shallow grid; budget separation on deep.  
- [ ] **G3** Grade set includes matched SAT/UNSAT, depth ladder, opaque twin, decoy, ≥1 held-out pattern; seeds partitioned.  
- [ ] **G4** Baselines behave as table above; reference grade all-pass.  
- [ ] **G5** Prompt: opspec fair; no algorithm/theory giveaway; workspace leak tests green.  
- [ ] **G6** Judge emits false-SAT, false-UNSAT, per-depth, check names; timeout ≠ unsat.  
- [ ] **G7** Pilot recipe lists **maze only**; siblings explicitly out of scope; claim language = H1 not “sheaf recovery.”  
- [ ] **G8** Human review of one printed SAT and one UNSAT instance: obstruction inspectable by a careful human without code.  
- [ ] **G9** No reliance on `174 passed` or four-app audit as maze validity.

**Go:** G1–G9 hold.  
**No-go:** any of G1–G4 fail (construct still L1-template or root-only flip).

---

## 7. What a successful pilot would not prove

- That the model possesses **sheaf**, **holonomy**, **Čech cohomology**, or “gluing” as internal mathematical concepts.  
- That success is **mechanism discovery (L3)** rather than quiet implementation of graph search (L1) or a memorized interface DP (L2), unless baselines, depth resource curves, and prompt ablations separate those.  
- That skills **transfer** to compilers, codes, coarse-graining, or holonomy apps.  
- That opaque labels test conceptual depth rather than string-handling.  
- That unit-test or reference-oracle green means benchmark validity.  
- That a single SAT/UNSAT accuracy number is enough—without false-SAT vs false-UNSAT, depth, and baseline deltas.  
- That failure means “models cannot do compositional reasoning”—could be prompt brittleness, tool limits, or time.

**Strongest claim a clean pilot may support:**  
*Under this opspec and instance family, model behaviour is consistent with recovering a finite nested-tile boundary summary sufficient for root orientation goals, and inconsistent with local-only gluing—on held-out depths/seeds, relative to stated baselines.*  
Anything stronger is overclaim.

---

## Round-style synthesis (agreement / disagreement / primary design)

### Agreement (treat as settled)

- Target is nasty self-similar composition where local ≠ global; maze is the center.  
- Current maze is **L1 fully specified search** on a **shallow fixed template** with **root-local** polarity.  
- Discovery is a strong **compact algorithm control**, not L3 discovery as prompted.  
- Siblings are not automatic replications; four-app “174 passed” is not model evidence.  
- Interface-style summaries are the right judge-side invariant family; must be proven on maze semantics.  
- Matched SAT/UNSAT + baselines + depth where brute force dies are mandatory.

### Residual substantive tensions

| Tension | Resolution adopted here |
|---|---|
| How much opspec in the prompt? | **State walk rules** (fair action model). **Do not** state the compact algorithm or theory. |
| Route-only vs certificate outputs? | Routes for L1; add compact cert track for L2 deep items once summary exists. |
| Keep discovery env? | Yes as **control/oracle**, not primary agent task; rename claims. |
| Edge-use in summary? | Prefer generator simplification if it blocks small \(S\); don’t cling to edge-use theater. |

### Primary design (accepted)

**Maze-first H1 experiment:** recursive nested orientation transport + sealing; matched polarity twins; compact orientation interface oracle; depth scaling; baselines; honest L1/L2/L3 separation in prompt and metrics.

### Rejected alternatives

- Broad four-app “replication suite” as the main result.  
- Making the prompt cryptic by deleting walk rules without a recovery protocol.  
- Scoring only discovery-style realizable certificates while calling it maze understanding.  
- “Increase difficulty to depth 3 / more decoys” without changing obstruction locus.  
- Claiming CSP `recursive_gluing` controls maze composition without a shared instance bridge.

### Deferred

- Cross-domain transfer (L4).  
- Epistemic/distributed gluing variants.  
- Model concept probes (L5).  
- Full maze↔grammar isomorphism arm (nice later positive control).  
- Any model/Astra run before G1–G9.

### Why the first pilot is informative if the gate passes

A single model run on the redesigned grade set can report, for one frontier agent:

- L1 route accuracy at depth ≤3 (ceiling expected high if search is easy);  
- H1 false-SAT rate on matched nested UNSAT;  
- depth-6/8 accuracy vs BFS-cap baseline and vs ignore-orientation;  
- opaque twin gap.

If L1 high and H1 false-SAT high, the construct bites. If both high, inspect traces for explicit interface tables vs lucky search. If L1 low, fix opspec clarity before claiming compositional failure. That is interpretable **without** overclaiming sheaves—and is exactly what the current repository cannot yet support.

---

### Immediate next step (if implementing in-repo)

Agree scope: **P1–P5 + tests only** in `recursive_maze_gluing` (+ judge metrics P7). No sibling edits. No model calls. Ship a small diff with `tests/test_recursive_maze_gluing.py` extensions proving nested obstruction and compact↔BFS agreement. Stop and re-review before Astra.

&&&&&&&&&&&&&&&

some model #4:

# Adversarial Design Review: Recursive Gluing Environments

This report constitutes a rigorous adversarial design review of the `StrangeTcy/rl_eval_generator` repository (branch `arena/1ddc930c-rl-eval-generator`, commit `0dcb51cbfa35598fa843905c3384d93a5fc95a71`). The goal is to enforce operational precision and separate the evaluation of explicit solvers from the true target: latent mechanism discovery and compositional generalization.

---

## 1. Concise Reconstruction of the Target Capability

The core research objective is to measure **Level 2 (Compositional Generalization)** and **Level 3 (Generating-Mechanism Recovery)**, explicitly rejecting Level 1 (solving a fully specified finite problem) and avoiding premature claims about Level 5 (internalization of sheaf-theoretic concepts). 

Operationally, the target capability is demonstrated if and only if an agent can:
1. **Observe** a self-similar system via opaque local interactions or traces without being explicitly handed the governing rules (e.g., orientation parity XOR, child-return sealing).
2. **Infer** the latent interface boundary rules—discovering that a boolean "is locally solvable" is structurally insufficient for global composition because boundary states must match.
3. **Construct** a reusable, compact structural algorithm (such as a dynamic programming recurrence over boundary-pair invariants) to determine global satisfiability.
4. **Execute** this algorithm on instance depths that strictly prohibit generic exact-search techniques like BFS or DFS.

If the prompt names the rules, the task degenerates to reading comprehension. If the depths are too shallow, the task degenerates to explicit unrolled search. Both are critical failures of construct validity.

---

## 2. Strongest Criticisms of the Current Environments

Based on the repository audit, the current code completely fails to isolate the target capability. 

### `envs/cat_theo/recursive_maze_gluing/`
*   **Prompt Leakage (`prompt.py` / generator):** The agent-facing prompt explicitly explains nesting, XOR orientation, sealing, and edge reuse. This violently invalidates Level 3 (mechanism recovery). The model is not discovering a latent mechanism; it is simply reading the documentation of a finite state machine.
*   **Insufficient Depth & Brute Force Vulnerability:** Configured depths are 1, 2, and 3. At depth 3, the total unfolded state space is trivial enough that a generically prompted Python DFS/BFS script will solve it. The benchmark does not *force* compositional generalization; it merely permits it.
*   **Weak Failure Modes:** The current grade suite does not rigorously ensure that paired SAT/UNSAT instances share identical local topologies but fail globally strictly due to recursive parity/sealing mismatches.

### `envs/cat_theo/recursive_gluing_discovery/`
*   **Provides the Algorithm:** While this env correctly forces scaling (depths 3, 6, 12), the prompt explicitly gives the recurrence semantics and demands a realizable-boundary-pair certificate. This is a Level 1 implementation task of a known compositional algorithm. It is a useful positive control, but useless for mechanism discovery.

### `envs/cat_theo/recursive_gluing/` (CSP Control)
*   If this is just an expanded flat CSP format, standard SAT solvers can crush it at shallow depths. It provides no unique signal regarding compositional reasoning.

### The Four Sibling Applications
*   **Irrelevant at this Stage:** `recursive_holonomy_gluing`, `recursive_compiler_bootstrap`, etc., are currently a distraction. Treating them as replications (Level 4 structural transfer) before the core construct is validated on the maze is a massive methodological error. They must be deferred.

---

## 3. Experiment Matrix: Separating Factors, Controls, and Confounds

To prove the target claim, we must isolate variables. The experiment must be parameterized along the following axes:

| Dimension | Variable | Purpose |
| :--- | :--- | :--- |
| **Mechanism Visibility** | Explicit Rules vs. Opaque API Sandbox | Isolates Level 3 (Mechanism Recovery). Does the agent fail when rules are hidden? |
| **Search Feasibility** | Shallow (d=1,2,3) vs. Deep (d=6,12,20) | Isolates Level 2 (Compositional Generalization). Shallow allows DFS; Deep strictly requires DP/boundary-pair extraction. |
| **Compositional Constraint** | Matched SAT vs. Matched UNSAT | Isolates the "Naive Gluing" failure mode. Both instances must have identical local subgraph reachability, differing only in a single parity requirement at a leaf that causes the root constraint to fail. |
| **Answer Format** | Explicit Route vs. Boundary Certificate | Validates that the model actually derived the invariant, rather than getting lucky with a random walk heuristic. |

**Key Confound to Prevent:** *Label Leakage.* The environment must not use graph-theoretic or topological terminology ("sheaf", "monodromy", "XOR parity"). Components must be labeled as generic opaque nodes (e.g., `sys_A`, `port_3`).

---

## 4. Minimal Redesign Recommendation & Concrete Code Changes

**The Central Hypothesis:** An agent provided with an interactive sandbox of depth-1 and depth-2 instances can infer the complete boundary-state invariant (orientation + seal state), write a compact summary generator, and correctly classify paired depth-15 SAT/UNSAT instances.

**Priority Code Changes:**
1.  **Strip Explicit Prompts (`envs/cat_theo/recursive_maze_gluing/`)**: 
    *   Remove all text explaining orientation XOR and exit sealing. 
    *   Replace it with: *"You are given a system of nested components. You have an interactive testing tool to observe local transitions. Determine whether a global transition from START to END is possible at depth D."*
2.  **Introduce the System ID Sandbox Tool**:
    *   Add a tool: `query_transition(component_id, entry_port, internal_state) -> (exit_port, new_internal_state)`.
    *   This provides the "public evidence" required to fuckingly make the mechanism recoverable without prompt hand-holding.
3.  **Implement Depth Scaling**:
    *   Hardcode evaluation splits into `shallow_eval` (d=3) and `deep_eval` (d=15).
    *   Deprecate depth 1 and 2 from evaluation (move them entirely to the interactive discovery phase).
4.  **Enforce Interface Summaries (Certificates)**:
    *   Instead of asking for a path (which is exponentially long at d=15), require the agent to output the `RealizableBoundaryPair` matrix for the root. 

**The Required Structural Invariant:**
To prove completeness: A valid summary at depth $d$ cannot just be "solvable=True". It must be a set of relations: 
$S_d = \{ (p_{in}, o_{in}, s_{in}) \to (p_{out}, o_{out}, s_{out}) \}$
where $p$ is the port, $o \in \{0,1\}$ is the orientation parity, and $s \in \{0,1\}$ is the seal status. If the code requires more state than this, the DP state space must be updated. This summary is strictly sufficient because parental composition only relies on the child's exit states matching the parent's corridor requirements.

---

## 5. Adversarial Regression Tests & Baselines

Before running any models, the following baselines must be implemented as Python scripts in the repo:

1.  **Baseline 1: Standard Unrolled DFS.** 
    *   *Test:* Must pass Depth 3. Must predictably OOM / Timeout at Depth 15.
2.  **Baseline 2: Naive Local Gluing.**
    *   *Test:* A script that assumes if `entry -> exit` is valid in a child *ignoring parity*, it is valid globally. This baseline **must score 0%** on the adversarial "Matched UNSAT" dataset.
3.  **Baseline 3: Parity-Only Heuristic.**
    *   *Test:* A solver that tracks parity but ignores exit-sealing. Must fail on specifically authored decoy instances where parity aligns but the seal constraint blocks the exit.
4.  **Generator Construct Validity Test:**
    *   Ensure `generator.py` can produce structurally identical mazes where flipping one leaf's orientation parity deterministically flips the root from SAT to UNSAT.

---

## 6. Pre-Model Go/No-Go Checklist

Do not spend a single cent on the Astra API until all of the following evaluate to TRUE:
- [ ] Explicit rule explanations (XOR, sealing) are provably deleted from the agent-facing prompt.
- [ ] The interactive API tool correctly outputs state transitions for d=1 and d=2 without exposing evaluator source code.
- [ ] Evaluation depths are set to at least $d=15$, rendering unrolled graph search mathematically impossible within context limits.
- [ ] The benchmark suite contains cleanly paired SAT/UNSAT cases with identical local components.
- [ ] The oracle dynamically checks the DP boundary certificate, not just a binary SAT/UNSAT guess.
- [ ] Unrolled DFS baseline crashes or times out on the deep evaluation set.

---

## 7. What a Successful Pilot Would Not Prove

If the model passes this revised, rigorous environment, we must strictly bound our claims. 
**A successful pilot would NOT prove:**
1.  **That the model "understands sheaves", "cohomology", or "global sections."** Task accuracy proves the model can infer finite state machine invariants and write dynamic programming recurrences. Claiming it possesses abstract mathematical representations requires mechanistic interpretability, not benchmark scores.
2.  **That the model achieves zero-shot compositional generalization.** Because we are giving it a sandbox to do system identification on $d=1,2$, the model is doing *few-shot interactive* generalization. 
3.  **That the model can transfer this skill.** Success on the maze does not guarantee success on `recursive_compiler_bootstrap`. Transfer is a separate Level 4 claim requiring a completely separate experimental paradigm. 

The immediate next step is to implement the **Code Changes in Section 4** and verify the **Baselines in Section 5**. Only then is the environment ready for adversarial model evaluation.


&&&&&&&&&&&&&&&&&

some model #5:

Key empirical facts are in hand. Now I'll write the report and package the reproducible scripts.I couldn't open the repository, so I haven't done the code audit you asked for. The sandbox has no `git` and no network access. Web search only showed that `StrangeTcy/rl_eval_generator` exists (some PR pages), then hit its usage limit. I haven't read any file on `arena/1ddc930c-rl-eval-generator` or commit `0dcb51cb`, and I haven't made up file or function names.

Instead, I rebuilt the maze rules as your brief describes them (tiles, local rooms, XOR orientation flips on corridors, shafts into child tiles, sealed exits, one use per corridor per copy). I ran tests against that model with an exact search oracle and the compact per-component summary. The report labels each claim as from the brief, from my model, or a check you still need to run on the real code (eight of these, P-1 to P-8, with pass/fail criteria).

## Main findings (from my model, reproducible)

1. **On random instances, orientation never mattered.** Over 1,500 random instances, ignoring orientation and treating each child as just "solvable or not" got the answer right every time, with no false SATs. Random flips almost always make both orientations reachable. If the repo's generator behaves the same way, the suite doesn't test the central claim, whatever the prompt says. Check P-1 tests this and is the most important one to run.
2. **Depth didn't add work.**
   - In every random setup, what a child can do was the same at every depth.
   - In a hand-built case where orientation does matter, the answer was simply whether depth is even.
   - Adding a second child shaft made every instance from depth 2 up solvable.
   - This is a general fact: with fixed rules and a finite interface, the answer repeats with depth after some point. Guessing deeper answers from depths 1–6 was 100% correct up to depth 40.
3. **One child per level never defeats brute force.** Exhaustive search grows only linearly with depth (11 to 75 states from depth 0 to 8). With two children per level it grows exponentially (about 12k states at depth 11). That only forces anyone to visit every copy if the exit stays sealed until *all* children are cleared. Then a full route at depth 12 is exponentially long, so a written-out route can't be the answer format.
4. **The entry/exit-state summary is exact only under four conditions:**
   - each child copy is entered once;
   - used corridors and cleared status are tracked per copy, not per tile type;
   - the parent's state on return depends only on the child's exit state;
   - nothing is shared across copies.

   I give a proof sketch. The summary and the exhaustive search agreed on 600 of 600 instances when copies are entered once. When a child can be re-entered and keeps its used corridors, I have a two-corridor counterexample where the truth is solvable but the summary says unsolvable. The brief says the oracle tracks a "tile stack". If that stack holds tile types rather than which copy you're in, sibling copies get mixed up (check P-4).

## Recommendation

Run three phases on the same instances and score them separately, with no combined score:

- **Phase 0:** the current maze, fully specified and small. This is a baseline check that the model understands the rules.
- **Phase 1:** rules fully stated, but large enough that brute force can't work. The model gives a verdict first and a compact certificate in a later turn, so the certificate format doesn't hint at the method.
- **Phase 2:** the corridor/shaft effects and which children appear at each level are hidden. The model can only learn them through a limited number of trial walks at depth 3 or less. The generator must check that this evidence fixes the answer within a hypothesis class the prompt states in plain operational terms.

The report gives seven code changes in priority order, each with a refuting test and a success/failure result. The first three:

- **Document the rules and add the summary module.** Then cross-check it against exhaustive search on 11k+ instances, requiring zero disagreements.
- **Build a paired-instance generator.** Each pair differs by one flip deep in the recursion, every tile is still locally passable, and the "child is solvable" shortcut scores exactly 50% on the pairs.
- **Replace the fixed depths 1–3.** Choose depths per rule set, past the measured brute-force limit, beyond where the answer starts repeating, and with equal numbers of solvable and unsolvable cases.

The rest are certificate checkers that work without unfolding the tree, the Phase 2 trial-walk tool, leakage hardening, and a prompt rewrite.

The four sibling apps should make no claims in this study; at most they're candidates for a later cross-domain test. The constraint-network version (`recursive_gluing`) is only a valid control if it's built from the same instances with a checked one-to-one mapping. Even then it tests presentation, not recursion.

The report also covers the experiment matrix, baseline thresholds, the go/no-go checklist, Round 4 attacks on my own proposal, the disagreements that remain (for example, whether Phase 2 is real mechanism discovery or just estimating hidden parameters), and **"What a successful pilot would not prove."**

**First step:** run P-1 to P-8 on the pinned commit. If you can upload the repo or paste the relevant files, I'll replace the "check" labels with findings tied to specific files and functions.

Files are in the output directory:
- `DESIGN_REVIEW.md` — the full report
- `review.tgz` — the model and five experiment scripts; `RUN_ALL.sh` reruns everything in about 15 seconds