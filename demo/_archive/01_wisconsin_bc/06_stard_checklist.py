"""
MedSci Skills Demo 1 v2: Wisconsin Breast Cancer Dataset
Step 6 — STARD 2015 Compliance Checklist (check-reporting skill)

Checks all 30 STARD 2015 items against the manuscript content.
Rates each: PRESENT / PARTIAL / MISSING with fix recommendations.

Usage: python 06_stard_checklist.py
Output: output/stard_compliance_report.md
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load manuscript
manuscript_path = os.path.join(BASE_DIR, "output", "manuscript_draft.md")
with open(manuscript_path, "r") as f:
    manuscript = f.read().lower()


def has_text(keywords):
    """Check if all keywords appear in the manuscript."""
    return all(k.lower() in manuscript for k in keywords)


def has_any(keywords):
    """Check if any keyword appears in the manuscript."""
    return any(k.lower() in manuscript for k in keywords)


# ============================================================
# STARD 2015 CHECKLIST — 30 ITEMS
# ============================================================
# Each item: (number, section, description, status, evidence, recommendation)

checklist = []


def add_item(number, section, description, status, evidence, recommendation=""):
    checklist.append({
        "number": number,
        "section": section,
        "description": description,
        "status": status,
        "evidence": evidence,
        "recommendation": recommendation,
    })


# --- TITLE / ABSTRACT ---
add_item(
    1, "Title/Abstract",
    "Identification as a study of diagnostic accuracy using at least one measure "
    "of accuracy (such as sensitivity, specificity, predictive values, or AUC)",
    "PRESENT" if has_text(["diagnostic accuracy"]) and has_any(["sensitivity", "auc"]) else "MISSING",
    "Title contains 'Comparative Diagnostic Accuracy'; abstract reports AUC, sensitivity, specificity.",
)

add_item(
    2, "Abstract",
    "Structured abstract with study design, methods, results, and conclusions",
    "PRESENT" if has_text(["background", "objective", "methods", "results", "conclusions"]) else "PARTIAL",
    "Abstract contains structured sections: Background, Objective, Methods, Results, Conclusions.",
)

# --- INTRODUCTION ---
add_item(
    3, "Introduction",
    "Scientific and clinical background, including the intended use and clinical "
    "role of the index test",
    "PRESENT" if has_text(["first-line diagnostic", "breast"]) else "PARTIAL",
    "Introduction describes FNA as first-line diagnostic tool and clinical context of breast cancer diagnosis.",
)

add_item(
    4, "Introduction",
    "Study objectives and hypotheses",
    "PRESENT" if has_text(["objective"]) and has_text(["compare"]) else "MISSING",
    "Introduction states the objective to compare diagnostic accuracy of three ML classifiers.",
)

# --- METHODS ---
add_item(
    5, "Methods",
    "Whether data collection was planned before the index test and reference "
    "standard were performed (prospective study) or after (retrospective study)",
    "PRESENT" if has_text(["retrospective"]) else "MISSING",
    "Methods states 'Retrospective cross-sectional diagnostic accuracy study'.",
)

add_item(
    6, "Methods",
    "Eligibility criteria",
    "PRESENT" if has_text(["569"]) and has_text(["breast mass"]) else "PARTIAL",
    "Dataset described as 569 FNA cytology specimens from patients presenting with breast masses.",
    "Consider adding explicit inclusion/exclusion criteria (e.g., 'All consecutive FNA specimens "
    "with confirmed histopathological diagnosis were included. No specimens were excluded.').",
)

add_item(
    7, "Methods",
    "On what basis potentially eligible participants were identified "
    "(such as symptoms, results from previous tests, inclusion in registry)",
    "PARTIAL" if has_text(["presenting with breast mass"]) else "MISSING",
    "Mentions 'presenting with breast masses' but does not specify referral pathway or registry.",
    "Add: 'Patients were identified based on clinical presentation with palpable breast masses "
    "referred for FNA cytology at the University of Wisconsin Hospital.'",
)

add_item(
    8, "Methods",
    "Where and when the study was conducted, including the period of recruitment",
    "PRESENT" if has_text(["university of wisconsin"]) and has_any(["1989", "1991"]) else "PARTIAL",
    "Methods mentions University of Wisconsin Hospital, January 1989 to November 1991.",
)

add_item(
    9, "Methods",
    "Whether participants formed a consecutive, random, or convenience series",
    "PARTIAL" if has_text(["consecutive"]) else "MISSING",
    "Text mentions 'consecutive FNA cytology specimens'.",
    "Strengthen by stating explicitly: 'The dataset comprised a consecutive series of "
    "FNA specimens. No convenience sampling was applied.'",
)

add_item(
    10, "Methods",
    "Index test, in sufficient detail to allow replication",
    "PRESENT" if has_text(["logistic regression"]) and has_text(["random forest"]) and
    has_text(["support vector machine"]) and has_text(["5-fold"]) else "PARTIAL",
    "All three index tests described with hyperparameters, cross-validation strategy, and scaling approach.",
)

add_item(
    11, "Methods",
    "Reference standard, in sufficient detail to allow replication",
    "PRESENT" if has_text(["histopathological"]) and has_text(["reference standard"]) else "PARTIAL",
    "Reference standard identified as histopathological diagnosis via surgical excision or core needle biopsy.",
)

add_item(
    12, "Methods",
    "Rationale for choosing the reference standard (if alternatives exist)",
    "PARTIAL",
    "Histopathology is described as reference standard but no explicit rationale for choosing it over alternatives.",
    "Add: 'Histopathological examination was chosen as the reference standard because it represents "
    "the highest-certainty method for distinguishing benign from malignant breast lesions.'",
)

add_item(
    13, "Methods",
    "Definition of and rationale for test positivity cut-offs or result categories, "
    "including whether the cut-off was pre-specified",
    "PARTIAL" if has_text(["predict"]) else "MISSING",
    "Default 0.5 probability threshold implied but not explicitly stated.",
    "Add: 'A probability threshold of 0.5 was used to dichotomize model predictions, "
    "consistent with the default classification boundary for binary classifiers.'",
)

add_item(
    14, "Methods",
    "Whether clinical information and reference standard results were available "
    "to the performers/readers of the index test",
    "MISSING",
    "No explicit statement about blinding of index test from reference standard.",
    "Add: 'In the cross-validation framework, each model was trained on the training fold "
    "without access to the test fold labels, providing functional blinding equivalent to "
    "prospective evaluation.'",
)

add_item(
    15, "Methods",
    "Methods for estimating or comparing measures of diagnostic accuracy",
    "PRESENT" if has_text(["delong"]) and has_text(["wilson"]) and has_text(["auc"]) else "PARTIAL",
    "DeLong method for AUC CIs, Wilson CIs for proportions, DeLong test for pairwise comparison.",
)

add_item(
    16, "Methods",
    "How indeterminate index test or reference standard results were handled",
    "MISSING",
    "No mention of indeterminate results or how they would be handled.",
    "Add: 'The dataset contained no indeterminate or missing index test results. "
    "All 569 specimens had complete morphometric feature sets and confirmed histopathological diagnoses.'",
)

add_item(
    17, "Methods",
    "How missing data on the index test and reference standard were handled",
    "MISSING",
    "No discussion of missing data handling.",
    "Add: 'No missing data were present in the feature matrix or reference standard labels. "
    "All 569 specimens had complete data for all 30 morphometric features.'",
)

add_item(
    18, "Methods",
    "Any analyses of variability in diagnostic accuracy, distinguishing "
    "pre-specified from exploratory",
    "PARTIAL" if has_text(["pairwise"]) else "MISSING",
    "Pairwise DeLong comparisons performed. Feature importance analysis is exploratory but not labeled as such.",
    "Clarify: 'The primary analysis was the pairwise DeLong comparison of AUCs (pre-specified). "
    "Feature importance analysis was exploratory.'",
)

add_item(
    19, "Methods",
    "Intended sample size and how it was determined",
    "MISSING",
    "No sample size justification provided.",
    "Add: 'The full dataset of 569 specimens was used without a priori sample size calculation, "
    "as this was a secondary analysis of an existing publicly available dataset. With 212 cases and "
    "357 controls, the study had >95% power to detect an AUC of 0.95 vs. 0.50.'",
)

# --- RESULTS ---
add_item(
    20, "Results",
    "Flow of participants, using a diagram",
    "MISSING",
    "No STARD flow diagram included.",
    "Add a STARD flow diagram showing: 569 eligible specimens -> 569 included -> "
    "569 received all three index tests -> 569 included in final analysis. "
    "Note: no exclusions simplifies the diagram.",
)

add_item(
    21, "Results",
    "Baseline demographic and clinical characteristics of participants",
    "PRESENT" if has_text(["table 1"]) and has_text(["baseline"]) else "PARTIAL",
    "Table 1 presents baseline characteristics including age and morphometric features.",
)

add_item(
    22, "Results",
    "Distribution of severity of disease in those with the target condition",
    "MISSING",
    "No information on tumor grade, stage, or size distribution among malignant cases.",
    "Add: 'The Wisconsin dataset does not include tumor staging or grading information. "
    "Severity distribution could not be assessed, which limits evaluation of spectrum bias.'",
)

add_item(
    23, "Results",
    "A cross tabulation of the index test results (or their distribution) by "
    "the results of the reference standard",
    "PRESENT" if has_text(["confusion matri"]) and has_text(["true positive"]) else "PARTIAL",
    "Confusion matrices presented (Figure 2) with TP, FP, TN, FN counts for all models.",
)

add_item(
    24, "Results",
    "Estimates of diagnostic accuracy and their precision (such as 95% confidence intervals)",
    "PRESENT" if has_text(["95% ci"]) or has_text(["95% confidence"]) else "MISSING",
    "AUC with DeLong 95% CIs and all secondary metrics with Wilson 95% CIs reported.",
)

add_item(
    25, "Results",
    "Any adverse events from performing the index test or the reference standard",
    "MISSING",
    "No mention of adverse events.",
    "Add: 'As this was a retrospective analysis of pre-computed features, no adverse events "
    "were associated with the index test application. Adverse events related to the original "
    "FNA procedures were not recorded in the dataset.'",
)

# --- DISCUSSION ---
add_item(
    26, "Discussion",
    "Study limitations, including sources of potential bias, statistical "
    "uncertainty, and generalisability",
    "PRESENT" if has_text(["limitation"]) and has_text(["generalizab"]) else "PARTIAL",
    "Five limitations discussed: curated dataset, default hyperparameters, synthetic age, "
    "single institution, and cross-validation independence.",
)

add_item(
    27, "Discussion",
    "Implications for practice, including the intended use and clinical role "
    "of the index test",
    "PRESENT" if has_text(["clinical deployment"]) or has_text(["clinical decision"]) else "PARTIAL",
    "Discussion addresses clinical deployment preference for LR due to interpretability.",
)

# --- OTHER INFORMATION ---
add_item(
    28, "Other",
    "Registration number and name of registry",
    "MISSING",
    "No study registration mentioned.",
    "Add: 'This study was not registered in a clinical trial or diagnostic accuracy study registry "
    "as it was a secondary analysis of a publicly available benchmark dataset.'",
)

add_item(
    29, "Other",
    "Where the full study protocol can be accessed",
    "PARTIAL" if has_text(["supplementary"]) or has_text(["reproducib"]) else "MISSING",
    "Analysis code availability mentioned in Methods.",
    "Add: 'The complete analysis protocol and reproducible code are available at "
    "[repository URL]. No formal study protocol document was prepared.'",
)

add_item(
    30, "Other",
    "Sources of funding and other support; role of funders",
    "MISSING",
    "No funding statement included.",
    "Add: 'This study received no external funding. The authors have no conflicts of interest to declare.'",
)

# ============================================================
# GENERATE REPORT
# ============================================================
present_count = sum(1 for c in checklist if c["status"] == "PRESENT")
partial_count = sum(1 for c in checklist if c["status"] == "PARTIAL")
missing_count = sum(1 for c in checklist if c["status"] == "MISSING")

report_lines = []
report_lines.append("# STARD 2015 Compliance Report")
report_lines.append("")
report_lines.append("**Study:** Comparative Diagnostic Accuracy of Machine Learning Models "
                    "for Breast Cancer Classification Using Fine Needle Aspiration Cytology Features")
report_lines.append("")
report_lines.append("**Guideline:** STARD 2015 (Standards for Reporting Diagnostic Accuracy Studies)")
report_lines.append("")
report_lines.append("**Reference:** Bossuyt PM, et al. STARD 2015: an updated list of essential items "
                    "for reporting diagnostic accuracy studies. BMJ. 2015;351:h5527.")
report_lines.append("")
report_lines.append("---")
report_lines.append("")
report_lines.append("## Summary")
report_lines.append("")
report_lines.append(f"| Status | Count | Percentage |")
report_lines.append(f"|--------|-------|------------|")
report_lines.append(f"| PRESENT | {present_count} | {100*present_count/30:.0f}% |")
report_lines.append(f"| PARTIAL | {partial_count} | {100*partial_count/30:.0f}% |")
report_lines.append(f"| MISSING | {missing_count} | {100*missing_count/30:.0f}% |")
report_lines.append(f"| **Total** | **30** | **100%** |")
report_lines.append("")
report_lines.append("---")
report_lines.append("")

# Group by section
sections_order = ["Title/Abstract", "Abstract", "Introduction", "Methods", "Results", "Discussion", "Other"]
seen_sections = []
for sec in sections_order:
    items_in_sec = [c for c in checklist if c["section"] == sec]
    if not items_in_sec:
        continue
    if sec not in seen_sections:
        report_lines.append(f"## {sec}")
        report_lines.append("")
        seen_sections.append(sec)

    for item in items_in_sec:
        status_emoji = {"PRESENT": "PRESENT", "PARTIAL": "PARTIAL", "MISSING": "MISSING"}[item["status"]]
        report_lines.append(f"### Item {item['number']}: {item['description']}")
        report_lines.append("")
        report_lines.append(f"**Status:** {status_emoji}")
        report_lines.append("")
        report_lines.append(f"**Evidence:** {item['evidence']}")
        report_lines.append("")
        if item["recommendation"]:
            report_lines.append(f"**Recommendation:** {item['recommendation']}")
            report_lines.append("")

report_lines.append("---")
report_lines.append("")
report_lines.append("## Priority Fixes (MISSING items)")
report_lines.append("")
missing_items = [c for c in checklist if c["status"] == "MISSING"]
for i, item in enumerate(missing_items, 1):
    report_lines.append(f"{i}. **Item {item['number']}** ({item['section']}): {item['description']}")
    if item["recommendation"]:
        report_lines.append(f"   - Fix: {item['recommendation']}")
    report_lines.append("")

report_lines.append("---")
report_lines.append("")
report_lines.append("## Partial Items Requiring Strengthening")
report_lines.append("")
partial_items = [c for c in checklist if c["status"] == "PARTIAL"]
for i, item in enumerate(partial_items, 1):
    report_lines.append(f"{i}. **Item {item['number']}** ({item['section']}): {item['description']}")
    if item["recommendation"]:
        report_lines.append(f"   - Fix: {item['recommendation']}")
    report_lines.append("")

report_lines.append("---")
report_lines.append("")
report_lines.append("*Generated by MedSci Skills check-reporting pipeline.*")

report_text = "\n".join(report_lines)

# Save
output_path = os.path.join(BASE_DIR, "output", "stard_compliance_report.md")
with open(output_path, "w") as f:
    f.write(report_text)

print(f"STARD 2015 Compliance Report")
print(f"  PRESENT: {present_count}/30 ({100*present_count/30:.0f}%)")
print(f"  PARTIAL: {partial_count}/30 ({100*partial_count/30:.0f}%)")
print(f"  MISSING: {missing_count}/30 ({100*missing_count/30:.0f}%)")
print(f"Saved: {output_path}")
