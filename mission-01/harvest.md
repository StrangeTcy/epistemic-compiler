# Mission 01 harvest: durable methodology carried forward

**Status.** Written 2026-10-02 by the compiler agent, on the instruction of the revised Arena brief
(`mission-02/sources/raw/2026-10-02_instruction_revision.gpt_5.6_luna.md`, TENTH section). Contains only
durable, evidence-backed methodological or benchmark objects from Mission 01, each with its evidence
path. Does not rewrite, reopen, or qualify Mission 01's scientific conclusions: those stand frozen in
`claim_set.md` (Gate 4 `APPROVE_BOUNDED`, pre-registration `cbd4e4a`), and nothing here changes them.
No frozen file was modified to write this one.

## H-1. Judge hardening by designated bypass variants (method)

Hand-constructed candidate variants that deliberately bypass the intended law are scored by BOTH the
judge in use and an independently specified reference oracle, under a fixed seed, with discovery/holdout
stratum separation and black-box exclusion of the judge from variant construction. The method produced
Mission 01's central operational numbers (Type I false-pass 1/12 hardened vs 4/9 unhardened
environments; evidence: `results/part_a_stratum_a1.json`, `results/part_a_stratum_a2.json`,
`results/blackbox_hashes.json`; claim C01 in `claim_set.md`). Durable because it is the cheapest known
way to show a judge can be fooled, and Mission 04 reuses it as the day-one hardening step for its new
environment family (`mission-04/design.md` section 7).

## H-2. Shared-dispatcher agreement validates nothing (negative lesson)

Grader B agreed with the truth oracle on 170/170 evaluations (`results/summary_metrics.json`, M04) —
and the agreement was worthless as independent validation, because `evaluate_grader_b()` calls the same
dispatcher as the oracle (`claim_set.md`, C01 remaining-uncertainty paragraph). Durable rule: two
verifiers validate each other only if their code paths differ; Mission 04 registers a closed-form
oracle cross-checked by exhaustive enumeration in separate modules (`mission-04/design.md` section 7).

## H-3. Hardened and unhardened judges behave differently (finding, method-relevant)

FALS-01 measured the judge's own sensitivity: error rates shifted 3.57 points on the pre-hardened
REFERENCES stratum versus 9.25 points on the unhardened compile-only stratum
(`falsification/falsification_results.json`, FALS-01; claim C01). Durable because any new benchmark
family must report whether its judge was hardened before model runs, and should include a
variant-count sensitivity check (FALS-01 pattern) rather than a single variant count.

## H-4. Valid-alternative audit with a zero-syntax-error control (method)

`reference_alt` variants were checked for syntax/import errors before counting judge rejections
(CTRL05: 56/56 clean, `falsification/falsification_results.json` FALS-02), separating "judge rejects a
valid solution" from "variant was broken". Durable as the template for any Type II audit, including
Mission 04's degenerate-policy hardening, where a policy must be shown well-formed before its score is
interpreted.

## H-5. Measurements whose inputs are not produced by the pipeline are not adjudicable (process lesson)

Gate 4 quarantined M07 and M08 because their inputs were hard-coded source constants rather than
measured quantities, and invalidated M10 because the underlying log was incomplete
(`claim_set.md`, "Quarantined measurements"; `reviews/post_run_analysis_errata.yaml`). Durable rule for
every later mission: a measurement exists only when its inputs are artifacts of the executed pipeline;
hard-coded intermediates are hypotheses, not evidence.

## H-6. Finite deterministic enumeration before any sampling claim (method)

Part B's deterministic generator enumerated 162 workspace variants exactly, and its falsification
comparisons were margins on that finite set (`results/part_b_multichart_gluing.json`; claims C03;
`falsification/falsification_results.json` FALS-03/03b). Durable because Mission 04's instance space is
likewise finite and small, and its design enumerates rather than samples (`mission-04/design.md`
section 5), and because the finite-set framing kept Mission 01's claims honest under a failed headline
threshold.

## H-7. Claim-ceiling and quarantine discipline (process)

The claim set's explicit cannot-justify list and the per-claim ceiling checks (`claim_set.md`,
sections "Explicit cannot-justify list" and each claim's CLAIM CEILING CHECK line) allowed an
inconclusive mission to ship bounded findings without overreach. Durable as the template every later
claim set should copy; Mission 04's seed carries a matching `candidate_claim_ceiling` block.

## Not harvested

Scientific conclusions (H0–H5 dispositions), the sheaf/presheaf framing and its frozen labels, council
records, and anything in `spec/approved.yaml` beyond what the claims cite — all remain Mission 01's
frozen business. Known Mission 01 weaknesses that are NOT durable assets: leading council prompts, no
Mindcluster context at run time, and an incomplete real-time log (all recorded in `claim_set.md`);
later missions should treat those as things to avoid, and Mission 04's design does (compiled context
packs in `mission-04/context/`, deterministic artifact logging specified in `mission-04/design.md`
section 10).
