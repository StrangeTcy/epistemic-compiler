# Cross-post series review

Review the five individually validated public articles together with their finding/evidence records, actual StrangeTcy style excerpts, and house-style conventions. Do not rewrite any article and do not invent a series-level result. Assess:

- duplicate or repetitive arguments and openings; structural similarity that makes the five posts feel like one template;
- conflicting numbers, denominators, benchmark/task descriptions, judge guarantees, or evidence status across posts;
- conceptual-role overlap: preserve each post's distinct job in the series (non-monotone capability map; Bayesian epistemic game, not recursive ToM; category-track implementation audit; what scalar scores conceal; surface/depth weird machines);
- one-seed scope, dirty-source/comparator uncertainty, judge defects, exclusions, provider failures, and unsupported causal/generalization claims;
- notation, equation/term reuse, public Jekyll conventions, transitions, tone, and StrangeTcy voice calibrated from the actual reference content.

Only request a revision where a concrete issue exists. Do not force structural variety by changing a strong opening, rewrite all five, or reject stylistic experimentation solely because it differs from the source draft. Return exactly one strict JSON object (no prose/fences) in this schema:
{"revisions":[{"post_id":"POST-01","needed":false,"issues":[],"change_request":""},{"post_id":"POST-02","needed":false,"issues":[],"change_request":""},{"post_id":"POST-03","needed":false,"issues":[],"change_request":""},{"post_id":"POST-04","needed":false,"issues":[],"change_request":""},{"post_id":"POST-05","needed":false,"issues":[],"change_request":""}]}
Set `needed` true only for a specific cross-post correction. `change_request` must say what to change and what to preserve; do not write replacement prose.
