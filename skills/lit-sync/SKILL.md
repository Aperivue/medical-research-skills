---
name: lit-sync
description: Sync research references from .bib files to Zotero library + Obsidian literature notes. Extract cross-cutting concept notes when enough literature accumulates. Works after /search-lit or standalone.
triggers: lit-sync, 문헌 동기화, 레퍼런스 정리, 개념 노트 추출, lit sync, Zotero 동기화, reference sync, 참고문헌 옵시디언
tools: Read, Write, Edit, Bash, Grep, Glob
model: inherit
---

# Literature Sync: Zotero + Obsidian Pipeline

`/search-lit`의 출력(.bib)을 받아 Zotero 라이브러리와 Obsidian 문헌 노트에 자동 동기화하고, 충분한 문헌 노트가 쌓이면 교차 개념 노트를 추출한다.

## When to Use

- `/search-lit` 완료 후 → "문헌 동기화해줘"
- 기존 .bib 파일의 레퍼런스를 Zotero + Obsidian에 일괄 등록
- 프로젝트 workspace의 references/ 폴더 정리
- "개념 노트 뽑아줘" → 문헌 노트 기반 교차 개념 추출

## Prerequisites

- Zotero MCP server 활성화 (없으면 Zotero 단계 skip)
- Obsidian CLI or direct file writing to the Obsidian vault
- Obsidian vault path: configured in user's environment (e.g., `$OBSIDIAN_VAULT`)

## Pipeline Overview

```
.bib 파일 (또는 /search-lit 출력)
    │
    ▼ Phase 1: Parse
    DOI, PMID, title, authors, journal, year 추출
    │
    ▼ Phase 2: Zotero Sync
    중복 체크 → zotero_add_by_doi → 컬렉션 배치
    │
    ▼ Phase 3: Obsidian Literature Notes
    02 연구/문헌/{citekey}.md 생성 (빈 노트 OK — 나중에 하이라이트 추가)
    │
    ▼ Phase 4: Concept Extraction (조건부)
    문헌 노트 10개 이상 → 교차 개념 스캔 → 개념 노트 제안
```

---

## Phase 1: Parse BibTeX

### Input

사용자가 지정한 .bib 파일 경로, 또는 방금 `/search-lit`이 생성한 .bib.

### Process

```python
# .bib 파일에서 엔트리 파싱 (정규식 기반)
# 각 엔트리에서 추출:
#   - citekey (e.g., Kim_2024_Validation)
#   - doi
#   - pmid
#   - title
#   - authors (first + last minimum)
#   - journal
#   - year
#   - volume, number, pages (있으면)
```

파싱 실패한 엔트리는 로그에 남기고 skip.

---

## Phase 2: Zotero Sync

### Step 2.1: 프로젝트 컬렉션 결정

현재 작업 디렉토리 또는 사용자 지정으로 프로젝트 판별.
기존 컬렉션 키가 있으면 사용, 없으면 새로 생성.

**Collection mapping**: Check existing Zotero collections for the current project. If no collection exists, create one with `zotero_create_collection`. Record the collection key for future use.

### Step 2.2: 중복 체크 + 추가

각 엔트리에 대해:

1. `zotero_search_items`로 DOI 또는 title 검색 → 이미 있으면 skip
2. 없으면 `zotero_add_by_doi` (DOI 있는 경우) 또는 `zotero_add_by_url` (DOI 없는 경우 PubMed URL)
3. `zotero_manage_collections`로 해당 프로젝트 컬렉션에 배치

### Step 2.3: 결과 리포트

```
Zotero Sync:
  Added:     8 papers (new)
  Skipped:   3 papers (already in library)
  Failed:    1 paper (no DOI/PMID)
  Collection: RFA-Meta (TZQEP4NH)
```

> Zotero MCP 미연결 시 이 Phase 전체를 skip하고 Phase 3으로 진행.

---

## Phase 3: Obsidian Literature Notes

### Step 3.1: 기존 문헌 노트 확인

```bash
ls "$VAULT/02 연구/문헌/" | grep -v "📊" | wc -l
```

### Step 3.2: 문헌 노트 생성

각 .bib 엔트리에 대해 `02 연구/문헌/{citekey}.md` 생성.
**이미 존재하면 skip** (덮어쓰지 않음).

#### 템플릿

```markdown
---
notetype: literature
citekey: "{citekey}"
title: "{title}"
authors: "{authors}"
journal: "{journal}"
year: {year}
doi: "{doi}"
pmid: "{pmid}"
created: "{today}"
tags:
  - type/literature
  - _unread
---

# {title}

## 서지 정보
- **저자**: {authors}
- **저널**: {journal}{volume_issue_pages}
- **연도**: {year}
- **DOI**: [{doi}](https://doi.org/{doi})
{pmid_line}

## 핵심 내용 (내 언어로)



## 내 생각



## 관련 노트
- [[🗺️ 연구 종합]]
- [[🗺️ 논문과 리뷰]]
-
-
```

**규칙:**
- `notetype: literature` — Zotero Integration 템플릿과 호환
- `_unread` 태그 — 나중에 Zotero에서 PDF 읽고 하이라이트 추가 시 `_read`로 변경
- `## 핵심 내용`과 `## 내 생각`은 **빈 칸으로 남김** — 사용자가 직접 채움
- `## 관련 노트`는 hub 2개 + 빈 슬롯 2개 (나중에 개념 노트 연결)
- PMID 있으면 PubMed 링크 추가

### Step 3.3: 결과 리포트

```
Obsidian Literature Notes:
  Created:   8 notes (new)
  Skipped:   3 notes (already exist)
  Location:  02 연구/문헌/
  Total in vault: 12 literature notes
```

---

## Phase 4: Concept Extraction (조건부)

### Trigger 조건

문헌 노트가 **10개 이상** 존재할 때만 실행.
10개 미만이면 "문헌 노트 {N}개 — 10개 이상 쌓이면 개념 추출 가능" 메시지만 출력.

### Step 4.1: 교차 개념 스캔

Vault의 `02 연구/문헌/*.md` 전체를 읽고:
1. 각 논문의 title, journal, tags에서 키워드 추출
2. .bib 엔트리의 title에서 주요 개념 추출
3. **3개 이상 문헌 노트에서 교차하는 개념** 식별

### Step 4.2: 필터링 (5가지 기준)

개념 후보에서 제외:
- 모델 이름 (GPT-4, Claude, etc.)
- 데이터셋 이름 (MedQA, ImageNet, etc.)
- 저널 이름
- 기관 이름
- 단순 기법 이름 (too generic)

남는 것만 개념 노트 후보로 제안.

### Step 4.3: 개념 노트 초안 생성

`02 연구/개념노트/{개념 이름}.md` 생성:

```markdown
---
title: "{개념 이름}"
type: concept
tags:
  - 🧠개념
  - {도메인 태그}
aliases:
  - {영문/한글 대체명}
related_papers:
  - "[[{문헌노트1}]]"
  - "[[{문헌노트2}]]"
  - "[[{문헌노트3}]]"
status: 🌱Seedling
---

# {개념 이름}

## 정의 (My Understanding)
> TODO: 내 말로 정리

## 왜 중요한가
{도메인에서의 중요성 — AI가 초안 제공}

## 논문별 관점
- **[[{문헌노트1}]]**: {이 논문에서의 관점}
- **[[{문헌노트2}]]**: {다른 각도}
- **[[{문헌노트3}]]**: {비교/보완}

## 관련 개념
- [[{다른 개념}]]

## 열린 질문
- {아직 답이 없는 질문 1}
- {아직 답이 없는 질문 2}

## 관련 노트
- [[🗺️ 연구 종합]]
- [[{관련 프로젝트 허브}]]
- [[{문헌노트1}]]
- [[{문헌노트2}]]
```

**핵심 규칙:**
- `## 정의` 섹션은 `> TODO` 마커 — 사용자가 직접 채워야 2층의 의미가 있음
- status는 항상 `🌱Seedling`으로 시작
- 관련 노트 4+ wikilinks 필수 (vault 규칙 준수)

### Step 4.4: 사용자에게 제안

```
개념 노트 후보 (3+ 문헌 교차):
  1. {Concept A} (4 papers)
  2. {Concept B} (3 papers)
  3. {Concept C} (5 papers)

생성할까요? (전부 / 선택 / 건너뛰기)
```

사용자 확인 후 생성. **자동 생성하되 확인은 받는다.**

---

## Standalone 모드

.bib 없이 독립 실행도 가능:

### "개념 노트 추출해줘"
→ 기존 `02 연구/문헌/*.md` 스캔 → Phase 4만 실행

### "이 프로젝트 레퍼런스 정리해줘"
→ workspace에서 .bib 파일 탐색 → Phase 1-3 실행

### "Zotero 동기화"
→ Zotero 컬렉션과 .bib 파일 비교 → 빠진 것 추가

---

## Safety Rules

1. **문헌 노트 덮어쓰기 금지** — 사용자 하이라이트/메모가 있을 수 있음
2. **개념 노트 `## 정의` 자동 채우기 금지** — TODO 마커만 (2층의 본질은 사용자 언어)
3. **DOI 없는 엔트리는 Zotero skip** — 수동 추가 안내
4. **Zotero MCP 미연결 시 graceful skip** — Obsidian 노트는 독립적으로 생성
5. **컬렉션 키는 기록** — 새 컬렉션 생성 시 사용자에게 키 보고

## Anti-Hallucination

- **Never fabricate DOIs, PMIDs, or citation metadata.** All bibliographic data must come from the .bib file or API responses.
- **Never auto-fill the "정의 (My Understanding)" section** of concept notes. This must be written by the user.
- **Never overwrite existing literature notes.** User highlights and annotations may be present.
- If a DOI lookup fails, report the failure rather than guessing the metadata.
