# Results Writing Guide

Reference for write-paper Phase 4 (Results).
Loaded on-demand when drafting the Results section.

---

## Core Principle: Mirror Symmetry with Methods

Results must follow the same order as Materials and Methods. Each M&M subsection
should have a corresponding Results subsection. If Methods describes the population
first, then the index test, then statistical analysis — Results presents population
characteristics first, then index test findings, then statistical comparisons.

| M&M Order | Results Counterpart |
|-----------|-------------------|
| Study population / Participants | Figure 1 (Flowchart) + Table 1 (Baseline characteristics) |
| Image analysis / Index test | Main diagnostic/measurement results |
| Statistical analysis methods | P-values, effect sizes, comparisons |

---

## Required Elements

### 1. Flowchart (Figure 1)

- Always present a patient flow diagram as Figure 1
- Numbers must be internally consistent across: Abstract, Methods, Results text, Tables, and the flowchart itself
- Show: initial cohort → exclusions (with reasons and counts) → final analysis set
- If applicable, show train/validation/test splits

### 2. Baseline Characteristics (Table 1)

- Present demographics and clinical characteristics of the study population
- Decimal places must be consistent throughout (pick one convention and hold it)
- Use footnotes for abbreviations and explanations
- Keep it concise — only variables relevant to the study

### 3. Main Results

- Present primary endpoint results first, then secondary endpoints
- Every result must include:
  - The metric value
  - 95% confidence interval (for primary endpoints)
  - Exact p-value (not "p < 0.05" unless truly < 0.001)
- Reference every Table and Figure at least once in the text

### 4. Figures

- Use the minimum number of figures that convey the key findings
- Each figure must be clear and high-resolution
- Representative cases: select typical examples, not cherry-picked best cases

---

## Strict Rules

### No Interpretation

Results contains **only factual findings**. Apply this self-check to every sentence:

1. Does this sentence explain "why"? → Move to Discussion
2. Does it reference another study? → Move to Discussion
3. Does it use "suggests" / "implies" / "indicates importance"? → Rewrite as factual statement
4. Does it use an evaluative adjective without a number ("high", "notable", "remarkable")? → Add the number or delete the adjective
5. Does it contain "interestingly" / "notably" / "remarkably" / "surprisingly"? → Delete the word

### No Unannounced Data

- **Data not described in Methods cannot appear in Results**
- If you discover an important finding during analysis that was not pre-specified, either:
  - Add the method to M&M (and note it as post-hoc)
  - Place it in Supplementary Materials

### Missing Data Handling

- Never leave table cells blank
- Use "NA" (not available) for missing data
- Add a footnote: "NA = not available" or "Data not available for N patients because [reason]"

### Tense

- **Text**: Past tense ("The sensitivity was 0.92")
- **Tables and Figures**: Present tense ("Table 1 shows...")

---

## Number Consistency Verification

Before finalizing Results, verify these cross-references:

| Check | Sources that Must Match |
|-------|----------------------|
| Total N | Abstract, Methods text, Figure 1, Table 1, Results text |
| Exclusion counts | Figure 1 boxes, Methods exclusion criteria |
| Subgroup N | Sum of subgroups = total N (or explain discrepancy) |
| Percentages | Numerator/denominator math verified |
| Primary metric | Abstract Results, Results text, relevant Table |

---

## Self-Check

Before finalizing Results:

- [ ] Follows the same order as Methods?
- [ ] Flowchart present with internally consistent numbers?
- [ ] Table 1 present with consistent decimal places?
- [ ] All primary endpoints have 95% CI and exact p-values?
- [ ] Every Table and Figure referenced in the text?
- [ ] Zero interpretation (no "why", no literature comparisons)?
- [ ] No blank cells in tables (NA with footnote instead)?
- [ ] All data in Results was described in Methods?
