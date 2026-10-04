#!/usr/bin/env python3
"""Generate accessible POST-05 charts from the frozen selected-case tables."""
from __future__ import annotations

import csv
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "campaign-01-analysis/post-production/source_snapshots/POST-05/evidence"
OUTPUT = ROOT / "campaign-01-analysis/post-production/handoffs/figures/family-maps"
COLORS = {
    "paper": "#fbfaf7",
    "ink": "#182631",
    "muted": "#52616d",
    "grid": "#d5dde2",
    "axis": "#778691",
    "white": "#ffffff",
    "equal": "#52616d",
    "easy": "#26736d",
    "medium": "#b7791f",
    "hard": "#b34d4a",
    "pass": "#34735d",
    "fail": "#b6534b",
    "input": "#dfe5e8",
    "panel": "#f2f4f4",
}

LENGTHS = {"easy": 32, "medium": 128, "hard": 512}
EXPECTED_REGEX = {
    ("easy", 32): ("PASS", 1.0, 32),
    ("easy", 128): ("PASS", 1.0, 128),
    ("easy", 512): ("PASS", 1.0, 512),
    ("medium", 32): ("FAIL", 0.208333, 34),
    ("hard", 32): ("FAIL", 0.208333, 66),
}
EXPECTED_TASKS = {
    "ci_dependency_graph": (5, 0),
    "spreadsheet_dataflow": (5, 0),
    "template_interpreter": (5, 0),
    "sql_fixed_point": (4, 1),
    "css_state_machine": (3, 2),
    "regex_state_machine": (3, 2),
}
TASK_LABELS = {
    "ci_dependency_graph": "Build dependency graph",
    "spreadsheet_dataflow": "Spreadsheet calculation",
    "template_interpreter": "Template interpreter",
    "sql_fixed_point": "SQL chain",
    "css_state_machine": "CSS parity selector",
    "regex_state_machine": "Regex update",
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def text(x: float, y: float, value: object, size: int = 13, fill: str | None = None,
         weight: int | str = 400, anchor: str = "start", extra: str = "") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Inter,Arial,sans-serif" '
        f'font-size="{size}px" font-weight="{weight}" fill="{fill or COLORS["ink"]}" '
        f'text-anchor="{anchor}" {extra}>{esc(value)}</text>'
    )


def rect(x: float, y: float, width: float, height: float, fill: str, stroke: str = "none",
         radius: int = 0, extra: str = "") -> str:
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{height:.1f}" '
        f'rx="{radius}" fill="{fill}" stroke="{stroke}" {extra}/>'
    )


def circle(x: float, y: float, radius: float, fill: str, stroke: str = COLORS["white"],
           stroke_width: int = 2) -> str:
    return (
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{stroke_width}"/>'
    )


def read_regex_rows() -> list[dict[str, object]]:
    path = EVIDENCE / "selected_case_results.csv"
    rows: list[dict[str, object]] = []
    with path.open(encoding="utf-8", newline="") as stream:
        for raw in csv.DictReader(stream):
            if raw["environment"] != "regex_state_machine":
                continue
            levels = json.loads(raw["difficulty_levels"])
            surface = levels["surface_deceptiveness"]
            input_length = LENGTHS[levels["hidden_depth"]]
            notes = " ".join(json.loads(raw["final_notes"]))
            match = re.search(r"in=(\d+),\s*out=(\d+)", notes)
            output_length = int(match.group(2)) if match else input_length
            row = {
                "surface": surface,
                "input": input_length,
                "output": output_length,
                "verdict": raw["verdict"],
                "score": float(raw["score"]),
            }
            rows.append(row)
    observed = {
        (str(row["surface"]), int(row["input"])):
        (str(row["verdict"]), float(row["score"]), int(row["output"]))
        for row in rows
    }
    if observed != EXPECTED_REGEX:
        raise ValueError(f"Unexpected POST-05 regex outcomes: {observed}")
    return sorted(rows, key=lambda row: (int(row["input"]), str(row["surface"])))


def read_task_rows() -> list[dict[str, object]]:
    path = EVIDENCE / "environment_summary.csv"
    rows: list[dict[str, object]] = []
    with path.open(encoding="utf-8", newline="") as stream:
        for raw in csv.DictReader(stream):
            name = raw["environment"]
            if name not in EXPECTED_TASKS:
                continue
            row = {
                "environment": name,
                "passes": int(raw["passes_performance_set"]),
                "fails": int(raw["fails_performance_set"]),
                "eligible": int(raw["performance_eligible_cases"]),
            }
            expected = EXPECTED_TASKS[name]
            if (row["passes"], row["fails"]) != expected or row["eligible"] != 5:
                raise ValueError(f"Unexpected POST-05 outcome tally for {name}: {row}")
            rows.append(row)
    if {str(row["environment"]) for row in rows} != set(EXPECTED_TASKS):
        raise ValueError("POST-05 environment summary does not contain the six expected tasks")
    if sum(int(row["passes"]) for row in rows) != 25 or sum(int(row["fails"]) for row in rows) != 5:
        raise ValueError("POST-05 task pass/fail totals do not sum to 25/5")
    return [next(row for row in rows if row["environment"] == name) for name in EXPECTED_TASKS]


def regex_length_svg(rows: list[dict[str, object]]) -> str:
    width, height = 1040, 610
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Regex input and output lengths</title>',
        '<desc id="desc">The main scatterplot compares input string length with returned string length. Easy-surface results lie on the equal-length diagonal at 32, 128, and 512. A close-up for input length 32 shows easy output 32, medium output 34, and hard output 66. Each setting is one selected run.</desc>',
        rect(0, 0, width, height, COLORS["paper"]),
        text(28, 38, "The regex output-length pattern", 23, COLORS["ink"], 700),
        text(28, 66, "The diagonal means input and output have the same length; the inset enlarges the 32-character cases.", 13, COLORS["muted"]),
    ]
    # Main full-range scatterplot.
    left, top, size, max_value = 74.0, 105.0, 420.0, 512.0
    bottom = top + size
    scale = size / max_value
    for tick in (0, 128, 256, 384, 512):
        x = left + tick * scale
        y = bottom - tick * scale
        parts.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{bottom}" stroke="{COLORS["grid"]}" stroke-width="1"/>')
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + size}" y2="{y:.1f}" stroke="{COLORS["grid"]}" stroke-width="1"/>')
        parts.append(text(x, bottom + 22, tick, 11, COLORS["muted"], 400, "middle"))
        parts.append(text(left - 12, y + 4, tick, 11, COLORS["muted"], 400, "end"))
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{left + size}" y2="{top}" stroke="{COLORS["equal"]}" stroke-width="2" stroke-dasharray="7 6"/>')
    parts.append(text(left + 220, top + 174, "same-length line", 11, COLORS["muted"], 600, "middle", 'transform="rotate(-45 294 279)"'))
    parts.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="{COLORS["axis"]}" stroke-width="1.5"/>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{left + size}" y2="{bottom}" stroke="{COLORS["axis"]}" stroke-width="1.5"/>')
    parts.append(text(left + size / 2, bottom + 52, "Input string length (characters)", 12, COLORS["ink"], 600, "middle"))
    parts.append(text(20, top + size / 2, "Output length (characters)", 11, COLORS["ink"], 600, "middle", f'transform="rotate(-90 20 {top + size / 2:.1f})"'))
    color_by_surface = {"easy": COLORS["easy"], "medium": COLORS["medium"], "hard": COLORS["hard"]}
    for row in rows:
        x = left + int(row["input"]) * scale
        y = bottom - int(row["output"]) * scale
        parts.append(circle(x, y, 7, color_by_surface[str(row["surface"])], stroke_width=2))
    # Legend.
    legend_x = 84
    for label, color, advance in (("easy surface", COLORS["easy"], 126), ("medium surface", COLORS["medium"], 145), ("hard surface", COLORS["hard"], 124)):
        parts.append(circle(legend_x + 5, 590, 5, color, stroke_width=1))
        parts.append(text(legend_x + 17, 594, label, 11, COLORS["muted"]))
        legend_x += advance

    # Inset: a common 32-character input, expanded on a 0–75 output scale.
    panel_x, panel_y, panel_w, panel_h = 565.0, 105.0, 435.0, 440.0
    parts.append(rect(panel_x, panel_y, panel_w, panel_h, COLORS["panel"], COLORS["grid"], radius=10))
    parts.append(text(panel_x + 22, panel_y + 34, "Close-up: input length is 32", 16, COLORS["ink"], 700))
    parts.append(text(panel_x + 22, panel_y + 58, "The vertical line marks the required output length.", 11, COLORS["muted"]))
    x0, x1, axis_y = panel_x + 112, panel_x + 365, panel_y + 365
    mini_max = 75
    mini_scale = (x1 - x0) / mini_max
    for tick in (0, 20, 40, 60):
        x = x0 + tick * mini_scale
        parts.append(f'<line x1="{x:.1f}" y1="{panel_y + 102}" x2="{x:.1f}" y2="{axis_y}" stroke="{COLORS["grid"]}" stroke-width="1"/>')
        parts.append(text(x, axis_y + 19, tick, 10, COLORS["muted"], 400, "middle"))
    input_x = x0 + 32 * mini_scale
    parts.append(f'<line x1="{input_x:.1f}" y1="{panel_y + 91}" x2="{input_x:.1f}" y2="{axis_y - 4}" stroke="{COLORS["equal"]}" stroke-width="2" stroke-dasharray="5 4"/>')
    row_y = {"easy": panel_y + 150, "medium": panel_y + 230, "hard": panel_y + 310}
    for surface in ("easy", "medium", "hard"):
        row = next(r for r in rows if r["surface"] == surface and r["input"] == 32)
        y = row_y[surface]
        output = int(row["output"])
        out_x = x0 + output * mini_scale
        parts.append(text(panel_x + 22, y + 5, surface, 12, color_by_surface[surface], 700))
        parts.append(rect(x0, y - 7, input_x - x0, 14, COLORS["input"], radius=7))
        if output > 32:
            parts.append(rect(input_x, y - 4, max(2, out_x - input_x), 8, color_by_surface[surface], radius=4))
        parts.append(circle(out_x, y, 6, color_by_surface[surface], stroke_width=2))
        parts.append(text(min(out_x + 12, panel_x + panel_w - 26), y + 5, f"{output}", 11, COLORS["ink"], 700))
    parts.append(text((x0 + x1) / 2, axis_y + 41, "Output string length (characters)", 10, COLORS["muted"], 400, "middle"))
    parts.append(text(input_x + 7, panel_y + 91, "input = 32", 10, COLORS["muted"], 600))
    parts.append(text(566, 572, "The full plot compresses 32→34; the close-up reveals the mismatch.", 11, COLORS["muted"]))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def task_outcomes_svg(rows: list[dict[str, object]]) -> str:
    width, height = 930, 520
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Pass and fail counts for the six code tasks</title>',
        '<desc id="desc">Horizontal stacked bars show five selected cases for each distinct task. The build dependency, spreadsheet, and template tasks each pass five; SQL passes four; CSS and regex pass three each. The bars are counts for different tasks and judges, not one shared difficulty scale.</desc>',
        rect(0, 0, width, height, COLORS["paper"]),
        text(28, 39, "The 30 cases are spread across six different tasks", 22, COLORS["ink"], 700),
        text(28, 68, "Each bar totals five selected cases; it does not put the tasks on one difficulty scale.", 13, COLORS["muted"]),
        rect(35, 91, 16, 16, COLORS["pass"], radius=3),
        text(58, 104, "PASS", 11, COLORS["muted"], 600),
        rect(126, 91, 16, 16, COLORS["fail"], radius=3),
        text(149, 104, "FAIL", 11, COLORS["muted"], 600),
    ]
    x0, unit, bar_h = 300.0, 76.0, 34.0
    start_y, row_gap = 143.0, 57.0
    for index, row in enumerate(rows):
        name = str(row["environment"])
        label = TASK_LABELS[name]
        passed, failed = int(row["passes"]), int(row["fails"])
        y = start_y + index * row_gap
        parts.append(text(34, y + 22, label, 13, COLORS["ink"], 600))
        if passed:
            parts.append(rect(x0, y, passed * unit, bar_h, COLORS["pass"], radius=6))
            if passed >= 2:
                parts.append(text(x0 + passed * unit / 2, y + 22, f"{passed} pass", 12, COLORS["white"], 700, "middle"))
        if failed:
            fx = x0 + passed * unit
            parts.append(rect(fx, y, failed * unit, bar_h, COLORS["fail"], radius=6))
            parts.append(text(fx + failed * unit / 2, y + 22, f"{failed} fail", 11, COLORS["white"], 700, "middle"))
        parts.append(text(x0 + 5 * unit + 16, y + 22, f"{passed}/5 passed", 12, COLORS["ink"], 600))
    parts.append(f'<line x1="{x0}" y1="{start_y - 8}" x2="{x0}" y2="{start_y + 5 * row_gap + bar_h + 8}" stroke="{COLORS["grid"]}" stroke-width="1"/>')
    parts.append(text(34, 505, "25 pass, 5 fail overall. Each task uses different code, inputs, and checks.", 12, COLORS["muted"], 600))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    regex_rows = read_regex_rows()
    task_rows = read_task_rows()
    outputs = {
        OUTPUT / "post05-regex-length-comparison.svg": regex_length_svg(regex_rows),
        OUTPUT / "post05-task-outcomes.svg": task_outcomes_svg(task_rows),
    }
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
        print(f"{path.relative_to(ROOT)}\t{path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
