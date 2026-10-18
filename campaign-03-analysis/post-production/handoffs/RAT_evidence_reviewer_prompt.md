# Stage A — Evidence Reviewer prompt (reasoning Atria campaign)

Review the evidence package for the reasoning Atria pairwise campaign. Do not rerun the campaign or call any provider. Work only from the materials below.

Inputs (repository paths):
- `campaign-03-analysis/evidence/PROVENANCE.md`
- `campaign-03-analysis/evidence/generated/headline_counts.csv`
- `campaign-03-analysis/evidence/generated/case_results.csv`
- `campaign-03-analysis/evidence/generated/campaign_exclusions.csv`
- `campaign-03-analysis/posts/POST_PLAN.md`

Task:
1. Verify each headline number in `headline_counts.csv` against `case_results.csv`. Report any mismatch.
2. Assess the open discrepancies in PROVENANCE §6. For each: what the data show, what can and cannot be concluded, and whether it blocks drafting.
3. For each planned post in POST_PLAN.md, state which claims the evidence supports, which it does not, and what additional disclosure is required.
4. State explicitly that the campaign is incomplete (415 of 416) and what that prevents claiming.
5. Do not use numbers from other campaigns (including normal-Atria posts or the Mercury campaign) as evidence about this campaign.

Output: a Markdown brief with sections per item above, ending with a list of blocking items (if any).
