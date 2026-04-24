# RESUME — medsci-skills Phase 1C 진입 (2026-04-24)

**⚠️ 이어서 작업 지시. "마무리할까요?" 금지. `## 즉시 실행` 첫 항목부터.**
**작업 디렉토리**: `/Users/eugene/workspace/medsci-skills`

---

## 즉시 실행

직전 세션에서 Phase 1B-a 회귀 + 1B-b dry-run + 1C scope lock 모두 완료. 미커밋 변경 다수.

1. **commit 묶음** (3개 커밋 분리 권장):
   - `feat(verify-refs): Phase 1B-a strict gate regression + P6 PubMed stub-error fix`
     → `skills/verify-refs/scripts/verify_refs.py`, `tests/test_phase1a_gates.sh`, `tests/fixtures/ssot_project/manuscript/_src/refs_seed_phase1b.bib`, `tests/fixtures/ssot_project/manuscript/index.qmd`
   - `docs(phase1c): scope lock — Hooks Warning Mode (4 subtasks, 2.5h)`
     → `docs/phase1c_scope.md`
   - `chore(followups): P6 done, P7/P8 added from Phase 1B-b dry-run`
     → `FOLLOWUPS.md`, `HANDOFF.md`
   - **제외**: `tests/fixtures/ssot_project/qc/reference_audit.json`(런타임 산출물, .gitignore 추가 필요), `README.md`/`README_FIRST.md`/`installers/`/`scripts/build_classroom_release.py`/`docs/classroom_*.md`(직전 작업과 무관, 별도 세션에서)

2. **Phase 1C 진입** (`docs/phase1c_scope.md` §8 진입점):
   - 순서: 1C.1 (feature flag) → 1C.2 (PreSave hook) → 1C.4 (bypass+audit) → 1C.3 (rule→hook 승격)
   - 1C.2 enforce 트리거는 `SSOT.yaml + qc/migration_complete` 둘 다 (오발화 방지)
   - settings.json 변경은 반드시 `update-config` 스킬 경유
   - 진입 직전 `tests/test_phase1a_gates.sh` 재실행으로 baseline 확인

3. **Phase 1B-b 실 BBT 검증 (deferred)**: 첫 SSOT-conformant 신규 프로젝트 생성 시점까지 defer. SkullFx/CK-1/MA-1 모두 legacy docx — §9 freeze 정책 정합.

**중단 조건**: 1C.2 hook이 verify-refs CLI invoke 시 PreSave latency >3s 발생 → cache 모드(P-신규) FOLLOWUPS 추가 후 1C.4로 우회.

---

## 직전 세션 산출물

- **1B-a**: 4/4 gate PASS. P6 (PubMed stub-error → FABRICATED) 버그 수정.
- **1B-b dry-run**: Polling 로직 4/4 isolation PASS. SkullFx P2가 legacy docx 프로젝트라 실 BBT 검증 불가 발견. 결과 `~/.local/cache/phase1b_b_dryrun/findings.md`. SkullFx 파일 0건 변경.
- **1C scope**: `docs/phase1c_scope.md` (67줄, v1.1.1 §8 정합 + HANDOFF 추정 정정).
- **FOLLOWUPS**: P6 done, P7 (lit-sync precondition assertion) + P8 (polling 회귀 스크립트 추출) 추가.

---

## 블로커 / 대기

- 진행 프로젝트(SkullFx P2 / MA-1 / CK-1) freeze 유지.
- Phase 1B.1 (`SSOT.yaml` template) 미착수 — 1C.2 트리거 활성화의 부분 의존. 1C는 flag만 두고 진입 가능.
- FOLLOWUPS P2/P3/P4/P7/P8 잔존.

---

## 주의사항

- **Phase 1A 계약 (건들지 말 것)**:
  - `/verify-refs`는 `qc/reference_audit.json`만 write. `references/*` 복귀 금지.
  - `/search-lit` → `references/library.bib`, `/lit-sync` → `manuscript/_src/refs.bib`. sole-writer 분리 유지.
  - `[@NEW:topic]`은 유일한 citation placeholder.
- **Legacy skill.yml WARN-only (2026-07-24 sunset)** — 1C에서 강제 마이그레이션 금지.
- **1C.2 hook은 진행 프로젝트 enforce 금지** — `SSOT.yaml + qc/migration_complete` 둘 다 있는 신규만.

---

## 참조

- v1.1.1 계획서: `/Users/eugene/workspace/_retros/medsci-skills_master-plan_2026-04-24_v1.1.1.md` §8 / §9 / §10.4
- 1C scope: `docs/phase1c_scope.md`
- 1B-b findings: `~/.local/cache/phase1b_b_dryrun/findings.md`
- 1B-a 회귀: `tests/test_phase1a_gates.sh`
- Contract: `docs/{ssot_schema_v1,skill_yml_schema_v2,zotero_policy,artifact_contract}.md`
- FOLLOWUPS: `FOLLOWUPS.md`
