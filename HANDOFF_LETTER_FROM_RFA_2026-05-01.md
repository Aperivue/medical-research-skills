# medsci-skills 세션 인계장

**보내는이**: RFA-Adjunct (01_RFA_Adjunct) 세션, Claude (Opus 4.7)
**받는이**: medsci-skills repo 작업 세션 (별도 진행)
**일자**: 2026-05-01
**상태**: 작업 인계 / 검토 요청

---

안녕하세요.

01_RFA_Adjunct 메타분석 프로젝트가 ER (European Radiology) submission 직전 단계에 도달했고, 이 과정에서 medsci-skills repo로 승격해야 할 학습 항목 다수가 누적되어 인계 드립니다. 사용자(유진)께서 본 인계장과 함께 medsci-skills 세션을 별도로 여실 예정이니, 거기서 본 내용을 우선 처리해 주시기 바랍니다.

## 핵심 메시지 한 줄

**RFA-Adjunct에서 발견한 lesson 4건 — (1) Zotero CWYW 자동화로 K-2 단계 제거, (2) Senior MA 멘토(KKW)의 manuscript convention 정형화, (3) AI-drafted document 환각 사고 → 글로벌 룰 신설, (4) 회람 1차 source 보존 워크플로우 정형화 — 가 medsci-skills의 후속 manuscript 프로젝트(02 CBCT_Biopsy, 03 CBCT_Ablation, 04~22 기획) 효율을 즉시 끌어올릴 수 있는 단계입니다.** 우선순위 P1 작업 4건만 집중 처리하시면 차기 manuscript 회람 round에서 동일 코멘트 반복이 자동 차단됩니다.

## 첨부 / 참고 파일 (medsci-skills repo 안)

| 파일 | 용도 |
|------|------|
| `HANDOFF_LESSONS_RFA_KKW_2026-04-26.md` | 본 인계의 **메인 plan**. KKW 멘토 lessons 11항목 + Ishikawa 환각 사고 lesson §G + 우선순위 표. 이 파일의 P1을 먼저 처리. |
| `PLANNED_REFACTOR_manage_refs.md` | `/manage-refs` 신규 스킬 분리 plan. K-2 (Zotero CWYW)에서 검증된 결과 반영됨. |
| `HANDOFF_LETTER_FROM_RFA_2026-05-01.md` | 본 인계장 (이 파일). |

## 1차 source (RFA-Adjunct 프로젝트, 참조 전용)

| 위치 | 자료 |
|------|------|
| `~/workspace/10_Meta_Analysis/01_RFA_Adjunct/8_Review_Comments/1_Professor_Comments/Prof_Kim_Kyungwon/originals/` | KKW 회신 docx 3개 (2026-04-12 directive 회신서 + Claude draft + 2026-04-26 v3 회람 답신) |
| `Prof_Rhim_Hyunchul/originals/` | LHC 회신 docx (2026-04-26) |
| `Shared/` | 회람 이메일 타래 2개 (2026-04-12, 2026-04-26) |
| `Prof_Kim_Kyungwon/comments_extracted.md` | KKW directive(K12-*) + 회람(K-C, K-T, K-S, K-E) 통합 1:1 verify |
| `Prof_Rhim_Hyunchul/comments_extracted.md` | LHC L-1~L-10 |
| `2_Response_Tracking/comment_resolution_tracker.md` | 38건 통합 tracker (37 Resolved + 1 Delegated) |
| `1_Code/zotero_cwyw_temp/` | Zotero CWYW 임시 vendoring (RFA submitted 후 삭제 예정, 정식 `/manage-refs`로 교체) |

## 우선순위 작업 (P1만 — 약 6시간)

`HANDOFF_LESSONS_RFA_KKW_2026-04-26.md` §F 표 참조. P1 작업 4건:

1. **`~/.claude/rules/manuscript-style-classical.md` 신설** — KKW의 senior MA 멘토 convention 11항목 (heading style, abstract sub-headers 콜론, eligibility numbered list, § 금지, AI Disclosure boilerplate 금지, em-dash 회피, et al. Vancouver, ORCID 한 줄 한 명, Table 헤더 점·공백, Figure Legends 위치, British English).
2. **`~/.claude/rules/senior-mentor-circulation.md` 신설** — 회람 1차 source 보존 + 1:1 verify + `8_Review_Comments/` 폴더 구조 표준 + 멘토별 README (KKW의 경우 "AI 패턴 직감 강함, 본문 PROSPERO chronology 금지, References 손-타이핑 금지, Funding grant ID 본인 직접 지정").
3. **`~/.claude/rules/ai-drafted-document-policy.md` 신설** — AI-drafted document verbatim 금지 + SSOT 재검증 + 파일명 `_DO_NOT_USE_VERBATIM` 접미어 강제. **Ishikawa 2017 분모 환각 사고 (RFA-Adjunct 2026-04-12)** 가 motivation. KKW Claude-draft에서 분모 "5/70 vs 12/33" → 원문 35/68. 사용자 SSOT 점검에서 발견 후 v3 exclusion. 잡지 못했으면 환각 분모로 메타분석 진행 → retraction 위험.
4. **`~/.claude/rules/data-integrity.md` 한 줄 보강** — AI-drafted document 재검증 룰을 기존 raw 데이터 무결성 룰과 통합.

## 우선순위 P2 작업 (P1 완료 후, 약 4시간)

5. **`/write-paper` Phase 7 (self-QC) 체크리스트 보강** — § 0건, AI Disclosure 단락 미존재, heading style 일치, eligibility numbered list 변환, Funding grant ID, PROSPERO chronology 본문 미존재, Reference list 손-타이핑 0건.
6. **`/humanize` 패턴 추가** — § 기호, "(Methods §X)" self-reference 패턴, AI Disclosure boilerplate.
7. **`/check-reporting prisma` Figure cross-check 자동화** — RFA-Adjunct 본 세션에서 검증한 본문 vs Figure 1 PRISMA 숫자 cross-check 스크립트를 정식화. 산수 일관성 (records screened = excluded + sought; sought = retrieved; assessed = excluded(stated) + included).

## P3 (선택, 차기)

- `/manage-refs` 신규 스킬 분리 — `PLANNED_REFACTOR_manage_refs.md` 참조. RFA submitted 후 트리거.
- `/circulate-manuscript` 신규 스킬 (회람 자동화, 선택) — RFA-Adjunct에서 회람 + 답신 수집 + 1:1 verification 흐름이 반복적이므로 스킬화 효과 큼. 단, P1-P2 우선.

## 검증 가능 산물 (P1 완료 시)

- `~/.claude/rules/manuscript-style-classical.md` 존재 + 11항목 명시
- `~/.claude/rules/senior-mentor-circulation.md` 존재 + 폴더 구조 + 멘토 README 표준
- `~/.claude/rules/ai-drafted-document-policy.md` 존재 + Ishikawa 사고 사례 인용
- `~/.claude/rules/data-integrity.md` 보강된 한 줄 추가 + cross-link
- `~/.claude/rules/agent-skill-routing.md` 또는 `domain-routing.md`에 위 신규 룰 cross-reference

## 트리거

본 인계장은 **즉시 트리거** (RFA-Adjunct ER submission 대기 중이지만 룰 신설 작업은 병행 가능, 동일 멘토 회람이 02_CBCT_Biopsy / 03_CBCT_Ablation에서 곧 발생할 가능성 높음).

`post-submission-harvest` 룰 ‌적용 시점:
- P1: **즉시** (회람-related 룰은 02_CBCT_Biopsy 회람 시작 전 완료 권장)
- P2: RFA-Adjunct submitted 후
- P3: RFA submitted + 02 시작 시점

## 추가 follow-up

Google Tasks: "medsci-skills /manage-refs 스킬 분리" + "medsci-skills KKW lessons 반영" 두 건 등록되어 있음.

## 사용자 의향

사용자(유진)께서 명시: *"이번에 MA 대가 김경원 교수님 코멘트를 통해 많이 배운거 같아. 이걸 스킬과 하네스 메모리에 잘 기록해야 다른 MA도 잘 할 수 있을 것 같아."*

→ medsci-skills 자체 학습 사이클의 핵심 단계. 본 인계 처리는 다음 manuscript의 회람 round를 단축시키는 직접 ROI를 가져옵니다.

## 답신

처리 완료 시 본 인계장 파일에 한 줄 status update 추가하거나, RFA-Adjunct 프로젝트 메모리 (`~/.claude/projects/-Users-eugene-workspace-10-Meta-Analysis-01-RFA-Adjunct/memory/`)에 답신 메모 두시면 RFA 측에서 인지하겠습니다.

감사합니다.

— 01_RFA_Adjunct 세션 (2026-05-01)
