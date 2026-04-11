# Handoff: LLM Transparency — STARD-AI, Journal AI Policies, CANGARU

> Date: 2026-04-11
> Trigger: medsci-skills에서 LLM 사용 투명성 기술 필요성 논의
> Prior session: MI-CLEAR-LLM 체크리스트 추가 + write-paper LLM disclosure 기능 추가
> Commit: 303cd75 (pushed to main)

---

## Completed (this session)

| # | Task | Files | Status |
|---|------|-------|--------|
| 1 | MI-CLEAR-LLM 체크리스트 (6항목) | `check-reporting/references/checklists/MI_CLEAR_LLM.md` (new) | Done |
| 2 | check-reporting SKILL.md 업데이트 | 21개 가이드라인, auto-detection, 보조 가이드라인 규칙 | Done |
| 3 | LICENSES.md 업데이트 | CC BY-NC 4.0 항목 추가 | Done |
| 4 | write-paper LLM disclosure 기능 | `--no-llm-disclosure` opt-out, 3곳 템플릿 | Done |
| 5 | Journal Profile AI Disclosure Policy (Tier 1) | 6 journals x 2 dirs + 2 SKILLs | Done |

---

## Remaining: Task 1 — STARD-AI 체크리스트 추가 (Priority: Medium)

### Context

- STARD-AI: 2025 Nature Medicine (vol. 31, pp. 3283-3289) 발표
- AI diagnostic accuracy 연구를 위한 보고 가이드라인
- MI-CLEAR-LLM과 함께 LLM 진단정확도 연구에 쌍으로 적용
- EQUATOR Network 등재: https://www.equator-network.org/reporting-guidelines/the-stard-ai-reporting-guideline-for-diagnostic-accuracy-studies-using-artificial-intelligence/
- 240+ 국제 전문가 참여 개발

### Steps

1. STARD-AI 원문에서 체크리스트 항목 추출 (Nature Medicine + EQUATOR 보충자료)
2. `check-reporting/references/checklists/STARD_AI.md` 생성
   - 기존 `STARD.md` (2015)를 템플릿으로 사용
   - STARD 2015와의 차이점(AI-specific 항목) 명시
3. `check-reporting/SKILL.md` 업데이트:
   - bundled list에 추가 (21→22)
   - auto-detection: `| Diagnostic accuracy study | STARD 2015 | STARD-AI |` 이미 있음 — 파일만 만들면 됨
   - STARD vs STARD-AI 사용 규칙: TRIPOD처럼 완전 대체인지, 보조인지 확인 필요
4. `LICENSES.md`에 라이선스 추가

### Verification

```bash
grep -n "STARD" skills/check-reporting/SKILL.md
# auto-detection 행에 STARD-AI가 AI Extension으로 이미 참조됨 (line ~61)
# 현재 STARD_AI.md 파일은 없음 — LLM knowledge fallback 상태
```

---

## ~~Remaining~~ Completed: Task 2 — Journal Profile AI Disclosure Policy 필드

> **Done (2026-04-11).** Tier 1 저널 6개 프로필에 `## AI Writing Disclosure Policy` 섹션 추가 완료.
> Nature/Science 일반 저널은 프로필 미존재 — Nature Medicine으로 대체.

### Completed files (8 profiles + 2 SKILLs)

| File | Type |
|------|------|
| `write-paper/references/journal_profiles/Radiology.md` | Detailed |
| `write-paper/references/journal_profiles/RYAI.md` | Detailed |
| `write-paper/references/journal_profiles/JAMA.md` | Detailed |
| `write-paper/references/journal_profiles/The_Lancet.md` | Detailed |
| `write-paper/references/journal_profiles/The_BMJ.md` | Detailed |
| `write-paper/references/journal_profiles/Nature_Medicine.md` | Detailed |
| `find-journal/references/journal_profiles/JAMA.md` | Compact |
| `find-journal/references/journal_profiles/Nature_Medicine.md` | Compact |
| `write-paper/SKILL.md` | Journal-Specific Overrides updated |
| `find-journal/SKILL.md` | Output format + profile parsing updated |

### Remaining sub-tasks
- Tier 2 (AJR, European Radiology, KJR, npj DM, Lancet DH) — 5개
- Tier 3 (나머지 46개) — 대부분 "Not specified" or ICMJE default

---

## Remaining: Task 3 — CANGARU 가이드라인 모니터링 (Priority: Low)

### Context

- CANGARU: Elsevier + Springer Nature + Wiley + eLife + Cell + BMJ + COPE 공동
- Giovanni Cacciamani (USC) 주도
- 2024년 8월 완성 목표였으나 아직 미확정 (2026-04 기준)
- LLM 사용 금지 사항 + 필수 공개 사항 포함 예정
- 매년 업데이트 계획

### Steps

1. 웹서치: `CANGARU AI publishing guidelines 2025 OR 2026`
2. 확정 시 check-reporting에 추가할지 또는 write-paper의 disclosure 정책에 반영할지 판단
3. 현재는 별도 작업 불필요 — 주간 리뷰 시 웹서치로 상태 확인

---

## Remaining: Task 4 — README/블로그 업데이트 (Priority: Low)

### Context

- medsci-skills README에 "20 guidelines" → "21 guidelines" 반영
- LLM disclosure 기능은 블로그 포스트 소재로 가치 있음

### Steps

1. `README.md` 업데이트: 가이드라인 수, MI-CLEAR-LLM 언급, LLM disclosure 기능 설명
2. (선택) aperivue.com/blog에 "LLM Transparency in Medical Research" 포스트 — `/biz-seo-blog`로

---

## Architecture Notes

### MI-CLEAR-LLM vs LLM Disclosure 구분 (혼동 주의)

| | MI-CLEAR-LLM | LLM Disclosure |
|---|---|---|
| **용도** | LLM 정확도를 *연구*할 때 | LLM으로 논문을 *작성*할 때 |
| **스킬** | check-reporting | write-paper |
| **위치** | 별도 체크리스트 | Methods + Acknowledgments + Cover Letter |
| **근거** | Park et al. KJR 2024/2025 | ICMJE 2025 + COPE |
| **선택** | auto-detect (LLM 연구이면 적용) | `--no-llm-disclosure`로 opt-out |

### 파일 위치

```
medical-research-skills/
├── skills/
│   ├── check-reporting/
│   │   ├── SKILL.md                    ← 21 guidelines (MI-CLEAR-LLM 추가됨)
│   │   └── references/
│   │       ├── checklists/
│   │       │   └── MI_CLEAR_LLM.md     ← NEW (6 items)
│   │       └── LICENSES.md             ← CC BY-NC 4.0 추가됨
│   └── write-paper/
│       └── SKILL.md                    ← LLM Disclosure 섹션 + --no-llm-disclosure 플래그
└── docs/
    └── handoff_llm_transparency.md     ← THIS FILE
```
