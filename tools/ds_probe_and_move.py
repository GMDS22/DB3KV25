from __future__ import annotations

import argparse
import time
from collections import defaultdict

import serial  # type: ignore


def chk_xor(pkt_wo_chk: bytes) -> int:
    return (0xFF ^ (sum(pkt_wo_chk[2:]) & 0xFF)) & 0xFF


def chk_sub(pkt_wo_chk: bytes) -> int:
    return (0xFF - (sum(pkt_wo_chk[2:]) & 0xFF)) & 0xFF


def build_ping(servo_id: int, mode: str) -> bytes:
    pkt_wo = bytes([0xFF, 0xFF, servo_id & 0xFF, 0x02, 0x01])
    chk = chk_xor(pkt_wo) if mode == "xor" else chk_sub(pkt_wo)
    return pkt_wo + bytes([chk])


def build_write_pos(servo_id: int, pos: int, move_ms: int, mode: str) -> bytes:
    params = bytes([0x2A, (pos >> 8) & 0xFF, pos & 0xFF, (move_ms >> 8) & 0xFF, move_ms & 0xFF])
    pkt_wo = bytes([0xFF, 0xFF, servo_id & 0xFF, 0x07, 0x03]) + params
    chk = chk_xor(pkt_wo) if mode == "xor" else chk_sub(pkt_wo)
    return pkt_wo + bytes([chk])


def hexd(b: bytes) -> str:
    return " ".join(f"{x:02X}" for x in b)


def read_rx(ser: serial.Serial, wait_s: float = 0.15) -> bytes:
    time.sleep(wait_s)
    out = bytearray()
    while True:
        chunk = ser.read(256)
        if not chunk:
            break
        out.extend(chunk)
        time.sleep(0.01)
    return bytes(out)


def seems_valid_reply(rx: bytes, sid: int) -> bool:
    if len(rx) < 6:
        return False
    # Look for FF FF <sid>
    for i in range(0, len(rx) - 2):
        if rx[i] == 0xFF and rx[i + 1] == 0xFF and rx[i + 2] == (sid & 0xFF):
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Probe DS bus IDs and force movement packets")
    ap.add_argument("--port", required=True)
    ap.add_argument("--baud", type=int, default=1000000)
    ap.add_argument("--id-start", type=int, default=1)
    ap.add_argument("--id-end", type=int, default=20)
    ap.add_argument("--move-time", type=int, default=1200)
    ap.add_argument("--wait", type=float, default=0.12)
    args = ap.parse_args()

    print(f"[INFO] port={args.port} baud={args.baud} ids={args.id_start}..{args.id_end}")

    ser = serial.Serial(args.port, args.baud, timeout=0.1, write_timeout=1.0)
    score = defaultdict(int)
    valid_hits = []

    try:
        for sid in range(args.id_start, args.id_end + 1):
            print(f"\n[ID {sid}]-----------------")
            for mode in ("xor", "sub"):
                # Ping
                try:
                    ser.reset_input_buffer()
                except Exception:
                    pass
                pkt = build_ping(sid, mode)
                ser.write(pkt)
                ser.flush()
                rx = read_rx(ser, wait_s=args.wait)
                if rx:
                    score[sid] += len(rx)
                    print(f"  ping {mode}: RX({len(rx)}): {hexd(rx)}")
                    if seems_valid_reply(rx, sid):
                        valid_hits.append((sid, "ping", mode, rx))

                # Big write move low->high around center
                for pos in (256, 3840, 2048):
                    try:
                        ser.reset_input_buffer()
                    except Exception:
                        pass
                    pkt2 = build_write_pos(sid, pos, int(args.move_time), mode)
                    ser.write(pkt2)
                    ser.flush()
                    rx2 = read_rx(ser, wait_s=args.wait)
                    if rx2:
                        score[sid] += len(rx2)
                        print(f"  wr {mode} pos={pos}: RX({len(rx2)}): {hexd(rx2)}")
                        if seems_valid_reply(rx2, sid):
                            valid_hits.append((sid, f"wr{pos}", mode, rx2))
                    time.sleep(0.18)

        print("\n=== SUMMARY ===")
        if score:
            ranked = sorted(score.items(), key=lambda kv: kv[1], reverse=True)
            print("Top IDs by RX bytes:", ranked[:10])
        else:
            print("No RX bytes captured from any ID.")

        if valid_hits:
            print("Potential valid servo replies detected:")
            for sid, kind, mode, rx in valid_hits[:20]:
                print(f"  ID={sid} {kind} {mode} RX={hexd(rx)}")
        else:
            print("No FF FF <ID> style valid replies detected.")

        return 0
    finally:
        try:
            ser.close()
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
