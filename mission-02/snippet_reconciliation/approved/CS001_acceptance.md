# Accepted source snippet CS001 — event-based Bayesian updating

Source: first Gemini review, E1, Python fence at lines 33–55 of `code snippets critique.md`, revision `aaca2cd0a1ada079d01bf4d3c918cae6260e2a87`.

The user explicitly selected **A / C / B** and then accepted the resulting snippet with “It's fine; please commit this particular snippet”.

- Retain `EpistemicEvent` and event-only calculation alongside the separate full-policy interface.
- Keep separately named sparse and strict contracts. Sparse fills missing prior-state likelihoods with zero and ignores unrelated entries; strict requires exact key coverage.
- Keep a mathematical core with documented preconditions and separate validated wrappers. Both reject zero evidence through the core.
- Preserve the original perfect-evidence behavior and add direct tests of the approved contract differences.

`event_bayes.py` is a self-contained **proposal artifact**, extracted from the accepted section of v3 with its required exact-arithmetic validation helpers. It does not implement or change the separate target repository. Only this snippet is accepted; other source snippets and v3 as a whole are not thereby approved.

Run the four source-specific tests:

```sh
python -m unittest discover -s mission-02/snippet_reconciliation/approved -p 'test_event_bayes.py' -v
```

The user authorized a commit, not a push.
