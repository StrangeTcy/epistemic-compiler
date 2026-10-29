claude fable 5.1:
# Mercury POST-02 — editorial critic blueprint, v3 (internal review and handoff)

Status of this document: internal editorial report and claim-check handoff. It does not choose a prose winner, merge the drafts, write the article, dispatch a stage, publish anything, or assert that the claim killer, final writer, local validator, or human review has passed. Candidate labels `gpt 6 luna max` and `opus 5` are used here for attribution only and must not enter the public article.

---

## 1. State and evidence-review disposition

### 1.1 Inputs received and read (through the final END marker)

| Block | Read | Notes |
|---|---|---|
| Governing instructions (POST-02 critic blueprint v3) | Yes | Contract, boundaries, exclusions |
| `WRITER_PAIR` — `gpt 6 luna max`, `opus 5` | Yes, complete | Verbatim order preserved |
| `COMPLETE_EVIDENCE_PACKET` — Tables A (38), B (416), C (80), D (340), Section E | Yes, complete | Section E is the only figure description available |
| `COMPLETE_DIFFICULTY_MATRIX_CSV` (340 rows with `difficulty_tuple`) | Yes, complete | Supplies the tuple keys the drafts call absent |
| `CAMPAIGN_PROVENANCE` | Yes | Source of "24 known gate-blocked", dirty=true, "1 retry, 60s" |
| `EARLIER_ANALYSIS_OVERVIEW` | Yes | Source of "10 environments at 0.00" and "~12 at 1.00" |
| `INELIGIBLE_PASS_CSV_EXCERPT` (row 409) | Yes | `exclusion_reason`, `performance_eligible=False`, attempt/time fields |
| `CURRENT_INTERNAL_ARTICLE` | Yes, complete | Already carries four figures and the env-by-label/guarantee tables; introduces new boundary errors (§6) |
| `HOUSE_STYLE`, `ACTUAL_REFERENCE_POST_EXCERPTS` | Yes | Voice/structure guidance only; historical attribution/process text not imported |
| `PRIOR_WORK_REFERENCES` (Campaign 01) | Yes | Not campaign evidence; links unverified here |
| `SUPPORTING_LOCAL_SOURCE_CHECK` (.md) and companion `.json` | Yes, both supplied | Attributed as local verification, not an Arena verdict |
| `CURRENT_V3_EVIDENCE_REVIEW_PAIR` — `grok 4.5`, `claude fable 5.1` | Yes, complete | Both rated "Both are bad" by orchestration; findings rechecked row by row below |
| `ORCHESTRATION_CAPTURE_NOTE` | Yes | Clipboard Markdown not claimed; DOM archived locally |
| Supporting reconciliation note (R1–R4) | Yes | Checked against supplied rows; all four findings reproduce |

Not supplied / not readable here: the SVG files themselves (captions below are checked against Section E text only, not a rendering); the earlier claim-killer/redactor handoffs (described as obsolete; their Figure 2 and bracket-removal instructions do not apply); the standalone `environment_summary.csv` (the local check derived environment totals from the matrix; Packet Table A supplies them and agrees); the exact dirty working-tree state; any public copy of the pinned commit.

### 1.2 Mode and external access

- Arena Web Search mode: required enabled for this stage. The setting is not observable from this document; orchestration must record the observed value. An enabled mode is not evidence that any source was read.
- External sources accessed by this stage: none. Every claim below rests on the supplied blocks.
- Both reviewers assert web access (Inception/Baseten/BusinessWire pages, repository landing page). Per the capture note, those access claims are recorded as asserted, not independently established, and none of them touches campaign numbers.

### 1.3 Recorded review verdicts (as stated by the reviewers)

| Reviewer | `gpt 6 luna max` | `opus 5` |
|---|---|---|
| `grok 4.5` | accept with corrections — 0 blocking, 2 corrections, 7 notes | accept with corrections — 0 blocking, 3 corrections, 6 notes |
| `claude fable 5.1` | accept with corrections — 1 blocking, 7 corrections, 1 note | accept with corrections — 2 blocking, 7 corrections, 1 note |
| Orchestration rating | "Both are bad" (substantive review defects) | "Both are bad" |

These verdicts are not acceptance of either candidate and are not carried forward as such.

### 1.4 Reviewer disagreements and reviewer errors (rechecked against rows)

| Point | `grok 4.5` | `claude fable 5.1` | Row check | Disposition |
|---|---|---|---|---|
| `moco` tuple keys "absent" | correction | blocking | Complete matrix: all 15 `moco` rows carry full keys | Correction required in both drafts and in the current internal article; severity label is editorial — treat as must-fix |
| Env-by-label / env-by-guarantee "unavailable" | softened to "no prebuilt table" for `opus 5`; accepted for `gpt 6 luna max` | blocking (`opus 5`), correction (`gpt`) | Table B and Table D carry environment, labels, guarantees; JSON cross-tabs and reconciliation R4 reproduce | `claude fable 5.1` supported; `grok 4.5` understated (R4). Unresolved disagreement preserved, resolved by rows |
| 9/9 environments by guarantee | not addressed | "four behavioral_reference; six compile_only" | 4 BR (`categorical_lenses`, `ci_dependency_graph`, `spreadsheet_dataflow`, `template_interpreter`) + 5 CO (`architecture_naturality`, `neuro_symbolic_parser`, `semiring_unification`, `stochastic_monad`, `tokenizer_adjunction`) = 9 | `claude fable 5.1` miscounted (R1). Carry 4 + 5 |
| "one seed per cell" quotation | not flagged | correction: unattributed | Phrase appears in no supplied source; only Figure 8's bar label "design cells" exists | `claude fable 5.1` supported |
| "judge-coverage gap" | not flagged | correction | Recorded status is `infrastructure_unscored`; `failure_mode_normalized` = `unknown` | `claude fable 5.1` supported |
| Figure 2 path | "required figure URL (not leakage)" | "unverifiable chart number/path" | The four required URLs are fig8–fig11; `fig2_environment_outcome_lollipop.svg` is not among them and Section E does not describe it | `grok 4.5` wrong; replace Figure 2 in both drafts |
| 214 uniform rows | correction (204 + 10) | correction (204 + 10) | 148 all-pass rows + 56 zero-pass rows = 204; +10 unscored-environment rows = 214 | Agreed; current internal article already correct |
| Overview "~12 at 1.00" vs 17 | not noted | noted | Table A: 17 all-pass environments, 172/172 | Add to open-claims list (R2) |
| Provider "1 retry, 60s" vs row 409 fields | not noted | noted | `http_attempts_result` 19, `elapsed_seconds` 46.101, `provider_transport` `completed_with_errors` | Preserve as field contrast, no unit conversion (R3) |

### 1.5 Missing or unverifiable material (explicit gaps)

- No rendering of any SVG was inspected; caption checks are against Section E prose.
- No second seed, clean source snapshot, config-hash comparison, or base rate for apparent non-monotonic patterns exists in the record; none may be invented.
- The origin of the overview's "10" and "~12", and of the provenance's "24", cannot be determined from supplied material.
- The operational meaning of dispositions `rejected` and `unscored` is undefined in the record.
- Links in `PRIOR_WORK_REFERENCES` are not verified usable from this stage.

### 1.6 Arithmetic rechecked here (from Tables A–D and the complete matrix)

416 / 405 / 11; 277 / 128; 277/405 = 68.395%; 277/416 = 66.587%. Environments 17 (172/172) / 7 (0/68) / 12 (105/165, +1 unscored) / 2 (10 unscored). Unweighted mean of 36 scored-environment fractions 69.21%; median 8/9. Matrix 340 rows; 296 single-case, 44 multi-case (`moco` 15/55, `glyph` 12/24, `css_state_machine` 9/18, `epistemic_games` 8/23); 329 rated, 320 at 0 or 1, 9 fractional (`moco` rows #1, 2, 4, 5, 6, 7, 8, 9, 14; values 2/3 ×4, 5/6, 1/6, 3/4, 2/5, 1/3); 6 `moco` endpoint rows (#3, 10, 11, 12, 13, 15). 98 zero-pass tuples in 19 environments; all 12 mixed environments contain at least one. 34 distinct difficulty-key names. Labels 51/49/11 (9 `RUNTIME_ERROR` + 2 `runtime_error`)/9/5/3 = 128. Guarantees: 11 BR environments, 189 cases, 141/189 scored PASS, 48 FAIL; 27 CO environments, 227 cases, 136/216 scored PASS, 80 FAIL, 11 `infrastructure_unscored` all CO. Dispositions: 10 `rejected` FAILs (rows 20, 225–231, 233, 401; 9 `source_invalid` + 1 `training_failed`); 9 `unscored`-disposition FAILs with status `scored` (rows 24, 145, 193, 214, 222, 232, 293, 405, 415; 5 `invalid_action`, 2 `training_failed`, 2 lowercase `runtime_error`). Omissions: `moco` 35 twin; `glyph` 9 gate + 12 twin = 21; `rope` 10 modality + 5 gate = 15; `epistemic_games` 9 twin; totals 56/14/10 = 80; 416 + 80 = 496. Sensitivities: 241/350 = 68.86%; 277/381 = 72.70%; 241/326 = 73.93%. The single `sql_fixed_point` FAIL: `hidden_depth=hard`, `surface_deceptiveness=easy`. The unscored `rd_adaptive_halting` row: all five keys `easy`. Environments within five points of 68.4%: only `moco` (65.5%) and `tensor_functor` (66.7%).

---

## 2. Seven-dimension comparison

### 2.1 Argument and structure

Concrete question the article answers: what does the scored pass rate 277/405 = 68.4% summarize, and what does the recorded environment and tuple structure permit a reader to conclude from it?

Strongest source-supported thesis: the pooled figure is an exact answer to one counting question, but it is a value almost no environment takes — 24 of 36 scored environments sit at an endpoint, the 12 mixed environments hold 40.7% of scored cases, and the 340-row map beneath is 87% single-case rows — so the record supports a descriptive map of where judged outcomes fell and does not support a difficulty ranking, a mechanism, or a stability estimate.

Structures of the two drafts:

- `gpt 6 luna max` is a linear audit: counts → endpoint list → names → matrix → cell → `moco` → withdrawn → unscored → 10-vs-7 → labels/guarantees → selection → confounds → conclusion. Thirteen headed blocks for roughly 2,300 words; the reader meets findings in sequence rather than an argument. Its sections "Unscored cases are not failures", "Ten zero-pass environments or seven?", and "Confounds we cannot ignore" repeat caveats stated earlier.
- `opus 5` uses the same skeleton but opens with a reader's question ("What should I expect if I open one environment at random?") and adds a density/sensitivity passage and a sharper matrix reading ("the matrix mostly repeats the endpoint pattern one level down, which is close to inevitable when nearly nine rows in ten contain a single case"). It is still a sequence of audit blocks, and its conclusion imports a false limit ("nothing in the present archive supplies it").

What to move, combine, shorten, remove:

- Combine "Unscored cases are not failures" into the counting section (where the 405 vs 416 denominators are introduced) rather than a standalone block.
- Combine "The selection frame" with the counting section, because Figure 8 is the selection frame and the omissions table belongs beside it.
- Move the sensitivity table (currently under "What a cell means" in the internal article) to the density discussion.
- Shorten the three enumerations of 9/9 environments to one compact table or one line.
- Remove the Figure 2 lollipop in both drafts (contract forbids substitution for Figures 8–11).
- Merge "Confounds I cannot remove" into local caveats and a short bounded ending; a separate confounds section is the "ending disclaimer" pattern the house style warns against.
- Progression to enforce: intelligible problem (the average nobody has) → counting result and frame → environment map → what the tuple map adds (and does not) → what labels/guarantees record → withdrawn/open → bounded consequence.

### 2.2 Opening

- `gpt 6 luna max`: "Mercury-2.5 received PASS on **68.4% of 405 scored cases** in this archived campaign. That is a precise case-weighted rate, but it does not describe what happened in each environment." Specific, flat; the limit (judged outcomes, selected cases, one seed) arrives in paragraph three; no tension beyond the `ts_*` contrast.
- `opus 5`: "What should I expect if I open one environment at random?" Creates tension quickly; limit arrives in paragraph two ("These are verdicts assigned by the campaign's judges to selected cases"). Its closing line of the opening — "descriptively thin; the structure worth looking at is the map underneath it" — is a thesis sentence, reusable in meaning.
- Both openings use the identical `ts_*` 4/4, 0/4, 0/4 contrast, as does the current internal article. A fresh device is proposed in §3.

### 2.3 Examples and technical depth

Selected examples (all source-supported):

- The two largest endpoint blocks: `epistemic_games` 23/23 and `glyph` 0/24 (Table A). Both are `behavioral_reference`, which lets the article say the guarantee does not by itself separate them.
- Near-pooled environments: only `moco` 36/55 and `tensor_functor` 6/9 land within five points of 68.4% (Table A; Figure 9 order 13–14).
- `ts_*` and `sheaf_*` name contrasts (Table A) — keep, but as a second-level example, not the opening.
- `css_state_machine` nine rows all 2/2 (matrix) — the withdrawn claim.
- `sql_fixed_point` single FAIL at `hidden_depth=hard`, `surface_deceptiveness=easy` (matrix) — the "one observation" example.
- `moco` row #6: six cases, 1/6, five `overfit_visible_tests`, key `distractors=hard, naming=easy, queue_math=easy, symptom_mask=hard, temperature=hard, visible_tests=easy` — one descriptive example that the keys exist; no shape claim.
- Row 409 `ts_parse_only` PASS with `performance_eligible=False` and the recorded `exclusion_reason`.

Tables/figures and their roles:

| Element | Role | Keep/compact |
|---|---|---|
| Figure 8 (selection frame) | Shows 496 → 416 → 405 → 277/128; omitted cases outside every rate | Keep; caption must carry the unlabelled 11 |
| Four-way environment table (17/7/12/2) | Replaces three enumerations with parallel counts | Keep |
| Figure 9 (intervals) | Shows endpoint-heaviness and interval width by n | Keep; caption states Wilson/binomial convention |
| Mixed-environment table (12 rows) | Preserves distinct fractions and the +1 unscored | Keep; add a flags column for `rejected`/ineligible rows |
| Omissions table (class × environment) | Connects selection concentration to interpretation | Keep, compact (4 environments × 3 classes) |
| Sensitivity table (exclude `moco`/`glyph`) | Arithmetic illustration of density | Keep, three rows; label as arithmetic |
| Figure 10 (tuple matrix) | Shows single-case dominance and the 9 amber `moco` rows | Keep |
| Figure 11 + global label table + env-by-label table | Shows labels are recorded classifications with an environment breakdown | Keep; rebuild env-by-label rows so each environment is identifiable |
| Guarantee table (BR/CO: environments, PASS, FAIL, scored, unscored) | Shows the confound | Keep, two rows |

Do not add: mathematics (no `$`), a shared difficulty scale, a `moco` heat map by dimension, Mermaid or any new rendering dependency, Wilson arithmetic in prose.

### 2.4 Prose and tone

Faults with exact quotations:

- Stock transitions: `gpt 6 luna max` "Thus **277/405, or 68.4%**, is the scored-case pass rate"; "Together, the mixed environments contain…"; `opus 5` "So the matrix mostly repeats…", "So I keep **68.4%**…" (serviceable individually, formulaic cumulatively).
- Empty emphasis: `gpt 6 luna max` bolds "**416 selected cases in 38 environments**", "**277/405, or 68.4%**", "**277/416, or 66.6%**", "**340 environment-by-tuple rows**" — bold on every number dilutes the thesis marker the house style reserves bold for.
- Repetitive caveats: `gpt 6 luna max` states the one-seed limit in the opening, under "What a cell means", and again under "Confounds we cannot ignore"; `opus 5` repeats "I keep all nine in the counts" / "all ten stay in the 128" / "all ten remain in the 128".
- Overlong setup: `gpt 6 luna max` lists all 17 all-pass names in running prose and again partially in the "endpoint-heavy" section.
- Unsupported superlatives/mechanism words: `opus 5` "The 68.4% is sensitive to how tuples were unrolled into cases" ("unrolled" implies a design step no source describes); `opus 5` "Being unscored is a property of the judging pipeline" (cause assigned).
- Mechanical benchmark-report prose: `gpt 6 luna max` "The campaign records 189 `behavioral_reference` and 227 `compile_only` judge guarantees across the 416 selected cases, including the unscored cases." followed by a two-row totals table that adds nothing to the sentence.
- Invented first-person experience: none found that asserts a personal act beyond reading records. `opus 5` "I have not found the derivation behind the 10" is acceptable as a statement about the record. Heading "Confounds we cannot ignore" (`gpt 6 luna max`) breaks the first-person voice.
- Author's wording exclusions present in candidates (internal quotation preserved; must not enter public prose): `opus 5` "Density matters for the top line too."; `opus 5` "the honest list of what the archive declines to settle". The current internal article also contains two: "environment identity matters more than difficulty" and "how little the archive can actually support" (Importance field).

Calibration against reference excerpts: the reference posts open on a short declarative or a self-correction, move in one-to-four-sentence paragraphs, mark one thesis in bold, and attach the limit where the attractive reading would overrun. Adopt that movement. Do not reuse their metaphors, jokes, emoji, or formulations ("failed diagrams", "the first formalisation was wrong", etc.). No numerical prose ratings are assigned here.

### 2.5 Transitions and caveat placement

| Limit | Attach to |
|---|---|
| Selected-case denominator (405 vs 416) | Counting section, the sentence introducing 66.6% |
| Unknown outcomes (11 `infrastructure_unscored`) | Same paragraph; recorded label, no cause |
| One-seed scope (seed 0 in all supplied records) | First appearance of an endpoint or interval; Figure 9 caption; not a separate section |
| Selection and dependence | Omissions table (concentration in `moco`/`glyph`/`rope`/`epistemic_games`) and the multi-case-row paragraph |
| Judge-guarantee/environment confound | Guarantee table, immediately after 141/189 vs 136/216 |
| Undefined dispositions | Mixed table flags column and `monadic_reward` 0/9 line; one sentence in labels section |
| Provider-note conflict (row 409) | Beside `ts_parse_only` 4/4 wherever first cited |
| Dirty source / no clean comparator | Beside any reproduction or "would a clean tree change this" sentence, in the bounded ending |

Consolidation: state each limit once in full at its anchor; later references are a clause, not a paragraph. The ending summarizes what is open; it does not introduce new limits.

### 2.6 Claim support and traceability

Full table in §6. Headline items: both drafts and the current internal article wrongly state that `moco` tuple keys are unavailable; both drafts wrongly state env-by-label and env-by-guarantee breakdowns are unavailable; both drafts quote "one seed per cell" without a source; both call unscored cases a "judge-coverage gap"; both use a Figure 2 that the contract forbids (`gpt 6 luna max`'s embed is also broken: a bare "!" line). The current internal article adds two boundary violations ("the 24 cannot coexist with the selection frame"; casing treated as "a data-quality artefact") and one unsupported quotation. Overclaims and unsupported "unavailable" claims are both flagged; editorial preferences are labelled separately in §6.3.

### 2.7 Public-site fit

- Frontmatter: all three texts carry the exact contracted title/date/layout. Keep.
- Byline: present and exact in all three.
- Epistemic-status `<dl>`: five fields in order in all three. Prose field in both drafts ("first-person and exploratory"; "Written for this article") discloses nothing about process; a neutral AI-assisted statement is permissible and recommended. No field may claim human verification or replication. Remove "actually" from the Importance field of the current internal article.
- MathJax: no inline or display mathematics is needed; plain fractions and "×" do not require the loader. Omit `{% include mathjax.html %}` unless `$` appears; if it does, place it immediately after the frontmatter and before the byline; no external scripts.
- Figures: both drafts lack all four required figures and use `fig2_environment_outcome_lollipop.svg`; the current internal article carries fig8–fig11 in sensible positions. Alt text and captions must match Section E (see §7).
- Markdown/HTML: `gpt 6 luna max` has a malformed image line ("!" alone). Tables render as GFM; the current internal article's env-by-label table has two rows that bundle several environments with a "3, 2, 2, 1, 1, 1" cell — hard to read; rebuild.
- Internal provenance: no candidate exposes source paths, case IDs, or stage terminology. The current internal article's label `infrastructure_unscored` is a recorded field value, acceptable. Keep `[m-word]` where its passage remains. Headings such as "Claims withdrawn or left open" are fine; avoid "handoff", "packet", "reviewer", "Arena" in public prose.
- Reading flow: the current internal article runs over the 2,800-word target; trimming must come from enumerations and repeated caveats, not from evidence tables.

---

## 3. Original thesis, reader question, opening strategy

Thesis (to be stated once, in bold, early): 277/405 = 68.4% is the exact answer to one counting question, and in this campaign it is a value almost no environment took — the record supports a map of where judged outcomes fell, not a difficulty ranking, a mechanism, or a stability estimate.

Reader question: when a single pass rate is reported for a model across many environments, what should a reader expect from any one environment, and what would they need to know before trusting that expectation?

Opening device (described, not drafted): begin with the mismatch between the pooled value and the per-environment values — only two of 36 scored environments land within five points of 68.4%, while 24 landed at exactly all or exactly none — stated as a prediction problem the reader can hold in mind before any table appears. Within the first three paragraphs, name the three limits that govern every later number: judged verdicts on selected cases, seed 0 throughout the supplied records, two kinds of judge guarantee fixed by environment. Then a one-sentence revision note that the earlier version is replaced and that one claim is withdrawn below. This follows the reference-post grammar of a short declarative problem followed immediately by the bound on what it can mean, without copying either candidate's `ts_*` opening or any reference-post phrasing. The `ts_*` contrast is retained later as the smallest illustration of the name problem.

---

## 4. Section-by-section blueprint (target 2,000–2,800 words, excluding tables)

### 4.0 Frame
- Frontmatter exactly as contracted; byline; `<dl class="epistemic-status">` with five fields making supportable disclosures (retrospective reading of archived judgments; regrouping of 416 cases/38 environments/340 rows; drafting and revision AI-assisted; confidence high in counts and low in causal readings; why a pooled number needs its map). No MathJax include unless math appears.
- Revision note, one or two sentences: replaces the earlier version; headline unchanged; tuple layer added as description; one claim withdrawn, several left open, listed in their own section.

### 4.1 Opening (no heading, ~250 words)
- Purpose: pose the prediction problem and bound it.
- Progression: pooled value → how few environments sit near it → what the verdicts are and are not (judged outcomes, selected cases, seed 0, two guarantees) → thesis in bold.
- Evidence: Table A (two environments within five points; 24 endpoints).
- Caveat: PASS/FAIL labels do not establish understanding or general capability; an environment name is not a difficulty rating.
- Transition: "count first" — what the denominators are.

### 4.2 Counting the judged cases and the frame around them (~450 words)
- Purpose: fix 416/405/277/128/11 and the 496 frame; separate 68.4% from 66.6%.
- Progression: 416 selected → 405 scored → 277/128 → 11 `infrastructure_unscored` (recorded label, no recorded cause) → 277/416 answers a different question and must not be read as a rate that treats unknowns as failures → the 80 omissions before selection.
- Figure 8 here, caption carrying the 11-count and the note that the nine conflicting-disposition FAILs are not drawn.
- Omissions table: `moco` 35 twin; `glyph` 9 gate + 12 twin; `rope` 10 modality + 5 gate; `epistemic_games` 9 twin; totals 56/14/10. One sentence: the provenance summary says 24 known-gate omissions against the 14 in the detailed rows; both are reported; unresolved.
- Caveats attached: the 496 frame counts case IDs and is not the 340-row matrix; "design cells" is a chart label, not a definition; selection was not random and concentrated in three environments, which bears on how the map is read without establishing a causal effect.
- Transition: with the denominator fixed, how are the 405 distributed across environments?

### 4.3 An endpoint-heavy map (~500 words)
- Purpose: show the shape the pooled value compresses.
- Progression: four-way table (17/7/12/2) → 24 of 36 at an endpoint, resting on 4 to 24 cases → the 12 mixed environments hold 165 cases, 2/15 to 8/9 → one sentence on unweighted mean 69.2% and median 8/9 as different questions.
- Figure 9 here; caption names the 95% Wilson interval, its binomial sampling convention, that it is not seed variation, pooled line at 68.4%, and that environments with no scored case are not drawn.
- Mixed table with a flags column: `transformer_ssm_lift` 8/9 (lone FAIL `rejected`); `batchnorm_ema` 2/15 (one `rejected`, one `unscored`-disposition); `rd_adaptive_halting` 8/14 + 1 unscored; `moco` 36/55 (three `unscored`-disposition FAILs).
- Endpoint flags in prose: `monadic_reward` 0/9 with eight `rejected`; `ts_parse_only` 4/4 with one performance-ineligible PASS whose `exclusion_reason` describes a provider-attributed terminal failure — recorded attribution that conflicts with the verdict, not proof of cause; it stays in the 277. If space allows, one clause that the provenance's "1 retry, 60s" and the row's 19 attempts / 46.1 s are not reconciled.
- Caveats: one seed; within-environment agreement does not establish independence; dispositions undefined.
- Transition: names and density — why "the map" is not a set of families.

### 4.4 Names, density, and what moves the number (~400 words)
- Purpose: block two shortcuts — reading prefixes as families and reading the pooled rate as representative.
- Progression: `ts_*` (4/4, 0/4, 0/4) and `sheaf_*` (8/9, 0/9, 0/9) and `categorical_lenses`/`functorial_augmentation`/`tensor_functor` (9/9, 0/9, 6/9) → `glyph`, `moco`, `batchnorm_ema` supply 94/405 cases and 56/128 FAILs → sensitivity table (exclude `moco` 68.86%; exclude `glyph` 72.70%; both 73.93%) labelled as arithmetic on recorded rows → link back to the omissions concentration in the same environments.
- Caveat: shared names do not imply shared conditions; sensitivity is to selected case density, not to any described design step; no shared failure mechanism is implied.
- Transition: what sits beneath each environment number.

### 4.5 Beneath the environments: 340 rows (~450 words)
- Purpose: show what the tuple layer adds (thinness, uniformity) and what it cannot (scale, effect, ranking).
- Progression: 340 rows, 4–15 per environment → 296 single-case, 44 multi-case in four environments → 329 rated, 320 at 0 or 1, 9 fractional all in `moco` → 204 rows in environments with a uniform scored outcome plus 10 rows in two environments with no scored outcome (214 only if shared absence is grouped) → 98 zero-pass tuples in 19 environments, all 12 mixed environments included; a different count from the 7 zero-pass environments.
- Figure 10 here; caption: 340 squares, grey for 11 unscored rows, numbers on 44 multi-case rows, amber only in `moco`, columns not comparable across environments.
- "Cell" paragraph without the unattributed quotation: the supplied records show seed 0 for all 416 selected cases and record no second seed; 44 rows hold more than one case; the inference that a planning unit is a row rather than a case is the writer's reading of the arithmetic, not a recorded convention.
- `moco` paragraph corrected: the complete matrix records a tuple key for every row, including the nine fractional ones; one example row (#6, 1/6) is described; 34 key names are environment-specific, so no cross-environment scale, dimension effect, or ranking is read. The unscored `rd_adaptive_halting` row at all-`easy` is a recorded field, not a cause.
- Caveat: multi-case rows do not estimate within-row dependence; single-case rows can only be 0 or 1.
- Transition: what the labels on the 128 FAILs record.

### 4.6 What the labels and guarantees record (~400 words)
- Purpose: present recorded breakdowns as recorded, and the confound that prevents a judge-effect reading.
- Progression: Figure 11 + global table (51/49/11/9/5/3) → casing: 9 `RUNTIME_ERROR` and 2 `runtime_error` are normalised to one bucket as an analysis convention; uppercase cases carry disposition `scored`, lowercase `unscored`; recorded association, no explanation → env-by-label table (one environment per row where counts differ; small environments may share a row only if each environment's own labels stay legible) → dispositions: 10 `rejected` (8 `monadic_reward`, 1 `batchnorm_ema`, 1 `transformer_ssm_lift`) and 9 `unscored`-disposition FAILs with status `scored`; the disposition value "unscored" is not the status `infrastructure_unscored` → guarantee table: BR 11 environments 141/189, CO 27 environments 136/216 with all 11 unscored cases → each environment carries one guarantee, so the contrast is confounded with environment.
- Caveats: labels are classifications, not mechanisms; a compile-only PASS is not behavioral validation; a 9/9 under `compile_only` (five environments) records what that judge checked; the four BR 9/9 environments are named if the point is made.
- Transition: what the earlier version claimed and what the record leaves open.

### 4.7 Withdrawn and open (~250 words)
- Withdrawn: `css_state_machine` non-monotonic variation — all nine rows 2/2.
- Open, not findings: apparent non-monotonic patterns in `moco`; the single `sql_fixed_point` FAIL at `hidden_depth=hard`, `surface_deceptiveness=easy` is one observation and establishes no effect; no base rate computed.
- Source disagreements preserved: 7 scored zero-pass environments vs the overview's 10; 17 all-pass vs the overview's "~12"; 14 vs 24 known-gate omissions; dispositions undefined; provider note vs recorded fields for row 409.
- Caveat: no reconciliation is asserted; 14 + 10 = 24 may be mentioned once as an unverified possibility or omitted.

### 4.8 What this supports (~250 words)
- Restate: 277/405; 17/7/12/2; 24 endpoints; 320 of 329 rated rows binary because most rows hold one case; near-pooled environments are two.
- Does not show: a common difficulty scale or ranking; a mechanism for `glyph`, `moco`, `batchnorm_ema`; how endpoints behave under another seed; what a uniform guarantee or a clean source tree would change (source recorded dirty; no clean config-hash comparison).
- Bounded consequence: the next evidence the record cannot supply — repeated seeds within environments and guarantees varied within an environment — and what each would and would not settle.
- End on the counting question 68.4% answers, without a new caveat paragraph.

---

## 5. Retention and reconstruction decisions

### 5.1 Useful elements from `gpt 6 luna max` (reasons)
- The four-way environment table and the mixed-environment table — exact and compact.
- "Treating their cases as zero-pass would invent judgments that are not in the record." — the right meaning for the 11 unknowns; reuse the meaning, not the sentence.
- Keeping the ineligible PASS in the 277 with the conflict stated, and reporting 14 and 24 without reconciling.
- The clear statement that the tuples "are not a shared scale and must not be pooled, ranked, or regressed across environments."

### 5.2 Useful elements from `opus 5` (reasons)
- A question-led opening and the thesis meaning "arithmetically correct and descriptively thin".
- The reasoning that single-case rows force binary rates, so the matrix "mostly repeats the endpoint pattern one level down".
- The sensitivity arithmetic and "94 of the 405 scored cases but 56 of the 128 failures".
- The principle that flags "belong beside the counts rather than inside a footnote".
- The revision-note framing of the tuple layer as "exploratory description rather than as a result".
- "Closely named environments landed far apart." as a summary meaning.

### 5.3 Elements to remove or narrow (both drafts unless noted)
- Figure 2 lollipop and its captions (both); the bare "!" line (`gpt 6 luna max`).
- "one seed per cell" as a quotation (both; also current internal article).
- "judge-coverage gap" / "property of the judging pipeline" (both).
- `moco` "no row-by-row key" (both; also current internal article).
- "No environment-by-label breakdown is available here" and "nothing in the present archive supplies it" (`opus 5`); "The counts are global only; they do not show which environments produced which labels" and "I cannot compare environment results under one common judging standard" (`gpt 6 luna max`).
- "Describing a 9/9 environment as behaviourally settled would outrun what the judge checked." (`opus 5`) — narrow to the five compile-only 9/9 environments.
- "unrolled into cases" (`opus 5`).
- "no case was re-run under a second seed" / "no case was run again under a second seed" (both) — narrow to "the supplied records show seed 0 for every selected case and record no second seed".
- Guarantee totals-only table (`gpt 6 luna max`) — replace with the two-row guarantee table carrying environments/PASS/FAIL/unscored.
- Excluded wording: "Density matters…", "the honest list…" (`opus 5`); "matters more than difficulty", "actually support" (current internal article).
- Current internal article: "So the 24 cannot coexist with the selection frame as reported"; "I treat the casing difference as a data-quality artefact"; the speculative 7 + 2 + `rope` derivation; the duplicated "I report both and do not resolve the conflict."

### 5.4 Problems neither draft handles adequately
- Neither draft uses any of the four required figures.
- Neither distinguishes the disposition value `unscored` (9 FAILs with status `scored`) from the status `infrastructure_unscored` (11 cases).
- Neither connects omission concentration (`moco` 35, `glyph` 21, `rope` 15, `epistemic_games` 9) to the environments that dominate the FAIL count, which is the one place selection bears directly on reading the map.
- Neither names the `sql_fixed_point` FAIL tuple; both obscure the environment name.
- Neither records the overview's "~12 at 1.00" against 17.
- Neither states that both `epistemic_games` 23/23 and `glyph` 0/24 carry `behavioral_reference`, which is the compact way to show the guarantee does not sort the endpoints.
- Neither says what `epistemic_games` tests if it is mentioned beyond a count; if discussed, keep the bounded description (Bayesian inference over stipulated policies, not recursive theory of mind) and do not import the overview's "belief computation exact while decisions fragile".

---

## 6. Claim-check handoff

### 6.1 Evidence corrections (factual)

| ID | Candidate quotation / location | Source citation | v3 attribution | Required action | Remaining limit |
|---|---|---|---|---|---|
| CC-01 | `gpt 6 luna max`, "`moco`: the only fractional rows": "The available record does not link each fractional value to its tuple key, so I cannot draw the outcome shape across `moco`'s dimensions."; "Claims withdrawn": "the missing row-by-row tuple key also prevents reconstructing the pattern." `opus 5`, same section: "no row-by-row key links each value back to its tuple." Current internal article: "The archive has no row-by-row key linking each value to its tuple." | Complete matrix, all 15 `moco` rows with `difficulty_tuple` (e.g., 1/6 row: distractors hard, naming easy, queue_math easy, symptom_mask hard, temperature hard, visible_tests easy) | `grok 4.5` correction; `claude fable 5.1` blocking; local check | Replace with: keys are recorded for every row; description available; pattern remains open | No isolated dimension effect, no scale, one seed, no base rate; within-row dependence not estimated |
| CC-02 | Both: "214 rows—63% of the matrix—sit in environments where every row has the same outcome." / "214 of 340 rows (63%) sit in environments where every row has the same outcome."; `opus 5` ending: "63% of rows inside environments with a single uniform outcome" | Matrix: 148 all-pass rows + 56 zero-pass rows = 204; `epistemic_silence` 6 + `epistemic_type_games` 4 = 10 blank | Both reviewers; local check `uniform_scored_environment_rows` 204 | 204 in uniform-scored environments plus 10 in entirely unscored environments; 214 only when shared absence of scored outcomes is grouped | Uniform outcome is not stability |
| CC-03 | `gpt 6 luna max`: "The counts are global only; they do not show which environments produced which labels or establish a mechanism." `opus 5`: "**No environment-by-label breakdown is available here**"; "nothing in the present archive supplies it." | Table B (environment, `failure_mode_raw`); Table D `failure_modes`; JSON `failure_cross_tab`; reconciliation R4 | `claude fable 5.1` (blocking/correction); `grok 4.5` understated per R4 | State breakdown as recorded (e.g., `glyph` overfit 22; `sheaf_*` zero-pass environments underfit 9 each; `rd_adaptive_halting` RUNTIME_ERROR 5; `source_invalid` 8 + 1) | Labels are classifications, not mechanisms |
| CC-04 | `gpt 6 luna max`: "The totals alone do not show how outcomes are distributed by environment and guarantee, so I cannot compare environment results under one common judging standard." `opus 5`: "without an environment-by-guarantee breakdown I cannot test whether the environment contrasts survive a uniform standard." | Table D `judge_guarantees`; JSON cross-tabs; R4: BR 11 envs 141/189; CO 27 envs 136/216 + 11 unscored | `claude fable 5.1`; R4 | Reword to the confound: one guarantee per environment, so the contrast cannot be read as a judge effect | No within-environment variation in guarantee |
| CC-05 | `opus 5`: "Describing a 9/9 environment as behaviourally settled would outrun what the judge checked." | Table B/D: 4 BR 9/9 environments, 5 CO 9/9 environments | `claude fable 5.1` correction (its "six compile_only" is wrong); R1 | Restrict to the five compile-only 9/9 environments or name guarantees | BR PASS still records only what that judge checked |
| CC-06 | `gpt 6 luna max`: 'The phrase "one seed per cell" is ambiguous here'; `opus 5`: "The campaign records one seed per cell."; current internal article: 'The campaign describes its design as "one seed per cell"' | Absent from provenance, overview, packet; only Figure 8 bar label "design cells" | `claude fable 5.1` correction | Drop quotation and attribution; seed 0 rests on Table B; present any row-as-unit reading as the writer's inference | "design cells" is not a definition of "cell" |
| CC-07 | Both: "a judge-coverage gap"; `opus 5`: "Being unscored is a property of the judging pipeline, not of the case's outcome." | Table B rows 109–118, 243: status `infrastructure_unscored`, verdict blank, `failure_mode_normalized` `unknown` | `claude fable 5.1` correction | Use the recorded status; record no cause | None recorded |
| CC-08 | Both drafts omit the nine FAILs with status `scored` and disposition `unscored` | Table B rows 24, 145, 193, 214, 222, 232, 293, 405, 415; JSON `scored_fail_unscored_disposition` | Both reviewers; local check | Add beside the 10 `rejected`; keep all 19 in the 128 and in `n_scored` | Dispositions undefined; do not equate with `infrastructure_unscored` |
| CC-09 | `gpt 6 luna max`: bare "!" line + "*Figure 2: Lollipop chart…*"; `opus 5`: `![…](../figures/fig2_environment_outcome_lollipop.svg)` + "*Figure 2: One dot per environment…*" | Section E describes Figures 8–11 only; contract requires fig8–fig11 and forbids Figure 2 | Both reviewers; `grok 4.5` wrongly treated fig2 as required | Remove Figure 2; place the four required figures with Section-E-checked captions | SVGs not rendered here |
| CC-10 | Both: "no case was re-run under a second seed" / "no case was run again under a second seed" | Table B seed column; boundary: absence of repeated-seed data establishes nothing archive-wide | — | "the supplied records show seed 0 for every selected case and record no second seed" | Not a variance estimate |
| CC-11 | Current internal article: "So the 24 cannot coexist with the selection frame as reported" | Table C 14 (9 `glyph` + 5 `rope`); provenance "24"; Section E Figure 8 496 frame | Governing boundary; both reviewers kept 14/24 open | Remove the impossibility claim; report both; at most note 14 + 10 = 24 once as unverified | Origin of 24 unknown |
| CC-12 | Current internal article: "I treat the casing difference as a data-quality artefact rather than two kinds of runtime failure." | Table B rows 127, 128, 131, 133, 244, 246, 252, 256, 257 (`RUNTIME_ERROR`, disposition `scored`); rows 405, 415 (`runtime_error`, disposition `unscored`) | `claude fable 5.1` handoff ("recorded coincidence, no documented explanation") | Describe normalisation as an analysis convention; state the disposition association; no cosmetic or mechanistic explanation | None documented |
| CC-13 | Current internal article: "Seven all-fail environments plus the two with no scored case give 9. Adding `rope`… gives 10 only if `rope` is counted as zero-pass." | Table A; boundary: combining unscored environments and omitted `rope` does not verify the overview's definition | — | Trim to "unresolved"; if kept, label as not a verification | Overview's rule unknown |
| CC-14 | Neither draft; overview: "vs ~12 at 1.00" | Table A: 17 all-pass environments, 172/172 | `claude fable 5.1` note; R2 | Add to open-claims list beside 10 vs 7 | No explanation available |
| CC-15 | Both: "exclusion note describes a provider-attributed terminal failure" (acceptable); provenance "1 retry, 60s" | Row 409 / excerpt: `http_attempts_result` 19, `elapsed_seconds` 46.101, `provider_transport` `completed_with_errors`, `performance_eligible` False | `claude fable 5.1`; R3 | Attribute description to the recorded `exclusion_reason`; keep PASS in 277; if the provenance figures are mentioned, present the field contrast without unit conversion | Attribution is recorded, not established cause |
| CC-16 | Both obscure the environment: "the SQL-named `sql_fixed_point`" / "a SQL-named environment"; current internal article: "a SQL environment" | Matrix: `sql_fixed_point` FAIL at `hidden_depth=hard`, `surface_deceptiveness=easy`; 8/9 | — | Name the environment and the tuple; one observation establishes no non-monotonic effect | One seed; no base rate |
| CC-17 | `opus 5`: "The 68.4% is sensitive to how tuples were unrolled into cases for a handful of environments." | No source describes an unrolling step; Table A n_tuples/n_cases | `claude fable 5.1` note | "sensitive to selected case density" | Density is recorded, mechanism is not |

### 6.2 Open questions referred to the claim-check stage (no answers invented)
- Origin of the overview's "10" and "~12"; origin of the provenance's "24".
- Operational meaning of `rejected` and `unscored` dispositions.
- Whether "1 retry, 60s" and the row-409 fields count the same quantities.
- Whether any public source link (e.g., prior-work references) is verified usable before it appears in the article; none is required.
- Whether the four SVGs render as Section E describes (captions here are text-checked only).

### 6.3 Editorial preferences (not evidence corrections)
- Open with the "value almost no environment takes" device rather than `ts_*`.
- One compact table instead of three enumerations of all-pass environments.
- Drop the unweighted mean/median to a single sentence.
- Place the sensitivity table in the density section.
- Add a flags column to the mixed table rather than scattered sentences.
- Mention one `moco` row as an example rather than listing nine keys.
- Omit external citations unless verified; the article stands on the record.
- Prose field: a neutral AI-assisted statement; Certainty field without the word "actually".
- Prefer first-person headings over "we".
- Reduce bold to the thesis and the two denominators.

---

## 7. Final writer checklist

Frame
- [ ] Frontmatter exactly: `title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"`, `date: 2026-10-16`, `layout: post`; no extra fields.
- [ ] `{% include mathjax.html %}` only if `$`/`$$` appears, placed after frontmatter and before byline; no external scripts.
- [ ] Byline `*by <span class="icon-self">StrangeTcy</span>*`.
- [ ] `<dl class="epistemic-status">` with Original ideas, Synthesis, Prose, Certainty, Importance, in order; supportable disclosures; neutral AI-assisted statement permitted; no claimed human verification, replication, or author experiences.
- [ ] Concise revision note; a "withdrawn and open" section with `css_state_machine` withdrawn, `moco`/`sql_fixed_point` open, 10 vs 7, ~12 vs 17, 14 vs 24, dispositions, row-409 field contrast.

Figures (positions and captions checked against Section E; no claim of visual inspection)
- [ ] `../figures/fig8_selection_frame.svg` in the counting section. Caption: three stacked bars; 496 recorded case IDs = 416 selected + 80 omitted (56 intervention-twin, 14 known-gate, 10 unsupported input modality); 416 = 405 scored + 11 `infrastructure_unscored` (the 11-case segment is unlabelled in the image, so the count is given here); 405 = 277 PASS + 128 FAIL; omitted cases in pale grey enter no pass rate; the nine scored FAILs with a conflicting disposition are not drawn separately. Alt text describes bars, not "cells" as a definition.
- [ ] `../figures/fig9_environment_intervals.svg` in the map section. Caption: one dot per environment with scored cases (36; the two unscored environments are not drawn) at PASS/scored; bars are 95% Wilson intervals under a binomial sampling convention — not measured seed variation; dotted line at 277/405 = 68.4%; label beside each bar is k/n; colour classes no scored pass / mixed / all scored passed; selection and possible dependence limit interpretation.
- [ ] `../figures/fig10_tuple_matrix.svg` in the rows section. Caption: 340 squares, one per environment × tuple row, grouped by environment; colour is row pass rate (red 0, amber fractional, green 1); grey marks the 11 rows with no scored case; numbers mark the 44 rows holding more than one case; the 9 fractional rows are all `moco`; tuples are environment-specific, so columns are not comparable across environments.
- [ ] `../figures/fig11_failure_labels.svg` in the labels section. Caption: normalised failure label for all 128 FAILs combined (underfit 51, overfit_visible_tests 49, runtime_error 11 — consolidating 9 upper-case and 2 lower-case spellings — source_invalid 9, invalid_action 5, training_failed 3); no environment split in the image; environment breakdown in the adjacent table.
- [ ] No Figure 2; no other image paths.

Numbers and boundaries
- [ ] 416 / 405 / 277 / 128 / 11 distinct; 277/405 = 68.4% is the scored-case rate; 277/416 = 66.6% is the share of selected cases with an observed PASS; unknowns receive no judgment; compile-only PASS is not behavioral validation.
- [ ] 496 case-ID frame separate from 340 rows; "design cells" not used as a definition; seed 0 stated as a property of the supplied records only; no variance or correlation claims.
- [ ] Omissions: `moco` 35, `glyph` 21 (9 + 12), `rope` 15 (10 + 5), `epistemic_games` 9; classes 56/14/10; 14 vs 24 open; no impossibility claim; 14 + 10 = 24 at most once as unverified.
- [ ] 7 scored zero-pass environments; overview's 10 and ~12 recorded as unresolved; 98 zero-pass tuples in 19 environments stated as a different count; no derivation offered as reconciliation.
- [ ] Matrix: 340; 296/44; 329/320/9; 204 + 10 (214 only with shared absence stated); 34 key names environment-specific; keys recorded for all rows including `moco`; no scale, effect, trend, or ranking; `rd_adaptive_halting` all-easy row is a recorded field, not a cause.
- [ ] `css_state_machine` withdrawn (nine rows 2/2); `sql_fixed_point` FAIL named with its tuple; one observation ≠ effect.
- [ ] Guarantees: 11 BR environments 141/189; 27 CO environments 136/216 with all 11 unscored; one guarantee per environment; confound stated; four BR and five CO among the 9/9 environments if that point is made.
- [ ] Runtime casing: normalisation as convention; uppercase ↔ `scored`, lowercase ↔ `unscored` disposition stated without explanation.
- [ ] 9 `unscored`-disposition FAILs (5 `invalid_action`, 2 `training_failed`, 2 lowercase `runtime_error`) and 10 `rejected` FAILs (8 `monadic_reward`, 1 `batchnorm_ema`, 1 `transformer_ssm_lift`) visible; caveats beside affected comparisons (`monadic_reward` 0/9, `transformer_ssm_lift` 8/9, `batchnorm_ema` 2/15); no disposition definitions invented.
- [ ] `ts_parse_only` ineligible PASS attributed to its recorded `exclusion_reason`; conflict stated; PASS kept in 277.
- [ ] Retrospective, single-campaign scope; source recorded dirty; no clean config-hash comparison; no Atria or other-post numbers; no random-selection assumption; `epistemic_games`, if discussed, described as Bayesian inference over stipulated policies.

Prose
- [ ] Local caveats at their anchors (§2.5); no ending disclaimer paragraph; no repeated one-seed paragraphs.
- [ ] Keep `[ac-word]`, `[d-word]`, `[m-word]` where their passages remain; remove transcript debris (e.g., stray "!" lines) and malformed text.
- [ ] Author's wording exclusions honoured in all public prose and proposed wording; the exclusion notation itself does not appear.
- [ ] No internal paths (other than the four figure URLs), case/trace/finding IDs, internal post IDs, Arena/reviewer/model labels, extraction instructions, or stage terminology; no blueprint citations copied into the article.
- [ ] First-person, curious, technically literate; bold reserved for the thesis and key denominators; no numerical self-ratings; no copied reference-post phrases or personal claims.
- [ ] Length about 2,000–2,800 words with compact tables; required evidence retained even if the count runs over.

---

Scope statement: this blueprint is internal editorial work on one archived campaign. It performed no new evaluation, model fitting, causal estimation, web access, SVG rendering, or code execution; the arithmetic in §1.6 is a recheck of supplied rows. The current review verdicts remain as recorded and rated; the local source check and the reconciliation note are attributed as supporting local verification, not Arena verdicts. Nothing here constitutes acceptance by the claim killer, final writer, local validator, or human review.

&&&&&&&&

grok 4.5:
Markdown
# Mercury POST-02 — Editorial Critic Blueprint (v3)
**Internal report only. Not the article. Not a winner selection. Not a stitch job.**

## 1. State and evidence-review disposition

**Inputs read (complete):**
- Writer pair: `gpt 6 luna max` and `opus 5` (full drafts).
- COMPLETE_EVIDENCE_PACKET (Tables A–D, Section E Figs 8–11 descriptions).
- COMPLETE_DIFFICULTY_MATRIX_CSV (340 rows with full `difficulty_tuple` keys).
- CAMPAIGN_PROVENANCE, EARLIER_ANALYSIS_OVERVIEW, INELIGIBLE_PASS_CSV_EXCERPT.
- CURRENT_INTERNAL_ARTICLE.
- HOUSE_STYLE + ACTUAL_REFERENCE_POST_EXCERPTS + PRIOR_WORK_REFERENCES.
- SUPPORTING_LOCAL_SOURCE_CHECK + JSON (2026-10-29).
- CURRENT_V3_EVIDENCE_REVIEW_PAIR (`grok 4.5`, `claude fable 5.1`).
- ORCHESTRATION_CAPTURE_NOTE + supporting reconciliation note.
- Pinned commit `6ed48cb1c4447d4f902d1fbc8a908a56185e34ed`.

**Arena Web Search mode:** Enabled per orchestration; reviews report access to public Mercury-2.5/Inception pages and repo landing page. No campaign CSVs, hashes, or StrangeTcy commit content retrieved externally. All factual claims rest on embedded sources. No fabrication of additional access.

**Current review verdicts (as recorded):**
- Both: “accept with corrections.”
- `grok 4.5`: 0 blocking / 2–3 corrections (moco keys, 214 wording; mild label availability) + notes.
- `claude fable 5.1`: 1–2 blocking (moco keys; “no env-by-label/guarantee breakdown”) + several corrections (214, cell phrase, judge-coverage language, 9 disposition cases, Fig 2, etc.).
- Orchestration note: both rated “Both are bad” for substantive defects. Reviewer A retained false source-availability limits; Reviewer B had inconsistent 9/9 guarantee counts and unestablished execution claims. **Useful findings preserved only after recheck against rows; neither response is acceptance or publication clearance.**

**Unresolved reviewer disagreements / gaps:**
- Strength of “unavailable” language for env×label and env×guarantee (stronger correction in claude + local reconciliation supported; breakdowns aggregable from Table B/D).
- Exact 9/9 guarantee split: local reconciliation R1 corrects to 4 behavioral_reference + 5 compile_only (not 4+6).
- Fig 2 vs Section E Figs 8–11 (neither draft’s “Figure 2” matches packet numbering; content nearest Fig 9).
- “One seed per cell” attribution (phrase not in supplied sources).
- “Judge-coverage gap” / “judging pipeline” causal language vs recorded `infrastructure_unscored`.

**Missing / unverifiable:**
- Actual SVG binary renders (Section E text descriptions only; captions/alt must not claim visual inspection).
- Exact dirty working-tree state; clean config-hash comparison (0 checked).
- Origin of overview “10” zero-pass and “~12 at 1.00”.
- Operational definitions of `rejected` / `unscored` dispositions.
- Independent causation for `ts_parse_only` exclusion_reason (recorded attribution only).
- Base rate of apparent non-monotonicity; seed variance; any new runs.

**Local verification attribution (not Arena verdict):** Supporting check + JSON + reconciliation confirm core arithmetic (416/405/11; 277/128; 17/7/12/2; 340/296/44; 329/320/9; 98 zero-pass tuples; 204 uniform-scored rows + 10 fully unscored; omission cross-tab; guarantee 141/189 vs 136/216; 9 scored-FAIL + disposition unscored; 10 rejected). 214 only when blanks included; must not be described as 214 observed success/failure outcomes.

**Handoff gap:** No fresh independent claim-killer or final human validation of these candidates beyond the supplied v3 pair + local checks. Missing current clean review of the exact pair must remain explicit.

---

## 2. Seven-dimension comparison

### 1. Argument and structure
**Reader question:** What does the single 68.4% scored-case pass rate compress, and what do the environment map + tuple matrix add (and still cannot establish)?

**Strongest source-supported thesis:** On this archived seed-0 selection of 416 cases (405 scored), Mercury-2.5 received 277 PASS / 128 FAIL (68.4%). The distribution is endpoint-heavy (17 all-pass 172/172, 7 scored zero-pass 0/68, 12 mixed 105/165 +1 unscored, 2 fully unscored). The 340-row environment×tuple matrix is mostly singleton/binary (296/340 single-case; 320/329 rated rows exactly 0 or 1; 9 fractionals all in `moco`); dimensions are environment-specific (no shared scale). Selection (80 omissions), single seed, dirty source, guarantee/environment confound, undefined dispositions, and open 14-vs-24 / 7-vs-10 discrepancies bound every causal or general-capability reading.

**Structures:**
- `gpt 6 luna max`: Cleaner linear count → endpoints → names-as-handles → matrix → withdrawn/open → unscored → 7-vs-10 → labels/guarantees → selection → confounds → supports/does-not. Slightly more compressed; ends with broken “!” + Figure 2.
- `opus 5`: Similar skeleton with stronger density/sensitivity arithmetic early, more explicit “what this does not show,” and a live Fig 2 embed. Slightly more rhetorical framing of the pooled number as “descriptively thin.”

**Move/combine/shorten/remove:**
- Progress: intelligible pooled-rate problem → exact counts + selection frame (Fig 8) → endpoint map (Fig 9) → density/names caution → tuple matrix (Fig 10) → failure labels (Fig 11) + guarantee confound → withdrawn/open + unresolved discrepancies → bounded consequence.
- Avoid audit-findings-as-essay. Shorten repeated caveat lists into point-of-use attachments. Remove any “no breakdown available” claims. Do not sequence every local-check row as prose.

### 2. Opening
**gpt:** Direct 68.4% + ts_* contrast; solid but report-like.
**opus:** “What should I expect if I open one environment at random?” + ts_*; better tension, still close to internal article.

**Proposed fresh strategy (do not draft full opening or copy either):** Open on a concrete, source-supported contrast that makes the pooled rate feel immediately insufficient—e.g., the three `ts_*` environments (4/4 vs 0/4 vs 0/4) or the sheaf split (8/9 vs 0/9 vs 0/9)—then state that 277/405 = 68.4% is the precise answer to one counting question and the rest of the piece maps what that number hides and cannot support. Ground in supplied example; establish single-seed/selected/retrospective limit within first screen. No slogan replacement; no imported reference-post scene.

### 3. Examples and technical depth
**Keep exact supported examples:**
- ts_* trio; sheaf_* split; categorical_lenses 9/9 vs functorial_augmentation 0/9 vs tensor_functor 6/9.
- Density: glyph 0/24, moco 36/55, batchnorm_ema 2/15 → 94/405 cases, 56/128 FAILs.
- css_state_machine all 2/2 (withdraw variation claim).
- sql_fixed_point single FAIL at hidden_depth=hard, surface_deceptiveness=easy (one observation; no non-monotonic effect).
- moco: 15 rows, 6 endpoint + 9 fractional (values 1/6, 1/3, 2/5, 2/3, 3/4, 5/6); complete matrix supplies keys—descriptive mapping only, no difficulty effect/ranking/scale.
- rd_adaptive_halting unscored at all-easy five-dimension tuple (missing outcome ≠ easy-case failure).
- 10 rejected FAILs (8 monadic_reward source_invalid, 1 batchnorm_ema, 1 transformer_ssm_lift); 9 scored-FAIL + disposition unscored (all 5 invalid_action, 2 training_failed, 2 lowercase runtime_error).
- ts_parse_only row performance_eligible=False PASS kept in 277; exclusion_reason = recorded provider-attribution conflict.

**Tables/figures (roles):**
- Compact env-outcome summary table (17/7/12/2).
- Mixed-env rate table (or integrate into Fig 9 reading).
- Optional compact omission table (56/14/10) + dual 14/24 note.
- Optional sensitivity arithmetic (ex-moco/ex-glyph) as illustration only.
- Fig 8 (selection frame): 496 → 80 omitted + 416; 405 scored + 11 unscored; 277+128. Caption must state 11-case segment unlabelled on image; does not plot 9 conflicting-disposition cases.
- Fig 9 (env intervals): 36 scored envs, k/n dots, 95% Wilson (binomial sampling convention, not seed variance), pooled 68.4% line; selection/dependence limit.
- Fig 10 (tuple matrix): 340 squares, 11 grey, 44 multi-case numbered; columns not comparable; 9 amber fractionals in moco.
- Fig 11 (failure labels): global 51/49/11/9/5/3; env breakdown in article table (aggregable from records).
- No new math, shared difficulty scale, or rendering dependency. Prefer parallel counts over long enumerations.

### 4. Prose and tone
**Faults to excise:** Stock transitions (“Thus,” “So I keep”); empty emphasis; repetitive global caveat dumps; mechanical benchmark-report cadence; unsupported superlatives; invented first-person experiential claims; “judge-coverage gap” causal promotion; unattributed “one seed per cell”; “no key/no breakdown available” overclaims; any excluded fragments (“If you want”, “matters”, “but wait”, “actually”, “honest”, “Let me”).

**Strengths to calibrate (not copy):** Both drafts’ first-person exploratory voice tied to arithmetic; willingness to withdraw/leave open; dry precision. Match house-style curious technically-literate judgment and self-correction (reference excerpts) without distinctive metaphors, openings, or personal claims from those posts. Epistemic-status must disclose AI-assisted drafting/revision neutrally; no invented independent human verification or dual-model authorship.

### 5. Transitions and caveat placement
Attach limits at point of interpretation:
- Selected-case denominator + 80 omissions + 14-vs-24 → with selection frame / Fig 8.
- 11 infrastructure_unscored (not failures; recorded status) + 277/416 ≠ pass rate → with first counts.
- One-seed scope / no variance → with endpoints, matrix, and any stability language.
- Selection + possible dependence → with Fig 9 Wilson reading and matrix aggregates.
- Guarantee/environment confound (each env one guarantee; 11 BR / 27 CO; 141/189 vs 136/216) → beside any guarantee contrast; not a measured judge effect.
- Undefined dispositions (10 rejected + 9 scored/FAIL/unscored) → beside affected counts/comparisons (incl. monadic_reward 0/9, transformer_ssm_lift 8/9).
- Provider-note conflict on ts_parse_only → at its PASS mention; keep in 277.
- Dirty source + no clean config-hash → beside any reproduction claim ([m-word]).
- Compile-only PASS ≠ behavioral validation; PASS/FAIL ≠ understanding/mechanism/general capability.
- Epistemic_games: bounded Bayesian inference over stipulated policies, not recursive ToM (if mentioned).
Consolidate repetition; no ending-disclaimer dump that hides qualifications.

### 6. Claim support and traceability
(See §6 Claim-check handoff for full table. Key corrections both drafts share:)
- moco keys **exist** in COMPLETE_DIFFICULTY_MATRIX_CSV (both claimed unavailable).
- 214 → 204 uniform-scored-outcome rows + 10 fully-unscored-environment rows (local check).
- Env×label and env×guarantee breakdowns **aggregable** from Table B/D (remove “not available”).
- 9 scored-FAIL + disposition=unscored must be visible alongside 10 rejected.
- Fig numbering/captions must align to packet Figs 8–11 (or descriptive match only).
- Overview 10 vs Table A 7; provenance 24 vs Table C 14; overview ~12 vs 17 all-pass: preserve as open.
Distinguish editorial preference (pacing, example order) from evidence correction.

### 7. Public-site fit
- Frontmatter exact: title/date/layout as contracted.
- Byline + five-field `<dl class="epistemic-status">` (Original ideas, Synthesis, Prose, Certainty, Importance) with supportable disclosures; neutral AI-assisted OK.
- MathJax include only if inline/display math used (plain fractions do not require it).
- Four figure URLs only: fig8_selection_frame, fig9_environment_intervals, fig10_tuple_matrix, fig11_failure_labels. No earlier Fig 2 substitution.
- Captions/alt checked against Section E / SVG descriptions (unread render ≠ visually inspected).
- Intentional tokens `[ac-word]`, `[d-word]`, `[m-word]` retained where passages remain.
- No internal paths, case/trace/finding IDs, Arena/reviewer/model labels, stage terminology, or blueprint citations in public prose.
- Clean Markdown/HTML; repair any broken embeds (gpt “!”).
- ~2,000–2,800 words; retain required evidence over mechanical length.
- Concise revision note + substantive withdrawn/open-claims disclosure.

---

## 3. Original thesis and opening strategy

**Thesis (source-supported):** The 68.4% (277/405) scored-case pass rate on this archived Mercury-2.5 campaign is arithmetically exact for one question and descriptively thin: environment outcomes are endpoint-heavy, case density is uneven, the 340-row tuple matrix is mostly single-case binary with environment-specific dimensions, and selection, single-seed, dirty-source, guarantee confound, undefined dispositions, and open record discrepancies sharply limit causal, stability, or general-capability claims.

**Reader question:** What does 68.4% hide about where the cases sit, and what can the environment + tuple maps actually support?

**Opening device:** Concrete mini-contrast (ts_* 4/4 vs 0/4 vs 0/4, or equivalent supplied split) that makes “open one environment at random” immediately awkward, then name the precise counting question the 68.4% answers and signal that the piece maps the compression and its bounds. No copied candidate/reference opening; no full draft here.

---

## 4. Section-by-section blueprint

**Frontmatter + byline + epistemic-status + revision note**  
Exact YAML. Byline. Five-field dl (retrospective archive reading; regrouping 416 + 340 matrix; first-person exploratory tied to recorded arithmetic; high on counts, low on causal given seed/dirty/unscored/guarantees/selection; importance = pooled number hides distribution and support limits). Revision note: replaces earlier version; headline 68.4% unchanged; matrix added as exploratory layer; withdrawn/open listed explicitly.

**Opening (no heading)**  
Device above. Establish 416 selected / 405 scored / 277 PASS / 68.4%; 11 infrastructure_unscored; retrospective, not new runs; environment name ≠ difficulty.

**## First, count the cases that received a judgment**  
Purpose: Fix denominators.  
Evidence: Table A/B; 277/405 vs 277/416; summary table 17/7/12/2; unweighted mean ~69.2%, median 8/9.  
Fig 8 + caption (11 unlabelled on image; 9 conflicting-disposition not plotted).  
Local caveat: unscored ≠ FAIL; selected denominator.  
Transition → map shape.

**## The endpoint-heavy distribution**  
Purpose: Show 24/36 endpoints without capability-population claim.  
Evidence: 17 all-pass list (9×9/9 + largers/smallers); 7 zero-pass; mixed table; monadic_reward 8/9 rejected; transformer_ssm_lift rejected FAIL; ts_parse_only ineligible PASS flag.  
Fig 9 + caption (Wilson binomial convention; not seed variance; selection/dependence).  
Caveat: small-n endpoints; one seed.  
Transition → names unreliable.

**## Names are useful handles, not forecasts**  
Purpose: Kill prefix-family and density misreadings.  
Evidence: ts_*, sheaf_*, category-flavoured splits; glyph/moco/batchnorm_ema density (94 cases / 56 FAILs); optional sensitivity arithmetic as illustration.  
Caveat: no shared mechanism inferred.  
Transition → tuple layer.

**## A second layer: the environment × tuple matrix**  
Purpose: Exploratory description of arrangement, not difficulty effects.  
Evidence: 340 rows; 296 singleton / 44 multi (moco/glyph/css/epistemic_games); 329 rated / 320 endpoint / 9 fractional (moco); 34 dim names environment-specific; 98 zero-pass tuples in 19 envs; **204 uniform-scored rows + 10 fully unscored** (or 214 only if shared absence explicit).  
Fig 10 + caption.  
### What a “cell” means: all seed 0; cell ≈ env×tuple row by arithmetic inference (do not quote unattributed “one seed per cell”); no within-tuple dependence estimate.  
### moco: only fractionals; keys exist in complete matrix—optional compact descriptive map of 9 fractionals; no shape/effect claim; overall 36/55.  
Caveat: single-case rows make 0/1 unsurprising; no cross-env scale/ranking/regression.  
Transition → withdrawn/open.

**## Claims withdrawn or left open**  
Withdraw css_state_machine non-monotonic (all 2/2).  
Open: apparent moco / sql_fixed_point patterns (single seed, mostly binary, no base rate); sql one FAIL location noted without effect claim.  
Disclose 7 vs overview 10; 17 vs ~12; 14 vs 24 known-gate (identity 14+10=24 possible but unverified).  

**## Unscored cases are not failures**  
11 = 6 epistemic_silence + 4 epistemic_type_games + 1 rd_adaptive_halting (all-easy tuple). Recorded status infrastructure_unscored. rd remains 8/14 +1.  

**## Failure labels and judge guarantees**  
Fig 11 global + article env-breakdown table (aggregable; descriptive only; labels ≠ mechanisms). Runtime 9 RUNTIME_ERROR (scored) + 2 runtime_error (unscored disposition)—convention, no cosmetic mechanism.  
9 disposition=unscored FAILs + 10 rejected visible; undefined; stay in 128.  
Guarantees: 189 BR / 227 CO; per-env constant (11/27); scored 141/189 vs 136/216 +11 unscored in CO; **confound, not judge effect**. Compile-only PASS ≠ behavioral validation.  

**## The selection frame**  
80 = 56 twin + 14 known-gate + 10 modality (all rope); totals by env 35 moco / 21 glyph / 15 rope / 9 epistemic_games. Dual 14/24 open. rope absent from 38. Flags: rejected, unscored-disposition, ineligible PASS.  

**## Confounds that remain**  
Single seed 0; dirty source [m-word]; selection/dependence; guarantee confound; undefined dispositions; open discrepancies. No Atria/other-campaign numbers.  

**## What this supports—and what it does not**  
Restate 277/405, 17/7/12/2, matrix descriptive facts.  
Does not: common difficulty scale or env-vs-difficulty ranking; mechanisms for glyph/moco/batchnorm; seed stability; uniform-judge counterfactual; clean-source effect; understanding/general capability.  
Keep 68.4% for the precise counting question; map + bounds are the informative answer.  
Optional bounded next step (repeated seeds) without new-run claim.

**Withdrawn/open disclosure** already integrated; ensure visible.

---

## 5. Retention and reconstruction decisions

**Useful from gpt 6 luna max:** Tight count-first progression; clear withdrawn/open section; restrained tone; good endpoint/mixed separation; intentional [m-word].  
**Remove/narrow:** Broken “!”/Fig 2; moco “no key”; 214 unglazed; “judge-coverage gap”; light treatment of 9 disposition cases; global-only label implication.

**Useful from opus 5:** Density/sensitivity arithmetic; stronger “what this does not show”; live figure attempt; explicit thinness of pooled number; good monadic_reward/rejected handling.  
**Remove/narrow:** moco “no key”; repeated “no breakdown available”; 214; “unrolled” mechanism language; Fig 2 path/caption mismatch with packet; over-general “behaviourally settled.”

**Neither handles adequately (blueprint must supply):**
- Exact 204+10 uniform distinction with shared-absence language.
- Visibility of both 10 rejected and 9 scored/FAIL/unscored disposition.
- Aggregation-available env×label and env×guarantee stated as recorded cross-tabs + confound limit.
- moco keys present → descriptive option without effect claim.
- Fig 8–11 alignment + caption fidelity to Section E (Wilson convention, unlabelled 11, grey 11, etc.).
- Overview ~12 vs 17 noted beside 10 vs 7.
- Guarantee split on 9/9 envs (4 BR + 5 CO) if discussed.
- Provider field contrast (prose 1 retry/60s vs http_attempts 19 / 46.1s) left unresolved.
- Clean public voice free of internal labels while preserving every numerical boundary.

Do not stitch quoted paragraphs. Reconstruct argumentatively from evidence.

---

## 6. Claim-check handoff

| Candidate quotation / location | Source / v3 finding | Required action | Remaining limit |
|---|---|---|---|
| Both: moco “no row-by-row key / cannot draw shape / missing key” | COMPLETE_DIFFICULTY_MATRIX_CSV all 15 moco keys; grok #1, claude #1 (blocking) | Replace: keys present in complete matrix; optional descriptive fractional map; pattern stays open | No difficulty effect, ranking, or shared scale |
| Both: “214 of 340 (63%) … same outcome” | Local check: 204 uniform-scored + 10 fully unscored; grok/claude + reconciliation | Reword to 204+10 (or 214 only with explicit shared-absence) | Blanks ≠ observed success/failure |
| opus (strong): “No environment-by-label breakdown is available”; “nothing … supplies” env×guarantee/label | Table B/D fields; local failure_cross_tab / guarantee tabs; claude blocking + R4 | Delete unavailability; report aggregated descriptive counts | Not controlled comparison; labels ≠ mechanisms; guarantee confounded with env |
| gpt: “counts are global only; do not show which environments…” | Same | Soften; supply breakdown table | Same |
| Both (implicit/light): 10 rejected only | Table B + JSON: also 9 scored+FAIL+disposition unscored | Make both visible; undefined; stay in 128 | No operational definitions |
| Both: “judge-coverage gap” / “judging pipeline” | status=`infrastructure_unscored` | Use recorded status label | Cause not established |
| Both: “one seed per cell” (quoted or as campaign record) | Phrase absent from supplied sources; all seed=0 in Table B | Drop unattributed quote; state all selected seed 0 | No variance estimate |
| Both Fig 2 lollipop / broken embed | Section E = Figs 8–11; nearest content = Fig 9 | Align to fig9 (or 8–11 set); caption = Wilson, pooled line, binomial convention, no unscored envs; repair MD | Unread SVG ≠ visual inspection |
| Both: 7 zero-pass vs overview 10 | Table A=7; overview=10; tuple=19 | Keep 7; leave 10 open | Do not invent filter |
| Add: overview “~12 at 1.00” vs 17 | Table A/Matrix=17 (172/172); R2 | Note unresolved beside 10-vs-7 | No invented rule |
| Both: 14 vs 24 known-gate | Table C=14 (9 glyph+5 rope); provenance=24 | Report both; open; 14+10=24 unverified | Do not double-count or assert coexistence impossibility beyond frame arithmetic |
| Both: ts_parse_only ineligible PASS | Excerpt + row 409: PASS, eligible=False, exclusion_reason provider-attribution | Keep in 277; flag conflict; recorded attribution only | Not independent proof of cause; retry/time fields unresolved (R3) |
| gpt/opus guarantees “cannot compare under common standard” because totals only | Per-env constant; 141/189 vs 136/216 | Reword to confound (no within-env variation) | Not measured judge effect |
| Optional 9/9 guarantee split | R1: 4 BR + 5 CO | If mentioned, use 4+5=9 | — |
| css non-monotonic | All rows 2/2 | Withdrawn | — |
| sql_fixed_point / moco non-monotonic | One FAIL location; moco fractionals | Open, not findings | Single seed, no base rate |
| Runtime casing | 9 upper scored + 2 lower unscored disp. | Normalize to 11 for display; note association | No cosmetic/mechanism claim |
| Epistemic_games (if used) | Task evidence | Bayesian stipulated policies, not recursive ToM | — |
| Dirty source / reproduction | Provenance dirty=true; 0 clean hashes | [m-word]; no clean comparison | — |

**Editorial preferences (not evidence corrections):** Opening contrast choice (ts_* vs sheaf); whether to print full 9 moco fractional key table vs prose summary; exact sensitivity rows; heading wording; length within 2–2.8k while retaining evidence.

**Refer to next claim-check:** Any residual SVG pixel-level caption match; final public-link verification; unresolved overview/provenance origins if new primary sources appear. Do not invent answers.

---

## 7. Final writer checklist

- [ ] Frontmatter exact:  
  ```yaml
  ---
  title: "What a 68.4% Pass Rate Hides: Mercury-2.5 Across 38 Environments"
  date: 2026-10-16
  layout: post
  ---
 {% include mathjax.html %} only if real math used (immediately after frontmatter).
 Byline: *by <span class="icon-self">StrangeTcy</span>*
 <dl class="epistemic-status"> five fields in order, supportable text; neutral AI-assisted drafting/revision OK; no invented human verification or dual external authorship.
 Concise revision note + substantive withdrawn/open disclosure.
 Figures only:
../figures/fig8_selection_frame.svg
../figures/fig9_environment_intervals.svg
../figures/fig10_tuple_matrix.svg
../figures/fig11_failure_labels.svg
Captions/alt match Section E (11 unlabelled; Wilson binomial ≠ seed var; 340/11 grey/44 multi; global labels + table breakdown).
 Intentional tokens [ac-word], [d-word], [m-word] preserved; accidental debris gone.
 Numerical boundaries: 416/405/11; 277/128; 68.4% (277/405) vs 66.6% (277/416); 17/7/12/2; 172/68/165; 340/296/44/329/320/9; 98 tuples/19 envs; 204+10 uniform; 51/49/11/9/5/3; 189/227; 141/189 & 136/216; 80=56+14+10; dual 14/24; 10 rejected + 9 unscored-disp; ts_parse_only PASS kept; all seed 0; 7 (not 10) scored zero-pass; css all 2/2 withdrawn; moco keys usable descriptively; no shared scale/ranking/causal/seed-variance/clean-hash.
 Local caveats at point of use (selection, seed, dirty [m-word], confound, dispositions, open discrepancies, compile-only limit).
 No excluded word fragments in public prose.
 No internal paths, IDs, Arena/reviewer/model labels (gpt 6 luna max/opus 5 etc.), stage terms, or blueprint citations in public text.
 Public citations only verified usable links supporting adjacent claim (prior-work list discipline).
 ~2,000–2,800 words; evidence retained over word-count pressure.
 Clean Markdown/HTML; no broken embeds; house-style voice/pacing without copied distinctive phrases.
 Retrospective single-campaign scope only; no new evals, fitted models, or cross-campaign imports.

End of blueprint. Do not produce the article, dispatch stages, or claim claim-killer / final-writer / local-validator / human-review passage.