# Accepted source snippet CS004 — Sonnet E1 test fixtures

Source: Sonnet 5 review, E1, Python fence at lines 340–363 of the critique, revision `aaca2cd0a1ada079d01bf4d3c918cae6260e2a87`.

The user selected **1B, 2B, 3C, 4A**, then explicitly accepted the result and authorized committing its tests and acceptance record and proceeding to the fifth snippet.

- Preserve original malformed source inputs as construction-rejection tests.
- Add corrected intended tests for both approved sparse and strict table contracts; valid construction precedes the update-time zero-evidence assertion.
- Retain the original half-and-half result, check Fraction output types, and add the asymmetric 2/5–3/5 fixture.
- Use unittest without adding pytest.

Eight new test methods pass; all 25 previously accepted tests also pass. Temporary in-memory negative checks demonstrated failure on float output, uniform exact output for the asymmetric fixture, and uniform fallback on impossible evidence. No accepted inference implementation was modified.

```sh
python -m unittest discover -s mission-02/snippet_reconciliation/approved -p 'test_source_e1_fixtures.py' -v
```

These are proposal tests, not target-repository integration or independent verification. Commit authorized; push not authorized. Other snippets remain subject to separate decisions.
