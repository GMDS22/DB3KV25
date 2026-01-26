from __future__ import annotations

import threading
import time
from dataclasses import dataclass

try:
    import serial  # type: ignore
except Exception as exc:  # pragma: no cover
    serial = None
    _SERIAL_IMPORT_ERROR = exc
else:
    _SERIAL_IMPORT_ERROR = None


@dataclass
class NanoState:
    armed: bool = False
    mode: int = 0  # 0 water, 1 projectile
    led: bool = False
    laser: bool = False
    fire: bool = False


class NanoIO:
    def __init__(self) -> None:
        self.ser = None
        self.state = NanoState()
        self._lock = threading.Lock()
        self._reader_stop = threading.Event()
        self._reader_thread: threading.Thread | None = None
        self.last_lines: list[str] = []

    def open(self, port: str, baud: int) -> None:
        if serial is None:
            raise RuntimeError(f"pyserial not available: {_SERIAL_IMPORT_ERROR}")
        self.ser = serial.Serial(port, baud, timeout=0.2)
        time.sleep(1.0)
        self._start_reader()

    def close(self) -> None:
        self._stop_reader()
        if self.ser is not None:
            try:
                self.ser.close()
            except Exception:
                pass
        self.ser = None

    def _start_reader(self) -> None:
        if self.ser is None:
            return
        self._reader_stop.clear()

        def _run() -> None:
            while not self._reader_stop.is_set():
                try:
                    if self.ser is None:
                        break
                    line = self.ser.readline().decode("utf-8", errors="ignore").strip()
                    if line:
                        with self._lock:
                            self.last_lines.append(line)
                            self.last_lines = self.last_lines[-50:]
                except Exception:
                    time.sleep(0.05)

        self._reader_thread = threading.Thread(target=_run, daemon=True, name="NanoReader")
        self._reader_thread.start()

    def _stop_reader(self) -> None:
        self._reader_stop.set()
        if self._reader_thread:
            self._reader_thread.join(timeout=0.5)
        self._reader_thread = None

    def _send(self, token: str) -> None:
        if self.ser is None:
            return
        if not token.endswith("\n"):
            token += "\n"
        with self._lock:
            self.ser.write(token.encode("utf-8"))

    def set_mode(self, mode: int) -> None:
        self.state.mode = 1 if mode else 0
        self._send(f"M{self.state.mode}")

    def set_safety(self, armed: bool) -> None:
        self.state.armed = bool(armed)
        token = "S0" if self.state.armed else "S1"
        self._send(token)

    def set_fire(self, on: bool) -> None:
        self.state.fire = bool(on)
        token = "F1" if self.state.fire else "F0"
        self._send(token)

    def set_led(self, on: bool) -> None:
        self.state.led = bool(on)
        token = "L1" if self.state.led else "L0"
        self._send(token)

    def set_laser(self, on: bool) -> None:
        self.state.laser = bool(on)
        token = "R1" if self.state.laser else "R0"
        self._send(token)


class BusServo:
    def __init__(self) -> None:
        self.ser = None
        self.checksum_mode = "auto"
        self._lock = threading.Lock()

    def open(self, port: str, baud: int) -> None:
        if serial is None:
            raise RuntimeError(f"pyserial not available: {_SERIAL_IMPORT_ERROR}")
        self.ser = serial.Serial(port, baud, timeout=0.05)
        time.sleep(0.2)

    def close(self) -> None:
        if self.ser is not None:
            try:
                self.ser.close()
            except Exception:
                pass
        self.ser = None

    def _checksum_sub(self, payload: list[int]) -> int:
        return (~sum(payload)) & 0xFF

    def _checksum_xor(self, payload: list[int]) -> int:
        chk = 0
        for b in payload:
            chk ^= b
        return chk & 0xFF

    def _build_packet(self, payload: list[int]) -> bytes:
        if self.checksum_mode == "xor":
            chk = self._checksum_xor(payload)
        else:
            chk = self._checksum_sub(payload)
        return bytes([0xFF, 0xFF] + payload + [chk])

    def _write_packet(self, payload: list[int]) -> None:
        if self.ser is None:
            return
        pkt = self._build_packet(payload)
        with self._lock:
            self.ser.write(pkt)

    def ping(self, servo_id: int) -> bool:
        if self.ser is None:
            return False
        payload = [servo_id, 0x02, 0x01]
        self._write_packet(payload)
        try:
            resp = self.ser.read(16)
        except Exception:
            return False
        return resp.startswith(b"\xFF\xFF")

    def auto_detect_checksum(self, servo_id: int) -> None:
        if self.checksum_mode != "auto":
            return
        for mode in ("sub", "xor"):
            self.checksum_mode = mode
            if self.ping(servo_id):
                return
        self.checksum_mode = "sub"

    def write_position(
        self,
        servo_id: int,
        goal_addr: int,
        position_ticks: int,
        time_ms: int,
        speed: int = 0,
    ) -> None:
        if self.ser is None:
            return
        pos = max(0, min(4095, int(position_ticks)))
        t = max(0, min(30000, int(time_ms)))
        spd = max(0, min(1023, int(speed)))
        pos_l = pos & 0xFF
        pos_h = (pos >> 8) & 0xFF
        t_l = t & 0xFF
        t_h = (t >> 8) & 0xFF
        s_l = spd & 0xFF
        s_h = (spd >> 8) & 0xFF
        params = [goal_addr, pos_l, pos_h, t_l, t_h, s_l, s_h]
        length = len(params) + 2
        payload = [servo_id, length, 0x03] + params
        self._write_packet(payload)


class SerialController:
    def __init__(self, bus_config: dict, aim_config: dict) -> None:
        self.bus_config = bus_config
        self.aim_config = aim_config
        self.nano = NanoIO()
        self.bus = BusServo()
        self.mode = "dual"
        self._lock = threading.Lock()
        self._pan_deg = aim_config.get("pan_center", 110.0)
        self._tilt_deg = aim_config.get("tilt_center", 80.0)

    def connect(self, mode: str, nano_port: str, nano_baud: int, bus_port: str, bus_baud: int) -> None:
        self.mode = mode
        if mode in ("dual", "nano"):
            self.nano.open(nano_port, nano_baud)
        if mode in ("dual", "bus"):
            self.bus.open(bus_port, bus_baud)
            self.bus.auto_detect_checksum(self.bus_config["pan_id"])

    def close(self) -> None:
        self.nano.close()
        self.bus.close()

    def set_safety(self, armed: bool) -> None:
        if self.mode in ("dual", "nano"):
            self.nano.set_safety(armed)

    def set_trigger_mode(self, projectile: bool) -> None:
        if self.mode in ("dual", "nano"):
            self.nano.set_mode(1 if projectile else 0)

    def set_led(self, on: bool) -> None:
        if self.mode in ("dual", "nano"):
            self.nano.set_led(on)

    def set_laser(self, on: bool) -> None:
        if self.mode in ("dual", "nano"):
            self.nano.set_laser(on)

    def fire_pulse(self, duration_ms: int = 120) -> None:
        if self.mode not in ("dual", "nano"):
            return

        def _pulse() -> None:
            self.nano.set_fire(True)
            time.sleep(duration_ms / 1000.0)
            self.nano.set_fire(False)

        threading.Thread(target=_pulse, daemon=True, name="FirePulse").start()

    def get_pose(self) -> tuple[float, float]:
        with self._lock:
            return self._pan_deg, self._tilt_deg

    def set_pose(self, pan_deg: float, tilt_deg: float, time_ms: int) -> None:
        with self._lock:
            pan = float(pan_deg)
            tilt = float(tilt_deg)
            self._pan_deg = pan
            self._tilt_deg = tilt
        if self.mode in ("dual", "bus"):
            self._send_bus(pan, tilt, time_ms)
        if self.mode == "nano":
            self._send_nano_pan_tilt(pan, tilt)

    def nudge(self, delta_pan: float, delta_tilt: float, time_ms: int) -> None:
        pan, tilt = self.get_pose()
        self.set_pose(pan + delta_pan, tilt + delta_tilt, time_ms=time_ms)

    def _send_bus(self, pan_deg: float, tilt_deg: float, time_ms: int) -> None:
        cfg = self.bus_config
        pan_min, pan_max = cfg["pan_min"], cfg["pan_max"]
        tilt_min, tilt_max = cfg["tilt_min"], cfg["tilt_max"]
        pan_deg = max(pan_min, min(pan_max, pan_deg))
        tilt_deg = max(tilt_min, min(tilt_max, tilt_deg))
        if cfg.get("invert_pan"):
            pan_deg = pan_max - (pan_deg - pan_min)
        if cfg.get("invert_tilt"):
            tilt_deg = tilt_max - (tilt_deg - tilt_min)
        ticks_max = cfg["ticks_max"]
        deg_max = cfg["deg_max"]
        pan_ticks = int((pan_deg / deg_max) * ticks_max)
        tilt_ticks = int((tilt_deg / deg_max) * ticks_max)
        goal_addr = cfg["goal_addr"]
        self.bus.write_position(cfg["pan_id"], goal_addr, pan_ticks, time_ms)
        self.bus.write_position(cfg["tilt_id"], goal_addr, tilt_ticks, time_ms)

    def _send_nano_pan_tilt(self, pan_deg: float, tilt_deg: float) -> None:
        if self.nano.ser is None:
            return
        command = f"P{int(pan_deg)}T{int(tilt_deg)}"
        self.nano._send(command)
