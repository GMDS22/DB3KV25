#!/usr/bin/env python3
"""Automated hardware + app smoke tests for DB3000.

Goal: one command that tells you what is working right now.

What it tests (best-effort):
- Detect Nano port (by reading firmware banner at 115200).
- Optionally run Nano "BUSPING" to confirm Nano->debug-board->servo comms.
- Optionally run Nano movement sequence (same as tools/servo_move_test_over_usb.py).
- Detect debug board port (by DS_v4 ping on IDs).
- Optionally move bus servos through debug board USB.
- Optionally run Python repo smoke tests (test_app_start.py, test_resolution_fix.py, servo_fix_test.py).

Notes:
- This script cannot prove *physical motion*; it proves serial protocol + replies.
- For the most deterministic diagnosis, keep the debug board USB unplugged
  while testing Nano BUSPING.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

try:
    import cv2  # type: ignore
except Exception:
    cv2 = None  # type: ignore

try:
    import serial  # type: ignore
    import serial.tools.list_ports  # type: ignore
except Exception as e:
    print(f"[ERROR] pyserial not available: {e}")
    print("Install dependencies with: pip install -r requirements.txt")
    raise


RE_READY = re.compile(r"DB3000 SerialBus Upgrade 2026: READY", re.I)
RE_OTHER_READY = re.compile(r"=== Turret Ready ===", re.I)

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SETTINGS_PATH = REPO_ROOT / "settings.json"
DEFAULT_LOG_DIR = REPO_ROOT / "logs"


@dataclass
class PortInfo:
    device: str
    description: str


@dataclass
class TestResult:
    name: str
    ok: bool
    details: str


def load_settings(path: Path) -> dict:
    try:
        if not path.exists():
            return {}
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _combo_index_to_camera_preference(camera_index: int) -> int | None:
    """Convert UI combo index to an actual camera device index.

    UI items are: ["Auto", "0", "1", "2", "3", "4"].
    - 0 means Auto
    - N means device index (N-1)
    """
    try:
        ci = int(camera_index)
    except Exception:
        return None
    if ci <= 0:
        return None
    return max(0, ci - 1)


def _parse_resolution_setting(val: object) -> tuple[int, int] | None:
    try:
        s = str(val)
        if "x" not in s:
            return None
        a, b = s.lower().split("x", 1)
        w = int(a.strip())
        h = int(b.strip())
        if w <= 0 or h <= 0:
            return None
        return w, h
    except Exception:
        return None


def _camera_probe(
    index: int,
    *,
    backend: int | None,
    desired_wh: tuple[int, int] | None,
    frames: int = 20,
) -> tuple[bool, str]:
    if cv2 is None:
        return False, "opencv-python not installed; cannot probe cameras"

    try:
        if backend is None:
            cap = cv2.VideoCapture(int(index))
            backend_name = "default"
        else:
            cap = cv2.VideoCapture(int(index), int(backend))
            backend_name = str(backend)
    except Exception as e:
        return False, f"open failed ({backend_name}): {e}"

    try:
        if not cap.isOpened():
            return False, f"not opened ({backend_name})"

        # Try to apply the app-requested resolution; some drivers return black frames
        # when set to an unsupported mode.
        if desired_wh is not None:
            try:
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(desired_wh[0]))
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(desired_wh[1]))
                time.sleep(0.05)
            except Exception:
                pass

        try:
            actual_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            actual_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        except Exception:
            actual_w, actual_h = 0, 0

        ok_reads = 0
        black_reads = 0
        motion_score = 0.0
        prev_gray = None

        for _ in range(int(frames)):
            ok, frame = cap.read()
            if not ok or frame is None:
                time.sleep(0.03)
                continue
            ok_reads += 1

            try:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                mean_val = float(gray.mean())
                if mean_val < 1.0:
                    black_reads += 1
                if prev_gray is not None:
                    diff = cv2.absdiff(gray, prev_gray)
                    motion_score += float(diff.mean())
                prev_gray = gray
            except Exception:
                # If conversions fail, still count it as a read.
                pass

            time.sleep(0.03)

        if ok_reads == 0:
            return False, f"opened but no frames ({backend_name}); actual={actual_w}x{actual_h}"

        avg_motion = motion_score / max(1, ok_reads - 1)
        if black_reads >= max(3, int(ok_reads * 0.8)) and avg_motion < 0.2:
            return False, (
                f"black/blank frames ({backend_name}); reads={ok_reads} avg_motion={avg_motion:.3f} "
                f"actual={actual_w}x{actual_h}"
            )

        return True, f"ok ({backend_name}); reads={ok_reads} avg_motion={avg_motion:.3f} actual={actual_w}x{actual_h}"
    finally:
        try:
            cap.release()
        except Exception:
            pass


def camera_tests(*, preferred_index: int | None, desired_wh: tuple[int, int] | None) -> list[TestResult]:
    if cv2 is None:
        return [TestResult("camera_probe", False, "opencv-python not installed; pip install opencv-python")]

    # Try preferred first, then fallback to 0..4.
    indices: list[int] = []
    if preferred_index is not None:
        indices.append(int(preferred_index))
        indices.extend([i for i in range(0, 5) if i != int(preferred_index)])
    else:
        indices = list(range(0, 5))

    # Backends to try on Windows; default first.
    backend_trials: list[tuple[str, int | None]] = [("default", None)]
    try:
        backend_trials.append(("dshow", int(getattr(cv2, "CAP_DSHOW", 700))))
    except Exception:
        pass
    try:
        backend_trials.append(("msmf", int(getattr(cv2, "CAP_MSMF", 1400))))
    except Exception:
        pass

    out: list[TestResult] = []
    for idx in indices:
        any_ok = False
        details_lines: list[str] = []
        for label, backend in backend_trials:
            ok, info = _camera_probe(idx, backend=backend, desired_wh=desired_wh)
            details_lines.append(f"{label}: {info}")
            any_ok = any_ok or ok
        out.append(TestResult(f"camera_index_{idx}", any_ok, " | ".join(details_lines)))
    return out


def list_ports() -> list[PortInfo]:
    out: list[PortInfo] = []
    for p in serial.tools.list_ports.comports():
        out.append(PortInfo(device=p.device, description=getattr(p, "description", "")))
    return out


def read_banner(port: str, *, baud: int = 115200, reset: bool = True, seconds: float = 3.0) -> str:
    try:
        ser = serial.Serial(port=port, baudrate=baud, timeout=0.2, write_timeout=1.0)
    except Exception as e:
        return f"(could not open {port}: {e})"
    try:
        if reset:
            try:
                ser.dtr = False
                time.sleep(0.2)
                ser.dtr = True
            except Exception:
                pass

        time.sleep(0.4)
        end = time.time() + float(seconds)
        buf = bytearray()
        while time.time() < end:
            chunk = ser.read(4096)
            if chunk:
                buf.extend(chunk)
                # stop early if we likely have the banner
                if b"READY" in buf or b"Turret" in buf:
                    break
            else:
                time.sleep(0.05)

        return buf.decode("utf-8", errors="replace")
    finally:
        try:
            ser.close()
        except Exception:
            pass


def nano_busping(port: str, *, baud: int = 115200, ids: list[int]) -> tuple[bool, str]:
    try:
        ser = serial.Serial(port=port, baudrate=baud, timeout=0.4, write_timeout=1.0)
    except Exception as e:
        return False, f"could not open {port}: {e}"
    try:
        # reset to get banner and ensure sketch is running
        try:
            ser.dtr = False
            time.sleep(0.2)
            ser.dtr = True
        except Exception:
            pass
        # Let bootloader + sketch prints finish
        time.sleep(2.0)

        # Drain any startup banner/noise
        drain_end = time.time() + 0.8
        while time.time() < drain_end:
            _ = ser.readline()
            if ser.in_waiting == 0:
                time.sleep(0.05)

        def send_busping() -> None:
            ser.write(b"BUSPING\n")
            ser.flush()

        # Send BUSPING and wait for response; retry once.
        lines: list[str] = []
        send_busping()

        end = time.time() + 2.0
        while time.time() < end and len(lines) < 30:
            line = ser.readline().decode("utf-8", errors="replace").strip()
            if line:
                lines.append(line)
                if line.startswith("BUSPING"):
                    break

        if not any(l.startswith("BUSPING") for l in lines):
            # Retry after a short pause
            time.sleep(0.2)
            send_busping()
            retry_end = time.time() + 2.0
            while time.time() < retry_end and len(lines) < 60:
                line = ser.readline().decode("utf-8", errors="replace").strip()
                if line:
                    lines.append(line)
                    if line.startswith("BUSPING"):
                        break

        out = "\n".join(lines)
        # Evaluate: require OK for each expected id
        ok = True
        for sid in ids:
            if f"id={sid}" in out or f"id={sid}" in out:
                pass
        # Our output is: BUSPING PAN(id=1)=OK TILT(id=2)=OK
        for sid in ids:
            if f"id={sid})=OK" not in out and f"id={sid}=OK" not in out:
                ok = False

        return ok, out or "(no BUSPING response)"
    finally:
        try:
            ser.close()
        except Exception:
            pass


def ds_ping(port: str, *, servo_id: int, baud: int = 115200, timeout: float = 0.25) -> tuple[bool, str]:
    def chk_sub(payload: bytes) -> int:
        return (0xFF - (sum(payload) & 0xFF)) & 0xFF

    def chk_xor(payload: bytes) -> int:
        return (0xFF ^ (sum(payload) & 0xFF)) & 0xFF

    payload = bytes([servo_id & 0xFF, 0x02, 0x01])
    pkt_sub = b"\xFF\xFF" + payload + bytes([chk_sub(payload)])
    pkt_xor = b"\xFF\xFF" + payload + bytes([chk_xor(payload)])

    try:
        ser = serial.Serial(port=port, baudrate=baud, timeout=timeout, write_timeout=1.0)
    except Exception as e:
        return False, f"could not open {port}: {e}"
    try:
        def _try(pkt: bytes) -> bytes:
            try:
                ser.reset_input_buffer()
            except Exception:
                pass
            ser.write(pkt)
            ser.flush()
            return ser.read(64)

        data_sub = _try(pkt_sub)
        if data_sub:
            ok = (len(data_sub) >= 3 and data_sub[0] == 0xFF and data_sub[2] == (servo_id & 0xFF))
            info = " ".join(f"{b:02X}" for b in data_sub[:16]) + (" ..." if len(data_sub) > 16 else "")
            return ok, f"sub rx={info}"

        data_xor = _try(pkt_xor)
        if data_xor:
            ok = (len(data_xor) >= 3 and data_xor[0] == 0xFF and data_xor[2] == (servo_id & 0xFF))
            info = " ".join(f"{b:02X}" for b in data_xor[:16]) + (" ..." if len(data_xor) > 16 else "")
            return ok, f"xor rx={info}"

        return False, "no response (sub+xor tried)"
    finally:
        try:
            ser.close()
        except Exception:
            pass


def debug_baud_scan(port: str, *, servo_id: int, bauds: list[int]) -> tuple[bool, str, int | None]:
    """Try pings across common baud rates to detect mismatches."""
    tried: list[str] = []
    for b in bauds:
        try:
            ok, info = ds_ping(port, servo_id=servo_id, baud=int(b))
            tried.append(f"{b}:{'OK' if ok else 'no'}")
            if ok:
                return True, f"found baud={b} (rx={info}); tried={', '.join(tried)}", int(b)
        except Exception as e:
            tried.append(f"{b}:err({e})")
    return False, f"no baud worked; tried={', '.join(tried)}", None


def ds_write_pos(
    port: str,
    *,
    servo_id: int,
    pos: int,
    time_ms: int = 120,
    baud: int = 115200,
    timeout: float = 0.25,
    allow_no_ack: bool = False,
) -> tuple[bool, str]:
    """Write a target position (0..4095) directly via the debug board."""
    p = int(pos)
    t = int(time_ms)
    if p < 0 or p > 4095:
        return False, f"pos out of range: {p}"
    if t < 0 or t > 65535:
        return False, f"time out of range: {t}"

    def chk_sub(payload: bytes) -> int:
        return (0xFF - (sum(payload) & 0xFF)) & 0xFF

    def chk_xor(payload: bytes) -> int:
        return (0xFF ^ (sum(payload) & 0xFF)) & 0xFF

    length = 7
    instruction = 3
    params = bytes([0x2A, (p >> 8) & 0xFF, p & 0xFF, (t >> 8) & 0xFF, t & 0xFF])
    payload = bytes([servo_id & 0xFF, length, instruction]) + params
    pkt_sub = b"\xFF\xFF" + payload + bytes([chk_sub(payload)])
    pkt_xor = b"\xFF\xFF" + payload + bytes([chk_xor(payload)])

    try:
        ser = serial.Serial(port=port, baudrate=baud, timeout=timeout, write_timeout=1.0)
    except Exception as e:
        return False, f"could not open {port}: {e}"
    try:
        def _try(pkt: bytes) -> bytes:
            try:
                ser.reset_input_buffer()
            except Exception:
                pass
            ser.write(pkt)
            ser.flush()
            return ser.read(64)

        data_sub = _try(pkt_sub)
        if data_sub:
            ok = (len(data_sub) >= 3 and data_sub[0] == 0xFF and data_sub[2] == (servo_id & 0xFF))
            info = " ".join(f"{b:02X}" for b in data_sub[:16]) + (" ..." if len(data_sub) > 16 else "")
            return ok, f"sub rx={info}"

        data_xor = _try(pkt_xor)
        if data_xor:
            ok = (len(data_xor) >= 3 and data_xor[0] == 0xFF and data_xor[2] == (servo_id & 0xFF))
            info = " ".join(f"{b:02X}" for b in data_xor[:16]) + (" ..." if len(data_xor) > 16 else "")
            return ok, f"xor rx={info}"

        data = b""
        # Some setups don't respond to write-pos.
        if not data:
            return bool(allow_no_ack), "no response (write-pos may be ACK-less; visually confirm motion)"
        ok = (len(data) >= 3 and data[0] == 0xFF and data[2] == (servo_id & 0xFF))
        return ok, " ".join(f"{b:02X}" for b in data[:16]) + (" ..." if len(data) > 16 else "")
    finally:
        try:
            ser.close()
        except Exception:
            pass


def run_py_test(py_exe: str, script: str) -> TestResult:
    try:
        env = os.environ.copy()
        # Force UTF-8 stdout/stderr on Windows consoles to avoid UnicodeEncodeError.
        env.setdefault("PYTHONUTF8", "1")
        env.setdefault("PYTHONIOENCODING", "utf-8")
        proc = subprocess.run(
            [py_exe, "-X", "utf8", script],
            cwd=os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
            capture_output=True,
            text=True,
            env=env,
            timeout=120,
        )
        ok = proc.returncode == 0
        details = (proc.stdout + "\n" + proc.stderr).strip()
        if len(details) > 2000:
            details = details[:2000] + "\n...(truncated)..."
        return TestResult(name=script, ok=ok, details=details or f"exit={proc.returncode}")
    except Exception as e:
        return TestResult(name=script, ok=False, details=str(e))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nano-port", default="auto", help="COM port for Nano (default: auto)")
    ap.add_argument("--debug-port", default="auto", help="COM port for debug board (default: auto)")
    ap.add_argument("--ids", default="1,2", help="Servo IDs to test (default: 1,2)")

    ap.add_argument("--from-settings", action="store_true", help="Use settings.json ports/baud (recommended for app issues)")
    ap.add_argument("--settings", default=str(DEFAULT_SETTINGS_PATH), help="Path to settings.json")
    ap.add_argument("--skip-camera", action="store_true")
    ap.add_argument("--do-debug-move", action="store_true", help="Send safe write-pos moves over debug board USB")
    ap.add_argument("--allow-no-ack", action="store_true", help="Treat missing write-pos ACK as PASS")
    ap.add_argument("--send-pten0", action="store_true", help="Send PTEN0 to Nano (disable Nano pan/tilt output)")

    ap.add_argument("--skip-nano", action="store_true")
    ap.add_argument("--skip-debug", action="store_true")
    ap.add_argument("--skip-python", action="store_true")

    ap.add_argument("--do-busping", action="store_true", help="Ask Nano to BUSPING and validate replies")
    ap.add_argument("--do-nano-move", action="store_true", help="Run tools/servo_move_test_over_usb.py")

    ap.add_argument("--py", default=None, help="Python executable (defaults to current interpreter)")

    args = ap.parse_args()

    log_lines: list[str] = []

    def emit(msg: str = "") -> None:
        print(msg)
        log_lines.append(msg)

    ids = [int(x) for x in args.ids.split(",") if x.strip()]

    settings_path = Path(args.settings)
    settings = load_settings(settings_path)

    if args.from_settings:
        try:
            mode_idx = int(settings.get("serial_device_type_index", 0))
        except Exception:
            mode_idx = 0

        nano_port = str(settings.get("com_port", "")) or None
        debug_port = str(settings.get("debug_board_com_port", "")) or None
        # In non-dual modes, debug_port may be blank; keep auto-detect fallback.
        if mode_idx != 2:
            debug_port = debug_port or None

        emit(f"[SETTINGS] {settings_path}")
        emit(f"[SETTINGS] serial_device_type_index={mode_idx} (0=nano,1=debug,2=dual)")
        emit(f"[SETTINGS] com_port={settings.get('com_port','')} baud_rate={settings.get('baud_rate',115200)}")
        emit(f"[SETTINGS] debug_board_com_port={settings.get('debug_board_com_port','')} debug_board_baud_rate={settings.get('debug_board_baud_rate',115200)}")
        emit(f"[SETTINGS] camera_index(combo)={settings.get('camera_index',0)}")
    else:
        nano_port = None if args.nano_port == "auto" else args.nano_port
        debug_port = None if args.debug_port == "auto" else args.debug_port

    ports = list_ports()
    emit("[PORTS]")
    for p in ports:
        emit(f"- {p.device}: {p.description}")

    # Auto-detect Nano by banner
    if not nano_port:
        for p in ports:
            try:
                banner = read_banner(p.device)
                if RE_READY.search(banner) or RE_OTHER_READY.search(banner):
                    nano_port = p.device
                    emit(f"[DETECT] Nano on {nano_port}")
                    break
            except Exception:
                continue

    # Auto-detect debug board by DS ping
    if not debug_port:
        for p in ports:
            if nano_port and p.device == nano_port:
                continue
            try:
                ok1, _ = ds_ping(p.device, servo_id=ids[0])
                if ok1:
                    debug_port = p.device
                    emit(f"[DETECT] Debug board on {debug_port}")
                    break
            except Exception:
                continue

    results: list[TestResult] = []

    # Camera tests
    if not args.skip_camera:
        preferred_cam = _combo_index_to_camera_preference(settings.get("camera_index", 0))
        desired_wh = _parse_resolution_setting(settings.get("frame_ratio_setting", ""))
        results.extend(camera_tests(preferred_index=preferred_cam, desired_wh=desired_wh))

    # Dual mode sanity (settings-driven only)
    if args.from_settings:
        try:
            mode_idx = int(settings.get("serial_device_type_index", 0))
        except Exception:
            mode_idx = 0
        if mode_idx == 2:
            if not nano_port:
                results.append(TestResult("dual_ports", False, "Dual mode selected but com_port is blank/unknown"))
            if not debug_port:
                results.append(TestResult("dual_ports", False, "Dual mode selected but debug_board_com_port is blank/unknown"))
            if nano_port and debug_port and str(nano_port).strip().upper() == str(debug_port).strip().upper():
                results.append(TestResult("dual_ports", False, f"Dual mode ports are the same ({nano_port}); must be different"))

    # Nano tests
    if not args.skip_nano:
        if not nano_port:
            results.append(TestResult("nano_detect", False, "Could not auto-detect Nano port"))
        else:
            banner = read_banner(nano_port)
            if RE_READY.search(banner):
                results.append(TestResult("nano_banner", True, "Dual-bus sketch READY"))
            elif RE_OTHER_READY.search(banner):
                results.append(TestResult("nano_banner", False, "Nano is running the older Turret Ready sketch"))
            else:
                results.append(TestResult("nano_banner", False, "No expected banner received"))

            # Optionally disable Nano pan/tilt output (Dual Port conflict prevention)
            if args.send_pten0:
                try:
                    ser = serial.Serial(port=nano_port, baudrate=int(settings.get("baud_rate", 115200)), timeout=0.2, write_timeout=1.0)
                    try:
                        time.sleep(1.6)
                        ser.write(b"PTEN0\n")
                        ser.flush()
                        results.append(TestResult("nano_pten0", True, "Sent PTEN0"))
                    finally:
                        ser.close()
                except Exception as e:
                    results.append(TestResult("nano_pten0", False, str(e)))

            if args.do_busping:
                ok, out = nano_busping(nano_port, ids=ids)
                results.append(TestResult("nano_busping", ok, out))

            if args.do_nano_move:
                cmd = [
                    sys.executable,
                    os.path.abspath(os.path.join(os.path.dirname(__file__), "servo_move_test_over_usb.py")),
                    "--port",
                    nano_port,
                    "--mode",
                    "sweep",
                    "--delay",
                    "1.2",
                    "--confirm",
                ]
                proc = subprocess.run(cmd, capture_output=True, text=True)
                results.append(TestResult("nano_move_sweep", proc.returncode == 0, (proc.stdout + "\n" + proc.stderr).strip()))

    # Debug board tests (PC -> debug board -> servos)
    if not args.skip_debug:
        if not debug_port:
            results.append(TestResult("debug_detect", False, "Could not auto-detect debug board port"))
        else:
            debug_baud = int(settings.get("debug_board_baud_rate", 115200))
            common_bauds = [debug_baud, 115200, 1000000, 57600, 38400, 9600]
            # de-dupe while preserving order
            seen: set[int] = set()
            bauds = [b for b in common_bauds if not (b in seen or seen.add(int(b)))]

            for sid in ids:
                ok, info = ds_ping(debug_port, servo_id=sid, baud=debug_baud)
                results.append(TestResult(f"debug_ping_id_{sid}", ok, f"{debug_port}: {info}"))

            # If primary ping failed, scan for baud mismatches.
            if any(r.name.startswith("debug_ping_id_") and (not r.ok) for r in results):
                ok_scan, info_scan, found = debug_baud_scan(debug_port, servo_id=ids[0], bauds=bauds)
                results.append(TestResult("debug_baud_scan", ok_scan, f"{debug_port}: {info_scan}"))
                if ok_scan and found is not None:
                    debug_baud = int(found)

            if args.do_debug_move:
                # Safe small moves around center. User should visually confirm motion.
                for sid in ids:
                    ok1, info1 = ds_write_pos(
                        debug_port,
                        servo_id=sid,
                        pos=2048,
                        time_ms=150,
                        baud=debug_baud,
                        allow_no_ack=bool(args.allow_no_ack),
                    )
                    results.append(TestResult(f"debug_write_center_id_{sid}", ok1, f"{debug_port}: {info1}"))
                    ok2, info2 = ds_write_pos(
                        debug_port,
                        servo_id=sid,
                        pos=2300,
                        time_ms=180,
                        baud=debug_baud,
                        allow_no_ack=bool(args.allow_no_ack),
                    )
                    results.append(TestResult(f"debug_write_offset_id_{sid}", ok2, f"{debug_port}: {info2}"))
                    ok3, info3 = ds_write_pos(
                        debug_port,
                        servo_id=sid,
                        pos=2048,
                        time_ms=180,
                        baud=debug_baud,
                        allow_no_ack=bool(args.allow_no_ack),
                    )
                    results.append(TestResult(f"debug_write_return_id_{sid}", ok3, f"{debug_port}: {info3}"))

    # Python tests
    if not args.skip_python:
        py_exe = args.py or sys.executable
        for script in ["test_app_start.py", "test_resolution_fix.py", "servo_fix_test.py"]:
            path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", script))
            if os.path.exists(path):
                results.append(run_py_test(py_exe, path))
            else:
                results.append(TestResult(script, False, "missing"))

    emit("\n[RESULTS]")
    any_fail = False
    for r in results:
        status = "PASS" if r.ok else "FAIL"
        emit(f"{status} {r.name}")
        if not r.ok:
            any_fail = True

    emit("\n[DETAILS]")
    for r in results:
        if (not r.ok) or r.name.startswith("camera_index_"):
            emit(f"--- {r.name} ---")
            emit(r.details)

    # Always write a timestamped log for easy sharing.
    try:
        DEFAULT_LOG_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = DEFAULT_LOG_DIR / f"run_all_tests_{ts}.txt"
        log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
        emit(f"\n[LOG] Wrote {log_path}")
    except Exception:
        pass

    return 1 if any_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
