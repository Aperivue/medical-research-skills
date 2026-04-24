# Peer Review Orchestration (3-tier)

**Extends**: 기존 `phase9_circulation.md` (회람 이메일 템플릿). 이 문서는 internal → external → journal 3중 라운드 전체 orchestration.

## 3-tier 구조

| Tier | Reviewer | 산출물 | 블로킹 포인트 |
|---|---|---|---|
| 1. Internal | Clinical PI (2차 dual) + 방법론 리드 | dual-rating consensus, QUADAS-2 domain table | PI 가용 시점 |
| 2. External | Adversarial GPT review + 독립 동료 (optional) | critique memo, defensive-tone audit | — |
| 3. Journal | Editorial + peer reviewers | reject/revise/accept, Response matrix | — |

## 핵심 규칙

### RO-1. Dual-rating 작업은 "figure + per-study table + supplementary" 3종 동시
- **Problem pattern**: A QUADAS-2 traffic-light figure ships without an accompanying per-study domain table → PRISMA-DTA Item 19 remains PARTIAL. The supplementary table must be planned alongside the figure, not added one revision later.
- **Rule**: QUADAS-2 / RoB2 / GRADE 등 dual-rating 산출물은 설계 단계에서 3종 세트로 기획. Figure만으로 PRISMA-DTA Item 19 완성 아님.

### RO-2. 회람 패키지 발송 전 "2차 리뷰어 리드타임" 선확보
- **Problem pattern**: Manuscript circulated after only first-reviewer screening → the second-reviewer dual rating then blocks the entire revision cycle for weeks, leaving PRISMA Item 9 PARTIAL.
- **Rule**: 회람 이메일 작성 전 clinical PI의 2차 평가 가용 시점 확인. 블로킹 항목은 이메일 본문 최상단 bullet. Circulation 템플릿에 "PH availability window" 필드 추가.

### RO-3. External review는 "defensive tone / bias-inflation / upper-bound framing" 에 특화
- **Problem pattern**: External adversarial review surfaces over-defensive Methods prose (multi-paragraph justifications for pre-specified protocol deviations) and flags that a homogeneity statistic (e.g., Sp I²=0%) is driven by universalized bias rather than true between-study agreement.
- **Rule**: External adversarial review 프롬프트에 (a) defensive tone audit (Methods 내 protocol deviation 설명 ≤3문장 체크), (b) bias-driven homogeneity 해석 체크, (c) upper-bound/lower-bound framing 체크 포함. 상세 rationale은 Supplement로 offload.

### RO-4. Response matrix는 reviewer 응답 + manuscript edit + supplement 동시 추적
- **Problem pattern**: During revision, a numeric value (e.g., a subgroup p-value) changes between versions with no before/after diff recorded in the Response matrix → the reviewer's re-review cannot verify the update.
- **Rule**: Response matrix의 각 comment 행에 (a) reviewer 원문, (b) 응답 요약, (c) manuscript edit locator (section/line), (d) 수치 변경 여부 `[VERIFY-CSV]` 부착. Submission day에 tag 전수 제거.

### RO-5. Protocol deviations는 PROSPERO amendment 1건으로 통합
- **Problem pattern**: Analysis-framework deviation, subgroup deviation, and search-amendment notes split across three manuscript sections and three separate tracker files → the PROSPERO amendment loses provenance.
- **Rule**: 프로젝트 루트 `protocol_deviations_tracker.md` 1개 파일. PROSPERO amendment 제출 시 1 ID로 묶음. Manuscript에서도 단일 citation.

## Templates

- Circulation 이메일: 기존 `phase9_circulation.md` 참조. 본 문서의 RO-2에 따라 "PH availability window" 필드 추가 제안.
- Internal peer review memo: `internal_peer_review_MA{n}_v{N}_{date}.md`
- External GPT review memo: `external_review_gpt_MA{n}_{date}.md`
- Response matrix: 기존 `/revise` skill 템플릿. RO-4에 따라 `[VERIFY-CSV]` 필드 추가.
