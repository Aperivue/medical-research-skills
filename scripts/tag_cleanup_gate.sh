#!/usr/bin/env bash
# Tag / TODO cleanup gate (DI-8).
#
# Blocks submission if draft-stage tags survive in the submission package.
# Patterns per skills/meta-analysis/references/data_integrity_checklist.md DI-8.
#
# Usage:
#   bash scripts/tag_cleanup_gate.sh [project_root]
#
# Exit codes: 0 clean, 1 tags found, 2 bad args / missing tool.

set -euo pipefail

PROJECT_ROOT="${1:-.}"
cd "$PROJECT_ROOT"

# Default MA scaffold dirs; non-existent ones are skipped silently.
DIRS=("7_Manuscript" "supplement" "5_Figures" "6_Tables" "1_Code" "SUBMISSION")

PATTERN='VERIFY-CSV|TODO|FIXME|XXX|to be regenerated|PH TODO|to-do'

# Meta-discussion files (tag conventions/history are legitimately quoted here, not live draft tags).
# Any file whose basename matches these globs is excluded from the scan.
EXCLUDE_GLOBS=(
    "peer_review*"
    "*edit_plan*"
    "checklist.md"
    "response_to_*"
    "_merged.md"
    "*_reviewer_*"
)

# Files can also opt-out with a line containing "DI-8:ignore-file" anywhere.
# (Handled post-scan by filtering hits whose file starts with that marker.)

if command -v rg >/dev/null 2>&1; then
    GREP_CMD=(rg -n --no-heading -e "$PATTERN")
    for g in "${EXCLUDE_GLOBS[@]}"; do
        GREP_CMD+=(-g "!$g")
    done
else
    GREP_CMD=(grep -rnE "$PATTERN")
    for g in "${EXCLUDE_GLOBS[@]}"; do
        GREP_CMD+=(--exclude="$g")
    done
fi

EXISTING_DIRS=()
for d in "${DIRS[@]}"; do
    [[ -d "$d" ]] && EXISTING_DIRS+=("$d")
done

if [[ ${#EXISTING_DIRS[@]} -eq 0 ]]; then
    echo "WARN: none of the expected dirs exist in $PROJECT_ROOT — nothing to scan." >&2
    echo "      Expected one of: ${DIRS[*]}" >&2
    exit 2
fi

echo "Tag cleanup gate (DI-8)"
echo "  Root:    $(pwd)"
echo "  Scan:    ${EXISTING_DIRS[*]}"
echo "  Pattern: $PATTERN"
echo

RAW_HITS=$("${GREP_CMD[@]}" "${EXISTING_DIRS[@]}" 2>/dev/null || true)

# Second filter: drop hits whose source file has a "DI-8:ignore-file" marker.
HITS=""
while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    file="${line%%:*}"
    if [[ -f "$file" ]] && grep -q "DI-8:ignore-file" "$file" 2>/dev/null; then
        continue
    fi
    HITS+="${line}"$'\n'
done <<< "$RAW_HITS"
HITS="${HITS%$'\n'}"

if [[ -n "$HITS" ]]; then
    echo "FAIL: draft-stage tags detected — remove before submission."
    echo
    echo "$HITS"
    exit 1
fi

echo "PASS: 0 hits. Submission package is tag-clean."
exit 0
