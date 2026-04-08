#!/usr/bin/env python3
"""
Smart Sentry v3 UDP bench test

Sends simple JSON payloads to the new Waveshare v3 bridge sketch without
touching the main Smart Sentry app path.
"""

from __future__ import annotations

import argparse
import json
import socket
import time
import zlib
from typing import Any, Dict


def _compact_json(payload: Dict[str, Any]) -> bytes:
    return json.dumps(payload, separators=(",", ":")).encode("utf-8")


def build_payload(args: argparse.Namespace) -> Dict[str, Any]:
    if args.action == "bus_ping":
        return {"action": "bus_ping"}
    if args.action == "sound":
        return {
            "action": "sound",
            "freq_hz": args.sound_freq_hz,
            "duration_ms": args.sound_duration_ms,
            "volume_pct": args.sound_volume_pct,
        }
    if args.action == "rc_mode":
        return {
            "action": "rc_mode",
            "mode": args.rc_mode,
            "control_source_mode": args.rc_mode,
        }
    if args.action == "rc_stub":
        return {
            "action": "rc_stub",
            "control_source_mode": args.rc_mode,
            "rc_link_active": int(args.rc_link_active),
            "rc_override_active": int(args.rc_override_active),
            "rc_failsafe_active": int(args.rc_failsafe_active),
            "rc_frame_age_ms": args.rc_frame_age_ms,
            "ch1_us": args.ch1_us,
            "ch2_us": args.ch2_us,
            "ch3_us": args.ch3_us,
            "ch4_us": args.ch4_us,
            "ch5_us": args.ch5_us,
            "ch6_us": args.ch6_us,
        }
    return {
        "pan_cmd": args.pan,
        "tilt_cmd": args.tilt,
        "move_time_ms": args.move_time_ms,
        "fire": int(args.fire),
        "safety": int(args.safety),
        "mode": int(args.mode),
        "led": int(args.led),
        "laser": int(args.laser),
        "acc": int(args.acc),
        "spare": int(args.spare),
        "trigger": {
            "rest_deg": args.trigger_rest_deg,
            "fire_deg": args.trigger_fire_deg,
            "pulse_ms": args.trigger_pulse_ms,
        },
    }


def build_wrapped_packet(args: argparse.Namespace) -> bytes:
    packet: Dict[str, Any] = {
        "v": 1,
        "t": args.packet_type,
        "seq": int(args.seq),
        "ts": int(time.time() * 1000),
    }
    if args.packet_type == "cmd":
        packet["p"] = build_payload(args)
    raw = _compact_json(packet)
    packet["crc"] = f"{(zlib.crc32(raw) & 0xFFFFFFFF):08x}"
    return _compact_json(packet)


def main() -> int:
    parser = argparse.ArgumentParser(description="Send bench commands to the Smart Sentry v3 Waveshare bridge")
    parser.add_argument("--host", default="192.168.4.1")
    parser.add_argument("--port", type=int, default=9000)
    parser.add_argument("--packet-type", choices=("cmd", "hello", "hb"), default="cmd")
    parser.add_argument("--pan", type=int, default=90)
    parser.add_argument("--tilt", type=int, default=35)
    parser.add_argument("--move-time-ms", type=int, default=120)
    parser.add_argument("--fire", action="store_true")
    parser.add_argument("--safety", type=int, choices=(0, 1), default=1)
    parser.add_argument("--mode", type=int, choices=(0, 1), default=0)
    parser.add_argument("--led", action="store_true")
    parser.add_argument("--laser", action="store_true")
    parser.add_argument("--acc", action="store_true")
    parser.add_argument("--spare", action="store_true")
    parser.add_argument("--trigger-rest-deg", type=int, default=0)
    parser.add_argument("--trigger-fire-deg", type=int, default=45)
    parser.add_argument("--trigger-pulse-ms", type=int, default=120)
    parser.add_argument("--sound-freq-hz", type=int, default=1200)
    parser.add_argument("--sound-duration-ms", type=int, default=60)
    parser.add_argument("--sound-volume-pct", type=int, default=100)
    parser.add_argument("--rc-mode", choices=("app", "rc", "auto"), default="app")
    parser.add_argument("--rc-link-active", action="store_true")
    parser.add_argument("--rc-override-active", action="store_true")
    parser.add_argument("--rc-failsafe-active", action="store_true")
    parser.add_argument("--rc-frame-age-ms", type=int, default=25)
    parser.add_argument("--ch1-us", type=int, default=1500)
    parser.add_argument("--ch2-us", type=int, default=1500)
    parser.add_argument("--ch3-us", type=int, default=1000)
    parser.add_argument("--ch4-us", type=int, default=1000)
    parser.add_argument("--ch5-us", type=int, default=1000)
    parser.add_argument("--ch6-us", type=int, default=1000)
    parser.add_argument("--seq", type=int, default=1)
    parser.add_argument("--action", choices=("bus_ping", "sound", "rc_mode", "rc_stub"), help="Send a command action instead of a motion payload")
    parser.add_argument("--raw", action="store_true", help="Send an unwrapped raw JSON payload instead of app-style cmd packet")
    parser.add_argument("--listen-ms", type=int, default=500, help="How long to wait for ack/state replies after sending")
    args = parser.parse_args()

    if args.raw:
        if args.packet_type != "cmd":
            raise SystemExit("--raw only supports cmd-style payloads")
        raw = _compact_json(build_payload(args))
    else:
        raw = build_wrapped_packet(args)

    print(f"Sending to {args.host}:{args.port}")
    print(raw.decode("utf-8"))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(max(0.05, args.listen_ms / 1000.0))
    try:
        sock.sendto(raw, (args.host, args.port))
        end_time = time.time() + max(0.0, args.listen_ms / 1000.0)
        while time.time() < end_time:
            try:
                data, addr = sock.recvfrom(2048)
            except socket.timeout:
                break
            print(f"Reply from {addr[0]}:{addr[1]} -> {data.decode('utf-8', errors='replace')}")
    finally:
        sock.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())