# GATE 4 — CLAIM (`mission-01/gates/gate4_claim.md`)

**Status:** `PENDING` (Requires executed experiments in `results/` + executable falsification in `falsification/`)

## 1. Gate Inputs Checklist
- [ ] Raw & aggregated empirical evidence in `mission-01/results/`
- [ ] Executed falsification experiments (`FALS-01..03`) in `mission-01/falsification/`
- [ ] Pre-committed `mission-01/spec/approved.yaml` (`claim_ceiling`, `cannot_justify`, `evidence_required`)

## 2. Gate 4 Acceptance Criteria Verification
- [ ] **Complete Evidence Backing:** Every claim in `claim_set.md` links to concrete files/metrics in `results/` and `falsification/`.
- [ ] **Claim Ceiling Enforcement:** No claim exceeds `spec/approved.yaml -> claim_ceiling`.
- [ ] **Executable Falsification Audit:** Up to 3 adversarial critiques were converted into executable falsification experiments and run; any unexecuted critiques are logged as explicit open questions.
- [ ] **Preservation of Negative/Weakened Hypotheses:** Rejected or falsified hypotheses remain documented.

## 3. Mission Outcome Classification
- **Outcome Class:** `[ PENDING: positive_finding | negative_result | inconclusive_result | failed_measurement_design | prior_work_collision | follow_up_question ]`
- **Human Adjudication Decision:** `[ PENDING ]`
