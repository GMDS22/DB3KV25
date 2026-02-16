import json
import socket
import time
import zlib

HOST = "192.168.4.1"
PORT = 9000


def encode(msg: dict) -> bytes:
    payload = dict(msg)
    payload.pop("crc", None)
    raw = json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    payload["crc"] = f"{(zlib.crc32(raw) & 0xFFFFFFFF):08x}"
    return json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def send(sock: socket.socket, seq: int, mtype: str, payload: dict) -> int:
    seq += 1
    msg = {"v": 1, "t": mtype, "seq": seq, "ts": int(time.time() * 1000.0), "p": payload}
    sock.sendto(encode(msg), (HOST, PORT))
    return seq


def read_brief(sock: socket.socket, timeout_s: float = 0.5) -> None:
    t0 = time.time()
    got = 0
    while (time.time() - t0) < timeout_s:
        try:
            data, _ = sock.recvfrom(4096)
            msg = json.loads(data.decode("utf-8"))
            t = msg.get("t")
            if t == "ack":
                print(f"  ACK seq={msg.get('seq')} ok={msg.get('ok')}")
                got += 1
            elif t == "state":
                p = msg.get("p", {}) or {}
                print(f"  STATE pan={p.get('pan')} tilt={p.get('tilt')}")
                got += 1
            elif t == "cap":
                got += 1
        except Exception:
            pass
    if got == 0:
        print("  (no replies in window)")


def set_profile(sock: socket.socket, seq: int, profile: str) -> int:
    print(f"PROFILE -> {profile}")
    seq = send(sock, seq, "hello", {"role": "pc", "want": ["state", "caps", "ack"]})
    time.sleep(0.12)
    seq = send(sock, seq, "cmd", {"action": "config", "bus": {"profile": profile}})
    read_brief(sock, 0.6)
    return seq


def move(sock: socket.socket, seq: int, pan: int, tilt: int, move_ms: int) -> int:
    print(f"MOVE -> pan={pan} tilt={tilt} t={move_ms}ms")
    seq = send(sock, seq, "cmd", {
        "pan_cmd": int(pan),
        "tilt_cmd": int(tilt),
        "move_time_ms": int(move_ms),
        "safety": 1,
        "mode": 0,
    })
    read_brief(sock, 0.8)
    return seq


def main() -> int:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 0))
    sock.settimeout(0.1)
    seq = 1

    print("===== LIVE A/B START =====")
    for cycle in range(1, 4):
        print(f"\n--- Cycle {cycle}: yb_4095 ---")
        seq = set_profile(sock, seq, "yb_4095")
        seq = move(sock, seq, 220, 70, 1800)
        time.sleep(0.7)
        seq = move(sock, seq, 0, 0, 1800)
        time.sleep(1.0)

        print(f"\n--- Cycle {cycle}: lx16a ---")
        seq = set_profile(sock, seq, "lx16a")
        seq = move(sock, seq, 220, 70, 1800)
        time.sleep(0.7)
        seq = move(sock, seq, 0, 0, 1800)
        time.sleep(1.0)

    print("\n===== LIVE A/B END =====")
    print("Reverting profile -> yb_4095")
    seq = set_profile(sock, seq, "yb_4095")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
