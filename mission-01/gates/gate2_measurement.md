# Gate 2 — Measurement, Decision-Table & Pre-Registration Gate (`mission-01/gates/gate2_measurement.md`)

- **Mission**: `mission-01`
- **Seed**: `S01` (Reframed at Gate 1: *Bidirectional Oracle Auditing and Compositional Gluing in Agent Benchmark Judges*)
- **Spec Audited**: `mission-01/spec/draft.yaml`

---

## 1. Gate 2 Checklist (`research_protocol/protocol.md` §3.2)

- [x] **Every Hypothesis (`H0`–`H5`) Has $\ge 1$ Operationalized Measurement (`M01`–`M10`)**:
  - `H0` $\leftrightarrow$ `M01`, `M02`, `M03`, `M05`
  - `H1` $\leftrightarrow$ `M01` ($\beta_A^{\text{glue}}, \beta_B^{\text{glue}}$ Type I only), `M02` ($\beta_A^{\text{all}}, \beta_B^{\text{all}}$ including Type 0), `M04` ($\text{ER}_{4\text{var}}$ vs. $\text{ER}_{6\text{var}}$)
  - `H2` $\leftrightarrow$ `M03` ($\gamma_A, \gamma_B$ Type II valid-solution false-rejection across $\ge 3$ independent `reference_alt` implementations per tested environment verified over $\ge 1,000$ inputs), `M04`
  - `H3` $\leftrightarrow$ `M05` ($\varphi_{\text{chart}}, \varphi_{\text{tree}}, \varphi_{\text{upToGauge}}, \varphi_{\text{circularAG}}, \varphi_{\text{sheaf}}$), `M06` (integer holonomy $\operatorname{hol}(\gamma) \in \mathbb{Z}$), `M09` (constraint predicate/LOC parsimony $\Delta\text{Pred}, \Delta\text{LOC}$)
  - `H4` $\leftrightarrow$ `M07` (solo-chart gauge concentration $\hat{\kappa}_e = \sum_c \hat{p}_{e,c}^2$ and effective gauge diversity $\hat{g}_e = 1/\hat{\kappa}_e$)
  - `H5` $\leftrightarrow$ `M08` (evaluator–orchestrator edge co-location $\text{Jaccard}(E_J, E_O)$)
- [x] **Calibrated Decision Table with Dual Priors ($\pi_T$ and $\pi_S$, Preserving `UD04` Without Averaging)**:
  - Observation regimes `O1`–`O6` partition the measurement space cleanly.
  - Expected Information Gain:
    - Under Theorist prior $\pi_T$ (`P01-T-9`): $\text{EIG}(\pi_T) = \mathbf{0.67\text{ bits}}$.
    - Under Skeptic hostile prior $\pi_S$ (`P03-S` §5): $\text{EIG}(\pi_S) = \mathbf{0.52\text{ bits}}$.
  - No row has uniform likelihoods; every observation regime shifts posterior mass decisively.
- [x] **Confound & Circularity Controls (`CTRL01`–`CTRL08`) Locked**:
  - `CTRL01`: Black-box context bundle SHA256 logging (excluding `judge.py`).
  - `CTRL02`: Strict stratification of Stratum A1 (`12 REFERENCES`: 5 Discovery + 7 Holdout) vs. Stratum A2 (`9 compile_only cat_theo`).
  - `CTRL03`: Pre-registration of `spec/approved.yaml` and `Grader B` restriction maps via Git commit SHA on `StrangeTcy/epistemic-compiler` prior to running the audit.
  - `CTRL04`: Explicit separation of deterministic gauge-orbit evaluation (`Track B-Mech`) from empirical solo-chart gauge concentration (`Track B-Emp`).
  - `CTRL05`: Mandatory inclusion of `Pairwise-Tree`, `Pairwise-UpToGauge`, and `Circular-AG` (`L11`) comparators against `Sheaf-Cocycle`.
  - `CTRL06`: Uncontaminated Holdout Slice (7 previously uninspected `REFERENCES` environments) + independent property-based truth oracles ($\ge 1,000$ random inputs per `reference_alt`).
  - `CTRL07`: AST predicate count and LOC parsimony comparison (`M09`).
  - `CTRL08`: Final code-artifact-only grading (episode trajectory logs inadmissible to pass/fail scoring).
- [x] **Strict Ontological Separation of `M01`–`M10` vs. `T01`–`T06`**:
  - Verified that all 6 engineering acceptance tests (`T01`–`T06`) test only synthetic fixtures, schema validity, SHA256 exclusion of `judge.py`, and zero regression on existing unit tests—**none** encode any desired scientific outcome for `H1`–`H5`.
- [x] **Mandatory `claim_ceiling`, `cannot_justify`, `killed_claims` (`K01`–`K05`), and `abort_conditions` (`ABORT-01`–`ABORT-05`)**:
  - Explicitly bound in Section 1 and Section 9 of `mission-01/spec/draft.yaml`.

---

## 2. Dual-Prior Posterior Update Matrix (`O1`–`O6`)

| Observation Regime | $P(O_j \mid \pi_T)$ | Modal Posterior under Theorist $\pi_T$ | $P(O_j \mid \pi_S)$ | Modal Posterior under Skeptic $\pi_S$ |
|---|---|---|---|---|
| **`O1` (Null / Local Parity)** | `0.103` | `H0` ($P(H_0 \mid O_1) = 0.68$) | `0.266` | `H0` ($P(H_0 \mid O_1) = 0.92$) |
| **`O2` (Type I Only; Sheaf Title Dies)** | `0.182` | `H1` ($0.48$), `H4` ($0.21$) | `0.181` | `H1` ($0.39$), `H4/Res` ($0.30$) |
| **`O3` (Bidirectional `N03` + Shared-Prior `H4`)** | `0.235` | `H4` ($0.29$), `H2` ($0.24$), `H1` ($0.23$) | `0.225` | `H4/Res` ($0.44$), `H2` ($0.25$), `H1` ($0.20$) |
| **`O4` (Full Bidirectional + Cycle Holonomy + Duality)** | `0.369` | `H3` ($0.38$), `H5` ($0.22$), `H1` ($0.20$), `H2` ($0.15$) | `0.201` | `H1` ($0.30$), `H2` ($0.28$), `H3` ($0.28$) |
| **`O5` (`Grader B` Overfit — `ABORT-02`)** | `0.055` | Triggers `ABORT-02` | `0.061` | Triggers `ABORT-02` |
| **`O6` (Holdout Collapse — `ABORT-05`)** | `0.056` | Triggers `ABORT-05` | `0.052` | Triggers `ABORT-05` |

---

## 3. Gate 2 Decision Log
- **Decision**: `APPROVE_AND_FREEZE` (`mission-01/spec/draft.yaml` frozen to `mission-01/spec/approved.yaml` and locked on `StrangeTcy/epistemic-compiler` prior to Part A/B execution and prior to inspecting the 7 Holdout `REFERENCES` environments)
- **Action Upon Approval**: Copy `mission-01/spec/draft.yaml` to `mission-01/spec/approved.yaml`, commit and push to `StrangeTcy/epistemic-compiler` to lock the pre-registration Git SHA (`CTRL03`), and generate the bounded Work Packages (`mission-01/work_packages/WP-01..WP-07`) for **Gate 3**.
- **Signed By**: Human Research Director (`ask_user` Gate 2 sign-off)
- **Timestamp**: `2026-10-01T16:28:00Z`

