# E1 — Updating from a supplied behavior policy

**Status:** first serial question card; working draft only. E1 remains in the retained portfolio. This card is not a Gate 1 decision, seed rewrite, Arena prompt, Gate 2 specification, or experiment authorization. No Arena call has been made for E1.

## Candidate empirical question

> **On the pinned v0 two-world task grid with disclosed behavior policies, do specified language models' reported posterior probabilities and categorical verdict/support answers track the exact Bayesian ground truth across the registered prior and evidence conditions, rather than following a prior-only prediction?**

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

- **Primary observable:** numeric `posterior_world1` error relative to the exact posterior (with calibration or proper-score summaries specified later). Track the evidence-strength `verdict` and directional `most_supported` classification as distinct categorical observables; a correct category alone does not establish posterior calibration.
- **Core contrast:** model outputs across instances that change the prior odds or likelihood ratio while holding the other formal inputs fixed; compare observed changes with Bayes-predicted changes and the prior-only prediction.
- **Potential matched rendering contrast:** the same formal instance presented in narrative and bare-table forms, as in the described v0 axes. This can test surface sensitivity but is not required to define H1 versus H0.
- **Do not set:** solver identities, trial counts, margins, power, sampling settings, or arm order here. Those belong to a later measurement design if Gate 1 is human-approved.

## Relation to the existing Mission 02 substrate

The pinned source is `rl_eval_generator` commit `e1b038a4efb7343afd713f4e981c90fc0fb0485c`, under `envs/epistemic_games/`. I made a read-only spot check of its configuration and renderer/judge path:

- `config.yaml` defines the existing axes: two templates, three evidence bands, two presentations, two priors, and two framings. The priors are specifically 0.5/0.5 and 0.6/0.4; the evidence cases are a small discrete set classified as R=1, 1<R<3, or R>=3. This is not a continuous sweep.
- `files/renderer.py` calls `core.build_instance(...)`, then obtains both `instance.public_task_md()` and `instance.to_spec()` from that same instance.
- `files/judge.py` imports `core`, rebuilds the instance from the parameters, checks it against the renderer-produced `INSTANCE_SPEC`, and grades the answer. `files/instance_spec.py` explicitly says the judge rebuilds using `core.py`.
- `files/core.py` contains both the exact rational Bayes computation and the public English/bare-table task rendering. Its own docstring says v0 does **not** implement a recursive level-k engine; level labels are used in the specified behavior-policy/narrative construction.
- The task requests four fields: evidence-strength `verdict`, numeric `posterior_world1`, directional `most_supported`, and a short justification. The existing grader scores posterior error plus both categorical fields (weights 0.5/0.3/0.2); strict correctness requires all categorical checks and posterior error at most 0.02. These are existing v0 scoring rules, not newly proposed thresholds.

**V3 / verifier finding:** v0 has a separate judge entry point and an explicit provenance/anti-tamper check, but the judge and renderer reuse the same `core.py`. This is not independent recomputation of the semantics. The environment format has a judge-side extension point, so a second implementation appears locally plausible, but the inspected files do not establish the effort or correctness of such an implementation.

**V1 / text-fidelity finding:** the renderer constructs the formal spec and agent-facing task from the same `Instance` object. The inspected path verifies clean rendering/provenance, but does not independently establish that a reader can reconstruct the intended formal instance from the English text. No independent text-to-model audit was found in these files.

Therefore, E1 is retained as a **baseline/anchor on the existing v0 substrate**, not as a novel task-family claim. Its current discrete prior/evidence grid can support a bounded calibration question; a broader posterior-calibration sweep would require a specified local extension. Do not relabel evidence neglect on supplied behavior tables as higher-order reasoning.

Source paths at the pinned revision: [`config.yaml`](https://github.com/StrangeTcy/rl_eval_generator/blob/e1b038a4efb7343afd713f4e981c90fc0fb0485c/envs/epistemic_games/config.yaml), [`renderer.py`](https://github.com/StrangeTcy/rl_eval_generator/blob/e1b038a4efb7343afd713f4e981c90fc0fb0485c/envs/epistemic_games/files/renderer.py), [`core.py`](https://github.com/StrangeTcy/rl_eval_generator/blob/e1b038a4efb7343afd713f4e981c90fc0fb0485c/envs/epistemic_games/files/core.py), [`judge.py`](https://github.com/StrangeTcy/rl_eval_generator/blob/e1b038a4efb7343afd713f4e981c90fc0fb0485c/envs/epistemic_games/files/judge.py), and [`instance_spec.py`](https://github.com/StrangeTcy/rl_eval_generator/blob/e1b038a4efb7343afd713f4e981c90fc0fb0485c/envs/epistemic_games/files/instance_spec.py). This is a bounded source spot-check, not a full code audit or proof that a proposed verifier extension will work.

## Gate 1 audit status

| Gate 1 criterion | Current E1 status | What remains |
|---|---|---|
| Sharp empirical discrimination | **Promising, now bounded to the pinned v0 grid** | Specify the unit of analysis and score later; keep the optional matched-rendering contrast separate from the primary Bayes-updating contrast. E1 is provisionally the baseline/anchor, not a novelty claim. |
| Competing plausible hypotheses | **Candidate pair stated** | H1/H0 still need domain evidence; keep H2 separate unless a matched-rendering claim is deliberately included. |
| Prior-work differentiation | **Open** | Search source-level work on LLM Bayesian updating, probability calibration, and supplied-policy inference; distinguish existing v0 and nearby benchmarks from any E1-specific contribution. |
| Existing/local architecture | **Pinned source spot-checked; feasibility partial** | v0 supplies exact Bayes ground truth but couples renderer and judge through `core.py`; a genuinely independent checker and text-fidelity audit are not present in the inspected path. Their local implementation remains to be specified and tested. |

## Remaining work before E1 is ready for Gate 1 review

E1 stays in the portfolio and is treated as a **baseline/anchor for now**, because v0 already supplies behavior policies and exact Bayesian ground truth. No standalone-novelty claim is being made. The candidate question is bounded to v0's finite grid; broader prior/likelihood coverage would need a separately specified extension.

1. Specify the posterior score and task unit so under-updating is distinguishable from prior neglect and ordinary numerical imprecision.
2. Search source-level prior work on LLM Bayesian/probabilistic updating with supplied likelihood tables, then state what (if anything) remains differentiated from v0 and nearby benchmarks.
3. For V3, define and test the smallest checker that does not reuse the generator's semantic implementation. For V1, define an independent text-to-formal fidelity check. The source check above identifies the gaps; it does not establish these extensions.

**Next dependency:** use this card's source findings to develop E1's V3 (independent-verifier feasibility) and V1 (text-to-formal fidelity) checks before using E1 as the substrate for S2/S3. This is local design work only: no Arena call, Gate 1 decision, Gate 2 specification, or experiment authorization. All other portfolio items remain retained and unapproved.
