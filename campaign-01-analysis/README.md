# Campaign 01 — Atria campaign analysis

**Status:** the separate campaign-analysis workstream is complete through archive reconstruction, source/judge audit, four-role Council and cross-critique, findings register, five full post drafts, internal `post_editor` review, and `rl_eval_generator` proposals. The drafts remain conditional on human editorial review and preserve the dirty-source/comparator caveat. This folder is separate from Missions 01–04. No Mission 01 frozen claim/result file, Mission 04 status/hypothesis/preregistration, or raw campaign evidence member was changed. No retroactive preregistration was created.

## Scope and evidence hierarchy

The primary evidence is the ZIP `atria-campaign-state-62.zip` identified at `origin/main`, SHA-256 `e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd`, Git blob `c1c416cdee773cffab7fbf5a1cc01b8c8c2fd8a3`. Its 2,968 ZIP members—not campaign summaries or pasted metrics—are indexed, SHA-256 hashed, and used to regenerate the tables in [`evidence/generated/`](evidence/generated/). See [`evidence/PROVENANCE.md`](evidence/PROVENANCE.md) for the reconstruction rules and exact links.

The archive records campaign repository commit `d7357092493f311f649a0742889b301d796911b5`, but also `repository.dirty=true`. All 33 selected environment-config hashes match the clean snapshot at that commit; this does **not** establish that every executed task/judge file is byte-identical to that clean snapshot. Source implementation notes therefore cite the inspected snapshot as a comparator and preserve the dirty-source limitation.

The preliminary Atria analysis pasted before the archive was found is retained unchanged under `sources/raw/`; it is treated as leads, not authority. The ZIP and its internal machine-readable records take precedence whenever they disagree.

## Reconstructed topline (read with the mode and exclusion caveats)

- The campaign status is `completed`; all **194/194 selected results** are recorded as scored, across 33 of 34 registered environments. The archive separately records 17 `rope` cases omitted for unsupported provider input modality and 7 cases omitted before provider access because of known judge/reference calibration failures; these 24 omissions are listed case-by-case in [`evidence/generated/campaign_exclusions.csv`](evidence/generated/campaign_exclusions.csv).
- Raw verdicts are **131 PASS / 63 FAIL**. A primary-artifact audit finds **two**, not one, final results whose notes explicitly say `provider transient failure after bounded retries`: one `ts_trajectory` row named by `campaign_report.json`, and an additional `sheaf_physical_constraints` row not listed in that report counter. Keeping both raw rows visible but excluding both provider-attributed terminal failures yields **131/192 PASS and 61/192 FAIL** for the analysis performance set. The report-listed-only sensitivity is 131/193 PASS and 62/193 FAIL. These are descriptive counts, not a uniform validated score.
- The 192-case set contains 72 `behavioral_reference` cases (56 PASS/16 FAIL) and 120 `compile_only` cases (75 PASS/45 FAIL). The archive's `campaign_report.json` explicitly says compile-only verdicts are exploratory and excluded from a validated aggregate. `oracle_preflight.json` records an environment-level behavioral self-test only for `epistemic_games`; the per-instance `instance_oracles.json` records 72 additional calibrated cases. Those are distinct records, not interchangeable claims of independent validation.
- One archived label is inconsistent with task semantics: all seven `epistemic_games` cases are assigned to the recorded `ml_debugging` track. [`evidence/generated/case_results.csv`](evidence/generated/case_results.csv) preserves that label in `track` and adds an analysis-family override; [`evidence/generated/analysis_family_summary.csv`](evidence/generated/analysis_family_summary.csv) separates the epistemic task rather than silently folding it into ML debugging.
- The campaign log records 261,135.03 seconds elapsed (~72.5 hours). The ZIP contains 268 run directories (194 selected final runs plus earlier/superseded attempts), 4,061 successful response records across all run directories, and 9,447,242 successful-response tokens. Retry counters in the API log, run manifests, result checkpoints, and progress report do not reconcile; they remain reported by source and scope rather than collapsed into one total.
- Run configuration says `reasoning_enabled=false`, while usage records 325,785 reasoning tokens and 2,710 response rows with a `reasoning_content` field. This is a metadata discrepancy. No reasoning content is reproduced in these artifacts.

## Work products

- [`evidence/`](evidence/): provenance, reproducible ZIP reconstruction script, complete member inventory, selected cases and omissions, run attempts, result/mode/failure/axis summaries, and trace hashes/links.
- [`sources/`](sources/): verified links and scope notes for cited prior work; `sources/raw/` retains earlier campaign leads without treating them as evidence.
- [`council/`](council/): separate Theorist, Experimentalist, Skeptic, and Prior-Work Killer analyses; prompts, provenance, cross-critique, and synthesis. The analyses are sequential role passes by the same Arena Agent, not independent external-model replications.
- [`findings/`](findings/): claim register with evidence links, status (`OBSERVED`, `INFERRED`, `SPECULATIVE`), confidence, alternatives, limits, falsifiers, novelty position, and follow-up requirements.
- [`posts/`](posts/): five complete drafts (POST-01 through POST-05), the `post_editor` review, and a claim traceability CSV linking 43 editorial claim IDs through findings to raw archive members and source references.
- [`followups/`](followups/): concrete `rl_eval_generator` evolution proposals split into evidence-backed improvement needs and future experiments; recommendations are not implemented or experimentally validated.

## Regeneration

Materialize the unchanged archive blob from `origin/main` into a temporary working path, then reconstruct with a clean source snapshot for the optional config-hash comparison:

```bash
git show origin/main:atria-campaign-state-62.zip > /tmp/atria-campaign-state-62.zip
python campaign-01-analysis/evidence/reconstruct_campaign.py \
  --archive /tmp/atria-campaign-state-62.zip \
  --out campaign-01-analysis/evidence/generated \
  --archive-ref origin/main:atria-campaign-state-62.zip \
  --git-blob c1c416cdee773cffab7fbf5a1cc01b8c8c2fd8a3 \
  --generator-source /path/to/rl_eval_generator-at-d735709
```

The reconstruction uses only Python's standard library and does not execute a campaign, call a provider, or modify the archive. Rebuild the post-to-raw-artifact links from the generated tables and draft markers with:

```bash
python campaign-01-analysis/posts/build_claim_traceability.py
```

See [`evidence/PROVENANCE.md`](evidence/PROVENANCE.md) for reconstruction rules and source-snapshot boundaries.
