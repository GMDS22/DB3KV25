# Smart Sentry Documentation Hub

Date: 2026-05-14
Status: Live documentation entry point for the current Smart Sentry app
Audience: Operators, developers, validators
Start Here: Open this first from the Documentation tab when you need the current document map

## Purpose

This hub is the current starting point for Smart Sentry documentation.

Use it to quickly identify:

- which documents describe the live runtime contract
- which documents describe proposal-only work that is not live yet
- which documents are validation, issue-history, or release-reference material
- which documents should be updated when app behavior changes

## Current App Snapshot

| Area | Current Live Contract |
|---|---|
| Runtime | Standalone Smart Sentry runtime under `app/sentry_v2/` |
| Canonical settings file | `app/config/smart_sentry_settings.json` |
| Current hardware contract | `NANO BOARD USB + DEBUG BOARD USB` |
| Documentation surfaces | Embedded `Documentation` tab and detached `Docs Browser` window share the same renderer and index |
| Current UI note | The settings architecture defines 14 active tabs, including live `Facial Recognition`, `AI Assistant`, and `Documentation` surfaces plus top-strip `Docs` and `Quick Keys` shortcuts |
| Current behavior authority | `SMART_SENTRY_MANUAL.md` plus `SMART_SENTRY_AUTOTRACKING_BEHAVIOR_BLUEPRINT.md` |

## Read These First

| If you need... | Read... | Why |
|---|---|---|
| Full live app reference | `SMART_SENTRY_MANUAL.md` | Canonical runtime behavior, UI, config, architecture, and troubleshooting |
| Documentation browser behavior | `SMART_SENTRY_DOCUMENT_BROWSER_GUIDE.md` | How the Documentation tab and detached browser work |
| Documentation formatting rules | `SMART_SENTRY_DOCUMENTATION_STYLE_STANDARD.md` | Required writing and formatting standard for live docs |
| Tracking and aiming behavior contract | `SMART_SENTRY_AUTOTRACKING_BEHAVIOR_BLUEPRINT.md` | Current target tracking and fire-gating behavior authority |
| PIR current contract audit | `PIR_AT_A_GLANCE.md` | Current PIR firmware, transport, settings, and hunt-behavior audit |
| PIR operator setup and tuning | `PIR_GUARD_QUICK_START.md` | Current operator setup, search, and troubleshooting guide |
| Shortcut and operator key map | `SMART_SENTRY_SHORTCUT_KEYS.md` | Live operator keyboard reference |
| Face import and voice-driven face workflows | `SMART_SENTRY_FACE_IMPORT_VOICE_GUIDE.md` | Current face import, preview-inbox, and batch-import contract |
| Runtime export behavior | `SMART_SENTRY_RUNTIME_DATA_EXPORT.md` | Snapshot and conversation export contract |

## Live Runtime Documents

These files should reflect the current app as it exists now:

- `SMART_SENTRY_MANUAL.md`
- `SMART_SENTRY_AUTOTRACKING_BEHAVIOR_BLUEPRINT.md`
- `SMART_SENTRY_DOCUMENT_BROWSER_GUIDE.md`
- `SMART_SENTRY_DOCUMENTATION_STYLE_STANDARD.md`
- `PIR_AT_A_GLANCE.md`
- `PIR_GUARD_QUICK_START.md`
- `PIR_DOCUMENTATION_INDEX.md`
- `SMART_SENTRY_SHORTCUT_KEYS.md`
- `SMART_SENTRY_FACE_IMPORT_VOICE_GUIDE.md`
- `SMART_SENTRY_RUNTIME_DATA_EXPORT.md`
- `SMART SENTRY — CONVERSATION & COMMAND.md`

## Proposal And Design Documents

These files are useful for planning, but they must not be treated as the live runtime contract until implementation is verified and promoted:

- `SMART_SENTRY_VNEXT_TRACKING_AND_SCENE_MEMORY_PROPOSAL.md`
- `SMART_SENTRY_VNEXT_IMPLEMENTATION_MAP.md`
- architecture or implementation proposal documents that explicitly describe future behavior

## Validation, Release, And History Documents

These files remain useful, but they describe validation state, release work, or issue history rather than the single source of truth for live behavior:

- `SMART_SENTRY_ISSUE_LOG.md`
- `PIR_INTEGRATION_SUMMARY.md`
- `PIR_GUARD_IMPLEMENTATION_COMPLETE.md`
- live validation checklists
- release compilation protocols
- release fix logs, reports, summaries, and update notes

## Documentation Tab Standard

The Documentation tab and detached Docs Browser now apply one shared presentation standard to all indexed documents:

- colorized headings for section scanning
- metadata chips for top-of-document summary lines such as `Date`, `Status`, and `Audience`
- consistent styling for tables, callouts, links, and code blocks
- the same rendering, indexing behavior, and live theme alignment in both documentation surfaces

This means source documents should stay structurally clean. Do not add random inline HTML colors to individual files unless a document genuinely needs a special visual cue.

## Maintenance Rules

1. Update `SMART_SENTRY_MANUAL.md` when live behavior, UI, settings, or hardware contracts change.
2. Update `SMART_SENTRY_DOCUMENT_BROWSER_GUIDE.md` when the Documentation tab, detached browser, or indexing rules change.
3. Update `SMART_SENTRY_DOCUMENTATION_STYLE_STANDARD.md` when the writing format or document presentation standard changes.
4. Keep proposal work in proposal documents until the implementation is verified.
5. Keep issue history and failed attempts in `SMART_SENTRY_ISSUE_LOG.md`, not in the manual.

## Recommended Documentation Tab Workflow

1. Start with this hub.
2. Open the manual for live behavior questions.
3. Open the blueprint for tracking or aiming contract questions.
4. Open specialized guides for face, export, shortcuts, PIR, or release tasks.
5. Refresh the browser after adding or editing documents so the live index updates.