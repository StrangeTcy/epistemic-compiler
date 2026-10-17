gemini 3.1 pro grounding:

Here is the editorial blueprint for the final POST-04 article, synthesizing the candidate drafts and enforcing all evidence constraints.

# BATTLE ARENA EDITORIAL CRITIC — POST-04 BLUEPRINT

## 1. BASE SELECTION
**Base Draft:** `fable 5.1`
**Rationale:** `fable 5.1` provides a complete, fully readable markdown draft that successfully integrates all nine Stage A blocking issues into its prose. It adopts a suitably cautious, correlational tone, builds an excellent tiered-evidence section, and enumerates the required caveats elegantly. `opus 5` is rejected as the base because it failed to output the actual draft text (instead summarizing a file written to a sandbox we cannot access) and admits to deriving its own Wilson intervals, which violates our strict adherence to the verified evidence packet. 

## 2. IMPORT PLAN
While `fable 5.1` will serve as the structural and textual foundation, the following analytical nuances must be imported from the `opus 5` summary:
*   **Taxonomy Clarification (`share_of_eligible_failures`):** Explicitly note that the 128 FAIL verdicts are a *subset* of eligible failures based on the F-007 field name. This prevents readers from attempting to improperly reconcile the 128 failures against the 416 selected cases or 331 base cases.
*   **The "76 coincidence":** Import `opus 5`'s sharp observation regarding the 76 shared latent specs vs. the 76 verified twins (132 total - 56 unverified). Explicitly flag that whether these are the *exact same* 76 cases is an unverified coincidence in the data, avoiding a false assumption of identity.
*   **F-009 Restatement:** Ensure F-009 is explicitly named in the text as a restatement of F-002, not an independent replication (as `fable 5.1` does, but reinforce the specific evidence IDs).
*   **Production Clean-up:** `fable 5.1` contains rogue emojis (`👹`, `🤥`). These must be replaced with standard editorial prose, while carefully preserving the intentional bracketed tokens (e.g., `[d-word]`).

## 3. CLAIM LEDGER
| Claim | Status | Evidence Basis / Resolution |
| :--- | :--- | :--- |
| "Mercury failures are mostly behavioural, not infrastructural." | **REMOVE / QUALIFY** | F-007 shows 78.1% (100/128) underfit/overfit vs. 21.9% mechanical. Retain `fable 5.1`'s explicit retraction of this binary, noting 1-in-5 failures is mechanical. |
| "The model usually produces a patch that runs." | **REMOVE** | Execution status is not recorded in F-007. Retain `fable 5.1`'s framing of this as an unverified "tempting inference." |
| "Several overfit cases actually had a trusted score of 1.0 but missed companion files." | **QUALIFY** | Ground truth shows `batchnorm_ema` as the only verified case. Retain `fable 5.1`'s bracketing of this uncertainty (could be 3/49 or 20/49). |
| "The proxy channel provides a shortcut the model takes." | **REMOVE** | Mechanistic/causal language unsupported by packet. Replace with correlational language + 5 alternative hypotheses (difficulty confounding, distraction, etc.). |
| "Single-file specs with exact oracles make failures disappear." | **QUALIFY** | Unsupported by any pass-rate data in the packet. Demote to a Tier 3 "unmeasured hypothesis." |

## 4. FIGURE PLACEMENT & HYGIENE
*   **Figure 5 (Failure Modes):** 
    *   *Placement:* After the paragraph detailing the 78.1% / 21.9% split in "The shape of the failure set."
    *   *Hygiene:* Caption must cite F-007 and explicitly state *n=128 eligible failures*.
*   **Figure 6 (Pairwise intervention):**
    *   *Placement:* At the end of "The one quantified intervention pattern" section.
    *   *Hygiene:* Caption must cite F-002. It must prominently flag that the `reward_proxy` cell (n=4) is statistically degenerate and cannot be interpreted as a stable rate. Do *not* include Wilson intervals (rejecting `opus 5`'s hallucinated derivation).

## 5. SECTION STRUCTURE
The final post must follow this refined structure:
1.  **Front Matter & Epistemic Status:** Metadata, author byline (preserving bracketed/icon tokens), and epistemic disclosures (low-to-moderate certainty, non-causal).
2.  **A Note on the Title:** Disclaiming the original "conditions" framing and downshifting to "observed patterns."
3.  **The Shape of the Failure Set:** Quantifying the F-007 labels (78.1% vs 21.9%) and retracting the behavioural/infrastructural overclaim. (Insert Figure 5).
4.  **What "Overfit" Does and Does Not Mean Here:** Exploring the `batchnorm_ema` companion-file artifact and bounding the uncertainty of the `overfit_visible_tests` label.
5.  **The One Quantified Intervention Pattern:** F-002 proxy channel metrics (0.30 vs 0.69). Explaining the 7/76 pass-to-fail flips. (Insert Figure 6).
6.  **What the Proxy Pattern Does Not Show:** Enumerating alternative hypotheses to the mechanistic "shortcut" claim.
7.  **Observed Patterns by Evidential Tier:** Grouping claims strictly into: Quantified, Descriptive, and Unmeasured.
8.  **Caveats (Limitations):** Six-part list (Judge composition, Unscored cases flatting rates, Unverified twins/76 coincidence, Single seed/No replication, Dirty repo).
9.  **Summary:** A strictly bounded conclusion wrapping up the verified observations.

## 6. RESPONSE-TO-REVIEW TABLE
| Stage A Blocking Issue | Resolution in Blueprint |
| :--- | :--- |
| 1. "Mostly behavioural" overclaim | Retracted. Explicitly quantified using F-007 (100/128 vs 28/128) and acknowledging the 21.9% mechanical failure rate. |
| 2. "Patch that runs" unsupported | Removed as fact; reframed as an unsupported inference since labels are not execution states. |
| 3. "Several" unquantified | Bounded with specific hypothetical margins (e.g., 6% vs 40%) to demonstrate the gap in evidence. |
| 4. n=4 / missing denominator | `reward_proxy` isolated as an unstable estimate. Denominators added to all flip rates (7/76). |
| 5. "Shortcut" causal | Replaced entirely with correlational findings ("associated with lower pass rate") and a list of 5 alternative explanations. |
| 6. Success conditions unsupported | Demoted to the "Not measured at all" tier. Identified explicitly as a hypothesis for future analysis. |
| 7. Overgeneralised from batchnorm_ema | Restricted to "Descriptive, from one or a few cases" tier. Bounded as a single verified instance. |
| 8. Missing caveats | Expanded into a dedicated 5+ point limitation section detailing single-seed, dirty repo, unverified twins, and unscored exclusions. |
| 9. Title promises causality | Title softened to "How Mercury Fails: Observed Failure Patterns in Mercury-2.5". Introductory paragraph explicitly disclaims counterfactuals. |

## 7. ACCEPTANCE CRITERIA
For the final production draft to be accepted, it must:
- [ ] Use `fable 5.1` as the base text but implement the targeted imports from `opus 5` (eligible failures, the unverified 76 coincidence).
- [ ] Scrub the unauthorized emojis (`👹`, `🤥`) inserted by `fable 5.1` and replace them with standard editorial phrasing.
- [ ] Preserve all intentional bracketed tokens (e.g., `[d-word]`) exactly as they appear.
- [ ] Make no mention of Wilson intervals or any statistical tests not present in the verified evidence packet.
- [ ] Maintain the strict boundary between measured intervention patterns (n=331/n=27), unverified hypotheses (single-file exact-oracles), and degenerate data (n=4).

&&&&&&&&&&&&&&&&

gpt 6 luna max:

# POST-04 Editorial Blueprint

**Editorial decision:** Use **Fable 5.1** as the working manuscript. Import selected evidence-handling decisions from **Opus 5**, but do not treat its change-log summary as an article draft. Fable is the only complete article supplied; it has a usable structure and includes most of the Stage A corrections. It is **not ready to publish as-is**: several statements need tighter denominators or more cautious wording.

## 1. Base Selection

### Use Fable 5.1 as the base

It provides a full article with a clear sequence: failure counts, the limits of the overfit label, the proxy comparison, evidence tiers, caveats, and a summary. It also includes the key arithmetic, distinguishes F-009 from a replication, and treats the single-file/exact-oracle claims as unmeasured.

### Do not use Opus 5 as the base

The supplied Opus material is a resolution summary, not a complete manuscript. It is useful as an editorial checklist, but there is no article text to assess for structure, claim placement, prose, or figure integration.

### Required corrections to the Fable base

Before publication:

- Add the F-007 denominator caveat: its field is `share_of_eligible_failures`; do not imply that 128 is the total number of failures among all 416 selected cases.
- Remove the assertion that the visible-proxy difference is not likely due to noise. The supplied evidence does not support that inference.
- Correct any description of the 7/76 flips that implies the denominator is 76 initially passing cases. It is 76 shared latent specifications.
- Remove the claim that unscored cases “slightly flatter” every rate. The direction of any effect is unknown.
- Rework the judge-guarantee caveat: the packet gives the 189/227 composition but does not establish that compile-only judges assign particular labels with less confidence.
- Avoid treating the absence of a difficulty-matching analysis or manual audit as established fact unless the underlying records confirm it. If not confirmed, say the packet does not report one.
- Make the title and lede describe observed patterns, not causes or proven failure conditions.

## 2. Import Plan

| Element from Opus 5 | Editorial action |
|---|---|
| **F-007 uses `share_of_eligible_failures`.** | Import this caveat. Say that the 128-category tally covers eligible failures; the eligibility denominator and its relationship to the 416 selected cases are not specified in the packet. Do not calculate a failure share over 416 or compare the 128 directly with the F-002 base denominator of 331. |
| **F-009 restates F-002.** | Keep Fable’s explicit statement that F-009 is not a replication. Describe the proxy comparison as one measurement. |
| **“Patch that runs” is an inference, not an execution result.** | Preserve Fable’s retraction. Prefer removing the claim; if discussed, label it explicitly as an inference unsupported by the failure labels. |
| **The count behind “several” is unknown.** | Import the uncertainty, but do not import illustrative counts such as 3/49 or 20/49 as bounds, estimates, or plausible endpoints. The supplied packet does not give a numerator. |
| **Wilson intervals.** | Do not import them solely from Opus’s summary: it supplies no interval values or calculation, while Fable says none were computed. Default to reporting counts and caveats. If intervals are retained after independent reproduction, identify them as derived and do not present them as resolving confounding or establishing causality. |
| **Quantified label arithmetic.** | Retain Fable’s 100/128 and 28/128 calculations, while making clear these are groupings of labels for arithmetic—not a behavioral/infrastructural classification in the data. |

## 3. Claim Ledger

| Major claim | Decision | Evidence basis and final treatment |
|---|---|---|
| F-007 contains 51 `underfit`, 49 `overfit_visible_tests`, 11 `runtime_error`, 9 `source_invalid`, 5 `invalid_action`, and 3 `training_failure` labels. | **RETAIN** | These counts sum to 128. Refer to them as the F-007 eligible-failure tally; preserve the source labels. |
| The two largest labels account for 100/128, or 78.1%; the other four account for 28/128, or 21.9%. | **RETAIN, WITH QUALIFICATION** | The arithmetic is correct. State that these are shares within the 128 counted cases, not shares of all 416 selected cases. |
| Mercury-2.5 is “mostly behavioural, not infrastructural.” | **REMOVE** | The taxonomy does not provide that distinction. Replace it with the quantified label distribution. |
| Mercury-2.5 “usually produces a patch that runs.” | **REMOVE AS A FINDING** | F-007 contains failure-mode labels, not an execution-status record. If the thought is retained at all, explicitly label it as an unsupported inference—not a result. |
| `overfit_visible_tests` means the model gamed the visible tests. | **QUALIFY** | Treat it as a judge-assigned label, not an audited mechanism. The packet reports cases with `trusted_score` 1.0 and a missing companion file; the count of such cases is unknown. |
| Companion-file failures occur, including `batchnorm_ema/model.py`. | **RETAIN, WITH QUALIFICATION** | Retain as descriptive evidence. The packet reports “several,” but does not quantify them; identify the named case and do not generalize to all 49 overfit-labeled cases. |
| Visible-proxy cases passed at 8/27 (0.30), versus 228/331 (0.69) for base cases. | **RETAIN, WITH QUALIFICATION** | Report as observed cell fractions and describe the comparison as an association. Do not claim a causal effect or rule out case-mix differences. |
| Reward-proxy cases passed at 1/4 (0.25). | **QUALIFY** | The observed count may be reported, but n=4 is too small to treat 0.25 as a stable underlying rate. |
| Seven pass-to-fail flips occurred within 76 shared latent specifications. | **RETAIN, WITH QUALIFICATION** | State the denominator exactly: 7 of 76 shared specifications. Do not call it 7 of 76 initially passing cases unless that denominator is verified. It is not causal proof. |
| F-009 independently replicates the proxy result. | **REMOVE** | F-009 is a restatement of F-002, not a replication. |
| Proxy channels are a “shortcut” the model takes. | **REMOVE AS A FACTUAL CLAIM** | Replace with an observed association and, if useful, clearly labeled possible explanations. Intent and mechanism are not observed in the packet. |
| Visible-test-heavy grading, multi-file edits, and companion files are established general failure conditions. | **QUALIFY** | Present as candidate risks or descriptive observations at the evidence level actually supplied. Do not imply a quantified effect or general causal rule. |
| Single-file specifications and exact oracles prevent failures or make them disappear. | **QUALIFY** | Present only as an unquantified hypothesis for future testing. No pass-rate for this stratum is supplied. |
| The 11 unscored cases and 56/132 unverified twins affect the reported rates in a known direction. | **REMOVE THE DIRECTIONAL CLAIM** | Retain the counts as limitations. Do not say the unscored cases flatter rates or assume the 76 shared specifications are the same set as the 76 verified twins. |
| Judge guarantees are 189 `behavioral_reference` and 227 `compile_only`, out of 416 selected. | **RETAIN, WITH QUALIFICATION** | Report the composition as context. The packet does not cross-tabulate these guarantees against F-007 labels. |

## 4. Figure Placement and Hygiene

### Figure 5 — failure-label counts

**Placement:** Immediately after the paragraph giving the F-007 counts and the 100/128 and 28/128 arithmetic.

**Recommended caption:**  
*Figure 5. Judge-assigned F-007 labels among 128 eligible failures: underfit 51, overfit_visible_tests 49, runtime_error 11, source_invalid 9, invalid_action 5, and training_failure 3. Counts sum to 128; the eligibility denominator beyond this tally is not specified.*

**Production requirements:**

- Show the six source labels and their exact counts.
- Do not regroup the chart into behavioral/infrastructural categories.
- Include accessible alt text that conveys the labels and counts, not just “Failure modes.”
- Verify that the SVG exists at the cited path, that its values match the caption, and that figure numbering is correct in the full post.

### Figure 6 — proxy-tagged pass fractions

**Placement:** After the proxy comparison and the separate 7/76 shared-specification statement.

**Recommended presentation:** Use a neutral title such as *Observed pass fractions by tag*. Keep the pass-fraction chart distinct from the 7/76 flip count; do not call a chart of aggregate cell rates “pairwise.”

**Production requirements:**

- Label each value with both numerator and denominator: base 228/331, visible proxy 8/27, reward proxy 1/4. Percentages may be shown alongside those counts.
- Make the n=4 limitation visible in the figure or caption.
- Do not use causal visual language such as “effect,” or add uncertainty bars unless their calculation and method have been verified.
- Note that F-009 restates F-002; the graphic represents one measurement.
- Verify the referenced SVG, alt text, axis, data labels, caption, and numbering.

## 5. Proposed Final Section Structure

1. **Title, metadata, byline, and epistemic status**  
   Keep a title framed around observed patterns. Make the certainty statement claim-specific: the counts are descriptive; mechanisms and generalizations are uncertain.

2. **Opening: what this post can and cannot say**  
   Briefly state that the post describes judge labels and one proxy-tagged comparison; it does not establish causes. Keep the published lede reader-facing rather than narrating internal draft history.

3. **What the failure counts cover**  
   Explain the F-007 eligible-failure denominator before presenting percentages. Distinguish that tally from the 416 judge-guarantee-selected cases and the separate F-002 base denominator of 331.

4. **Two labels account for 100 of 128 cases**  
   Present all six counts, the 78.1% and 21.9% arithmetic, and Figure 5. Avoid behavioral/infrastructural interpretation.

5. **What the overfit label does not establish**  
   Explain that the label is not proof of visible-test gaming. Describe the trusted-score/companion-file observation, name `batchnorm_ema/model.py`, and state that the number of affected cases is unknown.

6. **One proxy-tagged comparison**  
   Report the base, visible-proxy, and reward-proxy counts and fractions; explain the n=4 caveat; report the 7/76 shared-specification flips with the correct denominator; state that F-009 is a restatement, not replication. Place Figure 6 here.

7. **Evidence tiers for proposed “conditions”**  
   - **Quantified:** observed proxy-tagged pass fractions and the 7/76 flip count.  
   - **Descriptive but unquantified:** companion-file cases and the overfit-label ambiguity.  
   - **Hypotheses only:** broader claims about visible-test-heavy grading, multi-file edits, and the proposed success conditions of single-file specifications and exact oracles.

8. **Limitations**  
   Include the limitations listed below as a visible, numbered section.

9. **Conclusion**  
   Summarize the label distribution and the one proxy-tagged comparison without claiming an identified cause or a tested set of success conditions.

## 6. Response-to-Review Table

| Stage A blocking issue | Required response in the final article |
|---|---|
| **1. “Mostly behavioural” overclaim** | Replace the label with the arithmetic: 100/128 (78.1%) are the two largest labels; 28/128 (21.9%) are the other four. Explicitly say the data do not classify labels on a behavioral/infrastructural axis. |
| **2. “Patch that runs” unsupported** | Remove it as a finding. If discussed, call it an inference and explain that the taxonomy is not an execution-status record. Do not infer that the 108 cases outside `runtime_error` and `source_invalid` ran successfully. |
| **3. “Several” unquantified** | Say the packet reports several trusted-score-1.0 cases with missing companion files but does not give a count. Name the documented example without extrapolating from it. |
| **4. n=4 / missing denominator** | Report reward proxy as 1/4 and label it too small for a stable rate. State 7/76 using “shared latent specifications” as the denominator. Add the F-007 eligible-denominator caveat and do not equate the 76 shared specifications with the 76 verified twins without confirmation. |
| **5. “Shortcut” is causal** | Replace with correlational wording: pass fractions are lower in proxy-tagged cells. Any explanations—shortcut behavior, difficulty differences, complexity, grading differences, or sampling variation—must be presented as possibilities, not findings. |
| **6. Success conditions unsupported** | Recast single-file specifications and exact oracles as unquantified hypotheses. Do not say that failures disappear under those conditions. |
| **7. Overgeneralized from `batchnorm_ema`** | Separate quantified results from case-level description and untested generalizations. Keep companion-file or multi-file claims at the descriptive or hypothesis tier unless additional counts are supplied. |
| **8. Missing caveats** | Add at least five explicit limitations. The recommended six are: (1) F-007’s eligible denominator is unspecified; (2) the 189/227 judge-guarantee mix is not cross-tabulated with labels; (3) 11 cases are unscored, with the stated breakdown, and 56/132 twins are unverified; (4) one model/provider, one seed per cell, and no replication; (5) dirty repository state; (6) the packet does not provide a difficulty-matching analysis for the aggregate proxy comparison. Treat the relationship between the 76 shared specifications and the 76 remaining twins as unconfirmed. Assert that no manual audit occurred only if the underlying review record verifies it; otherwise say the packet supplies no audit result. |
| **9. Title promises causality** | Keep the softened observational framing and make it consistent across the title, lede, headings, captions, and conclusion. Do not promise “conditions,” causes, or explanations the data do not establish. |

## 7. Acceptance Criteria

The final article is ready only when all of the following are true:

- **Counts and arithmetic are correct:** F-007 counts sum to 128; 100/128 is reported as 78.1% and 28/128 as 21.9%; F-002 values are reported with their numerators and denominators; the flip count is 7/76.
- **Denominators are explicit:** F-007 is not presented as a share of 416 or 331; F-002’s base, proxy, and shared-specification denominators are distinguished.
- **Labels are not turned into mechanisms:** `overfit_visible_tests` is not treated as proof of gaming, and the failure labels are not presented as a behavioral/infrastructural taxonomy.
- **Small cells are treated cautiously:** 1/4 is reported as an observed fraction, not a stable estimate; no claim that the visible-proxy gap is beyond sampling noise appears without a separately supported analysis.
- **Causal language is controlled:** proxy results are described as associations; hypotheses are visibly labeled; no unsupported “shortcut” or “failures disappear” claim remains.
- **Replication is represented accurately:** F-009 is identified as a restatement of F-002.
- **Limitations are prominent:** at least five are explicitly listed, including the eligible-denominator issue, judge-guarantee composition, unscored and unverified cases, single-model/single-seed/no-replication design, and dirty repository.
- **Figures are verified:** both assets exist, values and captions match, captions cite F-007 or F-002, accessible alt text is meaningful, and figure numbering is correct.
- **Production markup is clean:** the published Markdown contains the article—not assistant narration or an enclosing code fence—and matches the site’s actual front-matter and byline conventions.
- **Date is checked:** the supplied front matter is dated **2026-10-16**. Confirm that it is the intended publication date; if publication is intended for **October 17, 2026**, update it before shipping.
