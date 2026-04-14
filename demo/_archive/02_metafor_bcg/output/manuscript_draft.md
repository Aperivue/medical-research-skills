# Efficacy of BCG Vaccination for Prevention of Tuberculosis: A Meta-Analysis of Randomized Controlled Trials

MedSci Skills Demo Author^1^

^1^ Medical Imaging Research Lab, Department of Radiology

*Note: This manuscript was generated as a teaching demonstration using the metafor::dat.bcg dataset (Colditz et al., 1994). It is not intended for peer-reviewed publication.*
## Abstract

**Background:** Bacillus Calmette-Guerin (BCG) vaccination is the most widely used vaccine worldwide for the prevention of tuberculosis (TB), yet its protective efficacy varies substantially across studies and geographic regions. We conducted a meta-analysis of randomized controlled trials to estimate the overall efficacy of BCG vaccination and to explore sources of heterogeneity.

**Methods:** Thirteen randomized controlled trials evaluating BCG vaccine efficacy for TB prevention were analyzed (Colditz et al., 1994 dataset). Risk ratios (RR) were computed from 2x2 tables. A random-effects model using restricted maximum likelihood (REML) estimation was fitted. Heterogeneity was assessed using the Q statistic, I-squared, and tau-squared. Subgroup analysis was performed by allocation method, and meta-regression examined the effect of absolute latitude. Publication bias was evaluated using Egger's regression test, Begg's rank correlation test, and trim-and-fill analysis. Leave-one-out sensitivity analysis assessed the robustness of findings.

**Results:** Thirteen RCTs (published 1948-1980) comprising 191,064 vaccinated and 166,283 control participants were included. The pooled risk ratio was 0.489 (95% CI: 0.344-0.696), indicating BCG vaccination reduced TB risk by approximately 51%. Substantial heterogeneity was observed (I-squared = 92.2%, tau-squared = 0.3132). Meta-regression identified absolute latitude as a significant moderator (coefficient = -0.0291, p <0.001), explaining 75.6% of between-study variance. No significant publication bias was detected (Egger's p = 0.189). All leave-one-out estimates remained statistically significant.

**Conclusion:** BCG vaccination significantly reduces the risk of tuberculosis, with greater efficacy observed in trials conducted at higher latitudes. The pronounced geographic heterogeneity suggests that environmental factors, particularly exposure to non-tuberculous mycobacteria at lower latitudes, may attenuate vaccine efficacy.

## Introduction

Tuberculosis (TB) remains one of the leading infectious causes of morbidity and mortality worldwide, with an estimated 10.6 million new cases and 1.3 million deaths annually (WHO, 2023). Bacillus Calmette-Guerin (BCG), an attenuated strain of *Mycobacterium bovis*, has been used as a vaccine against TB since 1921 and remains the only licensed TB vaccine, administered to over 100 million children annually worldwide.

Despite its widespread use, the reported efficacy of BCG vaccination varies dramatically across studies, ranging from no protection to over 80% risk reduction. This variability has been the subject of extensive investigation, with several hypotheses proposed to explain the heterogeneity, including differences in BCG strains, study populations, exposure to environmental non-tuberculous mycobacteria (NTM), and study methodology.

The landmark meta-analysis by Colditz et al. (1994) systematically reviewed the evidence from randomized controlled trials (RCTs) and demonstrated that geographic latitude was a key predictor of vaccine efficacy. This observation is consistent with the hypothesis that prior sensitization by NTM, which are more prevalent in tropical and subtropical regions, may reduce the incremental benefit of BCG vaccination.

The objective of this meta-analysis is to quantify the overall protective efficacy of BCG vaccination against TB based on evidence from RCTs, assess the degree and sources of heterogeneity among studies, and evaluate the robustness of findings through sensitivity and publication bias analyses. This analysis serves as a teaching demonstration of meta-analytic methodology using the well-characterized Colditz et al. (1994) dataset.

## Methods

### Data Source

This analysis used the dat.bcg dataset from the metafor R package (Viechtbauer, 2010), which contains data from 13 RCTs of BCG vaccine efficacy reported by Colditz et al. (1994). Each study provided 2x2 contingency tables of TB cases and non-cases in vaccinated and control groups, along with study-level covariates including year of publication, allocation method, and absolute latitude of the study location.

### Eligibility Criteria

The original systematic review by Colditz et al. (1994) included RCTs that: (1) randomized participants to BCG vaccination or control; (2) reported TB incidence as an outcome; and (3) had a minimum follow-up period. As this is a re-analysis of a curated dataset, no additional screening was performed.

### Effect Size Calculation

Log risk ratios (log RR) and their sampling variances were computed from the 2x2 tables using the escalc() function in metafor. The risk ratio quantifies the relative risk of developing TB in the vaccinated group compared to the control group, where RR < 1 indicates a protective effect.

### Statistical Model

A random-effects model was fitted using restricted maximum likelihood (REML) estimation via the rma() function in metafor. The random-effects model accounts for both within-study sampling variability and between-study heterogeneity, yielding a pooled effect estimate that represents the average true effect across the population of studies.

### Heterogeneity Assessment

Between-study heterogeneity was assessed using:
- Cochran's Q statistic with its p-value
- I-squared statistic, quantifying the proportion of total variability due to between-study heterogeneity
- Tau-squared, the estimated between-study variance
- A 95% prediction interval, indicating the expected range of true effects in future studies

### Subgroup Analysis

Subgroup analysis was performed according to the method of treatment allocation (random, alternate, or systematic assignment). Separate random-effects models were fitted for each subgroup to assess whether allocation method was associated with differences in estimated vaccine efficacy.

### Meta-Regression

Mixed-effects meta-regression was conducted with absolute latitude of the study location as the moderator variable. This analysis tested the hypothesis that studies conducted at higher latitudes (further from the equator) would demonstrate greater BCG efficacy, consistent with the NTM exposure hypothesis. The proportion of heterogeneity explained (R-squared) was reported.

### Publication Bias Assessment

Publication bias was evaluated using:
- Visual inspection of funnel plots (standard error vs. log RR)
- Egger's regression test for funnel plot asymmetry
- Begg and Mazumdar's rank correlation test
- Duval and Tweedie's trim-and-fill method, which estimates the number of potentially missing studies and provides an adjusted pooled estimate

### Sensitivity Analysis

Leave-one-out analysis was performed by iteratively removing each study and re-fitting the model to assess the influence of individual studies on the pooled estimate. Studies with externally standardized residuals exceeding |2| were flagged as potentially influential.

### Software

All analyses were conducted in R (version 4.x) using the metafor package (version 4.x) and the meta package. Significance was defined as p < 0.05. This manuscript draft was generated using MedSci Skills (write-paper).

## Results

### Study Characteristics

A total of 13 randomized controlled trials published between 1948 and 1980 were included, comprising 191,064 vaccinated and 166,283 control participants (357,347 total). Studies were conducted across diverse geographic locations, with absolute latitudes ranging from 13 to 55 degrees. Treatment allocation methods included random assignment (k = 7), alternate assignment (k = 2), and systematic assignment (k = 4).

### Overall Efficacy

The pooled risk ratio under the random-effects model was 0.489 (95% CI: 0.344-0.696; p < 0.001), indicating that BCG vaccination reduced the risk of tuberculosis by approximately 51% (95% CI: 30%-66%) (**Figure 1**). The 95% prediction interval ranged from 0.155 to 1.549, suggesting that while the average effect is protective, the true effect in a new study setting could potentially include no benefit.

### Heterogeneity

Substantial heterogeneity was observed among the included trials. The Q statistic was 152.23 (df = 12, p < 0.001), and the I-squared statistic was 92.2%, indicating that approximately 92% of the total variability in effect estimates was attributable to between-study heterogeneity rather than sampling error. The estimated between-study variance (tau-squared) was 0.3132.

### Subgroup Analysis by Allocation Method

Studies using random allocation (k = 7) showed the greatest protective effect (RR = 0.379, 95% CI: 0.221-0.65), followed by alternate allocation (k = 2; RR = 0.582, 95% CI: 0.335-1.011) and systematic allocation (k = 4; RR = 0.654, 95% CI: 0.323-1.324). High residual heterogeneity persisted within all subgroups (I-squared: 82%-89.9%).

### Meta-Regression: Latitude Effect

Meta-regression revealed that absolute latitude was a highly significant moderator of vaccine efficacy (coefficient = -0.0291, SE = 0.0072, p <0.001). The negative coefficient indicates that for each degree increase in absolute latitude, the log risk ratio decreased by 0.029, reflecting greater vaccine efficacy at higher latitudes. Latitude explained 75.6% of the between-study variance (R-squared = 0.756) (**Figure 3**).

### Publication Bias

Visual inspection of the funnel plot showed no obvious asymmetry (**Figure 2**). Egger's regression test (p = 0.189) and Begg's rank correlation test (p = 0.952) both indicated no statistically significant evidence of publication bias. Trim-and-fill analysis identified 1 potentially missing study on the right side of the funnel plot. The adjusted pooled RR after imputation was 0.518 (95% CI: 0.365-0.736), which remained statistically significant and was minimally changed from the unadjusted estimate.

### Sensitivity Analysis

Leave-one-out analysis demonstrated that the pooled estimate was robust to the exclusion of any single study. The range of pooled RR estimates across all leave-one-out iterations was 0.452 to 0.533, all remaining statistically significant. No studies had externally standardized residuals exceeding |2|, suggesting no unduly influential individual studies.

## Discussion

This meta-analysis of 13 RCTs confirms that BCG vaccination provides significant protection against tuberculosis, with an overall risk reduction of approximately 51%. However, the pronounced heterogeneity among trials (I-squared = 92.2%) underscores the complexity of BCG vaccine efficacy across different settings.

### The Latitude Effect

The most striking finding is the strong association between absolute latitude and vaccine efficacy, with latitude explaining over 75% of between-study variance. This geographic gradient is consistent with the prevailing hypothesis that environmental exposure to non-tuberculous mycobacteria (NTM) in tropical and subtropical regions confers partial cross-reactive immunity to mycobacterial antigens, thereby reducing the incremental benefit of BCG vaccination (Fine, 1995). In contrast, populations at higher latitudes, with less NTM exposure, derive greater benefit from vaccination.

This finding has important implications for global TB control strategies. In equatorial regions where BCG appears least effective, alternative vaccination strategies or novel TB vaccines may be needed. Conversely, the strong protective effect observed at higher latitudes supports the continued use of BCG in these settings.

### Heterogeneity Considerations

Beyond latitude, residual heterogeneity persisted even after meta-regression, suggesting additional unmeasured moderators. Potential sources include differences in BCG strains (Danish, Pasteur, Tokyo, Glaxo), dosing regimens, TB epidemiology, diagnostic criteria for TB, and duration of follow-up. The wide prediction interval (0.155-1.549) reinforces that BCG efficacy cannot be assumed to be uniform across all settings.

Subgroup analysis by allocation method showed that randomly allocated trials reported greater efficacy than those using alternate or systematic assignment. This may reflect methodological quality, as true randomization better controls for confounding, though the small number of studies in each subgroup limits firm conclusions.

### Publication Bias

Reassuringly, multiple tests for publication bias yielded non-significant results, and trim-and-fill analysis produced only minimal adjustment to the pooled estimate. This suggests that the body of evidence is not substantially distorted by selective reporting, although the small number of studies limits the power of these tests.

### Limitations

Several limitations warrant consideration. First, the included trials span over three decades (1948-1980), during which TB epidemiology, diagnostic methods, and BCG manufacturing practices evolved substantially. Second, this analysis relies on aggregate study-level data rather than individual patient data, precluding examination of within-study effect modification by age, sex, or TB strain. Third, the dataset is a curated teaching resource, and a contemporary systematic review would require updated literature searches and potentially yield additional eligible studies. Fourth, the small number of studies (k = 13) limits the power of meta-regression and subgroup analyses, and results should be interpreted with caution. Finally, this analysis uses the standard frequentist framework; Bayesian approaches could provide complementary insights, particularly given the small number of studies.

### Implications for Practice and Research

Despite these limitations, the consistent finding of BCG efficacy across multiple analytical approaches has important implications. For public health policy, BCG vaccination remains a valuable tool for TB prevention, particularly in non-tropical settings. For research, the latitude effect suggests that future vaccine trials should carefully consider geographic location and baseline NTM exposure as potential effect modifiers. The development of next-generation TB vaccines that overcome the limitations of BCG in tropical regions remains a global health priority.

## Conclusion

BCG vaccination significantly reduces the risk of tuberculosis by approximately 51% based on pooled evidence from 13 randomized controlled trials. Vaccine efficacy varies substantially by geographic latitude, with studies at higher latitudes demonstrating greater protection. Absolute latitude explains over 75% of between-study heterogeneity, supporting the hypothesis that environmental mycobacterial exposure attenuates BCG efficacy. These findings inform global vaccination strategies and highlight the need for next-generation TB vaccines effective across all geographic settings.

## References

1. Colditz GA, Brewer TF, Berkey CS, et al. Efficacy of BCG vaccine in the prevention of tuberculosis: meta-analysis of the published literature. *JAMA*. 1994;271(9):698-702.

2. Fine PEM. Variation in protection by BCG: implications of and for heterologous immunity. *Lancet*. 1995;346(8986):1339-1345.

3. Viechtbauer W. Conducting meta-analyses in R with the metafor package. *Journal of Statistical Software*. 2010;36(3):1-48.

4. Higgins JPT, Thompson SG, Deeks JJ, Altman DG. Measuring inconsistency in meta-analyses. *BMJ*. 2003;327(7414):557-560.

5. Egger M, Davey Smith G, Schneider M, Minder C. Bias in meta-analysis detected by a simple, graphical test. *BMJ*. 1997;315(7109):629-634.

6. Duval S, Tweedie R. Trim and fill: a simple funnel-plot-based method of testing and adjusting for publication bias in meta-analysis. *Biometrics*. 2000;56(2):455-463.

7. Begg CB, Mazumdar M. Operating characteristics of a rank correlation test for publication bias. *Biometrics*. 1994;50(4):1088-1101.

8. World Health Organization. *Global Tuberculosis Report 2023*. Geneva: WHO; 2023.

9. Mangtani P, Abubakar I, Ariti C, et al. Protection by BCG vaccine against tuberculosis: a systematic review of randomized controlled trials. *Clinical Infectious Diseases*. 2014;58(4):470-480.

10. Trunz BB, Fine P, Dye C. Effect of BCG vaccination on childhood tuberculous meningitis and miliary tuberculosis worldwide: a meta-analysis and assessment of cost-effectiveness. *Lancet*. 2006;367(9517):1173-1180.

## Figure Legends

**Figure 1.** Forest plot of risk ratios for BCG vaccine efficacy in the prevention of tuberculosis. Each horizontal line represents the risk ratio and 95% confidence interval for an individual study. The diamond represents the pooled risk ratio from the random-effects model (REML). Risk ratios less than 1.0 favor BCG vaccination.

**Figure 2.** Funnel plot of standard error versus log risk ratio for assessment of publication bias. The vertical line indicates the pooled effect estimate. The dashed lines represent the pseudo-95% confidence interval. Open circles represent original studies; filled circles represent imputed studies from trim-and-fill analysis.

**Figure 3.** Bubble plot from meta-regression of log risk ratio against absolute latitude. Each bubble is proportional to the inverse of the study's sampling variance (i.e., study precision). The regression line and 95% confidence band illustrate the significant negative relationship between latitude and risk ratio, indicating greater BCG efficacy at higher latitudes.


---
*Generated: 2026-04-08 | MedSci Skills Demo 2 — write-paper skill*
