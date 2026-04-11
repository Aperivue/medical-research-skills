# Journal Profile: Medical Image Analysis (MedIA)

## Journal Identity

- **Full name**: Medical Image Analysis
- **Abbreviation**: Med Image Anal
- **Publisher**: Elsevier
- **ISSN**: 1361-8415 (print), 1361-8423 (online)
- **Frequency**: 8 issues/year
- **Impact Factor**: ~10.9 (JCR 2023), top-ranked in medical image computing
- **Open Access**: Hybrid (optional OA; Elsevier transformative agreements may apply)
- **Acceptance rate**: ~20%
- **Peer review**: Single-blind; associate editors with strong technical backgrounds

## Manuscript Types and Word Limits

| Type | Body Word Limit | Abstract | References | Figures |
|------|----------------|----------|------------|---------|
| Original Article | No strict limit (typically 8000-12000) | 200 words | No strict limit | No strict limit |
| Short Communication | 4000 words | 150 words | 30 | 6 |
| Review Article | No strict limit | 200 words | No strict limit | No strict limit |
| Position Paper | No strict limit | 200 words | No strict limit | No strict limit |

**Note**: MedIA is methods-focused with no strict word or figure limits for full articles. Papers are typically longer than clinical journals (8000-12000 words common). Quality and completeness are prioritized over brevity.

---

## Abstract Requirements

**Unstructured abstract, 200 words maximum:**

A single paragraph covering:
- Problem and clinical motivation (1-2 sentences)
- Proposed method or approach (2-3 sentences)
- Key experimental results with quantitative metrics (2-3 sentences)
- Significance or conclusion (1 sentence)

---

## Required Sections (Original Article)

1. **Introduction** — thorough literature review expected (longer than clinical journals); clear statement of contribution at end
2. **Related Work** (optional but common) — detailed comparison with prior methods
3. **Methods**
   - Mathematical formulation
   - Model architecture with diagrams
   - Training details: optimizer, learning rate, batch size, epochs, augmentation
   - Loss function
   - Implementation details
4. **Experiments**
   - Datasets: detailed description with statistics (patients, images, annotations)
   - Evaluation metrics: standard metrics for the task (Dice, AUC, FROC, etc.)
   - Comparison with state-of-the-art methods
   - Ablation study: systematic evaluation of each component's contribution
   - Cross-validation or train/val/test split details
5. **Results** — tables and figures with quantitative comparisons
6. **Discussion** — clinical relevance, limitations, failure cases
7. **Conclusion**

---

## Statistical Reporting

MedIA follows technical computing conventions rather than clinical statistical standards:
- Report all metrics with standard deviation or 95% CI across folds/runs.
- For segmentation: Dice coefficient, Hausdorff distance (95th percentile preferred), average surface distance.
- For detection: sensitivity, false positives per scan (FROC), precision-recall.
- For classification: AUC, sensitivity, specificity, accuracy, F1-score.
- Statistical significance testing between methods: paired tests (Wilcoxon signed-rank, paired t-test, DeLong for AUC comparison).
- Report results across multiple random seeds if stochastic training is involved.
- Effect of hyperparameter choices should be evaluated (sensitivity analysis or ablation).
- Computational cost: report training time, inference time per image/volume, GPU memory.
- Software framework and version (PyTorch, TensorFlow) must be identified.

---

## Figures

- **No strict figure limit** — use as many as needed for clarity
- **Required figure types**: model architecture diagram, qualitative result examples (success and failure cases), quantitative comparison tables/charts
- **Resolution**: 300 DPI (vector preferred for diagrams)
- **Format**: PDF, EPS, TIFF
- **Color**: Free, encouraged
- **LaTeX**: Manuscripts in LaTeX are common and well-supported; use Elsevier article class

---

## Manuscript Format

- **LaTeX strongly preferred** — use `elsarticle.cls` document class
- **Microsoft Word** also accepted but less common
- **Line numbering**: Required for review
- **Supplementary material**: Unlimited; common for additional experiments, video demonstrations
- **Code**: Strongly encouraged to share via GitHub; mention in Data/Code Availability statement

---

## Common Rejection Reasons

1. **Insufficient technical novelty** — MedIA expects novel methodology; applying existing methods to new datasets without methodological contribution is insufficient
2. **No comparison with state-of-the-art** — must compare against recent competitive methods on same datasets
3. **Missing ablation study** — each proposed component must be justified experimentally
4. **Single dataset evaluation** — multi-dataset evaluation strongly preferred for generalizability claims
5. **No failure case analysis** — reviewers expect honest discussion of when the method fails
6. **Poor reproducibility** — missing implementation details, no code availability
7. **Weak clinical motivation** — pure technical novelty without medical relevance may be redirected to computer vision venues
8. **Unfair comparisons** — different training data, augmentation, or post-processing between proposed and baseline methods

---

## Cover Letter

Should emphasize:
- Technical contribution (novel method, not just novel application)
- Clinical relevance and potential impact
- Reproducibility (code/data availability plans)
- Suggested reviewers with relevant expertise (3-5 recommended)

---

## Author Guidelines URL

https://www.elsevier.com/journals/medical-image-analysis/1361-8415/guide-for-authors

---

## Positioning

Medical Image Analysis is appropriate when:
- Novel computational method for medical image analysis with rigorous evaluation
- Comprehensive benchmark study establishing new baselines
- Methodological innovation (new architecture, training strategy, representation) validated on medical data
- Multi-dataset evaluation with ablation demonstrating each component's contribution

Not appropriate for: clinical validation studies without methodological contribution (use clinical journals), application of off-the-shelf models without modification (use application-specific journals), pure computer vision without medical data (use CVPR/MICCAI proceedings).

---

## Differentiation from Related Venues

| Dimension | MedIA | IEEE TMI | MICCAI |
|-----------|-------|---------|--------|
| Format | Journal (long) | Journal (short, page limit) | Conference proceedings |
| Review cycle | 3-6 months | 3-6 months | Annual deadline |
| Length | 8000-12000 words | 10-12 pages (IEEE 2-col) | 8-10 pages |
| Emphasis | Method depth + ablation | Broader scope, shorter papers | Novelty + preliminary results |
| Impact factor | ~10.9 | ~10.6 | N/A (proceedings) |
