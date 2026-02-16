import argparse
import json
import socket
import threading
import time
import zlib
from typing import Any, Dict, Optional

try:
    import serial  # type: ignore
except Exception as exc:
    raise SystemExit(f"pyserial is required: {exc}")


def _compact_json(obj: Dict[str, Any]) -> bytes:
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def encode_with_crc(msg: Dict[str, Any]) -> bytes:
    payload = dict(msg)
    payload.pop("crc", None)
    raw = _compact_json(payload)
    payload["crc"] = f"{(zlib.crc32(raw) & 0xFFFFFFFF):08x}"
    return _compact_json(payload)


def try_decode_with_crc(data: bytes) -> Optional[Dict[str, Any]]:
    try:
        msg = json.loads(data.decode("utf-8", errors="strict"))
    except Exception:
        return None
    if not isinstance(msg, dict) or "crc" not in msg:
        return None
    payload = dict(msg)
    recv_crc = str(payload.pop("crc", "")).lower()
    calc = f"{(zlib.crc32(_compact_json(payload)) & 0xFFFFFFFF):08x}"
    if recv_crc != calc:
        return None
    return msg


def load_settings(path: str) -> Dict[str, Any]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f) or {}
    except Exception:
        return {}


def serial_reader(ser: serial.Serial, stop_evt: threading.Event, lines: list[str]) -> None:
    while not stop_evt.is_set():
        try:
            line = ser.readline().decode("utf-8", errors="replace").rstrip("\r\n")
        except Exception:
            line = ""
        if line:
            ts = time.strftime("%H:%M:%S")
            msg = f"[{ts}] {line}"
            lines.append(msg)
            print(f"[ESP32] {msg}")


def wait_for_serial(lines: list[str], markers: list[str], timeout_s: float) -> bool:
    deadline = time.time() + float(timeout_s)
    while time.time() < deadline:
        # scan from the end (recent lines) for speed
        tail = lines[-200:]
        for line in reversed(tail):
            if any(m in line for m in markers):
                return True
        time.sleep(0.05)
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Current setup diagnostic: ESP32 serial logs + UDP bus_ping")
    ap.add_argument("--com", default="COM8")
    ap.add_argument("--baud", type=int, default=115200)
    ap.add_argument("--settings", default="settings.json")
    ap.add_argument("--host", default=None)
    ap.add_argument("--port", type=int, default=None)
    ap.add_argument("--local-port", type=int, default=None)
    ap.add_argument("--listen-seconds", type=float, default=6.0)
    ap.add_argument("--wait-boot-seconds", type=float, default=8.0, help="Wait for ESP32 boot/UDP-ready on serial before sending UDP")
    ap.add_argument("--send-move", action="store_true", help="Send a slow/visible pan/tilt move command")
    ap.add_argument("--pan", type=int, default=130)
    ap.add_argument("--tilt", type=int, default=60)
    ap.add_argument("--move-time-ms", type=int, default=1200)
    args = ap.parse_args()

    settings = load_settings(args.settings)
    host = args.host or settings.get("esp32_host") or "192.168.4.1"
    port = int(args.port or settings.get("esp32_port") or 9000)
    local_port = int(args.local_port if args.local_port is not None else (settings.get("esp32_local_port") or 0))

    print(f"[CFG] COM={args.com}@{args.baud} target={host}:{port} local_port={local_port}")

    # Open serial monitor to ESP32 logs
    ser = serial.Serial(args.com, args.baud, timeout=0.15)
    stop_evt = threading.Event()
    lines: list[str] = []
    t = threading.Thread(target=serial_reader, args=(ser, stop_evt, lines), daemon=True)
    t.start()

    # Wait for boot completion / UDP listener before sending UDP packets.
    # This avoids the common "0 replies" case caused by flashing/rebooting.
    boot_ok = wait_for_serial(
        lines,
        markers=["UDP port 9000 ready", "BOOT COMPLETE", "Waiting for app"],
        timeout_s=float(args.wait_boot_seconds),
    )
    print(f"[BOOTWAIT] udp_ready={boot_ok}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setblocking(False)
    sock.bind(("0.0.0.0", local_port))

    seq = 1
    def send(msg: Dict[str, Any]) -> int:
        nonlocal seq
        seq += 1
        msg = dict(msg)
        msg["seq"] = seq
        msg.setdefault("ts", int(time.time() * 1000.0))
        msg.setdefault("v", 1)
        sock.sendto(encode_with_crc(msg), (str(host), int(port)))
        return seq

    # Send diagnostic packets
    sq_hello = send({"t": "hello", "p": {"role": "pc-diag", "want": ["ack", "state", "caps"]}})
    sq_hb = send({"t": "hb", "p": {}})
    sq_enc = send({"t": "cmd", "p": {"action": "encoder_request"}})
    sq_bus = send({"t": "cmd", "p": {"action": "bus_ping"}})
    sq_move = None
    if args.send_move:
        mt = int(max(0, min(5000, int(args.move_time_ms))))
        sq_move = send(
            {
                "t": "cmd",
                "p": {
                    "pan_cmd": int(args.pan),
                    "tilt_cmd": int(args.tilt),
                    "move_time_ms": mt,
                },
            }
        )
    print(
        f"[TX] hello={sq_hello} hb={sq_hb} encoder_request={sq_enc} bus_ping={sq_bus}"
        + (f" move={sq_move} pan={args.pan} tilt={args.tilt} mt={args.move_time_ms}" if sq_move else "")
    )

    acks: list[dict] = []
    states = 0
    caps = 0

    deadline = time.time() + float(args.listen_seconds)
    while time.time() < deadline:
        try:
            data, _addr = sock.recvfrom(8192)
        except BlockingIOError:
            time.sleep(0.01)
            continue
        msg = try_decode_with_crc(data)
        if not msg:
            continue
        mtype = msg.get("t")
        if mtype == "ack":
            acks.append(msg)
        elif mtype == "state":
            states += 1
        elif mtype == "cap":
            caps += 1

    def find_ack(seq_id: int) -> Optional[dict]:
        for m in acks:
            if int(m.get("seq", 0) or 0) == int(seq_id):
                return m
        return None

    ack_bus = find_ack(sq_bus)
    diag = {}
    if ack_bus:
        diag = ((ack_bus.get("p") or {}).get("bus") or {})

    stop_evt.set()
    time.sleep(0.1)
    try:
        ser.close()
    except Exception:
        pass
    try:
        sock.close()
    except Exception:
        pass

    print("\n=== SUMMARY ===")
    print(f"ack_count={len(acks)} state_count={states} cap_count={caps}")
    print(f"bus_ping_ack={'yes' if ack_bus else 'no'} diag={diag}")
    if sq_move is not None:
        ack_move = find_ack(sq_move)
        ok_move = None
        if ack_move is not None:
            ok_move = bool(ack_move.get("ok", False))
        print(f"move_ack={'yes' if ack_move else 'no'} ok={ok_move}")

    # Heuristic conclusions
    if not ack_bus:
        print("[RESULT] No bus_ping ACK.")
        print("         If you just flashed/rebooted: increase --wait-boot-seconds and retry.")
        print("         Otherwise: verify WiFi route is 192.168.4.x to DB3000-ESP32.")
        return 2

    pan_ok = bool(diag.get("pan_ok", False))
    tilt_ok = bool(diag.get("tilt_ok", False))
    rx_pan = int(diag.get("rx_pan", 0) or 0)
    rx_tilt = int(diag.get("rx_tilt", 0) or 0)
    baud = diag.get("baud")
    mode = diag.get("chk_mode")

    if pan_ok or tilt_ok:
        print(f"[RESULT] Bus replies detected (pan_ok={pan_ok}, tilt_ok={tilt_ok}, baud={baud}, chk_mode={mode}).")
        return 0

    if rx_pan == 0 and rx_tilt == 0:
        print(f"[RESULT] Zero RX bytes from bus devices (baud={baud}, chk_mode={mode}).")
        print("         Likely wiring/return-line/power/device-ID issue, not UDP/app issue.")
        return 3

    print(f"[RESULT] RX bytes seen but no valid servo packet (baud={baud}, chk_mode={mode}).")
    print("         Likely protocol/line-level mismatch.")
    return 4


if __name__ == "__main__":
    raise SystemExit(main())
