# Experimentalist (Mercury)

## Design reconstruction
- T1 probe: 6 cells (n_facts 3/4/5 x prior 1/2 or 1/3), 6 seeds each, 36 matched pairs. Two presentation orders (canonical bullet vs reversed numbered). Endpoints: elicited belief, terminal answer, diagnostic choices. Oracle exact.
- Main campaign: 416 cases, 38 environments, 405 scored + 11 unscored. 189 behavioral_reference (gated), 227 compile_only.
- Pair structure: 160 pair_ids (latent_spec basis); 97 multi-member; 76 intervention cases.

## Controlled contrasts
- T1: presentation order is the only manipulated variable; facts and oracle held fixed. Strong control.
- Intervention cases: share latent_spec with base; but difficulty levels often differ, so not fully controlled.
- Provider/model fixed (mercury-2.5, reasoning_effort=high).

## Valid denominators
- T1: 36 pairs (all measured).
- Campaign: 405 scored; report behavioral_reference (189) and compile_only (227) separately; never collapse.
- Proxy rates: 27 visible_proxy, 4 reward_proxy cases.

## Gaps
- 11 unscored; 56 unverified twin cases; config hashes unchecked (no clean source snapshot).
