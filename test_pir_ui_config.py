#!/usr/bin/env python3
"""
Quick verification test for PIR UI integration.
Tests that config dataclasses exist, serialize/deserialize properly,
and UI spinbox ranges are appropriate.
"""

import json
import sys
import time
from pathlib import Path
from types import SimpleNamespace

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
from app.sentry_v2.sentry_v2_comm import SentryV2Comm
from app.sentry_v2.sentry_v2_engine import SentryV2Engine, SentryV2State
from app.sentry_v2.sentry_v2_pir_manager import SentryV2PIRManager
from app.sentry_v2.sentry_v2_tab import (
    MANUAL_TRIGGER_SERVO_LATCH_MS,
    SentryV2TabWidget,
    _build_pin_assignment_dialog_content,
)


def test_pir_config_structure():
    """Test that PIR config dataclasses are properly structured."""
    print("[Test 1/9] PIR Config Structure...")
    
    # Create default config
    config = SentryV2Config()
    
    # Verify pir_guard exists and has correct defaults
    assert hasattr(config, 'pir_guard'), "Config missing pir_guard field"
    assert config.pir_guard.pir_enabled == False, "pir_enabled should default to False"
    assert len(config.pir_guard.sensors) == 3, "Should have 3 PIR sensors"
    assert config.pir_guard.cross_sensor_lockout_ms == 120, "cross_sensor_lockout_ms should default to 120"
    
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
    print("[Test 2/9] PIR Config Serialization...")
    
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
    print("[Test 3/9] PIR Sensor Angle Validation...")
    
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
    print("[Test 4/9] PIR Scan Settings Validation...")
    
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
    assert pg.cross_sensor_lockout_ms == 120, "cross_sensor_lockout_ms should default to 120 ms"
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
    print("[Test 5/9] PIR Manager Creation...")
    
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


def test_cross_sensor_lockout_allows_adjacent_hits_after_short_window():
    """Verify different PIR sensors are not suppressed for nearly a full second."""
    print("[Test 6/9] Cross-Sensor Lockout Window...")

    config = SentryV2Config()
    config.pir_guard.pir_enabled = True
    config.pir_guard.sensors[0].enabled = True
    config.pir_guard.sensors[1].enabled = True

    manager = SentryV2PIRManager(config.pir_guard)
    manager.on_pir_event(0, 1.0)
    manager.on_pir_event(1, 1.05)
    assert manager.peek_queue_count() == 1, "Second sensor should still respect the short overlap guard"

    manager.on_pir_event(1, 1.13)
    assert manager.peek_queue_count() == 2, "Second sensor should queue once the short cross-sensor guard clears"

    print("  ✓ Adjacent PIR hits can queue after the shorter cross-sensor window")


def test_engine_pir_stats_surface_search_progress():
    """Verify PIR search state is exposed through engine stats for the UI/log pane."""
    print("[Test 7/9] PIR Search Stats Visibility...")

    config = SentryV2Config()
    config.guard.guard_mode = 0
    config.guard.guard_pan = 135.0
    config.guard.guard_tilt = 35.0
    config.pir_guard.pir_enabled = True
    config.pir_guard.scan_on_no_detect = True
    config.pir_guard.cue_hold_time_s = 0.05
    config.pir_guard.search_style = "fast_reacquire"
    config.pir_guard.scan_grid_resolution = 2
    config.pir_guard.scan_speed = 12.0
    config.pir_guard.sensors[0].enabled = True
    config.pir_guard.sensors[0].cue_pan = 210.0
    config.pir_guard.sensors[0].cue_tilt = 55.0

    engine = SentryV2Engine(config)
    engine.start()
    now = time.time()
    engine.on_pir_sensor_fired(0, now)
    engine.update([], now + 0.2)

    stats = engine.get_engagement_stats()
    assert stats["pir_cue_mode"] == True, "PIR cue mode should still be active during the local search"
    assert stats["pir_scan_mode"] == True, "PIR scan mode should be exposed during no-target search"
    assert stats["pir_recent"] == True, "Recent PIR note should be flagged for the UI"
    assert "PIR search" in stats["pir_note"], "PIR search note should be exposed for logging"
    assert str(stats["pir_status"]).startswith("PIR: scanning s1"), "PIR status should report scanning progress"

    print("  ✓ Engine stats expose PIR search note and scanning status")


def test_pir_no_detect_returns_guard_home():
    """Verify PIR no-target completion commands the configured guard/home position."""
    print("[Test 8/9] PIR No-Detect Return Home...")

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
    print("[Test 9/9] Ignore Paused PIR Events...")

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


def test_comm_parses_active_firmware_pir_serial_lines_and_logs_transport():
    """Verify comm parsing matches the active firmware's PIR serial log format."""
    print("[Test 10/11] Comm PIR Serial Parse + Transport Log...")

    comm = SentryV2Comm()
    events = []
    transport_logs = []
    comm.set_on_pir_event(lambda sensor_id, timestamp: events.append((sensor_id, timestamp)))
    comm.set_on_transport_log(lambda message: transport_logs.append(str(message)))

    comm._handle_serial_line("[PIR] Sensor 2 triggered (GPIO39) t=1234")

    assert len(events) == 1, "Firmware PIR serial line should dispatch one PIR event"
    assert events[0][0] == 2, "Parsed PIR sensor index should match the firmware log"
    assert abs(events[0][1] - 1.234) < 0.0001, "Parsed PIR timestamp should convert from ms to seconds"
    assert any("ESP32 USB RX [PIR] Sensor 2 triggered" in message for message in transport_logs), "Raw serial line should be surfaced to the transport log"

    print("  ✓ Active firmware PIR serial lines reach the UI log and PIR callback")


def test_comm_udp_state_trace_is_visible_without_flooding_duplicates():
    """Verify WiFi modes emit visible state trace lines without spamming duplicates every packet."""
    print("[Test 11/11] UDP State Trace Visibility...")

    comm = SentryV2Comm()
    transport_logs = []
    comm.set_on_transport_log(lambda message: transport_logs.append(str(message)))

    first_state = json.dumps({
        "v": 1,
        "t": "state",
        "ts": 1000,
        "p": {"safety": 1, "mode": 0, "pir_enabled": 1, "current_fault": 0},
    }).encode("utf-8")
    second_state = json.dumps({
        "v": 1,
        "t": "state",
        "ts": 1200,
        "p": {"safety": 1, "mode": 0, "pir_enabled": 1, "current_fault": 0},
    }).encode("utf-8")
    changed_state = json.dumps({
        "v": 1,
        "t": "state",
        "ts": 1400,
        "p": {"safety": 0, "mode": 0, "pir_enabled": 1, "current_fault": 0},
    }).encode("utf-8")

    comm._handle_udp_packet(first_state)
    count_after_first = len(transport_logs)
    comm._handle_udp_packet(second_state)
    comm._handle_udp_packet(changed_state)

    assert any("ESP32 UDP STATE safety=LOCKED mode=WATER pir=ON fault=CLEAR" in message for message in transport_logs), "First UDP state should be surfaced to the log"
    assert len(transport_logs) == count_after_first + 1, "Duplicate UDP states inside the throttle window should not flood the log"
    assert any("ESP32 UDP STATE safety=ARMED mode=WATER pir=ON fault=CLEAR" in message for message in transport_logs), "Meaningful UDP state changes should still be logged immediately"

    print("  ✓ WiFi state trace stays visible without flooding identical packets")


def test_pin_assignment_dialog_content_lists_explicit_pir_gpio_mapping():
    """Verify the System-tab pin assignment dialog keeps PIR mapping readable and explicit."""
    print("[Test 12/12] Pin Assignment Dialog PIR Mapping...")

    tokens = {
        "text": "#f5f7fa",
        "subtle_text": "#d7dde5",
        "status_meta": "#aab4c0",
        "accent": "#72decf",
        "border": "#415062",
    }

    title, html = _build_pin_assignment_dialog_content(SentryV2Comm.MODE_WIFI_FULL, tokens)

    assert title == "Waveshare Pin Assignments", "Mode 3 should still identify the Waveshare bridge view"
    assert "PIR S1 / Sensor 0 / GPIO35" in html, "Dialog should list GPIO35 for the first PIR sensor"
    assert "PIR S2 / Sensor 1 / GPIO34" in html, "Dialog should list GPIO34 for the second PIR sensor"
    assert "PIR S3 / Sensor 2 / GPIO39 (VN)" in html, "Dialog should list GPIO39 and its VN board label for the third PIR sensor"
    assert "VN = GPIO39" in html, "Dialog should explain the expansion-board VN label"
    assert "#0f1720" not in html, "Dialog content should not hard-code dark heading colors"
    assert "#1e2936" not in html, "Dialog content should not hard-code dark body colors"

    print("  ✓ Pin assignment dialog keeps PIR GPIO mapping explicit and theme-aware")


class _DummySingleShotTimer:
    def __init__(self) -> None:
        self.started_ms: list[int] = []
        self.active = False

    def start(self, ms: int) -> None:
        self.started_ms.append(int(ms))
        self.active = True

    def stop(self) -> None:
        self.active = False


def test_manual_fire_projectile_mode_latches_release_long_enough_for_gpio13_pulse():
    """Projectile-mode manual fire should not clear the fire bit before the ESP32 can latch it."""
    print("[Test 13/13] Manual Fire Projectile Pulse Latch...")

    queued_calls = []
    dummy_timer = _DummySingleShotTimer()

    tab = SentryV2TabWidget.__new__(SentryV2TabWidget)
    tab._safety_armed = True
    tab._closing = False
    tab.engine = SimpleNamespace(current_pan=140.0, current_tilt=87.0)
    tab._comm = SimpleNamespace(
        trigger_mode_bb=True,
        MODE_WIFI_DEBUG_USB=2,
        _mode=2,
        _sock=object(),
        _udp_target=("192.168.4.1", 9000),
    )
    tab._manual_projectile_fire_release_timer = dummy_timer
    tab._manual_projectile_fire_latched = False
    tab._manual_projectile_fire_release_pan = 0.0
    tab._manual_projectile_fire_release_tilt = 0.0
    tab._host_controls_hardware = lambda: False
    tab._queue_comm_task = lambda name, *args, **kwargs: queued_calls.append((name, args, kwargs))
    tab._get_manual_move_time_ms = lambda: 35
    tab._log = lambda message: None
    tab.manual_fire_requested = SimpleNamespace(emit=lambda state: queued_calls.append(("emit", (state,), {})))

    tab._on_manual_fire(1)
    tab._on_manual_fire(0)

    assert len(queued_calls) == 1, "Projectile manual fire should not send an immediate fire=0 on button release"
    assert queued_calls[0][0] == "send_command", "Projectile manual fire should still queue a fire command"
    assert queued_calls[0][2].get("fire") == 1, "Projectile manual fire press should queue fire=1"
    assert dummy_timer.started_ms == [MANUAL_TRIGGER_SERVO_LATCH_MS], "Projectile manual fire should arm a delayed release latch"

    tab._flush_manual_projectile_fire_release()

    assert len(queued_calls) == 2, "Projectile manual fire should send a delayed fire=0 release"
    assert queued_calls[1][2].get("fire") == 0, "Delayed projectile release should queue fire=0"

    print("  ✓ Projectile manual fire keeps fire=1 latched long enough for the GPIO13 trigger pulse")


def main():
    print("\n=== SMART SENTRY V3 PIR UI Configuration Tests ===\n")
    
    try:
        test_pir_config_structure()
        test_pir_config_serialization()
        test_pir_sensor_angles()
        test_pir_scan_settings()
        test_pir_manager_creation()
        test_cross_sensor_lockout_allows_adjacent_hits_after_short_window()
        test_engine_pir_stats_surface_search_progress()
        test_pir_no_detect_returns_guard_home()
        test_paused_pir_events_do_not_queue_stale_motion()
        test_comm_parses_active_firmware_pir_serial_lines_and_logs_transport()
        test_comm_udp_state_trace_is_visible_without_flooding_duplicates()
        test_pin_assignment_dialog_content_lists_explicit_pir_gpio_mapping()
        test_manual_fire_projectile_mode_latches_release_long_enough_for_gpio13_pulse()
        
        print("\n✓ All 13 tests passed!\n")
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
