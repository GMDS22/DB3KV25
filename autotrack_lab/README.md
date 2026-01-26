# AutoTrack Lab (First-Lock / Quick Strike)

This is a standalone experimental autotracking app built to compare **serial-bus servos** vs PWM in terms of accuracy and stability. It does **not** reuse logic from the main app and is isolated in this folder.

## What’s different
- **First-Lock targeting**: the first detected object is locked and followed until it disappears.
- **Follow mode**: continuous tracking of the locked target.
- **Quick Strike mode**: only moves when the target has settled or when a predicted position is computed.
- **Hybrid tracking**: YOLO for detection + OpenCV tracker (CSRT/KCF/MOSSE) for smooth follow.
- **Dual Port ready**: Nano (COM8) handles IO/trigger; Debug Board (COM9) drives pan/tilt bus servos.

## Run
From the repo root:
```
python -m autotrack_lab.main
```

## Default ports
- Nano: COM8 (IO)
- Debug Board: COM9 (bus-servo pan/tilt)

## Presets
Pick from **Precision / Balanced / Fast**. Presets control:
- detection cadence
- aim gain & max step
- lead time and settle threshold
- bus move time

## Bus servo protocol
`serial_devices.py` uses a common SCS/STS-style packet:
```
FF FF ID LEN 03 ADDR POS_L POS_H TIME_L TIME_H SPEED_L SPEED_H CHK
```
If your servos use a different protocol or address map, adjust in [autotrack_lab/presets.py](autotrack_lab/presets.py) and [autotrack_lab/serial_devices.py](autotrack_lab/serial_devices.py).

## Files
- [autotrack_lab/main.py](autotrack_lab/main.py) — entry point
- [autotrack_lab/ui.py](autotrack_lab/ui.py) — UI
- [autotrack_lab/worker.py](autotrack_lab/worker.py) — camera + tracking loop
- [autotrack_lab/tracking.py](autotrack_lab/tracking.py) — detection + tracker helpers
- [autotrack_lab/serial_devices.py](autotrack_lab/serial_devices.py) — Nano + bus-servo IO
- [autotrack_lab/presets.py](autotrack_lab/presets.py) — presets and defaults
- [autotrack_lab/TRACKING_LAB_CHANGES.md](autotrack_lab/TRACKING_LAB_CHANGES.md) — change log
