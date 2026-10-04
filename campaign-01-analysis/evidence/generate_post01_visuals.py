#!/usr/bin/env python3
"""Generate auditable SVG heatmaps and within-family radar charts for POST-01.

All chart values are derived from the frozen campaign case_results.csv table.
The heatmaps preserve each selected configuration; radar plots summarize only
performance-eligible rows and are not intended for cross-family comparison.
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "campaign-01-analysis/evidence/generated/case_results.csv"
DEFAULT_OUTPUT = ROOT / "campaign-01-analysis/post-production/handoffs/figures/family-maps"

FAMILIES = {
    "category_theoretic_compositional": "Category-theoretic / compositional",
    "weird_machine": "Weird machines",
    "ml_debugging": "ML debugging",
    "epistemic_games": "Epistemic games",
}

COLORS = {
    "paper": "#fbfaf7",
    "ink": "#182631",
    "muted": "#52616d",
    "grid": "#d5dde2",
    "pass": "#197a69",
    "fail": "#b64d42",
    "excluded": "#c58a18",
    "neutral": "#edf1f3",
    "br": "#dceaf5",
    "co": "#e8e1f1",
    "br_ink": "#254f70",
    "co_ink": "#55436f",
    "white": "#ffffff",
    "radar_fill": "#2a8074",
}

FAILURE_LABELS = {
    "patch_invalid": "PATCH",
    "underfit": "UNDER",
    "source_invalid": "SOURCE",
    "runtime_error": "RUNTIME",
    "invalid_action": "ACTION",
    "overfit_visible_tests": "OVERFIT",
}

FAMILY_AXIS_ORDER = {
    "architecture_naturality": ["naming", "symptom_mask"],
    "categorical_lenses": ["naming", "symptom_mask"],
    "compositional_optimizer": ["naming", "symptom_mask"],
    "equivariant_diagram": ["naming", "symptom_mask"],
    "functorial_augmentation": ["naming", "symptom_mask"],
    "gnn_message_passing": ["naming", "symptom_mask"],
    "monadic_reward": ["naming", "symptom_mask"],
    "neuro_symbolic_parser": ["naming", "symptom_mask"],
    "semiring_unification": ["naming", "symptom_mask"],
    "sheaf_invariant_gluing": ["naming", "symptom_mask"],
    "sheaf_physical_constraints": ["naming", "symptom_mask"],
    "sheaf_schema_sync": ["naming", "symptom_mask"],
    "ssm_parallel_scan": ["naming", "symptom_mask"],
    "stochastic_monad": ["naming", "symptom_mask"],
    "tensor_functor": ["naming", "symptom_mask"],
    "tokenizer_adjunction": ["naming", "symptom_mask"],
    "transformer_ssm_lift": ["naming", "symptom_mask"],
    "ci_dependency_graph": ["hidden_depth", "surface_deceptiveness"],
    "css_state_machine": ["hidden_depth", "surface_deceptiveness"],
    "regex_state_machine": ["hidden_depth", "surface_deceptiveness"],
    "spreadsheet_dataflow": ["hidden_depth", "surface_deceptiveness"],
    "sql_fixed_point": ["hidden_depth", "surface_deceptiveness"],
    "template_interpreter": ["hidden_depth", "surface_deceptiveness"],
}

ML_AXIS_ORDER = {
    "batchnorm_ema": [
        ("data_complexity", "DC"),
        ("optimizer_hint", "OH"),
        ("red_herring", "RH"),
        ("symptom_mask", "SM"),
        ("visible_tests", "VT"),
    ],
    "glyph": [
        ("architecture", "Arch"),
        ("data_clue", "Clue"),
        ("red_herring", "Red"),
        ("symptom_mask", "Sym"),
        ("visible_tests", "Tests"),
    ],
    "moco": [
        ("distractors", "Dist"),
        ("queue_math", "Queue"),
        ("symptom_mask", "Sym"),
        ("temperature", "Temp"),
        ("visible_tests", "Tests"),
    ],
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def truth(value: str) -> bool:
    return value.strip().lower() == "true"


def text(x: float, y: float, value: object, size: int = 13, fill: str | None = None,
         weight: int | str = 400, anchor: str = "start", extra: str = "") -> str:
    color = fill or COLORS["ink"]
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Inter,Arial,sans-serif" '
        f'font-size="{size}px" font-weight="{weight}" fill="{color}" '
        f'text-anchor="{anchor}" {extra}>{esc(value)}</text>'
    )


def multiline(x: float, y: float, lines: list[str], size: int = 12,
              fill: str | None = None, weight: int | str = 500,
              anchor: str = "middle", line_height: int = 15) -> str:
    color = fill or COLORS["ink"]
    pieces = [
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Inter,Arial,sans-serif" '
        f'font-size="{size}px" font-weight="{weight}" fill="{color}" '
        f'text-anchor="{anchor}">'
    ]
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else line_height
        pieces.append(f'<tspan x="{x:.1f}" dy="{dy}">{esc(line)}</tspan>')
    pieces.append("</text>")
    return "".join(pieces)


def rect(x: float, y: float, w: float, h: float, fill: str,
         rx: int = 4, stroke: str = "none", sw: float = 1) -> str:
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
        f'rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )


def svg_start(width: int, height: int, title: str, description: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{esc(title)}</title>',
        f'<desc id="desc">{esc(description)}</desc>',
        rect(0, 0, width, height, COLORS["paper"], rx=0),
    ]


def svg_end(parts: list[str], path: Path) -> None:
    parts.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def summary(rows: list[dict]) -> tuple[int, int, int, int, int]:
    eligible_rows = [r for r in rows if r["eligible"]]
    passed = sum(r["verdict"] == "PASS" for r in eligible_rows)
    failed = sum(r["verdict"] == "FAIL" for r in eligible_rows)
    return len(rows), len(eligible_rows), passed, failed, len(rows) - len(eligible_rows)


def case_tooltip(row: dict) -> str:
    notes = row["final_notes"]
    try:
        notes = json.loads(notes)
    except (TypeError, json.JSONDecodeError):
        pass
    try:
        metrics = json.loads(row["final_metrics"])
    except (TypeError, json.JSONDecodeError):
        metrics = row["final_metrics"]
    reason = row.get("exclusion_reason", "")
    return (
        f'Case: {row["case_id"]}; settings: {json.dumps(row["difficulty"], sort_keys=True)}; '
        f'judge: {row["judge"]}; raw verdict: {row["verdict"]}; '
        f'terminal label: {row["terminal"]}; eligible for performance set: {row["eligible"]}; '
        f'final metrics: {metrics}; final notes: {notes}; exclusion note: {reason}'
    )


def outcome_style(row: dict) -> tuple[str, str]:
    if not row["eligible"]:
        return COLORS["excluded"], "EXCL"
    if row["verdict"] == "PASS":
        return COLORS["pass"], "PASS"
    label = FAILURE_LABELS.get(row["terminal"], row["terminal"].upper()[:8])
    return COLORS["fail"], f"F · {label}"


def mode_badge(x: float, y: float, mode: str, width: int = 42, height: int = 20) -> str:
    if mode == "behavioral_reference":
        fill, ink, label = COLORS["br"], COLORS["br_ink"], "BR"
    else:
        fill, ink, label = COLORS["co"], COLORS["co_ink"], "CO"
    return (
        rect(x, y, width, height, fill, rx=5)
        + text(x + width / 2, y + height / 2 + 4, label, size=10, fill=ink,
               weight=700, anchor="middle")
    )


def legend_cell(parts: list[str], x: float, y: float, fill: str, label: str) -> None:
    parts.append(rect(x, y - 12, 18, 16, fill, rx=3))
    parts.append(text(x + 25, y, label, size=11, fill=COLORS["muted"]))


def grouped_by_environment(rows: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[row["environment"]].append(row)
    return dict(grouped)


def standard_heatmap(rows: list[dict], family_key: str, family_label: str,
                     axis_fields: tuple[str, str], columns: list[tuple[str, str, str]],
                     output: Path) -> None:
    grouped = grouped_by_environment(rows)
    environments = sorted(grouped)
    width = 1310
    data_y = 170
    row_step = 32
    height = data_y + len(environments) * row_step + 93
    table_x = 400
    column_step = 176
    tile_w = 164
    tile_h = 24
    parts = svg_start(
        width, height,
        f"{family_label} case outcome heatmap",
        "Every selected case is a heatmap cell. Column headers show exact easy, medium, and hard settings; row badges show judge mode; cell color shows outcome and cell text shows terminal label or exclusion status.",
    )
    total, eligible_n, passed, failed, excluded = summary(rows)
    parts += [
        text(24, 39, f"{family_label} · case outcome heatmap", 22, weight=700),
        text(24, 67, f"{total} raw cases · {eligible_n} eligible · {passed} PASS · {failed} FAIL · {excluded} excluded", 13, fill=COLORS["muted"]),
    ]
    legend_cell(parts, 24, 100, COLORS["pass"], "PASS")
    legend_cell(parts, 130, 100, COLORS["fail"], "FAIL; tile text gives terminal label")
    legend_cell(parts, 425, 100, COLORS["excluded"], "EXCL; retained in raw rows, omitted from performance rates")
    parts.append(mode_badge(900, 87, "behavioral_reference"))
    parts.append(text(948, 101, "BR = behavioral reference", 11, fill=COLORS["muted"]))
    parts.append(mode_badge(1130, 87, "compile_only"))
    parts.append(text(1178, 101, "CO = compile-only", 11, fill=COLORS["muted"]))

    parts.append(text(24, 144, "ENVIRONMENT", 10, fill=COLORS["muted"], weight=700))
    parts.append(text(323, 144, "PASS / eligible", 10, fill=COLORS["muted"], weight=700, anchor="middle"))
    for j, (head, sub, _) in enumerate(columns):
        center = table_x + j * column_step + tile_w / 2
        parts.append(multiline(center, 132, [head, sub], size=11, fill=COLORS["muted"], line_height=14))

    for i, env in enumerate(environments):
        env_rows = grouped[env]
        eligible_rows = [r for r in env_rows if r["eligible"]]
        env_passes = sum(r["verdict"] == "PASS" for r in eligible_rows)
        modes = {r["judge"] for r in env_rows}
        if len(modes) != 1:
            raise ValueError(f"Mixed judge modes within environment {env}: {modes}")
        mode = next(iter(modes))
        y = data_y + i * row_step
        if i % 2 == 0:
            parts.append(rect(16, y - 2, width - 32, row_step, "#f4f2ed", rx=4))
        parts.append(text(24, y + 16, env, 12, weight=600))
        parts.append(mode_badge(268, y + 2, mode, width=38, height=19))
        parts.append(text(323, y + 16, f"{env_passes}/{len(eligible_rows)}", 11,
                          fill=COLORS["muted"], anchor="middle", weight=600))
        lookup = {tuple(row["difficulty"].get(axis, "") for axis in axis_fields): row for row in env_rows}
        for j, (head, sub, key_json) in enumerate(columns):
            key = tuple(json.loads(key_json)[axis] for axis in axis_fields)
            row = lookup.get(key)
            x = table_x + j * column_step
            if row is None:
                parts.append(rect(x, y + 2, tile_w, tile_h, COLORS["neutral"], rx=3, stroke=COLORS["grid"]))
                parts.append(text(x + tile_w / 2, y + 18, "—", 13, fill=COLORS["muted"], anchor="middle"))
                continue
            fill, label = outcome_style(row)
            parts.append(f'<g><title>{esc(case_tooltip(row))}</title>')
            parts.append(rect(x, y + 2, tile_w, tile_h, fill, rx=3))
            parts.append(text(x + tile_w / 2, y + 18, label, 10, fill=COLORS["white"],
                              weight=700, anchor="middle"))
            parts.append("</g>")

    footer_y = data_y + len(environments) * row_step + 26
    parts.append(text(24, footer_y, "Terminal labels:", 10, fill=COLORS["muted"], weight=700))
    parts.append(text(118, footer_y, "PATCH = patch_invalid · UNDER = underfit · SOURCE = source_invalid · RUN = runtime_error · ACTION = invalid_action · OVERFIT = overfit_visible_tests", 10, fill=COLORS["muted"]))
    parts.append(text(24, footer_y + 21, "E/M/H mean easy/medium/hard. Headers preserve the exact factor and level; those labels are not a shared scale.", 10, fill=COLORS["muted"]))
    svg_end(parts, output)


def ml_variant_order(env: str, row: dict) -> tuple[int, int]:
    axes = ML_AXIS_ORDER[env]
    non_easy = [(i, axis, abbrev, row["difficulty"].get(axis, "easy"))
                for i, (axis, abbrev) in enumerate(axes)
                if row["difficulty"].get(axis, "easy") != "easy"]
    if not non_easy:
        return (-1, -1)
    if len(non_easy) != 1:
        raise ValueError(f"Expected one changed factor for {env}: {row['difficulty']}")
    i, _, _, level = non_easy[0]
    level_order = {"medium": 0, "hard": 1}
    return (i, level_order.get(level, 2))


def ml_variant_label(env: str, row: dict) -> str:
    axes = ML_AXIS_ORDER[env]
    changed = [(abbrev, row["difficulty"].get(axis, "easy"))
               for axis, abbrev in axes if row["difficulty"].get(axis, "easy") != "easy"]
    if not changed:
        return "BASE"
    abbrev, level = changed[0]
    return f"{abbrev} {level[0].upper()}"


def ml_heatmap(rows: list[dict], output: Path) -> None:
    grouped = grouped_by_environment(rows)
    environments = ["batchnorm_ema", "glyph", "moco"]
    width = 1570
    height = 735
    x0 = 270
    tile_w = 105
    gap = 7
    tile_h = 35
    panel_y0 = 135
    panel_step = 190
    parts = svg_start(
        width, height,
        "ML debugging case outcome heatmaps",
        "Three separate heatmap strips preserve every selected batchnorm, glyph, and MoCo case. Each cell label identifies the one factor and source level changed from the all-easy baseline; judge mode, eligible pass count, outcome, and terminal label are shown.",
    )
    total, eligible_n, passed, failed, excluded = summary(rows)
    parts += [
        text(24, 39, "ML debugging · case outcome heatmaps", 22, weight=700),
        text(24, 67, f"{total} raw cases · {eligible_n} eligible · {passed} PASS · {failed} FAIL · {excluded} excluded", 13, fill=COLORS["muted"]),
        text(24, 96, "Cell headers: BASE = all easy; M/H = medium/hard on the named factor; all other factors remain easy.", 11, fill=COLORS["muted"]),
    ]
    for panel_i, env in enumerate(environments):
        env_rows = sorted(grouped[env], key=lambda r: ml_variant_order(env, r))
        eligible_rows = [r for r in env_rows if r["eligible"]]
        passes = sum(r["verdict"] == "PASS" for r in eligible_rows)
        mode = env_rows[0]["judge"]
        py = panel_y0 + panel_i * panel_step
        parts.append(rect(16, py - 16, width - 32, 170, "#f4f2ed" if panel_i % 2 == 0 else "#ffffff", rx=8, stroke=COLORS["grid"]))
        parts.append(text(28, py + 10, env, 16, weight=700))
        parts.append(mode_badge(205, py - 5, mode, width=38, height=19))
        parts.append(text(254, py + 10, f"{passes}/{len(eligible_rows)} eligible PASS", 12, fill=COLORS["muted"], weight=600))
        for j, row in enumerate(env_rows):
            x = x0 + j * (tile_w + gap)
            label = ml_variant_label(env, row)
            parts.append(text(x + tile_w / 2, py + 42, label, 10, fill=COLORS["muted"], anchor="middle", weight=700))
            fill, status = outcome_style(row)
            parts.append(f'<g><title>{esc(case_tooltip(row))}</title>')
            parts.append(rect(x, py + 52, tile_w, tile_h, fill, rx=4))
            parts.append(text(x + tile_w / 2, py + 74, status, 10, fill=COLORS["white"], weight=700, anchor="middle"))
            parts.append("</g>")
        axis_labels = [f"{abbrev} = {axis}" for axis, abbrev in ML_AXIS_ORDER[env]]
        parts.append(text(28, py + 116, "Factor key:", 10, fill=COLORS["muted"], weight=700))
        parts.append(text(90, py + 116, " · ".join(axis_labels), 10, fill=COLORS["muted"]))
    footer = panel_y0 + 3 * panel_step - 27
    legend_cell(parts, 24, footer, COLORS["pass"], "PASS")
    legend_cell(parts, 130, footer, COLORS["fail"], "FAIL; tile text is terminal label")
    legend_cell(parts, 415, footer, COLORS["excluded"], "EXCL; excluded from performance rates")
    parts.append(mode_badge(760, footer - 13, "behavioral_reference"))
    parts.append(text(808, footer + 1, "BR = behavioral reference", 11, fill=COLORS["muted"]))
    parts.append(mode_badge(990, footer - 13, "compile_only"))
    parts.append(text(1038, footer + 1, "CO = compile-only", 11, fill=COLORS["muted"]))
    svg_end(parts, output)


def epistemic_sort_key(row: dict) -> tuple:
    d = row["difficulty"]
    order = {
        "scenario": {"report": 0, "trap": 1},
        "evidence": {"ambiguous": 0, "strong": 1, "weak": 2},
        "prior": {"balanced": 0, "skewed": 1},
        "presentation": {"paired": 0, "solo": 1},
        "framing": {"bare_table": 0, "narrative": 1},
    }
    return tuple(order[axis].get(d.get(axis, ""), 9) for axis in order)


def epistemic_heatmap(rows: list[dict], output: Path) -> list[dict]:
    ordered = sorted(rows, key=epistemic_sort_key)
    width = 1330
    header_y = 145
    row_y0 = 177
    row_h = 44
    height = row_y0 + len(ordered) * row_h + 78
    cols = [
        (24, 56, "CASE"),
        (80, 135, "SCENARIO"),
        (215, 150, "EVIDENCE"),
        (365, 125, "PRIOR"),
        (490, 150, "PRESENTATION"),
        (640, 175, "FRAMING"),
        (815, 112, "JUDGE"),
        (927, 160, "OUTCOME"),
    ]
    parts = svg_start(
        width, height,
        "Epistemic games categorical case heatmap",
        "All selected epistemic-games cases are shown by their exact scenario, evidence, prior, presentation, and framing settings. The outcome heatmap is all pass under behavioral-reference judging; factor values are categories, not easy-medium-hard levels.",
    )
    total, eligible_n, passed, failed, excluded = summary(ordered)
    parts += [
        text(24, 39, "Epistemic games · categorical case heatmap", 22, weight=700),
        text(24, 67, f"{total} raw cases · {eligible_n} eligible · {passed} PASS · {failed} FAIL", 13, fill=COLORS["muted"]),
        text(24, 96, "These factors use categorical values, not easy/medium/hard levels.", 12, fill=COLORS["muted"]),
    ]
    for x, w, label in cols:
        parts.append(text(x + w / 2, header_y, label, 10, fill=COLORS["muted"], weight=700, anchor="middle"))
    for i, row in enumerate(ordered):
        y = row_y0 + i * row_h
        if i % 2 == 0:
            parts.append(rect(18, y - 3, width - 36, row_h, "#f4f2ed", rx=4))
        d = row["difficulty"]
        label = chr(ord("A") + i)
        values = [
            label,
            d["scenario"],
            d["evidence"],
            d["prior"],
            d["presentation"],
            d["framing"],
            "BR",
            "PASS" if row["verdict"] == "PASS" else "FAIL",
        ]
        for col_i, ((x, w, _), value) in enumerate(zip(cols, values)):
            if col_i == 7:
                fill = COLORS["pass"] if row["verdict"] == "PASS" else COLORS["fail"]
                fg = COLORS["white"]
            elif col_i == 6:
                fill = COLORS["br"]
                fg = COLORS["br_ink"]
            else:
                fill = "#e8edf0"
                fg = COLORS["ink"]
            parts.append(f'<g><title>{esc(case_tooltip(row))}</title>')
            parts.append(rect(x + 2, y, w - 5, 35, fill, rx=4))
            parts.append(text(x + w / 2, y + 22, value, 11, fill=fg, weight=650, anchor="middle"))
            parts.append("</g>")
    footer_y = row_y0 + len(ordered) * row_h + 25
    parts.append(text(24, footer_y, "Each row is one selected case; the full case ID, raw label, and final note are available on hover.", 10, fill=COLORS["muted"]))
    svg_end(parts, output)
    return ordered


def radar_svg(entities: list[dict], family_label: str, output: Path,
              spoke_kind: str = "environment") -> None:
    width, height = 960, 755
    cx, cy, radius = 480, 410, 205
    parts = svg_start(
        width, height,
        f"{family_label} within-family radar chart",
        "Radar radius is the pass fraction among performance-eligible rows, on a zero-to-one-hundred-percent scale. Marker shapes distinguish behavioral-reference from compile-only judge modes. Numbered spokes match the adjacent heatmap order; this is descriptive, not a cross-family score.",
    )
    total_raw = sum(e["raw_n"] for e in entities)
    total_eligible = sum(e["n"] for e in entities)
    total_pass = sum(e["passed"] for e in entities)
    total_fail = sum(e["failed"] for e in entities)
    radar_subtitle = (
        "Eligible PASS share by case configuration; one spoke per selected case"
        if spoke_kind == "case"
        else "Eligible PASS share by environment; each spoke is one task environment"
    )
    parts += [
        text(24, 39, f"{family_label} · within-family radar", 22, weight=700),
        text(24, 68, radar_subtitle, 12, fill=COLORS["muted"]),
        text(24, 96, f"{total_pass}/{total_eligible} eligible PASS · {total_fail} eligible FAIL · {total_raw - total_eligible} excluded from rate", 12, fill=COLORS["muted"], weight=600),
    ]
    # Mode legend; open circle = behavioral reference, square = compile-only.
    parts.append('<circle cx="31" cy="124" r="5" fill="#ffffff" stroke="#254f70" stroke-width="2"/>')
    parts.append(text(45, 128, "BR: behavioral-reference judge", 10, fill=COLORS["muted"]))
    parts.append(rect(250, 119, 10, 10, COLORS["co"], rx=1, stroke=COLORS["co_ink"], sw=2))
    parts.append(text(268, 128, "CO: compile-only judge", 10, fill=COLORS["muted"]))
    parts.append(text(485, 128, "Numbered spokes follow the adjacent heatmap order", 10, fill=COLORS["muted"]))

    n = len(entities)
    if n < 3:
        raise ValueError("Radar chart needs at least three spokes")
    angles = [-math.pi / 2 + 2 * math.pi * i / n for i in range(n)]
    # Concentric rings and radial axes.
    for level in (25, 50, 75, 100):
        r = radius * level / 100
        pts = []
        for a in angles:
            pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
        parts.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="{COLORS["grid"]}" stroke-width="1"/>')
        parts.append(text(cx + 6, cy - r + 3, f"{level}%", 9, fill=COLORS["muted"]))
    for i, a in enumerate(angles):
        x2, y2 = cx + radius * math.cos(a), cy + radius * math.sin(a)
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{COLORS["grid"]}" stroke-width="1"/>')
        label_r = radius + 29
        lx, ly = cx + label_r * math.cos(a), cy + label_r * math.sin(a)
        parts.append(text(lx, ly + 4, f"{i + 1:02d}", 10, fill=COLORS["muted"], weight=700, anchor="middle"))
    value_points = []
    for a, entity in zip(angles, entities):
        value = entity["passed"] / entity["n"] if entity["n"] else 0
        r = radius * value
        value_points.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    point_string = " ".join(f"{x:.1f},{y:.1f}" for x, y in value_points)
    parts.append(f'<polygon points="{point_string}" fill="{COLORS["radar_fill"]}" fill-opacity="0.22" stroke="{COLORS["radar_fill"]}" stroke-width="2.5"/>')
    for i, (point, entity) in enumerate(zip(value_points, entities)):
        x, y = point
        p = entity["passed"]
        den = entity["n"]
        percent = round(100 * p / den) if den else 0
        tooltip = (
            f'{entity["name"]}; PASS {p}/{den} eligible; {percent}%; '
            f'judge mode {entity["mode"]}; raw rows {entity["raw_n"]}'
        )
        parts.append(f'<g><title>{esc(tooltip)}</title>')
        if entity["mode"] == "behavioral_reference":
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="#ffffff" stroke="{COLORS["br_ink"]}" stroke-width="2.5"/>')
        else:
            parts.append(rect(x - 5, y - 5, 10, 10, COLORS["co"], rx=1, stroke=COLORS["co_ink"], sw=2.2))
        parts.append("</g>")
    if spoke_kind == "case":
        parts.append(text(24, 727, "Each spoke is a distinct selected case configuration, not a replicate; all categorical factor values are shown in the heatmap.", 10, fill=COLORS["muted"]))
    else:
        parts.append(text(24, 727, "Each spoke is one environment; spoke IDs match heatmap rows. Rates are one-seed descriptions, not causal estimates.", 10, fill=COLORS["muted"]))
    svg_end(parts, output)


def family_entities(rows: list[dict], family_key: str,
                    epistemic_order: list[dict] | None = None) -> list[dict]:
    if family_key == "epistemic_games":
        ordered = epistemic_order or sorted(rows, key=epistemic_sort_key)
        entities = []
        for i, row in enumerate(ordered):
            entities.append({
                "name": f"{chr(ord('A') + i)} · {row['difficulty']['scenario']} / {row['difficulty']['evidence']}",
                "mode": row["judge"],
                "raw_n": 1,
                "n": 1 if row["eligible"] else 0,
                "passed": 1 if row["eligible"] and row["verdict"] == "PASS" else 0,
                "failed": 1 if row["eligible"] and row["verdict"] == "FAIL" else 0,
            })
        return entities
    grouped = grouped_by_environment(rows)
    entities = []
    for env in sorted(grouped):
        env_rows = grouped[env]
        eligible_rows = [r for r in env_rows if r["eligible"]]
        entities.append({
            "name": env,
            "mode": env_rows[0]["judge"],
            "raw_n": len(env_rows),
            "n": len(eligible_rows),
            "passed": sum(r["verdict"] == "PASS" for r in eligible_rows),
            "failed": sum(r["verdict"] == "FAIL" for r in eligible_rows),
        })
    return entities


def load_rows(input_path: Path) -> list[dict]:
    result = []
    with input_path.open(newline="", encoding="utf-8") as handle:
        for raw in csv.DictReader(handle):
            raw["difficulty"] = json.loads(raw["difficulty_levels"])
            raw["eligible"] = truth(raw["performance_eligible"])
            raw["judge"] = raw["judge_guarantee"]
            raw["terminal"] = raw["failure_mode_normalized"]
            result.append(raw)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    all_rows = load_rows(args.input)
    selected = {key: [r for r in all_rows if r["analysis_family"] == key] for key in FAMILIES}
    expected = {
        "category_theoretic_compositional": (85, 84, 57, 27),
        "weird_machine": (30, 30, 25, 5),
        "ml_debugging": (30, 30, 9, 21),
        "epistemic_games": (7, 7, 7, 0),
    }
    for key, rows in selected.items():
        raw_n, eligible_n, passed, failed, _ = summary(rows)
        if (raw_n, eligible_n, passed, failed) != expected[key]:
            raise ValueError(f"Unexpected frozen counts for {key}: {(raw_n, eligible_n, passed, failed)}")

    category_cols = [
        ("Baseline", "naming E · symptom mask E", json.dumps({"naming": "easy", "symptom_mask": "easy"})),
        ("Symptom mask", "medium · naming E", json.dumps({"naming": "easy", "symptom_mask": "medium"})),
        ("Symptom mask", "hard · naming E", json.dumps({"naming": "easy", "symptom_mask": "hard"})),
        ("Naming", "medium · symptom mask E", json.dumps({"naming": "medium", "symptom_mask": "easy"})),
        ("Naming", "hard · symptom mask E", json.dumps({"naming": "hard", "symptom_mask": "easy"})),
    ]
    weird_cols = [
        ("Baseline", "hidden depth E · surface E", json.dumps({"hidden_depth": "easy", "surface_deceptiveness": "easy"})),
        ("Hidden depth", "medium · surface E", json.dumps({"hidden_depth": "medium", "surface_deceptiveness": "easy"})),
        ("Hidden depth", "hard · surface E", json.dumps({"hidden_depth": "hard", "surface_deceptiveness": "easy"})),
        ("Surface deceptiveness", "medium · hidden depth E", json.dumps({"hidden_depth": "easy", "surface_deceptiveness": "medium"})),
        ("Surface deceptiveness", "hard · hidden depth E", json.dumps({"hidden_depth": "easy", "surface_deceptiveness": "hard"})),
    ]
    standard_heatmap(
        selected["category_theoretic_compositional"],
        "category_theoretic_compositional", FAMILIES["category_theoretic_compositional"],
        ("naming", "symptom_mask"), category_cols, args.output / "category-heatmap.svg",
    )
    standard_heatmap(
        selected["weird_machine"], "weird_machine", FAMILIES["weird_machine"],
        ("hidden_depth", "surface_deceptiveness"), weird_cols,
        args.output / "weird-machines-heatmap.svg",
    )
    ml_heatmap(selected["ml_debugging"], args.output / "ml-debugging-heatmap.svg")
    epistemic_order = epistemic_heatmap(selected["epistemic_games"], args.output / "epistemic-games-heatmap.svg")

    for key, filename, kind in [
        ("category_theoretic_compositional", "category-radar.svg", "environment"),
        ("weird_machine", "weird-machines-radar.svg", "environment"),
        ("ml_debugging", "ml-debugging-radar.svg", "environment"),
        ("epistemic_games", "epistemic-games-radar.svg", "case"),
    ]:
        entities = family_entities(selected[key], key, epistemic_order if key == "epistemic_games" else None)
        radar_svg(entities, FAMILIES[key], args.output / filename, spoke_kind=kind)

    for path in sorted(args.output.glob("*.svg")):
        print(f"{path.relative_to(ROOT)}\t{path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
