# Accepted source snippet CS003 — full supplied-policy updating

Source: Sonnet 5 review, E1, Python fence at lines 298–336 of the critique, revision `aaca2cd0a1ada079d01bf4d3c918cae6260e2a87`.

The user selected **1A, 2A, 3C, 4A**, then explicitly accepted the result and authorized committing it and proceeding to the fourth snippet.

- Preserve `SuppliedPolicyInstance` and `bayes_update`; reuse approved CS001 exact validation and event arithmetic.
- Require policy-world keys to match prior-world keys exactly.
- Provide sparse and strict normalized full-policy contracts. Strict rows cover a declared observation alphabet explicitly.
- Reject zero evidence during updating, not construction. An undeclared strict observation is instead a construction-time schema error.

The two code/test files are proposal artifacts, not target-repository integration. `supplied_policy.py` depends on the accepted sibling `event_bayes.py`. Eleven source-specific tests pass. The following source test block CS004 remains separately unresolved.

```sh
python -m unittest discover -s mission-02/snippet_reconciliation/approved -p 'test_supplied_policy.py' -v
```

Commit authorized; push not authorized. No approval of other snippets or v3 as a whole is implied.
