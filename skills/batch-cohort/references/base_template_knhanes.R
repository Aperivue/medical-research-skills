#!/usr/bin/env Rscript
# ==============================================================================
# KNHANES Survey-Weighted Logistic Regression — Batch Template
# Combo: {{COMBO_ID}} | {{EXPOSURE_LABEL}} → {{OUTCOME_LABEL}}
#
# Slot variables (replaced by batch_template_generator.R):
#   {{EXPOSURE_VAR}}, {{EXPOSURE_LABEL}}, {{EXPOSURE_CODING}}
#   {{OUTCOME_VAR}}, {{OUTCOME_LABEL}}, {{OUTCOME_CODING}}
#   {{RESULTS_DIR}}, {{COMBO_ID}}, {{COVARIATES_REMOVE}}
#
# Data: KNHANES single-cycle CSV (e.g., HN18.csv)
# ==============================================================================

suppressPackageStartupMessages({
  library(survey)
  library(dplyr)
  library(tidyr)
})

# --- CONFIG (edit these paths for your setup) ---
DATA_PATH     <- "{{DATA_PATH}}"       # e.g., /path/to/HN18.csv
RESULTS_DIR   <- "{{RESULTS_DIR}}"
COMBO_ID      <- "{{COMBO_ID}}"
AGE_MIN       <- 20
AGE_MAX       <- Inf

# --- Standard Covariates ---
# Full set; exposure-specific removals applied below
ALL_COVARIATES <- c("age", "sex_binary", "edu_binary", "income_binary",
                     "smoking_3cat", "alcohol_3cat", "obesity_binary", "cvd_binary")
REMOVE_COVARS  <- c({{COVARIATES_REMOVE}})
COVARIATES     <- setdiff(ALL_COVARIATES, REMOVE_COVARS)

# --- Load & Clean ---
raw <- read.csv(DATA_PATH)

df <- raw %>%
  filter(age >= AGE_MIN, age <= AGE_MAX) %>%
  mutate(
    # --- Demographics ---
    sex_binary     = ifelse(sex == 1, 0, 1),  # 0=male, 1=female
    edu_binary     = ifelse(edu %in% 1:3, 0, 1),  # 0=non-college, 1=college
    income_binary  = ifelse(incm %in% 1:3, 0, 1),  # 0=bottom80, 1=top20

    # --- Standard Covariates ---
    smoking_3cat = case_when(
      BS3_1 %in% c(1, 2) ~ "current",
      BS3_1 == 3          ~ "former",
      BS3_1 == 8          ~ "never",
      TRUE                ~ NA_character_
    ),
    alcohol_3cat = case_when(
      BD1_11 %in% 2:6 ~ "frequent",
      BD1_11 == 1      ~ "occasional",
      BD1_11 == 8      ~ "never",
      TRUE             ~ NA_character_
    ),
    obesity_binary = ifelse(HE_obe >= 4, 1, 0),
    cvd_binary     = ifelse(DI4_dg == 1 | DI5_dg == 1 | DI6_dg == 1, 1, 0),

    # --- Exposure (SLOT) ---
    exposure = {{EXPOSURE_CODING}},

    # --- Outcome (SLOT) ---
    outcome = {{OUTCOME_CODING}}
  ) %>%
  filter(!is.na(exposure), !is.na(outcome))

cat(sprintf("[%s] N after filtering: %d (exposure=1: %d, outcome=1: %d)\n",
            COMBO_ID, nrow(df), sum(df$exposure == 1), sum(df$outcome == 1)))

# --- EPV Check ---
n_events <- min(sum(df$outcome == 1), sum(df$outcome == 0))
n_params <- length(COVARIATES) + 1  # +1 for exposure
epv <- n_events / n_params
if (epv < 10) {
  warning(sprintf("[%s] EPV = %.1f (< 10). Results may be unreliable.", COMBO_ID, epv))
}

# --- Survey Design ---
design <- svydesign(
  id      = ~psu,
  strata  = ~kstrata,
  weights = ~wt_itvex,
  nest    = TRUE,
  data    = df
)

# --- Table 1: Weighted Demographics by Exposure ---
table1_vars <- c("age", "sex_binary", "edu_binary", "income_binary",
                 "smoking_3cat", "alcohol_3cat", "obesity_binary", "cvd_binary", "outcome")

table1_rows <- lapply(table1_vars, function(v) {
  tryCatch({
    if (is.numeric(df[[v]])) {
      means <- svyby(as.formula(paste0("~", v)), ~exposure, design, svymean, na.rm = TRUE)
      data.frame(variable = v,
                 unexposed_mean = means[means$exposure == 0, v],
                 exposed_mean   = means[means$exposure == 1, v],
                 stringsAsFactors = FALSE)
    } else {
      props <- svyby(as.formula(paste0("~factor(", v, ")")), ~exposure, design, svymean, na.rm = TRUE)
      data.frame(variable = paste0(v, "_", names(props)[-1]),
                 unexposed_mean = as.numeric(props[props$exposure == 0, -1]),
                 exposed_mean   = as.numeric(props[props$exposure == 1, -1]),
                 stringsAsFactors = FALSE)
    }
  }, error = function(e) NULL)
})
table1 <- do.call(rbind, Filter(Negate(is.null), table1_rows))
write.csv(table1, file.path(RESULTS_DIR, "table1.csv"), row.names = FALSE)

# --- Helper: extract OR + CI + p from svyglm ---
extract_or <- function(model) {
  or_val  <- unname(exp(coef(model)["exposure"]))
  ci_vals <- unname(exp(confint(model))["exposure", ])
  p_val   <- unname(summary(model)$coefficients["exposure", "Pr(>|t|)"])
  c(OR = or_val, lower = ci_vals[1], upper = ci_vals[2], p = p_val)
}

# --- Main Analysis: Sequential Models ---
results <- list()

# Model 1: Unadjusted
m1 <- svyglm(outcome ~ exposure, design = design, family = quasibinomial())
results[["Model 1 (unadjusted)"]] <- extract_or(m1)

# Model 2: Age + Sex
m2 <- svyglm(outcome ~ exposure + age + sex_binary, design = design, family = quasibinomial())
results[["Model 2 (age+sex)"]] <- extract_or(m2)

# Model 3: Fully adjusted
formula_full <- as.formula(paste("outcome ~ exposure +", paste(COVARIATES, collapse = " + ")))
m3 <- svyglm(formula_full, design = design, family = quasibinomial())
results[["Model 3 (fully adjusted)"]] <- extract_or(m3)

# Save main results
main_df <- data.frame(
  combo_id = COMBO_ID,
  exposure = "{{EXPOSURE_LABEL}}",
  outcome  = "{{OUTCOME_LABEL}}",
  model    = names(results),
  N        = nrow(df),
  events   = sum(df$outcome == 1),
  OR       = sapply(results, `[`, "OR"),
  lower    = sapply(results, `[`, "lower"),
  upper    = sapply(results, `[`, "upper"),
  p_value  = sapply(results, `[`, "p"),
  row.names = NULL
)
write.csv(main_df, file.path(RESULTS_DIR, "main_results.csv"), row.names = FALSE)

# --- Subgroup Analyses (Model 3 within strata) ---
subgroup_vars <- list(
  sex     = list(var = "sex_binary", levels = c(0, 1), labels = c("Male", "Female")),
  age_grp = list(var = "age_group",  levels = c("20-39", "40-59", "60+"), labels = NULL),
  edu     = list(var = "edu_binary", levels = c(0, 1), labels = c("Non-college", "College")),
  income  = list(var = "income_binary", levels = c(0, 1), labels = c("Lower", "Higher"))
)

# Create age groups
df$age_group <- cut(df$age, breaks = c(20, 40, 60, Inf), right = FALSE,
                    labels = c("20-39", "40-59", "60+"))
design <- update(design, age_group = df$age_group)

subgroup_results <- list()
for (sg_name in names(subgroup_vars)) {
  sg <- subgroup_vars[[sg_name]]
  for (lev in sg$levels) {
    tryCatch({
      sub_design <- subset(design, get(sg$var) == lev)
      n_sub <- nrow(sub_design$variables)
      n_events_sub <- sum(sub_design$variables$outcome == 1)

      if (n_sub >= 30 && n_events_sub >= 5) {
        # Reduced model for subgroups (fewer covariates to avoid convergence issues)
        sg_covars <- setdiff(COVARIATES, sg$var)
        sg_formula <- as.formula(paste("outcome ~ exposure +", paste(sg_covars, collapse = " + ")))
        m_sg <- svyglm(sg_formula, design = sub_design, family = quasibinomial())
        r_sg <- extract_or(m_sg)

        subgroup_results[[length(subgroup_results) + 1]] <- data.frame(
          combo_id  = COMBO_ID,
          exposure  = "{{EXPOSURE_LABEL}}",
          outcome   = "{{OUTCOME_LABEL}}",
          subgroup  = sg_name,
          level     = as.character(lev),
          N         = n_sub,
          events    = n_events_sub,
          OR        = r_sg["OR"],
          lower     = r_sg["lower"],
          upper     = r_sg["upper"],
          p_value   = r_sg["p"],
          row.names = NULL
        )
      }
    }, error = function(e) {
      message(sprintf("[%s] Subgroup %s=%s failed: %s", COMBO_ID, sg_name, lev, e$message))
    })
  }
}

if (length(subgroup_results) > 0) {
  subgroup_df <- do.call(rbind, subgroup_results)
  write.csv(subgroup_df, file.path(RESULTS_DIR, "subgroup_results.csv"), row.names = FALSE)
}

cat(sprintf("[%s] Complete. Fully adjusted wOR: %.2f (%.2f–%.2f), p=%.3f\n",
            COMBO_ID,
            main_df$OR[3], main_df$lower[3], main_df$upper[3], main_df$p_value[3]))
