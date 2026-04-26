# RESUME — medsci-skills (2026-04-24 post-release)

**⚠️ 이어서 작업 지시. "마무리할까요?" 금지. `## 즉시 실행` 첫 항목부터.**
**작업 디렉토리**: `/Users/eugene/workspace/medsci-skills`

---

## 즉시 실행

직전 세션 결과물이 전부 live. 이 HANDOFF는 **다음 세션 진입점이 비어있다**는 신호 — 새 요청으로 시작하면 됨. 만약 follow-up 과제가 필요하면 아래 후보 중 하나를 골라 진행.

1. **(선택) batch-cohort Joo 2026 replication 경고 repo 역반영**
   - 백업 위치: `~/.local/cache/medsci-installed-backup-20260424-173740/batch-cohort/references/variable_coding_registry.md`
   - repo 버전(`skills/batch-cohort/references/variable_coding_registry.md`)과 `diff`로 삭제된 4줄 복원 후 커밋.
2. **(선택) define-variables 홈페이지 반영**
   - `aperivue-web/src/content/data/skills.{en,ko}.json`에 37번째 엔트리 추가, 페이지 메타 `36 → 37`, pipelineSteps 추가.
   - 기존 v2.1.0 블로그 포스트에 "follow-up: define-variables" 짧은 섹션 append.
3. **(선택) drift-risk 스킬 내용 양방향 검토**
   - 백업 5개(`author-strategy / batch-cohort / cross-national / lit-sync / replicate-study`) vs repo diff, installed-only 내용 있으면 repo로 pull.

---

## 블로커 / 대기

- 없음. v2.1.0 / v2.1.1 릴리스 + 홈페이지 블로그 배포 + skill registry symlink 전부 완료.

---

## 주의사항

- **Symlink 구조**: `~/.claude/skills/*` 36개는 repo로 symlink. repo 편집 = 즉시 live. 반대로 `~/.claude/skills/`에서 직접 수정하지 말 것 (repo 파일을 수정하는 것과 동일).
- **드리프트 백업**: `~/.local/cache/medsci-installed-backup-20260424-173740/` (5개 스킬 교체 전 스냅샷). 필요 시 참조, 오래되면 삭제 가능.
- **define-variables Anti-Hallucination 섹션**: 이번 세션에서 validator 통과용으로 추가됨. 다른 세션에서 이 스킬 편집 시 섹션 유지 필요.
- **dist/ gitignored**: 릴리스 ZIP은 local-only. `python3 scripts/build_classroom_release.py` 재빌드 후 `gh release upload`.
- **정리 원칙**: pre-commit hook이 `validate_skills.sh` + `tag_cleanup_gate.sh` 자동 실행. 커밋 전 기대.

---

## 참조

- FOLLOWUPS: `FOLLOWUPS.md`
- Release: https://github.com/Aperivue/medsci-skills/releases/tag/v2.1.1
- Homepage blog: https://aperivue.com/ko/blog/medsci-skills-v2-1-0-reference-safety
