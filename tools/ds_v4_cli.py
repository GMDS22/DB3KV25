"""DS_v4 serial-bus servo quick CLI.

Use this to sanity-check the Yahboom/DS_v4 debug board + servo wiring without the vendor GUI.

Examples:
  python tools/ds_v4_cli.py --port COM5 ping --id 1
  python tools/ds_v4_cli.py --port COM5 set-id --new-id 1
  python tools/ds_v4_cli.py --port COM5 set-id --new-id 2
  python tools/ds_v4_cli.py --port COM5 write-pos --id 1 --pos 2048 --time 100

Protocol (recovered from vendor tool):
  Header: FF FF
  Checksum: 0xFF ^ (sum(bytes[2..N-3]) & 0xFF)

Notes:
- The debug board is expected to be full-duplex UART (TX/RX), typically 115200 8N1.
- Some servos/debug boards may not respond to ping; this tool prints any bytes received.
"""

from __future__ import annotations

import argparse
import sys
import time

try:
    import serial  # type: ignore
except Exception as exc:  # pragma: no cover
    raise SystemExit(
        "pyserial is required. Install with: pip install pyserial\n"
        f"Import error: {exc}"
    )


def _checksum(pkt_wo_chk: bytes) -> int:
    """Compute DS_v4 checksum.

    pkt_wo_chk must include the full packet from header through last parameter, excluding checksum.
    """
    if len(pkt_wo_chk) < 4:
        raise ValueError("packet too short")

    # Sum from byte index 2 up to (N-1)-1 = N-2 (exclusive of checksum).
    # When called with pkt_wo_chk (no checksum), last included byte is N-1.
    s = sum(pkt_wo_chk[2:]) & 0xFF
    return (0xFF ^ s) & 0xFF


def build_packet(servo_id: int, length: int, instruction: int, params: bytes) -> bytes:
    if not (0 <= servo_id <= 0xFE):
        raise ValueError("servo_id must be 0..254")
    if not (0 <= length <= 0xFF):
        raise ValueError("length must fit byte")

    pkt_wo_chk = bytes([0xFF, 0xFF, servo_id, length, instruction]) + params
    chk = _checksum(pkt_wo_chk)
    return pkt_wo_chk + bytes([chk])


def hexdump(b: bytes) -> str:
    return " ".join(f"{x:02X}" for x in b)


def open_port(port: str, baud: int) -> serial.Serial:
    # Low timeout so we don't block forever.
    return serial.Serial(port=port, baudrate=baud, bytesize=8, parity="N", stopbits=1, timeout=0.2)


def txrx(port: serial.Serial, payload: bytes, rx_wait_s: float = 0.25) -> bytes:
    port.reset_input_buffer()
    port.write(payload)
    port.flush()

    # Give the servo time to answer.
    time.sleep(rx_wait_s)

    out = bytearray()
    while True:
        chunk = port.read(256)
        if not chunk:
            break
        out += chunk
        # small extra wait in case response is split
        time.sleep(0.02)
    return bytes(out)


def cmd_ping(args: argparse.Namespace) -> int:
    pkt = build_packet(args.id, length=2, instruction=1, params=b"")
    print(f"TX: {hexdump(pkt)}")
    with open_port(args.port, args.baud) as ser:
        rx = txrx(ser, pkt)
    print(f"RX({len(rx)}): {hexdump(rx)}")
    return 0


def cmd_set_id(args: argparse.Namespace) -> int:
    # Vendor tool uses broadcast ID 0xFE for set-id.
    new_id = args.new_id
    if not (0 <= new_id <= 0xFD):
        raise SystemExit("new-id must be 0..253")

    pkt = build_packet(0xFE, length=4, instruction=3, params=bytes([0x05, new_id]))
    print(f"TX: {hexdump(pkt)}")
    with open_port(args.port, args.baud) as ser:
        rx = txrx(ser, pkt)
    print(f"RX({len(rx)}): {hexdump(rx)}")
    print("If multiple servos were connected, they may ALL have taken the new ID.")
    return 0


def cmd_write_pos(args: argparse.Namespace) -> int:
    pos = args.pos
    t = args.time
    if not (0 <= pos <= 4095):
        raise SystemExit("pos must be 0..4095")
    if not (0 <= t <= 65535):
        raise SystemExit("time must be 0..65535")

    # Write position: instruction=0x03, address=0x2A, params: posH posL timeH timeL
    params = bytes(
        [
            0x2A,
            (pos >> 8) & 0xFF,
            pos & 0xFF,
            (t >> 8) & 0xFF,
            t & 0xFF,
        ]
    )
    pkt = build_packet(args.id, length=7, instruction=3, params=params)
    print(f"TX: {hexdump(pkt)}")
    with open_port(args.port, args.baud) as ser:
        rx = txrx(ser, pkt)
    print(f"RX({len(rx)}): {hexdump(rx)}")
    return 0


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="DS_v4 servo CLI")
    p.add_argument("--port", required=True, help="Serial port, e.g. COM5")
    p.add_argument("--baud", type=int, default=115200)

    sub = p.add_subparsers(dest="cmd", required=True)

    ping = sub.add_parser("ping", help="Send ping packet")
    ping.add_argument("--id", type=int, default=1)
    ping.set_defaults(func=cmd_ping)

    set_id = sub.add_parser("set-id", help="Broadcast set ID (connect ONE servo!)")
    set_id.add_argument("--new-id", type=int, required=True)
    set_id.set_defaults(func=cmd_set_id)

    write_pos = sub.add_parser("write-pos", help="Write target position")
    write_pos.add_argument("--id", type=int, default=1)
    write_pos.add_argument("--pos", type=int, required=True, help="0..4095 (2048=center)")
    write_pos.add_argument("--time", type=int, default=100, help="ms")
    write_pos.set_defaults(func=cmd_write_pos)

    args = p.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
