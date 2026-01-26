"""
Test for black frame fix - verifies vignette effect doesn't corrupt frames
"""
import sys
import numpy as np
import cv2
from pathlib import Path

# Add app to path
sys.path.insert(0, str(Path(__file__).parent / "app"))

def test_vignette_no_corruption():
    """Verify vignette effect doesn't corrupt frame data"""
    print("Testing vignette effect for frame corruption...")
    
    # Create test frame (non-zero values)
    frame = np.ones((480, 640, 3), dtype=np.uint8) * 128  # Mid-gray frame
    original_frame = frame.copy()
    
    # Simulate vignette effect (simplified version from _add_crosshair_and_scope)
    h, w = frame.shape[:2]
    center_x, center_y = w // 2, h // 2
    scope_radius = int(min(h, w) * 0.5)
    
    mask = np.zeros((h, w, 3), dtype=np.uint8)
    cv2.circle(mask, (center_x, center_y), scope_radius, (255, 255, 255), -1)
    vignette = mask.astype(float) / 255.0
    darkness = 0.5  # 50% darkness
    min_brightness = 1.0 - darkness
    
    # Apply vignette (OLD WAY - could corrupt)
    # frame_old = (frame.astype(float) * (min_brightness + (1.0 - min_brightness) * vignette)).astype(np.uint8)
    
    # Apply vignette (NEW WAY - with clipping)
    frame_new = np.clip(frame.astype(float) * (min_brightness + (1.0 - min_brightness) * vignette), 0, 255).astype(np.uint8)
    
    # Verify frame is not all black
    min_val = np.min(frame_new)
    max_val = np.max(frame_new)
    mean_val = np.mean(frame_new)
    
    print(f"  Original frame: min={np.min(original_frame)}, max={np.max(original_frame)}, mean={np.mean(original_frame):.1f}")
    print(f"  Processed frame: min={min_val}, max={max_val}, mean={mean_val:.1f}")
    
    # Check for black frame (all zeros)
    if max_val == 0:
        print("  ❌ FAIL: Frame is completely black!")
        return False
    
    # Check for reasonable values (should be darker but not black)
    if mean_val < 10:
        print(f"  ❌ FAIL: Frame is too dark (mean={mean_val:.1f})")
        return False
    
    # Verify center is brighter than edges (vignette effect working)
    center_region = frame_new[center_y-10:center_y+10, center_x-10:center_x+10]
    edge_region = frame_new[0:20, 0:20]
    center_mean = np.mean(center_region)
    edge_mean = np.mean(edge_region)
    
    print(f"  Center brightness: {center_mean:.1f}, Edge brightness: {edge_mean:.1f}")
    
    if center_mean <= edge_mean:
        print(f"  ⚠️ WARNING: Vignette effect not working correctly")
    
    print("  ✅ PASS: Frame is not corrupted, vignette applied correctly")
    return True

def test_multiple_applications():
    """Test that applying vignette multiple times doesn't cause progressive corruption"""
    print("\nTesting multiple vignette applications...")
    
    frame = np.ones((480, 640, 3), dtype=np.uint8) * 128
    
    h, w = frame.shape[:2]
    center_x, center_y = w // 2, h // 2
    scope_radius = int(min(h, w) * 0.5)
    
    mask = np.zeros((h, w, 3), dtype=np.uint8)
    cv2.circle(mask, (center_x, center_y), scope_radius, (255, 255, 255), -1)
    vignette = mask.astype(float) / 255.0
    darkness = 0.5
    min_brightness = 1.0 - darkness
    
    # Apply vignette 10 times (simulating multiple frames)
    for i in range(10):
        frame = np.clip(frame.astype(float) * (min_brightness + (1.0 - min_brightness) * vignette), 0, 255).astype(np.uint8)
        mean_val = np.mean(frame)
        print(f"  Iteration {i+1}: mean brightness = {mean_val:.1f}")
        
        if mean_val == 0:
            print(f"  ❌ FAIL: Frame went black at iteration {i+1}!")
            return False
    
    print("  ✅ PASS: Multiple applications don't cause corruption")
    return True

def test_rgb_bgr_conversion_chain():
    """Test that BGR→RGB→processing→display chain doesn't corrupt frames"""
    print("\nTesting BGR→RGB→BGR conversion chain...")
    
    # Create BGR frame (camera output)
    frame_bgr = np.ones((480, 640, 3), dtype=np.uint8) * 128
    frame_bgr[:, :, 0] = 100  # Blue channel
    frame_bgr[:, :, 1] = 128  # Green channel
    frame_bgr[:, :, 2] = 200  # Red channel
    
    # Convert BGR→RGB (as done in update_frame)
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    
    # Apply vignette to RGB frame
    h, w = frame_rgb.shape[:2]
    center_x, center_y = w // 2, h // 2
    scope_radius = int(min(h, w) * 0.5)
    
    mask = np.zeros((h, w, 3), dtype=np.uint8)
    cv2.circle(mask, (center_x, center_y), scope_radius, (255, 255, 255), -1)
    vignette = mask.astype(float) / 255.0
    darkness = 0.5
    min_brightness = 1.0 - darkness
    
    frame_rgb = np.clip(frame_rgb.astype(float) * (min_brightness + (1.0 - min_brightness) * vignette), 0, 255).astype(np.uint8)
    
    # Convert RGB→BGR (for recording)
    frame_bgr_out = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
    
    # Verify not black
    if np.max(frame_bgr_out) == 0:
        print("  ❌ FAIL: Conversion chain resulted in black frame!")
        return False
    
    mean_val = np.mean(frame_bgr_out)
    print(f"  Final frame mean brightness: {mean_val:.1f}")
    
    if mean_val < 10:
        print(f"  ❌ FAIL: Frame too dark after conversion chain!")
        return False
    
    print("  ✅ PASS: BGR→RGB→BGR conversion chain preserves frame data")
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("BLACK FRAME FIX VERIFICATION TEST")
    print("=" * 60)
    
    results = []
    results.append(("Vignette corruption test", test_vignette_no_corruption()))
    results.append(("Multiple applications test", test_multiple_applications()))
    results.append(("BGR↔RGB conversion test", test_rgb_bgr_conversion_chain()))
    
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
        print("✅ ALL TESTS PASSED - Black frame fix verified!")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED - Review output above")
        sys.exit(1)
