#!/usr/bin/env python3
"""Approximate power of the Mission 03 primary contrast S (own-card minus other-card).

Design simulated (see ../DESIGN.md): two task families, two cards, each card is "own" for one
family and "other" for the other. For every run both card arms are played on the same instance.

    S = 1/2 * [ (own - other) in family 1  +  (own - other) in family 2 ]

Family 1 (moco-like): every run is a distinct instance, so the cluster is the run.
Family 2 (weird-machine-like): only K2 = 45 agent-visible cells exist (5 environments x 9
difficulty vectors); runs are spread over them and the cluster is the cell.

Assumptions (all of them, so nobody has to guess):
  * success probability of a cell/instance ~ Normal(p0, TAU_CELL) clipped to [0.02, 0.98]; the
    cell effect is shared by both arms (paired design), so it cancels in the difference;
  * the own-card arm adds +S/2 and the other-card arm -S/2 to that probability;
  * each (cell, card) pair has its own interaction effect ~ Normal(0, TAU_CARD): cards help some
    cells more than others, which does NOT average out inside a cell;
  * outcomes are independent Bernoulli draws given those probabilities;
  * the statistic is the cluster-level paired difference; the test is a normal approximation
    with a cluster-robust standard error. This is a planning approximation, not the registered
    analysis (the registered analysis is a cluster bootstrap).

Run `python power_simulation.py --out power_table.json`; `--check` verifies the committed file.
Standard library only; fully deterministic for a given seed.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path

SEED = 20261002
N_SIMS = 2000
K2_CELLS = 45
TAU_CELL = 0.20
TAU_CARD = 0.08
DELTAS = (0.10, 0.15)  # smallest effects of interest examined; the registered margin is fixed at Gate 2
Z95 = 1.959964
RUNS_PER_ARM = (40, 60, 100, 150, 200)
TRUE_S = (0.0, 0.05, 0.10, 0.15)
BASELINES = (0.30, 0.50)


def _clip(x: float, lo: float = 0.02, hi: float = 0.98) -> float:
    return lo if x < lo else hi if x > hi else x


def _cluster_diffs(rng: random.Random, p0: float, s: float, n_runs: int, n_cells: int | None) -> list[float]:
    """Per-cluster mean of (own - other) outcomes for one family."""
    cells = n_runs if n_cells is None else n_cells
    base = [_clip(rng.gauss(p0, TAU_CELL)) for _ in range(cells)]
    w_own = [rng.gauss(0.0, TAU_CARD) for _ in range(cells)]
    w_oth = [rng.gauss(0.0, TAU_CARD) for _ in range(cells)]
    sums = [0.0] * cells
    counts = [0] * cells
    for i in range(n_runs):
        c = i % cells
        p_own = _clip(base[c] + s / 2 + w_own[c])
        p_oth = _clip(base[c] - s / 2 + w_oth[c])
        sums[c] += (rng.random() < p_own) - (rng.random() < p_oth)
        counts[c] += 1
    return [sums[c] / counts[c] for c in range(cells) if counts[c]]


def _mean_and_var_of_mean(xs: list[float]) -> tuple[float, float]:
    m = sum(xs) / len(xs)
    if len(xs) < 2:
        return m, float("inf")
    v = sum((x - m) ** 2 for x in xs) / (len(xs) - 1)
    return m, v / len(xs)


def config_rng(p0: float, s: float, n_runs: int) -> random.Random:
    """One independent, reproducible stream per configuration, so any single row can be re-run alone."""
    return random.Random(f"{SEED}|{p0:.2f}|{s:.2f}|{n_runs}")


def one_config(p0: float, s: float, n_runs: int) -> dict[str, float]:
    rng = config_rng(p0, s, n_runs)
    lower_pos = 0
    upper_below = {d: 0 for d in DELTAS}
    for _ in range(N_SIMS):
        m1, v1 = _mean_and_var_of_mean(_cluster_diffs(rng, p0, s, n_runs, None))
        m2, v2 = _mean_and_var_of_mean(_cluster_diffs(rng, p0, s, n_runs, min(K2_CELLS, n_runs)))
        s_hat = 0.5 * (m1 + m2)
        se = 0.5 * math.sqrt(v1 + v2)
        if s_hat - Z95 * se > 0:
            lower_pos += 1
        for d in DELTAS:
            if s_hat + Z95 * se < d:
                upper_below[d] += 1
    out = {"p_detect": round(lower_pos / N_SIMS, 3)}
    for d in DELTAS:
        out[f"p_rule_out_{d:.2f}"] = round(upper_below[d] / N_SIMS, 3)
    return out


def build() -> dict:
    table = []
    for p0 in BASELINES:
        for n in RUNS_PER_ARM:
            for s in TRUE_S:
                table.append({"baseline_pass_rate": p0, "runs_per_arm_per_family": n, "true_S": s, **one_config(p0, s, n)})
    return {
        "script": "mission-03/analysis/power_simulation.py",
        "seed": SEED,
        "n_sims_per_config": N_SIMS,
        "assumptions": {
            "family_2_cells": K2_CELLS,
            "tau_cell_probability_sd": TAU_CELL,
            "tau_card_by_cell_interaction_sd": TAU_CARD,
            "deltas_examined": list(DELTAS),
            "test": "normal approximation, cluster-robust standard error, two-sided 95%",
        },
        "reading": {
            "p_detect": "probability the 95% interval for S excludes zero on the positive side",
            "p_rule_out_<delta>": "probability the 95% interval's upper end falls below delta, i.e. effects of at least delta are ruled out (an informative null)",
        },
        "results": table,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", type=Path, default=Path(__file__).with_name("power_table.json"))
    ap.add_argument("--check", action="store_true", help="fail if the committed file differs from a fresh run")
    args = ap.parse_args(argv)
    text = json.dumps(build(), indent=1, sort_keys=True) + "\n"
    if args.check:
        if not args.out.exists() or args.out.read_text(encoding="utf-8") != text:
            print(f"{args.out} does not match a fresh run", file=sys.stderr)
            return 1
        print(f"{args.out} reproduces")
        return 0
    args.out.write_text(text, encoding="utf-8")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
