# Paper Type: Technical Note

## Overview

- **Purpose:** Describe a novel technique, method, algorithm, or device — NOT clinical outcomes
- **Typical word count:** 1500–2500 words
- **Structure:** Abstract (unstructured or brief structured) → Introduction → Materials and Methods → Results (proof of concept) → Discussion → Conclusion
- **Key requirement:** Sufficient reproducibility data; must demonstrate feasibility, not efficacy

---

## What a Technical Note Is (and Is Not)

**IS:** A concise description of a new technique, workflow, algorithm, software tool, or modified procedure, with proof-of-concept validation data.

**IS NOT:** A clinical efficacy study. Technical notes do not aim to demonstrate that a new technique is better than existing ones — that requires a full original article with appropriate controls and statistical power.

---

## Abstract (150–200 words, unstructured or brief structured)

"We describe [technique/method/tool] for [application]. [One sentence on how it works]. Using [validation dataset / N cases / N samples], we demonstrated [key performance metric with value]. [One sentence on potential clinical or research utility]. [This technique is available / Code is available at [URL]]."

---

## Introduction (300–500 words)

1. **Clinical or research problem:** Why is a new technique needed? What is the limitation of existing methods?
2. **Description of the new approach:** Brief overview without technical detail (that belongs in Methods).
3. **Objective:** "The purpose of this technical note is to describe [technique] and demonstrate its feasibility in [application context]."

---

## Materials and Methods (600–1000 words)

This is the core of the technical note. Write in enough detail that the technique can be replicated by another group.

### System/Technique Description

Describe the method step by step. Use numbered steps or clear paragraphs. Include:

**For imaging techniques:**
- Equipment (manufacturer, model, software version)
- Acquisition parameters (field strength, sequence parameters, slice thickness, FOV, contrast agent if used)
- Post-processing steps
- Analysis software and version

**For software/algorithm:**
- Programming language and version (e.g., Python 3.10, PyTorch 2.0.1)
- Architecture description (high-level; detailed architecture in supplementary)
- Training/validation/test split
- Computational requirements (GPU, RAM, processing time per case)
- Availability: "Code is publicly available at [GitHub URL] under [license]"

**For procedural techniques:**
- Equipment, instruments, materials (with catalog numbers if novel)
- Step-by-step procedure
- Safety considerations and failure modes

### Validation Dataset

- Source: retrospective or prospective, single center
- N cases / samples
- Inclusion/exclusion criteria (brief)
- Reference standard used for comparison (if applicable)

### Evaluation Metrics

Define exactly what you measured and how:
- For segmentation: Dice similarity coefficient, Hausdorff distance
- For detection: sensitivity, specificity at fixed operating point
- For measurement tools: ICC with 95% CI against reference method (Bland-Altman analysis)
- For image quality: signal-to-noise ratio, contrast-to-noise ratio, or expert reader assessment

State how reproducibility was assessed (intra- and inter-observer variability).

---

## Results (400–600 words — Proof of Concept)

Report the key feasibility metrics. This section should be concise.

- Success rate (technical feasibility)
- Primary performance metric with 95% CI
- Processing time (if relevant)
- Any failure cases and their characteristics

"The technique was successfully applied in [N/N] ([%]) cases. [Primary metric] was [value] (95% CI, [lower]–[upper]). Mean processing time per case was [X ± SD] seconds on a [hardware specification]."

If comparing to an existing reference method:
"Compared with [reference method], [new technique] demonstrated [similar/higher/lower] [metric] ([value] vs. [value]; difference, [X]; 95% CI, [lower]–[upper]; P = [value])."

---

## Discussion (300–500 words)

1. **Summary of findings:** What did you demonstrate? Keep to feasibility.
2. **Technical advantages:** What does this technique offer that existing approaches do not?
3. **Limitations:**
   - Small validation set (cannot make efficacy claims)
   - Single-center, single-vendor
   - May not generalize (state conditions under which technique may fail)
   - Computational requirements (if any)
4. **Future directions:** What clinical validation is needed? Will you make the tool publicly available?

---

## Conclusion (50–100 words)

"We describe [technique] for [application]. Proof-of-concept validation in [N] [cases/samples] demonstrated [key metric]. This technique [potential utility]. [Clinical validation in larger prospective studies is warranted]."

---

## Supplementary Materials

Technical notes commonly require supplementary materials:
- Detailed algorithm pseudocode or flowchart
- Full acquisition parameter tables
- Additional validation cases (figures)
- Code repository link + usage instructions

---

## Common Technical Note Pitfalls

1. **Making efficacy claims instead of feasibility claims** — a technical note cannot conclude that the technique is better; say it "demonstrates feasibility" or "warrants further investigation."
2. **Missing reproducibility data** — always report intra- and inter-observer variability (ICC) for measurement tools.
3. **Insufficient Methods detail** — another lab must be able to replicate from your Methods alone.
4. **Not specifying software versions** — exact versions are required for reproducibility.
5. **Combining technical note and clinical study** — keep the paper focused; add clinical data in supplementary only if very limited.
6. **No code availability statement** — increasingly expected for algorithm papers; GitHub link strongly encouraged.
