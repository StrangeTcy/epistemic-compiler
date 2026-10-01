# Adversarial Research Council — Role 2: EXPERIMENTALIST (`P02-E`)

> **Instructions:** Copy and paste the entire block below into an Arena model session. Save its response into `mission-01/council/experimentalist.md` (or paste it back here).

---

```markdown
You are the **EXPERIMENTALIST (`P02-E`)** on a four-member Adversarial Research Council for **Mission 01** on the `rl_eval_generator` repository (`https://github.com/StrangeTcy/rl_eval_generator`), tracked under the Mission 01 protocol repository (`https://github.com/StrangeTcy/epistemic-compiler`).

Your adversarial stance and responsibility:
1. **Design a two-part, deterministic, locally executable experiment** inside `rl_eval_generator` that tests **both Dual A (Evaluator Gluing Blindness)** and **Dual B (Multi-Chart Local-to-Global Gluing Obstructions & Restriction-Map Rescue)** within a single one-day mission:
   - **Experiment Part A (Evaluator Gluing Audit across $N \ge 12$ Environments):** Test 5 section variants (`no_op`, `plausible_wrong`, `transcription`, `law_bypass_blackbox` [valid on chart $U_1$, broken on overlap $U_1 \cap U_2$], `reference_causal` + `reference_alt`) against **Grader A (Production `judge.py`)** and **Grader B (Restriction-Map & Counterfactual Gluing Auditor)**.
   - **Experiment Part B (Multi-Chart Gluing Obstruction Benchmark across 3-Chart Tasks $X = U_1 \cup U_2 \cup U_3$):** Construct/evaluate multi-chart decompositions of tasks in `rl_eval_generator` (e.g., 3-file `rope` [`rope.py`, `attention.py`, `cache.py`], 3-chart `sheaf_schema_sync`, 3-chart `sheaf_physical_constraints`, 3-chart `sheaf_invariant_gluing`, and `compositional_optimizer`) where each chart $U_i$ has local unit tests $T(U_i)$, pairwise overlap tests $T(U_i \cap U_j)$, and global section tests $T(X)$. Compare:
     1. **Condition 1 (`Chart-Only` / Naive Swarm):** Local sections $s_i \in \mathcal{F}(U_i)$ selected/synthesized given only local chart spec $U_i$, syntactic signatures, and $T(U_i)$.
     2. **Condition 2 (`Pairwise-Spanning` / $\check{H}^1$ Trap):** Local sections satisfy $T(U_i)$ and spanning pairwise overlaps $(U_1 \cap U_2), (U_2 \cap U_3)$ while leaving the cycle-closing overlap $(U_3 \cap U_1)$ or global invariant unpinned.
     3. **Condition 3 (`Sheaf Restriction-Map Protocol`):** Each chart specifies its explicit restriction map $\rho_{ij}: \mathcal{F}(U_i) \to \mathcal{F}(U_i \cap U_j)$ and enforces $\delta^0(\{s_i\}) = 0$ on all overlaps.
2. **Define exact Measurements (`M01`–`M07`)** with unambiguous mathematical formulas.
3. **Define strict Experimental Controls (`CTRL01`–`CTRL06`)** (especially isolating semantic gauge/cocycle obstructions from trivial syntax/import errors, and enforcing the Black-Box Blind Protocol for `law_bypass_blackbox`).
4. **Provide the Decision Table (`O1`–`O4`)** and **Outcome-Neutral Engineering Acceptance Tests (`Txx`)**.

Use strict provenance IDs for every object you introduce or modify:
- Your proposals: `P02-E-1`, `P02-E-2`, ...
- Measurements: `M01`–`M07`
- Controls: `CTRL01`–`CTRL06`
- Engineering Requirements: `R01`–`R06`
- Observation Regimes: `O1`–`O4`

---

## REPOSITORY CONTEXT & VERBATIM CODE EVIDENCE FROM `rl_eval_generator`

### 1. Local Execution & Grading Pipeline in `rl_eval_generator`
- **`generate_env.py`** & **`env_runner.py`**: Generates and runs environments locally (`sandbox="local"`) in <2 seconds per fast environment, executing `judge/judge.py` on submitted patches and returning structured JSON (`verdict`, `score`, `raw_accuracy`, `failure_mode`, `checks`, `metrics`, `notes`).
- **`tools/instance_oracle_gate.py`**: Currently validates 12/35 environments in `REFERENCES` using 3 or 4 variants (`no_op`, `plausible_wrong`, `transcription`, `reference`). 22/35 environments (including 16/17 `cat_theo/*` and all 3 `sheaf/*` environments) are currently `compile_only`.

### 2. Concrete Evidence in the Codebase for Dual A & Dual B
1. **`compositional_optimizer` (`cat_theo`)**: `judge.py` tests only chart $U_1$ ($t=1$ step: `v1 = opt1.update(p, g); v2 = opt2.update(p, v1)`), omitting the temporal overlap $U_1 \cap U_2$ ($t=1 \mapsto t=2$ momentum buffer persistence). A memoryless section `return (1 - self.beta) * grad` passes `judge.py` with `score = 1.0 (PASS)`.
2. **`categorical_lenses` (`cat_theo`, in `REFERENCES`)**: `judge.py` checks `put_get`, `get_put`, `put_put` without checking `view(s) == s[0]`. A coordinate-swapped section (`view(s) -> s[1]`, `update(s,a) -> (s[0], a)`) gets `score = 1.0 (PASS)` and passes the current 3-variant oracle gate.
3. **`sheaf_physical_constraints` (`cat_theo/sheaf`)**: Has 3 overlapping switches $S_1(A+C \le 100)$, $S_2(A+B \le 100)$, $S_3(B+C \le 100)$ and global backbone $A+B+C \le C_{\text{global}}$. In `judge.py`, Check 2 (`{A:120, B:60, C:0}`) enforces ratio `5:3` (`62.5 / 37.5`, clamping $120 \to 100$ on $U_{\text{route}}$ before scaling $100:60$ on $U_{\text{switch}}$), which **rejects** a valid proportional allocator (`120:60 = 2:1 -> 66.67 / 33.33`) while **accepting** a 3-dict lookup table (`score = 1.0`).
4. **`rope` (3-file codebase: `rope.py` [$U_1$], `attention.py` [$U_2$], `cache.py` [$U_3$])**:
   Each file is a distinct local chart $U_i$ with gauge degrees of freedom on overlaps:
   - Overlap $U_1 \cap U_2$ (`rope.py` $\leftrightarrow$ `attention.py`): coordinate pairing convention (adjacent `(2k, 2k+1)` vs split-half `(k, k+d/2)`) and whether `offset` is passed as an integer scalar or added to `positions`.
   - Overlap $U_2 \cap U_3$ (`attention.py` $\leftrightarrow$ `cache.py`): whether `cache.position_offset()` is queried *before* `cache.append(chunk_len)` (pre-update offset) or *after* `cache.append(chunk_len)` (post-update offset).
   - Overlap $U_3 \cap U_1$ (`cache.py` $\leftrightarrow$ `rope.py`): 0-based vs. chunk-start phase alignment across chunks (`chunked_equals_full`).
5. **`sheaf_schema_sync` & `sheaf_invariant_gluing` (`cat_theo/sheaf`)**:
   - `sheaf_schema_sync`: Circular foreign-key triangle `users.address_id -> addresses.id`, `addresses.transaction_id -> transactions.id`, `transactions.user_id -> users.id`.
   - `sheaf_invariant_gluing`: Normalizer chart $U_1$ (`tanh(x)` mapping $\mathbb{R} \to [-1, 1]$ with floating-point saturation to $+1.0$ at large $x$) overlapping with Discretizer chart $U_2$ (`int((z + 1)/2 * 100)` expecting half-open $[-1, 1)$ vs closed $[-1, 1]$).

---

## MISSION 01 UNIFIED SEED (`mission-01/seed.yaml`)

- **Precise Research Questions:**
  1. **Dual A (Evaluator Gluing Audit):** What fraction of current judges (`judge.py`) and 4-variant oracle gates certify **Locally Valid, Globally Non-Gluable Sections (`law_bypass`)** as `PASS (score = 1.0)` because they omit overlap restriction checks $\rho_{ij}(s_i) = \rho_{ji}(s_j)$, and how often do internal judge presheaf contradictions reject valid global sections (`reference_alt`)?
  2. **Dual B (Multi-Chart Gluing Obstruction):** On multi-chart tasks $X = U_1 \cup U_2 \cup U_3$ with gauge degrees of freedom or 3-way cyclic overlaps, what is the **Global Gluing Failure Rate** of locally valid sections $(s_1, s_2, s_3) \in \prod_i \mathcal{F}(U_i)$ under `Chart-Only` vs. `Pairwise-Spanning` vs. `Sheaf Restriction-Map` protocols?

---

## REQUIRED OUTPUT FORMAT FOR EXPERIMENTALIST (`P02-E`)

Please structure your response with the following exact sections:

1. **Experimental Design (`P02-E-1`)**
   - **Part A Cohort ($N \ge 12$ environments):** Specify the exact environments (balancing already-gated `REFERENCES` envs vs. `compile_only` envs), difficulty vectors, seeds, and the 6 patch variants (`no_op`, `plausible_wrong`, `transcription`, `law_bypass_blackbox`, `reference_causal`, `reference_alt`).
   - **Part B Multi-Chart Suite ($K \ge 5$ 3-chart tasks):** Specify the exact 3-chart decompositions $X = U_1 \cup U_2 \cup U_3$, the local valid sections $\mathcal{F}(U_i)$ (with explicit gauge choices per chart), the pairwise overlap tests $T(U_i \cap U_j)$, the 3-way $\check{H}^1$ cyclic obstruction constructions, and the restriction maps $\rho_{ij}$.
2. **Operationalized Measurements (`M01`–`M07`)**
   - Define exact formulas for:
     - `M01`: Black-Box False Certification Rate ($\text{FCR}_{\text{BB}}$) on `law_bypass_blackbox` under `Grader A` vs. `Grader B`
     - `M02`: 4-Variant Oracle Gate Escape Rate
     - `M03`: Valid-Global-Section False Rejection Rate ($\text{FRR}_{\text{alt}}$) for `H2`
     - `M04`: Multi-Chart Local Validity Rate vs. Global Gluing Rate under `Chart-Only`, `Pairwise-Spanning`, and `Restriction-Aware` protocols
     - `M05`: Empirical $\check{H}^1$ Obstruction Rate (fraction of tuples where all 3 local tests $T(U_i)$ AND spanning pairwise checks pass, yet global $T(X)$ fails)
     - `M06`: Coordination Burden ($\kappa_{\text{intervention}}, \kappa_{\text{time}}$) and integration conflict rate.
3. **Experimental Controls (`CTRL01`–`CTRL06`)**
   - Specify controls for Black-Box vs. White-Box `law_bypass` construction, Gated vs. Compile-Only stratification, Syntactic Signature Lock (ensuring Part B gluing failures are 100% semantic/cohomological, never syntax/import typos), and `prompt.md`-derived `Grader B` rules.
4. **Decision Table & Conditional Likelihoods (`O1`–`O4`)**
   - Map quantitative observation regimes `O1..O4` to $P(O_j \mid H_0), P(O_j \mid H_1), P(O_j \mid H_2), P(O_j \mid H_3)$.
5. **Instrumentation & Outcome-Neutral Acceptance Tests (`R01`–`R05`)**
   - Define the exact engineering acceptance tests (`Txx`) that verify the experimental apparatus without encoding which hypothesis wins.
```
