# Campaign 02 — Mercury pairwise-state analysis

## Scope
Retrospective analysis of the completed Mercury campaign archive. No campaign rerun.

## Archive identity
- File: `mercury-pairwise-state-38873207827.zip`
- Git blob SHA-1: `b96d00d3206929da5089ca63b75b667639e87ebc`
- Size: 10,580,748 bytes
- SHA-256: `ece98bcf1cfd53dd24625c43da5e647aa63a5fac645603976c1213bdbd9af389`
- Members: 5,129

## Conclusions
Strongest defensible finding: Mercury-2.5's belief computation is presentation-invariant and content-sensitive, while its terminal decisions are presentation- and proxy-sensitive (dissociation). See findings/findings.json and posts/.

## Limitations
Single model/provider; small T1 sample (36 pairs); intervention cases not difficulty-matched; source repo dirty; 11 unscored; 56 unverified twins.

## Regeneration
Run `python campaign-02-analysis/evidence/reconstruct_campaign.py --archive mercury-pairwise-state-38873207827.zip --out campaign-02-analysis/evidence/generated`.
