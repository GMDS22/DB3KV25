# Vosk Offline Model Folder

Place your extracted Vosk model files in this folder.

Recommended model:
- `vosk-model-small-en-us-0.15` (small footprint, good command latency)

Expected structure example:
- `models/vosk/am`
- `models/vosk/conf`
- `models/vosk/graph`
- `models/vosk/ivector`

Notes:
- Smart Sentry voice commands require a valid model folder at runtime.
- If this folder is missing model files, the listener stays disabled and logs a startup warning.
