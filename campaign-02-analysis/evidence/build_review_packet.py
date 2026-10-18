#!/usr/bin/env python3
"""Build the self-contained evidence packet for the POST-02 evidence review.

Reads the generated tables under evidence/generated and evidence/generated2 and
writes a plain-text markdown packet that a reviewer can read without a shell.
Only the fields needed to check the article's claims are kept. Long free-text
fields and case IDs are dropped to keep the packet readable; every kept value is
copied verbatim from the source tables. Section E describes in text what each
article chart plots, with its values, because a reviewer cannot render SVG.
No provider calls, no campaign rerun.

Run from campaign-02-analysis/:
    python3 evidence/build_review_packet.py
"""
import csv
import hashlib
import json
import math
import os
from collections import Counter

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GEN = os.path.join(BASE, "evidence", "generated")
GEN2 = os.path.join(BASE, "evidence", "generated2")
OUT = os.path.join(BASE, "post-production", "handoffs", "POST-02-redo_evidence_packet.md")


def read(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def sha256(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(out)


def wilson(k, n, z=1.959964):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def chart_section(cases, envs, matrix):
    """Plain-text description of what each article chart plots, with its values."""
    n_scored = sum(1 for c in cases if c["status"] == "scored")
    n_unscored = len(cases) - n_scored
    n_pass = sum(1 for c in cases if c["verdict"] == "PASS")
    n_fail = sum(1 for c in cases if c["verdict"] == "FAIL")
    out = ["## Section E — what each chart draws\n"]
    out.append("The charts are SVG files that the reviewer cannot render. This section states what each one plots, with the values from the tables above.\n")
    out.append(
        f"**Figure 8 (selection frame).** Three stacked horizontal bars. Bar 1, design cells: 496 = 416 selected + 80 omitted "
        f"(56 intervention-twin, 14 known-gate, 10 unsupported modality). Bar 2, selected cases: {n_scored} scored + {n_unscored} unscored. "
        f"Bar 3, scored cases: {n_pass} PASS + {n_fail} FAIL. The 80 omitted cases are drawn in pale grey and are in no pass rate. "
        f"Only segments of 40 or more cases carry a text label; the {n_unscored}-case unscored segment is unlabelled, and its count appears only in the caption.\n"
    )

    rows = []
    for e in envs:
        k, n = int(e["n_pass"]), int(e["n_scored"])
        if n == 0:
            continue
        lo, hi = wilson(k, n)
        cls = "all scored passed" if k == n else ("no scored pass" if k == 0 else "mixed")
        rows.append((k / n, n, e["environment"], k, lo, hi, cls))
    rows.sort(key=lambda t: (t[0], t[1], t[2]))
    out.append(
        f"**Figure 9 (environment intervals).** One dot per environment with scored cases ({len(rows)} environments; "
        "environments with no scored case are not drawn). The dot is the pass fraction k/n. The bar is the 95% Wilson interval. "
        "The label beside each bar is k/n. A dotted vertical line marks the pooled 277/405 = 68.4%. Rows below are in the order drawn, from lowest to highest pass fraction.\n"
    )
    out.append(md_table(
        ["order", "environment", "k/n", "pass fraction", "Wilson 95% low", "Wilson 95% high", "colour class"],
        [[i, r[2], f"{r[3]}/{r[1]}", f"{r[0]:.3f}", f"{r[4]:.3f}", f"{r[5]:.3f}", r[6]] for i, r in enumerate(rows, 1)],
    ))
    out.append("")

    grey = sum(1 for r in matrix if int(r["n_scored"]) == 0)
    multi = sum(1 for r in matrix if int(r["n_cases"]) > 1)
    frac = sum(1 for r in matrix if int(r["n_scored"]) > 0 and float(r["pass_rate"]) not in (0.0, 1.0))
    out.append(
        f"**Figure 10 (tuple matrix).** One square per environment × difficulty-tuple row: {len(matrix)} squares, grouped by environment "
        f"({len(envs)} environments, one row of squares each). The colour is the row pass rate (red 0, amber fractional, green 1). "
        f"Grey marks the {grey} rows with no scored case. A number is written in squares that hold more than one case ({multi} such rows). "
        f"Fractional rows: {frac}, all in `moco`. Tuples are environment-specific, so columns are not comparable across environments.\n"
    )

    labels = Counter(c["failure_mode_normalized"] for c in cases if c["verdict"] == "FAIL")
    label_text = ", ".join(f"{k} {v}" for k, v in labels.most_common())
    out.append(
        f"**Figure 11 (failure labels).** A horizontal bar chart of the normalised failure label across all {n_fail} FAIL cases combined. "
        f"There is no environment split. Counts: {label_text}.\n"
    )
    return "\n".join(out)


def main():
    cases = read(os.path.join(GEN, "case_results.csv"))
    excl = read(os.path.join(GEN, "campaign_exclusions.csv"))
    matrix = read(os.path.join(GEN2, "environment_difficulty_matrix.csv"))
    envs = read(os.path.join(GEN2, "environment_summary_v2.csv"))

    m_rows = []
    per_env = Counter()
    for r in matrix:
        env = r["environment"]
        per_env[env] += 1
        ndims = len(json.loads(r["difficulty_tuple"]))
        m_rows.append((env, per_env[env], ndims, r["n_cases"], r["n_scored"], r["n_unscored"], r["n_pass"], r["n_fail"], r["pass_rate"], r["failure_modes"], r["judge_guarantees"]))

    sources = [
        "evidence/generated/case_results.csv",
        "evidence/generated/campaign_exclusions.csv",
        "evidence/generated2/environment_difficulty_matrix.csv",
        "evidence/generated2/environment_summary_v2.csv",
    ]

    lines = []
    lines.append("# POST-02 redo — evidence packet for review\n")
    lines.append("This packet is the only data source for the evidence review. It is generated by `evidence/build_review_packet.py` from the four tables below. Values are copied verbatim. Long free-text fields and case IDs are omitted. Case rows are numbered 1 to 416 in source order. Matrix rows are referenced as `environment#k`, where k numbers the rows of that environment in source order. Section E describes each article chart in text.\n")
    lines.append("Source tables and their SHA-256 hashes (of the full source files, not of this packet):\n")
    for s in sources:
        lines.append(f"- `{s}`: `{sha256(os.path.join(BASE, s))}`")
    lines.append("")

    lines.append(f"## Table A — environment summary ({len(envs)} environments)\n")
    lines.append(md_table(["environment", "n_tuples", "n_cases", "n_scored", "n_pass", "n_fail", "pass_rate"],
                          [[e["environment"], e["n_tuples"], e["n_cases"], e["n_scored"], e["n_pass"], e["n_fail"], e["pass_rate"]] for e in envs]))
    lines.append("")

    lines.append(f"## Table B — selected cases ({len(cases)} rows)\n")
    lines.append("Fields: status, verdict, seed, judge_guarantee, failure_mode_normalized, failure_mode_raw, case_disposition, performance_eligible, environment.\n")
    rows = [[i, c["environment"], c["status"], c["verdict"], c["seed"], c["judge_guarantee"], c["failure_mode_normalized"], c["failure_mode_raw"], c["case_disposition"], c["performance_eligible"]]
            for i, c in enumerate(cases, 1)]
    lines.append(md_table(["row", "environment", "status", "verdict", "seed", "judge_guarantee", "failure_mode_normalized", "failure_mode_raw", "case_disposition", "performance_eligible"], rows))
    lines.append("")

    lines.append(f"## Table C — pre-scoring omissions ({len(excl)} rows)\n")
    lines.append("Fields: environment and exclusion_class.\n")
    rows = [[i, x.get("environment", ""), x.get("exclusion_class", "")] for i, x in enumerate(excl, 1)]
    lines.append(md_table(["row", "environment", "exclusion_class"], rows))
    lines.append("")

    lines.append(f"## Table D — environment × difficulty-tuple matrix ({len(matrix)} rows)\n")
    lines.append("Fields: environment, k (row number within environment), n_dims (number of difficulty keys in the tuple), n_cases, n_scored, n_unscored, n_pass, n_fail, pass_rate, failure_modes, judge_guarantees.\n")
    lines.append(md_table(["environment", "k", "n_dims", "n_cases", "n_scored", "n_unscored", "n_pass", "n_fail", "pass_rate", "failure_modes", "judge_guarantees"], m_rows))
    lines.append("")

    lines.append(chart_section(cases, envs, matrix))
    lines.append("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
