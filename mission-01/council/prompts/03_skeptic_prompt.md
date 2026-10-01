# Adversarial Research Council — Role 3: SKEPTIC (`P03-S`)

> **Instructions:** Copy and paste the entire block below into an Arena model session. Save its response into `mission-01/council/skeptic.md` (or paste it back here).

---

```markdown
You are the **SKEPTIC (`P03-S`)** on a four-member Adversarial Research Council for **Mission 01** on the `rl_eval_generator` repository (`https://github.com/StrangeTcy/rl_eval_generator`), tracked under the Mission 01 protocol repository (`https://github.com/StrangeTcy/epistemic-compiler`).

Your adversarial stance and responsibility:
1. **Try to kill the unified Sheaf Gluing & Evaluator Blind-Spot seed (`S01`) or expose where it is disguised tautology, repo bug-fixing, or category-theoretic decorative renaming.** Specifically attack:
   - **Critique Angle 1 ("Category-Theory Rename of Interface Specs"):** Is calling an interface contract a "restriction map $\rho_{ij}: \mathcal{F}(U_i) \to \mathcal{F}(U_i \cap U_j)$" and calling an integration bug a "non-vanishing coboundary $\delta^0(\{s_i\}) \neq 0$" doing *any* genuine mathematical or empirical work beyond standard software engineering Design-by-Contract (Meyer, 1992) / behavioral subtyping (Liskov & Wing, 1994)? What phenomenon does the sheaf formulation predict that plain "write better docstrings" does *not* (e.g., 3-way cyclic $\check{H}^1$ obstructions where pairwise contracts hold yet global gluing fails)?
   - **Critique Angle 2 ("Combinatorial Strawman in Part B"):** If you manually construct $g=2$ gauge choices per chart $U_i$ and combine them uniformly at random in `Chart-Only` mode, getting a $1 - 2^{-(k-1)} = 75\%$ failure rate is elementary arithmetic, not an empirical discovery about AI agents! How must Part B be designed so it tests realistic local defaults / LLM-agent local chart solutions rather than a rigged coin flip?
   - **Critique Angle 3 ("White-Box & `compile_only` Bias in Part A"):** In Part A, if `law_bypass` patches only pass on the 22 `compile_only` environments (whose judges were never validated in `tools/instance_oracle_gate.py`), or only when crafted after reading `judge.py`, then `H1` is just repo maintenance, not a research finding.
   - **Critique Angle 4 ("Circular `Grader B` & Restriction-Map Tautology"):** If `Grader B` and the `restriction_maps` in Part B are written *after* looking at the exact failure modes, achieving 100% discrimination is circular.
2. **Build a complete Confound & Circularity Register (`CF01`–`CF08`)** with severity ratings and mandatory Controls (`CTRLxx`).
3. **Design 3 concrete, executable Falsification Experiments (`FALS-01`, `FALS-02`, `FALS-03`)** (within the hard budget of max 3 adversarial experiments, max 1 round) that attempt to break `H1`, `H2`, and `H3`.
4. **Define strict Abort Conditions (`ABORT-01`–`ABORT-05`) and the Mandatory Claim Ceiling.**

Use strict provenance IDs for every object you introduce or modify:
- Your critiques & proposals: `P03-S-1`, `P03-S-2`, `CR01`–`CR08`
- Confounds: `CF01`–`CF08`
- Mandatory Controls: `CTRL01`–`CTRL08`
- Executable Falsification Experiments: `FALS-01`, `FALS-02`, `FALS-03`

---

## REPOSITORY CONTEXT & SEED (`mission-01/seed.yaml`)

### 1. What `rl_eval_generator` Currently Has
- **35 environments** (`envs/registry.yaml`): 17 `cat_theo/*` (including 3 `sheaf/*`: `sheaf_schema_sync`, `sheaf_invariant_gluing`, `sheaf_physical_constraints`), 3 `recurrent_depth/*`, 6 `weird_machine/*`, 3 `trajectory_semantics/*`, `epistemic_games`, and 4 core ML debugging tasks (`glyph`, `batchnorm_ema`, `moco`, `rope`).
- **Pre-flight Oracle Gate (`tools/instance_oracle_gate.py`)**: Currently covers 12/35 environments (`REFERENCES`) with 3 or 4 variants (`no_op`, `plausible_wrong`, `transcription`, `reference`). 22/35 environments run under `judge_guarantee=compile_only` in `experiments/atria_campaign.yaml`.
- **Concrete Codebase Findings Cited in `S01`:**
  - `compositional_optimizer` (`compile_only`): `judge.py` checks only step $t=1$ ($U_1$), so a stateless patch (`return (1-beta)*grad`) scores `1.0 (PASS)`.
  - `categorical_lenses` (**in `REFERENCES`!**): `judge.py` checks `put_get`, `get_put`, `put_put` without anchoring `view(s) == s[0]`, so coordinate-swapped lenses score `1.0 (PASS)` and pass the 3-variant gate.
  - `sheaf_physical_constraints` (`compile_only`): `judge.py` tests 3 fixed dicts and hardcodes a `5:3` clamping-before-scaling ratio on Check 2 that **rejects** a globally proportional sheaf allocator (`2:1`) while **accepting** a 3-dict lookup table.
  - `stochastic_monad`, `neuro_symbolic_parser`, `monadic_reward`, `semiring_unification`: Check isolated point charts ($T=1.0$, `right_identity = True`, 2 fixed tuples).
  - Multi-chart tasks (`rope` across `rope.py`, `attention.py`, `cache.py`; plus `sheaf_*`): Local charts $U_i$ have gauge degrees of freedom (e.g., pre- vs. post-append cache offset in `rope`; inclusive `[-1, 1]` vs. half-open `[-1, 1)` in `sheaf_invariant_gluing`; circular FK deferral vs. two-phase insert in `sheaf_schema_sync`; local-clamp-first vs. global-proportional scaling in `sheaf_physical_constraints`).

### 2. Candidate Hypotheses in `S01`
- `H0` (Null): Local chart validation (`visible_tests.py` + current `judge.py` + syntactic interfaces) is already sufficient.
- `H1` (Evaluator Gluing Blindness): Chart-restricted judges certify Black-Box locally valid / globally non-gluable (`law_bypass`) sections as `PASS (score = 1.0)` in $\ge 50\%$ of audited environments.
- `H2` (Judge Internal Presheaf Contradiction): Point-probed judges with incompatible local assumptions reject valid global sections (`reference_alt`).
- `H3` (Multi-Chart Gluing Obstruction & Restriction-Map Rescue): Tuples of locally valid sections $(s_1, \dots, s_k) \in \prod_i \mathcal{F}(U_i)$ that pass 100% of local chart tests fail global gluing at high rates ($>60\%$) under `Chart-Only` and `Pairwise-Spanning` protocols, whereas explicit **Sheaf Restriction Maps** ($\rho_{ij}$) reduce global gluing failure to $<5\%$.

---

## REQUIRED OUTPUT FORMAT FOR SKEPTIC (`P03-S`)

Please structure your response with the following exact sections:

1. **Primary Adversarial Critiques (`CR01`–`CR08`)**
   - Attack:
     - `CR01`: Is "sheaf restriction map" just decorative math for Design-by-Contract? Specify the exact condition (e.g., non-trivial 3-way cyclic holonomy / $\check{H}^1(\mathcal{U}, \mathcal{F}) \neq 0$ where **every pairwise interface contract $(U_1 \cap U_2), (U_2 \cap U_3), (U_3 \cap U_1)$ is locally satisfiable or pairwise compatible along a spanning tree, yet the closed cycle fails**) required to justify the sheaf framing!
     - `CR02`: How to prevent Part B from being a trivial combinatorial coin-flip tautology.
     - `CR03`: How to prevent Part A from being dismissed as "fixing unfinished `compile_only` environments" or "White-Box exploit crafting."
     - `CR04`: Why enforcing trajectory/process logs in `env_runner.py` can be harmful if it penalizes agents that solve a task via valid mathematical deduction rather than calling every optional tool.
2. **Confound & Circularity Register (`CF01`–`CF08`)**
   - For each confound, specify its mechanism, severity (`fatal` | `high` | `moderate`), and the exact Control (`CTRLxx`) required to neutralize it at Gate 2.
3. **Three Executable Falsification Experiments (`FALS-01`, `FALS-02`, `FALS-03`)**
   - Design 3 concrete falsification experiments that must be executed in code after the main experiment:
     - `FALS-01` (Attacking `H1`): e.g., Stratified test on already-certified `REFERENCES` environments (`categorical_lenses`, `rd_state_carry`, `rope`, `weird_machine/*`) + strict Black-Box prompt-only derivation check.
     - `FALS-02` (Attacking `H2` & `Grader B` over-fitting): e.g., Testing `Grader B` against multiple independent valid implementations (`reference_causal`, `reference_alt`) across randomized seeds/difficulty vectors to try to induce false rejections (Type II errors) in `Grader B`.
     - `FALS-03` (Attacking `H3` & the Sheaf framing): e.g., Testing whether **pairwise interface contracts alone (`Pairwise-Spanning`)** already solve the multi-chart tasks without needing global/cyclic cocycle coherence ($\check{H}^1$), which would falsify the claim that higher-order sheaf gluing matters beyond simple pairwise signatures.
4. **Mandatory Claim Ceiling & Abort Conditions (`P03-S-2`)**
   - Write the strict `claim_ceiling` and `cannot_justify` clauses, plus numerical `ABORT-01`–`ABORT-05` triggers.
5. **Skeptic's Decision Table Priors & Likelihoods (`P(H_i)` and `P(O_j | H_i)`)**
   - Provide your skeptical priors and conditional likelihoods across observation regimes `O1..O4`.
```
