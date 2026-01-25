#!/usr/bin/env python3
"""
Simple test to verify resolution configuration is working correctly.
Tests that frame_width and frame_height are only modified in appropriate places.
"""

import re
import sys

def test_resolution_configuration():
    """Verify resolution configuration follows the new rules."""
    
    print("=" * 70)
    print("RESOLUTION CONFIGURATION TEST")
    print("=" * 70)
    
    with open('app/MAIN_FILE_SINGLE_CAM.py', 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    # Test 1: Find all frame_width assignments
    print("\n1. Checking frame_width assignments...")
    frame_width_assignments = []
    for i, line in enumerate(lines, 1):
        # Skip print statements and comments
        if re.search(r'self\.frame_width\s*=(?!=)', line) and not line.strip().startswith('#') and 'print' not in line.lower():
            frame_width_assignments.append((i, line.strip()))
    
    print(f"   Found {len(frame_width_assignments)} frame_width assignments:")
    for line_num, line_text in frame_width_assignments:
        print(f"   Line {line_num}: {line_text[:80]}")
    
    # Test 2: Find all frame_height assignments
    print("\n2. Checking frame_height assignments...")
    frame_height_assignments = []
    for i, line in enumerate(lines, 1):
        # Skip print statements and comments
        if re.search(r'self\.frame_height\s*=(?!=)', line) and not line.strip().startswith('#') and 'print' not in line.lower():
            frame_height_assignments.append((i, line.strip()))
    
    print(f"   Found {len(frame_height_assignments)} frame_height assignments:")
    for line_num, line_text in frame_height_assignments:
        print(f"   Line {line_num}: {line_text[:80]}")
    
    # Test 3: Verify we have exactly 3 assignments for each
    print("\n3. Verifying correct number of assignments...")
    expected_count = 3
    
    if len(frame_width_assignments) == expected_count:
        print(f"   PASS frame_width: {len(frame_width_assignments)} assignments (expected {expected_count})")
    else:
        print(f"   ❌ frame_width: {len(frame_width_assignments)} assignments (expected {expected_count})")
        return False
    
    if len(frame_height_assignments) == expected_count:
        print(f"   PASS frame_height: {len(frame_height_assignments)} assignments (expected {expected_count})")
    else:
        print(f"   ❌ frame_height: {len(frame_height_assignments)} assignments (expected {expected_count})")
        return False
    
    # Test 4: Verify no assignments in update_frame method
    print("\n4. Checking update_frame method for illegal assignments...")
    
    # Find the update_frame method
    update_frame_start = None
    update_frame_end = None
    
    for i, line in enumerate(lines):
        if 'def update_frame(self):' in line:
            update_frame_start = i
        elif update_frame_start is not None and re.match(r'\s*def\s+\w+', line):
            update_frame_end = i
            break
    
    if update_frame_start is None:
        print("   ⚠️  Could not find update_frame method")
        return False
    
    if update_frame_end is None:
        update_frame_end = len(lines)
    
    print(f"   update_frame method: lines {update_frame_start+1} to {update_frame_end}")
    
    # Check for assignments within update_frame
    illegal_assignments = []
    for i in range(update_frame_start, update_frame_end):
        line = lines[i]
        if not line.strip().startswith('#') and 'print' not in line.lower():
            if re.search(r'self\.frame_width\s*=(?!=)', line) or re.search(r'self\.frame_height\s*=(?!=)', line):
                illegal_assignments.append((i+1, line.strip()))
    
    if illegal_assignments:
        print(f"   ❌ Found {len(illegal_assignments)} illegal assignments in update_frame:")
        for line_num, line_text in illegal_assignments:
            print(f"      Line {line_num}: {line_text[:80]}")
        return False
    else:
        print("   PASS No illegal assignments found in update_frame")
    
    # Test 5: Verify warning comments exist
    print("\n5. Checking for protective warning comments...")

    def _find_line_index(needle: str):
        for idx, ln in enumerate(lines):
            if needle in ln:
                return idx
        return None

    def _find_regex_index(pattern: str):
        rx = re.compile(pattern)
        for idx, ln in enumerate(lines):
            if rx.search(ln):
                return idx
        return None

    def _section_has_warning(start_idx: int, end_idx: int) -> bool:
        if start_idx is None:
            return False
        start_idx = max(0, int(start_idx))
        end_idx = min(len(lines), int(end_idx))
        if end_idx <= start_idx:
            end_idx = min(len(lines), start_idx + 120)
        section_text = "\n".join(lines[start_idx:end_idx]).upper()
        return ("DO NOT" in section_text) or ("WARNING" in section_text) or ("CRITICAL" in section_text)

    checks = []

    # 5a) Resolution configuration section (init defaults)
    idx_res_cfg = _find_line_index("# ⚠️ CRITICAL: TO CHANGE RESOLUTION")
    checks.append(("Resolution configuration section", idx_res_cfg, (idx_res_cfg + 60) if idx_res_cfg is not None else None))

    # 5b) Camera opening section
    idx_open_camera = _find_regex_index(r"^\s*def\s+open_camera\(")
    checks.append(("Camera opening section", idx_open_camera, (idx_open_camera + 220) if idx_open_camera is not None else None))

    # 5c) Resolution change handler (look for the specific comment marker)
    idx_res_change = _find_line_index("# ⚠️ CRITICAL: Update frame dimensions when resolution changes")
    if idx_res_change is None:
        idx_res_change = _find_line_index("# ⚠️ CRITICAL: Update frame_width/height with ACTUAL camera resolution")
    checks.append(("Resolution change handler", idx_res_change, (idx_res_change + 80) if idx_res_change is not None else None))

    # 5d) update_frame warning section
    idx_update_frame = _find_regex_index(r"^\s*def\s+update_frame\(self\):")
    checks.append(("update_frame warning section", idx_update_frame, (idx_update_frame + 120) if idx_update_frame is not None else None))

    all_warnings_present = True
    for section_name, start_idx, end_idx in checks:
        if start_idx is None:
            print(f"   ⚠️  {section_name}: Could not locate section")
            all_warnings_present = False
            continue
        if _section_has_warning(start_idx, end_idx):
            print(f"   PASS {section_name}: Warning comments present")
        else:
            print(f"   ❌ {section_name}: Warning comments MISSING")
            all_warnings_present = False

    if not all_warnings_present:
        return False
    
    # All tests passed
    print("\n" + "=" * 70)
    print("ALL TESTS PASSED")
    print("=" * 70)
    print("\nResolution configuration is properly implemented:")
    print("  • Exactly 3 assignments to frame_width/height (init, camera open, resolution change)")
    print("  • No assignments in update_frame method")
    print("  • Protective warning comments in all critical sections")
    print("\nThe fix successfully prevents future errors!")
    return True

if __name__ == "__main__":
    success = test_resolution_configuration()
    sys.exit(0 if success else 1)
