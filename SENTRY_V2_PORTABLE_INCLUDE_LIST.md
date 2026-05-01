# Smart Sentry v2 Portable Build Include List

This document defines the intended **portable-only** surface for Smart Sentry v2 packaging.

## Required entrypoints

- run.py

## Compatibility entrypoints retained only so older launch paths still resolve

- run_smart_sentry_v3.py
- app/run_sentry_v2.py

## Required Smart Sentry v2 package files

- app/sentry_v2/__init__.py
- app/sentry_v2/engagement_planner.py
- app/sentry_v2/ml_training_helper.py
- app/sentry_v2/ml_training_logger.py
- app/sentry_v2/precision_tuning_logger.py
- app/sentry_v2/prompted_targets.py
- app/sentry_v2/sentry_v2_comm.py
- app/sentry_v2/sentry_v2_config.py
- app/sentry_v2/sentry_v2_detector.py
- app/sentry_v2/sentry_v2_engine.py
- app/sentry_v2/sentry_v2_no_fire_masks.py
- app/sentry_v2/sentry_v2_overlay.py
- app/sentry_v2/sentry_v2_pir_manager.py
- app/sentry_v2/sentry_v2_tab.py
- app/sentry_v2/sentry_v2_tooltips.py
- app/sentry_v2/sentry_v2_video_canvas.py
- app/sentry_v2/sound_engine.py
- app/sentry_v2/simple_tracker.py
- app/sentry_v2/target_filter.py
- app/sentry_v2/threat_scorer.py

## Required Smart Sentry v2 data/config/assets

- app/config/smart_sentry_settings.json
- app/config/smart_sentry_custom_presets.json
- app/config/smart_sentry_prompted_targets.json
- app/config/smart_sentry_faces.json
- app/LOGO.png

## Required detection model folders

- YOLO_MODELS/

This is the only supported source-side and operator-facing portable-release model folder. Do not mirror models into app/models/ or app/YOLO_MODELS/.

For the packaged release, keep the public drop location at the release root as `F:\SMART SENTRY V<version>\YOLO_MODELS`. Bundled fallback weights may also exist under `SMART_SENTRY_V<version_token>_FILES\YOLO_MODELS`, but that support-folder copy is not the operator-facing drop target.

Use the interpreter selected by the build helper in this order: `SMART_SENTRY_PYTHON_EXE`, then parent or repo `.venv311`, then parent or repo `.venv`.

## Required dependency manifest

- requirements-sentry-v2-portable.txt

## Exclusion intent

Portable Smart Sentry v2 packaging should not require loading or importing main app UI modules from app/MAIN_FILE_SINGLE_CAM.py.
