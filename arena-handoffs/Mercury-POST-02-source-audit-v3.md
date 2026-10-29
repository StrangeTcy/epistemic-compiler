# Mercury POST-02 — supporting source check, 2026-10-29

This is local arithmetic and field verification, not an Arena review, a new evaluation run, or a final article validation. The accompanying JSON preserves input hashes, environment aggregates, failure/guarantee cross-tabs, exact flagged case IDs, and omission counts. Source files were read without alteration using PowerShell CSV parsing.

## Verified counts

| Quantity | Verified value |
|---|---:|
| Selected / scored / infrastructure-unscored | 416 / 405 / 11 |
| PASS / FAIL | 277 / 128 |
| Scored-case PASS rate | 68.3951% |
| Selected share with observed PASS | 66.5865% |
| Environments | 38 |
| All-pass / scored zero-pass / mixed / unscored-only environments | 17 / 7 / 12 / 2 |
| Environment-by-tuple rows | 340 |
| Singleton / multi-case rows | 296 / 44 |
| Rows with recorded pass fractions | 329 |
| Endpoint / fractional rows | 320 / 9 |
| Scored zero-pass tuples | 98 |
| Unweighted mean among scored environments | 69.2080% |
| Behavioral-reference scored PASS / scored cases | 141 / 189 |
| Compile-only scored PASS / scored cases | 136 / 216 |
| Distinct omitted case IDs | 80 |

All supplied selected cases have seed 0. Nine scored FAILs carry disposition `unscored`; ten different FAILs carry disposition `rejected`. Their exact case IDs are preserved in the JSON rather than changed or excluded.

Omissions by environment and reason: rope has ten modality omissions and five known-gate omissions; glyph has nine known-gate and twelve intervention-twin omissions; MoCo has 35 intervention-twin omissions; epistemic games has nine intervention-twin omissions. This verifies the detailed rows, not a reconciliation of the historical provenance prose.

## Additional correction for the next review

The drafts describe **214 rows** as belonging to environments where every row has the same outcome. Grouping identical `pass_rate` values reproduces 214 only when blank values are included. The count includes all six `epistemic_silence` rows and all four `epistemic_type_games` rows, which have no scored outcomes.

The supported distinction is **204 rows in environments with uniform scored outcomes, plus ten rows in entirely unscored environments**. Alternatively, 214 can describe a grouping that explicitly includes a shared absence of scored outcomes. It cannot describe 214 observed success/failure outcomes. Trace: complete matrix, all rows in those two environments; the JSON's `uniform_environment_breakdown` and `uniform_scored_environment_rows` retain the calculation.

Carry this to the resumed evidence review and editorial handoff with attribution to this local source check. Do not manufacture an Arena finding or silently modify the preserved candidate responses.

## Scope

The standalone environment-summary CSV was absent from this local snapshot. Environment totals and fractions were therefore derived from the complete tuple matrix. The JSON records this derivation. This check does not verify figure rendering, external sources, raw execution semantics, reviewer completeness, or publication readiness.
