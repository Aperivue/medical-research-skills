---
name: ma-scout
description: Meta-analysis topic discovery and feasibility assessment. Professor-first (profile → gap) or Topic-first (question → gap → co-author). Pre-protocol phase from idea to ranked topic list.
triggers: ma-scout, MA 주제 찾기, professor MA, 메타분석 주제, MA gap, topic-first MA, 트렌드 MA, meta-analysis topic, 교수님 분석, 연구 분석
tools: Read, Write, Edit, Bash, Grep, Glob
model: opus
---

# MA Scout Skill

You are helping a medical researcher discover meta-analysis topics.
Two modes are available depending on the starting point.

This skill handles the **pre-protocol phase** — from idea to ranked topic list.
For actual MA execution (PROSPERO, screening, analysis), hand off to `/meta-analysis`.

## Mode Selection

Determine the mode from user input:

| Signal | Mode |
|--------|------|
| 교수님 이름 / profile URL 제공 | **A: Professor-first** |
| 임상 질문, 키워드, 트렌드, "주제 찾아줘" | **B: Topic-first** |
| 둘 다 있으면 (e.g., "이 교수님한테 이 주제로") | **A** (topic as filter) |

If ambiguous, ask: "교수님 기반으로 찾을까요, 주제 기반으로 찾을까요?"

## Communication Rules

- Communicate with the user in Korean.
- Research questions, PICO/PIRD, and README content in English.
- Medical terminology always in English.

---

## Inputs

### Mode A: Professor-first
- Professor name (Korean + English)
- Profile URL (ScholarWorks, SKKU Faculty, Google Scholar, ORCID)
- PubMed author link (preferably with cauthor_id for disambiguation)
- Known specialty (e.g., "흉부영상", "복부영상")
- Affiliation history (e.g., "Hospital A → Hospital B → retired")
- Minimum required: **name + at least one profile URL or PubMed link**

### Mode B: Topic-first
- Clinical question or keyword (e.g., "AI로 폐결절 악성도 예측", "dual-energy CT body composition")
- Radiology subspecialty scope (e.g., "흉부", "복부", "신경")
- MA type preference (DTA, prognostic, intervention — optional)
- Desired role: 1저자 단독 / co-first / 교수님 매칭 희망
- Minimum required: **clinical question or keyword**

---

## Workflow

> **Mode A (Professor-first):** Phase 0 → 1 → 2 → 3 → 4 → 5
> **Mode B (Topic-first):** T-Phase 0 → T-1 → T-2 → T-3 → T-4 → T-5
> Phase 2 (MA Gap Analysis) and Phase 4 (README template) are shared between both modes.

---

# ═══════════════════════════════════════════
# MODE A: PROFESSOR-FIRST WORKFLOW
# ═══════════════════════════════════════════

### Phase 0: Disambiguation & Context Confirmation

**Goal:** Resolve author identity before any search, and confirm user's relationship context.

**CRITICAL — Do this BEFORE any PubMed search:**

1. **Resolve full English name first:**
   - If cauthor_id is provided → fetch that specific PMID page to get full name + affiliation
   - NEVER start with initials-only search (e.g., "Ha HK") — common Korean initials cause massive contamination
   - First search must be `"[Full Name]"[Author]` (e.g., `"Ha Hyun Kwon"[Author]`)

2. **Confirm affiliation chain with user:**
   - Ask: "교수님 소속 이력이 {확인된 소속}이 맞나요? 관계도 알려주시면 주제 제안에 반영하겠습니다."
   - This prevents wrong-institution assumptions
   - Skip only if user already provided explicit affiliation history

3. **Profile URL fallback chain** (Scopus requires auth, so plan alternatives):
   - 1st: PubMed full name search (always works)
   - 2nd: Google Scholar profile (WebSearch `"[Full Name]" radiology scholar`)
   - 3rd: ResearchGate profile (WebSearch `"[Full Name]" researchgate radiology`)
   - 4th: ScholarWorks / SKKU / university faculty page (if URL provided)
   - Last: Scopus/ScienceDirect (often fails due to auth — do NOT rely on it)

---

### Phase 1: Profile Exploration (E-utilities API)

**Goal:** Identify the professor's 5-6 distinct research pillars using PubMed E-utilities API.

**CRITICAL — Use E-utilities API, NOT WebFetch for PubMed:**
- Scripts: `~/.claude/skills/search-lit/references/pubmed_eutils.sh` + `parse_pubmed.py`
- Rate limit: 350ms between calls (100ms with NCBI_API_KEY)
- These are faster, more reliable, and return structured data (JSON/XML)

**Step 1 — Total publication count + PMID list:**
```bash
bash ~/.claude/skills/search-lit/references/pubmed_eutils.sh search \
  '"[Full Name]"[Author]' 200 \
  | python3 ~/.claude/skills/search-lit/references/parse_pubmed.py esearch
```

**Step 2 — Fetch metadata for MeSH-based clustering (parallel):**
```bash
# Get PMIDs from Step 1, then fetch summaries
bash ~/.claude/skills/search-lit/references/pubmed_eutils.sh fetch_json \
  "PMID1,PMID2,..." \
  | python3 ~/.claude/skills/search-lit/references/parse_pubmed.py esummary
```

**Step 3 — Topic-specific counts (launch 4-5 searches in parallel via Bash):**
```bash
# Run these in parallel Bash calls
bash ~/.claude/skills/search-lit/references/pubmed_eutils.sh search \
  '"[Full Name]"[Author] AND "keyword1"' 5
bash ~/.claude/skills/search-lit/references/pubmed_eutils.sh search \
  '"[Full Name]"[Author] AND "keyword2"' 5
# ... repeat for each suspected pillar keyword
```

**Step 4 — MeSH term extraction for automatic pillar clustering:**
```bash
# Fetch full XML for top-cited papers to extract MeSH headings
bash ~/.claude/skills/search-lit/references/pubmed_eutils.sh fetch \
  "PMID1,PMID2,...,PMID20" \
  | python3 -c "
import sys, xml.etree.ElementTree as ET
from collections import Counter
root = ET.fromstring(sys.stdin.read())
mesh_counts = Counter()
for article in root.findall('.//PubmedArticle'):
    for mh in article.findall('.//MeshHeading/DescriptorName'):
        mesh_counts[mh.text] += 1
for term, count in mesh_counts.most_common(30):
    print(f'{count:3d}  {term}')
"
```
→ Top MeSH terms reveal natural research pillars (e.g., "Colonography, Computed Tomographic" = CTC pillar).

**Step 5 — Google Scholar profile (parallel with PubMed calls):**
- WebSearch: `"[Full Name]" radiology scholar google` for h-index, citation data

**Output: Pillar Summary Table**

| Pillar | 영역 | 대표 키워드 | MeSH terms | 추정 논문 수 |
|--------|------|------------|-----------|-------------|
| 1 | ... | ... | ... | ~N+ |

---

### Phase 2: MA Gap Analysis (Multi-Source)

**Goal:** For each pillar, determine if a viable MA topic exists using PubMed + Consensus + Scholar Gateway + bioRxiv.

For each pillar (run in parallel using meta-analyst agents):

#### 2a. PubMed E-utilities — Existing MAs + Primary studies

```bash
# Existing MAs (structured count)
bash ~/.claude/skills/search-lit/references/pubmed_eutils.sh search \
  '[pillar keywords] AND ("meta-analysis"[pt] OR "systematic review"[pt])' 50

# Primary studies with extractable outcomes
bash ~/.claude/skills/search-lit/references/pubmed_eutils.sh search \
  '[pillar keywords] AND ("sensitivity" OR "specificity" OR "accuracy" OR "prognosis" OR "outcome")' 50
```

#### 2b. Consensus MCP — Semantic MA gap detection

Use `mcp__claude_ai_Consensus__search` to find existing SRs/MAs that PubMed keyword search might miss:
```
query: "systematic review OR meta-analysis [pillar topic] [imaging modality]"
```
Consensus returns citation-ranked results — check if any highly-cited MA already covers the proposed scope.
**Limit:** max 3 Consensus calls per Phase 2 batch (rate limit).

#### 2c. Scholar Gateway — Semantic similarity search

Use `mcp__claude_ai_Scholar_Gateway__semanticSearch` for:
- Finding MAs with different terminology (e.g., "pooled analysis" instead of "meta-analysis")
- Detecting scope-overlapping MAs that use different keywords
- Identifying methodological review papers that partially cover the topic

#### 2d. bioRxiv/medRxiv — In-press competition detection

Use `mcp__claude_ai_bioRxiv__search_preprints` to catch:
- MAs posted as preprints but not yet indexed in PubMed
- Ongoing SR/MA protocols shared as preprints
- Very recent primary studies that could change feasibility

```
query: "[pillar keywords] meta-analysis OR systematic review"
server: "medrxiv"  (for clinical topics)
```

#### 2e. Assessment matrix

| Factor | Criteria |
|--------|----------|
| MA gap | 0 existing = best, 1-3 = check scope overlap, >5 = saturated |
| Primary k | ≥8 for DTA, ≥6 for prognostic (minimum), ≥15 ideal |
| Recency | Last MA >5 years old = update opportunity |
| Competition | Check 2024-2026 for very recent MAs that block entry |

#### 2f. PROSPERO competition check (MANDATORY)

- Search PROSPERO via WebSearch: `site:crd.york.ac.uk/prospero [topic keywords]`
- Also try WebFetch: `https://www.crd.york.ac.uk/prospero/#searchadvanced`
- Look for registered-but-unpublished protocols that could block entry
- If PROSPERO match found → flag as 🚫 competition risk in ranking

#### 2g. Realistic k estimation

- Raw PubMed hit count is NOT the real k — most studies lack 2x2 data or HR
- Apply conservative discount: **k_realistic ≈ raw_count × 0.15–0.30** for DTA topics
- Flag if k_realistic < 8 (DTA) or < 6 (prognostic) as ⚠️ feasibility risk
- Report both: `추정 k: ~130편 (raw) → ~20-40편 (DTA 추출 가능 추정)`

#### 2h. Niche subtopic discovery (if pillar appears saturated)

- AI/radiomics angle on a classical topic
- Specific modality comparison (e.g., CEUS vs MRI)
- Treatment response (vs diagnosis which is often saturated)
- Specific subpopulation or disease subtype
- Use Consensus to check if the niche angle has already been covered

---

### Phase 3: Topic Ranking

**Goal:** Rank all viable topics by composite score.

Score each candidate on 5 criteria (★1-5):

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Professor fit** | 최고 | 교수님 커리어 핵심 영역인가, 논문 수, 독보적 기여 |
| **MA gap** | 높음 | 기존 MA 없음 > 5년 이상 경과 > 최근 MA 존재 |
| **Feasibility (k)** | 높음 | 포함 가능 연구 수, 2x2 또는 HR 추출 가능성 |
| **Clinical impact** | 중간 | 임상 의사결정에 직결되는 주제인가 |
| **Execution ease** | 중간 | 문헌 기반만으로 완료 가능, heterogeneity 관리 난이도 |

**Output: Ranked Topic Table**

| 순위 | 주제 | 교수님 Pillar | 기존 MA | 추정 k (raw→realistic) | PROSPERO 경쟁 | 종합 판정 |
|------|------|-------------|---------|----------------------|--------------|----------|
| 1 | ... | ... | 0편 | ~98→15-30 | 없음 | ✅ 최적 |

---

### Phase 4: Folder & README Scaffolding

**Goal:** Create project folders and README for each viable topic.

1. **Folder location:** `{working_dir}/ma-scout/{initials}_{professor_name}/`
2. **Naming convention:** `{NN}_{주제약칭}/` (within professor folder)
   - Professor folder: `{initials}_{name}` (e.g., `KDK_Kim`, `LKS_Lee`)
   - NN: sequential number within professor (01, 02, ...)
   - 주제약칭: English, underscore-separated
   - Check existing folders with `ls` before creating

3. **README.md template (PROSPERO-ready):**

   ```markdown
   # {Topic Title} — {MA Type} Meta-analysis ({교수님 성함})

   ## Overview
   - Supervisor: {교수님 성함} ({소속 이력})
   - 교수님 영역: Pillar {N} — {영역명}
   - Status: 기획 단계
   - Priority: {순위}순위
   - Created: {YYYY-MM-DD}

   ## Research Question
   ### PICO/PIRD
   - **P**opulation: {구체적 환자군, 질환, 세팅}
   - **I**ndex test / Intervention: {검사법 또는 중재}
   - **C**omparator / Reference standard: {비교군 또는 참조표준}
   - **O**utcome: {DTA: Se/Sp/AUC, Prognostic: HR/OR, 부작용 등}

   ### One-line RQ
   {완성형 연구 질문 1문장}

   ## Key Gap
   - 기존 MA: {N}편 ({상세, 가장 최근 연도, 범위 한계})
   - Consensus/Scholar Gateway 추가 확인: {결과 요약}
   - medRxiv/bioRxiv preprint MA: {있음/없음}
   - PROSPERO 등록 프로토콜: {있음 (CRD#) / 없음}
   - {구체적 gap 설명 — 왜 새 MA가 필요한지}

   ## Professor's Authority
   - {분야 관련 논문 수, 대표 논문 1-2편, 독보적 기여}
   - {왜 이 교수님이 이 주제에 적합한지}

   ## Preliminary Search ({날짜})
   ### Search Strategy (PubMed)
   ```
   {실제 사용한 PubMed 검색식 — E-utilities esearch query 그대로}
   ```
   - Total hits: {N}편 (raw)
   - DTA/outcome extractable (estimated): {N}편 (×0.15-0.30 discount)
   - 기존 MA: {N}편 (narrow) / {N}편 (broad SR 포함)
   - Consensus 검색 결과: {N}편 추가 발견 여부
   - bioRxiv/medRxiv: {N}편 preprint

   ### Embase Search Strategy (Draft)
   ```
   {Embase용 검색식 초안 — Emtree 용어 포함}
   ```
   (실행 전 초안 — Embase 접속 시 검증 필요)

   ## Target Journal
   | 순위 | 저널명 | IF | MA 게재 비율 | Turnaround | 비고 |
   |------|--------|-----|-------------|-----------|------|
   | 1차 | {저널} | {IF} | {높음/중간} | {개월} | {근거} |
   | 2차 | {저널} | {IF} | {높음/중간} | {개월} | {근거} |

   ## Timeline (역산)
   | 단계 | 예상 시점 | 선행 조건 |
   |------|----------|----------|
   | 교수님 제안 | {YYYY-MM} | {조건} |
   | PROSPERO 등록 | +1주 | 교수님 승인 |
   | 검색 완료 | +2주 | PROSPERO 등록 |
   | 스크리닝 완료 | +3주 | 2nd reviewer 확보 |
   | 데이터 추출 | +4주 | 스크리닝 합의 |
   | 분석 + 초안 | +6주 | 데이터 lock |
   | 교수님 리뷰 | +8주 | 초안 완성 |
   | 투고 | +10주 | 교수님 승인 |

   ## Data Sources Used
   - PubMed E-utilities: ✅ (esearch count + efetch metadata)
   - Consensus MCP: ✅/❌
   - Scholar Gateway: ✅/❌
   - bioRxiv/medRxiv: ✅/❌
   - PROSPERO: ✅
   ```

---

### Phase 5: Output Summary

**Goal:** Persist findings for the user.

1. Save the ranked topic table and README files to the working directory.
2. Summarize: total topics scanned, viable topics found, recommended next steps.
3. Suggest the user save results to their project management system (e.g., `/manage-project`).

---

## Niche Topic Discovery Heuristics

When all major pillars are saturated (MA >5편), try these angles:

1. **"첫 번째 MA" rule:** Professor's most unique/niche subtopic where MA = 0
2. **AI/radiomics overlay:** Classical imaging topic + AI approach = new MA angle
3. **Treatment response:** Diagnosis MAs saturated → treatment monitoring MA often open
4. **Modality comparison:** Head-to-head (e.g., CEUS vs MRI) often underserved
5. **Guideline gap:** Professor authored guidelines → MA supporting/updating those guidelines
6. **Geographic/population niche:** Korean/Asian population-specific MA (e.g., parasitic diseases, TB)
7. **Temporal update:** Last MA >5 years old + significant new primary studies since

---

## Quality Gates

Before finalizing a topic as viable:

- [ ] **Author identity confirmed** — full name resolved via E-utilities efetch, no initials-only contamination
- [ ] **Affiliation confirmed** with user (or from reliable source)
- [ ] Confirmed MA = 0 or last MA >5 years (via PubMed E-utilities, not assumption)
- [ ] **Cross-validated via Consensus/Scholar Gateway** — no hidden MAs with different terminology
- [ ] **bioRxiv/medRxiv checked** — no preprint MA in progress
- [ ] Confirmed k_realistic ≥ 8 (DTA) or ≥ 6 (prognostic) after discount
- [ ] **PROSPERO searched** — no registered competing protocol found
- [ ] No 2024-2026 competing MA in press (check PubMed + preprints)
- [ ] Professor's publication record demonstrates clear authority in this area
- [ ] Research question is specific enough for PROSPERO registration
- [ ] **README contains:** complete PICO/PIRD, PubMed search strategy, Embase draft, target journal with IF, timeline

---

## Handoff

After MA Scout completes:
- To **`/meta-analysis`**: When a topic is approved and ready for PROSPERO protocol (README has PICO + search strategy ready)
- To **`manage-project`**: When project folder needs full scaffolding
- To **`search-lit`**: When deeper preliminary search is needed before committing
- To **`/analyze-stats`**: When feasibility requires power/sample-size calculation for the estimated k

---

## Parallel Execution Strategy

For efficiency, launch multiple agents and API calls in parallel:

**Phase 0 (Identity):**
1. E-utilities esearch: `"[Full Name]"[Author]` → total count + PMIDs (FIRST)
2. E-utilities efetch: top 20 PMIDs → MeSH terms → automatic pillar clustering

**Phase 1 (Profile — all parallel):**
3. Bash × 4-5: E-utilities esearch with topic-specific filters (parallel Bash calls)
4. WebSearch: Google Scholar profile
5. WebFetch: any provided profile URLs (skip Scopus)

**Phase 2 (MA Gap — multi-source parallel):**
6. Up to 4 meta-analyst agents in parallel, each covering 1-2 pillars
7. Each agent runs ALL of:
   - E-utilities esearch: existing MA count + primary study count
   - Consensus MCP: semantic MA search (max 3 calls total across all agents)
   - Scholar Gateway: scope-overlap check
   - bioRxiv/medRxiv: preprint MA detection
   - PROSPERO: competition check (WebSearch)
8. Each agent reports: raw k, realistic k (15-30% discount), all sources checked

**Phase 3 (Ranking):** Sequential, uses Phase 2 outputs.

**Phase 4 (Scaffolding):** Sequential, creates folders + PROSPERO-ready READMEs.

Total (Mode A): 5-8 parallel agents per professor, ~8-12 minutes per professor.

### Mode B Parallel Strategy

**T-Phase 0:** Sequential (user interaction for scope clarification).

**T-Phase 1 (Landscape — all angles in parallel):**
1. Per angle: Bash (PubMed MA count) + Bash (primary k) + Consensus + bioRxiv + PROSPERO
2. 3-5 angles × 5 sources = 15-25 parallel calls

**T-Phase 2 (Deep-dive):** Same as Mode A Phase 2, only for viable angles (typically 1-2).

**T-Phase 4 (Co-author — if needed):**
3. Bash: PubMed author frequency search
4. WebSearch: Google Scholar profiles for top candidates

Total (Mode B): ~5-8 minutes per topic scan (faster than Mode A — no profile exploration).

### Known Pitfalls (from 3 professor analyses)
- Common Korean/Asian initials (e.g., "Lee KS", "Kim DK") return 300+ papers with massive contamination. Always use full name first.
- Scopus/ScienceDirect → 403 or redirect to login. Never rely on Scopus as primary data source.
- Raw PubMed counts overestimate by 3-7x. ~130 hits often means 20-40 with extractable DTA data.
- Professor may have moved institutions. Don't assume affiliation without verification.
- **Consensus rate limit:** Max 3 batch calls. If rate-limited, wait 30s and retry once.
- **E-utilities rate limit:** 350ms between calls (100ms with NCBI_API_KEY). Scripts handle this automatically.
- **bioRxiv MCP:** Use `server: "medrxiv"` for clinical topics, `server: "biorxiv"` for preclinical.

---

# ═══════════════════════════════════════════
# MODE B: TOPIC-FIRST WORKFLOW
# ═══════════════════════════════════════════

### T-Phase 0: Topic Clarification & Scope

**Goal:** Refine the user's clinical question into a searchable, PROSPERO-registrable scope.

1. **Parse the input** — extract:
   - Disease/condition (e.g., "lung nodule", "hepatocellular carcinoma")
   - Imaging modality or intervention (e.g., "dual-energy CT", "AI CAD")
   - Outcome type: DTA (Se/Sp), prognostic (HR/OR), intervention (RR/MD), dosimetry
   - Population specifics (e.g., "screening setting", "cirrhotic patients")

2. **Expand to neighboring angles** — propose 3-5 variations:
   ```
   사용자 입력: "AI로 폐결절 악성도 예측"
   → 변형 1: AI vs radiologist for lung nodule malignancy prediction (DTA)
   → 변형 2: Radiomics for lung nodule malignancy (DTA)
   → 변형 3: Deep learning for incidental pulmonary nodule management (prognostic)
   → 변형 4: AI-assisted Lung-RADS upgrade accuracy (DTA)
   → 변형 5: Low-dose CT AI for lung cancer screening (DTA)
   ```

3. **User selects 1-3 angles** to investigate further.

---

### T-Phase 1: Landscape Scan (Multi-Source)

**Goal:** For each selected angle, rapidly assess the MA landscape.

**Run all angles in parallel. For each angle:**

#### 1a. PubMed — Existing MA count
```bash
bash ~/.claude/skills/search-lit/references/pubmed_eutils.sh search \
  '[topic keywords] AND ("meta-analysis"[pt] OR "systematic review"[pt])' 50
```

#### 1b. PubMed — Primary study pool
```bash
bash ~/.claude/skills/search-lit/references/pubmed_eutils.sh search \
  '[topic keywords] AND ("sensitivity" OR "specificity" OR "hazard" OR "outcome")' 100
```

#### 1c. Consensus MCP — Semantic MA discovery
```
query: "systematic review [topic] [modality]"
```
Check for MAs using different terminology.

#### 1d. bioRxiv/medRxiv — Preprint competition
```
query: "[topic] meta-analysis"
server: "medrxiv"
```

#### 1e. PROSPERO — Registered protocols
WebSearch: `site:crd.york.ac.uk/prospero [topic keywords]`

**Output: Landscape Summary Table**

| 변형 | 기존 MA | Primary k (raw) | k (realistic) | PROSPERO | Preprint MA | 판정 |
|------|---------|----------------|--------------|----------|------------|------|
| 1 | 3편 | 120 | 18-36 | 1건 | 0 | ⚠️ 경쟁 |
| 2 | 0편 | 85 | 13-25 | 0 | 0 | ✅ 최적 |

---

### T-Phase 2: Feasibility Deep-Dive

**Goal:** For viable angles (MA ≤ 2, no PROSPERO conflict), run full gap analysis.

This phase uses the **same Phase 2 (MA Gap Analysis)** as Mode A — steps 2a through 2h.
The only difference: no "Professor fit" to evaluate, so focus on:
- **Gap certainty** — are existing MAs truly non-overlapping with proposed scope?
- **k quality** — are primary studies heterogeneous enough to warrant MA, or too uniform?
- **User's domain fit** — does this align with user's radiology AI / imaging expertise?

---

### T-Phase 3: Topic Ranking (Topic-first weights)

**Goal:** Rank viable topics with weights adjusted for topic-first approach.

| Criteria | Weight | Description |
|----------|--------|-------------|
| **MA gap** | 최고 | 기존 MA 없음 > update 기회 > 포화 |
| **Feasibility (k)** | 최고 | k_realistic ≥ 8 (DTA) or ≥ 6 (prognostic) |
| **User domain fit** | 높음 | 사용자의 전문 분야와 맞는가 |
| **Clinical impact** | 중간 | 가이드라인 변경 가능성, 임상 의사결정 직결 |
| **Co-author availability** | 중간 | 해당 분야 전문가 접근 가능성 (기존 관계 or 접근 용이) |
| **Execution ease** | 중간 | 단독 진행 가능 vs 전문가 해석 필수 |

**Output: Ranked Topic Table**

| 순위 | 주제 | 기존 MA | 추정 k | PROSPERO | Co-author 필요 | 종합 |
|------|------|---------|--------|----------|--------------|------|
| 1 | ... | 0편 | 25 | 없음 | 선택적 | ✅ 최적 |

---

### T-Phase 4: Co-Author Matching (Optional)

**Goal:** If the user wants a senior co-author, find candidates.

**Strategy 1 — Existing network (memory-based):**
- Check memory files for professors with overlapping expertise
- Cross-reference existing professor folders in the working directory
- Best match = professor whose pillar naturally covers this topic

**Strategy 2 — PubMed reverse search:**
```bash
# Find prolific authors in this specific topic
bash ~/.claude/skills/search-lit/references/pubmed_eutils.sh search \
  '[topic keywords] AND ("{user_country}"[Affiliation])' 100
```
Then:
- E-utilities efetch → extract author frequency from results
- Top 5 most-published authors in this niche = potential co-authors
- Cross-check Google Scholar for h-index and recent activity

**Strategy 3 — Self-led (no senior co-author):**
- Viable when: user has 2+ published MAs, topic is methodologically straightforward
- Still need 2nd reviewer (junior colleague or peer) — flag this in README
- Corresponding author = user

**Output:** Co-author recommendation table or "단독 진행 가능" judgment.

---

### T-Phase 5: Folder & README Scaffolding (Topic-first)

**Goal:** Create project folder and PROSPERO-ready README.

1. **Folder location:** `{working_dir}/ma-scout/TOPIC/`
   - Topic-first projects use `TOPIC/` prefix (not professor initials)
   - Naming: `{NN}_{Topic_Abbreviation}/` (e.g., `01_AI_Lung_Nodule_DTA/`)
   - If co-author matched later, can be moved under professor folder

2. **README.md template:** Same PROSPERO-ready template as Mode A Phase 4, with these changes:
   - `Supervisor:` → `Lead: {user_name}` or `Lead: {user_name} + {co-author}`
   - `교수님 영역:` → `Domain: {subspecialty}`
   - `Professor's Authority` → `Team Expertise` (user's credentials + co-author if any)
   - Timeline: no "교수님 제안" step → starts directly at "PROSPERO 등록"

   **Timeline template (self-led):**
   | 단계 | 예상 시점 | 선행 조건 |
   |------|----------|----------|
   | PROSPERO 등록 | {YYYY-MM} | 주제 확정 |
   | 검색 완료 | +1주 | PROSPERO 등록 |
   | 스크리닝 완료 | +2주 | 2nd reviewer 확보 |
   | 데이터 추출 | +3주 | 스크리닝 합의 |
   | 분석 + 초안 | +5주 | 데이터 lock |
   | Co-author 리뷰 | +7주 | 초안 완성 |
   | 투고 | +8주 | 최종 승인 |

3. **Summary:** Same as Mode A Phase 5 — save ranked results and recommend next steps.

---

### Topic Discovery Heuristics (Mode B specific)

When the user says "주제 찾아줘" without a specific idea:

1. **Trend scan** — Search recent high-IF radiology journals for "gap in the literature" + "meta-analysis needed":
   ```bash
   bash ~/.claude/skills/search-lit/references/pubmed_eutils.sh search \
     '"no meta-analysis" AND "radiology"[Journal] AND 2024:2026[dp]' 30
   ```

2. **Guideline update gaps** — New guidelines (ACR, ESR, RSNA) often cite lack of MA evidence:
   - Consensus search: `"practice guideline" AND "insufficient evidence" AND [radiology subspecialty]`

3. **AI + classical imaging** — Overlay AI/DL/radiomics on well-studied classical topics:
   - Many classical DTA topics have 10+ MAs, but AI angle has 0-1

4. **Korean/Asian population** — Population-specific MA for diseases with geographic variation:
   - TB, NTM, parasitic diseases, gastric cancer, liver fluke, HBV-related HCC

5. **Technology adoption** — New modalities with growing evidence but no synthesis:
   - Photon-counting CT, abbreviated MRI, contrast-enhanced mammography, AI CAD

6. **Cross-subspecialty** — Topics spanning two subspecialties often fall through MA cracks:
   - Cardiac + thoracic (coronary CT + lung screening), neuro + MSK (spine imaging)

---

### Quality Gates (Mode B specific)

Before finalizing a topic-first MA as viable:

- [ ] Clinical question refined to PICO/PIRD (not just a keyword)
- [ ] MA gap confirmed via PubMed + Consensus + Scholar Gateway + bioRxiv (all 4 sources)
- [ ] k_realistic ≥ 8 (DTA) or ≥ 6 (prognostic) after 15-30% discount
- [ ] PROSPERO searched — no competing registered protocol
- [ ] No 2024-2026 competing MA in press or preprint
- [ ] User's domain expertise sufficient for clinical interpretation (or co-author identified)
- [ ] 2nd reviewer identified or plan to recruit
- [ ] README contains: complete PICO/PIRD, PubMed + Embase search strategy, target journal with IF, timeline
- [ ] If self-led: user has ≥ 2 published MAs (otherwise, recommend co-author)

---

## Phase 6: Pre-Proposal Pipeline (Post-Scout)

After MA Scout identifies viable topics, run the **pre-proposal pipeline** to prepare
a "ready-to-propose" package before contacting the professor.

### Pipeline Steps

1. **Search Execution** — E-utilities with broadened synonyms (retmax=200)
   - Primary search: `[topic] AND [outcome keywords]`
   - Existing MA search: `[topic] AND ("meta-analysis"[pt] OR "systematic review"[pt])`

2. **Metadata Collection** — `fetch_json` → `esummary` (batch 40-50 PMIDs)

3. **Title-Based Triage** — Classify as INCLUDE / MAYBE / EXCLUDE
   - CRITICAL: Check for existing MAs within results (initial scout may miss them)
   - Separate bronchoscopic vs percutaneous (30% contamination in CBCT topics)
   - Flag professor's own papers (authority evidence)
   - Flag retracted papers

4. **PRISMA Flow Draft** — Identification → Screening → Eligibility → Included (estimated)

5. **Gap Re-assessment** — Update MA count, re-position if needed:
   - MA=0 → "first MA" | MA=1 (>5yr) → "update MA" | MA≥3 (recent) → skip/niche

6. **Output Files**:
   - `candidates.md` — full triage table + PRISMA flow + gap finding
   - `README.md` — updated Preliminary Search section with actual numbers

### Parallel Execution
- Launch up to 4 agents per wave (each topic independent)
- Each agent: search → fetch → triage → write files → ~5-10 min
- 21 topics completed in ~1 hour with 16 parallel agents

### Professor Contact Package
The pre-proposal gives the professor:
- Candidate count + gap evidence ("MA=0, 35편 include")
- Clear role description ("스크리닝 독립 검토 + discussion만")
- PROSPERO 선점 urgency

## Anti-Hallucination

- **Never fabricate publication counts, h-index, or pillar classifications.** All numbers must come from PubMed E-utilities API output.
- **Never fabricate existing MA counts.** Always verify via PubMed search + PROSPERO check before claiming "MA = 0".
- **Never invent professor expertise or affiliation.** Confirm with user before proceeding.
- **k_realistic must use the 15-30% discount.** Raw PubMed counts overestimate by 3-7x. Always report both raw and realistic estimates.
- If PubMed returns 0 or Consensus/Scholar Gateway is unavailable, state the limitation rather than guessing.
