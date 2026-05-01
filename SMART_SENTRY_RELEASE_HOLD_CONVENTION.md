# Smart Sentry Release-Hold Convention

Use the phrase `release-hold <feature-or-tab-name>` when an unfinished Smart Sentry feature must stay out of the active release UI but must remain easy to restore later.

## Purpose

- Keep unfinished work out of the release surface without deleting the implementation.
- Prevent unfinished tabs from changing runtime behavior in a release build.
- Give future editors one named workflow and one implementation point.
- Make restoring the tab quick: remove the hold entry and the normal tab returns without rebuilding the tab system.

## Current Command

- `release-hold Facial Recognition`
- `release-hold AI Assistant`

## Files To Read Before Applying A Release Hold

1. `app/sentry_v2/sentry_v2_tab.py`
2. `SMART_SENTRY_MANUAL.md`
3. `SMART_SENTRY_APP_CHANGE_IMPACT.md`
4. `SMART_SENTRY_BUILD_RELEASE_STANDARD.md`

## Implementation Rule

1. Add the unfinished tab to `SETTINGS_TAB_RELEASE_HOLDS` in `app/sentry_v2/sentry_v2_tab.py`.
2. Keep the tab definition in `SETTINGS_TAB_SPECS`; the release-hold filter hides it temporarily instead of deleting its normal registration.
3. Do not add the held tab to the active `QTabWidget` for the release build.
4. Ensure previous and next settings-tab navigation still works on the reduced visible tab set.
5. Do not let the held tab create runtime side effects during app startup.
6. Restoration rule: removing the tab from `SETTINGS_TAB_RELEASE_HOLDS` must make it visible again without any further code changes.

## Documentation Rule

1. Update `SMART_SENTRY_MANUAL.md` so the tab is described as temporarily hidden by release hold.
2. Update `SMART_SENTRY_APP_CHANGE_IMPACT.md` so reviewers know the tab is intentionally hidden for release but restored by removing the hold entry.
3. Update `SMART_SENTRY_BUILD_RELEASE_STANDARD.md` so release validation checks the held state before packaging.
4. Add a concise entry to `RECENT_UPDATES.json` when the release-hold state changes.

## Removal Rule

When the feature is ready for release, remove it from `SETTINGS_TAB_RELEASE_HOLDS`, restore any documentation that still marks it as held, and revalidate the tab as a normal runtime surface before packaging. No other tab-registration edits should be required.
