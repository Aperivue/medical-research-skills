# Marketing Assets — Demo 2: BCG Meta-Analysis

## One-Liner
> One R dataset. One script. A complete meta-analysis with forest plot, funnel plot, meta-regression, and publication bias assessment — in under 60 seconds.

## Blog Post Hook
"We ran a complete meta-analysis of BCG vaccine efficacy — 13 RCTs, 357,000 participants — from `data(dat.bcg)` to publication-ready forest plot and funnel plot. The R script handles random-effects modeling (REML), heterogeneity assessment (I² = 92.2%), meta-regression (latitude explains 75.6% of variance), and a three-test publication bias battery. All figures at 300 dpi. Total time: less than a minute."

---

## X/Twitter Thread (5 tweets)

**Tweet 1:**
Meta-analysis from zero to publication-ready in under 60 seconds.

One R dataset (metafor::dat.bcg). One script. Full pipeline:
- Forest plot
- Funnel plot
- Meta-regression
- Publication bias assessment

All powered by MedSci Skills for Claude Code. [Thread]

**Tweet 2:**
The classic BCG vaccine MA (Colditz et al., 1994):
- 13 RCTs, 357K participants
- Pooled RR = 0.49 (95% CI: 0.34-0.70)
- BCG reduced TB risk by 51%

But I² = 92% — massive heterogeneity. So what explains it?

**Tweet 3:**
Meta-regression answer: absolute latitude explains 75.6% of between-study variance (p < 0.001).

BCG works better at higher latitudes. This is the textbook finding — and MedSci Skills reproduces it automatically with the correct bubble plot.

**Tweet 4:**
Publication bias? Three-test battery:
- Egger's: p = 0.189 (no asymmetry)
- Begg's: p = 0.952
- Trim-and-fill: 1 study imputed, adjusted RR = 0.52 (still significant)

Plus leave-one-out sensitivity: no single study drives the result.

**Tweet 5:**
20 free, MIT-licensed Claude Code skills for medical researchers.

From literature search to submission-ready manuscript — including proper statistical rigor that most AI tools skip.

github.com/Aperivue/medsci-skills

---

## LinkedIn Post

**From data(dat.bcg) to a complete meta-analysis in 60 seconds**

I just demonstrated MedSci Skills (Demo 2) using the classic BCG vaccine dataset from Colditz et al. (1994).

One R script produced:
- Random-effects model (REML) — pooled RR = 0.49, 95% CI: 0.34-0.70
- Forest plot and funnel plot at 300 dpi
- Heterogeneity assessment (I² = 92.2%) with prediction interval
- Meta-regression showing latitude explains 75.6% of variance
- Publication bias battery (Egger's + Begg's + trim-and-fill)
- Leave-one-out sensitivity analysis
- Manuscript-ready results paragraph

The key insight: it's not just about generating figures. It's about doing the statistics correctly — DeLong CIs, proper heterogeneity reporting, prediction intervals, multiple bias tests.

MedSci Skills is free, MIT-licensed, and built by a radiologist who actually runs meta-analyses.

github.com/Aperivue/medsci-skills

#MedicalResearch #MetaAnalysis #OpenSource #ClaudeCode

---

## Key Metrics for Marketing

| Metric | Value | Why It Matters |
|--------|-------|----------------|
| Studies | 13 RCTs | Reproducible, well-known dataset |
| Participants | 357,347 | Large scale, real clinical data |
| RR reduction | 51% | Clinically meaningful result |
| I² | 92.2% | Shows proper heterogeneity handling |
| R² (latitude) | 75.6% | Classic finding, reproduced automatically |
| Figures | 4 publication-ready | Forest + funnel + trim-fill + bubble |
| Bias tests | 3 complementary | More thorough than most published MAs |
| Script | 1 file | Simple, reproducible |

---

*Generated: 2026-04-08*
