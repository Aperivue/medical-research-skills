#!/usr/bin/env Rscript
# ============================================================
# MedSci Skills Demo 2: BCG Vaccine Meta-Analysis
# Step 1 — Full Meta-Analysis Pipeline (meta-analysis + analyze-stats skills)
#
# Dataset: metafor::dat.bcg (13 RCTs of BCG vaccine for TB prevention)
# Reference: Colditz et al. (1994) JAMA
#
# Pipeline:
#   Load data -> compute RR -> random-effects model -> forest plot ->
#   funnel plot -> heterogeneity -> subgroup analysis -> meta-regression ->
#   sensitivity analysis -> publication bias
#
# Usage: Rscript 01_meta_analysis.R
# ============================================================

cat("=" , rep("=", 59), "\n", sep = "")
cat("MedSci Skills Demo 2: BCG Vaccine Meta-Analysis\n")
cat("=" , rep("=", 59), "\n", sep = "")

# === REPRODUCIBILITY HEADER ===
set.seed(42)
cat("Date:", format(Sys.Date()), "\n")
cat("R:", R.version.string, "\n")

library(metafor)
library(meta)

cat("metafor:", as.character(packageVersion("metafor")), "\n")
cat("meta:", as.character(packageVersion("meta")), "\n\n")

# === LOAD DATA ===
data(dat.bcg)
cat("Loaded: dat.bcg —", nrow(dat.bcg), "studies\n")
cat("Years:", min(dat.bcg$year), "-", max(dat.bcg$year), "\n")
cat("Total participants (treatment):", sum(dat.bcg$tpos + dat.bcg$tneg), "\n")
cat("Total participants (control):", sum(dat.bcg$cpos + dat.bcg$cneg), "\n\n")

# Save raw data for reference
write.csv(dat.bcg, "data/bcg_raw.csv", row.names = FALSE)
cat("Saved: data/bcg_raw.csv\n")

# === COMPUTE EFFECT SIZES ===
# Log risk ratio with 95% CI
dat <- escalc(measure = "RR", ai = tpos, bi = tneg, ci = cpos, di = cneg,
              data = dat.bcg, append = TRUE)
cat("\n--- Effect Sizes (log Risk Ratio) ---\n")
print(dat[, c("author", "year", "yi", "vi")])

# ============================================================
# PART A: RANDOM-EFFECTS MODEL (REML)
# ============================================================
cat("\n", rep("=", 60), "\n", sep = "")
cat("PART A: Random-Effects Model (REML)\n")
cat(rep("=", 60), "\n", sep = "")

res <- rma(yi, vi, data = dat, method = "REML")
cat("\n")
print(summary(res))

# Extract key results
pooled_rr <- exp(coef(res))
pooled_ci_lb <- exp(res$ci.lb)
pooled_ci_ub <- exp(res$ci.ub)
cat("\n--- Pooled Risk Ratio ---\n")
cat(sprintf("RR = %.3f (95%% CI: %.3f - %.3f)\n", pooled_rr, pooled_ci_lb, pooled_ci_ub))
cat(sprintf("Interpretation: BCG vaccination reduced TB risk by %.1f%% (95%% CI: %.1f%% - %.1f%%)\n",
            (1 - pooled_rr) * 100,
            (1 - pooled_ci_ub) * 100,
            (1 - pooled_ci_lb) * 100))

# ============================================================
# PART B: HETEROGENEITY ASSESSMENT
# ============================================================
cat("\n", rep("=", 60), "\n", sep = "")
cat("PART B: Heterogeneity Assessment\n")
cat(rep("=", 60), "\n", sep = "")

cat(sprintf("Q statistic: %.2f (df = %d, p %s)\n",
            res$QE, res$k - 1,
            ifelse(res$QEp < 0.001, "< 0.001", sprintf("= %.3f", res$QEp))))
cat(sprintf("I-squared: %.1f%%\n", res$I2))
cat(sprintf("tau-squared: %.4f (SE = %.4f)\n", res$tau2, res$se.tau2))
cat(sprintf("tau: %.4f\n", sqrt(res$tau2)))
cat(sprintf("H-squared: %.2f\n", res$H2))

# Prediction interval
pred <- predict(res)
cat(sprintf("\nPrediction interval (RR): %.3f - %.3f\n",
            exp(pred$pi.lb), exp(pred$pi.ub)))
cat("Interpretation: In a new study, the true RR would fall between",
    sprintf("%.3f and %.3f with 95%% probability\n", exp(pred$pi.lb), exp(pred$pi.ub)))

# ============================================================
# PART C: FOREST PLOT
# ============================================================
cat("\n", rep("=", 60), "\n", sep = "")
cat("PART C: Forest Plot\n")
cat(rep("=", 60), "\n", sep = "")

pdf("figures/forest_plot.pdf", width = 10, height = 7)
forest(res, slab = paste0(dat$author, " (", dat$year, ")"),
       atransf = exp,
       header = c("Study", "Risk Ratio [95% CI]"),
       xlab = "Risk Ratio (log scale)",
       mlab = sprintf("RE Model (I² = %.1f%%, p %s)",
                      res$I2,
                      ifelse(res$QEp < 0.001, "< 0.001", sprintf("= %.3f", res$QEp))),
       cex = 0.85, efac = 0.8)
dev.off()

png("figures/forest_plot.png", width = 10, height = 7, units = "in", res = 300)
forest(res, slab = paste0(dat$author, " (", dat$year, ")"),
       atransf = exp,
       header = c("Study", "Risk Ratio [95% CI]"),
       xlab = "Risk Ratio (log scale)",
       mlab = sprintf("RE Model (I² = %.1f%%, p %s)",
                      res$I2,
                      ifelse(res$QEp < 0.001, "< 0.001", sprintf("= %.3f", res$QEp))),
       cex = 0.85, efac = 0.8)
dev.off()
cat("Saved: figures/forest_plot.pdf\n")
cat("Saved: figures/forest_plot.png\n")

# ============================================================
# PART D: FUNNEL PLOT
# ============================================================
cat("\n", rep("=", 60), "\n", sep = "")
cat("PART D: Funnel Plot + Publication Bias\n")
cat(rep("=", 60), "\n", sep = "")

pdf("figures/funnel_plot.pdf", width = 7, height = 6)
funnel(res, xlab = "Log Risk Ratio", main = "Funnel Plot — BCG Vaccine Efficacy")
dev.off()

png("figures/funnel_plot.png", width = 7, height = 6, units = "in", res = 300)
funnel(res, xlab = "Log Risk Ratio", main = "Funnel Plot — BCG Vaccine Efficacy")
dev.off()
cat("Saved: figures/funnel_plot.pdf\n")
cat("Saved: figures/funnel_plot.png\n")

# Egger's test
cat("\n--- Egger's Regression Test ---\n")
egger <- regtest(res, model = "lm")
print(egger)

# Rank correlation test (Begg)
cat("\n--- Rank Correlation Test (Begg & Mazumdar) ---\n")
begg <- ranktest(res)
print(begg)

# Trim-and-fill
cat("\n--- Trim-and-Fill Analysis ---\n")
tf <- trimfill(res)
print(tf)
cat(sprintf("Trim-and-fill: %d studies imputed\n", tf$k0))
cat(sprintf("Adjusted RR: %.3f (95%% CI: %.3f - %.3f)\n",
            exp(coef(tf)), exp(tf$ci.lb), exp(tf$ci.ub)))

# Funnel plot with trim-and-fill
pdf("figures/funnel_trimfill.pdf", width = 7, height = 6)
funnel(tf, xlab = "Log Risk Ratio",
       main = "Funnel Plot with Trim-and-Fill Imputation")
dev.off()

png("figures/funnel_trimfill.png", width = 7, height = 6, units = "in", res = 300)
funnel(tf, xlab = "Log Risk Ratio",
       main = "Funnel Plot with Trim-and-Fill Imputation")
dev.off()
cat("Saved: figures/funnel_trimfill.pdf\n")
cat("Saved: figures/funnel_trimfill.png\n")

# ============================================================
# PART E: SUBGROUP ANALYSIS (by allocation method)
# ============================================================
cat("\n", rep("=", 60), "\n", sep = "")
cat("PART E: Subgroup Analysis (Allocation Method)\n")
cat(rep("=", 60), "\n", sep = "")

res_alloc <- rma(yi, vi, data = dat, mods = ~ alloc, method = "REML")
cat("\n")
print(summary(res_alloc))

# Subgroup-specific estimates
for (a in unique(dat$alloc)) {
  sub <- rma(yi, vi, data = dat, subset = (alloc == a), method = "REML")
  cat(sprintf("\n%s (k=%d): RR = %.3f (95%% CI: %.3f - %.3f), I² = %.1f%%\n",
              a, sub$k, exp(coef(sub)),
              exp(sub$ci.lb), exp(sub$ci.ub),
              sub$I2))
}

# ============================================================
# PART F: META-REGRESSION (absolute latitude)
# ============================================================
cat("\n", rep("=", 60), "\n", sep = "")
cat("PART F: Meta-Regression (Absolute Latitude)\n")
cat(rep("=", 60), "\n", sep = "")

res_lat <- rma(yi, vi, mods = ~ ablat, data = dat, method = "REML")
cat("\n")
print(summary(res_lat))
cat(sprintf("\nR-squared: %.1f%%\n", res_lat$R2))
cat(sprintf("Interpretation: Absolute latitude explains %.1f%% of between-study variance\n",
            res_lat$R2))

# Bubble plot
pdf("figures/bubble_plot.pdf", width = 7, height = 6)
regplot(res_lat, xlab = "Absolute Latitude",
        ylab = "Log Risk Ratio",
        main = "Meta-Regression: Vaccine Efficacy vs. Latitude",
        atransf = exp,
        pi = TRUE, legend = TRUE)
dev.off()

png("figures/bubble_plot.png", width = 7, height = 6, units = "in", res = 300)
regplot(res_lat, xlab = "Absolute Latitude",
        ylab = "Log Risk Ratio",
        main = "Meta-Regression: Vaccine Efficacy vs. Latitude",
        atransf = exp,
        pi = TRUE, legend = TRUE)
dev.off()
cat("Saved: figures/bubble_plot.pdf\n")
cat("Saved: figures/bubble_plot.png\n")

# ============================================================
# PART G: SENSITIVITY ANALYSIS (Leave-One-Out)
# ============================================================
cat("\n", rep("=", 60), "\n", sep = "")
cat("PART G: Sensitivity Analysis (Leave-One-Out)\n")
cat(rep("=", 60), "\n", sep = "")

loo <- leave1out(res)
loo_df <- data.frame(
  study = paste0(dat$author, " (", dat$year, ")"),
  RR = round(exp(loo$estimate), 3),
  ci.lb = round(exp(loo$ci.lb), 3),
  ci.ub = round(exp(loo$ci.ub), 3),
  I2 = round(loo$I2, 1),
  Q = round(loo$Q, 2),
  Qp = loo$Qp,
  stringsAsFactors = FALSE
)
cat("\n")
print(loo_df, digits = 3)

# Influential study detection
cat("\n--- Influence Diagnostics ---\n")
inf <- influence(res)
# Identify studies with externally standardized residual > 2
ext_res <- rstudent(res)
influential <- which(abs(ext_res$z) > 2)
if (length(influential) > 0) {
  cat("Potentially influential studies (|rstudent| > 2):\n")
  for (i in influential) {
    cat(sprintf("  %s (%d): rstudent = %.3f\n",
                dat$author[i], dat$year[i], ext_res$z[i]))
  }
} else {
  cat("No studies with |rstudent| > 2 detected.\n")
}

# ============================================================
# PART H: OUTPUT SUMMARY TABLE
# ============================================================
cat("\n", rep("=", 60), "\n", sep = "")
cat("PART H: Summary Results Table\n")
cat(rep("=", 60), "\n", sep = "")

# Per-study results
study_results <- data.frame(
  Study = paste0(dat$author, " (", dat$year, ")"),
  RR = round(exp(dat$yi), 3),
  CI_lower = round(exp(dat$yi - 1.96 * sqrt(dat$vi)), 3),
  CI_upper = round(exp(dat$yi + 1.96 * sqrt(dat$vi)), 3),
  Weight = round(weights(res), 1),
  Latitude = dat$ablat,
  Allocation = dat$alloc,
  stringsAsFactors = FALSE
)
write.csv(study_results, "output/study_results.csv", row.names = FALSE)
cat("Saved: output/study_results.csv\n")

# Summary table
summary_table <- data.frame(
  Analysis = c(
    "Overall (REML)",
    "Subgroup: random",
    "Subgroup: alternate",
    "Subgroup: systematic",
    "Trim-and-fill adjusted"
  ),
  k = c(res$k, NA, NA, NA, tf$k),
  RR = NA, CI_lower = NA, CI_upper = NA,
  I2 = NA, tau2 = NA,
  stringsAsFactors = FALSE
)

# Fill in overall
summary_table$RR[1] <- round(pooled_rr, 3)
summary_table$CI_lower[1] <- round(pooled_ci_lb, 3)
summary_table$CI_upper[1] <- round(pooled_ci_ub, 3)
summary_table$I2[1] <- round(res$I2, 1)
summary_table$tau2[1] <- round(res$tau2, 4)

# Subgroups
for (i in seq_along(unique(dat$alloc))) {
  a <- unique(dat$alloc)[i]
  sub <- rma(yi, vi, data = dat, subset = (alloc == a), method = "REML")
  summary_table$k[i + 1] <- sub$k
  summary_table$RR[i + 1] <- round(exp(coef(sub)), 3)
  summary_table$CI_lower[i + 1] <- round(exp(sub$ci.lb), 3)
  summary_table$CI_upper[i + 1] <- round(exp(sub$ci.ub), 3)
  summary_table$I2[i + 1] <- round(sub$I2, 1)
  summary_table$tau2[i + 1] <- round(sub$tau2, 4)
}

# Trim-and-fill
summary_table$RR[5] <- round(exp(coef(tf)), 3)
summary_table$CI_lower[5] <- round(exp(tf$ci.lb), 3)
summary_table$CI_upper[5] <- round(exp(tf$ci.ub), 3)
summary_table$I2[5] <- round(tf$I2, 1)
summary_table$tau2[5] <- round(tf$tau2, 4)

write.csv(summary_table, "output/summary_table.csv", row.names = FALSE)
cat("Saved: output/summary_table.csv\n")

# Meta-regression table
metareg_table <- data.frame(
  Covariate = c("Intercept", "Absolute latitude"),
  Estimate = round(coef(res_lat), 4),
  SE = round(res_lat$se, 4),
  z = round(res_lat$zval, 3),
  p = ifelse(res_lat$pval < 0.001, "<0.001", round(res_lat$pval, 3)),
  stringsAsFactors = FALSE
)
write.csv(metareg_table, "output/metaregression_table.csv", row.names = FALSE)
cat("Saved: output/metaregression_table.csv\n")

# ============================================================
# OUTPUT MANIFEST
# ============================================================
manifest <- paste0(
  "# Analysis Outputs\n",
  "Generated: ", Sys.Date(), "\n",
  "Study type: Meta-analysis (intervention, RCTs)\n\n",
  "## Tables\n",
  "- `output/study_results.csv` -- Per-study RR with 95% CI and weights\n",
  "- `output/summary_table.csv` -- Pooled estimates (overall, subgroup, trim-and-fill)\n",
  "- `output/metaregression_table.csv` -- Meta-regression coefficients\n\n",
  "## Figures\n",
  "- `figures/forest_plot.pdf` -- Forest plot (13 studies, REML)\n",
  "- `figures/funnel_plot.pdf` -- Funnel plot\n",
  "- `figures/funnel_trimfill.pdf` -- Funnel plot with trim-and-fill\n",
  "- `figures/bubble_plot.pdf` -- Meta-regression bubble plot (latitude)\n\n",
  "## Data\n",
  "- `data/bcg_raw.csv` -- Original dataset from metafor::dat.bcg\n"
)
writeLines(manifest, "output/_analysis_outputs.md")
cat("Saved: output/_analysis_outputs.md\n")

# ============================================================
# MANUSCRIPT-READY RESULTS TEXT
# ============================================================
cat("\n", rep("=", 60), "\n", sep = "")
cat("MANUSCRIPT-READY RESULTS TEXT\n")
cat(rep("=", 60), "\n\n", sep = "")

cat(sprintf(
  "A total of 13 randomized controlled trials (published %d-%d) were included ",
  min(dat$year), max(dat$year)))
cat(sprintf(
  "comprising %s vaccinated and %s control participants.\n\n",
  format(sum(dat$tpos + dat$tneg), big.mark = ","),
  format(sum(dat$cpos + dat$cneg), big.mark = ",")))

cat(sprintf(
  "The pooled risk ratio was %.3f (95%% CI: %.3f-%.3f), ",
  pooled_rr, pooled_ci_lb, pooled_ci_ub))
cat(sprintf(
  "indicating that BCG vaccination reduced the risk of tuberculosis by %.0f%% ",
  (1 - pooled_rr) * 100))
cat(sprintf(
  "(95%% CI: %.0f%%-%.0f%%) (Figure 1). ",
  (1 - pooled_ci_ub) * 100, (1 - pooled_ci_lb) * 100))
cat(sprintf(
  "Substantial heterogeneity was observed (I² = %.1f%%, Q = %.1f, p %s; tau² = %.4f).\n\n",
  res$I2, res$QE,
  ifelse(res$QEp < 0.001, "< 0.001", sprintf("= %.3f", res$QEp)),
  res$tau2))

cat("Meta-regression analysis revealed that absolute latitude was a significant moderator ")
cat(sprintf(
  "(coefficient = %.4f, SE = %.4f, p %s), explaining %.1f%% of between-study variance. ",
  coef(res_lat)[2], res_lat$se[2],
  ifelse(res_lat$pval[2] < 0.001, "< 0.001", sprintf("= %.3f", res_lat$pval[2])),
  res_lat$R2))
cat("Studies conducted at higher latitudes showed greater vaccine efficacy (Figure 3).\n\n")

cat(sprintf(
  "Egger's regression test showed %s evidence of funnel plot asymmetry (p %s). ",
  ifelse(egger$pval < 0.05, "significant", "no significant"),
  ifelse(egger$pval < 0.001, "< 0.001", sprintf("= %.3f", egger$pval))))
cat(sprintf(
  "Trim-and-fill analysis imputed %d additional studies, yielding an adjusted RR of %.3f ",
  tf$k0, exp(coef(tf))))
cat(sprintf(
  "(95%% CI: %.3f-%.3f), which remained statistically significant.\n",
  exp(tf$ci.lb), exp(tf$ci.ub)))

cat("\n", rep("=", 60), "\n", sep = "")
cat("ANALYSIS COMPLETE\n")
cat(rep("=", 60), "\n", sep = "")
