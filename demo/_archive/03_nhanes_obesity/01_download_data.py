"""
MedSci Skills Demo 3: NHANES Obesity & Diabetes
Step 1 — Download and prepare NHANES 2017-2018 data

Downloads three XPT files from CDC:
  - DEMO_J: Demographics + survey weights
  - BMX_J: Body measures (BMI)
  - GHB_J: Glycohemoglobin (HbA1c)

Usage: python3 01_download_data.py
Output: data/nhanes_2017_2018.csv
"""

import os
import pandas as pd
import numpy as np
from urllib.request import urlretrieve

print("=" * 60)
print("MedSci Skills Demo 3: NHANES Data Download")
print("=" * 60)

# CDC NHANES 2017-2018 (cycle J)
BASE_URL = "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles"
FILES = {
    "DEMO_J": f"{BASE_URL}/DEMO_J.xpt",
    "BMX_J": f"{BASE_URL}/BMX_J.xpt",
    "GHB_J": f"{BASE_URL}/GHB_J.xpt",
}

# Download XPT files
for name, url in FILES.items():
    dest = f"data/{name}.XPT"
    if os.path.exists(dest):
        print(f"Already exists: {dest}")
    else:
        print(f"Downloading: {name}...")
        urlretrieve(url, dest)
        print(f"  Saved: {dest} ({os.path.getsize(dest) / 1024:.0f} KB)")

# Load and merge
print("\nLoading XPT files...")
demo = pd.read_sas("data/DEMO_J.XPT", format="xport", encoding="utf-8")
bmx = pd.read_sas("data/BMX_J.XPT", format="xport", encoding="utf-8")
ghb = pd.read_sas("data/GHB_J.XPT", format="xport", encoding="utf-8")

print(f"  DEMO_J: {demo.shape[0]} rows, {demo.shape[1]} cols")
print(f"  BMX_J:  {bmx.shape[0]} rows, {bmx.shape[1]} cols")
print(f"  GHB_J:  {ghb.shape[0]} rows, {ghb.shape[1]} cols")

# Select variables of interest
demo_vars = demo[["SEQN", "RIAGENDR", "RIDAGEYR", "RIDRETH3",
                   "DMDEDUC2", "INDFMPIR", "WTMEC2YR", "SDMVPSU", "SDMVSTRA"]].copy()
bmx_vars = bmx[["SEQN", "BMXBMI", "BMXWAIST"]].copy()
ghb_vars = ghb[["SEQN", "LBXGH"]].copy()

# Merge on SEQN
df = demo_vars.merge(bmx_vars, on="SEQN", how="inner")
df = df.merge(ghb_vars, on="SEQN", how="inner")
print(f"\nMerged: {df.shape[0]} participants with complete data linkage")

# Recode variables
df = df.rename(columns={
    "RIAGENDR": "gender_code",
    "RIDAGEYR": "age",
    "RIDRETH3": "race_ethnicity_code",
    "DMDEDUC2": "education_code",
    "INDFMPIR": "poverty_income_ratio",
    "WTMEC2YR": "survey_weight",
    "SDMVPSU": "psu",
    "SDMVSTRA": "stratum",
    "BMXBMI": "bmi",
    "BMXWAIST": "waist_circumference",
    "LBXGH": "hba1c",
})

# Create derived variables
# Gender
df["gender"] = df["gender_code"].map({1: "Male", 2: "Female"})

# Race/ethnicity (RIDRETH3 codes)
race_map = {
    1: "Mexican American",
    2: "Other Hispanic",
    3: "Non-Hispanic White",
    4: "Non-Hispanic Black",
    6: "Non-Hispanic Asian",
    7: "Other/Multi-Racial",
}
df["race_ethnicity"] = df["race_ethnicity_code"].map(race_map)

# Education (adults 20+)
edu_map = {
    1: "Less than 9th grade",
    2: "9-11th grade",
    3: "High school/GED",
    4: "Some college/AA",
    5: "College graduate+",
}
df["education"] = df["education_code"].map(edu_map)

# BMI categories (WHO)
df["bmi_category"] = pd.cut(
    df["bmi"],
    bins=[0, 18.5, 25, 30, 100],
    labels=["Underweight", "Normal", "Overweight", "Obese"],
    right=False,
)

# Diabetes status (ADA criteria: HbA1c >= 6.5%)
df["diabetes"] = (df["hba1c"] >= 6.5).astype(int)
df["diabetes_label"] = df["diabetes"].map({0: "No diabetes", 1: "Diabetes"})

# Prediabetes (5.7-6.4%)
df["glycemic_status"] = pd.cut(
    df["hba1c"],
    bins=[0, 5.7, 6.5, 100],
    labels=["Normal", "Prediabetes", "Diabetes"],
    right=False,
)

# Filter: adults 20+ with valid data
df_adults = df[(df["age"] >= 20) & df["bmi"].notna() & df["hba1c"].notna()
               & df["survey_weight"].notna()].copy()

print(f"Adults 20+ with complete BMI + HbA1c: {len(df_adults)}")

# Save
df_adults.to_csv("data/nhanes_2017_2018.csv", index=False)

# Summary
print("\n--- Dataset Summary ---")
print(f"Total participants: {len(df_adults)}")
print(f"Age: {df_adults['age'].mean():.1f} +/- {df_adults['age'].std():.1f}")
print(f"Female: {(df_adults['gender'] == 'Female').sum()} ({100 * (df_adults['gender'] == 'Female').mean():.1f}%)")
print(f"BMI: {df_adults['bmi'].mean():.1f} +/- {df_adults['bmi'].std():.1f}")
print(f"HbA1c: {df_adults['hba1c'].mean():.2f} +/- {df_adults['hba1c'].std():.2f}")
print(f"\nBMI categories:")
print(df_adults["bmi_category"].value_counts().sort_index())
print(f"\nGlycemic status:")
print(df_adults["glycemic_status"].value_counts().sort_index())
print(f"\nDiabetes prevalence: {100 * df_adults['diabetes'].mean():.1f}%")
print(f"\nSaved: data/nhanes_2017_2018.csv")
print("=" * 60)
