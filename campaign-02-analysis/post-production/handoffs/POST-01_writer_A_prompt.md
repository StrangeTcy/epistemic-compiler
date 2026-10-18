BATTLE WRITER A — POST-01: The Model's Belief Is Right; Its Decision Is Fragile (Mercury-2.5)

You are Writer A, an independent candidate producing a complete research essay for the StrangeTcy public site. You receive the evidence packet and reviewer brief below. Writer B will receive the same packet separately and must not see your draft.

ARTICLE SLOT: POST-01 — Belief/decision dissociation (primary mechanistic article).
RESEARCH QUESTION: Does Mercury-2.5's stated belief track content while its terminal decisions are fragile to presentation order and proxy channels?

EVIDENCE PACKET (verified against source snapshots and findings register)

T1 same_fact_presentation probe:
- 6 cells × 6 seeds = 36 matched pairs.
- 0/36 belief flips (posterior identical in both presentation orders in every trial).
- 5/36 terminal answer flips (all 5 are correctness flips — right in one order, wrong in the other).
- 17/36 diagnostic-choice divergences (which evidence to inspect/request next).
- 3 fact counts (3, 4, 5) × 2 priors (1/2, 1/3) = 6 cells.
- Canonical bullet order vs reversed numbered order.
- Oracle is exact; correctness is not in dispute.

Epistemic games:
- 23/23 exact posterior match (base scenarios + evidence/presentation/prior interventions).
- Zero posterior error in all 23 cases.
- posterior_reported equals posterior_true in every case.

Proxy interventions:
- visible_proxy: 8/27 pass (0.30).
- reward_proxy: 1/4 pass (0.25).
- base: 228/331 pass (0.69).
- Paired flips: 7 pass→fail under interventions (4 visible_proxy), within 76 intervention cases sharing a latent spec with a base case.

Campaign context:
- 416 selected cases across 38 environments; 405 scored; 11 unscored.
- 277 PASS / 128 FAIL; scored pass rate 0.684.
- Judge guarantees: 189 behavioral_reference, 227 compile_only.
- Single seed per selected cell; source repo dirty at run time.
- 56 of 132 twin cases unverified.

Limitations:
- Single model/provider (mercury-2.5, reasoning_effort=high).
- T1 sample: 36 pairs; no confidence intervals.
- Intervention cases not difficulty-matched.
- Terminal-answer extraction may be brittle.
- No independent replication.
- Single seed per selected cell (campaign-wide).

REVIEWER BRIEF (accepted Stage A) — key points to respect:
- The strongest defensible thesis is the narrow behavioral dissociation: stated belief was order-invariant (and content-tracking in epistemic games), while terminal decisions and diagnostic choices were not. This is a clean, narrow, well-supported claim.
- NOT defensible: stitching T1 (belief/decision probe) and proxy-intervention campaign (pass/fail scoring) into one "decision layer" narrative. These are incommensurable experiments — T1 measures belief-elicitation/terminal-answer/diagnostic-choice on an oracle-exact probabilistic task; proxy interventions use judge-guaranteed pass/fail scoring on coding tasks. Nothing establishes they test the same construct.
- NOT defensible: "pass rates from 0.00 to 1.00" — not in the evidence packet.
- NOT defensible: judge guarantees (189/227 = 416) attached to "405 scored cases" — they partition the 416 selected cases.
- NOT defensible: "wrong in one in seven of those" — all 5/5 flips are correctness flips (100%), not 1/7.
- NOT defensible: "56 unverified twin groups" — should be "56 of 132 twin cases unverified (~42%)."
- Missing caveats: single seed per cell (campaign-wide), intervention taxonomy gap (76 intervention cases but only 31 disclosed as visible/reward proxy), non-independence of T1 and epistemic games, extraction brittleness as alternative explanation for terminal flips.
- "Exact source identity is unresolved" is an inference from "dirty repo," not a direct packet claim.
- Difficulty confound for proxy pass rates is live, not dismissed.
- The title "Belief Is Right" is strongest for epistemic games (23/23 exact); T1 shows invariance, not explicit per-trial correctness tally.
- Tone: remove profanity ("fuckingly"), stray 🤥 glyph.

STYLE REFERENCE
- Jekyll frontmatter: title, date, layout: post. No extra fields.
- Byline: *by <span class="icon-self">StrangeTcy</span>*
- Epistemic-status <dl> with five fields: Original ideas, Synthesis, Prose, Certainty, Importance.
- First-person, curious, technically literate, self-correcting.
- Concrete cases, exact counts, caveats beside claims.
- No internal file paths/finding IDs/trace IDs/draft labels in public copy.
- Target ~1800-2800 words. Do not inflate.

TASK
Write a complete, independently structured research essay (not an outline, not a summary) for POST-01. Lead with a real question or tension. Present the T1 dissociation as the narrow, defensible core. Present proxy interventions as a parallel, independent line of evidence — NOT as the same "decision" construct. State exactly what the evidence establishes and what it cannot. Embed at least one figure with a caption. Place caveats where needed. Do not stitch incommensurable experiments into one narrative. Do not imply internal mechanisms ("belief layer," "decision layer," "downstream"). Do not make general evaluation prescriptions beyond what the evidence supports.

OUTPUT: the full article markdown only.
