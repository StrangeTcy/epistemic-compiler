# `rl_eval_generator` evolution proposals

These are campaign-analysis recommendations, not implemented changes. “Confirmed improvement” means the archive/source audit provides direct evidence for the need; it does **not** mean an implementation has been merged or its benefit experimentally validated. The paid campaign recorded a dirty repository, so comparator-based findings remain conditional on the inspected clean source snapshot.

## A. Confirmed improvements — direct evidence supports fixing the contract

### P0 — Make case disposition and denominators first-class data

**Observed basis:** 194 selected cases are scored, 17 `rope` cases are omitted for unsupported provider modality, and 7 are blocked before provider access by calibration failures. The campaign report names one provider outage, while two selected final results carry provider-transient terminal notes. Raw PASS/FAIL is 131/63; sensitivities are 131/193 when only the report-listed case is excluded and 131/192 when both terminal provider-coded cases are excluded. (`F-02`, `F-03`.)

**Proposal:** Store an immutable case-ledger row for every planned case with separate fields:

- `planned`, `selected`, `submitted`, `scored`, `omitted`, `excluded_after_run`;
- exactly one disposition reason, owner, timestamp, and whether any provider request was sent;
- raw verdict and mode, performance-eligibility decision, rule/version used, and a link to the final judge record;
- provider terminal state and model/action terminal state as separate enums.

Generate raw totals and each published sensitivity directly from that ledger. The report should list every terminal provider-coded result and distinguish an outage episode from individual retried requests.

### P0 — Separate infrastructure termination from agent action errors

**Observed basis:** the two provider-terminal final rows are both recorded as `invalid_action`; the selected API logs include timeout/provider-transient events. The current label makes provider availability look like an agent-format failure. (`F-03`, `F-09`.)

**Proposal:** Add independent fields for `provider_status`, `transport_status`, `action_parse_status`, `patch_validation_status`, `source_validation_status`, `runtime_status`, and `behavioral_judge_status`. Do not overload one `failure_mode` enum. If the provider terminates after bounded retries, record `infrastructure_inconclusive` or the campaign’s explicit equivalent, retain the raw provider note, and omit it from model-performance denominators under a named policy.

### P0 — Enforce task/judge/test contract checks before a paid sweep

**Observed basis:** the clean comparator has an optimizer prompt that promises multi-step associativity while the judge checks a narrower one-chain behavior; the physical-constraints judge imposes a 5:3 ratio absent from the prompt; the lens prompt/judge/visible-test claims do not line up exactly. (`F-15`.)

**Proposal:** Give each task a machine-readable contract declaring:

- the behavior/property and valid alternatives the task intends to test;
- which requirements appear in prompt, starter code, visible tests, and hidden judge;
- the independent reference/oracle and its verified instances;
- expected fail/pass examples, counterexamples, and generated workspace hashes.

A preflight should fail closed when a hidden judge requirement is absent from the task specification, when a visible and hidden test contradict, or when a reference fails its own instance. Keep compile-only tasks clearly exploratory until they receive an independent behavioral reference.

### P0 — Lint every advertised axis against rendered task and judge artifacts

**Observed basis:** a static comparator scan finds ten category-track control/value placeholders across nine environments with no direct source-template reference; both `compositional_optimizer` axes are among them. This does not prove the paid workspaces were identical, because the campaign records a dirty tree. (`F-01`, `F-14`.)

**Proposal:** For every axis level, materialize and diff the rendered agent-visible prompt/starter/tests and judge-visible files. Require at least one declared artifact to change, verify that the changed value is consumed (not only text-substituted), and store per-level hashes/diffs. Mark axes as `label_only`, `agent_visible`, `judge_only`, or `both`; block a campaign when an axis is advertised as a manipulation but produces no relevant diff. Include a clean tree hash and complete dirty diff in the campaign bundle.

### P1 — Validate failure taxonomy labels against final artifacts

**Observed basis:** all 24 eligible `patch_invalid` rows have empty patch files; the two `overfit_visible_tests` rows have trusted scores of 1.0 and missing-required-companion-file notes; ten `source_invalid` rows are validator outcomes. (`F-09`.)

**Proposal:** Implement post-judge consistency checks:

- `patch_invalid` must include a validator code and patch hash; empty patch gets its own subcode.
- `overfit_visible_tests` requires evidence of a visible-test pass and a hidden/reference-test failure attributable to leakage/overfitting, not a missing-file condition.
- `source_invalid` must include parser/allowlist diagnostics.
- `runtime_error` must link stderr/exit status and distinguish agent-code errors from runner/container errors.
- `underfit` must identify the specific behavioral checks that failed.

If label evidence is insufficient, emit `unclassified` instead of a confident cognitive-sounding label.

### P1 — Report score mode, reference coverage, and semantic family separately

**Observed basis:** 122 raw cases are `compile_only` and explicitly exploratory; `behavioral_reference` labels are not equivalent to an independent environment-level oracle self-test; seven epistemic cases are assigned to `ml_debugging` despite different task semantics. (`F-04`, `F-05`.)

**Proposal:** Store independent dimensions for `execution_track`, `task_family`, `judge_mode`, `instance_reference_status`, and `external_validation_status`. Require score tables to stratify by mode and display exclusions. A single combined score may be shown only when calibration demonstrates compatible semantics; otherwise label it descriptive and mixed-mode.

### P1 — Define and reconcile telemetry counters

**Observed basis:** successful response rows, turn IDs, per-run manifest attempts, API error logs, checkpoint attempts, and progress totals disagree; `reasoning_enabled=false` coexists with reasoning-usage fields; no spend field is exported. (`F-13`.)

**Proposal:** Specify distinct counters for logical model turns, HTTP requests, retries, successful responses, provider failures, token usage, and wall/active time. Emit one event ID per attempt so counters can be reconciled. Persist request settings and provider-reported usage separately; validate incompatible metadata but never infer a cost if billing data is absent. Public tables should report source and scope for every counter.

### P1 — Preflight provider modality and case feasibility before selection

**Observed basis:** 17 selected `rope` cases were unsupported by the text-only provider; 7 more were blocked before provider calls because known references/calibration were not valid for their instances. (`F-02`.)

**Proposal:** Add a non-billable preflight that validates provider input modality, required task assets, reference coverage, negative controls, and oracle self-tests before a case enters the paid selected set. Persist `provider_calls_before_omission=0` as a checked invariant for gate-blocked rows.

## B. Future experiments — useful hypotheses, not confirmed fixes

### E1 — Replicate nominal-axis effects

Run multiple independently sampled seeds per cell, randomize order, and separate axis factors rather than changing size, name, hint, and implementation requirements together. Pre-register the analysis before a new campaign if confirmatory language is desired. A factorial or blocked design is a future experiment; the current archive cannot estimate those effects retrospectively.

### E2 — Test surface cues separately from hidden input size

For the regex and other weird-machine tasks, hold class names and instructions fixed while changing only the operative implementation, then hold the implementation fixed while changing only names/hints. Generate matched instances across sizes and use a judge that separately reports valid output, behavioral correctness, and runtime. Replicate at each point. This can test the surface/depth hypothesis; the existing 25/30 weird-machine total and regex contrast do not establish it.

### E3 — Build an explicit recursive strategic-reasoning family

Keep current epistemic-games tasks as exact Bayesian calibration. Separately specify player policies, utilities, observer alternation, recursive belief updates, and how those produce actions. Evaluate held-out policies and counterfactual observations with independent expected answers. The seven current passes are not a baseline estimate for this future task.

### E4 — Validate category/compositional properties independently

For each mathematical task, define a formal property and generate valid alternatives/counterexamples. Compare model submissions with an independent executable reference, property-based tests, or human mathematical adjudication as appropriate. Avoid using a framework/theory label as a proxy for task construct. A stronger oracle could reveal whether the current source/judge mismatches materially change pass outcomes.

### E5 — Assess compile-only score calibration

On a sample of compile-only tasks, run independent behavioral adjudication without showing adjudicators model verdicts. Estimate how often compile/test passes agree with that reference and whether agreement varies by environment. Until such a study exists, keep compile-only rows exploratory and report them separately.

### E6 — Replicate the failure-layer dashboard

After implementing the layered status schema, replay archived raw cases offline through the revised report generator and check that provider failures, empty patches, syntax errors, missing files, and behavioral test failures land in distinct bins. This is a deterministic reporting test, not a model rerun. Then compare the new report against the archived raw evidence before using it on a paid campaign.

## C. Implementation order and acceptance checks

1. **Before the next paid campaign:** complete P0 case ledger, provider/action separation, task/judge contract validation, axis rendered-diff lint, and provider/oracle preflight.
2. **Before publishing a single score:** include mode-stratified counts, explicit omissions/exclusions, final provider notes, and a validated failure taxonomy.
3. **Before causal language:** run E1/E2 with repeated cells and matched interventions; do not retroactively reinterpret the existing seed-0 sweep.
4. **Before capability or mathematical-competence language:** complete E3/E4 and independent reference validation.
5. **After any implementation:** add offline report/schema tests and show a before/after comparison on the unchanged archive. Do not claim an improvement until these checks pass; do not run the inert campaign YAML as a runtime mission.
