# MedSci Skills Demo 2: BCG Vaccine Meta-Analysis

> **One R dataset, one script, a complete PRISMA-ready meta-analysis.**

## Demo Overview

| Item | Value |
|------|-------|
| Dataset | metafor::dat.bcg (Colditz et al., 1994) |
| Studies | 13 RCTs (1948-1980) |
| Participants | 357,347 total (191,064 vaccinated, 166,283 control) |
| Skills Used | 3 (meta-analysis, analyze-stats, make-figures) |
| Total Scripts | 1 R file |
| Output Files | 12 (CSV x3, PDF x4, PNG x4, MD x1) |
| Data Loading | `data(dat.bcg)` — zero download |

---

## Pipeline Flow

```
library(metafor); data(dat.bcg)     # 1 line — zero download
        |
        v
  [meta-analysis + analyze-stats]
  01_meta_analysis.R
    ├── Effect size computation (log RR)
    ├── Random-effects model (REML)
    ├── Heterogeneity (I², Q, tau², prediction interval)
    ├── Subgroup analysis (allocation method)
    ├── Meta-regression (absolute latitude, R² = 75.6%)
    ├── Publication bias (Egger's, Begg's, trim-and-fill)
    └── Sensitivity analysis (leave-one-out, influence diagnostics)
        |
        v
  [make-figures]
  → figures/forest_plot.png (300 dpi)
  → figures/funnel_plot.png
  → figures/funnel_trimfill.png
  → figures/bubble_plot.png
        |
        v
  → output/study_results.csv
  → output/summary_table.csv
  → output/metaregression_table.csv
  → Manuscript-ready results text
```

---

## Key Results

### Pooled Estimate

| Metric | Value |
|--------|-------|
| **Pooled RR** | **0.489 (95% CI: 0.344-0.696)** |
| Risk reduction | 51.1% (95% CI: 30.4%-65.6%) |
| I² | 92.2% |
| Q | 152.23 (p < 0.001) |
| tau² | 0.3132 |
| Prediction interval | 0.155-1.549 |

### Subgroup Analysis (Allocation Method)

| Subgroup | k | RR (95% CI) | I² |
|----------|---|-------------|-----|
| Random | 7 | 0.379 (0.221-0.650) | 89.9% |
| Alternate | 2 | 0.582 (0.335-1.011) | 82.0% |
| Systematic | 4 | 0.654 (0.323-1.324) | 86.4% |

### Meta-Regression

| Covariate | Coefficient | SE | p | R² |
|-----------|------------|-----|---|----|
| Absolute latitude | -0.0291 | 0.0072 | < 0.001 | 75.6% |

### Publication Bias

| Test | Result |
|------|--------|
| Egger's regression | t = -1.40, p = 0.189 (no asymmetry) |
| Begg's rank | tau = 0.026, p = 0.952 (no asymmetry) |
| Trim-and-fill | 1 study imputed, adjusted RR = 0.518 (0.365-0.736) |

---

## Output Files

```
demo/02_metafor_bcg/
├── 01_meta_analysis.R               # Full analysis pipeline
├── DEMO_LOG.md                      # This file
├── data/
│   └── bcg_raw.csv                  # Original dataset
├── figures/
│   ├── forest_plot.pdf              # Forest plot (vector)
│   ├── forest_plot.png              # Forest plot (300 dpi)
│   ├── funnel_plot.pdf              # Funnel plot
│   ├── funnel_plot.png
│   ├── funnel_trimfill.pdf          # Funnel plot + imputed studies
│   ├── funnel_trimfill.png
│   ├── bubble_plot.pdf              # Meta-regression (latitude)
│   └── bubble_plot.png
├── output/
│   ├── _analysis_outputs.md         # Output manifest
│   ├── study_results.csv            # Per-study RR + weights
│   ├── summary_table.csv            # Pooled estimates
│   └── metaregression_table.csv     # Regression coefficients
└── logs/
    └── step1_analysis.log
```

---

## What This Demo Proves

1. **Complete MA pipeline in one script**: From `data(dat.bcg)` to publication-ready forest plot, funnel plot, subgroup analysis, meta-regression, and publication bias assessment.

2. **Proper heterogeneity handling**: I² + Q + tau² + prediction interval. Doesn't just report I² in isolation — includes prediction interval to show clinical relevance of heterogeneity.

3. **Meta-regression with R²**: Latitude explains 75.6% of between-study variance — the classic finding that BCG is more effective at higher latitudes.

4. **Publication bias battery**: Egger's + Begg's + trim-and-fill. Three complementary tests, not just one.

5. **Sensitivity analysis**: Leave-one-out + influence diagnostics. No single study drives the result (all leave-one-out RRs remain < 1 and significant).

---

## Skills Demonstrated

| Skill | What It Did | Key Output |
|-------|-------------|------------|
| **meta-analysis** | Full RE model + subgroup + meta-regression + sensitivity | All statistical results |
| **analyze-stats** | Effect size computation, heterogeneity assessment | study_results.csv, summary_table.csv |
| **make-figures** | Forest plot, funnel plot, bubble plot (300 dpi) | 4 PDF + 4 PNG figures |

---

*Demo created: 2026-04-08*
*MedSci Skills: https://github.com/Aperivue/medsci-skills*
