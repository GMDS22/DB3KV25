import argparse
import json
import socket
import time
import zlib
from typing import Any, Dict, Optional, Tuple


def _compact_json(obj: Dict[str, Any]) -> bytes:
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def encode_with_crc(msg: Dict[str, Any]) -> bytes:
    payload = dict(msg)
    payload.pop("crc", None)
    raw = _compact_json(payload)
    crc = zlib.crc32(raw) & 0xFFFFFFFF
    payload["crc"] = f"{crc:08x}"
    return _compact_json(payload)


def try_decode_with_crc(data: bytes) -> Optional[Dict[str, Any]]:
    try:
        msg = json.loads(data.decode("utf-8", errors="strict"))
    except Exception:
        return None
    if not isinstance(msg, dict):
        return None
    crc = msg.get("crc")
    if not crc:
        return None

    payload = dict(msg)
    payload.pop("crc", None)
    raw = _compact_json(payload)
    calc = f"{(zlib.crc32(raw) & 0xFFFFFFFF):08x}"
    if str(crc).lower() != calc:
        return None
    return msg


def load_settings(path: str) -> Dict[str, Any]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f) or {}
    except Exception:
        return {}


def local_route_ip(dest_host: str, dest_port: int) -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect((dest_host, int(dest_port)))
        return s.getsockname()[0]
    finally:
        try:
            s.close()
        except Exception:
            pass


def recv_loop(sock: socket.socket, *, deadline_s: float) -> Tuple[int, int, int]:
    """Receive packets until deadline. Returns (ack, state, cap) counts."""
    ack = state = cap = 0
    while time.time() < deadline_s:
        try:
            data, addr = sock.recvfrom(8192)
        except BlockingIOError:
            time.sleep(0.01)
            continue
        except Exception as e:
            print(f"[RX] socket error: {e}")
            break

        msg = try_decode_with_crc(data)
        if not msg:
            preview = data[:120]
            print(f"[RX] {len(data)} bytes from {addr} (bad crc/json) preview={preview!r}")
            continue

        t = msg.get("t")
        if t == "ack":
            ack += 1
        elif t == "state":
            state += 1
        elif t == "cap":
            cap += 1

        print(f"[RX] from {addr} type={t!r} keys={list(msg.keys())}")
        if t == "ack":
            ok = msg.get("ok")
            seq = msg.get("seq")
            print(f"      ack: ok={ok} seq={seq} state={msg.get('state', {})}")
        elif t in ("state", "cap"):
            print(f"      p={msg.get('p', {})}")

    return ack, state, cap


def main() -> int:
    ap = argparse.ArgumentParser(description="DB3000 ESP32 UDP link communication test")
    ap.add_argument("--settings", default="settings.json")
    ap.add_argument("--host", default=None)
    ap.add_argument("--port", type=int, default=None)
    ap.add_argument("--local-port", type=int, default=None)
    ap.add_argument("--timeout", type=float, default=2.5)
    ap.add_argument("--repeat", type=int, default=3)
    args = ap.parse_args()

    settings = load_settings(args.settings)
    host = args.host or settings.get("esp32_host") or "192.168.4.1"
    port = int(args.port or settings.get("esp32_port") or 9000)
    local_port = args.local_port
    if local_port is None:
        local_port = int(settings.get("esp32_local_port") or 0)

    if local_port != 0 and local_port < 1024:
        print(f"[WARN] local_port={local_port} is privileged; using 0")
        local_port = 0

    print(f"[CFG] target={host}:{port} local_port={local_port}")
    try:
        lip = local_route_ip(str(host), int(port))
        print(f"[NET] local route IP to {host}:{port} is {lip}")
        if str(host).startswith("192.168.4.") and not str(lip).startswith("192.168.4."):
            print("[NET] ⚠ Not on ESP32 AP subnet (192.168.4.x). Join ESP32 WiFi and try again.")
    except Exception as e:
        print(f"[NET] route probe failed: {e}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setblocking(False)
    sock.bind(("0.0.0.0", int(local_port)))

    seq = 1

    def send(msg: Dict[str, Any]) -> None:
        nonlocal seq
        if "seq" not in msg:
            seq = (seq + 1) & 0x7FFFFFFF
            if seq == 0:
                seq = 1
            msg["seq"] = seq
        if "ts" not in msg:
            msg["ts"] = int(time.time() * 1000.0)
        if "v" not in msg:
            msg["v"] = 1
        data = encode_with_crc(msg)
        sock.sendto(data, (str(host), int(port)))

    # 1) HELLO (expects ACK + CAP)
    print("[TX] hello")
    send({"t": "hello", "p": {"role": "pc-test", "want": ["state", "caps", "ack"]}})

    # 2) Heartbeat (ESP32 responds with STATE)
    print("[TX] hb")
    send({"t": "hb", "p": {}})

    # 3) Safe command that should ACK + STATE
    print("[TX] cmd(action=encoder_request)")
    send({"t": "cmd", "p": {"action": "encoder_request"}})

    deadline = time.time() + float(args.timeout)
    ack, state, cap = recv_loop(sock, deadline_s=deadline)

    # Retry a few times to handle WiFi wake / first packet loss.
    for i in range(max(0, int(args.repeat) - 1)):
        if ack or state or cap:
            break
        print(f"[RETRY] no replies yet ({i + 1}/{args.repeat - 1})")
        print("[TX] hello")
        send({"t": "hello", "p": {"role": "pc-test", "want": ["state", "caps", "ack"]}})
        print("[TX] hb")
        send({"t": "hb", "p": {}})
        print("[TX] cmd(action=encoder_request)")
        send({"t": "cmd", "p": {"action": "encoder_request"}})
        deadline = time.time() + float(args.timeout)
        a2, s2, c2 = recv_loop(sock, deadline_s=deadline)
        ack += a2
        state += s2
        cap += c2

    print(f"[RESULT] ack={ack} state={state} cap={cap}")
    if ack == 0 and state == 0 and cap == 0:
        print("[FAIL] No valid replies received. Likely causes:")
        print("  - PC not connected to ESP32 WiFi (DB3000-ESP32)")
        print("  - Wrong ESP32 IP/port")
        print("  - Windows Firewall blocking inbound UDP replies")
        print("  - ESP32 firmware not running / not listening")
        return 2

    print("[OK] ESP32 is replying to UDP.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
