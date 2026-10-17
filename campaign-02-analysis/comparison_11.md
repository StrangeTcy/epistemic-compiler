opus 5:

# ADVERSARIAL EVIDENCE REVIEW — POST-03

**Reviewer role:** Independent Evidence Reviewer
**Subject:** "Where Mercury Breaks: Non-Monotonic Difficulty Transitions" (draft stub, dated 2026-10-16)
**Verdict:** **MAJOR REVISION REQUIRED.** The three descriptive observations (MoCo, CSS, SQL) are faithfully transcribed from F-008 and survive review. Almost everything the draft builds *on top of* them does not. The central problem is that the post's headline finding is statistically indistinguishable from the null hypothesis that difficulty labels do nothing at all, and the draft never computes that null. A secondary problem is that two of the three showcase transitions turn on **source-validation failures** — a harness/format failure mode — which the draft silently reclassifies as evidence about task difficulty.

---

## A. BLOCKING ISSUES

### A-1. The null hypothesis is never computed, and it eats the finding whole

**Claim challenged:** "In several Mercury environments, the outcome across difficulty levels is non-monotonic" — presented as a discovery worth a post title.

**Problem:** With binary pass/fail outcomes and a campaign-wide pass rate of 0.684 (F-004: 277/405), a three-level sweep has a **14.8% chance of producing pass→fail→pass by coin-flip alone**, with zero difficulty structure. Any non-monotonic triple (PFP or FPF) occurs with probability **21.6%**.

The matrix has 340 environment × difficulty-tuple rows. Even a conservative estimate of 40 extractable three-level triples gives an expected **~8.6 non-monotonic triples under pure noise**, and the probability of observing *zero* is 5.9×10⁻⁵. **Finding three is not a finding. Finding three is below the noise floor.** The genuinely surprising outcome — the one that would have warranted a post — would have been monotonicity.

**Required fix:** Either (a) report the denominator — how many three-level sweeps were examined, how many were monotone, and how that compares to the binomial expectation — or (b) retitle and reframe the post as a *methodological* piece about why single-seed binary cells cannot support transition claims. Option (b) is the honest one and is actually the stronger post.

**Severity:** Blocking. The draft's own paragraph 4 concedes "single-seed cells cannot distinguish a real transition from noise," then proceeds as if it had. The concession and the thesis cannot coexist.

### A-2. Look-elsewhere / selection effect is unacknowledged

Three triples were named out of 340 matrix rows spanning 38 environments. The draft gives no account of how these three were selected. If they were found by scanning the matrix *for* non-monotonicity, the reported pattern is a selection artifact by construction and carries no inferential weight. The post must state the search procedure explicitly: was every eligible triple enumerated, or were these the interesting-looking ones?

**Required fix:** One sentence stating the enumeration rule, plus the count of monotone triples. Without it, the post is reporting the maximum of a noisy sample and calling it a signal.

### A-3. Two of three showcase cases are source-validation failures — a different failure class

**Evidence:** F-008 states CSS 4-bit "source-validation failure" and SQL length-12 "fail source validation." The matrix carries a dedicated `failure_modes` column, so this distinction is recorded and available.

**Problem:** The draft folds source-validation failures into "the middle level is harder." A source-validation failure is plausibly a *harness, format, truncation, or compilation* failure — not a capability failure on the underlying task. The competing hypothesis the draft never states, let alone rules out: **output length grows with bit count / chain length into a region where generated source trips a validator or a token budget, then the relationship resets.** That mechanism would produce exactly the observed interior dips while having nothing to do with "latent difficulty" at all.

**Required fix:** (i) Define what source validation checks. (ii) Report, for every cell in each triple, the recorded `failure_modes` value. (iii) State whether failure modes are *the same* across the dips — if CSS-4bit and SQL-12 fail for different reasons, they are two anecdotes, not one pattern. (iv) Explicitly address the truncation/length hypothesis.

**Severity:** Blocking. The post's title claims Mercury breaks. The evidence as presented is equally consistent with *the harness* breaking.

### A-4. The stated cause does not explain the stated effect

**Claim challenged:** "The reason is that 'difficulty' changes different things in different environments."

**Problem:** This is a non sequitur, and it is the load-bearing causal sentence in the post. Cross-environment axis heterogeneity explains why difficulty labels are **incommensurable across environments** — a real and well-supported point from the evidence packet. It does **not** explain non-monotonicity **within** a single environment, where the axis is by definition held constant. In MoCo, one axis (visible-test level) moves across three levels and produces pass/fail/pass. "Different environments use different axes" has no purchase on that observation whatsoever.

**Required fix:** Split the two claims. Incommensurability across environments is supported — keep it, state it as its own point. The within-environment non-monotonicity needs a different candidate explanation (noise per A-1; failure-mode heterogeneity per A-3; axis non-isolation per A-5), and each must be labelled hypothesis, not "the reason."

**Severity:** Blocking. "The reason is" asserts a mechanism the evidence cannot reach. Downgrade to "one candidate explanation, untested here."

### A-5. "The manipulation is not isolating a single latent difficulty" is an unsupported inference

**Claim challenged:** "a non-monotonic result is a signal that the manipulation is not isolating a single latent difficulty — it is changing the task."

**Problem:** False as a general statement. A perfectly isolated, perfectly monotone latent difficulty, sampled once per cell from a stochastic model, produces non-monotonic observed sequences at the rate computed in A-1. Non-monotonicity in n=1 binary outcomes is **evidence of nothing** beyond the model not being deterministic. The inference only becomes available when cell-level pass *rates* over many seeds are non-monotonic with confidence intervals that exclude each other.

**Required fix:** Delete or rewrite as a conditional: *"If these transitions replicate across seeds, that would suggest the manipulation is not isolating a single latent difficulty."*

---

## B. FACTUAL ERRORS AND UNVERIFIED ASSERTIONS

### B-1. Regex pass claim is not in the evidence packet
"In regex state machines, hidden depth means input-string length (32, 128, 512 characters) and **the model passes all three at the easy surface label**."

The packet supports only *"regex changes input-string length (32/128/512)."* The pass-all-three result is **not in the packet**. Also unsupported: the mapping of input-string length to "hidden depth" and the existence/identity of an "easy surface label" for regex. Three separate unverified assertions in one sentence. **Verify against the matrix or cut.**

### B-2. "easy-surface" qualifier on SQL is not in F-008
F-008 reads: *"SQL fixed points pass at graph-chain lengths 6 and 25 but fail source validation at length 12."* No surface-label qualifier. The draft adds "easy-surface cases." Either source it from the matrix or drop it. (The CSS "easy-surface" qualifier *is* in F-008 and is fine.)

### B-3. CSS axis mis-described
Packet: CSS surface labels change *class names and bit counts*. Draft (para 3): "In CSS and SQL, surface labels change class names and graph sizes." The draft drops **bit counts** from CSS and imports **graph sizes** — which belongs to SQL, and which is itself a mis-statement of SQL's axis (F-008 says **graph-chain length**, not graph size; a chain length is one dimension of a graph, not its size). Two errors in one clause.

### B-4. "Hardest label passes while an easier one fails" conflates two axes
In the CSS cases, the *surface label* is "easy" throughout; what varies is bit count. 5 bits is therefore not "the hardest label" — it is the largest value on a secondary axis at a fixed easy label. The draft's framing sentence describes a pattern (hardest-label pass, easier-label fail) that **no cited case actually instantiates**. All three cited cases are the *same* pattern: an interior dip. Collapse the framing sentence to one pattern or produce a case for the second.

### B-5. "Partial score" is unreconciled with the campaign's binary accounting
F-004 reports 277 PASS and 128 FAIL summing exactly to 405 scored — a two-category scheme. F-008 reports a CSS cell with a **partial score**. Where does a partial score sit in that accounting? If it is counted as FAIL, then the CSS sequence is fail/fail/pass — **monotone**, and the CSS case collapses entirely. This needs resolving before publication; it is potentially a one-third reduction in the post's evidence base.

### B-6. "Middle level is harder than both ends" is inaccurate for CSS
At 3 bits (the easiest end) CSS yields a *partial*, not a pass. The claimed shape — pass, dip, pass — does not hold at the low end. Describe the actual sequence.

### B-7. Evidence-packet internal inconsistency the draft must not launder
F-006 states "7 environments score 0.00" and then lists: glyph, functorial_augmentation, monadic_reward, sheaf_invariant, ts_one_step, ts_trajectory (= 6), plus "epistemic_silence/type_games unscored" (= 2 more, and *unscored* is a different condition from *scoring 0.00*). The count does not reconcile. The draft currently sidesteps this by omitting F-006 entirely — but if F-006 is cited in revision (see C-1), the discrepancy must be resolved, not inherited.

### B-8. Arithmetic that does check out
277 + 128 = 405 ✓; 277/405 = 0.6840 ✓; 416 − 405 = **11 unscored selected cases** — a figure the draft never mentions (see C-2).

---

## C. MISSING CAVEATS AND CONTEXT

### C-1. The bimodality context (F-006) is omitted, and it shrinks the eligible denominator
Pass rates range 0.00 to 1.00 with a cluster of environments pinned at 0.00. Environments at a floor or ceiling **cannot exhibit a transition by construction**. The honest denominator for "several environments show non-monotonicity" is not 38 — it is the subset with intermediate, multi-level, fully-scored sweeps. That number is likely small, and three-out-of-small reads very differently from three-out-of-38. Report it.

### C-2. The 11 unscored cases are a missing-not-at-random hazard
If a cell fails to score, the sweep that contains it is *truncated*, and truncation is almost certainly correlated with difficulty (harder cells are likelier to crash or time out). This systematically removes the cells most likely to be genuine failures, **biasing observed sequences toward apparent non-monotonicity**. The draft mentions "grey = unscored" in a figure caption and never discusses the inferential consequence.

### C-3. The dirty-repo caveat is listed but its implication is suppressed
"Dirty source repository" appears in the trailing caveat line as a generic disclaimer. Its actual force is specific and severe: **the code state at run time is not recoverable, and there is no guarantee that all cells in a given triple were produced under the same working-tree state.** A transition observed across cells run under different uncommitted code is not a difficulty transition at all. This belongs in the body, adjacent to the transition claims, not in a footer.

### C-4. Judge guarantees are a within-triple confound, never checked
The matrix carries a `judge_guarantees` column, and the draft's footer concedes "mixed judge guarantees." But the draft never asks the obvious question: **do the judge guarantees vary across the three levels within each cited triple?** If the middle level of MoCo was graded under a different guarantee than its neighbours, the "transition" is a grading-regime artifact. This is a two-minute lookup that could invalidate a third of the post. It must be done before publication.

### C-5. Sampling of the SQL axis is sparse and unevenly spaced
Chain lengths 6, 12, 25 — gaps of 6 and 13. The draft calls these "adjacent levels." They are adjacent *sampled points*, not adjacent values. Nothing is known about 9, 15, or 18. A dip inferred from three sparse, unevenly spaced samples on a continuous axis is a very thin basis for the word "transition." (CSS 3/4/5 bits is genuinely adjacent; MoCo's spacing is unstated.)

### C-6. "These are not smooth degradations" is vacuous
Smoothness is unobservable in binary outcomes at n=1. The contrast with "smooth degradation" can only be drawn using cell-level `pass_rate` with multiple cases per cell. Either use the pass_rate column (the matrix has it — are these cells n_cases=1 or larger?) or delete the claim.

### C-7. Model, harness, and run provenance absent from the body
"Mercury-2.5" appears in the task header; the post body never names the model version, the harness version, the date range of the run, or sampling parameters (temperature in particular — a temperature-0 run and a temperature-1 run have radically different implications for A-1). Epistemic-status says "Observed on one model" without saying which.

### C-8. "Challenges the assumption that harder labels mean harder outcomes" — attribute the assumption
No one is on record expecting strict monotonicity in single-sample binary outcomes. As written this is a strawman. Either cite someone who made the assumption, or restate as the narrower and defensible version: *difficulty labels in this suite are not validated as an ordinal scale.*

### C-9. Provenance of the "original idea"
Epistemic-status claims "Non-monotonic difficulty transitions as the central object of study" as an original idea. F-008 is a *verified finding in the supplied dossier*. The original contribution is the framing and the analysis, not the observation. Adjust the attribution.

---

## D. FIGURE AND CAPTION DEFECTS

| Issue | Detail |
|---|---|
| **Numbering inverted** | `fig4_difficulty_transitions.svg` is captioned "Figure 3"; `fig3_difficulty_heatmap.svg` is captioned "Figure 4." Filenames and labels are swapped. |
| **Numbering starts at 3** | The first figure in the post is "Figure 3." If Figures 1–2 are not in this post, the sequence is broken. |
| **"holding other dimensions fixed"** | Unsupported by the packet. The matrix key is a *difficulty_tuple*; verify that non-swept tuple entries are in fact constant across each line, and say so with reference to the data. |
| **"easy/medium/hard visible-test levels"** | The packet says only "visible-test levels." The level names and the pass/fail/pass → easy/medium/hard mapping are both unverified. If levels are not named easy/medium/hard, the caption is fabricating an ordinal scale. |
| **"each line is one control combination"** | Implies multiple sweeps; F-008 describes one sequence. If there are multiple lines, **how many are monotone?** A figure showing one dipping line among several flat ones would substantially undercut the text. |
| **"six representative environments"** | Representative by what rule? With 38 environments and a documented floor cluster, "representative" requires a stated selection criterion or it reads as cherry-picking. |
| **"pass counts over scored counts"** | Shows n_pass/n_scored but hides n_cases. The 11-case scored/selected gap (C-2) is invisible in this encoding. Show n_scored/n_cases too. |
| **Caption ≠ claim** | Neither caption states the seed count. Every figure in this post should carry "n=1 seed per cell" on its face. |

---

## E. NUMBERS REQUIRING VERIFICATION BEFORE PUBLICATION

1. Regex: does the model in fact pass at 32/128/512? (Not in packet — B-1.)
2. `n_cases` for every cell in the MoCo, CSS, and SQL triples — are these 1-case cells or multi-case cells with a pass_rate?
3. `pass_rate` values for those same cells (replaces binary pass/fail throughout).
4. `failure_modes` strings for CSS-4bit, SQL-12, and the MoCo middle level — same mode or different?
5. `judge_guarantees` for all nine cited cells — constant within each triple? (C-4.)
6. The MoCo level names and their true ordinal order.
7. Total count of eligible three-level sweeps in the 340-row matrix, and the count that are monotone. (A-1, A-2.)
8. Disposition of "partial score" in the 277/128 accounting. (B-5.)
9. Reconciliation of the F-006 count of 7 against the 8 listed names. (B-7.)
10. Whether the 11 unscored cases fall inside any cited sweep. (C-2.)
11. Sampling temperature for the campaign.

---

## F. WHAT THE EVIDENCE ACTUALLY SUPPORTS

Three claims survive adversarial review intact:

1. **Difficulty axes are incommensurable across environments.** MoCo varies test coverage, CSS varies class names and bit counts, SQL varies graph-chain length, regex varies input-string length. These are not a common scale, and aggregating "hard" cells across environments is therefore meaningless. This is fully supported, genuinely useful, and currently buried as a subordinate clause in a paragraph that misuses it as a causal explanation.

2. **Three specific triples have the recorded outcome sequences in F-008.** Descriptively true. They support no inference beyond their own existence.

3. **The campaign design cannot distinguish a transition from noise.** Single seed, dirty repo, mixed judges, no replication, binary outcomes. This is the real finding and it deserves the headline.

**Suggested minimal defensible restatement of the thesis paragraph:**

> *In this archived single-seed run, three environments produced non-monotonic outcome sequences across their difficulty axes. We report them because they are what a reader scanning the matrix will notice first — and because, on inspection, they cannot be distinguished from sampling noise. At the campaign pass rate of 0.68, roughly one in five three-level sweeps will look non-monotonic by chance alone, and two of the three dips are source-validation failures rather than task failures. The durable observation here is not about Mercury's difficulty curve; it is that this suite's difficulty labels are not a validated ordinal scale, that the axes mean different things in different environments, and that one seed per cell buys no power to detect a threshold even if one exists.*

---

## G. ACCEPTANCE CRITERIA FOR RESUBMISSION

- [ ] Null-hypothesis calculation reported in-body (A-1).
- [ ] Triple-enumeration procedure and monotone/non-monotone counts stated (A-2).
- [ ] `failure_modes` reported per cell; truncation/validator hypothesis addressed (A-3).
- [ ] "The reason is" downgraded; cross-environment and within-environment claims separated (A-4).
- [ ] Latent-difficulty inference made conditional on replication (A-5).
- [ ] Regex and SQL-surface claims sourced to the matrix or cut (B-1, B-2).
- [ ] CSS/SQL axis descriptions corrected (B-3); two-pattern framing collapsed to one (B-4).
- [ ] "Partial score" reconciled with the 277/128 split (B-5).
- [ ] F-006 bimodality and the eligible denominator added (C-1).
- [ ] 11 unscored cases and the truncation bias discussed (C-2).
- [ ] Dirty-repo and judge-guarantee confounds moved into the body with within-triple checks (C-3, C-4).
- [ ] Figure numbering repaired; captions sourced; "n=1 seed per cell" on every figure (D).
- [ ] Model version, harness version, and sampling temperature stated (C-7).

**Note on house conventions:** bracketed substitution tokens and the 👹 substitution in paragraph 4 are author-intentional and are explicitly **not** flagged. The only adjacent observation worth making is that the referent of "This" in that sentence is ambiguous — it could point to the non-monotonicity, the incommensurability, or both — and a reader will have to guess. That is a clarity note about the pronoun, not about the substitution.


&&&&&&&&&&&&&&&&&&

gpt 6.1 sol max:

# Adversarial evidence review — POST-03

**Verdict: major revision.** The draft has a defensible descriptive core: **F-008 records non-monotonic outcome sequences in several environments.** Its main weakness is the jump from those observations to explanations about latent difficulty, task changes, and thresholds. Those explanations are not established by the packet.

There are also narrower problems: the SQL surface/size attribution is unsupported, the regex success claim exceeds the supplied evidence, and the figure captions assert controls and representativeness that cannot be verified here.

**Review scope:** I treat the supplied packet as authoritative. The underlying matrix rows, run logs, repository snapshot, and SVG contents were not supplied. “Unsupported” below means unsupported by this packet, not necessarily false.

## 1. Claim-by-claim audit

| Draft claim | Evidence assessment and required correction |
|---|---|
| **“Difficulty labels are not a staircase.”** | **Defensible only as a scoped description of recorded outcomes.** F-008 supports examples that do not follow a monotone outcome ordering. It does not establish that underlying difficulty or expected success probability is non-monotonic. Prefer: “Recorded outcomes do not always follow the ordering suggested by difficulty labels.” |
| **“The middle level is harder than both ends.”** | **Overclaim.** A failure between two passes establishes an observed outcome reversal, not that the middle setting is intrinsically harder or has a lower success probability. Replace “is harder” with “fails in this run while both sampled endpoints pass.” |
| **“The hardest label passes while an easier one fails.”** | **Supported as a statement about labels and recorded judgments**, assuming the axis ordering is correctly identified. Do not silently turn “hardest label” into “most demanding task.” That distinction is the central issue under review. |
| **MoCo visible-test levels yield pass/fail/pass.** | **Supported by F-008.** However, the packet does not identify the MoCo failure mode or provide the complete control tuples. The sequence alone does not establish why the middle case failed or that all other relevant conditions were held fixed. |
| **CSS easy-surface cases at 3/4/5 bits yield partial score/source-validation failure/pass.** | **Supported by F-008.** Preserve those exact outcome categories. They mix a score description with a validation status; they are not automatically three values on a common numerical response curve. Verify the partial score and its mapping to campaign PASS/FAIL before plotting or aggregating it as binary. |
| **SQL passes at lengths 6 and 25 and fails source validation at 12.** | **Supported by F-008.** The added **“easy-surface”** qualifier is not supplied for SQL in the packet; it is explicitly supplied only for CSS. Verify the SQL tuples before retaining that qualifier. A source-validation failure also does not, by itself, diagnose failure of fixed-point reasoning. |
| **“These are not smooth degradations.”** | **Unsupported if this describes underlying performance.** Three categorical observations cannot establish the shape or smoothness of a response function. They are not a monotone sequence of observed outcomes; that is the narrower warranted statement. |
| **“Qualitatively different failure layers at adjacent levels.”** | **Not established.** MoCo’s failure layer is unspecified. CSS includes a partial score, but its diagnostic layer is not given. SQL has one reported source-validation failure, not multiple demonstrated failure layers. Also, SQL lengths 6, 12, and 25 are sampled settings—not adjacent integer lengths. |
| **“The reason is that ‘difficulty’ changes different things in different environments.”** | **Causal overreach.** The packet supports heterogeneous axis meanings. It does not show that heterogeneity causes the within-environment reversals. Those are separate findings. Replace “The reason” with a non-causal transition such as “Interpreting these patterns also requires inspecting what each axis changes.” |
| **Regex “hidden depth” means input length 32/128/512.** | **Partly supported.** The packet confirms the input-length values and manipulation. It does not explicitly confirm the internal axis name “hidden depth.” Verify the schema terminology rather than presenting it as established here. |
| **Regex passes all three lengths at the easy surface label.** | **Unsupported by the supplied packet.** The length mapping is supplied; these outcomes and the easy-surface qualification are not. Add exact matrix/run evidence or remove the claim. |
| **“In CSS and SQL, surface labels change class names and graph sizes.”** | **Axis conflation requiring correction.** The packet describes CSS class-name/bit-count variation and SQL graph-chain-length variation. It does not establish that SQL *surface labels* change graph size. The sentence also obscures the earlier claim that SQL length changes while surface remains easy. Report the mappings separately and verify the exact surface/depth fields. |
| **“The labels are not commensurable across environments, and sometimes not within one.”** | **Overstated.** Different operationalizations mean that no common calibrated scale has been established. They do not, by themselves, prove that comparison is impossible. The within-environment claim is especially weak: bit count and chain length remain ordered quantities even if one model’s observed outcomes reverse. |
| **A reversal signals that the manipulation is not isolating one latent difficulty and “is changing the task.”** | **The strongest unsupported inference in the draft.** A reversal can motivate an audit of the manipulation; it does not demonstrate confounding or a task change. Scaling input length or graph length can remain within one task family. Conversely, even a clean single-axis manipulation can produce a pass/fail/pass sample. |
| **Single-seed cells cannot distinguish a “real transition” from noise.** | **The limitation is supported; the framing needs refinement.** The recorded outcomes are real observations. What is unestablished is their repeatability, prevalence, and mechanism. “Noise” is also underspecified: instance generation, model sampling, judging, and implementation differences have not been separated. |
| **“Whether those are real thresholds or seed-specific accidents requires replication.”** | **Replication is necessary for repeatability claims, but “thresholds” is premature.** Three sampled settings do not locate a threshold. “Threshold versus accident” is also a false dichotomy: systematic evaluator effects, item-specific behavior, and other mechanisms remain possible. Replication alone will not identify causation without controlled comparisons and judge inspection. |

### Epistemic-status block

- **Single model; single seed per cell; no replication:** consistent with the packet and appropriately disclosed. Keep the scope explicitly tied to Mercury-2.5 and this archive.
- **“Original ideas”:** the packet cannot establish originality. This is an authorial/provenance claim, not an empirical result.
- **“Role-separated analysis” and “final writer from evidence dossier”:** likewise require workflow provenance outside the supplied experimental evidence.
- **“Challenges the assumption that harder labels mean harder outcomes”:** reasonable as motivation, but only if “outcomes” means these recorded judgments—not a demonstrated reversal in expected performance.

## 2. The central inferential distinction is missing

The draft needs to separate three propositions:

1. **Some recorded outcome sequences reverse across ordered settings.**  
   Supported by F-008.

2. **Mercury-2.5’s expected success probability is non-monotonic across those settings.**  
   Not established by one seed per selected cell.

3. **The reversals occur because the difficulty manipulation changes multiple properties or changes the task.**  
   Not established by the supplied evidence.

The first proposition does not entail either of the others. For example, a monotonically declining success probability is compatible with observing pass/fail/pass in three individual trials. That is a general statistical possibility, not a diagnosis of this campaign.

Likewise, the fact that MoCo changes test coverage while SQL changes chain length explains why cross-environment labels require care. It does **not** explain why either environment produced its particular reversal.

**Required correction:** present axis heterogeneity as an interpretive limitation or audit target, not as the demonstrated cause of the observations.

## 3. Caveats named in the draft but not carried through its conclusions

### A. Recorded failure is not a diagnosis of the underlying capability

CSS and SQL include **source-validation failures**. Those are valid reported evaluation outcomes, but the packet does not establish what the failed source would have done under a semantic evaluation.

The draft should distinguish:

- recorded judgment;
- failure category;
- evaluator guarantee;
- inferred model capability.

It should not treat all four as interchangeable. Similarly, a PASS should not be presented as proof of equally strong correctness across mixed judge guarantees.

Use the matrix’s **`failure_modes`** and **`judge_guarantees`** fields in the interpretation, rather than relegating “mixed guarantees” to the final caveat line.

### B. Matching difficulty labels is not necessarily matching experimental conditions

“One seed-0 run per selected cell” does not, by itself, demonstrate:

- identical underlying instances across settings;
- that only one generator property changed;
- identical model-generation conditions;
- unchanged judging conditions.

A shared seed label is not sufficient evidence of a controlled paired comparison. The full tuples and generation procedure are needed.

### C. Dirty repository is a reproducibility limitation—not a proven explanation

The draft correctly mentions the dirty repository. It should identify the exact archived source state or available diff if the analysis depends on implementation details.

Do not infer that dirty source caused the reversals. Equally, do not make confident implementation-level causal claims without pinning the source state.

### D. Example selection and prevalence remain unknown

“Several” is justified by the supplied examples. **“Common,” “typical,” or “representative” would require more.**

The packet does not provide:

- the number of eligible complete sweeps;
- the number exhibiting reversals;
- the criteria used to select the examples;
- whether the reported sweeps cover all relevant control combinations.

Without those denominators, the draft can establish existence, not prevalence.

## 4. Numbers and denominators requiring careful handling

The campaign totals are internally consistent:

- **416 selected**
- **405 scored**
- **277 PASS + 128 FAIL = 405**
- **277 / 405 ≈ 0.684**
- **11 selected cases were unscored**
- **38 environments**

These are **F-004** figures. The 0.684 is the scored-case pass fraction, not an average environment pass rate or a transition frequency.

The matrix contains **340 environment × difficulty-tuple rows**. That is a different unit from selected cases, scored cases, and complete sweeps. Before using the matrix quantitatively, explain how its rows aggregate the campaign cases. Do not present 340 rows as 340 independent replications.

Specific checks needed:

- Confirm the full tuples underlying every quoted sequence.
- Verify the CSS partial score and its binary-status mapping.
- Verify the SQL easy-surface qualifier.
- Verify the regex three-pass claim.
- Check row-level count identities against the documented scoring schema.
- Treat `n_scored = 0` as unscored/undefined performance—not a zero pass rate.
- If reporting reversal frequency, use eligible matched sweeps as the denominator, not all matrix rows.

### F-006 needs careful reuse

F-006 supplies between-environment context: reported scores include zeroes, and pass rates span 0.00–1.00. That does not independently support within-environment reversals.

Its compact enumeration also needs reconciliation before reproducing a named list: it reports seven zero-score environments but names six clear zero-score examples alongside an explicitly unscored `epistemic_silence/type_games` entry. **Do not count an unscored entry as a scored zero to complete the roster.** Resolve the enumeration against `n_scored`.

This is not an error currently made in the draft, but it is a trap when adding campaign context.

## 5. Figure claims are currently unaudited

### Transition figure

The caption asserts:

> “MoCo visible-test sweeps holding other dimensions fixed; each line is one control combination.”

F-008 supports the reported MoCo outcome pattern. It does **not** supply enough information to verify that caption.

Before publication, check:

- which dimensions constitute each control combination;
- whether every line contains a complete matched sweep;
- whether easy/medium/hard are the actual recorded visible-test labels;
- whether missing or unscored points are shown as gaps rather than failures;
- whether the figure includes all eligible combinations or selected examples.

A MoCo-only figure also does not visually substantiate the CSS and SQL examples. Those need their own row references, table, or panel.

### Heatmap

> “Six representative environments.”

Both parts need checking:

- **Six:** the SVG contents were not supplied.
- **Representative:** no selection rule or representativeness evidence is provided.

🫪 a sampling rationale exists, use **“six selected illustrative environments.”**

The caption should also distinguish:

- scored zero-pass cells;
- selected-but-unscored cells;
- absent or unselected combinations.

“Grey = unscored” is insufficient if the same colour also represents structurally missing combinations.

### Numbering

The transition asset is named `fig4_difficulty_transitions.svg` but captioned Figure 3; the heatmap asset is named `fig3_difficulty_heatmap.svg` but captioned Figure 4. Filenames need not dictate figure numbering, so this is **a cross-reference check, not a proven factual error**.

## 6. Strongest defensible replacement claim

> In the selected Mercury-2.5 archive, F-008 records outcome reversals across ordered settings: MoCo visible-test levels yield pass/fail/pass; CSS easy-surface cases at 3/4/5 bits yield partial score/source-validation failure/pass; and SQL chain lengths 6/12/25 yield pass/source-validation failure/pass. These are observations about recorded judgments, not estimates of intrinsic difficulty or expected success probability. The axes manipulate different task or testing properties, but this evidence does not establish that those differences caused the reversals. With one seed-0 run per selected cell, no replication, mixed judge guarantees, and a dirty repository, their repeatability, prevalence, and mechanism remain unresolved.

**Bottom line:** retain the observed sequences. Correct the axis attribution, substantiate or remove the regex and figure claims, and remove the inference that reversals demonstrate a failed latent-difficulty manipulation or a threshold. The evidence supports an exploratory audit of recorded outcomes—not yet an explanation of where or why Mercury breaks.
