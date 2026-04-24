# Data Integrity Checklist

**Applies to**: Phase 3 (Extraction) ~ Phase 6 (Statistical synthesis) ~ Phase 9 (Circulation) 전 구간. MA 고유 수치 정합성 리스크 차단.

## 1. Extraction 단계

### DI-1. Extraction consensus log 정식화
- **Problem pattern**: Comparative extraction results kept only as inline comments inside the R analysis script — no standalone consensus log → arm-specific numbers become irretraceable once the script is edited.
- **Rule**: 모든 MA 프로젝트 초기 단계에서 `2_Data/extraction_consensus_log.md` 또는 `3_Extraction/extraction_consensus_log.md` 생성. 컬럼: study_id, arm, numerator, denominator, source_page, source_type (text/table/figure/KM-reconstruction), extractor_initials, second_reviewer_initials, timestamp, notes. 비교분석 추출은 스크립트 주석이 아닌 정식 행으로만.

### DI-2. 2x2 cell count 이중검수 필수
- **Problem pattern**: Hand-typed 2x2 cells with arm order swapped against the source paper, or with numerator/denominator misread from a KM-derived subgroup rather than the raw table. Both fail silently until a third reviewer back-calculates the proportion.
- **Rule**: 모든 2x2 / comparative 추출은 (a) 1차 추출 + (b) 독립 2차 재추출 + (c) mismatch 시 원문 재확인 + consensus log 행 생성. Phase 6b "numerical safety gate" 수행.

### DI-3. KM 재구성 감사 추적 완결
- **Problem pattern**: Subgroup cell counts reconstructed from a published KM curve without preserving the WebPlotDigitizer trace or the IPDfromKM reconstruction log → numbers cannot be re-derived if a reviewer challenges them.
- **Rule**: KM 재구성 산출물은 반드시 (a) WebPlotDigitizer JSON, (b) IPDfromKM CSV, (c) 도구 버전 + 좌표값 + 파라미터 + 날짜 메타데이터를 `3_Extraction/km_reconstruction/{study_id}/`에 세트로 보관. Consensus log에 "km-reconstruction" type으로 링크.

### DI-4. Denominator 변경 = 원문 페이지 인용 + consensus log 행
- **Problem pattern**: Denominator correction (e.g., treatment-naive subset) entered only as an R-script comment without citing the source paper's page/table → the correction's rationale is lost at revision.
- **Rule**: 모든 denominator 수정은 (a) 원문 page / table 인용, (b) 변경 근거 문장, (c) consensus log 한 행. 3개 중 하나라도 없으면 수정 거부.

### DI-5. Methodology mismatch random spot-check
- **Problem pattern**: A source paper reports per-protocol analysis while the SR framework is ITT/ITD (or vice versa). Without a methodology spot-check, the study's effect estimate is silently re-used under a different analysis framework.
- **Rule**: Extraction spot-check scope에 "methodology flag" 포함 — 각 study의 원논문 분석 unit (per-protocol / ITT / ITD)이 우리 SR framework과 일치하는지. 불일치 시 재추출.

## 2. 3~5-way consistency

### DI-6. PRISMA flow 5-way consistency
- **Problem pattern**: PRISMA flow numbers drift across the search CSV, the screening log, the Methods prose, the Results prose, and the Figure 1 caption — five surfaces reach submission in three mutually inconsistent states (reversed database order, divergent full-text-assessed counts, stale caption numbers).
- **Rule**: PRISMA flow 숫자는 5곳 동시 일치 검증:
  1. `1_Search/*.csv` 원본 (source of truth, 수정 금지)
  2. `2_Screening/prisma_flow_final.md`
  3. Manuscript Methods prose
  4. Manuscript Results prose (중복 언급 시)
  5. Figure 1 caption (`5_Figures/_captions.md` + DOCX 단문 caption 둘 다)
- **ID-Set Gate Rule 5**: prose 먼저 고정 → 그 후 diagram 렌더링. Diagram 먼저 만들면 prose 수정 시 drift.
- **검증 자동화 후보**: `k`, `n`, search numbers를 YAML로 single source에서 관리하고 prose/diagram template에 substitute.

### DI-7. k값 single source = `4_Analysis/*.csv`
- **Problem pattern**: Included-study count `k` quoted as two different values across consecutive manuscript versions because it was hand-typed into prose rather than derived from the analysis CSV.
- **Rule**: k는 `4_Analysis/*.csv` row count에서만 역산. Manuscript / MANIFEST / PROSPERO 업데이트에 k 기입 시 CSV path + row count 함께 명시.

## 3. Submission 전 cleanup

### DI-8. Tag / TODO 전수 제거
- **Problem pattern**: `TODO`, `[VERIFY-CSV]`, "to be regenerated" strings survive into the submission package — found in R scripts, figure captions, and supplementary material banners.
- **Rule**: Submission day 전 다음 grep 0 hits:
  ```bash
  rg -n "VERIFY-CSV|TODO|FIXME|XXX|to be regenerated|PH TODO|to-do" \
     7_Manuscript/ supplement/ 5_Figures/ 6_Tables/ 1_Code/
  ```
- **`[VERIFY-CSV]` lifecycle**: attach (v6) → verify (v7) → mark (v8+) → remove (submission). 각 stage를 MANIFEST에 기록.

### DI-9. Bias-driven homogeneity 해석 명시
- **Problem pattern**: In a DTA pool where every included study is retrospective with differential verification, Sp I²=0% reflects universalized bias compression rather than true between-study homogeneity — easy to over-interpret as robust agreement.
- **Rule**: I²=0% + QUADAS-2 Domain 4 risk 모두 high/unclear → "universalized bias compression" 명시, "upper-bound estimate" framing. Discussion에 bias context 필수.
