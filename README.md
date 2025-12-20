# Auto Turret — Setup & Troubleshooting

## Rapid-Fire Support — Arduino Firmware Requirements

The rapid-fire feature in this software works by sending repeated ON/OFF commands to the Arduino to pulse the firing trigger at the configured rate and duty cycle.

**IMPORTANT:** For rapid-fire to work as intended, your Arduino sketch (firmware) must support receiving and acting on multiple ON/OFF trigger commands in quick succession. If your current firmware only responds to a single ON/OFF (i.e., it latches the trigger and ignores further ON/OFF commands until reset), you will need to update your Arduino code.

**Recommended:**

- Ensure your Arduino code toggles the firing output each time it receives an ON or OFF command from the host.
- The host will send ON/OFF commands at the rapid-fire rate you set in the UI.
- If you want true rapid-fire, the Arduino must not ignore repeated ON/OFF commands.

If you are unsure, check your Arduino sketch for logic that only allows a single trigger pulse per session, and update it to allow repeated pulsing.

If you need a sample Arduino code snippet for rapid-fire support, ask in the project issues or see the documentation.


This README contains quick setup steps and troubleshooting guidance, especially
for Windows users with AMD GPUs.

## Versioning (main)

- Single source of truth: `DB3K_VERSION.txt`
- Commit subject prefix for `main`: `db3kv<version> - <summary>` (see `COMMIT_NAMING_CONVENTION.md`)
- Home tab shows a versioned title and a "Recent Updates" list from `RECENT_UPDATES.json`

## Recommended install (safe)

1. Create and activate a virtual environment (recommended):

   PowerShell:

   ```powershell
   python -m venv .venv; .\.venv\Scripts\Activate.ps1
   ```

2. Install the pinned runtime dependencies:

   PowerShell:

   ```powershell
   pip install -r requirements-main.txt
   ```

3. (Optional) Install development tools or optional heavy packages:

   PowerShell:

   ```powershell
   pip install -r requirements-dev.txt
   pip install -r requirements-optional.txt  # only if you want torch/pygame etc.
   ```

## AMD GPUs on Windows — common issue and quick fix

If you have an AMD Radeon GPU on Windows, you may see errors like a PyTorch
DLL initialization failure (examples: `c10.dll` / `WinError 1114`). This is
usually because the prebuilt PyTorch wheel in your environment expects a
CUDA-enabled NVIDIA GPU or a different ABI.

Recommended approach (works for most users): install the CPU-only PyTorch
build and then ultralytics. This avoids GPU drivers and runs YOLO on CPU.

PowerShell commands:

```powershell
# CPU-only PyTorch wheels (official index for CPU builds)
pip install --index-url https://download.pytorch.org/whl/cpu torch torchvision torchaudio --upgrade
pip install --upgrade ultralytics
```

Or, if you use conda/Miniconda:

```powershell
conda install pytorch torchvision torchaudio cpuonly -c pytorch
pip install --upgrade ultralytics
```

After installing the CPU-only torch and ultralytics, restart the application.

If you *do* have a compatible NVIDIA CUDA setup and want to use GPU, set the
environment variable `TURRET_USE_GPU=1` before starting the app (PowerShell):

```powershell
setx TURRET_USE_GPU 1
# restart your shell/session after setx
```

Note: On Windows with AMD GPUs, GPU acceleration is usually not available.

## Quick runtime check

Run the small dependency checker included in the repository:

```powershell
python .\scripts\check_dependencies.py
```

This prints which packages are present and offers targeted advice if it
detects a common DLL/init failure for PyTorch.

## Runtime modes

The application supports multiple detection modes. If YOLO is not available
or you prefer not to use it, switch to:

- `Frame Difference`
- `Background Subtraction`

These modes work without ultralytics/torch and are suitable for many use cases.

## Presets (minimal UI workflow)

Factory presets (from `app/turret_presets.py`) can be applied from two places:

- **Configuration & Connection dock** (COM/Connect/Tracking area): a **Factory Preset** dropdown is available for quick preset changes without opening the Behavior panel.
- **Tracking Behavior dock**: includes the full behavior/preset controls.

Implementation note for future editors: when launching via `run.py`, the Connection-panel dropdown is created in `app/MAIN_FILE_SINGLE_CAM.py` as `connection_preset_combo` and it calls `apply_preset()`. (There is also a mirrored implementation in `app/ui_builder.py` for alternate UI build paths.)

## Next steps

- If you want me to force a CPU-only ultralytics import inside the app, or add
  an on-screen guidance dialog, say so and I will perform the change.
