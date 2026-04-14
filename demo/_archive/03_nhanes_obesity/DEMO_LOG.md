# MedSci Skills Demo 3: NHANES Obesity & Diabetes

> **Real CDC data, survey weights, a STROBE-ready cross-sectional study.**

## Demo Overview

| Item | Value |
|------|-------|
| Dataset | NHANES 2017-2018 (CDC) |
| Participants | 4,866 US adults (age 20+) |
| Research Question | Association between BMI category and diabetes (HbA1c >= 6.5%) |
| Skills Used | 4 (analyze-stats, make-figures, clean-data template, check-reporting/STROBE) |
| Total Scripts | 2 Python files |
| Output Files | 12 (CSV x3, PDF x4, PNG x4, MD x1) |
| Data Source | CDC XPT download (free, no registration) |

---

## Pipeline Flow

```
CDC NHANES 2017-2018 XPT files     # 3 files, free download
(DEMO_J + BMX_J + GHB_J)
        |
        v
  [clean-data template]
  01_download_data.py
    ├── Download 3 XPT files from CDC
    ├── Merge on SEQN (participant ID)
    ├── Recode variables (BMI categories, diabetes, demographics)
    └── data/nhanes_2017_2018.csv (n=4,940)
        |
        v
  [analyze-stats]
  02_analyze.py
    ├── Table 1: Demographics by BMI category
    ├── Survey-weighted diabetes prevalence
    ├── Logistic regression (unadjusted + adjusted)
    └── Subgroup analysis (age x BMI)
        |
        v
  [make-figures]
  → Figure 1: Prevalence bar chart with Wilson CIs
  → Figure 2: Adjusted OR forest plot
  → Figure 3: HbA1c distribution by BMI
  → Figure 4: Prevalence by age and BMI
```

---

## Key Results

### Diabetes Prevalence by BMI

| BMI Category | n | Unweighted | Survey-Weighted |
|-------------|---|------------|-----------------|
| Normal | 1,189 | 7.5% | 4.1% |
| Overweight | 1,593 | 13.9% | 8.8% |
| Obese | 2,084 | 19.9% | 14.7% |

### Adjusted Logistic Regression (key ORs)

| Variable | OR (95% CI) | p |
|----------|-------------|---|
| **Obese vs Normal** | **4.50 (4.49-4.51)** | **<0.001** |
| Overweight vs Normal | 2.06 (2.05-2.06) | <0.001 |
| Age (per year) | 1.06 (1.06-1.06) | <0.001 |
| Female vs Male | 0.70 (0.70-0.70) | <0.001 |
| NH Black vs NH White | 1.84 (1.83-1.84) | <0.001 |
| NH Asian vs NH White | 2.97 (2.96-2.97) | <0.001 |

---

## Output Files

```
demo/03_nhanes_obesity/
├── 01_download_data.py              # Data download + preprocessing
├── 02_analyze.py                    # Full analysis pipeline
├── DEMO_LOG.md                      # This file
├── data/
│   ├── DEMO_J.XPT                   # Raw demographics (CDC)
│   ├── BMX_J.XPT                    # Raw body measures (CDC)
│   ├── GHB_J.XPT                    # Raw glycohemoglobin (CDC)
│   └── nhanes_2017_2018.csv         # Prepared dataset
├── figures/
│   ├── prevalence_by_bmi.pdf        # Bar chart (vector)
│   ├── prevalence_by_bmi.png        # Bar chart (300 dpi)
│   ├── or_forest_plot.pdf           # OR forest plot
│   ├── or_forest_plot.png
│   ├── hba1c_distribution.pdf       # Density plot
│   ├── hba1c_distribution.png
│   ├── prevalence_by_age_bmi.pdf    # Grouped bar chart
│   └── prevalence_by_age_bmi.png
├── output/
│   ├── _analysis_outputs.md         # Output manifest
│   ├── table1.csv                   # Baseline characteristics
│   ├── prevalence_by_bmi.csv        # Weighted prevalence
│   └── regression_results.csv       # OR table
└── logs/
    ├── step1_download.log
    └── step2_analyze.log
```

---

## What This Demo Proves

1. **Real-world data pipeline**: Downloads actual CDC NHANES data (not toy datasets). Same workflow that thousands of epidemiologists use for published papers.

2. **Survey weight handling**: Demonstrates the critical difference between unweighted (14.9%) and survey-weighted (10.2%) prevalence — a common mistake in NHANES publications.

3. **Proper epidemiological analysis**: Table 1 with appropriate tests (ANOVA for continuous, chi-square for categorical), multivariable logistic regression with confounders, subgroup analysis by age.

4. **STROBE-compatible structure**: Research question, study design, participant flow, results with effect sizes and CIs — all following cross-sectional study reporting guidelines.

5. **Reproducibility**: Fixed seed, version-pinned output, XPT files cached locally for re-runs.

---

## Skills Demonstrated

| Skill | What It Did | Key Output |
|-------|-------------|------------|
| **analyze-stats** | Table 1 + weighted prevalence + logistic regression | table1.csv, regression_results.csv |
| **make-figures** | 4 publication-ready figures (300 dpi) | 4 PDF + 4 PNG |
| **clean-data** (template) | CDC XPT download, merge, recode | nhanes_2017_2018.csv |
| **check-reporting** | STROBE-compatible structure | (built into analysis flow) |

---

*Demo created: 2026-04-08*
*MedSci Skills: https://github.com/Aperivue/medsci-skills*
