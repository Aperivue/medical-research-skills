# Handoff — KKW Senior MA Mentor Lessons → medsci-skills 룰/스킬 업데이트

**작성**: 2026-05-01 (RFA-Adjunct 세션, 사용자 지시)
**대상**: medsci-skills repo 작업 세션 (별도 진행)
**Why**: 김경원(KKW) 교수님 — Asan/UoU College of Medicine, MA 분야 senior 멘토. RFA-Adjunct에서 **두 차례** 회신 — (1) 2026-04-12 initial directive (메타분석 구조 자체 재설계: Primary outcome 변경, dual-tool 권고, AI-draft 첨부 + verbatim 사용 금지 명시), (2) 2026-04-26 v3 회람 답신 (구체 수정 코멘트·track-changes). 다른 MA 프로젝트(02_CBCT_Biopsy, 03_CBCT_Ablation, 04~22 기획본)에 동일 멘토 회람 가능성 높음 — 사전에 자동 처리 가능한 항목은 스킬·룰로 승격해야 동일 코멘트 반복 회피.

## 1차 source

### 2026-04-12 KKW Initial Directive (메타분석 구조 재설계)
- `Prof_Kim_Kyungwon/originals/2026-04-12_kkw_directive_response.docx` — KKW가 Claude로 작성한 directive 회신서
- `Prof_Kim_Kyungwon/originals/2026-04-12_kkw_claude_draft_DO_NOT_USE_VERBATIM.docx` — ⚠ 환각 포함, verbatim 금지
- `Shared/2026-04-12_email_thread.md` — directive 이메일 전문 + Ishikawa 환각 사고 경위

### 2026-04-26 v3 회람 답신
- `Prof_Kim_Kyungwon/originals/2026-04-26_kkw_revision.docx` — 코멘트 6 + track-changes 16 ins/15 del
- `Prof_Rhim_Hyunchul/originals/2026-04-26_lhc_revision.docx` — 코멘트 10
- `Shared/2026-04-26_email_thread.md` — 회람 이메일 전문

### 추출 + verify
- `Prof_Kim_Kyungwon/comments_extracted.md` — KKW directive(K12-*) + 회람(K-C, K-T, K-S, K-E) 통합 1:1
- `Prof_Rhim_Hyunchul/comments_extracted.md` — LHC L-1~L-10
- `2_Response_Tracking/comment_resolution_tracker.md` — 27건 1:1 verify (K12-* 별도)

## 학습 항목 → medsci-skills 변경안

### A. 글로벌 룰 신설 — `manuscript-style-classical.md`

신규 파일: `~/.claude/rules/manuscript-style-classical.md`

**Why**: KKW 코멘트 K-C1 ("AI 쓴 티 안내는 클래식 형태로") + 직접 수정 결과를 일반화. senior reviewer가 즉시 "AI가 썼다"고 판단하는 시그널을 제거하는 글로벌 정책.

**핵심 룰**:
- Section heading 본문 표기는 `## **METHODS**` 등 대문자+bold (KKW preference). Abstract / Figure Legends / Table headers는 `## ` h2 유지.
- Abstract sub-headers는 콜론 + bold: `**Objectives:**`, `**Methods:**`, `**Results:**`, `**Conclusion:**`, `**Key Points:**`. inline 줄바꿈 X.
- Table 헤더는 점·공백 정확히: `Table 1. Characteristics of included studies` 형식. `Table1:`, `**Table 1**:` 등 변형 금지.
- Authors / Affiliations / ORCID 한 줄당 한 명 (`\-` prefix로 markdown bullet 회피).
- Eligibility / Inclusion criteria 등 enumerable list는 산문 X, numbered list `(1)... (2)...` 사용 — KKW track-changes에서 산문 → numbered 변경 패턴 다수.
- § 기호 절대 금지 — KKW가 "AI인 줄 알아보는 표식"으로 명시. `grep -c "§" = 0` 강제.
- "Artificial Intelligence Disclosure" / "AI Acknowledgement" 단락 manuscript 본문에 미포함 — 저널이 submission 양식에서 별도로 요구할 때만 cover letter / 양식에 기재.
- `"It is important to note"`, `"In conclusion"` 등 18 AI 패턴 — 기존 `writing-style.md` 확장.
- Em-dash 남용 회피 (manuscript당 25건 미만 권장).
- "We" 1인칭 / "we believe / we think" 금지 (이미 writing-style.md).

`~/.claude/rules/writing-style.md`와 차이: writing-style은 일반 학술 톤, classical은 senior MA reviewer 대비 보강. 두 파일 cross-reference.

### B. 기존 스킬 업데이트

#### B-1. `/write-paper` — Phase 7 (self-QC) 보강
체크리스트 추가:
- [ ] § 기호 0건 (`grep -c "§"`)
- [ ] AI Disclosure 단락 미존재 (저널이 양식에서 요구하면 cover letter 기재)
- [ ] Section heading style 일치 (Methods/Results/Discussion = 대문자+bold; Abstract/Figure Legends = h2)
- [ ] Eligibility / Inclusion criteria 산문 → numbered list 변환 확인
- [ ] Funding 섹션에 grant ID 명시 (PI 또는 senior author 직접 입력 필요)
- [ ] PROSPERO chronology / amendment lodging timeline 본문 미존재, supplementary로 위임
- [ ] Reference list 손-타이핑 0건 (전수 reference manager 처리 — 이미 manuscript-references.md)

#### B-2. `/humanize` — 새 패턴 추가
기존 18 AI 체크리스트에 추가:
- § 기호
- "(Methods §X)", "(Results §Y)" 형식의 self-reference (KKW가 § 삭제하면서 이 패턴도 함께 제거함)
- "Artificial Intelligence Disclosure" / "Generative AI was not used" 류 boilerplate

#### B-3. `/check-reporting prisma` — 본문 vs Figure 1 cross-check 자동화
KKW K-4 / K-C6: "PRISMA 2020 표준 다이아그램 + flow와 number 확인 필수".
PRISMA Figure 자동 검증 스크립트 (RFA-Adjunct 본 세션에서 수행):
- 본문 PRISMA 숫자 추출 (예: 315/122/186/7/111/204/102/84/3/15)
- Figure caption 또는 PPT 텍스트에서 동일 숫자 추출
- 산수 일관성 (records screened = excluded + sought; sought = retrieved; assessed = excluded(stated reasons) + included)
- 산출: PRESENT / MISSING / MISMATCH 표
- `~/.claude/rules/numerical-safety.md`와 통합 (PRISMA 5-way consistency check + Figure)

#### B-4. `/find-journal` 또는 신규 룰 — Author 권한 / Funding ID 사전 수집
회람 직전 단계에서 senior author에게 다음 항목 직접 입력 요청 (자동화 불가):
- Funding grant IDs
- ORCID
- Affiliation 정확 표기
- COI disclosure
- Corresponding author 확정
- Recommended reviewers (편지에서 LHC가 명시적으로 "특별히 추천 reviewer 없음" 회신 — 즉 reviewer 추천도 회람의 명시적 항목으로 둘 것)

이를 `~/.claude/templates/circulation_memo_template.md` (KKW/LHC 회람용)로 정형화.

### C. 신규 스킬 후보

#### C-1. `/manage-refs` — 이미 별도 plan 존재
참조: `PLANNED_REFACTOR_manage_refs.md` (medsci-skills repo). KKW K-E2 ("References EndNote 등 reference manager 전면 수정")가 이 스킬의 가장 강력한 use case.

해당 plan 추가 항목:
- KKW Vancouver 6+ author "et al." 룰 — ER CSL 자동 처리됨을 명시 (RFA에서 검증)
- Reference list 손-타이핑 절대 금지 룰은 `manuscript-references.md`에 이미 존재 — KKW 코멘트 #1 (2026-04-26 KKW 사고)이 이 룰의 motivation으로 인용 가능
- `inject_zotero_cwyw.py` 가 webpage / 기타 non-journal 항목 처리하도록 native CSL-JSON fetch (`?format=csljson`) 사용 — RFA Wells NOS 케이스에서 검증
- BIBL field 첫 build 시 "Add/Edit Bibliography" 1회 manual 클릭 필요 (Zotero CWYW 구조적 한계) — workflow 노트로 명시

#### C-2. `/circulate-manuscript` — 회람 자동화 스킬 (선택)
RFA-Adjunct에서 회람 + 답신 수집 + 1:1 verification 흐름이 반복적. 잠재 신규 스킬:
- 입력: manuscript md + 공저자 list + 회람 마감
- Phase 1: 회람 메일 draft 생성 (cover, attachments staging)
- Phase 2: Gmail draft 생성 (gws CLI)
- Phase 3: 답신 docx 수집 → comments + track-changes 자동 추출 → `8_Review_Comments/` 적재
- Phase 4: 1:1 verification table (manuscript ↔ 코멘트 grep)
- Phase 5: `comment_resolution_tracker.md` 생성

이게 매 manuscript마다 재현되는 작업이므로 스킬화 효과 큼.

### D. 새 글로벌 룰 — `senior-mentor-circulation.md`

핵심:
- **회람 1차 source는 반드시 프로젝트에 저장**: `8_Review_Comments/1_Professor_Comments/Prof_<lastname>_<firstname>/originals/YYYY-MM-DD_<initials>_revision.docx` 또는 `_email.md`. self-referential reflection log (예: `v4_change_summary.md`)는 1차 source 대체 불가.
- **반영 후 1:1 verification 필수**: 1차 source의 코멘트·track-changes ↔ manuscript 본문 grep/XML diff. `comment_resolution_tracker.md` 작성.
- **회람 폴더 구조**:
  ```
  8_Review_Comments/
  ├── 0_Internal_Review/      # codex / self-review
  ├── 1_Professor_Comments/
  │   ├── Prof_<Name>/
  │   │   ├── originals/      # 1차 source (docx, eml, screenshot)
  │   │   ├── comments_extracted.md  # 추출 + verify table
  │   │   └── README.md       # 멘토 특이 선호 메모
  │   └── Shared/             # 회람 메일 타래
  ├── 2_Response_Tracking/
  │   └── comment_resolution_tracker.md
  └── 3_Independent_Review/   # 공저자 / KDY 등
  ```
- **멘토 특이 선호** (`Prof_<Name>/README.md`)에 누적: KKW의 경우 "AI 패턴 직감 강함, § 표시 금지, classical heading style, References 손-타이핑 금지, Funding grant ID 본인이 직접 지정, 본문 PROSPERO chronology 금지". 다음 manuscript 회람 전에 이 README 검토 → 사전 차단.

### E. memory 보강

다음 메모리 파일 추가 (medsci-skills repo 또는 글로벌 `~/.claude/projects/...memory/`):

- `feedback_kkw_manuscript_conventions.md` — KKW 멘토 특이 선호 누적 (전 RFA + 향후 02/03/etc.)
- `feedback_lhc_corresponding_author.md` — 임현철 corresponding author 패턴 (methodology는 KKW 위임, ER>JVIR>CVIR cascade, reviewer 추천 안 함)

이미 존재하는 `feedback_kim_kw_prospero_assessor.md`, `feedback_self_mail_as_draft.md` 등과 통합 검토.

### F. 후속 액션 (medsci-skills 세션에서)

| 우선순위 | 작업 | 산출 |
|----------|------|------|
| P1 | `~/.claude/rules/manuscript-style-classical.md` 신설 | 위 §A 내용 |
| P1 | `~/.claude/rules/senior-mentor-circulation.md` 신설 | 위 §D 내용 |
| P1 | `~/.claude/rules/ai-drafted-document-policy.md` 신설 | 위 §G-1 (Ishikawa 환각 사고 기반) |
| P1 | `~/.claude/rules/data-integrity.md` 한 줄 보강 | §G-2 (AI-draft 재검증 룰) |
| P2 | `/write-paper` Phase 7 self-QC 체크리스트 보강 | 위 §B-1 |
| P2 | `/humanize` 패턴 추가 (§, AI Disclosure boilerplate) | 위 §B-2 |
| P2 | `/check-reporting prisma` Figure cross-check 자동화 | 위 §B-3 |
| P3 | `/manage-refs` 분리 (별도 plan PLANNED_REFACTOR_manage_refs.md) | 본 plan 참고 |
| P3 | `templates/circulation_memo_template.md` | 회람 메일 정형화 |
| P4 | `/circulate-manuscript` 신규 스킬 (선택) | 회람 자동화 |

P1-P2가 완료되면 02_CBCT_Biopsy, 03_CBCT_Ablation 등 다음 manuscript에서 KKW 회람 코멘트가 사전 차단 / 자동 검증되어 회람 round 단축 효과.

### G. 핵심 lesson — AI-drafted starting document 환각 사고 (2026-04-12)

**사건**: KKW가 RFA-Adjunct 메타분석 directive를 Claude로 작성하여 첨부 (`2026-04-12_kkw_claude_draft_DO_NOT_USE_VERBATIM.docx`). KKW 본인도 메일에 명시: *"이 내용 (수치, 레퍼런스 등) 그냥 받아들이시면 절대 안되고, 참고해서 직접 모든 통계결과 내시고, Risk of Bias 새로 하시고, figure/table 새로 만드시는 등의 revision 하셔야 합니다."*

그러나 사용자가 v2 작성 과정에서 일부 수치를 KKW draft에서 그대로 따라가다가 SSOT(원문 PDF)와 어긋나는 방향으로 한 차례 진행 → 후속 점검에서 환각 발견 → 되돌림. 시간 손실 발생.

**환각 예시**:
- **Ishikawa 2017 분모**: Claude draft에서 "treatment support 5/70 vs no support 12/33"으로 추출 → 실제 원문(PDF) 검증 결과 APE arm 35/68. 분모 자체가 다름.
- 결과: Ishikawa 2017은 v3에서 exposure-definition grounds로 base dataset 제외. v4 Limitations First 항목 + Supplementary consensus log §3에 사고 경위 기재.
- LTP/OR 수치: KKW draft 값 전수 폐기 → 사용자 R/Python 재계산.

**lesson — senior mentor가 보낸 AI-drafted document도 SSOT 재검증 필수**:

1. **Trust hierarchy**:
   - SSOT (원문 PDF + 자체 분석 스크립트 stdout) > 1
   - Senior mentor의 직접 텍스트 (이메일 본문 / track-changes) > 2  
   - Senior mentor가 첨부한 AI-draft = **2와 같지 않음**, 1차 source 아님 (참고용 starting point)
2. **Ishikawa 사고가 잡힐 수 있었던 이유**: 사용자가 "지적해주신 내용 바탕으로 문헌들 꼼꼼히 점검" 정책을 견지. 모든 분모/수치는 원문 PDF에서 재검증.
3. **반대 사례** (실패 시나리오): KKW draft를 verbatim 흡수하면 v2 PROSPERO 등록 + 메타분석 결과가 환각 분모로 산출됨 → 회람·revision까지 진행되다 reviewer 또는 reader가 발견하면 retraction 위험.

### G-1. 신규 글로벌 룰 — `~/.claude/rules/ai-drafted-document-policy.md`

**핵심 룰**:

```markdown
# AI-Drafted Document Policy

## 원칙
Senior mentor / collaborator / external party가 AI-drafted document(Claude/ChatGPT/Gemini draft)를 1차 source로 첨부하더라도 **verbatim 흡수 금지**. AI-draft는 *starting reference*이지 *authoritative source* 아님.

## When triggered
첨부 docx / md / xlsx 파일이 다음 중 하나에 해당:
- 파일명에 "claude", "ai_draft", "gpt", "draft" 명시
- 메일 본문에 "AI 도움 받아", "Claude로 작성", "참고삼아" 류 disclaimer
- 발신자가 본인 회신에 verbatim 사용 금지 명시

## 의무 절차
1. AI-draft 파일을 프로젝트에 저장할 때 파일명에 `_DO_NOT_USE_VERBATIM` 또는 `_AI_DRAFT_REFERENCE_ONLY` 접미어 필수.
2. 모든 인용 수치(N, 분모, OR, CI, p-value, 저자명, 연도, 페이지)는 원문 PDF + 자체 분석 스크립트 stdout으로 재검증.
3. 환각 의심 항목 발견 시 즉시 사고 로그 (`memory/ai_draft_hallucination_<topic>.md` 또는 `extraction_consensus_log.md`)에 기재.
4. 인용 검증은 `/verify-refs --strict` (PubMed/CrossRef + first-author cross-check) 적용.

## 환각 회피 워크플로우 (메타분석 컨텍스트)
- AI-draft에 등장하는 study별 N / event count → 원문 PDF의 해당 Table / Figure 재판독.
- AI가 Kaplan-Meier에서 event count를 역산해주면 100% 의심 (역산 자체는 AI가 잘함, 그러나 분모 정의 일관성은 환각 빈발).
- AI가 제공한 OR / CI는 자체 R/Python 재계산 후 교체.

## 사고 사례
- 2026-04-12 RFA-Adjunct: KKW Claude-draft에서 Ishikawa 2017 "treatment support 5/70 vs no support 12/33" → 원문 35/68. 분모 환각. 결과적으로 Ishikawa 2017 v3 exclusion 결정.
- (참조) 2026-04-26 CK-1 paper 3 ref 8 환각: DOI는 진짜인데 첫 저자 환각 ("Ebrahimi" → 실제 "Ballard"). `~/.claude/rules/citation-safety.md` v1.1.2 motivation.

## 관련 룰
- `~/.claude/rules/citation-safety.md` — DOI/PMID 진위 + first-author cross-check
- `~/.claude/rules/data-integrity.md` — raw 데이터 무결성 + 손-입력 금지
- `~/.claude/rules/dictionary-first.md` — DB-backed 연구의 컬럼명 verbatim 인용 (유사 정신)
```

### G-2. `data-integrity.md` 보강

기존 룰에 다음 한 줄 추가:
> AI-drafted starting document(senior mentor가 첨부한 Claude/GPT draft 등)에 등장하는 모든 N / event count / 수치는 원문 PDF 재검증 후 사용. AI-draft는 1차 source 아님 — 별도 룰 `ai-drafted-document-policy.md` 참조.

### G-3. `/meta-analysis` Phase 2 (Search/Screening) 체크리스트 보강

신규 항목:
- [ ] **AI-drafted starting document 식별**: collaborator가 첨부한 AI-draft가 있는가? 있다면 파일명에 `_AI_DRAFT_REFERENCE_ONLY` 접미어 강제 + 모든 study별 N / event count 원문 PDF 재검증.
- [ ] **분모 정의 cross-check**: 한 study에서 여러 분모(treatment-naïve / full-cohort / per-arm) 가능성 점검. extraction_consensus_log에 분모 선택 근거 verbatim 기재.

### G-4. `senior-mentor-circulation.md` 룰에 추가 (앞 §D 보강)

신규 항목:
- 회람 시 senior mentor가 AI-draft를 첨부하는 경우 별도 처리 (위 G-1 룰 적용).
- 멘토 README.md에 멘토의 AI 도구 사용 패턴 기록 (KKW의 경우: "Claude로 directive draft + 이메일에 verbatim 금지 명시 + 본인이 직접 humanize 약속").

## 트리거

- 본 handoff 파일 = trigger. medsci-skills 세션에서 이 파일 읽고 P1부터 진행.
- post-submission-harvest 룰과 결합: RFA-Adjunct ER submitted 후 본 plan 실행 시점.
- 별개 세션 작업 위치: `/Users/eugene/workspace/medsci-skills/`

## 관련

- `PLANNED_REFACTOR_manage_refs.md` — /manage-refs 신규 스킬 분리 (RFA에서 검증된 결과 반영)
- `~/.claude/rules/post-submission-harvest.md` — 마일스톤 후 학습 추출 룰
- `~/.claude/rules/manuscript-references.md` — 손-타이핑 금지 룰 (이미 존재)
- `~/.claude/rules/writing-style.md` — 18 AI 패턴 체크리스트 (확장 대상)
- `~/.claude/rules/numerical-safety.md` — PRISMA 5-way consistency (Figure 추가 대상)
- RFA-Adjunct verification artifacts:
  - `8_Review_Comments/1_Professor_Comments/Prof_Kim_Kyungwon/comments_extracted.md`
  - `8_Review_Comments/1_Professor_Comments/Prof_Rhim_Hyunchul/comments_extracted.md`
  - `8_Review_Comments/2_Response_Tracking/comment_resolution_tracker.md` (27 items 1:1 verified)
