# skill.yml — Schema v2

**Status**: Frozen (Phase 0.5.3, 2026-04-24)
**Supersedes**: skill.yml schema v1 (3-month dual-schema period)
**Validator**: `scripts/validate_skill_contracts.py` (v1 warn, v2 enforce)

Skill contract file, one per skill at `skills/<skill>/skill.yml`. Machine-readable companion to `SKILL.md`. Declares execution layer, domain ownership, I/O artifacts, deterministic hooks, and forbidden actions.

## Design principles

1. **Layer-as-policy**: `layer:` classifies execution privilege. Layer A (deterministic script) forbids LLM free-form writes; Layer D (intent/decision) forbids file writes entirely.
2. **Domain ≠ layer**: `owner_domain` routes work (see `capabilities.yml`); `layer` controls how work executes. Both required.
3. **Deterministic steps are declarative**: `deterministic_steps:` is a list the orchestrator MUST invoke during skill execution. Failure modes are explicit.
4. **Forbidden actions are enforceable**: Items in `forbidden_actions:` map to hook/policy checks. Adding one should be enforceable (pre-save hook, validator, or runtime guard).
5. **Path templating via `${SSOT.*}`**: Paths reference the project's `SSOT.yaml` resolver. Literal paths allowed but discouraged.

## Layer definitions

| Layer | Role | Writes allowed | LLM free-form | Example |
|---|---|---|---|---|
| A | Deterministic artifact | Yes, via script | No — script-only | `/render`, `/verify-refs` |
| B | Structured authoring (patch DSL) | Yes, via YAML patch | LLM generates YAML, script applies | `/revise` patches, `/analyze-stats` numbers |
| C | Semantic text (draft/edit) | Yes, diff-tracked | Yes, with change markers | `/write-paper`, `/humanize` |
| D | Intent/decision | `decisions/*.md` append-only | Yes, no other writes | `/orchestrate`, `/self-review` recommendations |

Validator rule: `layer` is required and must be one of `A`, `B`, `C`, `D`.

## Top-level fields

| Field | Required | Type | Notes |
|---|---|---|---|
| `schema_version` | yes | int | Must be `2`. |
| `name` | yes | str | Must equal parent directory name. |
| `layer` | yes | enum | `A` / `B` / `C` / `D`. |
| `owner_domain` | yes | str | Key from `capabilities.yml`. |
| `when_to_use` | yes | str | One-sentence trigger description. |
| `when_NOT_to_use` | yes | str | Anti-trigger / routing guard. |
| `exclusive_with` | no | list[str] | Skills that MUST NOT run concurrently in same project. |
| `sequence_after` | no | list[str] | Skills expected to run first. |
| `inputs` | yes | list[map] | See [inputs/outputs](#inputs--outputs). |
| `outputs` | yes | list[map] | See [inputs/outputs](#inputs--outputs). |
| `deterministic_steps` | no | list[map] | LLM-invoked checkpoints with fail semantics. |
| `deterministic_scripts` | no | list[str] | Scripts bundled by the skill (inventory). |
| `side_effects` | yes | list[str] | Free-form tags (e.g., `writes_project_artifacts`). |
| `downstream_consumers` | yes | list[str] | Skills that read this skill's outputs. |
| `forbidden_actions` | yes | list[str] | Enforceable policy items. |
| `tokens_cap` | no | int | Soft warn threshold (per D-7 session cap). |
| `deprecated` | no | bool | If true, skill is in sunset window. |
| `aliases` | no | list[str] | Accepted alternative names. |

## inputs / outputs

```yaml
inputs:
  - path: "${SSOT.truth.manuscript}"
    schema: pandoc_markdown                 # pandoc_markdown | bibtex | yaml_dict | json | csv
    required: true
  - path: "${SSOT.truth.refs_bib}"
    schema: bibtex
    required: true
  - path: "${SSOT.truth.numbers_yaml}"
    schema: yaml_dict
    required: false

outputs:
  - path: "${SSOT.truth.manuscript}"
    change_log_key: "draft_{date}"
    append_marker: "<!-- change:write-paper:{date} {summary} -->"
```

- `schema:` is advisory metadata; validator does not enforce payload schema in v2.
- `change_log_key` and `append_marker` are templated strings; `{date}` / `{summary}` resolved at runtime by the skill.
- Legacy v1 string-list form (`inputs: [project.yaml, ...]`) accepted by validator with a migration warning.

## deterministic_steps

```yaml
deterministic_steps:
  - name: verify_citekeys
    run: "python3 scripts/verify_refs.py --check-citekeys ${SSOT.truth.manuscript}"
    fail: stop                              # stop | warn | continue
  - name: refresh_manifest
    run: "python3 scripts/update_manifest.py"
    fail: warn
```

- `run` is a shell command. Orchestrator executes before skill body (for gates) or after (for manifests).
- `fail: stop` aborts skill execution on non-zero exit; `warn` logs and proceeds.

## forbidden_actions (common values)

| Tag | Enforcement |
|---|---|
| `generate_references_from_memory` | citation-safety hook, verify-refs gate |
| `silently_edit_frozen_submission` | sync-submission diff check |
| `write_refs_bib_directly` | artifact_contract.md owner rule |
| `hand_tally_counts` | numerical-safety hook |
| `bypass_verify_refs` | pre-save hook verify-refs-guard.sh |

## v1 → v2 migration guide

1. Add `schema_version: 2`.
2. Add `layer:` (see table above).
3. Upgrade `inputs:` / `outputs:` from string list to `{path, schema, required}` maps. (Optional — v1 string lists still parse with warnings.)
4. Add `when_to_use:` and `when_NOT_to_use:` if missing.
5. Optionally add `deterministic_steps:`, `tokens_cap:`, `exclusive_with:`, `sequence_after:`.

**Transition window**: Both v1 and v2 accepted for 3 months (2026-04-24 → 2026-07-24). Validator emits WARN for v1 during window, FAIL thereafter.

## v2 example — write-paper

```yaml
schema_version: 2
name: write-paper
layer: C
owner_domain: manuscript_drafting

when_to_use: "Draft original manuscript or section from scratch."
when_NOT_to_use: "Revising existing text; use revise. Tone cleanup; use humanize."
exclusive_with: [revise, humanize]
sequence_after: [search-lit, analyze-stats]

inputs:
  - path: "${SSOT.truth.manuscript}"
    schema: pandoc_markdown
    required: true
  - path: "${SSOT.truth.refs_bib}"
    schema: bibtex
    required: true
  - path: "${SSOT.truth.numbers_yaml}"
    schema: yaml_dict
    required: false

outputs:
  - path: "${SSOT.truth.manuscript}"
    change_log_key: "draft_{date}"
    append_marker: "<!-- change:write-paper:{date} {summary} -->"

deterministic_steps:
  - name: verify_citekeys
    run: "python3 scripts/verify_refs.py --check-citekeys ${SSOT.truth.manuscript}"
    fail: stop

deterministic_scripts:
  - scripts/inject_citekey_inventory.py

side_effects:
  - writes_project_artifacts
downstream_consumers:
  - self-review
  - verify-refs
  - render
forbidden_actions:
  - generate_references_from_memory
  - silently_edit_frozen_submission
  - write_refs_bib_directly

tokens_cap: 45000
deprecated: false
aliases: [wp, draft_manuscript]
```

## Change log

- **2026-04-24** Schema v2 frozen (Phase 0.5.3). D-3 retained three agents; skill contracts now cover routing previously handled by agent definitions.
