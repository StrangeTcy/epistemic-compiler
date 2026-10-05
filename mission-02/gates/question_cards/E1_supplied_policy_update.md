# E1 — Updating from a supplied behavior policy

**Status:** first serial question card; working draft only. E1 remains in the retained portfolio. This card is not a Gate 1 decision, seed rewrite, Arena prompt, Gate 2 specification, or experiment authorization. No Arena call has been made for E1.

## Candidate empirical question

> **On finite two-world instances with a disclosed behavior table, do specified language models' numeric posterior estimates and categorical verdicts track exact Bayesian updating as prior odds and observation likelihood ratios vary, rather than reflecting the prior alone or surface framing?**

This asks about use of supplied evidence and policy tables. It does **not** claim to measure recursive level-k reasoning, theory of mind generally, or inference of an undisclosed partner policy.

## Minimal formal target

For worlds `w1` and `w2`, a prior `P(w1)`, and an observed action `a` with registered likelihoods `P(a|w1)` and `P(a|w2)`, the ground-truth posterior is:

```text
posterior_odds(w1 | a)
  = prior_odds(w1) * likelihood_ratio(a)

likelihood_ratio(a) = P(a | w1) / P(a | w2)
```

E1 varies the prior odds and likelihood ratio independently across finite, well-posed cases. The response format and score must distinguish a numeric posterior from a categorical verdict; a correct category alone does not establish posterior calibration.

## Competing hypotheses (candidate, not registered)

- **H1 — evidence-sensitive updating:** model posterior estimates move in the direction and approximate amount specified by the Bayes factor when likelihood ratios change, while also responding correctly to prior odds.
- **H0 — prior-dominant / evidence-neglect account:** estimates mostly follow the prior or a simple base-rate rule and under-respond to changes in the supplied likelihood ratio.
- **H2 — surface-sensitive account (optional alternative):** estimates change with narrative/table presentation even when the formal prior and likelihoods are identical; apparent updating is not stable across equivalent renderings.

H1 versus H0 is the core discrimination. H2 is a candidate alternative that would need a matched-rendering comparison; it should not be folded into the primary contrast without stating that claim separately.

## Observable and contrast

- **Primary observable:** numeric `posterior_world1` error relative to the exact posterior (with calibration or proper-score summaries specified later), plus the registered categorical verdict as a secondary observable.
- **Core contrast:** model outputs across instances that change the prior odds or likelihood ratio while holding the other formal inputs fixed; compare observed changes with Bayes-predicted changes and the prior-only prediction.
- **Potential matched rendering contrast:** the same formal instance presented in narrative and bare-table forms, as in the described v0 axes. This can test surface sensitivity but is not required to define H1 versus H0.
- **Do not set:** solver identities, trial counts, margins, power, sampling settings, or arm order here. Those belong to a later measurement design if Gate 1 is human-approved.

## Relation to the existing Mission 02 substrate

`mission-02/seed.yaml` describes an upstream `envs/epistemic_games` v0 prototype at `rl_eval_generator` commit `e1b038a`. The seed says v0 has two hidden worlds, one public observation, a supplied behavior table, exact rational Bayes ground truth, and axes including evidence strength, prior, and narrative-versus-table presentation. It also says the generator and judge share `core.py`, the task is answer-only, and v0 does not implement recursive level-k reasoning.

Therefore, E1 as currently worded may be a **reuse/baseline question on the existing v0 substrate**, not a novel task-family contribution. Keep E1 in the portfolio as directed. During its development, state clearly whether it tests a new behavioral factor beyond the existing prototype or serves as a calibration/baseline anchor for later E- and S-questions. Do not relabel evidence neglect on supplied tables as higher-order reasoning.

## Gate 1 audit status

| Gate 1 criterion | Current E1 status | What remains |
|---|---|---|
| Sharp empirical discrimination | **Promising candidate** | Confirm the task unit and whether E1 is a standalone behavior question or a baseline/anchor for other questions. |
| Competing plausible hypotheses | **Candidate pair stated** | Source-check whether H1/H0 are both plausible in this target domain; separate H2 if retained. |
| Prior-work differentiation | **Open** | Search source-level work on LLM Bayesian updating, probability calibration, and supplied-policy inference; distinguish existing v0 and nearby benchmarks from any E1-specific contribution. |
| Existing/local architecture | **Seed-described, not freshly verified here** | Confirm the pinned source and the feasibility of independent ground-truth checking; the shared generator/judge implementation is an explicit limitation. |

## Questions to resolve before E1 is marked ready for Gate 1 review

1. Is E1 intended as an independently interesting question about model use of supplied likelihoods, or primarily as a baseline that enables another question?
2. Which exact posterior observable makes under-updating distinguishable from prior neglect and ordinary numerical imprecision?
3. What source-level prior work addresses LLM Bayesian/probabilistic updating on supplied likelihood tables, and what specific regime—if any—remains open?
4. Does reusing v0 provide enough accessible architecture for E1, and what minimal independent check is needed given that its current generator and judge share an implementation?

**Next dependency:** resolve the E1 substrate description, then develop V3 (verifier feasibility) and V1 (text-to-formal fidelity) for this same family before using E1 as the substrate for S2/S3. This sequence does not drop or approve any other portfolio item.
