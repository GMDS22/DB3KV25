from __future__ import annotations

from typing import Any, Dict, List, Tuple

from .models import AssistantFinding


class RuntimeAnalyzer:
    def analyze(self, snapshot: Dict[str, Any]) -> Tuple[List[AssistantFinding], List[str], str]:
        findings: List[AssistantFinding] = []
        recommendations: List[str] = []

        config = snapshot.get("config") or {}
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

        if not bool(yolo.get("detector_loaded")) and int(snapshot.get("config", {}).get("detection_mode", {}).get("detection_mode", 0)) in (2, 4, 5, 9, 10):
            findings.append(AssistantFinding("medium", "YOLO mode without loaded model", "The active detection path expects YOLO, but no model is reported as loaded."))
            recommendations.append("Load a YOLO model or switch to a non-YOLO mode before expecting semantic detections.")

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
            f"assistant_provider={bool(assistant_runtime.get('provider_available'))}; speech_ready={bool(assistant_runtime.get('speech_supported')) and bool(assistant_runtime.get('human_voice_enabled'))}; "
            f"current_fault={io_runtime.get('current_fault') or 'none'}"
        )
        return findings, recommendations, summary
