# PRISMA 2020 Compliance Report

**Study:** Efficacy of BCG Vaccination for Prevention of Tuberculosis: A Meta-Analysis of Randomized Controlled Trials
**Assessment date:** 2026-04-08
**Assessor:** MedSci Skills (check-reporting skill)
**Guideline:** PRISMA 2020 (Page et al., BMJ 2021;372:n71)

> **Note:** This is a re-analysis of the Colditz et al. (1994) dataset available as `metafor::dat.bcg`. Items related to literature searching, screening, and study selection are rated N/A because no de novo systematic search was conducted.

## Summary

| Status | Count |
|--------|-------|
| PRESENT | 18 |
| PARTIAL | 1 |
| MISSING | 6 |
| N/A | 6 |
| **Total items** | **31** |
| **Compliance (applicable)** | **74%** |

## Detailed Checklist

| Section | Item | Topic | Status | Comment |
|---------|------|-------|--------|---------|
| Title | 1 | Identify the report as a systematic review incorporating a meta-analysis | PRESENT | Title includes 'Meta-Analysis of Randomized Controlled Trials' |
| Abstract | 2 | Structured summary with background, methods, results, conclusion | PRESENT | Abstract: structured with Background, Methods, Results, Conclusion sections |
| Introduction | 3 | Rationale: describe the rationale in the context of existing knowledge | PRESENT | Introduction: discusses BCG efficacy variability, NTM hypothesis, Colditz 1994 |
| Introduction | 4 | Objectives: provide an explicit statement of the questions addressed | PRESENT | Introduction: quantify BCG efficacy, assess heterogeneity sources, evaluate robustness |
| Methods | 5 | Eligibility criteria: report criteria with rationale | PARTIAL | Methods/Eligibility: references original Colditz criteria; limited detail since built-in dataset |
| Methods | 6 | Information sources: describe all sources with dates of searches | N/A | Built-in dataset (metafor::dat.bcg). No de novo literature search was conducted |
| Methods | 7 | Search strategy: present full search strategy for at least one database | N/A | Built-in dataset. No search strategy applicable |
| Methods | 8 | Selection process: state process for selecting studies | N/A | Built-in curated dataset; no independent study selection performed |
| Methods | 9 | Data collection process: describe methods of data extraction | N/A | Pre-extracted 2x2 tables provided in dataset; no manual data extraction |
| Methods | 10 | Data items: list and define all variables for which data were sought | PRESENT | Methods: specifies 2x2 table cells, allocation method, latitude, year |
| Methods | 11 | Study risk of bias assessment: methods for assessing risk of bias | MISSING | No formal risk of bias tool (e.g., Cochrane RoB 2) was applied to individual studies |
| Methods | 12 | Effect measures: specify for each outcome the effect measure used | PRESENT | Methods: risk ratio (RR) from 2x2 tables, computed via escalc() |
| Methods | 13 | Synthesis methods: describe processes for deciding which studies to combine, tab... | PRESENT | Methods: REML random-effects model, Q/I-squared/tau-squared, subgroup, meta-regression, LOO, publication bias |
| Methods | 13 | Synthesis methods (a): describe criteria for tabulating and combining studies | PRESENT | All 13 RCTs combined; subgroup by allocation method |
| Methods | 13 | Synthesis methods (b): describe methods for meta-analysis (model, estimator) | PRESENT | Random-effects REML via metafor::rma() |
| Methods | 13 | Synthesis methods (c): describe methods for heterogeneity (Q, I-squared, predict... | PRESENT | Q statistic, I-squared, tau-squared, prediction interval all reported |
| Methods | 13 | Synthesis methods (d): describe sensitivity analyses planned | PRESENT | Leave-one-out analysis, influence diagnostics |
| Methods | 14 | Reporting bias assessment: describe methods for assessing publication bias | PRESENT | Funnel plot, Egger's test, Begg's test, trim-and-fill |
| Methods | 15 | Certainty assessment: describe methods for assessing certainty (e.g., GRADE) | MISSING | No GRADE or certainty of evidence assessment was performed |
| Results | 16 | Study selection: numbers of studies screened, assessed, included with flow diagr... | N/A | Built-in dataset; no screening process. PRISMA flow diagram not applicable |
| Results | 17 | Study characteristics: cite each study and present characteristics | PRESENT | Results/Table: 13 studies with author, year, RR, CI, weight, latitude, allocation |
| Results | 18 | Risk of bias in studies: present assessments for each study | MISSING | No individual study risk of bias assessment reported |
| Results | 19 | Results of individual studies: present data for each study and forest plot | PRESENT | Forest plot (Figure 1) and study_results.csv with per-study RR and 95% CI |
| Results | 20 | Results of syntheses: present pooled estimate with CI, heterogeneity, forest plo... | PRESENT | RR = 0.489 (95% CI: 0.344-0.696), I-squared = 92.2%, forest plot with diamond |
| Results | 21 | Reporting biases: present results of publication bias assessment | PRESENT | Egger's p = 0.189, Begg's p = 0.952, trim-and-fill: 1 study, adjusted RR = 0.518 |
| Results | 22 | Certainty of evidence: present certainty for each outcome | MISSING | No GRADE assessment presented |
| Discussion | 23 | Discussion: provide general interpretation in context, limitations, implications | PRESENT | Discussion: latitude effect interpretation, NTM hypothesis, heterogeneity, 5 limitations listed |
| Other | 24 | Registration and protocol: provide registration number and protocol access | N/A | Teaching demonstration; no PROSPERO registration |
| Other | 25 | Support: describe sources of financial or non-financial support | MISSING | No funding statement included |
| Other | 26 | Competing interests: declare any competing interests | MISSING | No conflict of interest statement included |
| Other | 27 | Availability of data, code, and materials | PRESENT | Dataset: metafor::dat.bcg (publicly available). Analysis code: 01_meta_analysis.R |

## Recommendations for Improvement

### Missing Items

- **Item 11 (Methods):** Study risk of bias assessment: methods for assessing risk of bias
  - *Action needed:* No formal risk of bias tool (e.g., Cochrane RoB 2) was applied to individual studies

- **Item 15 (Methods):** Certainty assessment: describe methods for assessing certainty (e.g., GRADE)
  - *Action needed:* No GRADE or certainty of evidence assessment was performed

- **Item 18 (Results):** Risk of bias in studies: present assessments for each study
  - *Action needed:* No individual study risk of bias assessment reported

- **Item 22 (Results):** Certainty of evidence: present certainty for each outcome
  - *Action needed:* No GRADE assessment presented

- **Item 25 (Other):** Support: describe sources of financial or non-financial support
  - *Action needed:* No funding statement included

- **Item 26 (Other):** Competing interests: declare any competing interests
  - *Action needed:* No conflict of interest statement included

### Partial Items

- **Item 5 (Methods):** Eligibility criteria: report criteria with rationale
  - *Improvement:* Methods/Eligibility: references original Colditz criteria; limited detail since built-in dataset

### Priority Actions

1. **Risk of bias assessment (Items 11, 18):** Apply Cochrane Risk of Bias 2 (RoB 2) tool to each included RCT and present results in a summary figure.
2. **GRADE certainty assessment (Items 15, 22):** Evaluate certainty of evidence using the GRADE framework (risk of bias, inconsistency, indirectness, imprecision, publication bias) and present a Summary of Findings table.
3. **Funding and COI statements (Items 25, 26):** Add declarations even if none exist (state 'No funding received' and 'No conflicts of interest').
4. **Eligibility criteria (Item 5):** Expand description of original Colditz criteria including population, intervention, comparator, outcome, and study design.

---
*Generated: 2026-04-08 | MedSci Skills Demo 2 — check-reporting skill*
