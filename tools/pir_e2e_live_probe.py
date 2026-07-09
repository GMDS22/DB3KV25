from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.runtime_paths import runtime_root_path
from app.sentry_v2.sentry_v2_comm import SentryV2Comm
from app.sentry_v2.sentry_v2_config import SentryV2Config
from app.sentry_v2.sentry_v2_engine import SentryV2Engine


def _ts() -> float:
    return float(time.time())


def _write_jsonl(path: Path, record: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def _parse_transport_pir_line(message: str) -> Optional[Tuple[int, float]]:
    text = str(message or "").strip()
    if not text:
        return None

    m = re.search(r"PIR_EVENT\s+sensor_id=(\d+)\s+timestamp=(\d+)", text, re.IGNORECASE)
    if m:
        return int(m.group(1)), float(int(m.group(2)) / 1000.0)

    m = re.search(r"\[PIR\]\s*Sensor\s+(\d+)\s+triggered\b.*?\bt=(\d+)", text, re.IGNORECASE)
    if m:
        return int(m.group(1)), float(int(m.group(2)) / 1000.0)

    m = re.search(r"ESP32 UDP RX PIR S(\d+) ts=(\d+)", text, re.IGNORECASE)
    if m:
        # UDP trace logs S1/S2/S3 labels, convert to zero-based sensor id.
        return max(0, int(m.group(1)) - 1), float(int(m.group(2)) / 1000.0)

    return None


def _load_config() -> SentryV2Config:
    return SentryV2Config.load("app/config/smart_sentry_settings.json")


def _build_connection_attempts(config: SentryV2Config) -> List[Dict[str, Any]]:
    attempts: List[Dict[str, Any]] = []
    ports = SentryV2Comm.list_serial_ports()
    preferred_ports = [name for (name, desc) in ports if "USB-SERIAL" in str(desc or "").upper()]
    fallback_ports = [name for (name, _desc) in ports if name not in preferred_ports]
    serial_ports = preferred_ports + fallback_ports

    conn = config.connection
    udp_host = str(getattr(conn, "udp_host", "192.168.4.1") or "192.168.4.1")
    udp_port = int(getattr(conn, "udp_port", 9000) or 9000)

    if len(serial_ports) >= 2:
        a, b = serial_ports[0], serial_ports[1]
        attempts.append(
            {
                "label": f"dual_usb esp32={a} debug={b}",
                "mode": SentryV2Comm.MODE_DUAL_USB,
                "kwargs": {"esp32_port": a, "debug_port": b},
            }
        )
        attempts.append(
            {
                "label": f"dual_usb esp32={b} debug={a}",
                "mode": SentryV2Comm.MODE_DUAL_USB,
                "kwargs": {"esp32_port": b, "debug_port": a},
            }
        )

    for port in serial_ports:
        attempts.append(
            {
                "label": f"esp32_usb port={port}",
                "mode": SentryV2Comm.MODE_ESP32_USB,
                "kwargs": {"esp32_port": port},
            }
        )

    attempts.append(
        {
            "label": f"wifi_full {udp_host}:{udp_port}",
            "mode": SentryV2Comm.MODE_WIFI_FULL,
            "kwargs": {"udp_host": udp_host, "udp_port": udp_port},
        }
    )

    return attempts


def run_probe(duration_s: float, max_attempts: int) -> Dict[str, Any]:
    runtime_root = runtime_root_path()
    ts_token = time.strftime("%Y%m%d_%H%M%S")
    trace_path = runtime_root / "logs" / "pir_trace" / f"pir_e2e_probe_{ts_token}.jsonl"
    summary_path = runtime_root / "logs" / "pir_trace" / f"pir_e2e_probe_summary_{ts_token}.json"

    config = _load_config()
    engine = SentryV2Engine(config)
    engine.start()

    comm = SentryV2Comm()

    trace_events: List[Dict[str, Any]] = []
    transport_events: List[Dict[str, Any]] = []
    callback_events: List[Dict[str, Any]] = []
    engine_trace_events: List[Dict[str, Any]] = []
    moves: List[Dict[str, Any]] = []

    def emit(record: Dict[str, Any]) -> None:
        data = dict(record)
        data.setdefault("timestamp", _ts())
        trace_events.append(data)
        _write_jsonl(trace_path, data)

    def on_transport_log(message: str) -> None:
        now = _ts()
        parsed = _parse_transport_pir_line(message)
        rec = {
            "source": "transport",
            "action": "transport_log",
            "timestamp": now,
            "message": str(message or ""),
        }
        if parsed is not None:
            rec["action"] = "transport_pir_event"
            rec["sensor_id"] = int(parsed[0])
            rec["sensor_timestamp"] = float(parsed[1])
        transport_events.append(rec)
        emit(rec)

    def on_engine_pir_trace(payload: Dict[str, Any]) -> None:
        rec = dict(payload or {})
        rec["source"] = "engine"
        engine_trace_events.append(rec)
        emit(rec)

    def on_move(pan: float, tilt: float) -> None:
        rec = {
            "source": "engine",
            "action": "move_command",
            "timestamp": _ts(),
            "pan": float(pan),
            "tilt": float(tilt),
            "state": engine.get_state_name(),
        }
        moves.append(rec)
        emit(rec)

    def on_fire(burst_count: int) -> None:
        emit(
            {
                "source": "engine",
                "action": "fire_command",
                "timestamp": _ts(),
                "burst_count": int(burst_count),
                "state": engine.get_state_name(),
            }
        )

    def on_state_change(old, new) -> None:
        emit(
            {
                "source": "engine",
                "action": "state_change",
                "timestamp": _ts(),
                "old_state": str(getattr(old, "name", old)),
                "new_state": str(getattr(new, "name", new)),
            }
        )

    def on_pir(sensor_id: int, sensor_timestamp: float) -> None:
        receipt = _ts()
        rec = {
            "source": "callback",
            "action": "pir_callback_received",
            "timestamp": receipt,
            "sensor_id": int(sensor_id),
            "sensor_timestamp": float(sensor_timestamp),
            "transport_latency_s": max(0.0, receipt - float(sensor_timestamp)),
            "state_before": engine.get_state_name(),
        }
        callback_events.append(rec)
        emit(rec)
        engine.on_pir_sensor_fired(int(sensor_id), float(sensor_timestamp))
        rec_after = {
            "source": "callback",
            "action": "pir_callback_processed",
            "timestamp": _ts(),
            "sensor_id": int(sensor_id),
            "state_after": engine.get_state_name(),
            "engagement_stats": engine.get_engagement_stats(),
        }
        emit(rec_after)

    comm.set_on_transport_log(on_transport_log)
    comm.set_on_pir_event(on_pir)
    engine.set_pir_trace_callback(on_engine_pir_trace)
    engine.on_move(on_move)
    engine.on_fire(on_fire)
    engine.on_state_change(on_state_change)

    attempts = _build_connection_attempts(config)
    if max_attempts > 0:
        attempts = attempts[:max_attempts]

    selected_attempt: Optional[Dict[str, Any]] = None
    selected_success = False

    for attempt in attempts:
        label = str(attempt["label"])
        mode = int(attempt["mode"])
        kwargs = dict(attempt["kwargs"])
        emit({"source": "probe", "action": "connect_attempt", "label": label, "mode": mode, "kwargs": kwargs})
        ok = comm.connect(mode, **kwargs)
        emit(
            {
                "source": "probe",
                "action": "connect_result",
                "label": label,
                "ok": bool(ok),
                "connection_info": comm.connection_info(),
                "last_error": str(getattr(comm, "_last_error", "") or ""),
            }
        )
        if ok:
            selected_attempt = attempt
            selected_success = True
            send_ok = bool(comm.send_pir_enabled(True))
            emit(
                {
                    "source": "probe",
                    "action": "send_pir_enabled",
                    "enabled": True,
                    "ok": send_ok,
                }
            )
            break

    if selected_success:
        end_time = _ts() + float(duration_s)
        while _ts() < end_time:
            engine.update([], None)
            time.sleep(0.05)
        comm.disconnect()
        emit({"source": "probe", "action": "disconnect", "label": selected_attempt.get("label", "") if selected_attempt else ""})
    else:
        emit({"source": "probe", "action": "aborted_no_connection"})

    transport_pir = [e for e in transport_events if e.get("action") == "transport_pir_event"]
    callback_pir = [e for e in callback_events if e.get("action") == "pir_callback_received"]

    ordered = True
    last_ts = -1.0
    for entry in transport_pir:
        ts = float(entry.get("sensor_timestamp", 0.0) or 0.0)
        if ts < last_ts:
            ordered = False
            break
        last_ts = ts

    latencies = [float(e.get("transport_latency_s", 0.0) or 0.0) for e in callback_pir]
    summary = {
        "trace_path": str(trace_path),
        "selected_connection": dict(selected_attempt or {}),
        "connection_success": bool(selected_success),
        "duration_s": float(duration_s),
        "transport_pir_events": int(len(transport_pir)),
        "callback_pir_events": int(len(callback_pir)),
        "engine_trace_events": int(len(engine_trace_events)),
        "move_commands": int(len(moves)),
        "transport_ordering_ok": bool(ordered),
        "latency_min_s": min(latencies) if latencies else None,
        "latency_max_s": max(latencies) if latencies else None,
        "latency_avg_s": (sum(latencies) / len(latencies)) if latencies else None,
        "potential_drop_count": max(0, int(len(transport_pir) - len(callback_pir))),
        "final_engine_state": engine.get_state_name(),
        "final_engagement_stats": engine.get_engagement_stats(),
    }

    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Live PIR end-to-end probe")
    parser.add_argument("--duration", type=float, default=60.0, help="Probe duration in seconds after connection")
    parser.add_argument("--max-attempts", type=int, default=5, help="Maximum connection attempts from auto-generated plan")
    args = parser.parse_args()
    run_probe(duration_s=float(args.duration), max_attempts=int(args.max_attempts))


if __name__ == "__main__":
    main()
