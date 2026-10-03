# Targeted validator repair — POST-02

The attached local-validator report identifies specific public-copy defects. Repair only those defects while keeping the evidence boundaries intact. The source draft/evidence packet and exact current article are attached. Do not broaden claims, invent facts, change the article merely to imitate the draft, or expose internal trace IDs. Return only the complete corrected Jekyll Markdown article with its frontmatter, include, and site signature. If a reported check appears to be a false positive, make the smallest public-copy adjustment that resolves it without weakening the caveat; the revised response is validated again locally.

# Compiler-supplied inputs
Use the following attached artifacts as source material; do not echo internal paths, hashes, claim IDs, or editorial labels in public prose.
Filtered evidence tables are task-relevant rendered excerpts; source snapshots and full input hashes remain immutable in the compiler.

[[[ BEGIN INPUT 01 — job:post02_post_validator:response | source_sha256=c5afe692c8c5bedb0cc25f7a8ce4df14a6c2ab76c7abd0c8f7a3b6b846bbb8a9 | rendered_sha256=c5afe692c8c5bedb0cc25f7a8ce4df14a6c2ab76c7abd0c8f7a3b6b846bbb8a9 ]]]
{
  "checks": {
    "frontmatter": true,
    "html_tag_balance": true,
    "independent_replication_overclaim": true,
    "internal_provenance_leakage": true,
    "jekyll_layout_include_author": true,
    "markdown_fences_and_links": true,
    "numeric_claim_traceability": true,
    "numerical_claim_literals": true,
    "post_specific_overclaim_and_caveats": true
  },
  "date": "2026-10-03",
  "errors": [
    "numeric literals are not present in the source draft/evidence packet: 14, 85",
    "quantitative result claim sentence(s) do not map to an internal claim-traceability row; see traceability_audit",
    "required caveat missing: the paid-run source/comparator identity was unresolved because the repository was dirty"
  ],
  "evidence_input_sha256": {
    "mission:campaign_provenance": "3d0f3255143366c9a2521ef8d7f1ba6576b0d537169d9fb391a3d6848378e3f9",
    "mission:evidence_analysis_family_summary_POST-02": "30c966fff429a3d634ef6eca92b3e167af55ceee459176ffe9b758381d6d86ee",
    "mission:evidence_axis_summary_POST-02": "ef2e3448ac367023c5705cd38bad376f03ee81092ff7abf3c73cafa11e8c2fd3",
    "mission:evidence_case_results_POST-02": "d3f6e76008fdbdf2e85f5959a366aae6a53a7fd8004fd98bab0dcfdd086860d6",
    "mission:evidence_environment_summary_POST-02": "a29d015640d99e171cb2a861df5759b23503073e204bf690d8d72be8dfb7df76",
    "mission:evidence_extract_POST-02": "b276f9e3564eb7cb8e3a016684dffa58763ac6252de85e7840941f553a58a8dc",
    "mission:evidence_failure_taxonomy_POST-02": "49155e9c8f1d8bfbdccb50f44c8b2a55c22e0866bb86c8d0b2ce8022d0669ca4",
    "mission:house_style": "590b57b503361c4a535a2566626c06a019bd3c19c52f52f48a82e64f75569973",
    "mission:limitations_POST-02": "7fcc58d4ce9331cf23a1a2d1f143627110749b0f6dc2245a36a33af51c7f6bd6",
    "mission:references": "54a35af7db803d8c0af0e1098a761e0ffc99eacc1a717127c532419bde6c0cc0",
    "mission:relevant_findings_POST-02": "0cd1bb194592dc77e92fce37bf1730470d98aa2c74618dd7210caebf192b7f1d",
    "mission:source_audit_POST-02": "168935bd41f48a2c281a43aa4c6a5d83ef78e8d89c4e86f1098b264adf691beb",
    "mission:source_draft_POST-02": "eeea2454b3b15e67568a54efc9f1ddd2e3b06e560be15f5fac1a6a78e6903964",
    "mission:style_reference_material": "bd5b755d0b5f308d07c2ae525937b5b7219b18f4be3d093a44df4fda78f5d3f4",
    "mission:trace_rows_POST-02": "40abbbb39f0b435e9e77e79f50202460a7db4834cd887477d7b845a6e84d0ce9",
    "mission:workflow_input_manifest": "15409d70ae25020b8327d9f102956b7cb288b470e594682095655eb7ca05a158"
  },
  "numeric_literals_checked": [
    "0",
    "0.0666667",
    "0.519774",
    "1",
    "1.0",
    "14",
    "2",
    "3",
    "33",
    "85",
    "92"
  ],
  "post_id": "POST-02",
  "schema_version": 1,
  "slug": "a-correct-posterior-is-not-a-model-of-the-speaker",
  "spelled_quantitative_counts_checked": [
    "1",
    "2",
    "5",
    "7"
  ],
  "suggested_jekyll_filename": "2026-10-03-a-correct-posterior-is-not-a-model-of-the-speaker.md",
  "title": "A Correct Posterior Is Not a Model of the Speaker",
  "trace_row_ids_loaded": [
    "POST-02-C01",
    "POST-02-C02",
    "POST-02-C03",
    "POST-02-C04",
    "POST-02-C05",
    "POST-02-C06",
    "POST-02-C07",
    "POST-02-C08"
  ],
  "traceability_audit": {
    "mapped_numeric_claim_sentences": [
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          }
        ],
        "numbers": [
          "7"
        ],
        "sentence": "None for any generalisation past these seven items."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "One answer in the archive gives World 1 a probability of three fifths."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "It names World 1 as the better-supported world."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "1."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "2"
        ],
        "sentence": "2."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "3"
            ]
          }
        ],
        "numbers": [
          "3"
        ],
        "sentence": "3."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "33"
            ]
          }
        ],
        "numbers": [
          "33"
        ],
        "sentence": "All 33 selected configuration hashes match the clean comparator."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1.0"
            ]
          }
        ],
        "numbers": [
          "1.0"
        ],
        "sentence": "Atria-Dawn-Preview passed all seven selected cases with score 1.0."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "The numerator asks how plausible World 1 was to begin with, and how likely World 1 would be to produce this announcement."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "The likelihood ratio is 1 and the observation contributes nothing."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1",
              "2",
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1",
              "2",
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1",
              "2",
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1",
              "2",
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1",
              "2",
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1",
              "2",
              "3"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1",
              "2",
              "3"
            ]
          }
        ],
        "numbers": [
          "1",
          "2",
          "3"
        ],
        "sentence": "With the skewed prior in the selected case, the posterior stays at the prior:  , which is odds of 3 to 2 for World 1."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "World 1 leads, but the announcement did nothing to put it in front."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "| Evidence, prior | Posterior for World 1 | Evidence verdict | More-supported world |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "| Ambiguous, skewed |   | Indistinguishable | World 1 |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "2"
        ],
        "sentence": "| Strong, balanced |   | Distinguishable | World 2 |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "| Weak, balanced |   | Weakly distinguishable | World 1 |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "With a balanced prior, the prior odds are 1."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1",
          "14"
        ],
        "sentence": "- In the strong case,   corresponds to odds of 1 to 14 for World 1."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "2"
        ],
        "sentence": "The observation favours World 2 heavily."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "92"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "92"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "92"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "92"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "92"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "92"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "92"
            ]
          }
        ],
        "numbers": [
          "85",
          "92"
        ],
        "sentence": "- In the weak case,   corresponds to odds of 92 to 85."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "That leans slightly towards World 1."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "2"
        ],
        "sentence": "For these two cases the judge checks the posterior value and, separately, whether the evidence falls in the correct likelihood-ratio band."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "5"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "5"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "5"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "5"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "5"
            ]
          },
          {
            "claim_id": "POST-02-C06",
            "finding_ids": "F-17",
            "matched_numbers": [
              "5"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "5"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "5"
            ]
          }
        ],
        "numbers": [
          "5"
        ],
        "sentence": "It is tempting to read perfect scores across five axes (evidence, framing, presentation, prior and scenario) as showing that framing doesn't matter, that presentation doesn't matter, or that the model resists narrative pull in general."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "Exactly one case uses narrative framing, one uses solo presentation and one uses a skewed prior."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "2"
        ],
        "sentence": "When the narrative case and its bare-table counterpart both pass, all we learn is that neither of those two cells failed."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          }
        ],
        "numbers": [
          "7"
        ],
        "sentence": "These seven cases are also not seven independent draws from \"strategic situations\"."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "7"
            ]
          }
        ],
        "numbers": [
          "7"
        ],
        "sentence": "I mention the split only so that nobody adds these seven passes into a larger fraction where they would sit next to results judged under weaker guarantees."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "Several role-separated writing passes looked at these seven records, but there is still one run per cell."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "World 1 sits at  , and the announcement is indistinguishable between the worlds."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-02-C01",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C02",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C03",
            "finding_ids": "F-01;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C04",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C05",
            "finding_ids": "F-04;F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C07",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          },
          {
            "claim_id": "POST-02-C08",
            "finding_ids": "F-07",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "All of this rests on one run per cell and on source identity that remains unresolved."
      }
    ],
    "unmapped_numeric_claim_sentences": [
      "For example, it gave 0.519774 in the weak case and 0.0666667 in the strong case.",
      "**The evidence licenses this:** on seven selected seed-0 instances, the model returned answers credited as correct for the posterior, the likelihood-ratio verdict and the most-supported world, with consistency and provenance checks passing."
    ]
  },
  "unsupported_numeric_literals": [
    "14",
    "85"
  ],
  "unsupported_spelled_quantitative_counts": [],
  "valid": false,
  "warnings": [
    "methodological numeric caveat is sourced in the immutable packet but has no post-claim row: **The evidence licenses this:** on seven selected seed-0 instances, the model returned answers credited as correct for the posterior, the likelihood-ratio verdict and the most-supported world, with consistency and provenance checks passing."
  ],
  "word_count": 2451
}
[[[ END INPUT 01 — job:post02_post_validator:response ]]]

[[[ BEGIN INPUT 02 — job:post02_final_writer:response | source_sha256=f3a3bf43b2cedf3b667f1368f36d98b0a7d505f3852d55e708785ec150f273bb | rendered_sha256=f3a3bf43b2cedf3b667f1368f36d98b0a7d505f3852d55e708785ec150f273bb ]]]
---
title: "A Correct Posterior Is Not a Model of the Speaker"
date: 2026-10-03
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
  <dt>Original ideas</dt>
  <dd>The argument here is a reading discipline. It separates three questions: what an observation tells you, which world you now favour, and who supplied the speaker's behaviour. The recursive follow-up is a proposal. It has not been run.</dd>
  <dt>Synthesis</dt>
  <dd>Seven selected case records from one archived evaluation campaign, an inspected clean-source comparator for the task, and three prior epistemic-reasoning papers cited only as precedent.</dd>
  <dt>Prose</dt>
  <dd>Language models wrote this through a role-separated Arena process: two separate drafts, an editorial critique, and a final synthesis, all working from a supplied evidence dossier. It is published under the site byline. These writing passes are not replications of the experiment, and none of them executed the model under test.</dd>
  <dt>Certainty</dt>
  <dd>High for the recorded judgments on the seven selected cases. Unresolved for whether the executed task code exactly matches the source I inspected. None for any generalisation past these seven items.</dd>
  <dt>Importance</dt>
  <dd>Moderate. Treating a calculation as a capability costs little to do and a lot to undo.</dd>
</dl>

One answer in the archive gives World 1 a probability of three fifths. It names World 1 as the better-supported world. It also says the observation is *indistinguishable* between the two worlds. The judge credits all three parts.

Is that a contradiction?

No. The observation never moved anything to three fifths. The probability started there.

That small accounting point leads to a bigger one. A model can update correctly on what a speaker said without having worked out *why* the speaker would say it. The task this answer comes from is called epistemic games. Its narratives talk about "genuine" and "strategic" speakers. But in the source I could inspect, the speakers' behaviour is not derived by anyone. It is given in a table.

So I want to keep three questions apart throughout:

1. **Does this observation discriminate between the worlds?**
2. **Which world is more probable after seeing it?**
3. **Who supplied the account of what each world would produce?**

The judge scores answers to the first two. In the inspected implementation, the answer to the third is "the task did". That implementation says explicitly that this version does not implement a fully recursive level-$k$ engine with utilities and recursive belief updates. Its own design description calls the target Bayesian inference over two specified behavioural policies, presented through genuine-versus-strategic narratives.

That description has a caveat attached, and it belongs here rather than in a footnote. I read the clean comparator source, not a certified copy of the code that ran. The paid campaign recorded its repository as dirty. All 33 selected configuration hashes match the clean comparator. Matching configurations are still not byte-for-byte proof that the executed task, judge or helper code was identical. Exactly which source ran is unresolved.

Within those limits the result is clean. Atria-Dawn-Preview passed all seven selected cases with score 1.0. Each final result credits the posterior, the likelihood-ratio verdict and the most-supported world, and records the consistency and provenance checks as passing.

This is a real success, but it is a Bayesian one. It is not evidence of recursive theory of mind.

## Three fields, three questions

The inspected task gives the model two hypotheses, $W_1$ and $W_2$, a prior over them, an observed announcement $o$, and a likelihood for that announcement under each stipulated behavioural policy. The update is ordinary two-hypothesis Bayes:

$$
P(W_1 \mid o) = \frac{P(o \mid W_1)\,P(W_1)}{P(o \mid W_1)\,P(W_1) + P(o \mid W_2)\,P(W_2)}
$$

The numerator asks how plausible World 1 was to begin with, and how likely World 1 would be to produce this announcement. The denominator applies the same question to both worlds, so the result is a proper probability.

The odds form is easier to read, because it separates the two contributions:

$$
\frac{P(W_1 \mid o)}{P(W_2 \mid o)} = \frac{P(W_1)}{P(W_2)} \cdot \frac{P(o \mid W_1)}{P(o \mid W_2)}
$$

The first factor on the right is where you stood before the observation. The second factor is the likelihood ratio: what the observation itself contributes. The task's evidence verdict is about the second factor. The most-supported-world label is about the left-hand side.

Now the three-fifths case makes sense. In the ambiguous-evidence condition, both worlds produce the announcement with equal likelihood. The likelihood ratio is 1 and the observation contributes nothing. With a balanced prior, the posterior stays at $1/2$ and neither world leads. With the skewed prior in the selected case, the posterior stays at the prior: $3/5$, which is odds of 3 to 2 for World 1. World 1 leads, but the announcement did nothing to put it in front.

"More supported" and "indistinguishable" are answers to different questions. Someone who changes the evidence verdict because the posterior isn't one half has merged two outputs that the judge deliberately keeps apart.

## What was answered

Four of the selected cases show the separation. All four use paired presentation, bare-table framing and the "report" scenario. The values are the judge-credited reference answers. They are not new measurements of how any speaker behaves.

| Evidence, prior | Posterior for World 1 | Evidence verdict | More-supported world |
| --- | ---: | --- | --- |
| Ambiguous, balanced | $1/2$ | Indistinguishable | Neither |
| Ambiguous, skewed | $3/5$ | Indistinguishable | World 1 |
| Strong, balanced | $1/15$ | Distinguishable | World 2 |
| Weak, balanced | $92/177$ | Weakly distinguishable | World 1 |

A note on precision. The model reported decimals. For example, it gave 0.519774 in the weak case and 0.0666667 in the strong case. The judge credited those against the exact reference fractions $92/177$ and $1/15$. "Exact" here describes the reference the judge checks against. It does not mean the model printed a fraction.

The strong and weak rows separate *how much* the evidence moves things from *which way* it moves them. With a balanced prior, the prior odds are 1. The posterior odds therefore equal the likelihood ratio, and I can derive them from the credited posteriors:

- In the strong case, $1/15$ corresponds to odds of 1 to 14 for World 1. The observation favours World 2 heavily.
- In the weak case, $92/177$ corresponds to odds of 92 to 85. That leans slightly towards World 1.

Both ratios are derived from the posteriors and priors. They are not a speaker-policy table that anyone inferred. For these two cases the judge checks the posterior value and, separately, whether the evidence falls in the correct likelihood-ratio band. I don't know the band thresholds and won't invent them. I don't need them to see that a near-coin-flip posterior and a "weakly distinguishable" verdict are distinct claims, and that the model got both right.

The other three selected cases are all balanced, ambiguous-evidence variants:

- one with narrative framing instead of a bare table;
- one with solo presentation instead of paired;
- one in the scenario labelled "trap", still with bare-table framing.

All three returned $1/2$, "indistinguishable" and "neither", as the arithmetic requires. I have only the recorded levels and outputs for these cases. I'm not going to describe what the trap scenario's story contained, or what its designers meant it to provoke.

## Where did the likelihoods come from?

This is where the task's boundary sits.

Every row above depends on two numbers: $P(o \mid W_1)$ and $P(o \mid W_2)$. In a recursive strategic setting, those numbers would be the hard part. A speaker who knows a listener is watching chooses what to announce based on what they expect the listener to infer. The listener knows that, and the speaker knows the listener knows. The likelihood of an announcement comes out of that regress, together with whatever utilities drive it.

In the inspected comparator, that regress is not present. An evidence table supplies the likelihoods for two stipulated policies. The genuine-versus-strategic narrative explains *why* a speaker might announce one thing rather than another, but it doesn't generate the table. Bayesian inference is performed on numbers that arrive already computed.

I don't think this is a flaw in the task. Supplying the policies isolates the update, and that is valuable. If an answer is wrong, you can tell whether the posterior, the verdict or the label went wrong. You don't have to wonder whether the model's theory of the speaker simply differed from the evaluator's. The task is well specified and has a unique answer, and the environment carries a public Bayesian-oracle behavioural self-test that was recorded as executed and passed.

The same isolation limits what a pass can mean. Giving a reasoner a likelihood table and checking that it uses the table correctly is a different test from checking whether it could build that table from interacting minds.

It matters which way this limit runs. The archive doesn't show that Atria-Dawn-Preview *cannot* reason recursively. It shows nothing in either direction about that. A passing final answer doesn't reveal the procedure behind it. The model might have done explicit arithmetic, used some other reliable route, or something else. The archive contains no evidence that the model inferred a policy table, built an opponent model or updated beliefs recursively over several strategic agents. The task never asked it to.

The oracle self-test also needs to stay in its own box. It is an environment-level check that the task's reference machinery behaves as intended. It is separate from the per-case calibration and final judgment on each answer. It isn't an eighth model answer, and its existence says nothing about how the model produced its seven.

## Seven green cells are not a robustness curve

It is tempting to read perfect scores across five axes (evidence, framing, presentation, prior and scenario) as showing that framing doesn't matter, that presentation doesn't matter, or that the model resists narrative pull in general. The design can't support any of those conclusions.

There is **one selected seed per case**. There is one model and one configuration. The axis comparisons are sparse substitutions of one factor at a time around a fixed base cell, not an interaction grid. Exactly one case uses narrative framing, one uses solo presentation and one uses a skewed prior. When the narrative case and its bare-table counterpart both pass, all we learn is that neither of those two cells failed. That is not a framing effect of zero, and it is certainly not a robustness estimate over a population of stories.

These seven cases are also not seven independent draws from "strategic situations". They are hand-varied neighbours of each other. Five of the seven share ambiguous evidence, where the correct move is to leave the prior alone.

One more boundary concerns how these cases sit inside the wider campaign. All seven were judged in the behavioural-reference mode, which scores answers against a reference. The campaign also contains compile-only results, which the report treats as exploratory and excludes from any validated behavioural aggregate. None of the seven is compile-only, and none of the campaign's other outcomes says anything about this task. I mention the split only so that nobody adds these seven passes into a larger fraction where they would sit next to results judged under weaker guarantees.

Rereading or redrafting an article about the run doesn't change any of this. Several role-separated writing passes looked at these seven records, but there is still one run per cell. Editorial attention is not replication.

## What a recursive test would have to specify

If someone wants to measure what the task's name suggests, the seven current cases make a good calibration floor. They check that the update itself is sound. A recursive layer above them would be a different and separately specified experiment. I am proposing it here, not reporting it.

At a minimum, it would need:

- **Base policies and utilities**, so that a speaker's choice of announcement follows from what they want rather than from a table.
- **An information structure**: who observes what, in what order, and how player and observer moves alternate.
- **Belief-update rules**, so the regress has a defined depth and a defined fixed point, or at least a defined truncation.
- **A mapping from beliefs to public actions**, so that the likelihood of an announcement is something the model must *derive*.

The model would then predict how each world's speaker acts, turn that into observation likelihoods, and only then compute the posterior.

The scoring has to keep those stages apart. If only the final fraction is judged, an incorrect speaker model could produce a correct posterior through errors that happen to cancel. The policy predictions need a reference check of their own.

The design would also need unseen policy structures and likelihoods rather than public ones, multiple seeds per cell, and perturbations that change one player's information or incentives while holding everything else fixed. A natural stress test would put a narrative cue in tension with the generated evidence. That would be a new condition. I don't claim the current trap case did this.

There is one trap in the design itself. If the evaluator withholds the likelihood table without fully defining how actions are generated, the problem may no longer have a unique posterior. Removing necessary information makes a task underdetermined, which is not the same as making it test a deeper model of another agent.

Other researchers have already made social and epistemic reasoning precise in other ways. [MindGames](https://aclanthology.org/2023.findings-emnlp.303/) uses dynamic epistemic logic to build controlled theory-of-mind problems. [Hi-ToM](https://aclanthology.org/2023.findings-emnlp.717/) targets higher-order recursive beliefs and deception. [BigToM](https://proceedings.neurips.cc/paper_files/paper/2023/file/2b9efb085d3829a2aadffab63ba206de-Paper-Datasets_and-Benchmarks.pdf) uses causal templates to generate social-reasoning evaluations. These target different constructs with different machinery. They don't validate anything in this campaign, and this targeted comparison is not a novelty claim. Their relevance is simple: careful work already exists on the construct that the name "epistemic games" points to. A seven-item supplied-likelihood update should not be presented as a new benchmark of it.

Even the stronger version would measure performance on specified outputs. It would still not reveal the model's private reasoning. It would only place the scored outputs closer to the capability people fuckingly want to talk about.

## What the three-fifths answer licenses

Back to where I started. World 1 sits at $3/5$, and the announcement is indistinguishable between the worlds. Atria-Dawn-Preview got that right. It also got the six other selected behavioural-reference cases right, as recorded.

**The evidence licenses this:** on seven selected seed-0 instances, the model returned answers credited as correct for the posterior, the likelihood-ratio verdict and the most-supported world, with consistency and provenance checks passing. This was Bayesian inference over two behavioural policies stipulated by the task. It includes the cases where the right move is to let an uninformative observation leave the prior where it was. That is a narrow result, and a good one.

**The evidence does not license these claims:**

- that the model can build the policies it was given, or did build them;
- that it models opponents recursively, or has theory of mind in any general sense;
- that framing, presentation or scenario wording has no effect;
- a difficulty scale or a ranking of strategic reasoners;
- any statement about the procedure the model used internally.

All of this rests on one run per cell and on source identity that remains unresolved. The task's name is about games. What the evidence shows is a correctly computed posterior on given inputs.
[[[ END INPUT 02 — job:post02_final_writer:response ]]]

[[[ BEGIN INPUT 03 — job:post02_prepare_post:response | source_sha256=7260ac159609bf6c8cf8469ee1f8199d43590c61da960fae031e9785f478813d | rendered_sha256=4200e56c197412fb6c904b7c7094fc68fb5e0c826a8aa10969f28464e6a86825 ]]]
# Compiler evidence packet — POST-02

This packet is an immutable snapshot of the source draft, audited findings, evidence, and style inputs attached to this DAG job.
Do not treat the internal draft as prose to paraphrase. Its embedded evidence IDs are private compiler bookkeeping.

## Original source draft
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

## Target-site style and Jekyll conventions
Target Jekyll frame: YAML frontmatter with `title`, `date: 2026-10-03`, `layout: post`; when using math, place `{% include mathjax.html %}` immediately after it. Then use the exact byline `*by <span class="icon-self">StrangeTcy</span>*` and the site's `<dl class="epistemic-status">` fields, in order: Original ideas, Synthesis, Prose, Certainty, Importance. Attribute the actual Arena writing process accurately; do not invent outside authors.

Voice: first-person, curious, technically literate, willing to self-correct. Open in prose, not an `Introduction`; use short, specific `##` argumentative turns and airy paragraphs. Questions should move the argument. End by stating what the evidence does and does not license. Links/citations belong where they matter; avoid a generic benchmark-report register. Target 1,800–2,800 words without padding.

## Actual StrangeTcy reference-post excerpts
Short excerpts from actual StrangeTcy/strangetcy.github.io posts at revision bcc89c392920b3be172a27eec10ad205b58d4fa3; style evidence only, not wording to reuse.
### The Diagram Is the Spec — a concrete distinction (2026-09-27)
A unit test says:

> On these inputs, produce these outputs.

A diagram says:

> **These two paths are the same morphism.**

### Knowing What Kind of Problem You Are In — conceptual opening (2026-09-26)
Most benchmarks hand the agent its context for free.

Not deliberately. It is what happens when you collect tasks: each one arrives already classified. *This is a Python bug, fix it. This is a competition problem, solve it. This is a paper, reproduce it.* The agent is rarely asked to determine what sort of situation it has walked into before deciding how to act, because the first line of the prompt has already told it.

### The Next Question Is Part of the Game — question-led opening (2026-09-30)
Suppose I want you to make the wrong decision.

The stupid way is to lie to you; the more interesting way is to make you run the wrong experiment.

I don't need to convince you that the machine is healthy if I can make you spend your diagnostic budget measuring the optimiser while the representation collapses. I don't need to make you believe a particular false proposition if I can determine which source you consult, which hypothesis you test first, or which anomaly you dismiss as irrelevant.

The strategic object is no longer just your current answer -- it's your **next question**.

### Lying With Truth — visible self-correction (2026-10-01)
The first formalisation was wrong.

I modelled a world-model as a graph $G$ & looked for a message $m$ maximising $D\big(G,\mathrm{Update}(G,m)\big)$: the bigger the change, the stronger the attack.

That's backwards.

A short, decisive true observation *should* demolish a bad theory. An excellent reasoner undergoes violent revision on purpose. If a physicist has a beautiful theory and then someone produces a clean experiment that kills it, “the model changed a lot” is not evidence that the experiment was an attack.

## Relevant prior-work references
POST-01 prior-work citations from the source draft; precedent only, not validation of this campaign.

- HELM, Liang et al. (TMLR 2023), “Holistic Evaluation of Language Models”: 42 scenarios and multiple metrics. https://arxiv.org/abs/2211.09110
- VarBench, Qian et al. (Findings of EMNLP 2024), “Robust Language Model Benchmarking Through Dynamic Variable Perturbation”: dynamic variable perturbation; five sampled runs (seeds 40–44) for variable-based experiments. https://aclanthology.org/2024.findings-emnlp.946/

This targeted reference check supports no “first” or exhaustive-novelty claim.

## Claim-to-finding map
post_id,claim_id,finding_ids
POST-02,POST-02-C01,F-07
POST-02,POST-02-C02,F-07
POST-02,POST-02-C03,F-01;F-07
POST-02,POST-02-C04,F-07
POST-02,POST-02-C05,F-04;F-07
POST-02,POST-02-C06,F-17
POST-02,POST-02-C07,F-07
POST-02,POST-02-C08,F-07

## Relevant finding records
{"claim_ids":["POST-02-C01","POST-02-C02","POST-02-C03","POST-02-C04","POST-02-C05","POST-02-C06","POST-02-C07","POST-02-C08"],"findings":[{"claim":"The selected archive is a completed paid Atria-Dawn-Preview campaign tied to source commit d7357092493f311f649a0742889b301d796911b5; the archive records the campaign repository as dirty.","confidence":"HIGH for archive identity, config-hash comparison, and recorded dirty flag; MEDIUM for source-snapshot association because the comparator is outside the ZIP.","id":"F-01","limitations":["Config equality is not byte-for-byte proof that all task, visible-test, judge, or helper code used in paid runs matches the clean snapshot.","The config comparison source path is an external /tmp snapshot and is not bundled as source code."],"quantitative_result":"ZIP SHA-256 e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd; 2,968 members; 33/33 selected config hashes match the clean comparator snapshot.","status":"OBSERVED"},{"claim":"The campaign contains two materially different scoring-guarantee groups, and the report excludes compile-only results from a validated aggregate.","confidence":"HIGH for the labels, counts, and report disclaimer.","id":"F-04","limitations":["Only epistemic_games has an environment-level public_bayes_oracle behavioral self-test recorded as executed/passed.","The exact-instance per-case calibration and environment-level oracle preflight are separate mechanisms."],"quantitative_result":"Raw: 72 behavioral_reference rows with 56 PASS/16 FAIL; 122 compile_only rows with 75 PASS/47 FAIL. After excluding both provider-coded terminal rows, compile_only is 120 rows with 75 PASS/45 FAIL; behavioral_reference remains 72 with 56/16.","status":"OBSERVED"},{"claim":"The archive assigns all seven epistemic_games cases to the recorded ml_debugging track, although the inspected task core implements symbolic Bayesian inference.","confidence":"HIGH for recorded label; HIGH that task semantics are symbolic Bayesian inference in the comparator; MEDIUM for whether the recorded grouping was intentionally multi-purpose.","id":"F-05","limitations":["The analysis_family override is an explicit editorial regrouping; the raw track is preserved unchanged.","A dirty source tree limits claims about the exact executed task code."],"quantitative_result":"Recorded track summary: ml_debugging 37 cases, 16 PASS/21 FAIL. Source-semantic regrouping: 30 ML-debugging cases, 9 PASS/21 FAIL; epistemic_games separate at 7/7 PASS.","status":"OBSERVED"},{"claim":"Atria-Dawn-Preview returned fully correct answers on the seven selected epistemic_games instances, whose source defines Bayesian inference over two specified behavioral policies rather than a recursive level-k process.","confidence":"HIGH for the recorded task-level outcomes and source-described target; MEDIUM for generalization to the executed tree due dirty-source provenance.","id":"F-07","limitations":["Seven instances, one seed, one model/configuration; only one solo presentation and one skewed prior.","The policies and likelihood tables are stipulated and public; there is no recursively generated strategic agent with utilities and alternating beliefs."],"quantitative_result":"7/7 PASS, score 1.0; each final result records exact posterior credit, correct likelihood-ratio verdict, correct most-supported world, provenance_ok=true, and all_correct=true. The selected exact posteriors include 1/2, 3/5, 1/15, and 92/177.","status":"OBSERVED"},{"claim":"The cited prior work already covers broad multi-scenario/multi-metric evaluation, variable perturbation, controlled epistemic-logic tasks, recursive ToM/deception, causal-template ToM generation, and test-coverage limits in code-agent evaluation.","confidence":"HIGH for the cited paper abstracts/metadata and the narrow precedent summaries; LOW for any exhaustive novelty conclusion.","id":"F-17","limitations":["This is a targeted prior-work check, not a systematic literature review.","External prior-work findings do not directly establish correctness or error in the current archive."],"quantitative_result":"HELM reports 42 scenarios and multiple metrics; VarBench applies dynamic variable perturbation and five seeds for variable-based experiments; MindGames uses dynamic epistemic logic; Hi-ToM studies higher-order recursive beliefs/deception; BigToM uses causal templates; the SWE-bench empirical study reports 7.8% of plausible patches counted correct failing the full developer test suite in its studied setting.","status":"OBSERVED"}],"post_id":"POST-02","schema_version":1,"trace_finding_ids":["F-01","F-04","F-07","F-17"]}

## Archive evidence extract
Frozen paid-run archive SHA-256: `e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd`. The archive records a dirty repository; the inspected clean source is a comparator, not proof of exact paid-run source identity. Copied tables are summaries, not substitutes for primary artifacts.

## Evidence limitations
- One selected seed per case; no cell-level replications. Keep 194 raw results, 24 separate omissions, two provider-terminal cases, and the 192-case sensitivity set distinct.
- The eligible set mixes 72 behavioral-reference and 120 compile-only cases; compile-only results are exploratory, not a validated behavioral aggregate.
- The repository was recorded dirty; matching config hashes do not establish exact task/judge identity. Axes are task-specific and sparse; names/hints are bundled, and validator/runtime/judge failures are not behavioral misses.

## Source-comparator audit
## Source identity and comparator
The archive points to commit `d7357092493f311f649a0742889b301d796911b5` and records a dirty repository. All 33 selected config hashes match the clean comparator, but exact paid-run task/judge source identity remains unresolved.

## Sampling design
One selected seed per case across 33 environments; no environment-level replication. Most contrasts are sparse one-factor substitutions, not interaction tests or population estimates.

## Analysis-family totals
analysis_family,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
epistemic_games,7,7,7,0,1.0,7,7,0,0,0,0

## Selected axis results
environment,axis,level,control,recorded,eligible,passes,fails,rate,judge
epistemic_games,evidence,ambiguous,"{""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,strong,"{""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,weak,"{""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,ambiguous,"{""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""trap""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,ambiguous,"{""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""skewed"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,ambiguous,"{""framing"": ""bare_table"", ""presentation"": ""solo"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,evidence,ambiguous,"{""framing"": ""narrative"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""ambiguous"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,narrative,"{""evidence"": ""ambiguous"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""ambiguous"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""trap""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""ambiguous"", ""presentation"": ""paired"", ""prior"": ""skewed"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""ambiguous"", ""presentation"": ""solo"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""strong"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,framing,bare_table,"{""evidence"": ""weak"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,solo,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""prior"": ""balanced"", ""scenario"": ""trap""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""prior"": ""skewed"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""ambiguous"", ""framing"": ""narrative"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""strong"", ""framing"": ""bare_table"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,presentation,paired,"{""evidence"": ""weak"", ""framing"": ""bare_table"", ""prior"": ""balanced"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,skewed,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""scenario"": ""trap""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""solo"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""ambiguous"", ""framing"": ""narrative"", ""presentation"": ""paired"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""strong"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,prior,balanced,"{""evidence"": ""weak"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""scenario"": ""report""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,trap,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""skewed""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""solo"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""ambiguous"", ""framing"": ""narrative"", ""presentation"": ""paired"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""strong"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference
epistemic_games,scenario,report,"{""evidence"": ""weak"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced""}",1,1,1,0,1.0,behavioral_reference

## Evidence Case Results Post-02
case_id,environment,track,analysis_family,seed,difficulty_levels,judge_guarantee,status,verdict,score,failure_mode_normalized,final_notes,performance_eligible,exclusion_reason
epistemic_games__scenario=report_evidence=ambiguous_presentation=paired_prior=balanced_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.5 vs true 1/2 (0.5000); reported verdict='indistinguishable' vs true 'indistinguishable'; reported support='neither' vs true 'neither'; consistent=True; strict=True""]",True,
epistemic_games__scenario=report_evidence=ambiguous_presentation=paired_prior=balanced_framing=narrative__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""ambiguous"", ""framing"": ""narrative"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.5 vs true 1/2 (0.5000); reported verdict='indistinguishable' vs true 'indistinguishable'; reported support='neither' vs true 'neither'; consistent=True; strict=True""]",True,
epistemic_games__scenario=report_evidence=ambiguous_presentation=paired_prior=skewed_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""skewed"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.6 vs true 3/5 (0.6000); reported verdict='indistinguishable' vs true 'indistinguishable'; reported support='world1' vs true 'world1'; consistent=True; strict=True""]",True,
epistemic_games__scenario=report_evidence=ambiguous_presentation=solo_prior=balanced_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""solo"", ""prior"": ""balanced"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.5 vs true 1/2 (0.5000); reported verdict='indistinguishable' vs true 'indistinguishable'; reported support='neither' vs true 'neither'; consistent=True; strict=True""]",True,
epistemic_games__scenario=report_evidence=strong_presentation=paired_prior=balanced_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""strong"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.0666667 vs true 1/15 (0.0667); reported verdict='distinguishable' vs true 'distinguishable'; reported support='world2' vs true 'world2'; consistent=True; strict=True""]",True,
epistemic_games__scenario=report_evidence=weak_presentation=paired_prior=balanced_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""weak"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""report""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.519774 vs true 92/177 (0.5198); reported verdict='weakly_distinguishable' vs true 'weakly_distinguishable'; reported support='world1' vs true 'world1'; consistent=True; strict=True""]",True,
epistemic_games__scenario=trap_evidence=ambiguous_presentation=paired_prior=balanced_framing=bare_table__seed-0,epistemic_games,ml_debugging,epistemic_games,0,"{""evidence"": ""ambiguous"", ""framing"": ""bare_table"", ""presentation"": ""paired"", ""prior"": ""balanced"", ""scenario"": ""trap""}",behavioral_reference,scored,PASS,1.0,pass,"[""reported P(W1)=0.5 vs true 1/2 (0.5000); reported verdict='indistinguishable' vs true 'indistinguishable'; reported support='neither' vs true 'neither'; consistent=True; strict=True""]",True,

## Relevant environment totals
environment,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
epistemic_games,7,7,7,0,1.0,7,7,0,0,0,0

## Failure taxonomy
failure_mode_normalized,count,share_of_eligible_failures,judge_guarantees
invalid_action,2,0.03278688524590164,"{""compile_only"": 2}"
overfit_visible_tests,2,0.03278688524590164,"{""behavioral_reference"": 1, ""compile_only"": 1}"
patch_invalid,24,0.39344262295081966,"{""behavioral_reference"": 9, ""compile_only"": 15}"
runtime_error,3,0.04918032786885246,"{""compile_only"": 3}"
source_invalid,10,0.16393442622950818,"{""behavioral_reference"": 3, ""compile_only"": 7}"
underfit,20,0.32786885245901637,"{""behavioral_reference"": 3, ""compile_only"": 17}"
[[[ END INPUT 03 — job:post02_prepare_post:response ]]]
