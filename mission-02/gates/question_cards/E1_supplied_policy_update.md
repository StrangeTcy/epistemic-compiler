# E1 — Updating from a supplied behavior policy

**Status:** first serial question card; working draft only. E1 remains in the retained portfolio. This card is not a Gate 1 decision, seed rewrite, Arena prompt, Gate 2 specification, or experiment authorization. The assistant has made no Arena call for E1.

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

E1 varies the prior odds and likelihood ratio independently across finite, well-posed cases. For the posterior update, the likelihood ratio is signed: it can be below or above 1. In a log-odds analysis use `log(P(a|w1)/P(a|w2))`; do not substitute the unsigned evidence-strength statistic `R = max(L1/L2, L2/L1)`, which loses the direction of the update. The response format and score must distinguish a numeric posterior from categorical outputs; a correct category alone does not establish posterior calibration.

## Competing hypotheses (candidate, not registered)

A reviewer-suggested diagnostic for making the numeric predictions distinct is a response model in log-odds space:

```text
logit(reported_posterior)
  = beta0 + beta_prior * logit(prior_world1)
          + beta_LR * log(P(a|w1) / P(a|w2)) + error
```

Under exact Bayesian updating, the point target is `(beta0, beta_prior, beta_LR) = (0, 1, 1)`. This is a candidate estimand, not a registered analysis; any equivalence margins, estimator details, boundary handling, and sample design remain open.

- **H1 — evidence-sensitive Bayesian updating:** reported posteriors track both prior odds and the signed likelihood ratio, with coefficients near the exact Bayes targets.
- **H0a — likelihood neglect / prior-only updating:** `beta_LR` is near zero while prior odds retain influence.
- **H0b — prior neglect / base-rate neglect:** `beta_prior` is near zero while the signed likelihood ratio retains influence.
- **H0c — conservative updating:** the likelihood-ratio coefficient is positive but below the Bayes target, indicating systematic under-updating rather than merely noisy answers.
- **Noise:** zero-mean response imprecision would appear as residual variation and can coexist with any of the updating accounts; it is not itself a competing mechanism.
- **H2 — surface-sensitive account (optional):** estimates change with narrative/table presentation when the formal inputs are identical. Keep this matched-rendering contrast separate from the primary update contrast.

These are candidate distinctions, not registered thresholds. The signed likelihood ratio is essential: the v0 verdict band uses unsigned evidence strength `R`, which cannot serve as the directional log-likelihood predictor.

## Observable and contrast

- **Primary response:** model-reported numeric `posterior_world1`. Aggregate absolute posterior error can be reported descriptively, but by itself it does not distinguish systematic under-updating, prior-only responses, and noisy responses.
- **Candidate discriminator:** compare posterior log-odds against prior log-odds and the **signed** log likelihood ratio, with the Bayes coefficient vector as the reference. Test the model's evidence sensitivity on matched instances that vary the likelihood ratio while holding the prior fixed, and vice versa. Confirm from the realized finite item grid—not just the axis labels—that these inputs vary independently enough to identify the contrasts.
- **Boundary caution:** `logit(reported_posterior)` is undefined at reports of exactly 0 or 1; predefine how boundary/heaped responses are represented before interpreting coefficients. Check whether true posteriors in the v0 grid approach saturation. No clipping rule or threshold is selected here.
- **Categorical outputs:** score the evidence-strength `verdict` and directional `most_supported` separately. The verdict is based on unsigned `R`, not posterior direction; categorical correctness cannot substitute for numeric calibration. If retained as an outcome, inspect how much of the grid lies near its decision boundaries.
- **Potential matched-rendering contrast:** the same formal instance presented in narrative and bare-table forms, as in the v0 axes. This can test surface sensitivity but is not required to define the primary updating contrast.
- **Do not set:** solver identities, trial counts, numerical tolerance/equivalence margins, power, sampling settings, or arm order here. Those belong to later measurement design if Gate 1 is human-approved; no reviewer-suggested numeric tolerance is adopted.

## Relation to the existing Mission 02 substrate

The pinned source is `rl_eval_generator` commit `e1b038a4efb7343afd713f4e981c90fc0fb0485c`, under `envs/epistemic_games/`. I made a read-only spot check of its configuration and renderer/judge path:

- `config.yaml` defines the existing axes: two templates, three evidence bands, two presentations, two priors, and two framings. The priors are specifically 0.5/0.5 and 0.6/0.4; the evidence cases are a small discrete set classified as R=1, 1<R<3, or R>=3. This is not a continuous sweep.
- `files/renderer.py` calls `core.build_instance(...)`, then obtains both `instance.public_task_md()` and `instance.to_spec()` from that same instance.
- `files/judge.py` imports `core`, rebuilds the instance from the parameters, checks it against the renderer-produced `INSTANCE_SPEC`, and grades the answer. `files/instance_spec.py` explicitly says the judge rebuilds using `core.py`.
- `files/core.py` contains both the exact rational Bayes computation and the public English/bare-table task rendering. Its own docstring says v0 does **not** implement a recursive level-k engine; level labels are used in the specified behavior-policy/narrative construction.
- The task requests four fields: evidence-strength `verdict`, numeric `posterior_world1`, directional `most_supported`, and a short justification. The existing grader scores posterior error plus both categorical fields (weights 0.5/0.3/0.2); strict correctness requires all categorical checks and posterior error at most 0.02. These are existing v0 scoring rules, not newly proposed thresholds.

**V3 / verifier finding:** v0 has a separate judge entry point and an explicit provenance/anti-tamper check, but the judge and renderer reuse the same `core.py`. This is not independent recomputation of the semantics. The environment format has a judge-side extension point, so a second implementation appears locally plausible, but the inspected files do not establish the effort or correctness of such an implementation.

**V1 / text-fidelity finding:** the renderer constructs the formal spec and agent-facing task from the same `Instance` object. The inspected path verifies clean rendering/provenance, but does not independently establish that a reader can reconstruct the intended formal instance from the English text. No independent text-to-model audit was found in these files.

## Advisory response synthesis (non-decisional)

The linked bundle is preserved at [`e1_responses`](e1_responses). Its headings self-label two response sources (`grok 4.3`, `opus 5`); Arena mode, verified Arena-displayed model labels, session times, and tool metadata were not supplied. Treat the contents as advisory critiques, not as source-level evidence, verified literature review, Gate disposition, or authorization.

- The reviews converge on retaining E1 as the supplied-policy/v0 baseline rather than claiming a novel family. A possible agent-policy-versus-abstract-signal framing contrast is parked as a separate candidate extension; it is not folded into E1's primary question.
- The log-odds coefficient decomposition above is retained as a candidate way to distinguish likelihood neglect, prior neglect, and conservative updating. It is not registered; the realized grid's identifiability and boundary handling still need checking.
- The bundle's named papers and novelty claims remain **unverified leads**. The reviews do not close Gate 1's prior-work criterion; verify primary sources before citing or relying on those claims.
- No numeric tolerance or equivalence margin proposed in the bundle is adopted here.

## Proposed local V1/V3 feasibility check (not yet run)

1. **V1 — text-to-formal fidelity:** from only the rendered task text, independently record the prior, the two worlds' probabilities for the observed action, the observed action, and the world/action mappings. Freeze that record before exposing the annotator to `INSTANCE_SPEC` or generator internals; then compare the record with the formal spec. Include both narrative and bare-table renderings in the local check.
2. **V3 — independent recomputation:** compute the posterior, unsigned evidence-strength band, and directional support from the V1 text-derived record using a separate exact-arithmetic implementation (or a documented manual calculation). Do not call/import the generator's `core.py` or calculate from hidden instance parameters. Compare the independent result with the frozen spec and existing grader outputs.

This is a bounded feasibility plan, not an executed audit or an experiment. It remains to be implemented and tested before E1 can support later S2/S3 work.

Therefore, E1 is retained as a **baseline/anchor on the existing v0 substrate**, not as a novel task-family claim. Its current discrete prior/evidence grid can support a bounded calibration question; a broader posterior-calibration sweep would require a specified local extension. Do not relabel evidence neglect on supplied behavior tables as higher-order reasoning.

Source paths at the pinned revision: [`config.yaml`](https://github.com/StrangeTcy/rl_eval_generator/blob/e1b038a4efb7343afd713f4e981c90fc0fb0485c/envs/epistemic_games/config.yaml), [`renderer.py`](https://github.com/StrangeTcy/rl_eval_generator/blob/e1b038a4efb7343afd713f4e981c90fc0fb0485c/envs/epistemic_games/files/renderer.py), [`core.py`](https://github.com/StrangeTcy/rl_eval_generator/blob/e1b038a4efb7343afd713f4e981c90fc0fb0485c/envs/epistemic_games/files/core.py), [`judge.py`](https://github.com/StrangeTcy/rl_eval_generator/blob/e1b038a4efb7343afd713f4e981c90fc0fb0485c/envs/epistemic_games/files/judge.py), and [`instance_spec.py`](https://github.com/StrangeTcy/rl_eval_generator/blob/e1b038a4efb7343afd713f4e981c90fc0fb0485c/envs/epistemic_games/files/instance_spec.py). This is a bounded source spot-check, not a full code audit or proof that a proposed verifier extension will work.

## Gate 1 audit status

| Gate 1 criterion | Current E1 status | What remains |
|---|---|---|
| Sharp empirical discrimination | **Promising candidate, with a sharper estimand proposed** | Check the realized grid's rank/conditioning and boundary cases for the candidate log-odds contrast; keep numerical margins, scores, and design choices open for later. E1 remains the baseline/anchor, not a novelty claim. |
| Competing plausible hypotheses | **Candidate accounts now separated conceptually** | Assess whether the finite grid can distinguish likelihood neglect, prior neglect, and conservative updating; do not set thresholds here. Keep H2 separate unless the matched-rendering claim is deliberately promoted. |
| Prior-work differentiation | **Open; response-bundle leads unverified** | Verify source-level work on Bayesian updating, probability calibration, and supplied-policy inference before making any novelty claim. The `e1_responses` literature summaries are not verified findings. |
| Existing/local architecture | **Pinned source spot-checked; bounded check proposed, not run** | v0 couples renderer and judge through `core.py`. The proposed independent V1/V3 check must derive inputs from rendered text, not generator internals; agreement and feasibility remain untested. |

## Remaining work before E1 is ready for Gate 1 review

E1 stays in the portfolio and is treated as a **baseline/anchor for now**, because v0 already supplies behavior policies and exact Bayesian ground truth. No standalone-novelty claim is being made. The candidate question is bounded to v0's finite grid; a broader prior/likelihood sweep or the parked agent-policy-versus-abstract-signal contrast would be a separate extension, not part of this baseline.

1. Check the realized finite grid for independent variation and identifiability of prior and signed-likelihood effects; inspect true posterior saturation and define boundary handling for reported 0/1 values. Keep numerical margins and sample design for later.
2. Verify source-level prior work on LLM Bayesian/probabilistic updating with supplied likelihoods. Treat papers and novelty claims in `e1_responses` as unverified leads until checked against primary sources.
3. Run the proposed local V1/V3 feasibility check: blind text-to-formal extraction, then separate exact recomputation from those extracted values. Record outcomes and missing information; do not rely on the shared `core.py` path or generate model/experiment calls.

**Next dependency:** after human review of this synthesis, continue with the local V1/V3 check on E1 before using E1 as the substrate for S2/S3. This remains local, non-decisional work: no Gate 1 decision, Gate 2 specification, or experiment authorization. All other portfolio items remain retained and unapproved.
