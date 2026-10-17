grok 4.5:

**EDITORIAL BLUEPRINT — POST-01**  
**Title retained:** The Model’s Belief Is Right; Its Decision Is Fragile (Mercury-2.5)  
**Core directive:** Produce an *original* final article. Do not merge the drafts. Prefer the narrow behavioral dissociation (invariant stated posterior + variable terminal answer/diagnostic choice under matched presentations). Keep T1 (paired probe), epistemic games, proxy interventions, and campaign coverage as *distinct measurements*. Enforce all reviewer-brief corrections and caveats. House style: StrangeTcy Jekyll (epistemic-status dl, precise counts, restrained first-person, SVG figures with accessible titles/descs, no profanity, no unsupported sweep, bracketed author-disliked tokens left intact).

### 1. Strongest thesis to adopt (and why)
**Adopt (tightened):** In a controlled 36-pair presentation probe, Mercury-2.5 produced identical reported posteriors across every matched pair of fact presentations, yet its terminal answer flipped in 5/36 pairs (all correctness flips under an exact oracle) and its diagnostic choice diverged in 17/36 pairs. Separately, in 23 oracle-scored epistemic games the reported posterior exactly matched the true posterior every time. Proxy-tagged cases showed lower observed pass fractions in a confounded comparison; these do not measure or explain the same dissociation.  

**Why this version:** It is the only claim fully licensed by the evidence packet (0/36 belief flips; 5/36 terminal answer flips all correctness; 17/36 diagnostic; 23/23 exact posterior match; proxy numbers as given; campaign 416/405/277/128). It treats the findings as distinct measurements, refuses internal-module or “knows-but-fails-to-act” stories, and stays inside the reviewer brief’s “narrow behavioral dissociation is defensible; stitching T1 and proxy into one ‘decision’ narrative is NOT.” Anything stronger (causal mechanism, general decision fragility, proxy-as-explanation) is unsupported and must be rejected. Anything weaker loses the informative conjunction that a posterior-only summary would miss the five correctness reversals.

### 2. Opening strategy (which draft’s opening is stronger and why)
**Prefer Draft B’s opening strategy, reconstructed with Draft A’s precision.**  

Draft B opens with the sharp, reader-facing question (“What should I conclude when a model reports the same probability under two presentations of the same facts, yet gives a correct answer in one presentation and an incorrect answer in the other?”) then immediately disciplines the tempting over-read (“knew the answer but failed to use it… more than these measurements establish”). This is stronger: it surfaces the exact tension the title names, sets the epistemic posture of restraint in the first two paragraphs, and primes the reader for the dissociation-of-outputs framing.  

Draft A’s opening is solid but flatter (“If a model gives the same probability… should it also give the same answer? I would have expected so…” then dumps the 36-pair counts). It buries the restraint and feels more like a results dump.  

**Final opening blueprint:**  
- Lead with B-style question.  
- Immediately state the narrow observation (0/36, 5/36 all correctness, 17/36) using A’s exact wording density.  
- Explicit restraint sentence (belief = stated posterior; “right” licensed only by the separate 23 games; do not quietly merge).  
- One-sentence map: “These are distinct measurements.”  
- Then drop into the epistemic-status dl (hybrid of both, preferring A’s more precise “Original ideas” and “Importance” while adopting B’s certainty caveats).

### 3. Section-by-section structure for the final article (ordered list with purpose)
1. **Epistemic-status dl** (mandatory house element) — Bound originality, synthesis, prose provenance, certainty, importance. Purpose: set reader expectations and prevent overclaim.  
2. **Opening + core observation** (1–2 short paras) — Pose the question, state the 36-pair numbers cleanly, enforce the “belief = stated posterior; right licensed separately” restraint. Purpose: hook + thesis lock.  
3. **Hold the facts fixed; change their presentation (One comparison, three endpoints)** — Describe the 6-cell × 6-seed design, the bundled manipulation (order + format), the three endpoints with counts, and what each does/does not establish. Include the primary SVG bar figure. Purpose: ground the reader in the exact experiment.  
4. **The dissociation is between outputs, not modules** — Explain why identical reported posteriors + flipped answers is informative yet does not license internal “belief module → defective decision module,” parsing/extraction caveats, and why a posterior-only summary would miss real correctness reversals. Purpose: kill the tempting over-interpretation early.  
5. **Where “right” is directly observed (epistemic games)** — 23/23 exact match; keep strictly separate from the 36 pairs; no denominator addition; no claim that the five flipped pairs’ posteriors were themselves oracle-correct. Purpose: supply the accuracy warrant for the title’s first half without contamination.  
6. **A separate observation about proxy interventions** — Report the base/visible/reward numbers and the 7/76 pass→fail (4 visible) exactly; emphasize non-matched difficulty, incomplete taxonomy, directional-only count, and *explicitly* that these are not the same measurement as the presentation dissociation. Purpose: include the data the campaign contains while refusing the stitch.  
7. **How much weight can the campaign bear?** — 416 selected / 405 scored / 277–128 / 0.684; judge guarantees 189 + 227 = 416 (not 405); single-seed campaign vs 6-seed probe; dirty repo; 56 of 132 twin cases unverified; one model/config; no independent replication. Purpose: provenance and scope limits.  
8. **The next tests I would run** — Concrete, ordered follow-ups starting from the five flipped pairs (hand extraction audit + oracle check on those posteriors), then factorial separation of order vs format, more seeds, second model, difficulty-matched proxy redesign with both endpoints. Purpose: turn limitations into actionable science.  
9. **Bounded closing answer** — Restate the narrow behavioral finding in one tight paragraph; refuse mechanism claims; end on “worth replicating under cleaner conditions.” Purpose: leave the reader with the exact licensed claim.

No other sections. Keep total length lean; every paragraph must advance a verified count or a necessary caveat.

### 4. Material to retain from Draft A (gpt 6 sol max) and from Draft B (gpt 6.1 sol max)
**From Draft A (high-value, retain/adapt):**  
- The full SVG bar figure (Figure 1) and its figcaption — best visual of the three endpoints; keep the exact geometry and accessibility tags.  
- Precise cell description (“crosses three fact counts—three, four, and five—with two priors, 1/2 and 1/3… six cells, each tested with six seeds”).  
- The explicit warning that results do not locate which cell the five flips occurred in, and the refusal to invent a vivid example.  
- Extraction-brittleness paragraph and the “without the individual transcripts” [h-word]y.  
- Dirty-repo + single-seed + “commit identifier alone might be insufficient” provenance language.  
- The “next test I would run” sequence that starts with the five flipped pairs and hand-checking extraction blind to condition.  
- Epistemic-status “Original ideas” and “Importance” formulations (narrow dissociation; reason to examine both readouts).  
- The sentence that the five flips do not tell total accuracy across the 72 presentations nor which presentation was better.  

**From Draft B (high-value, retain/adapt):**  
- Opening question + immediate discipline of the “knew but failed to use” impulse.  
- Clean three-row table of endpoints (or convert to the A SVG; either works, prefer SVG for house style).  
- “The dissociation is between outputs, not modules” framing and the explicit “I do not need to identify an internal ‘decision layer’.”  
- Strong separation language: “The probe and the epistemic games are related campaign evidence, not independent replications. Their different units should not be added.”  
- Proxy table (base 228/331 0.69; visible 8/27 0.30; reward 1/4 0.25) and the 7/76 (4 visible) paragraph.  
- Judge-guarantee correction language and the insistence they partition the 416 selected, not the 405 scored.  
- “56 unverified twin cases out of 132” (correcting “groups”).  
- Closing “bounded answer” structure and the “posterior-only summary would have missed real correctness reversals.”  
- Certainty caveats in epistemic-status (one model/config, no CIs, proxy not difficulty-matched).

### 5. Material to reject or reconstruct — be specific
**Reject outright:**  
- Any residual stitching of proxy into the “decision” narrative (both drafts largely avoid this, but B’s “Calling it further evidence for one fragile ‘decision layer’” is the correct rejection tone; keep the rejection, discard any softer phrasing).  
- Draft A’s “I would have expected so, at least in a task with an exact oracle.” (mild anthropomorphism; replace with neutral).  
- Draft B’s incomplete “!” figure placeholder and any “Figure 1. Campaign coverage” ASCII art; replace with proper SVG or omit.  
- Both drafts’ stray “👹” glyphs (A: “where it 👹:”; B: “That distinction 👹 because”). These are production artifacts; remove.  
- Any implication that the 23 games certify the posteriors *inside the five flipped pairs*.  
- “Wrong in one in seven” or any garbled fraction language (B already corrects it; ensure final never uses it).  
- Pass-rate ranges “from 0.00 to 1.00” (absent, keep absent).  
- Treating 56 unverified as “groups.”  
- Attaching judge guarantees to the 405.  
- Any claim of run-to-run stability or generalizability beyond the recorded sample.  

**Reconstruct:**  
- Epistemic-status: hybrid — A’s originality/importance + B’s certainty + explicit “Prose: written from verified aggregates; no individual transcripts for this essay.”  
- Manipulation description: both note the bundle (order + format); final must say “presentation sensitivity is therefore the [d-word] description. The probe cannot assign the difference specifically to position vs numbering.”  
- Diagnostic choices: both correctly say “not necessarily incorrect”; keep and strengthen.  
- Title half “Belief Is Right”: must be explicitly scoped to the 23 games only.  
- All first-person: keep restrained “I” of house style; remove any residual casualness.

**At least three specific weaknesses per draft:**  
**Draft A:** (1) Stray 👹 glyph and slightly flatter opening that delays the restraint. (2) No table; relies solely on prose + one SVG, making the three-endpoint contrast slightly less scannable. (3) “Next test” section is excellent but buries the extraction-audit priority slightly less cleanly than B; also contains a dangling “the answer I can [d-word] now.”  
**Draft B:** (1) Incomplete figure markup (“!”) and campaign-coverage figure that is not real SVG. (2) Stray 👹 and slightly softer “attractive explanation” language that still needs one more beat of discipline. (3) Epistemic-status “Original ideas” is vaguer than A’s; proxy section, while correct, spends a fraction more words on the 76-case subset without enough taxonomy-gap emphasis.

### 6. Figure placement and which SVGs to embed where
- **Primary (required):** Draft A’s existing SVG bar figure (0/36 posterior, 5/36 answer, 17/36 diagnostic) immediately after the design description in Section 3. Keep title, desc, and figcaption almost verbatim; minor caption tweak to emphasize “All five answer changes changed correctness; diagnostic divergence ≠ error.”  
- **Secondary (optional, only if space):** A simple campaign-coverage SVG (416 selected → 405 scored / 11 unscored; 189 behavioral-reference + 227 compile-only = 416) in Section 7. Do *not* use Draft B’s broken placeholder. If no clean SVG is authored, omit and keep prose only.  
- No other figures. No tables that duplicate the SVG. If a markdown table is kept for endpoints, place it *before* the SVG and make the SVG the visual summary.

### 7. Technical examples and case selections to use
- Use *only* aggregate verified counts. No invented single-cell walkthroughs (A correctly refuses this; keep the refusal).  
- Design: 3/4/5 facts × priors 1/2 & 1/3 = 6 cells × 6 seeds = 36 pairs. Canonical bullets vs reversed numbered list.  
- Endpoints: posterior (0/36), terminal answer (5/36, all correctness flips), diagnostic choice (17/36).  
- Epistemic games: 23/23 exact posterior_true match (base + evidence/presentation/prior interventions).  
- Proxy: visible_proxy 8/27 (0.30), reward_proxy 1/4 (0.25), base 228/331 (0.69); 7 pass→fail (4 visible) within 76 intervention cases sharing latent spec.  
- Campaign: 416 selected, 405 scored (277 PASS / 128 FAIL = 0.684), 11 unscored; 189 behavioral_reference + 227 compile_only = 416; 56 of 132 twin cases unverified; single seed per selected cell (probe used 6); dirty repo; mercury-2.5 high reasoning effort.  
- No individual prompt/response transcripts (explicitly note their absence). No new measurements.

### 8. Weak sections, missing counterarguments, and gaps
- **Weak in both:** The proxy section still risks being read as “supporting” the title even when the text denies it. Final must open that section with “These results are tempting to enlist… I do not think they permit that move.”  
- **Missing counterargument:** Explicitly address “Maybe extraction noise explains the five flips.” Both mention it; final must elevate it to a first-class live alternative and make the hand-audit the #1 next test.  
- **Missing:** Short note that the other 31 pairs could be RR, WW, or mixed; stability alone does not give accuracy.  
- **Gap:** No confidence intervals or statistical test; both correctly stay descriptive — keep and say so.  
- **Gap:** Intervention taxonomy incomplete; final must say the labels do not give a uniform construction or full breakdown of scoring guarantees.  
- **Tone gap:** Both still contain residual “I” flourishes that can be tightened.  
- **Structural:** Draft A’s “What a stable number does—and does not—explain” and B’s “dissociation… not modules” cover the same ground; final collapses them into one tight section.

### 9. Exact unsupported claims to remove or narrow
- Remove any residual “the model’s belief is right *in the flipped pairs*.” Narrow to: right in the 23 games; invariant (not necessarily right) in the 36.  
- Remove any causal language about proxy “disrupting decision.”  
- Narrow “presentation sensitivity” to the bundled manipulation only.  
- Remove any implication that 5/36 or 17/36 generalize; they are descriptions of this probe.  
- Remove any “one in seven” or “14 % error rate” misreadings (B already flags; enforce).  
- Narrow judge guarantees strictly to 416 selected.  
- Narrow twin statement to “56 of 132 twin cases unverified.”  
- Remove any claim that dirty repo *did* contaminate; keep only the reconstruction caveat.  
- No “general theory of how the model decides.”

### 10. House-style fit assessment
Both drafts are already close to StrangeTcy Jekyll house style (epistemic-status dl, first-person restrained, exact counts, SVG-first, no hype). Final must:  
- Preserve the dl exactly as structured.  
- Keep bracketed [d-word], [ac-word], etc., untouched.  
- Use `<figure>` + inline SVG with title/desc/figcaption.  
- Short paragraphs, precise verbs (“elicited,” “reported,” “scored”), no profanity, no emoji/glyphs.  
- Date/layout/author span unchanged.  
- Tone: curious, precise, self-limiting — closer to A’s carefulness + B’s clarity.  
Fit score after reconstruction: high. Main risks are leftover glyphs and any accidental stitch of proxy into the main narrative.

### 11. A response-to-review table skeleton (objection → required change)
| Objection (from reviewer brief or evidence) | Required change in final article |
|---------------------------------------------|----------------------------------|
| Stitching T1 + proxy into one “decision” narrative | Keep proxy in its own section; open with explicit refusal to enlist it as explanation of the five flips; never use “decision layer” affirmatively. |
| “Pass rates from 0.00 to 1.00” fabricated | Absent; ensure no range language appears. |
| Judge guarantees misattached to 405 | State 189 + 227 = 416 selected; never attach to scored denominator. |
| “Wrong in one in seven” garbled | Never use; state “5/36 pairs… every change was a correctness change” and explicitly deny overall error-rate reading. |
| “56 unverified twin groups” | Write “56 of 132 twin cases unverified.” |
| Missing single-seed caveat | State campaign = single seed per cell; probe = six seeds; do not equate. |
| Missing intervention taxonomy gap | Explicit sentence: labels do not specify uniform construction or full scoring-guarantee breakdown. |
| Non-independence / extraction brittleness | Elevate extraction audit to #1 next test; note possible non-independence of games vs pairs. |
| Dirty repo | Keep provenance caveat; do not claim contamination. |
| Tone (profanity, stray glyph) | Remove all 👹 and any casual residual; keep [d-word] tokens. |
| Over-strong internal mechanism | Section 4 must say equality of reported numbers ≠ equality of internal states or discrete modules. |
| Title’s “right” over-claimed | Scope “right” exclusively to the 23 games; invariance ≠ accuracy for the 36. |

**Final production note:** After blueprint implementation, the article must be re-checked against the evidence packet line-by-line for every numeral. The five correctness flips and the 0/36 posterior invariance are the only load-bearing results; everything else is context or caveat. This yields an original, defensible, house-style piece that is stronger than either candidate.

&&&&&&&&&&&

fable 5.1:

# Editorial Blueprint — POST-01 "The Model's Belief Is Right; Its Decision Is Fragile"

Working convention: **Draft A** = gpt 6 sol max; **Draft B** = gpt 6.1 sol max. Where I quote a draft I quote only enough to locate the passage.

---

## 1. Strongest thesis to adopt

**Adopt:** *In 36 matched presentation pairs, Mercury-2.5's elicited posterior never moved while its terminal answer crossed the correctness boundary five times and its diagnostic choice diverged seventeen times. That is a dissociation between two measured outputs, not between two internal modules. "Right" is borrowed from a separate 23/23 oracle check and must be labelled as borrowed. The proxy-intervention pass rates are a parallel, confounded association and are not a second measurement of the same thing.*

**Why this one and not the alternatives:**

- It is the only thesis the reviewer brief marks as defensible (narrow behavioral dissociation), and both drafts independently converge on it, which is weak but real evidence that it's the natural reading of the packet.
- It survives every verified count without needing any of the fabricated or garbled numbers ("0.00 to 1.00", "one in seven wrong", "56 groups").
- It gives the article a genuine intellectual move — *the tempting "knew but didn't use it" story outruns the data* — rather than just a list of caveats. Draft B's section header "The dissociation is between outputs, not modules" is the sharpest single formulation of this move and should be promoted to a structural pillar.
- The title is fixed for POST-01, and it overclaims relative to the evidence (the "Right" half comes from a different experiment than the "Fragile" half). The thesis therefore has to *defuse the title within the first 200 words*. Draft A's "There is an important restraint hidden in the title" paragraph does exactly this and is the best paragraph in either draft.

**Reject as thesis:** anything of the form "the model has a belief layer and a fragile decision layer" (B explicitly refutes this; A implicitly does). Also reject "proxy cues disrupt the same mechanism" — both drafts correctly refuse this, and the brief forbids it.

---

## 2. Opening strategy

**Draft A's opening is stronger. Use its structure, graft one sentence from B.**

Draft A, paragraph 1: question → "Mercury-2.5 did not always oblige" → 0/36, 5/36, all-correctness, 17/36, all inside one paragraph. The reader has every headline count before the first section break. Paragraph 2 then immediately defuses *Belief* and *Right*. This is the correct order for a sceptical readership: numbers, then what the numbers cannot mean.

Draft B's opening has a better *hook sentence* — "My first instinct is to say that it knew the answer but failed to use it... It is also more than these measurements establish" — but it then fragments into six one- or two-sentence paragraphs, delays the counts to paragraph 3, and closes with a telegraphing paragraph ("Those findings deserve discussion, but they do not all measure the same thing. Keeping them separate is essential...") that announces the essay's structure instead of doing it.

**Prescription for the final opening (two paragraphs, ~220 words):**

1. A's question + A's counts paragraph, with B's "knew the answer but failed to use it" inserted as the *named* tempting explanation after the counts, and a one-clause deferral ("I'll argue that explanation outruns the data").
2. A's "restraint hidden in the title" paragraph nearly verbatim, with B's two-sentence addition "Zero posterior flips is not the same as zero posterior error. A model could report the same incorrect probability twice" spliced in after "*Right* is established by a related set of 23 oracle-scored epistemic games". That sentence pair is the cleanest statement of the invariance/accuracy distinction in either draft.

Delete B's "Keeping them separate is essential to understanding what the campaign [ac-word] tells us" — it's a thesis statement for a five-paragraph essay, not for this house.

---

## 3. Section-by-section structure for the final article

| # | Section (working header) | Purpose | Primary source |
|---|---|---|---|
| 0 | Front matter + byline + `dl.epistemic-status` | House-standard disclosure. | A's block as base; see §4 for B grafts. |
| 1 | *(untitled lede, 2 paras)* | Headline counts; name and defer the tempting explanation; operationalize *Belief* and *Right*. | A paras 1–2 + B's "zero flips ≠ zero error". |
| 2 | **Hold the facts fixed; change their presentation** | Describe design: 3×2 cells, 6 seeds, canonical bullets vs reversed numbered list, three elicited outputs. State the order+format confound. | A's design prose; B's confound para is slightly tighter. |
| 3 | **Three endpoints, one comparison** | Present 0/5/17 as **Figure 1** (A's SVG) + B's three-column table beneath or in place of a prose list. Percentages, non-additivity, "flip count ≠ overall accuracy", "diagnostic divergence ≠ diagnostic error". | A's percentage/non-additive paras; B's table and its "What the change establishes" column. |
| 4 | **The dissociation is between outputs, not modules** | The intellectual core. Why "knew but didn't use it" overreaches: identical reported numbers ≠ identical computation; the posterior need not be what determines the answer; extraction brittleness; parsing not ruled out. | B's header and body; A's "This experiment records outputs; it does not locate a failure inside the computation." |
| 5 | **Where "right" is actually observed** | 23/23 games. Bounded sense of "tracked content". Non-independence with T1; different questions; do not pool denominators. | A's "I cannot treat the 23 games as an independent replication" para; B's two-bullet invariance/accuracy contrast. |
| 6 | **A separate finding: proxy-tagged cases pass less often** | Proxy table; 7/76 pass→fail (4 visible_proxy); difficulty confound; one-directional count; n=4; taxonomy gap; explicit refusal to stitch to T1. | B's table; A's "packet does not provide a corresponding fail→pass count" and "not an estimated probability" paras. |
| 7 | **How much weight can the campaign bear?** | 416/405/277/128/0.684; **Figure 2** (new SVG: judge guarantees partition 416, not 405); single seed per selected cell vs 6-seed probe; 56/132 twins; dirty repo; one model/one config. | Both; A's "Provenance and sampling" para is more complete. |
| 8 | **What I would run next** | Five flipped pairs first (blind extraction audit, per-pair oracle check); factorial separation of order × format; **same-presentation resampling null** (new — see §8); second model/provider; difficulty-matched proxy with both endpoints elicited. | A's first two paras; B's "revised rather than defended through the oracle's exactness". |
| 9 | **A bounded answer** | Short restatement of what is and is not established. End on the gap, not on a lesson. | B's section structure; A's final paragraph content. |

Nine sections plus lede. Target length ~2,100–2,400 words — both drafts are near this; neither needs to grow except for the new null-baseline material.

---

## 4. Material to retain

### From Draft A

- **Epistemic-status block** as the base. Its *Certainty* and *Importance* entries are the most precise ("bounded by 36 matched pairs, possible extraction errors, and no independent replication"; "a reason to examine both readouts, not a general theory of how the model decides").
- **Paragraph 1** (question → counts) essentially intact.
- **"There is an important restraint hidden in the title"** paragraph — the article's anchor. Keep "*Belief* means the posterior the model stated, not an internal state I can inspect" and "I want to keep that finding intact rather than strengthen it by quietly merging two sets of results."
- **The inline SVG** (Figure 1), with fixes noted in §6.
- **Figure 1 caption** language: "A different diagnostic choice is not necessarily an incorrect choice. Every terminal-answer difference changed correctness; the counts do not establish which presentation was better overall."
- **"Nor should the two counts be added"** sentence — neither the brief nor B raises non-additivity; it's a real reader trap.
- **"That does not tell us the model's total answer accuracy across all 72 presentations"** — the 72 figure makes the denominator concrete.
- **"This experiment records outputs; it does not locate a failure inside the computation."**
- **Extraction paragraph**: "An exact oracle tells us which answer is correct *if the recorded answer is what the model gave*."
- **Non-independence paragraph**: "Adding their denominators would manufacture a single experiment that was never run."
- **Proxy directional-count caveat**: "The seven paired changes count one reported direction, pass→fail; the packet does not provide a corresponding fail→pass count... Seven out of 76 is therefore not an estimated probability that a passing base case will fail under intervention."
- **Provenance paragraph**: the six-seeds-vs-single-seed contrast, and "'dirty' does not establish that a relevant file changed during execution."
- **"Start with the five flipped pairs, not a larger headline number"** and the blind-extraction-audit protocol.
- **Final paragraph** (from "The answer I can [d-word] now is narrow") as the raw material for §9.

### From Draft B

- **Section header** "The dissociation is between outputs, not modules."
- **"Zero posterior flips is not the same as zero posterior error. A model could report the same incorrect probability twice."**
- **The three-column endpoint table**, specifically the third column ("What the change establishes") — it does the interpretive work in-line.
- **The two-bullet contrast**: probe establishes posterior *invariance*; games establish posterior *accuracy*. Bold the two nouns as B does.
- **Proxy table** (Base / Visible proxy / Reward proxy with n and rate). Keep the n column prominent so 1/4 is visibly tiny.
- **"Sharing a latent specification is useful... But it does not, by itself, hold difficulty or every other relevant feature constant."**
- **"Calling it further evidence for one fragile 'decision layer' would make the narrative smoother by making the evidence less faithful."** — best closing line for the proxy section.
- **"If some do not, the result should be revised rather than defended through the oracle's exactness."**
- **"Observing one invariant output is not an audit of everything that produced it."**
- **56/132 ≈ 42%** with the explicit "These are cases, not 56 unverified groups" correction.
- **Closing-section architecture** ("A bounded answer" as a short titled coda).
- *Certainty* dd phrase "no confidence intervals" and "Proxy comparisons are not difficulty-matched" → graft into A's block.

---

## 5. Material to reject or reconstruct

### Draft A — reject/reconstruct

1. **"Consider what a single cell specifies. With four facts and a prior of 1/3..."** paragraph. This is a paragraph about *not* having an example. The refusal to fabricate is correct; the paragraph is dead weight. Compress to one sentence in §2 ("The aggregates do not say which cells the five flips fell in, and I won't invent one") or cut and surface the per-cell breakdown as a data request in §8.
2. **"My first impulse was to treat a changed answer as evidence that the model had read different facts."** The "read different facts" framing is murkier than B's "knew the answer but failed to use it." Replace with B's framing; keep A's rebuttal logic.
3. **"the verdict was correct in all 23"** — not in the verified packet summary (which says 23/23 exact posterior match). Verify against the raw packet or cut. Same for "Posterior error was zero in all 23" if "error" is a distinct field from "match".
4. **Stray glyph** "where it 👹" → "where it matters".
5. **Litany rhythm.** §"What a stable number does" and §"A separate observation" each run 5–7 consecutive sentences of the form "It does not... It cannot... It does not." Cut one in three; vary to positive statements of what *is* established.
6. **Figure 1 axis labels**: "36 pairs" placed at x=584 while bars end at x=635. Fix (see §6).
7. **No titled closing section.** The bounded answer is buried as the last paragraph of "The next test I would run." Give it B's header.
8. **"The reported model was mercury-2.5 with reasoning effort set to high."** Verify — not in packet summary. (Also appears in B.)

### Draft B — reject/reconstruct

1. **The broken image.** A bare `!` followed by an orphan "Figure 1. Campaign coverage..." caption. Either the markdown image collapsed or the SVG was never written. Replace with the new Figure 2 SVG (§6). Also: B's *only* figure is campaign coverage, not the headline result — wrong priority.
2. **Paragraph fragmentation.** The lede has six paragraphs under 40 words; "The dissociation..." section has nine. This reads as a slide deck. Merge to paragraphs of 3–5 sentences throughout.
3. **"nor does it mean that only one in seven changed answers was wrong."** This reintroduces the reviewer-flagged "one in seven" garble in negated form, and the negation is itself confusing (the proportion of *changed* answers that were wrong is exactly half, by construction). Reconstruct: "Roughly one pair in seven flipped. Within each flipped pair exactly one presentation was wrong — that follows from the oracle, not from a 14% error rate."
4. **"The differences are substantial in these observations."** Vague. Replace: "The raw gaps are large — 0.69 against 0.30 and 0.25 — and they are confounded."
5. **The "reporting lesson" paragraph** ("For this probe, I would preserve posterior invariance, terminal correctness reversals, and diagnostic-choice divergence as separate outcomes...") drifts into evaluation-methodology advice. Keep only the final two sentences ("This is not evidence that every evaluation needs the same structure. It is evidence that, here, the structure changes what we can see.") and move them to §9.
6. **Stray glyph** "The distinction 👹 because" → "The distinction matters because".
7. **"Keeping them separate is essential to understanding what the campaign [ac-word] tells us."** Cut (announces structure).
8. **Epistemic-status *Prose*: "AI-drafted from the archived evidence."** This is an author-policy decision, not mine to make — flag for StrangeTcy. If the house convention is to disclose drafting method, keep; otherwise A's "Written from verified aggregate results, without access to individual prompt-and-response transcripts" is more informative about *what limits the prose*.
9. **"Campaign-wide single-seed results do not establish run-to-run stability."** True but incomplete — it misses the stronger point that the 6-seed probe *also* lacks a same-presentation resampling baseline (see §8).

---

## 6. Figure placement and SVGs

**Figure 1 — Three endpoints (A's SVG), placed in §3 immediately after the design description and before the percentages.**
Fixes required:
- Move the "36 pairs" tick label so it right-aligns with bar end (x≈635, `text-anchor="end"`), or add tick marks at 0 and 36.
- Add a faint mid-tick at 18 (x=455) so 17/36 ≈ half is visually anchored.
- Change `<title>` from "Different outputs across two presentations of the same facts" to "Pairs with a changed output, by endpoint (n=36)" — the current title is a sentence, not a chart title.
- Keep `role="img"`, `aria-labelledby`, and the `<desc>`; these are correct and should be the accessibility template for Figure 2.
- Keep the caption text noted in §4.

**Figure 2 — Campaign denominators (new SVG), placed in §7 at the point where the judge-guarantee split is introduced.**
Design: two horizontal stacked bars of equal total width (416):
- Row 1 "Scoring status": 405 scored (subdivided 277 PASS / 128 FAIL) + 11 unscored.
- Row 2 "Judge guarantee": 189 behavioral_reference + 227 compile_only.
Both rows span the same 416 width. The visual argument is that the guarantee split partitions the *selected* set, not the *scored* set — which is exactly the reviewer's misattachment correction, made without a sentence of prose. Caption: "Two partitions of the same 416 selected cases. Judge guarantees (189 + 227) sum to 416, not to the 405 scored cases; the pooled pass fraction 0.684 is computed on 405."
Use A's SVG palette (`#dce5ec` / `#226b99` plus one more tone for the third segment) and the same `viewBox` width for visual consistency.

**Do not add a proxy pass-rate bar chart.** A bar for 1/4 next to 228/331 invites exactly the over-reading the text warns against. B's table with the n column is the right instrument. If a figure is insisted upon, it must plot counts (8 of 27, 1 of 4) as dot-and-denominator, not rates.

Optional B-derived table in §3 beneath Figure 1 — acceptable if the table and figure aren't redundant; I'd keep the table because its third column is interpretive, and drop the figure's redundancy by keeping the figure's caption short.

---

## 7. Technical examples and case selections

Both drafts correctly refuse to fabricate transcripts. The final article should:

- **Describe one pair structurally, not by content.** "A pair in the 3-fact, prior-1/2 cell presents the same three facts once as canonical bullets and once as a reversed numbered list, then asks for a posterior, a terminal answer, and which evidence to inspect or request next." This shows the reader the unit of analysis without inventing a fact set.
- **If transcripts for any of the five flipped pairs are retrievable before publication, pull one** — the raw canonical and reversed responses with the extracted answer highlighted — and present it as "one of the five," noting whether extraction held up under manual check. If not retrievable, say so in a single sentence and move the request to §8. Do *not* paraphrase a hypothetical.
- **Use 4-of-7 visible_proxy among pass→fail as the concrete proxy anchor**, with the explicit note that 4 is a count of tags among seven transitions, not a rate.
- **Use 189 + 227 = 416 as the worked denominator example** (and Figure 2). This is the single most concrete arithmetic correction from the brief and makes the "wrong denominator" error legible to a general reader.
- **Use 56 of 132 twin cases (≈42%)** as the coverage caveat example, with B's "cases, not groups" clarification.
- **Use the 72-presentations figure** (A) when stating that flip counts don't yield overall accuracy.

Do not use: any cell-specific flip attribution; any "0.00 to 1.00" range; any per-environment pass rate (the "38 environments" figure itself needs verification — see §9).

---

## 8. Weak sections, missing counterarguments, and gaps

**Missing from both drafts — must be added:**

1. **No sampling-noise null.** Six seeds per cell implies stochastic decoding. Neither draft asks: *what is the answer-flip rate between two runs of the same presentation?* Without a same-presentation resampling baseline, 5/36 cannot be attributed to the presentation swap rather than to decoding variance. This is the single largest hole in the argument, and it also cuts against the title's "fragile" — fragile *to what*? §8 must list "same-presentation resampling at matched seeds" as the first follow-up alongside the extraction audit, and §4 must concede that presentation sensitivity has not been separated from run-to-run variance. (A's "repeating across more seeds" gestures at this; B's "repeated runs" likewise; neither names the null.)
2. **Chance agreement for diagnostic choices.** 17/36 divergence means nothing without the size of the choice set. If there are eight inspectable items, two independent draws agree rarely; if two, they agree often. Add one sentence: the divergence rate is uninterpretable without the option-set size, which the packet does not report.
3. **Is posterior invariance a floor effect?** If the posterior is a small-integer-ratio computation with few distinct reachable values, 0/36 may be near-guaranteed by output granularity, while terminal answers and diagnostic choices live in larger spaces. Both drafts treat 0/36 as a striking stability; it may be a trivial one. Add as a caveat in §4.
4. **Is the terminal answer supposed to be a function of the posterior?** If the task defines the correct answer as a threshold on the posterior, the dissociation is sharp (same number, different threshold crossing). If the answer depends on other information, the dissociation is unsurprising. Neither draft states the task's answer rule. Either state it or flag that the packet doesn't.
5. **Per-cell distribution of the five flips.** Unknown. If all five sit in the 5-fact cells, the story is "long fact lists"; if spread, it's "presentation." Request in §8.
6. **Post-hoc selection.** Was T1 one of several probes, with 0/36 the one worth writing about? Neither draft addresses whether the probe was pre-specified. One sentence of disclosure or one sentence of uncertainty.

**Weak sections:**

- A §"What a stable number does": correct content, but the mechanism caveats and extraction caveat are interleaved. Separate into "identical reports ≠ identical computation" and "the recorded answer may not be the given answer."
- B §"How much weight": the broken figure and the "!" leave the judge-guarantee argument hanging — the prose says "require their own denominator" and then the evidence vanishes.
- Both §proxy: neither says plainly what the *base* denominator 331 is relative to 405 scored (331 base + 27 + 4 = 362 ≠ 405; the other 43 scored cases are presumably other intervention types). This gap *is* the "intervention taxonomy gap" from the brief; A names it abstractly, B names it as "no complete crosswalk." The final article should state the arithmetic: 331 + 27 + 4 = 362, leaving 43 scored cases in categories the packet does not break out.

---

## 9. Exact unsupported claims to remove or narrow

| Claim | Draft | Status | Action |
|---|---|---|---|
| "the verdict was correct in all 23" | A | Not in verified packet (only "23/23 exact posterior match") | Verify against raw packet; else cut |
| "Posterior error was zero in all 23 / throughout" | A, B | Redundant with exact match if "error" = |reported − true|; otherwise unverified | Keep only if a distinct field exists |
| "spanning base scenarios and evidence, presentation, and prior interventions" | A, B | Intervention types for the 23 games not in packet summary | Verify; else "across the tested scenarios" |
| "across 38 environments" | A, B | Not in packet summary | Verify; else cut (not load-bearing) |
| "mercury-2.5 with reasoning effort set to high" / "high reasoning effort" | A, B | Not in packet summary | Verify; else "one provider configuration" |
| "intervention cases sharing a latent specification with a base case" | A, B | Packet says "within 76 intervention cases"; latent-spec linkage not confirmed | Verify; else "76 intervention cases paired to base cases" |
| "nor does it mean that only one in seven changed answers was wrong" | B | Garbled restatement of flagged error | Reconstruct per §5 |
| "The differences are substantial" | B | Evaluative without support | Replace with the three rates |
| "Eleven were unscored" | A, B | 416 − 405 = 11, arithmetic ✓ | Keep |
| 5/36 ≈ 14%, 17/36 ≈ 47%, 56/132 ≈ 42%, 277/405 = 0.684 | both | ✓ | Keep |
| "pass rates from 0.00 to 1.00" | neither | Fabricated per brief | Confirm absent from final |
| Judge guarantees attached to 405 | neither | Both correctly attach to 416 | Confirm; reinforce with Figure 2 |
| "56 unverified twin groups" | neither | Both say "cases" | Confirm; keep B's explicit correction |
| Any sentence implying T1's 36 pairs are inside or outside the 405 scored | neither asserts | Unknown | Keep it unasserted, or verify and state |
| "Its choice of what evidence to inspect or request next" as the definition of diagnostic choice | both | Presumably from packet | Verify wording matches the probe's actual field |

---

## 10. House-style fit assessment

Assessed against the StrangeTcy Jekyll conventions visible in both drafts (YAML front matter, `icon-self` byline, `dl.epistemic-status`, inline SVG with `figcaption`, first-person essayistic voice, bracketed word-replacement tokens).

- **Draft A fits better.** Continuous paragraphs, inline accessible SVG, figure caption in house format, first-person deliberation ("My first impulse was…", "I would start with…"). Its weakness is rhythm (the "does not" litanies), not register.
- **Draft B is structurally house-compliant but tonally off.** The one-sentence-paragraph cadence reads as a product-update post, not an essay. The broken image is a hard style failure. Its two tables are fine in Jekyll markdown and should be kept.
- **Bracketed tokens** ([d-word], [ac-word]) appear in both and are intentional — retain as-is.
- **Stray glyph** 👹 in both — reviewer's tone flag. Replace with "[m-word]" in both locations.
- **Profanity**: none present in either draft. The reviewer's flag presumably refers to an earlier version; confirm the final contains none.
- **Epistemic-status block**: A's five entries are the template; graft B's "no confidence intervals" and "not difficulty-matched" into *Certainty*. Author to rule on "AI-drafted" disclosure in *Prose*.
- **Closing**: house pieces appear to end on a bounded, slightly open question rather than a lesson. B's "A bounded answer" header with A's final-paragraph content delivers this; B's "reporting lesson" paragraph does not and should be cut to its last two sentences.

---

## 11. Response-to-review table skeleton

| # | Objection (source) | Required change in final | Section |
|---|---|---|---|
| R1 | Stitching T1 and proxy into one "decision" narrative is not defensible (brief) | Proxy section opens with explicit refusal; retain B's "smoother by making the evidence less faithful" closer; no causal language linking proxy to flips | §6 |
| R2 | "Pass rates from 0.00 to 1.00" fabricated (brief) | Confirm absent; no per-environment rates anywhere | all |
| R3 | Judge guarantees misattached to 405 (brief) | State 189 + 227 = 416 in prose; Figure 2 shows both partitions of 416 | §7 |
| R4 | "Wrong in one in seven" garbled (brief) | Reconstruct: ~1 in 7 pairs flipped; each flipped pair has exactly one wrong presentation; not an error rate | §3 |
| R5 | "56 unverified twin groups" → "56 of 132 twin cases" (brief) | Use B's wording with explicit "cases, not groups" | §7 |
| R6 | Missing caveat: single seed (brief) | A's six-seeds-vs-single-seed contrast paragraph | §7 |
| R7 | Missing caveat: intervention taxonomy gap (brief) | State 331 + 27 + 4 = 362 of 405; 43 scored cases uncategorized in packet | §6 |
| R8 | Missing caveat: non-independence of T1 and games (brief) | A's "manufacture a single experiment that was never run" paragraph; B's invariance/accuracy bullets | §5 |
| R9 | Missing caveat: extraction brittleness (brief) | A's "if the recorded answer is what the model gave"; B's "revised rather than defended" | §4, §8 |
| R10 | Tone: profanity, stray glyph (brief) | Replace 👹 → "👹" (two sites); confirm no profanity | all |
| R11 | No sampling-noise null (new, this review) | Add same-presentation resampling as first follow-up; concede in §4 that presentation effect is not separated from decoding variance | §4, §8 |
| R12 | Diagnostic divergence uninterpretable without option-set size (new) | One sentence stating the dependency and that the packet lacks it | §3 |
| R13 | Posterior invariance may be a granularity floor effect (new) | One caveat sentence | §4 |
| R14 | Answer–posterior relationship in task undefined (new) | State the task's answer rule or flag that packet omits it | §2 |
| R15 | Unverified details: "verdict correct in all 23", "38 environments", "reasoning effort high", "latent specification", game intervention types (new) | Verify each against raw packet; cut or soften if unverifiable | §5, §6, §7 |
| R16 | Broken image in B (new) | Replace with Figure 2 SVG | §7 |
| R17 | Figure 1 axis label misaligned (new) | Right-align "36 pairs" to bar end; add mid-tick | §3 |
| R18 | Fabricated-example risk (A's non-example paragraph) (new) | Compress to one sentence; structural pair description only; real transcript if retrievable | §2, §7 |
| R19 | Per-cell flip distribution unknown (new) | Add to data requests | §8 |
| R20 | Pre-specification of T1 unknown (new) | One disclosure or uncertainty sentence | §2 or §7 |

---

**Bottom line for the writer of the final:** build on Draft A's skeleton and voice; import Draft B's two tables, its "outputs, not modules" header, its "zero flips ≠ zero error" couplet, and its titled coda; add the sampling-noise null and the 331+27+4 arithmetic that neither draft has; replace B's broken figure with a two-partition denominator SVG; verify the five unverified details in §9 before anything else goes to layout.
