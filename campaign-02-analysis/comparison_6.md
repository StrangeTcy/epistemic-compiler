sonnet 5:

# ADVERSARIAL REVIEW BRIEF — POST-01
**"The Model's Belief Is Right; Its Decision Is Fragile"**
**Reviewer role:** Evidence Reviewer, Battle Arena
**Verdict:** Core finding is defensible in narrow form; the draft overreaches in stitching two incommensurable experiments into one "decision" narrative, contains one fabricated statistic, one arithmetic misattribution, one garbled quantitative claim, and several under-weighted caveats. Requires revision before publication.

---

## 1. Strongest defensible thesis vs. what is NOT defensible

**Defensible:** Within the T1 `same_fact_presentation` probe (36 matched pairs), Mercury‑2.5's elicited posterior was invariant to presentation order (0/36 flips) while its terminal answer (5/36) and diagnostic choice (17/36) were not, and every terminal-answer flip was a correctness flip. This is a clean, narrow, well-supported dissociation claim, and it is the draft's load-bearing result.

**Also defensible, separately:** Across the epistemic-game suite (23/23 cases), posterior accuracy was exact. Separately again, pass rates in the campaign's proxy-intervention conditions (visible_proxy 8/27, reward_proxy 1/4) were markedly lower than base (228/331), with 7/76 paired cases flipping pass→fail.

**NOT defensible as currently written:** That these are evidence of *one* fragile "decision layer" being hit by "a different manipulation." The draft's transition sentence — treating proxy-channel pass/fail as the same "decision side" that T1 tested — is an unsupported bridging inference. T1 measures belief-elicitation/terminal-answer/diagnostic-choice behavior on an oracle-exact probabilistic task. The proxy-intervention data comes from the 38-environment campaign with **judge guarantees of `behavioral_reference`/`compile_only`**, which is the vocabulary of agentic/coding-task scoring, not belief-elicitation scoring. Nothing in the evidence packet establishes that T1's "terminal decision" and the campaign's pass/fail outcome are the same construct, measured in the same model pathway, under the same task family. The draft's framing ("The decision side breaks under a different manipulation") asserts continuity that the evidence does not establish. This is the single most important structural problem in the piece — it converts two parallel, non-comparable lines of evidence into a false compound narrative.

---

## 2. Specific claims challenged against evidence

**(a) "The decision side breaks under a different manipulation" (proxy section intro).**
Unsupported. The packet gives no basis for equating T1's terminal-answer/diagnostic-choice endpoints with the campaign's task pass/fail endpoint. Required: either drop the "same decision, different manipulation" framing and present proxy results as an independent, parallel line of evidence for a broader "stated correctness ≠ behavioral reliability" pattern — or explicitly justify why they're the same construct (which the packet doesn't support).

**(b) "The 405 scored cases span environments with pass rates from 0.00 to 1.00..."**
This specific range (0.00 to 1.00) **does not appear anywhere in the evidence packet.** The packet gives only aggregate figures (277/405, 0.684) and the 38-environment count — no per-environment range. This is a fabricated/unsupported statistic and must be cut or sourced.

**(c) "...and the judge guarantees differ (189 behavioral-reference, 227 compile-only)."**
Arithmetic/attribution error: 189 + 227 = 416, which is the **selected-case** total, not the **405 scored-case** total the sentence attaches it to. As written, the sentence implies the judge-guarantee split partitions the 405 scored cases; it actually appears to partition the 416 selected cases (including the 11 unscored). This needs correction or an explicit note that the guarantee split is over the selected pool, not the scored pool.

**(d) "...it is presentation-sensitive in roughly one in seven pairs, and wrong in one in seven of those."**
This is garbled and arguably incorrect. 5/36 ≈ "one in seven" is a fair rounding for the flip rate. But "wrong in one in seven of those" double-applies the fraction to a population that's already fully accounted for: by the draft's own earlier sentence, **all 5 of 5** flips are correctness flips (100%, not 1/7). As written, a careful reader could infer a much smaller and wrong number (~1/49) is implied. This sentence needs to be rewritten for numerical accuracy — e.g., something like "in those 5 pairs, the model was wrong in whichever order it happened to encounter" — not re-apply the same ratio.

**(e) "56 unverified twin groups" (limitations section).**
The packet states **"56 of 132 twin cases unverified"** — i.e., a denominator of 132 and a unit of "cases," not "groups." Dropping the denominator (132) also strips the reader of the actual severity: 56/132 ≈ 42% unverified is a substantial fraction, materially larger-sounding than a bare "56." This should be restated with the denominator and corrected terminology ("twin cases," not "groups").

**(f) The 🤥 glyph mid-sentence** ("The 🤥 claim is behavioral...").
This reads as a leftover editorial marker, not a deliberate stylistic device — it doesn't parse as meaningful in context and should be removed or clarified before publication. If it was meant as a tongue-in-cheek self-flag, it needs to be legible as such; currently it just looks like a stray artifact.

---

## 3. Missing caveats, confounds, unsupported inferences

1. **Single seed per cell in the main campaign is never disclosed to the reader.** The evidence packet explicitly flags "Single seed per selected cell" as a limitation, but the draft's limitations section never mentions it — even though the proxy pass rates it leans on (especially **reward_proxy at 1/4**, n=4) are exactly the kind of statistic a single-seed design makes unstable. A 25% pass rate on 4 cases is not a number that should sit next to 0.30 and 0.69 as if comparably reliable; the draft treats them with equal rhetorical weight.

2. **Undisclosed intervention taxonomy gap.** The paired-flip analysis is "within 76 intervention cases," but visible_proxy (27) + reward_proxy (4) = 31, far short of 76. There are evidently other intervention categories contributing to that denominator whose individual pass rates are never reported. The draft presents visible/reward proxy as if they're the whole story behind the 7/76 flips; readers should be told that most of the 76 intervention cases belong to an unspecified, unreported category.

3. **No acknowledgment that T1 and epistemic-games may not be fully independent samples.** The draft treats the 23/23 epistemic-game result as separate corroboration of belief invariance ("The same exactness shows up in the epistemic-game suite") without clarifying whether T1's presentation manipulation is itself one of the "presentation interventions" counted within those 23 cases. If so, citing both as independent confirmations double-counts the same evidence.

4. **"Exact source identity is unresolved" is an inference, not a quoted fact.** The packet says only "source repo dirty at run time." The draft's gloss is a reasonable interpretation but should be flagged as such rather than stated flatly, since "dirty" repo state has a narrower meaning (uncommitted changes) than "exact source identity unresolved" (which implies broader provenance uncertainty).

5. **No confound discussion for the terminal-answer-flip mechanism.** The draft argues against a "parsing story" because belief didn't flip — reasonable — but doesn't consider or rule out that the terminal-answer extraction step itself (already flagged as "brittle" elsewhere) could introduce its own order-sensitive noise unrelated to any internal decision process. The hedge exists in the limitations section but is disconnected from the strong claim made two sections earlier ("pushes the locus of fragility downstream of belief computation").

6. **No mention that difficulty-mismatch could fully explain the proxy-channel pass-rate gap**, beyond a one-line disclaimer. Given reward_proxy's n=4, a difficulty confound could flip the entire 0.25 figure with one case. The "the direction is consistent and within-pair flips are hard to explain by difficulty alone" claim is asserted rather than demonstrated — the packet gives us flip counts, not difficulty-controlled comparisons.

---

## 4. Arithmetic / factual check summary

| Claim in draft | Packet value | Status |
|---|---|---|
| 36 matched pairs, 6×6 | 6 cells × 6 seeds = 36 | ✅ correct |
| 0/36 belief flips | 0/36 | ✅ correct |
| 5/36 terminal flips, all correctness flips | 5/36, all correctness | ✅ correct |
| 17/36 diagnostic divergences | 17/36 | ✅ correct |
| 23/23 epistemic-game exact match | 23/23 | ✅ correct |
| visible_proxy 8/27 (0.30) | 8/27 = 0.296 | ✅ correct (rounds to 0.30) |
| reward_proxy 1/4 (0.25) | 1/4 = 0.25 | ✅ correct |
| base 228/331 (0.69) | 228/331 = 0.689 | ✅ correct |
| 7/76 paired flips, 4 visible_proxy | matches packet phrasing | ✅ correct |
| 277/405 PASS, 0.684 | 277/405 = 0.684 | ✅ correct |
| "pass rates from 0.00 to 1.00" | not in packet | ❌ **fabricated** |
| judge guarantees (189/227) attached to "405 scored cases" | 189+227=416 (selected total, not scored) | ❌ **misattribution** |
| "wrong in one in seven of those" | all 5/5 flips are correctness flips | ❌ **garbled/incorrect framing** |
| "56 unverified twin groups" | "56 of 132 twin cases" | ❌ **terminology + missing denominator** |

---

## 5. House-style fit

- Frontmatter, byline, five-field epistemic-status `<dl>`: compliant.
- First-person, self-correcting voice, concrete counts beside claims: largely compliant and a genuine strength — the draft does caveat near its claims rather than burying caveats at the end.
- Two issues undercut the "technically literate" register: the stray `🤥` glyph (reads as an artifact, not a device) and the terminal profanity ("fuckingly settle it"), which — absent confirmation this is an established voice tic elsewhere in the series — risks reading as tonal inconsistency against an otherwise careful, hedge-heavy piece. Flag for editorial confirmation rather than hard rejection.
- No file paths, finding IDs, or trace IDs leaked into public copy: compliant.

---

## 6. Response-to-review table

| Objection | Required change |
|---|---|
| T1 (belief/decision) and proxy-intervention (campaign pass/fail) are treated as the same "decision" construct hit by "a different manipulation" | Rewrite transition to present proxy results as an independent, parallel line of evidence; do not imply shared locus/mechanism unless packet supports it |
| "pass rates from 0.00 to 1.00" is unsupported | Delete or replace with a sourced figure |
| Judge-guarantee counts (189/227, sum 416) misattached to "405 scored cases" | Correct to reflect that 189+227=416 is the selected-case total, not the scored-case total; clarify which pool the guarantee split describes |
| "wrong in one in seven of those" double-applies the flip ratio and is numerically misleading | Rewrite to state plainly that all 5 flips were correctness flips (100%), without re-applying a fraction |
| "56 unverified twin groups" drops denominator and changes unit | Restate as "56 of 132 twin cases unverified (~42%)" |
| Single-seed-per-cell limitation never disclosed | Add to limitations section; flag reward_proxy's n=4 as especially fragile |
| 76-case paired-flip denominator exceeds disclosed visible_proxy+reward_proxy (31) with no account of the remainder | Note that most of the 76 intervention cases belong to an unspecified/unreported category |
| Possible non-independence of T1 and epistemic-game samples | Clarify whether T1 pairs are a subset of the 23 epistemic-game cases before citing both as independent corroboration |
| "exact source identity is unresolved" stated as fact | Reframe as an inference from "repo dirty at run time," not a direct packet claim |
| Stray `🤥` glyph mid-sentence | Remove or replace with legible phrasing |
| Difficulty-confound dismissal ("hard to explain by difficulty alone") is asserted, not shown | Soften to explicit uncertainty given non-difficulty-matched design and small n |

&&&&&&&&&&&&&&&&

grok 4.5:

# Adversarial Evidence Review Brief: POST-01
**Article slot:** Belief/decision dissociation (primary mechanistic article)  
**Research question under test:** Does Mercury-2.5's stated belief track content while its terminal decisions are fragile to presentation order and proxy channels?  
**Reviewer stance:** Independent, adversarial, evidence-bound. Only the supplied packet is authoritative. No external knowledge, no charity on rhetoric, no invention of missing numbers.

## 1. Strongest Defensible Thesis (and What Is Not Defensible)

**Strongest defensible thesis (packet-strict):**  
In the T1 `same_fact_presentation` probe (exactly 6 cells × 6 seeds = 36 matched pairs), Mercury-2.5 produced identical elicited/stated posteriors in both presentation orders in 0/36 trials (zero belief flips). Terminal answers flipped in 5/36 pairs, and all 5 were correctness flips (right in one order, wrong in the other). Diagnostic-choice divergences occurred in 17/36. Separately, the epistemic-games suite showed 23/23 exact posterior matches with zero posterior error (`posterior_reported` = `posterior_true`). Proxy-tagged intervention cases showed lower raw pass rates (visible_proxy 8/27 ≈ 0.30; reward_proxy 1/4 = 0.25) than base (228/331 ≈ 0.69), with 7 pass→fail flips inside 76 paired intervention cases that share a latent spec with a base case (4 of those 7 under visible_proxy).  

This supports a narrow **behavioral dissociation on endpoints** for this model/provider/config on these exact items: stated belief was order-invariant (and, in the epistemic suite, content-tracking), while terminal decisions and diagnostic choices were not. The campaign totals (416 selected / 405 scored / 277 PASS / 128 FAIL ≈ 0.684) and judge split (189 behavioral_reference, 227 compile_only) supply context only.

**What is NOT defensible from the packet:**  
- Any architectural or mechanistic claim (“belief layer,” “decision layer,” “downstream of belief computation,” “maps a correct posterior into an answer”). The packet measures endpoints only.  
- That the invariant posterior in T1 was the *correct* posterior in every trial (packet states “Oracle is exact; correctness is not in dispute” for the setup and reports zero belief flips + correctness flips on answers, but does not tabulate per-trial posterior error for T1 itself; that exactness is only explicit for the 23 epistemic-games cases).  
- Causal claims about proxies, presentation, or “fragility.” Packet explicitly notes interventions are not difficulty-matched.  
- Generalization beyond one model (mercury-2.5, reasoning_effort=high), one provider, these 36 pairs + 23 games + the listed proxy counts, or the dirty-repo single-seed campaign.  
- That this is “the most informative result” of the whole campaign, that scoring stated belief “overstates reliability” in general, that any evaluation fixing one presentation “is measuring a presentation, not just a capability,” or that the dissociation “would fuckingly settle” anything. Those are authorial valuations.  
- Claims about variance, confidence intervals, replication, or twin-case verification beyond the stated 56 of 132 unverified.  
- Environment-level pass-rate range “from 0.00 to 1.00” (absent from packet).

The title “The Model's Belief Is Right; Its Decision Is Fragile” is rhetorically strong but only partially packet-supported: “right” is cleanest for the epistemic-games posteriors; “fragile” is an interpretation of 5/36 and the proxy associations.

## 2. Specific Claim Challenges (with Packet Evidence)

**Challenge A – Opening and core numeric framing**  
Draft: “In a controlled probe of 36 matched pairs, Mercury-2.5's stated posterior never changed with the order… terminal decision changed in 5 of those pairs, and every one of those 5 changes was a correctness flip. Diagnostic choices diverged in 17 of 36. The belief layer is order-invariant; the behavior is not.”  
Packet match on the raw counts (0/36, 5/36 all correctness, 17/36) is exact.  
**Overclaim:** “belief layer” and the clean singular “the behavior.” Packet supplies three endpoints (posterior, terminal answer, diagnostic choice). Diagnostic divergence (17/36) is larger than terminal-answer flips (5/36); collapsing them loses information. “Layer” is mechanistic language the draft itself later disclaims.  

**Challenge B – “Roughly one in seven” gloss**  
Draft: “presentation-sensitive in roughly one in seven pairs, and wrong in one in seven of those.”  
5/36 ≈ 0.1389 (≈1/7.2). The first clause is acceptable rough language. The second clause is ambiguous/misleading: all 5 flips are correctness flips, so in those 5 pairs the model is wrong *in one of the two orders*. It is not “wrong in one in seven of those [sensitive pairs]” in a nested sense; the “and wrong…” restates the same 5/36. This invites readers to double-count or think the error rate inside the sensitive subset is also ~1/7.  

**Challenge C – Parsing dismissal**  
Draft: “The natural first explanation is that presentation changes parsing… That would make the belief flip too… It did not. … pushes the locus of fragility downstream of belief computation.”  
Packet supports the observation (0 belief flips). It does **not** support the inference that parsing is ruled out or that the locus is “downstream.” A parsing difference that is later corrected before the stated-posterior elicitation, or an extraction/report artifact that affects only the terminal-answer field, remains possible. Packet lists “Terminal-answer extraction may be brittle” as a limitation; the draft mentions brittleness only in the limits section and does not weigh it against the 5 flips. The “downstream” language is an unsupported inference.  

**Challenge D – Epistemic-games gloss**  
Draft: “all 23 cases — base scenarios plus evidence, presentation, and prior interventions — produced zero posterior error and the correct verdict. … Belief tracks content.”  
Packet: 23/23 exact posterior match, zero posterior error, `posterior_reported` equals `posterior_true`.  
“Correct verdict” is not explicitly in the packet (only posterior equality). If verdict is downstream of posterior, it may follow, but it is an extra attribution. “Belief tracks content” is a reasonable summary for these 23 but is not licensed as a general campaign property.  

**Challenge E – Proxy section**  
Draft: “pass at 0.30 (8 of 27)… 0.25 (1 of 4)… against a 0.69 base… 7 of 76… 4 of them under the visible-proxy tag. … direction is consistent and the within-pair flips are hard to explain by difficulty alone.”  
Raw fractions match the packet.  
**Overclaims:** (1) Treating 1/4 and 8/27 as stable rates (tiny n, especially reward_proxy). (2) “Hard to explain by difficulty alone” – packet states interventions are *not* difficulty-matched; therefore difficulty remains a live confound and the “hard to explain” dismissal is unsupported. (3) The 7 flips are “within 76 intervention cases sharing a latent spec with a base case”; the draft correctly flags non-matched difficulty earlier but then softens it. Base denominator 331 vs overall scored 405 is fine but should be caveated that base and intervention sets are not a clean partition of the same difficulty distribution.  

**Challenge F – “Most informative result” and evaluation consequences**  
Draft: “That is the most informative result I can defend… a benchmark that scores only the former will miss it. … Evaluating a model on its stated belief alone overstates reliability. … any evaluation that fixes one presentation and reports one number is measuring a presentation, not just a capability.”  
These are authorial judgments, not packet facts. The packet supplies no ranking of “informativeness,” no benchmark comparison, and no demonstration that other evaluations are thereby invalidated. The consequences paragraph escalates a 36-pair observation into a general evaluation prescription without additional evidence.  

**Challenge G – Limits section completeness and wording**  
Draft correctly lists single model/provider, n=36 no CIs, not difficulty-matched, brittle extraction, no replication, dirty repo, 11 unscored, judge-guarantee split.  
**Gaps / misstatements:**  
- “56 unverified twin groups” vs packet “56 of 132 twin cases unverified.” Terminology drift (groups vs cases; omits the 132 denominator).  
- “pass rates from 0.00 to 1.00” – absent from packet → unsupported.  
- Omits “Single seed per selected cell” (packet) as a distinct limitation on campaign variance.  
- “exact source identity is unresolved” is fair given dirty repo, but the draft does not quantify how that interacts with the 36 T1 pairs or the 5 flips.  

**Challenge H – Title + final sentence**  
Title asserts “Belief Is Right.” Packet supports rightness most cleanly on the 23 epistemic games; T1 supplies invariance + answer correctness flips but not an explicit per-trial posterior-error table. Final sentence (“the experiment that would fuckingly settle it”) is tone-breaking and overclaims decisiveness.

## 3. Missing Caveats, Confounds, and Unsupported Inferences

- **Extraction brittleness vs. the 5 flips:** Packet flags terminal-answer extraction may be brittle. This is a direct alternative explanation for some or all of the 5 terminal flips and must sit beside the claim, not only in a later limits dump. Diagnostic choices (17/36) may share extraction or formatting sensitivity.  
- **Stated vs. internal belief:** All belief data are *elicited/reported* posteriors. Packet never validates that the reported number equals an internal computational state. The dissociation is between reported belief and reported decisions.  
- **T1 posterior correctness:** Invariance is shown; unconditional correctness of the invariant number is assumed from “Oracle is exact” + answer correctness flips, but not directly tallied for the 36 pairs the way it is for the 23 games.  
- **Sample-size and multiplicity:** 36 pairs, 6 cells, no CIs, single model. 5/36 and 17/36 need binomial uncertainty or at least explicit “descriptive only.” Reward-proxy n=4 is anecdotal. Multiple endpoints (belief, answer, diagnostic) on the same pairs inflate the chance of observing some divergence.  
- **Difficulty and selection confounds on proxies:** Explicitly not matched; paired flips help but do not eliminate the confound. Campaign uses single seed per selected cell + dirty repo → cell-level noise and irreproducibility are first-order.  
- **Judge heterogeneity:** 189 behavioral_reference vs 227 compile_only. Pass/fail meaning is not uniform; collapsing into “0.69 base” without stratification is a mild unsupported inference when discussing decision fragility.  
- **Unverified twins (56/132):** Directly relevant to any claim that relies on matched or paired structure. Draft buries it.  
- **No variance estimate / no second seed:** Packet notes single seed for selected cells. T1’s 6 seeds are the exception; the rest of the campaign cannot speak to stability.  
- **Presentation orders themselves:** “Canonical bullet order” vs “reversed numbered order” – packet does not detail whether numbering, list format, or pure order is the active factor. Draft treats it as pure order.  
- **Inference leap from “can come apart” to evaluation prescriptions:** Unsupported. The packet shows they came apart on these items; it does not show that belief-only scoring systematically overstates reliability across benchmarks.

## 4. Arithmetic Errors or Misattributions

- Core T1 fractions: 0/36, 5/36, 17/36 – correct. 6 cells × 6 seeds = 36 – correct. 3×2=6 cells – correct.  
- Epistemic 23/23 – correct.  
- Proxy: 8/27=0.296→0.30, 1/4=0.25, 228/331≈0.6888→0.69 – acceptable rounding. 7 flips (4 visible_proxy) inside 76 – matches.  
- Campaign: 416 selected, 405 scored, 11 unscored, 277 PASS / 128 FAIL, 277/405≈0.68395→0.684 – correct. 189+227=416 – correct.  
- **Misattribution / wording:** “56 unverified twin groups” ≠ packet’s “56 of 132 twin cases unverified.”  
- **Unsupported number:** Environment pass rates “from 0.00 to 1.00” – not in packet.  
- **Gloss error risk:** “one in seven” is roughly ok for 5/36 but the doubled “wrong in one in seven of those” is sloppy.  
- No other arithmetic failures detected. Base 331 + interventions do not sum to 405 (as expected; they are overlapping/paired subsets), and draft does not claim they do.

## 5. House-Style Fit

**Fits well:**  
- Jekyll frontmatter, byline with `icon-self`, epistemic-status `<dl>` with the five fields, first-person voice, concrete counts placed early, caveats present (though back-loaded), no internal paths/IDs/draft labels.  
- Certainty and Importance fields in the dl are appropriately modest.  
- Structure (probe → why-not-parsing → broader suite → proxies → implications → limits → bounded conclusion) is readable and self-correcting in intent.

**Fit problems:**  
- “belief layer,” “locus of fragility downstream,” and title absolutism sit uneasily with the later “not a diagnosis of an internal mechanism” and the Certainty field (“Interpretation, not mechanism”).  
- “fuckingly settle it” violates the “technically literate, self-correcting,” non-crude register implied by the style reference and the rest of the draft.  
- “🤥 claim” (literal in the supplied draft) is either a typo, an unrendered emoji, or an editing artifact; it has no place in public copy.  
- “the most informative result I can defend” is stronger authorial assertion than the hedged dl Importance field.  
- Figure reference and caption are fine if the asset exists; otherwise they become an unsupported claim.  
- Date 2026-10-16 is internally consistent with a future-dated series but irrelevant to evidence.  
Overall: 80 % style-compliant; the mechanistic slips, the profanity, the “🤥”, and the twin-cases wording are the main defects.

## 6. Response-to-Review Table  
(Objection → Required change. Minimum actionable edits to make the piece packet-safe.)

| # | Objection (concrete) | Required change |
|---|----------------------|-----------------|
| 1 | “Belief layer” / “downstream of belief computation” / title “Belief Is Right” overclaim mechanism and unconditional correctness | Replace all “layer” language with “stated/elicited posterior” or “reported belief endpoint.” Soften title to “Stated Belief Invariant; Terminal Decisions Fragile (on this probe)” or equivalent. Explicitly note that T1 shows invariance; unconditional posterior correctness is directly evidenced only for the 23 epistemic-games cases. |
| 2 | “Roughly one in seven… and wrong in one in seven of those” is ambiguous and risks double-counting | Rewrite to exact fractions: “terminal answer flipped in 5/36 pairs (all correctness flips); diagnostic choices diverged in 17/36.” Drop or precisely gloss the “one in seven.” |
| 3 | Parsing alternative and extraction brittleness under-weighted relative to the 5 flips | Move “Terminal-answer extraction may be brittle” into the main T1 results paragraph or the “why this is not a parsing story” section. State that a reporting/extraction artifact remains a live alternative for (some of) the terminal flips; belief invariance makes wholesale parsing failure less likely but does not eliminate field-specific brittleness. |
| 4 | Proxy causal language and “hard to explain by difficulty alone” | Keep the raw rates and the 7/76 flips. Delete or heavily hedge “hard to explain…”. Reiterate immediately: “not difficulty-matched; association only; n=4 for reward_proxy is too small for rate claims.” |
| 5 | “Most informative result,” general evaluation prescriptions, and “measuring a presentation, not just a capability” | Demote to first-person opinion: “the clearest dissociation I can defend from these data.” Soften consequences to “suggests that belief and decision endpoints should be scored separately on this style of task; presentation order is a design variable worth controlling or randomizing.” Remove any implication that existing benchmarks are thereby invalidated. |
| 6 | Twin-cases wording + missing single-seed + invented 0.00–1.00 range | Change to “56 of 132 twin cases unverified.” Add “single seed per selected cell” to limitations. Delete “pass rates from 0.00 to 1.00” or replace with packet-only statements (overall 0.684, base ≈0.69, proxy lower). |
| 7 | Tone breaks (“fuckingly,” “🤥 claim”) and residual mechanistic phrasing | Delete “fuckingly”; replace with “would help settle.” Fix or remove “🤥.” Audit every sentence for endpoint vs. mechanism language; keep the existing disclaimer but make the body match it. |
| 8 | Missing uncertainty / small-n caveats beside the headline numbers | Immediately after the 0/36, 5/36, 17/36 statement add: “Descriptive counts only; n=36 pairs, no confidence intervals, one model/provider, six seeds.” Same for proxy fractions. |
| 9 | Epistemic-games “correct verdict” extra attribution | Change to packet language: “23/23 exact posterior match, zero posterior error (`posterior_reported` = `posterior_true`).” Only add “verdict” if the packet or source snapshots explicitly support it. |
| 10 | Campaign context over-weighting | Keep 416/405/277/128 and judge split as background. Do not let campaign size imply that the 36-pair dissociation is more robust than it is. Stress that T1 is the primary evidence for the order effect. |

## Summary Judgment

The draft’s central numeric claims about T1 (0/36 belief, 5/36 terminal correctness flips, 17/36 diagnostic) and the epistemic-games exactness are tightly supported and constitute a real, interesting behavioral dissociation on endpoints. The proxy associations are directionally consistent with the packet but weaker (small n, no difficulty matching).  

Everything beyond those descriptive facts—layers, loci, “most informative,” general evaluation morals, causal flavor on proxies, unconditional “belief is right,” and the rhetorical close—is overclaim or unsupported inference. Extraction brittleness, stated-vs-internal belief, single-seed dirty-repo status, and the 56/132 unverified twins are under-emphasized relative to their threat against the 5 flips.  

With the table implemented, the piece becomes a clean, caveated, house-style-compliant report of a narrow but genuine endpoint dissociation. Without those changes it overreaches the verified packet and risks readers treating a 36-pair observation + associations as a mechanistic or benchmarking result.  

**Minimum viable fix priority:** Items 1, 2, 3, 6, 7, 8 in the table. Those alone remove the clearest factual and inferential failures.
