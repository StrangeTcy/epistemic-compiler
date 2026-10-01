# Research Process Instrumentation & Friction Protocol (V0)

> **Purpose:** Manual execution can serve as a process-instrumentation pilot. A coordination-efficiency data point is reportable only when intervention coverage and timing are adequate; an incomplete log is not evidence of zero friction. The goal is to turn observations in `mission-01/friction_log.yaml` into tentative V1 tooling requirements without overstating the data.

---

## 1. Real-Time Friction Logging Rules

1. **Append at the event:** Record each human or lead-operator intervention when it occurs. Do not reconstruct unlogged events at the end of a mission; if a missing event is discovered later, record a separate data-quality note and mark the metric incomplete.
2. **Append-only history:** Never edit an existing event to update recurrence. Give related events a shared `root_cause_id` and list earlier event IDs in the newer event's `recurs_on` field.
3. **Honest timestamps:** Use ISO-8601 timestamps with an explicit offset (`+03:00`) or `Z` only for true UTC. An event timestamp is not automatically a start or finish time. Record `started_at` / `resolved_at` only when actually observed; otherwise use `null` and a `timestamp_quality` note. Never manufacture a duration to satisfy the schema.
4. **Derived vs. legacy duration:** `derived_duration_minutes` is calculated only when both `started_at` and `resolved_at` are known. Keep an older manually reported duration in `legacy_reported_duration_minutes`, clearly marked as reported rather than derived.
5. **No freeform-only records:** Each event must use the schema in Section 2 and exactly one primary `type` from Section 3.

---

## 2. Friction Log Schema (`mission-XX/friction_log.yaml`)

```yaml
schema_version: 2
mission_id: "mission-XX"
timezone: "Europe/Moscow"
mission_started_at: "2026-10-01T15:38:00+03:00"
friction_events:
  - id: F-001
    event_kind: "intervention" # intervention | resolution_update | data_quality_note
    related_event_id: null # Required for resolution_update or data_quality_note
    event_at: "2026-10-01T15:39:00+03:00" # When intervention was logged/observed
    started_at: null # Populate only if observed
    resolved_at: null # Populate only if observed
    derived_duration_minutes: null # Only derive from observed start/end
    legacy_reported_duration_minutes: 2 # Optional; preserve, don't mislabel as derived
    timestamp_quality: "migrated_offset_inferred" # exact | approximate | migrated_offset_inferred | not_recorded
    stage: "bootstrap"
    work_package: null
    type: "missing_information" # exactly one controlled type
    category: "specification" # specification | measurement | execution | integration | judgment
    root_cause_id: "RC-01"
    recurs_on: []
    trigger: "Concrete blocker or intervention trigger."
    root_cause_guess: "Why upstream artifacts failed to prevent it."
    resolution: "Exact action taken; do not list intended actions as completed."
    automatable: "likely" # yes | likely | unlikely | no_research_judgment
    automation_sketch: "Specific rule/tool or reason to preserve human judgment."
```

**Migration rule:** When importing a legacy log, preserve the original entry text and timestamp in a versioned snapshot. For v2 records migrated before `event_kind` was introduced, absence of the field defaults to `intervention`; later resolution/data-quality records must set it explicitly. Any timezone interpretation or type mapping must be labelled as a migration inference. Historical `resolution_time_minutes` is not an observed interval; retain it as `legacy_reported_duration_minutes`, never relabel it as derived. If completeness is unknown, report intervention and time metrics as incomplete/lower-bound or not estimable.

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

## 4. Coordination Efficiency Metrics & Anti-Goodharting Rules

At the conclusion of a mission, calculate these metrics only if the friction log is known to be complete for the stated interval. Otherwise report logged counts as a lower bound and mark the per-package metrics `not_estimable`; never encode missing logging as zero.

### 4.1 Single-Mission Coordination Efficiency (Not a Scaling Claim)
Let $W_{\text{completed}}$ be the number of packages that passed engineering acceptance and integrated cleanly; $N_{\text{int}}$ is the number of complete records with `event_kind: intervention` (excluding resolution updates/data-quality notes); and $T_{\text{coord}}$ is the sum of durations derived from observed start/end timestamps. Legacy reported durations must be shown separately.

1. **Intervention Burden per Completed Package ($\kappa_{\text{intervention}}$):**
   $$\kappa_{\text{intervention}} = \frac{N_{\text{int}}}{W_{\text{completed}}}$$
2. **Coordination Time per Completed Package ($\kappa_{\text{time}}$):**
   $$\kappa_{\text{time}} = \frac{T_{\text{coord}}\text{ (minutes)}}{W_{\text{completed}}}$$

These are **coordination-efficiency** measures for one mission. A single mission cannot establish sublinear scaling. A future cross-mission scaling claim would require multiple comparable missions and a fit such as $T_{\text{human}}(W) \approx aW^\beta+c$ with uncertainty supporting $\beta<1$.

### 4.2 Diagnostic Breakdown Metrics
Report, when the log is complete: total interventions by `stage` and `type`; observed and legacy-reported time separately; clarifications per completed package; packages repaired or re-dispatched; and packages blocked by `missing_interface`, `ambiguous_acceptance`, `dependency_error`, or `missing_information`. If the log is incomplete, annotate every count with the coverage limitation.

### 4.3 Anti-Goodharting Constraint (Fixed Granularity Rule)
- Do not lower either $\kappa$ by splitting coherent modules into trivial packages.
- Keep the package count within `[5, 15]` unless the mission's pre-registration explicitly justifies another range.
- Each package must map to a distinct requirement, measurement, control, evidence item, or experimental run.
- Always report raw counts, coverage/completeness, and time provenance alongside ratios.

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

## 6. Post-Mission Friction Analysis Protocol

After the applicable human gate, analyze the friction log without rewriting prior events:

1. Aggregate by `type`, `category`, `stage`, `root_cause_id`, and `recurs_on`.
2. Sum only `derived_duration_minutes` from observed start/end timestamps. Report legacy manual durations in a separate column; do not combine them as if equally precise.
3. State log coverage/completeness. If intervention logging was not complete in real time, report lower bounds and mark coordination ratios `not_estimable`.
4. Rank candidate automation targets by observed recurrence and reliable duration evidence; do not derive priority from imputed time.
5. Preserve events tagged `no_research_judgment` as human decisions, and document why premature automation could degrade research quality.
