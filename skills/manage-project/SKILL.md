---
name: manage-project
description: Research project management for medical manuscripts. Scaffold project structure, track writing progress across phases, maintain project memory files, generate submission checklists and backwards timelines. Commands: init, status, sync-memory, checklist, timeline.
triggers: manage project, project init, project status, submission checklist, project scaffold, create project, new paper project
tools: Read, Write, Edit, Bash, Grep, Glob
model: inherit
---

# Manage-Project Skill -- Research Project Management

## Purpose

Scaffold new research projects, track manuscript writing progress, maintain lightweight project memory, generate pre-submission checklists, and create backwards submission timelines. Integrates with all other writing skills and the project-manager agent.

---

## Commands

### `/manage-project init {name} --type {type} --journal {journal}`

Create a complete project scaffold for a new research paper.

**Parameters:**
- `{name}` -- Project identifier (e.g., `nnunet-skull-fracture`, `rfa-meta-analysis`)
- `--type` -- Paper type: `original | meta | case | animal | technical | ai_validation | letter`
- `--journal` -- Target journal: `RYAI | AJR | Radiology | European_Radiology | KJR | INSI | AJNR | generic`

**What it creates:**

```
{name}/
├── paper/
│   ├── main.qmd               <- Main manuscript (Quarto)
│   ├── sections/
│   │   ├── abstract.qmd
│   │   ├── introduction.qmd
│   │   ├── methods.qmd
│   │   ├── results.qmd
│   │   ├── discussion.qmd
│   │   └── conclusion.qmd
│   ├── figures/
│   │   └── .gitkeep
│   ├── tables/
│   │   └── table_shells.md    <- Table structure designed before prose
│   └── supplementary/
│       └── .gitkeep
├── analysis/
│   ├── scripts/
│   │   └── .gitkeep
│   └── outputs/
│       └── .gitkeep
├── references/
│   ├── library.bib
│   └── checklist_{GUIDELINE}.md  <- Loaded from /check-reporting
├── revision/
│   └── .gitkeep
├── submission/
│   └── .gitkeep
├── PROJECT.md                <- Project identity and scope
├── STATUS.md                 <- Current phase, blockers, next actions
├── CLAIMS.md                 <- Claim-to-result map
├── DATA_DICTIONARY.md        <- Variable and outcome definitions
├── ANALYSIS_PLAN.md          <- Primary/secondary analyses
├── REVIEW_LOG.md             <- Reviewer comments and responses
├── project_state.json         <- Progress tracking
└── README.md                  <- Project overview
```

**Also creates** `project_state.json`:

```json
{
  "name": "{name}",
  "type": "{type}",
  "journal": "{journal}",
  "created": "YYYY-MM-DD",
  "target_submission": null,
  "current_phase": 0,
  "phases": {
    "0_init": "complete",
    "1_outline": "pending",
    "2_tables_figures": "pending",
    "3_methods": "pending",
    "4_results": "pending",
    "5_discussion": "pending",
    "6_intro_abstract": "pending",
    "7_polish": "pending"
  },
  "word_counts": {
    "abstract": 0,
    "introduction": 0,
    "methods": 0,
    "results": 0,
    "discussion": 0,
    "total": 0
  },
  "checklist_status": "pending",
  "citation_status": "unverified",
  "revision_round": null,
  "memory_files": {
    "PROJECT.md": true,
    "STATUS.md": true,
    "CLAIMS.md": true,
    "DATA_DICTIONARY.md": true,
    "ANALYSIS_PLAN.md": true,
    "REVIEW_LOG.md": true
  }
}
```

---

### `/manage-project status`

Report current progress. Reads `project_state.json`, scans existing files, and checks whether key project memory files are present and aligned.

**Output format:**

```
## Project Status: {name}
Journal: {journal} | Type: {type} | Created: {date}
Target submission: {date or "not set"}

### Phase Progress
[check] Phase 0: Project Init (complete)
[check] Phase 1: Outline (complete)
[check] Phase 2: Tables & Figures (complete)
[work]  Phase 3: Methods (IN PROGRESS)
[wait]  Phase 4: Results (pending)
[wait]  Phase 5: Discussion (pending)
[wait]  Phase 6: Introduction & Abstract (pending)
[wait]  Phase 7: Polish (pending)

### Word Counts
Abstract:     0 / 250 words
Introduction: 0 / 600 words
Methods:      847 / 1000 words  85%
Results:      0 / 900 words
Discussion:   0 / 800 words
Total:        847 / 3500 words (journal limit)

### Quality Gates
Critic score (Methods): 87/100 PASS
Citations verified: 12/12
Reporting guideline: pending

### Project Memory
PROJECT.md: present
STATUS.md: stale (last updated 12 days ago)
CLAIMS.md: missing
DATA_DICTIONARY.md: present
ANALYSIS_PLAN.md: missing
REVIEW_LOG.md: n/a (not in revision)

### Next Steps
1. Complete Methods draft (150 words remaining)
2. Run /analyze-stats for Table 1 and diagnostic accuracy
3. Begin Results (Phase 4)
```

### `/manage-project sync-memory`

Audit and refresh project memory files so other agents can work with less ambiguity.

**What it does:**
- checks for presence of `PROJECT.md`, `STATUS.md`, `CLAIMS.md`, `DATA_DICTIONARY.md`, `ANALYSIS_PLAN.md`, `REVIEW_LOG.md`
- identifies stale or contradictory project metadata
- proposes the minimum files to create or update
- aligns `project_state.json` with the current manuscript phase

**Suggested use cases:**
- before handing the project to `project-manager`
- before a large revision cycle
- when returning to an old folder after weeks or months
- when multiple collaborators are editing in parallel

---

### `/manage-project checklist`

Generate a pre-submission checklist covering all quality dimensions.

**Output:** `submission/pre_submission_checklist.md`

Read and output the pre-submission checklist from
`${CLAUDE_SKILL_DIR}/references/pre_submission_checklist.md`.

---

### `/manage-project timeline {submission_date}`

Generate a backwards timeline from submission date.

**Example:** `/manage-project timeline 2026-05-01`

**Output:**

```
## Backwards Timeline to Submission: 2026-05-01

Week -8 (2026-03-06): Phase 0-2 complete (scaffold, outline, tables)
Week -7 (2026-03-13): Methods draft -> critic pass
Week -6 (2026-03-20): Results draft -> critic pass + /analyze-stats complete
Week -5 (2026-03-27): Discussion draft -> critic pass
Week -4 (2026-04-03): Introduction + Abstract -> critic pass
Week -3 (2026-04-10): AI pattern removal + /check-reporting (reporting guideline)
Week -2 (2026-04-17): /self-review + co-author review
Week -1 (2026-04-24): Final revisions + figures at 300 DPI + /lit verification
SUBMISSION (2026-05-01): Upload to journal portal

Critical path: Statistics must be complete by Week -6.
Run /analyze-stats as soon as data is available.
```

---

## Project Scaffold Templates

### PROJECT.md Template

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

### STATUS.md Template

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

### CLAIMS.md Template

```markdown
# CLAIMS

| Claim | Supporting result | Source table/figure | Citation status |
|------|-------------------|---------------------|-----------------|
| ...  | ...               | ...                 | ...             |
```

### DATA_DICTIONARY.md Template

```markdown
# DATA DICTIONARY

| Variable | Definition | Timing | Notes |
|----------|------------|--------|------|
| ...      | ...        | ...    | ...  |
```

### ANALYSIS_PLAN.md Template

```markdown
# ANALYSIS PLAN

- Primary endpoint:
- Secondary endpoints:
- Main comparator:
- Statistical methods:
- Validation strategy:
- Sensitivity analyses:
```

### REVIEW_LOG.md Template

```markdown
# REVIEW LOG

| Reviewer comment | Planned action | Status | Location updated |
|------------------|----------------|--------|------------------|
| ...              | ...            | ...    | ...              |
```

---

## Integration with Other Skills

When called from `/manage-project init`, automatically:
1. Load the correct journal profile from `write-paper/references/journal_profiles/{JOURNAL}.md`
2. Load the correct paper type template from `write-paper/references/paper_types/{TYPE}.md`
3. Copy the appropriate reporting guideline checklist from `check-reporting/references/checklists/`
4. Set word count targets based on the journal profile

After `/manage-project checklist`, recommend calling:
- `/self-review` for manuscript quality gate
- `/search-lit` to verify all citations
- AI pattern removal (built into `/write-paper` Phase 7)

---

## Project State Conventions

**Phase numbers:**
- 0 = Init (scaffold created)
- 1 = Outline approved
- 2 = Table/Figure shells approved
- 3 = Methods (critic >= 85)
- 4 = Results (critic >= 85)
- 5 = Discussion (critic >= 85)
- 6 = Introduction + Abstract (critic >= 85)
- 7 = Polish complete (AI pattern removal + checklist + self-review >= 80)

**Phase status values:** `pending | in_progress | complete | blocked`
