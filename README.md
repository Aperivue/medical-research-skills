# Medical Research Skills for Claude Code

![Medical Research Skills](assets/social-preview.png)

A collection of Claude Code skills covering the full medical research lifecycle -- from literature search to manuscript revision. Built by physicians and researchers, battle-tested on real publications.

![check-reporting demo](demo.gif)

## Skills

```
                              ┌─────────────────────────────────┐
                              │  orchestrate: single entry point │
                              │  classifies intent, routes to    │
                              │  the right skill or chains them  │
                              └───────────────┬─────────────────┘
                                              │
Literature Review -> Study Design -> Analysis -> Figures -> Writing -> Reporting -> Revision -> Presenting
      |                  |              |           |          |            |            |           |
  search-lit       design-study   analyze-stats make-figures write-paper check-reporting revise present-paper
                                                                |             |
                                                           self-review   manage-project
                                                                |
                                                           meta-analysis

                              ┌─────────────────────────────────────────────┐
                              │  publish-skill: package any skill above for │
                              │  open-source distribution (PII audit,       │
                              │  license check, generalization)             │
                              └─────────────────────────────────────────────┘
```

### Available Now

| Skill | What It Does |
|-------|-------------|
| **orchestrate** | Single entry point for the full bundle. Classifies your request and routes to the right skill -- or chains multiple skills for multi-step workflows. Start here if you're unsure which skill to use. |
| **search-lit** | PubMed + Semantic Scholar + bioRxiv search with anti-hallucination citation verification. Full-text OA retrieval pipeline (Unpaywall, PMC, OpenAlex). |
| **check-reporting** | Manuscript compliance audit against 15 reporting guidelines and risk of bias tools (STROBE, STARD, TRIPOD+AI, PRISMA, PRISMA-DTA, ARRIVE, QUADAS-2, RoB 2, ROBINS-I, PROBAST, NOS, and more). |
| **analyze-stats** | Statistical analysis code generation (Python/R) for diagnostic accuracy, DTA meta-analysis (bivariate/HSROC), inter-rater agreement, survival analysis, and demographics tables. |
| **meta-analysis** | Full systematic review and meta-analysis pipeline (8 phases). DTA (bivariate/HSROC) and intervention meta-analysis. Protocol to submission-ready manuscript with PRISMA-DTA compliance. |
| **make-figures** | Publication-ready figures: ROC curves, forest plots, PRISMA/CONSORT/STARD flow diagrams, Kaplan-Meier curves, Bland-Altman plots, confusion matrices. |
| **design-study** | Study design review: identifies analysis unit, cohort logic, data leakage risks, comparator design, validation strategy, and reporting guideline fit. |
| **intake-project** | Classifies new research projects, summarizes current state, identifies missing inputs, and recommends next steps. |
| **grant-builder** | Structures grant proposals: significance, innovation, approach, milestones, and consortium roles. |
| **present-paper** | Academic presentation preparation: paper analysis, supporting research, speaker scripts, slide note injection, and Q&A prep. |
| **publish-skill** | Convert personal Claude Code skills into distributable, open-source-ready packages. PII audit, license compatibility check, generalization, and packaging workflow. |
| **write-paper** | Full IMRAD manuscript pipeline (8 phases). Outline to submission-ready manuscript with critic-fixer loops, AI pattern avoidance, and journal compliance. |
| **self-review** | Pre-submission self-review from reviewer perspective. Systematic check across 7 categories (study design, reference standard, statistics, clinical framing, reproducibility, reporting, guidelines). |
| **revise** | Response to reviewers with tracked changes. Parses decision letters, classifies comments as MAJOR/MINOR/REBUTTAL, generates point-by-point responses and cover letter. |
| **manage-project** | Research project scaffolding and progress tracking. Commands: init, status, sync-memory, checklist, timeline. Backwards submission timelines and pre-submission checklists. |

## Installation

### Option 1: Install all skills (recommended)

```bash
git clone https://github.com/aperivue/medical-research-skills.git
cp -r medical-research-skills/skills/* ~/.claude/skills/
```

### Option 2: Install individual skills

```bash
git clone https://github.com/aperivue/medical-research-skills.git
cp -r medical-research-skills/skills/check-reporting ~/.claude/skills/
```

After copying, restart Claude Code. Skills are automatically discovered from `~/.claude/skills/`.

> **Tip:** Not sure which skill to use? Start with `/orchestrate` -- it will classify your request and route you to the right tool.

## Key Features

### Anti-Hallucination Citations
Every reference produced by `search-lit` is verified against PubMed, Semantic Scholar, or CrossRef APIs. No citation is ever generated from memory alone.

### 15 Reporting Guidelines & RoB Tools Built-in
`check-reporting` includes STROBE, STARD, TRIPOD+AI, PRISMA, PRISMA-DTA, ARRIVE, QUADAS-2, RoB 2, ROBINS-I, PROBAST, and NOS checklists. CONSORT, CARE, SPIRIT, and CLAIM are supported via knowledge-based assessment (checklists not bundled due to license restrictions).

### Publication-Ready Output
`analyze-stats` generates reproducible Python/R code. `make-figures` produces journal-specification figures (300 DPI, colorblind-safe palettes, proper dimensions).

### Skills Work Together
Skills can call each other. For example, `check-reporting` can invoke `make-figures` to generate a PRISMA flow diagram, or `analyze-stats` to fill in missing statistical details.

## Requirements

- [Claude Code](https://claude.ai/code) CLI or IDE extension
- Python 3.9+ (for statistical analysis and figure generation)
- R 4.0+ with `meta` (>=7.0), `metafor` (>=4.0), `mada` (>=0.5.11) packages (for meta-analysis)

## Disclaimer

These skills are research productivity tools. They do **not** provide clinical decision support, medical advice, or diagnostic recommendations. All outputs should be reviewed by qualified researchers before use in any publication or clinical context.

## License

MIT License. See [LICENSE](LICENSE) for details.

Bundled reporting guideline checklists retain their original Creative Commons licenses. See each checklist file for attribution.

## About

Built by [Aperivue](https://aperivue.com) -- tools for medical AI research and education.
