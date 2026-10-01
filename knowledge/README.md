# Knowledge Graph Input (V0)

`knowledge/` is the persistent research-memory boundary for the epistemic compiler. It is now populated from the user-uploaded `epistemic_research_graph(2).html` in the repository. The import is **provenance-preserving but not source-verified**: graph entries, annotations, URLs, relation labels, and uncertainty flags were transcribed from the export; the linked external pages were not fetched or independently checked.

## Imported snapshot

- Repository upload commit: `2e3847aaf7310eb648c5e1edfab2cf02315a8127`
- Git blob SHA: `b84b483b1a21bd0607e0c3521c9cfb92c3f8e4f1`
- HTML SHA-256: `e9f25e257d207cd1998e51eb7403b175706e435fe994375d4e7715fd3c42adf9`
- Imported data: **118 nodes**, **301 directed edges**, **76 external-link records** plus the HTML export source record (**77 source records total**); **21 edges** were marked uncertain in the export.
- The export's `meta.last_verified` value is preserved as source metadata; it is not an independent verification performed during import.

## Files

- `index.yaml` — graph status, paths, import provenance, counts, and original export metadata.
- `nodes.yaml` — all graph nodes with stable source IDs, exported fields, record-level claims, annotations, limitations, and epistemic status.
- `edges.yaml` — directed relations copied from the export, with stable IDs, exact relation labels, original uncertainty flags, and provenance.
- `sources.yaml` — the imported HTML record plus candidate external links. External URLs are leads, not evidence that the destination supports the accompanying graph annotation; Google Scholar query URLs are explicitly marked as search leads.
- `import_manifest.json` — input hash, counts, validation checks, export metadata, and hashes of generated YAML files.

The source-backed assertion “the export contains this entry/annotation/relation” is kept separate from the export's interpretation of an external work. Node annotations are marked `unverified`; unflagged edges are `interpretive`, and edges marked uncertain by the export are `unverified`. Each record retains the import source and an HTML data location. No HTML or JavaScript was executed.

## Re-importing a compatible HTML graph

`scripts/import_mindcluster_html.py` extracts only a JSON object assigned to the literal `const G=`. It validates unique node IDs, unique directed relations, and edge endpoints before writing the graph files. Example for this snapshot:

```bash
python3 scripts/import_mindcluster_html.py \
  --html 'epistemic_research_graph(2).html' \
  --out-dir knowledge \
  --source-url 'https://github.com/StrangeTcy/epistemic-compiler/blob/main/epistemic_research_graph%282%29.html' \
  --raw-url 'https://raw.githubusercontent.com/StrangeTcy/epistemic-compiler/main/epistemic_research_graph%282%29.html' \
  --repository-commit 2e3847aaf7310eb648c5e1edfab2cf02315a8127 \
  --git-blob-sha b84b483b1a21bd0607e0c3521c9cfb92c3f8e4f1 \
  --retrieved-at 2026-10-01T22:38:21+03:00
```

This is a format-specific importer, not a general HTML scraper or truth validator. Review each external item against its linked primary source before promoting its description to an established or source-verified claim.

## Node fields and epistemic status

Each node preserves the export's ID, type, title, author, date, URL, and description. It also carries `source_refs`, `claims`, `limitations`, `concepts`, `relevance`, `epistemic_status`, and `import_provenance`. Every generated record claim cites the HTML import source; an export annotation is labelled `unverified`. External candidate links are kept separately from the HTML source that supports the transcription.

Recommended statuses include `established`, `reported_by_source`, `interpretive`, `hypothesis`, `disputed`, and `unverified`. These labels are not automatic truth judgments.

## Retrieval

Run the deterministic lexical retriever (no embeddings or vector database):

```bash
python3 scripts/retrieve_context.py \
  --seed mission-XX/seed.yaml \
  --hops 2 \
  --roles theorist,experimentalist,skeptic,prior_work_killer \
  --out mission-XX/context
```

It emits `shared.md`, one role-specific pack per requested role, and a `retrieval_manifest.json` with input hashes, selected node/edge IDs, match terms, graph distance, and scores. Each role gets the same retrieved evidence set with different emphasis; no role receives another role's critique. Source URLs and epistemic statuses are retained, candidate verification links are explicitly labelled as unreviewed, and agents are instructed to verify important claims against primary sources. Retrieval is a relevance projection, not an evidence-quality ranking or automatic truth validator.

**Mission 01 status:** This graph was imported only after Mission 01's Council and Gate 4. No Mindcluster context pack informed Mission 01; this data is prospective and must not be retroactively treated as an experimental input.
