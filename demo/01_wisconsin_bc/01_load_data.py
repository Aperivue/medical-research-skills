"""
MedSci Skills Demo 1 v2: Wisconsin Breast Cancer Dataset
Step 1 — Load and prepare data

This script loads the sklearn built-in breast cancer dataset,
converts it to a clinical-style DataFrame, and saves as CSV
for downstream analysis with MedSci Skills.

Usage: python 01_load_data.py
Output: data/breast_cancer_clinical.csv
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer

# Load dataset — one line, zero download
data = load_breast_cancer()

# Build clinical-style DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df["diagnosis"] = pd.Series(data.target).map({0: "malignant", 1: "benign"})

# Add synthetic clinical variables for realistic demo
rng = np.random.default_rng(42)
df["patient_id"] = [f"WBC-{i+1:04d}" for i in range(len(df))]
df["age"] = rng.normal(55, 12, len(df)).clip(25, 85).astype(int)
df["sex"] = "F"  # breast cancer dataset
df["imaging_modality"] = rng.choice(
    ["FNA cytology"], size=len(df)
)

# Reorder columns: ID + demographics first
id_cols = ["patient_id", "age", "sex", "imaging_modality", "diagnosis"]
feature_cols = [c for c in df.columns if c not in id_cols]
df = df[id_cols + feature_cols]

# Save
output_path = "data/breast_cancer_clinical.csv"
df.to_csv(output_path, index=False)

# Summary for demo log
print("=" * 60)
print("MedSci Skills Demo 1 v2: Data Loading Complete")
print("=" * 60)
print(f"Dataset: Wisconsin Breast Cancer (UCI/sklearn)")
print(f"Samples: {len(df)}")
print(f"Features: {len(feature_cols)} imaging features + 4 clinical")
print(f"Diagnosis: {df['diagnosis'].value_counts().to_dict()}")
print(f"Age: mean {df['age'].mean():.1f} +/- {df['age'].std():.1f}")
print(f"Output: {output_path}")
print(f"File size: {pd.read_csv(output_path).memory_usage(deep=True).sum() / 1024:.1f} KB")
print("=" * 60)
