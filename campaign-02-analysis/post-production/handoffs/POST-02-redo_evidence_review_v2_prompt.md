# POST-02 redo — Evidence review of the revised article (v2 prompt, not dispatched)

## Inputs (read these first; you have no shell and cannot clone a repository)

1. **Article under review:** `campaign-02-analysis/posts/POST-02-cross-environment-map.md` at the commit given in the link you were sent. Read the whole article.
2. **Evidence packet (the only data source):** `campaign-02-analysis/post-production/handoffs/POST-02-redo_evidence_packet.md` at the same commit. It holds four tables:
   - Table A: environment summary (38 rows)
   - Table B: selected cases (416 rows)
   - Table C: pre-scoring omissions (80 rows)
   - Table D: environment × difficulty-tuple matrix (340 rows)

   Read the full packet, in chunks if your fetch tool returns chunks. Do not stop after the first chunk.
3. **Chart descriptions:** Section E of the same packet. It states, in text, what each of the four charts plots, with the values. You cannot render the charts; judge the captions against Section E.

If you cannot read any of these, say which one and which part, and withhold any verdict on claims that depend on it. Do not reconstruct the tables from the article, from earlier reviewer summaries, or from memory. Do not say you have cloned, checked out, or run anything. You can only read what you fetched.

**In your response, state:** the commit you read; the row counts you actually saw in Tables A to D (expected 38, 416, 80, 340); and any part you could not read.

## Your role

You are an independent Evidence Reviewer. Check every number, count and factual claim in the article against the packet. Produce an adversarial brief. Do not rewrite the article. Do not propose new analyses that need data outside the packet.

## Facts the packet should confirm (check them, do not assume them)

- 416 selected cases; 405 scored (`status = scored`); 11 `infrastructure_unscored`.
- 277 PASS / 128 FAIL; 277/405 = 68.4%; 277/416 = 66.6%.
- 80 omissions: 56 intervention-twin, 14 known-gate, 10 unsupported input modality (all in `rope`).
- 38 environments; 36 with scored cases. Outcome split: 17 all-pass, 12 mixed, 7 all-fail, 2 with no scored case.
- Mixed environments: 165 scored cases, 105 PASS. All 12 contain at least one zero-pass tuple.
- Unweighted mean of environment pass fractions 69.2%; median 88.9%.
- Matrix: 340 rows; 296 single-case; 44 multi-case. 329 rows have a pass rate; 320 of those are exactly 0 or 1; 9 are fractional, all in `moco`. 204 rows sit in environments where every scored row has the same outcome; 214 if the two no-scored environments are added.
- Judge guarantee is fixed per environment: 11 `behavioral_reference` (141/189 scored PASS), 27 `compile_only` (136/216 scored PASS; 11 unscored).
- Failure labels (normalised): underfit 51, overfit_visible_tests 49, runtime_error 11 (9 `RUNTIME_ERROR` and 2 `runtime_error` in the raw column), source_invalid 9, invalid_action 5, training_failed 3.
- Disposition: 10 `rejected` (all FAIL; 9 with label `source_invalid`); 9 scored FAILs with disposition `unscored`.
- One PASS in `ts_parse_only` has `performance_eligible = False`.
- Seed is 0 for all 416 cases.

## Tasks

1. Check each number in the article against the packet. Report each mismatch with the article location, the article value, and the packet value and row.
2. Check each figure caption against Section E of the packet. Report any caption that claims more or less than the chart plots.
3. Check each disclosure beside a claim: the 10 `rejected` FAILs, the 80 omissions, the performance-ineligible PASS, the 9 `unscored`-disposition FAILs, and the 14-vs-24 known-gate conflict.
4. Identify any causal or mechanism claim the packet does not support, and any "cannot" or "does not show" statement that the packet contradicts.
5. Identify any statement that treats a recorded label, disposition or guarantee as a fact about the model rather than a recorded classification.
6. Note any open discrepancy, such as the zero-pass count in `campaign-02-analysis/ANALYSIS_OVERVIEW.md` (stated as 10; the packet gives 7 at environment level and 19 at tuple level).

## Output format

- Verdict: accept / accept with corrections / reject.
- Numbered findings, each with: article location, claim, packet evidence (table and row or column), severity (blocking / correction / note).
- Final line: count of blocking findings and count of corrections.
- Start the response with the "State" line described above (commit read, row counts seen, anything unread).

## Constraints

- No internal finding IDs, trace IDs or draft labels in any suggested public wording.
- Bracketed tokens such as `[m-word]` are intentional replacements, not errors.
- Do not suggest preregistration framing. The analysis is retrospective.
