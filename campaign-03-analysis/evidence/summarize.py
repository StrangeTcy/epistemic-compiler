#!/usr/bin/env python3
"""Recompute headline counts for the reasoning Atria campaign from generated tables.

Reads only evidence/generated/*.csv and writes evidence/generated/headline_counts.csv.
No provider calls, no campaign rerun.
"""
import csv
import json
from collections import Counter
from pathlib import Path

GEN = Path(__file__).resolve().parent / "generated"


def rows(name):
    with (GEN / name).open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main():
    cases = rows("case_results.csv")
    excl = rows("campaign_exclusions.csv")
    out = []

    def add(metric, value, note=""):
        out.append({"metric": metric, "value": value, "note": note})

    n = len(cases)
    p = sum(c["verdict"] == "PASS" for c in cases)
    f = sum(c["verdict"] == "FAIL" for c in cases)
    add("recorded_cases", n, "rows in case_results.csv (all status=scored)")
    add("pass", p)
    add("fail", f)
    add("pass_rate_recorded", f"{p}/{n} = {100*p/n:.1f}%", "all recorded rows, incl. provider-outage FAIL")
    perf = [c for c in cases if c["performance_eligible"] == "True"]
    pp = sum(c["verdict"] == "PASS" for c in perf)
    add("performance_eligible_cases", len(perf), "excludes one provider-outage-attributed case")
    add("pass_rate_performance", f"{pp}/{len(perf)} = {100*pp/len(perf):.1f}%")
    for jg in ["behavioral_reference", "compile_only"]:
        sub = [c for c in cases if c["judge_guarantee"] == jg]
        add(f"judge_{jg}_pass", f"{sum(c['verdict']=='PASS' for c in sub)}/{len(sub)}",
            "compile_only is exploratory per campaign report" if jg == "compile_only" else "")
    for disp, cnt in sorted(Counter(c["case_disposition"] for c in cases).items()):
        add(f"disposition_{disp}", cnt, "see README: 'unscored' rows still carry FAIL verdicts")
    for mode, cnt in sorted(Counter(c["failure_mode_normalized"] for c in cases).items()):
        if mode != "pass":
            add(f"failure_mode_{mode}", cnt)
    envs = {c["environment"] for c in cases}
    add("scored_environments", len(envs))
    for cls, cnt in sorted(Counter(e["exclusion_class"] for e in excl).items()):
        add(f"omitted_{cls}", cnt, "outside the 416-case manifest; no score recorded")
    add("manifest_cases_unrecorded", 1, "ts_trajectory__witness_status=valid_representation=reflective__seed-0 (campaign paused)")

    with (GEN / "headline_counts.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["metric", "value", "note"])
        w.writeheader()
        w.writerows(out)
    for r in out:
        print(f"{r['metric']:<40} {r['value']}  {r['note']}")


if __name__ == "__main__":
    main()
