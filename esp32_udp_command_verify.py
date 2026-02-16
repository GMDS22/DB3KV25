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


def recv_until(sock: socket.socket, *, deadline_s: float) -> list[Dict[str, Any]]:
    out: list[Dict[str, Any]] = []
    while time.time() < deadline_s:
        try:
            data, addr = sock.recvfrom(8192)
        except BlockingIOError:
            time.sleep(0.01)
            continue
        msg = try_decode_with_crc(data)
        if not msg:
            continue
        msg["_from"] = f"{addr[0]}:{addr[1]}"
        out.append(msg)
    return out


def pick_last_state(msgs: list[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    for m in reversed(msgs):
        if m.get("t") == "state" and isinstance(m.get("p"), dict):
            return m
        if m.get("t") == "ack" and isinstance(m.get("state"), dict):
            return {"t": "state", "p": m.get("state")}
    return None


def _print_bus_diag(state_payload: Dict[str, Any], *, prefix: str) -> None:
    bus = state_payload.get("bus")
    if not isinstance(bus, dict):
        return
    send_count = bus.get("send_count")
    baud = bus.get("baud")
    last_send_ms = bus.get("last_send_ms")
    last_sent_pan = bus.get("last_sent_pan")
    last_sent_tilt = bus.get("last_sent_tilt")
    chk_locked = bus.get("chk_locked")
    chk_mode = bus.get("chk_mode")
    move_time_override_ms = bus.get("move_time_override_ms")
    print(
        f"{prefix} bus: send_count={send_count} baud={baud} last_send_ms={last_send_ms} "
        f"last_sent_pan={last_sent_pan} last_sent_tilt={last_sent_tilt} chk={chk_mode} locked={chk_locked} "
        f"move_time_override_ms={move_time_override_ms}"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="ESP32 UDP command verification (ACK + state confirmation)")
    ap.add_argument("--settings", default="settings.json")
    ap.add_argument("--host", default=None)
    ap.add_argument("--port", type=int, default=None)
    ap.add_argument("--local-port", type=int, default=None)
    ap.add_argument("--timeout", type=float, default=2.0)
    ap.add_argument("--do-move", action="store_true", help="Actually send a pan/tilt command (small move)")
    ap.add_argument("--pan", type=int, default=None, help="Target pan_cmd (degrees). If omitted, uses current+5")
    ap.add_argument("--tilt", type=int, default=None, help="Target tilt_cmd (degrees). If omitted, uses current+3")
    ap.add_argument("--move-time-ms", type=int, default=900, help="Optional diagnostic move_time_ms override (slows motion for visibility)")
    ap.add_argument("--do-self-test", action="store_true", help="Send cmd(action=test). WARNING: triggers hardware test actions.")
    ap.add_argument("--bus-ping", action="store_true", help="Send cmd(action=bus_ping) to confirm UART2/bus servo responses (requires updated ESP32 firmware).")
    ap.add_argument("--config-bus-profile", choices=["yb_4095", "lx16a"], default=None, help="Send cmd(action=config) with bus.profile before other actions.")
    ap.add_argument("--config-bus-pan-id", type=int, default=None, help="Optional bus.pan_id override (1..253) via cmd(action=config)")
    ap.add_argument("--config-bus-tilt-id", type=int, default=None, help="Optional bus.tilt_id override (1..253) via cmd(action=config)")
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
            print("[NET] ⚠ Not on ESP32 AP subnet (192.168.4.x). Join ESP32 WiFi and retry.")
    except Exception as e:
        print(f"[NET] route probe failed: {e}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setblocking(False)
    sock.bind(("0.0.0.0", int(local_port)))

    seq = 1

    def send(msg: Dict[str, Any]) -> int:
        nonlocal seq
        if "seq" not in msg:
            seq = (seq + 1) & 0x7FFFFFFF
            if seq == 0:
                seq = 1
            msg["seq"] = seq
        msg.setdefault("ts", int(time.time() * 1000.0))
        msg.setdefault("v", 1)
        data = encode_with_crc(msg)
        sock.sendto(data, (str(host), int(port)))
        return int(msg["seq"])

    # 1) HELLO
    hello_seq = send({"t": "hello", "p": {"role": "pc-verify", "want": ["state", "caps", "ack"]}})
    print(f"[TX] hello seq={hello_seq}")

    # 2) heartbeat
    hb_seq = send({"t": "hb", "p": {}})
    print(f"[TX] hb seq={hb_seq}")

    msgs = recv_until(sock, deadline_s=time.time() + float(args.timeout))
    print(f"[RX] {len(msgs)} msgs")

    state0 = pick_last_state(msgs)
    if state0 and isinstance(state0.get("p"), dict):
        p = state0["p"]
        print(f"[STATE0] pan={p.get('pan')} tilt={p.get('tilt')} safety={p.get('safety')} mode={p.get('mode')} current_fault={p.get('current_fault')}")
        _print_bus_diag(p, prefix="[STATE0]")
    else:
        print("[STATE0] none")

    # Always send encoder_request once (safe) so we can confirm command ACK path.
    enc_seq = send({"t": "cmd", "p": {"action": "encoder_request"}})
    print(f"[TX] cmd(action=encoder_request) seq={enc_seq}")

    cfg_seq = None
    bus_cfg: Dict[str, Any] = {}
    if args.config_bus_profile:
        bus_cfg["profile"] = str(args.config_bus_profile)
    if args.config_bus_pan_id is not None:
        bus_cfg["pan_id"] = int(max(1, min(253, int(args.config_bus_pan_id))))
    if args.config_bus_tilt_id is not None:
        bus_cfg["tilt_id"] = int(max(1, min(253, int(args.config_bus_tilt_id))))
    if bus_cfg:
        cfg_seq = send({"t": "cmd", "p": {"action": "config", "bus": bus_cfg}})
        print(f"[TX] cmd(action=config,bus={bus_cfg}) seq={cfg_seq}")

    bus_seq = None
    if args.bus_ping:
        bus_seq = send({"t": "cmd", "p": {"action": "bus_ping"}})
        print(f"[TX] cmd(action=bus_ping) seq={bus_seq}")

    if args.do_self_test:
        test_seq = send({"t": "cmd", "p": {"action": "test"}})
        print(f"[TX] cmd(action=test) seq={test_seq}  (WARNING: hardware self-test)")

    # Optional movement command.
    move_seq = None
    target_pan = None
    target_tilt = None
    if args.do_move:
        base_pan = None
        base_tilt = None
        if state0 and isinstance(state0.get("p"), dict):
            try:
                base_pan = int(state0["p"].get("pan"))
                base_tilt = int(state0["p"].get("tilt"))
            except Exception:
                base_pan = None
                base_tilt = None
        if args.pan is not None:
            target_pan = int(args.pan)
        elif base_pan is not None:
            target_pan = int(base_pan + 5)
        else:
            target_pan = 95

        if args.tilt is not None:
            target_tilt = int(args.tilt)
        elif base_tilt is not None:
            target_tilt = int(base_tilt + 3)
        else:
            target_tilt = 43

        move_payload = {
            "pan_cmd": int(target_pan),
            "tilt_cmd": int(target_tilt),
            "move_time_ms": int(max(0, min(5000, int(args.move_time_ms)))),
        }
        move_seq = send({"t": "cmd", "p": move_payload})
        print(
            f"[TX] move cmd seq={move_seq} pan_cmd={target_pan} tilt_cmd={target_tilt} "
            f"move_time_ms={move_payload['move_time_ms']}"
        )

    msgs2 = recv_until(sock, deadline_s=time.time() + float(args.timeout))
    print(f"[RX2] {len(msgs2)} msgs")

    all_msgs = msgs + msgs2
    acks = [m for m in all_msgs if m.get("t") == "ack"]
    caps = [m for m in all_msgs if m.get("t") == "cap"]
    states = [m for m in all_msgs if m.get("t") == "state"]

    def ack_ok_for(seq_id: int) -> Optional[bool]:
        for m in acks:
            if int(m.get("seq", 0) or 0) == int(seq_id):
                return bool(m.get("ok", False))
        return None

    def ack_for(seq_id: int) -> Optional[Dict[str, Any]]:
        for m in acks:
            if int(m.get("seq", 0) or 0) == int(seq_id):
                return m
        return None

    print(f"[SUMMARY] ack={len(acks)} state={len(states)} cap={len(caps)}")

    ok_hello = ack_ok_for(hello_seq)
    ok_enc = ack_ok_for(enc_seq)
    print(f"[ACK] hello={ok_hello} encoder_request={ok_enc}")

    if bus_seq is not None:
        ok_bus = ack_ok_for(bus_seq)
        ackm = ack_for(bus_seq) or {}
        diag = {}
        try:
            diag = (ackm.get("p") or {}).get("bus") or {}
        except Exception:
            diag = {}
        print(f"[ACK] bus_ping={ok_bus} diag={diag}")

    if cfg_seq is not None:
        ok_cfg = ack_ok_for(cfg_seq)
        ackm = ack_for(cfg_seq) or {}
        p = ackm.get("p") or {}
        print(f"[ACK] config={ok_cfg} p={p}")

    if args.do_move and move_seq is not None:
        ok_move = ack_ok_for(move_seq)
        print(f"[ACK] move={ok_move}")

        # Confirm last reported state matches the target if we got one.
        last_state = pick_last_state(all_msgs)
        if last_state and isinstance(last_state.get("p"), dict):
            p = last_state["p"]
            pan = p.get("pan")
            tilt = p.get("tilt")
            print(f"[STATE_LAST] pan={pan} tilt={tilt}")
            _print_bus_diag(p, prefix="[STATE_LAST]")
            if target_pan is not None and target_tilt is not None:
                if int(pan) == int(target_pan) and int(tilt) == int(target_tilt):
                    print("[OK] ESP32 state reflects the move command.")
                    return 0
                print("[WARN] ESP32 replied but state did not reflect the move target (may be clamped or ignored).")
                return 3

        print("[WARN] No state received after move.")
        return 4

    if (ok_hello is True or ok_enc is True) or states:
        print("[OK] ESP32 is communicating and acknowledging commands.")
        if not args.do_move:
            print("      Tip: run with --do-move to verify pan/tilt command acceptance.")
        return 0

    print("[FAIL] No ACK/STATE received. Check WiFi/subnet/host/port/firewall.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
