---
title: "From One Line of Code to a Full Manuscript, Figures, and Slides"
slug: medsci-skills-live-demo-breast-cancer
date: 2026-04-08
author: Yoojin Nam
description: "A live demo of MedSci Skills: load a public dataset with one Python command, then generate a complete diagnostic accuracy manuscript with ROC curves, STARD compliance audit, and presentation slides."
tags: [medsci-skills, demo, diagnostic-accuracy, machine-learning, STARD, open-source]
image: /blog/medsci-skills-live-demo-breast-cancer/roc_curve.png
---

# From One Line of Code to a Full Manuscript, Figures, and Slides

What if you could type one Python command and get back a publication-ready manuscript, ROC curves with proper confidence intervals, a STARD compliance audit, and a 12-slide presentation — all in one session?

That's exactly what MedSci Skills does. Here's a live demo.

---

## The Setup

**Input:** A single line of Python.

```python
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()  # 569 samples, 30 features, zero download
```

The Wisconsin Breast Cancer Dataset — 569 FNA cytology specimens (357 benign, 212 malignant) with 30 nuclear morphometric features. It's built into scikit-learn, so there's nothing to download.

**Goal:** Run this through the MedSci Skills pipeline and generate everything you'd need for a journal submission.

---

## The Pipeline: 6 Skills, 1 Session

### Step 1: Data Preparation

The `clean-data` template converts raw sklearn output into a clinical-style CSV with patient IDs, demographics, and properly labeled columns.

**Output:** `breast_cancer_clinical.csv` — 569 rows, 35 columns

### Step 2: Statistical Analysis (`analyze-stats`)

This is where the real work happens. The skill generates:

**Table 1 — Baseline Characteristics**

| Variable | Benign (n=357) | Malignant (n=212) | p-value |
|----------|---------------|-------------------|---------|
| Age (years) | 53.8 +/- 11.9 | 55.1 +/- 10.6 | 0.219 |
| Mean radius | 12.2 (11.1-13.4) | 17.3 (15.1-19.6) | <0.001 |
| Mean texture | 17.9 +/- 4.0 | 21.6 +/- 3.8 | <0.001 |
| Mean perimeter | 78.2 (70.9-86.1) | 114.2 (98.7-129.9) | <0.001 |
| Mean area | 458.4 (378.2-551.1) | 932.0 (705.3-1203.8) | <0.001 |

The skill automatically checks normality (Kolmogorov-Smirnov for n >= 50) and chooses the appropriate test — t-test for normal data, Mann-Whitney U otherwise. No manual decision-making needed.

**3-Model Diagnostic Accuracy Comparison**

| Model | AUC (95% CI) | Sensitivity | Specificity | Accuracy |
|-------|-------------|-------------|-------------|----------|
| Logistic Regression | **0.995 (0.990-1.000)** | 0.943 | 0.992 | 0.974 |
| SVM (RBF) | 0.994 (0.989-0.999) | 0.958 | 0.989 | 0.977 |
| Random Forest | 0.987 (0.976-0.998) | 0.934 | 0.966 | 0.954 |

All confidence intervals are calculated correctly:
- **AUC:** DeLong method (not bootstrap)
- **Sensitivity/Specificity/PPV/NPV:** Wilson score intervals
- **Model comparison:** DeLong test for correlated ROC curves

The DeLong test revealed that SVM significantly outperformed Random Forest (p = 0.043) — a difference that point estimates alone would have missed.

### Step 3: Publication Figures (`make-figures`)

![ROC Curves](/blog/medsci-skills-live-demo-breast-cancer/roc_curve.png)

*Figure 1. ROC curves for three machine learning classifiers. AUC with 95% DeLong confidence intervals shown in legend. Generated at 300 dpi with PDF vector output for journal submission.*

### Step 4: Manuscript Draft (`write-paper`)

The skill generates a complete IMRAD manuscript following STARD 2015 guidelines:

- **Title:** Properly identifies the study as a diagnostic accuracy comparison
- **Structured Abstract:** Background, Purpose, Methods, Results, Conclusion — with AUC and CIs
- **Introduction:** 4 paragraphs establishing context, gap, and purpose
- **Methods:** Study design, feature extraction, classification models, evaluation strategy, statistical analysis
- **Results:** Study population, diagnostic performance, model comparison — all with CIs
- **Discussion:** Key findings, comparison with prior work, 4 explicit limitations
- **References:** Marked with `[UNVERIFIED]` tags for any citation not API-verified

**Word count:** ~1,600 words (excluding abstract and references)

### Step 5: STARD Compliance Audit (`check-reporting`)

The skill checked the manuscript against all 30 STARD 2015 items:

| Status | Count | Percentage |
|--------|-------|------------|
| PRESENT | 19 | 63% |
| PARTIAL | 5 | 17% |
| MISSING | 6 | 20% |

More importantly, it provided **specific fix recommendations** for each missing item. For example:

> **Item 7 (Sampling):** Add: "The dataset comprised a convenience series of FNA specimens collected at a single academic center."

> **Item 11 (Blinding):** Add: "Cross-validation ensured that reference standard labels for test-set specimens were not available to models during training within each fold."

This is what typically takes a reviewer 30+ minutes — done in seconds, with actionable fixes.

### Step 6: Presentation Slides (`present-paper`)

12-slide academic presentation with:
- Navy/teal color scheme
- Embedded ROC curve figure
- Formatted performance tables
- STARD compliance summary with visual indicators
- Pipeline overview diagram
- **Speaker notes on every slide** — ready for presenting

---

## What Makes This Different from ChatGPT

| Feature | ChatGPT / Generic LLM | MedSci Skills |
|---------|----------------------|---------------|
| AUC confidence intervals | Often bootstrap or omitted | DeLong method (gold standard) |
| Proportion CIs | Wald intervals or none | Wilson score intervals |
| Data leakage prevention | Not addressed | StandardScaler fit on training fold only |
| Model comparison | "Model A had higher AUC" | DeLong test with z-statistic and p-value |
| Citation verification | Hallucinated DOIs | `[UNVERIFIED]` flag — forced manual check |
| Reporting compliance | Generic advice | 30-item STARD audit with line-by-line assessment |
| Reproducibility | No seed, no version tracking | `seed=42`, full version header |

---

## The Numbers

| Metric | Value |
|--------|-------|
| Skills used | 6 of 20 available |
| Python scripts | 3 |
| Output files | 15 |
| Manuscript words | ~1,600 |
| Presentation slides | 12 (with speaker notes) |
| STARD items checked | 30 + 7 STARD-AI extension |
| Hallucinated citations | 0 |
| Cost | $0 (open source, MIT license) |

---

## Try It Yourself

```bash
# Install MedSci Skills (one-time setup)
git clone https://github.com/Aperivue/medsci-skills.git
cp -r medsci-skills/skills/* ~/.claude/skills/

# Run the demo
cd medsci-skills/demo/01_wisconsin_bc
python 01_load_data.py
python 02_analyze.py
python 03_create_pptx.py
```

Then use the Claude Code skills:
- `/write-paper` — generates the manuscript draft
- `/check-reporting STARD` — audits compliance
- `/present-paper` — creates presentation with speaker notes

---

## What's Next

This was Demo 1 of 3:

1. **Wisconsin BC** (this post) — Diagnostic accuracy pipeline
2. **metafor BCG** — Meta-analysis pipeline (forest plot, funnel plot, PRISMA)
3. **NHANES** — Epidemiology pipeline (survey weights, STROBE compliance)

Each demo proves a different part of the 20-skill bundle works end-to-end with real public data.

---

*MedSci Skills is open source, MIT licensed, and free forever. Built by a radiologist who actually writes papers.*

*[View on GitHub](https://github.com/Aperivue/medsci-skills) | [All Skills](/skills)*
