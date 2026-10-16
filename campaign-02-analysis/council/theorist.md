# Theorist (Mercury)

## Strongest explanatory structure
The campaign supports a dissociation: Mercury-2.5's elicited posterior is presentation-invariant and content-sensitive (F-003: 23/23 exact match across epistemic-game variants; T1: 0/36 belief flips), while its terminal answer and diagnostic choices are presentation/proxy-sensitive (F-001: 5/36 terminal flips, 17/36 diagnostic divergences; F-002: proxy interventions cut pass rates to 0.25-0.30).

This is best explained by a two-stage architecture: a belief-computation stage that correctly integrates explicit likelihoods, and a decision/selection stage that is sensitive to surface presentation and proxy channels. The belief stage is robust; the decision stage is not.

## Competing explanations
1. Parsing artifact: presentation changes how facts are parsed, altering the effective likelihood set. Falsified partially by T1: belief (which depends on the same parsed facts) is invariant, so parsing is not the locus.
2. Decision-layer fragility: the model computes the right posterior but selects actions inconsistently. Consistent with evidence.
3. Task-specific shortcut: proxy channels offer a salient but wrong shortcut. Consistent with F-002.

## Discriminating evidence
- T1 belief invariance rules out pure parsing accounts.
- Proxy interventions (visible_proxy, reward_proxy) flip passing cases to FAIL within shared latent specs (7 pass->fail), supporting a shortcut account for F-002.
- Exact posterior match across interventions (F-003) shows belief tracks content.

## Claim ceiling
Observational dissociation on one model/provider/configuration. Not a claim about internal mechanisms or generalization.

## Falsifier
A model variant where terminal answers are presentation-invariant, or a replication showing belief flips under the same manipulation.
