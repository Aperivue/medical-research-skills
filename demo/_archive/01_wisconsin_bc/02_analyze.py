"""
MedSci Skills Demo 1 v2: Wisconsin Breast Cancer Dataset
Step 2 — Statistical Analysis (analyze-stats skill)

Demonstrates the analyze-stats skill pipeline:
  Table 1 demographics -> 3-model comparison -> ROC curves -> DeLong tests

Based on: skills/analyze-stats/references/templates/
  - table1_demographics.py
  - diagnostic_accuracy.py

Usage: python 02_analyze.py
Output: output/table1.csv, output/diagnostic_accuracy.csv, figures/roc_curve.png
"""

# === REPRODUCIBILITY HEADER ===
import sys
import os
import datetime
import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(42)
print(f"Date: {datetime.date.today()}")
print(f"Python: {sys.version.split()[0]}")
import scipy
print(f"numpy: {np.__version__}, pandas: {pd.__version__}, scipy: {scipy.__version__}")

from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, roc_auc_score
import sklearn
print(f"sklearn: {sklearn.__version__}")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# v2: corrected style path after repo move
STYLE_PATH = os.path.expanduser(
    "~/workspace/6_Aperivue/medical-research-skills/skills/analyze-stats/references/style/figure_style.mplstyle"
)
if os.path.exists(STYLE_PATH):
    plt.style.use(STYLE_PATH)

print()

# === LOAD DATA ===
df = pd.read_csv("data/breast_cancer_clinical.csv")
print(f"Loaded: {df.shape[0]} samples, {df.shape[1]} columns")

# ============================================================
# PART A: TABLE 1 — BASELINE DEMOGRAPHICS
# ============================================================
print("\n" + "=" * 60)
print("PART A: Table 1 — Baseline Characteristics")
print("=" * 60)

GROUP_COL = "diagnosis"
CONTINUOUS_VARS = ["age", "mean radius", "mean texture", "mean perimeter",
                   "mean area", "mean smoothness"]
CATEGORICAL_VARS = ["sex", "imaging_modality"]
VAR_LABELS = {
    "age": "Age (years)",
    "mean radius": "Mean radius",
    "mean texture": "Mean texture",
    "mean perimeter": "Mean perimeter",
    "mean area": "Mean area (pixels)",
    "mean smoothness": "Mean smoothness",
    "sex": "Sex",
    "imaging_modality": "Imaging modality",
}


def test_normality(series, alpha=0.05):
    clean = series.dropna()
    if len(clean) < 3:
        return False, np.nan
    if len(clean) < 50:
        stat, p = stats.shapiro(clean)
    else:
        stat, p = stats.kstest(clean, "norm", args=(clean.mean(), clean.std()))
    return p >= alpha, p


def format_continuous(series, is_normal, dp=1):
    clean = series.dropna()
    if is_normal:
        return f"{clean.mean():.{dp}f} +/- {clean.std():.{dp}f}"
    else:
        q1, median, q3 = clean.quantile([0.25, 0.5, 0.75])
        return f"{median:.{dp}f} ({q1:.{dp}f}-{q3:.{dp}f})"


def format_p(p):
    if pd.isna(p):
        return ""
    if p < 0.001:
        return "<0.001"
    return f"{p:.3f}"


# Build Table 1
groups = sorted(df[GROUP_COL].unique())
group_dfs = {g: df[df[GROUP_COL] == g] for g in groups}
rows = []

# N row
n_row = {"Variable": "n"}
for g in groups:
    n_row[g] = str(len(group_dfs[g]))
n_row["Overall"] = str(len(df))
n_row["p-value"] = ""
rows.append(n_row)

# Continuous
for var in CONTINUOUS_VARS:
    label = VAR_LABELS.get(var, var)
    is_normal, _ = test_normality(df[var])
    stat_type = "mean +/- SD" if is_normal else "median (IQR)"
    row = {"Variable": f"{label}, {stat_type}"}
    row["Overall"] = format_continuous(df[var], is_normal)
    for g in groups:
        row[g] = format_continuous(group_dfs[g][var], is_normal)
    # p-value
    grp_series = [group_dfs[g][var].dropna() for g in groups]
    if is_normal:
        _, p = stats.ttest_ind(*grp_series)
        test_name = "t-test"
    else:
        _, p = stats.mannwhitneyu(*grp_series, alternative="two-sided")
        test_name = "Mann-Whitney U"
    row["p-value"] = format_p(p)
    rows.append(row)

# Categorical
for var in CATEGORICAL_VARS:
    label = VAR_LABELS.get(var, var)
    row = {"Variable": f"{label}, n (%)"}
    row["Overall"] = ""
    for g in groups:
        row[g] = ""
    contingency = pd.crosstab(df[var], df[GROUP_COL])
    if contingency.shape[0] == 1:
        row["p-value"] = "N/A"
    else:
        _, p, _, _ = stats.chi2_contingency(contingency)
        row["p-value"] = format_p(p)
    rows.append(row)
    for cat in df[var].unique():
        cat_row = {"Variable": f"  {cat}"}
        total = len(df)
        cat_row["Overall"] = f"{(df[var]==cat).sum()} ({100*(df[var]==cat).mean():.1f}%)"
        for g in groups:
            gdf = group_dfs[g]
            n_cat = (gdf[var] == cat).sum()
            cat_row[g] = f"{n_cat} ({100*n_cat/len(gdf):.1f}%)"
        cat_row["p-value"] = ""
        rows.append(cat_row)

table1 = pd.DataFrame(rows)
col_order = ["Variable"] + groups + ["Overall", "p-value"]
table1 = table1[col_order]
table1.to_csv("output/table1.csv", index=False)

print("\n--- Table 1. Baseline Characteristics ---\n")
print(table1.to_markdown(index=False))
print(f"\nSaved: output/table1.csv")

# ============================================================
# PART B: DIAGNOSTIC ACCURACY — 3-MODEL COMPARISON
# ============================================================
print("\n" + "=" * 60)
print("PART B: Diagnostic Accuracy — 3-Model Comparison")
print("=" * 60)

# Prepare features and labels
feature_cols = [c for c in df.columns if c not in
                ["patient_id", "age", "sex", "imaging_modality", "diagnosis"]]
X = df[feature_cols].values
y = (df["diagnosis"] == "malignant").astype(int).values
print(f"\nFeatures: {X.shape[1]}, Positive (malignant): {y.sum()}, Negative (benign): {(1-y).sum()}")

# Stratified 5-fold cross-validation for predicted probabilities
models = {
    "Logistic Regression": LogisticRegression(max_iter=5000, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "SVM (RBF)": SVC(kernel="rbf", probability=True, random_state=42),
}

y_scores = {name: np.zeros(len(y)) for name in models}
y_preds = {name: np.zeros(len(y), dtype=int) for name in models}

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scaler = StandardScaler()

for fold, (train_idx, test_idx) in enumerate(skf.split(X, y)):
    X_train, X_test = scaler.fit_transform(X[train_idx]), scaler.transform(X[test_idx])
    y_train = y[train_idx]

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_scores[name][test_idx] = model.predict_proba(X_test)[:, 1]
        y_preds[name][test_idx] = model.predict(X_test)

# Wilson CI for proportions
def wilson_ci(p, n, alpha=0.05):
    if n == 0:
        return (0.0, 0.0)
    z = stats.norm.ppf(1 - alpha / 2)
    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    spread = z * np.sqrt((p * (1 - p) + z**2 / (4 * n)) / n) / denom
    return (max(0.0, center - spread), min(1.0, center + spread))


# DeLong AUC CI
def delong_auc_ci(y_true, y_score, alpha=0.05):
    pos = y_score[y_true == 1]
    neg = y_score[y_true == 0]
    m, n = len(pos), len(neg)
    v_pos = np.array([np.mean(neg < p) + 0.5 * np.mean(neg == p) for p in pos])
    v_neg = np.array([np.mean(pos > nv) + 0.5 * np.mean(pos == nv) for nv in neg])
    var_auc = np.var(v_pos, ddof=1) / m + np.var(v_neg, ddof=1) / n
    auc = roc_auc_score(y_true, y_score)
    z = stats.norm.ppf(1 - alpha / 2)
    se = np.sqrt(var_auc)
    return auc, max(0, auc - z * se), min(1, auc + z * se)


# Compute metrics for each model
print("\n--- Performance Metrics (5-fold CV) ---\n")
results_rows = []

for name in models:
    y_s = y_scores[name]
    y_p = y_preds[name]

    tp = ((y_p == 1) & (y == 1)).sum()
    fp = ((y_p == 1) & (y == 0)).sum()
    tn = ((y_p == 0) & (y == 0)).sum()
    fn = ((y_p == 0) & (y == 1)).sum()

    sens = tp / (tp + fn)
    spec = tn / (tn + fp)
    ppv = tp / (tp + fp)
    npv = tn / (tn + fn)
    acc = (tp + tn) / len(y)
    auc, auc_lo, auc_hi = delong_auc_ci(y, y_s)

    sens_ci = wilson_ci(sens, tp + fn)
    spec_ci = wilson_ci(spec, tn + fp)
    ppv_ci = wilson_ci(ppv, tp + fp)
    npv_ci = wilson_ci(npv, tn + fn)
    acc_ci = wilson_ci(acc, len(y))

    row = {
        "Model": name,
        "AUC (95% CI)": f"{auc:.3f} ({auc_lo:.3f}-{auc_hi:.3f})",
        "Sensitivity (95% CI)": f"{sens:.3f} ({sens_ci[0]:.3f}-{sens_ci[1]:.3f})",
        "Specificity (95% CI)": f"{spec:.3f} ({spec_ci[0]:.3f}-{spec_ci[1]:.3f})",
        "PPV (95% CI)": f"{ppv:.3f} ({ppv_ci[0]:.3f}-{ppv_ci[1]:.3f})",
        "NPV (95% CI)": f"{npv:.3f} ({npv_ci[0]:.3f}-{npv_ci[1]:.3f})",
        "Accuracy (95% CI)": f"{acc:.3f} ({acc_ci[0]:.3f}-{acc_ci[1]:.3f})",
        "TP": tp, "FP": fp, "TN": tn, "FN": fn,
    }
    results_rows.append(row)

results_df = pd.DataFrame(results_rows)
results_df.to_csv("output/diagnostic_accuracy.csv", index=False)
print(results_df[["Model", "AUC (95% CI)", "Sensitivity (95% CI)",
                   "Specificity (95% CI)", "Accuracy (95% CI)"]].to_markdown(index=False))
print(f"\nSaved: output/diagnostic_accuracy.csv")

# DeLong pairwise comparisons
print("\n--- DeLong Test: Pairwise AUC Comparison ---\n")
model_names = list(models.keys())
for i in range(len(model_names)):
    for j in range(i + 1, len(model_names)):
        n1, n2 = model_names[i], model_names[j]
        s1, s2 = y_scores[n1], y_scores[n2]

        pos_mask = y == 1
        neg_mask = y == 0
        m, n = pos_mask.sum(), neg_mask.sum()

        v1p = np.array([np.mean(s1[neg_mask] < p) + 0.5 * np.mean(s1[neg_mask] == p) for p in s1[pos_mask]])
        v2p = np.array([np.mean(s2[neg_mask] < p) + 0.5 * np.mean(s2[neg_mask] == p) for p in s2[pos_mask]])
        v1n = np.array([np.mean(s1[pos_mask] > nv) + 0.5 * np.mean(s1[pos_mask] == nv) for nv in s1[neg_mask]])
        v2n = np.array([np.mean(s2[pos_mask] > nv) + 0.5 * np.mean(s2[pos_mask] == nv) for nv in s2[neg_mask]])

        var1 = np.var(v1p, ddof=1) / m + np.var(v1n, ddof=1) / n
        var2 = np.var(v2p, ddof=1) / m + np.var(v2n, ddof=1) / n
        cov = np.cov(v1p, v2p)[0, 1] / m + np.cov(v1n, v2n)[0, 1] / n

        auc1 = roc_auc_score(y, s1)
        auc2 = roc_auc_score(y, s2)
        z_stat = (auc1 - auc2) / np.sqrt(var1 + var2 - 2 * cov)
        p_val = 2 * stats.norm.sf(abs(z_stat))
        print(f"  {n1} vs {n2}: z = {z_stat:.3f}, p = {format_p(p_val)}")

# Save predicted probabilities for figure generation
pred_df = pd.DataFrame({
    "patient_id": df["patient_id"],
    "ground_truth": y,
})
for name in models:
    safe_name = name.replace(" ", "_").replace("(", "").replace(")", "")
    pred_df[f"score_{safe_name}"] = y_scores[name]
    pred_df[f"pred_{safe_name}"] = y_preds[name]
pred_df.to_csv("output/predictions.csv", index=False)
print(f"\nSaved: output/predictions.csv")

# ============================================================
# PART C: ROC CURVE FIGURE
# ============================================================
print("\n" + "=" * 60)
print("PART C: ROC Curve")
print("=" * 60)

fig, ax = plt.subplots(figsize=(4.5, 4.5))
colors = ["#0072B2", "#D55E00", "#009E73"]

for i, name in enumerate(models):
    fpr, tpr, _ = roc_curve(y, y_scores[name])
    auc, auc_lo, auc_hi = delong_auc_ci(y, y_scores[name])
    label = f"{name}: {auc:.3f} ({auc_lo:.3f}-{auc_hi:.3f})"
    ax.plot(fpr, tpr, color=colors[i], linewidth=1.5, label=label)

ax.plot([0, 1], [0, 1], color="gray", linestyle="--", linewidth=0.8)
ax.set_xlabel("1 - Specificity (FPR)")
ax.set_ylabel("Sensitivity (TPR)")
ax.set_xlim([-0.02, 1.02])
ax.set_ylim([-0.02, 1.02])
ax.set_aspect("equal")
ax.legend(loc="lower right", fontsize=7, title="AUC (95% CI)")
ax.set_title("ROC Curves — Breast Cancer Diagnosis")

fig.tight_layout()
fig.savefig("figures/roc_curve.pdf", format="pdf", bbox_inches="tight")
fig.savefig("figures/roc_curve.png", format="png", dpi=300, bbox_inches="tight")
plt.close(fig)
print("Saved: figures/roc_curve.pdf")
print("Saved: figures/roc_curve.png")

# ============================================================
# RESULTS TEXT (manuscript-ready)
# ============================================================
print("\n" + "=" * 60)
print("MANUSCRIPT-READY RESULTS TEXT")
print("=" * 60)
print()
print("A total of 569 patients (357 benign, 212 malignant) were included.")
print("Baseline characteristics are summarized in Table 1.")
print()
for row in results_rows:
    name = row["Model"]
    print(f"The {name} achieved an AUC of {row['AUC (95% CI)']}, "
          f"sensitivity of {row['Sensitivity (95% CI)']}, "
          f"specificity of {row['Specificity (95% CI)']}, "
          f"and accuracy of {row['Accuracy (95% CI)']}.")
print()
print("ROC curves for all three models are shown in Figure 1.")
print("=" * 60)

# ============================================================
# OUTPUT MANIFEST (for downstream skill discovery)
# ============================================================
import datetime
manifest = f"""# Analysis Outputs
Generated: {datetime.date.today()}
Study type: Diagnostic accuracy (cross-sectional)

## Tables
- `output/table1.csv` -- Baseline characteristics (benign vs malignant)
- `output/diagnostic_accuracy.csv` -- Performance metrics (AUC, Se, Sp, PPV, NPV) with 95% CIs

## Figures
- `figures/roc_curve.pdf` -- ROC curves for 3 models (vector)
- `figures/roc_curve.png` -- ROC curves for 3 models (300 DPI)

## Data
- `output/predictions.csv` -- Per-subject model predictions with ground truth
- `data/breast_cancer_clinical.csv` -- Prepared clinical dataset
"""
with open("output/_analysis_outputs.md", "w") as f:
    f.write(manifest)
print("\nSaved: output/_analysis_outputs.md")
