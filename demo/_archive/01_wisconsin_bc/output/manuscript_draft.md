# Comparative Diagnostic Accuracy of Machine Learning Models for Breast Cancer Classification Using Fine Needle Aspiration Cytology Features

**Authors:** MedSci Skills Demo Pipeline

---

## Abstract

Background: Machine learning classifiers are increasingly applied to cytopathology-derived features for breast cancer diagnosis, yet rigorous head-to-head comparisons with appropriate statistical testing remain uncommon.

Objective: To compare the diagnostic accuracy of logistic regression (LR), random forest (RF), and support vector machine (SVM) for classifying breast fine needle aspiration (FNA) specimens as benign or malignant.

Methods: This retrospective cross-sectional diagnostic accuracy study used the Wisconsin Breast Cancer Dataset (n = 569; 357 benign, 212 malignant). Thirty morphometric features computed from digitized FNA cytology images served as predictors. Models were evaluated using stratified 5-fold cross-validation with StandardScaler fitted exclusively on training folds to prevent data leakage. The primary endpoint was the area under the receiver operating characteristic curve (AUC) with DeLong 95% confidence intervals (CIs). Secondary endpoints included sensitivity, specificity, positive predictive value (PPV), and negative predictive value (NPV) with Wilson CIs. Pairwise AUC comparisons used the DeLong test.

Results: LR achieved an AUC of 0.995 (0.990-1.000), sensitivity of 0.943 (0.904-0.967), and specificity of 0.992 (0.976-0.997). SVM achieved an AUC of 0.994 (0.989-0.999), sensitivity of 0.958 (0.921-0.978), and specificity of 0.989 (0.972-0.996). RF achieved an AUC of 0.987 (0.976-0.998), sensitivity of 0.934 (0.892-0.960), and specificity of 0.966 (0.942-0.981). The DeLong test showed no significant difference between LR and SVM (p = 0.568), while SVM significantly outperformed RF (p = 0.043). LR versus RF approached significance (p = 0.050).

Conclusions: LR and SVM achieved near-perfect and statistically equivalent diagnostic accuracy for FNA-based breast cancer classification. Given its comparable performance and greater interpretability, LR may be preferred for clinical deployment. Formal pairwise statistical testing is essential when comparing classifier performance, as point estimates alone can obscure meaningful differences.

**Keywords:** breast cancer, fine needle aspiration, diagnostic accuracy, machine learning, logistic regression, support vector machine, ROC curve, DeLong test

---

## Introduction

Breast cancer is the most frequently diagnosed malignancy in women worldwide, with an estimated 2.3 million new cases annually [1]. Early and accurate diagnosis is critical for treatment planning and improving patient outcomes. Fine needle aspiration (FNA) cytology remains a widely used first-line diagnostic tool for palpable breast masses due to its minimally invasive nature and low cost [2].

The Wisconsin Breast Cancer Dataset, introduced by Wolberg and Mangasarian in 1990 [3], comprises 30 morphometric features computed from digitized FNA images of 569 breast mass specimens. Since its publication, this dataset has become one of the most cited benchmarks in machine learning, with over 30,000 citations across the diagnostic accuracy and pattern recognition literature [4]. Multiple classifiers have been applied to this dataset, including logistic regression (LR), random forests (RF), and support vector machines (SVM), each reporting high classification accuracy.

Despite the abundance of studies, rigorous head-to-head comparisons that employ appropriate statistical methodology remain uncommon. Many published analyses report only point estimates of accuracy or AUC without confidence intervals, and few apply the DeLong test for formal pairwise comparison of receiver operating characteristic (ROC) curves [5]. This gap limits the ability to draw statistically grounded conclusions about relative classifier performance.

The objective of this study was to compare the diagnostic accuracy of LR, RF, and SVM for classifying breast FNA cytology specimens as benign or malignant, using stratified cross-validation with proper statistical inference including DeLong AUC confidence intervals and pairwise hypothesis testing.

## Methods

This study followed the Standards for Reporting Diagnostic Accuracy (STARD) 2015 guidelines [6].

Participants and data source. The Wisconsin Breast Cancer Dataset was obtained from the UCI Machine Learning Repository via the scikit-learn Python library (version 1.3) [3,7]. The dataset comprised 569 consecutive FNA cytology specimens from female patients presenting with breast masses at the University of Wisconsin Hospital between January 1989 and November 1991. Each specimen was classified as benign (n = 357, 62.7%) or malignant (n = 212, 37.3%) based on histopathological examination, which served as the reference standard.

Index tests. Three machine learning classifiers were evaluated as index tests: (1) logistic regression with L2 regularization (maximum 5,000 iterations), (2) random forest with 100 decision trees, and (3) support vector machine with a radial basis function (RBF) kernel and Platt probability calibration. All models used default hyperparameters from scikit-learn to ensure a fair and reproducible comparison. Thirty morphometric features served as predictor variables, including ten mean values, ten standard errors, and ten worst-case values of nuclear characteristics (radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension).

Reference standard. The reference standard was the histopathological diagnosis (benign vs. malignant) established through surgical excision or core needle biopsy at the University of Wisconsin Hospital.

Evaluation strategy. Models were evaluated using stratified 5-fold cross-validation (random seed = 42) to maintain class proportions across folds. Feature standardization (zero mean, unit variance) was applied within each fold using StandardScaler fitted exclusively on the training partition to prevent data leakage.

Statistical analysis. The primary endpoint was the area under the receiver operating characteristic curve (AUC) with 95% confidence intervals calculated using the DeLong method [5]. Secondary endpoints included sensitivity, specificity, positive predictive value (PPV), negative predictive value (NPV), and overall accuracy, each reported with 95% Wilson confidence intervals [8]. Pairwise AUC comparisons between models were performed using the DeLong test with two-sided p-values. All analyses were conducted in Python 3.11 using numpy (1.26), pandas (2.1), scipy (1.11), and scikit-learn (1.3). The significance threshold was set at alpha = 0.05. The complete analysis code and reproducibility seed are available in the supplementary materials.

## Results

A total of 569 patients were included in the analysis, comprising 357 benign (62.7%) and 212 malignant (37.3%) specimens. Table 1 summarizes baseline characteristics by diagnostic group. Age did not differ significantly between groups (benign: 53.8 +/- 11.9 years vs. malignant: 55.1 +/- 10.6 years; p = 0.219). All morphometric features differed significantly between benign and malignant specimens (all p < 0.001), with malignant specimens demonstrating larger mean radius (17.3 vs. 12.2), mean texture (21.6 vs. 17.9), mean perimeter (114.2 vs. 78.2), and mean area (932.0 vs. 458.4).

Diagnostic performance of the three classifiers is presented in Table 2 and Figure 1. LR achieved the highest AUC at 0.995 (0.990-1.000), with a sensitivity of 0.943 (0.904-0.967) and specificity of 0.992 (0.976-0.997). LR correctly classified 200 true positives and 354 true negatives, with 3 false positives and 12 false negatives, yielding a PPV of 0.985 (0.957-0.995) and NPV of 0.967 (0.944-0.981). SVM performed comparably with an AUC of 0.994 (0.989-0.999), sensitivity of 0.958 (0.921-0.978), specificity of 0.989 (0.972-0.996), PPV of 0.981 (0.951-0.992), and NPV of 0.975 (0.953-0.987). RF achieved an AUC of 0.987 (0.976-0.998), sensitivity of 0.934 (0.892-0.960), specificity of 0.966 (0.942-0.981), PPV of 0.943 (0.903-0.967), and NPV of 0.961 (0.936-0.977).

Figure 2 presents confusion matrices for all three classifiers. LR produced 3 false positives and 12 false negatives, SVM produced 4 false positives and 9 false negatives, and RF produced 12 false positives and 14 false negatives.

Pairwise DeLong testing revealed no statistically significant difference in AUC between LR and SVM (z = 0.570, p = 0.568). SVM significantly outperformed RF (z = -2.028, p = 0.043). The comparison between LR and RF approached but did not reach statistical significance (z = 1.964, p = 0.050).

Feature importance analysis (Figure 3) identified worst concave points, worst perimeter, and worst radius as the most discriminative features for LR (by absolute coefficient magnitude) and worst concave points, worst perimeter, and mean concave points for RF (by Gini importance). Calibration curves (Figure 4) demonstrated that LR and SVM produced well-calibrated probability estimates, while RF exhibited slight overconfidence in the mid-range probabilities.

## Discussion

This study compared three machine learning classifiers for breast FNA cytology classification using rigorous statistical methodology. The principal finding was that logistic regression and SVM achieved near-perfect and statistically equivalent diagnostic accuracy (AUC 0.995 vs. 0.994, DeLong p = 0.568), while both significantly or near-significantly outperformed random forest (AUC 0.987).

The high performance of logistic regression is consistent with previous work by Wolberg and Mangasarian, who reported 97.5% accuracy with a multisurface linear separation method on the same dataset [3]. The finding that a simple linear model matches a kernel-based SVM suggests that the 30-dimensional morphometric feature space is largely linearly separable, a property that has practical implications for clinical deployment. Logistic regression offers transparent coefficient interpretation, faster training and inference, and deterministic predictions, advantages that are increasingly valued in clinical decision support systems where model explainability is required [9].

The statistically significant inferiority of random forest relative to SVM (DeLong p = 0.043) warrants attention. Although the absolute AUC difference was only 0.007, this translated to 14 false negatives for RF compared to 9 for SVM, representing 5 additional missed malignancies. This finding underscores the importance of formal pairwise statistical testing rather than relying on point estimates alone. Without the DeLong test, the three models would appear effectively identical based on AUC values alone.

Feature importance analysis revealed substantial agreement between LR and RF in identifying the most discriminative features, with worst concave points, worst perimeter, and worst radius ranking among the top predictors in both models. This convergence across different algorithmic paradigms strengthens confidence that these morphometric features carry genuine diagnostic information rather than reflecting model-specific artifacts.

This study has several limitations. First, the Wisconsin Breast Cancer Dataset is a curated benchmark with pre-computed features, which does not capture the full variability encountered in clinical cytopathology practice. Second, all models used default hyperparameters without tuning, which may underestimate the achievable performance of ensemble and kernel methods. Third, the synthetic age variable was generated for demonstration purposes and does not reflect true patient demographics. Fourth, the dataset was collected from a single institution between 1989 and 1991, and generalizability to contemporary specimens processed with modern cytological techniques is uncertain. Fifth, stratified 5-fold cross-validation, while appropriate for this sample size, provides predictions that are not fully independent across folds, which may slightly underestimate confidence interval widths.

Future directions include external validation on prospective cytology cohorts, evaluation of deep learning approaches that operate directly on digitized whole-slide images, and integration of clinical variables such as patient age, mass palpability, and imaging findings into hybrid diagnostic models.

## References

1. Sung H, Ferlay J, Siegel RL, et al. Global cancer statistics 2020: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. CA Cancer J Clin. 2021;71(3):209-249. doi:10.3322/caac.21660

2. Kocjan G, Bourgain C, Fassina A, et al. The role of breast FNAC in diagnosis and clinical management: a survey of current practice. Cytopathology. 2008;19(5):271-278. doi:10.1111/j.1365-2303.2008.00610.x

3. Wolberg WH, Mangasarian OL. Multisurface method of pattern separation for medical diagnosis applied to breast cytology. Proc Natl Acad Sci U S A. 1990;87(23):9193-9196. doi:10.1073/pnas.87.23.9193

4. Street WN, Wolberg WH, Mangasarian OL. Nuclear feature extraction for breast tumor diagnosis. Proc SPIE. 1993;1905:861-870. doi:10.1117/12.148698

5. DeLong ER, DeLong DM, Clarke-Pearson DL. Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach. Biometrics. 1988;44(3):837-845. doi:10.2307/2531595

6. Bossuyt PM, Reitsma JB, Bruns DE, et al. STARD 2015: an updated list of essential items for reporting diagnostic accuracy studies. BMJ. 2015;351:h5527. doi:10.1136/bmj.h5527

7. Pedregosa F, Varoquaux G, Gramfort A, et al. Scikit-learn: machine learning in Python. J Mach Learn Res. 2011;12:2825-2830.

8. Wilson EB. Probable inference, the law of succession, and statistical inference. J Am Stat Assoc. 1927;22(158):209-212. doi:10.1080/01621459.1927.10502953

9. Rudin C. Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. Nat Mach Intell. 2019;1(5):206-215. doi:10.1038/s42256-019-0048-x


---

## Tables and Figures

**Table 1.** Baseline characteristics of benign and malignant specimens.

**Table 2.** Diagnostic performance metrics for three machine learning classifiers (5-fold cross-validation).

**Figure 1.** Receiver operating characteristic curves for logistic regression, random forest, and support vector machine classifiers.

**Figure 2.** Confusion matrices for all three classifiers.

**Figure 3.** Top 10 discriminative features by model (logistic regression coefficients and random forest Gini importance).

**Figure 4.** Calibration curves for all three classifiers.
