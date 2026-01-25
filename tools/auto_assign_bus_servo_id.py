"""Automatically assign a DS_v4 serial-bus servo ID.

This is meant for the Yahboom YB-SD35M + debug/driver board setup.

SAFETY:
- CONNECT ONLY ONE SERVO while running this.
- Ensure the servo has proper external power (USB alone is usually not enough).
- Close the vendor servo software and any Serial Monitor first.

Examples:
  python tools/auto_assign_bus_servo_id.py --port COM5 --new-id 1 --confirm
  python tools/auto_assign_bus_servo_id.py --port COM5 --new-id 2 --confirm --verify

If you want it to use the DB3000 app’s saved COM/baud (usually Arduino COM, not the debug board):
  python tools/auto_assign_bus_servo_id.py --from-settings --new-id 1 --confirm

"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

try:
    import serial  # type: ignore
except Exception as exc:  # pragma: no cover
    raise SystemExit(
        "pyserial is required. Install with: pip install pyserial\n"
        f"Import error: {exc}"
    )


REPO_ROOT = Path(__file__).resolve().parent.parent
SETTINGS_JSON = REPO_ROOT / "settings.json"


def _checksum(pkt_wo_chk: bytes) -> int:
    # DS_v4 checksum recovered from vendor tool:
    # CHK = 0xFF ^ (sum(bytes[2..N-3]) & 0xFF)
    # When computing on pkt_wo_chk (without checksum), this becomes sum(bytes[2:]).
    s = sum(pkt_wo_chk[2:]) & 0xFF
    return (0xFF ^ s) & 0xFF


def build_packet(servo_id: int, length: int, instruction: int, params: bytes) -> bytes:
    pkt_wo_chk = bytes([0xFF, 0xFF, servo_id & 0xFF, length & 0xFF, instruction & 0xFF]) + params
    return pkt_wo_chk + bytes([_checksum(pkt_wo_chk)])


def hexdump(b: bytes) -> str:
    return " ".join(f"{x:02X}" for x in b)


def open_port(port: str, baud: int) -> serial.Serial:
    return serial.Serial(port=port, baudrate=baud, bytesize=8, parity="N", stopbits=1, timeout=0.25)


def txrx(port: serial.Serial, payload: bytes, rx_wait_s: float = 0.25) -> bytes:
    port.reset_input_buffer()
    port.write(payload)
    port.flush()
    time.sleep(rx_wait_s)

    out = bytearray()
    while True:
        chunk = port.read(256)
        if not chunk:
            break
        out += chunk
        time.sleep(0.02)
    return bytes(out)


def load_app_settings() -> dict:
    if not SETTINGS_JSON.exists():
        raise SystemExit(f"settings.json not found at: {SETTINGS_JSON}")
    try:
        return json.loads(SETTINGS_JSON.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"Failed to parse settings.json: {exc}")


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="Auto-assign DS_v4 bus servo ID")
    p.add_argument("--port", help="Serial port for the servo debug board (e.g., COM5)")
    p.add_argument("--baud", type=int, default=115200)
    p.add_argument("--new-id", type=int, required=True, help="New servo ID to assign (0..253). Common: pan=1, tilt=2")
    p.add_argument(
        "--from-settings",
        action="store_true",
        help="Use settings.json com_port/baud_rate instead of --port/--baud (WARNING: usually this is the Arduino COM, not the debug board)",
    )
    p.add_argument(
        "--confirm",
        action="store_true",
        help="Required safety flag: acknowledges that ONLY ONE SERVO is connected.",
    )
    p.add_argument(
        "--verify",
        action="store_true",
        help="After assignment, attempt a ping and a small move to confirm comms.",
    )

    args = p.parse_args(argv)

    if not args.confirm:
        raise SystemExit(
            "Refusing to run without --confirm.\n"
            "Connect ONLY ONE servo, power it properly, then re-run with --confirm."
        )

    new_id = int(args.new_id)
    if not (0 <= new_id <= 0xFD):
        raise SystemExit("new-id must be 0..253 (do not use 254)")

    port = args.port
    baud = int(args.baud)

    if args.from_settings:
        s = load_app_settings()
        port = str(s.get("com_port") or "").strip() or port
        baud = int(s.get("baud_rate") or baud)

    if not port:
        raise SystemExit("No port specified. Provide --port COMx (recommended) or use --from-settings.")

    print(f"Port: {port} @ {baud}")
    print(f"Assigning new servo ID: {new_id}")

    # Broadcast set-id: FF FF FE 04 03 05 <new_id> CHK
    pkt_set_id = build_packet(0xFE, length=4, instruction=3, params=bytes([0x05, new_id]))
    print(f"TX set-id: {hexdump(pkt_set_id)}")

    with open_port(port, baud) as ser:
        rx = txrx(ser, pkt_set_id)
        print(f"RX({len(rx)}): {hexdump(rx)}")

        if args.verify:
            # Ping: FF FF <id> 02 01 CHK
            pkt_ping = build_packet(new_id, length=2, instruction=1, params=b"")
            print(f"TX ping:   {hexdump(pkt_ping)}")
            rx2 = txrx(ser, pkt_ping)
            print(f"RX({len(rx2)}): {hexdump(rx2)}")

            # Small move (center): write pos @ 0x2A
            # FF FF ID 07 03 2A posH posL timeH timeL CHK
            pos = 2048
            move_ms = 200
            params = bytes([0x2A, (pos >> 8) & 0xFF, pos & 0xFF, (move_ms >> 8) & 0xFF, move_ms & 0xFF])
            pkt_move = build_packet(new_id, length=7, instruction=3, params=params)
            print(f"TX move:   {hexdump(pkt_move)}")
            rx3 = txrx(ser, pkt_move)
            print(f"RX({len(rx3)}): {hexdump(rx3)}")

    print("Done.")
    print("If nothing responded, common causes: servo not powered, wrong wiring/pin orientation, wrong COM/baud, or wrong board.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
