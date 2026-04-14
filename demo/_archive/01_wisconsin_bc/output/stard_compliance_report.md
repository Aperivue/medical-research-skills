# STARD 2015 Compliance Report

**Study:** Comparative Diagnostic Accuracy of Machine Learning Models for Breast Cancer Classification Using Fine Needle Aspiration Cytology Features

**Guideline:** STARD 2015 (Standards for Reporting Diagnostic Accuracy Studies)

**Reference:** Bossuyt PM, et al. STARD 2015: an updated list of essential items for reporting diagnostic accuracy studies. BMJ. 2015;351:h5527.

---

## Summary

| Status | Count | Percentage |
|--------|-------|------------|
| PRESENT | 15 | 50% |
| PARTIAL | 6 | 20% |
| MISSING | 9 | 30% |
| **Total** | **30** | **100%** |

---

## Title/Abstract

### Item 1: Identification as a study of diagnostic accuracy using at least one measure of accuracy (such as sensitivity, specificity, predictive values, or AUC)

**Status:** PRESENT

**Evidence:** Title contains 'Comparative Diagnostic Accuracy'; abstract reports AUC, sensitivity, specificity.

## Abstract

### Item 2: Structured abstract with study design, methods, results, and conclusions

**Status:** PRESENT

**Evidence:** Abstract contains structured sections: Background, Objective, Methods, Results, Conclusions.

## Introduction

### Item 3: Scientific and clinical background, including the intended use and clinical role of the index test

**Status:** PRESENT

**Evidence:** Introduction describes FNA as first-line diagnostic tool and clinical context of breast cancer diagnosis.

### Item 4: Study objectives and hypotheses

**Status:** PRESENT

**Evidence:** Introduction states the objective to compare diagnostic accuracy of three ML classifiers.

## Methods

### Item 5: Whether data collection was planned before the index test and reference standard were performed (prospective study) or after (retrospective study)

**Status:** PRESENT

**Evidence:** Methods states 'Retrospective cross-sectional diagnostic accuracy study'.

### Item 6: Eligibility criteria

**Status:** PRESENT

**Evidence:** Dataset described as 569 FNA cytology specimens from patients presenting with breast masses.

**Recommendation:** Consider adding explicit inclusion/exclusion criteria (e.g., 'All consecutive FNA specimens with confirmed histopathological diagnosis were included. No specimens were excluded.').

### Item 7: On what basis potentially eligible participants were identified (such as symptoms, results from previous tests, inclusion in registry)

**Status:** PARTIAL

**Evidence:** Mentions 'presenting with breast masses' but does not specify referral pathway or registry.

**Recommendation:** Add: 'Patients were identified based on clinical presentation with palpable breast masses referred for FNA cytology at the University of Wisconsin Hospital.'

### Item 8: Where and when the study was conducted, including the period of recruitment

**Status:** PRESENT

**Evidence:** Methods mentions University of Wisconsin Hospital, January 1989 to November 1991.

### Item 9: Whether participants formed a consecutive, random, or convenience series

**Status:** PARTIAL

**Evidence:** Text mentions 'consecutive FNA cytology specimens'.

**Recommendation:** Strengthen by stating explicitly: 'The dataset comprised a consecutive series of FNA specimens. No convenience sampling was applied.'

### Item 10: Index test, in sufficient detail to allow replication

**Status:** PRESENT

**Evidence:** All three index tests described with hyperparameters, cross-validation strategy, and scaling approach.

### Item 11: Reference standard, in sufficient detail to allow replication

**Status:** PRESENT

**Evidence:** Reference standard identified as histopathological diagnosis via surgical excision or core needle biopsy.

### Item 12: Rationale for choosing the reference standard (if alternatives exist)

**Status:** PARTIAL

**Evidence:** Histopathology is described as reference standard but no explicit rationale for choosing it over alternatives.

**Recommendation:** Add: 'Histopathological examination was chosen as the reference standard because it represents the highest-certainty method for distinguishing benign from malignant breast lesions.'

### Item 13: Definition of and rationale for test positivity cut-offs or result categories, including whether the cut-off was pre-specified

**Status:** PARTIAL

**Evidence:** Default 0.5 probability threshold implied but not explicitly stated.

**Recommendation:** Add: 'A probability threshold of 0.5 was used to dichotomize model predictions, consistent with the default classification boundary for binary classifiers.'

### Item 14: Whether clinical information and reference standard results were available to the performers/readers of the index test

**Status:** MISSING

**Evidence:** No explicit statement about blinding of index test from reference standard.

**Recommendation:** Add: 'In the cross-validation framework, each model was trained on the training fold without access to the test fold labels, providing functional blinding equivalent to prospective evaluation.'

### Item 15: Methods for estimating or comparing measures of diagnostic accuracy

**Status:** PRESENT

**Evidence:** DeLong method for AUC CIs, Wilson CIs for proportions, DeLong test for pairwise comparison.

### Item 16: How indeterminate index test or reference standard results were handled

**Status:** MISSING

**Evidence:** No mention of indeterminate results or how they would be handled.

**Recommendation:** Add: 'The dataset contained no indeterminate or missing index test results. All 569 specimens had complete morphometric feature sets and confirmed histopathological diagnoses.'

### Item 17: How missing data on the index test and reference standard were handled

**Status:** MISSING

**Evidence:** No discussion of missing data handling.

**Recommendation:** Add: 'No missing data were present in the feature matrix or reference standard labels. All 569 specimens had complete data for all 30 morphometric features.'

### Item 18: Any analyses of variability in diagnostic accuracy, distinguishing pre-specified from exploratory

**Status:** PARTIAL

**Evidence:** Pairwise DeLong comparisons performed. Feature importance analysis is exploratory but not labeled as such.

**Recommendation:** Clarify: 'The primary analysis was the pairwise DeLong comparison of AUCs (pre-specified). Feature importance analysis was exploratory.'

### Item 19: Intended sample size and how it was determined

**Status:** MISSING

**Evidence:** No sample size justification provided.

**Recommendation:** Add: 'The full dataset of 569 specimens was used without a priori sample size calculation, as this was a secondary analysis of an existing publicly available dataset. With 212 cases and 357 controls, the study had >95% power to detect an AUC of 0.95 vs. 0.50.'

## Results

### Item 20: Flow of participants, using a diagram

**Status:** MISSING

**Evidence:** No STARD flow diagram included.

**Recommendation:** Add a STARD flow diagram showing: 569 eligible specimens -> 569 included -> 569 received all three index tests -> 569 included in final analysis. Note: no exclusions simplifies the diagram.

### Item 21: Baseline demographic and clinical characteristics of participants

**Status:** PRESENT

**Evidence:** Table 1 presents baseline characteristics including age and morphometric features.

### Item 22: Distribution of severity of disease in those with the target condition

**Status:** MISSING

**Evidence:** No information on tumor grade, stage, or size distribution among malignant cases.

**Recommendation:** Add: 'The Wisconsin dataset does not include tumor staging or grading information. Severity distribution could not be assessed, which limits evaluation of spectrum bias.'

### Item 23: A cross tabulation of the index test results (or their distribution) by the results of the reference standard

**Status:** PRESENT

**Evidence:** Confusion matrices presented (Figure 2) with TP, FP, TN, FN counts for all models.

### Item 24: Estimates of diagnostic accuracy and their precision (such as 95% confidence intervals)

**Status:** PRESENT

**Evidence:** AUC with DeLong 95% CIs and all secondary metrics with Wilson 95% CIs reported.

### Item 25: Any adverse events from performing the index test or the reference standard

**Status:** MISSING

**Evidence:** No mention of adverse events.

**Recommendation:** Add: 'As this was a retrospective analysis of pre-computed features, no adverse events were associated with the index test application. Adverse events related to the original FNA procedures were not recorded in the dataset.'

## Discussion

### Item 26: Study limitations, including sources of potential bias, statistical uncertainty, and generalisability

**Status:** PRESENT

**Evidence:** Five limitations discussed: curated dataset, default hyperparameters, synthetic age, single institution, and cross-validation independence.

### Item 27: Implications for practice, including the intended use and clinical role of the index test

**Status:** PRESENT

**Evidence:** Discussion addresses clinical deployment preference for LR due to interpretability.

## Other

### Item 28: Registration number and name of registry

**Status:** MISSING

**Evidence:** No study registration mentioned.

**Recommendation:** Add: 'This study was not registered in a clinical trial or diagnostic accuracy study registry as it was a secondary analysis of a publicly available benchmark dataset.'

### Item 29: Where the full study protocol can be accessed

**Status:** PARTIAL

**Evidence:** Analysis code availability mentioned in Methods.

**Recommendation:** Add: 'The complete analysis protocol and reproducible code are available at [repository URL]. No formal study protocol document was prepared.'

### Item 30: Sources of funding and other support; role of funders

**Status:** MISSING

**Evidence:** No funding statement included.

**Recommendation:** Add: 'This study received no external funding. The authors have no conflicts of interest to declare.'

---

## Priority Fixes (MISSING items)

1. **Item 14** (Methods): Whether clinical information and reference standard results were available to the performers/readers of the index test
   - Fix: Add: 'In the cross-validation framework, each model was trained on the training fold without access to the test fold labels, providing functional blinding equivalent to prospective evaluation.'

2. **Item 16** (Methods): How indeterminate index test or reference standard results were handled
   - Fix: Add: 'The dataset contained no indeterminate or missing index test results. All 569 specimens had complete morphometric feature sets and confirmed histopathological diagnoses.'

3. **Item 17** (Methods): How missing data on the index test and reference standard were handled
   - Fix: Add: 'No missing data were present in the feature matrix or reference standard labels. All 569 specimens had complete data for all 30 morphometric features.'

4. **Item 19** (Methods): Intended sample size and how it was determined
   - Fix: Add: 'The full dataset of 569 specimens was used without a priori sample size calculation, as this was a secondary analysis of an existing publicly available dataset. With 212 cases and 357 controls, the study had >95% power to detect an AUC of 0.95 vs. 0.50.'

5. **Item 20** (Results): Flow of participants, using a diagram
   - Fix: Add a STARD flow diagram showing: 569 eligible specimens -> 569 included -> 569 received all three index tests -> 569 included in final analysis. Note: no exclusions simplifies the diagram.

6. **Item 22** (Results): Distribution of severity of disease in those with the target condition
   - Fix: Add: 'The Wisconsin dataset does not include tumor staging or grading information. Severity distribution could not be assessed, which limits evaluation of spectrum bias.'

7. **Item 25** (Results): Any adverse events from performing the index test or the reference standard
   - Fix: Add: 'As this was a retrospective analysis of pre-computed features, no adverse events were associated with the index test application. Adverse events related to the original FNA procedures were not recorded in the dataset.'

8. **Item 28** (Other): Registration number and name of registry
   - Fix: Add: 'This study was not registered in a clinical trial or diagnostic accuracy study registry as it was a secondary analysis of a publicly available benchmark dataset.'

9. **Item 30** (Other): Sources of funding and other support; role of funders
   - Fix: Add: 'This study received no external funding. The authors have no conflicts of interest to declare.'

---

## Partial Items Requiring Strengthening

1. **Item 7** (Methods): On what basis potentially eligible participants were identified (such as symptoms, results from previous tests, inclusion in registry)
   - Fix: Add: 'Patients were identified based on clinical presentation with palpable breast masses referred for FNA cytology at the University of Wisconsin Hospital.'

2. **Item 9** (Methods): Whether participants formed a consecutive, random, or convenience series
   - Fix: Strengthen by stating explicitly: 'The dataset comprised a consecutive series of FNA specimens. No convenience sampling was applied.'

3. **Item 12** (Methods): Rationale for choosing the reference standard (if alternatives exist)
   - Fix: Add: 'Histopathological examination was chosen as the reference standard because it represents the highest-certainty method for distinguishing benign from malignant breast lesions.'

4. **Item 13** (Methods): Definition of and rationale for test positivity cut-offs or result categories, including whether the cut-off was pre-specified
   - Fix: Add: 'A probability threshold of 0.5 was used to dichotomize model predictions, consistent with the default classification boundary for binary classifiers.'

5. **Item 18** (Methods): Any analyses of variability in diagnostic accuracy, distinguishing pre-specified from exploratory
   - Fix: Clarify: 'The primary analysis was the pairwise DeLong comparison of AUCs (pre-specified). Feature importance analysis was exploratory.'

6. **Item 29** (Other): Where the full study protocol can be accessed
   - Fix: Add: 'The complete analysis protocol and reproducible code are available at [repository URL]. No formal study protocol document was prepared.'

---

*Generated by MedSci Skills check-reporting pipeline.*