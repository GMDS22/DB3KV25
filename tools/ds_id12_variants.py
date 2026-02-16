from __future__ import annotations

import argparse
import time

import serial  # type: ignore


def chk_xor(pkt_wo_chk: bytes) -> int:
    return (0xFF ^ (sum(pkt_wo_chk[2:]) & 0xFF)) & 0xFF


def chk_sub(pkt_wo_chk: bytes) -> int:
    return (0xFF - (sum(pkt_wo_chk[2:]) & 0xFF)) & 0xFF


def build_write_pkt(servo_id: int, pos: int, move_ms: int, *, checksum_mode: str, byte_order: str) -> bytes:
    pos_h = (pos >> 8) & 0xFF
    pos_l = pos & 0xFF
    t_h = (move_ms >> 8) & 0xFF
    t_l = move_ms & 0xFF

    if byte_order == "HL":
        params = bytes([0x2A, pos_h, pos_l, t_h, t_l])
    else:  # LH
        params = bytes([0x2A, pos_l, pos_h, t_l, t_h])

    pkt_wo = bytes([0xFF, 0xFF, servo_id & 0xFF, 0x07, 0x03]) + params
    chk = chk_xor(pkt_wo) if checksum_mode == "xor" else chk_sub(pkt_wo)
    return pkt_wo + bytes([chk])


def hexd(b: bytes) -> str:
    return " ".join(f"{x:02X}" for x in b)


def read_rx(ser: serial.Serial, wait_s: float = 0.12) -> bytes:
    time.sleep(wait_s)
    out = bytearray()
    while True:
        chunk = ser.read(256)
        if not chunk:
            break
        out.extend(chunk)
        time.sleep(0.01)
    return bytes(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="ID 1/2 only movement variant test")
    ap.add_argument("--port", default="COM9")
    ap.add_argument("--baud", type=int, default=1000000)
    ap.add_argument("--move-time", type=int, default=1800)
    ap.add_argument("--pause", type=float, default=1.8)
    args = ap.parse_args()

    variants = [
        ("xor", "HL"),
        ("xor", "LH"),
        ("sub", "HL"),
        ("sub", "LH"),
    ]
    # Very obvious moves
    positions = [128, 3968, 2048]
    ids = [1, 2]

    print(f"[INFO] port={args.port} baud={args.baud} ids={ids} positions={positions} move_time={args.move_time}ms")
    ser = serial.Serial(args.port, args.baud, timeout=0.15, write_timeout=1.0)
    try:
        for chk, order in variants:
            print(f"\n=== Variant checksum={chk} order={order} ===")
            for sid in ids:
                print(f"[ID {sid}]")
                for pos in positions:
                    pkt = build_write_pkt(sid, pos, int(args.move_time), checksum_mode=chk, byte_order=order)
                    try:
                        ser.reset_input_buffer()
                    except Exception:
                        pass
                    ser.write(pkt)
                    ser.flush()
                    rx = read_rx(ser)
                    print(f"  TX pos={pos:4d} RX({len(rx)}): {hexd(rx) if rx else '-'}")
                    time.sleep(float(args.pause))

        print("\n[DONE] ID1/ID2 variant sweep complete.")
        return 0
    finally:
        try:
            ser.close()
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
