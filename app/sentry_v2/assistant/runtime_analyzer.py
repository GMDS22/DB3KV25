from __future__ import annotations

from typing import Any, Dict, List, Tuple

from .models import AssistantFinding


_DETECTION_MODE_LABELS = {
    0: "Frame Difference",
    1: "Background Subtraction",
    2: "YOLO Object Detection",
    3: "Hybrid FrameDiff + BackSub",
    4: "Hybrid FrameDiff + YOLO",
    5: "Hybrid BackSub + YOLO",
    6: "Color Detection",
    7: "Hybrid Color + FrameDiff",
    8: "Hybrid Color + BackSub",
    9: "Hybrid Color + YOLO",
    10: "Motion-Locked Filtered Target",
}


def _guard_mode_label(mode_index: int) -> str:
    return {
        0: "static_guard",
        1: "slow_sweep",
        2: "waypoint_patrol",
        3: "random_scan",
    }.get(int(mode_index), f"mode_{int(mode_index)}")


def _engagement_speed_label(speed_value: int) -> str:
    speed = int(speed_value)
    if speed >= 80:
        return "aggressive"
    if speed >= 60:
        return "balanced"
    return "deliberate"


class RuntimeAnalyzer:
    def analyze(self, snapshot: Dict[str, Any]) -> Tuple[List[AssistantFinding], List[str], str]:
        findings: List[AssistantFinding] = []
        recommendations: List[str] = []

        config = snapshot.get("config") or {}
        detection_cfg = config.get("detection_mode") or {}
        target_cfg = config.get("target_filter") or {}
        engagement_cfg = config.get("engagement") or {}
        guard_cfg = config.get("guard") or {}
        face_cfg = config.get("face_recognition") or {}
        pir_cfg = config.get("pir_guard") or {}
        engine = snapshot.get("engine_state") or {}
        comm = snapshot.get("comm_telemetry") or {}
        camera = snapshot.get("camera_status") or {}
        yolo = snapshot.get("yolo_status") or {}
        assistant_runtime = snapshot.get("assistant_runtime") or {}
        io_runtime = comm.get("io_runtime") or {}
        servo_feedback = comm.get("servo_feedback") or {}
        ai_cfg = config.get("ai_assistant") or {}

        state = str(engine.get("state") or "UNKNOWN")
        visible_targets = int(engine.get("targets_visible", len(engine.get("visible_targets") or [])) or 0)
        targets_detected = int(engine.get("targets_detected") or 0)
        targets_qualified = int(engine.get("targets_qualified") or engine.get("qualified_count") or 0)
        aim_lock_frames = int(engine.get("aim_lock_frames") or 0)
        last_err_pan_deg = float(engine.get("last_err_pan_deg") or 0.0)
        last_err_tilt_deg = float(engine.get("last_err_tilt_deg") or 0.0)
        loss_recovery_phase = str(engine.get("loss_recovery_phase") or "")
        filter_rejections = list(engine.get("filter_rejections") or [])
        autotracking = engine.get("autotracking") or {}

        detection_mode_idx = int(detection_cfg.get("detection_mode", 0) or 0)
        detection_mode_name = _DETECTION_MODE_LABELS.get(detection_mode_idx, f"mode_{detection_mode_idx}")
        allowed_classes = [str(item).strip() for item in list(target_cfg.get("allowed_classes") or []) if str(item).strip()]
        tracked_scope = ", ".join(allowed_classes[:5]) if allowed_classes else "all detectable classes"
        if allowed_classes and len(allowed_classes) > 5:
            tracked_scope = f"{tracked_scope}, +{len(allowed_classes) - 5} more"
        engagement_speed = int(engagement_cfg.get("engagement_speed", 0) or 0)
        engagement_speed_style = _engagement_speed_label(engagement_speed)
        burst_count = int(engagement_cfg.get("burst_count", 0) or 0)
        burst_interval_ms = int(engagement_cfg.get("burst_interval_ms", 0) or 0)
        trigger_mode_bb = bool(engagement_cfg.get("trigger_mode_bb", False))
        trigger_label = "projectile_servo" if trigger_mode_bb else "water_mosfet"
        return_delay = float(engagement_cfg.get("return_delay", 0.0) or 0.0)
        auto_trigger_enabled = bool(engagement_cfg.get("auto_trigger_enabled", False))
        guard_mode = int(guard_cfg.get("guard_mode", 0) or 0)
        guard_mode_name = _guard_mode_label(guard_mode)
        face_enabled = bool(face_cfg.get("enabled", False))
        pir_enabled = bool(pir_cfg.get("pir_enabled", False))

        findings.append(
            AssistantFinding(
                "low",
                "Active behavior profile",
                f"Detection={detection_mode_name}; tracking_scope={tracked_scope}; guard_mode={guard_mode_name}; speed={engagement_speed} ({engagement_speed_style}); trigger={trigger_label}; burst={burst_count}@{burst_interval_ms}ms; return_delay={return_delay:.2f}s; face={'on' if face_enabled else 'off'}; pir={'on' if pir_enabled else 'off'}.",
            )
        )

        if not bool(comm.get("is_connected")):
            findings.append(AssistantFinding("high", "Controller link offline", "The sentry is not currently connected to its controller link."))
            recommendations.append("Reconnect the controller link before expecting movement, trigger commands, or live bridge telemetry.")

        if not bool(camera.get("capture_open")):
            findings.append(AssistantFinding("high", "Camera feed closed", "No active video source is open, so live detection cannot run."))
            recommendations.append("Open the camera or test media source before asking for live analysis or engagement diagnostics.")

        if camera.get("camera_recovery_in_progress"):
            findings.append(AssistantFinding("medium", "Camera recovery active", "The camera pipeline is attempting to recover from repeated frame grabs."))

        if int(camera.get("camera_recovery_attempts") or 0) > 0 and not bool(camera.get("capture_open")):
            recommendations.append("Review camera source, cable stability, and requested resolution because the capture has already attempted recovery.")

        if not bool(yolo.get("detector_loaded")) and detection_mode_idx in (2, 4, 5, 9, 10):
            findings.append(AssistantFinding("medium", "YOLO mode without loaded model", "The active detection path expects YOLO, but no model is reported as loaded."))
            recommendations.append("Load a YOLO model or switch to a non-YOLO mode before expecting semantic detections.")

        if detection_mode_idx in (6, 7, 8, 9) and str(detection_cfg.get("color_preset", "any") or "any").strip().lower() == "any":
            findings.append(AssistantFinding("low", "Color gate is broad", "Color mode is active with preset=any, so color filtering will be permissive and may not narrow detections."))

        if auto_trigger_enabled and bool(io_runtime.get("safety", 0)):
            findings.append(AssistantFinding("high", "Auto-trigger armed while safety is locked", "Auto-trigger is enabled, but runtime safety reports LOCKED. The system will track but cannot fire."))
            recommendations.append("Unlock safety or disable auto-trigger so firing behavior matches the intended profile.")

        if trigger_mode_bb and int(engagement_cfg.get("trigger_servo_fire_deg", 45) or 45) == int(engagement_cfg.get("trigger_servo_rest_deg", 0) or 0):
            findings.append(AssistantFinding("high", "Projectile trigger servo has zero travel", "Trigger servo fire and rest angles are equal, so projectile firing will not actuate."))
            recommendations.append("Set distinct trigger servo rest/fire angles for projectile mode.")

        if bool(engagement_cfg.get("single_target_only", True)) and int(engagement_cfg.get("max_queue_length", 1) or 1) > 1:
            findings.append(AssistantFinding("medium", "Queue mismatch with single-target mode", "single_target_only is ON while max_queue_length is greater than 1; queue settings are inconsistent."))

        if return_delay < 0.15:
            findings.append(AssistantFinding("medium", "Very short return delay", f"return_delay is {return_delay:.2f}s, which can cause abrupt return transitions."))

        guard_pan = float(guard_cfg.get("guard_pan", engine.get("guard_pan", engine.get("current_pan", 0.0))) or 0.0)
        guard_tilt = float(guard_cfg.get("guard_tilt", engine.get("guard_tilt", engine.get("current_tilt", 0.0))) or 0.0)
        pan_min = float(guard_cfg.get("pan_min", 0.0) or 0.0)
        pan_max = float(guard_cfg.get("pan_max", 270.0) or 270.0)
        tilt_min = float(guard_cfg.get("tilt_min", 0.0) or 0.0)
        tilt_max = float(guard_cfg.get("tilt_max", 110.0) or 110.0)
        if guard_pan < min(pan_min, pan_max) or guard_pan > max(pan_min, pan_max) or guard_tilt < min(tilt_min, tilt_max) or guard_tilt > max(tilt_min, tilt_max):
            findings.append(AssistantFinding("high", "Guard/home position out of bounds", "Configured guard/home pan or tilt is outside the active guard limits."))
            recommendations.append("Clamp guard/home pan and tilt inside guard limit ranges.")

        if face_enabled and int(face_cfg.get("min_profile_samples", 1) or 1) > 1 and int(face_cfg.get("recognition_refresh_interval_ms", 250) or 250) < 120:
            findings.append(AssistantFinding("low", "Aggressive face refresh cadence", "Face recognition is enabled with a fast refresh interval, which can increase UI load on slower systems."))

        if pir_enabled:
            sensors = list(pir_cfg.get("sensors") or [])
            enabled_sensors = [sensor for sensor in sensors if bool((sensor or {}).get("enabled", False))]
            if not enabled_sensors:
                findings.append(AssistantFinding("medium", "PIR guard enabled without active sensors", "PIR guard is ON but no PIR sensor entries are enabled."))
                recommendations.append("Enable at least one PIR sensor or disable PIR guard to match actual intent.")

        if bool(ai_cfg.get("enabled", True)):
            provider_available = bool(assistant_runtime.get("provider_available"))
            prompt_model_ready = bool(assistant_runtime.get("selected_prompt_installed"))
            conversational = str(ai_cfg.get("mode") or "").strip().lower() == "conversational_voice"
            auto_speak = bool(assistant_runtime.get("auto_speak"))
            human_voice_enabled = bool(assistant_runtime.get("human_voice_enabled"))
            speech_supported = bool(assistant_runtime.get("speech_supported"))
            selected_prompt_model = str(assistant_runtime.get("selected_prompt_model") or ai_cfg.get("model") or "llama3.2:latest")

            if not provider_available:
                findings.append(AssistantFinding("medium", "Ollama unavailable", "The local Ollama endpoint is unavailable, so assistant replies will fall back to deterministic guidance."))
                recommendations.append("Start Ollama and make sure the local endpoint is reachable before expecting real model responses.")
            elif not prompt_model_ready:
                findings.append(AssistantFinding("medium", "Selected model missing", f"The selected prompt model {selected_prompt_model} is not installed locally."))
                recommendations.append(f"Pull or switch to an installed Ollama model before expecting local AI responses from {selected_prompt_model}.")

            if conversational and auto_speak and not human_voice_enabled:
                findings.append(AssistantFinding("medium", "Auto-speak armed but human voice is off", "Conversational Voice mode is selected and auto-speak is enabled, but the human voice path is disabled."))
                recommendations.append("Enable Human voice in Controls or turn off auto-speak if you want a text-only assistant.")
            elif conversational and auto_speak and not speech_supported:
                findings.append(AssistantFinding("high", "Speech backend unavailable", "Conversational Voice mode is selected, but Qt text-to-speech is unavailable in the current runtime."))
                recommendations.append("Validate the Qt speech backend before relying on spoken assistant replies.")
            elif conversational and not auto_speak:
                findings.append(AssistantFinding("low", "Conversational mode is text-only", "Conversational Voice mode is selected, but assistant auto-speak is turned off."))

        if servo_feedback.get("active") and servo_feedback.get("age_s") is not None and float(servo_feedback.get("age_s") or 0.0) > 5.0:
            findings.append(AssistantFinding("medium", "Servo telemetry stale", "Servo feedback exists but has not updated recently."))

        if io_runtime.get("current_fault"):
            findings.append(AssistantFinding("high", "Current fault present", f"Bridge current fault reports: {io_runtime.get('current_fault')}"))
            recommendations.append("Inspect power and bridge wiring before continuing aggressive movement or fire testing.")

        if state == "GUARDING" and visible_targets == 0 and bool(camera.get("capture_open")):
            findings.append(AssistantFinding("low", "Idle guard state", "The system is guarding with no currently visible qualified targets."))

        if targets_detected > 0 and targets_qualified <= 0 and filter_rejections:
            top_rejection = filter_rejections[0]
            findings.append(
                AssistantFinding(
                    "medium",
                    "Targets rejected before engagement",
                    f"Detections are reaching the engine, but the top rejection is {top_rejection.get('class_name', 'unknown')} via {top_rejection.get('reason', 'filter')}.",
                )
            )
            recommendations.append("Review allowed classes, confirmation hits, and the current detection mode before lowering threat thresholds.")

        if state == "ENGAGING" and visible_targets == 0:
            findings.append(AssistantFinding("medium", "Engaging without visible target", "The engine is still in engaging state even though no visible targets are reported right now."))

        if state == "ENGAGING" and visible_targets > 0 and aim_lock_frames <= 0 and (abs(last_err_pan_deg) > 0.75 or abs(last_err_tilt_deg) > 0.75):
            findings.append(AssistantFinding("medium", "Tracking is not yet locked", "The engine is engaging with visible targets, but aim lock has not accumulated and tracking error is still elevated."))
            recommendations.append("Check tracking error, detection mode stability, and aim-lock thresholds before assuming the current target can be held cleanly.")

        if loss_recovery_phase:
            findings.append(AssistantFinding("low", "Loss recovery active", f"The engine is currently in loss recovery phase: {loss_recovery_phase}."))

        if bool(autotracking.get("logging_enabled")):
            loss_events = int(autotracking.get("loss_events") or 0)
            reacquisitions = int(autotracking.get("reacquisitions") or 0)
            avg_tracking_error_deg = autotracking.get("avg_tracking_error_deg")
            if loss_events >= 3 and loss_events > (reacquisitions + 1):
                findings.append(AssistantFinding("medium", "Repeated target-loss churn", "Autotracking logs show repeated loss events without matching reacquisition recovery."))
                recommendations.append("Use the current mode and rejection data to reduce churn before widening engagement or fire settings.")
            if avg_tracking_error_deg is not None and float(avg_tracking_error_deg) >= 1.5:
                findings.append(AssistantFinding("low", "Tracking corrections remain large", f"Average logged tracking error is {float(avg_tracking_error_deg):.2f} degrees."))

        if not recommendations:
            recommendations.append("Runtime looks stable enough for local assistant coaching. No immediate corrective action stands out from the current snapshot.")

        summary = (
            f"State={state}; connected={bool(comm.get('is_connected'))}; camera_open={bool(camera.get('capture_open'))}; "
            f"visible_targets={visible_targets}; yolo_loaded={bool(yolo.get('detector_loaded'))}; "
            f"detection_mode={detection_mode_name}; tracking_scope={tracked_scope}; guard_mode={guard_mode_name}; "
            f"speed={engagement_speed}({engagement_speed_style}); trigger={trigger_label}; burst={burst_count}@{burst_interval_ms}ms; return_delay={return_delay:.2f}s; "
            f"assistant_provider={bool(assistant_runtime.get('provider_available'))}; speech_ready={bool(assistant_runtime.get('speech_supported')) and bool(assistant_runtime.get('human_voice_enabled'))}; "
            f"current_fault={io_runtime.get('current_fault') or 'none'}"
        )
        return findings, recommendations, summary
