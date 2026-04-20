# RESUME — medsci-skills (2026-04-20 세션 인계)

**⚠️ 이 파일은 이어서 작업하라는 지시입니다. "마무리할까요?" 질문 금지.**
**진입점**: 아래 `## 즉시 실행` 섹션 첫 항목부터 시작.
**작업 디렉토리**: `/Users/eugene/workspace/medsci-skills`
**다음 세션 시작 모드**: **plan 모드** — 유진이 "계획으로 시작할거야" 명시.

---

## 세션 목표 (유진 지시, 2026-04-20)

**현재 작성 중 / 제출 전 원고들의 flow diagram을 전부 R+DiagrammeR 파이프라인으로 새로 그려 저장.**
- MeducAI Paper1/Paper3도 리젝 대비 미리 새 버전 생성해서 **저장 + 기억**만 해둠 (현재 제출본은 건드리지 않음).
- 모든 새 그림은 **유진이 눈으로 확인 후** 원고에 반영. 자동 반영 금지.
- 파일은 각 프로젝트 `manuscript/figures/` 에 신규 저장, 기존은 `_legacy` 보존.

---

## 직전 세션 완료 (2026-04-20, Infrastructure + CK-5 POC)

### Infrastructure (commit + push 완료)
- `skills/make-figures/scripts/generate_flow_diagram.R` — CLI dispatcher (`--type {strobe|consort|prisma|stard} --config <yaml> --out <prefix>`). Graphviz `dot` 엔진으로 자동 레이아웃, rsvg로 진짜 벡터 PDF + 300/600 dpi PNG 동시 export. Arial + 단색 outline 강제.
- `skills/make-figures/references/exemplar_diagrams/{strobe,consort,prisma,stard}/template_input.yaml + template_output.{pdf,png,_600.png}` — 4종 양식 라운드트립 예시.
- `skills/make-figures/SKILL.md` — 4종 flow diagram 전부 R pipeline 라우팅. D2는 legacy fallback로 강등.
- `skills/make-figures/references/figure_specs.md` — Flow Diagram Tool Selection 섹션 추가 (matplotlib/D2/consort/PRISMA2020/Mermaid 기각 근거 + PRISMA 2020 compliance).
- **CK-5 Emphysema_COPD_Mortality Figure 1** 실전 retrofit 완료 (회람 대기 중 원고). `create_figure1_legacy.py` 보존, `create_figure1.R` 신규, `figure1_flow.{pdf,png,_600.png}` 재생성. **원고 재빌드는 아직 안 됨 — 유진 시각 확인 후 docx/pdf 재생성 필요.**

### 부가 (같이 묶어 푸시됨)
- meta-analysis Phase 3f + self-review Phase 2.5b — SR/MA **ID-set count reconciliation gate** (CBCT Biopsy MA-1 32/10/46 → 24/2/54 precedent). Screening TSV ∩ Consensus Sheet으로 canonical total 도출, prose-level N→M transition 금지.

### Push 완료
`3c8a986..863f189 main -> main` (4 commits: aa8b346, 78e41d7, 7692479, 863f189).

### Validator
266 PASS / 31 WARN / 0 FAIL.

---

## 즉시 실행 — plan mode로 진입해 아래 스코프 확정

### Step 0. Pre-submission 원고 전수 조사 (스코프 확정)

유진이 "현재 작성해서 제출 전의 원고들 그림 다 새로 그리자" 라고 했으므로 **submission/ 이 없는 또는 제출 전 원고를 전수 조사**. 11개 후보:

| # | 프로젝트 후보 | 경로 (재확인 필요) | Flow 타입 | 현 도구 | 상태 |
|---|---|---|---|---|---|
| 1 | CK-5 Emphysema_COPD_Mortality | `/Users/eugene/workspace/1_Samsung_Changwon/11_CheckUP_DB/05_Emphysema_COPD_Mortality/manuscript/figures/` | STROBE | **완료** (이번 세션) | 유진 눈확인 + 원고 재빌드 대기 |
| 2 | CAC_Warranty_Period | `1_Samsung_Changwon/11_CheckUP_DB/` 하위 | STROBE | D2 `figure1_flow.d2` | 제출 전 |
| 3 | SkullFx Paper2_Clinical | `{SkullFx}/Paper2_Clinical/` | STARD | **원본 스크립트 없음** | 재구성 필요 |
| 4 | CXRscoliosis | `{CXRscoliosis}/` | STARD | matplotlib `stard_flow_diagram.py` | 제출 전 |
| 5 | MA-01 RFA_Adjunct | `10_Meta_Analysis/01_RFA_Adjunct/` | PRISMA | R ggplot + D2 이중 | screening TSV+Consensus 필요 |
| 6 | MA-02 CBCT_Biopsy | `10_Meta_Analysis/02_CBCT_Biopsy/` | PRISMA-DTA | matplotlib + D2 이중 | 가장 복잡. 24/2/54 ID-verified |
| 7 | MA-03 CBCT_Ablation | `10_Meta_Analysis/03_CBCT_Ablation/` | PRISMA | matplotlib + D2 이중 | 제출 전 |
| 8 | MA-21 Aneurysm_FD | `10_Meta_Analysis/21_Aneurysm_AI_Validation_SR_Paper1_FD/` | PRISMA | 확인 필요 | 제출 전 |
| 9 | **MeducAI Paper1** | `{MeducAI}/Paper1/` | STARD | matplotlib `generate_stard_flow_npj.py` | **제출됨. 리젝 대비 병렬 버전** |
| 10 | **MeducAI Paper3** | `{MeducAI}/Paper3/` | CONSORT-edu | matplotlib `fig1_flow_diagram.py` + utils | **제출됨. 리젝 대비 병렬 버전** |
| 11 | 기타 누락분 | `/Users/eugene/workspace/**/manuscript/figures/` | ? | ? | Step 0에서 발굴 |

**Step 0 실행 방법** (다음 세션 첫 번째 작업):
```bash
find /Users/eugene/workspace -type f \( \
  -name "*prisma*flow*" -o -name "*stard*flow*" -o \
  -name "*consort*flow*" -o -name "*strobe*flow*" -o \
  -name "figure1*.py" -o -name "figure1*.R" -o -name "figure1*.d2" \
\) -not -path "*/node_modules/*" -not -path "*/.git/*" 2>/dev/null
```
각 프로젝트의 `submission/` 디렉토리 존재 여부로 제출 전/후 구분. MeducAI는 제출 완료라도 리젝 대비 포함.

### Step 1. 스코프 확정 (plan mode AskUserQuestion)

Step 0 결과를 유진에게 표로 보고하고 **retrofit 대상 확정** 받기:
- Q1: 후보 중 retrofit 대상 확정 (전부 / 선별 / 추가)
- Q2: MeducAI P1/P3 병렬 버전 저장 위치 (예: `manuscript/figures/v2_monochrome/` vs 별도)
- Q3: 순서 우선순위 (CK-5 회람 / MA 제출 준비 / MeducAI 리젝 대비 / 기타)
- Q4: 각 retrofit 후 유진 시각 확인 방식 (Preview 자동 오픈 / 배치 확인 / 프로젝트별 단건)

### Step 2. 프로젝트별 retrofit (plan 확정 후)

각 프로젝트 표준 루틴:

1. **Input 준비** (데이터 출처별 분기):
   - **Cohort (STROBE)**: `00_data_preparation.{py,R}` 에서 box 숫자 추출 → YAML
   - **Diagnostic (STARD)**: screening + index test + reference 결과 CSV → YAML
   - **MA (PRISMA)**: `2_Screening/fulltext_screening_final.tsv` ∩ `MA{N}_Consensus_Sheet.xlsx` 로 ID-set 재계산 → YAML. **prose N→M transition 금지 (meta-analysis Phase 3f)**
2. **YAML 작성** — `exemplar_diagrams/{type}/template_input.yaml` 을 참고해 프로젝트별 `figure1_counts.yaml`
3. **Render**:
   ```bash
   Rscript /Users/eugene/workspace/medsci-skills/skills/make-figures/scripts/generate_flow_diagram.R \
     --type {strobe|consort|prisma|stard} \
     --config manuscript/figures/figure1_counts.yaml \
     --out manuscript/figures/figure1_flow
   ```
4. **Legacy 보존** — 기존 `.py` / `.R` / `.d2` → `{name}_legacy.{ext}` 리네임. **삭제 절대 금지**
5. **유진 시각 확인 대기** — retrofit PNG를 Preview로 자동 오픈, 유진 승인 대기. **자동 반영 금지**
6. 승인 후에만 manuscript 재빌드 (pandoc / build_unified_docx.py)
7. 각 프로젝트 HANDOFF.md에 "flow diagram migrated to R pipeline (2026-MM-DD)" 기록

### Step 3. medsci-skills 반영

- `CHANGELOG.md` Unreleased에 retrofit 완료 프로젝트 목록 누적
- 프로젝트별 교훈은 `feedback_*.md` 메모리 추가 (예: YAML wiring pattern)
- 11개 retrofit 완료 시점에 v2.4 bump 검토

---

## MA 4편 특수 주의 (높은 위험도)

CBCT Biopsy MA-1 v11 사건 (2026-04-20) 선례: prose 숫자 "30→32 after FLAG consensus" 가 v7부터 v11까지 ID-level 재검증 없이 캐리되어 4개 다운스트림 artifact 에코. **이번 retrofit은 단순 리디자인이 아니라 ID-set 재검증 기회**.

각 MA 프로젝트 retrofit 전 MANDATORY:
1. `fulltext_screening_final.tsv` INCLUDE IDs = A
2. `MA{N}_Consensus_Sheet.xlsx` Exclude IDs = B, Include-qualitative IDs = C
3. Table 1 IDs = T
4. k_qualitative = |A\B| + |C|, k_bivariate = |T|, k_narrative-only = |(A∪C)\B\T|
5. **narrative-only IDs 명시 리스팅** (2개면 2개 ID, 10개면 10개 ID 모두)
6. Abstract/Methods/Results/Fig1 caption/Discussion 대조 — 불일치 시 P0 보고, retrofit 보류하고 수정 먼저
7. 일치 확인 후에만 YAML 작성 → render

---

## Non-goals (하지 말 것)

- **이미 제출되어 under review 상태인 원고의 현 제출본 수정** — MeducAI P1/P3는 병렬 버전만 생성, 현 제출본 불변
- **CK-5 manuscript 자동 재빌드** — 유진 시각 확인 후에만
- **flow diagram 이외의 figure (forest, ROC, KM, Bland-Altman)** — 이번 세션 스코프 아님
- **신규 스킬 추가** — medsci-skills 33개 동결 유지
- **figure style 재논의** — 이미 확정 (단색 outline + Arial + 벡터 PDF + 300/600 dpi PNG)
- **D2 / matplotlib FancyBboxPatch / PRISMA2020 R 패키지** — 전부 기각됨 (근거: `figure_specs.md` §Flow Diagram Tool Selection)
- **자동 반영** — 모든 retrofit은 유진 눈확인 후에만 원고 반영

---

## 참조 파일

- `skills/make-figures/scripts/generate_flow_diagram.R` — CLI dispatcher (이번 세션 신규)
- `skills/make-figures/references/exemplar_diagrams/{strobe,consort,prisma,stard}/template_input.yaml` — YAML 스키마 예시
- `skills/make-figures/SKILL.md` — Flow Diagram workflow 섹션
- `skills/make-figures/references/figure_specs.md` — Flow Diagram Tool Selection 섹션
- `skills/meta-analysis/SKILL.md` §3f — ID-set reconciliation gate (MA retrofit 전 필수)
- `skills/self-review/SKILL.md` §2.5b — screening-count reconciliation
- CK-5 POC 참고: `/Users/eugene/workspace/1_Samsung_Changwon/11_CheckUP_DB/05_Emphysema_COPD_Mortality/manuscript/figures/create_figure1.R`
- `HANDOFF_FLOW_DIAGRAM_OVERHAUL.md` (repo root, untracked) — 직전 overhaul 조사 보고서

---

## 사용자 확인 완료 사항 (이번 세션)

- ✅ Infrastructure 먼저 commit+push, MA는 별도 세션 (완료)
- ✅ DiagrammeR 단일 스택 (PRISMA2020 R 패키지 배제)
- ✅ CK-5를 POC로 바로 실전 retrofit (완료)
- ✅ 단색 outline + Arial + 벡터 PDF + 300/600 dpi PNG

## 확인 대기 (Step 1에서 유진 결정)

- ⏳ pre-submission 원고 전수 조사 결과 확정
- ⏳ MeducAI P1/P3 병렬 버전 저장 위치
- ⏳ retrofit 순서 우선순위
- ⏳ CK-5 Figure 1 눈확인 + manuscript 재빌드 승인
