# Accepted source snippet CS009 — Sonnet E4 callable common knowledge

Source: Sonnet 5 review, lines 521–538 of critique revision `aaca2cd0a1ada079d01bf4d3c918cae6260e2a87`.

User selected **1A, 2A, 3A, 4A**, accepted the result, and authorized committing and pushing code, tests and acceptance record and proceeding to the tenth snippet.

- Preserve common_knowledge(agents, f) as a callable combinator using the source's finite reachability closure over the accepted propositional model.
- Empty group reaches only the starting world and evaluates f there.
- Validate starting world and all selected agents before traversal.
- Snapshot agents at formula construction; allow harmless duplicates.
- Recompute closure for each supplied model; no arbitrary depth cutoff or cross-model cache.

Ten new tests pass; all 70 accepted tests pass. Checks distinguish common knowledge from shallower nested knowledge and cover disconnected worlds, cycles, nested formulas, empty groups, references, group snapshots, duplicates and reevaluation after announcement. No earlier accepted implementation changed.

```sh
python -m unittest discover -s mission-02/snippet_reconciliation/approved -p 'test_*.py' -q
```

Local proposal checks only: not target integration, independent verification or global v3 acceptance. Commit and push authorized. CS010 source tests remain separately pending.
