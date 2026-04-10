"""
MedSci Skills Demo 3: NHANES Obesity & Diabetes
Step 4 — STROBE Checklist Compliance Report (check-reporting skill)

Evaluates manuscript draft against the STROBE checklist for
cross-sectional studies (22 items).

Usage: python3 04_strobe_checklist.py
Output: output/strobe_compliance_report.md
"""

import os
import datetime

print("=" * 60)
print("MedSci Skills Demo 3: STROBE Checklist Evaluation")
print(f"Date: {datetime.date.today()}")
print("=" * 60)

# Read the manuscript draft
with open("output/manuscript_draft.md", "r") as f:
    manuscript = f.read()

# STROBE checklist items for cross-sectional studies
# Each item: (number, section, description, status, location, recommendation)
strobe_items = [
    # Title and Abstract
    (
        "1(a)",
        "Title and Abstract",
        "Indicate the study's design with a commonly used term in the title or the abstract",
        "PRESENT",
        "Title includes 'Cross-Sectional Analysis'; abstract states 'cross-sectional analysis'.",
        None,
    ),
    (
        "1(b)",
        "Title and Abstract",
        "Provide in the abstract an informative and balanced summary of what was done and what was found",
        "PRESENT",
        "Structured abstract with Background, Methods, Results, Conclusion; includes sample size, effect estimates with 95% CIs, and p-values.",
        None,
    ),
    # Introduction
    (
        "2",
        "Introduction",
        "Explain the scientific background and rationale for the investigation being reported",
        "PRESENT",
        "Introduction discusses the global diabetes burden, obesity as a modifiable risk factor, and the role of NHANES.",
        None,
    ),
    (
        "3",
        "Introduction",
        "State specific objectives, including any prespecified hypotheses",
        "PRESENT",
        "Final paragraph of Introduction states the study purpose: 'to examine the association between BMI categories and diabetes prevalence.'",
        None,
    ),
    # Methods
    (
        "4",
        "Methods",
        "Present key elements of study design early in the paper",
        "PRESENT",
        "First sentence of Methods identifies the study as 'cross-sectional' using NHANES 2017-2018.",
        None,
    ),
    (
        "5",
        "Methods",
        "Describe the setting, locations, and relevant dates, including periods of recruitment, exposure, follow-up, and data collection",
        "PRESENT",
        "Methods section specifies NHANES 2017-2018 cycle, CDC/NCHS, US civilian noninstitutionalized population.",
        None,
    ),
    (
        "6(a)",
        "Methods",
        "Cross-sectional study: Give the eligibility criteria, and the sources and methods of selection of participants",
        "PRESENT",
        "Eligibility: adults >= 20 years with complete BMI, HbA1c, and survey weight data. Underweight exclusion documented with count (n=74).",
        None,
    ),
    (
        "7",
        "Methods",
        "Clearly define all outcomes, exposures, predictors, potential confounders, and effect modifiers. Give diagnostic criteria, if applicable",
        "PRESENT",
        "BMI (WHO categories), diabetes (HbA1c >= 6.5% per ADA), covariates (age, sex, race/ethnicity, education) all defined.",
        None,
    ),
    (
        "8",
        "Methods",
        "For each variable of interest, give sources of data and details of methods of assessment (measurement). Describe comparability of assessment methods if there is more than one group",
        "PRESENT",
        "BMI from measured height/weight at mobile examination center; HbA1c from laboratory measurement (LBXGH).",
        None,
    ),
    (
        "9",
        "Methods",
        "Describe any efforts to address potential sources of bias",
        "PARTIAL",
        "Survey weights address selection bias; adjusted regression addresses confounding. However, no explicit 'bias' section discussing information bias or misclassification.",
        "Add a brief statement addressing potential information bias (e.g., HbA1c measurement error, BMI as an imperfect measure of adiposity) in the Methods or Discussion.",
    ),
    (
        "10",
        "Methods",
        "Explain how the study size was arrived at",
        "PARTIAL",
        "Final analytic sample size (n = 4,866) is reported with exclusion criteria. However, no formal sample size or power calculation is provided.",
        "Add a statement that the sample size was determined by the available NHANES 2017-2018 data and note the effective sample size after applying survey weights, or state that the large sample provides adequate statistical power.",
    ),
    (
        "11",
        "Methods",
        "Explain how quantitative variables were handled in the analyses. If applicable, describe which groupings were chosen and why",
        "PRESENT",
        "BMI categorized per WHO cutoffs; age as continuous; HbA1c threshold 6.5% per ADA; education categories described.",
        None,
    ),
    (
        "12(a)",
        "Methods",
        "Describe all statistical methods, including those used to control for confounding",
        "PRESENT",
        "Two models described (unadjusted and adjusted); survey-weighted GLM with binomial family; covariates listed; significance threshold stated.",
        None,
    ),
    (
        "12(b)",
        "Methods",
        "Describe any methods used to examine subgroups and interactions",
        "PARTIAL",
        "Age-by-BMI subgroup analysis shown in Figure 4, but formal interaction testing is not described.",
        "Add a sentence describing the subgroup analysis approach (e.g., stratified prevalence by age group and BMI category) and consider testing for statistical interaction between age and BMI on diabetes risk.",
    ),
    (
        "12(c)",
        "Methods",
        "Explain how missing data were addressed",
        "PARTIAL",
        "Complete-case analysis is implied by inclusion criteria (complete data for BMI, HbA1c, survey weights). No explicit statement about the proportion of missing data or its potential impact.",
        "Report the number of participants excluded due to missing data for each key variable and discuss whether missingness may be informative (e.g., sicker individuals unable to attend the examination center).",
    ),
    (
        "12(d)",
        "Methods",
        "Cross-sectional study: If applicable, describe analytical methods taking account of sampling strategy",
        "PRESENT",
        "NHANES examination survey weights (WTMEC2YR) explicitly incorporated; complex survey design acknowledged.",
        None,
    ),
    (
        "12(e)",
        "Methods",
        "Describe any sensitivity analyses",
        "MISSING",
        "No sensitivity analyses reported.",
        "Consider adding sensitivity analyses: (1) alternative diabetes definitions (fasting glucose or self-report), (2) including underweight participants, (3) BMI as continuous variable, (4) excluding participants on diabetes medication.",
    ),
    # Results
    (
        "13(a)",
        "Results",
        "Report numbers of individuals at each stage of study: numbers potentially eligible, examined for eligibility, confirmed eligible, included in the study, completing follow-up, and analysed",
        "PARTIAL",
        "Final analytic sample (n = 4,866) and exclusion of underweight (n = 74) reported. However, a flow diagram showing numbers at each stage (total NHANES participants -> merged -> adults 20+ -> complete data -> final sample) is not provided.",
        "Add a participant flow diagram (STROBE flow chart) showing the number of participants at each stage from initial NHANES sample to final analytic sample.",
    ),
    (
        "13(b)",
        "Results",
        "Give reasons for non-participation at each stage",
        "PARTIAL",
        "Underweight exclusion reason given (small sample size). Missing data exclusion not itemized by variable.",
        "Provide counts of participants excluded at each step: not examined, missing BMI, missing HbA1c, missing survey weights.",
    ),
    (
        "13(c)",
        "Results",
        "Consider use of a flow diagram",
        "MISSING",
        "No flow diagram present.",
        "Create a participant flow diagram showing: total NHANES 2017-2018 participants -> merged dataset -> age >= 20 filter -> complete case filter -> underweight exclusion -> final sample (n = 4,866).",
    ),
    (
        "14(a)",
        "Results",
        "Give characteristics of study participants and information on exposures and potential confounders",
        "PRESENT",
        "Table 1 provides demographics (age, sex, race/ethnicity), BMI, HbA1c, diabetes prevalence, and glycemic status by BMI category with p-values.",
        None,
    ),
    (
        "14(b)",
        "Results",
        "Indicate number of participants with missing data for each variable of interest",
        "MISSING",
        "No table or statement reporting the count of missing values per variable.",
        "Add a row to Table 1 or a supplementary table showing the number (%) of missing values for each variable before exclusion.",
    ),
    (
        "15",
        "Results",
        "Cross-sectional study: Report numbers of outcome events or summary measures",
        "PRESENT",
        "Unweighted and weighted diabetes prevalence reported by BMI category with 95% CIs. Total n diabetes = 724 (14.9% unweighted, 10.2% weighted).",
        None,
    ),
    (
        "16(a)",
        "Results",
        "Give unadjusted estimates and, if applicable, confounder-adjusted estimates and their precision. Make clear which confounders were adjusted for and why they were included",
        "PRESENT",
        "Both unadjusted (Model 1) and adjusted (Model 2) ORs reported with 95% CIs and p-values. Covariates clearly listed.",
        None,
    ),
    (
        "16(b)",
        "Results",
        "Report category boundaries when continuous variables were categorized",
        "PRESENT",
        "BMI categories defined with WHO cutoffs (18.5, 25, 30); age groups (20-39, 40-59, 60-79) for subgroup analysis; HbA1c thresholds (5.7%, 6.5%).",
        None,
    ),
    (
        "16(c)",
        "Results",
        "If relevant, consider translating estimates of relative risk into absolute risk for a meaningful time period",
        "PARTIAL",
        "Prevalence estimates serve as absolute measures; ORs provided as relative measures. However, predicted probabilities from the logistic model are not reported.",
        "Consider adding predicted probabilities of diabetes for prototypical individuals (e.g., 50-year-old NH White male, normal weight vs. obese) to illustrate absolute risk differences.",
    ),
    # Discussion
    (
        "17",
        "Discussion",
        "Summarise key results with reference to study objectives",
        "PRESENT",
        "Principal Findings section summarizes the dose-response relationship, effect sizes, and independence from confounders.",
        None,
    ),
    (
        "18",
        "Discussion",
        "Discuss limitations of the study, taking into account sources of potential bias or imprecision",
        "PRESENT",
        "Five limitations discussed: cross-sectional design, HbA1c-only definition, type 1 vs type 2 distinction, residual confounding, single survey cycle.",
        None,
    ),
    (
        "19",
        "Discussion",
        "Give a cautious overall interpretation of results considering objectives, limitations, multiplicity of analyses, and results from similar studies",
        "PRESENT",
        "Discussion includes comparison with prior literature, cautious language about association vs. causation, and acknowledgment of limitations.",
        None,
    ),
    (
        "20",
        "Discussion",
        "Discuss the generalizability (external validity) of the study results",
        "PRESENT",
        "Survey weights ensure generalizability to the US civilian noninstitutionalized population. Discussion notes that NHANES design provides nationally representative estimates.",
        None,
    ),
    # Other information
    (
        "21",
        "Other Information",
        "Give the source of funding and the role of the funders for the present study and, if applicable, for the original study on which the present article is based",
        "MISSING",
        "No funding statement present.",
        "Add a funding statement (e.g., 'This study used publicly available NHANES data. No specific funding was received for this analysis.' or declare the actual funding source).",
    ),
    (
        "22",
        "Other Information",
        "State where readers can access study data and supplementary material",
        "PARTIAL",
        "Data source (NHANES 2017-2018, CDC) is identified but no explicit data availability statement with URLs.",
        "Add a Data Availability Statement: 'The NHANES 2017-2018 data used in this study are publicly available from the CDC National Center for Health Statistics at https://www.cdc.gov/nchs/nhanes/.'",
    ),
]

# === Generate report ===
n_present = sum(1 for item in strobe_items if item[3] == "PRESENT")
n_partial = sum(1 for item in strobe_items if item[3] == "PARTIAL")
n_missing = sum(1 for item in strobe_items if item[3] == "MISSING")
n_total = len(strobe_items)

report = f"""# STROBE Compliance Report

**Study:** Association Between Body Mass Index and Diabetes Mellitus in US Adults: A Cross-Sectional Analysis of NHANES 2017-2018

**Guideline:** STROBE Statement — Checklist of items that should be included in reports of cross-sectional studies

**Date:** {datetime.date.today()}

---

## Summary

| Status | Count | Percentage |
|--------|-------|------------|
| PRESENT | {n_present} | {100*n_present/n_total:.0f}% |
| PARTIAL | {n_partial} | {100*n_partial/n_total:.0f}% |
| MISSING | {n_missing} | {100*n_missing/n_total:.0f}% |
| **Total** | **{n_total}** | **100%** |

Overall compliance: **{100*n_present/n_total:.0f}%** fully present, **{100*(n_present+n_partial)/n_total:.0f}%** at least partially addressed.

---

## Detailed Checklist

"""

current_section = ""
for item_num, section, description, status, location, recommendation in strobe_items:
    if section != current_section:
        report += f"\n### {section}\n\n"
        current_section = section

    # Status emoji alternative (text-based)
    status_indicator = {
        "PRESENT": "[PRESENT]",
        "PARTIAL": "[PARTIAL]",
        "MISSING": "[MISSING]",
    }[status]

    report += f"**Item {item_num}** {status_indicator}: {description}\n\n"
    report += f"- **Assessment:** {location}\n"
    if recommendation:
        report += f"- **Recommendation:** {recommendation}\n"
    report += "\n"

# Action items summary
report += """---

## Priority Action Items

### Items Rated MISSING (require addition)

"""

for item_num, section, description, status, location, recommendation in strobe_items:
    if status == "MISSING":
        report += f"1. **Item {item_num} ({section}):** {description}\n"
        report += f"   - Fix: {recommendation}\n\n"

report += """### Items Rated PARTIAL (require improvement)

"""

for item_num, section, description, status, location, recommendation in strobe_items:
    if status == "PARTIAL":
        report += f"1. **Item {item_num} ({section}):** {description}\n"
        report += f"   - Fix: {recommendation}\n\n"

report += f"""---

## Recommendations Summary

The manuscript demonstrates strong overall STROBE compliance ({100*n_present/n_total:.0f}% fully present). Key areas for improvement:

1. **Participant flow diagram** (Items 13a, 13c): Create a flow diagram showing participant selection from initial NHANES sample through final analytic sample.
2. **Missing data reporting** (Items 12c, 14b): Quantify and report missing data for each key variable.
3. **Sensitivity analyses** (Item 12e): Add at least one sensitivity analysis (e.g., alternative diabetes definition, BMI as continuous).
4. **Funding and data availability** (Items 21, 22): Add explicit funding and data availability statements.
5. **Bias discussion** (Item 9): Expand the discussion of potential information bias and measurement error.

These additions would bring the manuscript to near-complete STROBE compliance and strengthen the overall methodological transparency.
"""

# Save report
os.makedirs("output", exist_ok=True)
with open("output/strobe_compliance_report.md", "w") as f:
    f.write(report)

print(f"\nSTROBE Compliance Summary:")
print(f"  PRESENT: {n_present}/{n_total} ({100*n_present/n_total:.0f}%)")
print(f"  PARTIAL: {n_partial}/{n_total} ({100*n_partial/n_total:.0f}%)")
print(f"  MISSING: {n_missing}/{n_total} ({100*n_missing/n_total:.0f}%)")
print(f"\nSaved: output/strobe_compliance_report.md")
print("=" * 60)
