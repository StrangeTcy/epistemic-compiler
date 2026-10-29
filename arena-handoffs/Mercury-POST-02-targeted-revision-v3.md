# Mercury POST-02: targeted revision proposal

The final Arena articles remain unchanged. Local validation fails A on the five evidence-scope issues below; B has no blocking findings. These are exact proposed replacements for A, prepared for the pipeline’s human revision gate. No stylistic rewrite or candidate selection is proposed.

## A-S01 — line 11

**Current wording**

> Recorded verdicts for 416 cases in 38 environments

**Proposed replacement**

> Records for 416 selected cases in 38 environments

416 counts selected records. Only 405 have a verdict; 11 have blank verdict and status infrastructure_unscored. The later body states this correctly, but the epistemic-status summary blurs the distinction.

Evidence: cases: status/verdict grouping across all 416 rows; packet Table A and Table B

## A-S05 — line 46

**Current wording**

> The records say nothing about how selection was done, so I assume neither random nor targeted selection.

**Proposed replacement**

> The records explain these exclusions but do not establish a general sampling scheme, so I infer neither random nor targeted sampling.

The detailed omission records do explain exclusions through modality limits, known gate failures and unsuccessful twin checks. The broader sampling scheme is not established, but denying all selection information contradicts the supplied omission reasons. Preserve the known filters while declining to infer random or targeted sampling.

Evidence: omissions grouped by exclusion_class, reason and disposition: 10 unsupported_provider_input_modality / provider_input_modality_unsupported / omitted_before_scoring; 14 known_gate_calibration_failure / known_gate_blocked_calibration_failures / omitted_before_provider_access; 56 intervention_twin_omission / twin_check did not return pass, so the overlay's equivalence expectation is unproven for this instance / omitted_before_provider_access.

## A-S02 — line 119

**Current wording**

> `moco` is the one environment whose rows vary.

**Proposed replacement**

> `moco` is the only environment with fractional pass rates within tuple rows.

Other mixed environments vary across tuple rows. MoCo alone has fractional PASS fractions within a row. For example, batchnorm_ema has 0.0 rows and 1.0 rows, so the unqualified across-row uniqueness is false.

Evidence: matrix CSV line 11: batchnorm_ema pass_rate 0.0; line 23: batchnorm_ema pass_rate 1.0; lines 135-149: moco's nine fractional rows and six endpoints. SQL lines 267 and 270 provide another across-row counterexample.

## A-S03 — line 128

**Current wording**

> The labels are recorded classifications, not observations of what the model did.

**Proposed replacement**

> The labels are recorded classifications; their names do not establish an internal reasoning mechanism.

The source boundary concerns internal reasoning and mechanisms. It does not establish that failure labels are unrelated to observed behavior. The sentence broadens a sound limitation into an unsupported negative assertion.

Evidence: internal_article line 179: These are recorded classifications, not observations of Mercury-2.5's internal reasoning. I cannot infer a mechanism from the label names. Current instructions require labels to remain recorded classifications.

## A-S04 — line 177

**Current wording**

> no clean configuration-hash comparison exists

**Proposed replacement**

> the supplied records contain no clean configuration-hash comparison

The available evidence establishes a missing comparison in the supplied reconstruction environment, not global nonexistence. Restore the source scope beside this reproduction claim.

Evidence: provenance line 34: config hashes not compared(no clean source snapshot available in this environment); config_hash_audit.csv has 0 checked. Campaign dirty source commit in provenance line 13 is ea827277d42a714d4cd9760f4a4930ab5237e6de, distinct from the pinned analysis snapshot.

All five current snippets occur exactly once. Proposed replacements pass the author’s wording exclusions. Applying these replacements will require a new candidate filename and validation of the revised text; the two Arena originals stay preserved.
