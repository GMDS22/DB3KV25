import sys
import time

try:
    import serial
    from serial.tools import list_ports
except Exception as e:  # pragma: no cover
    print("pyserial is required:", e)
    sys.exit(2)


def _is_bluetooth_port(p) -> bool:
    text = f"{p.description} {p.hwid}".lower()
    return "bluetooth" in text or "bth" in text or "standard serial over bluetooth" in text


def main() -> int:
    ports = list(list_ports.comports())
    if not ports:
        print("No COM ports found.")
        return 1

    print("Detected COM ports:")
    for p in ports:
        tag = "BT" if _is_bluetooth_port(p) else "  "
        print(f"- [{tag}] {p.device}: {p.description}")

    bt_ports = [p for p in ports if _is_bluetooth_port(p)]
    if not bt_ports:
        print("\nNo obvious Bluetooth COM ports detected.")
        print("If you already paired an HC-05/HC-06, check Windows Device Manager → Ports.")
        return 0

    print("\nAttempting to open Bluetooth COM ports (115200 then 9600):")
    for p in bt_ports:
        for baud in (115200, 9600):
            try:
                ser = serial.Serial(p.device, baud, timeout=0.25)
                time.sleep(0.2)
                ser.reset_input_buffer()
                ser.write(b"S1\n")  # safe (disarm)
                time.sleep(0.2)
                read_bytes = ser.in_waiting
                preview = b""
                if read_bytes:
                    preview = ser.read(min(read_bytes, 200))
                ser.close()
                msg = "OPEN_OK"
                if preview:
                    msg += f" (rx {len(preview)} bytes)"
                print(f"- {p.device} @ {baud}: {msg}")
                break
            except Exception as e:
                print(f"- {p.device} @ {baud}: OPEN_FAIL ({e.__class__.__name__})")
                continue

    print("\nNext:")
    print("- Set DB3000 settings.json com_port to your BT COM port")
    print("- Ensure baud_rate matches the module DATA baud")
    print("- Run: python test_nano_io.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
