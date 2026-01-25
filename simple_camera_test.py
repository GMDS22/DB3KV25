import cv2
import time

def test_camera():
    print("Opening camera...")
    # Try index 0 (default) or 1/2 if 0 fails
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("Index 0 failed. Trying index 1...")
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Failed to open camera on index 0 or 1")
        return

    print("Camera opened!")
    
    # Request 1280x720
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    time.sleep(1.0)
    
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f"Resolution: {w}x{h}")

    print("Reading 30 frames... (press Ctrl+C to stop early)")
    for i in range(30):
        ret, frame = cap.read()
        if not ret:
            print(f"Frame {i}: Failed to read")
        else:
            print(f"Frame {i}: Success ({frame.shape})")
        time.sleep(0.03)

    cap.release()
    print("Done.")

if __name__ == "__main__":
    test_camera()
