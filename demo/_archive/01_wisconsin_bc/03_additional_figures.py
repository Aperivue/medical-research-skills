"""
MedSci Skills Demo 1 v2: Wisconsin Breast Cancer Dataset
Step 3 — Additional Publication Figures (make-figures skill)

Generates:
  Figure 2: Confusion matrices (3 models side-by-side)
  Figure 3: Feature importance (top 10 features, LR coefficients vs RF importance)
  Figure 4: Calibration curves (3 models)

Usage: python 03_additional_figures.py
"""

import os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# v2: corrected style path after repo move
STYLE_PATH = os.path.expanduser(
    "~/workspace/6_Aperivue/medical-research-skills/skills/analyze-stats/references/style/figure_style.mplstyle"
)
if os.path.exists(STYLE_PATH):
    plt.style.use(STYLE_PATH)

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.calibration import calibration_curve
from sklearn.metrics import confusion_matrix

np.random.seed(42)

# === LOAD FROM ANALYSIS OUTPUTS (not re-fitting) ===
# Read predictions saved by 02_analyze.py to ensure figure/table consistency
pred_df = pd.read_csv("output/predictions.csv")
y = pred_df["ground_truth"].values

model_names = ["Logistic_Regression", "Random_Forest", "SVM_RBF"]
display_names = {"Logistic_Regression": "Logistic Regression",
                 "Random_Forest": "Random Forest",
                 "SVM_RBF": "SVM (RBF)"}

y_scores = {}
y_preds = {}
for m in model_names:
    y_scores[display_names[m]] = pred_df[f"score_{m}"].values
    y_preds[display_names[m]] = pred_df[f"pred_{m}"].values

# Feature importance still needs full-data fit (no predictions needed)
data = load_breast_cancer()
feature_names = data.feature_names
X = data.data
# Flip labels to match convention: 1=malignant, 0=benign
y_full = 1 - data.target
scaler_full = StandardScaler()
X_full = scaler_full.fit_transform(X)
lr_full = LogisticRegression(max_iter=5000, random_state=42).fit(X_full, y_full)
rf_full = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_full, y_full)

model_order = ["Logistic Regression", "Random Forest", "SVM (RBF)"]
COLORS = {"Logistic Regression": "#0072B2", "Random Forest": "#D55E00", "SVM (RBF)": "#009E73"}
NAVY = "#1B2A4A"

# ============================================================
# FIGURE 2: Confusion Matrices
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(10, 3.2))

for ax, name in zip(axes, model_order):
    cm = confusion_matrix(y, y_preds[name])
    # cm: [[TN, FP], [FN, TP]]

    im = ax.imshow(cm, cmap="Blues", aspect="equal")

    # Annotate cells
    for i in range(2):
        for j in range(2):
            val = cm[i, j]
            total = cm.sum()
            pct = 100 * val / total
            color = "white" if val > cm.max() * 0.6 else "black"
            ax.text(j, i, f"{val}\n({pct:.1f}%)",
                    ha="center", va="center", fontsize=11, color=color, fontweight="bold")

    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(["Benign", "Malignant"], fontsize=9)
    ax.set_yticklabels(["Benign", "Malignant"], fontsize=9)
    ax.set_xlabel("Predicted", fontsize=10)
    if ax == axes[0]:
        ax.set_ylabel("Actual", fontsize=10)
    ax.set_title(name, fontsize=11, fontweight="bold", color=COLORS[name])

fig.suptitle("Figure 2. Confusion Matrices (5-Fold Cross-Validation)", fontsize=12, y=1.02)
fig.tight_layout()
fig.savefig("figures/confusion_matrices.png", dpi=300, bbox_inches="tight")
fig.savefig("figures/confusion_matrices.pdf", bbox_inches="tight")
plt.close(fig)
print("Saved: figures/confusion_matrices.png")

# ============================================================
# FIGURE 3: Feature Importance (Top 10)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

# LR coefficients (absolute value, standardized)
lr_coef = np.abs(lr_full.coef_[0])
top10_lr = np.argsort(lr_coef)[-10:][::-1]

axes[0].barh(range(10), lr_coef[top10_lr], color="#0072B2", alpha=0.85)
axes[0].set_yticks(range(10))
axes[0].set_yticklabels([feature_names[i] for i in top10_lr], fontsize=9)
axes[0].set_xlabel("Absolute Coefficient", fontsize=10)
axes[0].set_title("Logistic Regression", fontsize=11, fontweight="bold", color="#0072B2")
axes[0].invert_yaxis()

# RF feature importance
rf_imp = rf_full.feature_importances_
top10_rf = np.argsort(rf_imp)[-10:][::-1]

axes[1].barh(range(10), rf_imp[top10_rf], color="#D55E00", alpha=0.85)
axes[1].set_yticks(range(10))
axes[1].set_yticklabels([feature_names[i] for i in top10_rf], fontsize=9)
axes[1].set_xlabel("Gini Importance", fontsize=10)
axes[1].set_title("Random Forest", fontsize=11, fontweight="bold", color="#D55E00")
axes[1].invert_yaxis()

fig.suptitle("Figure 3. Top 10 Discriminative Features by Model", fontsize=12, y=1.02)
fig.tight_layout()
fig.savefig("figures/feature_importance.png", dpi=300, bbox_inches="tight")
fig.savefig("figures/feature_importance.pdf", bbox_inches="tight")
plt.close(fig)
print("Saved: figures/feature_importance.png")

# ============================================================
# FIGURE 4: Calibration Curves
# ============================================================
fig, ax = plt.subplots(figsize=(4.5, 4.5))

for name in model_order:
    prob_true, prob_pred = calibration_curve(y, y_scores[name], n_bins=10, strategy="uniform")
    ax.plot(prob_pred, prob_true, marker="o", markersize=4, linewidth=1.5,
            color=COLORS[name], label=name)

ax.plot([0, 1], [0, 1], color="gray", linestyle="--", linewidth=0.8, label="Perfect calibration")
ax.set_xlabel("Mean Predicted Probability")
ax.set_ylabel("Observed Proportion of Positives")
ax.set_xlim([-0.02, 1.02])
ax.set_ylim([-0.02, 1.02])
ax.set_aspect("equal")
ax.legend(loc="lower right", fontsize=7)
ax.set_title("Figure 4. Calibration Curves")

fig.tight_layout()
fig.savefig("figures/calibration_curves.png", dpi=300, bbox_inches="tight")
fig.savefig("figures/calibration_curves.pdf", bbox_inches="tight")
plt.close(fig)
print("Saved: figures/calibration_curves.png")

print("\nAll additional figures generated.")
