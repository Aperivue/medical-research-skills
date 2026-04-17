# Variable Coding Registry

Pre-validated variable definitions for batch code generation.
Each entry provides raw variable names, coding logic, and human-readable labels
for KNHANES and NHANES. Add new variables as they are validated in replication studies.

## Exposures

### Depression (PHQ-9 ≥ 10)

| Field | KNHANES | NHANES |
|-------|---------|--------|
| Raw vars | BP_PHQ_1 ~ BP_PHQ_9 | DPQ010 ~ DPQ090 |
| Coding | sum(BP_PHQ_1:9), NA if any missing | recode text→0-3, sum, NA if any missing |
| Binary | phq_score ≥ 10 → 1 | phq_score ≥ 10 → 1 |
| Label | Depression (PHQ-9 ≥ 10) | Depression (PHQ-9 ≥ 10) |
| Notes | Items are numeric 0-3 | Items are TEXT: "Not at all"→0, "Several days"→1, "More than half the days"→2, "Nearly every day"→3 |

### Obesity

| Field | KNHANES | NHANES |
|-------|---------|--------|
| Raw vars | HE_obe (or BMXBMI) | BMXBMI (BMX_J) |
| Coding | HE_obe ≥ 4 (Asian cutoff: BMI ≥ 25) | BMXBMI ≥ 30 (WHO cutoff) |
| Binary | obesity = 1 if HE_obe ≥ 4 | obesity = 1 if BMXBMI ≥ 30 |
| Label | Obesity (BMI ≥ 25, Asian) | Obesity (BMI ≥ 30, WHO) |
| Notes | 6-level: 1=underweight to 6=morbid obesity | Continuous BMI; use 25 for Asian-Americans analysis |

### Current Smoking

| Field | KNHANES | NHANES |
|-------|---------|--------|
| Raw vars | BS3_1 | SMQ020, SMQ040 |
| Coding | BS3_1 %in% c(1,2) → current; 3 → former; 8 → never | SMQ020=="Yes" & SMQ040 %in% c("Every day","Some days") → current |
| Binary | smoking_current = 1 if BS3_1 in (1,2) | smoking_current = 1 if above |
| Label | Current smoking | Current smoking |
| Notes | 1=daily, 2=occasional, 3=former, 8=never | Two-step: ≥100 lifetime cigs + currently smoke |

### Heavy/Frequent Drinking

| Field | KNHANES | NHANES |
|-------|---------|--------|
| Raw vars | BD1_11 | ALQ111, ALQ121 |
| Coding | BD1_11 in 2:6 → frequent; 1 → occasional; 8 → never | ALQ111=="No" → never; ALQ121 frequency mapping |
| Binary | drinking_freq = 1 if BD1_11 in 2:6 | drinking_freq = 1 if ALQ121 indicates monthly+ |
| Label | Frequent alcohol use | Frequent alcohol use |
| Notes | 1=past-year abstainer, 2-6=frequency levels, 8=lifetime never | ALQ121 text labels; never=ALQ111=="No" (ALQ121 is NA) |

### Low Education

| Field | KNHANES | NHANES |
|-------|---------|--------|
| Raw vars | edu | DMDEDUC2 |
| Coding | edu in 1:3 → non-college; 4 → college+ | "Less than 9th grade"/"9-11th grade"/"High school" → non-college |
| Binary | low_edu = 1 if edu in 1:3 | low_edu = 1 if non-college |
| Label | Non-college education | Non-college education |

### Low Income

| Field | KNHANES | NHANES |
|-------|---------|--------|
| Raw vars | incm | INDFMPIR (INQ_J) |
| Coding | incm in 1:3 → bottom 80% | INDFMPIR < 1.3 → low income |
| Binary | low_income = 1 if incm in 1:3 | low_income = 1 if PIR < 1.3 |
| Label | Lower income (bottom 80%) | Low income (PIR < 1.3) |
| Notes | 4-level quartile | Poverty income ratio; threshold varies by study |

## Outcomes

### Diabetes

| Field | KNHANES | NHANES |
|-------|---------|--------|
| Raw vars | HE_glu, HE_HbA1c, DE1_dg | LBXSGL (BIOPRO_J), LBXGH (GHB_J), DIQ010 |
| Coding | HE_glu≥126 \| HE_HbA1c≥6.5 \| DE1_dg==1 | LBXSGL≥126 \| LBXGH≥6.5 \| DIQ010=="Yes" |
| Label | Diabetes mellitus | Diabetes mellitus |
| Notes | FPG=fasting plasma glucose | LBXSGL not LBXSGLU; DIQ010 is text |

### Hypertension

| Field | KNHANES | NHANES |
|-------|---------|--------|
| Raw vars | HE_sbp, HE_dbp, DI1_dg | BPXOSY1-4, BPXODI1-4, BPQ020 |
| Coding | mean(SBP)≥140 \| mean(DBP)≥90 \| DI1_dg==1 | mean(SBP readings)≥140 \| mean(DBP)≥90 \| BPQ020=="Yes" |
| Label | Hypertension | Hypertension |
| Notes | HE_sbp/dbp are already averaged | Average of up to 4 readings; BPQ020 is text |

### CVD History

| Field | KNHANES | NHANES |
|-------|---------|--------|
| Raw vars | DI4_dg, DI5_dg, DI6_dg | MCQ160B, MCQ160C, MCQ160D |
| Coding | any == 1 → CVD | any == "Yes" → CVD |
| Label | Cardiovascular disease history | Cardiovascular disease history |
| Notes | 4=MI, 5=angina, 6=stroke | B=CHF, C=CHD, D=angina |

### Metabolic Syndrome

| Field | KNHANES | NHANES |
|-------|---------|--------|
| Raw vars | HE_wc, HE_sbp, HE_dbp, HE_TG, HE_HDL_st2, HE_glu | BMXWAIST, BPXOSY, BPXODI, LBXSTR, LBDHDD, LBXSGL |
| Coding | NCEP ATP III: ≥3 of 5 criteria | NCEP ATP III: ≥3 of 5 criteria |
| Label | Metabolic syndrome (NCEP ATP III) | Metabolic syndrome (NCEP ATP III) |
| Notes | Waist: M≥90, F≥85 (Korean) | Waist: M≥102, F≥88 (US/WHO) |

## Standard Covariate Set

Default covariates for fully adjusted model (remove exposure if overlap):

| Covariate | KNHANES var | NHANES var | Type |
|-----------|-------------|------------|------|
| Age | age | RIDAGEYR | Continuous |
| Sex | sex | RIAGENDR | Binary |
| Education | edu | DMDEDUC2 | Binary (college vs non) |
| Income | incm | INDFMPIR | Binary (threshold varies) |
| Smoking | BS3_1 | SMQ020+SMQ040 | 3-level (current/former/never) |
| Alcohol | BD1_11 | ALQ111+ALQ121 | 3-level (frequent/occasional/never) |
| Obesity | HE_obe | BMXBMI | Binary (country-specific cutoff) |
| CVD | DI4-6_dg | MCQ160B-D | Binary |

## Survey Design

| Component | KNHANES | NHANES |
|-----------|---------|--------|
| Strata | kstrata | SDMVSTRA |
| PSU/Cluster | psu | SDMVPSU |
| Weight | wt_itvex | WTMEC2YR (single-cycle) or WTMECPRP (pooled) |
| R function | svydesign(id=~psu, strata=~kstrata, weights=~wt_itvex, nest=TRUE) | svydesign(id=~SDMVPSU, strata=~SDMVSTRA, weights=~WTMEC2YR, nest=TRUE) |

## Adding New Variables

When a new variable is validated through /replicate-study or /cross-national:
1. Add an entry in the appropriate section (Exposure or Outcome)
2. Include both KNHANES and NHANES coding
3. Note any text-label gotchas for NHANES
4. Document the source paper that validated the coding
