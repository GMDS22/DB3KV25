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

## Serial Bus Servo Upgrade (2026): Current Telemetry

If your Arduino/MCU firmware emits current telemetry lines, the app will parse and display them in the **Current Monitor** dock.

- **Expected telemetry (MCU → Host):** `CUR PmA=<pan_mA> TmA=<tilt_mA> TOTmA=<total_mA>`
- **Units:** milliamps (mA)
- **UI:** Pan/Tilt/Total show “—” until telemetry is received

## Serial connection modes (Nano vs Debug Board vs Dual Port)

The app supports three serial modes (UI: **Configuration & Connection → Serial Device**). These control which COM port(s) are used and which features are available.

| Mode | What it connects to | COM ports | PAN/TILT | IO (fire/relays/safety) | Notes |
| --- | --- | --- | --- | --- | --- |
| Arduino/Nano (DB3000 ASCII) | Arduino Nano | 1 (primary) | via Nano | ✅ | Host sends packed ASCII `P..T..F..L..R..G..S..M..` |
| Debug Board (Bus Servo Direct) | Debug Board | 1 (Debug Board COM) | ✅ direct | ❌ | Bus packets are binary; no Nano IO in this mode |
| Dual Port (Nano IO + Debug Board Pan/Tilt) | Nano + Debug Board | 2 (primary + Debug Board COM) | ✅ direct | ✅ | Recommended when Debug Board is connected directly to PC (no daisy-chain needed) |

**Typical Windows mapping (your setup):**

- Nano: **COM8** (IO + telemetry)
- Debug Board: **COM9** (bus-servo PAN/TILT)

**Quick sanity tests (no camera required):**

- `python test_nano_io.py` (checks COM8 IO)
- `python test_bus_servo_read.py COM9` (checks COM9 bus-servo comms)

## Presets (minimal UI workflow)

Factory presets (from `app/turret_presets.py`) can be applied from two places:

- **Configuration & Connection dock** (COM/Connect/Tracking area): a **Factory Preset** dropdown is available for quick preset changes without opening the Behavior panel.
- **Tracking Behavior dock**: includes the full behavior/preset controls.

Implementation note for future editors: when launching via `run.py`, the Connection-panel dropdown is created in `app/MAIN_FILE_SINGLE_CAM.py` as `connection_preset_combo` and it calls `apply_preset()`. (There is also a mirrored implementation in `app/ui_builder.py` for alternate UI build paths.)

## Detection Pause Feature (Tracking Behavior)

The **Detection Pause** slider (Tracking Behavior panel, right dock) pauses detection updates when a target enters the big scope circle. This prevents detection jitter from moving the target away during final aiming approach.

**Key Behaviors:**
- **Trigger:** Target enters scope circle (edge detection)
- **Effect:** Detection updates pause for configured duration (0-2000ms, default 1000ms)
- **Video:** Continues playing normally (NOT frozen)
- **Servos:** Continue aiming to last known target position
- **Use Case:** Allows precise convergence before firing, eliminates oscillation

**UI Location:**
```
Tracking Behavior Panel (Right Dock)
├── Tracking Speed
├── Deadzone
├── Detection Pause (ms) ◄── HERE (slider 0-2000ms)
├── Trigger Cooldown
└── ... other settings
```

**Settings Persistence:** Saved to `settings.json` as `"detection_pause_ms": 1000`

See `DETECTION_PAUSE_UI_LOCATION.md` for detailed usage guide and troubleshooting.

## Next steps

- If you want me to force a CPU-only ultralytics import inside the app, or add
  an on-screen guidance dialog, say so and I will perform the change.
