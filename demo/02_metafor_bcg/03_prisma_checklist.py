#!/usr/bin/env python3
"""
MedSci Skills Demo 2: BCG Vaccine Meta-Analysis
Step 3 — PRISMA 2020 Compliance Checklist (check-reporting skill)

Generates a PRISMA 2020 compliance report evaluating all 27 items.
Screening/selection items are N/A since this uses a built-in dataset.

Usage: python3 03_prisma_checklist.py
"""

import sys
import logging
from pathlib import Path
from datetime import date

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "output"
LOGS = BASE / "logs"
LOGS.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOGS / "step3_prisma.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# PRISMA 2020 Checklist — 27 Items
# ---------------------------------------------------------------------------
# Each item: (Section, Item#, Topic, Status, Location/Comment)
# Status: PRESENT / PARTIAL / MISSING / N/A

PRISMA_ITEMS = [
    # TITLE
    ("Title", 1, "Identify the report as a systematic review incorporating a meta-analysis",
     "PRESENT",
     "Title includes 'Meta-Analysis of Randomized Controlled Trials'"),

    # ABSTRACT
    ("Abstract", 2, "Structured summary with background, methods, results, conclusion",
     "PRESENT",
     "Abstract: structured with Background, Methods, Results, Conclusion sections"),

    # INTRODUCTION
    ("Introduction", 3, "Rationale: describe the rationale in the context of existing knowledge",
     "PRESENT",
     "Introduction: discusses BCG efficacy variability, NTM hypothesis, Colditz 1994"),

    ("Introduction", 4, "Objectives: provide an explicit statement of the questions addressed",
     "PRESENT",
     "Introduction: quantify BCG efficacy, assess heterogeneity sources, evaluate robustness"),

    # METHODS
    ("Methods", 5, "Eligibility criteria: report criteria with rationale",
     "PARTIAL",
     "Methods/Eligibility: references original Colditz criteria; limited detail since built-in dataset"),

    ("Methods", 6, "Information sources: describe all sources with dates of searches",
     "N/A",
     "Built-in dataset (metafor::dat.bcg). No de novo literature search was conducted"),

    ("Methods", 7, "Search strategy: present full search strategy for at least one database",
     "N/A",
     "Built-in dataset. No search strategy applicable"),

    ("Methods", 8, "Selection process: state process for selecting studies",
     "N/A",
     "Built-in curated dataset; no independent study selection performed"),

    ("Methods", 9, "Data collection process: describe methods of data extraction",
     "N/A",
     "Pre-extracted 2x2 tables provided in dataset; no manual data extraction"),

    ("Methods", 10, "Data items: list and define all variables for which data were sought",
     "PRESENT",
     "Methods: specifies 2x2 table cells, allocation method, latitude, year"),

    ("Methods", 11, "Study risk of bias assessment: methods for assessing risk of bias",
     "MISSING",
     "No formal risk of bias tool (e.g., Cochrane RoB 2) was applied to individual studies"),

    ("Methods", 12, "Effect measures: specify for each outcome the effect measure used",
     "PRESENT",
     "Methods: risk ratio (RR) from 2x2 tables, computed via escalc()"),

    ("Methods", 13, "Synthesis methods: describe processes for deciding which studies to combine, "
     "tabulation, statistical model, heterogeneity assessment, sensitivity analyses",
     "PRESENT",
     "Methods: REML random-effects model, Q/I-squared/tau-squared, subgroup, meta-regression, LOO, publication bias"),

    ("Methods", 13, "Synthesis methods (a): describe criteria for tabulating and combining studies",
     "PRESENT",
     "All 13 RCTs combined; subgroup by allocation method"),

    ("Methods", 13, "Synthesis methods (b): describe methods for meta-analysis (model, estimator)",
     "PRESENT",
     "Random-effects REML via metafor::rma()"),

    ("Methods", 13, "Synthesis methods (c): describe methods for heterogeneity (Q, I-squared, prediction interval)",
     "PRESENT",
     "Q statistic, I-squared, tau-squared, prediction interval all reported"),

    ("Methods", 13, "Synthesis methods (d): describe sensitivity analyses planned",
     "PRESENT",
     "Leave-one-out analysis, influence diagnostics"),

    ("Methods", 14, "Reporting bias assessment: describe methods for assessing publication bias",
     "PRESENT",
     "Funnel plot, Egger's test, Begg's test, trim-and-fill"),

    ("Methods", 15, "Certainty assessment: describe methods for assessing certainty (e.g., GRADE)",
     "MISSING",
     "No GRADE or certainty of evidence assessment was performed"),

    # RESULTS
    ("Results", 16, "Study selection: numbers of studies screened, assessed, included with flow diagram",
     "N/A",
     "Built-in dataset; no screening process. PRISMA flow diagram not applicable"),

    ("Results", 17, "Study characteristics: cite each study and present characteristics",
     "PRESENT",
     "Results/Table: 13 studies with author, year, RR, CI, weight, latitude, allocation"),

    ("Results", 18, "Risk of bias in studies: present assessments for each study",
     "MISSING",
     "No individual study risk of bias assessment reported"),

    ("Results", 19, "Results of individual studies: present data for each study and forest plot",
     "PRESENT",
     "Forest plot (Figure 1) and study_results.csv with per-study RR and 95% CI"),

    ("Results", 20, "Results of syntheses: present pooled estimate with CI, heterogeneity, forest plot",
     "PRESENT",
     "RR = 0.489 (95% CI: 0.344-0.696), I-squared = 92.2%, forest plot with diamond"),

    ("Results", 21, "Reporting biases: present results of publication bias assessment",
     "PRESENT",
     "Egger's p = 0.189, Begg's p = 0.952, trim-and-fill: 1 study, adjusted RR = 0.518"),

    ("Results", 22, "Certainty of evidence: present certainty for each outcome",
     "MISSING",
     "No GRADE assessment presented"),

    # DISCUSSION
    ("Discussion", 23, "Discussion: provide general interpretation in context, limitations, implications",
     "PRESENT",
     "Discussion: latitude effect interpretation, NTM hypothesis, heterogeneity, 5 limitations listed"),

    # OTHER
    ("Other", 24, "Registration and protocol: provide registration number and protocol access",
     "N/A",
     "Teaching demonstration; no PROSPERO registration"),

    ("Other", 25, "Support: describe sources of financial or non-financial support",
     "MISSING",
     "No funding statement included"),

    ("Other", 26, "Competing interests: declare any competing interests",
     "MISSING",
     "No conflict of interest statement included"),

    ("Other", 27, "Availability of data, code, and materials",
     "PRESENT",
     "Dataset: metafor::dat.bcg (publicly available). Analysis code: 01_meta_analysis.R"),
]

# ---------------------------------------------------------------------------
# Generate report
# ---------------------------------------------------------------------------
def generate_report() -> str:
    lines = []
    lines.append("# PRISMA 2020 Compliance Report")
    lines.append("")
    lines.append(f"**Study:** Efficacy of BCG Vaccination for Prevention of Tuberculosis: "
                 f"A Meta-Analysis of Randomized Controlled Trials")
    lines.append(f"**Assessment date:** {date.today()}")
    lines.append(f"**Assessor:** MedSci Skills (check-reporting skill)")
    lines.append(f"**Guideline:** PRISMA 2020 (Page et al., BMJ 2021;372:n71)")
    lines.append("")
    lines.append("> **Note:** This is a re-analysis of the Colditz et al. (1994) dataset "
                 "available as `metafor::dat.bcg`. Items related to literature searching, "
                 "screening, and study selection are rated N/A because no de novo "
                 "systematic search was conducted.")
    lines.append("")

    # Summary counts
    counts = {"PRESENT": 0, "PARTIAL": 0, "MISSING": 0, "N/A": 0}
    for _, _, _, status, _ in PRISMA_ITEMS:
        counts[status] += 1

    total_applicable = counts["PRESENT"] + counts["PARTIAL"] + counts["MISSING"]
    compliance_pct = (
        (counts["PRESENT"] + 0.5 * counts["PARTIAL"]) / total_applicable * 100
        if total_applicable > 0 else 0
    )

    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Status | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| PRESENT | {counts['PRESENT']} |")
    lines.append(f"| PARTIAL | {counts['PARTIAL']} |")
    lines.append(f"| MISSING | {counts['MISSING']} |")
    lines.append(f"| N/A | {counts['N/A']} |")
    lines.append(f"| **Total items** | **{len(PRISMA_ITEMS)}** |")
    lines.append(f"| **Compliance (applicable)** | **{compliance_pct:.0f}%** |")
    lines.append("")

    # Detailed checklist
    lines.append("## Detailed Checklist")
    lines.append("")
    lines.append("| Section | Item | Topic | Status | Comment |")
    lines.append("|---------|------|-------|--------|---------|")

    for section, item, topic, status, comment in PRISMA_ITEMS:
        # Status emoji for visual scanning
        icon = {
            "PRESENT": "PRESENT",
            "PARTIAL": "PARTIAL",
            "MISSING": "MISSING",
            "N/A": "N/A",
        }[status]
        # Truncate topic for table readability
        short_topic = topic[:80] + "..." if len(topic) > 80 else topic
        lines.append(f"| {section} | {item} | {short_topic} | {icon} | {comment} |")

    lines.append("")

    # Recommendations
    lines.append("## Recommendations for Improvement")
    lines.append("")

    missing_items = [(s, i, t, c) for s, i, t, st, c in PRISMA_ITEMS if st == "MISSING"]
    partial_items = [(s, i, t, c) for s, i, t, st, c in PRISMA_ITEMS if st == "PARTIAL"]

    if missing_items:
        lines.append("### Missing Items")
        lines.append("")
        for section, item, topic, comment in missing_items:
            lines.append(f"- **Item {item} ({section}):** {topic}")
            lines.append(f"  - *Action needed:* {comment}")
            lines.append("")

    if partial_items:
        lines.append("### Partial Items")
        lines.append("")
        for section, item, topic, comment in partial_items:
            lines.append(f"- **Item {item} ({section}):** {topic}")
            lines.append(f"  - *Improvement:* {comment}")
            lines.append("")

    lines.append("### Priority Actions")
    lines.append("")
    lines.append("1. **Risk of bias assessment (Items 11, 18):** Apply Cochrane Risk of Bias 2 "
                 "(RoB 2) tool to each included RCT and present results in a summary figure.")
    lines.append("2. **GRADE certainty assessment (Items 15, 22):** Evaluate certainty of evidence "
                 "using the GRADE framework (risk of bias, inconsistency, indirectness, "
                 "imprecision, publication bias) and present a Summary of Findings table.")
    lines.append("3. **Funding and COI statements (Items 25, 26):** Add declarations even if "
                 "none exist (state 'No funding received' and 'No conflicts of interest').")
    lines.append("4. **Eligibility criteria (Item 5):** Expand description of original Colditz "
                 "criteria including population, intervention, comparator, outcome, and study design.")
    lines.append("")

    lines.append("---")
    lines.append(f"*Generated: {date.today()} | MedSci Skills Demo 2 — check-reporting skill*")
    lines.append("")

    return "\n".join(lines)


def main():
    log.info("=" * 60)
    log.info("Step 3: PRISMA 2020 Compliance Checklist")
    log.info("=" * 60)

    report = generate_report()
    out_path = OUTPUT / "prisma_compliance_report.md"
    out_path.write_text(report, encoding="utf-8")

    # Count summary
    counts = {"PRESENT": 0, "PARTIAL": 0, "MISSING": 0, "N/A": 0}
    for _, _, _, status, _ in PRISMA_ITEMS:
        counts[status] += 1

    log.info(f"Saved: {out_path}")
    log.info(f"  PRESENT: {counts['PRESENT']}, PARTIAL: {counts['PARTIAL']}, "
             f"MISSING: {counts['MISSING']}, N/A: {counts['N/A']}")
    log.info(f"  Total items evaluated: {len(PRISMA_ITEMS)}")
    log.info("=" * 60)
    log.info("PRISMA compliance check complete.")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
