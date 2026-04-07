# Statistical Methods — Section Templates for Radiology Papers

Reusable paragraph templates for the Statistical Analysis subsection of Methods. Adapt to the specific study; do not copy verbatim. All templates use past tense (Methods convention).

---

## 1. Descriptive Statistics

### Template
Continuous variables were expressed as mean +/- standard deviation or median (interquartile range [IQR]) depending on data distribution, which was assessed using the Shapiro-Wilk test. Categorical variables were reported as frequencies and percentages. Baseline characteristics were compared between groups using {the independent t test or Mann-Whitney U test} for continuous variables and {the chi-square test or Fisher exact test} for categorical variables, as appropriate.

### When to use each
- **Mean +/- SD**: normally distributed continuous data.
- **Median [IQR]**: skewed distributions, ordinal data, or small samples.
- **Shapiro-Wilk**: preferred normality test for n < 50; for larger samples, also consider visual inspection (Q-Q plot, histogram).

---

## 2. Comparison Tests

### Two-Group Continuous (Parametric)
Differences in {outcome} between {group A} and {group B} were compared using the independent-samples t test. For paired data (e.g., pre- vs post-intervention in the same subjects), the paired t test was used.

### Two-Group Continuous (Nonparametric)
Differences in {outcome} between groups were compared using the Mann-Whitney U test for independent samples or the Wilcoxon signed-rank test for paired samples.

### Categorical
The association between {variable 1} and {variable 2} was evaluated using the chi-square test. Fisher exact test was used when the expected cell count was less than 5.

### Multi-Group
Differences in {outcome} among {3+} groups were assessed using one-way analysis of variance (ANOVA) with post hoc pairwise comparisons using the Tukey honestly significant difference test. For non-normally distributed data, the Kruskal-Wallis test was used with post hoc Dunn test.

---

## 3. Diagnostic Accuracy

### Template
Diagnostic performance of {model/reader/test} was evaluated by calculating sensitivity, specificity, positive predictive value (PPV), negative predictive value (NPV), and accuracy with exact binomial 95% confidence intervals (CIs). The area under the receiver operating characteristic curve (AUC) was calculated with 95% CIs using the DeLong method. The operating point was determined by {maximizing the Youden index / using a pre-specified sensitivity threshold of X% / clinical consensus}. AUC values were compared between {model A} and {model B} using the DeLong test for correlated ROC curves.

### Sensitivity/Specificity at Fixed Threshold
At the pre-specified operating point of {threshold}, sensitivity and specificity were calculated with 95% CIs using the exact binomial method.

### Multi-Class
For multiclass classification, per-class sensitivity and specificity were calculated using a one-versus-rest approach. The overall performance was summarized using the macro-averaged AUC.

---

## 4. Inter-Rater Agreement

### Two Raters, Categorical
Inter-rater agreement between {rater 1} and {rater 2} was assessed using Cohen kappa coefficient. Kappa values were interpreted as follows: less than 0, poor; 0-0.20, slight; 0.21-0.40, fair; 0.41-0.60, moderate; 0.61-0.80, substantial; and 0.81-1.00, almost perfect agreement.

### Multiple Raters, Categorical
Inter-rater agreement among {N} raters was assessed using Fleiss kappa with 95% CIs.

### Continuous Measurements
Inter-rater reliability for continuous measurements was assessed using the intraclass correlation coefficient (ICC) with a two-way random-effects model for absolute agreement (ICC[2,1] for single measures, ICC[2,k] for average measures). ICC values were interpreted as: less than 0.50, poor; 0.50-0.75, moderate; 0.75-0.90, good; and greater than 0.90, excellent.

### Weighted Kappa (Ordinal)
For ordinal ratings, inter-rater agreement was assessed using the weighted kappa coefficient with quadratic weights.

---

## 5. Survival Analysis

### Template
Overall survival and progression-free survival were estimated using the Kaplan-Meier method and compared between groups using the log-rank test. Median survival times were reported with 95% CIs. Multivariable analysis was performed using the Cox proportional hazards model, reporting hazard ratios (HRs) with 95% CIs. The proportional hazards assumption was verified using Schoenfeld residuals. Variables with P < .10 on univariable analysis were included in the multivariable model.

---

## 6. Sample Size Justification

### Template (Diagnostic Accuracy)
Based on an expected AUC of {X} for the AI model with a null hypothesis AUC of 0.50, a minimum of {N} cases ({n} positive, {n} negative) were required to achieve 80% power at a two-sided significance level of .05, using the method described by Hanley and McNeil. Accounting for {X%} expected data loss, a target enrollment of {N} was set.

### Template (Comparison Study)
To detect a difference of {X} in {metric} between {group A} and {group B}, assuming a standard deviation of {Y}, a sample of {N} per group was required to achieve {80/90}% power at a two-sided alpha of .05 using a {two-sample t test / chi-square test}. This calculation was performed using {software}.

### Template (No Formal Power Analysis)
No formal sample size calculation was performed for this {retrospective / exploratory} study. All eligible patients during the study period were included.

---

## 7. Multiple Comparison Correction

### Bonferroni
To account for multiple comparisons across {N} primary endpoints, a Bonferroni-corrected significance threshold of P < {0.05/N} was applied.

### Holm
Multiple comparisons were adjusted using the Holm-Bonferroni sequential correction method.

### False Discovery Rate
For exploratory analyses involving {N} comparisons, the Benjamini-Hochberg procedure was used to control the false discovery rate at 5%.

### No Correction (with justification)
Given that the {subgroup / secondary} analyses were pre-specified and hypothesis-driven, no correction for multiple comparisons was applied; these results should be interpreted with appropriate caution.

---

## 8. Software Statement

### Template (Python-primary)
Statistical analyses were performed using Python {version} (Python Software Foundation) with the following packages: scipy {version} for statistical tests, scikit-learn {version} for machine learning metrics, statsmodels {version} for regression analyses, and lifelines {version} for survival analysis. Figures were generated using matplotlib {version} and seaborn {version}.

### Template (R-primary)
Statistical analyses were performed using R {version} (R Foundation for Statistical Computing, Vienna, Austria). Key packages included pROC for ROC analysis, survival and survminer for survival analysis, irr for inter-rater reliability, and ggplot2 for visualization.

### Template (Mixed)
Data preprocessing and model development were performed using Python {version} with PyTorch {version}. Statistical analyses were performed using R {version} with the pROC, irr, and survival packages. All statistical tests were two-sided, and P < .05 was considered to indicate a statistically significant difference.

### Significance Statement (append to any software template)
All statistical tests were two-sided, and P < .05 was considered to indicate a statistically significant difference unless otherwise specified.

---

## 9. Ethics Statement

### Template (Retrospective, Consent Waived)
This retrospective study was approved by the institutional review board of {institution name} (protocol no. {number}), and the requirement for written informed consent was waived owing to the retrospective nature of the study. All procedures were performed in accordance with the Declaration of Helsinki.

### Template (Prospective, Consent Obtained)
This prospective study was approved by the institutional review board of {institution name} (protocol no. {number}). Written informed consent was obtained from all participants prior to enrollment.

### Template (Multi-Institutional)
This study was approved by the institutional review boards of all participating institutions: {institution 1} (protocol no. {X}), {institution 2} (protocol no. {Y}), and {institution 3} (protocol no. {Z}). {Informed consent was obtained from all participants / The requirement for informed consent was waived at all sites}.

### Template (Educational Study, No Patient Data)
This study was reviewed by the institutional review board of {institution name} and was determined to be exempt from full review (protocol no. {number}) as it involved educational evaluation with no patient data.

---

## 10. AI Disclosure Statement

### Template (AI Used in Research Pipeline)
{Model name} ({version}, {company}) was used for {specific task, e.g., generating educational content, classifying images, extracting structured data}. The model was accessed via {API / local deployment} between {start date} and {end date}. Generation parameters included a temperature of {X} and a maximum token length of {Y}. {All outputs were reviewed by a board-certified radiologist (author initials, X years of experience) / All outputs underwent multi-stage quality assurance as described in Section 2.X}.

### Template (AI Used in Writing)
{Tool name} ({version}) was used for {grammar checking / language editing / code generation for statistical analysis}. All AI-assisted content was critically reviewed, edited, and verified by the authors, who take full responsibility for the final manuscript.

### Template (Study About AI, No AI in Writing)
No AI writing tools were used in the preparation of this manuscript. The AI models evaluated in this study are described in Section 2.X.
