# Smart Sentry Face Import Voice Guide

Date: 2026-05-13
Status: Live and validated in the current Smart Sentry runtime.
Audience: Operators and developers

## Purpose

Smart Sentry now supports two folder-backed face image flows so operators do not need to speak Windows file paths.

Flow 1 uses a preview inbox for multi-face scene review.
Flow 2 uses per-profile photo batches for direct enrollment or refresh of one saved identity.

## Folder Layout

All voice-backed face image imports live under:

`face_imports/`

The preview inbox is:

`face_imports/preview_inbox/`

The per-profile batch folder root is:

`face_imports/profile_batches/`

Create one folder per person under the batch root. Example:

`face_imports/profile_batches/Mom/`
`face_imports/profile_batches/Intruder/`

Supported image files:

- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`
- `.tif`
- `.tiff`
- `.webp`

## Flow 1: Preview Inbox

Use this flow when one photo may contain multiple faces and you want Smart Sentry to detect them in preview before saving.

1. Drop a photo into `face_imports/preview_inbox/`.
2. Say `load latest face import` or `load latest face import into preview`.
3. Smart Sentry loads the newest image into the preview and immediately runs face detection.
4. Review the detected face rows and then say `save detected faces` if they look correct.

When the Facial Recognition tab is visible, the Photo Enrollment group also exposes:

- `Load Latest Inbox Photo`
- `Open Import Folder`

## Flow 2: Per-Profile Photo Batches

Use this flow when you want to enroll or refresh one saved identity from several photos at once.

1. Create or reuse a folder under `face_imports/profile_batches/<face name>/`.
2. Place one or more photos of that person in the folder.
3. Use one of these commands:

- `import face photos for Mom`
- `import target face photos for Intruder`
- `import friendly face photos for Mom`

Behavior rules:

- If the profile already exists and you do not say target or friendly, Smart Sentry preserves the saved disposition, announce-name flag, greeting gesture flag, and notes.
- If you explicitly say `target`, the imported profile is stored as a target.
- If you explicitly say `friendly`, the imported profile is stored as friendly.
- Imported image batches use the same face-library save path as the existing UI enrollment flow.

## Voice Examples

- `Load latest face import`
- `Open face import inbox`
- `Save detected faces`
- `Import face photos for Alice Johnson`
- `Import target face photos for Intruder`

## Operational Notes

- The preview inbox always loads the newest supported image file first.
- Batch imports resolve folder names using the same tolerant face-name normalization used by other face voice commands.
- If face recognition was disabled, a successful image import automatically enables it so the newly saved profiles become active immediately.