# AutoTrack Lab — Change Log

## 2026-01-26
- Initial experimental app: First-Lock targeting + Follow / Quick Strike modes.
- Hybrid YOLO + OpenCV tracker pipeline with preset-driven tuning.
- Dual Port ready (COM8 Nano IO + COM9 Debug Board pan/tilt).
- Auto-run on launch, single Connect/Disconnect toggle, dark theme, and camera debug logging.
- Added camera selection with live reopen and saved camera index.
- Synced pan/tilt min/max to main app defaults (PAN 0–220, TILT 0–70).
- Simplified detection pipeline with default blob detector (YOLO optional).
- Fixed OpenCV tracker dependency by adding detection-only fallback.
- Added target/candidate overlays and stabilized blob detection to reduce aim drift.
