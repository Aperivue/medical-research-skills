---
name: design-study
description: >
  Study design and validity review for radiology and medical AI research. Identifies analysis unit,
  cohort logic, leakage risks, comparator design, validation strategy, and reporting guideline fit before
  drafting or submission.
triggers: study design, leakage check, cohort design, analysis plan, validation strategy, comparator design, bias check
tools: Read, Write, Edit, Bash, Grep, Glob
model: inherit
---

# Design-Study Skill

## Purpose

This skill pressure-tests whether a study is answerable, interpretable, and defensible before large amounts of drafting or analysis work accumulate.

Use it when:
- a study question is known but the analysis plan is still fluid
- the user wants a methods sanity check
- a manuscript feels vulnerable to reviewer criticism
- a peer review requires explicit methodological diagnosis

---

## Communication Rules

- Communicate with the user in their preferred language.
- Use English for statistical, radiologic, and reporting-guideline terminology.
- Be direct about validity risks, but always propose the smallest feasible fix first.

---

## Core Review Questions

Always inspect these dimensions:

1. What is the exact research question?
2. What is the analysis unit: patient, lesion, exam, study, phase, report?
3. What is the index date or decision point?
4. How are inclusion and exclusion criteria applied?
5. Is there any information leakage?
6. What is the reference standard or endpoint definition?
7. What comparator is clinically meaningful?
8. What validation strategy is used?
9. What uncertainty reporting is required?
10. Which reporting guideline best fits?
11. Are exposure/outcome/covariate **definitions literature-grounded**, or invented ad-hoc from the data dictionary? If ad-hoc, defer to `/define-variables` before drafting Methods.

---

## Standard Output

```text
## Study Design Review
Question: ...
Study type: ...
Analysis unit: ...
Index date / prediction timepoint: ...

### Strengths
- ...

### Major validity risks
1. ...
2. ...

### Minimal fixes
- ...

### Reporting fit
- Recommended guideline: ...

### Decision
- Ready for analysis / Needs redesign / Drafting can proceed with limitations
```

---

## Workflow

### Phase 1: Reconstruct the study

Extract from protocol, draft, slides, tables, or notes:
- clinical problem
- intended use case
- population
- inputs
- outputs
- outcome definition
- timing of variable availability

**Gate:** Present the reconstructed study summary (question, analysis unit, intended use)
to the user. Confirm before proceeding — if the reconstruction is wrong, the entire
validity review will be misdirected.

### Phase 2: Check structural validity

#### A. Analysis unit

Look for mismatches such as:
- patient-level claim from lesion-level analysis
- exam-level split with patient overlap
- phase-level samples treated as independent

#### B. Leakage

Look for:
- postoperative features used for preoperative prediction
- normalization or thresholding performed before data split
- repeated exams across train/test
- reader annotations derived from outcome information

#### C. Reference standard

Check:
- who established ground truth
- when it was established
- whether blinding was possible
- whether only a subset had gold standard verification

#### D. Validation

Classify:
- apparent only
- internal split
- cross-validation
- temporal validation
- external validation
- multi-center external validation

### Phase 3: Clinical framing

Ask whether the comparator and endpoint support the stated claim:
- is the model better than current practice or just another model?
- is the endpoint clinically meaningful?
- does performance translate to action?

### Phase 4: Reporting fit

Recommend one primary guideline:
- `TRIPOD-AI`
- `CLAIM`
- `STARD`
- `STROBE`
- `PRISMA`
- `CARE`
- `ARRIVE`
- journal-specific additions if needed

---

## Frequent Failure Modes

### Diagnostic AI
- no clinically relevant comparator
- exam-level split instead of patient-level split
- unclear reference standard
- AUROC-only reporting without threshold metrics

### Prognostic modeling
- unclear time zero
- immortal time bias
- feature timing mismatch
- no calibration

### Retrospective cohort / screening database
- **time zero misalignment**: cohort entry ≠ follow-up start → immortal time bias
- interval-censored outcomes treated as exact → underestimation of event times
- healthy volunteer bias unacknowledged → inflated external validity claims
- surveillance bias from unequal follow-up frequency between groups
- **3 bias classification (Hernan/Robins)**: selection bias (who enters), information bias (how measured), confounding (what else differs) — explicitly map each threat

### Multimodal LLM / report generation
- no clear rubric for clinical correctness
- benchmark labels derived from noisy reports without adjudication
- unsupported claims about safety or workflow benefit

### Imaging meta-analysis
- overlapping cohorts
- paired modalities analyzed as independent
- heterogeneity metrics missing
- zero-cell handling unspecified

---

## Minimal-Fix Principle

Whenever possible, recommend the smallest feasible repair first:

- clarify the claim
- narrow the target population
- add a limitation statement
- add a clinically relevant baseline
- re-run one key sensitivity analysis
- redefine the endpoint more explicitly

Escalate to redesign only when the central claim is not defensible otherwise.

---

## Handoff Rules

- route to `analyze-stats` when the design is basically sound but analysis details need refinement
- route to `check-reporting` after the design is locked
- route to `self-review` when the user wants a pre-submission quality check on their own manuscript
- route back to `write-paper` only after the main validity risks are documented

---

## What This Skill Does NOT Do

- It does not compute statistics directly
- It does not draft full manuscript prose
- It does not resolve raw data engineering issues
- It does not replace a full peer review when journal-facing tone is required

## Anti-Hallucination

- **Never fabricate references.** All citations must be verified via `/search-lit` with confirmed DOI or PMID. Mark unverified references as `[UNVERIFIED - NEEDS MANUAL CHECK]`.
- **Never invent clinical definitions, diagnostic criteria, or guideline recommendations.** If uncertain, flag with `[VERIFY]` and ask the user.
- **Never fabricate numerical results** — compliance percentages, scores, effect sizes, or sample sizes must come from actual data or analysis output.
- If a reporting guideline item, journal policy, or clinical standard is uncertain, state the uncertainty rather than guessing.
