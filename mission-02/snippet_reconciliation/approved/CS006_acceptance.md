# Accepted source snippet CS006 — Sonnet E2 test fixtures

Source: Sonnet 5 review, E2 tests, lines 433–461 of critique revision `aaca2cd0a1ada079d01bf4d3c918cae6260e2a87`.

The user chose **1A, 2B, 3B, 4A**, then accepted the result and authorized committing its tests and acceptance record and proceeding to the seventh snippet.

- Preserve both original fixtures separately from CS005 implementation tests.
- Retain Boolean identity assertions about knowledge before/after announcement; add exact surviving-world, both-agent partition, restricted-valuation and input-preservation checks.
- Correct the comment: stale partition references may cause a wrong answer or an error.
- Rename the original singleton rejection test to describe an announcement false throughout that model. Add a separate callable logical-contradiction test.
- Translate to unittest while retaining the source ValueError contract.

Three new test methods pass; the full accepted suite now has 48 passing tests. No accepted implementation changed.

```sh
python -m unittest discover -s mission-02/snippet_reconciliation/approved -p 'test_*.py' -q
```

These are local proposal checks, not independent verification, target integration or acceptance of v3 as a whole. Commit authorized; push not authorized. Later snippets require separate decisions and acceptance.
