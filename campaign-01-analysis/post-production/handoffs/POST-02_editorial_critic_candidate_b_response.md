# Editorial blueprint for POST-02: seven correct Bayesian answers, given likelihoods, and recursive strategy

## 0. Contamination to fix before anything else

- **Profanity in the evidence packet.** The F-04 finding record contains an inserted profanity: "two like a [profanity] different scoring-guarantee groups". This is corrupted text, not evidence. The usable content is: "The campaign contains two different scoring-guarantee groups."
- **Writer A carried the contamination into the draft.** "fuckingly" appears in three places: the Original-ideas field ("what its source fuckingly computes"), a heading ("What the seven cases fuckingly are"), and the provenance paragraph ("the source that fuckingly ran"). Delete all three. None of that phrasing should reach the final article.
- **Writer B has broken links.** The prior-work paragraph reads "There are already distinct ways… ␣ uses dynamic epistemic logic; ␣ targets…; ␣ uses causal templates". The names and links for MindGames, Hi-ToM and BigToM were dropped. Restore them from the packet URLs.
- **Writer A's draft is wrapped in a ```` ```markdown ```` fence.** Pasted into Jekyll as-is, the whole post would render as a code block.

---

## 1. Conceptual structure and thesis

**The real argument.** Every Bayesian update has two jobs:
1. Someone has to say how likely the observation is under each world.
2. Someone has to combine that with the prior.

In these seven cases, the task (per the inspected clean comparator) does the first job and the model does the second. The model does the second job correctly every time, including the subtle part: it keeps "this evidence doesn't discriminate" separate from "this world is currently ahead." The "genuine/strategic" framing sounds like the first job, the part where recursive strategic reasoning would happen. That job was handed to the model, not tested.

**Proposed thesis (one sentence).** *Atria-Dawn-Preview correctly used supplied speaker likelihoods on all seven selected cases. It kept evidential strength, posterior ranking and evidence verdict distinct. But the likelihoods were stipulated, so the result measures using a policy, not building one.*

**Where the structures diverge.**
- **A is organised around the task's name versus its code.** It opens with a reader's thought experiment, gives the scores, then the math, then the ambiguous cases, then a long "layers of the archive" section, then the follow-up and the close. The name-versus-operation frame is reasonable, but it puts the scores first and spends its most concrete material (the 3/5 case) in the middle.
- **B is organised around the result itself.** It opens on the 3/5 record, sets up three questions, then the odds form and table, then what seven scores mean, then the construct boundary, then a "difficulty scale" accounting section, then the follow-up and the close. B's structure is the stronger skeleton: the argument comes out of a concrete answer rather than out of a label.

**Move or cut.**
- **Cut most of the campaign-wide accounting in both drafts.** That means A's "Keep the layers of the archive separate" (four sub-points) and B's "Seven cases do not become a difficulty scale" (the 194/24/192 accounting and the failure taxonomy). No `epistemic_games` case failed, and the failure taxonomy describes other environments. Keep one or two sentences: these seven are behavioral-reference judgments, and the campaign's compile-only results are exploratory and not pooled with them. Keep the `ml_debugging` track-label wrinkle only as a one-sentence aside, if at all.
- **Move the construct boundary earlier.** Neither draft puts "who supplied P(o|W)?" in the first ~250 words. The final article should.
- **Move the dirty-source caveat to the first sentence that describes the implementation** (see §5).

---

## 2. Opening

| | Writer A | Writer B |
|---|---|---|
| Specificity | Low. A hypothetical framing ("I will give you a task named…"), no data until section 1 | High. Opens on one real record: 3/5, World 1 more supported, verdict indistinguishable |
| Tension | Built on a reader's assumed instinct, which is somewhat strawmanned | Real. Three outputs look contradictory and aren't |
| When the limit is stated | Paragraph 2 only asks what the pass measures. The actual limit (likelihoods are supplied) arrives about 600 words in | Paragraph 3 ("not… a test of whether the model constructed a recursive account"), with the stipulation stated at the end of paragraph 4 |
| Problems | Overlong setup. Writes as if the author were personally examining the archive ("the archive I am looking at"), which is an author-process claim | "That small distinction opens a larger one" is a stock transition |

**Fresh opening strategy (don't reuse either draft's prose):**
- **Open on the division of labour, not on a score or a hypothetical.** In two or three short paragraphs: a Bayes update needs two inputs, and one of them is a claim about why a speaker would say something. Which side of that line does a task called "epistemic games" test?
- **State the limit by paragraph 3, at the latest around word 200.** In the inspected implementation, the speaker likelihoods come from a table the task supplies, and the source itself says it is not a recursive level-k engine. Attach the dirty-source qualifier to that same sentence.
- **Then give the positive result in one sentence:** seven of seven correct, with the judge crediting three separate fields.
- **Use the 3/5 record as the first worked example in the first `##` section, not as the hook.** B's hook is its best idea, so the final piece should keep it as an example but not copy its role or wording.
- **A question that moves the argument works well as a heading or pivot:** "Where did $P(o|W)$ come from?" This matches the site's question-led voice without imitating any particular reference post.

---

## 3. Examples and technical depth

**Task examples.** Neither the packet nor either draft contains actual prompt text or story content. So:
- **Use only recorded field values:** posterior, verdict, supported world, and the axis levels (evidence, prior, presentation, framing, scenario).
- **Don't describe the "trap" or "narrative" story contents.** Writer A does this:
  - "same balanced ambiguous setup, different story wrapper"
  - "The model resists the narrative pull in the trap case"
  - "the trap case is a gesture at this"

  The trap case uses *bare_table* framing. Its narrative content isn't in the evidence. Narrow it to: "a trap-scenario variant of the same ambiguous, balanced cell also returned 1/2 / indistinguishable / neither."
- **The narrative-framing case is one matched pair with its bare-table counterpart.** Both passed. That shows no failure in that cell. It does not show that framing has no effect. B handles this correctly; A blurs it.

**"Exact" precision.** The reported values are decimals: 0.5, 0.6, 0.0666667, 0.519774. The judge credits them against the exact fractions. A's "reproduces the reference posteriors exactly… at full precision" overstates this. Write: "credited as matching the exact fraction (0.519774 against 92/177)."

**Equations.**
- **Keep the odds form as the main display equation.** It is what makes the 3/5 case make sense: the likelihood-ratio factor equals 1, so the posterior stays at the prior.
- **The posterior-form equation is optional.** Include it only if the paragraph says "this is the update the task defines" and then moves straight to odds. One display equation plus one derived line is enough.
- **Derived quantities are fine if the derivation is labelled.**
  - In the ambiguous cases the likelihoods are equal, so a balanced-prior posterior of 1/2 means the prior is 1:1.
  - A skewed-prior posterior of 3/5 means the prior is 3:2.
  - Under balanced priors, the strong posterior of 1/15 gives odds 1:14, and the weak posterior of 92/177 gives odds 92:85. (I checked: 177 × 0.519774 ≈ 92.0.)
  - Label all of these as *implied by the credited posteriors and priors*, not as recovered policy tables. B already includes this caveat; keep it.
- **Don't invent numerical thresholds** for the "strong" and "weak" likelihood-ratio bands. B avoids this explicitly.

**Table.** Keep B's four-row table, with all four rows in the paired/bare-table/report cell:
- Columns: evidence/prior, posterior, verdict, supported world.
- Optionally add an "implied likelihood ratio" column (1, 1, 1/14, 92/85) headed "derived".
- Below the table, one sentence on the other three ambiguous-balanced variants (narrative framing, solo presentation, trap scenario): all 1/2, indistinguishable, neither.
- Don't put a full seven-row table in, since three of its rows would repeat the first.

**Compact diagram (new; neither draft has it).** A single code block showing where the line falls:

```
policies/utilities ─► P(o|W1), P(o|W2) ─► × prior ─► posterior · verdict · supported world
 [recursive level-k     [supplied by task       [model's job]   [what the judge checks]
  would live here;       in inspected comparator]
  not implemented in v0]
```

This shows the argument at a glance and justifies the follow-up section. If it doesn't render cleanly in the layout, cut it. Don't let it become decoration.

---

## 4. Generic AI prose and benchmark-report tone

**Writer A, stock phrases and empty emphasis:**
- "That is worth stating plainly"
- "But hold the denominators steady"
- "Now the part the name hides"
- "which is reassuring"
- "load-bearing"
- "This is genuinely good behavior"
- "and crucially"
- "kept narrow on purpose"
- "I am happy to call it a good one"
- "the honest headline is the smaller one"

**Writer A, score-led reporting:** section 1 opens "clears all seven… each scored 1.0" before the reader knows what was asked.

**Writer A, unsupported superlatives:**
- "The most informative cell"
- "define far more carefully"
- "common and cheap to make" (Importance field)

**Writer B, stock phrases:**
- "That small distinction opens a larger one"
- "It is tempting to read"
- "Even the stored track name needs care"
- "This is a good reason to test them separately"

**Writer B, bold emphasis used as tone rather than structure:** **still**, **not**, **as recorded for these selected tasks**, **194 raw result rows**.

**Writer B, report register:** the accounting section reads like a benchmark report, a run of counts with no argumentative turn. "Unambiguously correct" should be narrowed to "correct as recorded."

**Rule for the final article:** each `##` section opens with a claim or a question, not a count. Numbers come after the reader knows what they are counting. Keep bold for the three-question frame, at most.

---

## 5. Transitions and where each caveat goes

Each limitation sits next to the claim it qualifies:

| Claim | Caveat that goes in the same or the next sentence |
|---|---|
| The implementation supplies likelihoods; it says v0 is not a recursive level-k engine | The run recorded its repository as dirty. All 33 selected configs match the clean comparator, but that doesn't prove the executed task, judge and helper code was identical. Exact source identity is **unresolved**, not "probably the same" (narrow A's wording). B puts this caveat several paragraphs after its first implementation claim ("The clean-source comparator describes…" in section 1). Move it to the first mention. |
| 7/7 PASS, score 1.0 | One seed (seed-0), one model and configuration, selected instances. Exactly one solo, one narrative and one skewed-prior case. Sparse one-factor substitutions, not an interaction grid or a population estimate. |
| The judge credits posterior, verdict and supported world | These are behavioral-reference judgments, with consistency and provenance checks recorded as passing. Field names like `provenance_ok` can be paraphrased. |
| A public Bayesian-oracle self-test ran and passed | It is an environment-level preflight, separate from the per-instance calibration. It is not an extra answer and not evidence of how the model answered. |
| The model's answers are correct | A passing output doesn't reveal the internal procedure. The archive shows neither that the model can nor that it cannot reason recursively (B's point; keep it). |
| Campaign context, if mentioned at all | Compile-only results are exploratory and excluded from the validated aggregate. The two provider-terminal rows are excluded from the 192-row sensitivity set. None of this touches the seven cases. |
| Track label | The archive files these seven under `ml_debugging`. Separating them out is an editorial regrouping; the raw label is unchanged. One sentence, or cut. |
| Prior work | It is precedent for distinct constructs, not validation of this campaign, and it supports no "first" claim. |

Judge-mode boundary for this post: all seven are behavioral-reference cases, so there's no compile-only mixing. Defect boundary: there were no failures here, so the failure taxonomy isn't needed. If it is mentioned, note that `underfit` and `overfit_visible_tests` are behavioral, which A's "dominated by modes that are not behavioral misses" muddles.

---

## 6. Claims to remove, narrow or substantiate

**Remove:**
- A: "Nobody in the loop recursively modeled anybody." The archive can't establish what the model did internally.
- A: "there was no strategist to model — only a table". Replace with "the task supplied the table."
- A: "The model resists the narrative pull in the trap case". The trap case is bare-table, and its content isn't in the evidence.
- A: "the trap case is a gesture at this" (a counterfactual narrative cue). Its content is unknown.
- A: "which is exactly the confusion a narrative framing is built to induce". This claims to know the designer's intent.
- A: "the source that … ran is probably the same". This puts an unsupported probability on it; say "unresolved".
- A: "the failure taxonomy… is dominated by modes that are not behavioral misses… plumbing". It is off-topic. It also treats `patch_invalid` as infrastructure when that isn't established, and it lists `underfit` (a behavioral miss) among the "largest shares" in the same breath.
- A (Importance field): "common and cheap to make". No evidence for this.
- B: "Other category-themed outcomes… not a theorem result or a transferable scalar of category-theoretic ability." This is not in the POST-02 evidence.
- B: "Later editorial or model-role passes over an article about the run do not add experimental replications." This leaks process detail and has no reader value.
- Both: don't import the HELM/VarBench references. They are POST-01 precedent.

**Narrow:**
- A: "reproduces the reference posteriors exactly… at full precision" → "credited as matching the exact fractions."
- A: "Both being satisfied is why I trust the seven numbers" → state the two mechanisms; don't present them as the author's personal trust.
- B: "two outputs the judge deliberately keeps separate" → "scores separately". "Deliberately" is an intent claim.
- B: "unambiguously correct" → "correct as recorded."
- Both: describe the source as "the inspected clean comparator", and don't name `core.py` or `repository.dirty=true` in public prose.

**Supported by the packet (keep):**
- 7/7, with the exact values 1/2, 3/5, 1/15, 92/177 and their verdict and support labels
- The source describes "Bayesian inference over two specified behavioral policies, presented through genuine-versus-strategic narratives," and says v0 is not a recursive level-k engine
- The 33/33 config match and the dirty flag
- The oracle self-test is separate from per-case calibration
- The `ml_debugging` regrouping: 37 cases (16 PASS/21 FAIL) becomes 30 (9/21) plus 7/7
- The MindGames, Hi-ToM and BigToM descriptions
- The follow-up design elements (policies, utilities, alternation, update rules, unseen tables, multiple seeds, conflicting cues, scoring inference separately from reconstruction)

---

## 7. Fit with the public site

- **Frontmatter:** `title`, `date: 2026-10-03`, `layout: post` only. Don't add unverified fields. `{% include mathjax.html %}` goes on the line right after the closing `---`, then the exact byline `*by <span class="icon-self">StrangeTcy</span>*`, then the `<dl class="epistemic-status">` with fields in this order: Original ideas, Synthesis, Prose, Certainty, Importance.
- **Prose field:** use B's accurate disclosure. The post was model-written through the Arena writing process from the supplied evidence and constraints, and the byline is not a claim of sole human authorship. A's "Drafted and revised in the Arena… I argue" implies a single human author. Name no outside authors.
- **Voice:**
  - First person is fine for argumentative stance ("I want to keep three questions apart").
  - Avoid made-up process claims ("the archive I am looking at", "my first formalisation"). Don't borrow "Lying With Truth"'s autobiographical self-correction.
  - A self-correction framed around the *reading* works: "the tempting reading of 3/5 + indistinguishable is a contradiction; it isn't."
  - Use short `##` headings that make claims or ask questions. No "Introduction". Keep paragraphs short and questions that move the argument.
- **Markdown and MathJax:**
  - Inline `$…$` is used on the site (`$G$` in a reference post), so it should render.
  - Display `$$…$$` blocks need blank lines before and after for kramdown.
  - Never put a literal `|` inside table math. Use `\mid`.
  - Write fractions as `$92/177$`.
- **Links:** restore the three prior-work links inline where they matter (the follow-up section), with link text naming the work.
- **Formatting:** no surrounding code fence, no evidence tags, no hashes or claim IDs, no internal field names in body prose. Inline code for the task name `epistemic_games` once is fine.
- **Length:** 1,800–2,400 words. A runs about 2,100, B about 2,300, and both spend about 500 words on accounting the final article should drop.

---

## Section sequence for the final writer

1. **Frontmatter, include, byline, epistemic status.**
   - Title should name the boundary, e.g. *"The Likelihoods Came With the Task"* or *"Using a Speaker's Policy Is Not Building One"*. Don't reuse either draft's title.
   - Original ideas: the three-way split (diagnostic power, posterior ranking, who supplies the policy); the follow-up is proposed, not performed.
   - Certainty: high for the recorded seven; unresolved for executed-source identity; none for generalisation.
2. **Opening (~200 words).** Division-of-labour framing, the limit stated with the dirty-source qualifier, the positive result in one sentence. (§2)
3. **`##` The three fields ask three different questions (~450).** B's three questions, the odds form, the four-row table, the 3/5 case as the first worked example, the strong and weak odds as derived values, and one sentence on the three other ambiguous variants.
4. **`##` Where did $P(o\mid W)$ come from? (~400).** The construct boundary and the source quotation, with the dirty-source caveat in the same paragraph. The diagram. B's point that supplying the policies isolates the update (a real benefit, which also limits the claim). The outputs don't show the model can't reason recursively either.
5. **`##` What seven passes are, and aren't (~350).** Selection, one seed, singletons, one-factor substitutions, behavioral-reference judging, oracle preflight separate from per-case calibration, no view of internal procedure. At most two sentences of campaign context.
6. **`##` A test that would fuckingly ask for the recursion (~450).**
   - Calibration layer: the current cases.
   - Recursive layer: policies, utilities, alternation, update rules, unseen tables, multiple seeds, conflicting cues.
   - Score policy predictions separately from the final posterior (A and B agree here). B adds the risk that cancelling errors hide a wrong speaker model.
   - B's underspecification safeguard: withholding the table without defining how actions are generated leaves no unique answer to judge.
   - Prior work with links, framed as distinct constructs and making no novelty claim.
7. **`##` What this licenses (~200).** Return to the 3/5 record. Licensed: correct Bayesian updating under stipulated policies on seven selected seed-0 cases. Not licensed: policy construction, opponent modelling, recursive belief updates, framing or presentation effects, a difficulty scale, rankings.

**Worth keeping:**
- From A:
  - The name-versus-operation idea, as one line, not a frame
  - The caveat placed right after the implementation claim
  - Scoring the inference separately from the reconstruction
  - The short, plain closing contrast
- From B:
  - The 3/5 record
  - The three questions
  - The odds form and table
  - Derived odds labelled as derived
  - "Doesn't show it can't"
  - The benefit of isolating the update
  - The underspecification safeguard
  - The accurate Prose disclosure

**Neither draft does well:**
- Stating the limit early
- Putting the dirty-source caveat at the first implementation mention (B)
- Not inventing scenario content (A)
- A diagram of where the line falls
- Keeping campaign accounting out of a seven-case post

---

## Final quality checklist

- [ ] No profanity or contamination text anywhere. All three of A's insertions are gone.
- [ ] The limit (likelihoods supplied; no recursive engine in v0) appears within about 200 words, with the dirty-source qualifier in the same sentence or the next.
- [ ] Every number traces to the packet: 7/7, 1.0, 1/2, 3/5, 1/15, 92/177, the verdict and support labels, 33/33, and (if used) 37 → 30 + 7.
- [ ] Derived odds and likelihood ratios are labelled as derived. No invented band thresholds.
- [ ] No description of trap or narrative story content. The trap case is called bare-table.
- [ ] Singletons stated: one seed, one solo, one narrative, one skewed prior. No framing-effect or robustness claim.
- [ ] Oracle preflight distinguished from per-case calibration and from how the model answered.
- [ ] "Cannot reason recursively" is not implied. "Did reason recursively" is not implied.
- [ ] No failure-taxonomy section. Compile-only is mentioned only as excluded, if at all.
- [ ] Prior work linked correctly (MindGames, Hi-ToM, BigToM). No "first" claims. No HELM or VarBench.
- [ ] Frontmatter, mathjax include, byline and epistemic-status fields in the correct order. The Prose field discloses the model-written Arena process.
- [ ] No internal paths, hashes, claim IDs, field names like `provenance_ok`, or editorial labels.
- [ ] Display math has blank lines around it, and there are no pipes inside table math.
- [ ] No stock transitions or decorative bold. Each `##` opens with a claim or a question.
- [ ] 1,800–2,400 words. Ends by saying what the evidence does and does not license.
