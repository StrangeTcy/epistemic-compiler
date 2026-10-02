# POST-02 — Seven correct Bayesian answers are not seven recursive strategists

**Dek:** The selected epistemic-games cases were answered perfectly. The task source, however, defines inference over specified behavioral policies—not an engine for recursive strategic reasoning.

**Draft**

A model can calculate what an observation says about two possible worlds without reasoning recursively about what one player believes another player believes. The distinction matters in the `epistemic_games` results from this campaign.

The archived Atria-Dawn-Preview run passes all seven selected `epistemic_games` cases, with score 1.0 in each final result. The judge records the posterior, likelihood-ratio verdict, most-supported world, consistency, and provenance checks; all required checks pass. Examples of the exact posterior values in the final results include 1/2, 3/5, 1/15, and 92/177. These are observed task-level outcomes for seven selected seed-0 instances—not an estimate across models, seeds, or a broad theory-of-mind population. ⟦POST-02-C01 · F-07⟧

The source code defines two hypotheses, priors over those worlds, an observed announcement, and a likelihood table for each stipulated behavior policy. The posterior is computed as:

> P(W1 | o) = P(o | W1) P(W1) / [P(o | W1) P(W1) + P(o | W2) P(W2)]

The judge checks whether the submitted answer matches the resulting posterior and whether the accompanying verdict and most-supported-world label are internally consistent. That is a well-specified Bayesian calculation, and the archived answers are correct on the selected cases. ⟦POST-02-C02 · F-07⟧

But the task’s “genuine” and “strategic” labels should not be mistaken for a demonstrated recursive policy solver. The inspected `core.py` says explicitly that v0 does not implement a fully recursive level-k engine with utilities and recursive belief updates. It supplies the likelihoods directly through an evidence table. Its own design description characterizes the target as “Bayesian inference over two specified behavioral policies, presented through genuine-versus-strategic narratives.” The story motivates the inference problem; it does not make the likelihood table a product of the model’s recursive strategic reasoning. These implementation statements follow the inspected clean source comparator; the campaign records `repository.dirty=true`, so exact paid-run source identity remains unresolved. ⟦POST-02-C03 · F-01/F-07⟧

That boundary is especially important in the paired-world cases. In the ambiguous-evidence condition, both worlds can produce the observation with equal likelihood. The correct conclusion is non-identifiability, not confidence in whichever narrative sounds more plausible. The selected balanced-prior cases return 1/2; the skewed-prior case returns 3/5. For the strong and weak evidence cases, the judge separately checks the posterior value and whether the evidence belongs in the appropriate likelihood-ratio band. ⟦POST-02-C04 · F-07⟧

The result is therefore meaningful, but bounded: the model produced exact answers on a small, public, deterministic family with a reference behavior table and a public Bayesian oracle self-test. The archive contains no evidence that the model inferred the policy table itself, generated an opponent model, or recursively updated beliefs over multiple strategic agents. Nor does a passing result reveal which internal procedure produced the answer. ⟦POST-02-C05 · F-04/F-07⟧

This is not a claim that epistemic evaluation is unimportant. Prior work already uses dynamic epistemic logic to isolate controlled theory-of-mind problems in MindGames, targets higher-order recursive beliefs and deception in Hi-ToM, and uses causal templates to generate social-reasoning evaluations in BigToM. Those are distinct tasks and methods; their relevance here is that a seven-item Bayesian-calculation result should not be presented as a new recursive ToM benchmark or as evidence that the same construct was measured. ([MindGames](https://aclanthology.org/2023.findings-emnlp.303/); [Hi-ToM](https://aclanthology.org/2023.findings-emnlp.717/); [BigToM](https://proceedings.neurips.cc/paper_files/paper/2023/file/2b9efb085d3829a2aadffab63ba206de-Paper-Datasets_and-Benchmarks.pdf)). ⟦POST-02-C06 · F-17⟧

A stronger follow-up would keep the current Bayesian cases as calibration and add a separately specified recursive task: define base policies, utilities, observer/player alternation, belief-update rules, and how those generate public actions. It should test unseen likelihood tables and multiple seeds, and include counterfactual cases where a narrative cue conflicts with the supplied evidence. The benchmark should then score the final inference separately from evidence that the model reconstructed the policy or recursion. ⟦POST-02-C07 · F-07⟧

For now, the accurate headline is narrower and still positive: **Atria-Dawn-Preview answered all seven selected Bayesian-inference cases correctly under the policies specified by the task implementation.** The result supports competence on those bounded calculations. It does not establish recursive strategic reasoning. ⟦POST-02-C08 · F-07⟧

**Editor’s note:** Evidence tags and source paths are internal provenance markers; see the claim-traceability sheet before removing them.
