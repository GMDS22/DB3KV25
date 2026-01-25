#!/usr/bin/env python3
"""Quick servo movement test over Nano USB serial.

This sends a few safe pan/tilt commands using the standard packed format:
  P{pan}T{tilt}F{fire}L{led}R{laser}G{acc}S{safety}M{mode}\n
Designed for verifying that:
- PC -> Nano serial is working (COM port)
- Nano -> bus servo debug board wiring is correct
- Bus servos respond (movement)

Example:
  python tools/servo_move_test_over_usb.py --port COM8 --confirm

Safety notes:
- Uses S1 (SAFE) and F0 (no firing)
- Uses small movements around home
"""

from __future__ import annotations

import argparse
import sys
import time

try:
    import serial  # type: ignore
except Exception as e:
    print(f"[ERROR] pyserial not available: {e}")
    print("Install dependencies with: pip install -r requirements.txt")
    raise


def build_cmd(*, pan: int, tilt: int, safety: int = 1, mode: int = 0) -> str:
    pan_i = int(pan)
    tilt_i = int(tilt)
    safety_i = 1 if int(safety) != 0 else 0
    mode_i = 1 if int(mode) != 0 else 0
    # Always keep firing OFF for this test.
    return f"P{pan_i}T{tilt_i}F0L0R0G0S{safety_i}M{mode_i}\n"


def read_lines(ser: serial.Serial, *, seconds: float = 0.25, max_lines: int = 50) -> list[str]:
    out: list[str] = []
    end = time.time() + float(seconds)
    while time.time() < end and len(out) < int(max_lines):
        try:
            if ser.in_waiting:
                line = ser.readline().decode("utf-8", errors="replace").strip()
                if line:
                    out.append(line)
            else:
                time.sleep(0.01)
        except Exception:
            break
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", required=True, help="COM port, e.g. COM8")
    ap.add_argument("--baud", type=int, default=115200, help="Baud rate (default: 115200)")
    ap.add_argument("--home-pan", type=int, default=90)
    ap.add_argument("--home-tilt", type=int, default=40)
    ap.add_argument("--pan-step", type=int, default=15, help="Degrees to nudge pan (nudge mode)")
    ap.add_argument("--tilt-step", type=int, default=8, help="Degrees to nudge tilt (nudge mode)")
    ap.add_argument("--pan-min", type=int, default=0, help="Pan minimum for sweep mode")
    ap.add_argument("--pan-max", type=int, default=220, help="Pan maximum for sweep mode")
    ap.add_argument("--tilt-min", type=int, default=0, help="Tilt minimum for sweep mode")
    ap.add_argument("--tilt-max", type=int, default=70, help="Tilt maximum for sweep mode")
    ap.add_argument(
        "--mode",
        choices=["nudge", "sweep"],
        default="nudge",
        help="nudge: small moves around home; sweep: go to min/max endpoints",
    )
    ap.add_argument(
        "--delay", type=float, default=0.8, help="Delay between moves (seconds)"
    )
    ap.add_argument(
        "--confirm",
        action="store_true",
        help="Actually send movement commands (otherwise prints what it would do)",
    )
    args = ap.parse_args()

    delay_s = max(0.05, float(args.delay))

    if args.mode == "sweep":
        sequence = [
            (args.home_pan, args.home_tilt, delay_s, "Home"),
            (args.pan_min, args.home_tilt, delay_s, "Pan MIN"),
            (args.pan_max, args.home_tilt, delay_s, "Pan MAX"),
            (args.pan_min, args.home_tilt, delay_s, "Pan MIN (return)"),
            (args.home_pan, args.home_tilt, delay_s, "Home"),
            (args.home_pan, args.tilt_min, delay_s, "Tilt MIN"),
            (args.home_pan, args.tilt_max, delay_s, "Tilt MAX"),
            (args.home_pan, args.tilt_min, delay_s, "Tilt MIN (return)"),
            (args.home_pan, args.home_tilt, delay_s, "Home"),
        ]
    else:
        sequence = [
            (args.home_pan, args.home_tilt, 0.6, "Home"),
            (args.home_pan + args.pan_step, args.home_tilt, 0.7, "Pan +"),
            (args.home_pan - args.pan_step, args.home_tilt, 0.7, "Pan -"),
            (args.home_pan, args.home_tilt + args.tilt_step, 0.7, "Tilt +"),
            (args.home_pan, args.home_tilt - args.tilt_step, 0.7, "Tilt -"),
            (args.home_pan, args.home_tilt, 0.7, "Back Home"),
        ]

    print(f"[INFO] Target port: {args.port} @ {args.baud}")
    if args.mode == "sweep":
        print(
            f"[INFO] Sweep endpoints: pan={args.pan_min}..{args.pan_max} tilt={args.tilt_min}..{args.tilt_max} (delay={delay_s:.2f}s)"
        )
    for pan, tilt, delay_s, label in sequence:
        cmd = build_cmd(pan=pan, tilt=tilt, safety=1, mode=0)
        print(f"[PLAN] {label}: {cmd.strip()} (wait {delay_s:.1f}s)")

    if not args.confirm:
        print("\n[DRY RUN] Re-run with --confirm to actually move the servos.")
        return 0

    try:
        ser = serial.Serial(
            port=args.port,
            baudrate=int(args.baud),
            timeout=0.2,
            write_timeout=1.0,
        )
    except Exception as e:
        print(f"[ERROR] Could not open {args.port}: {e}")
        return 2

    try:
        # Nano resets when serial opens; give it a moment.
        time.sleep(2.0)

        # Drain any startup banner.
        banner = read_lines(ser, seconds=0.8)
        if banner:
            print("[RX] Startup:")
            for line in banner[:10]:
                print(f"  {line}")

        for pan, tilt, delay_s, label in sequence:
            cmd = build_cmd(pan=pan, tilt=tilt, safety=1, mode=0)
            try:
                ser.write(cmd.encode("utf-8"))
                ser.flush()
                print(f"[TX] {label}: {cmd.strip()}")
            except Exception as e:
                print(f"[ERROR] Write failed: {e}")
                return 3

            # Read any immediate responses/telemetry.
            rx = read_lines(ser, seconds=0.25)
            for line in rx[:10]:
                print(f"[RX] {line}")

            time.sleep(float(delay_s))

        print("[OK] Movement sequence sent.")
        return 0
    finally:
        try:
            ser.close()
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
