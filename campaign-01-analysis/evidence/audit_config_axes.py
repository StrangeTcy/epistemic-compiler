#!/usr/bin/env python3
"""Statically link selected config-axis placeholders to environment templates.

This audits the clean source comparator only. It does not execute a campaign
or prove that dirty campaign files were identical to this snapshot.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

PLACEHOLDER = re.compile(r"%%([A-Z0-9_]+)%%")
AXIS_ID = re.compile(r"^\s{2}-\s+id:\s*['\"]?([^'\"#]+)['\"]?\s*(?:#.*)?$")
TOP_LEVEL = re.compile(r"^[^\s#][^:]*:")


def parse_axes(text: str) -> list[tuple[str, set[str], list[str]]]:
    axes: list[tuple[str, set[str], list[str]]] = []
    in_axes = False
    current_id: str | None = None
    current_lines: list[str] = []
    for line in text.splitlines():
        if TOP_LEVEL.match(line):
            if current_id is not None:
                block = "\n".join(current_lines)
                axes.append((current_id, set(PLACEHOLDER.findall(block)), current_lines))
            current_id = None
            current_lines = []
            in_axes = line.split(":", 1)[0].strip() == "axes"
            continue
        if not in_axes:
            continue
        match = AXIS_ID.match(line)
        if match:
            if current_id is not None:
                block = "\n".join(current_lines)
                axes.append((current_id, set(PLACEHOLDER.findall(block)), current_lines))
            current_id = match.group(1).strip()
            current_lines = [line]
        elif current_id is not None:
            current_lines.append(line)
    if current_id is not None:
        block = "\n".join(current_lines)
        axes.append((current_id, set(PLACEHOLDER.findall(block)), current_lines))
    return axes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, required=True, help="clean rl_eval_generator source snapshot")
    ap.add_argument("--config-list", type=Path, required=True, help="newline-separated selected config paths")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--source-revision", default="d7357092493f311f649a0742889b301d796911b5")
    args = ap.parse_args()

    source = args.source.expanduser().resolve()
    config_paths = [line.strip() for line in args.config_list.read_text().splitlines() if line.strip()]
    rows: list[dict[str, str]] = []
    for config_path in config_paths:
        config_file = source / config_path
        if not config_file.is_file():
            raise FileNotFoundError(config_file)
        env_dir = config_file.parent
        files_dir = env_dir / "files"
        template_files = [p for p in files_dir.rglob("*") if p.is_file()] if files_dir.exists() else []
        corpus = {str(p.relative_to(env_dir)): p.read_text(encoding="utf-8", errors="replace") for p in template_files}
        for axis, variables, axis_lines in parse_axes(config_file.read_text(encoding="utf-8")):
            axis_digest = hashlib.sha256("\\n".join(axis_lines).encode("utf-8")).hexdigest()
            if not variables:
                rows.append({
                    "config_path": config_path,
                    "source_revision": args.source_revision,
                    "axis": axis,
                    "placeholder": "",
                    "template_placeholder_files": [],
                    "literal_key_or_name_files": [],
                    "source_reference_status": "axis has no parsed placeholders; inspect config manually",
                    "axis_block_sha256": axis_digest,
                })
                continue
            for variable in sorted(variables):
                exact_refs = sorted(
                    path for path, content in corpus.items()
                    if f"%%{variable}%%" in content
                )
                literal_refs = sorted(
                    path for path, content in corpus.items()
                    if re.search(rf"\b{re.escape(variable)}\b", content)
                )
                if exact_refs:
                    status = "placeholder referenced in environment file templates"
                elif literal_refs:
                    status = "literal variable name referenced; inspect renderer/runtime use"
                else:
                    status = "no reference in environment file templates"
                rows.append({
                    "config_path": config_path,
                    "source_revision": args.source_revision,
                    "axis": axis,
                    "placeholder": variable,
                    "template_placeholder_files": json.dumps(exact_refs),
                    "literal_key_or_name_files": json.dumps(literal_refs),
                    "source_reference_status": status,
                    "axis_block_sha256": axis_digest,
                })

    args.out.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else []
    with args.out.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} placeholder-reference rows to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
