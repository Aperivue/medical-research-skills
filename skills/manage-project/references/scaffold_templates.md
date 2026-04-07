# Project Scaffold Templates

## PROJECT.md Template

```markdown
# PROJECT

- Title:
- Type:
- Primary question:
- Target journal/venue:
- Lead folder:
- Collaborators:
- Last updated:
```

## STATUS.md Template

```markdown
# STATUS

- Current stage:
- Current blocker:
- Next actions:
  1.
  2.
  3.
- Last updated:
```

## CLAIMS.md Template

```markdown
# CLAIMS

| Claim | Supporting result | Source table/figure | Citation status |
|------|-------------------|---------------------|-----------------|
| ...  | ...               | ...                 | ...             |
```

## DATA_DICTIONARY.md Template

```markdown
# DATA DICTIONARY

| Variable | Definition | Timing | Notes |
|----------|------------|--------|------|
| ...      | ...        | ...    | ...  |
```

## ANALYSIS_PLAN.md Template

```markdown
# ANALYSIS PLAN

- Primary endpoint:
- Secondary endpoints:
- Main comparator:
- Statistical methods:
- Validation strategy:
- Sensitivity analyses:
```

## REVIEW_LOG.md Template

```markdown
# REVIEW LOG

| Reviewer comment | Planned action | Status | Location updated |
|------------------|----------------|--------|------------------|
| ...              | ...            | ...    | ...              |
```

## main.qmd Header (RYAI example)

```yaml
---
title: "[Manuscript Title]"
author:
  - name: "[First Author]"
    affiliation: "[Institution]"
    corresponding: true
    email: "[email]"
date: "`r Sys.Date()`"
format:
  docx:
    reference-doc: submission/template_RYAI.docx
  pdf:
    documentclass: article
bibliography: references/library.bib
csl: references/radiology-ai.csl
---
```

## README.md Template

```markdown
# {name}

**Type:** {type}
**Target journal:** {journal}
**Status:** In progress

## Key Files
- `paper/main.qmd` — Main manuscript
- `analysis/scripts/` — Analysis scripts
- `references/library.bib` — Verified citations
- `project_state.json` — Progress tracker

## Data
[Describe data location and access]

## Analysis Plan
[One-paragraph summary of statistical approach]

## Timeline
[Key milestones]
```
