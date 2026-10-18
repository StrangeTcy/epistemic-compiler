#!/usr/bin/env python3
"""Figures for the revised cross-environment map article (POST-02).

Reads only the generated tables under evidence/generated and evidence/generated2.
No provider calls, no campaign rerun. Writes SVG files next to this script's parent.

Figures
  fig8_selection_frame.svg     design cells -> selected -> scored -> outcomes
  fig9_environment_intervals.svg  per-environment pass fraction with 95% Wilson intervals
  fig10_tuple_matrix.svg       environment x difficulty-tuple outcome grid
  fig11_failure_labels.svg     global failure-label counts (no environment breakdown exists)

Run:  python3 figures/scripts/make_post02_figures.py   (from campaign-02-analysis/)
"""
import csv
import math
import os
from collections import Counter

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
GEN = os.path.join(BASE, "evidence", "generated")
GEN2 = os.path.join(BASE, "evidence", "generated2")
OUT = os.path.join(BASE, "figures")

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "svg.fonttype": "none"})
C_PASS = "#2e7d4f"
C_FAIL = "#b23a3a"
C_MIX = "#d89b2b"
C_UNS = "#9e9e9e"
C_INK = "#222222"


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def wilson(k, n, z=1.959964):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    print("wrote", path)


env_rows = read_csv(os.path.join(GEN2, "environment_summary_v2.csv"))
matrix = read_csv(os.path.join(GEN2, "environment_difficulty_matrix.csv"))
cases = read_csv(os.path.join(GEN, "case_results.csv"))
exclusions = read_csv(os.path.join(GEN, "campaign_exclusions.csv"))


# ---------- fig8: selection frame ----------
def fig8():
    omitted = Counter(r["exclusion_class"] for r in exclusions)
    n_omit = len(exclusions)
    n_sel = len(cases)
    n_scored = sum(1 for r in cases if r["status"] == "scored")
    n_uns = n_sel - n_scored
    n_pass = sum(1 for r in cases if r["verdict"] == "PASS")
    n_fail = sum(1 for r in cases if r["verdict"] == "FAIL")
    total = n_sel + n_omit
    rows = [
        ("Design cells", [(n_sel, "#546e7a", f"{n_sel} selected"), (omitted["intervention_twin_omission"], "#cfd8dc", "56"), (omitted["known_gate_calibration_failure"], "#e3e8eb", "14"), (omitted["unsupported_provider_input_modality"], "#f2f4f5", "10")]),
        ("Selected cases", [(n_scored, "#546e7a", f"{n_scored} scored"), (n_uns, C_UNS, "11 unscored")]),
        ("Scored cases", [(n_pass, C_PASS, f"{n_pass} PASS"), (n_fail, C_FAIL, f"{n_fail} FAIL")]),
    ]
    fig, ax = plt.subplots(figsize=(9, 3.4))
    for i, (label, segs) in enumerate(rows[::-1]):
        left = 0
        for width, colour, text in segs:
            ax.barh(i, width, left=left, color=colour, edgecolor="white", height=0.6)
            dark = colour in (C_PASS, C_FAIL, "#546e7a")
            if width >= 40:
                ax.text(left + width / 2, i, text, ha="center", va="center", color="white" if dark else C_INK, fontsize=9)
            left += width
        ax.text(-12, i, label, ha="right", va="center", fontsize=10)
    ax.text(total + 10, 2, "Omitted before scoring (no score recorded):\n56 intervention-twin, 14 known-gate,\n10 unsupported input modality (rope)", va="center", fontsize=8, color=C_INK)
    ax.set_xlim(0, total + 10)
    ax.set_yticks([])
    ax.set_xticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(f"From {total} design cells to {n_pass} PASS and {n_fail} FAIL judgments (Mercury-2.5 archive)", loc="left", fontsize=11)
    save(fig, "fig8_selection_frame.svg")


# ---------- fig9: environment pass fraction with Wilson intervals ----------
def fig9():
    rows = [r for r in env_rows if int(r["n_scored"]) > 0]
    pts = []
    for r in rows:
        k, n = int(r["n_pass"]), int(r["n_scored"])
        lo, hi = wilson(k, n)
        pts.append((r["environment"], k, n, k / n, lo, hi))
    pts.sort(key=lambda t: (t[3], t[2], t[0]))
    fig, ax = plt.subplots(figsize=(8.5, 9.5))
    for i, (env, k, n, p, lo, hi) in enumerate(pts):
        colour = C_PASS if k == n else (C_FAIL if k == 0 else C_MIX)
        ax.plot([lo, hi], [i, i], color=colour, lw=2, alpha=0.6)
        ax.plot(p, i, "o", color=colour, ms=6)
        ax.text(1.03, i, f"{k}/{n}", va="center", fontsize=8, color=C_INK)
    ax.set_yticks(range(len(pts)))
    ax.set_yticklabels([t[0] for t in pts], fontsize=8)
    ax.set_xlim(-0.02, 1.12)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.axvline(277 / 405, color=C_INK, ls=":", lw=1)
    ax.text(277 / 405, len(pts) - 0.2, "pooled 68.4%", ha="center", fontsize=8, color=C_INK)
    ax.set_xlabel("Pass fraction among scored cases (dot); 95% Wilson interval (bar)")
    ax.grid(axis="x", color="#eeeeee", lw=0.8)
    ax.set_axisbelow(True)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.legend(handles=[Patch(color=C_PASS, label="all scored passed"), Patch(color=C_MIX, label="mixed"), Patch(color=C_FAIL, label="no scored pass")], loc="upper left", fontsize=8, frameon=False)
    ax.set_title("36 environments with scored cases: small n gives wide intervals", loc="left", fontsize=11)
    save(fig, "fig9_environment_intervals.svg")


# ---------- fig10: environment x tuple outcome grid ----------
def fig10():
    envs = {}
    for r in env_rows:
        envs[r["environment"]] = r
    order = sorted(envs, key=lambda e: (-(int(envs[e]["n_pass"]) / int(envs[e]["n_scored"])) if int(envs[e]["n_scored"]) else 2, e))
    cmap = LinearSegmentedColormap.from_list("pf", [C_FAIL, C_MIX, C_PASS])
    width = max(sum(1 for r in matrix if r["environment"] == e) for e in order)
    fig, ax = plt.subplots(figsize=(10, 11))
    for i, env in enumerate(order):
        rows = sorted((r for r in matrix if r["environment"] == env), key=lambda r: r["difficulty_tuple"])
        for j, r in enumerate(rows):
            if int(r["n_scored"]) == 0:
                colour = C_UNS
            else:
                colour = cmap(float(r["pass_rate"]))
            ax.add_patch(plt.Rectangle((j, len(order) - 1 - i), 0.92, 0.92, color=colour, lw=0))
            if int(r["n_cases"]) > 1:
                ax.text(j + 0.46, len(order) - 1 - i + 0.46, str(r["n_cases"]), ha="center", va="center", fontsize=6, color="white")
    ax.set_xlim(0, width)
    ax.set_ylim(0, len(order))
    ax.set_yticks([len(order) - 1 - i + 0.46 for i in range(len(order))])
    ax.set_yticklabels(order, fontsize=7)
    ax.set_xticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    handles = [Patch(color=cmap(1.0), label="pass rate 1"), Patch(color=cmap(0.5), label="fractional (moco only)"), Patch(color=cmap(0.0), label="pass rate 0"), Patch(color=C_UNS, label="unscored")]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.01), ncol=4, fontsize=8, frameon=False)
    ax.set_title("Each square is one environment x difficulty-tuple row (340 rows)\nNumbers mark rows with several cases; most rows hold one", loc="left", fontsize=10)
    save(fig, "fig10_tuple_matrix.svg")


# ---------- fig11: failure labels ----------
def fig11():
    counts = Counter(r["failure_mode_normalized"] for r in cases if r["verdict"] == "FAIL")
    labels = [k for k, _ in counts.most_common()]
    vals = [counts[k] for k in labels]
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    bars = ax.barh(labels[::-1], vals[::-1], color="#607d8b")
    for b, v in zip(bars, vals[::-1]):
        ax.text(v + 0.8, b.get_y() + b.get_height() / 2, str(v), va="center", fontsize=9)
    ax.set_xlabel("FAIL outcomes (n = 128)")
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.set_title("Recorded failure labels, all environments combined", loc="left", fontsize=11)
    fig.text(0.01, -0.04, "Global counts only: the archive gives no environment-level breakdown of labels.", fontsize=8, color=C_INK)
    save(fig, "fig11_failure_labels.svg")


if __name__ == "__main__":
    fig8()
    fig9()
    fig10()
    fig11()
