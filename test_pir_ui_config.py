#!/usr/bin/env python3
"""
Quick verification test for PIR UI integration.
Tests that config dataclasses exist, serialize/deserialize properly,
and UI spinbox ranges are appropriate.
"""

import json
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.sentry_v2_config import (
    SentryV2Config,
    PIRSensorConfig,
    PIRGuardConfig,
    SENTRY_PAN_MIN,
    SENTRY_PAN_MAX,
    SENTRY_TILT_MIN,
    SENTRY_TILT_MAX,
)
from app.sentry_v2.sentry_v2_engine import SentryV2Engine, SentryV2State


def test_pir_config_structure():
    """Test that PIR config dataclasses are properly structured."""
    print("[Test 1/5] PIR Config Structure...")
    
    # Create default config
    config = SentryV2Config()
    
    # Verify pir_guard exists and has correct defaults
    assert hasattr(config, 'pir_guard'), "Config missing pir_guard field"
    assert config.pir_guard.pir_enabled == False, "pir_enabled should default to False"
    assert len(config.pir_guard.sensors) == 3, "Should have 3 PIR sensors"
    
    # Verify first sensor has correct defaults
    sensor_0 = config.pir_guard.sensors[0]
    assert isinstance(sensor_0, PIRSensorConfig), "sensors[] should contain PIRSensorConfig"
    assert hasattr(sensor_0, 'cue_pan'), "Sensor missing cue_pan"
    assert hasattr(sensor_0, 'cue_tilt'), "Sensor missing cue_tilt"
    assert hasattr(sensor_0, 'enabled'), "Sensor missing enabled"
    assert hasattr(sensor_0, 'debounce_ms'), "Sensor missing debounce_ms"
    assert sensor_0.enabled == False, "Sensors should default to disabled"
    
    print("  ✓ PIR config structure correct")


def test_pir_config_serialization():
    """Test JSON serialization/deserialization."""
    print("[Test 2/5] PIR Config Serialization...")
    
    # Create config and modify PIR settings
    config = SentryV2Config()
    config.pir_guard.pir_enabled = True
    config.pir_guard.sensors[0].enabled = True
    config.pir_guard.sensors[0].cue_pan = 270.0
    config.pir_guard.sensors[0].cue_tilt = 45.0
    config.pir_guard.scan_pan_range = 30.0
    config.pir_guard.scan_grid_resolution = 4
    config.pir_guard.cue_hold_time_s = 0.12
    config.pir_guard.search_style = "fast_reacquire"
    config.pir_guard.search_rounds = 2
    
    # Serialize to dict
    config_dict = config.to_dict()
    assert 'pir_guard' in config_dict, "to_dict() missing pir_guard"
    
    # Verify nested structure
    pir_dict = config_dict['pir_guard']
    assert pir_dict['pir_enabled'] == True, "Serialized pir_enabled not preserved"
    assert pir_dict['sensors'][0]['enabled'] == True, "Serialized sensor[0].enabled not preserved"
    assert pir_dict['sensors'][0]['cue_pan'] == 270.0, "Serialized cue_pan not preserved"
    assert pir_dict['scan_grid_resolution'] == 4, "Serialized grid resolution not preserved"
    assert pir_dict['cue_hold_time_s'] == 0.12, "Serialized cue hold not preserved"
    assert pir_dict['search_style'] == "fast_reacquire", "Serialized search style not preserved"
    assert pir_dict['search_rounds'] == 2, "Serialized search rounds not preserved"
    
    # Deserialize back
    config2 = SentryV2Config.from_dict(config_dict)
    assert config2.pir_guard.pir_enabled == True, "Deserialized pir_enabled lost"
    assert config2.pir_guard.sensors[0].enabled == True, "Deserialized sensor[0].enabled lost"
    assert config2.pir_guard.sensors[0].cue_pan == 270.0, "Deserialized cue_pan lost"
    assert config2.pir_guard.scan_grid_resolution == 4, "Deserialized grid resolution lost"
    assert config2.pir_guard.cue_hold_time_s == 0.12, "Deserialized cue hold lost"
    assert config2.pir_guard.search_style == "fast_reacquire", "Deserialized search style lost"
    assert config2.pir_guard.search_rounds == 2, "Deserialized search rounds lost"
    
    print("  ✓ PIR config serialization/deserialization working")


def test_pir_sensor_angles():
    """Test that sensor cue angles respect turret limits."""
    print("[Test 3/5] PIR Sensor Angle Validation...")
    
    config = SentryV2Config()
    
    # Test that default angles are within limits
    for i, sensor in enumerate(config.pir_guard.sensors):
        assert SENTRY_PAN_MIN <= sensor.cue_pan <= SENTRY_PAN_MAX, \
            f"Sensor {i} cue_pan {sensor.cue_pan} out of range [{SENTRY_PAN_MIN}, {SENTRY_PAN_MAX}]"
        assert SENTRY_TILT_MIN <= sensor.cue_tilt <= SENTRY_TILT_MAX, \
            f"Sensor {i} cue_tilt {sensor.cue_tilt} out of range [{SENTRY_TILT_MIN}, {SENTRY_TILT_MAX}]"
    
    # Test that we can set valid angles
    config.pir_guard.sensors[0].cue_pan = SENTRY_PAN_MAX
    config.pir_guard.sensors[1].cue_tilt = SENTRY_TILT_MAX
    config.pir_guard.sensors[2].cue_pan = SENTRY_PAN_MIN
    
    # Verify they persist
    assert config.pir_guard.sensors[0].cue_pan == SENTRY_PAN_MAX
    assert config.pir_guard.sensors[1].cue_tilt == SENTRY_TILT_MAX
    assert config.pir_guard.sensors[2].cue_pan == SENTRY_PAN_MIN
    
    print("  ✓ PIR sensor angles validated")


def test_pir_scan_settings():
    """Test PIR scan grid settings."""
    print("[Test 4/5] PIR Scan Settings Validation...")
    
    config = SentryV2Config()
    pg = config.pir_guard
    
    # Verify defaults are sensible
    assert 5 <= pg.scan_pan_range <= 90, "scan_pan_range out of expected range"
    assert 5 <= pg.scan_tilt_range <= 90, "scan_tilt_range out of expected range"
    assert 2 <= pg.scan_grid_resolution <= 6, "scan_grid_resolution out of expected range"
    assert 1 <= pg.scan_speed <= 30, "scan_speed out of expected range"
    assert 0.05 <= pg.cue_hold_time_s <= 2.0, "cue_hold_time_s out of expected range"
    assert 0.5 <= pg.confirmation_timeout <= 10, "confirmation_timeout out of expected range"
    assert pg.scan_pan_range == 45.0, "scan_pan_range should default to 45 degrees"
    assert pg.scan_tilt_range == 45.0, "scan_tilt_range should default to 45 degrees"
    assert pg.search_rounds == 1, "search_rounds should default to 1"
    assert isinstance(pg.scan_on_no_detect, bool), "scan_on_no_detect should be bool"
    
    # Test modifications
    pg.scan_grid_resolution = 5
    pg.cue_hold_time_s = 0.10
    pg.confirmation_timeout = 2.5
    pg.scan_on_no_detect = False
    pg.search_style = "hunting"
    pg.search_rounds = 3
    
    assert pg.scan_grid_resolution == 5
    assert pg.cue_hold_time_s == 0.10
    assert pg.confirmation_timeout == 2.5
    assert pg.scan_on_no_detect == False
    assert pg.search_style == "hunting"
    assert pg.search_rounds == 3
    
    print("  ✓ PIR scan settings validated")


def test_pir_manager_creation():
    """Test that PIRManager can be instantiated with config."""
    print("[Test 5/5] PIR Manager Creation...")
    
    from app.sentry_v2.sentry_v2_pir_manager import SentryV2PIRManager
    
    config = SentryV2Config()
    pg = config.pir_guard
    
    # Create manager
    manager = SentryV2PIRManager(pg)
    
    # Verify manager methods exist
    assert hasattr(manager, 'on_pir_event'), "Manager missing on_pir_event method"
    assert hasattr(manager, 'get_next_cue'), "Manager missing get_next_cue method"
    assert hasattr(manager, 'generate_scan_grid'), "Manager missing generate_scan_grid method"
    assert hasattr(manager, 'get_status_text'), "Manager missing get_status_text method"
    
    # Get initial status
    status = manager.get_status_text()
    assert isinstance(status, str), "get_status_text should return string"
    
    print(f"  ✓ PIR manager created successfully")
    print(f"    Initial status: {status}")


def test_pir_no_detect_returns_guard_home():
    """Verify PIR no-target completion commands the configured guard/home position."""
    print("[Test 6/6] PIR No-Detect Return Home...")

    config = SentryV2Config()
    config.guard.guard_mode = 0
    config.guard.guard_pan = 135.0
    config.guard.guard_tilt = 35.0
    config.pir_guard.pir_enabled = True
    config.pir_guard.scan_on_no_detect = True
    config.pir_guard.cue_hold_time_s = 0.05
    config.pir_guard.scan_grid_resolution = 2
    config.pir_guard.scan_speed = 12.0
    config.pir_guard.sensors[0].enabled = True
    config.pir_guard.sensors[0].cue_pan = 210.0
    config.pir_guard.sensors[0].cue_tilt = 55.0

    engine = SentryV2Engine(config)
    engine.start()
    engine.on_pir_sensor_fired(0, 1.0)

    now = 1.0
    for _ in range(60):
        now += 0.6
        engine.update([], now)
        if not engine._pir_cue_mode:
            break

    assert engine.state == SentryV2State.GUARDING, "Engine should remain in guarding after PIR no-detect completion"
    assert engine.current_pan == config.guard.guard_pan, "PIR no-detect completion should command guard pan"
    assert engine.current_tilt == config.guard.guard_tilt, "PIR no-detect completion should command guard tilt"
    assert engine._pir_cue_mode == False, "PIR cue mode should be cleared after no-detect completion"
    assert engine._pir_scan_mode == False, "PIR scan mode should be cleared after no-detect completion"

    print("  ✓ PIR no-detect completion returns to configured guard/home position")


def test_paused_pir_events_do_not_queue_stale_motion():
    """Verify PIR hits received while paused do not trigger a stale cue on enable."""
    print("[Test 7/7] Ignore Paused PIR Events...")

    config = SentryV2Config()
    config.guard.guard_pan = 140.0
    config.guard.guard_tilt = 87.0
    config.pir_guard.pir_enabled = True
    config.pir_guard.sensors[0].enabled = True
    config.pir_guard.sensors[0].cue_pan = 270.0
    config.pir_guard.sensors[0].cue_tilt = 55.0

    engine = SentryV2Engine(config)

    engine.on_pir_sensor_fired(0, 1.0)
    engine.start()

    assert engine.state == SentryV2State.GUARDING, "Engine should be guarding after start"
    assert engine.current_pan == config.guard.guard_pan, "Start should move to guard pan, not a stale PIR cue"
    assert engine.current_tilt == config.guard.guard_tilt, "Start should move to guard tilt, not a stale PIR cue"
    assert engine._pir_cue_mode == False, "Paused PIR events should not arm PIR cue mode"
    assert engine._pir_manager.peek_queue_count() == 0, "Paused PIR events should not remain queued after start"

    print("  ✓ Paused PIR events no longer queue stale startup motion")


def main():
    print("\n=== SMART SENTRY V3 PIR UI Configuration Tests ===\n")
    
    try:
        test_pir_config_structure()
        test_pir_config_serialization()
        test_pir_sensor_angles()
        test_pir_scan_settings()
        test_pir_manager_creation()
        test_pir_no_detect_returns_guard_home()
        test_paused_pir_events_do_not_queue_stale_motion()
        
        print("\n✓ All 7 tests passed!\n")
        return 0
    
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}\n")
        return 1
    
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}\n")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
