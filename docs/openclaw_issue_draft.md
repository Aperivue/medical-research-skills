# OpenClaw Inclusion Issue — Draft (2026-05-13)

**Target repo:** https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills
**Action:** File an issue (not a PR) asking the maintainers about inclusion process for external skill collections.

**Tone:** Collaborative, not promotional. We want to learn their preferred format before sending a PR — sending an unsolicited PR to a 2.5k-star aggregator without checking their inclusion criteria is the wrong move.

---

## Issue Title

`Question: inclusion process for external skill collections (medsci-skills)`

## Issue Body

Hi OpenClaw team — really impressive aggregation work, especially the curation across 12+ source repositories.

I maintain [medsci-skills](https://github.com/Aperivue/medsci-skills), a 39-skill MIT-licensed Claude Code skill collection focused specifically on the medical-manuscript pipeline (PubMed search with anti-hallucination citation verification, IRB protocol drafting, IMRAD writing, 33-guideline EQUATOR reporting compliance, peer review, revision response). It's built and used by a practicing radiologist, with three end-to-end demos that produce submission-ready manuscripts from public datasets in under 10 minutes. v3.0.0 is archived on Zenodo for academic citation.

I noticed that the README mentions aggregating 12+ open-source skill repositories but I couldn't find a `CONTRIBUTING.md` or a documented inclusion process. Before sending a PR, I wanted to ask:

1. **Preferred format**: Do you prefer (a) a PR adding a single linked entry to the README, (b) a structured manifest file (e.g., YAML/JSON) listing source repos, or (c) a category-specific listing under a particular section?
2. **Mirror vs link-only**: Are skills from external repos mirrored into your `skills/` directory, or only linked from the README?
3. **Quality gates**: Are there any inclusion criteria (minimum stars, license requirements beyond MIT/Apache/BSD, demo coverage, contributor identity)?

Happy to follow whatever format you prefer. Repo for reference: https://github.com/Aperivue/medsci-skills

Thanks for the work on this — it's a great resource for the biomedical AI community.

---

## 제출 후 Follow-up

- 답변 받으면 그쪽 preferred format으로 PR 즉시 작성
- 1주 무응답 시 한 번만 ping (정중하게)
- 2주 무응답 시 close 권장 (다른 채널에 시간 투자)
- 응답이 "그냥 PR 보내라" 면 README에 단일 엔트리 형태로 PR 작성

## 톤 가드

- ❌ "We have N skills, can you add us?" (sales pitch)
- ✅ "Before sending a PR, wanted to check your preferred format" (collaborative)
- ❌ "Our skills are better because..." (comparative)
- ✅ "Specifically focused on the medical-manuscript pipeline" (scope clarification)
- ❌ "Please consider including" (begging)
- ✅ "Happy to follow whatever format you prefer" (deferential to maintainer)
