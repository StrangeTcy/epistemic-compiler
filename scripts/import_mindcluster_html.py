#!/usr/bin/env python3
"""Import the JSON graph embedded in a Mindcluster HTML export.

The importer never executes HTML or JavaScript. Imported node annotations and
edges are kept as graph-export reports/interpretations, not independently
verified literature claims. External URLs are recorded as unverified leads.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

REQUIRED_NODE_FIELDS = {"id", "type", "title", "author", "date", "url", "desc"}


def _export_source_id(source_meta: dict[str, str]) -> str:
    """Stable source ID tied to the imported content's Git blob."""
    blob = source_meta.get("git_blob_sha", "unknown")
    return f"src-mindcluster-html-export-{blob[:8]}"


def extract_graph(html_text: str) -> dict[str, Any]:
    """Parse the literal JSON assigned to `const G=` without evaluating JS."""
    marker = "const G="
    if html_text.count(marker) != 1:
        raise ValueError(f"expected exactly one `{marker}` assignment")
    start = html_text.index(marker) + len(marker)
    end = html_text.find(";const ", start)
    if end < 0:
        raise ValueError("could not locate the end of the embedded graph JSON")
    try:
        graph = json.loads(html_text[start:end])
    except json.JSONDecodeError as exc:
        raise ValueError(f"embedded graph is not valid JSON: {exc}") from exc
    validate_graph(graph)
    return graph


def validate_graph(graph: Any) -> None:
    if not isinstance(graph, dict):
        raise ValueError("embedded graph must be a JSON object")
    if not isinstance(graph.get("nodes"), list) or not isinstance(graph.get("edges"), list):
        raise ValueError("embedded graph must contain node and edge lists")
    if not isinstance(graph.get("meta", {}), dict):
        raise ValueError("graph metadata must be an object")

    node_ids: list[str] = []
    for index, node in enumerate(graph["nodes"]):
        if not isinstance(node, dict):
            raise ValueError(f"node {index} must be an object")
        missing = REQUIRED_NODE_FIELDS - node.keys()
        if missing:
            raise ValueError(f"node {index} missing fields: {sorted(missing)}")
        if not all(isinstance(node[field], str) for field in REQUIRED_NODE_FIELDS):
            raise ValueError(f"node {index} fields must be strings")
        node_ids.append(node["id"])
    if len(set(node_ids)) != len(node_ids):
        raise ValueError("graph contains duplicate node IDs")
    known = set(node_ids)

    relation_keys: list[tuple[str, str, str]] = []
    for index, edge in enumerate(graph["edges"]):
        if not isinstance(edge, dict):
            raise ValueError(f"edge {index} must be an object")
        if not all(isinstance(edge.get(key), str) for key in ("source", "target", "type")):
            raise ValueError(f"edge {index} requires string source, target, and type")
        if edge["source"] not in known or edge["target"] not in known:
            raise ValueError(f"edge {index} has an endpoint absent from nodes")
        if "uncertain" in edge and not isinstance(edge["uncertain"], bool):
            raise ValueError(f"edge {index} `uncertain` must be a boolean")
        relation_keys.append((edge["source"], edge["type"], edge["target"]))
    if len(set(relation_keys)) != len(relation_keys):
        raise ValueError("graph contains duplicate directed relations")


def _slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "-", value).strip("-").lower()


def _is_search_url(url: str) -> bool:
    return "scholar.google.com/scholar?" in url.lower()


def _make_sources(
    graph: dict[str, Any], source_meta: dict[str, str], export_source_id: str
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    sources: list[dict[str, Any]] = [{
        "id": export_source_id,
        "source_kind": "user_uploaded_html_graph_export",
        "title": source_meta["title"],
        "url": source_meta["url"],
        "raw_url": source_meta["raw_url"],
        "local_path": source_meta["local_path"],
        "repository_commit": source_meta["repository_commit"],
        "git_blob_sha": source_meta["git_blob_sha"],
        "sha256": source_meta["sha256"],
        "retrieved_at": source_meta["retrieved_at"],
        "verification_status": "integrity_checked_html_export",
        "primary_status": "not_applicable",
        "notes": [
            "The importer extracted the literal JSON assigned to `const G`; no HTML script or external JavaScript was executed.",
            "Integrity metadata identifies the repository file and its content; the export's literature descriptions and links were not independently verified.",
            "The export's own `meta.last_verified` value is preserved in index.yaml but has not been independently audited.",
        ],
    }]
    node_source_ids: dict[str, str] = {}
    for node in graph["nodes"]:
        url = node["url"].strip()
        if not url:
            continue
        sid = f"src-{_slug(node['id'])}"
        node_source_ids[node["id"]] = sid
        is_search = _is_search_url(url)
        source: dict[str, Any] = {
            "id": sid,
            "source_kind": "discovery_search_query" if is_search else "external_source_link_from_export",
            "title": node["title"],
            "source_node_id": node["id"],
            "node_type": node["type"],
            "url": url,
            "author_as_recorded": node["author"],
            "date_as_recorded": node["date"],
            "provenance_source_refs": [export_source_id],
            "verification_status": "search_query_not_verified" if is_search else "link_not_independently_verified",
            "primary_status": "not_assessed",
            "limitations": [
                "Title, author, date, type, description, and URL were transcribed from the uploaded graph export.",
                "The linked page was not retrieved or checked during this import; this record is a lead, not evidence that the page supports the graph annotation.",
            ],
        }
        if node.get("desc"):
            source["description_as_recorded"] = node["desc"]
        sources.append(source)
    return sources, node_source_ids


def build_documents(
    graph: dict[str, Any],
    *,
    source_meta: dict[str, str],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    validate_graph(graph)
    export_source_id = _export_source_id(source_meta)
    sources, node_source_ids = _make_sources(graph, source_meta, export_source_id)
    node_rows: list[dict[str, Any]] = []
    for index, original in enumerate(graph["nodes"]):
        node_id = original["id"]
        source_claim = {
            "id": f"claim-{_slug(node_id)}-export-record",
            "statement": (
                f"The uploaded graph export records node `{node_id}` as type `{original['type']}` "
                f"with title `{original['title']}`. Metadata fields such as author, date, and URL "
                "below are transcribed from that export, not externally verified."
            ),
            "epistemic_status": "reported_by_source",
            "source_refs": [export_source_id],
        }
        claims = [source_claim]
        if original["desc"]:
            annotation_claim: dict[str, Any] = {
                "id": f"claim-{_slug(node_id)}-export-annotation",
                "statement": f"Export annotation (not independently verified): {original['desc']}",
                "epistemic_status": "unverified",
                "source_refs": [export_source_id],
            }
            claims.append(annotation_claim)

        limitations = [
            "This node and its annotation were imported from the HTML graph; external metadata and substantive descriptions were not independently verified.",
        ]
        if original["type"] == "concept":
            limitations.append("Concept/category assignment is the export's synthesis, not a verified bibliographic claim.")
        if original["type"] in {"fiction", "fictional-construct"}:
            limitations.append("Fictional works/constructs are preserved as graph entries and are not evidence of real-world events.")
        if node_id in node_source_ids and _is_search_url(original["url"]):
            limitations.append("The recorded URL is a Google Scholar search query, not a primary-source URL.")

        node_row: dict[str, Any] = {
            "id": node_id,
            "type": original["type"],
            "title": original["title"],
            "author": original["author"],
            "authors": [original["author"]] if original["author"] else [],
            "date": original["date"],
            "url": original["url"],
            "description_from_export": original["desc"],
            "summary": original["desc"],
            "source_refs": [export_source_id],
            "claims": claims,
            "limitations": limitations,
            "concepts": [],
            "relevance": [],
            "keywords": [original["type"], original["author"]] if original["author"] else [original["type"]],
            "epistemic_status": "interpretive" if original["type"] == "concept" else "reported_by_source",
            "import_provenance": f"epistemic_research_graph(2).html:const G.nodes[{index}]",
        }
        if node_id in node_source_ids:
            node_row["candidate_source_refs"] = [node_source_ids[node_id]]
        node_rows.append(node_row)

    edge_rows: list[dict[str, Any]] = []
    uncertain_count = 0
    for index, original in enumerate(graph["edges"]):
        uncertain = bool(original.get("uncertain", False))
        uncertain_count += int(uncertain)
        edge_rows.append({
            "id": f"mindcluster-edge-{index + 1:03d}",
            "source": original["source"],
            "target": original["target"],
            "relation": original["type"],
            "source_relation": original["type"],
            "uncertain": uncertain,
            "epistemic_status": "unverified" if uncertain else "interpretive",
            "source_refs": [export_source_id],
            "import_provenance": f"epistemic_research_graph(2).html:const G.edges[{index}]",
            "limitations": [
                "Directed relation copied from the uploaded graph; it is a graph annotation, not independent evidence for a factual claim."
            ],
        })

    index_doc = {
        "schema_version": 1,
        "knowledge_base_id": "user-mindcluster",
        "status": "populated_from_user_export_unverified",
        "nodes_file": "nodes.yaml",
        "edges_file": "edges.yaml",
        "sources_file": "sources.yaml",
        "import_manifest_file": "import_manifest.json",
        "import": {
            "source_id": export_source_id,
            "retrieved_at": source_meta["retrieved_at"],
            "local_path": source_meta["local_path"],
            "repository_commit": source_meta["repository_commit"],
            "git_blob_sha": source_meta["git_blob_sha"],
            "sha256": source_meta["sha256"],
            "extraction_method": "Parse literal JSON assigned to `const G=`; do not execute HTML/JavaScript.",
            "node_count": len(node_rows),
            "edge_count": len(edge_rows),
            "external_link_count": len(node_source_ids),
            "source_record_count": len(sources),
            "uncertain_edge_count": uncertain_count,
        },
        "export_metadata_as_recorded": graph.get("meta", {}),
        "notes": [
            "The export self-reports its own verification date/criteria; these were not independently audited.",
            "All external source links and graph summaries are unverified until checked against the linked sources.",
            "Edges preserve the uploaded graph's semantic relations and uncertainty flags; edges are not source-backed factual claims.",
            "This import occurred after Mission 01 Gate 4; no Mindcluster context pack informed Mission 01.",
        ],
    }
    nodes_doc = {"nodes": node_rows}
    edges_doc = {"edges": edge_rows}
    sources_doc = {"sources": sources}
    return index_doc, nodes_doc, edges_doc, sources_doc


def write_import(
    html_path: Path,
    out_dir: Path,
    *,
    source_url: str,
    raw_url: str,
    repository_commit: str,
    git_blob_sha: str,
    retrieved_at: str,
) -> dict[str, Any]:
    html_bytes = html_path.read_bytes()
    try:
        html_text = html_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("HTML export must be UTF-8") from exc
    graph = extract_graph(html_text)
    digest = hashlib.sha256(html_bytes).hexdigest()
    actual_git_blob_sha = hashlib.sha1(b"blob " + str(len(html_bytes)).encode() + b"\0" + html_bytes).hexdigest()
    if git_blob_sha != actual_git_blob_sha:
        raise ValueError(f"Git blob SHA mismatch: expected {git_blob_sha}, computed {actual_git_blob_sha}")
    title_match = re.search(r"<title>(.*?)</title>", html_text, flags=re.IGNORECASE | re.DOTALL)
    source_title = " ".join(title_match.group(1).split()) if title_match else html_path.name
    source_meta = {
        "title": source_title,
        "url": source_url,
        "raw_url": raw_url,
        "local_path": str(html_path),
        "repository_commit": repository_commit,
        "git_blob_sha": git_blob_sha,
        "sha256": digest,
        "retrieved_at": retrieved_at,
    }
    index_doc, nodes_doc, edges_doc, sources_doc = build_documents(graph, source_meta=source_meta)
    out_dir.mkdir(parents=True, exist_ok=True)
    documents = {
        "index.yaml": index_doc,
        "nodes.yaml": nodes_doc,
        "edges.yaml": edges_doc,
        "sources.yaml": sources_doc,
    }
    for filename, document in documents.items():
        (out_dir / filename).write_text(
            yaml.safe_dump(document, sort_keys=False, allow_unicode=True, width=110),
            encoding="utf-8",
        )

    node_ids = {node["id"] for node in graph["nodes"]}
    relation_types = Counter(edge["type"] for edge in graph["edges"])
    uncertain_count = sum(bool(edge.get("uncertain", False)) for edge in graph["edges"])
    manifest = {
        "manifest_version": 1,
        "knowledge_base_id": index_doc["knowledge_base_id"],
        "input": source_meta,
        "export_metadata_as_recorded": graph.get("meta", {}),
        "counts": {
            "nodes": len(graph["nodes"]),
            "edges": len(graph["edges"]),
            "source_records_including_html_export": len(sources_doc["sources"]),
            "external_link_records": len(sources_doc["sources"]) - 1,
            "uncertain_edges": uncertain_count,
            "node_types": dict(sorted(Counter(node["type"] for node in graph["nodes"]).items())),
            "edge_relations": dict(sorted(relation_types.items())),
        },
        "validation": {
            "node_ids_unique": len(node_ids) == len(graph["nodes"]),
            "edge_endpoints_resolve": all(edge["source"] in node_ids and edge["target"] in node_ids for edge in graph["edges"]),
            "directed_relations_unique": len({(e["source"], e["type"], e["target"]) for e in graph["edges"]}) == len(graph["edges"]),
            "html_or_javascript_executed": False,
            "external_urls_fetched": False,
        },
        "generated_file_sha256": {
            name: hashlib.sha256((out_dir / name).read_bytes()).hexdigest()
            for name in documents
        },
    }
    (out_dir / "import_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", type=Path, required=True, help="HTML graph export to import")
    parser.add_argument("--out-dir", type=Path, default=Path("knowledge"))
    parser.add_argument("--source-url", required=True, help="Repository/browser URL for the imported file")
    parser.add_argument("--raw-url", required=True, help="Raw content URL for the imported file")
    parser.add_argument("--repository-commit", required=True, help="Commit containing the uploaded HTML")
    parser.add_argument("--git-blob-sha", required=True, help="Git blob SHA of the uploaded HTML")
    parser.add_argument("--retrieved-at", required=True, help="Import timestamp with timezone")
    args = parser.parse_args()
    manifest = write_import(
        args.html,
        args.out_dir,
        source_url=args.source_url,
        raw_url=args.raw_url,
        repository_commit=args.repository_commit,
        git_blob_sha=args.git_blob_sha,
        retrieved_at=args.retrieved_at,
    )
    print(json.dumps(manifest["counts"], ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
