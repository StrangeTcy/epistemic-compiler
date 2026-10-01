# GATE 2 — MEASUREMENT (`mission-01/gates/gate2_measurement.md`)

**Status:** `PENDING` (Requires Gate 1 PASS + `spec/draft.yaml`)

## 1. Gate Inputs Checklist
- [ ] Approved `mission-01/gates/gate1_question.md`
- [ ] `mission-01/critiques/cross_critique.md`
- [ ] `mission-01/spec/draft.yaml`

## 2. Gate 2 Acceptance Criteria Verification
- [ ] **Non-Degenerate Decision Table:** Every hypothesis $H_i$ has a prior $P(H_i)$ and conditional likelihoods $P(O_j \mid H_i)$ across mutually exclusive observation regimes $O_j$.
- [ ] **Marginal Plausibility / EIG Check:** Discriminating observations $O_j$ are not vanishingly rare corner cases.
- [ ] **Non-Circular Measurements (`M01..Mnn`):** Measurements quantify independent structural properties rather than assuming the conclusion.
- [ ] **Confound Coverage (`CF01..CFnn` $\rightarrow$ `CTRL01..CTRLnn`):** Every critical confound has a concrete control or an explicit scope boundary in the Claim Ceiling.
- [ ] **Pre-Committed Claim Ceiling & Evidence Contract:** `claim_ceiling`, `cannot_justify`, and `evidence_required` (`E01..Enn`) are locked before implementation.

## 3. Audited Decision Table Summary
*(To be populated during Gate 2 review)*

## 4. Human Adjudication Decision
- **Decision:** `[ PENDING: PASS -> write spec/approved.yaml | REVISE (max 3) | ABORT-03 ]`
- **Human Notes / Corrections:**
