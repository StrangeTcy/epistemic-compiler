sonnet 5:

# Adversarial Evidence Review — POST-04 ("How Mercury Fails")

**Reviewer verdict: Draft is directionally consistent with the evidence packet but contains at least four overclaims, two unsupported causal/behavioral inferences, one circular inference, and several material omissions (unscored cases, unverified twins, judge-guarantee composition, replication status). None of the core counts are factually wrong, but the *interpretive layer* wrapped around them outruns what F-002/F-005/F-007/F-009 actually support.**

---

## 1. "Mercury's failures are mostly behavioural, not infrastructural"

**Status: Overclaim — framing not supported by the taxonomy as given.**

The draft treats `runtime_error` (11), `source_invalid` (9), and `invalid_action` (5) as "the minority" and implicitly non-behavioral, while folding `underfit` and `overfit_visible_tests` into "behavioural." But:

- The evidence packet (F-007) does **not** label any category as "behavioural" or "infrastructural" — that taxonomy is an interpretive overlay invented by the draft, not present in the data.
- `runtime_error` + `source_invalid` + `invalid_action` + `training_failure` = 11+9+5+3 = **28/128 = 21.9%** of all FAIL verdicts. That is not a negligible residual — it is roughly one in five failures, and the draft's own flagged number (runtime_error = 11/128 = 8.6%) is explicitly non-trivial on its own.
- Calling a fifth of all failures "the minority" is numerically true but rhetorically minimizing. The sentence "mostly behavioural, not infrastructural" asserts a clean binary that the data doesn't cleanly support — it would be more honest to say "underfit and visible-test overfit dominate (100/128, 78%), but roughly one in five failures are mechanical (runtime/source/action/training errors)."

**Recommendation:** Replace "mostly behavioural, not infrastructural" with a hedged, quantified statement, and drop the implied binary.

---

## 2. "The model usually produces a patch that runs; it just does not solve the task"

**Status: Unsupported inference — not established by F-007.**

This sentence asserts that underfit and overfit_visible_tests cases are, by definition, *runnable* patches. Nothing in the evidence packet confirms this. `underfit` is a failure-mode label, not a runtime-status label; F-007 gives no field confirming execution success for the underfit/overfit bucket. The draft is reading "the code runs" into a category name. This is plausible but **not evidenced** — it should be flagged as an inference, not stated as fact. The only place execution status is directly evidenced is via the `runtime_error` bucket (11 cases where it explicitly did *not* run cleanly), which if anything undercuts the certainty of "usually."

**Recommendation:** Soften to "the taxonomy's naming suggests the model's patch often executes rather than crashing, though the packet does not directly confirm execution status for underfit/overfit cases."

---

## 3. "The label 'overfit' is therefore not direct evidence of visible-test gaming in every case"

**Status: Correct directionally, but under-quantified — a single anecdote is being used to qualify an entire 49-case bucket.**

The packet states only that **"several"** overfit cases have trusted_score 1.0 but fail due to a missing companion file (e.g., batchnorm_ema/model.py), offered as one illustrative example. The draft is right to flag that "overfit" ≠ "gaming" in every instance, but:

- "Several" is not quantified. We don't know if this affects 3 of 49 or 20 of 49 overfit_visible_tests cases. The draft should state this uncertainty explicitly rather than let the reader assume it's a minor edge case.
- This caveat, once taken seriously, also complicates the clean 51/49 underfit/overfit split presented at the top of the post as if those labels were self-evidently meaningful — if an unknown number of "overfit" cases are actually companion-file artifacts, the taxonomy's face-value reading is weaker than the opening paragraph implies.

**Recommendation:** State explicitly "the packet does not specify how many of the 49 overfit_visible_tests cases are companion-file artifacts vs. genuine visible-test gaming — this fraction is unknown and should not be assumed small."

---

## 4. Proxy intervention numbers

**Status: Numerically correct, but presented with false precision and without sample-size caveats.**

Checking the arithmetic: visible_proxy 8/27 = 0.296 ≈ 0.30 ✓; reward_proxy 1/4 = 0.25 ✓; base 228/331 = 0.689 ≈ 0.69 ✓; these match F-002/F-009. However:

- **n=4 for reward_proxy** is an extremely small sample. A single flip either direction changes the rate by 25 percentage points. Presenting "0.25" with the same confidence as "0.69" (n=331) is misleading without a sample-size caveat.
- The draft states "seven interventions flipped a passing base case to a failure" but omits the denominator — F-002 specifies this is **7 flips within 76 shared latent specs**. Omitting the 76 understates how modest this effect is in absolute terms (~9% flip rate) and makes "sharper" read as a bigger effect than the raw numbers justify.

**Recommendation:** Add the n=76 denominator and flag n=4 (reward_proxy) as too small to support a stable rate estimate.

---

## 5. "The proxy channel appears to offer a shortcut that the model takes"

**Status: Unsupported causal/intentional claim — this is the clearest overreach in the draft.**

This sentence anthropomorphizes the result: it implies the model *perceives* a shortcut and *chooses* to take it — a claim about internal model behavior/strategy. The evidence only supports a **correlational, outcome-level** fact: pass rates are lower when a proxy channel is present (0.30, 0.25 vs 0.69 base). Nothing in F-002/F-009 characterizes *why* pass rates drop — it could reflect the model being misled, the proxy channel making the task objectively harder to verify, grading artifacts in how proxy cases are scored, or confounds in which specs happen to get proxy treatment. "Offers a shortcut that the model takes" asserts a specific causal mechanism (strategic shortcut-taking) that the data cannot distinguish from several alternative explanations.

**Recommendation:** Replace with something like "pass rates drop sharply under proxy-channel conditions; the packet does not establish why — plausible explanations include genuine shortcut-seeking behavior, confounded task difficulty, or scoring artifacts specific to proxy grading, and the current design cannot adjudicate between them" (echoing the draft's own later caveat that "intervention cases not difficulty-matched" — which directly undercuts the shortcut-taking claim and should be pulled forward rather than buried in the caveats line).

---

## 6. "The conditions under which they disappear: environments with clear single-file specifications and exact oracles"

**Status: Unsupported / likely circular — no success-rate data is cited to back this claim.**

This is the weakest claim in the draft. The evidence packet contains a bare assertion — "Success conditions: single-file specifications, exact oracles" — but **no pass-rate numbers, counts, or comparison group** for single-file/exact-oracle cases are given anywhere in the packet (unlike the proxy-intervention claims, which have hard numbers). As written, the draft:

- Presents this as symmetric, evidence-backed counterpart to the failure conditions, when in fact the failure conditions (proxy, visible-test grading, multi-file/companion files) are backed by quantified data (F-002, F-007, the batchnorm_ema example) while the success conditions are backed by nothing but a label.
- Risks circularity: if "single-file spec" is essentially the *absence* of "multi-file edits/companion files," then asserting it as a cause of success is just restating the failure condition in reverse, not independent evidence that such environments actually show elevated pass rates.

**Recommendation:** Either cut this sentence or explicitly flag it as "asserted in the taxonomy but not independently quantified in the available data — no pass-rate comparison for single-file/exact-oracle cases is provided."

---

## 7. "Visible-test-heavy grading" and "multi-file edits/companion files" as general failure *conditions*

**Status: Overgeneralized from a single example.**

The only concrete evidence for multi-file/companion-file failure is the one batchnorm_ema illustration. The draft elevates this into a general "condition under which failures appear," alongside proxy channels (which *do* have n=27/n=4/n=331 quantification) and visible-test-heavy grading (which is really just a restatement of the `overfit_visible_tests` label itself, not an independently measured environmental condition). Lumping a well-quantified condition (proxy channels) together with two essentially anecdotal/definitional ones in a single bulleted list implies they carry equal evidential weight. They do not.

**Recommendation:** Separate the bullet list by evidential strength — proxy-channel effects are quantified; multi-file/companion-file and visible-test-heavy grading are descriptive/anecdotal and should be labeled as such.

---

## 8. Missing caveats the draft omits entirely

The draft's caveat paragraph ("judge-assigned labels; intervention cases not difficulty-matched; single model") is incomplete relative to what's in the packet:

- **Unscored/excluded cases (F-005):** 11 cases (6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting) are unscored and thus excluded from the 128-FAIL taxonomy entirely. If "epistemic_silence" means the model produced no scoreable output, that is arguably a *failure mode in its own right* that's missing from the draft's taxonomy altogether — the post should disclose that the 128-count denominator excludes these cases rather than presenting it as the complete universe of failures.
- **Unverified twins (F-005):** 56 of 132 twin cases (42%) are unverified. If the "76 shared latent specs" used for the pass→fail flip analysis draws on this twin pool, the flip count of 7 could be sensitive to unverified cases — this is a direct threat to the proxy-intervention claim in section 3 of the draft and is not mentioned anywhere.
- **Judge guarantee composition:** 189 behavioral_reference vs. 227 compile_only (416 selected) — the draft calls labels "judge-assigned" but never discloses that over half the judged pool relies on compile_only guarantees, which are a weaker correctness signal than behavioral_reference. This matters directly for how much weight readers should put on FAIL/PASS labels, especially for the overfit-vs-companion-file ambiguity discussed above.
- **Single seed per cell, dirty repo, no replication:** the draft mentions "single model" but drops three other explicitly flagged reliability threats (single seed per cell, dirty repository state, no replication). These are standard-setting caveats for this kind of benchmark post and their omission makes the piece read more confident than the underlying methodology warrants.

**Recommendation:** Expand the caveat paragraph to explicitly name all five limitations (judge-label composition, unscored cases, unverified twins, single-seed/no-replication, dirty repo), not just three.

---

## 9. Title/framing-level concern

"Recurring Failure Modes and **Their Conditions**" promises causal/conditional claims. Given single-seed, non-difficulty-matched, non-replicated data with a materially incomplete scored set, "conditions" is a strong word for what is, at best, a correlational pattern in one run of one model. This is not necessarily a factual error, but it's a framing choice that should be softened or caveated up front, not just in a closing disclaimer paragraph.

---

## Summary table of issues

| Draft Claim | Evidence Support | Verdict |
|---|---|---|
| "Mostly behavioural, not infrastructural" | F-007 raw counts only; taxonomy labels invented by draft | **Overclaim** |
| "Model usually produces a patch that runs" | Not stated in F-007 | **Unsupported inference** |
| "Overfit ≠ gaming in every case" | F-007 example, but "several" unquantified | **Correct but under-quantified** |
| Proxy pass-rate numbers (0.30/0.25/0.69) | F-002/F-009 | **Numerically correct**, but n=4 and n=27 need caveat |
| "7 flips" | F-002 | **Correct but missing denominator (76)** |
| "Shortcut that the model takes" | F-002 correlation only | **Unsupported causal claim** |
| "Conditions under which failures disappear" (single-file/exact oracle) | Asserted label only, no rates | **Unsupported / possibly circular** |
| Caveats listed | F-005, judge-guarantee split, replication status omitted | **Incomplete** |


&&&&&&&&&&&&&&&


gpt 6 luna max:

## Adversarial evidence review

**Bottom line:** The arithmetic in the draft checks out. The main problem is interpretive: it turns normalized failure labels into claims about what the code did, observed pass-rate differences into a mechanism, and qualitative condition notes into causal guarantees. Scope the findings to Mercury-2.5 in this particular, unreplicated setup.

### 1. “Mostly behavioural, not infrastructural”

**Supported:** F-007 reports 51 underfit and 49 `overfit_visible_tests` failures: **100/128, or 78.1%**, of the FAIL verdicts. The other four categories total 28/128 (21.9%), so calling them a numerical minority is correct.

**Not established:** The packet gives failure-mode labels, not a behavioral-versus-infrastructure classification. “Behavioural” is an interpretation, and the companion-file examples complicate treating every `overfit_visible_tests` case as behavioral overfitting.

The execution-related categories are material: `runtime_error` is **11/128 (8.6%)**, and `source_invalid` is another 9/128 (7.0%); together they account for **20/128 (15.6%)**. Runtime errors are not necessarily *infrastructure outages*—they may be code-level failures—but the packet does not define “infrastructural” or establish the proposed dichotomy. Safer wording would report the labels rather than classify them as behavioral versus infrastructural.

### 2. “The model usually produces a patch that runs”

**Unsupported by the supplied data.** F-007 describes the distribution *within FAIL verdicts*. It does not report how often submitted patches execute successfully across all attempts, or give a per-case execution-status count for the underfit and overfit labels. The 108 FAILs not labeled `runtime_error` or `source_invalid` cannot simply be counted as patches that ran.

F-005 also records 11 unscored cases, including six `epistemic_silence` cases. The packet does not say whether those are in the same overall attempt population; their treatment should be clarified before making a broad claim about what Mercury “usually” produces. The sentence “it just does not solve the task” also erases the runtime, source-validity, invalid-action, and training-failure categories.

### 3. The proposed “signatures” of underfit and overfit

The packet supports the **counts** of the two labels, but not all the detailed behavior attributed to them.

- **Underfit:** “Partial solutions,” “the code runs,” and “misses hidden checks” are not established for all—or even most—of the 51 cases by the supplied evidence. Those claims need case-level output and evaluation evidence.
- **Overfit-visible-tests:** The label suggests visible-test overfitting, but the packet does not provide a definition or case-level evidence that every such case passed visible tests and failed hidden ones. This 👹 because the packet reports that some cases with `trusted_score = 1.0` still failed due to a missing required companion file.

The judge-guarantee breakdown also cautions against blanket behavioral claims: the packet lists **189 `behavioral_reference` and 227 `compile_only` cases (416 selected)**, but gives no cross-tab linking these guarantees to the 128 FAILs or to each failure mode. A compile-only guarantee by itself does not establish hidden-test behavior.

### 4. Trusted scores, missing files, and “gaming”

The draft’s example that several cases had `trusted_score = 1.0` but failed because a companion file was missing is **supported** by the packet; `batchnorm_ema` missing `model.py` is given as an example. But “several” has no exact count here, and the meaning of `trusted_score` is not defined. It should not automatically be glossed as “passed the visible tests.”

The draft’s conclusion that the `overfit` label is not direct evidence of visible-test gaming in every case is a sound caveat. Tighten it further: a label does not demonstrate that the model *strategically chose* to exploit visible tests. The missing-file examples show that at least some labels may capture artifact completeness or task-requirement failures instead.

### 5. Proxy rates and the “shortcut” explanation

The reported arithmetic is correct:

- Base: **228/331 ≈ 0.69**
- Visible proxy: **8/27 ≈ 0.30**
- Reward proxy: **1/4 = 0.25**

These support the statement that observed pass rates were lower in the proxy-labeled samples. But the reward-proxy estimate is only one pass in four, and the group sizes differ substantially. The rates alone do not establish a general causal effect or its size. F-009 restates F-002; it is **not an independent replication**.

The paired result is relevant but incompletely presented: the packet reports **7 pass-to-fail flips among 76 shared latent specifications**. The draft omits the denominator. It also does not report the reverse transition count or a full paired outcome table, so readers cannot assess the net change across those comparisons.

Most importantly, **“the proxy channel appears to offer a shortcut that the model takes” is a mechanistic claim not shown by these results.** Lower pass rates—and even observed pass-to-fail changes—do not show that the model recognized or used a shortcut. The evidence supplied does not include behavior traces or other evidence of proxy exploitation. It supports worse observed outcomes under proxy conditions, not the proposed explanation for why.

The draft’s caveat that intervention cases were “not difficulty-matched” is **not documented in the supplied packet**. It may be true, but should be substantiated. The packet does report 76 shared latent specifications; clarify how those comparisons relate to the aggregate base and proxy samples rather than implying either full matching or no matching.

### 6. Failure conditions versus conditions where failures “disappear”

The packet lists proxy channels, visible-test-heavy grading, multi-file edits, and companion files as failure conditions. That supports describing them as **reported failure-associated patterns**. But the supplied evidence gives no condition-specific counts, denominators, or controlled comparisons for most of these. In particular, the 49 `overfit_visible_tests` labels do not by themselves prove that visible-test-heavy grading causes failures; the companion-file example is not a quantified estimate of risk across multi-file tasks.

The claim that failures “disappear” under clear single-file specifications and exact oracles is **not supported**. Although the packet’s high-level summary lists single-file specifications and exact oracles under success conditions, it supplies no rates or comparison showing that single-file specifications lead to success, and no evidence that either condition yields zero failures. “Clear” is also an added characterization not established in the packet. Present these, at most, as hypotheses or qualitative observations—not as conditions that eliminate failures.

### 7. Missing caveats and numbers to reconcile

The draft’s caveats about judge-assigned labels and a single model are useful but incomplete:

- The results are from one model/provider, **one seed per cell**, a **dirty repo**, and **no replication**. That limits both reproducibility and generalization.
- F-005 lists **11 unscored cases** (6 `epistemic_silence`, 4 `epistemic_type_games`, 1 `rd_adaptive_halting`) and **56 of 132 twin cases unverified**—about 42%. Clarify how these cases are handled in the FAIL and pass-rate denominators.
- There is a numerical coincidence worth checking: **132 − 56 = 76**, the same number as the shared latent specifications in F-002. The packet does not explicitly link those groups; verify whether they are the same cohort before treating the counts as separate evidence.
- The taxonomy includes `share_of_eligible_failures`, `case_ids`, and `judge_guarantees`. The draft should clarify the eligible-failure denominator and provide the mode-by-guarantee breakdown.
- The exact count and case IDs behind “several” trusted-score-1.0 companion-file failures should be supplied.

**Number audit:** No arithmetic error is apparent in the draft. The category counts sum to 128; 51 + 49 = 100; the proxy rates round as stated. Runtime errors are 8.6% of FAIL verdicts—not a majority, but a material share. The main numerical omissions are the **76-spec denominator** for the paired flips and the lack of traceable counts for “several” companion-file cases.

**Defensible core:** The packet supports saying that underfit and `overfit_visible_tests` are the two most common normalized failure labels, and that the proxy-labeled samples had lower observed pass rates. It does **not** establish that most failures were behavioral in a strict sense, that Mercury usually generated runnable patches, that it used a proxy as a shortcut, or that single-file specifications make failures disappear.
