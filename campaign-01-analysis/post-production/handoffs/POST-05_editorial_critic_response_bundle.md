# POST-05 editorial critic response bundle

Compiler-assembled wrapper containing two separately labeled user-supplied critiques. The bodies are preserved verbatim; labels match the supplied text and are not independently verified. This bundle does not synthesize, rank, or select a critic.

## Critic response 1 — sonnet 4.6

# Editorial Blueprint — POST-05
## "Surface cues, hidden depth, and what the weird-machine sweep can't prove"

---

## 1. Conceptual Structure and Thesis

**What the real argument is.** The post has four load-bearing claims, all of which are supported by the packet, none of which require synthesis beyond the archive:

1. The regex surface contrast (easy surface → all three lengths pass; altered surface at shortest length → two length mismatches) is the sharpest local pattern in the track, and it is confounded by construction: the surface manipulation bundles a class-name change with, at the hard level, an added performance hint.
2. The five failures across 30 cells are not the same kind of failure. Two are source-validator rejections that never reached a behavioral test. Three are behavioral underfits. Collapsing them obscures exactly the diagnostic information the archive retains.
3. The 25/30 aggregate pools six distinct programs, six distinct judges, and six incommensurable "depth" parameters. It is accurate bookkeeping, not a calibrated score of hidden-depth competence.
4. One seed per cell, a dirty repository, and a comparator-only source audit mean the archive supports the observed response pattern; it does not support any causal attribution.

**Proposed thesis sentence (for the writer to recast in voice):** *One archived sweep shows a sharp regex contrast that looks like surface deception—and it is exactly confounded enough that you cannot tell whether it is.*

**What to move or cut:**

- Both drafts have a standalone prior-work section. Shrink to two inline sentences at the first citation of VarBench or HELM; the packet (F-17) explicitly limits novelty claims to LOW confidence, so no section heading should suggest the comparison is thorough.
- Writer A's dedicated "One seed, dirty tree, comparator only" section should dissolve into caveat placement beside the claims it qualifies (§§ on the regex contrast and the source audit), not stand alone as a methodological recitation.
- Writer B's "What 34 and 66 tell us" section contains mechanical speculation (+2 as boundary-padding, ~2× as duplication) that the author half-retracts. The retraction is correct; the speculation should be compressed to one sentence acknowledging the temptation and then giving the retraction. The archive records only the two lengths; the post should not tour candidate failure mechanisms the evidence cannot distinguish.
- The axis-placeholder finding (F-14, category-track scan) is adjacent benchmark QA, not direct evidence about the regex manipulation. Keep it to one sentence with the dirty-source caveat, placed in or near the source-audit section.

**Where the two structures diverge.** Writer A orders: track overview → regex → failure layers → design limits → prior work → better design → license statement. Writer B orders: hook → task family → regex table → two bundled changes → 34/66 → failure layers with tables → 25/30 critique → source audit → better design → license statement. Writer B's ordering better earns each move—the hook motivates the task family, which motivates the table, which motivates the confound analysis. Writer A's track-overview-first approach asks the reader to absorb the six-environment landscape before the payoff cell is shown. However, Writer B's 34/66 section is an unnecessary detour between the confound analysis and the failure-layer taxonomy. The recommended section order is: hook and specific contrast → what the surface label controls (confound) → failure-layer heterogeneity → 25/30 is not a unit → source audit and caveat → what a better experiment isolates → license statement.

---

## 2. Opening

**Writer A's opening.** "I keep returning to five cells." Specificity is high within two sentences (seed 0, Rule 110, 32/128/512, collapse). Tension arrives immediately. The limiting claim ("the question is not whether the model sees weird machines") appears in the second paragraph. Weakness: the reader does not yet know why Rule 110 in regex is interesting as a task design choice; the setup treats the strangeness as given.

**Writer B's opening.** "Suppose you rename a class and the model's regex stops preserving string length. What did you learn?" Tension is immediate and epistemological. Specificity is lower (no numbers yet). The limiting claim arrives more slowly (paragraph 3). Strength: frames the core problem as an interpretive one before showing any data, which is more intellectually honest about the order in which the question arises.

**Problems with both.** Writer A front-runs numbers before motivating why those numbers are puzzling. Writer B's "suppose" frame slightly generic compared to the site's existing openings, which tend to open with a pointed observation or a committed claim that is then complicated.

**Fresh opening strategy.** Open with the two integers as a puzzle and a refusal: the archive gives you the output lengths (34 and 66), the input length (32), and the judge note ("collapsed on length mismatch"), and those are nearly all the forensics you have. Do not start with the sweep or the track or the 25/30 count. Do not open with an abstract definition of weird machines. The post's governing question—*how much argument can two integers bear?*—should be live from the first sentence. The opening should then concede, in the same paragraph, that the answer is "less than they appear to," and that this is itself the finding worth stating carefully. This is consistent with the site's pattern of opening with a committed claim that the body then earns rather than reverses.

Do not copy either draft's prose. Do not open with "I keep returning to" or with "Suppose."

---

## 3. Examples and Technical Depth

**Regex five-cell table.** Writer B's table (surface, input length, verdict, score, judge note) is the most useful single element in either draft. Retain it. The exact judge notes—"length mismatch, in=32, out=34" and "in=32, out=66"—are verbatim archive records and should appear verbatim. The table earns its space because the argument depends on the reader seeing all five cells together.

**Failure-detail table.** Writer B's five-failure table (environment, condition, score, where it stopped) is useful for the failure-layer section. It can be slightly compressed: environment and failure layer are the essential columns; exact scores can move to inline prose. Keep it if it stays under five rows; it does here.

**CSS and SQL depth tables.** These two tables (CSS: 3/4/5 bits; SQL: 6/12/25 chain) are borderline. The non-monotone argument is clear in prose with the numbers inline. Recommended: convert to two short inline sentences with the scores embedded. "Under the easy surface, CSS scores partial, source-invalid, pass across 3, 4, and 5 bits—the middle row rejected for a disallowed import before any parity test." Tables are warranted when the reader needs to scan; here the argument is short enough that scanning a table adds friction.

**Environment summary table.** Writer B's per-environment pass-rate table (6 rows) is accurate bookkeeping but does not advance the argument more than a sentence would. Convert to prose: "Three environments—spreadsheet, CI graph, and template interpreter—pass every selected cell. SQL passes four of five, CSS and regex each pass three." This is cleaner for the site's airy-paragraph aesthetic.

**Mathematics.** No equations are warranted. Rule 110 does not need a transition-function formula; the post's argument is about output length, not about the automaton's state semantics. Do not include a Rule 110 truth table or state diagram—these would be decorative, and the packet does not use them.

**Task specification precision.** Both drafts correctly note that the regex judge checks four criteria including 15 seeded strings and length preservation. This should appear once, precisely, when the pass/fail verdicts are first cited, to bound what "pass" means. It is a genuine evidential boundary, not padding.

---

## 4. Generic AI Prose and Benchmark-Report Tone

**Remove from Writer B immediately:**

- Every instance of "fuckingly"—these are generation artifacts throughout Writer B and must all be excised before any editorial work proceeds.
- "I believed that for about one paragraph of the first draft"—author-process self-reference, prohibited by the blueprint constraint.
- "The underlying move isn't new" as a section-opening sentence—this is empty setup. Fold the prior-work context into a single sentence at the inline citation.

**Stock transitions and empty emphasis to cut or rework in both drafts:**

- "That contrast is sharp enough to feel like a finding" (Writer A)—the hedging works but "sharp enough to feel like" is slightly evasive. The contrast is a finding; the question is what kind. Say so.
- "These are heterogeneous code-repair outcomes. They do not form a theorem, a scalar difficulty scale, or evidence..." (Writer A)—correct but the triple negative list reads as a benchmark-report boilerplate disavowal. One direct sentence works better than three parallel negations.
- "None of the methodological worries are new" (Writer A)—correct per F-17 but the phrasing slightly dismisses the context-setting role of VarBench and HELM. The reference is useful; the framing should be "these design principles are established" not "I am not claiming novelty."
- "useful residue" (Writer A)—slightly precious; replace with a direct statement of what the archive supports.
- "Uneventful in this run" (Writer B, spreadsheet/CI/template)—colloquial and fine for voice, but make sure it is not the only characterization of three 5/5 environments; the all-pass result also belongs in the 25/30 critique section.

**Benchmark-report overload in both drafts:**

- Both drafts end with a bulleted license-statement structure ("does not establish… does not license…"). This is useful content but should arrive as prose paragraphs in the site voice, not as a formatted list. The site's reference posts end with argued conclusions, not tabulated disclaimers.

---

## 5. Transitions and Caveat Placement

**Dirty-source caveat (F-01):** Should appear twice: once when the source-comparator observations are introduced (the class-name / performance-hint finding), and once in the source-audit section. Do not give it a standalone section (Writer A's approach). Do not pepper it throughout every paragraph (Writer B's approach). The rule: place it exactly where a claim depends on it.

**One-seed caveat (F-06, F-10):** State once in the framing paragraph where the regex contrast is introduced. Reference it again—briefly—when the causal hypothesis is labeled speculative. Do not repeat it in every section.

**Comparator/dirty boundary:** Any observation drawn from the clean source (class-name differences, the performance hint, the axis-placeholder scan) must be introduced as "in the clean-source comparator" and must carry the dirty-repository qualifier at first use. Subsequent mentions in the same section do not need to repeat the qualifier.

**CSS source-invalid caveat:** Place it immediately when the CSS case is cited. "The middle cell fails source validation—a disallowed import of `re`—before any parity behavior is tested" must appear at the sentence where the CSS medium-depth zero score appears, not in a subsequent paragraph.

**SQL source-invalid caveat:** Same rule. The unterminated triple-quoted string error is a gate failure, not a behavioral failure. This must be stated at the first mention of the SQL zero score.

**Judge-mode caveat (behavioral_reference guarantee):** State once when 25/30 is first cited: "all 30 cases are graded by behavioral-reference judges; none are compile-only verdicts." This is a boundary condition on the aggregate count, not a general caveat.

**Provider/exclusion boundary:** From F-09, two provider-coded rows sit outside the broader campaign taxonomy denominator. This is relevant to the 192-case campaign-wide context (Writer B introduces it briefly) but is not relevant to the weird-machine track specifically, where all 30 cases are eligible and no provider-terminal rows appear. Do not introduce this in the weird-machine sections; if context requires citing the broader campaign failure taxonomy, one sentence with the denominator note is sufficient.

**Speculative hypothesis (F-18):** The hypothesis that class-name changes or the added hard-level hint mattered more than input length must be labeled speculative at the point of statement, not in a subsequent paragraph. Writer B does this correctly ("labelling it plainly as speculation"). Writer A does it correctly ("I am stating it as speculation, not as an inferred effect"). Either phrasing works; pick one and do not repeat the label.

---

## 6. Unsupported Claims and Claim Traceability

**Statements to remove or narrow:**

| Statement | Location | Problem | Action |
|---|---|---|---|
| "+2 looks like a boundary-padding slip" and "~2× looks like something duplicating or interleaving the string" | Writer B, "What 34 and 66 tell us" | The archive records only output lengths; no mechanism is in evidence. The author retracts these but the text still tours the speculation. | Cut the candidate mechanisms; keep only: "Both failures are behavioral misses of the same kind—the patch ran and violated a structural property the task requires." |
| "I believed that for about one paragraph of the first draft" | Writer B | Author-process claim, prohibited. | Remove. |
| "The measurement principle is not novel" / "None of the methodological worries are new" | Writer A | F-17 is explicitly LOW confidence for any exhaustive novelty conclusion. "Not novel" as a global claim overstates the prior-work check. | Replace with: "Dynamic variable perturbation and repeated sampling appear in VarBench; broad multi-scenario evaluation is HELM's central design rationale." Cite inline. Do not generalize to "all methodological worries." |
| "the absence of direct template references for certain advertised axes in the wider category track" | Both drafts (source audit section) | Supported by F-14 but must carry dirty-source qualifier and must be scoped to "the category track, not the weird-machine track." | Keep with both qualifiers. |
| Any claim that Rule 110 Turing-completeness is relevant to what the model did | Both drafts correctly avoid it; source draft mentions it only to negate it | Limitation 1 in the packet is explicit: one update step does not establish arbitrary iteration. | Retain the negation as stated. One sentence is sufficient. |
| "Several nominal controls with no direct template references in the clean comparator" (paraphrase of F-14) | Writer A | F-14's finding covers ten axes across nine category environments; specifying "several" is an undercount that may be read as softer than the evidence. | Use the packet's number: ten axes across nine environments, or cite the finding without a count if the count feels out of place. Do not say "several" when the evidence has a figure. |
| "The contribution here is narrower" (source draft) / "The useful contribution here is small and specific" (Writer B) | Both | Self-evaluation of novelty. F-17 supports this as a characterization but the phrasing risks the benchmark-report register. | Reframe as what the post shows, not what it contributes. |

**Boundaries the packet does not permit crossing:**

- Do not assert that any axis change caused any specific outcome. The archive supports the observed response pattern only.
- Do not assert that the dirty-repository flag invalidates the comparator observations; it qualifies them. The distinction matters.
- Do not assert that the CSS or SQL source-invalid failures are evidence of semantic inability. They are gate failures.
- Do not assert that the axis-placeholder finding (F-14) applies to the weird-machine track; the packet scopes it to the category track.

---

## 7. Public-Site Fit

**Jekyll frontmatter.**
Both drafts have correct `title`, `date: 2026-10-03`, and `layout: post`. No math is used in either draft, so `{% include mathjax.html %}` is correctly absent. Final writer: confirm no equation is introduced (none is warranted per §3), then omit the include. If a display formula is ever added, the include must appear immediately after the frontmatter block, before the byline.

**Byline.**
Both drafts use the exact required form: `*by <span class="icon-self">StrangeTcy</span>*`. Retain exactly.

**Epistemic-status block.**
Writer A's block is clean and accurate. Writer B's block is accurate on the five fields but the Prose field reads "A language model drafted this in an Arena writing pass, working from a compiled evidence packet"—this is an author-process statement with internal-process language ("Arena writing pass," "compiled evidence packet"). The house style says to "attribute the actual Arena writing process accurately; do not invent outside authors." The Prose field should describe how the post was made without reproducing internal workflow terminology. Model Writer A's Prose field instead: "First-person technical narrative written from the campaign evidence packet and style constraints." The order of the five fields (Original ideas → Synthesis → Prose → Certainty → Importance) is correct in both drafts.

**Voice check against reference excerpts.**
The reference posts open with a committed observation or a short pointed claim that creates immediate interpretive pressure. "Suppose you rename a class" (Writer B) is closer to the question-led "Suppose I want you to make the wrong decision" pattern of reference post 3, but is less committed. Writer A's "I keep returning to five cells" is concrete and specific in the site's manner. The blueprint's proposed opening (§2 above—open with the two integers as a puzzle and a refusal) fits the site's visible self-correction pattern ("The first formalisation was wrong") more tightly, because it admits the temptation to over-read before the body earns the more careful conclusion.

The ending of reference post 4 ("Lying With Truth") demonstrates that the site voice can sustain a tight conclusion that restates what the evidence *does* license in a single sharp sentence. Writer B's closing—"I'd just rather find out what produced them than write as if I already know"—fits the site voice well and earns its place. Writer A's closing—"a dirty tree plus one seed per cell is a pilot, not a proof"—is also strong. Either can anchor the final paragraph; the blueprint recommends ending on the evidential limit, not on the desire for better data.

**Link and Markdown details.**
Writer B links VarBench and HELM inline at first mention, which is correct site practice. Writer A names them without links; add links. The VarBench URL is `https://aclanthology.org/2024.findings-emnlp.946/` and the HELM URL is `https://arxiv.org/abs/2211.09110` per the references packet. Do not link these a second time.

Table use: see §3. Maximum two tables in the final article. The five-cell regex table is justified; a compact failure-layer table is optional. Environment summary and CSS/SQL depth comparisons should be prose.

**Word count.** Writer A runs approximately 1,650 words (short of the 1,800 floor). Writer B runs approximately 2,400 words (within range but dense). The recommended structure with one retained table and compressed prior-work section should land between 1,900 and 2,300 words without padding.

---

## Actionable Section-by-Section Sequence

**§1 — Opening (no heading).** Open with the two specific integers and the judge's length notes as a concrete puzzle. State immediately that the archive gives you those numbers, one seed, and a comparator; establish the interpretive constraint before showing the task family. Roughly 150 words.

**§2 — "The track is six programs, not one axis."** Introduce the six environments with their distinct judges and depth parameters. State 25/30 once, with the behavioral-reference qualifier, and immediately note it pools incommensurable units. Introduce the three all-pass environments in one sentence. Roughly 200 words.

**§3 — "The regex contrast."** Present the five-cell table. State the pattern directly (easy surface: all lengths pass; altered surface at shortest length: both fail with length mismatches). Cite the verbatim judge notes. Do not interpret yet. Roughly 150 words.

**§4 — "What the surface label controls."** Introduce the confound: class-name change plus, at hard, an added performance hint. State the speculative hypothesis (names or hint may have mattered more than length) with explicit speculation label. State one-seed limit. Place comparator/dirty qualifier here. Roughly 200 words.

**§5 — "Failure layers are not interchangeable."** Compact failure-layer table or tightly described prose covering the five failures: two regex underfits (behavioral, length mismatch), one CSS partial-credit underfit (behavioral), one CSS source-invalid (disallowed import, pre-behavioral), one SQL source-invalid (syntax error, pre-behavioral). State explicitly that source-invalid failures are not evidence of semantic inability. Roughly 200 words.

**§6 — "25/30 is accurate bookkeeping."** Argue why the aggregate is not a capability score: different programs, different judges, incommensurable depth parameters. Cite HELM and VarBench inline here (one sentence each). Note that easy/medium/hard are not a common calibrated scale. Roughly 200 words.

**§7 — "The source audit adds one specific thing."** State the name-plus-hint bundling finding from the comparator. Note the axis-placeholder finding for the category track in one sentence with the dirty-source qualifier. Be explicit that the audit shows what the comparator contains, not what the paid run executed. Roughly 150 words.

**§8 — "A separation would look different."** State the four-step design required to isolate surface from size: split the bundled manipulation; replicate cells with multiple seeds; diff rendered artifacts before model sees them; score patch creation, source validity, and behavioral correctness as distinct outcomes. Do not make this section a numbered list if the site voice is flowing better in prose by this point. Roughly 200 words.

**§9 — "What the evidence licenses" (no formatted list).** Restate the local claim in one or two sentences. Name what the archive does not support (causal attribution, general capability score, Turing-completeness inference, difficulty ranking). End on the evidential limit in site voice. Roughly 150 words.

---

## Elements Worth Retaining from Each Draft

**From Writer A:**
- The epistemic-status block (clean, accurate, correct field order). Adapt Prose field per §7 note.
- The failure-layer analysis logic: "a source-invalid or runtime failure is a different kind of miss from an underfit that reaches the judge." The concept is from the packet; Writer A's prose articulation is precise.
- The better-design paragraph's four-factor separation (fix name/vary hint; vary name/fix hint; multiple seeds; diff artifacts). This is more structured than Writer B's version.
- "A dirty tree plus one seed per cell is a pilot, not a proof" as a possible closing line.

**From Writer B:**
- The five-cell regex table (exact scores, judge notes, format). It is the clearest single element in either draft.
- The title "Thirty-Four Characters Out of Thirty-Two." It commits to the specific evidence and cues the post's epistemological constraint.
- The argumentative section heading "Why 25/30 isn't a number about anything in particular"—or its spirit. Strong.
- The observation that the CSS and SQL non-monotone rows have their middle failures at the gate, not at behavioral test—and that plotting these on a "depth curve" would bury the distinction. This is sharp and source-grounded.
- "I'd just rather find out what produced them than write as if I already know" as a candidate closing beat.
- The inline failure-detail table (five rows), compressed to the essential columns.

---

## Elements Neither Draft Handles Well

1. **The CSS surface sweep.** The axis table shows that at depth=easy, the CSS surface sweep is fail/pass/pass (easy/medium/hard). This is the opposite directional pattern from regex. Both drafts mention it; neither makes it analytically useful. The blueprint recommendation is to cite it once as evidence that surface-level patterns are not consistent across environments, then leave it. Do not speculate about a mechanism.

2. **The "behavioral_reference guarantee" as an actual constraint.** Both drafts mention it but neither explains what it means for what we can say: the guarantee means all 30 cells were run against a behavioral judge, not that the judge is correct or complete. One sentence explaining the judge's specific criteria (length preservation + 15 seeded strings for regex) would bound the pass more precisely.

3. **The transition from the description of failure modes to the implication for the 25/30 count.** Both drafts treat "failure layers" and "25/30 is not a unit" as adjacent but separate sections. The more natural structure is: the failure-layer heterogeneity is *one of the reasons* the aggregate is hard to interpret—not an independent observation. The section flow should make this connection explicit.

---

## Evidence Boundaries

The final writer must not:
- Cite a mechanism for the 34/66 outputs (none is in the archive).
- Assert exact paid-run source identity (dirty flag, comparator-only).
- Claim novelty beyond the local pattern and comparator audit (F-17: LOW).
- Assign a cause to any specific failure (F-06, F-18: LOW or SPECULATIVE).
- Extend the axis-placeholder finding to the weird-machine track (F-14 scopes it to category tasks).
- Suggest Rule 110 Turing-completeness is relevant to what the task measures (Limitation 1).
- Present source-invalid failures as behavioral evidence (F-09, Limitation 6).

The final writer may:
- State 25/30 with the behavioral-reference qualifier (F-10: HIGH confidence for observed outcomes).
- State the regex 3/5 pattern with exact scores and judge notes (F-10, F-06: HIGH confidence).
- State the confound (class-name + performance hint bundled) with the comparator qualifier (F-18, F-03: supported with dirty-source caveat).
- State the speculative hypothesis as speculation (F-18: SPECULATIVE, explicitly labeled).
- State that CSS and SQL source-invalid failures are gate failures, not behavioral evidence (F-09: HIGH for terminal labels).
- State the dirty-repository flag and its implication for source identity (F-01: HIGH).

---

## Final Quality Checklist

Before the article is published, confirm:

- [ ] No instance of "fuckingly" (Writer B artifact, all must be removed).
- [ ] No author-process language in the epistemic-status Prose field.
- [ ] Dirty-source caveat appears at each comparator observation, not as a standalone section.
- [ ] One-seed caveat placed beside the regex contrast and the causal hypothesis only.
- [ ] CSS and SQL source-invalid failures described as gate failures, not semantic failures, at point of first citation.
- [ ] 25/30 cited with behavioral-reference qualifier and incommensurability note in same paragraph.
- [ ] Speculative hypothesis explicitly labeled speculative at point of statement.
- [ ] No mechanical diagnosis of the 34/66 outputs.
- [ ] No general novelty claim; prior-work references inline with correct URLs.
- [ ] No Rule 110 Turing-completeness inference.
- [ ] No axis-placeholder finding (F-14) attributed to the weird-machine track.
- [ ] Tables reduced to two maximum (five-cell regex table required; failure-layer table optional).
- [ ] No `{% include mathjax.html %}` unless a display formula is introduced (none should be).
- [ ] Byline exact: `*by <span class="icon-self">StrangeTcy</span>*`.
- [ ] Epistemic-status fields in order: Original ideas, Synthesis, Prose, Certainty, Importance.
- [ ] Word count 1,800–2,300 without padding.
- [ ] Closing paragraph ends on the evidential limit, in site voice, not as a bulleted disclaimer list.
- [ ] VarBench and HELM linked inline at first mention only.

## Critic response 2 — opus 4.7

# Editorial blueprint — POST-05

## 1. Conceptual structure and thesis

**The real argument** (which both drafts gesture at but neither fully centers): A one-seed sweep produced a visually sharp contrast — length invariance under one surface label, length-mismatched failures under two others at the shortest length — but the manipulation bundles at least two factors (class name + hard-level hint), the five failures occur at *different stages of the pipeline* (behavioral vs. source-validator), and the aggregate 25/30 is a bookkeeping total over six incomparable programs. The piece is about why that archive *cannot* answer the question it looks like it answers, and what a design that could would need.

**Structural divergence:**
- **A** moves linearly from aggregate (25/30) → regex contrast → failure layers → design caveats → prior work → cleaner experiment → what the evidence licenses. It is tight but withholds the regex table and never shows the reader the 34/66 numbers in their visual context until near the end.
- **B** opens question-first, uses two tables early (regex 5-cell grid; failure stratification), and does the layer-separation argument *before* the aggregate critique. This ordering is stronger: the reader sees the shape of the data before being told what to make of it.

**Recommended shape for the final piece:**
1. Open on the two integers (34, 66) or on the renamed-class puzzle — concrete, not aggregate.
2. Lay out the task family and the 5-cell-per-environment design so the reader knows what "25/30" is made of.
3. Show the regex table and admit the confound in the *same* section.
4. Separate behavioral miss from source-invalid before pooling anything.
5. Explain why 25/30 is bookkeeping, not measurement.
6. State the comparator-vs-dirty-tree boundary explicitly, once, where it bites.
7. Describe the cleaner experiment.
8. Close with a precise license statement.

**Cut from source draft / A:**
- The "weird-machine benchmark asks whether a model can infer…" opener (abstract definition before specifics).
- The paragraph that reintroduces the regex contrast *after* the aggregate — avoid two passes at the same material.
- A's "What the measurement tradition already knew" is slightly defensive; fold the HELM/VarBench reference into the aggregate-critique section as context, not a standalone turn.

**Move:**
- Failure-layer separation (currently buried in A, well-placed in B) should sit immediately after the regex table so the reader learns early that FAIL ≠ FAIL.

## 2. Opening

**Comparison:**
- Source draft opens with abstract definition. Low tension, high setup cost.
- **A** opens on "I keep returning to five cells" — specific, first-person, states the puzzle in two sentences. Good tension, limit stated by paragraph two.
- **B** opens with a conditional: "Suppose you rename a class and the model's regex stops preserving string length." This is the style-reference register (question-led, cf. "Suppose I want you to make the wrong decision"). Fastest to tension and to limit.

**Fresh opening strategy (do not copy either):** Open on the asymmetry a reader can hold in their head *before* any framing — a concrete scene of three passing lengths and two failing renamed cells, stated as what-happened, followed immediately by the limit: single seed, dirty repo, comparator-only. The opener should name what the post refuses to claim (a general weird-machine detector, a surface-beats-depth law) before it discusses what it does claim. Do not define "weird machine" in the opener; let the examples do the definitional work.

## 3. Examples and technical depth

**Keep (exact, source-grounded, useful):**
- Regex table (B's five-row table). This is the central exhibit; it must appear.
- Explicit numbers: 32/128/512 input lengths; outputs 34 and 66 at input 32; CSS 0.416667 / 0 / 1.0 at 3/4/5 bits; SQL passes at chain 6 and 25, source-invalid at 12; CSS validator rejected `import re`; SQL unterminated triple-quoted string.
- Per-environment pass counts (B's second summary table: CI 5/5, spreadsheet 5/5, template 5/5, SQL 4/5, CSS 3/5, regex 3/5).
- Failure stratification table (B's "three layers" table). Useful because it visually enforces the behavioral/source-invalid distinction.

**Cut / avoid:**
- Equations: none needed. Rule 110 is referenced, not derived. Do **not** introduce an equation; it would be decorative here. (The style reference uses math only when the formalism itself is the subject.)
- Diagrams: not needed. The two tables carry the argument. A pipeline-stage diagram would be decorative given the small failure count.
- Do not add a `{% include mathjax.html %}` block — there is no math in this post.

**Judge criteria depth:** State once that the regex judge checks length preservation plus 15 seeded strings (four criteria total). That's the right level of detail; do not elaborate beyond it.

**Rule 110 handling:** B's half-paragraph on "Rule 110 is Turing complete when iterated; this task asks for one update" is exactly right and should be retained in substance. A mentions it only glancingly.

## 4. Generic AI prose and benchmark-report tone

**Issues to eliminate:**
- "That contrast is sharp enough to feel like a finding" (A) is good — keep that register but do not multiply it.
- A has mild score-led tone in the "The track is six programs, not one depth axis" opening sentences; prefer B's question-first framing of the same material.
- Avoid stock transitions: "Furthermore," "Importantly," "It is worth noting." Neither draft overuses these; keep that discipline.
- Avoid empty superlatives: "sharp," "clean," "cleanest" are used sparingly in both — fine, but do not let them stack.
- **Both drafts contain the literal token "fuckingly"** in multiple places (A: once; B: three times). This is a sanitized remnant of findings-text expletives in the evidence packet. Strip it everywhere. The findings text itself used it as emphasis; it must not appear in public prose.
- Do not report 0.8333333333333334 as a percentage with that precision; "25 of 30" is the readable form. Avoid "83.3%" framing because the pooled rate is specifically what the post argues against.
- Avoid "the model passed/failed" when "the recorded cell passed/failed" would be more honest — this is a running tone issue in benchmark writing. Both drafts mostly handle it; keep the discipline.

## 5. Transitions and caveat placement

Each limitation must sit beside its claim:

- **Dirty-source / comparator caveat**: attach it specifically to the sentence that says the surface levels differ in class names *and* the hard prompt adds a performance hint. Do not relegate it to a late methodology paragraph.
- **Judge-mode / defect**: when stating 25/30, immediately note that all 30 are behavioral_reference-judged (so the number is not inflated by compile-only). This is a *supportive* caveat and must not be omitted even though it strengthens the number — the point is that even clean grading does not make the count a capability measure.
- **One-seed boundary**: attach to any sentence that could be read as an effect estimate. Especially the regex contrast and the "non-monotone" CSS/SQL rows.
- **Provider/exclusion**: the weird-machine track has no excluded rows and no provider-terminal rows. State this once, briefly, when introducing the 30-case denominator. Do not import the broader 192/61 taxonomy except as a one-sentence scale check — B uses it well; A omits it.
- **Speculative hypothesis**: the name-or-hint-mattered-more-than-length claim must stay explicitly flagged as speculation (both drafts handle this; keep B's plainer "I'm labelling it plainly as speculation" register).

**Specific placement fixes:**
- Do not let the comparator caveat and the dirty-tree caveat drift into separate paragraphs; they are one point and should be stated once, where it bites hardest (the moment the "class name + hint" bundle is named).
- The "clean comparator shows X about the category track" aside (ten no-reference axes) should be brief and clearly marked as *adjacent* evidence — B handles this well; A buries it.

## 6. Unsupported claims and claim traceability

**Statements to remove or narrow:**
- Any phrasing that treats the regex failures as caused by surface deception. The data support a response pattern, not a cause.
- Any framing of the aggregate 25/30 that reads as a capability number. Both drafts avoid this; the final must as well.
- "Length invariance" as a property of the model: narrow to "three passes at three lengths under one surface label, which is not an invariance estimate."
- "The model represented a weird machine": do not assert; the judge saw length + 15 seeded strings.
- Do not claim Turing completeness, arbitrary iteration, or general regex correctness were demonstrated.
- Do not describe the clean-source observations as facts about the paid run.
- Do not claim novelty against HELM/VarBench. Cite them for context only; the targeted prior-work check supports no "first" or exhaustive-novelty claim.

**Substantiate:**
- Every table number must trace to the evidence packet exactly. Allowed numeric vocabulary includes: 30, 25, 5, 3, 4, 32, 34, 66, 128, 512, 6, 12, 25, 0.416667, 0.208333, 0.0, 1.0, 15, 110, 33, 42, 192, 61, 10, 9. Do not round 0.416667 or 0.208333 in table cells.
- When citing HELM "42 scenarios" and VarBench "five seeds," keep those exact figures from the references.

**Do not invent:**
- Mechanistic stories for +2 or ~2× length (B wisely refuses this; A doesn't attempt it — keep the refusal).
- Any seed count other than 1 per cell.
- Any claim about what the paid-run source actually contained beyond what the comparator shows.
- Any author identity beyond the stated byline and the honest "written in an Arena pass from a compiled evidence packet" framing. Do not invent collaborators or external reviewers.

## 7. Public-site fit

**Jekyll frontmatter:**
- `title:` — avoid colons unless quoted; B wisely quotes "Thirty-Four Characters Out of Thirty-Two." Pick a title that is specific and non-grandiose; both A and B are acceptable models. Avoid "weird machine" in the headline since the post argues against treating it as measured.
- `date: 2026-10-03` (exact).
- `layout: post`.
- **No** `{% include mathjax.html %}` — no math in this post.

**Byline and epistemic status:**
- Exact byline: `*by <span class="icon-self">StrangeTcy</span>*`.
- `<dl class="epistemic-status">` with the five dt/dd pairs in order: Original ideas, Synthesis, Prose, Certainty, Importance. B's content is better calibrated (explicit "modest," "low for any causal reading," honest Arena-pass note). A's is adequate but slightly over-polished.
- Prose field: honestly describe the Arena writing pass from the compiled evidence packet; do not invent an author process beyond that; do not copy author-process claims from the style reference posts.

**Voice fit against StrangeTcy excerpts:**
- The style reference favors: short declarative openers that set a scene, visible self-correction, questions that move the argument, airy paragraphs, first-person.
- B is closer to the reference register ("I believed that for about one paragraph of the first draft" is pure style-reference voice; cf. "The first formalisation was wrong").
- A is more measured but slightly closer to benchmark-report register in its middle sections.
- The final piece should allow at least one visible self-correction moment and at least one question that genuinely moves the argument, not a rhetorical one.

**Links/Markdown:**
- Cite HELM and VarBench inline where they're mentioned (B does this correctly). Links go where they matter, not in a bibliography block.
- Tables use standard Markdown pipes; both drafts' table syntax is fine.
- Do not include editorial markers, evidence IDs, finding IDs, SHA hashes, or claim IDs in public prose.
- Do not include an "Editor's note" footer referencing internal CSVs (source draft does this; strip it).

**Layout mismatches to avoid:**
- No `## Introduction` heading. Open in prose.
- Keep headings short, argumentative turns (`## The regex contrast is real and confounded` works; `## Background` does not).
- Target 1,800–2,800 words. A ≈ 1,500 (short); B ≈ 2,400 (within range). Final should land ~2,000–2,400.

## A/B elements worth retaining

**From A:**
- The disciplined "What the evidence licenses" closing register — a bulletless, prose statement of what is and is not supported. Use this *as* the closing section's spine, but keep B's enumerated "licenses / does not license" lists for scannability.
- The crisp "I keep the layers distinct on purpose" principle statement about not collapsing failure types.
- The one-sentence framing that comparator findings are not paid-run identity.

**From B:**
- The question-led opener style (not the exact words).
- Both tables (regex 5-cell; failure stratification by layer) — these are the piece's most informative artifacts.
- The explicit per-environment pass table.
- The honest refusal to invent a mechanism for 34 and 66.
- The one-paragraph aside on the broader 192/61 taxonomy for scale, with the "overfit_visible_tests" mislabel noted briefly.
- The "experiment I'd want" numbered list — cleaner than A's prose version.
- The Rule 110 / Turing-completeness disclaimer paragraph.

## Elements neither draft handles well

- **Why the depth axes aren't commensurable as units of work.** Both state it; neither gives the reader a one-line intuition. A single sentence like "a 512-character string is not twice the computational demand of a 25-node chain" would land it.
- **The judge's four criteria for regex** are mentioned (15 seeded strings + length) but the full count of four criteria is underused; stating "the judge checks four things, and three passes mean those four held on seed 0" would sharpen the "local" claim.
- **The CSS surface sweep at 3 bits (fail/pass/pass) runs opposite to the regex surface sweep.** B notes this; A doesn't. Final piece should give it one sentence as a check against overgeneralization *from the regex contrast itself*.
- **The adjacent category-track axis-placeholder audit** is mentioned by both but the connection to the regex finding (same class of problem: labels promise manipulations that artifacts may not deliver) is explicit only in B. Keep B's framing.
- **Explicit statement that no compile-only cases exist in this track** — A has it, B does not. Include it; it defuses a plausible reader objection.

## Exact evidence boundaries

**In-bounds:**
- All numbers in the allowed-numbers list, used in their exact packet context.
- The dirty-repository flag.
- 33/33 config-hash match with the clean comparator (as comparator-level evidence, not run-identity proof).
- The regex judge criteria (four, including 15 seeded strings and length preservation).
- Failure modes exactly as labeled: underfit, source_invalid.
- HELM: 42 scenarios. VarBench: dynamic variable perturbation, five seeds for variable-based experiments.
- Broader campaign: 61 fails of 192 eligible; the two mislabeled overfit_visible_tests cases.

**Out-of-bounds:**
- Any seed count > 1.
- Any causal attribution for the two regex failures.
- Any claim about paid-run source identity beyond "comparator shows X."
- Any Turing-completeness / arbitrary-iteration claim.
- Any novelty claim against prior work.
- Any mechanism for +2 or +34 output-length discrepancies.
- Any inference about model capability from the aggregate 25/30.

## Final quality checklist

- [ ] Frontmatter: title, `date: 2026-10-03`, `layout: post`. No mathjax include.
- [ ] Exact byline present; epistemic-status `<dl>` with five fields in order.
- [ ] Opens in prose (no `## Introduction`); limit stated within first two paragraphs.
- [ ] Regex 5-cell table present with exact scores 1.0, 0.208333 and the length-mismatch notes.
- [ ] Failure-layer stratification table present; behavioral vs. source-invalid distinction visible before any pooling.
- [ ] Per-environment pass table present.
- [ ] Comparator / dirty-repository caveat placed at the moment the name+hint bundle is first named.
- [ ] One-seed caveat placed beside the regex contrast and beside any non-monotone pattern.
- [ ] Behavioral-reference judge-mode noted when the 25/30 is first stated.
- [ ] No-exclusions / no-provider-terminal note included once for this track.
- [ ] Rule 110 single-update vs. Turing-completeness disclaimer present.
- [ ] Speculative hypothesis (name-or-hint > length) explicitly marked speculative.
- [ ] HELM (42 scenarios) and VarBench (five seeds) cited as context only, with inline links; no novelty claim.
- [ ] Category-track axis-placeholder audit (10 axes / 9 environments) mentioned briefly as adjacent, with dirty-repo caveat.
- [ ] Visible self-correction moment present at least once.
- [ ] "What the evidence licenses / does not license" closing with explicit lists.
- [ ] Word count 1,800–2,800.
- [ ] No "fuckingly," no evidence IDs, no SHA hashes, no claim IDs, no "Editor's note" with internal file references.
- [ ] No equation, no `{% include mathjax.html %}`.
- [ ] All numerics drawn from the allowed vocabulary and used in packet context.
- [ ] No invented authors, no invented reviewers, no author-process claims copied from style-reference posts.
