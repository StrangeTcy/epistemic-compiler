# Source draft — POST-01: The model's belief is right; its decision is fragile

## Thesis
Mercury-2.5 computes the correct posterior under presentation and intervention variation, but its terminal decisions are fragile to presentation order and proxy channels. Belief computation and decision selection are dissociated.

## Evidence
- T1: 36 matched pairs; 0/36 belief flips; 5/36 terminal flips; 17/36 diagnostic-choice divergences.
- Epistemic games: 23/23 exact posterior match.
- Proxy interventions: visible_proxy 8/27 (0.30); reward_proxy 1/4 (0.25); base 228/331 (0.69).

## Caveats
- Single model; small sample; intervention cases not difficulty-matched; terminal extraction may be brittle.

## Claim markers
- C1: 0/36 belief flips [F-001]
- C2: 5/36 terminal flips [F-001]
- C3: 17/36 diagnostic divergences [F-001]
- C4: 23/23 exact posterior match [F-003]
- C5: proxy pass rates [F-002]
