---
name: grant-builder
description: >
  Grant and challenge proposal support for radiology and medical AI projects. Structures significance,
  innovation, approach, milestones, and consortium roles while keeping claims evidence-based and executable.
triggers: grant, proposal, aims page, grant proposal, significance, innovation, approach, milestones, 산학과제, 산학협력, 과제계획서, 연구계획서, 연구비 신청, 첨부3
tools: Read, Write, Edit, Bash, Grep, Glob
model: inherit
---

# Grant-Builder Skill

## Purpose

This skill supports competitive proposal writing for:

- national R&D grants
- multi-institution consortia
- challenge proposals
- internal pilot funding
- translational medical AI project plans
- **Korean government grants** (복지부, 산자부, 중기부, 지자체 산학협력 과제)

It is optimized for projects where clinical relevance, multi-site coordination, and executable milestones matter as much as technical novelty.

---

## Korean Government Grant Mode (산학과제 / 연구계획서)

When the user asks for a **Korean산학과제 or 연구계획서**, apply the following adaptations:

### Document Structure (첨부 기반)
Most Korean grants use a standardized 3-attachment format:
- **첨부1 (기본정보)**: 과제명, 참여기관, 연구진 인적사항, 논문/특허 실적
- **첨부2 (매칭확인서)**: 기관별 연구비 부담 비율 확인 (Zoom 미팅 후 작성)
- **첨부3 (연구계획서)**: 10-page 본문 — 아래 구성

### 첨부3 Standard Structure
```
1. 연구의 필요성 및 목적 (약 2p)
   - 임상 문제점 + 수치 제시
   - 국내외 동향 (최근 3-5년 논문/가이드라인 기반)
   - 본 과제의 차별성

2. 연구 내용 및 방법 (약 4p)
   - 단계별 추진 계획 (Phase 1~N, 기간 명시)
   - 연구 모식도 (AI 파이프라인 포함 시 도식화)
   - 세부 과제별 담당 기관/인력

3. 연구팀 역량 (약 1p)
   - 각 참여자 전문성 + 대표 실적 (SCI 논문, 특허)
   - 기관별 시너지 (병원 = 데이터/임상, 대학 = 알고리즘)

4. 기대 성과 및 활용 방안 (약 2p)
   - 정량 목표: SCI 논문 N편, 특허 N건
   - 정성 목표: 임상 파급효과, 표준화 기여
   - 후속 대형 과제 연계 가능성 (seed 역할)

5. 연구비 집행 계획 (약 1p)
   - 인건비(RA), 전산장비, 소모품, 학술활동비, 간접비
```

### Writing Tips for Small-Scale Grants (3천만원 미만)
- 비전문가도 이해 가능한 서술 (심사위원이 비전공자일 수 있음)
- 실현 가능성을 기술 혁신성보다 강조
- 분량·형식 준수 우선 (양식 초과 감점)
- 선행연구 데이터나 예비 결과가 있으면 반드시 포함
- 정량 목표는 보수적으로 — 미달보다 초과 달성이 유리

---

## Communication Rules

- Communicate with the user in their preferred language.
- Proposal prose should be in the language required by the target call.
- Avoid hype. Emphasize unmet need, feasibility, differentiation, and deliverables.

---

## Core Outputs

Depending on the request, produce one or more of:

- project concept summary
- `Significance`
- `Innovation`
- `Approach`
- specific aims
- work packages
- milestone table
- role split by institution
- evaluation framework
- reviewer-risk memo

---

## Workflow

### Phase 1: Decode the funding call

Extract:
- funding body
- call theme
- eligibility constraints
- deliverable expectations
- timeline
- evaluation criteria

If no call text is available, infer a generic academic-medical AI proposal structure and label assumptions.

### Phase 2: Frame the problem

Define:
- clinical pain point
- current workflow limitation
- why existing AI or standard care is insufficient
- who benefits if the project succeeds

**Gate:** Present the problem framing (clinical pain point, gap, proposed solution) to the
user. Confirm before building proposal sections — a misframed problem produces an
unfundable proposal.

### Phase 3: Build the proposal spine

Always articulate:
- problem
- gap
- proposed solution
- why this team can execute it
- measurable outputs

### Phase 4: Convert to proposal sections

#### Significance

Must answer:
- why this matters clinically
- why this matters now
- why the proposed solution is worth funding

#### Innovation

Should focus on:
- what is genuinely different
- why the integration is new
- why the novelty is useful, not just technical

#### Approach

Should define:
- dataset and participating sites
- model or workflow components
- validation plan
- benchmark/comparator
- failure analysis
- risk mitigation

### Phase 5: Execution plan

Generate:
- milestones by quarter or year
- institution-level responsibilities
- dependencies and handoffs
- required infrastructure

---

## Default Structure

```text
## Proposal Summary
Title: ...
Goal: ...
Clinical problem: ...

### Significance
...

### Innovation
...

### Approach
Aim 1. ...
Aim 2. ...
Aim 3. ...

### Milestones
- ...

### Consortium roles
- ...

### Major risks and mitigations
- ...
```

---

## Evaluation Heuristics

Before finalizing, check:

1. Is the clinical need explicit and credible?
2. Is the novelty more than "we will use AI"?
3. Are the aims linked to measurable outputs?
4. Is the validation plan convincing?
5. Is the multi-site structure realistic?
6. Are compute, annotation, and regulatory needs acknowledged?
7. Does each institution have a distinct role?

---

## Common Weaknesses To Flag

- novelty described without clinical consequence
- vague benchmark or success criterion
- no external validation or deployment path
- too many aims for the timeline
- consortium members listed but not functionally integrated
- proposal sounds like a paper, not a funded program

---

## Handoff Rules

- route to `search-lit` to support significance and prior-art positioning
- route to `design-study` if the evaluation framework is weak
- route to `write-paper` only when the proposal requires publication-style narrative sections

---

## What This Skill Does NOT Do

- It does not fabricate budget details
- It does not promise datasets, partners, or infrastructure not evidenced by the user
- It does not replace institutional administrative review
