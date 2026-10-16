# Candidate Writer A draft (Mercury POST-01)

---
title: "The Model's Belief Is Right; Its Decision Is Fragile"
layout: post
...

Mercury-2.5 computes the correct posterior in every tested epistemic-game variant, yet its terminal decisions flip under presentation reordering and proxy channels. This is a dissociation between belief and action.

In a controlled probe of 36 matched pairs (six cells crossing fact count and prior, six seeds each), the model's elicited posterior was identical in both presentation orders in all 36 cases. The terminal answer, however, flipped in 5 of those 36 pairs, and every flip was a correctness flip. Diagnostic choices diverged in 17 of 36.

The same exactness appears in the broader epistemic-game suite: 23 of 23 cases, including evidence, presentation, and prior interventions, produced zero posterior error.

Where the model breaks is not in belief but in action. Intervention cases that introduce a visible proxy channel pass at 0.30 (8 of 27) and a reward proxy at 0.25 (1 of 4), against a 0.69 base pass rate. Within paired groups sharing a latent specification, seven interventions flipped a passing base case to a failure.

The implication: evaluating a model on its stated belief alone overstates its reliability. The decision layer needs its own audit.

Caveats: single model and provider; 36 pairs; intervention cases not difficulty-matched; terminal-answer extraction may be brittle.
