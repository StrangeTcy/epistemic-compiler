#!/usr/bin/env python3
"""Generate auditable POST-04 SVGs from the frozen failure evidence tables."""
from __future__ import annotations

import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "campaign-01-analysis/post-production/source_snapshots/POST-04/evidence"
OUTPUT = ROOT / "campaign-01-analysis/post-production/handoffs/figures/family-maps"

COLORS = {
    "paper": "#fbfaf7",
    "ink": "#182631",
    "muted": "#52616d",
    "grid": "#d5dde2",
    "neutral": "#edf1f3",
    "white": "#ffffff",
    "br": "#254f70",
    "co": "#55436f",
    "excluded": "#c58a18",
    "excluded_bg": "#fff7e6",
    "note_bg": "#f4f2ed",
    "node_bg": "#ffffff",
}

ORDER = [
    "patch_invalid",
    "underfit",
    "source_invalid",
    "runtime_error",
    "invalid_action",
    "overfit_visible_tests",
]
EXPECTED = {
    "patch_invalid": (24, 9, 15),
    "underfit": (20, 3, 17),
    "source_invalid": (10, 3, 7),
    "runtime_error": (3, 0, 3),
    "invalid_action": (2, 0, 2),
    "overfit_visible_tests": (2, 1, 1),
}
DISPLAY_LABELS = {
    "patch_invalid": "Empty patch file",
    "underfit": "Score below pass bar",
    "source_invalid": "Code rejected before run",
    "runtime_error": "Execution failure",
    "invalid_action": "Malformed action",
    "overfit_visible_tests": "Label / note conflict",
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def text(
    x: float,
    y: float,
    value: object,
    size: int = 13,
    fill: str | None = None,
    weight: int | str = 400,
    anchor: str = "start",
    extra: str = "",
) -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Inter,Arial,sans-serif" '
        f'font-size="{size}px" font-weight="{weight}" fill="{fill or COLORS["ink"]}" '
        f'text-anchor="{anchor}" {extra}>{esc(value)}</text>'
    )


def multiline(
    x: float,
    y: float,
    values: list[str],
    size: int = 12,
    fill: str | None = None,
    weight: int | str = 400,
    anchor: str = "middle",
    line_height: int = 17,
) -> str:
    color = fill or COLORS["muted"]
    spans = []
    for index, value in enumerate(values):
        dy = 0 if index == 0 else line_height
        spans.append(f'<tspan x="{x:.1f}" dy="{dy}">{esc(value)}</tspan>')
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Inter,Arial,sans-serif" '
        f'font-size="{size}px" font-weight="{weight}" fill="{color}" '
        f'text-anchor="{anchor}">{"".join(spans)}</text>'
    )


def read_taxonomy() -> list[dict[str, object]]:
    with (EVIDENCE / "failure_taxonomy.csv").open(encoding="utf-8", newline="") as stream:
        source = list(csv.DictReader(stream))
    rows: dict[str, dict[str, object]] = {}
    for raw in source:
        label = raw["failure_mode_normalized"]
        split = json.loads(raw["judge_guarantees"])
        row = {
            "label": label,
            "count": int(raw["count"]),
            "br": int(split.get("behavioral_reference", 0)),
            "co": int(split.get("compile_only", 0)),
        }
        rows[label] = row
    if set(rows) != set(ORDER):
        raise ValueError(f"Unexpected POST-04 failure labels: {sorted(rows)}")
    for label, expected in EXPECTED.items():
        row = rows[label]
        observed = (row["count"], row["br"], row["co"])
        if observed != expected:
            raise ValueError(f"Unexpected POST-04 split for {label}: {observed}")
        if row["br"] + row["co"] != row["count"]:
            raise ValueError(f"Judge-mode counts do not sum for {label}")
    ordered = [rows[label] for label in ORDER]
    if sum(row["count"] for row in ordered) != 61:
        raise ValueError("Expected 61 eligible failures")
    return ordered


def excluded_provider_rows() -> int:
    with (EVIDENCE / "failure_details.csv").open(encoding="utf-8", newline="") as stream:
        failures = list(csv.DictReader(stream))
    rows = [
        row for row in failures
        if row["performance_eligible"].strip().lower() == "false"
        and "provider transient" in row["exclusion_reason"].lower()
    ]
    if len(rows) != 2 or any(row["failure_mode_raw"] != "invalid_action" for row in rows):
        raise ValueError("Expected two provider-terminal raw invalid_action rows outside the primary set")
    return len(rows)


def omission_count() -> int:
    with (EVIDENCE / "campaign_exclusions.csv").open(encoding="utf-8", newline="") as stream:
        return sum(1 for _ in csv.DictReader(stream))


def pipeline_svg(rows: list[dict[str, object]], provider_count: int, omissions: int) -> str:
    by_label = {row["label"]: row for row in rows}
    total_failures = sum(row["count"] for row in rows)
    width, height = 1240, 540
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Where a code-repair case can stop</title>',
        '<desc id="desc">A plain-language map of saved code-repair outcomes: provider-service errors, empty patches and malformed actions, code rejected before running, execution errors, and judge or record conflicts. Two cases with provider-service notes are outside the 192-case comparison; 24 unscored cases are separate. The map is not a trace of each execution.</desc>',
        f'<rect x="0" y="0" width="{width}" height="{height}" fill="{COLORS["paper"]}"/>',
        text(24, 39, "Where a code-repair case can stop", 22, COLORS["ink"], 700),
        text(24, 68, "Typical route through evaluation · cards summarize the saved notes, not each run", 12, COLORS["muted"]),
        '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#52616d"/></marker></defs>',
    ]
    stages = [
        ("Model service", [
            f"{provider_count} final notes report service errors",
            "after retries; outside the 192-case",
            "comparison; raw label is retained",
        ], True),
        ("Answer and patch", [
            f"{by_label['patch_invalid']['count']} saved patch files are empty",
            f"{by_label['invalid_action']['count']} answers could not be parsed",
            "as valid actions",
        ], False),
        ("Basic code check", [
            f"{by_label['source_invalid']['count']} code submissions rejected",
            "for syntax or import-policy issues",
            "before execution",
        ], False),
        ("Run the code", [
            f"{by_label['runtime_error']['count']} cases failed during execution",
            "after passing the basic",
            "code checks",
        ], False),
        ("Test and saved result", [
            f"{by_label['underfit']['count']} results below the pass bar",
            f"{by_label['overfit_visible_tests']['count']} labels conflict",
            "with score fields and final notes",
        ], False),
    ]
    box_xs = [40, 280, 520, 760, 1000]
    box_w = 200
    node_y, node_h = 116, 56
    card_y, card_h = 190, 114
    for index, ((heading, details, is_excluded), x) in enumerate(zip(stages, box_xs)):
        if index < len(box_xs) - 1:
            parts.append(
                f'<line x1="{x + box_w + 5}" y1="{node_y + node_h / 2:.1f}" '
                f'x2="{box_xs[index + 1] - 7}" y2="{node_y + node_h / 2:.1f}" '
                f'stroke="{COLORS["muted"]}" stroke-width="1.6" marker-end="url(#arrow)"/>'
            )
        fill = COLORS["excluded_bg"] if is_excluded else COLORS["neutral"]
        stroke = COLORS["excluded"] if is_excluded else COLORS["grid"]
        parts.append(f'<rect x="{x}" y="{node_y}" width="{box_w}" height="{node_h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
        parts.append(text(x + box_w / 2, node_y + 35, heading, 14, COLORS["ink"], 700, "middle"))
        card_fill = COLORS["excluded_bg"] if is_excluded else COLORS["node_bg"]
        parts.append(f'<rect x="{x}" y="{card_y}" width="{box_w}" height="{card_h}" rx="7" fill="{card_fill}" stroke="{stroke}" stroke-width="1"/>')
        parts.append(multiline(x + box_w / 2, card_y + 28, details, 11, COLORS["muted"], 500, "middle", 20))

    parts.append(f'<rect x="40" y="330" width="1160" height="82" rx="8" fill="{COLORS["note_bg"]}" stroke="{COLORS["grid"]}"/>')
    parts.append(text(58, 357, f"{total_failures} FAIL cases in the 192-case comparison", 14, COLORS["ink"], 700))
    parts.append(text(58, 382, "24 empty patches + 2 malformed actions + 10 code-check rejections + 3 run errors + 20 below-pass results + 2 label/note conflicts", 12, COLORS["muted"]))
    parts.append(text(58, 402, f"The separate {omissions} cases omitted before scoring have no PASS/FAIL result.", 11, COLORS["muted"]))
    parts.append(text(40, 455, "The two provider-service rows remain in the raw 194 but are outside this 192-case comparison.", 12, COLORS["muted"], 600))
    parts.append(text(40, 481, "These records show what was logged, not who caused each failure or what the model was thinking.", 12, COLORS["muted"]))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def taxonomy_svg(rows: list[dict[str, object]]) -> str:
    width, height = 1120, 590
    left, top, plot_width = 330, 152, 620
    max_count, bar_h, pitch = 25, 28, 58
    scale = plot_width / max_count
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">The 61 failed cases by plain-language category and grading method</title>',
        '<desc id="desc">A stacked horizontal bar chart of 61 failures in the 192-case comparison. Bars show counts in each of six plain-language categories, split between a reference-behavior check and build or available checks, which the campaign report calls exploratory.</desc>',
        f'<rect x="0" y="0" width="{width}" height="{height}" fill="{COLORS["paper"]}"/>',
        text(24, 39, "How the 61 failed cases split across grading methods", 22, COLORS["ink"], 700),
        text(24, 68, "Bar length is a count · the two provider-service cases are outside this comparison", 12, COLORS["muted"]),
        f'<rect x="26" y="91" width="15" height="15" rx="2" fill="{COLORS["br"]}"/>',
        text(49, 103, "Reference-behavior check", 11, COLORS["muted"]),
        f'<rect x="269" y="91" width="15" height="15" rx="2" fill="{COLORS["co"]}"/>',
        text(292, 103, "Build + available checks (exploratory)", 11, COLORS["muted"]),
        text(24, 135, "WHAT THE RECORD SAYS", 10, COLORS["muted"], 700, extra='letter-spacing="0.7px"'),
        text(left, 135, "NUMBER OF CASES", 10, COLORS["muted"], 700, extra='letter-spacing="0.7px"'),
        text(985, 135, "TOTAL", 10, COLORS["muted"], 700, extra='letter-spacing="0.7px"'),
    ]
    axis_bottom = top + (len(rows) - 1) * pitch + bar_h + 8
    for tick in range(0, max_count + 1, 5):
        x = left + tick * scale
        parts.append(f'<line x1="{x:.1f}" y1="{top - 7}" x2="{x:.1f}" y2="{axis_bottom}" stroke="{COLORS["grid"]}" stroke-width="1"/>')
        parts.append(text(x, 149, tick, 10, COLORS["muted"], 400, "middle"))
    for index, row in enumerate(rows):
        y = top + index * pitch
        parts.append(text(24, y + 19, DISPLAY_LABELS[row["label"]], 12, COLORS["ink"], 550))
        br_width = row["br"] * scale
        co_width = row["co"] * scale
        if br_width:
            parts.append(f'<rect x="{left}" y="{y}" width="{br_width:.1f}" height="{bar_h}" rx="3" fill="{COLORS["br"]}"/>')
            parts.append(text(left + br_width / 2, y + 19, row["br"], 11, COLORS["white"], 700, "middle"))
        if co_width:
            co_x = left + br_width
            parts.append(f'<rect x="{co_x:.1f}" y="{y}" width="{co_width:.1f}" height="{bar_h}" rx="3" fill="{COLORS["co"]}"/>')
            parts.append(text(co_x + co_width / 2, y + 19, row["co"], 11, COLORS["white"], 700, "middle"))
        parts.append(text(985, y + 19, f"{row['count']}", 12, COLORS["ink"], 650))
    parts.append(text(24, 535, "The campaign treats build-and-available-check results as exploratory; category labels do not explain why code failed.", 11, COLORS["muted"]))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> None:
    rows = read_taxonomy()
    providers = excluded_provider_rows()
    omissions = omission_count()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    outputs = {
        "post04-failure-pipeline.svg": pipeline_svg(rows, providers, omissions),
        "post04-failure-taxonomy.svg": taxonomy_svg(rows),
    }
    for name, content in outputs.items():
        path = OUTPUT / name
        path.write_text(content, encoding="utf-8")
        print(f"{path.relative_to(ROOT)}\t{path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
