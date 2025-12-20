# Commit naming convention (main)

This repo uses a simple version tag prefix so every commit to `main` is easy to scan.

## Single source of truth for the version
- Update `DB3K_VERSION.txt` when bumping versions (e.g. `4.1` -> `4.2` -> `4.3`).

## Commit subject format (required for main)
Prefix every commit subject to `main` with:

`db3kv<version> - <summary>`

Examples:
- `db3kv4.1 - fix: stabilize serial reconnect`
- `db3kv4.2 - feat: add new idle behavior presets`
- `db3kv4.3 - refactor: unify tracking toggles`

Notes:
- Keep `<summary>` short and action-oriented.
- If you bump the version, bump it in `DB3K_VERSION.txt` first, then use that same version in the commit prefix.

