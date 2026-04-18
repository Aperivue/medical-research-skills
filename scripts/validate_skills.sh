#!/usr/bin/env bash
# validate_skills.sh — Lint all medsci-skills for required structure
# Run from repo root: bash scripts/validate_skills.sh

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"
PASS=0
WARN=0
FAIL=0
TOTAL=0

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

pass() { echo -e "  ${GREEN}PASS${NC} $1"; ((PASS++)); }
warn() { echo -e "  ${YELLOW}WARN${NC} $1"; ((WARN++)); }
fail() { echo -e "  ${RED}FAIL${NC} $1"; ((FAIL++)); }

echo "========================================="
echo " MedSci Skills Validator"
echo "========================================="
echo ""

for skill_dir in "$SKILLS_DIR"/*/; do
  skill_name=$(basename "$skill_dir")
  skill_file="$skill_dir/SKILL.md"

  if [ ! -f "$skill_file" ]; then
    fail "$skill_name: SKILL.md not found"
    continue
  fi

  ((TOTAL++))
  echo "[$skill_name]"
  lines=$(wc -l < "$skill_file")

  # 1. Frontmatter: required fields
  has_name=$(head -20 "$skill_file" | grep -c "^name:" || true)
  has_desc=$(head -20 "$skill_file" | grep -c "^description:" || true)
  has_triggers=$(head -20 "$skill_file" | grep -c "^triggers:" || true)
  has_tools=$(head -20 "$skill_file" | grep -c "^tools:" || true)
  has_model=$(head -20 "$skill_file" | grep -c "^model:" || true)

  if [ "$has_name" -ge 1 ] && [ "$has_desc" -ge 1 ] && [ "$has_triggers" -ge 1 ] && [ "$has_tools" -ge 1 ] && [ "$has_model" -ge 1 ]; then
    pass "Frontmatter (all 5 fields)"
  else
    missing=""
    [ "$has_name" -eq 0 ] && missing="$missing name"
    [ "$has_desc" -eq 0 ] && missing="$missing description"
    [ "$has_triggers" -eq 0 ] && missing="$missing triggers"
    [ "$has_tools" -eq 0 ] && missing="$missing tools"
    [ "$has_model" -eq 0 ] && missing="$missing model"
    fail "Frontmatter missing:$missing"
  fi

  # 2. Anti-Hallucination section
  if grep -qi "anti.hallucination\|Anti-Hallucination" "$skill_file"; then
    pass "Anti-Hallucination section"
  else
    fail "Anti-Hallucination section MISSING"
  fi

  # 3. Quality gates (look for "Gate" or "user approval" or "user review")
  gate_count=$(grep -ci "gate\|user approval\|user review\|user confirms\|present.*user" "$skill_file" || true)
  if [ "$gate_count" -ge 3 ]; then
    pass "Quality gates ($gate_count references)"
  elif [ "$gate_count" -ge 1 ]; then
    warn "Quality gates ($gate_count — recommend 3+)"
  else
    warn "Quality gates (0 found)"
  fi

  # 4. Line count tier
  if [ "$lines" -ge 300 ]; then
    pass "Size: $lines lines (HIGH tier)"
  elif [ "$lines" -ge 150 ]; then
    pass "Size: $lines lines (MID tier)"
  else
    warn "Size: $lines lines (THIN tier — consider expanding)"
  fi

  # 5. Reference file integrity
  ref_count=0
  ref_missing=0
  while IFS= read -r ref_line; do
    ref_path=$(echo "$ref_line" | grep -oE '\$\{SKILL_DIR\}/references/[^ `*),]+' | head -1 | sed "s|\${SKILL_DIR}|${skill_dir%/}|" | sed 's/[`\*]//g' || true)
    if [ -n "$ref_path" ]; then
      ((ref_count++))
      if [ ! -f "$ref_path" ] && [ ! -d "$ref_path" ]; then
        # Try without trailing characters
        clean_path=$(echo "$ref_path" | sed 's/[,;]$//')
        if [ ! -f "$clean_path" ] && [ ! -d "$clean_path" ]; then
          ((ref_missing++))
        fi
      fi
    fi
  done < <(grep 'SKILL_DIR.*references' "$skill_file" || true)

  if [ "$ref_count" -eq 0 ]; then
    pass "References: none declared"
  elif [ "$ref_missing" -eq 0 ]; then
    pass "References: $ref_count declared, all found"
  else
    fail "References: $ref_missing of $ref_count missing"
  fi

  echo ""
done

echo "========================================="
echo " Summary"
echo "========================================="
echo -e " Skills checked: ${TOTAL}"
echo -e " ${GREEN}PASS${NC}: ${PASS}"
echo -e " ${YELLOW}WARN${NC}: ${WARN}"
echo -e " ${RED}FAIL${NC}: ${FAIL}"
echo ""

if [ "$FAIL" -gt 0 ]; then
  echo -e "${RED}VALIDATION FAILED${NC} — fix $FAIL issue(s) before release"
  exit 1
else
  echo -e "${GREEN}ALL CHECKS PASSED${NC}"
  exit 0
fi
