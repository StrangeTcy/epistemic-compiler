# POST-01 — The benchmark’s “hard” is not one difficulty scale

**Dek:** A single campaign sweep produced a jagged pattern across task families. That is useful evidence about these cases, but not a universal ranking of reasoning ability.

**Draft**

“Easy, medium, hard” sounds like a staircase. In this campaign archive, it is closer to a set of labels attached to different stairs—and sometimes to a different building entirely.

The raw checkpoint contains 194 selected results: 131 PASS and 63 FAIL. The archive separately lists 24 cases that never became scored model results. Two of the 194 final results carry provider-transient failure notes. For the primary performance analysis, I exclude both while keeping the raw counts visible: 131 PASS and 61 FAIL among 192 eligible cases. This is a descriptive result from one Atria-Dawn-Preview campaign, not a common score for general reasoning. ⟦POST-01-C01 · F-02/F-03⟧

Even that 192-case set combines two different judge guarantees: 72 behavioral-reference cases and 120 compile-only cases after provider exclusions. The campaign report explicitly calls compile-only verdicts exploratory. Any capability map should therefore show task and judge mode—not just color each environment green or red. All source-implementation descriptions below use the clean comparator at the recorded commit; the archive’s `repository.dirty=true` flag means exact paid-run source identity is unresolved. ⟦POST-01-C02 · F-01/F-04⟧

## What changes when “difficulty” changes?

In the regex Rule 110 environment, “hidden depth” means input-string length: 32, 128, or 512 characters. With the surface label held at easy, the selected model run passes all three lengths. At length 32, however, the medium and hard surface labels fail: the output grows to 34 and 66 characters, respectively, instead of preserving length. The archived cases show a sharp contrast, but they do not isolate a general surface effect: in the clean source comparator, those labels also change class names, and the hard prompt includes an extra performance hint. Because the campaign records `repository.dirty=true`, those comparator details do not prove the exact paid-run files. There is one seed-0 run per selected cell. ⟦POST-01-C03 · F-01/F-06/F-10⟧

CSS and SQL make the word “difficulty” even less portable. In the CSS state-machine task, the easy-surface cases over 3, 4, and 5 bits yield a partial score, a source-validation failure caused by a disallowed import, and a pass. At the fixed three-bit input, the surface-label sweep yields a failure followed by two passes. For SQL, the easy-surface cases pass at graph-chain lengths 6 and 25, while the 12-node case fails source validation because of an unterminated string. The 4/5 SQL and 3/5 CSS environment totals hide those different failure layers. ⟦POST-01-C04 · F-06/F-09/F-10⟧

Other task families produce different profiles again. The five selected spreadsheet cases pass at their tested class-name and grid-length levels; the six weird-machine environments together have 25 passes out of 30 eligible cases. In the MoCo debugging task, the visible-test levels produce pass, fail, pass; the middle case has a trusted test score of 1.0 but is marked failed because a required companion file is missing. In adaptive recurrence halting, the easy-depth case is a syntax error, while the medium- and hard-depth cases pass. None of those patterns is a clean measure of one shared latent “difficulty.” ⟦POST-01-C05 · F-06/F-09/F-10/F-11/F-12⟧

## A map, not a leaderboard

A useful map here has at least four layers: what input changed, what the judge actually checked, whether the judge had an instance-specific behavioral reference, and how the submission terminated. It should display the empty-patch, validator, runtime, and behavioral-test outcomes separately. A red cell for an empty file is not the same observation as a wrong algorithm that runs and fails a hidden behavioral test. ⟦POST-01-C06 · F-04/F-09/F-16⟧

The archive’s family totals reinforce that caution. Recurrent-depth has 31 passes in 33 eligible cases, while trajectory/synthesis has 2 in 8. That contrast is a description of these selected tasks, model, prompts, and judges—not evidence that recurrence is intrinsically easier than synthesis. The family labels cover different code tasks, sizes, tests, and score modes, and they are not calibrated to a common construct. ⟦POST-01-C07 · F-04/F-11/F-16⟧

This is not a new evaluation principle. HELM is an established example of broad scenario coverage with multiple metrics, while VarBench dynamically perturbs task variables and repeats variable-based experiments across sampled values. The relevant lesson is modest: a benchmark should expose what each score means and where a manipulation changed the actual task. This campaign’s single-seed contrasts fall short of estimating general intervention effects. ([HELM](https://arxiv.org/abs/2211.09110); [VarBench](https://aclanthology.org/2024.findings-emnlp.946/)). ⟦POST-01-C08 · F-17⟧

So what can the “capability map” say? It can show that, in this archived run, outcomes are heterogeneous and some nominal contrasts are non-monotone. It cannot rank general capabilities, make “hard” comparable across environments, or establish that surface form caused the differences. A repaired follow-up would first verify each rendered axis, then hold names and hints constant, run multiple seeds, and report results by judge guarantee and failure layer. Until then, the map is most useful as a guide to which cases and implementations need inspection—not as a model leaderboard. ⟦POST-01-C09 · F-06/F-14/F-16⟧

**Editor’s note:** Evidence tags and links in double brackets are internal provenance markers; they can be removed from a public-facing copy after the traceability sheet is reviewed.
