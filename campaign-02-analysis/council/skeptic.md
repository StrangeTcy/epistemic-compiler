# Skeptic (Mercury)

## Attacks on F-001
- Small sample: 36 pairs, 5 terminal flips. Could be noise. No CI provided.
- Single model/provider; may be mercury-specific.
- Terminal answer extraction may be brittle; a parsing difference could masquerade as a decision flip.
- Diagnostic-choice divergence (17/36) is a softer endpoint; choice ordering may not matter.

## Attacks on F-002
- Intervention cases are not difficulty-matched; visible_proxy cases may be intrinsically harder.
- Pass/fail is a coarse endpoint; score differences may be small.
- Base pass rate mixes environments; comparison across different tasks.

## What survives
- Belief invariance across 36 pairs is striking (0 flips) and internally consistent with F-003.
- Proxy pass rates are very low (0.25-0.30) and directionally consistent with 7 pass->fail flips within shared pairs.

## Required to overturn
- Replication with more seeds showing belief flips or zero terminal flips.
- Difficulty-stratified re-analysis showing proxy effect disappears.
