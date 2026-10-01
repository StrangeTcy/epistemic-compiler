# Research Production Protocol (V0 — Protocol-Defined Research IR & Human-Gated Execution)

> **Core Principle:** V0 is a **protocol-defined research IR**, not yet a machine-enforced typed IR. It consists of provenance conventions, schemas in this document, and a four-gate human process. No `validate_ir.py`, general-purpose orchestration engine, dispatcher, or agent runtime is part of V0. The light-weight `scripts/retrieve_context.py` is an optional deterministic knowledge-view compiler; it does not validate research claims or automate judgment.
>
> **Protocol amendment note:** The methodological clarification below was added after Mission 01 execution in response to `REV-01`. It applies prospectively; it does **not** rewrite the Gate 2-locked `spec/approved.yaml`, the pre-registration commit, council record, or already produced results.
>
> **Methodological Thesis (Question, Not Premise):** *Local validity does not necessarily compose into global validity.* Whether in benchmark evaluation (Dual A: what an evaluator observes locally) or in multi-agent decomposition (Dual B: what distributed agents construct locally), a study may test whether missing boundary semantics are associated with local-to-global failure along:
> $$\text{Local Validity} \longrightarrow \text{Boundary Compatibility} \longrightarrow \text{Global Validity}.$$
> Presheaves ($\mathcal{P}: \mathcal{C}^{\text{op}} \to \mathbf{Set}$), descent data / gauge holonomy ($g_{31}g_{23}g_{12} \neq 1$), assume-guarantee contracts, and relational joins are **candidate formalisms**, not premises. In an ordinary sheaf $\mathcal{F}$, sections on a cover that agree on every overlap glue uniquely by the sheaf axiom. Therefore “pairwise agreement on all overlaps but no global section” is not a valid ordinary-sheaf counterexample. Empirical local-to-global failures must instead specify the actual structure involved (e.g., a presheaf family failing a canonical boundary-compatibility condition, or a descent problem with explicitly defined transition maps and non-trivial cycle holonomy). Do not call an observed interface mismatch a Čech cohomology class unless the relevant cover, coefficient structure, cocycles, coboundaries, and equivalence relation are formally defined.

---

## 1. Ontological Type System (Strict Separation of Concerns)

Every artifact in a mission must distinguish the following seven epistemic/engineering object types. Conflating any two of these—especially conflating **Engineering Acceptance Tests** with **Scientific Outcomes**—is a protocol violation.

| Type | ID Prefix | Definition | Validated By |
| :--- | :--- | :--- | :--- |
| **1. Scientific Hypothesis** | `H1`, `H2`, ... | A falsifiable candidate causal or structural explanation for an empirical phenomenon. Must make distinct predictions over observable measurements. | Gate 1 & Gate 2 |
| **2. Engineering Requirement** | `R01`, `R02`, ... | A deterministic capability, environment property, instrumentation hook, or baseline required so an experiment can be executed cleanly. | Gate 3 |
| **3. Measurement** | `M01`, `M02`, ... | An operationalized, reproducible function mapping raw experimental trajectories/states to a quantitative or categorical observable $O_j$. | Gate 2 |
| **4. Acceptance Test** | `T01`, `T02`, ... | A deterministic check verifying that an implemented work package satisfies its **engineering contract** (e.g., environment determinism, oracle computability, schema compliance, capability to represent *both* positive and negative scientific outcomes). **Must never assert that a scientific hypothesis came out true.** | Gate 3 & Package Execution |
| **5. Evidence** | `E01`, `E02`, ... | Concrete, immutable empirical artifacts produced by executing verified code (raw trajectory logs, state diffs, seed-indexed score tables, test outputs, literature citations). | Post-Execution / Gate 4 |
| **6. Interpretation** | `I01`, `I02`, ... | A model- or human-generated argument connecting Evidence (`E`) to Hypotheses (`H`) under explicit Controls (`CTRL`) and Confounds (`CF`). | Adversarial Critique / Gate 4 |
| **7. Claim** | `C01`, `C02`, ... | A bounded assertion published in `claim_set.md` that has survived executable falsification, obeys the pre-committed **Claim Ceiling**, and links to complete Evidence (`E`). | Gate 4 |

### Anti-Conflation Rule for Acceptance Tests
- **ILLEGAL Acceptance Test:** *"Verify that frontier models fail the causal execution check on >30% of outcome-successful trajectories."* (Prejudges the empirical outcome; pressures the coding agent to rig the environment or threshold.)
- **LEGAL Acceptance Test:** *"Verify that (a) the environment admits both a valid causal policy $\pi_{\text{valid}}$ and a shortcut policy $\pi_{\text{shortcut}}$ that achieve identical outcome reward $R_{\text{out}} = 1.0$, (b) the causal auditor scores $\pi_{\text{valid}} = 1.0$ and $\pi_{\text{shortcut}} = 0.0$ deterministically across 50 seeds, and (c) both trajectory classes serialize to `results/schema.json`."*

---

## 2. Traceability & Provenance Invariants

### 2.1 Forward & Backward Epistemic Traceability
Every substantive claim in `claim_set.md` must satisfy a complete, unbroken chain:

$$\text{Claim } (C_q) \longrightarrow \text{Hypothesis } (H_i) \longrightarrow \text{Experiment } (X_r) \longrightarrow \text{Measurement } (M_j) \longrightarrow \text{Evidence Artifact } (E_n)$$

- **Rule 1 (No Unmeasured Claims):** If a proposed claim has no path to a concrete Measurement ($M_j$) and Evidence Artifact ($E_n$), it is **speculation** and must be stripped or moved to `unresolved_questions`.
- **Rule 2 (No Orphan Engineering):** Every Work Package (`WP-XX`) must trace back to at least one Measurement (`M`), Control (`CTRL`), or Falsification Experiment (`FALS`), which in turn traces to a Hypothesis (`H`). Any task without a path back to a hypothesis is unnecessary engineering and must be deleted.

### 2.2 Provenance Identifier Conventions
All council outputs, critiques, specs, and work packages must preserve explicit provenance IDs so disagreements are tracked rather than silently averaged away:

- `S01`: Seed identifier
- `P01`, `P02`, ...: Specific proposals from Council roles (`P01-T` Theorist, `P02-E` Experimentalist, `P03-S` Skeptic, `P04-PW` Prior-Work Killer)
- `CR01`, `CR02`, ...: Cross-critique items attacking a proposal or hypothesis
- `H1`, `H2`, `H3`, ...: Competing hypotheses (must include at least one null/boring/artifactual hypothesis $H_0$)
- `A01`, `A02`, ...: Explicit background assumptions
- `U01`, `U02`, ...: Unresolved disagreements between council members
- `L01`, `L02`, ...: Prior-work / literature items
- `X01`, `X02`, ...: Registered experiment/run conditions and execution records (must bind to a `WP-XX`, measurements, seeds/conditions, and produced evidence)
- `M01`, `M02`, ...: Measurements
- `O01`, `O02`, ...: Candidate observation outcomes in the Decision Table
- `CF01`, `CF02`, ...: Confounds
- `CTRL01`, `CTRL02`, ...: Experimental controls (each must state which `CF` or `CR` it rules out)
- `WP-01`, `WP-02`, ...: Bounded engineering/execution work packages
- `FALS-01`, `FALS-02`, `FALS-03`: Post-experiment executable falsification tests
- `F-001`, `F-002`, ...: Real-time friction log entries (`friction_log.yaml`)

---

## 3. Pipeline Architecture, Mindcluster Retrieval & The Four Human Gates

```text
Global Mindcluster Knowledge Graph (knowledge/: nodes, edges, sources; if supplied)
    │
    ▼  scripts/retrieve_context.py (--seed, --hops 2, --roles)
mission-XX/seed.yaml  +  Compiled Role Context Packs (mission-XX/context/*.md)
    │
    ▼
Adversarial Council (Theorist, Experimentalist, Skeptic, Prior-Work Killer)
    │
    ▼
═══════════════════════════════════════════════════════════════
  GATE 1 — QUESTION  (gates/gate1_question.md)
  "Is this a meaningful, non-trivial, unkilled research question?"
═══════════════════════════════════════════════════════════════
    │
    ▼
Measurement Design & Decision Table (P(O_j | H_i), Priors, Controls, Claim Ceiling)
    │
    ▼
Cross-Critique & Draft Spec (spec/draft.yaml)
    │
    ▼
═══════════════════════════════════════════════════════════════
  GATE 2 — MEASUREMENT  (gates/gate2_measurement.md)
  "Can the proposed observations actually distinguish H1..Hn?"
═══════════════════════════════════════════════════════════════
    │
    ▼
Approved Research Spec (spec/approved.yaml)
    ──► Canonical Overlap Contracts (work_packages/overlaps.yaml)
    ──► Bounded Work Packages (work_packages/WP-*.yaml)
    │
    ▼
═══════════════════════════════════════════════════════════════
  GATE 3 — EXECUTION  (gates/gate3_execution.md)
  "Can stateless agents implement these packages independently?"
═══════════════════════════════════════════════════════════════
    │
    ▼
Manual Dispatch & Execution + Real-Time Friction Logging (friction_log.yaml)
    │
    ▼
Raw Results (results/) ──► Executable Falsification (falsification/, max 3 exps, 1 round)
    │
    ▼
═══════════════════════════════════════════════════════════════
  GATE 4 — CLAIM  (gates/gate4_claim.md)
  "What does the audited evidence actually support under the Claim Ceiling?"
═══════════════════════════════════════════════════════════════
    │
    ▼
mission-XX/claim_set.md + Bootstrap Friction Analysis
```

---

### GATE 1 — QUESTION (`gates/gate1_question.md`)
**Purpose:** Determine whether the seed contains a meaningful, nontrivial research question that survives initial theoretical scrutiny and prior-work collision checks.

- **Inputs:**
  - `mission-XX/seed.yaml`
  - Independent outputs from the 4 Council roles (`council/theorist.md`, `council/experimentalist.md`, `council/skeptic.md`, `council/prior_work_killer.md`)
- **Required Artifacts:**
  - Completed `gates/gate1_question.md` recording surviving hypotheses ($H_0, H_1, \dots$), pruned ideas, prior-work overlap differentiation (`L01..Lnn`), and explicit statement of what remains novel.
- **Acceptance Conditions:**
  1. The research question is stated as a sharp empirical discrimination problem, not a vague theme.
  2. At least two genuinely competing hypotheses ($H_1$ vs. $H_0$/$H_2$) exist where both are a priori plausible.
  3. Prior-Work Killer (`prior_work_killer.md`) has searched existing literature/benchmarks and verified that the exact contribution is not already established (or narrowed the question to the unestablished regime).
  4. The question is testable within the repository's existing or locally extensible architecture.
- **Failure Conditions:**
  - Prior work (`Lxx`) already establishes the exact claim with equivalent controls.
  - All candidate hypotheses reduce to tautologies or definitional preferences.
  - Testing the question requires compute, proprietary environments, or data completely inaccessible to the mission.
- **If Gate 1 Fails:**
  - **Option A (Reframe):** Narrow or pivot the seed using the gap exposed by `prior_work_killer.md` or `skeptic.md` (max 1 re-seed iteration, logged in `friction_log.yaml`).
  - **Option B (Abort Mission):** Record a `prior_work_collision` or `vacuous_question` outcome in `claim_set.md` and terminate the mission cleanly. (Stopping early on a killed seed is a **successful execution of Gate 1**, not a protocol failure.)

---

### GATE 2 — MEASUREMENT (`gates/gate2_measurement.md`)
**Purpose:** Determine whether the proposed measurements and controls can empirically distinguish the competing hypotheses in expectation, before writing experiment code.

- **Inputs:**
  - Approved Gate 1 output (`gates/gate1_question.md`)
  - Cross-critique (`critiques/cross_critique.md`)
  - Draft Research Spec (`spec/draft.yaml`)
- **Required Artifacts:**
  - `spec/draft.yaml` revised into `spec/approved.yaml`
  - Completed `gates/gate2_measurement.md` containing the audited Decision Table, Confound Register, and Claim Ceiling sign-off.
- **Acceptance Conditions:**
  1. **Non-Degenerate Decision Table:** Every surviving hypothesis $H_i$ has a rough prior $P(H_i)$ and qualitative/approximate conditional likelihoods $P(O_j \mid H_i)$ across mutually exclusive observation regimes $O_1, \dots, O_k$.
  2. **Non-Negligible Marginal Probability of Discrimination:** The discriminating observations $O_j$ where $P(O_j \mid H_1) \gg P(O_j \mid H_0)$ are not vanishingly rare corner cases under reasonable priors (high qualitative Expected Information Gain $\operatorname{EIG} = H(H) - \sum_o P(o) H(H \mid o)$).
  3. **Confound Coverage:** Every high-severity confound (`CFxx`) raised by the Skeptic has an explicit experimental Control (`CTRLxx`) or is logged as a strict limitation in the Claim Ceiling.
  4. **Explicit Claim Ceiling & Evidence Contract:** `spec/approved.yaml` defines both the maximum justifiable claim (`claim_ceiling`) and the claims explicitly out of bounds (`cannot_justify`), plus the exact evidence set $\{E_1, \dots, E_n\}$ required.
- **Failure Conditions:**
  - **Collapsed Decision Table:** Plausible observations leave all hypotheses equally supported ($P(O_j \mid H_1) \approx P(O_j \mid H_0)$).
  - **Circular Measurement:** The measurement $M_j$ bakes in the conclusion by definition rather than measuring an independent property.
  - **Uncontrolled Fatal Confound:** A boring artifact (e.g., prompt length, parser error, step limit truncation) completely explains the predicted effect and no control isolates it.
- **If Gate 2 Fails:**
  - Return `spec/draft.yaml` for measurement redesign (max 2 revision cycles; each logged in `friction_log.yaml`).
  - If the Decision Table still collapses or passes >3 total revisions without a discriminating measurement, trigger **Abort Condition A2** and close the mission as `failed_measurement_design`.

---

### GATE 3 — EXECUTION (`gates/gate3_execution.md`)
**Purpose:** Verify that `spec/approved.yaml` has been compiled into 5–15 bounded work packages with explicit ownership, dependencies, mission-level boundary contracts, and outcome-neutral engineering tests. Work packages may be represented as local views for analysis, but contract compatibility does not by itself establish a sheaf or guarantee scientific global validity.

- **Inputs:**
  - Gate-2-frozen `spec/approved.yaml`
  - Mission-level `work_packages/overlaps.yaml`, frozen before execution
  - Work package files `work_packages/WP-01.yaml` ... `WP-NN.yaml`
- **Required Artifacts:**
  - Completed `gates/gate3_execution.md` containing the structural validation checklist, canonical boundary-contract matrix (or an explicit statement that no frozen manifest existed), dependency/parallelism map, and test outputs.
- **Acceptance Conditions:**
  1. **Bounded Count:** Between 5 and 15 work packages total.
  2. **Complete Traceability:** Every `WP-XX` cites the specific `Mxx`, `CTRLxx`, or `Rxx` it implements, and every required Evidence item `Exx` in `spec/approved.yaml` is produced by at least one `WP-XX`.
  3. **Explicit Ownership:** Each `WP-XX` defines owned paths and read-only inputs. No two parallel work packages modify the same file.
  4. **Mission-Level Canonical Boundary Contracts:** Before execution, the mission owner freezes every shared boundary in `work_packages/overlaps.yaml`, including schema, semantics, producer/consumer projections, compatibility relation, and deterministic check. WPs may instantiate a contract but may not invent or redefine its semantics. The manifest is an engineering contract; calling it a mathematical restriction map requires separate formal justification.
  5. **Outcome-Neutral Acceptance Tests:** Every `WP-XX` includes runnable engineering tests verifying its contract and ability to represent admissible positive and negative outcomes, without asserting which scientific hypothesis wins.
- **Failure Conditions:**
  - Implicit interfaces or agent-defined shared semantics.
  - Missing or nondeterministic compatibility checks for declared shared interfaces.
  - Overlapping write boundaries across concurrent packages.
  - Acceptance tests that test the scientific hypothesis rather than engineering correctness.
- **If Gate 3 Fails:**
  - Pause execution. Contract/schema repairs are logged as amendments and may require re-registration; never imply a post-hoc manifest existed during a locked run.

---

### GATE 4 — CLAIM (`gates/gate4_claim.md`)
**Purpose:** Adjudicate what the empirical results and executed falsification experiments actually support, strictly bounded by the pre-committed Claim Ceiling.

- **Inputs:**
  - Raw and aggregated evidence in `results/`
  - Adversarial critique & executed falsification experiments in `falsification/` (up to budget: max 3 adversarial experiments, max 1 recursive round)
  - `spec/approved.yaml` (specifically `decision_table`, `claim_ceiling`, `cannot_justify`, `evidence_required`)
- **Required Artifacts:**
  - Completed `gates/gate4_claim.md`
  - Final `mission-XX/claim_set.md`
- **Acceptance Conditions:**
  1. Every claim in `claim_set.md` cites concrete, existing artifacts in `results/` and `falsification/`.
  2. No claim exceeds the pre-committed `claim_ceiling` in `spec/approved.yaml`.
  3. Every high-plausibility alternative explanation raised by critics was either (a) tested via an executable falsification experiment (`FALS-01..03`) or (b) explicitly logged under `Remaining Uncertainty / Open Questions` if outside the falsification budget.
  4. Failed or falsified hypotheses are preserved in the record rather than silently erased.
- **Failure Conditions:**
  - Post-hoc rhetoric inflation (claiming general LLM properties from a single environment family).
  - Unresolved fatal confound revealed by a falsification experiment (`FALS-XX`) that invalidates the primary measurement.
  - Missing required evidence artifacts (`Exx`).
- **If Gate 4 Fails:**
  - Downgrade the claim to match the surviving evidence (`negative_result`, `inconclusive_result`, or `failed_measurement_design` are first-class valid outputs), or execute within the remaining falsification budget (if <3 falsification experiments have been run). Never rewrite history in `spec/approved.yaml`.

---

## 4. Artifact Schemas

### 4.1 Seed Schema (`mission-XX/seed.yaml`)
```yaml
seed_id: S01
title: "<Concise title of the empirical intuition>"
repo_context: "<Summary of relevant existing modules/envs in rl_eval_generator>"
intuition: |
  <Why we suspect this phenomenon exists>
precise_research_question: |
  <Sharp, operationalized question>
why_it_might_be_true:
  - "<Mechanism 1>"
  - "<Mechanism 2>"
what_would_surprise_us:
  - "<Observation that would falsify our intuition>"
candidate_hypotheses:
  - id: H0
    name: "<Null / Baseline / Artifactual Hypothesis>"
    statement: "<Statement>"
  - id: H1
    name: "<Primary Structural Hypothesis>"
    statement: "<Statement>"
  - id: H2
    name: "<Competing Mechanism Hypothesis>"
    statement: "<Statement>"
known_alternatives:
  - "<Alternative explanation 1>"
possible_experiment: |
  <Initial sketch of discriminating experiment>
known_unknowns:
  - "<Unknown 1>"
likely_confounds:
  - id: CF01
    description: "<Confound description>"
relevant_prior_work:
  - id: L01
    citation: "<Paper / benchmark>"
    relationship: "<How it relates and what gap remains>"
candidate_claim_ceiling:
  max_justifiable_claim: |
    <Strongest claim this seed could establish if H1 holds>
  cannot_justify:
    - "<Overbroad claim 1>"
possible_future_research_on_failure:
  - "<What we learn and what seed spawns next if H1 is falsified>"
```

### 4.2 Decision Table Schema (inside `spec/draft.yaml` & `spec/approved.yaml`)
For each mutually exclusive observation regime $O_j$ and hypothesis $H_i$, specify qualitative likelihoods (`very_high` $\approx 0.8$, `high` $\approx 0.6$, `moderate` $\approx 0.3$, `low` $\approx 0.1$, `very_low` $< 0.05$) and rough priors $P(H_i)$:

```yaml
hypotheses:
  - id: H0
    prior: 0.40
    statement: "..."
    provenance: ["P03-S"]
  - id: H1
    prior: 0.40
    statement: "..."
    provenance: ["S01", "P01-T"]
  - id: H2
    prior: 0.20
    statement: "..."
    provenance: ["P02-E", "P03-S"]

decision_table:
  observations:
    - id: O1
      description: "<Observation regime 1 defined in terms of M01, M02>"
      marginal_plausibility: "moderate-to-high (~0.45)"
      likelihoods:
        H0: "very_low (0.05)"
        H1: "high (0.75)"
        H2: "low (0.15)"
      diagnostic_interpretation: "Strongly updates toward H1 over H0 and H2."
    - id: O2
      description: "<Observation regime 2>"
      marginal_plausibility: "moderate (~0.35)"
      likelihoods:
        H0: "high (0.80)"
        H1: "low (0.10)"
        H2: "low (0.15)"
      diagnostic_interpretation: "Supports H0 (null/outcome grading sufficient)."
    - id: O3
      description: "<Observation regime 3>"
      marginal_plausibility: "low-to-moderate (~0.20)"
      likelihoods:
        H0: "low (0.15)"
        H1: "low (0.15)"
        H2: "high (0.70)"
      diagnostic_interpretation: "Supports H2 (confound/evaluator artifact)."
  expected_information_gain_assessment: |
    <Qualitative/quantitative EIG check verifying that O1/O2/O3 are well-separated
    and none of the discriminating regimes has near-zero marginal probability.>
```

### 4.3 Research Spec Schema (`spec/draft.yaml` & `spec/approved.yaml`)
Must contain:
- `mission_id`, `seed_id`, `status` (`draft` | `approved`)
- `research_question`
- `hypotheses` (with `id`, `prior`, `statement`, `predictions`, `provenance`)
- `assumptions` (`A01..Ann`)
- `unresolved_disagreements` (`U01..Unn` with council provenance)
- `prior_work` (`L01..Lnn` with `topic_similarity_vs_actual_overlap`)
- `measurements` (`M01..Mnn` with exact mathematical/operational definition)
- `decision_table` (as above)
- `confound_register` (`CF01..CFnn`)
- `controls` (`CTRL01..CTRLnn` with `rules_out: [CFxx, CRyy]`)
- `expected_observations`
- `claim_ceiling` (`max_justifiable_claim`, `cannot_justify`)
- `evidence_required` (`E01..Enn` mapping each claim to required output files/tables)
- `abort_conditions` (`ABORT-01..ABORT-nn`)
- `deliverables`

### 4.4 Canonical Overlap Contracts (`work_packages/overlaps.yaml`) & Work Package Schema (`work_packages/WP-XX.yaml`)

**Architectural Rule (Mission-Level Boundary Ownership):** Individual work packages must **never** invent or self-declare the semantics of their own shared boundaries. Before package execution, define all cross-package boundaries in `work_packages/overlaps.yaml`. These are canonical engineering projections from package-owned artifacts into shared interface objects. A presheaf interpretation is optional and must be separately justified; the manifest itself does not establish one:

```yaml
overlaps:
  - overlap: O12
    left: WP-01
    right: WP-02
    boundary:
      name: blackbox_context_hash_manifest
      artifact_path: "mission-01/results/blackbox_hashes.json"
      schema: "dict[env_id, {blackbox_sha256, visible_files, patchable_files, judge_excluded}]"
      semantics: "Deterministic SHA-256 of agent-visible workspace excluding judge.py (CTRL01)"
    left_projection:
      source: "tools/blackbox_context_bundler.py:bundle_all_environments()"
    right_projection:
      source: "tools/grader_b_and_truth_oracles.py:OUT_HASHES_PATH"
    compatibility:
      relation: "equal"
      verification_command: "pytest -q tests/test_bidirectional_audit_harness.py -k test_blackbox_isolation_and_hash_verification"
```

For operational planning, a work package may be denoted by a local view $U_i$; this notation does not assert that the collection forms a topological cover or sheaf. Each WP references (rather than defines) its assigned canonical overlaps from `overlaps.yaml`:

```yaml
id: WP-01
title: "<Short imperative title>"
purpose: "<1-2 sentence description of the artifact this package produces>"
research_requirements_served:
  hypotheses: ["H1", "H0"]
  measurements: ["M01"]
  controls: ["CTRL01"]
  evidence_produced: ["E01"]
local_chart:
  chart_id: U_1
  owned_paths:
    - "<Explicit whitelist of file paths this agent is permitted to create/edit>"
canonical_overlaps_instantiated: ["O12", "O13", "O14"]
boundary_contracts_instantiated:
  - overlap_id: "O12"
    shared_contract_ref: "work_packages/overlaps.yaml#O12"
    compatibility_test: "<Deterministic test named by the frozen contract>"
engineering_acceptance_tests:
  - id: T01-1
    type: engineering_only # NEVER scientific outcome
    scope: artifact_or_boundary # artifact | boundary_contract
    command: "pytest tests/test_wp01.py"
    assertions:
      - "<Deterministic invariant verifying the produced artifact>"
      - "<Verify both positive and negative trajectory/patch fixtures are scored as specified>"
scientific_relevance: |
  <Why this artifact and its frozen boundary contracts are necessary for measurement of H1 vs H0>
expected_evidence:
  - id: E01
    path: "mission-01/results/..."
failure_conditions:
  - "<When the artifact or a referenced boundary contract fails its engineering check>"
```

### 4.5 Executable Falsification Budget & Schema (`falsification/`)
- **Hard Budget:**
  - Maximum **3 adversarial falsification experiments** (`FALS-01`, `FALS-02`, `FALS-03`).
  - Maximum **1 recursive round** per mission.
  - Any critique that cannot be tested within this budget must be logged explicitly in `claim_set.md` under `Unresolved Questions & Logged Critiques`.
- Each falsification item must specify:
  - `id` (`FALS-01`)
  - `attacked_claim_or_hypothesis` (`H1` / `C01`)
  - `boring_alternative_explanation`
  - `executable_test_specification` (what script/control parameter is run)
  - `falsification_criterion` (what result kills `C01`)
  - `execution_result` & `survives_falsification` (`true` | `false` | `partially_weakened`)

### 4.6 Claim Set Schema (`mission-XX/claim_set.md`)
Every candidate claim must be documented with the following 8 mandatory fields:
```markdown
### Claim C01
- **CLAIM:** <Precise empirical statement>
- **EVIDENCE:** <Exact file paths, tables, seed counts, and metrics in `results/` and `falsification/`>
- **HYPOTHESIS SUPPORTED:** <H_i (and which H_j are weakened)>
- **ALTERNATIVE EXPLANATION:** <Strongest surviving boring/confound explanation>
- **CONTROL:** <CTRLxx and FALS-xx that tested against the alternative explanation>
- **REMAINING UNCERTAINTY:** <What was not ruled out or remains untested>
- **CLAIM CEILING CHECK:** <PASS/FAIL verification against `spec/approved.yaml` claim_ceiling>
- **FALSIFICATION STATUS:** <Survived FALS-01..03 / Weakened / Refuted / Unresolved within budget>
```
