# Human Gate 3 Packet: Execution, Contract Audit & Falsification Review (`mission-01`)

- **Gate ID**: `GATE-03`
- **Mission**: `mission-01`
- **Pre-Registration Lock (`CTRL03`)**: `cbd4e4a081d0b5b1af8a062b6cdf5c4a4ac7d4e7` (`StrangeTcy/epistemic-compiler`)
- **Target Benchmark**: `StrangeTcy/rl_eval_generator` (`branch: mission-01/sheaf-gluing-protocol`)
- **Status**: `PASS_LIMITED_DIAGNOSTIC_HUMAN_SIGNED_OFF`
- **Human Decision:** `accept_bounded_record` (Gate 3 only; F-012 in the friction log)
- **Scope of Sign-Off:** Proceed to Gate 4 as a limited V0 diagnostic; this is not approval of sheaf/cohomology, H4/H5, calibrated posterior, or multi-agent efficacy claims.

---


## Gate 3 Methodological Review Notice (`REV-01`)

The user supplied an external review before Gate 3 sign-off. Its core correction is accepted: an ordinary sheaf cannot exhibit “all restrictions agree but no global section.” The executed work used pre-registered operational predicates and a finite variant generator; it did not establish a sheaf/cohomology theorem. The independent multi-agent comparison A/B/C was not run. The post-run overlap manifest is retrospective only. A source audit additionally found that M07's “sample” counts and M08's E_J/E_O edges are hard-coded, and Grader B shares its evaluator function with TruthOracle; those values are quarantined as non-independent/non-empirical. Do not rewrite the frozen registration; use `reviews/REV-01_methodological_review.md` for full disposition.

The `rope` example is a strong candidate for a **new** Dual-B experiment because the actual task spans `rope.py`, `attention.py`, and `cache.py`. A future contract must specify that the chunk's starting `position_offset()` is read before `append(chunk_len)` advances the cache and that `rope.py` honors the absolute offset (the current `_angles()` uses `torch.arange(seq_len)` when positions are omitted). This candidate contract was not the treatment tested in Mission 01.

## 1. Work Package Execution & Cross-Artifact Test Matrix (`WP-01`..`WP-07`)

All 7 bounded Work Packages (`WP-01`..`WP-07`) completed. The initial recorded combined command `pytest -q tests/test_scoring.py tests/test_generator.py tests/test_bidirectional_audit_harness.py tests/test_multichart_gluing_harness.py` returned **17 passed in 7.78s**. A later repeat in the current sandbox could not collect two harness modules because `torch` is unavailable (`ModuleNotFoundError`); no fresh rerun pass is claimed. The initial run was a combined engineering-test run—not 17 mathematical gluing assertions. Execution involved code/test changes (including the WP-06 judge-path inspection fix, an initial WP-07 schema-key failure followed by correction, and addition of T06). Those interventions were not fully logged in real time; therefore zero intervention burden and M10/κ values are invalid and not estimable. See `reviews/post_run_analysis_errata.yaml` and `reviews/REV-01_methodological_review.md`.

| Work Package | Workstream | Primary Artifacts | Executed cross-artifact checks (not mathematical restriction maps) | Acceptance Tests | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`WP-01`** | Black-box provenance | `tools/blackbox_context_bundler.py`, `mission-01/results/blackbox_hashes.json` | 21 environment hashes; `judge_excluded: true`; seed `42` | `T05` (`PASS`) | `completed` |
| **`WP-02`** | Constructed oracle implementation | `tools/grader_b_and_truth_oracles.py`, `tests/test_bidirectional_audit_harness.py` | Grader B wraps `evaluate_truth_oracle()` / same `AUDIT_DISPATCH`; 170/170 agreement is by design | `T01`, `T02`, `T05` (`PASS`) | `completed` |
| **`WP-03`** | Part A / Stratum A1 | `tools/stratum_a1_audit.py`, `mission-01/results/part_a_stratum_a1.json` | 12 A1 environments; 89 evaluations; 29 `reference_alt` variants; provenance/polarity assertions | `T01`, `T05`, `T06` (`PASS`) | `completed` |
| **`WP-04`** | Part A / Stratum A2 | `tools/stratum_a2_audit.py`, A2/FDR/Type-II artifacts | 9 A2 environments; 81 evaluations; 27 `reference_alt` variants; `CTRL05=True` | `T01`, `T02`, `T05`, `T06` (`PASS`) | `completed` |
| **`WP-05`** | Deterministic Part B benchmark | `tools/multichart_gluing_benchmark.py`, `mission-01/results/part_b_multichart_gluing.json` | 6 tasks × 27 generated workspaces = 162; five implemented protocol predicates | `T03` (`PASS`) | `completed` |
| **`WP-06`** | Gauge/parsimony analysis | `tools/gauge_and_parsimony_analysis.py`, `mission-01/results/gauge_duality_parsimony.json` | Consumes Part B outputs; reports `M07`–`M09` | `T04` (`PASS`) | `completed` |
| **`WP-07`** | Falsification/synthesis | `tools/run_falsification_suite.py`, WP-07 outputs | FALS-01..03, abort flags, aggregate schemas; posterior/M10 values quarantined by errata | Combined suite (`17 passed`) | `completed` |

---

## 2. Part A Results: Bidirectional Judge / Truth-Oracle Audit (`M01`..`M04`; “presheaf” is historical framing, not a formal result)

Per `CTRL02` (`P03-S`), Stratum A1 (`REFERENCES`, 12 environments that previously underwent `tools/instance_oracle_gate.py` hardening) and Stratum A2 (`compile_only` `cat_theo`, 9 environments without reference-oracle hardening) are reported separately alongside the pooled 21-environment summary. **Terminology caveat:** `beta_A_glue` / “Type I gluing” are frozen field labels; operationally they count judge acceptance of the constructed bypass variants, not a formally defined sheaf-gluing failure. **Oracle caveat:** `evaluate_grader_b()` calls `evaluate_truth_oracle()`, which dispatches the same `AUDIT_DISPATCH` function. Therefore 170/170 Grader B/TruthOracle agreement is by implementation design, not independent validation of the oracle. Part A compares existing judges with a constructed reference oracle whose correctness still requires independent review.

### 2.1 Stratified Summary Table (`M01`, `M02`, `M03`, `M04`)

Wilson 95% intervals for the recorded integer proportions are in `results/part_a_confidence_intervals_addendum.json`. This is a post-run reporting addendum using the pre-registered helper; because the cohorts are fixed enumerations rather than probability samples, the intervals are model-based and do not establish population generalization.

| Stratum / Slice | Envs ($N$) | Evaluations | `Grader A` Type I Gluing Blindness ($\beta_{A,\text{glue}}$) | `Grader A` Total False-Pass Rate ($\beta_{A,\text{all}}$) | `Grader B` False-Pass Rate ($\beta_B$) | `Grader A` Type II Gauge Rejection ($\gamma_A$ Env / Variant) | `Grader B` Type II Rejection ($\gamma_B$) | `Grader A` $\text{ER}_4 \to \text{ER}_6 \to \text{ER}_7$ | `Grader B` $\text{ER}_{4,6,7}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Stratum A1 (`Discovery`)** | 3 | 25 | **33.33%** (`1/3`: `categorical_lenses`) | **33.33%** (`1/3`) | **0.00%** (`0/3`) | **0.00%** (`0/3` envs, `0/7` alts) | **0.00%** | `1.000 -> 0.944 -> 0.905` | `1.000` |
| **Stratum A1 (`Holdout`)** | 9 | 64 | **0.00%** (`0/9` Type I-A) | **11.11%** (`1/9`: `ci_dependency_graph` Type 0) | **0.00%** (`0/9`) | **0.00%** (`0/9` envs, `0/22` alts) | **0.00%** | `1.000 -> 1.000 -> 0.984` | `1.000` |
| **Stratum A1 Total (`REFERENCES`)** | **12** | **89** | **8.33%** (`1/12`) | **16.67%** (`2/12`) | **0.00%** (`0/12`) | **0.00%** (`0/12` envs, `0/29` alts) | **0.00%** | `1.000 -> 0.986 -> 0.964` | `1.000` |
| **Stratum A2 (`compile_only`)** | **9** | **81** | **44.44%** (`4/9`) | **55.56%** (`5/9`) | **0.00%** (`0/9`) | **44.44%** (`4/9` envs, **25.93%** `7/27` alts; **22.22%** systematic $\ge 2/3$) | **0.00%** | `0.944 -> 0.852 -> 0.873` | `1.000` |
| **Pooled All 21 Envs** | **21** | **170** | **23.81%** (`5/21`) | **33.33%** (`7/21`) | **0.00%** (`0/21`) | **19.05%** (`4/21` envs, **12.50%** `7/56` alts) | **0.00%** | `0.976 -> 0.929 -> 0.925` | `1.000` |

### 2.2 Per-Environment Bidirectional Audit Breakdown (All 21 Environments)

| Env ID | Stratum | `Grader A` False Passes (Type 0 / Type I / Trans.) | `Grader A` Type II Rejected Oracle-Accepted Gauges | Grader B / TruthOracle output (same dispatcher) | Structural Mechanism |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `rope` | `A1_Discovery` | None (`0/5`) | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | Hardened `judge.py` checks streaming cache offset and rotation equivariance. |
| `rd_state_carry` | `A1_Discovery` | None (`0/5`) | `0/1` (`alt_1` passes) | `7/7` (`100%`) | Hardened `judge.py` checks multi-step recurrent state handoff. |
| `categorical_lenses` | `A1_Discovery` | **`law_bypass_type0` (`PASS`)**, **`law_bypass_type1` (`PASS`)** | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | **Type 0 + Type I-A**: `Grader A` checks `PutGet`/`GetPut`/`PutPut` on a single trajectory without testing statelessness (`Type 0`) or the base-space coordinate anchor `view((x,y))==x` (`Type I-A`, coordinate-swapped lens `view(s)=s[1], update(s,a)=(s[0],a)` passes `1.0`). |
| `moco` | `A1_Holdout` | None (`0/5`) | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | Hardened `judge.py` verifies EMA momentum update and queue pointer invariance. |
| `glyph` | `A1_Holdout` | None (`0/5`) | `0/1` (`alt_1` passes) | `7/7` (`100%`) | Hardened `judge.py` verifies MSE + cosine loss and optimizer step. |
| `epistemic_games` | `A1_Holdout` | None (`0/5`) | `0/1` (`alt_1` passes) | `7/7` (`100%`) | Hardened `judge.py` verifies exact rational Bayesian posterior & indistinguishability. |
| `regex_state_machine` | `A1_Holdout` | None (`0/5`) | `0/2` (`alt_1..2` pass) | `8/8` (`100%`) | Hardened `judge.py` verifies epsilon-closure fixed point and Kleene star matching. |
| `sql_fixed_point` | `A1_Holdout` | None (`0/5`) | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | Hardened `judge.py` verifies cyclic transitive closure termination. |
| `css_state_machine` | `A1_Holdout` | None (`0/5`) | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | Hardened `judge.py` verifies `:not()` recursion and `!important` cascade lattice. |
| `spreadsheet_dataflow` | `A1_Holdout` | None (`0/5`) | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | Hardened `judge.py` verifies cycle detection and reactive topological re-evaluation. |
| `template_interpreter` | `A1_Holdout` | None (`0/5`) | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | Hardened `judge.py` verifies `SandboxedEnvironment` blocks SSTI dunder traversal. |
| `ci_dependency_graph` | `A1_Holdout` | **`law_bypass_type0` (`PASS`)** | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | **Unscripted Holdout Type 0 Finding**: `Grader A` only tests DAGs where parent job IDs precede child job IDs in dictionary iteration order; a single-pass non-convergent loop passes `Grader A` (`1.0`) but fails on reverse-ordered chains (`J1->J2->J3`). |
| `compositional_optimizer` | `A2_CompileOnly` | **`plausible_wrong` (`PASS`)**, **`law_bypass_type1` (`PASS`)** | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | **Type I-B**: `Grader A` only checks a single step from zero velocity (where $v_1 = (1-\beta)g$ equals memoryless scaling) and never checks multi-step recurrence at $t \ge 3$. |
| `functorial_augmentation` | `A2_CompileOnly` | None (`0/5`) | **`1/3` rejected** (`alt_3` `score=0.417, FAIL`) | `9/9` (`100%`) | **Type II**: `Grader A` rejects valid `[B, 1, D]` broadcast scaling gauge (`alt_3`) even though it satisfies exact $T_\alpha \circ T_\beta = T_{\alpha\beta}$ equivariance. |
| `monadic_reward` | `A2_CompileOnly` | **`law_bypass_type1` (`PASS`)** | **`1/3` rejected** (`alt_2` `score=0.633, FAIL`) | `9/9` (`100%`) | **Bidirectional Type I + Type II**: `Grader A` only runs `run_fn([])` from an empty state (missing `law_bypass_type1` which overwrites prior log state and breaks Kleisli `bind` composition!), AND over-constrains the log string gauge to `"processed {val}"` (rejecting `"transition:{v0}->{v0+1}"` in `alt_2`). |
| `neuro_symbolic_parser` | `A2_CompileOnly` | **`law_bypass_type1` (`PASS`)** | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | **Type I-B**: `Grader A` only tests $x = y$ at $T=1.0$ (`law_bypass_type1` `torch.minimum(x,y) - T*log(2)` matches exact value and $\nabla=(0.5,0.5)$ at $x=y$, but has discontinuous step gradients for $x \neq y$). |
| `semiring_unification` | `A2_CompileOnly` | **`transcription` (`PASS`)** | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | **Point-Test Collapse**: `Grader A` only tests positive identities where the correct return list is all-`True`; `return [True] * len(pairs)` passes `Grader A` (`1.0`) without checking a single non-distributive counterexample! |
| `sheaf_physical_constraints` | `A2_CompileOnly` | None (`0/5`) | **`3/3` rejected** (`alt_1..3` `score=0.633, FAIL`) | `9/9` (`100%`) | **Systematic Type II (`100%` alt rejection)**: `prompt.md` specifies only local switch caps ($\le 100$) and global cap ($\le 150$), leaving the fair projection gauge under-specified; `Grader A` hardcodes one specific per-route ratio formula and rejects simultaneous uniform scaling (`alt_1`), sequential pairwise switch scaling (`alt_2`), and global-first scaling (`alt_3`). |
| `sheaf_schema_sync` | `A2_CompileOnly` | None (`0/5`) | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | `Grader A` and `Grader B` both accept two-phase `NULL`+`UPDATE` and `PRAGMA defer_foreign_keys` gauges. |
| `sheaf_invariant_gluing` | `A2_CompileOnly` | None (`0/5`) | **`2/3` rejected** (`alt_1, alt_3` `score=0.80, FAIL`) | `9/9` (`100%`) | **Systematic Type II (`66.7%` alt rejection)**: `pipeline.py`'s docstring states `discretize` maps `x in [-1.0, 1.0] to [0, 99]`, yet `Grader A` tests `discretize(1.0)` in isolation and demands it still raise `IndexError`, rejecting both Chart 2 clamping (`alt_1`) and joint Chart 1+2 clamping (`alt_3`). |
| `stochastic_monad` | `A2_CompileOnly` | **`law_bypass_type1` (`PASS`)** | `0/3` (`alt_1..3` pass) | `9/9` (`100%`) | **Type I-A**: `Grader A` only checks simplex normalization $\sum p_i = 1$ without checking Markov transition law $p_{\text{out}} = p_{\text{in}} T$; returning the row-average stationary distribution `transition_matrix.mean(dim=0)` ignores `state_probs` completely and passes `Grader A` (`1.0`). |

---

## 3. Part B Results: Deterministic Multi-Chart Compatibility Benchmark (`M05`..`M09`; historical “gluing/holonomy” labels are implementation labels)

### 3.1 Track B-Mech: 5-Protocol Gluing Obstruction Comparison across 162 Glued Workspaces (`M05`, `M06`)

Across the 6 Part B environments, each chart $U_i$ ($i \in \{1,2,3\}$) was instantiated with $|\mathcal{G}(U_i)| = 3$ locally valid sections ($3^3 = 27$ glued workspaces per environment; $162$ workspaces total). Every glued workspace was evaluated by the runtime `TruthOracle`:

**Scope limitation:** these are deterministic generated workspace/gauge-orbit cases, not independent LLM-agent outputs and not the proposed Protocol A/B/C causal comparison. `Sheaf-Cocycle` denotes the implemented checker arm; the results do not by themselves establish a formal sheaf, a Čech cohomology class, or ecological agent failure rates.

| Environment | Globally Valid Sections | `Chart-Only` $\Phi$ / CondFPR | `Pairwise-Tree` $\Phi$ / CondFPR | `Pairwise-UpToGauge` $\Phi$ / CondFPR | `Circular-AG` (`L11`) $\Phi$ / CondFPR | `Sheaf-Cocycle` $\Phi$ / CondFPR | Non-Zero $\operatorname{hol}(\gamma)$ Hollow Cycles |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `rope` | `14/27` | `0.4815` / `0.4815` | `0.1852` / `0.2632` | `0.4815` / `0.4815` | `0.0370` / `0.0667` | **`0.0000` / `0.0000`** | `1` (`(1,1,1)` $\mathbb{Z}_2$ holonomy $=3$) |
| `rd_state_carry` | `5/27` | `0.8148` / `0.8148` | `0.0741` / `0.4000` | `0.1481` / `0.4444` | `0.0370` / `0.3333` | **`0.0000` / `0.0000`** | `1` (`(1,1,1)` channel-swap cycle) |
| `sheaf_schema_sync` | `20/27` | `0.2593` / `0.2593` | `0.1111` / `0.1304` | `0.2593` / `0.2593` | `0.1481` / `0.1667` | **`0.0000` / `0.0000`** | `4` (3-table FK deadlock $\operatorname{hol}=3$) |
| `sheaf_invariant_gluing` | `11/27` | `0.5926` / `0.5926` | `0.1481` / `0.2667` | `0.2222` / `0.3529` | `0.0741` / `0.1538` | **`0.0000` / `0.0000`** | `2` (`(0,1,0)` leak & `(2,2,2)` double-shift) |
| `compositional_optimizer` | `8/27` | `0.7037` / `0.7037` | `0.2593` / `0.4667` | `0.4074` / `0.5789` | `0.0741` / `0.2000` | **`0.0000` / `0.0000`** | `2` (shared shape-key collision cycle) |
| `sheaf_physical_constraints` | `5/27` | `0.8148` / `0.8148` | `0.1852` / `0.5000` | `0.2593` / `0.5833` | `0.0741` / `0.2857` | **`0.0000` / `0.0000`** | `2` (3-switch deferred cap cycle) |
| **Mean (All 6 Envs)** | **`63/162`** | **`0.6111` / `0.6111`** | **`0.1605` / `0.3378`** | **`0.2963` / `0.4501`** | **`0.0741` / `0.2010`** | **`0.0000` / `0.0000`** | **`12` hollow-cycle failures** |

### 3.2 Constructed M07/M08 Metadata and Code-Parsimony Audit (`M09`)

1. **`M07` (`H4` Solo-Chart Gauge Concentration — quarantined as non-empirical):**
   - The generated JSON reports mean $\hat{\kappa}_e=0.6000$ and $\hat{g}_e=2.1242$. However, `tools/gauge_and_parsimony_analysis.py` hard-codes `SOLO_CHART_EMPIRICAL_SAMPLES` as literal five-count tables; no raw independent completions or model-run IDs substantiate them. These values are deterministic calculations from hand-entered counts, not empirical solo-agent observations. **Do not claim H4 from M07.**
2. **`M08` (`H5` Evaluator–Orchestrator Duality Co-Location — quarantined as hand-coded metadata):**
   - The reported arithmetic is `16/18 = 0.8889`, but `E_J` and `E_O` are literal entries in `NERVE_METADATA` in `tools/multichart_gluing_benchmark.py`. This is a code-internal metadata comparison, not independently measured co-location. **Do not claim H5 from M08.**
3. **`M09` (`CTRL07` Grader Complexity & Parsimony Audit)**:
   - The registered source-count routine reports **`241` AST predicates in the dispatched Grader B audit functions vs. `178` in the Grader A judge files** ($\text{Pred}(B)/\text{Pred}(A) = \mathbf{1.3539} \le 1.50$; `0.8014` on Stratum A1 and `3.4595` on Stratum A2 where `compile_only` judges had only 4 predicates per file) and **`943` non-comment LOC vs. `2,243`** ($\text{LOC}(B)/\text{LOC}(A) = \mathbf{0.4204} \le 1.00$). This is a source-size count, not a measurement of accuracy or efficiency.

---

## 4. Executable Falsification (`FALS-01`..`FALS-03`), Abort Triggers & Quarantined Decision-Table Reweighting

### 4.1 Falsification Budget & Results (`R05`)
- **Budget**: `3/3` pre-registered adversarial experiments executed (`FALS-01`, `FALS-02`, `FALS-03`/`FALS-03b`); `0/1` recursive rounds used.
- **`FALS-01` (FDR Cohort Sensitivity)**: Confirmed that `Grader A`'s Effective Resolution on Stratum A2 drops from `0.9444` (`FDR = 18.18%`) on the 4-variant baseline to `0.8519` (`FDR = 27.27%`, `FNR = 11.11%`) on the 6-variant cohort, whereas Stratum A1 shifts by only `3.57 pp` (`1.000 -> 0.9643`). The constructed `Grader B`/TruthOracle dispatcher yields `ER = 1.000` (`FDR = 0.0%`, `FNR = 0.0%`) by shared implementation; this is not independent evidence of oracle accuracy.
- **`FALS-02` (Multi-Variant Type II Gauge Audit)**: Verified `CTRL05 = True` (`0` syntax/import errors across 56 `reference_alt` runs). Confirmed `0/12` Type II rejection on Stratum A1 (`REFERENCES`) vs. `4/9` (`44.44%` of environments; `7/27 = 25.93%` of variants) on Stratum A2 (`compile_only`).
- **`FALS-03` & `FALS-03b` (`Sheaf-Cocycle` vs. `Pairwise-Tree` & `Circular-AG`)**:
  - `Sheaf-Cocycle` beats `Pairwise-Tree` by **`16.05 pp`** on unconditional orbit fraction ($\ge 15\text{ pp}$ threshold of `FALS-03` **PASSED**) and **`33.78 pp`** on conditional accepted-handoff FPR.
  - Against `Circular-AG` (`L11`), `Sheaf-Cocycle` beats `Circular-AG` by **`7.41 pp`** on unconditional orbit fraction ($\ge 5\text{ pp}$ on 4 cyclic environments, satisfying `O4`, but below the $15\text{ pp}$ unconditional threshold of `FALS-03b`) and by **`20.10 pp`** on conditional accepted-handoff FPR (`CondFPR` reduced from `20.10%` to `0.00%`).

### 4.2 Abort Trigger Audit & Automatic Claim-Ceiling Scoping (`ABORT-01`..`ABORT-05`)

| Abort ID | Condition | Global Fire? | Partial / Stratum Fire? | Automatic Claim-Ceiling Scoping Applied |
| :--- | :--- | :---: | :---: | :--- |
| **`ABORT-01`** | Holdout Type I-A $< 0.20$ | No (`A2 = 44.4%`) | **Yes (`A1 Holdout Type I-A = 0/9`, `Type 0 = 1/9`)** | `H1` is **not** claimed as a uniform defect of pre-hardened `REFERENCES` judges; it is scoped to the contrast between `instance_oracle_gate`-hardened `REFERENCES` (`8.3%` Type I-A, `16.7%` Type 0+I) and unhardened `compile_only` judges (`44.4%` Type I-A, `55.6%` total). |
| **`ABORT-02`** | Type II $\gamma_A < 0.15$ or $\gamma_B > 0.05$ | No ($\gamma_B = 0.0$, `A2` $\gamma_A = 44.4\%$) | **Yes (`A1` $\gamma_A = 0/12$)** | `H2` is scoped strictly to unhardened `compile_only` environments (`4/9 = 44.4%` any Type II; `2/9 = 22.2%` systematic $\ge 2/3$ Type II). |
| **`ABORT-03`** | `Sheaf-Cocycle` margin $< 0.15$ | No vs `Tree` (`+16.05 pp`) | **Yes vs `Circular-AG` unconditional $\Phi$ (`+7.41 pp`, CondFPR `+20.10 pp`)** | `H3` explicitly credits `Circular-AG` (`L11`) with eliminating 2-chart edge mismatches on the 27-tuple orbit and scopes `Sheaf-Cocycle`'s marginal advantage over `Circular-AG` to non-zero holonomy hollow cycles (`7.41%` of full orbit; `20.10%` of `Circular-AG` accepted handoffs). |
| **`ABORT-04`** | Solo-chart $\hat{\kappa}_e > 0.85$ | Numerically no in generated JSON | Numerically yes in hard-coded canonical subset | `M07` counts are hand-entered constants, not verified solo-agent samples; the trigger and H4 interpretation are not empirically adjudicable from this run. |
| **`ABORT-05`** | $\text{Jaccard}(E_J, E_O) < 0.50$ | Numerically no in metadata | Not applicable | `E_J/E_O` are hard-coded in `NERVE_METADATA`; threshold arithmetic is retained but is not evidence for H5. |

### 4.3 Quarantined Decision-Table Reweighting Output (Not Calibrated Bayesian Evidence)

| Hypothesis | Theorist Prior $\pi_T$ | Skeptic Prior $\pi_S$ | Illustrative single-row reweighting under `O4` $\pi_T$ / $\pi_S$ | Illustrative single-row reweighting under `O3` $\pi_T$ / $\pi_S$ | **Unvalidated composite reweighting** $\pi_T$ | **Unvalidated composite reweighting** $\pi_S$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`H0` (Null / Adequacy)** | `0.1000` | `0.3500` | `0.0056` / `0.0299` | `0.0226` / `0.1011` | **`0.0165`** | **`0.0771`** |
| **`H1` (Type I Gluing Blindness)** | `0.2500` | `0.2000` | `0.2098` / `0.2564` | `0.2489` / `0.2542` | **`0.2491`** | **`0.2661`** |
| **`H2` (Type II Gauge Over-Constraint)** | `0.1500` | `0.1500` | `0.1594` / `0.2436` | `0.2579` / `0.3293` | **`0.1982`** | **`0.2647`** |
| **`H3` (1-Cocycle Holonomy Yield)** | `0.2000` | `0.0800` | `0.3916` / `0.2393` | `0.0905` / `0.0462` | **`0.2403`** | **`0.1284`** |
| **`H4` (Prior Gauge Concentration)** | `0.1500` | `0.1400` | `0.0336` / `0.0479` | `0.3054` / `0.3640` | **`0.0992`** | **`0.1237`** |
| **`H5` (Evaluator–Orchestrator Duality)** | `0.1500` | `0.0800` | `0.2000` / `0.1628` | `0.0747` / `0.0491` | **`0.1967`** | **`0.1401`** |

**Do not interpret the table above as posterior evidence.** The row conditions overlap, the empirical row assignment is not a frozen classifier, the Skeptic residual prior was split after registration, and the composite weighting was not preregistered. Values are retained solely for reproducibility; see `reviews/posterior_audit.yaml`.


## 5. Claim-Floor and Data-Quality Disposition

- **Part A:** Report the observed counts only as outcomes of the specified, manually constructed variant audit against the implemented reference oracle. Do not call the oracle independently validated; Grader B wraps the same `AUDIT_DISPATCH` function.
- **Part B `M05/M06`:** Report finite deterministic outcomes over the generated 162 workspace variants and implemented predicates. Do not generalize to real LLM-agent decomposition or describe the output as a Čech cohomology measurement.
- **`M07/H4` and `M08/H5`:** Quarantined as hand-entered sample counts / hard-coded edge metadata; not empirical support.
- **`M09`:** The AST/LOC values are source-code counts under the registered counting routine; they do not establish that a grader is more accurate or more efficient at benchmark outcomes.
- **Bayesian fields:** Not calibrated posterior evidence (`reviews/posterior_audit.yaml`).
- **Process metrics:** M10/coordination efficiency is not estimable (`reviews/post_run_analysis_errata.yaml`).
- **No `claim_set.md` has been written.** Gate 3 must choose whether to accept this bounded diagnostic record, hold the mission as inconclusive, or require a separately preregistered redesign.
