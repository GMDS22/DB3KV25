import serial
import time

def test_io_board(port="COM10", baud=115200):
    print(f"Opening IO board (ESP32) on {port} at {baud}...")
    try:
        ser = serial.Serial(port, baud, timeout=1.0)
        time.sleep(2) # Wait for reset
        print("IO board opened.")
        
        # Helper to send and print
        def send(cmd):
            print(f"Sending: {cmd.strip()}")
            ser.write(cmd.encode('ascii'))
            time.sleep(1.0) # Visual observation time

        print("\n--- TESTING LED (L1/L0) ---")
        send("L1\n")
        send("L0\n")

        print("\n--- TESTING LASER (R1/R0) ---")
        send("R1\n")
        send("R0\n")
        
        print("\n--- TESTING WATER TRIGGER (M0, S0, F1/F0) ---")
        send("M0\n") # Water mode
        send("S0\n") # Arm safety
        send("F1\n") # Fire
        send("F0\n") # Stop
        send("S1\n") # Safety On

        ser.close()
        print("\nTest Complete. If you saw the LED/Laser/trigger outputs activate, the ESP32 IO board is working correctly.")

    except Exception as e:
        print(f"ERROR: {e}")


def test_nano_io(port="COM10", baud=115200):
    # Backward-compatible wrapper
    return test_io_board(port=port, baud=baud)

if __name__ == "__main__":
    test_io_board()
