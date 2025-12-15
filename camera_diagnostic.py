#!/usr/bin/env python3
"""
DADBOT Camera Resolution Diagnostic Tool
Tests which resolutions your camera actually supports
Run this BEFORE making changes to understand your camera's capabilities
"""

import cv2
import sys

def test_camera_resolution():
    print("=" * 80)
    print("DADBOT CAMERA RESOLUTION DIAGNOSTIC TOOL")
    print("=" * 80)
    
    backends = [
        (cv2.CAP_DSHOW, "DSHOW (DirectShow)"),
        (cv2.CAP_MSMF, "MSMF (Media Foundation)"),
        (0, "CAP_ANY (Auto-detect)"),
    ]
    
    working_backend = None
    
    for backend_id, backend_name in backends:
        print(f"\n[TEST] Trying backend: {backend_name}")
        try:
            cap = cv2.VideoCapture(0, backend_id)
            if cap.isOpened():
                print(f"  ✓ {backend_name} WORKS")
                working_backend = (backend_id, backend_name, cap)
                break
            else:
                print(f"  ✗ {backend_name} failed to open")
                cap.release()
        except Exception as e:
            print(f"  ✗ {backend_name} exception: {e}")
            continue
    
    if not working_backend:
        print("\n[ERROR] No backend could open camera!")
        return
    
    backend_id, backend_name, cap = working_backend
    print(f"\n[SUCCESS] Using backend: {backend_name}")
    
    # Get current properties
    print("\n" + "=" * 80)
    print("CURRENT CAMERA PROPERTIES")
    print("=" * 80)
    print(f"  Width:        {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}")
    print(f"  Height:       {int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
    print(f"  FPS:          {cap.get(cv2.CAP_PROP_FPS)}")
    print(f"  Buffer Size:  {int(cap.get(cv2.CAP_PROP_BUFFERSIZE))}")
    
    # Test resolutions
    test_resolutions = [
        (640, 480),
        (800, 600),
        (1024, 768),
        (1280, 720),
        (1600, 900),
        (1920, 1080),
        (2560, 1440),
    ]
    
    print("\n" + "=" * 80)
    print("TESTING SUPPORTED RESOLUTIONS")
    print("=" * 80)
    
    supported = []
    
    for width, height in test_resolutions:
        # Set resolution
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        
        # Small delay
        import time
        time.sleep(0.05)
        
        # Try to grab a frame
        ret, frame = cap.read()
        
        if ret and frame is not None:
            frame_h, frame_w = frame.shape[:2]
            status = "✓ EXACT" if (frame_w == width and frame_h == height) else f"⚠ DELIVERED {frame_w}x{frame_h}"
            print(f"  {width:4d}x{height:4d}  →  {status}")
            supported.append((width, height, frame_w, frame_h))
        else:
            print(f"  {width:4d}x{height:4d}  →  ✗ FAILED")
    
    # Find best resolution
    print("\n" + "=" * 80)
    print("ANALYSIS & RECOMMENDATION")
    print("=" * 80)
    
    if supported:
        # Get exact matches (no downscaling)
        exact_matches = [(w, h) for w, h, fw, fh in supported if w == fw and h == fh]
        
        if exact_matches:
            # Sort by area (largest first)
            exact_matches.sort(key=lambda x: x[0] * x[1], reverse=True)
            best_w, best_h = exact_matches[0]
            print(f"\n✓ RECOMMENDED RESOLUTION: {best_w}x{best_h}")
            print(f"  (Your camera delivers this EXACTLY without downscaling)\n")
            
            print(f"✓ ALL SUPPORTED RESOLUTIONS (exact match):")
            for w, h in sorted(exact_matches, key=lambda x: x[0]*x[1], reverse=True):
                print(f"    • {w}x{h}")
        else:
            print("\n⚠ No exact matches found, camera provides downscaled versions")
            print("\n✓ Resolutions delivered (possibly downscaled):")
            delivered = set((fw, fh) for _, _, fw, fh in supported)
            for w, h in sorted(delivered, key=lambda x: x[0]*x[1], reverse=True):
                print(f"    • {w}x{h}")
    else:
        print("\n✗ No resolutions could be tested successfully")
    
    cap.release()
    
    print("\n" + "=" * 80)
    print("DIAGNOSTIC COMPLETE")
    print("=" * 80)
    print("\nUse the recommended resolution in the app configuration.")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    test_camera_resolution()
