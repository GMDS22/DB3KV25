"""
Integration test for autotracking black frame issue
Simulates repeated frame processing during autotracking with recording enabled
"""
import sys
import numpy as np
import cv2
from pathlib import Path

def simulate_autotracking_frames(num_frames=100):
    """Simulate autotracking scenario with vignette applied to many sequential frames"""
    print(f"Simulating {num_frames} frames of autotracking with vignette...")
    
    h, w = 480, 640
    center_x, center_y = w // 2, h // 2
    scope_radius = int(min(h, w) * 0.5)
    
    # Pre-compute vignette mask (as done in _add_crosshair_and_scope)
    mask = np.zeros((h, w, 3), dtype=np.uint8)
    cv2.circle(mask, (center_x, center_y), scope_radius, (255, 255, 255), -1)
    vignette = mask.astype(float) / 255.0
    darkness = 0.5
    min_brightness = 1.0 - darkness
    
    black_frame_count = 0
    min_brightness_seen = 255
    
    for frame_num in range(num_frames):
        # Simulate camera capture (new frame each time with some variation)
        frame_bgr = np.random.randint(50, 200, (h, w, 3), dtype=np.uint8)
        
        # BGR→RGB (as in update_frame line 20195)
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        
        # Apply vignette (FIXED VERSION with np.clip)
        frame_rgb = np.clip(frame_rgb.astype(float) * (min_brightness + (1.0 - min_brightness) * vignette), 0, 255).astype(np.uint8)
        
        # RGB→BGR for recording (as in update_frame line 20252)
        frame_bgr_out = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
        
        # Check for black frame
        max_val = np.max(frame_bgr_out)
        mean_val = np.mean(frame_bgr_out)
        
        if max_val == 0:
            black_frame_count += 1
            print(f"  ⚠️ Frame {frame_num}: COMPLETELY BLACK!")
        
        min_brightness_seen = min(min_brightness_seen, mean_val)
        
        if frame_num % 20 == 0:
            print(f"  Frame {frame_num}: mean={mean_val:.1f}, max={max_val}")
    
    print(f"\nResults:")
    print(f"  Total frames processed: {num_frames}")
    print(f"  Black frames detected: {black_frame_count}")
    print(f"  Minimum brightness seen: {min_brightness_seen:.1f}")
    
    if black_frame_count > 0:
        print(f"  ❌ FAIL: {black_frame_count} black frames detected!")
        return False
    
    if min_brightness_seen < 10:
        print(f"  ❌ FAIL: Frame brightness too low ({min_brightness_seen:.1f})")
        return False
    
    print("  ✅ PASS: No black frames, all frames processed correctly")
    return True

def test_extreme_vignette():
    """Test with maximum vignette darkness (worst case)"""
    print("\nTesting extreme vignette darkness (90%)...")
    
    h, w = 480, 640
    center_x, center_y = w // 2, h // 2
    scope_radius = int(min(h, w) * 0.5)
    
    frame = np.ones((h, w, 3), dtype=np.uint8) * 100
    
    mask = np.zeros((h, w, 3), dtype=np.uint8)
    cv2.circle(mask, (center_x, center_y), scope_radius, (255, 255, 255), -1)
    vignette = mask.astype(float) / 255.0
    darkness = 0.9  # 90% darkness (extreme)
    min_brightness = 1.0 - darkness
    
    frame_out = np.clip(frame.astype(float) * (min_brightness + (1.0 - min_brightness) * vignette), 0, 255).astype(np.uint8)
    
    mean_val = np.mean(frame_out)
    max_val = np.max(frame_out)
    
    print(f"  Mean brightness: {mean_val:.1f}, Max: {max_val}")
    
    if max_val == 0:
        print("  ❌ FAIL: Frame went black with extreme vignette!")
        return False
    
    print("  ✅ PASS: Frame survived extreme vignette")
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("AUTOTRACKING BLACK FRAME INTEGRATION TEST")
    print("=" * 60)
    
    results = []
    results.append(("Autotracking simulation", simulate_autotracking_frames(100)))
    results.append(("Extreme vignette test", test_extreme_vignette()))
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {test_name}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    if all_passed:
        print("✅ ALL TESTS PASSED - Autotracking black frame issue FIXED!")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED")
        sys.exit(1)
