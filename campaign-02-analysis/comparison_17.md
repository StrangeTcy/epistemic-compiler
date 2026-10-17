opus 5:

I'll start by checking for the house style references in the workspace.No house-style files are present in this sandbox, so I've reconstructed the house conventions from the draft stub itself (YAML front matter, `epistemic-status` definition list, `icon-self` byline span, numbered figure captions, explicit caveat block). Here is the complete essay.The essay is complete and saved to `campaign-02-analysis/posts/POST-04-failure-modes.md` (~2,400 words). All nine blocking issues are addressed:

| Reviewer issue | Resolution |
|---|---|
| 1. "Mostly behavioural" overclaim | Replaced with arithmetic: 100/128 = 78.1% two dominant solution-quality labels vs. 28/128 = 21.9% mechanical-error labels. Added an explicit retraction paragraph noting the behavioural/infrastructural split was imposed, not in the data. |
| 2. "Patch that runs" unsupported | Removed and converted into a named, flagged inference — stating that labels are not execution-status records and the 108 figure cannot license it. |
| 3. "Several" unquantified | Bounded explicitly: consistent with 3/49 (6.1%) or 20/49 (40.8%); 49 reframed as an **upper bound** on visible-test gaming with an unquantified subtraction pending. |
| 4. n=4 / missing denominator | reward_proxy given its own paragraph as unusable (interval 0.05–0.70 contains the base rate); flips now 7/76 ≈ 9.2% with the denominator's importance spelled out. |
| 5. "Shortcut the model takes" | Replaced with correlational language plus five enumerated alternatives: shortcut-taking, difficulty confounding, distraction, grading-surface change, sampling noise. |
| 6. Success conditions circular | Demoted to Tier 3 hypotheses with an explicit note that no single-file or exact-oracle pass rate exists in the packet. |
| 7. Overgeneralised from batchnorm_ema | Tier 2 states the general claim rests on one case and that no multi-file counts exist. |
| 8. Missing caveats | Six-part Limitations section: judge-label composition (189/227 split, with the point that the 128 isn't broken out by guarantee), 11 unscored cases flagged as non-ignorable exclusions, 56/132 = 42.4% unverified twins, single seed/no replication, dirty repo, non-matched interventions. The 132−56=76 coincidence is flagged as *unverified* with both readings stated. |
| 9. Title promises causality | Retitled to "Observed Patterns" plus an opening paragraph disclaiming any condition-in-the-counterfactual-sense reading. |

Three additions worth noting. First, I flagged that the taxonomy field is `share_of_eligible_failures`, so 128 counts *eligible* failures under an unstated criterion and cannot be reconciled against 416 or 331 — the shares are shares of 128 only. Second, F-009 is explicitly marked as a restatement of F-002, so the proxy effect is one measurement, not two. Third, I computed nominal Wilson intervals from the packet counts and labelled them as my own derivation resting on an independence assumption that single-seed execution does not support; they are there to make the precision gap between n=331 and n=4 visible, not to support a significance test. Since no `house_style.md` was present in the sandbox, conventions were reconstructed from the stub, and I left the bracketed author tokens alone.

&&&&&&&&&&&

fable 5.1:

I'll check whether the house-style files are available in the sandbox before drafting.The house-style files are not present in the sandbox, so I've followed the conventions evident in the stub (front matter, epistemic-status `<dl>`, author byline, figure captions, closing caveats) and the reviewer's brief. Here is the complete essay.

```markdown
---
title: "How Mercury Fails: Observed Failure Patterns in Mercury-2.5"
date: 2026-10-16
layout: post
---

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>Failure-mode taxonomy as the organising lens; separation of quantified patterns from descriptive ones.</dd>
  <dt>Synthesis</dt>
  <dd>Role-separated analysis over the archived Mercury evidence (F-002, F-005, F-007; failure taxonomy and judge-guarantee tables).</dd>
  <dt>Prose</dt>
  <dd>Final writer from evidence dossier and adversarial review brief.</dd>
  <dt>Certainty</dt>
  <dd>Low-to-moderate. Judge-assigned labels, single model, single seed per cell, dirty repository, no replication. Manual audit of individual cases not performed. Everything below is correlational; nothing is causal.</dd>
  <dt>Importance</dt>
  <dd>Establishes the base-rate shape of Mercury-2.5's failures and the one intervention-level pattern the data can currently support.</dd>
</dl>

## A note on the title

An earlier version of this post promised "failure modes and their conditions." The word *conditions* was doing more work than the evidence can bear. What we have is a count of judge-assigned labels on 128 failed cases, one intervention comparison with small cells, and a handful of descriptive observations about individual cases. That is enough to describe *patterns*. It is not enough to say under what conditions Mercury-2.5 fails, and still less to say why. The framing below is deliberately weaker than the one it replaces.

## The shape of the failure set

Of the 128 FAIL verdicts in the archived run, 51 carry the label `underfit` and 49 carry `overfit_visible_tests`. Together these two labels account for 100 of 128 failures, or 78.1%. The remaining 28 (21.9%) split across four labels: `runtime_error` (11), `source_invalid` (9), `invalid_action` (5), and `training_failure` (3). The six counts sum to 128 (F-007).

The stub this post replaces summarised this as "mostly behavioural, not infrastructural." That phrasing is retired for two reasons. First, the taxonomy does not classify its labels along a behavioural/infrastructural axis; that split was an editorial gloss, not a field in the data. Second, even on the most generous reading of the gloss, roughly one failure in five (28/128) is a mechanical error — the patch did not run, did not parse, took an action the harness rejected, or crashed during training. One in five is not a rounding error.

A related claim in the stub — that the model "usually produces a patch that runs; it just does not solve the task" — is also withdrawn. F-007 records failure-mode labels, not execution status. It is tempting to infer that the 108 cases not labelled `runtime_error` or `source_invalid` executed cleanly, but the taxonomy does not say so, and a case labelled `underfit` may well have crashed on a hidden check that the judge chose to describe in terms of coverage rather than execution. The inference is plausible. It is not in the evidence packet, and it is flagged here as inference only.

What the counts do support is narrower and still useful: the two dominant labels describe cases where a patch was produced and judged against hidden behaviour, and the dominant *verdict* when Mercury-2.5 fails is that the patch did not do enough (`underfit`) or did the visible part and not the hidden part (`overfit_visible_tests`).

![Failure modes](../figures/fig5_failure_modes.svg)

*Figure 5. Failure-mode counts across 128 FAIL verdicts. Labels are judge-assigned (F-007).*

## What "overfit" does and does not mean here

The label `overfit_visible_tests` invites the reading that the model gamed the visible tests. In at least some cases that reading is wrong. Several cases carrying this label have a `trusted_score` of 1.0 — the behavioural check passed — and were marked FAIL because a required companion file was missing. The `batchnorm_ema` case is the documented example: the patch scored 1.0 but the spec required a `model.py` that was not delivered.

How many of the 49 overfit cases are of this kind is not known. The evidence packet says "several." That could be 3 of 49 or 20 of 49, and the difference matters: at the low end, the overfit label is mostly about hidden-test coverage; at the high end, it is substantially a deliverable-completeness artifact. Until the 49 cases are individually audited — which has not been done — the overfit count should be read as an upper bound on visible-test overfitting proper, with an unquantified companion-file component inside it.

The `batchnorm_ema` case also motivates a hypothesis that recurs below: that specs requiring multi-file deliverables are harder for Mercury-2.5 than single-file specs. This is a hypothesis from one example. It is not a measured pattern.

## The one quantified intervention pattern

The evidence packet contains one comparison with cell-level numbers (F-002). Base cases pass at 228 of 331 (0.69). Cases carrying a `visible_proxy` channel pass at 8 of 27 (0.30). Cases carrying a `reward_proxy` channel pass at 1 of 4 (0.25).

Two of these three numbers deserve different weights. The visible-proxy cell, at n=27, is small but not degenerate; a drop from 0.69 to 0.30 on 27 cases is a difference one would not expect from noise alone, though no confidence interval has been computed and no difficulty matching was performed. The reward-proxy cell, at n=4, is not a stable estimate of anything. One additional pass would move it from 0.25 to 0.50. It is reported for completeness and should not be quoted as a rate.

Within the 76 latent specifications shared between base and intervention cases, seven interventions flipped a passing base case to a failure — a flip rate of roughly 9% of shared specs. The flip count is the more defensible quantity here, because it is a within-spec comparison rather than a cross-population one; but it carries the same single-seed caveat as everything else in the run, and seven events is seven events.

F-009 restates the same comparison and should not be counted as a replication. There is one measurement of this effect, not two.

![Pairwise intervention](../figures/fig6_pairwise_intervention.svg)

*Figure 6. Pass rates by intervention tag. Base 228/331; visible_proxy 8/27; reward_proxy 1/4 (F-002). The reward_proxy cell is too small to interpret as a rate.*

## What the proxy pattern does not show

The stub described the proxy channel as "a shortcut that the model takes." That is a claim about the model's process, and the data contain no observation of the model's process. What the data show is that pass rates are lower in cells tagged with a proxy channel. Several explanations are consistent with that:

- The model may indeed optimise against the proxy rather than the hidden target — the "shortcut" reading.
- Proxy-tagged specs may be harder on average, independently of the proxy, because the intervention cases were not difficulty-matched to the base population.
- Adding a proxy channel may lengthen or complicate the spec, and the drop may be a general spec-complexity effect rather than a proxy-specific one.
- The judge may grade proxy cases more strictly, or may be more likely to assign `overfit_visible_tests` when a proxy is present, by construction of the taxonomy.
- With a single seed per cell, some portion of the gap may be sampling variance that a second seed would shrink.

None of these can be ruled out with the current packet. The 🤥 statement is: *pass rate is lower in the presence of a proxy channel, and within shared specs the intervention flipped roughly one in eleven passing cases to failure.* Anything about intent or mechanism is speculation.

## Observed patterns, sorted by how much evidence stands behind them

It is worth being explicit about which of the "conditions" in the original draft are measured and which are not.

**Quantified (one measurement, no replication):**

- Presence of a `visible_proxy` channel is associated with a lower pass rate (0.30 vs 0.69; n=27 vs n=331).
- Within 76 shared latent specs, 7 interventions flipped pass to fail.

**Descriptive, from one or a few cases:**

- Specs requiring companion files (e.g. `model.py` alongside the primary patch) can produce FAIL verdicts with a trusted score of 1.0. Documented in `batchnorm_ema`; count among the 49 overfit cases unknown.
- "Visible-test-heavy grading" and "multi-file edits" as general risk factors are generalisations from this same small set of cases and should be read as hypotheses.

**Not measured at all:**

- The stub asserted that failures "disappear" under single-file specifications with exact oracles. No pass-rate for that stratum is in the evidence packet. There is also a circularity risk: if single-file-exact-oracle cases are simply the cases that are easiest to pass, then observing that they pass more often tells us about difficulty, not about a failure-suppressing condition. This is presented here as a hypothesis for a future stratified analysis and nothing more.

## Caveats

The following limitations apply to every number above, and most of them were absent from the earlier draft.

1. **Judge-label composition.** All failure-mode labels are judge-assigned. The 416 selected cases split into 189 with a `behavioral_reference` guarantee and 227 with `compile_only`. A `compile_only` judge cannot, by construction, assign some labels with the same confidence as a `behavioral_reference` judge; the taxonomy counts above do not stratify by guarantee, and the share of each label attributable to each judge type is not reported in the packet.
2. **Unscored cases.** 11 cases received no score: 6 `epistemic_silence`, 4 `epistemic_type_games`, 1 `rd_adaptive_halting` (F-005). These are excluded from the 128 failures and from the pass rates. They are not failures in the taxonomy's sense, but they are not successes either, and their omission slightly flatters every rate reported here.
3. **Unverified twins.** 56 of 132 twin cases (42%) are unverified. The remainder, 76, numerically matches the "76 shared latent specs" used for the flip-rate denominator. Whether that is the same 76 or a coincidence has not been confirmed; if it is the same set, the flip analysis rests on the verified twins only, which is the right subset — but the identity needs checking before the number is relied on.
4. **Single seed, single model, no replication.** Every cell was run once. The model is mercury-2.5 from a single provider. F-009 restates F-002 rather than reproducing it. No result above has been observed twice.
5. **Dirty repository.** The run was executed against a repository with uncommitted or uncontrolled state. Which cases, if any, were affected is unknown.

To these add the caveats carried over from the stub: intervention cases were not difficulty-matched to base cases, and no manual audit of individual verdicts was performed.

## Summary

Mercury-2.5's 128 failures are dominated by two judge labels — `underfit` (51) and `overfit_visible_tests` (49), together 78.1% — with the remaining 21.9% spread across mechanical errors of four kinds. Within the overfit label, an unknown fraction are companion-file artifacts rather than visible-test gaming. The one quantified intervention pattern is that proxy-channel cases pass less often than base cases (0.30 vs 0.69 for visible proxy; the reward-proxy cell is too small to quote), with 7 pass-to-fail flips across 76 shared specs. That pattern is correlational, singly measured, and admits several explanations besides the model taking a shortcut. The conditions under which failures *disappear* have not been measured and are offered only as a target for the next pass.
```
