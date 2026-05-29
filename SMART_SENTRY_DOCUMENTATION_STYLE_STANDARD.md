# Smart Sentry Documentation Style Standard

Date: 2026-05-13
Status: Live documentation formatting standard
Applies To: Markdown and text documents shown in the Smart Sentry Documentation tab and Docs Browser
Owner: Smart Sentry repository documentation

## Purpose

This standard keeps Smart Sentry documentation readable, visually consistent, and aligned with the current app.

The in-app document browser now supplies the shared colorized presentation layer. Source files should focus on clean structure, accurate content, and predictable metadata.

## Required Header Pattern

For new or rewritten live documents, use this opening pattern whenever possible:

```md
# Document Title

Date: 2026-05-13
Status: Live current-app guide
Audience: Operators, developers, validators
```

The shared document browser turns these metadata lines into visual summary chips.

## Section Structure

Use this order where it fits the document:

1. Purpose or current-app snapshot
2. How to use or how it works
3. Important rules, limits, or contracts
4. Troubleshooting, validation, or update notes

Prefer short sections with descriptive headings over long unbroken paragraphs.

## Formatting Rules

- Use `#`, `##`, and `###` headings with clear names.
- Use tables for settings, launch paths, status vocabularies, and comparison summaries.
- Use blockquotes only for important notes, warnings, or contract statements.
- Use code blocks for commands, payloads, or file-layout examples.
- Use bold text sparingly for critical terms.
- Keep filenames, commands, config keys, and spoken phrases in backticks.

## Status Vocabulary

| Label | Meaning |
|---|---|
| `Live` | Verified current runtime behavior |
| `Current App` | Verified and intended for present operator use |
| `Proposal` | Planned or experimental work that is not yet the live contract |
| `Validation` | Test, checklist, or verification material |
| `Historical` | Release notes, reports, or archived context |

## Current-App Accuracy Rules

- Do not describe proposal work as if it is already live.
- When behavior changes, update the manual and any specialized live guide in the same change.
- If a file is historical or release-specific, say so clearly near the top.
- Prefer versionless canonical runtime paths when they are the live contract.

## Naming Guidance

- Use `SMART_SENTRY_...` naming for canonical Smart Sentry documents.
- Use `...GUIDE` for task-oriented docs.
- Use `...MANUAL` for broad reference.
- Use `...STANDARD` for repository-wide writing or formatting rules.
- Use `...CHECKLIST`, `...REPORT`, `...SUMMARY`, or `...PROTOCOL` only when the file truly serves that role.

## In-App Presentation Rules

The shared renderer now provides:

- colorized heading hierarchy
- metadata chips for top summary lines
- styled tables, links, code, and callouts
- the same formatting in the embedded Documentation tab and detached Docs Browser

Because of that shared renderer:

- do not hardcode arbitrary font colors inside individual Markdown files just to make them readable
- prefer clean Markdown structure and let the viewer supply the visual treatment
- only use inline HTML when a document requires a genuinely special layout or compatibility workaround

## Update Triggers

Update the relevant documentation when any of these change:

- visible runtime UI tabs or major controls
- voice commands or operator workflows
- canonical config paths or persistence rules
- hardware topology contracts
- document browser behavior or indexing rules

## Minimum Review Checklist

Before considering a document current:

1. Confirm it reflects the current Smart Sentry runtime rather than planned behavior.
2. Confirm paths, filenames, and tab names match the app.
3. Confirm the top metadata lines are present for new or heavily updated live docs.
4. Confirm the document reads cleanly inside the Documentation tab.