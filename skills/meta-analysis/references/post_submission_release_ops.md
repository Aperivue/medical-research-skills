# Post-Submission Release Operations

**When**: Phase 9 (circulation) 완료 직후 ~ 저널 submission 사이. Phase 10 (recovery)와 별개.

**Why it's hard**: 회람 중(v7~v18 병존) 수치가 계속 흔들린다. DOI를 너무 일찍 찍으면 content mismatch로 재발급 필요. 너무 늦게 찍으면 submission 당일 급함.

## Checklist

### Gate 1 — Release 발급 시점

- [ ] 내부 회람 종결: 모든 reviewer(내부 PI, 외부 peer)가 sign-off.
- [ ] `[VERIFY-CSV]` / `TODO` / `FIXME` / `(to be regenerated)` tag가 manuscript / supplement / figures / code에서 전수 제거 (`rg -n` 0 hits).
- [ ] k값(포함 연구 수)이 `4_Analysis/*.csv` row count와 manuscript prose / PRISMA flow / figure caption 전체에서 일치.
- [ ] 저자 순서 / ICMJE COI가 최종 확정 (Zenodo 저자 메타데이터 반영 직전).

### Gate 2 — GitHub repo

- [ ] `_build.sh`로 저널 타깃 번들 재생성 성공.
- [ ] Repo에 raw analysis code, extraction_consensus_log.md, PROSPERO amendments tracker, methodology 포함.
- [ ] README에 DOI placeholder (Zenodo 발급 후 치환).
- [ ] `.gitignore`에 raw PDF / 저작권 자료 제외 확인.
- [ ] LICENSE 명시 (CC-BY 4.0 또는 저널 요구 license).

### Gate 3 — Zenodo DOI

- [ ] Zenodo record metadata: 저자 순서, affiliation, ORCID, keywords, related identifiers (PROSPERO registration number).
- [ ] `related_identifiers`에 GitHub repo release tag URL을 `isSupplementTo`로.
- [ ] Submission package(.tar.gz)가 Zenodo에 업로드됐는지. 회람 패키지(vN)가 아닌 저널 제출 번들.
- [ ] DOI 발급 후 manuscript / cover letter / submission portal의 "data availability" 섹션에 반영.

### Gate 4 — Reject 후 재타깃 처리

- [ ] 동일 content로 다른 저널 재제출: **Zenodo new version 발급 금지** (DOI는 content에 붙음). `_build.sh --journal {new}`로 새 SUBMISSION 폴더만 생성.
- [ ] Revision 후 재제출: content 변경 → Zenodo new version 발급. concept DOI는 유지.
- [ ] 저자 변경 발생 시 ICMJE COI 재배포 + Zenodo new version.

## Common failures

- **F1**: Zenodo DOI minted while `k` (included study count) is still oscillating between versions → content-DOI mismatch forces re-issue. **차단**: Gate 1.
- **F2**: Journal-specific folders edited by hand without a `_build.sh` → the journal copies drift from master. **차단**: `submission_package_drift.md` 참조.
- **F3**: `TODO` / `FIXME` tag left in an R analysis script surfaces only after the repo is pushed to GitHub. **차단**: Gate 1 `rg` scope에 code 포함.
