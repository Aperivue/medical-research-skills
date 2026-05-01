# PLANNED — `/manage-refs` skill separation

**Status**: planned, not started.
**Trigger**: 01_RFA_Adjunct submitted to European Radiology (post-submission-harvest rule).
**Origin**: 2026-05-01 conversation (RFA-Adjunct K-2 자동화 R&D).

## 배경

레퍼런스 처리 책임이 현재 분산되어 있음:

- `/verify-refs` (독립 skill, audit-only) — PubMed/CrossRef 검증
- `skills/write-paper/scripts/check_citation_keys.py`, `check_xref.py`, `render_manuscript.sh` — write-paper 내부에 묻혀 있는 lifecycle 도구
- `skills/write-paper/references/citation_styles/` — 저널 CSL 라이브러리
- (예정) Zotero CWYW field-code injection — 추가 시 write-paper 더 비대해짐

레퍼런스 파이프라인은 write-paper 외에도 **revise**, **peer-review**, **sync-submission**, **find-journal** (cascade rejection 시 CSL 교체) 모두 사용하는 cross-cutting concern.

## 분리 대상 → `skills/manage-refs/`

```
skills/manage-refs/
├── SKILL.md                         # decision tree (pandoc vs Zotero CWYW vs verify-refs 호출)
├── skill.yml
├── scripts/
│   ├── check_citation_keys.py       # write-paper에서 이전
│   ├── check_xref.py                # 이전
│   ├── render_pandoc.sh             # render_manuscript.sh 이전·개명
│   ├── inject_zotero_cwyw.py        # 신규 (vendored citation_writer.py)
│   └── md_marker_convert.py         # [N]/[N,M] ↔ [@bibkey] 변환 (RFA-Adjunct에서 검증된 임시 스크립트 정식화)
├── citation_styles/                  # CSL 이전 (european-radiology, radiology, ajr, cvir, kjr, vancouver 등)
├── LICENSE.zotero-mcp               # vendored citation_writer 원본 MIT 라이선스
└── NOTICE.md                        # vendored 코드 출처/SHA/변경이력
```

## Decision tree (SKILL.md 핵심)

| 상황 | 도구 | 이유 |
|------|------|------|
| 공저자 Word 협업, review round 빈번 | `inject_zotero_cwyw.py` (또는 사용자 GUI) | native CWYW field code, Word "Refresh" 1회 후 정상 워크플로우 |
| 단일 작성자 submission 굳히기 | `render_pandoc.sh` | frozen output, 재현성 |
| 저널 cascade rejection (ER → JVIR → CVIR) | `render_pandoc.sh` + CSL 교체 | CSL swap만으로 출력 형식 변경 |
| Reviewer revision: ref 1–2개 추가 | Word + Zotero plugin (사용자 GUI) | minimal disruption |
| Reviewer revision: ref 대량 변경 | markdown 재편집 + pandoc 재컴파일 | 일관성 |
| 키 매칭 검증 (UNDEFINED / UNUSED) | `check_citation_keys.py` | 빌드 실패 게이트 |
| PubMed/CrossRef audit | `/verify-refs` 호출 | audit-only (write 책임 분리) |

## Vendored 코드 — Zotero CWYW

- **출처**: https://github.com/alisoroushmd/zotero-mcp
- **파일**: `src/zotero_mcp/citation_writer.py`
- **Upstream SHA**: `ed5dfb718b78f355f300545eb375aec7a543e027` (2026-05-01)
- **라이선스**: MIT, © 2026 Ali Soroush
- **의존성**: `python-docx`만 (이미 medsci-skills에서 fill-icmje-coi, fill-protocol이 사용)
- **Self-contained 검증**: `from .` relative import 0건, 다른 zotero-mcp 모듈 의존 없음 (확인 2026-05-01)

### 통합 시 추가할 헤더 (모든 vendored 파일 최상단)

```python
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Ali Soroush
# Vendored from https://github.com/alisoroushmd/zotero-mcp
#   src/zotero_mcp/citation_writer.py @ ed5dfb71
# Imported into medsci-skills <DATE>. <변경 요약 or "No functional modifications.">
# Full license: ./LICENSE.zotero-mcp
```

### NOTICE.md 항목

```markdown
## Third-party components

### scripts/inject_zotero_cwyw.py
- Source: alisoroushmd/zotero-mcp (https://github.com/alisoroushmd/zotero-mcp)
- File: src/zotero_mcp/citation_writer.py
- Upstream SHA: ed5dfb718b78f355f300545eb375aec7a543e027 (2026-05-01)
- License: MIT, © 2026 Ali Soroush
- Modifications: <list or "none">
```

### Metadata 인터페이스

`insert_citations(document_path, item_data: dict[key→Zotero metadata], user_id, output_path)` 의 `item_data`는 기존 read-only MCP `54yyyu/zotero-mcp` `zotero_get_item_metadata` 결과 dict와 동일 포맷. 신규 MCP 서버 등록 불필요.

## 마이그레이션 순서

1. `skills/manage-refs/` 디렉토리 + SKILL.md skeleton 작성
2. `write-paper/scripts/{check_citation_keys.py, check_xref.py, render_manuscript.sh}` → `manage-refs/scripts/` 이전 (path-aware fix)
3. `write-paper/references/citation_styles/` → `manage-refs/citation_styles/` 이전
4. Vendored `inject_zotero_cwyw.py` + LICENSE.zotero-mcp + NOTICE.md 추가
5. RFA-Adjunct 임시 스크립트 (`1_Code/zotero_cwyw_temp/`) 에서 검증된 `md_marker_convert.py` 정식화
6. `write-paper/SKILL.md` Phase 7.6 → `/manage-refs` 호출 1줄로 축소
7. `revise`, `peer-review`, `sync-submission` 의 reference 관련 코드 → `/manage-refs` 호출로 통일
8. `~/.claude/rules/manuscript-references.md` decision tree 재작성 (`/manage-refs` 단일 진입점)
9. `~/.claude/rules/agent-skill-routing.md` 표 업데이트
10. RFA-Adjunct `1_Code/zotero_cwyw_temp/` 삭제 + 정식 `/manage-refs` 호출로 교체
11. 02_CBCT_Biopsy, 03_CBCT_Ablation 등 active manuscript 횡전개

## RFA-Adjunct 임시 vendoring (분리 전 잠정 위치)

- 위치: `/Users/eugene/workspace/10_Meta_Analysis/01_RFA_Adjunct/1_Code/zotero_cwyw_temp/`
- 구성: `citation_writer.py` (vendored), `LICENSE.zotero-mcp`, `convert_v4_markers.py`, `build_v4_docx.py`
- 수명: RFA submitted 후 본 스킬 분리되면 즉시 삭제

## Known limitations + workarounds (RFA-Adjunct 검증 결과 2026-05-01)

1. **BIBL field 첫 build 시 빈 bibliography**: `citation_writer.add_bibliography_field`가 만드는 BIBL field는 `separate→end` 사이가 비어 있는 stub. Zotero Refresh는 빈 BIBL을 "사용자 정의 비어 있는 bibliography"로 간주하고 채우지 않음. **워크플로우**: 첫 build 후 Word에서 Zotero **Add/Edit Bibliography** 1회 명시적 실행 필요. 이후 ref 변경(reviewer revision 등)은 Refresh만으로 자동 갱신.
   - SKILL.md에 워크플로우 노트로 명시 예정.
   - 잠재적 fix: BIBL field에 placeholder bibliography content를 미리 inject (시간 있을 때 prototyping).

2. **webpage / non-journal item types**: upstream `citation_writer.zotero_to_csl_json`의 `_ITEM_TYPE_MAP`에 `webpage`, `report` 등이 없어 fallback `"article"` + 누락 필드(URL, accessDate)로 매핑됨. **결과**: Zotero가 field를 silent fail. **fix**: build script에서 Zotero `?format=csljson` API로 native CSL-JSON을 직접 가져와 사용 (RFA-Adjunct에서 검증). `inject_zotero_cwyw.py`에는 이 native fetch가 default로 들어가야 함.

3. **마커 vs Zotero rendered output 구분 필요**: surgical 후속 패치(ref 추가) 시 정규식 `[N]`이 plain marker만 매칭해야 함. Refresh 후 Zotero가 만든 rendered superscript `[N]`도 plain text로 보일 수 있어 충돌. **워크플로우**: 후속 ref 추가 시 patch 대신 markdown 재편집 + 전체 build_v4_zotero_docx.py 재실행 (clean rebuild) 권장. surgical은 위험.

## Out of scope (이 분리에서는 안 다룸)

- `/verify-refs` 통폐합 — 이미 audit-only로 깔끔히 분리되어 있음. 호출만 한다.
- Zotero MCP 서버 자체 추가/교체 — vendored single file로 충분. 기존 read-only `54yyyu/zotero-mcp` 유지.
- BBT auto-export 워크플로우 변경 — `~/.claude/rules/zotero-workflow.md` 그대로.

## 관련

- `~/.claude/rules/manuscript-references.md` — decision tree (재작성 대상)
- `~/.claude/rules/agent-skill-routing.md` — 라우팅 표 (업데이트 대상)
- `~/.claude/rules/post-submission-harvest.md` — 트리거 룰
- `~/.claude/projects/-Users-eugene-workspace-10-Meta-Analysis-01-RFA-Adjunct/memory/zotero_cwyw_automation.md` — 원래 결정 메모
