#!/usr/bin/env bash
# Phase 1A gate regression tests (Phase 1B-a).
#
# Verifies that /verify-refs --strict exits non-zero when the SSOT fixture's
# seed bib contains FABRICATED-shaped or UNVERIFIED references.
#
# Network required (CrossRef + PubMed esummary). Skip with NETWORK=0.
#
# Usage:
#   tests/test_phase1a_gates.sh
# Exit codes:
#   0 — all gates behaved as specified
#   1 — at least one gate regressed
#   2 — environment problem (missing fixture / python3)

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FIXTURE="$REPO_ROOT/tests/fixtures/ssot_project"
SCRIPT="$REPO_ROOT/skills/verify-refs/scripts/verify_refs.py"
SEED_BIB="$FIXTURE/manuscript/_src/refs_seed_phase1b.bib"

fail=0
ran=0

assert_exit() {
    local label="$1" expected="$2" actual="$3"
    ran=$((ran + 1))
    if [[ "$expected" == "$actual" ]]; then
        printf '  PASS  %-40s exit=%s\n' "$label" "$actual"
    else
        printf '  FAIL  %-40s exit=%s (expected %s)\n' "$label" "$actual" "$expected"
        fail=$((fail + 1))
    fi
}

[[ -f "$SCRIPT" ]] || { echo "Missing $SCRIPT" >&2; exit 2; }
[[ -f "$SEED_BIB" ]] || { echo "Missing $SEED_BIB" >&2; exit 2; }
command -v python3 >/dev/null || { echo "python3 required" >&2; exit 2; }

echo "Phase 1A gate regression — fixture: $FIXTURE"

# Gate 1: --strict with FABRICATED/UNVERIFIED seed → exit 1
cd "$FIXTURE"
python3 "$SCRIPT" "$SEED_BIB" --project-root . --strict --timeout 30 >/dev/null 2>&1
assert_exit "strict gate on seed bib" 1 $?

# Gate 2: --offline + --strict mutually exclusive → exit 2
python3 "$SCRIPT" "$SEED_BIB" --project-root . --strict --offline >/dev/null 2>&1
assert_exit "strict + offline rejected" 2 $?

# Gate 3: missing input → exit 2
python3 "$SCRIPT" "$FIXTURE/does_not_exist.bib" --project-root . --offline >/dev/null 2>&1
assert_exit "missing input rejected" 2 $?

# Gate 4: empty bib (no records detected) → exit 3
EMPTY=$(mktemp)
trap 'rm -f "$EMPTY"' EXIT
echo "% empty stub" > "$EMPTY"
python3 "$SCRIPT" "$EMPTY" --project-root . --offline >/dev/null 2>&1
assert_exit "empty bib rejected" 3 $?

echo
if [[ $fail -eq 0 ]]; then
    echo "All $ran gate(s) passed."
    exit 0
else
    echo "$fail of $ran gate(s) failed."
    exit 1
fi
