# POST-02 Source Snapshot — Limitations

## Known Limitations
1. Single seed per selected cell (seed-0). No replication.
2. Dirty repository state. Reproduction requires frozen snapshot.
3. 11 unscored cases (6 epistemic_silence, 4 epistemic_type_games, 1 rd_adaptive_halting).
4. 56 of 132 twin cases unverified (42%).
5. Judge guarantees: 189 behavioral_reference, 227 compile_only = 416 selected. No cross-tab with failure modes or difficulty tuples.
6. Single model/provider (mercury-2.5). No comparison across models.
7. 44 of 340 matrix rows have n_cases > 1 (up to 6), complicating "one seed per cell" narrative.
8. Difficulty axes differ across environments (34 unique keys). No common ordinal scale validated.
9. No difficulty-matching analysis between intervention and base cases.
10. No manual audit of individual verdicts.
