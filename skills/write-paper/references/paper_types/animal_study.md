# Paper Type: Animal Study

## Overview

- **Reporting guideline:** ARRIVE 2.0 (2020) — mandatory
- **Ethical approval:** IACUC (Institutional Animal Care and Use Committee) approval number required
- **Typical word count:** 3500–5000 words
- **Structure:** Abstract → Introduction → Materials and Methods → Results → Discussion → Conclusions
- **Key requirement:** 3Rs (Replacement, Reduction, Refinement) statement in Methods

---

## ARRIVE 2.0 — Essential 10 Items

These 10 items are the minimum required for publication. **All must be present.**

| # | Item | Where in Paper |
|---|------|----------------|
| 1 | Study design | Methods: Study Design |
| 2 | Sample size | Methods: Sample Size |
| 3 | Inclusion/exclusion criteria | Methods: Animals |
| 4 | Randomization | Methods: Randomization |
| 5 | Blinding | Methods: Blinding |
| 6 | Outcome measures | Methods: Outcome Measures |
| 7 | Statistical methods | Methods: Statistical Analysis |
| 8 | Experimental animals | Methods: Animals |
| 9 | Experimental procedures | Methods: Procedures |
| 10 | Results | Results section |

---

## Structured Abstract (250 words)

```
Background: [Scientific rationale; why this animal model was used]
Objective: [Specific aim and hypothesis]
Methods: [Species, strain, sex, N per group, intervention, primary outcome,
          statistical test]
Results: [Primary outcome with effect size, 95% CI, and exact p-value]
Conclusions: [Main finding and translational implication]
```

---

## Introduction (400–600 words)

1. **Clinical/biological problem:** Why does this research question matter?
2. **Gap in knowledge:** What is unknown and why animal work is needed to address it.
3. **Rationale for animal model:** Why was this species/model chosen? What aspects of the human condition does it recapitulate? Cite validation literature for the model.
4. **Hypothesis and aims:** State explicitly. "We hypothesized that [X]. To test this, we [aim 1], [aim 2], [aim 3]."
5. **3Rs statement:** "All procedures were performed in accordance with the 3Rs principles (Replacement, Reduction, Refinement)."

---

## Materials and Methods (1200–1800 words)

### 2.1 Ethical Approval

"All animal experiments were approved by the Institutional Animal Care and Use Committee of [Institution] (protocol number [XXXXX]) and conducted in accordance with the [National Institutes of Health Guide for the Care and Use of Laboratory Animals / Korean Animal Protection Act / relevant local regulation]."

### 2.2 Animals (ARRIVE Essential Item 8)

Report all of the following:
- Species, strain, substrain (e.g., Sprague-Dawley rat, Charles River, Wilmington, MA)
- Source (commercial vendor or in-house breeding)
- Sex (justify if single sex: biological rationale required)
- Age and weight at the start of the experiment (mean ± SD or range)
- Health status (specific pathogen-free, germ-free, etc.)
- Any genetic modification (full genotype for transgenic models)

### 2.3 Housing and Husbandry (ARRIVE Recommended)

- Housing conditions: cage type, group or individually housed, N per cage
- Environmental conditions: temperature (°C), humidity (%), light cycle (e.g., 12h light/12h dark, lights on at 07:00)
- Access to food and water (ad libitum or restricted; specify diet)
- Acclimatization period before experiment
- Any enrichment provided

### 2.4 Study Design (ARRIVE Essential Item 1)

State clearly:
- Design type: parallel group, crossover, factorial
- Control groups: sham, vehicle, naïve
- Number of experimental groups and treatment allocations
- Timeline (from baseline to final outcome measurement)

Include a figure showing the experimental design timeline if complex.

### 2.5 Sample Size Justification (ARRIVE Essential Item 2)

**Required.** Calculate using G*Power or equivalent. Report:
- Effect size expected (based on pilot data or literature)
- α (0.05) and β (0.20, i.e., 80% power)
- Formula used
- Calculated N per group
- Inflation for expected attrition (typically +15–20%)

"Sample size was estimated using G*Power (version 3.1.9.7) based on a two-sample t-test with an expected effect size of Cohen's d = [X] (derived from [pilot data/[Author Year]]). With α = 0.05 and 80% power, [N] animals per group were required. Accounting for an estimated [15]% attrition, [N] animals per group were enrolled."

### 2.6 Inclusion and Exclusion Criteria (ARRIVE Essential Item 3)

State pre-specified criteria applied at the time of animal selection AND during the experiment. Common exclusion reasons: failure to reach surgical endpoint, infection, weight loss >20%, death before planned outcome measurement.

"Animals were excluded if: (a) they failed to recover from anesthesia, (b) technical failure of the intervention occurred, or (c) the primary outcome could not be measured. All exclusions were recorded in the study log."

### 2.7 Randomization (ARRIVE Essential Item 4)

"Animals were randomly allocated to treatment groups using [computer-generated random numbers / block randomization / stratified randomization] with block size [N]. Allocation was performed by [person] who was not involved in [surgery/treatment/outcome assessment]."

If randomization was not performed, justify.

### 2.8 Blinding (ARRIVE Essential Item 5)

"Outcome assessment was performed by [role] who was blinded to group allocation. [Describe specifically what was blinded at each stage: surgery, treatment, outcome assessment, statistical analysis.]"

If full blinding was not possible, explain why and what steps were taken to minimize bias.

### 2.9 Anesthesia and Procedures (ARRIVE Essential Item 9)

- Anesthetic agent, dose, route (e.g., isoflurane 2–3% via inhalation, ketamine 80 mg/kg + xylazine 10 mg/kg i.p.)
- Monitoring during anesthesia (temperature, heart rate, respiratory rate)
- Analgesia (pre- and post-operative)
- Humane endpoints: criteria for euthanasia
- Specific surgical or experimental procedure: describe in enough detail for replication

### 2.10 Outcome Measures (ARRIVE Essential Item 6)

For each outcome:
- Primary or secondary
- Operational definition
- Measurement method and equipment (manufacturer, location)
- Timing of measurements
- Observer reliability (if applicable: ICC, kappa)

### 2.11 Statistical Analysis (ARRIVE Essential Item 7)

- State the primary outcome and the test used for the primary analysis
- Parametric vs. non-parametric decision (justify based on distribution)
- Mixed-effects models for repeated measures (preferred over repeated ANOVA)
- Correction for multiple comparisons (Bonferroni, FDR — state which and why)
- Handling of missing data
- Software: R (version X.X.X) or SPSS (version X.X); packages used
- Significance threshold: α = 0.05 (two-tailed)

---

## Results (900–1200 words)

### 3.1 Animal Attrition

Report in a CONSORT-style flow diagram or table:
- Animals enrolled
- Animals excluded (reason)
- Animals analyzed per group

"Of [N] enrolled animals, [N] were excluded: [N] due to [reason 1], [N] due to [reason 2]. Final analysis included [N] animals per group."

### 3.2 Baseline Characteristics

Table comparing groups at baseline (weight, age, any baseline measurements). Include statistical comparison — groups should be comparable.

### 3.3 Primary Outcome

Report: mean ± SD (or median [IQR]) for each group. Effect size with 95% CI. Exact p-value.

"[Primary outcome] was significantly [higher/lower] in [Group A] compared with [Group B] ([mean ± SD] vs. [mean ± SD]; difference, [X] [units]; 95% CI, [lower–upper]; P = [exact value])."

### 3.4 Secondary Outcomes and Adverse Events

Report all pre-specified secondary outcomes. **Always report adverse events** (infections, weight loss, unexpected deaths) even if none occurred: "No adverse events were observed during the study period."

---

## Discussion (600–800 words)

1. Summary of main findings (with effect size)
2. Mechanistic interpretation
3. Comparison with previous animal studies of same model or intervention
4. Translational relevance: how do findings relate to the human condition?
5. Limitations: model limitations (does not fully recapitulate human disease), single sex (if applicable), limited follow-up, sample size
6. Future directions

---

## Common Animal Study Pitfalls

1. **Missing IACUC number** — always required; reviewers check this.
2. **No sample size justification** — G*Power calculation is mandatory.
3. **Not reporting sex** — increasing pressure to include both sexes or justify exclusion.
4. **Confounding housing conditions** — different cages, litters, or technicians are confounders; report and control.
5. **Outcome assessor not blinded** — blinding of outcome assessment is the most important bias control in animal studies.
6. **Inconsistent or missing humane endpoints** — specify pre-determined criteria for euthanasia.
7. **Reporting group means without individual data points** — show individual data (dot plots) for small N.
8. **Using repeated ANOVA without accounting for sphericity** — use linear mixed-effects models instead.
