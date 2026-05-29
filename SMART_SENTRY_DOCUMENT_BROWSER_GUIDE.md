# Smart Sentry Document Browser Guide

Date: 2026-05-14
Status: Live and validated in the current Smart Sentry runtime.
Audience: Operators and developers

## Purpose

Smart Sentry now includes a built-in document browser so operators can search manuals, guides, reports, checklists, and other repository documents from either the integrated Documentation tab or a separate browser window.

The current recommended first document is `SMART_SENTRY_DOCUMENTATION_HUB.md`, which acts as the live entry point for the current Smart Sentry document set.

## How To Open It

UI launch paths:

- Settings tabs -> `Documentation`
- Settings nav -> `?` for current-tab help in the detached browser
- Top strip -> `Docs`
- Controls tab -> Quick Actions -> `Docs Browser`

Voice launch paths:

- `open document browser`
- `open docs browser`
- `browse documents`

The voice launch paths continue to open the separate browser window. The Documentation tab uses the same formatted browser widget inside the main settings stack.

## Reader Standard

The Documentation tab and detached `Docs Browser` window now share one presentation layer for every indexed document.

That shared renderer provides:

- colorized section headings for faster scanning
- top-of-document metadata chips for fields such as `Date`, `Status`, and `Audience`
- consistent table, code, callout, and link styling
- the same content rendering in both documentation surfaces
- live Smart Sentry theme colors in both documentation surfaces instead of a separate fixed browser palette

The writing standard that pairs with this renderer is documented in `SMART_SENTRY_DOCUMENTATION_STYLE_STANDARD.md`.

## What It Indexes

The browser scans Smart Sentry markdown and text documents under the runtime root.

Indexed document types:

- `.md`
- `.txt`

The browser skips runtime-heavy or non-document folders such as `.git`, `.venv`, `logs`, `snapshots`, `sounds`, and model directories.

Overview documents such as the documentation hub and style standard are prioritized ahead of general guides and reports so operators can find the current document map quickly.

## How To Use It

1. Use the quick-search bar at the top of the browser to type a feature, file name, path fragment, or keyword.
2. Optionally narrow the list with the category filter.
3. Review the compact left-pane file list, which stays at one line per matching file name even when the search matched document body text.
4. Select a file in the left pane.
5. Read it in the formatted viewer on the right.
6. Use `Open File` or `Open Folder` if you want the original document in the external editor or folder view.

## Recommended Starting Path

1. Open `SMART_SENTRY_DOCUMENTATION_HUB.md`.
2. Jump to `SMART_SENTRY_MANUAL.md` for live app behavior and UI contracts.
3. Open specialized guides such as the face, export, shortcut, or PIR documents only when you need their specific workflow.

## Notes

- The browser renders markdown in-app when Qt markdown rendering is available.
- Use `Refresh` after adding or editing documentation so the index updates immediately.
- The Documentation tab and the separate `Docs Browser` window share the same top quick-search bar, category filter, compact single-line file list, formatted reader, and file or folder actions.
- The Documentation tab and detached browser now also share the same colorized formatting standard and live theme-token styling, so improvements to the renderer automatically apply across the whole in-app documentation surface.
- The settings-nav `?` action opens the detached browser with the quick-search field already filled for the current settings topic, so operators can jump from a tab directly into the matching docs.
- Use the Documentation tab when you want the docs embedded inside the main runtime UI, and use the separate `Docs Browser` window when you want a detached reader on another monitor or beside other settings work.
- The document browser is intended to be the fast operator and developer entry point for finding Smart Sentry documentation without leaving the runtime UI.