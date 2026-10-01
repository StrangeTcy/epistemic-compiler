# Research Process Instrumentation & Friction Protocol (V0)

> **Purpose:** The manual execution of Mission 01 is itself an empirical experiment whose subject is the research coordination process. Its goal is to turn "vibes about what to automate" into a structured dataset (`mission-01/friction_log.yaml`) from which V1 tooling requirements are derived empirically.

---

## 1. Real-Time Friction Logging Rules

1. **Log Immediately Upon Intervention:** Every time a human (or lead operator acting on a human gate/clarification) must intervene, clarify, repair an artifact, resolve a boundary collision, or supply missing context, an entry **must** be appended to `mission-01/friction_log.yaml` at the moment it occurs—never reconstructed from memory at the end of the run.
2. **No Freeform Prose Notes:** Every entry must conform strictly to the YAML schema in Section 2 and use the Controlled Vocabulary in Section 3.
3. **Update Recurrence Counts:** When a friction event shares the same underlying root cause and `type` as an earlier entry, increment `recurrence_count` (and reference the prior `F-XXX` ID in `root_cause_guess`) so recurring bottlenecks separate cleanly from one-off accidents.

---

## 2. Friction Log Schema (`mission-XX/friction_log.yaml`)

```yaml
friction_events:
  - id: F-001
    timestamp: "2026-10-01T15:40:00Z"
    stage: "bootstrap" # See Section 3.1 for allowed stage values
    work_package: null # WP-01 .. WP-NN, or null if pre/post package execution
    type: "missing_information" # See Section 3.2 for Controlled Vocabulary
    category: "specification" # specification | measurement | execution | integration | judgment
    trigger: >
      Concrete description of what blocked progress or prompted the intervention.
    root_cause_guess: >
      Why the protocol, seed, spec, or work-package contract failed to prevent this.
    resolution: >
      Exact action taken to unblock the step.
    resolution_time_minutes: 3
    recurrence_count: 1
    automatable: "likely" # yes | likely | unlikely | no_research_judgment
    automation_sketch: >
      Concrete description of the validator rule, schema field, or pre-flight check
      that would eliminate this friction in V1 (or why it must remain human judgment).
```

---

## 3. Controlled Vocabularies

### 3.1 Allowed `stage` Values
- `bootstrap` — Initial repo inspection, workspace setup, protocol initialization
- `seed` — Constructing or revising `seed.yaml`
- `council` — Running the 4 adversarial roles (`theorist`, `experimentalist`, `skeptic`, `prior_work_killer`)
- `gate1_question` — Human adjudication at Gate 1
- `critique` — Cross-critique of proposals and measurement design
- `spec_synthesis` — Synthesizing `spec/draft.yaml` and `spec/approved.yaml`
- `gate2_measurement` — Human adjudication at Gate 2 (Decision Table, Controls, Claim Ceiling)
- `package_compilation` — Compiling `spec/approved.yaml` into `work_packages/WP-*.yaml`
- `gate3_execution` — Human adjudication at Gate 3
- `dispatch` — Handing work packages to coding/execution agents
- `implementation` — Agent execution of a work package
- `integration` — Combining outputs from multiple work packages
- `experiment` — Running environments, policies/models, and collecting `results/`
- `falsification` — Designing and executing `FALS-01..03`
- `gate4_claim` — Human adjudication at Gate 4 and producing `claim_set.md`

### 3.2 Controlled Vocabulary for `type` (Mandatory)
Every friction event must be assigned **exactly one** primary `type` from this list:

| `type` | Operational Definition |
| :--- | :--- |
| `clarification` | An agent or operator had to ask a question to disambiguate a term, parameter, or intent not settled in the artifact. |
| `missing_interface` | A work package omitted an exact function signature, data schema, state dictionary key, or CLI contract needed by a producer/consumer. |
| `ambiguous_acceptance` | An acceptance criterion was underspecified, subjective, or admitted degenerate/trivial implementations. |
| `boundary_violation` | An agent modified files outside its `allowed_files` whitelist or stepped on another package's module. |
| `repair` | The operator/human had to manually edit code, YAML, or tests produced by an agent because it failed acceptance or broke an invariant. |
| `re-dispatch` | A work package or council prompt had to be re-sent to an agent after rejecting a defective output. |
| `integration_conflict` | Two work packages passed their individual acceptance tests in isolation but failed when wired together (e.g., mismatched state conventions, seed handling, or return types). |
| `dependency_error` | A package could not be started or tested because an undeclared dependency (file, package, fixture, or upstream artifact) was missing. |
| `scientific_engineering_confusion` | An acceptance test or implementation conflated engineering correctness (does the instrument work?) with scientific outcome (did Hypothesis $H_1$ win?). |
| `scope_creep` | An agent or spec drifted into building unrequested abstractions, generalized frameworks, or extra features not traceable to a hypothesis. |
| `missing_information` | Required external context (repository files, API keys, environment docs, prior-work details) was absent from the workspace or prompt. |
| `model_failure` | An agent hallucinated APIs, ignored explicit instructions present in the prompt, or failed a reasoning step despite a complete specification. |
| `tooling_failure` | A local runtime, environment, shell, package manager, or test-runner failure unrelated to the scientific design. |

### 3.3 Allowed `category` Values (for Part XI Aggregation)
- `specification` — Missing/ambiguous schemas, interfaces, or provenance in seed/spec/WP
- `measurement` — Flaws in metrics, decision tables, controls, or confound isolation
- `execution` — Agent implementation errors, model failures, or runtime issues
- `integration` — Cross-package mismatches or file boundary collisions
- `judgment` — Irreducible scientific/epistemic trade-offs requiring human research taste

---

## 4. Coordination Metrics & Anti-Goodharting Rules

At the conclusion of Mission 01, compute and report the following metrics from `friction_log.yaml` and `work_packages/`:

### 4.1 Primary Sublinearity Metrics
Let $W_{\text{completed}}$ be the number of work packages that passed all engineering acceptance tests and integrated cleanly, $N_{\text{int}}$ be the total number of human interventions logged in `friction_log.yaml`, and $T_{\text{coord}}$ be the sum of `resolution_time_minutes` across all human interventions.

1. **Intervention Burden per Completed Package ($\kappa_{\text{intervention}}$):**
   $$\kappa_{\text{intervention}} = \frac{N_{\text{int}}}{W_{\text{completed}}}$$

2. **Coordination Time per Completed Package ($\kappa_{\text{time}}$):**
   $$\kappa_{\text{time}} = \frac{T_{\text{coord}}\text{ (minutes)}}{W_{\text{completed}}}$$

### 4.2 Diagnostic Breakdown Metrics
Also report unconditionally:
- **Total Human Interventions ($N_{\text{int}}$)** (broken down by `stage` and `type`)
- **Total Human Coordination Time ($T_{\text{coord}}$)** in minutes
- **Clarifications per Package:** $\frac{\text{count}(\texttt{type == clarification})}{W_{\text{completed}}}$
- **Repaired Packages ($W_{\text{repaired}}$):** Number and fraction of work packages requiring manual `repair`
- **Re-dispatched Packages ($W_{\text{redispatched}}$):** Number and fraction of work packages requiring `re-dispatch`
- **Packages Blocked by Missing Spec ($W_{\text{blocked}}$):** Count of packages encountering `missing_interface`, `ambiguous_acceptance`, `dependency_error`, or `missing_information`

### 4.3 Anti-Goodharting Constraint (Fixed Granularity Rule)
- **Prohibition:** You may **not** reduce $\kappa_{\text{intervention}}$ or $\kappa_{\text{time}}$ by artificially splitting a single coherent module into tiny trivial work packages (e.g., 30 one-function packages).
- **Granularity Guardrail:**
  1. Total work packages for Mission 01 must remain within $[5, 15]$.
  2. Every work package must produce a standalone, testable artifact mapped to a distinct requirement (`Rxx`), measurement (`Mxx`), control (`CTRLxx`), or experimental run (`Exx`).
  3. Always report raw totals ($N_{\text{int}}$ and $T_{\text{coord}}$) alongside $\kappa_{\text{intervention}}$ and $\kappa_{\text{time}}$.

---

## 5. Pre-Committed Mission 01 Abort Conditions

To prevent sunk-cost continuation on a broken seed or non-discriminating experiment, Mission 01 must immediately halt and write a post-mortem in `claim_set.md` if any of the following pre-committed abort conditions trigger:

- **`ABORT-01` (Prior-Work Kill at Gate 1):** The Prior-Work Killer demonstrates that the exact proposed claim and controls are already established in published literature or existing benchmarks, and 1 re-scoping attempt fails to isolate a genuinely open question.
- **`ABORT-02` (Council Non-Discrimination):** After 2 synthesis rounds, the council fails to produce an experiment whose Decision Table distinguishes $H_1$ from $H_0$/$H_2$.
- **`ABORT-03` (Measurement Gate Collapse at Gate 2):** Gate 2 cannot be passed within 3 revisions of `spec/draft.yaml` (e.g., all proposed metrics remain circular or confounded by trivial artifacts).
- **`ABORT-04` (Runaway Package Coordination):** Any single work package consumes more than **90 minutes** of human coordination time or requires more than **3 re-dispatches** without passing its engineering acceptance tests.
- **`ABORT-05` (Trivial Claim Ceiling):** During Gate 2 or Gate 4, the surviving `claim_ceiling` shrinks to a tautology or a statement too narrow to be worth writing up as a research note.

> **Epistemic Note:** Triggering an abort condition is a **successful execution of the protocol's filter**, saving days of wasted engineering.

---

## 6. Post-Mission Friction Analysis Protocol (Part XI)

Upon completing Gate 4 (or triggering an abort), analyze `mission-01/friction_log.yaml` before writing a single line of V1 infrastructure code:

1. **Aggregate Table:** Group all `F-XXX` entries by:
   - `type` (13-class vocabulary)
   - `category` (`specification`, `measurement`, `execution`, `integration`, `judgment`)
   - `recurrence_count`
   - `sum(resolution_time_minutes)`
2. **Rank Top 3 Automation Targets:** Select the 3 recurring friction patterns with the highest product of recurrence and coordination time where `automatable` is `yes` or `likely`. For each target, document:
   - `OBSERVED FRICTION`
   - `EVIDENCE` (specific `F-XXX` IDs, timestamps, and package IDs)
   - `WHY IT RECURRED`
   - `PROPOSED AUTOMATION` (exact validator rule, schema constraint, or script)
   - `EXPECTED REDUCTION IN HUMAN COORDINATION` ($\Delta N_{\text{int}}$ and $\Delta T_{\text{coord}}$)
   - `WHY THIS SHOULD BE AUTOMATED`
3. **Protect Research Judgment:** Explicitly list all friction events tagged `no_research_judgment` (e.g., choosing which hypothesis framing is scientifically deepest, deciding whether a claim ceiling is honest) and document why automating them prematurely would degrade research quality into polished-spec theater.
