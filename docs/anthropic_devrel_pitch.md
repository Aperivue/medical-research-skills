# Anthropic DevRel Pitch — Draft (2026-05-13)

**Target channels (in escalation order):**
1. **Anthropic Discord** `#claude-code` — first post, lower bar (community visibility, peer feedback)
2. **devrel@anthropic.com** — only if Discord post gets traction or after 1-2 weeks no traction
3. **Anthropic Cookbook contribution** — separate workflow, only after Discord/email open the door

**Tone:** Personal narrative + concrete artifacts + low-pressure ask. Anthropic DevRel sees a lot of pitches; what differentiates is the physician-researcher identity + working demos that are reproducible by anyone with a Claude account.

---

## Discord Post (`#claude-code`)

```
👋 Hey folks — I'm Eugene Kim (Aperivue), a radiologist at Samsung Changwon Hospital
and incoming clinical fellow at Asan Medical Center.

I built medsci-skills — 39 Claude Code skills covering the full medical research lifecycle
(PubMed search w/ anti-hallucination citation verification, IRB protocols, statistical
analysis, IMRAD drafting, 33-guideline EQUATOR reporting compliance, peer review,
revision response). MIT-licensed, archived on Zenodo for academic citation.

What's different from other skill collections:
• Built by a clinician, used on real submissions, not a SaaS demo
• Three end-to-end demos with public datasets (Wisconsin BC, BCG meta-analysis,
  NHANES obesity) — each produces a submission-ready manuscript + figures + STARD/
  PRISMA/STROBE compliance audit in <10 min
• Read-only `setup-medsci` diagnostic so doctors who haven't installed Python
  before can self-debug
• Clinician onboarding guide at docs/setup/ (Mac + Windows, no WSL required)

Repo: https://github.com/Aperivue/medsci-skills

Sharing in case it's useful as:
• a domain-specific reference for the SKILL.md pattern (longer, more workflow-rich
  than typical)
• a case study for "non-developer domain experts using Claude Code"
• a candidate for community spotlights / Cookbook entries

Happy to do a 15-min walkthrough or write a guest post on "Designing skills for
clinicians who haven't used the command line." Feedback welcome 🙏
```

**Length:** ~200 words. Discord-friendly (skimmable, emoji bullets).

**Best posting time:** Tuesday-Thursday 9-11am PST (Anthropic team most active in that window).

---

## Email — `devrel@anthropic.com` (if Discord traction)

**Subject:** Physician-built Claude Code skill collection — case study candidate?

**Body:**

Hi Anthropic DevRel,

[If Discord interaction happened: "Following up on our Discord exchange in #claude-code on [date]..."]

I'm Eugene Kim, a radiologist (Aperivue). Over the past year I've built medsci-skills — 39 Claude Code skills covering the full medical-manuscript lifecycle: PubMed search with anti-hallucination citation verification, study design, IRB protocols, statistical analysis, IMRAD drafting, 33-guideline EQUATOR reporting compliance (STARD-AI, TRIPOD+AI, CLAIM, PRISMA-DTA, etc.), journal selection, peer review, revision response. MIT-licensed, archived on Zenodo (DOI 10.5281/zenodo.XXXXXXX), tested on real publications.

Three end-to-end demos run on public data and produce submission-ready manuscripts in <10 minutes:
- Wisconsin Breast Cancer (diagnostic accuracy, STARD)
- BCG vaccine meta-analysis (PRISMA 2020, R metafor)
- NHANES obesity (epidemiology, STROBE, survey weights)

Repo: https://github.com/Aperivue/medsci-skills

Sharing in case it's useful as:
1. A reference for the SKILL.md pattern in regulated domains (workflow-heavy, audit-trail-aware, anti-hallucination guards)
2. A case study for the "non-developer domain expert" persona — clinicians who don't ship code but want Claude to handle the manuscript pipeline
3. A candidate for community spotlights, the Cookbook, or a guest post on Anthropic's blog

Happy to do a 30-min demo call or contribute a written piece on "Designing Claude Code skills for clinicians" — covering the read-only diagnostic pattern, the docs/setup/ onboarding flow, and the EQUATOR-guideline embedding strategy.

Thanks for your work on Claude Code — the skill system has been the right primitive for this kind of domain-specific tooling.

Best,
Eugene Kim, MD
[ORCID 0000-0001-8565-1360]

---

## 제출 후 Follow-up

- Discord 포스트 링크 또는 thread ID 캡처해서 `docs/anthropic_devrel_pitch.md` notes 섹션에 기록
- Discord 반응 (이모지, 댓글, DM) 24-48시간 모니터링
- 반응이 있으면: DM으로 더 깊은 대화 → 그쪽이 원하면 email로 escalate
- 반응 없으면: 1주 후 channel을 다른 시간대에 한 번 더 cross-post (toxic 아님)
- email 보낼 때는 반드시 DOI 채워진 후 (Zenodo archive 완료 후)

## 톤 가드

- ❌ "Looking for a feature on the Anthropic blog" (직접 요구)
- ✅ "in case it's useful as a candidate for ..." (제안형)
- ❌ 별 수 (86), 사용자 수 광고
- ✅ Demo 결과물 + 의사 정체성 차별점
- ❌ "the most comprehensive medical Claude skills"
- ✅ "specifically focused on the manuscript pipeline"
