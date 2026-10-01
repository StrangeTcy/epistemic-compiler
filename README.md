# Epistemic Compiler & Research Production Protocol (V0)

> ** Core Principle:** V0 is not speculative orchestration software. It is a typed, provenance-preserving **Intermediate Representation (IR) for research** (modeled as a sheaf of local work-package charts $U_i$ with explicit restriction maps $\rho_{ij}: \mathcal{F}(U_i) \to \mathcal{F}(U_i \cap U_j)$), paired with a **four-gate manual execution protocol** and a **real-time friction instrumentation system** (`friction_log.yaml`).

---

## Repository Structure

```text
.
├── README.md
├── research_protocol/
│   ├── protocol.md                        # Part I: 7-type Ontological IR, 4 Human Gates, Sheaf Restriction WP Schema
│   └── instrumentation.md                 # Part II: Real-time friction schema, 13-type vocabulary, kappa metrics, Aborts
└── mission-01/
    ├── seed.yaml                          # Part III: Unified Seed S01 (Evaluator Blind Spots + Sheaf Gluing Obstructions)
    ├── friction_log.yaml                  # Real-time log of all human interventions (F-001 .. F-004+)
    ├── council/
    │   ├── prompts/                       # Part IV: Self-contained prompts for external Arena models
    │   │   ├── 01_theorist_prompt.md
    │   │   ├── 02_experimentalist_prompt.md
    │   │   ├── 03_skeptic_prompt.md
    │   │   └── 04_prior_work_killer_prompt.md
    │   ├── theorist.md                    # Target file for P01-T output
    │   ├── experimentalist.md             # Target file for P02-E output
    │   ├── skeptic.md                     # Target file for P03-S output
    │   └── prior_work_killer.md           # Target file for P04-PW output
    ├── critiques/                         # Cross-critique outputs
    ├── gates/
    │   ├── gate1_question.md              # Gate 1: Question & Prior-Work Survival
    │   ├── gate2_measurement.md           # Gate 2: Decision Table, Controls & Claim Ceiling
    │   ├── gate3_execution.md             # Gate 3: Work Package Cover & Restriction-Map Validation
    │   └── gate4_claim.md                 # Gate 4: Audited Evidence & Executable Falsification Sign-off
    ├── spec/                              # draft.yaml and approved.yaml (populated at Gate 2)
    ├── work_packages/                     # Bounded work packages WP-01..WP-NN (populated at Gate 3)
    ├── results/                           # Raw and aggregated experimental evidence
    ├── falsification/                     # Executable falsification experiments (max 3 exps, 1 round)
    └── claim_set.md                       # Final audited claims (populated at Gate 4)
```

---

## Mission 01 Target: `rl_eval_generator`

- **Target Repository:** [`StrangeTcy/rl_eval_generator`](https://github.com/StrangeTcy/rl_eval_generator)
- **Seed Title (`S01`):** *Local-Section Validity vs. Global Sheaf Gluing in Multi-Module Agent Evaluation and Orchestration*
- **Current Stage:** **Stage 1 — Adversarial Research Council (Pre-Gate 1)**
  - Run the four self-contained prompts in [`mission-01/council/prompts/`](mission-01/council/prompts/) across independent Arena models and record their outputs in `mission-01/council/*.md` to adjudicate [`mission-01/gates/gate1_question.md`](mission-01/gates/gate1_question.md).
