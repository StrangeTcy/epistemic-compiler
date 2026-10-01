# Gate 1 — Question & Novelty Gate (`mission-01/gates/gate1_question.md`)

- **Mission**: `mission-01`
- **Seed**: `S01` (*Local-Section Validity vs. Global Sheaf Gluing in Multi-Module Agent Evaluation and Orchestration*)
- **Inputs Audited**:
  - `mission-01/seed.yaml`
  - `mission-01/council/theorist.md` (`P01-T-1`..`P01-T-9`, `H0`..`H5`, `A01`..`A19`)
  - `mission-01/council/experimentalist.md` (`P02-E-1`, `M01`..`M07`, `CTRL01`..`CTRL06` + `F-005` repo-grounding audit)
  - `mission-01/council/skeptic.md` (`P03-S-1`..`P03-S-2`, `CR01`..`CR08`, `CF01`..`CF08`, `FALS-01`..`FALS-03`, `ABORT-01`..`ABORT-05`)
  - `mission-01/council/prior_work_killer.md` (`P04-PW-3`..`P04-PW-7`, `L01`..`L12`, `K01`..`K05`, `N01`..`N03`, `C1`..`C8`)
  - `mission-01/critiques/cross_critique.md` (`CR01`..`CR12`, `UD01`..`UD04`)

---

## 1. Gate 1 Checklist (`research_protocol/protocol.md` §3.1)

- [x] **Novelty & Prior-Work Collision Audit (`P04-PW`)**:
  - Audited against 12 prior-work anchors (`L01`–`L12`): `EvalPlus` (`L01`), `UTBoost` (`L02`), `UIUC Agentic Benchmark Checklist` (`L03`), `QuickCheck / Metamorphic Testing` (`L04`), `Mutation Testing` (`L05`), `Cellular Sheaves / Čech Cohomology` (`L06`), `Sheaf Contextuality & Database Join Acyclicity` (`L07`), **`Schmid April 2025 Prospectus on Applied Sheaf Theory for Multi-Agent AI/RL (arXiv:2504.17700)` (`L08`)**, `Neural Sheaf Diffusion` (`L09`), `Design-by-Contract` (`L10`), **`Circular Assume-Guarantee Verification` (`L11`)**, and `MAST / AI Control` (`L12`).
  - **Killed Claims (`K01`–`K05`)**: Bound as hard exclusions (no claim of mathematical novelty, no claim of being first to propose sheaf cohomology for multi-agent AI, no claim that 5-variant mutation gating or relational testing is novel, no citation of unverifiable `SWE-ABS`).
  - **Surviving Novelty Wedges (`N01`–`N03`)**:
    1. **`N03` (Primary Unoccupied Ground — Strong)**: **Bidirectional Oracle Presheaf Audit** — simultaneously measuring **Type I Shortcut Certification ($\beta_A^{\text{glue}}$)** and **Type II Valid-Solution Rejection ($\gamma_A$, oracle presheaf inconsistency / over-anchored gauge $G_{\text{judge}} \subsetneq G_{\text{spec}}$)** on the same environment cohort, and showing how over-anchored judges manufacture reward hacking by rejecting valid alternative gauges (`reference_alt`) while passing degenerate sections.
    2. **`N01` (Evaluator-as-Presheaf Duality — Conditional on `ABORT-01`)**: Placing the presheaf on **the benchmark evaluator (`judge.py`)** rather than the agent (`L08`), and testing whether judge unchecked overlap edges $E_J$ co-locate with multi-chart gluing failure edges $E_O$ (`H5`: $\text{Jaccard}(E_J, E_O) \ge 0.70$).
    3. **`N02` (Marginal Yield of Cocycle/Holonomy Enforcement over `Circular-AG` + Ecological Gauge Diversity $\hat{g}$ / $\hat{\kappa}_e$)**: Measuring incremental global-gluing failure reduction across `Chart-Only` $\to$ `Pairwise-Tree` $\to$ `Pairwise-UpToGauge` $\to$ `Circular-AG` (`L11`) $\to$ `Sheaf-Cocycle`, plus solo-agent convention concentration (`H4`).
- [x] **Non-Triviality**:
  - `H0`..`H5` are genuinely contested between Theorist (`P01-T`, modal forecast `O4`, $\text{EIG}=0.67\text{ bits}$) and Skeptic (`P03-S`, modal forecast `O3`/`O4`).
- [x] **Value**:
  - Directly answers a high-leverage frontier-safety and benchmark-engineering question: when do RL/agent benchmark verifiers simultaneously **over-certify shortcuts (Type I)** and **under-certify valid unconventional solutions (Type II)**, and when do multi-chart interfaces exhibit cyclic holonomy beyond standard pairwise / circular assume-guarantee contracts?
- [x] **Scope Discipline**:
  - Capped to `H0`–`H5`, strictly adhering to `C1`–`C8` and `CTRL01`–`CTRL08`.

---

## 2. Recommended Gate 1 Verdict: **`REFRAME` (Proceed to Gate 2 under `P04-PW` & `P03-S` Constraints)**

Per `P04-PW` (`P04-PW-7`) and `P03-S` (`P03-S-2`), Mission 01 is **reframed** from *"Sheaf Cohomology for Multi-Agent AI"* (killed by `L06`–`L08`, `K02`) to:

> **Reframed Mission 01 Title & Thesis (`N03` + `N01` + `N02`)**:
> *"Bidirectional Oracle Auditing and Compositional Gluing in Agent Benchmark Judges: Measuring Type I Shortcut Certification, Type II Valid-Solution Rejection, and Multi-Chart Holonomy"*
> *(Subject to `C7` / `ABORT-03`: the words "sheaf," "cohomology," and "cocycle" are carried strictly as attributed mathematical notation [`C2`, `C4`] and may appear in the final paper title/abstract if and only if `Sheaf-Cocycle` beats `Pairwise-Tree` and `Circular-AG` by $\ge 5\text{pp}$ on $\ge 2$ environments.)*

---

## 3. Human Gate 1 Decisions Required (`UD01`–`UD03`)

To sign off on **Gate 1** and advance immediately to **Gate 2 (`mission-01/gates/gate2_measurement.md`)** and **Part VII (`mission-01/spec/draft.yaml`)**, the Human Research Director's decision is requested on:

1. **Gate 1 Verdict & Framing (`UD01`)**:
   - Approve the **`REFRAME`** verdict centering on **`N03` (Bidirectional Type I + Type II Oracle Presheaf Audit)** + **`N01` (Evaluator-as-Presheaf Duality `H5`)** + **`N02` (Marginal Yield over `Circular-AG` & Gauge Diversity `H3`/`H4`)**, enforcing `C1`–`C8` and `K01`–`K05`.
2. **Part A Environment Cohort Scope (`UD03`)**:
   - **Option A (Expanded 21-Environment Stratified Cohort — Recommended by `P03-S` `CR03`/`CR07`)**: Audit **all 12 `REFERENCES` environments** (`Stratum A1`, where the 7 previously uninspected `REFERENCES` environments serve as the uncontaminated Holdout Slice for `CR07`) **plus** all **9 `compile_only` `envs/cat_theo/*` environments** (`Stratum A2`), reported strictly separately.
   - **Option B (Original 14-Environment Cohort)**: Keep the 14 environments from `seed.yaml` (5 `REFERENCES` in Stratum A1 + 9 `compile_only` `cat_theo` in Stratum A2).
3. **Part B Execution Scope (`UD02`)**:
   - **Option A (Two-Track Part B in Sandbox + Optional External Arena Sample)**: Run **Track B-Mech** (complete deterministic execution across `Chart-Only`, `Pairwise-Tree`, `Pairwise-UpToGauge`, `Circular-AG` [`L11`], and `Sheaf-Cocycle` over the enumerated gauge orbits $\mathcal{G}(U_{ij})$ on the multi-chart environments, measuring exact integer holonomy $\operatorname{hol}(\gamma) \in \mathbb{Z}$ and constraint LOC/predicate parity `CTRL07`) **plus** a bounded solo-chart completion sample (`Track B-Emp`), enforcing the `CTRL04` `claim_ceiling` on ecological agent rates.
   - **Option B (Full External Multi-Model Sampling)**: Pause at Part IX for human-dispatched multi-model completions ($N \ge 30 \times 3$ families) before concluding `N02`.

---

## 4. Gate 1 Decision Log
- **Decision**: `PENDING HUMAN SIGN-OFF` (`PASS` | `REFRAME` | `ABORT`)
- **Signed By**: _Awaiting Human Research Director_
- **Timestamp**: _Pending_
