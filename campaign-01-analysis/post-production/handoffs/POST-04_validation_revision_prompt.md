# Targeted validator repair — POST-04

The attached local-validator report identifies specific public-copy defects. Repair only those defects while keeping the evidence boundaries intact. The source draft/evidence packet and exact current article are attached. Do not broaden claims, invent facts, change the article merely to imitate the draft, or expose internal trace IDs. Return only the complete corrected Jekyll Markdown article with its frontmatter, include, and site signature. If a reported check appears to be a false positive, make the smallest public-copy adjustment that resolves it without weakening the caveat; the revised response is validated again locally.


POST-04 targeted repair notes from the report and the original final-writer contract:
- The current article is 2,596 words; bring it within the original 1,800–2,500-word target while preserving the argument.
- Remove the public-copy phrase “internal source draft” (and avoid exposing internal artifact labels). The byline/process statement can say it was written in the Arena pipeline from an audited evidence packet and an earlier draft.
- Rephrase “None of that is an independent replication” to avoid the validator's negation false positive, while keeping the clear caveat that editorial/model-role passes were not new experimental runs.
- Remove the unsupported 82% and physical-constraints 0/4 claims. Address the other unmapped numeric claims in the report’s traceability audit; omit any detail or environment-specific rates that are not traceable to this POST-04 packet. Retain supported counts only.
- Include an explicit, bounded statement that this benchmark does not establish a general capability ranking, common difficulty scale, or causal effect. Keep the dirty-source, one-seed, judge-mode, and compile-only caveats adjacent to claims.

# Compiler-supplied inputs
Use the following attached artifacts as source material; do not echo internal paths, hashes, claim IDs, or editorial labels in public prose.
Filtered evidence tables are task-relevant rendered excerpts; source snapshots and full input hashes remain immutable in the compiler.

[[[ BEGIN INPUT 01 — job:post04_post_validator:response | source_sha256=5fd72e145efbecbececa17d3e0a5b75fc291a635866a1891d7349c2452e07a2b | rendered_sha256=5fd72e145efbecbececa17d3e0a5b75fc291a635866a1891d7349c2452e07a2b ]]]
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
    "public copy leaks internal source or result identifier",
    "numeric literals are not present in the source draft/evidence packet: 0%, 82, 82%",
    "quantitative result claim sentence(s) do not map to an internal claim-traceability row; see traceability_audit",
    "article overstates independent replication or independent model execution",
    "required caveat missing: explicitly limit what the benchmark establishes"
  ],
  "evidence_input_sha256": {
    "mission:campaign_provenance": "3d0f3255143366c9a2521ef8d7f1ba6576b0d537169d9fb391a3d6848378e3f9",
    "mission:evidence_analysis_family_summary_POST-04": "adf76efc0842ab0fc123a5ac021c56227588d65938f3bfc15ae5a203a2c7f4b4",
    "mission:evidence_campaign_exclusions_POST-04": "3300ad90064458a38b1166bd9f5b3c840fa690604c2219cbc3129a3207b92542",
    "mission:evidence_campaign_scope_POST-04": "acacd9f7891af79958df9f66838bdafa4a237021826784d195a3b1eae5c9208e",
    "mission:evidence_case_results_POST-04": "6fac93cfe36d331f85bf454908d40989f5337e68546354023267f9742a986e09",
    "mission:evidence_environment_summary_POST-04": "3de3177a6dbdd61e74b3532f14157efc865b517aa3f4f9c6023e721d22e6d806",
    "mission:evidence_extract_POST-04": "d6a8a332ff5173f4b42371b0e06ae4668d31d7733003cf8ec2a2517269565203",
    "mission:evidence_failure_details_POST-04": "ddfbf8f204f2f1935b4166d4fee88ec7e5988fdabd191c09c9fc0c7f2268ba84",
    "mission:evidence_failure_taxonomy_POST-04": "49155e9c8f1d8bfbdccb50f44c8b2a55c22e0866bb86c8d0b2ce8022d0669ca4",
    "mission:house_style": "590b57b503361c4a535a2566626c06a019bd3c19c52f52f48a82e64f75569973",
    "mission:limitations_POST-04": "e83695e956d4dcb47177cde0ec505b963650898e34ed5d20e47f148f734f629e",
    "mission:references": "54a35af7db803d8c0af0e1098a761e0ffc99eacc1a717127c532419bde6c0cc0",
    "mission:relevant_findings_POST-04": "dd0c94b3d256a124cfdf5eb45f8c7dc4fa51ebc9a633936b970cb1b7d6f38f12",
    "mission:source_audit_POST-04": "2c17ea0fb622c866b5d11582080817041bc7abb59b098333b2c78c465d878b72",
    "mission:source_draft_POST-04": "1ae2208ea2af67f284e042f7522f7340ba6a100611c4369ca908c4d495000b38",
    "mission:style_reference_material": "bd5b755d0b5f308d07c2ae525937b5b7219b18f4be3d093a44df4fda78f5d3f4",
    "mission:trace_rows_POST-04": "c64b4bd39323d9ed8d26f176dda07eba0c929ef59bc1822a7c5bc8067ce97362",
    "mission:workflow_input_manifest": "15409d70ae25020b8327d9f102956b7cb288b470e594682095655eb7ca05a158"
  },
  "numeric_literals_checked": [
    "0",
    "0%",
    "0.95",
    "1",
    "1.0",
    "10",
    "11",
    "120",
    "122",
    "131",
    "15",
    "16",
    "17",
    "192",
    "193",
    "194",
    "2",
    "20",
    "21",
    "24",
    "268",
    "2710",
    "3",
    "30",
    "31",
    "32",
    "325785",
    "33",
    "34",
    "37",
    "3869",
    "4",
    "45",
    "47",
    "5",
    "56",
    "61",
    "62",
    "63",
    "6412",
    "66",
    "7",
    "7.8",
    "7.8%",
    "72",
    "75",
    "8",
    "82",
    "82%",
    "9"
  ],
  "post_id": "POST-04",
  "schema_version": 1,
  "slug": "one-pass-rate-six-stopping-points",
  "spelled_quantitative_counts_checked": [
    "1",
    "16",
    "2",
    "20",
    "3",
    "4",
    "7"
  ],
  "suggested_jekyll_filename": "2026-10-03-one-pass-rate-six-stopping-points.md",
  "title": "One Pass Rate, Six Stopping Points",
  "trace_row_ids_loaded": [
    "POST-04-C01",
    "POST-04-C02",
    "POST-04-C03",
    "POST-04-C04",
    "POST-04-C05",
    "POST-04-C06",
    "POST-04-C07",
    "POST-04-C08",
    "POST-04-C09"
  ],
  "traceability_audit": {
    "mapped_numeric_claim_sentences": [
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "What this post adds is one row-level attribution exercise on one frozen campaign archive, with the places where the archive disagrees with itself left visible."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "2"
        ],
        "sentence": "The work is reconciling a result checkpoint, per-row terminal notes, two judge-mode labels, a campaign report, a clean source comparator, and telemetry counters that do not agree."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "2"
        ],
        "sentence": "Two rows in this archive carry the label  ."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "1.0"
            ]
          }
        ],
        "numbers": [
          "1.0"
        ],
        "sentence": "Both rows also record a trusted score of 1.0."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "Three fields on one row, pointing three ways."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "131",
              "194",
              "63"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "131",
              "194",
              "63"
            ]
          }
        ],
        "numbers": [
          "131",
          "194",
          "63"
        ],
        "sentence": "The result checkpoint holds **194 scored cases: 131 PASS and 63 FAIL**."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "17",
              "24",
              "7"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "24"
            ]
          }
        ],
        "numbers": [
          "17",
          "24",
          "7"
        ],
        "sentence": "Alongside it the campaign records **24 omissions**: 17   cases dropped because the provider did not support their input modality, and 7 cases blocked before any provider call by known calibration failures."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "24"
            ]
          }
        ],
        "numbers": [
          "24"
        ],
        "sentence": "None of the 24 has a model score."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "131",
              "194",
              "63"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "131",
              "194",
              "63"
            ]
          }
        ],
        "numbers": [
          "131",
          "194",
          "63"
        ],
        "sentence": "| Raw checkpoint | nothing | 131 / 63 of 194 | every selected scored row, provider-terminal rows included |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "131",
              "193",
              "62"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "131",
              "193",
              "62"
            ]
          }
        ],
        "numbers": [
          "131",
          "193",
          "62"
        ],
        "sentence": "| Report-consistent set | the one outage the report counter names | 131 / 62 of 193 | follows the campaign report's own count |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "131",
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "131",
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "192",
              "61"
            ]
          }
        ],
        "numbers": [
          "131",
          "192",
          "61"
        ],
        "sentence": "| Analysis set | both rows whose final notes blame the provider | 131 / 61 of 192 | follows the row-level terminal notes |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "192"
            ]
          }
        ],
        "numbers": [
          "192"
        ],
        "sentence": "The 192-row set is my explicit exclusion, not a corrected campaign figure."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "192"
            ]
          }
        ],
        "numbers": [
          "192"
        ],
        "sentence": "Everything below uses 192 unless I say otherwise."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "33"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "33"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "33"
            ]
          }
        ],
        "numbers": [
          "33"
        ],
        "sentence": "All 33 selected configuration hashes match a clean source comparator, but matching configs are not byte-level proof that the task, visible-test, judge, and helper code used in the paid run were the clean code."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "192",
              "61"
            ]
          }
        ],
        "numbers": [
          "192",
          "61"
        ],
        "sentence": "My first plan was to compute a model-attributable failure rate: take the 61 failures, remove the obviously infrastructural ones, divide the remainder by 192."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "192",
              "61"
            ]
          }
        ],
        "numbers": [
          "192",
          "61"
        ],
        "sentence": "Here are the 61 failures in the 192-row set, with the judge mode kept visible:"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "9"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "24"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "24"
            ]
          }
        ],
        "numbers": [
          "15",
          "24",
          "9"
        ],
        "sentence": "|   | 24 | 9 / 15 | every final note says the patch file is empty |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "17"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "20",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "20",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "20",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "20",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "20",
              "3"
            ]
          }
        ],
        "numbers": [
          "17",
          "20",
          "3"
        ],
        "sentence": "|   | 20 | 3 / 17 | a judge scored the submission below passing |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "10",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "10",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "10",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "10",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "10",
              "3"
            ]
          }
        ],
        "numbers": [
          "10",
          "3",
          "7"
        ],
        "sentence": "|   | 10 | 3 / 7 | syntax error or disallowed import, before execution |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "3"
            ]
          }
        ],
        "numbers": [
          "0",
          "3"
        ],
        "sentence": "|   | 3 | 0 / 3 | the patch executed and crashed |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "0",
          "2"
        ],
        "sentence": "|   | 2 | 0 / 2 | action rejected as malformed; see the next section |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "1",
              "2"
            ]
          }
        ],
        "numbers": [
          "1",
          "2"
        ],
        "sentence": "|   | 2 | 1 / 1 | label contradicted by score and note; see the next section |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "One   case was rejected for  , one   case for  ."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "2",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "2",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "2",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2",
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "2",
              "3"
            ]
          }
        ],
        "numbers": [
          "2",
          "3"
        ],
        "sentence": "The three   rows are an   case that used a float tensor as a boolean condition and two   cases with no further note."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C02",
            "finding_ids": "F-04",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "16"
            ]
          }
        ],
        "numbers": [
          "16"
        ],
        "sentence": "The behavioral-reference slice has 16 failures."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C02",
            "finding_ids": "F-04",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "16"
            ]
          }
        ],
        "numbers": [
          "16"
        ],
        "sentence": "So in the slice with the stronger guarantee, three of sixteen failures are the kind a behavioral test is designed to catch."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "20"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "20"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "20"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "20"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "20"
            ]
          }
        ],
        "numbers": [
          "20"
        ],
        "sentence": "Seventeen of the twenty   rows are compile-only."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "2"
        ],
        "sentence": "Back to the two rows I opened with."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "1.0"
            ]
          }
        ],
        "numbers": [
          "0.95",
          "1.0"
        ],
        "sentence": "|   | compile-only |   | 0.95 | 1.0 | required companion file missing:   |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "1.0"
            ]
          }
        ],
        "numbers": [
          "0.95",
          "1.0"
        ],
        "sentence": "|   | behavioral-reference |   | 0.95 | 1.0 | required companion file missing:  ; note also mentions   |"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "2"
        ],
        "sentence": "It does establish that these two rows are not straightforward evidence of anything called overfitting."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "2",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "2",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "2",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "2",
              "61"
            ]
          }
        ],
        "numbers": [
          "2",
          "61"
        ],
        "sentence": "That matters because the *other* two   rows, the ones inside the 61, both compile-only, carry no such note."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "2"
        ],
        "sentence": "## Two judges, two promises"
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "192"
            ]
          }
        ],
        "numbers": [
          "192"
        ],
        "sentence": "The 192 rows were not graded under one contract."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C02",
            "finding_ids": "F-04",
            "matched_numbers": [
              "16",
              "56",
              "72"
            ]
          },
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "16",
              "56",
              "72"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "16",
              "56",
              "72"
            ]
          }
        ],
        "numbers": [
          "16",
          "56",
          "72"
        ],
        "sentence": "**72 are  : 56 PASS, 16 FAIL."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "194"
            ]
          },
          {
            "claim_id": "POST-04-C02",
            "finding_ids": "F-04",
            "matched_numbers": [
              "120",
              "122",
              "45",
              "47",
              "75"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "194"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "120",
              "122",
              "45",
              "47",
              "75"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "120",
              "122",
              "45",
              "47",
              "75"
            ]
          }
        ],
        "numbers": [
          "120",
          "122",
          "194",
          "45",
          "47",
          "75"
        ],
        "sentence": "120 are  : 75 PASS, 45 FAIL.** In the raw 194 the compile-only count is 122 at 75/47; both provider-terminal rows were compile-only."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "131",
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "131",
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "192"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "192"
            ]
          }
        ],
        "numbers": [
          "131",
          "192"
        ],
        "sentence": "So 131/192 is not an accuracy."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C02",
            "finding_ids": "F-04",
            "matched_numbers": [
              "56",
              "72"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "56",
              "72"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "56",
              "72"
            ]
          }
        ],
        "numbers": [
          "56",
          "72"
        ],
        "sentence": "If you want a validated behavioral figure from this archive, it is 56 of 72, and even that is one selected seed per cell across a handful of environments, not a population estimate."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "A pass under compile-only scoring is not interchangeable with a pass under a behavioral-reference judge even when both are recorded as 1."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "3"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "3",
              "5"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "3",
              "5"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "3"
            ]
          }
        ],
        "numbers": [
          "3",
          "5"
        ],
        "sentence": "The physical-constraints judge enforces a 5:3 ratio the task never states."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "7.8",
              "7.8%"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "7.8",
              "7.8%"
            ]
          }
        ],
        "numbers": [
          "7.8",
          "7.8%"
        ],
        "sentence": "An [empirical study of SWE-bench] found that, in its studied SWE-bench Verified setting, 7.8% of plausible patches counted correct by benchmark validation failed the full developer-written test suite."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "1"
            ]
          }
        ],
        "numbers": [
          "1"
        ],
        "sentence": "The same thing happens one level up."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "7"
            ]
          }
        ],
        "numbers": [
          "7"
        ],
        "sentence": "All seven   rows are recorded under the   track."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C02",
            "finding_ids": "F-04",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "16",
              "21",
              "37"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "16"
            ]
          }
        ],
        "numbers": [
          "16",
          "21",
          "37"
        ],
        "sentence": "The recorded track total stays as recorded: ** , 37 cases, 16 PASS / 21 FAIL**."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "7"
            ]
          },
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "30",
              "7",
              "9"
            ]
          }
        ],
        "numbers": [
          "30",
          "7",
          "9"
        ],
        "sentence": "As an analysis view, not an edit to the archive, I separate it into the three ML-debugging environments at **9 / 30** and   at **7 / 7**."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "30"
            ]
          }
        ],
        "numbers": [
          "30"
        ],
        "sentence": "Even the 30 are not one thing."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "9"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "8"
            ]
          }
        ],
        "numbers": [
          "0",
          "11",
          "8",
          "9"
        ],
        "sentence": "is 9/11 under behavioral-reference judging,   is 0/8 under behavioral-reference,   is 0/11 under compile-only."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C02",
            "finding_ids": "F-04",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "16",
              "37"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "16"
            ]
          }
        ],
        "numbers": [
          "16",
          "37"
        ],
        "sentence": "The recorded 16/37 blends a perfect inference slice into a debugging slice whose own environments span the whole range under different judges."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C07",
            "finding_ids": "F-13",
            "matched_numbers": [
              "268"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "268"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "268"
            ]
          }
        ],
        "numbers": [
          "268"
        ],
        "sentence": "The archive has 268 run directories, including earlier and superseded attempts."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C07",
            "finding_ids": "F-13",
            "matched_numbers": [
              "3869",
              "6412"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "3869",
              "6412"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "3869",
              "6412"
            ]
          }
        ],
        "numbers": [
          "3869",
          "6412"
        ],
        "sentence": "Retry counts depend on where you look: 3,869 attempts in the selected final manifests, 6,412 in campaign progress, with the API logs and checkpoint rows disagreeing in between."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C07",
            "finding_ids": "F-13",
            "matched_numbers": [
              "2710",
              "325785"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2710",
              "325785"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "2710",
              "325785"
            ]
          }
        ],
        "numbers": [
          "2710",
          "325785"
        ],
        "sentence": "The run configuration says  , while usage logs report 325,785 reasoning tokens and 2,710 response rows containing a   field."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "33"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "2",
              "33"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "2",
              "31",
              "33",
              "8"
            ]
          }
        ],
        "numbers": [
          "2",
          "31",
          "33",
          "8"
        ],
        "sentence": "Outcomes vary sharply by environment, from 2/8 eligible passes in trajectory synthesis to 31/33 in the recurrent-depth family, under judge guarantees that differ case by case and with no common calibration demonstrated across them."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C01",
            "finding_ids": "F-01;F-02;F-03",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "192",
              "61"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "192",
              "61"
            ]
          }
        ],
        "numbers": [
          "192",
          "61"
        ],
        "sentence": "In the 192-row set the 61 failures span at least six recorded stopping points."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C02",
            "finding_ids": "F-04",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C05",
            "finding_ids": "F-05",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "16"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "16"
            ]
          }
        ],
        "numbers": [
          "16"
        ],
        "sentence": "In the behavioral-reference slice, three of sixteen failures are the   kind nearest to a behavioral miss."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "1.0"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "1.0"
            ]
          }
        ],
        "numbers": [
          "1.0"
        ],
        "sentence": "Two \"overfit\" labels describe missing companion files beside a trusted score of 1.0."
      },
      {
        "candidate_trace_rows": [
          {
            "claim_id": "POST-04-C03",
            "finding_ids": "F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C04",
            "finding_ids": "F-03;F-09",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C06",
            "finding_ids": "F-01;F-04;F-09;F-15;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C08",
            "finding_ids": "F-04;F-09;F-13;F-17",
            "matched_numbers": [
              "2"
            ]
          },
          {
            "claim_id": "POST-04-C09",
            "finding_ids": "F-09;F-13;F-16",
            "matched_numbers": [
              "2"
            ]
          }
        ],
        "numbers": [
          "2"
        ],
        "sentence": "Two   rows have notes blaming the provider."
      }
    ],
    "unmapped_numeric_claim_sentences": [
      "Four   cases were rejected for importing  .",
      "Two of the three have specific notes:   outputs of length 66 and 34 where the input had length 32.",
      "It shows that \"the judge said FAIL\" and \"the task was failed\" can come apart in both directions, and that a 0/4 in the physical-constraints environment is a fact about a particular judge as much as about a particular model.",
      "Each of those numbers comes from one selected seed per case, so the contrast between 82% and 0% is an observation about this run, not a stable difference between tasks."
    ]
  },
  "unsupported_numeric_literals": [
    "0%",
    "82",
    "82%"
  ],
  "unsupported_spelled_quantitative_counts": [],
  "valid": false,
  "warnings": [
    "methodological numeric caveat is sourced in the immutable packet but has no post-claim row: Each of those numbers comes from one selected seed per case, so the contrast between 82% and 0% is an observation about this run, not a stable difference between tasks."
  ],
  "word_count": 2596
}
[[[ END INPUT 01 — job:post04_post_validator:response ]]]

[[[ BEGIN INPUT 02 — job:post04_final_writer:response | source_sha256=6517f850bd17fd5b57ea1af560a1476b6c3c7bd564aaa2e45aa64ef578a96a94 | rendered_sha256=6517f850bd17fd5b57ea1af560a1476b6c3c7bd564aaa2e45aa64ef578a96a94 ]]]
---
title: "One Pass Rate, Six Stopping Points"
date: 2026-10-03
layout: post
---

{% include mathjax.html %}

*by <span class="icon-self">StrangeTcy</span>*

<dl class="epistemic-status">
<dt>Original ideas</dt><dd>Low to moderate. Splitting a pass rate by pipeline stage is standard practice. What this post adds is one row-level attribution exercise on one frozen campaign archive, with the places where the archive disagrees with itself left visible.</dd>
<dt>Synthesis</dt><dd>Moderate. The work is reconciling a result checkpoint, per-row terminal notes, two judge-mode labels, a campaign report, a clean source comparator, and telemetry counters that do not agree.</dd>
<dt>Prose</dt><dd>Written by a language model inside the Arena writing pipeline, working from an audited evidence packet and an internal source draft. Two candidate drafts and a critique round were revisions of the same analysis. None of that is an independent replication, and none of it re-ran the model.</dd>
<dt>Certainty</dt><dd>High for the archived counts, labels, and terminal notes. Medium for anything that depends on the source comparator, because the archive records its repository as dirty. Low for any claim about why a given output came out the way it did.</dd>
<dt>Importance</dt><dd>Moderate as a reporting method. Low as a statement about model capability: one model, one provider, one configuration, one selected seed per case.</dd>
</dl>

Two rows in this archive carry the label `overfit_visible_tests`. It is the most interesting failure label in the set: a patch that fits the tests it can see instead of the problem. Both rows also record a trusted score of 1.0. Both terminal notes say the same thing in different words: a required companion file is missing.

So the label says the model gamed the tests. The score says the trusted check passed. The note says a file was not where the judge expected it. Three fields on one row, pointing three ways.

That is not a curiosity. If a single row can carry a label that its own note contradicts, then every aggregate built from those labels inherits the contradiction, and no amount of care at the top of the table repairs it. The only place to fix it is the row. This post reads the rows.

## Who gets a row at all

The result checkpoint holds **194 scored cases: 131 PASS and 63 FAIL**. I am not going to edit that. Alongside it the campaign records **24 omissions**: 17 `rope` cases dropped because the provider did not support their input modality, and 7 cases blocked before any provider call by known calibration failures. None of the 24 has a model score. Charging them to the model as failures would score tasks it never saw; crediting them as passes would be absurd in the other direction. They are outside every denominator below.

Then there is a disagreement inside the scored set. The campaign-level outage counter names one provider failure. But two final result files end with a terminal note attributing the failure to a provider transient after bounded retries. Which count do I believe? The archive does not settle it, so I carry all three:

| View | What is removed | PASS / FAIL | What the view represents |
|---|---|---|---|
| Raw checkpoint | nothing | 131 / 63 of 194 | every selected scored row, provider-terminal rows included |
| Report-consistent set | the one outage the report counter names | 131 / 62 of 193 | follows the campaign report's own count |
| Analysis set | both rows whose final notes blame the provider | 131 / 61 of 192 | follows the row-level terminal notes |

The 192-row set is my explicit exclusion, not a corrected campaign figure. The two excluded rows stay in the raw archive, scored, with their original labels. Everything below uses 192 unless I say otherwise.

One caveat applies to every sentence in this post about what a task asked or a judge checked. The archive records its repository as dirty. All 33 selected configuration hashes match a clean source comparator, but matching configs are not byte-level proof that the task, visible-test, judge, and helper code used in the paid run were the clean code. When I describe a judge, I am describing the comparator.

## Six labels are six places to stop

My first plan was to compute a model-attributable failure rate: take the 61 failures, remove the obviously infrastructural ones, divide the remainder by 192.

The plan was wrong, and the way it was wrong is the point.

Each FAIL row names a stopping point along a path: the provider has to return something; the agent has to emit a well-formed action carrying a non-empty patch; the patch has to parse and clear the source validator's import policy; it has to run; and only then does a judge decide whether it is right. The scoreboard applies a projection $\pi : \textsf{Outcome} \to \{0, 1\}$ that forgets which stage produced the zero. Nothing downstream can recover the stage from the bit. So after I strip out infrastructure, what is left is still not one homogeneous quantity; it is several, with different owners.

Here are the 61 failures in the 192-row set, with the judge mode kept visible:

| Recorded label | Count | Behavioral-reference / compile-only | What the record supports |
|---|---:|---:|---|
| `patch_invalid` | 24 | 9 / 15 | every final note says the patch file is empty |
| `underfit` | 20 | 3 / 17 | a judge scored the submission below passing |
| `source_invalid` | 10 | 3 / 7 | syntax error or disallowed import, before execution |
| `runtime_error` | 3 | 0 / 3 | the patch executed and crashed |
| `invalid_action` | 2 | 0 / 2 | action rejected as malformed; see the next section |
| `overfit_visible_tests` | 2 | 1 / 1 | label contradicted by score and note; see the next section |

Compile-only verdicts are exploratory throughout; the campaign report excludes them from any validated aggregate.

The `source_invalid` notes make the layering concrete. Four `monadic_reward` cases were rejected for importing `ast`. One `compositional_optimizer` case was rejected for `weakref`, one `css_state_machine` case for `re`. Three died on syntax: an unterminated triple-quoted string in `sql_fixed_point` and again in `ts_one_step`, and an unexpected indentation in `rd_adaptive_halting`. One of the ten carries no detail at all. The three `runtime_error` rows are an `rd_adaptive_halting` case that used a float tensor as a boolean condition and two `ts_trajectory` cases with no further note.

These are not the same kind of event. A syntax error is plausibly the model's output being broken, and I will not strengthen that beyond "plausibly." A rejected `import ast` is a collision between the output and a validator policy; whether that is the model's error depends on whether the policy was disclosed to the agent, and the archive does not tell me. An empty patch says nothing reached the validator, and from the label I cannot tell whether the agent emitted nothing or something was lost between the agent and the patch file. All of them score zero.

Now the number that changed my mind about the plan. The behavioral-reference slice has 16 failures. Nine are empty patches. Three are source rejections. One is the mislabeled "overfit" row. **Three are `underfit`**, and those three are the only rows in the slice where an independent behavioral judge ran on a submitted patch and found it short. Two of the three have specific notes: `regex_state_machine` outputs of length 66 and 34 where the input had length 32.

So in the slice with the stronger guarantee, three of sixteen failures are the kind a behavioral test is designed to catch. The other thirteen stopped earlier. I am not saying the model is blameless for those thirteen; an empty patch may well be the agent's doing. I am saying the labels do not let me assign it, so the honest move is to leave the attribution open rather than default it to the model.

One more thing the table hides. Seventeen of the twenty `underfit` rows are compile-only. Under compile-only scoring, "underfit" records a shortfall in a mode the report itself calls exploratory; under behavioral-reference scoring, it records a finding by the judge with the stronger guarantee. Same string, two different epistemic objects. And `failure_mode` generally is a campaign/judge label, not a validated taxonomy of mechanisms. It says where a row stopped, not why.

## When the label and the note disagree

Back to the two rows I opened with.

| Environment | Judge mode | Recorded label | Score | Trusted score | Final note |
|---|---|---|---:|---:|---|
| `batchnorm_ema` | compile-only | `overfit_visible_tests` | 0.95 | 1.0 | required companion file missing: `train.py` |
| `moco` | behavioral-reference | `overfit_visible_tests` | 0.95 | 1.0 | required companion file missing: `moco_model.py`; note also mentions `temperature_cancelled` |

Whatever happened on these rows, the notes describe a packaging or contract failure, not overfitting. The label is the only evidence for overfitting, and the label is contradicted by the rest of its own row. The record does not resolve whether the cause sits in the agent's output packaging, the judge's artifact requirements, or some interaction between them. It does establish that these two rows are not straightforward evidence of anything called overfitting.

The two provider-terminal rows are the mirror case. In the raw archive they carry the label `invalid_action`, and read naively that is two instances of the model emitting malformed output. Their final notes say the terminal failure was a provider transient after bounded retries. I hold both facts: the raw label stays, and the note is why the rows sit outside the analysis denominator. What I will not do is describe them as ordinary model-format failures.

That matters because the *other* two `invalid_action` rows, the ones inside the 61, both compile-only, carry no such note. The same raw string appears in two different evidentiary situations, and only the terminal note distinguishes them. A count of `invalid_action` labels, four in the raw checkpoint, would merge events that the archive itself keeps apart.

## Two judges, two promises

The 192 rows were not graded under one contract. **72 are `behavioral_reference`: 56 PASS, 16 FAIL. 120 are `compile_only`: 75 PASS, 45 FAIL.** In the raw 194 the compile-only count is 122 at 75/47; both provider-terminal rows were compile-only.

So 131/192 is not an accuracy. It is a sum across two guarantees, and the campaign report says one of them is exploratory and excluded from any validated aggregate. If you want a validated behavioral figure from this archive, it is 56 of 72, and even that is one selected seed per cell across a handful of environments, not a population estimate. A pass under compile-only scoring is not interchangeable with a pass under a behavioral-reference judge even when both are recorded as 1.

Why does the guarantee matter this much? Because a test only certifies what it executes, and the comparator gives specific reasons for care even where behavioral judges ran. These are comparator observations; the dirty repository means they describe the clean snapshot, not the paid-run code with certainty. With that said: in the comparator, the compositional-optimizer prompt promises nested associativity across multiple steps, while its judge checks tensor shape and one state-isolation chain. The physical-constraints judge enforces a 5:3 ratio the task never states. The categorical-lens hidden judge checks the laws but does not itself assert the coordinate-zero view, though the visible test does. None of this shows that every task is under-specified. It shows that "the judge said FAIL" and "the task was failed" can come apart in both directions, and that a 0/4 in the physical-constraints environment is a fact about a particular judge as much as about a particular model.

The gap has been measured elsewhere. An [empirical study of SWE-bench](https://dl.acm.org/doi/10.1145/3744916.3764576) found that, in its studied SWE-bench Verified setting, 7.8% of plausible patches counted correct by benchmark validation failed the full developer-written test suite. That is a rate for that setting, not for this campaign. I cite it only because it shows the problem is not hypothetical.

## A track label is a tag too

The same thing happens one level up. All seven `epistemic_games` rows are recorded under the `ml_debugging` track. In the comparator, the task's core is Bayesian inference over stipulated policy tables: the agent is handed the policies and asked to update over them. That is a well-posed inference problem, but it is not ML debugging, and it is not recursive theory of mind either. (It is also the only environment with an environment-level behavioral oracle self-test recorded as executed and passed, which is one more way its guarantee differs from its neighbours'.)

The recorded track total stays as recorded: **`ml_debugging`, 37 cases, 16 PASS / 21 FAIL**. As an analysis view, not an edit to the archive, I separate it into the three ML-debugging environments at **9 / 30** and `epistemic_games` at **7 / 7**.

Even the 30 are not one thing. `moco` is 9/11 under behavioral-reference judging, `glyph` is 0/8 under behavioral-reference, `batchnorm_ema` is 0/11 under compile-only. Each of those numbers comes from one selected seed per case, so the contrast between 82% and 0% is an observation about this run, not a stable difference between tasks. The recorded 16/37 blends a perfect inference slice into a debugging slice whose own environments span the whole range under different judges. It describes none of them.

## Counters that will not reconcile

Underneath the results sits the run telemetry, and it does not agree with itself either. The archive has 268 run directories, including earlier and superseded attempts. Retry counts depend on where you look: 3,869 attempts in the selected final manifests, 6,412 in campaign progress, with the API logs and checkpoint rows disagreeing in between. The run configuration says `reasoning_enabled=false`, while usage logs report 325,785 reasoning tokens and 2,710 response rows containing a `reasoning_content` field.

The tempting inference is obvious: the flag was off, the tokens are there, so the model reasoned anyway. I decline it. A field's presence is not its semantics, the cause of the disagreement is unknown, and no reasoning text is reproduced or examined here. What the archive establishes is a metadata discrepancy, full stop. There is also no spend field anywhere in the export, so the archive cannot support a cost estimate and I will not offer one.

## What a pass rate can still be

I do not think the scalar is useless. I think it has to come last.

A row that can answer "whose zero is it?" carries, at minimum: the raw verdict, any exclusion and its reason, the judge mode, whether a valid action and a non-empty patch existed, the validator outcome, the runtime outcome, and the judge's terminal note, with missing required artifacts recorded separately from behavioral misses. Aggregate within documented judge modes before combining them. [HELM](https://arxiv.org/abs/2211.09110) made the broad case for many scenarios and many metrics over one number; it is precedent, not validation of anything here, and the specific layers have to fit the machine being measured. For an agent that edits files and submits them to a validator, the layers above are where it can stop.

What the archive licenses is a descriptive map. Outcomes vary sharply by environment, from 2/8 eligible passes in trajectory synthesis to 31/33 in the recurrent-depth family, under judge guarantees that differ case by case and with no common calibration demonstrated across them. In the 192-row set the 61 failures span at least six recorded stopping points. In the behavioral-reference slice, three of sixteen failures are the `underfit` kind nearest to a behavioral miss. Two "overfit" labels describe missing companion files beside a trusted score of 1.0. Two `invalid_action` rows have notes blaming the provider. One recorded track bundles an unrelated inference task.

What it does not license is a capability ranking, a common difficulty scale, or a causal claim about any task axis: one selected seed per cell, no replication, a dirty repository, two grading contracts in one table with the compile-only half exploratory throughout. Validator rejections, runtime crashes, harness contract misses, judge-label mismatches, and provider outages are failures of different parts of the apparatus, and the thing people want to measure is only one of those parts.

A pass rate can still go at the bottom of the page. It just has to be computed from rows that still carry their tags. In this archive the tags are where the answer lives, and for most of the zeros the answer is still open.
[[[ END INPUT 02 — job:post04_final_writer:response ]]]

[[[ BEGIN INPUT 03 — job:post04_prepare_post:response | source_sha256=5660bc1bcd44eb95f5f7c39ed22b537d288b9f8790330240a56ff8c241249f31 | rendered_sha256=4742cf0dc42718d8625ad9eda2d193ec5a6822d66e34e2e5ff36d591d1e2e2d5 ]]]
# Compiler evidence packet — POST-04

This packet is an immutable snapshot of the source draft, audited findings, evidence, and style inputs attached to this DAG job.
Do not treat the internal draft as prose to paraphrase. Its embedded evidence IDs are private compiler bookkeeping.

## Original source draft
# POST-04 — One score, six different ways to fail

**Dek:** In this archive, a zero can mean no patch, invalid source, a runtime crash, a failed behavioral test, a malformed action, or a provider outage. Treating all of them as one model failure hides the engineering story.

**Draft**

A campaign summary usually starts with a pass rate. This archive shows why the next question should be: *what exactly happened in each failed case?*

The raw checkpoint records 131 PASS and 63 FAIL across 194 scored cases. It separately lists 24 omissions: 17 unsupported `rope` cases and 7 cases blocked before provider access by calibration problems. Those omissions are not failures. The campaign report names one provider outage, but two final result files contain the terminal note “provider transient failure after bounded retries.” Removing only the report-listed row gives 131/193 PASS; excluding both final provider-coded rows gives 131/192 PASS and 61 eligible FAIL. All three counts matter because the report counter and the row-level terminal notes do not fully agree. Any implementation details below come from the clean source comparator; the campaign records `repository.dirty=true`, so this is not proof of the exact paid-run code. ⟦POST-04-C01 · F-01/F-02/F-03⟧

The 192-case analysis set is itself mixed: 72 cases are labeled `behavioral_reference`, while 120 are `compile_only`. The campaign report says compile-only verdicts are exploratory and excluded from a validated aggregate. That means 131/192 is bookkeeping across two judge modes—not a uniform accuracy estimate or a standalone model score. ⟦POST-04-C02 · F-04⟧

Among the 61 eligible failed cases, the recorded taxonomy contains 24 `patch_invalid`, 20 `underfit`, 10 `source_invalid`, 3 `runtime_error`, 2 `invalid_action`, and 2 `overfit_visible_tests`. Every `patch_invalid` final note says the patch file is empty. The source-invalid cases are syntax or disallowed-import rejections. The runtime errors are execution failures. These are different points in the pipeline, not six interchangeable ways of being conceptually wrong. ⟦POST-04-C03 · F-09⟧

Even a failure label can conceal the wrong event. Two cases are labeled `overfit_visible_tests`, but their final metrics give a trusted score of 1.0 and their notes say a required companion file is missing. The two provider-coded cases are both raw `invalid_action` rows, although the terminal note blames provider transients. Keeping those in the raw result is faithful to the archive; treating them as ordinary invalid model submissions is not. ⟦POST-04-C04 · F-03/F-09⟧

The track summary has a similar problem. All seven `epistemic_games` rows are assigned to `ml_debugging`, despite the inspected task core implementing Bayesian inference over policy tables. The recorded track total is 37 cases with 16 passes; separating the seven epistemic rows leaves 30 ML-debugging cases with 9 passes and 21 failures, and a distinct 7/7 epistemic result. The analysis preserves the original labels and adds a semantic regrouping instead of silently rewriting the archive. ⟦POST-04-C05 · F-05⟧

Prior work on test-based software-agent benchmarks makes the general warning familiar: a passing test suite is only as strong as the tests that ran. A recent SWE-bench study reported that 7.8% of plausible patches in its studied setting passed the benchmark validation while failing the full developer-written test suite. That rate is not an estimate for this campaign; it is context for why local judge contracts and exact artifacts matter. Here, the more direct evidence is already in the ZIP: 122 raw rows are compile-only, two “overfit” labels describe missing files, and several task/judge contracts differ in the inspected comparator. The archive also records `repository.dirty=true`, so comparator mismatches are not proof of the exact paid-run source. ([Study](https://dl.acm.org/doi/10.1145/3744916.3764576)). ⟦POST-04-C06 · F-01/F-04/F-09/F-15/F-17⟧

Telemetry adds another layer. The archive contains 268 run directories, including earlier and superseded attempts, and its retry counts differ by source: selected run manifests, API logs, checkpoint rows, and campaign progress do not reconcile. The run configuration says `reasoning_enabled=false`, while usage logs report 325,785 reasoning tokens and 2,710 response rows with a `reasoning_content` field. Those are metadata discrepancies, not evidence about cognition; no reasoning text is reproduced here. No spend field is present, so the archive cannot support a cost estimate. ⟦POST-04-C07 · F-13⟧

A better campaign dashboard would separate at least four layers: (1) whether the provider returned a usable response, (2) whether the agent emitted a valid action and nonempty patch, (3) whether the patch passed source/runtime checks, and (4) whether it satisfied independent behavioral tests. It would also retain raw verdicts, explicit exclusions, scoring mode, judge notes, and per-case artifacts. This is consistent with broader multi-metric evaluation practice, but the exact layers must fit the code-agent pipeline being measured. ([HELM](https://arxiv.org/abs/2211.09110)). ⟦POST-04-C08 · F-04/F-09/F-13/F-17⟧

The central result is not that scalar scores are useless. It is that a scalar should be the last line of a traceable evidence chain, not the first and only one. In this archive, the most informative questions concern empty patches, validator policy, required files, provider termination, and what each judge actually verifies. ⟦POST-04-C09 · F-09/F-13/F-16⟧

**Editor’s note:** Double-bracket tags are evidence keys. The exact per-case source paths and quantitative result are mapped in `claim_traceability.csv`.

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
POST-04 prior-work references from the source draft; context only, not validation of this campaign.

- You Wang, Michael Pradel, and Zhongxin Liu. “Are ‘Solved Issues’ in SWE-bench Really Solved Correctly? An Empirical Study.” The study reports that 7.8% of plausible patches counted correct by benchmark validation failed the full developer-written test suite in its studied SWE-bench Verified setting. This rate is not an estimate for the Atria campaign. https://dl.acm.org/doi/10.1145/3744916.3764576
- HELM, Liang et al. (TMLR 2023), “Holistic Evaluation of Language Models”: a precedent for broad scenario and metric coverage, not a validation of this campaign. https://arxiv.org/abs/2211.09110

This targeted reference check supports no “first” or exhaustive-novelty claim.

## Claim-to-finding map
post_id,claim_id,finding_ids
POST-04,POST-04-C01,F-01;F-02;F-03
POST-04,POST-04-C02,F-04
POST-04,POST-04-C03,F-09
POST-04,POST-04-C04,F-03;F-09
POST-04,POST-04-C05,F-05
POST-04,POST-04-C06,F-01;F-04;F-09;F-15;F-17
POST-04,POST-04-C07,F-13
POST-04,POST-04-C08,F-04;F-09;F-13;F-17
POST-04,POST-04-C09,F-09;F-13;F-16

## Relevant finding records
{"claim_ids":["POST-04-C01","POST-04-C02","POST-04-C03","POST-04-C04","POST-04-C05","POST-04-C06","POST-04-C07","POST-04-C08","POST-04-C09"],"findings":[{"claim":"The selected archive is a completed paid Atria-Dawn-Preview campaign tied to source commit d7357092493f311f649a0742889b301d796911b5; the archive records the campaign repository as dirty.","confidence":"HIGH for archive identity, config-hash comparison, and recorded dirty flag; MEDIUM for source-snapshot association because the comparator is outside the ZIP.","id":"F-01","limitations":["Config equality is not byte-for-byte proof that all task, visible-test, judge, or helper code used in paid runs matches the clean snapshot.","The config comparison source path is an external /tmp snapshot and is not bundled as source code."],"quantitative_result":"ZIP SHA-256 e69dfc08ae988dada65e1b20a3674a5cb9282b3e98d1cdbdf84d4f15709b55dd; 2,968 members; 33/33 selected config hashes match the clean comparator snapshot.","status":"OBSERVED"},{"claim":"The campaign report records 194 scored selected cases and 24 separate pre-scoring omissions; the case manifest and result checkpoint contain the same 194 case IDs.","confidence":"HIGH.","id":"F-02","limitations":["The 7 gate-blocked and 17 unsupported cases have no model score and must not be counted as failures or passes.","A complete unfiltered planned-design file is not required to reproduce this report-level union."],"quantitative_result":"194/194 selected results have status scored across 33 environments; 17 rope cases are omitted for unsupported provider input modality and 7 cases are omitted before provider access for known calibration failures; 218 case IDs are recorded as scored or explicitly omitted.","status":"OBSERVED"},{"claim":"Two final selected results, not just the one named in the campaign-level outage counter, explicitly attribute their terminal failure to provider transients after bounded retries.","confidence":"HIGH that both final notes exist; MEDIUM that every terminal provider-coded row should be excluded from model-performance analysis, because the official campaign counter tracks only one episode.","id":"F-03","limitations":["The raw row remains scored and its raw failure label is retained; the 192 denominator is an explicit analysis exclusion, not a rewritten campaign report.","API error events also include transient retries that recovered; only final-result terminal notes define these two exclusions."],"quantitative_result":"Raw checkpoint: 131 PASS / 63 FAIL among 194. Removing only report-listed ts_trajectory gives 131/193 PASS and 62 FAIL. Removing both final-note provider cases gives 131/192 PASS and 61 FAIL.","status":"OBSERVED"},{"claim":"The campaign contains two materially different scoring-guarantee groups, and the report excludes compile-only results from a validated aggregate.","confidence":"HIGH for the labels, counts, and report disclaimer.","id":"F-04","limitations":["Only epistemic_games has an environment-level public_bayes_oracle behavioral self-test recorded as executed/passed.","The exact-instance per-case calibration and environment-level oracle preflight are separate mechanisms."],"quantitative_result":"Raw: 72 behavioral_reference rows with 56 PASS/16 FAIL; 122 compile_only rows with 75 PASS/47 FAIL. After excluding both provider-coded terminal rows, compile_only is 120 rows with 75 PASS/45 FAIL; behavioral_reference remains 72 with 56/16.","status":"OBSERVED"},{"claim":"The archive assigns all seven epistemic_games cases to the recorded ml_debugging track, although the inspected task core implements symbolic Bayesian inference.","confidence":"HIGH for recorded label; HIGH that task semantics are symbolic Bayesian inference in the comparator; MEDIUM for whether the recorded grouping was intentionally multi-purpose.","id":"F-05","limitations":["The analysis_family override is an explicit editorial regrouping; the raw track is preserved unchanged.","A dirty source tree limits claims about the exact executed task code."],"quantitative_result":"Recorded track summary: ml_debugging 37 cases, 16 PASS/21 FAIL. Source-semantic regrouping: 30 ML-debugging cases, 9 PASS/21 FAIL; epistemic_games separate at 7/7 PASS.","status":"OBSERVED"},{"claim":"The scalar PASS/FAIL and failure-mode labels conceal materially different terminal events, including empty patches, source-validation failures, runtime failures, malformed actions, provider transients, and missing required companion files.","confidence":"HIGH for terminal notes/metrics and counts; MEDIUM for mapping those terminal labels to latent reasoning failures.","id":"F-09","limitations":["`failure_mode` is a campaign/judge label; it is not a validated taxonomy of cognitive mechanisms.","The `overfit_visible_tests` label does not match the recorded notes in two cases."],"quantitative_result":"Among 192 eligible cases, 61 fails: 24 patch_invalid (all empty patches), 20 underfit, 10 source_invalid, 3 runtime_error, 2 invalid_action, and 2 overfit_visible_tests. The latter two are labeled overfit but have trusted_score=1.0 and missing required-file notes. Two provider-coded final rows are outside this taxonomy denominator.","status":"OBSERVED"},{"claim":"After removing the epistemic_games track-label anomaly, the three selected ML-debugging environments show 9/30 PASS, with highly uneven task outcomes.","confidence":"HIGH for per-environment result counts and notes; MEDIUM for using the three tasks as a coherent ML-debugging construct.","id":"F-12","limitations":["Only three environment families are grouped here; one has compile-only judgments.","One seed and one selected response per case; no general ML-debugging inference."],"quantitative_result":"batchnorm_ema 0/11 (compile_only), glyph 0/8 (behavioral_reference), moco 9/11 (behavioral_reference); the two MoCo/BatchNorm rows labeled overfit_visible_tests have notes about missing required companion files.","status":"OBSERVED"},{"claim":"The archive contains incompatible retry counters and a reasoning-mode metadata discrepancy; usage or retry totals should not be collapsed into a single canonical value.","confidence":"HIGH that the archived counters/fields disagree; LOW about the underlying cause.","id":"F-13","limitations":["No spend/cost field exists in the exported archive.","No reasoning content is copied or interpreted; presence counts are metadata only."],"quantitative_result":"All 268 runs: 4,061 successful responses, 4,023 summed run/turn IDs, 9,447,242 successful-response tokens. `reasoning_enabled=false` coexists with 325,785 reported reasoning tokens and 2,710 rows containing a reasoning_content field. Retry counts range by source/scope from 3,869 selected final-manifest attempts to 6,412 progress-reported attempts.","status":"OBSERVED"},{"claim":"The inspected source comparator contains task/judge mismatches that materially limit interpretation of category-family pass rates.","confidence":"HIGH for line-level source-comparator observations; MEDIUM for executed-run attribution due dirty source.","id":"F-15","limitations":["These audit examples do not prove that every category task is under-specified.","The lens visible test partly anchors the first-coordinate convention even though the hidden judge does not assert it directly."],"quantitative_result":"Compositional optimizer prompt promises nested associativity/multiple steps while judge checks shape and one state-isolation chain; physical constraints judge enforces an unstated 5:3 ratio; categorical-lens hidden judge checks laws but does not itself assert coordinate-zero view, while the visible test does.","status":"OBSERVED"},{"claim":"The most defensible synthesis is a descriptive map of task-specific result and failure patterns, not a scalar measure of general reasoning capability.","confidence":"HIGH as a reporting recommendation; MEDIUM as a theoretical interpretation.","id":"F-16","limitations":["The archive measures one model/provider/configuration, with one seed per selected instance and mixed grading modes.","The same model may have different sampling variance across environments and retries."],"quantitative_result":"Family counts range from 2/8 eligible PASS in trajectory synthesis to 31/33 in recurrent depth, while judge guarantees, task sizes, no-op axes, and failure modes vary; no common score calibration is demonstrated.","status":"INFERRED"},{"claim":"The cited prior work already covers broad multi-scenario/multi-metric evaluation, variable perturbation, controlled epistemic-logic tasks, recursive ToM/deception, causal-template ToM generation, and test-coverage limits in code-agent evaluation.","confidence":"HIGH for the cited paper abstracts/metadata and the narrow precedent summaries; LOW for any exhaustive novelty conclusion.","id":"F-17","limitations":["This is a targeted prior-work check, not a systematic literature review.","External prior-work findings do not directly establish correctness or error in the current archive."],"quantitative_result":"HELM reports 42 scenarios and multiple metrics; VarBench applies dynamic variable perturbation and five seeds for variable-based experiments; MindGames uses dynamic epistemic logic; Hi-ToM studies higher-order recursive beliefs/deception; BigToM uses causal templates; the SWE-bench empirical study reports 7.8% of plausible patches counted correct failing the full developer test suite in its studied setting.","status":"OBSERVED"}],"post_id":"POST-04","schema_version":1,"trace_finding_ids":["F-01","F-02","F-03","F-04","F-05","F-09","F-13","F-15","F-16","F-17"]}

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

## Evidence Case Results Post-04
case_id,environment,track,analysis_family,seed,difficulty_levels,judge_guarantee,status,verdict,score,failure_mode_normalized,final_notes,performance_eligible,exclusion_reason

## Relevant environment totals
environment,recorded_cases,performance_eligible_cases,passes_performance_set,fails_performance_set,pass_rate_performance_set,behavioral_reference_n,behavioral_reference_passes,behavioral_reference_fails,compile_only_n,compile_only_passes,compile_only_fails
architecture_naturality,5,5,5,0,1.0,0,0,0,5,5,0
batchnorm_ema,11,11,0,11,0.0,0,0,0,11,0,11
categorical_lenses,5,5,4,1,0.8,5,4,1,0,0,0
ci_dependency_graph,5,5,5,0,1.0,5,5,0,0,0,0
compositional_optimizer,5,5,3,2,0.6,0,0,0,5,3,2
css_state_machine,5,5,3,2,0.6,5,3,2,0,0,0
epistemic_games,7,7,7,0,1.0,7,7,0,0,0,0
equivariant_diagram,5,5,5,0,1.0,0,0,0,5,5,0
functorial_augmentation,5,5,2,3,0.4,0,0,0,5,2,3
glyph,8,8,0,8,0.0,8,0,8,0,0,0
gnn_message_passing,5,5,0,5,0.0,0,0,0,5,0,5
moco,11,11,9,2,0.8181818181818182,11,9,2,0,0,0
monadic_reward,5,5,1,4,0.2,0,0,0,5,1,4
neuro_symbolic_parser,5,5,4,1,0.8,0,0,0,5,4,1
rd_adaptive_halting,11,11,9,2,0.8181818181818182,0,0,0,11,9,2
rd_gradient_credit,11,11,11,0,1.0,0,0,0,11,11,0
rd_state_carry,11,11,11,0,1.0,11,11,0,0,0,0
regex_state_machine,5,5,3,2,0.6,5,3,2,0,0,0
semiring_unification,5,5,5,0,1.0,0,0,0,5,5,0
sheaf_invariant_gluing,5,5,5,0,1.0,0,0,0,5,5,0
sheaf_physical_constraints,5,4,0,4,0.0,0,0,0,4,0,4
sheaf_schema_sync,5,5,1,4,0.2,0,0,0,5,1,4
spreadsheet_dataflow,5,5,5,0,1.0,5,5,0,0,0,0
sql_fixed_point,5,5,4,1,0.8,5,4,1,0,0,0
ssm_parallel_scan,5,5,5,0,1.0,0,0,0,5,5,0
stochastic_monad,5,5,5,0,1.0,0,0,0,5,5,0
template_interpreter,5,5,5,0,1.0,5,5,0,0,0,0
tensor_functor,5,5,2,3,0.4,0,0,0,5,2,3
tokenizer_adjunction,5,5,5,0,1.0,0,0,0,5,5,0
transformer_ssm_lift,5,5,5,0,1.0,0,0,0,5,5,0
ts_one_step,3,3,0,3,0.0,0,0,0,3,0,3
ts_parse_only,3,3,2,1,0.6666666666666666,0,0,0,3,2,1
ts_trajectory,3,2,0,2,0.0,0,0,0,2,0,2

## Selected failure details
environment,condition,judge,score,failure,detail
batchnorm_ema,optimizer_hint=easy_red_herring=medium_visible_tests=easy_data_complexity=easy_symptom_mask=easy,compile_only,0.95,overfit_visible_tests,required companion file missing: train.py; trusted_score=1.0 despite failed terminal label
categorical_lenses,naming=easy_symptom_mask=hard,behavioral_reference,0.0,source_invalid,
compositional_optimizer,naming=medium_symptom_mask=easy,compile_only,0.0,source_invalid,source validator rejected import weakref
css_state_machine,surface_deceptiveness=easy_hidden_depth=easy,behavioral_reference,0.416667,underfit,
css_state_machine,surface_deceptiveness=easy_hidden_depth=medium,behavioral_reference,0.0,source_invalid,source validator rejected import re
functorial_augmentation,naming=easy_symptom_mask=easy,compile_only,0.416667,underfit,
functorial_augmentation,naming=hard_symptom_mask=easy,compile_only,0.416667,underfit,
functorial_augmentation,naming=medium_symptom_mask=easy,compile_only,0.416667,underfit,
gnn_message_passing,naming=easy_symptom_mask=easy,compile_only,0.416667,underfit,
gnn_message_passing,naming=easy_symptom_mask=hard,compile_only,0.416667,underfit,
gnn_message_passing,naming=easy_symptom_mask=medium,compile_only,0.416667,underfit,
gnn_message_passing,naming=hard_symptom_mask=easy,compile_only,0.416667,underfit,
gnn_message_passing,naming=medium_symptom_mask=easy,compile_only,0.416667,underfit,
moco,naming=easy_distractors=easy_queue_math=easy_temperature=easy_visible_tests=medium_symptom_mask=easy,behavioral_reference,0.95,overfit_visible_tests,required companion file missing: moco_model.py temperature_cancelled; trusted_score=1.0 despite failed terminal label
monadic_reward,naming=easy_symptom_mask=hard,compile_only,0.0,source_invalid,source validator rejected import ast
monadic_reward,naming=easy_symptom_mask=medium,compile_only,0.0,source_invalid,source validator rejected import ast
monadic_reward,naming=hard_symptom_mask=easy,compile_only,0.0,source_invalid,source validator rejected import ast
monadic_reward,naming=medium_symptom_mask=easy,compile_only,0.0,source_invalid,source validator rejected import ast
neuro_symbolic_parser,naming=hard_symptom_mask=easy,compile_only,0.0,underfit,
rd_adaptive_halting,recurrence_depth=easy_clue_clarity=easy_visible_tests=easy_implementation_obfuscation=easy_batching_complexity=easy,compile_only,0.0,source_invalid,source syntax error: unexpected indentation
rd_adaptive_halting,recurrence_depth=easy_clue_clarity=easy_visible_tests=easy_implementation_obfuscation=medium_batching_complexity=easy,compile_only,0.0,RUNTIME_ERROR,runtime error: float tensor used as a boolean condition
regex_state_machine,surface_deceptiveness=hard_hidden_depth=easy,behavioral_reference,0.208333,underfit,"length mismatch: input 32, output 66"
regex_state_machine,surface_deceptiveness=medium_hidden_depth=easy,behavioral_reference,0.208333,underfit,"length mismatch: input 32, output 34"
sheaf_physical_constraints,naming=easy_symptom_mask=hard,compile_only,0.277778,underfit,
sheaf_physical_constraints,naming=medium_symptom_mask=easy,compile_only,0.277778,underfit,
sql_fixed_point,surface_deceptiveness=easy_hidden_depth=medium,behavioral_reference,0.0,source_invalid,source syntax error: unterminated triple-quoted string
tensor_functor,naming=easy_symptom_mask=hard,compile_only,0.0,underfit,
tensor_functor,naming=easy_symptom_mask=medium,compile_only,0.0,underfit,
tensor_functor,naming=medium_symptom_mask=easy,compile_only,0.0,underfit,
ts_one_step,witness_status=broken_representation=flat,compile_only,0.2857142857142857,underfit,
ts_one_step,witness_status=broken_representation=reflective,compile_only,0.0,source_invalid,source syntax error: unterminated triple-quoted string
ts_one_step,witness_status=valid_representation=flat,compile_only,0.7142857142857143,underfit,
ts_parse_only,witness_status=broken_representation=reflective,compile_only,0.5,underfit,
ts_trajectory,witness_status=broken_representation=flat,compile_only,0.0,runtime_error,
ts_trajectory,witness_status=valid_representation=flat,compile_only,0.0,runtime_error,

## Failure taxonomy
failure_mode_normalized,count,share_of_eligible_failures,judge_guarantees
invalid_action,2,0.03278688524590164,"{""compile_only"": 2}"
overfit_visible_tests,2,0.03278688524590164,"{""behavioral_reference"": 1, ""compile_only"": 1}"
patch_invalid,24,0.39344262295081966,"{""behavioral_reference"": 9, ""compile_only"": 15}"
runtime_error,3,0.04918032786885246,"{""compile_only"": 3}"
source_invalid,10,0.16393442622950818,"{""behavioral_reference"": 3, ""compile_only"": 7}"
underfit,20,0.32786885245901637,"{""behavioral_reference"": 3, ""compile_only"": 17}"
[[[ END INPUT 03 — job:post04_prepare_post:response ]]]
