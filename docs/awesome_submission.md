# awesome-claude-code Resubmission — v3.0 Update (2026-05-13)

Updated for v3.0.0 release (39 skills, 3 demos, Zenodo DOI). Eligible to resubmit (extension period expired 2026-04-27).

## Issue Template Fields

**Title:** [Resource]: MedSci Skills

**Display Name:** MedSci Skills

**Category:** Agent Skills

**Sub-Category:** General

**Primary Link:** https://github.com/Aperivue/medsci-skills

**Author Name:** Aperivue

**Author Link:** https://github.com/Aperivue

**License:** MIT

**Description:**

39 Claude Code skills for the full medical research lifecycle — from PubMed literature search with anti-hallucination citation verification (every reference cross-checked via PubMed/CrossRef API) to submission-ready IMRAD manuscripts with reporting compliance audits against 33 EQUATOR guidelines (STARD-AI, TRIPOD+AI, CLAIM, PRISMA-DTA, STROBE, CONSORT, etc.). Includes three end-to-end demos that each produce a complete manuscript, 300-dpi figures, compliance report, and presentation slides from public datasets in under 10 minutes. Built by a practicing radiologist and tested on real publications. v3.0.0 archived on Zenodo for academic citation.

**Validate Claims:**

Run Demo 1 end-to-end in under 10 minutes:

```bash
git clone https://github.com/Aperivue/medsci-skills.git
cd medsci-skills
python3 installers/install.py --target claude
cd demo/01_wisconsin_bc
```

Then in Claude Code: `/orchestrate --e2e` — produces a full IMRAD manuscript, ROC curves with DeLong CIs, STARD 2015 compliance audit (28 items), self-review (scores 74→83 across 2 fix iterations), DOCX, and 12-slide presentation with speaker notes.

For a quick single-skill test: `/check-reporting any_manuscript.md --guideline STARD` produces an item-by-item compliance report (PRESENT/PARTIAL/MISSING).

For new users: `/setup-medsci` runs a read-only diagnostic of Python/R/Claude Code/MCP installation and prints a checklist.

**Specific Task(s):**

1. Run Demo 1 (Wisconsin BC) — produces manuscript + ROC curves + STARD audit + slides from `sklearn.datasets.load_breast_cancer()`. Output viewable at `demo/01_wisconsin_bc/`.
2. Run Demo 2 (BCG meta-analysis) — pooled RR = 0.489 (95% CI 0.344–0.696) across 13 RCTs from `metafor::dat.bcg`, with PRISMA 2020 audit (77.8% compliance, 21/27 PRESENT).
3. Run Demo 3 (NHANES obesity) — STROBE-compliant epidemiology manuscript from CDC NHANES 2017-18 with survey weights.
4. `/check-reporting` against any manuscript — supports 33 EQUATOR guidelines.
5. `/search-lit` PubMed query — verify every citation has a real PMID (anti-hallucination).
6. `/setup-medsci` diagnostic — verifies environment without modifying anything.

**Specific Prompt(s):**

1. `/check-reporting manuscript.md --guideline STARD-AI`
2. `/search-lit "diagnostic accuracy of AI for lung nodule detection" --database pubmed --limit 10`
3. `/make-figures prisma --identified 500 --screened 350 --eligible 45 --included 23`

**Additional Comments:**

Resubmission of #1389 (closed for 7-day cooldown) and #1518 (closed same day, 14-day extension applied, eligible after 2026-04-27).

**v3.0.0 updates since the prior submission:**
- 22 → 39 skills (covers full lifecycle: topic discovery, IRB, data cleaning, de-identification, presentation, peer review, revision response)
- Three end-to-end demos (Wisconsin BC, BCG MA, NHANES) with public datasets and reproducible output artifacts
- 33 EQUATOR reporting guidelines (added STARD-AI, TRIPOD+AI, CLAIM 2024, MI-CLEAR-LLM, PROBAST+AI, etc.)
- New `setup-medsci` skill — read-only diagnostic for clinicians new to Python/R/Claude Code
- New `docs/setup/` clinician onboarding guide (mac, windows, MCP, common-issues)
- v3.0.0 archived on Zenodo (DOI: pending — to be filled in upon issue review)
- CITATION.cff for academic citation
- Anti-Reviewer-2 tone audit integrated into peer-review skill (Aczel 2021 patterns)

All reporting guideline checklists retain original CC licenses. No network requests except public APIs (PubMed, Semantic Scholar, CrossRef). Repository renamed from `medical-research-skills` to `medsci-skills` (old URL auto-redirects).

---

## 제출 메모 (한국어 작업 노트)

- 제출일: 2026-05-13 (v3.0.0 release 직후)
- 이전 issues: #1389 (7-day cooldown closed), #1518 (14-day extension)
- 두 cooldown 모두 만료 (2026-04-27 이후)
- v3.0.0 release URL: https://github.com/Aperivue/medsci-skills/releases/tag/v3.0.0
- Zenodo DOI: 첫 archive 후 본문에 update
- 체크리스트 재확인:
  - License (MIT) ✓
  - 활동 (commits this week) ✓
  - 구조 (SKILL.md frontmatter, validator PASS) ✓
  - 데모 (3종 end-to-end) ✓
  - 이전 issue reference (#1389, #1518 명시) ✓
