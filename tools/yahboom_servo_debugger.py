import queue
import threading
import time
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

import serial


def calculate_checksum(payload):
    return (~sum(int(b) & 0xFF for b in payload)) & 0xFF


def build_ping_packet(servo_id):
    payload = [int(servo_id) & 0xFF, 0x02, 0x01]
    return bytes([0xFF, 0xFF] + payload + [calculate_checksum(payload)])


def build_read_packet(servo_id, addr, read_len):
    payload = [int(servo_id) & 0xFF, 0x04, 0x02, int(addr) & 0xFF, int(read_len) & 0xFF]
    return bytes([0xFF, 0xFF] + payload + [calculate_checksum(payload)])


def build_write_position_packet(servo_id, pos_ticks, move_time_ms):
    pos = max(0, min(4095, int(pos_ticks)))
    move_time = max(0, min(30000, int(move_time_ms)))
    payload = [
        int(servo_id) & 0xFF,
        0x07,
        0x03,
        0x2A,
        (pos >> 8) & 0xFF,
        pos & 0xFF,
        (move_time >> 8) & 0xFF,
        move_time & 0xFF,
    ]
    return bytes([0xFF, 0xFF] + payload + [calculate_checksum(payload)])


def build_set_id_packet(new_id):
    payload = [0xFE, 0x04, 0x03, 0x05, int(new_id) & 0xFF]
    return bytes([0xFF, 0xFF] + payload + [calculate_checksum(payload)])


def parse_reply(data):
    raw = bytes(data or b"")
    start = -1
    header_len = 0
    for candidate in (b"\xFF\xFF", b"\xFF\xF5"):
        idx = raw.find(candidate)
        if idx >= 0:
            start = idx
            header_len = len(candidate)
            break
    if start < 0 or len(raw) < start + header_len + 4:
        return None
    packet = raw[start:]
    packet = packet[header_len - 2:]
    declared_len = int(packet[3])
    total_len = declared_len + 4
    if len(packet) < total_len:
        return None
    packet = packet[:total_len]
    payload = list(packet[2:-1])
    checksum = calculate_checksum(payload)
    return {
        "packet": packet,
        "valid_checksum": checksum == packet[-1],
        "id": packet[2],
        "length": packet[3],
        "error": packet[4],
        "params": bytes(packet[5:-1]),
        "checksum": packet[-1],
        "expected_checksum": checksum,
    }


class YahboomServoDebugger(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Yahboom Bus Servo Debugger")
        self.geometry("980x720")
        self.minsize(840, 560)

        self._serial = None
        self._lock = threading.Lock()
        self._ui_queue = queue.Queue()

        self._build_ui()
        self.after(50, self._drain_ui_queue)

    def _build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        top = ttk.Frame(self, padding=10)
        top.grid(row=0, column=0, sticky="ew")
        for column in range(8):
            top.columnconfigure(column, weight=1 if column in (1, 3, 5) else 0)

        ttk.Label(top, text="COM Port").grid(row=0, column=0, sticky="w")
        self.port_var = tk.StringVar(value="COM34")
        ttk.Entry(top, textvariable=self.port_var, width=12).grid(row=0, column=1, sticky="ew", padx=(6, 12))

        ttk.Label(top, text="Baud").grid(row=0, column=2, sticky="w")
        self.baud_var = tk.StringVar(value="115200")
        ttk.Entry(top, textvariable=self.baud_var, width=10).grid(row=0, column=3, sticky="ew", padx=(6, 12))

        ttk.Label(top, text="Servo ID").grid(row=0, column=4, sticky="w")
        self.servo_id_var = tk.StringVar(value="1")
        ttk.Entry(top, textvariable=self.servo_id_var, width=8).grid(row=0, column=5, sticky="ew", padx=(6, 12))

        self.connect_btn = ttk.Button(top, text="Open Port", command=self._toggle_port)
        self.connect_btn.grid(row=0, column=6, sticky="ew", padx=(0, 8))

        self.status_var = tk.StringVar(value="Disconnected")
        ttk.Label(top, textvariable=self.status_var).grid(row=0, column=7, sticky="e")

        controls = ttk.LabelFrame(self, text="Servo Actions", padding=10)
        controls.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 10))
        for column in range(8):
            controls.columnconfigure(column, weight=1)

        ttk.Button(controls, text="Ping", command=self._ping).grid(row=0, column=0, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Read Position", command=self._read_position).grid(row=0, column=1, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Read Version", command=lambda: self._read_register(0x03, 1, "version")).grid(row=0, column=2, sticky="ew", padx=4, pady=4)

        ttk.Label(controls, text="Pos Ticks").grid(row=0, column=3, sticky="e")
        self.pos_var = tk.StringVar(value="2048")
        ttk.Entry(controls, textvariable=self.pos_var, width=10).grid(row=0, column=4, sticky="ew", padx=4, pady=4)

        ttk.Label(controls, text="Move ms").grid(row=0, column=5, sticky="e")
        self.move_time_var = tk.StringVar(value="1000")
        ttk.Entry(controls, textvariable=self.move_time_var, width=10).grid(row=0, column=6, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Send Position", command=self._send_position).grid(row=0, column=7, sticky="ew", padx=4, pady=4)

        ttk.Label(controls, text="New ID").grid(row=1, column=0, sticky="e")
        self.new_id_var = tk.StringVar(value="2")
        ttk.Entry(controls, textvariable=self.new_id_var, width=10).grid(row=1, column=1, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Write New ID", command=self._set_id).grid(row=1, column=2, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Center", command=lambda: self._send_position(2048)).grid(row=1, column=3, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Low", command=lambda: self._send_position(900)).grid(row=1, column=4, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="High", command=lambda: self._send_position(3100)).grid(row=1, column=5, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Clear Log", command=self._clear_log).grid(row=1, column=6, sticky="ew", padx=4, pady=4)

        self.result_var = tk.StringVar(value="No data yet")
        ttk.Label(controls, textvariable=self.result_var).grid(row=1, column=7, sticky="e")

        log_frame = ttk.LabelFrame(self, text="Raw TX / RX Log", padding=10)
        log_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=(0, 10))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)

        self.log = ScrolledText(log_frame, wrap="word", font=("Consolas", 10))
        self.log.grid(row=0, column=0, sticky="nsew")

    def _log(self, text):
        self.log.insert("end", text + "\n")
        self.log.see("end")

    def _clear_log(self):
        self.log.delete("1.0", "end")

    def _drain_ui_queue(self):
        while True:
            try:
                action, payload = self._ui_queue.get_nowait()
            except queue.Empty:
                break
            if action == "log":
                self._log(payload)
            elif action == "status":
                self.status_var.set(payload)
            elif action == "result":
                self.result_var.set(payload)
        self.after(50, self._drain_ui_queue)

    def _enqueue(self, action, payload):
        self._ui_queue.put((action, payload))

    def _toggle_port(self):
        if self._serial is not None and self._serial.is_open:
            self._close_port()
        else:
            self._open_port()

    def _open_port(self):
        try:
            port = self.port_var.get().strip()
            baud = int(self.baud_var.get().strip())
            self._serial = serial.Serial(port, baud, timeout=0.15, write_timeout=1)
            self.connect_btn.configure(text="Close Port")
            self.status_var.set(f"Connected: {port} @ {baud}")
            self._log(f"OPEN {port} @ {baud}")
        except Exception as exc:
            self.status_var.set("Open failed")
            self._log(f"ERROR open: {exc}")

    def _close_port(self):
        try:
            if self._serial is not None:
                self._serial.close()
        except Exception:
            pass
        self._serial = None
        self.connect_btn.configure(text="Open Port")
        self.status_var.set("Disconnected")
        self._log("CLOSE")

    def _worker(self, label, packet, expect_reply=True):
        def run():
            try:
                with self._lock:
                    if self._serial is None or not self._serial.is_open:
                        self._enqueue("log", "ERROR: serial port is not open")
                        return
                    self._serial.reset_input_buffer()
                    self._serial.write(packet)
                    self._serial.flush()
                    self._enqueue("log", f"TX {label}: {packet.hex().upper()}")
                    if not expect_reply:
                        self._enqueue("result", f"{label}: sent")
                        return
                    time.sleep(0.05)
                    response = self._serial.read(64)
                if response:
                    self._enqueue("log", f"RX {label}: {response.hex().upper()}")
                    parsed = parse_reply(response)
                    if parsed is None:
                        self._enqueue("result", f"{label}: unparsed reply")
                        return
                    params = parsed["params"]
                    if label == "read_position" and len(params) >= 2:
                        value = (params[0] << 8) | params[1]
                        self._enqueue("result", f"Position: {value} ticks")
                    else:
                        self._enqueue(
                            "result",
                            f"Reply id={parsed['id']} err=0x{parsed['error']:02X} params={params.hex().upper() or '-'} chk={'OK' if parsed['valid_checksum'] else 'BAD'}",
                        )
                else:
                    self._enqueue("log", f"RX {label}: <none>")
                    self._enqueue("result", f"{label}: no reply")
            except Exception as exc:
                self._enqueue("log", f"ERROR {label}: {exc}")
                self._enqueue("result", f"{label}: failed")

        threading.Thread(target=run, daemon=True).start()

    def _get_servo_id(self):
        return int(self.servo_id_var.get().strip())

    def _ping(self):
        self._worker("ping", build_ping_packet(self._get_servo_id()))

    def _read_register(self, addr, read_len, label):
        self._worker(label, build_read_packet(self._get_servo_id(), addr, read_len))

    def _read_position(self):
        self._read_register(0x38, 2, "read_position")

    def _send_position(self, pos_ticks=None):
        if pos_ticks is None:
            pos_ticks = int(self.pos_var.get().strip())
        move_time = int(self.move_time_var.get().strip())
        packet = build_write_position_packet(self._get_servo_id(), pos_ticks, move_time)
        self._worker("write_position", packet, expect_reply=False)

    def _set_id(self):
        packet = build_set_id_packet(int(self.new_id_var.get().strip()))
        self._worker("write_id", packet, expect_reply=False)


if __name__ == "__main__":
    YahboomServoDebugger().mainloop()