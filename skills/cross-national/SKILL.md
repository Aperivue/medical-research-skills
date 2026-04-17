---
name: cross-national
description: End-to-end cross-national comparison study using KNHANES + NHANES (or other parallel surveys). Variable harmonization, parallel weighted analysis, and comparison tables.
triggers: cross-national, 한미 비교, Korea US comparison, KNHANES NHANES, 양국 비교, binational, cross-country, 비교연구
tools: Read, Write, Edit, Bash, Grep, Glob
model: opus
---

# Cross-National Comparison Study Skill

You are assisting a medical researcher in conducting a cross-national comparison study
using parallel nationally representative surveys (e.g., KNHANES for Korea, NHANES for the US).

## When to Use

- Researcher has a clinical question to compare across two countries
- KNHANES + NHANES data available (or other parallel survey pairs)
- Goal: produce a complete analysis with country-stratified results + comparison table

## Inputs

1. **Research question**: exposure → outcome association to compare across countries
2. **Korean data path**: KNHANES CSV file
3. **US data path**: NHANES CSV directory (multiple tables to merge)
4. **Harmonization table** (optional): CSV mapping variables across surveys
   - Default: replicate-study skill's `harmonization_knhanes_nhanes.csv`

## Reference Files

- `${SKILL_DIR}/references/cross_national_analysis_template.R` — R template for parallel analysis
- Harmonization table: `~/.claude/skills/replicate-study/references/harmonization_knhanes_nhanes.csv`
- Upstream:
  - `medsci-skills/skills/write-paper/references/paper_types/cross_national.md` — writing template
  - `medsci-skills/skills/analyze-stats/references/analysis_guides/survey_weighted.md`

## Workflow

### Phase 1: Study Definition

1. Confirm research question: Exposure → Outcome
2. Define variable coding for both countries:
   - Exposure: PHQ-9, BMI category, smoking, etc.
   - Outcome: diabetes, hypertension, mortality, etc.
   - Covariates: age, sex, education, income, smoking, alcohol, obesity, CVD
3. Check harmonization table for variable availability
4. Output: study protocol summary for user approval

### Phase 2: Data Preparation

**KNHANES (single CSV)**:
1. Load CSV, filter age ≥20 (or per protocol)
2. Derive variables using KNHANES coding:
   - Smoking: BS3_1 (1,2=current, 3=former, 8=never)
   - Alcohol: BD1_11 (2-6=frequent, 1=occasional, 8=never)
   - Obesity: HE_obe (≥4=obesity for BMI≥25 Asian cutoff)
   - PHQ-9: BP_PHQ_1~9, sum score, ≥10=depression
   - Diabetes: HE_glu≥126 | HE_HbA1c≥6.5 | DE1_dg=1
   - CVD: DI4_dg=1 | DI5_dg=1 | DI6_dg=1
3. Set survey design: svydesign(id=~psu, strata=~kstrata, weights=~wt_itvex, nest=TRUE)

**NHANES (multiple CSVs)**:
1. Load and merge tables by SEQN (DEMO_J, DPQ_J, GHB_J, BIOPRO_J, BMX_J, SMQ_J, ALQ_J, DIQ_J, MCQ_J, BPQ_J)
2. Derive variables using NHANES coding:
   - Smoking: SMQ020 + SMQ040 (100 cigs + now smoke)
   - Alcohol: ALQ121 (past 12 mo frequency → categories)
   - Obesity: BMXBMI ≥30 (WHO cutoff, NOT Asian)
   - PHQ-9: DPQ010~DPQ090, sum score, ≥10=depression
   - Diabetes: LBXSGL≥126 | LBXGH≥6.5 | DIQ010=="Yes" (CRITICAL: LBXSGL not LBXSGLU)
   - CVD: MCQ160B=="Yes" (CHF) | MCQ160C=="Yes" (CHD) | MCQ160D=="Yes" (angina) | MCQ160E=="Yes" (MI)
3. Set survey design: svydesign(id=~SDMVPSU, strata=~SDMVSTRA, weights=~WTMECPRP, nest=TRUE)

### Phase 3: Parallel Analysis

For EACH country independently:
1. **Table 1**: Baseline characteristics by exposure (weighted counts + percentages)
2. **Main analysis**: Sequential logistic regression models
   - Model 1 (unadjusted)
   - Model 2 (age + sex)
   - Model 3 (fully adjusted: + education, income, smoking, alcohol, obesity, CVD)
3. **Subgroup analyses**: By sex, age group, education, income, alcohol, smoking, CVD, obesity
4. **Dose-response** (if applicable): RCS with 3 knots

### Phase 4: Cross-National Comparison Table

Generate a side-by-side comparison:

| Analysis | Korea wOR (95% CI) | US wOR (95% CI) | Direction Agreement |
|----------|-------------------|-----------------|---------------------|
| Overall (fully adjusted) | ... | ... | ✓/✗ |
| Male | ... | ... | |
| Female | ... | ... | |
| ... | ... | ... | |

### Phase 5: Output Files

```
{working_dir}/
├── cross_national_report.md    — Study summary + comparison tables
├── variable_mapping.csv        — Variable mapping with match status
├── analysis_korea.R            — KNHANES analysis (self-contained)
├── analysis_us.R               — NHANES analysis (self-contained)
├── results/
│   ├── table1_korea.csv
│   ├── table1_us.csv
│   ├── main_results_comparison.csv
│   └── subgroup_comparison.csv
└── manuscript_draft/           — Optional: Methods + Results draft
    ├── methods_draft.md
    └── results_draft.md
```

## Critical Rules

1. **NEVER pool data across countries**. Each country analyzed with its own survey design.
2. **Country-specific BMI cutoffs**: Korea ≥25 (Asian), US ≥30 (WHO).
3. **Country-specific income**: KNHANES quartile, NHANES PIR → harmonize to binary.
4. **Weighted analysis mandatory**: Both KNHANES and NHANES are complex surveys.
5. **Document all harmonization decisions**: What matches, what needed recoding, what differs.
6. **Same analytic approach**: Identical model specifications for both countries for fair comparison.

## KNHANES Variable Coding Reference (validated via Joo 2026 replication)

| Variable | Raw Var | Coding |
|----------|---------|--------|
| Smoking | BS3_1 | 1,2=Current; 3=Former; 8=Never |
| Alcohol | BD1_11 | 2-6=Frequent (current drinker); 1=Occasional (past-year abstainer); 8=Never |
| Obesity | HE_obe | 1-3=Normal; 4-6=Obesity (BMI≥25) |
| Depression | BP_PHQ_1~9 | Sum ≥10 = depression |
| Diabetes | HE_glu, HE_HbA1c, DE1_dg | FPG≥126 or HbA1c≥6.5 or DE1_dg=1 |
| CVD | DI4_dg, DI5_dg, DI6_dg | Any = 1 → CVD yes |
| Education | edu | 1-3=Non-college; 4=College |
| Income | incm | 1-3=Bottom 80%; 4=Top 20% |
| Survey design | kstrata, psu, wt_itvex | strata, cluster, weight |

## NHANES Variable Coding Reference (validated via Joo 2026 cross-national)

**CRITICAL**: NHANES data downloaded via R `nhanesA` package uses TEXT LABELS, not numeric codes.

| Variable | Raw Var | Text Labels → Numeric |
|----------|---------|----------------------|
| PHQ-9 items | DPQ010~DPQ090 | "Not at all"→0, "Several days"→1, "More than half the days"→2, "Nearly every day"→3 |
| Sex | RIAGENDR | "Male" / "Female" (NOT 1/2) |
| Smoking (100 cigs) | SMQ020 | "Yes" / "No" |
| Smoking (now) | SMQ040 | "Every day" / "Some days" / "Not at all" |
| Alcohol freq | ALQ121 | Text labels (see below) |
| Alcohol ever | ALQ111 | "Yes" / "No" |
| Education | DMDEDUC2 | 5 text levels (see SKILL.md Phase 2) |
| Diabetes dx | DIQ010 | "Yes" / "No" / "Borderline" |
| CVD (CHF) | MCQ160B | "Yes" / "No" / "Don't know" |
| CVD (CHD) | MCQ160C | "Yes" / "No" / "Don't know" |
| CVD (angina) | MCQ160D | "Yes" / "No" / "Don't know" |
| Fasting glucose | LBXSGL (BIOPRO_J) | Numeric (mg/dL) — note: NOT LBXSGLU |
| HbA1c | LBXGH (GHB_J) | Numeric (%) |
| BMI | BMXBMI (BMX_J) | Numeric (kg/m²) |
| Weight | WTMEC2YR (single-cycle) or WTMECPRP (pre-pandemic pooled) | Numeric |
| Strata | SDMVSTRA | Numeric |
| PSU | SDMVPSU | Numeric |

### ALQ121 Text Label Mapping (Alcohol Frequency)
- Frequent (current drinker): Any specific frequency except "Never in the last year"
- Occasional (past-year abstainer): "Never in the last year"
- Never (lifetime non-drinker): ALQ111 == "No" (ALQ121 will be NA)
