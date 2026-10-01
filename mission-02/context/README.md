# Mission 02 context

- `digest.md` is the evidence pack the Council is shown, identical for all four roles. It renders the retrieval below (30 nodes) plus 10 nodes added by hand and clearly labelled as such (Part B), and lists the relations among them as labelled by the graph export.
- `retrieval_manifest.json` is the manifest written by `scripts/retrieve_context.py` (retrieval id `2ea40c06945d4cdd`, 2 hops, 30 nodes). It records the hashes of the query file and the graph.
- The query is `../retrieval_seed.yaml`, a short concept-only view of the seed. It is a curated query, not a neutral projection of the seed.

## Not committed

The full provenance packs (`shared.md` and four role packs, about 590 KB, mostly repeated provenance boilerplate). They are deterministic and can be regenerated:

```bash
python3 scripts/retrieve_context.py --seed mission-02/retrieval_seed.yaml \
  --hops 2 --roles theorist,experimentalist,skeptic,prior_work_killer --out mission-02/context
```

## What this use of the retriever showed (not fixed)

- Run on the full seed, the v0 retriever selected 5 of 22 epistemic-game-theory nodes named in the seed and filled most of its 30 slots with generic agent-benchmark nodes. Long prose is scored word by word, so common words outweigh specific vocabulary, and a hyphenated id such as `aumann-1976` cannot match the text "Aumann".
- On the concept-only query it selected 30 relevant nodes but still missed 10 of 24 named cluster nodes. Raising the node cap above about 40 did not help. Author names are not a scored field, so a node titled "Agreeing to Disagree" is invisible to a query that says "Aumann". Those nodes were added by hand (digest Part B).
- The graph itself is thin. Of 118 nodes, 72 carry any description text, 25 concept nodes carry only a placeholder, and of 15 classic epistemic-game-theory papers in the cluster only one (Schelling 1960) has a description. For most of them the graph supplies a title, an author, a year and a link.
