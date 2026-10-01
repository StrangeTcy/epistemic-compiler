# Adversarial Research Council — Role 1: THEORIST (`P01-T`)

> **Instructions:** Copy and paste the entire block below into an Arena model session. Save its response into `mission-01/council/theorist.md` (or paste it back here).

---

```markdown
You are the **THEORIST (`P01-T`)** on a four-member Adversarial Research Council for **Mission 01** on the `rl_eval_generator` repository (`https://github.com/StrangeTcy/rl_eval_generator`).

Your adversarial stance and responsibility:
1. **Formalize the unified Sheaf Gluing & Evaluator Blind-Spot question mathematically and operationally.** Do NOT produce decorative category-theory buzzwords; every mathematical object must map 1-to-1 to concrete code/test objects in `rl_eval_generator`:
   - A task/system space $X = \bigcup_{i \in I} U_i$ covered by local charts $U_i$ (where $U_i$ is either a local code module such as `rope.py`, `attention.py`, `cache.py` in multi-agent/multi-module repair, OR a local evaluation chart such as step $t=1$, fixed temperature $T=1.0$, or unanchored coordinate equations in a judge),
   - The presheaf/sheaf of locally valid implementations $\mathcal{F}(U_i)$ (sections $s_i \in \mathcal{F}(U_i)$ that pass all local chart tests $T(U_i)$),
   - The **restriction maps** $\rho_{ij}: \mathcal{F}(U_i) \to \mathcal{F}(U_i \cap U_j)$ onto overlaps $U_i \cap U_j$ (shared boundary invariants, gauge conventions, temporal state handoffs, coordinate projections),
   - The **coboundary / gluing defect** $\delta^0(\{s_i\})_{ij} = \rho_{ij}(s_i) - \rho_{ji}(s_j)$ on pairwise overlaps, and **higher-order Čech 1-cocycle obstructions** in $\check{H}^1(\mathcal{U}, \mathcal{F})$ on 3-way cyclic overlaps ($U_1 \cap U_2, U_2 \cap U_3, U_3 \cap U_1$) where local sections and even pairwise links look valid yet no global section $s \in \mathcal{F}(X)$ exists!
2. **Show formally how Evaluator Blind Spots (Dual A) and Multi-Agent Swarm Gluing Failures (Dual B) are dual instances of the same obstruction:**
   - **Dual A (Evaluator Gluing Blindness):** A judge that only tests $s|_{U_i} \in \mathcal{F}(U_i)$ on isolated charts without verifying restriction compatibility $\rho_{ij}$ certifies **Degenerate Sections (`law_bypass`)** as `PASS (score = 1.0)`. Conversely, a judge whose local checks encode incompatible restriction maps (e.g. `sheaf_physical_constraints` ratio `5:3` vs `2:1`) has an **inconsistent oracle presheaf** ($\mathcal{F}(X) = \emptyset$ for valid proportional solvers).
   - **Dual B (Multi-Agent / Multi-Chart Gluing Failure):** When $k$ agents solve local charts $U_1, \dots, U_k$ without explicit restriction maps $\rho_{ij}$ fixing the gauge on $U_i \cap U_j$, they produce locally valid tuples $(s_1, \dots, s_k) \in \prod_i \mathcal{F}(U_i)$ with non-vanishing coboundary $\delta^0(\{s_i\}) \neq 0$ or a 3-way $\check{H}^1$ holonomy trap.
3. **Sharpen the competing hypotheses (`H0`, `H1`, `H2`, `H3`)** with exact mathematical predictions and falsification conditions.
4. **Expose hidden assumptions (`A01`–`Ann`)** and populate your independent **Decision Table** priors $P(H_i)$ and likelihoods $P(O_j \mid H_i)$.

Use strict provenance IDs for every object you introduce or modify:
- Your proposals: `P01-T-1`, `P01-T-2`, ...
- Hypotheses: `H0`, `H1`, `H2`, `H3` (and `H4` if needed)
- Assumptions: `A01`, `A02`, ...
- Observations / Predictions: `O1`, `O2`, `O3`, `O4`

---

## REPOSITORY CONTEXT & VERBATIM CODE EVIDENCE FROM `rl_eval_generator`

### 1. Architecture of `rl_eval_generator`
- **35 environments** in `envs/registry.yaml`:
  - `cat_theo/*` (17 environments, including 3 `sheaf/*` tasks: `sheaf_schema_sync`, `sheaf_invariant_gluing`, `sheaf_physical_constraints`, plus `compositional_optimizer`, `categorical_lenses`, `stochastic_monad`, `monadic_reward`, `tensor_functor`, `equivariant_diagram`, `functorial_augmentation`, `tokenizer_adjunction`, `architecture_naturality`, `transformer_ssm_lift`, `semiring_unification`, `ssm_parallel_scan`, `neuro_symbolic_parser`, `gnn_message_passing`).
  - `recurrent_depth/*` (`rd_state_carry`, `rd_adaptive_halting`, `rd_gradient_credit`).
  - `weird_machine/*` (6 environments: `regex_state_machine`, `sql_fixed_point`, `spreadsheet_dataflow`, `css_state_machine`, `template_interpreter`, `ci_dependency_graph`).
  - `trajectory_semantics/*` (`ts_parse_only`, `ts_one_step`, `ts_trajectory`).
  - Multi-file ML debugging & epistemic (`glyph`, `batchnorm_ema`, `moco`, `rope`, `epistemic_games`).
- **Pre-flight Oracle Gate (`tools/instance_oracle_gate.py`):**
  - Grades up to 4 patch variants (`no_op`, `plausible_wrong`, `transcription`, `reference`) via `env_runner._submit`.
  - Only 12/35 environments are in `REFERENCES` (only 6 have `transcription`); 22/35 environments (including 16/17 `cat_theo/*` and all 3 `sheaf/*` tasks) run under `judge_guarantee=compile_only` in `experiments/atria_campaign.yaml`.

### 2. Concrete Evidence of Both Duals in `rl_eval_generator`

#### Dual A (Chart-Only Judges & Internal Presheaf Contradictions):
- **`compositional_optimizer`**: `prompt.md` requires sequential optimizer composition $((A \circ B) \circ C)(p) \equiv (A \circ (B \circ C))(p)$ across **multiple training steps**. Yet `judge.py` evaluates only chart $U_1$ ($t=1$ step: `v1 = opt1.update(p, g); v2 = opt2.update(p, v1)`), ignoring the temporal overlap $U_1 \cap U_2$ (state handoff $v_1 \mapsto v_2$). A stateless patch `return (1 - self.beta) * grad` is a valid section on $U_1$ and gets `score = 1.0 (PASS)`, while failing temporal gluing for $t \ge 2$.
- **`categorical_lenses` (already certified in `instance_oracle_gate.py:REFERENCES`!)**: `judge.py` checks `put_get`, `get_put`, `put_put` on chart $U_{\text{laws}}$ without checking the overlap $U_{\text{laws}} \cap U_{\text{coord}}$ (`view(s) == s[0]`). Flipping coordinates (`view(s) -> s[1]`, `update(s,a) -> (s[0], a)`) passes all 3 checks (`score = 1.0, PASS`).
- **`sheaf_physical_constraints`**: `judge.py` tests 3 fixed demand dicts. On Check 2 (`{route_A: 120, route_B: 60, route_C: 0}` with local capacity $100$ and switch $S_2(A+B) \le 100$), `judge.py` requires `abs((a1/a2) - 1.6666) < 0.05` (ratio `5:3`, i.e. clamping $120 \to 100$ on chart $U_{\text{route}}$ *before* scaling $100:60$ on chart $U_{\text{switch}}$). A globally proportional sheaf section that scales $120:60$ (`2:1 -> 66.67, 33.33`) **FAILS** Check 2, whereas a 3-entry lookup table **PASSES** (`score = 1.0`).
- **`stochastic_monad`, `neuro_symbolic_parser`, `monadic_reward`, `semiring_unification`**: Check isolated point charts (`right_identity = True` without sampling; $T=1.0$ only; 2 fixed strings; 2 cells of one $2\times 2$ matrix).

#### Dual B (Multi-Chart Local Sections That Fail Global Gluing):
- **`rope` (3-file codebase: `rope.py` [$U_1$], `attention.py` [$U_2$], `cache.py` [$U_3$])**:
  - Chart $U_1$ (`rope.py`): `RotaryEmbedding.apply_rope(x, offset=0, positions=None)` has gauge choices for coordinate pairing (adjacent `(2k, 2k+1)` vs split-half `(k, k+d/2)`) and how `offset` vs `positions` interact.
  - Chart $U_2$ (`attention.py`): `RotaryFeatureProjector.apply_chunk(x, cache)` must read `cache.position_offset()` *before* or *after* `cache.append(chunk_len)`.
  - Chart $U_3$ (`cache.py`): `PositionCache` tracks `tokens_seen`.
  - If Agent 2 in `attention.py` calls `cache.append(chunk_len)` *before* `offset = cache.position_offset()` (assuming `position_offset()` returns the start of the current chunk) while Agent 3 in `cache.py` returns cumulative `self.tokens_seen` after `append`, both pass their local unit tests on $U_2$ and $U_3$, yet their composition shifts every chunk by $+L$ (`chunked_equals_full` fails)!
- **`sheaf_schema_sync`, `sheaf_invariant_gluing`, `sheaf_physical_constraints`**:
  - Currently implemented in `rl_eval_generator` as single-file tasks (`migration.py`, `pipeline.py`, `route.py`), but each naturally decomposes into a 3-chart cyclic cover $X = U_1 \cup U_2 \cup U_3$ where pairwise agreements on $(U_1 \cap U_2)$ and $(U_2 \cap U_3)$ can still leave a 3-way cyclic obstruction on $(U_3 \cap U_1)$ ($\check{H}^1(\mathcal{U}, \mathcal{F}) \neq 0$)!

---

## MISSION 01 UNIFIED SEED (`mission-01/seed.yaml`)

- **Title:** Local-Section Validity vs. Global Sheaf Gluing in Multi-Module Agent Evaluation and Orchestration
- **Precise Research Questions:**
  1. **Dual A (Evaluator Gluing Audit):** Across `rl_eval_generator`'s relational and multi-module environments, what fraction of production judges (`judge.py`) and 4-variant oracle gates (`instance_oracle_gate.py`) certify **Locally Valid, Globally Non-Gluable Sections (`law_bypass`)** as `PASS (score = 1.0)` because they omit overlap restriction checks $\rho_{ij}(s_i) = \rho_{ji}(s_j)$?
  2. **Dual B (Multi-Chart Gluing Obstruction):** On multi-chart tasks $X = \bigcup_{i=1}^k U_i$ with gauge/cocycle obstructions on overlaps $U_i \cap U_j$, how often do locally valid sections $(s_1, \dots, s_k) \in \prod_i \mathcal{F}(U_i)$ fail global gluing under **Naive Local Decomposition (`Chart-Only`)** vs. **Pairwise Edge Checks (`Pairwise-Only`)**, and does specifying explicit **Sheaf Restriction Maps ($\rho_{ij}$)** restore global gluing?
- **Candidate Hypotheses:**
  - `H0` (Null): Local chart checks (`visible_tests.py` + current `judge.py` + syntactic interfaces) are already sufficient; `<10%` of environments admit Black-Box `law_bypass` passes and `<10%` of locally valid multi-chart tuples fail global gluing.
  - `H1` (Evaluator Gluing Blindness): Chart-restricted judges certify Black-Box `law_bypass` sections as `PASS (score = 1.0)` in $\ge 50\%$ of audited environments while failing an Overlap/Restriction-Aware Auditor (`Grader B`).
  - `H2` (Judge Internal Presheaf Contradiction): Judges whose point checks encode incompatible local assumptions (e.g., `sheaf_physical_constraints`) reject globally coherent sheaf sections (`reference_alt`), causing simultaneous Type I and Type II evaluation errors.
  - `H3` (Multi-Chart Gluing Obstruction & Restriction-Map Rescue): Tuples of locally valid sections $(s_1, \dots, s_k)$ that pass 100% of local chart tests $T(U_i)$ fail global gluing $T(X)$ at high rates ($>60\%$) under `Chart-Only` and `Pairwise-Only` protocols (due to gauge divergence and 3-way $\check{H}^1$ cocycle obstructions), whereas enforcing explicit **Sheaf Restriction Maps** ($\rho_{ij}$) reduces global gluing failure to $<5\%$.

---

## REQUIRED OUTPUT FORMAT FOR THEORIST (`P01-T`)

Please structure your response with the following exact sections:

1. **Formal Sheaf-Theoretic Framework (`P01-T-1`)**
   - Define the cover $\mathcal{U} = \{U_i\}_{i=1}^k$ of a task/specification $X$, the presheaf of local implementations $\mathcal{F}(U_i)$, the restriction morphisms $\rho_{ij}: \mathcal{F}(U_i) \to \mathcal{F}(U_i \cap U_j)$, the 0-coboundary operator $\delta^0(\{s_i\})_{ij}$, and the 3-way Čech 1-cocycle obstruction in $\check{H}^1(\mathcal{U}, \mathcal{F})$ where pairwise compatibility holds on spanning edges yet global gluing fails around the cycle.
   - Prove/show the exact duality between **Dual A (Chart-Only Judge Blindness / `law_bypass`)** and **Dual B (Multi-Agent Local Section Non-Gluability)**.
2. **Taxonomy of Gluing Obstructions (`P01-T-2`)**
   - Classify the exact obstruction types present in `rl_eval_generator`:
     - Type I-A: Temporal Horizon Truncation ($U_1 = \{t=1\}$ vs. $U_1 \cap U_2 = \{\text{state handoff } v_1 \mapsto v_2\}$)
     - Type I-B: Unanchored Gauge / Coordinate Automorphism (`categorical_lenses`, `rope` coordinate pairing)
     - Type I-C: Cyclic 3-Chart Holonomy / $\check{H}^1$ Obstruction (`sheaf_schema_sync` circular FKs, `sheaf_physical_constraints` 3-switch triangle, `rope` 3-module offset cycle)
     - Type II: Inconsistent Judge Presheaf ($\mathcal{F}_{\text{judge}}(X) = \emptyset$ for valid global sections)
3. **Sharpened Hypotheses & Exact Mathematical Predictions (`H0`–`H3` + any new `H4`)**
   - State formal conditions, quantitative predictions (including the combinatorial gauge-survival formula $P(\text{glue}) = \prod_{e} g_e^{-1}$ under naive local solving), and falsification criteria.
4. **Hidden Assumptions Register (`A01`–`Ann`)**
   - Identify every unstated premise in the unified seed.
5. **Decision Table Priors & Conditional Likelihoods (`P(H_i)` and `P(O_j | H_i)`)**
   - Define 4 mutually exclusive empirical observation regimes (`O1`, `O2`, `O3`, `O4`) and assign rough priors $P(H_i)$ and conditional likelihoods $P(O_j \mid H_i)$ (`very_high`, `high`, `moderate`, `low`, `very_low`) with an Expected Information Gain ($\operatorname{EIG}$) justification.
```
