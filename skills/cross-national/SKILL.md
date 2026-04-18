---
name: cross-national
description: End-to-end cross-national comparison study using KNHANES + NHANES + CHNS (or other parallel surveys). Variable harmonization, parallel weighted analysis, and comparison tables. Supports 2-country (KR+US) and 3-country (KR+US+CN) designs.
triggers: cross-national, 한미 비교, Korea US comparison, KNHANES NHANES, 양국 비교, binational, cross-country, 비교연구, 3국 비교, CHNS, 한미중
tools: Read, Write, Edit, Bash, Grep, Glob
model: opus
---

# Cross-National Comparison Study Skill

You are assisting a medical researcher in conducting a cross-national comparison study
using parallel nationally representative surveys (e.g., KNHANES for Korea, NHANES for the US, CHNS for China).

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

- Harmonization table: `medsci-skills/skills/replicate-study/references/harmonization_knhanes_nhanes.csv`
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
   - HTN: BPXOSY3≥140 | BPXODI3≥90 | BPQ020=="Yes"
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

### Additional KNHANES Variables (validated via LE8-Asthma replication)

| Variable | Raw Var | Coding |
|----------|---------|--------|
| Asthma | DJ2_dg | 0=No, 1=Yes (physician dx), 9=Don't know → exclude |
| Asthma treatment | DJ2_pt | 0=No, 1=Yes, 8=N/A, 9=Don't know |
| Sleep (2017-18) | BP16_11/12/13/14 | **Clock times, NOT hours!** 11=bed hour, 12=bed min, 13=wake hour, 14=wake min. Calculate: duration = wake_time - bed_time (handle midnight crossing). 99=Don't know→NA |
| Sleep (2017-18 weekend) | BP16_21/22/23/24 | Same format as weekday |
| Sleep (2019-20) | BP16_1/2 | Direct sleep hours (weekday/weekend). 99=Don't know→NA |
| PA aerobic | pa_aerobic | 0=Doesn't meet, 1=Meets guidelines. **Note: values are 0/1, NOT 1/2** |
| HTN treatment | DI1_pr | 1=Yes, 0=No (currently treating hypertension) |
| Dyslipidemia tx | DI3_pr | 1=Yes, 0=No (if available) |
| Non-HDL chol | HE_chol - HE_HDL_st2 | Derived: total cholesterol minus HDL |

### Additional NHANES Variables (validated via LE8-Asthma replication)

| Variable | Raw Var | Coding |
|----------|---------|--------|
| Asthma | MCQ010 | "Yes" / "No" (ever told by doctor) |
| Sleep hours | SLD012 | Numeric (hours/night on weekdays) |
| BP treatment | BPQ020 | "Yes" / "No" (told by doctor, high BP) |
| Cholesterol treatment | BPQ100D | "Yes" / "No" (taking cholesterol Rx) |
| PA vigorous work | PAQ605/PAQ610/PAD615 | Yes/No, days/week, min/day |
| PA moderate work | PAQ620/PAQ625/PAD630 | Yes/No, days/week, min/day |
| PA walk/bike | PAQ635/PAQ640/PAD645 | Yes/No, days/week, min/day |
| PA vigorous rec | PAQ665/PAQ670/PAD675 | Yes/No, days/week, min/day |
| PA moderate rec | PAQ650/PAQ655/PAD660 | Yes/No, days/week, min/day |
| Dietary fiber | DR1TFIBE (DR1TOT_J) | Numeric (grams, day 1 recall) |
| Dietary sodium | DR1TSODI (DR1TOT_J) | Numeric (mg) |
| Dietary sat fat | DR1TSFAT (DR1TOT_J) | Numeric (grams) |
| Total energy | DR1TKCAL (DR1TOT_J) | Numeric (kcal) |
| Total sugars | DR1TSUGR (DR1TOT_J) | Numeric (grams) |
| Non-HDL chol | LBXTC - LBDHDD | Derived: TCHOL_J minus HDL_J |

## CHNS Variable Coding Reference (validated via 3-country batch)

**Data source**: cpc.unc.edu/projects/china (free registration)
**Biomarker wave**: 2009 only (N=9,549). Other variables available 1989-2015.
**Survey design**: No formal weights. Use `svydesign(id=~COMMID, weights=~1)` or cluster-robust SE.

### Key Files and Merge Strategy

| File | Key Variables | Join Key |
|------|--------------|----------|
| mast_pub_12 | IDind, GENDER (1=M/2=F), WEST_DOB_Y (birth year) | IDind |
| pexam_00 | HEIGHT, WEIGHT, U10 (waist), SYSTOL1-3, DIASTOL1-3, U22 (HBP dx), U24 (HBP meds), U24A (DM dx), U25 (ever smoked), U27 (still smokes), U40 (alcohol), U41 (freq), U48A (self-health), COMMID | IDind + filter WAVE==2009 |
| biomarker_09 | GLUCOSE_MG, HbA1c, TC_MG, TG_MG, HDL_C_MG, LDL_C_MG, HS_CRP, HGB, WBC, ALT, CRE_MG | IDind |
| educ_12 | A12 (education 0-6) | IDind + filter WAVE==2009 |
| indinc_10 | indwage (yuan, continuous → quartiles) | IDind + filter wave==2009 |

### Variable Coding

| Variable | Raw Var | Coding | Notes |
|----------|---------|--------|-------|
| Sex | GENDER | 1=Male, 2=Female | Same as KNHANES/NHANES |
| Age | WEST_DOB_Y | age = wave_year - WEST_DOB_Y | Integer truncation |
| BMI | HEIGHT, WEIGHT | WEIGHT / (HEIGHT/100)^2 | **Obesity: BMI ≥ 28 (WGOC, NOT 25 or 30)** |
| Waist | U10 | cm, direct measurement | **Central obesity: ≥90M / ≥80F (IDF-Asian)** |
| SBP | SYSTOL1-3 | mean(SYSTOL1, SYSTOL2, SYSTOL3) | 3 readings averaged |
| DBP | DIASTOL1-3 | mean(DIASTOL1, DIASTOL2, DIASTOL3) | 3 readings averaged |
| HBP diagnosed | U22 | 0=No, 1=Yes, 9=Don't know (→NA) | |
| HBP medication | U24 | 0=No, 1=Yes | |
| DM diagnosed | U24A | 0=No, 1=Yes, 9=Don't know (→NA) | |
| Smoking | U25 + U27 | never(U25==0) / former(U25==1 & U27==0) / current(U25==1 & U27==1) | |
| Alcohol | U40 + U41 | never(U40==0) / occasional(U41≥4) / frequent(U41≤3, ≥1x/week) | U41: 1=daily, 2=3-4x/wk, 3=1-2x/wk, 4=1-2x/mo, 5=<1x/mo |
| Education | A12 | 0=none, 1=primary, 2=lower-mid, 3=upper-mid, 4=technical, 5=university, 6=master+. Recode: 0-2→low, 3-4→mid, 5-6→high | |
| Income | indwage | Continuous yuan → quartiles within wave | |
| Glucose | GLUCOSE_MG | mg/dL (also GLUCOSE in mmol/L) | 2009 only |
| HbA1c | HbA1c | % (direct) | 2009 only |
| TC | TC_MG | mg/dL | 2009 only |
| TG | TG_MG | mg/dL | 2009 only |
| HDL | HDL_C_MG | mg/dL | 2009 only |
| hsCRP | HS_CRP | mg/L | 2009 only |
| Hemoglobin | HGB | **g/L (divide by 10 for g/dL)** | Unit differs from KR/US |
| Self-health | U48A | Self-reported health status | 2004-2011 |
| Depression | — | **NOT AVAILABLE** in standard download. CES-D exists but needs separate dataset. | Cannot directly compare with PHQ-9 |

### CHNS-Specific Warnings

1. **No survey weights**: CHNS is NOT a formally weighted survey. Use unweighted analysis with cluster-robust SE by COMMID. Report as limitation.
2. **Biomarker = 2009 only**: Glucose, HbA1c, lipids, hsCRP available only in 2009 wave. Other waves lack lab data.
3. **CES-D not in standard download**: Depression comparison requires separate dataset download from cpc.unc.edu.
4. **BMI cutoff ≠ KR ≠ US**: China=28, Korea=25, US=30. Use country-specific cutoffs AND sensitivity analysis with WHO cutoff=25.
5. **SES-health gradient may reverse**: Low education and low income are NOT always risk factors in China (null/protective). This is the "developing country health transition" — do NOT treat as a bug.
6. **Hemoglobin unit**: CHNS reports g/L (KR/US report g/dL). Divide by 10 when comparing.
7. **Education scale**: 7-level (0-6) vs KR 4-level vs US 5-level. Harmonize to 3-level for comparison.

### Composite Score Replication Warnings (learned from LE8 replication)

1. **BMI cutoff mismatch**: LE8 uses WHO <25 which classifies most Koreans as "ideal" → Factor subscore loses BMI discriminatory power in Asian populations. Report this limitation.
2. **KNHANES sleep = clock times**: BP16_11-14 are bedtime/waketime (hour:min), NOT sleep duration. Must compute `wake_time - bed_time` with midnight crossing.
3. **pa_aerobic codes**: Values are 0/1 (not 1/2). Binary → MET-hours approximation is coarse.
4. **Diet quality scoring**: AHEI-2010 requires detailed food group data; nutrient-based proxy gives different distribution. Recommend downloading NHANES DR1TOT_J for dietary recall nutrients.
5. **LE8 sensitivity to implementation**: Small scoring differences compound across 8 components → overall score can diverge substantially, especially in the "moderate" range where most people cluster.

## Anti-Hallucination

- **Never fabricate variable names, dataset column names, or variable codings.** If a variable mapping is uncertain, output `[VERIFY: variable_name]` and ask the user to confirm against the data dictionary.
- **Never fabricate statistical results** — no invented p-values, effect sizes, confidence intervals, or sample sizes. All numbers must come from executed code output.
- **Never generate references from memory.** Use `/search-lit` for all citations.
- If a function, package, or API does not exist or you are unsure, say so explicitly rather than guessing.
