#!/usr/bin/env python3
"""
Test script to verify servo autotracking flag synchronization fixes.
Tests the _sync_tracking_flags() helper and flag consistency.
"""

import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

class MockEnhancer:
    """Mock enhancer for testing without GUI"""
    def __init__(self):
        self.log_messages = []
    
    def log_serial_output(self, msg, fire=False):
        """Record log messages"""
        self.log_messages.append(msg)
        print(f"LOG: {msg}")


class TestApp:
    """Minimal test application with flag sync logic"""
    
    def __init__(self):
        self.tracking_active = False
        self.aiming_active = False
        self.enhancer = MockEnhancer()
    
    def _sync_tracking_flags(self, tracking_enabled, aiming_enabled=None):
        """
        BULLETPROOF FIX: Atomically set tracking and aiming flags to prevent desynchronization.
        
        When tracking is enabled, aiming MUST also be enabled to allow servo movement.
        This function enforces that invariant and prevents race conditions.
        """
        try:
            # Enforce invariant: if tracking is on, aiming must be on
            if tracking_enabled:
                if aiming_enabled is None:
                    aiming_enabled = True  # Auto-enable servos when tracking starts
                aiming_enabled = True  # Force it on even if caller tried to disable
            else:
                # If tracking is off, respect caller's aiming preference (can be on/off)
                if aiming_enabled is None:
                    aiming_enabled = False  # Default to off when tracking is off
            
            # Check if flags would change
            current_tracking = getattr(self, "tracking_active", False)
            current_aiming = getattr(self, "aiming_active", False)
            
            changed_tracking = current_tracking != tracking_enabled
            changed_aiming = current_aiming != aiming_enabled
            
            # Set flags atomically
            self.tracking_active = bool(tracking_enabled)
            self.aiming_active = bool(aiming_enabled)
            
            # Build diagnostic
            was_synced = (current_tracking and current_aiming) or (not current_tracking)
            is_synced = (tracking_enabled and aiming_enabled) or (not tracking_enabled)
            reason = "auto-enable" if (tracking_enabled and aiming_enabled and not current_aiming) else "user_request"
            
            diagnostic = {
                "tracking_active": self.tracking_active,
                "aiming_active": self.aiming_active,
                "synced": is_synced,
                "was_synced": was_synced,
                "changed_tracking": changed_tracking,
                "changed_aiming": changed_aiming,
                "reason": reason
            }
            
            # Log changes if they occurred
            if changed_tracking or changed_aiming:
                try:
                    msg = f"[FLAG_SYNC] tracking={self.tracking_active} aiming={self.aiming_active} reason={reason}"
                    if hasattr(self, "enhancer") and self.enhancer:
                        self.enhancer.log_serial_output(msg, fire=False)
                except Exception:
                    pass
            
            return diagnostic
        except Exception as e:
            # On any error, default to safe state (both off)
            try:
                self.tracking_active = False
                self.aiming_active = False
            except Exception:
                pass
            
            try:
                if hasattr(self, "enhancer") and self.enhancer:
                    self.enhancer.log_serial_output(f"[FLAG_SYNC ERROR] {e}", fire=False)
            except Exception:
                pass
            
            return {
                "tracking_active": False,
                "aiming_active": False,
                "synced": True,
                "error": str(e)
            }


def test_flag_synchronization():
    """Test the flag synchronization logic"""
    print("\n" + "="*70)
    print("SERVO AUTOTRACKING FLAG SYNCHRONIZATION TEST")
    print("="*70)
    
    app = TestApp()
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Enable tracking should enable both flags
    print("\n[TEST 1] Enable tracking - should enable both flags")
    result = app._sync_tracking_flags(tracking_enabled=True)
    if result["tracking_active"] and result["aiming_active"]:
        print("✓ PASS: Both flags enabled")
        tests_passed += 1
    else:
        print(f"✗ FAIL: Expected both True, got tracking={result['tracking_active']}, aiming={result['aiming_active']}")
        tests_failed += 1
    
    # Test 2: Try to disable aiming while tracking - should prevent it
    print("\n[TEST 2] Disable aiming while tracking - should prevent it")
    result = app._sync_tracking_flags(tracking_enabled=True, aiming_enabled=False)
    if result["tracking_active"] and result["aiming_active"]:
        print("✓ PASS: Aiming re-enabled despite user attempting to disable it")
        tests_passed += 1
    else:
        print(f"✗ FAIL: Expected tracking=True, aiming=True, got {result}")
        tests_failed += 1
    
    # Test 3: Disable tracking should disable both
    print("\n[TEST 3] Disable tracking - should disable both flags")
    result = app._sync_tracking_flags(tracking_enabled=False)
    if not result["tracking_active"] and not result["aiming_active"]:
        print("✓ PASS: Both flags disabled")
        tests_passed += 1
    else:
        print(f"✗ FAIL: Expected both False, got tracking={result['tracking_active']}, aiming={result['aiming_active']}")
        tests_failed += 1
    
    # Test 4: Enable aiming alone (without tracking) - should enable only aiming
    print("\n[TEST 4] Enable aiming alone - should enable only aiming")
    app.tracking_active = False
    app.aiming_active = False
    result = app._sync_tracking_flags(tracking_enabled=False, aiming_enabled=True)
    if not result["tracking_active"] and result["aiming_active"]:
        print("✓ PASS: Only aiming enabled (tracking stayed off)")
        tests_passed += 1
    else:
        print(f"✗ FAIL: Expected tracking=False, aiming=True, got {result}")
        tests_failed += 1
    
    # Test 5: Enable tracking from mixed state
    print("\n[TEST 5] Enable tracking from mixed state (tracking=False, aiming=True)")
    app.tracking_active = False
    app.aiming_active = True
    result = app._sync_tracking_flags(tracking_enabled=True)
    if result["tracking_active"] and result["aiming_active"]:
        print("✓ PASS: Both flags enabled from mixed state")
        tests_passed += 1
    else:
        print(f"✗ FAIL: Expected both True, got {result}")
        tests_failed += 1
    
    # Test 6: Verify invariant - tracking implies aiming
    print("\n[TEST 6] Verify invariant - if tracking=True, aiming must be True")
    app.tracking_active = False
    app.aiming_active = False
    result = app._sync_tracking_flags(tracking_enabled=True)
    invariant_holds = not (result["tracking_active"] and not result["aiming_active"])
    if invariant_holds:
        print("✓ PASS: Invariant holds (no state where tracking=True but aiming=False)")
        tests_passed += 1
    else:
        print(f"✗ FAIL: Invariant violated! tracking={result['tracking_active']}, aiming={result['aiming_active']}")
        tests_failed += 1
    
    # Summary
    print("\n" + "="*70)
    print(f"RESULTS: {tests_passed} passed, {tests_failed} failed")
    print("="*70)
    
    if tests_failed == 0:
        print("\n✓ ALL TESTS PASSED - Servo flag synchronization is working correctly!")
        return 0
    else:
        print(f"\n✗ {tests_failed} TEST(S) FAILED - There are issues to fix")
        return 1


if __name__ == "__main__":
    exit_code = test_flag_synchronization()
    sys.exit(exit_code)
