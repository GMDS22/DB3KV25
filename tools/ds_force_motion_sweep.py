from __future__ import annotations

import argparse
import time

import serial  # type: ignore


def checksum(pkt_wo_chk: bytes) -> int:
    s = sum(pkt_wo_chk[2:]) & 0xFF
    return (0xFF ^ s) & 0xFF


def build_write_pos_packet(servo_id: int, pos: int, move_time_ms: int) -> bytes:
    params = bytes([
        0x2A,
        (pos >> 8) & 0xFF,
        pos & 0xFF,
        (move_time_ms >> 8) & 0xFF,
        move_time_ms & 0xFF,
    ])
    pkt_wo = bytes([0xFF, 0xFF, servo_id & 0xFF, 0x07, 0x03]) + params
    return pkt_wo + bytes([checksum(pkt_wo)])


def run_once(port: str, baud: int, ids: list[int], positions: list[int], move_time_ms: int, pause_s: float) -> None:
    print(f"\n[BAUD] {baud}")
    try:
        ser = serial.Serial(port=port, baudrate=baud, timeout=0.2, write_timeout=1.0)
    except Exception as e:
        print(f"[ERROR] open failed at {baud}: {e}")
        return

    try:
        for sid in ids:
            print(f"  [ID] {sid}")
            for pos in positions:
                pkt = build_write_pos_packet(sid, pos, move_time_ms)
                try:
                    ser.reset_input_buffer()
                except Exception:
                    pass
                ser.write(pkt)
                ser.flush()
                time.sleep(0.08)
                rx = ser.read(64)
                print(f"    TX pos={pos:4d} time={move_time_ms:4d}ms | RX={len(rx)} bytes")
                time.sleep(pause_s)
    finally:
        try:
            ser.close()
        except Exception:
            pass


def main() -> int:
    ap = argparse.ArgumentParser(description="Force DS bus movement sweep across IDs/bauds")
    ap.add_argument("--port", required=True)
    ap.add_argument("--ids", default="1,2,3,4,5,6")
    ap.add_argument("--bauds", default="115200,57600,1000000,38400")
    ap.add_argument("--positions", default="512,3584,2048")
    ap.add_argument("--move-time", type=int, default=500)
    ap.add_argument("--pause", type=float, default=0.8)
    args = ap.parse_args()

    ids = [int(x.strip()) for x in args.ids.split(",") if x.strip()]
    bauds = [int(x.strip()) for x in args.bauds.split(",") if x.strip()]
    positions = [int(x.strip()) for x in args.positions.split(",") if x.strip()]

    print(f"[INFO] port={args.port} ids={ids} bauds={bauds} positions={positions}")
    for b in bauds:
        run_once(args.port, b, ids, positions, int(args.move_time), float(args.pause))

    print("\n[DONE] Sent force movement sweep.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
