# Council round 1: intake log

The compiler's running notes on each response as it is stored: how it conforms to the required output format, which of its checkable claims were checked and how, and what it asks of the seed. This is the compiler's reading, not part of the Council record, and it decides nothing. All four Council roles are stored. The human chose to keep the earlier Arena dialogue in `mission-02/sources/2026-09-29_arena_round_note.md` separate from round 1. The compiler-prepared cross-critique is in `mission-02/council/cross_critique.md`; it is a comparative synthesis, not source verification or a gate decision. Gate 1 remains an explicit human decision. Legacy response files retain their original formatting; workbench-ingested response bodies are preserved unedited with provenance in `.intake.json` sidecars.

| Role | Stored | File | Format | Checked claims |
| :--- | :--- | :--- | :--- | :--- |
| Theorist (P01-T) | 2026-10-02 | `theorist.md` | sections 1 to 9 of 10; section 10 absent and not declared cut; 4,261 words against a 3,500 guide | the 3 claims that could be checked all hold |
| Experimentalist (P02-E), two samples | 2026-10-02 | `experimentalist.a.md` ("opus 4.6"), `experimentalist.b.md` ("fable 5.1") | all 10 sections in both; 3,630 and 3,674 words against a 3,500 guide; b's section 1 heading is glued to a preceding sentence | the claims that could be checked hold; both responses' power figures are slightly optimistic |
| Skeptic (P03-S), two samples | 2026-10-05 | `skeptic.a.md` (`opus 5`); `skeptic.b.md` (`gpt 6 luna max`) | sections 1–7 in both; **a** declares cuts for length; wrapper metadata recorded separately | not yet checked |
| Prior-Work Killer (P04-PW), two samples | 2026-10-02 | `prior_work_killer.a.md` ("fable 5"), `prior_work_killer.b.md` ("gpt 6 luna max") | all 7 sections in both; a has a duplicated header block glued to search narration | not yet checked |

For the pre-workbench Theorist, Experimentalist, and Prior-Work Killer artifacts, no structured intake sidecars exist; this log records missing Arena mode, Arena-displayed model label, session time, and tool-presence metadata, with model names only self-reported. For the Skeptic pair, the bundle supplies self-reported model and tool details plus role/prompt labels, but not Arena mode, the exact Arena-displayed model label, or session time. These self-reports are not independently verified; see each `.intake.json`.

## Theorist (P01-T)

**Conformance.** Header lines present. Evidence tags: 19 x [R], no [V] or [S]; it says it had tools available but used none, so every external claim is recalled. Role-prefixed ids T-A01 to T-A10 and T-H0 to T-H8 minted as instructed. **Section 10 (qualitative outcome table, P01-T-10) is absent and was not listed under "cut for length"**, which names only the action-model definitions and a power estimate. About 22% over the length guide.

**Checked on 2026-10-02.**
1. The ten relations it calls dubious all exist in `knowledge/edges.yaml` (edges 004, 005, 038, 138, 166, 009, 081, 085, 086, 080). None was invented. Whether each is wrong is a literature judgment, tagged [R] and not checked.
2. A real data error: `bernheim-1984` and `pearce-1984` carry the same title ("Rationalizable Strategic Behavior") and the same JSTOR link in the graph. The importer reproduces the user's HTML export faithfully, so the fault is in the source graph and the fix belongs there, followed by a re-import. Pearce's own paper has a different title [R].
3. Its recalled claim about L01 is confirmed by the paper (read two of four chunks of the PDF, Findings of EMNLP 2023): labels come from the SMCDEL model checker (an S5 announcement logic); code and data are public; 2 to 4 agents, belief order up to 2, announcements restricted to first-order beliefs; a small trained classifier flags examples with shortcut cues, which is precedent for the Theorist's shortcut certificate.

**Not checked.** L02 (neither it nor the compiler has read it); the Hi-ToM order claim; every other [R] literature claim; the construction of SCH-1 to SCH-4 (no generator or verifier exists), including its prediction that the semi-public variant of SCH-1 typically gives "never".

**What it asks of the seed** (for Gate 1; none applied):
1. **Strata.** Define S2 from validity conditions declared independently of the cards (publicness, truthfulness, protocol, prior, incentive alignment, commitment, dominance type), then map cards onto them at Gate 2. Leave the leaking validity features undeclared in problem states, because declaring them makes S2 empty by construction.
2. **Q-A reframed.** One finite probabilistic epistemic model; level-k and rationalizability as generators of behaviour tables, not as semantics; reject belief revision and equilibrium-selection questions; keep v0 as the control subfamily.
3. **Certificates.** A depth certificate (a (k-1)-bisimilar witness model with a different answer) and a shortcut-failure certificate against a registered set of naive programs (B1 to B6).
4. **Reuse.** Use L01's generator and SMCDEL as source and verifier for the public-announcement subfamilies; build only the rest (T-H8).
5. **Controls and hypotheses.** A generic-enumeration arm (T-H3); a validity-clause warning with no method (T-H7); a scored parse of the formal spec; load crossed with depth (T-H6).
6. **Verdict.** "Do not proceed as framed", with the reframed Q-A and strata that do not depend on the cards. Its strongest argument is that H3 is close to true by construction: on a finite explicit semantics, full enumeration is always valid, so a card can only help by being a valid shortcut.

**Compiler observations** (from the five frozen cards, which the Theorist did not see and which were written independently of it):
- **Card A as written has the problem the Theorist describes.** Its trigger feature `public_events_change_what_agents_know` already says events are "available to all agents", and its exclusion is the negation. A semi-public instance fires the exclusion or fails the trigger. It does not sit as "trigger present, move invalid".
- **Convergence.** Six of the Theorist's nine declared validity conditions have a matching obligation in a frozen card: publicness, truthfulness and protocol (card A, OB3, OB4, XC1), knowledge versus belief (B, OB1), policy status (C OB1, E OB1), dominance type (D, OB3, OB4). The three with no card are the common prior, incentive alignment and commitment, which are exactly the agreement, signalling and persuasion cards the library lacks.
- One voice, not corroboration: the Theorist's doubts about Q-B's design are consistent with the case in `mission-03/DESIGN.md` for testing the Strategy IR's central claim on existing tasks first.

**Open.** Substantive review of the other Council roles; the missing Arena metadata; the Pearce/Bernheim correction in the source graph.

## Experimentalist (P02-E), two samples

Two answers to the same prompt arrived together: **a** is labelled "opus 4.6" and **b** "fable 5.1" (the user's labels; each response self-reports "Claude", which is not reliable). Neither saw the other, or the Theorist.

**Conformance.** Both have the header lines and all ten required sections, and neither shows the insertion artifact seen in the Theorist's text.
- **a:** 3,630 words, though it states "about 3,400, nothing cut". Tags: [V] x1, [S] x2. Mints E-M01 to E-M05, E-CTRL01 to 06, E-T01 to 08, E-O01 to 05.
- **b:** 3,674 words; declares what it cut (a numeric power table, F2 construction detail, a tolerance spec). Tags: [S] x4, [R] x1. Mints E-M01 to 05, E-CTRL01 to 10, E-T01 to 09, E-O01 to 10 and one new confound, E-CF12. Its section 1 heading sits on the same line as a preceding sentence ("...independent verifier.## 1. Kill attempt"), so a strict parser would miss it.

**Checked on 2026-10-02.**
1. **b's named repository exists.** `sileod/llm-theory-of-mind` is public, Apache-2.0, last pushed 2026-07-03, with a small generator (`src/`: about 600 lines across three files). The Hugging Face dataset `sileod/mindgames` exists: 18.6k rows (train 11.2k, validation 3.73k, test 3.73k), with an `smcdel_problem` field, 2 to 4 agents, 0 to 4 announcements, hypothesis depth 0 to 1, and a trained-classifier difficulty score.
2. **a's [V] claim is real.** Its MindGames quote is verbatim from that repository's README.
3. **A reuse cost neither response mentions.** The generator labels each problem by POSTing it to a third-party SMCDEL web service (`https://tools.malv.in/smcdelweb/check`) with browser-spoofed headers. An independent, reproducible verifier would need a local SMCDEL install, or the dataset's shipped specifications and labels, not the generator's web call.
4. **Power figures, recomputed with the exact McNemar test** under the assumptions both state (baseline 0.45, effect 0.15, correlation 0.3, so discordance 0.364). 133 instances give 80% power. a's "about 105" gives 68%; a's "about 65% at 80 instances" is 54%; a's "about 80% for 20 points at 80 instances" holds (81%); a's "above 25 points at 17 pairs" is true but understated (even 40 points reaches only 69%). b's "100 to 130 instances" is close to 133; its "about 40% at 48 pairs" is 33%; its "25 points needs 40 to 50" is 50 and "about 80% at 48 pairs" is 79%; its Wilson half-width at 12 trials is 0.25, not 0.27. Both are slightly optimistic. Neither conclusion changes.
5. **b misattributes a source.** It says the control prose comes from "the strategy_ir.md 'generic explicit model' wording". That phrase is not in `strategy_ir.md`; it is the seed's H3 text. The Council saw only section 10 of the spec.
6. **a is internally inconsistent.** Section 2 plans 2 solvers x about 66 instances (396 dispatches); section 5 plans 1 solver x 133 instances (399).

**Not checked.** Both responses' recalled claims about prompting effects; L02 and GTBench quotes (a's match the abstracts seen earlier in this project); b's proposed nonsense lexicon, classifier thresholds and 24-paste test-retest subset (nobody has built them).

**Where the two agree.**
- **Scale:** 60 pastes cannot decide H1 to H3. They can only check for floor and ceiling and exercise the pipeline. 400 pastes give modest power.
- **Registration:** one primary solver, three primary arms (P, L, N), random cards dropped (a) or secondary (b), and one primary contrast, P minus L on S1, paired by instance.
- **Design details:** schema-level characterization; an independent verifier and a MindGames cross-check; leakage audits; opaque ids and a sealed key; a pilot with a floor/ceiling rule; "uninformative" kept distinct from "null".
- **The gate text:** both fault it for naming no primary contrast, no sample size, and no headroom or verifier precondition.

**Where they differ.**
- **Solver channel.** a makes at least one API solver a condition ("without it session variance alone can mask or fabricate any effect"). b keeps arena paste and adds controls for it: a test-retest subset, a pack-only leak probe, framing rotation, a surface-feature classifier, a tool-use declaration.
- **Margin.** a recommends 12 points; b fixes 15.
- **Extras.** a adds a staleness clause for the gate. b adds a point a does not make: **for a fixed schema every S1 instance receives the same pack, so retrieval contributes no variance; the registered Q-B compares one fixed paragraph with another, a prompt A/B and not a test of the Strategy IR.**

**What they ask of the seed** (for Gate 1; none applied):
1. Name one primary contrast (P minus L on S1) and fix a minimum sample size and a margin.
2. Make headroom (H5) and independent verification (H4) preconditions in the gate, with an "uninformative" outcome distinct from a null.
3. Characterize at the schema level, and say that this tests obligations, not characterization.
4. Use at least one API-driven solver (a), or add test-retest and session controls (b).
5. Merge H0 and H3, since a P/L/N design cannot tell them apart (b).
6. Disclose who wrote the control prose, not only the cards.

**Compiler observations.**
- **b's retrieval point is the one that matters most** and is the same concern that shaped `mission-03/DESIGN.md`: trigger selection can only be tested by applying a card where its trigger does and does not hold.
- **Mission 03's channel.** It uses the existing API-driven runner, which is a's condition (c).
- **On S2.** Both treat S2 as something that can be planted mechanically. Neither notes that, with the frozen cards, a private announcement would fire card A's exclusion; the Theorist's concern applies. b's rule that a card whose method cannot be made mechanical gets no S2 cell is compatible with the Theorist's proposal.
- **On obligations.** b's seventh critique is accurate for the IR as built: obligations are prose shown to the solver, and the validator checks only recorded statuses, so only the solver's response to prose can be tested.

**Open.** Substantive review of the Skeptic pair and Prior-Work Killer responses; remaining Arena metadata; whether to adopt a local SMCDEL install for the verifier.

## Skeptic (P03-S), two samples — intake only

The tracked source bundle `skeptic_prompt_responses` remains unchanged. Its two labeled sections were split in source order: **a** = `opus 5`; **b** = `gpt 6 luna max`. The canonical response bodies begin at the first Markdown heading; wrapper labels/headers and the section separator are recorded in each `.intake.json`. Both contain sections 1–7; **a** also declares material cut for length. No Skeptic response claims have been independently checked. The comparative synthesis is in `cross_critique.md`; it is not verification of those claims.

**Provenance supplied in the bundle (self-reported, not independently verified).** Both identify role P03-S and prompt ID M02-P03-S v1 and report no other roles' output. **a** reports Claude (Anthropic), Sonnet-class, browsing used (four web searches), and code execution used for a power calculation. **b** reports ChatGPT with the exact serving-model label unavailable, browsing yes, and code execution no. Arena mode, exact Arena-displayed model label, and session time were not supplied; each sidecar records those required fields as missing.

## Prior-Work Killer (P04-PW), two samples

Two answers to the same prompt arrived together: **a** is labelled "fable 5" (self-reports Claude) and **b** "gpt 6 luna max" (self-reports ChatGPT). Neither saw the other or any other role. Stored verbatim on 2026-10-02; checking of their claims is pending.

**First reading (not checked).**
- **Verdicts:** both REFRAME Q-A (reuse MindGames/SMCDEL; the residue is behaviour generated from explicit utilities/policies). On Q-B, a says PROCEED (narrowed) and b says REFRAME.
- **Coverage:** a ran 5 searches and leaves L02, L04, L05, L07, L08 unchecked; b reports L01 to L07 checked, L08 unchecked.
- **b's strongest new item:** TRS ("Thinking with Reasoning Skills", ACL 2026 Industry), trigger-retrieved cards with `Trigger / Do / Avoid / Check / Risk` fields. a does not cite it, which weakens a's Q-B PROCEED. b also asks for a with/without-obligations arm and a distinct generic-modelling control for H3.
- **a's distinctive items:** ExploreToM, DEL-ToM, AutoToM, ToM-LM, MCMAS/DEMO/MCK, and a recalled ([R]) bibliographic audit flagging suspect identifiers on `aumann-1976`, `baltag-moss-solecki-1998`, `camerer-ho-chong-2004`, `rubinstein-1989` and the Plaza dating. Both repeat the Bernheim/Pearce duplicate JSTOR link already found by the Theorist.
- **Disagreements to check:** Hi-ToM author order (a: He first in the ACL PDF; b: Wu first); ExploreToM accuracy figures (a notes 0%/9% vs 5% across versions).

**Open.** Verify TRS, L02 and the [R] identifier flags; review the Skeptic pair; resolve remaining Arena metadata.
