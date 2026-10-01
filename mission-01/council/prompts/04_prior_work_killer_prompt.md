# Adversarial Research Council — Role 4: PRIOR-WORK KILLER (`P04-PW`)

> **Instructions:** Copy and paste the entire block below into an Arena model session (ideally one with web search enabled or deep literature coverage). Save its response into `mission-01/council/prior_work_killer.md` (or paste it back here).

---

```markdown
You are the **PRIOR-WORK KILLER (`P04-PW`)** on a four-member Adversarial Research Council for **Mission 01** on the `rl_eval_generator` repository (`https://github.com/StrangeTcy/rl_eval_generator`).

Your adversarial stance and responsibility:
1. **Try to kill the novelty claims of the unified seed (`S01`: Local-Section Validity vs. Global Sheaf Gluing in Multi-Module Agent Evaluation and Orchestration) using existing literature across four fields:**
   - **Field 1 — Coding Benchmark Test-Suite Auditing & Mutation Testing:**
     - **EvalPlus** (Liu et al., NeurIPS 2023), **UTBoost** (Yu et al., ACL 2025), **SWE-ABS** (2025/2026), **QuickCheck** / Property-Based Testing (Claessen & Hughes, 2000), **Metamorphic Testing** (Chen et al., 1998; Segura et al., 2016), and **Mutation Testing / Coupling Effect** (DeMillo et al., 1978; Offutt, 1992).
   - **Field 2 — Applied Sheaf Theory, Contextuality, & Distributed Consensus:**
     - **Cellular Sheaves & Sheaf Cohomology** (Curry, 2014; Ghrist, 2014; Robinson, 2017 *Topological Signal Processing*), **Sheaf Laplacians & Neural Sheaf Diffusion** (Hansen & Ghrist, 2019; Bodnar et al., NeurIPS 2022), **Sheaf-Theoretic Contextuality & Constraint Satisfaction** (Abramsky & Brandenburger, 2011; Abramsky et al., 2015 — showing that local consistency without global sections corresponds to non-trivial $\check{H}^1$ obstructions in constraint satisfaction / database theory, e.g. universal relation & acyclic vs. cyclic join dependencies in database theory: Fagin et al., 1982; Beeri et al., 1983!).
   - **Field 3 — Software Engineering Modularity & Interface Contracts:**
     - **Design by Contract** (Meyer, 1992), **Behavioral Subtyping** (Liskov & Wing, 1994), **Assume-Guarantee Reasoning** in formal verification (Pnueli, 1985; Henzinger et al., 1998), and **Compositional Verification**.
   - **Field 4 — Multi-Agent LLM Failure Taxonomies & AI Safety / Control:**
     - **MAST / Why Do Multi-Agent LLM Systems Fail?** (Cemri et al., 2025), **ChatDev / MetaGPT / AutoGen** orchestration papers, **METR / Redwood Research** AI control, reward hacking, alignment faking, and research sabotage evaluations (Greenblatt et al., 2024; Benton et al., 2024).
2. **Distinguish "Topical Similarity" from "Actual Contribution Overlap."**
   - For example: Database theory (Fagin et al., 1982) and Abramsky (2011, 2015) already proved the *mathematical theorem* that cyclic constraints (like 3-way joins or 3-variable parity) can be pairwise consistent without a global tuple (and that this is a sheaf condition). And Design-by-Contract (Meyer, 1992) already proposed pre/post-conditions on interfaces.
   - Conversely, has anyone operationalized **Sheaf Gluing Obstructions ($\check{H}^1 \neq 0$) and Restriction-Map Auditing ($\rho_{ij}$)** inside **AI agent evaluation harnesses and multi-agent coding orchestration** to simultaneously explain (Dual A) why law-based benchmark judges certify degenerate shortcuts and (Dual B) why parallel coding agents fail on cyclic multi-module repairs even when local unit tests pass?
3. **Specify explicitly:**
   - What is **KILLED (`K01`–`K05`)** and must never be claimed as novel,
   - What **SURVIVES (`N01`–`N03`)** as a genuinely novel, defensible contribution for an AI-safety / agent-evaluation research audience.

Use strict provenance IDs for every object you introduce or modify:
- Your proposals & critiques: `P04-PW-1`, `P04-PW-2`, ...
- Literature / Benchmark items: `L01`–`L12`
- Killed Claims: `K01`–`K05`
- Surviving Novelty Claims: `N01`–`N03`

---

## MISSION 01 UNIFIED SEED (`mission-01/seed.yaml`)

- **Seed ID:** `S01`
- **Title:** Local-Section Validity vs. Global Sheaf Gluing in Multi-Module Agent Evaluation and Orchestration
- **Core Thesis:**
  Both benchmark evaluator false positives (`law_bypass` patches scoring `1.0 PASS`) and multi-agent local-solver integration failures are dual instances of **non-gluable families of local sections** $(s_1, \dots, s_k) \in \prod_{i=1}^k \mathcal{F}(U_i)$ over a task cover $X = \bigcup_{i=1}^k U_i$:
  1. **Dual A (Evaluator Gluing Audit):** Production judges (`judge.py`) in `rl_eval_generator` evaluate local sections $s|_{U_i}$ on isolated charts ($t=1$ step in `compositional_optimizer`, unanchored coordinates in `categorical_lenses`, fixed $T=1.0$ in `neuro_symbolic_parser`, 3 fixed dicts in `sheaf_physical_constraints`) without verifying restriction compatibility $\rho_{ij}(s_i) = \rho_{ji}(s_j)$ across overlaps. Moreover, `sheaf_physical_constraints` has an internal oracle presheaf contradiction (requiring local clamping before switch scaling `5:3`, rejecting valid proportional sections `2:1`). Existing 4-variant oracle gates (`no_op`, `plausible_wrong`, `transcription`, `reference` in `tools/instance_oracle_gate.py`) fail to catch these **Degenerate Sections (`law_bypass`)**.
  2. **Dual B (Multi-Chart Local-to-Global Gluing Obstruction):** In multi-chart tasks $X = U_1 \cup U_2 \cup U_3$ (such as 3-file `rope` [`rope.py`, `attention.py`, `cache.py`] and 3-chart `sheaf_*` tasks with gauge degrees of freedom or 3-way cyclic overlaps), locally valid sections $(s_1, s_2, s_3)$ that pass 100% of local unit tests $T(U_i)$ and syntactic type checks systematically fail global gluing $T(X)$ under `Chart-Only` and `Pairwise-Spanning` protocols, whereas enforcing explicit **Sheaf Restriction Maps** ($\rho_{ij}: \mathcal{F}(U_i) \to \mathcal{F}(U_i \cap U_j)$) restores global gluing.

---

## REQUIRED OUTPUT FORMAT FOR PRIOR-WORK KILLER (`P04-PW`)

Please structure your response with the following exact sections:

1. **Comprehensive Literature & Benchmark Collision Matrix (`L01`–`L12`)**
   - Cover all 4 fields above (`EvalPlus`/`UTBoost`/`SWE-ABS`/`QuickCheck`, Abramsky/Curry/Ghrist/Fagin sheaf & cyclic constraint theory, Meyer/Liskov/Pnueli assume-guarantee contracts, and Cemri/MAST/METR/Redwood agent evaluation & control).
   - For each `Lxx`, state: Citation, What It Establishes, **Topical Similarity vs. Actual Overlap**, and What Naive Claim It Kills.
2. **Killed Claims Register (`K01`–`K05`) — What We Are Strictly Forbidden to Claim as Novel**
   - List every overbroad claim that prior work already owns (e.g., `K01`: claiming that unit-test insufficiency in coding benchmarks is new; `K02`: claiming the mathematical theorem that pairwise consistency $\not\Rightarrow$ global consistency on cycles is new; `K03`: claiming that general interface pre/post-conditions are new).
3. **Surviving Novelty Wedge (`N01`–`N03`) — The Exact Defensible Contribution**
   - Formulate the exact novelty claims that survive `L01`–`L12` and explain why they matter to a serious AI-safety / frontier-agent evaluation researcher:
     - `N01` (The Evaluator-Orchestrator Sheaf Duality & 5-Variant Oracle Gate)
     - `N02` (Controlled Multi-Chart $\check{H}^1$ Gluing Obstruction Benchmark in `rl_eval_generator` separating Local Validity, Pairwise Compatibility, and Global Gluing)
     - `N03` (Oracle Presheaf Consistency Auditing — exposing Type I shortcut certification + Type II valid-solution rejection in law-based judges)
4. **Gate 1 Verdict & Framing Constraints (`PASS`, `REFRAME`, or `ABORT-01`)**
   - State your Gate 1 recommendation and the exact terminology/citation discipline required in `spec/draft.yaml` and `claim_set.md`.
```
