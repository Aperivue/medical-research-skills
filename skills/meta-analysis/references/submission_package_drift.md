# Submission Package Drift Control

**Applies to**: 저널 다중 타깃(academic radiology / DIR / BJR / MDPI Diagnostics 등) 병존 상황.

## 문제

저널별 `SUBMISSION/{journal}/` 폴더가 4~5개 병존하는 상황에서, 각 폴더에 본문/supplement/figures가 모두 들어 있으면 rebuild 후 drift 위험 (어느 폴더가 master인지 불분명해지고, 한쪽에서만 수정된 오타가 다른 타깃으로 재전파됨).

## 규칙

### SPD-1. Single master + build script
- **Rule**: `7_Manuscript/` master는 1개. 저널별 변환은 `SUBMISSION/_build.sh`가 담당.
- **Build output**: `SUBMISSION/{journal}/{manuscript.docx, supplement.docx, figures/, tables/}` — 이것들은 **build artifact, 수동 편집 금지**.

### SPD-2. `DO_NOT_EDIT_HERE.md` 게이트
- **Rule**: 저널별 폴더에 `DO_NOT_EDIT_HERE.md` 파일 배치. 이 파일이 있으면 해당 디렉토리의 본문/supplement/figure는 편집 금지. 예외 허용 파일:
  - `cover_letter.docx`
  - `title_page.docx`
  - `highlights.txt`
  - `checklist.md` (journal-specific reporting checklist)
  - `response_to_reviewers.docx` (revision 시)
- 이 예외 파일들은 저널별로만 필요하므로 직접 편집 허용.

### SPD-3. `MANIFEST.md`에 build 시점 기록
- **Rule**: 각 `SUBMISSION/{journal}/MANIFEST.md`에 4줄:
  1. `_build.sh` 실행 시각
  2. Source: master manuscript commit / `v{N}`
  3. 저널 폴더에서 편집 허용된 파일 목록
  4. `[VERIFY-CSV]` tag 전수 제거 확인 (`rg` 0 hits 시각)

### SPD-4. Reject 후 재타깃 처리
- **동일 content → 다른 저널**: `_build.sh --journal {new}` 로 새 폴더. Zenodo DOI 재발급 불필요. 기존 저널 폴더는 `_archive/`.
- **Revision 후 동일 저널**: `_build.sh --journal {same} --revision {n}`. Response matrix + 변경 manuscript 같이 build.
- **Major revision → 다른 저널**: 새 폴더 + Zenodo new version (content 변경).

## Templates

### `_build.sh` 기본 구조
```bash
#!/bin/bash
# SUBMISSION/_build.sh
# Usage: ./_build.sh --journal {academic_radiology|dir|bjr|mdpi_diagnostics|...} [--revision N]

set -euo pipefail
JOURNAL="$1"
# Per-journal config: word limit, figure limit, reference style, supplement rules
source "configs/${JOURNAL}.sh"

# Build manuscript
pandoc "../7_Manuscript/master.md" \
    --reference-doc "configs/${JOURNAL}_template.docx" \
    --citeproc --csl "configs/${JOURNAL}.csl" \
    -o "${JOURNAL}/manuscript.docx"

# Build supplement
# ... figures, tables, DO_NOT_EDIT_HERE.md touch, MANIFEST.md update
```

### `DO_NOT_EDIT_HERE.md` 내용
```
이 디렉토리는 SUBMISSION/_build.sh 의 build artifact입니다.

본문/supplement/figure는 여기서 편집하지 마세요. master는 /7_Manuscript/ 입니다.

허용된 편집 파일:
- cover_letter.docx
- title_page.docx
- highlights.txt
- checklist.md
- response_to_reviewers.docx (revision 시)
```
