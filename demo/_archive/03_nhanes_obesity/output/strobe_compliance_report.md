# STROBE Compliance Report

**Study:** Association Between Body Mass Index and Diabetes Mellitus in US Adults: A Cross-Sectional Analysis of NHANES 2017-2018

**Guideline:** STROBE Statement — Checklist of items that should be included in reports of cross-sectional studies

**Date:** 2026-04-08

---

## Summary

| Status | Count | Percentage |
|--------|-------|------------|
| PRESENT | 20 | 62% |
| PARTIAL | 8 | 25% |
| MISSING | 4 | 12% |
| **Total** | **32** | **100%** |

Overall compliance: **62%** fully present, **88%** at least partially addressed.

---

## Detailed Checklist


### Title and Abstract

**Item 1(a)** [PRESENT]: Indicate the study's design with a commonly used term in the title or the abstract

- **Assessment:** Title includes 'Cross-Sectional Analysis'; abstract states 'cross-sectional analysis'.

**Item 1(b)** [PRESENT]: Provide in the abstract an informative and balanced summary of what was done and what was found

- **Assessment:** Structured abstract with Background, Methods, Results, Conclusion; includes sample size, effect estimates with 95% CIs, and p-values.


### Introduction

**Item 2** [PRESENT]: Explain the scientific background and rationale for the investigation being reported

- **Assessment:** Introduction discusses the global diabetes burden, obesity as a modifiable risk factor, and the role of NHANES.

**Item 3** [PRESENT]: State specific objectives, including any prespecified hypotheses

- **Assessment:** Final paragraph of Introduction states the study purpose: 'to examine the association between BMI categories and diabetes prevalence.'


### Methods

**Item 4** [PRESENT]: Present key elements of study design early in the paper

- **Assessment:** First sentence of Methods identifies the study as 'cross-sectional' using NHANES 2017-2018.

**Item 5** [PRESENT]: Describe the setting, locations, and relevant dates, including periods of recruitment, exposure, follow-up, and data collection

- **Assessment:** Methods section specifies NHANES 2017-2018 cycle, CDC/NCHS, US civilian noninstitutionalized population.

**Item 6(a)** [PRESENT]: Cross-sectional study: Give the eligibility criteria, and the sources and methods of selection of participants

- **Assessment:** Eligibility: adults >= 20 years with complete BMI, HbA1c, and survey weight data. Underweight exclusion documented with count (n=74).

**Item 7** [PRESENT]: Clearly define all outcomes, exposures, predictors, potential confounders, and effect modifiers. Give diagnostic criteria, if applicable

- **Assessment:** BMI (WHO categories), diabetes (HbA1c >= 6.5% per ADA), covariates (age, sex, race/ethnicity, education) all defined.

**Item 8** [PRESENT]: For each variable of interest, give sources of data and details of methods of assessment (measurement). Describe comparability of assessment methods if there is more than one group

- **Assessment:** BMI from measured height/weight at mobile examination center; HbA1c from laboratory measurement (LBXGH).

**Item 9** [PARTIAL]: Describe any efforts to address potential sources of bias

- **Assessment:** Survey weights address selection bias; adjusted regression addresses confounding. However, no explicit 'bias' section discussing information bias or misclassification.
- **Recommendation:** Add a brief statement addressing potential information bias (e.g., HbA1c measurement error, BMI as an imperfect measure of adiposity) in the Methods or Discussion.

**Item 10** [PARTIAL]: Explain how the study size was arrived at

- **Assessment:** Final analytic sample size (n = 4,866) is reported with exclusion criteria. However, no formal sample size or power calculation is provided.
- **Recommendation:** Add a statement that the sample size was determined by the available NHANES 2017-2018 data and note the effective sample size after applying survey weights, or state that the large sample provides adequate statistical power.

**Item 11** [PRESENT]: Explain how quantitative variables were handled in the analyses. If applicable, describe which groupings were chosen and why

- **Assessment:** BMI categorized per WHO cutoffs; age as continuous; HbA1c threshold 6.5% per ADA; education categories described.

**Item 12(a)** [PRESENT]: Describe all statistical methods, including those used to control for confounding

- **Assessment:** Two models described (unadjusted and adjusted); survey-weighted GLM with binomial family; covariates listed; significance threshold stated.

**Item 12(b)** [PARTIAL]: Describe any methods used to examine subgroups and interactions

- **Assessment:** Age-by-BMI subgroup analysis shown in Figure 4, but formal interaction testing is not described.
- **Recommendation:** Add a sentence describing the subgroup analysis approach (e.g., stratified prevalence by age group and BMI category) and consider testing for statistical interaction between age and BMI on diabetes risk.

**Item 12(c)** [PARTIAL]: Explain how missing data were addressed

- **Assessment:** Complete-case analysis is implied by inclusion criteria (complete data for BMI, HbA1c, survey weights). No explicit statement about the proportion of missing data or its potential impact.
- **Recommendation:** Report the number of participants excluded due to missing data for each key variable and discuss whether missingness may be informative (e.g., sicker individuals unable to attend the examination center).

**Item 12(d)** [PRESENT]: Cross-sectional study: If applicable, describe analytical methods taking account of sampling strategy

- **Assessment:** NHANES examination survey weights (WTMEC2YR) explicitly incorporated; complex survey design acknowledged.

**Item 12(e)** [MISSING]: Describe any sensitivity analyses

- **Assessment:** No sensitivity analyses reported.
- **Recommendation:** Consider adding sensitivity analyses: (1) alternative diabetes definitions (fasting glucose or self-report), (2) including underweight participants, (3) BMI as continuous variable, (4) excluding participants on diabetes medication.


### Results

**Item 13(a)** [PARTIAL]: Report numbers of individuals at each stage of study: numbers potentially eligible, examined for eligibility, confirmed eligible, included in the study, completing follow-up, and analysed

- **Assessment:** Final analytic sample (n = 4,866) and exclusion of underweight (n = 74) reported. However, a flow diagram showing numbers at each stage (total NHANES participants -> merged -> adults 20+ -> complete data -> final sample) is not provided.
- **Recommendation:** Add a participant flow diagram (STROBE flow chart) showing the number of participants at each stage from initial NHANES sample to final analytic sample.

**Item 13(b)** [PARTIAL]: Give reasons for non-participation at each stage

- **Assessment:** Underweight exclusion reason given (small sample size). Missing data exclusion not itemized by variable.
- **Recommendation:** Provide counts of participants excluded at each step: not examined, missing BMI, missing HbA1c, missing survey weights.

**Item 13(c)** [MISSING]: Consider use of a flow diagram

- **Assessment:** No flow diagram present.
- **Recommendation:** Create a participant flow diagram showing: total NHANES 2017-2018 participants -> merged dataset -> age >= 20 filter -> complete case filter -> underweight exclusion -> final sample (n = 4,866).

**Item 14(a)** [PRESENT]: Give characteristics of study participants and information on exposures and potential confounders

- **Assessment:** Table 1 provides demographics (age, sex, race/ethnicity), BMI, HbA1c, diabetes prevalence, and glycemic status by BMI category with p-values.

**Item 14(b)** [MISSING]: Indicate number of participants with missing data for each variable of interest

- **Assessment:** No table or statement reporting the count of missing values per variable.
- **Recommendation:** Add a row to Table 1 or a supplementary table showing the number (%) of missing values for each variable before exclusion.

**Item 15** [PRESENT]: Cross-sectional study: Report numbers of outcome events or summary measures

- **Assessment:** Unweighted and weighted diabetes prevalence reported by BMI category with 95% CIs. Total n diabetes = 724 (14.9% unweighted, 10.2% weighted).

**Item 16(a)** [PRESENT]: Give unadjusted estimates and, if applicable, confounder-adjusted estimates and their precision. Make clear which confounders were adjusted for and why they were included

- **Assessment:** Both unadjusted (Model 1) and adjusted (Model 2) ORs reported with 95% CIs and p-values. Covariates clearly listed.

**Item 16(b)** [PRESENT]: Report category boundaries when continuous variables were categorized

- **Assessment:** BMI categories defined with WHO cutoffs (18.5, 25, 30); age groups (20-39, 40-59, 60-79) for subgroup analysis; HbA1c thresholds (5.7%, 6.5%).

**Item 16(c)** [PARTIAL]: If relevant, consider translating estimates of relative risk into absolute risk for a meaningful time period

- **Assessment:** Prevalence estimates serve as absolute measures; ORs provided as relative measures. However, predicted probabilities from the logistic model are not reported.
- **Recommendation:** Consider adding predicted probabilities of diabetes for prototypical individuals (e.g., 50-year-old NH White male, normal weight vs. obese) to illustrate absolute risk differences.


### Discussion

**Item 17** [PRESENT]: Summarise key results with reference to study objectives

- **Assessment:** Principal Findings section summarizes the dose-response relationship, effect sizes, and independence from confounders.

**Item 18** [PRESENT]: Discuss limitations of the study, taking into account sources of potential bias or imprecision

- **Assessment:** Five limitations discussed: cross-sectional design, HbA1c-only definition, type 1 vs type 2 distinction, residual confounding, single survey cycle.

**Item 19** [PRESENT]: Give a cautious overall interpretation of results considering objectives, limitations, multiplicity of analyses, and results from similar studies

- **Assessment:** Discussion includes comparison with prior literature, cautious language about association vs. causation, and acknowledgment of limitations.

**Item 20** [PRESENT]: Discuss the generalizability (external validity) of the study results

- **Assessment:** Survey weights ensure generalizability to the US civilian noninstitutionalized population. Discussion notes that NHANES design provides nationally representative estimates.


### Other Information

**Item 21** [MISSING]: Give the source of funding and the role of the funders for the present study and, if applicable, for the original study on which the present article is based

- **Assessment:** No funding statement present.
- **Recommendation:** Add a funding statement (e.g., 'This study used publicly available NHANES data. No specific funding was received for this analysis.' or declare the actual funding source).

**Item 22** [PARTIAL]: State where readers can access study data and supplementary material

- **Assessment:** Data source (NHANES 2017-2018, CDC) is identified but no explicit data availability statement with URLs.
- **Recommendation:** Add a Data Availability Statement: 'The NHANES 2017-2018 data used in this study are publicly available from the CDC National Center for Health Statistics at https://www.cdc.gov/nchs/nhanes/.'

---

## Priority Action Items

### Items Rated MISSING (require addition)

1. **Item 12(e) (Methods):** Describe any sensitivity analyses
   - Fix: Consider adding sensitivity analyses: (1) alternative diabetes definitions (fasting glucose or self-report), (2) including underweight participants, (3) BMI as continuous variable, (4) excluding participants on diabetes medication.

1. **Item 13(c) (Results):** Consider use of a flow diagram
   - Fix: Create a participant flow diagram showing: total NHANES 2017-2018 participants -> merged dataset -> age >= 20 filter -> complete case filter -> underweight exclusion -> final sample (n = 4,866).

1. **Item 14(b) (Results):** Indicate number of participants with missing data for each variable of interest
   - Fix: Add a row to Table 1 or a supplementary table showing the number (%) of missing values for each variable before exclusion.

1. **Item 21 (Other Information):** Give the source of funding and the role of the funders for the present study and, if applicable, for the original study on which the present article is based
   - Fix: Add a funding statement (e.g., 'This study used publicly available NHANES data. No specific funding was received for this analysis.' or declare the actual funding source).

### Items Rated PARTIAL (require improvement)

1. **Item 9 (Methods):** Describe any efforts to address potential sources of bias
   - Fix: Add a brief statement addressing potential information bias (e.g., HbA1c measurement error, BMI as an imperfect measure of adiposity) in the Methods or Discussion.

1. **Item 10 (Methods):** Explain how the study size was arrived at
   - Fix: Add a statement that the sample size was determined by the available NHANES 2017-2018 data and note the effective sample size after applying survey weights, or state that the large sample provides adequate statistical power.

1. **Item 12(b) (Methods):** Describe any methods used to examine subgroups and interactions
   - Fix: Add a sentence describing the subgroup analysis approach (e.g., stratified prevalence by age group and BMI category) and consider testing for statistical interaction between age and BMI on diabetes risk.

1. **Item 12(c) (Methods):** Explain how missing data were addressed
   - Fix: Report the number of participants excluded due to missing data for each key variable and discuss whether missingness may be informative (e.g., sicker individuals unable to attend the examination center).

1. **Item 13(a) (Results):** Report numbers of individuals at each stage of study: numbers potentially eligible, examined for eligibility, confirmed eligible, included in the study, completing follow-up, and analysed
   - Fix: Add a participant flow diagram (STROBE flow chart) showing the number of participants at each stage from initial NHANES sample to final analytic sample.

1. **Item 13(b) (Results):** Give reasons for non-participation at each stage
   - Fix: Provide counts of participants excluded at each step: not examined, missing BMI, missing HbA1c, missing survey weights.

1. **Item 16(c) (Results):** If relevant, consider translating estimates of relative risk into absolute risk for a meaningful time period
   - Fix: Consider adding predicted probabilities of diabetes for prototypical individuals (e.g., 50-year-old NH White male, normal weight vs. obese) to illustrate absolute risk differences.

1. **Item 22 (Other Information):** State where readers can access study data and supplementary material
   - Fix: Add a Data Availability Statement: 'The NHANES 2017-2018 data used in this study are publicly available from the CDC National Center for Health Statistics at https://www.cdc.gov/nchs/nhanes/.'

---

## Recommendations Summary

The manuscript demonstrates strong overall STROBE compliance (62% fully present). Key areas for improvement:

1. **Participant flow diagram** (Items 13a, 13c): Create a flow diagram showing participant selection from initial NHANES sample through final analytic sample.
2. **Missing data reporting** (Items 12c, 14b): Quantify and report missing data for each key variable.
3. **Sensitivity analyses** (Item 12e): Add at least one sensitivity analysis (e.g., alternative diabetes definition, BMI as continuous).
4. **Funding and data availability** (Items 21, 22): Add explicit funding and data availability statements.
5. **Bias discussion** (Item 9): Expand the discussion of potential information bias and measurement error.

These additions would bring the manuscript to near-complete STROBE compliance and strengthen the overall methodological transparency.
