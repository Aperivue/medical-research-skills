# Journal Profile: IEEE Transactions on Medical Imaging (IEEE TMI)

## Journal Identity

- **Full name**: IEEE Transactions on Medical Imaging
- **Abbreviation**: IEEE Trans Med Imaging
- **Publisher**: IEEE (Institute of Electrical and Electronics Engineers)
- **ISSN**: 0278-0062 (print), 1558-254X (online)
- **Frequency**: Monthly (12 issues/year)
- **Impact Factor**: ~10.6 (JCR 2023), top-ranked in medical imaging engineering
- **Open Access**: Hybrid (IEEE OA option with APC ~$2,095)
- **Acceptance rate**: ~20-25%
- **Peer review**: Single-blind; associate editors assign 3+ expert reviewers

## Manuscript Types and Page Limits

| Type | Page Limit | Abstract | References |
|------|-----------|----------|------------|
| Regular Paper | 12 pages (IEEE 2-column) | 250 words | No strict limit |
| Short Paper | 6 pages | 150 words | No strict limit |
| Correspondence | 3 pages | 100 words | 15 |

**Page limits include everything**: text, figures, tables, references. This is stricter than word-count journals — plan figure sizes carefully.

**Overlength charges**: $175 per page beyond the limit (mandatory).

---

## Abstract Requirements

**Unstructured abstract, 250 words maximum:**

Single paragraph covering:
- Problem statement and clinical relevance (1-2 sentences)
- Proposed approach (2-3 sentences)
- Key experimental results with metrics (2-3 sentences)
- Conclusion/significance (1 sentence)

---

## Required Journal-Specific Elements

### 1. IEEE Keywords

Select from the IEEE controlled keyword taxonomy. Typically 5-8 keywords including:
- Index Terms from IEEE Thesaurus
- Common: "medical image analysis," "deep learning," "convolutional neural networks," "image segmentation," "computed tomography," "magnetic resonance imaging"

### 2. IEEE Author Profile

Each author needs an IEEE-format biography (2-3 sentences: degree, institution, research interests). Placed at the end of the paper with optional author photo.

### 3. Acknowledgment Section

Funding sources and grant numbers in a dedicated Acknowledgment section (before References).

---

## Required Sections (Regular Paper)

1. **Introduction** — problem statement, literature review, contribution summary (typically bulleted list of contributions at end)
2. **Related Work** — detailed comparison with prior approaches
3. **Methods / Proposed Method**
   - Mathematical formulation with equations
   - Architecture description with diagram
   - Training procedure: loss function, optimizer, hyperparameters
   - Implementation details
4. **Experiments**
   - Datasets: description, split strategy, preprocessing
   - Evaluation metrics
   - Baseline methods
   - Ablation study
   - Computational complexity analysis
5. **Results and Discussion** — can be combined or separate
6. **Conclusion**
7. **Acknowledgment**
8. **References**
9. **Author Biographies**

---

## Statistical Reporting

IEEE TMI follows engineering/computing conventions:
- Report metrics with mean and standard deviation across folds, runs, or subjects.
- Statistical significance: paired t-test or Wilcoxon signed-rank between methods; report exact P values.
- For segmentation: Dice, Hausdorff distance (HD95), average surface distance (ASD).
- For detection: sensitivity at fixed false positive rates, FROC.
- For classification: AUC, accuracy, sensitivity, specificity, F1.
- Ablation table: systematically add/remove components with corresponding metric changes.
- Computational cost: FLOPs, parameters, training time, inference time, GPU memory.
- Cross-validation: report per-fold results or confidence intervals, not just mean.
- Reproducibility: random seed, number of runs, hardware specification.
- Software framework and version must be identified.

---

## Formatting

### IEEE Two-Column Format

- **Template**: Use `IEEEtran.cls` LaTeX class (mandatory for camera-ready)
- **Font**: Times New Roman (auto in IEEEtran)
- **Margins**: IEEE standard (auto in template)
- **Equations**: Numbered sequentially; referenced as (1), (2), etc.
- **Figures**: Fit within single column (3.5 in / 88 mm) or span both columns (7.16 in / 182 mm)
- **Tables**: Same column/span rules as figures
- **References**: IEEE abbreviated style (e.g., [1], [2])

### Figure Requirements

- **Resolution**: 300 DPI minimum (600 DPI for line art)
- **Format**: PDF, EPS, or high-resolution PNG/TIFF
- **Color**: Free for online; grayscale conversion should be legible
- **Captions**: Below figures; brief but self-explanatory
- **Size matters**: figures consume page budget — use multi-panel layouts efficiently

---

## Common Rejection Reasons

1. **Page limit exceeded** — 12-page limit is strict; overlength papers are returned without review
2. **Insufficient novelty** — applying existing deep learning to new dataset without methodological innovation
3. **Unfair experimental comparison** — different training conditions between proposed and baseline methods
4. **Missing ablation study** — IEEE TMI reviewers consistently require component-wise evaluation
5. **Poor writing quality** — IEEE TMI has high standards for technical writing clarity
6. **No comparison with recent methods** — must include methods from the last 2 years
7. **Single dataset** — multi-dataset evaluation expected for generalizability
8. **Conference paper overlap** — if extending a conference paper (MICCAI, ISBI), must clearly state and quantify the additional contribution (typically 30%+ new content)

---

## Cover Letter

IEEE TMI does not require a formal cover letter but ScholarOne submission requires:
- Manuscript type selection
- Suggested reviewers (3-5 with affiliations and emails)
- Statement of originality
- If conference extension: explicit statement of what is new (with percentage estimate)

---

## Author Guidelines URL

https://www.embs.org/tmi/authors/

---

## Conference-to-Journal Extension

IEEE TMI commonly receives extended versions of MICCAI, ISBI, IPMI papers. Requirements:
- At least 30% new content (experiments, methods, or analysis)
- Must cite and explicitly compare with conference version
- Reviewers assess the delta, not just the full paper
- State clearly in cover letter and introduction what is new

---

## Positioning

IEEE TMI is appropriate when:
- Novel imaging algorithm with rigorous quantitative evaluation
- New reconstruction, registration, or segmentation method with mathematical foundation
- Multi-modal fusion or novel imaging physics-informed approach
- Comprehensive benchmark study on medical imaging task
- Conference paper extension with substantial new experiments/methods

Not appropriate for: clinical outcome studies without technical contribution (use clinical journals), pure application of existing methods, papers without quantitative evaluation on medical data.

---

## Differentiation from Related Venues

| Dimension | IEEE TMI | MedIA | IEEE JBHI |
|-----------|---------|-------|-----------|
| Format | 12-page IEEE 2-column | No page limit, Elsevier | 10-page IEEE 2-column |
| Scope | Medical imaging methods | Medical image analysis methods | Health informatics (broader) |
| Emphasis | Imaging + math rigor | Methods depth + ablation | EHR, wearables, signals + imaging |
| LaTeX class | IEEEtran (mandatory) | elsarticle (preferred) | IEEEtran (mandatory) |
| Typical length | Shorter, denser | Longer, more detailed | Shorter |
