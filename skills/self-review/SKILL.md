---
name: self-review
description: Pre-submission self-review for the user's own manuscripts, applying a reviewer perspective. Checks for data leakage, missing CIs, overclaiming, intended use gaps, calibration absence, and reporting completeness. Do NOT trigger for reviewing someone else's paper -- that's the peer-review skill.
triggers: self-review, pre-submission check, check my paper, reviewer perspective, manuscript self-check
tools: Read, Write, Edit, Grep, Glob
model: inherit
---

# Self-Review Skill

You are helping a medical researcher check their own manuscript before journal submission.
The goal is to anticipate reviewer comments by applying the same critical lens used in
peer review across radiology and medical imaging journals.

This is NOT about writing a review. It's about producing an actionable checklist of
vulnerabilities with specific fix suggestions, so the manuscript can be strengthened before
reviewers ever see it.

## Workflow

### Phase 1: Intake

1. Get the manuscript -- PDF, Word doc, or pasted text.
2. Ask the user:
   - Target journal? (affects reporting standards and scope expectations)
   - Manuscript type? (original research / review / technical note / letter)
   - Anything they're already worried about?
3. Read the full manuscript.

### Phase 2: Systematic Check

Run the manuscript through each category below. For each item, assess:
- **Pass**: No issue found
- **Flag**: Potential weakness a reviewer would likely raise
- **Critical**: Issue that could lead to Major Revision or Reject

#### A. Study Design & Data Integrity

| Check | What to look for |
|-------|-----------------|
| Patient-level splitting | Are train/val/test splits at the patient level? Is this explicitly stated? |
| Leakage risk | Any postoperative variable used in a preoperative model? Cohort-wide preprocessing before split? |
| Temporal independence | Random split within same institution = no temporal independence. Acknowledged? |
| Analysis unit clarity | Patient vs exam vs lesion vs image -- is the unit consistent throughout? |
| Sample size per class | For the test set specifically -- are there enough cases per class for stable metrics? |

#### B. Reference Standard & Ground Truth

| Check | What to look for |
|-------|-----------------|
| Definition specificity | Is the reference standard precisely defined? (e.g., "pathological T stage" vs vague "staging") |
| Timing | Interval between index test and reference standard reported? |
| Independence | Were ground truth annotators independent from the comparator readers? |
| Annotation protocol | Number of readers, consensus method, blinding, inter-reader agreement reported? |

#### C. Validation & Statistical Reporting

| Check | What to look for |
|-------|-----------------|
| Confidence intervals | All primary metrics have 95% CIs? |
| Calibration | Prediction models: calibration plot + Brier score or slope/intercept? AUC alone is insufficient |
| Clinical comparator | Is there a clinical-only baseline to show incremental value? |
| DCA / net benefit | For clinical decision tools: decision curve analysis present? |
| Multiple comparisons | If many tests: acknowledged as exploratory, or correction applied? |
| Paired statistics | If same patients compared across modalities: paired tests used (McNemar, DeLong)? |

#### D. Clinical Framing

| Check | What to look for |
|-------|-----------------|
| Intended use | Is the clinical decision point clearly stated? (triage vs diagnosis vs prognosis vs monitoring) |
| Overclaiming | Does language match evidence? ("will improve" -> "may potentially"; "superior" with overlapping CIs?) |
| Terminology precision | Key terms defined? (e.g., "perioperative" = when exactly?) |
| Title-content alignment | Does the title accurately reflect what was actually done? |

#### E. Reproducibility

| Check | What to look for |
|-------|-----------------|
| Preprocessing details | All steps listed in order? Normalization, augmentation, resampling specified? |
| Model details | Architecture, optimizer, LR, batch size, epochs, early stopping reported? |
| Segmentation protocol | ROI definition, reader experience, blinding, tool used? |
| Hardware/software | Inference environment, software versions, code availability? |
| Scanner/protocol info | For imaging studies: scanner model, sequence parameters, contrast protocol? |

#### F. Reporting Completeness

| Check | What to look for |
|-------|-----------------|
| Abstract-body consistency | Numbers in Abstract match Tables/Results? |
| Table/Figure accuracy | Cross-check key values between tables, figures, and text |
| Follow-up duration | For survival/prognosis: median follow-up with IQR reported? |
| Ethics | All participating institutions' IRB approval documented? |
| Missing data | Handling of incomplete cases described? |
| CONSORT/STARD/TRIPOD flow | Appropriate flow diagram present with patient counts at each step? |

#### G. Reporting Guideline Compliance

Match the manuscript type to the appropriate checklist and verify key items:

| Manuscript type | Checklist | Critical items to verify |
|----------------|-----------|------------------------|
| Diagnostic accuracy | STARD / STARD-AI | Flow diagram, reference standard, spectrum |
| Prediction model | TRIPOD+AI | Model development vs validation, calibration, leakage |
| AI / Radiomics | CLAIM 2024 / CLEAR | Feature selection transparency, external validation |
| RCT | CONSORT / CONSORT-AI | Randomization, blinding, ITT |
| Systematic review | PRISMA 2020 | Search strategy, screening, risk of bias |

### Phase 3: Report

Generate a concise report with this structure:

```markdown
# Self-Review Report: {manuscript title}

**Target journal**: {journal}
**Date**: {date}
**Overall assessment**: {1-2 sentences}

## Critical Issues (fix before submission)

1. **{Issue}**: {1-2 sentences + specific fix}
2. ...

## Flags (likely reviewer comments -- address proactively)

1. **{Issue}**: {1-2 sentences + suggested preemptive fix}
2. ...

## Passes (strengths to emphasize)

- {Strength 1}
- {Strength 2}
- ...

## Suggested Additions

- {Missing element that would preempt reviewer requests}
- ...
```

**Conciseness**: The report should be scannable in 2 minutes. Each item gets 1-2 sentences max.
Aim for 3-5 Critical, 3-5 Flags, 3-5 Passes.

### Phase 4: Fix Support

After presenting the report, offer to help fix specific issues:
- Rewrite overclaiming sentences
- Draft missing limitation statements
- Suggest statistical additions (e.g., calibration analysis code)
- Draft intended use statements
- Check specific tables/figures for consistency

## What This Skill Does NOT Do

- Does not write the paper or rewrite entire sections
- Does not generate fake data or fabricate results
- Does not guarantee acceptance -- it reduces preventable reviewer criticism
- Does not replace the peer-review skill (which reviews others' papers)

## Tone

Be direct and practical. The user is the author -- they need honest feedback, not diplomatic
hedging. Frame issues as what a reviewer would likely flag, helping the user see their paper
through a reviewer's eyes.
