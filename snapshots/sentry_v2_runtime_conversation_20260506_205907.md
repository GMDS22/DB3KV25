# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-06 20:59:07
- Entries: 158
- Roles: {'assistant': 9, 'system': 1, 'operator': 148}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 2, 'voice_status': 1, 'voice_transcript_partial': 119, 'voice_transcript_final': 22, 'voice_command': 7, 'spoken_confirmation': 5, 'spoken_reply': 1}
- Channels: {'text': 3, 'voice': 155}
- Latest operator request: unk
- Latest assistant message: Analysis [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Local runtime analysis fallback: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=projectile_servo; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Runtime facts: state=ENGAGING | camera_open=True | yolo_loaded=True | face_backend=opencv_sface | face_profiles_ready=3/6 | mode=2 | tracking_scope=person | loss_protocols=rapid_handoff_search/persistent_reacquire_search | speed=100 trigger=projectile burst=6@70ms | return_delay=1.5 | guard_mode=2 guard_pan_tilt=140.0/83.0. Next step: Enable at least one PIR sensor or disable PIR guard to match actual intent. Supporting Findings: - [low] Active behavior profile: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=projectile_servo; burst=6@70ms; return_delay=1.50s; face=on; pir=on. - [medium] PIR guard enabled without active sensors: PIR guard is ON but no PIR sensor entries are enabled. - [low] Conversational mode is text-only: Conversational Voice mode is selected, but assistant auto-speak is turned off. - [medium] Tracking is not yet locked: The engine is engaging with visible targets, but aim lock has not accumulated and tracking error is still elevated. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-06 20:50:54] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 20:50:54] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 20:50:57] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778071857.3533769 | source=vosk
- [2026-05-06 20:51:18] operator / voice_transcript_partial / voice: human
  meta: kind=partial | timestamp=1778071878.062739 | source=vosk | frequency_hz=345.4 | rms=283 | updated_at=1778071877.5559318
- [2026-05-06 20:51:18] operator / voice_transcript_partial / voice: human voice
  meta: kind=partial | timestamp=1778071878.5619805 | source=vosk | frequency_hz=348.3 | rms=305 | updated_at=1778071878.5579796
- [2026-05-06 20:51:19] operator / voice_transcript_final / voice: human
  meta: kind=final | timestamp=1778071879.3822758 | source=final | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:19] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1778071879.8123648 | source=vosk | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:20] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1778071880.0612066 | source=vosk | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:20] operator / voice_transcript_partial / voice: smart sentry human voice
  meta: kind=partial | timestamp=1778071880.5644884 | source=vosk | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:21] operator / voice_transcript_partial / voice: smart sentry human voice mode
  meta: kind=partial | timestamp=1778071881.0622056 | source=vosk | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:21] operator / voice_transcript_partial / voice: smart sentry human voice mode the
  meta: kind=partial | timestamp=1778071881.3115838 | source=vosk | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:21] operator / voice_transcript_partial / voice: smart sentry human voice mode the is on
  meta: kind=partial | timestamp=1778071881.5632515 | source=vosk | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:21] operator / voice_transcript_partial / voice: smart sentry human voice mode the is on light
  meta: kind=partial | timestamp=1778071881.8138988 | source=vosk | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:23] operator / voice_transcript_final / voice: smart sentry human voice mode the is on light
  meta: kind=final | timestamp=1778071883.0288272 | source=final | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:23] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1778071883.6237752 | source=vosk | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:23] operator / voice_transcript_partial / voice: of voice
  meta: kind=partial | timestamp=1778071883.8742182 | source=vosk | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:24] operator / voice_transcript_partial / voice: of greeting
  meta: kind=partial | timestamp=1778071884.1240559 | source=vosk | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:24] operator / voice_transcript_partial / voice: of mute
  meta: kind=partial | timestamp=1778071884.3756342 | source=vosk | frequency_hz=355.2 | rms=308 | updated_at=1778071878.806475
- [2026-05-06 20:51:24] operator / voice_transcript_final / voice: of voice neutral
  meta: kind=final | timestamp=1778071884.717729 | source=final | frequency_hz=412.0 | rms=310 | updated_at=1778071884.6183653
- [2026-05-06 20:51:26] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1778071886.1235824 | source=vosk | frequency_hz=375.6 | rms=308 | updated_at=1778071885.1178489
- [2026-05-06 20:51:26] operator / voice_transcript_partial / voice: status zone
  meta: kind=partial | timestamp=1778071886.6234696 | source=vosk | frequency_hz=375.6 | rms=308 | updated_at=1778071885.1178489
- [2026-05-06 20:51:26] operator / voice_transcript_partial / voice: status the greeting
  meta: kind=partial | timestamp=1778071886.8793147 | source=vosk | frequency_hz=375.6 | rms=308 | updated_at=1778071885.1178489
- [2026-05-06 20:51:27] operator / voice_transcript_final / voice: status zone greeting
  meta: kind=final | timestamp=1778071887.719241 | source=final | frequency_hz=342.9 | rms=298 | updated_at=1778071887.6191745
- [2026-05-06 20:51:28] operator / voice_transcript_partial / voice: human
  meta: kind=partial | timestamp=1778071888.8730006 | source=vosk | frequency_hz=327.9 | rms=299 | updated_at=1778071887.8678627
- [2026-05-06 20:51:29] operator / voice_transcript_partial / voice: cue
  meta: kind=partial | timestamp=1778071889.1242487 | source=vosk | frequency_hz=320.9 | rms=286 | updated_at=1778071889.1182353
- [2026-05-06 20:51:29] operator / voice_transcript_final / voice: cue
  meta: kind=final | timestamp=1778071889.941677 | source=final | frequency_hz=310.4 | rms=305 | updated_at=1778071889.617392
- [2026-05-06 20:51:30] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1778071890.3743584 | source=vosk | frequency_hz=310.4 | rms=305 | updated_at=1778071889.617392
- [2026-05-06 20:51:30] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1778071890.6237855 | source=vosk | frequency_hz=310.4 | rms=305 | updated_at=1778071889.617392
- [2026-05-06 20:51:31] operator / voice_transcript_partial / voice: smart sentry human
  meta: kind=partial | timestamp=1778071891.1229382 | source=vosk | frequency_hz=310.4 | rms=305 | updated_at=1778071889.617392
- [2026-05-06 20:51:31] operator / voice_transcript_partial / voice: smart sentry human voice
  meta: kind=partial | timestamp=1778071891.3730621 | source=vosk | frequency_hz=310.4 | rms=305 | updated_at=1778071889.617392
- [2026-05-06 20:51:31] operator / voice_transcript_partial / voice: smart sentry human voice mode
  meta: kind=partial | timestamp=1778071891.8741562 | source=vosk | frequency_hz=310.4 | rms=305 | updated_at=1778071889.617392
- [2026-05-06 20:51:32] operator / voice_transcript_partial / voice: smart sentry human voice mode the
  meta: kind=partial | timestamp=1778071892.1230495 | source=vosk | frequency_hz=310.4 | rms=305 | updated_at=1778071889.617392
- [2026-05-06 20:51:32] operator / voice_transcript_partial / voice: smart sentry human voice mode the is elian
  meta: kind=partial | timestamp=1778071892.6246397 | source=vosk | frequency_hz=420.0 | rms=306 | updated_at=1778071892.6186755
- [2026-05-06 20:51:33] operator / voice_transcript_final / voice: smart sentry human voice mode the is on light
  meta: kind=final | timestamp=1778071893.2728953 | source=final | frequency_hz=350.8 | rms=302 | updated_at=1778071893.118304
- [2026-05-06 20:51:37] operator / voice_transcript_partial / voice: slew order
  meta: kind=partial | timestamp=1778071897.9144228 | source=vosk | frequency_hz=210.0 | rms=230 | updated_at=1778071897.3892367
- [2026-05-06 20:51:38] operator / voice_transcript_final / voice: slew
  meta: kind=final | timestamp=1778071898.263526 | source=final | frequency_hz=210.0 | rms=230 | updated_at=1778071897.3892367
- [2026-05-06 20:51:45] operator / voice_transcript_partial / voice: voice speech
  meta: kind=partial | timestamp=1778071905.1156056 | source=vosk | frequency_hz=378.0 | rms=304 | updated_at=1778071899.6602862
- [2026-05-06 20:51:46] operator / voice_transcript_partial / voice: voice speech mask
  meta: kind=partial | timestamp=1778071906.4016235 | source=vosk | frequency_hz=378.0 | rms=304 | updated_at=1778071899.6602862
- [2026-05-06 20:51:46] operator / voice_transcript_final / voice: voice speech model
  meta: kind=final | timestamp=1778071906.755572 | source=final | frequency_hz=212.0 | rms=364 | updated_at=1778071906.6428685
- [2026-05-06 20:52:11] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human
  meta: kind=partial | timestamp=1778071931.7138236 | source=vosk | frequency_hz=327.2 | rms=286 | updated_at=1778071926.2076693
- [2026-05-06 20:52:11] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice
  meta: kind=partial | timestamp=1778071931.965023 | source=vosk | frequency_hz=327.2 | rms=286 | updated_at=1778071926.2076693
- [2026-05-06 20:52:12] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode
  meta: kind=partial | timestamp=1778071932.47057 | source=vosk | frequency_hz=327.2 | rms=286 | updated_at=1778071926.2076693
- [2026-05-06 20:52:12] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is
  meta: kind=partial | timestamp=1778071932.7150407 | source=vosk | frequency_hz=327.2 | rms=286 | updated_at=1778071926.2076693
- [2026-05-06 20:52:12] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is automatic
  meta: kind=partial | timestamp=1778071932.9644647 | source=vosk | frequency_hz=327.2 | rms=286 | updated_at=1778071926.2076693
- [2026-05-06 20:52:13] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is on lion
  meta: kind=partial | timestamp=1778071933.2155206 | source=vosk | frequency_hz=364.0 | rms=306 | updated_at=1778071933.2087598
- [2026-05-06 20:52:13] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is on lion voice
  meta: kind=partial | timestamp=1778071933.965267 | source=vosk | frequency_hz=364.0 | rms=306 | updated_at=1778071933.2087598
- [2026-05-06 20:52:14] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is on lion voice mode
  meta: kind=partial | timestamp=1778071934.21488 | source=vosk | frequency_hz=364.0 | rms=306 | updated_at=1778071933.2087598
- [2026-05-06 20:52:14] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is on lion voice of microphone
  meta: kind=partial | timestamp=1778071934.4706109 | source=vosk | frequency_hz=380.8 | rms=299 | updated_at=1778071934.4570942
- [2026-05-06 20:52:14] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is on lion voice of microphone anomaly
  meta: kind=partial | timestamp=1778071934.7142508 | source=vosk | frequency_hz=380.8 | rms=299 | updated_at=1778071934.4570942
- [2026-05-06 20:52:15] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is on lion voice of microphone
  meta: kind=partial | timestamp=1778071935.2127705 | source=vosk | frequency_hz=380.8 | rms=299 | updated_at=1778071934.4570942
- [2026-05-06 20:52:15] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is on lion voice of microphone style blink
  meta: kind=partial | timestamp=1778071935.4675672 | source=vosk | frequency_hz=380.8 | rms=299 | updated_at=1778071934.4570942
- [2026-05-06 20:52:15] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is on lion voice of microphone style brightness
  meta: kind=partial | timestamp=1778071935.7145355 | source=vosk | frequency_hz=380.8 | rms=299 | updated_at=1778071934.4570942
- [2026-05-06 20:52:15] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is on lion voice of microphone style board gesture
  meta: kind=partial | timestamp=1778071935.9637554 | source=vosk | frequency_hz=380.8 | rms=299 | updated_at=1778071934.4570942
- [2026-05-06 20:52:16] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is on lion voice of microphone style blink ask cleanup
  meta: kind=partial | timestamp=1778071936.214205 | source=vosk | frequency_hz=380.8 | rms=299 | updated_at=1778071934.4570942
- [2026-05-06 20:52:16] operator / voice_transcript_partial / voice: voice set to ml engagement lion hello smart sentry human voice mode is on lion voice of microphone style blink ask clear the
  meta: kind=partial | timestamp=1778071936.4667368 | source=vosk | frequency_hz=380.8 | rms=299 | updated_at=1778071934.4570942
- [2026-05-06 20:52:18] operator / voice_transcript_final / voice: elion voice set to ml engagement light hello smart sentry human voice mode is on lion voice of microphone style blink ask cleanup
  meta: kind=final | timestamp=1778071938.1852686 | source=final | frequency_hz=403.8 | rms=307 | updated_at=1778071936.9567487
- [2026-05-06 20:52:18] operator / voice_command / voice: voice set to ml engagement light hello smart sentry human voice mode is on lion voice of microphone style blink ask cleanup
  meta: normalized=True
- [2026-05-06 20:52:21] assistant / spoken_confirmation / voice: I could not map that to a command yet. Please say it again.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:52:33] operator / voice_transcript_final / voice: hey
  meta: kind=final | timestamp=1778071953.8995397 | source=final
- [2026-05-06 20:54:58] operator / voice_transcript_final / voice: hey
  meta: kind=final | timestamp=1778072098.2540288 | source=final | frequency_hz=372.0 | rms=290 | updated_at=1778072072.408397
- [2026-05-06 20:55:13] operator / voice_transcript_final / voice: hey
  meta: kind=final | timestamp=1778072113.0011535 | source=final | frequency_hz=372.0 | rms=290 | updated_at=1778072072.408397
- [2026-05-06 20:55:23] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1778072123.167002 | source=vosk | frequency_hz=372.0 | rms=290 | updated_at=1778072072.408397
- [2026-05-06 20:55:23] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1778072123.4174826 | source=vosk | frequency_hz=372.0 | rms=290 | updated_at=1778072072.408397
- [2026-05-06 20:55:23] operator / voice_transcript_partial / voice: alien loss
  meta: kind=partial | timestamp=1778072123.6666977 | source=vosk | frequency_hz=372.0 | rms=290 | updated_at=1778072072.408397
- [2026-05-06 20:55:30] operator / voice_transcript_partial / voice: running
  meta: kind=partial | timestamp=1778072130.1673856 | source=vosk | frequency_hz=368.5 | rms=285 | updated_at=1778072128.6598
- [2026-05-06 20:55:30] operator / voice_transcript_partial / voice: run the smart
  meta: kind=partial | timestamp=1778072130.4189193 | source=vosk | frequency_hz=368.5 | rms=285 | updated_at=1778072128.6598
- [2026-05-06 20:55:31] operator / voice_transcript_partial / voice: run the smart sentry
  meta: kind=partial | timestamp=1778072131.33333 | source=vosk | frequency_hz=368.5 | rms=285 | updated_at=1778072128.6598
- [2026-05-06 20:55:32] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778072132.4393802 | source=final | frequency_hz=350.0 | rms=780 | updated_at=1778072132.0828557
- [2026-05-06 20:55:32] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-06 20:55:33] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:56:35] operator / voice_transcript_partial / voice: guard system recognition
  meta: kind=partial | timestamp=1778072195.4636378 | source=vosk | frequency_hz=349.7 | rms=303 | updated_at=1778072189.9564695
- [2026-05-06 20:56:35] operator / voice_transcript_partial / voice: guard system threat scores
  meta: kind=partial | timestamp=1778072195.7148774 | source=vosk | frequency_hz=349.7 | rms=303 | updated_at=1778072189.9564695
- [2026-05-06 20:56:36] operator / voice_transcript_final / voice: guard system threat
  meta: kind=final | timestamp=1778072196.9191623 | source=final | frequency_hz=349.7 | rms=303 | updated_at=1778072189.9564695
- [2026-05-06 20:56:47] operator / voice_transcript_partial / voice: known
  meta: kind=partial | timestamp=1778072207.9862924 | source=vosk | frequency_hz=370.0 | rms=309 | updated_at=1778072196.9952202
- [2026-05-06 20:56:48] operator / voice_transcript_partial / voice: known disable zone
  meta: kind=partial | timestamp=1778072208.7363315 | source=vosk | frequency_hz=370.0 | rms=309 | updated_at=1778072196.9952202
- [2026-05-06 20:56:48] operator / voice_transcript_partial / voice: known disable
  meta: kind=partial | timestamp=1778072208.988043 | source=vosk | frequency_hz=370.0 | rms=309 | updated_at=1778072196.9952202
- [2026-05-06 20:56:49] operator / voice_transcript_partial / voice: known disable servo face
  meta: kind=partial | timestamp=1778072209.2345698 | source=vosk | frequency_hz=370.0 | rms=309 | updated_at=1778072196.9952202
- [2026-05-06 20:56:49] operator / voice_transcript_partial / voice: known disable servo face hello
  meta: kind=partial | timestamp=1778072209.9975266 | source=vosk | frequency_hz=370.0 | rms=309 | updated_at=1778072196.9952202
- [2026-05-06 20:56:50] operator / voice_transcript_partial / voice: known disable servo face the current
  meta: kind=partial | timestamp=1778072210.2463753 | source=vosk | frequency_hz=370.0 | rms=309 | updated_at=1778072196.9952202
- [2026-05-06 20:56:50] operator / voice_transcript_partial / voice: known disable servo face the current status
  meta: kind=partial | timestamp=1778072210.4845943 | source=vosk | frequency_hz=370.0 | rms=309 | updated_at=1778072196.9952202
- [2026-05-06 20:56:50] operator / voice_transcript_partial / voice: known disable servo face the current the guard
  meta: kind=partial | timestamp=1778072210.7362158 | source=vosk | frequency_hz=370.0 | rms=309 | updated_at=1778072196.9952202
- [2026-05-06 20:56:51] operator / voice_transcript_final / voice: known disable servo face the current the guard
  meta: kind=final | timestamp=1778072211.8228319 | source=final | frequency_hz=370.0 | rms=309 | updated_at=1778072196.9952202
- [2026-05-06 20:57:16] operator / voice_transcript_partial / voice: acoustic guard detection on the motion control
  meta: kind=partial | timestamp=1778072236.5012815 | source=vosk | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:16] operator / voice_transcript_partial / voice: acoustic guard detection on the spare output output
  meta: kind=partial | timestamp=1778072236.738978 | source=vosk | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:17] operator / voice_transcript_partial / voice: acoustic guard detection on startup to
  meta: kind=partial | timestamp=1778072237.2523603 | source=vosk | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:18] operator / voice_transcript_partial / voice: acoustic guard detection on startup to anything
  meta: kind=partial | timestamp=1778072238.2382624 | source=vosk | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:18] operator / voice_transcript_partial / voice: acoustic guard detection on startup to alion
  meta: kind=partial | timestamp=1778072238.4882355 | source=vosk | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:18] operator / voice_transcript_partial / voice: acoustic guard detection on startup to alion disable
  meta: kind=partial | timestamp=1778072238.7683568 | source=vosk | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:19] operator / voice_transcript_partial / voice: acoustic guard detection on startup to alion disable overlay
  meta: kind=partial | timestamp=1778072239.252598 | source=vosk | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:19] operator / voice_transcript_partial / voice: acoustic guard detection on startup to alion disable auto face
  meta: kind=partial | timestamp=1778072239.524675 | source=vosk | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:20] operator / voice_transcript_final / voice: elion acoustic guard detection on the motion startup to disable auto face
  meta: kind=final | timestamp=1778072240.8235474 | source=final | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:21] operator / voice_command / voice: acoustic guard detection on the motion startup to disable auto face
  meta: normalized=True
- [2026-05-06 20:57:22] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:57:28] operator / voice_transcript_partial / voice: i have the reports include current leon run motion on can change theme
  meta: kind=partial | timestamp=1778072248.9565961 | source=vosk | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:29] operator / voice_transcript_partial / voice: i have the reports include current leon run motion on can change theme sentry
  meta: kind=partial | timestamp=1778072249.2159638 | source=vosk | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:30] operator / voice_transcript_final / voice: change theme
  meta: kind=final | timestamp=1778072250.096769 | source=final | frequency_hz=365.0 | rms=307 | updated_at=1778072230.4795978
- [2026-05-06 20:57:30] operator / voice_command / voice: change theme
  meta: normalized=True
- [2026-05-06 20:57:30] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1778072250.4543717 | source=vosk | frequency_hz=348.0 | rms=293 | updated_at=1778072250.4488628
- [2026-05-06 20:57:30] operator / voice_transcript_partial / voice: of a
  meta: kind=partial | timestamp=1778072250.7141924 | source=vosk | frequency_hz=348.0 | rms=293 | updated_at=1778072250.4488628
- [2026-05-06 20:57:31] operator / voice_transcript_final / voice: of a
  meta: kind=final | timestamp=1778072251.5867782 | source=final | frequency_hz=348.0 | rms=293 | updated_at=1778072250.4488628
- [2026-05-06 20:58:04] assistant / spoken_reply / voice: Smart Sentry is engaging person target 17 in precision phase. Visible detections include 1 person. 1 person in view are not matched to known faces. The acoustic guard has also detected unusual sound recently. Latest AI note. Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts. End of analysys report.
  meta: interrupt=False | assistant_output=True | spoken=False
- [2026-05-06 20:58:10] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output for
  meta: kind=partial | timestamp=1778072290.8304229 | source=vosk | frequency_hz=376.0 | rms=287 | updated_at=1778072290.301829
- [2026-05-06 20:58:11] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output for disable the
  meta: kind=partial | timestamp=1778072291.49806 | source=vosk | frequency_hz=376.0 | rms=287 | updated_at=1778072290.301829
- [2026-05-06 20:58:11] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output for disable the motion
  meta: kind=partial | timestamp=1778072291.5606458 | source=vosk | frequency_hz=376.0 | rms=287 | updated_at=1778072290.301829
- [2026-05-06 20:58:11] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output for disable servo
  meta: kind=partial | timestamp=1778072291.807029 | source=vosk | frequency_hz=376.0 | rms=287 | updated_at=1778072290.301829
- [2026-05-06 20:58:12] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output for disable servo face
  meta: kind=partial | timestamp=1778072292.0730188 | source=vosk | frequency_hz=376.0 | rms=287 | updated_at=1778072290.301829
- [2026-05-06 20:58:12] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output for disable servo face lion
  meta: kind=partial | timestamp=1778072292.3064907 | source=vosk | frequency_hz=344.0 | rms=289 | updated_at=1778072292.300482
- [2026-05-06 20:58:13] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output for disable servo face lion current
  meta: kind=partial | timestamp=1778072293.0818408 | source=vosk | frequency_hz=344.0 | rms=289 | updated_at=1778072292.300482
- [2026-05-06 20:58:13] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output for disable servo face lion current status
  meta: kind=partial | timestamp=1778072293.3071415 | source=vosk | frequency_hz=344.0 | rms=289 | updated_at=1778072292.300482
- [2026-05-06 20:58:14] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output for disable servo face lion current status engaging
  meta: kind=partial | timestamp=1778072294.0575233 | source=vosk | frequency_hz=368.0 | rms=278 | updated_at=1778072294.0515141
- [2026-05-06 20:58:14] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output for disable servo face lion current status engaging scope
  meta: kind=partial | timestamp=1778072294.3254542 | source=vosk | frequency_hz=358.9 | rms=300 | updated_at=1778072294.3019001
- [2026-05-06 20:58:15] operator / voice_transcript_final / voice: elion acoustic guard detection id on neutral sound of output for disable servo face lion current status engaging
  meta: kind=final | timestamp=1778072295.7376196 | source=final | frequency_hz=368.4 | rms=290 | updated_at=1778072294.551633
- [2026-05-06 20:58:16] operator / voice_command / voice: acoustic guard detection id on neutral sound of output for disable servo face lion current status engaging
  meta: normalized=True
- [2026-05-06 20:58:16] assistant / spoken_confirmation / voice: Received. I started a live runtime analysis in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:58:21] operator / voice_transcript_partial / voice: rest the ai start elian runtime analysis
  meta: kind=partial | timestamp=1778072301.7216759 | source=vosk | frequency_hz=369.6 | rms=294 | updated_at=1778072297.9641268
- [2026-05-06 20:58:22] operator / voice_transcript_partial / voice: rest the ai start elian runtime analysis on the
  meta: kind=partial | timestamp=1778072302.021171 | source=vosk | frequency_hz=369.6 | rms=294 | updated_at=1778072297.9641268
- [2026-05-06 20:58:22] operator / voice_transcript_partial / voice: rest the ai start elian runtime analysis on the manual
  meta: kind=partial | timestamp=1778072302.2210062 | source=vosk | frequency_hz=369.6 | rms=294 | updated_at=1778072297.9641268
- [2026-05-06 20:58:22] operator / voice_transcript_partial / voice: rest the ai start elian runtime analysis on the
  meta: kind=partial | timestamp=1778072302.469861 | source=vosk | frequency_hz=369.6 | rms=294 | updated_at=1778072297.9641268
- [2026-05-06 20:58:23] operator / voice_transcript_final / voice: elion rest the ai start runtime analysis
  meta: kind=final | timestamp=1778072303.2713282 | source=final | frequency_hz=316.0 | rms=284 | updated_at=1778072302.714187
- [2026-05-06 20:58:24] operator / voice_command / voice: rest the ai start runtime analysis
  meta: normalized=True
- [2026-05-06 20:58:24] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:58:37] operator / voice_transcript_partial / voice: acoustic guard detection on the visual overlay
  meta: kind=partial | timestamp=1778072317.398704 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:37] operator / voice_transcript_partial / voice: acoustic guard detection on inversion of output
  meta: kind=partial | timestamp=1778072317.6327887 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:38] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml turn
  meta: kind=partial | timestamp=1778072318.3856459 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:38] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml refinement
  meta: kind=partial | timestamp=1778072318.4086757 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:38] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning hi
  meta: kind=partial | timestamp=1778072318.6468415 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:39] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for
  meta: kind=partial | timestamp=1778072319.130965 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:39] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for deactivate
  meta: kind=partial | timestamp=1778072319.648199 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:39] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable suppress
  meta: kind=partial | timestamp=1778072319.895876 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:40] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable the
  meta: kind=partial | timestamp=1778072320.166472 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:40] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face
  meta: kind=partial | timestamp=1778072320.4097595 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:40] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion
  meta: kind=partial | timestamp=1778072320.628215 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:41] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current status
  meta: kind=partial | timestamp=1778072321.398877 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:41] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak
  meta: kind=partial | timestamp=1778072321.885665 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:42] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak engaging scope
  meta: kind=partial | timestamp=1778072322.3795156 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:42] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak engaging acoustic
  meta: kind=partial | timestamp=1778072322.9017138 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:43] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak engaging acoustic guard
  meta: kind=partial | timestamp=1778072323.4120157 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:43] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak engaging acoustic guard disabled
  meta: kind=partial | timestamp=1778072323.706632 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:43] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak engaging acoustic guard detection
  meta: kind=partial | timestamp=1778072323.9093335 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:44] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak engaging acoustic guard detection id on
  meta: kind=partial | timestamp=1778072324.146176 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:44] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak engaging acoustic guard detection id on mute
  meta: kind=partial | timestamp=1778072324.38226 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:44] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak engaging acoustic guard detection id on use
  meta: kind=partial | timestamp=1778072324.6296458 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:44] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak engaging acoustic guard detection id on neutral
  meta: kind=partial | timestamp=1778072324.879325 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:45] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak engaging acoustic guard detection id on neutral sound
  meta: kind=partial | timestamp=1778072325.1322494 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:45] operator / voice_transcript_partial / voice: acoustic guard detection on inversion is ml learning fire for disable servo face lion current speak engaging acoustic guard detection id on neutral sound ml
  meta: kind=partial | timestamp=1778072325.636084 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:48] operator / voice_transcript_final / voice: elion acoustic guard detection id on inversion is ml learning fire for disable servo face lion current speak engaging acoustic guard detection id on neutral sound ml
  meta: kind=final | timestamp=1778072328.4212637 | source=final | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:49] operator / voice_command / voice: acoustic guard detection id on inversion is ml learning fire for disable servo face lion current speak engaging acoustic guard detection id on neutral sound ml
  meta: normalized=True
- [2026-05-06 20:58:49] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1778072329.049537 | source=vosk | frequency_hz=362.4 | rms=291 | updated_at=1778072312.3925579
- [2026-05-06 20:58:49] operator / voice_transcript_partial / voice: suggestions
  meta: kind=partial | timestamp=1778072329.5685983 | source=vosk | frequency_hz=62.0 | rms=1205 | updated_at=1778072329.5565867
- [2026-05-06 20:58:49] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1778072329.8077474 | source=vosk | frequency_hz=62.0 | rms=1205 | updated_at=1778072329.5565867
- [2026-05-06 20:58:54] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1778072334.4737213 | source=final | frequency_hz=413.1 | rms=300 | updated_at=1778072334.183617
- [2026-05-06 20:59:02] assistant / assistant_analysis / text: Analysis [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Local runtime analysis fallback: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=projectile_servo; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Runtime facts: state=ENGAGING | camera_open=True | yolo_loaded=True | face_backend=opencv_sface | face_profiles_ready=3/6 | mode=2 | tracking_scope=person | loss_protocols=rapid_handoff_search/persistent_reacquire_search | speed=100 trigger=projectile burst=6@70ms | return_delay=1.5 | guard_mode=2 guard_pan_tilt=140.0/83.0. Next step: Enable at least one PIR sensor or disable PIR guard to match actual intent. Supporting Findings: - [low] Active behavior profile: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=projectile_servo; burst=6@70ms; return_delay=1.50s; face=on; pir=on. - [medium] PIR guard enabled without active sensors: PIR guard is ON but no PIR sensor entries are enabled. - [low] Conversational mode is text-only: Conversational Voice mode is selected, but assistant auto-speak is turned off. - [medium] Tracking is not yet locked: The engine is engaging with visible targets, but aim lock has not accumulated and tracking error is still elevated. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 20:59:03] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound
  meta: kind=partial | timestamp=1778072343.7003644 | source=vosk | frequency_hz=373.8 | rms=316 | updated_at=1778072336.687358
- [2026-05-06 20:59:04] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output
  meta: kind=partial | timestamp=1778072344.1923492 | source=vosk | frequency_hz=373.8 | rms=316 | updated_at=1778072336.687358
- [2026-05-06 20:59:04] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of
  meta: kind=partial | timestamp=1778072344.4444258 | source=vosk | frequency_hz=373.8 | rms=316 | updated_at=1778072336.687358
- [2026-05-06 20:59:04] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output running
  meta: kind=partial | timestamp=1778072344.962983 | source=vosk | frequency_hz=373.8 | rms=316 | updated_at=1778072336.687358
- [2026-05-06 20:59:05] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output running a
  meta: kind=partial | timestamp=1778072345.7281928 | source=vosk | frequency_hz=373.8 | rms=316 | updated_at=1778072336.687358
- [2026-05-06 20:59:06] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output running ai assistant
  meta: kind=partial | timestamp=1778072346.0306976 | source=vosk | frequency_hz=373.8 | rms=316 | updated_at=1778072336.687358
