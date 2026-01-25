import serial
import time

def test_nano_io(port="COM8", baud=115200):
    print(f"Opening Nano on {port} at {baud}...")
    try:
        ser = serial.Serial(port, baud, timeout=1.0)
        time.sleep(2) # Wait for reset
        print("Nano opened.")
        
        # Helper to send and print
        def send(cmd):
            print(f"Sending: {cmd.strip()}")
            ser.write(cmd.encode('ascii'))
            time.sleep(1.0) # Visual observation time

        # Disable internal Bus Servo helper on Nano (as we are using Dual Mode)
        send("PTEN 0\n")

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
        print("\nTest Complete. If you saw the LED/Laser/Solenoid activate, the Nano is working correctly.")

    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_nano_io()
