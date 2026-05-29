# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-06 20:16:52
- Entries: 337
- Roles: {'assistant': 15, 'system': 1, 'operator': 321}
- Event types: {'assistant_prompt': 3, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_partial': 253, 'voice_transcript_final': 47, 'voice_command': 21, 'spoken_confirmation': 9, 'spoken_reply': 2}
- Channels: {'text': 4, 'voice': 333}
- Latest operator request: elion
- Latest assistant message: I am here. Ask your question.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-06 20:09:25] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 20:09:25] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 20:09:27] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778069367.7660723 | source=vosk
- [2026-05-06 20:09:41] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1778069381.6124127 | source=vosk
- [2026-05-06 20:09:42] operator / voice_transcript_partial / voice: buzzer
  meta: kind=partial | timestamp=1778069382.1165335 | source=vosk
- [2026-05-06 20:09:42] operator / voice_transcript_partial / voice: buzzer mute
  meta: kind=partial | timestamp=1778069382.3649554 | source=vosk
- [2026-05-06 20:09:42] operator / voice_transcript_partial / voice: buzzer machine
  meta: kind=partial | timestamp=1778069382.6141632 | source=vosk
- [2026-05-06 20:09:42] operator / voice_transcript_partial / voice: buzzer machine you doing
  meta: kind=partial | timestamp=1778069382.865214 | source=vosk
- [2026-05-06 20:09:43] operator / voice_transcript_final / voice: buzzer machine you doing
  meta: kind=final | timestamp=1778069383.2174952 | source=final
- [2026-05-06 20:09:43] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1778069383.6132834 | source=vosk
- [2026-05-06 20:10:04] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:09:43] operator / voice_transcript_partial / voice: loop
  meta: kind=partial | timestamp=1778069383.8701122 | source=vosk
- [2026-05-06 20:09:44] operator / voice_transcript_final / voice: blink
  meta: kind=final | timestamp=1778069384.7593317 | source=final
- [2026-05-06 20:09:47] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1778069387.862917 | source=vosk
- [2026-05-06 20:09:48] operator / voice_transcript_partial / voice: output
  meta: kind=partial | timestamp=1778069388.1148958 | source=vosk
- [2026-05-06 20:09:48] operator / voice_transcript_partial / voice: automatic
  meta: kind=partial | timestamp=1778069388.3687515 | source=vosk
- [2026-05-06 20:09:48] operator / voice_transcript_partial / voice: to hunt on no detection
  meta: kind=partial | timestamp=1778069388.6153867 | source=vosk
- [2026-05-06 20:09:49] operator / voice_transcript_partial / voice: manual movement
  meta: kind=partial | timestamp=1778069389.1215262 | source=vosk
- [2026-05-06 20:09:49] operator / voice_transcript_partial / voice: local mode switching
  meta: kind=partial | timestamp=1778069389.3624775 | source=vosk
- [2026-05-06 20:09:50] operator / voice_transcript_final / voice: to hunting on local mode switching
  meta: kind=final | timestamp=1778069390.2155714 | source=final
- [2026-05-06 20:09:51] operator / voice_transcript_partial / voice: nano model
  meta: kind=partial | timestamp=1778069391.8666992 | source=vosk
- [2026-05-06 20:09:52] operator / voice_transcript_partial / voice: nano model the natural
  meta: kind=partial | timestamp=1778069392.363419 | source=vosk
- [2026-05-06 20:09:52] operator / voice_transcript_partial / voice: nano model the natural speech
  meta: kind=partial | timestamp=1778069392.6144762 | source=vosk
- [2026-05-06 20:09:52] operator / voice_transcript_partial / voice: nano model the not loading
  meta: kind=partial | timestamp=1778069392.8641877 | source=vosk
- [2026-05-06 20:09:53] operator / voice_transcript_partial / voice: nano model the natural what's the
  meta: kind=partial | timestamp=1778069393.1147275 | source=vosk
- [2026-05-06 20:09:54] operator / voice_transcript_partial / voice: nano model the natural what's the window
  meta: kind=partial | timestamp=1778069394.115661 | source=vosk
- [2026-05-06 20:09:54] operator / voice_transcript_partial / voice: nano model the natural what's the window shortcuts
  meta: kind=partial | timestamp=1778069394.3647907 | source=vosk
- [2026-05-06 20:09:54] operator / voice_transcript_partial / voice: nano model the natural speech cleanup active
  meta: kind=partial | timestamp=1778069394.613737 | source=vosk
- [2026-05-06 20:09:54] operator / voice_transcript_partial / voice: nano model the natural what's the current
  meta: kind=partial | timestamp=1778069394.8670378 | source=vosk
- [2026-05-06 20:09:55] operator / voice_transcript_partial / voice: nano model the natural what's the current eileen greeting
  meta: kind=partial | timestamp=1778069395.6165304 | source=vosk
- [2026-05-06 20:09:56] operator / voice_transcript_final / voice: nano model the natural what s the window active current engaging recovery
  meta: kind=final | timestamp=1778069396.0616443 | source=final
- [2026-05-06 20:09:59] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778069399.616101 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:09:59] operator / voice_transcript_partial / voice: display
  meta: kind=partial | timestamp=1778069399.8644845 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:00] operator / voice_transcript_partial / voice: display disabled
  meta: kind=partial | timestamp=1778069400.1133409 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:00] operator / voice_transcript_partial / voice: spare strict on the blink
  meta: kind=partial | timestamp=1778069400.3640783 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:01] operator / voice_transcript_partial / voice: spare strict on the blink running
  meta: kind=partial | timestamp=1778069401.1209643 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:01] operator / voice_transcript_partial / voice: spare strict on the blink
  meta: kind=partial | timestamp=1778069401.3632655 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:01] operator / voice_transcript_partial / voice: acoustic voice style
  meta: kind=partial | timestamp=1778069401.6366732 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:01] operator / voice_transcript_partial / voice: acoustic voice status
  meta: kind=partial | timestamp=1778069401.8674548 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:02] operator / voice_transcript_partial / voice: acoustic voice style
  meta: kind=partial | timestamp=1778069402.1128285 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:02] operator / voice_transcript_partial / voice: acoustic voice the pan
  meta: kind=partial | timestamp=1778069402.3691769 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:02] operator / voice_transcript_partial / voice: acoustic voice the assistant
  meta: kind=partial | timestamp=1778069402.862509 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:03] operator / voice_transcript_partial / voice: acoustic voice the current active ml
  meta: kind=partial | timestamp=1778069403.1198013 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:03] operator / voice_transcript_partial / voice: acoustic voice the pan inversion
  meta: kind=partial | timestamp=1778069403.3631952 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:03] operator / voice_transcript_partial / voice: acoustic voice the current active ml
  meta: kind=partial | timestamp=1778069403.6132746 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:03] operator / voice_transcript_partial / voice: acoustic voice the pan inversion a
  meta: kind=partial | timestamp=1778069403.8649702 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:04] operator / voice_transcript_partial / voice: acoustic voice the pan inversion a lion
  meta: kind=partial | timestamp=1778069404.119195 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:04] operator / voice_transcript_partial / voice: acoustic voice the pan inversion enabled
  meta: kind=partial | timestamp=1778069404.365838 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:04] operator / voice_transcript_partial / voice: acoustic voice the pan inversion the ml
  meta: kind=partial | timestamp=1778069404.626929 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:05] operator / voice_transcript_final / voice: strict on the blink human voice the pan inversion aim enable
  meta: kind=final | timestamp=1778069405.2234352 | source=final | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:05] operator / voice_transcript_partial / voice: spoken
  meta: kind=partial | timestamp=1778069405.6140673 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:06] operator / voice_transcript_partial / voice: spoken detection
  meta: kind=partial | timestamp=1778069406.4200559 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:06] operator / voice_transcript_partial / voice: spoken the changes
  meta: kind=partial | timestamp=1778069406.4297972 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:07] operator / voice_transcript_final / voice: spoken the changes
  meta: kind=final | timestamp=1778069407.6234455 | source=final | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:07] operator / voice_transcript_partial / voice: window
  meta: kind=partial | timestamp=1778069407.6814785 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:07] operator / voice_transcript_partial / voice: window shortcuts
  meta: kind=partial | timestamp=1778069407.9364202 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:08] operator / voice_transcript_final / voice: window
  meta: kind=final | timestamp=1778069408.830695 | source=final | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:13] operator / voice_transcript_partial / voice: face recognition
  meta: kind=partial | timestamp=1778069413.1941135 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:15] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1778069415.1927333 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:16] operator / voice_transcript_final / voice: running
  meta: kind=final | timestamp=1778069416.048507 | source=final | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:18] operator / voice_transcript_partial / voice: manual
  meta: kind=partial | timestamp=1778069418.687995 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:18] operator / voice_transcript_partial / voice: running
  meta: kind=partial | timestamp=1778069418.937335 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:19] operator / voice_transcript_final / voice: running
  meta: kind=final | timestamp=1778069419.7820475 | source=final | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:34] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778069434.6847966 | source=vosk | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:36] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1778069436.3177333 | source=final | frequency_hz=360.8 | rms=718 | updated_at=1778069397.6068616
- [2026-05-06 20:10:38] operator / voice_transcript_partial / voice: prompted
  meta: kind=partial | timestamp=1778069438.3365207 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:10:40] operator / voice_transcript_final / voice: running
  meta: kind=final | timestamp=1778069440.92384 | source=final | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:10:41] operator / voice_transcript_partial / voice: tuning
  meta: kind=partial | timestamp=1778069441.3364131 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:10:49] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778069449.0874424 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:10:49] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:10:49] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1778069449.335553 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:10:50] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778069450.177308 | source=final | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:10:56] operator / voice_transcript_partial / voice: buzzer mute
  meta: kind=partial | timestamp=1778069456.0874739 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:10:57] operator / voice_transcript_final / voice: buzzer mute
  meta: kind=final | timestamp=1778069457.1789987 | source=final | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:03] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778069463.0868747 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:03] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:11:04] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778069464.1958091 | source=final | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:09] operator / voice_transcript_partial / voice: enabled on
  meta: kind=partial | timestamp=1778069469.3306353 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:09] operator / voice_transcript_partial / voice: reporting enabled
  meta: kind=partial | timestamp=1778069469.581427 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:09] operator / voice_transcript_partial / voice: enabled deactivate
  meta: kind=partial | timestamp=1778069469.8328378 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:10] operator / voice_transcript_partial / voice: enabled deactivate adaptive
  meta: kind=partial | timestamp=1778069470.3323781 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:11] operator / voice_transcript_final / voice: enable deactivate adaptive
  meta: kind=final | timestamp=1778069471.4446092 | source=final | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:14] operator / voice_transcript_partial / voice: run
  meta: kind=partial | timestamp=1778069474.5802915 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:14] operator / voice_transcript_partial / voice: run the smart
  meta: kind=partial | timestamp=1778069474.8300378 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:15] operator / voice_transcript_partial / voice: run the smart sentry
  meta: kind=partial | timestamp=1778069475.0832481 | source=vosk | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:16] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778069476.2409344 | source=final | frequency_hz=276.0 | rms=666 | updated_at=1778069437.0794578
- [2026-05-06 20:11:16] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-06 20:11:16] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:11:30] operator / voice_transcript_partial / voice: give another recognition
  meta: kind=partial | timestamp=1778069490.8185756 | source=vosk | frequency_hz=182.0 | rms=1143 | updated_at=1778069488.7875793
- [2026-05-06 20:11:32] operator / voice_transcript_final / voice: give another matching
  meta: kind=final | timestamp=1778069492.026325 | source=final | frequency_hz=182.0 | rms=1143 | updated_at=1778069488.7875793
- [2026-05-06 20:11:32] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778069492.815576 | source=vosk | frequency_hz=182.0 | rms=1143 | updated_at=1778069488.7875793
- [2026-05-06 20:11:33] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778069493.0682342 | source=vosk | frequency_hz=182.0 | rms=1143 | updated_at=1778069488.7875793
- [2026-05-06 20:11:33] operator / voice_transcript_partial / voice: change your voice to on invert
  meta: kind=partial | timestamp=1778069493.5724473 | source=vosk | frequency_hz=182.0 | rms=1143 | updated_at=1778069488.7875793
- [2026-05-06 20:11:33] operator / voice_transcript_partial / voice: change your voice to on include logs
  meta: kind=partial | timestamp=1778069493.8172474 | source=vosk | frequency_hz=182.0 | rms=1143 | updated_at=1778069488.7875793
- [2026-05-06 20:11:34] operator / voice_transcript_partial / voice: change your voice to on in human voice
  meta: kind=partial | timestamp=1778069494.074629 | source=vosk | frequency_hz=182.0 | rms=1143 | updated_at=1778069488.7875793
- [2026-05-06 20:11:35] operator / voice_transcript_final / voice: change your voice to on in human voice
  meta: kind=final | timestamp=1778069495.2023308 | source=final | frequency_hz=182.0 | rms=1143 | updated_at=1778069488.7875793
- [2026-05-06 20:11:35] operator / voice_command / voice: change your voice to on in human voice
  meta: normalized=True
- [2026-05-06 20:11:37] assistant / spoken_confirmation / voice: Understood. I will use Online English (India) - Neerja now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:11:47] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778069507.1708002 | source=vosk
- [2026-05-06 20:11:47] operator / voice_transcript_partial / voice: voice disabled
  meta: kind=partial | timestamp=1778069507.4268486 | source=vosk
- [2026-05-06 20:11:47] operator / voice_transcript_partial / voice: voice the shortcuts
  meta: kind=partial | timestamp=1778069507.6679785 | source=vosk
- [2026-05-06 20:11:47] operator / voice_transcript_partial / voice: voice the show the
  meta: kind=partial | timestamp=1778069507.9175856 | source=vosk
- [2026-05-06 20:11:48] operator / voice_transcript_final / voice: is voice the show the
  meta: kind=final | timestamp=1778069508.7936578 | source=final
- [2026-05-06 20:11:49] operator / voice_transcript_partial / voice: go leon
  meta: kind=partial | timestamp=1778069509.1720488 | source=vosk
- [2026-05-06 20:11:50] operator / voice_transcript_partial / voice: go leon alion
  meta: kind=partial | timestamp=1778069510.29909 | source=vosk
- [2026-05-06 20:11:50] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:11:50] operator / voice_transcript_partial / voice: go leon alion is assistant
  meta: kind=partial | timestamp=1778069510.5636902 | source=vosk
- [2026-05-06 20:11:50] operator / voice_transcript_partial / voice: go leon alion is
  meta: kind=partial | timestamp=1778069510.8167458 | source=vosk | frequency_hz=122.0 | rms=1204 | updated_at=1778069510.8042305
- [2026-05-06 20:11:53] operator / voice_transcript_partial / voice: hunt on
  meta: kind=partial | timestamp=1778069513.295642 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:11:54] operator / voice_transcript_final / voice: hunt
  meta: kind=final | timestamp=1778069514.1124666 | source=final | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:11:55] operator / voice_transcript_partial / voice: logger
  meta: kind=partial | timestamp=1778069515.0283978 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:11:55] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1778069515.5262072 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:11:58] operator / voice_transcript_partial / voice: the status
  meta: kind=partial | timestamp=1778069518.5291533 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:11:58] operator / voice_transcript_partial / voice: elliot is the recovery
  meta: kind=partial | timestamp=1778069518.7881114 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:11:59] operator / voice_transcript_final / voice: is the status
  meta: kind=final | timestamp=1778069519.1688988 | source=final | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:00] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1778069520.0668406 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:00] operator / voice_transcript_partial / voice: enabled
  meta: kind=partial | timestamp=1778069520.2790184 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:01] operator / voice_transcript_final / voice: enable
  meta: kind=final | timestamp=1778069521.224616 | source=final | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:01] operator / voice_transcript_partial / voice: movement
  meta: kind=partial | timestamp=1778069521.7886062 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:02] operator / voice_transcript_partial / voice: movement again
  meta: kind=partial | timestamp=1778069522.0262754 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:02] operator / voice_transcript_partial / voice: loop enabled
  meta: kind=partial | timestamp=1778069522.4286237 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:03] operator / voice_transcript_partial / voice: loop enabled media loop
  meta: kind=partial | timestamp=1778069523.2850096 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:03] operator / voice_transcript_partial / voice: loop enabled media the pir
  meta: kind=partial | timestamp=1778069523.5328236 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:03] operator / voice_transcript_partial / voice: loop enabled media loop on auto
  meta: kind=partial | timestamp=1778069523.7785609 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:04] operator / voice_transcript_partial / voice: loop enabled media loop on auto invert tilt
  meta: kind=partial | timestamp=1778069524.5275931 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:04] operator / voice_transcript_partial / voice: loop enabled media loop on auto the hello
  meta: kind=partial | timestamp=1778069524.7958233 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:05] operator / voice_transcript_partial / voice: loop enabled media loop on auto the hello assistant
  meta: kind=partial | timestamp=1778069525.0257494 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:05] operator / voice_transcript_partial / voice: loop enabled media loop on auto the hello safe zone
  meta: kind=partial | timestamp=1778069525.5260684 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:06] operator / voice_transcript_final / voice: loop enable media loop on auto the hello safe
  meta: kind=final | timestamp=1778069526.4819553 | source=final | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:07] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1778069527.5268574 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:07] operator / voice_transcript_partial / voice: voice is
  meta: kind=partial | timestamp=1778069527.7850416 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:08] operator / voice_transcript_partial / voice: voice reports
  meta: kind=partial | timestamp=1778069528.0412755 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:08] operator / voice_transcript_partial / voice: voice is the
  meta: kind=partial | timestamp=1778069528.290773 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:09] operator / voice_transcript_final / voice: rest voice is the
  meta: kind=final | timestamp=1778069529.2030697 | source=final | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:16] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1778069536.0408719 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:16] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778069536.2765503 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:16] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:12:16] operator / voice_transcript_partial / voice: alion hide
  meta: kind=partial | timestamp=1778069536.8826058 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:17] operator / voice_transcript_partial / voice: alion hide the
  meta: kind=partial | timestamp=1778069537.0264046 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:17] operator / voice_transcript_partial / voice: alion hide the camera
  meta: kind=partial | timestamp=1778069537.28058 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:17] operator / voice_transcript_partial / voice: alion hide the camera loop
  meta: kind=partial | timestamp=1778069537.5283406 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:18] operator / voice_transcript_final / voice: elion hide the camera loop
  meta: kind=final | timestamp=1778069538.5533953 | source=final | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:19] operator / voice_command / voice: elion hide the camera loop
  meta: normalized=True
- [2026-05-06 20:12:27] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778069547.5361364 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:28] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:12:28] assistant / spoken_confirmation / voice: Yes? I am listening.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:12:27] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1778069547.7948613 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:29] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778069549.0110567 | source=final | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:32] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1778069552.58488 | source=vosk | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:32] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1778069552.751991 | source=final | frequency_hz=106.5 | rms=1205 | updated_at=1778069512.769889
- [2026-05-06 20:12:33] operator / voice_command / voice: yes
  meta: normalized=True
- [2026-05-06 20:12:34] operator / voice_transcript_partial / voice: of acoustic
  meta: kind=partial | timestamp=1778069554.0986254 | source=vosk | frequency_hz=410.0 | rms=1200 | updated_at=1778069553.09377
- [2026-05-06 20:12:34] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778069554.3858762 | source=vosk | frequency_hz=410.0 | rms=1200 | updated_at=1778069553.09377
- [2026-05-06 20:12:34] operator / voice_transcript_partial / voice: is acoustic
  meta: kind=partial | timestamp=1778069554.618775 | source=vosk | frequency_hz=410.0 | rms=1200 | updated_at=1778069553.09377
- [2026-05-06 20:12:34] operator / voice_transcript_partial / voice: is output
  meta: kind=partial | timestamp=1778069554.886696 | source=vosk | frequency_hz=410.0 | rms=1200 | updated_at=1778069553.09377
- [2026-05-06 20:12:35] operator / voice_transcript_final / voice: is output
  meta: kind=final | timestamp=1778069555.557937 | source=final | frequency_hz=410.0 | rms=1200 | updated_at=1778069553.09377
- [2026-05-06 20:12:40] assistant / assistant_prompt / text: You are Elion Mesk, the conversational AI assistant voice for Smart Sentry. Answer naturally, briefly, and like a normal AI unless the operator explicitly asks for runtime status or diagnostics.
  meta: task_kind=prompt | speak_requested=True
- [2026-05-06 20:12:40] assistant / spoken_reply / voice: You are Elion Mesk, the conversational AI assistant voice for Smart Sentry. Answer naturally, briefly, and like a normal AI unless the operator explicitly asks for runtime status or diagnostics.
  meta: interrupt=False | assistant_output=True | spoken=False
- [2026-05-06 20:12:46] operator / voice_transcript_partial / voice: of on
  meta: kind=partial | timestamp=1778069566.3509042 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:46] operator / voice_transcript_final / voice: of on
  meta: kind=final | timestamp=1778069566.991803 | source=final | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:48] operator / voice_transcript_partial / voice: system
  meta: kind=partial | timestamp=1778069568.0982866 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:49] operator / voice_transcript_partial / voice: system elian
  meta: kind=partial | timestamp=1778069569.1042957 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:49] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:12:49] operator / voice_transcript_partial / voice: system of on
  meta: kind=partial | timestamp=1778069569.3977005 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:49] operator / voice_transcript_partial / voice: system of on face name
  meta: kind=partial | timestamp=1778069569.5987508 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:49] operator / voice_transcript_partial / voice: system of on face suppression
  meta: kind=partial | timestamp=1778069569.8587892 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:50] operator / voice_transcript_partial / voice: system of on face
  meta: kind=partial | timestamp=1778069570.0987163 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:50] operator / voice_transcript_final / voice: system of on face
  meta: kind=final | timestamp=1778069570.73323 | source=final | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:51] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1778069571.3576784 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:52] operator / voice_transcript_partial / voice: status engaging scope
  meta: kind=partial | timestamp=1778069572.11191 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:53] operator / voice_transcript_final / voice: the engaging
  meta: kind=final | timestamp=1778069573.024256 | source=final | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:54] operator / voice_transcript_partial / voice: change your
  meta: kind=partial | timestamp=1778069574.6008632 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:54] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778069574.8485003 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:55] operator / voice_transcript_partial / voice: change your voice to
  meta: kind=partial | timestamp=1778069575.3501961 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:55] operator / voice_transcript_partial / voice: change your voice to another
  meta: kind=partial | timestamp=1778069575.5975132 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:55] operator / voice_transcript_partial / voice: change your voice to another command
  meta: kind=partial | timestamp=1778069575.8644047 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:56] operator / voice_transcript_partial / voice: change your voice to another in human
  meta: kind=partial | timestamp=1778069576.0987682 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:56] operator / voice_transcript_partial / voice: change your voice to another in human voice
  meta: kind=partial | timestamp=1778069576.3482094 | source=vosk | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:57] operator / voice_transcript_final / voice: change your voice to another in human voice
  meta: kind=final | timestamp=1778069577.4975557 | source=final | frequency_hz=238.0 | rms=1125 | updated_at=1778069565.094436
- [2026-05-06 20:12:57] operator / voice_command / voice: change your voice to another in human voice
  meta: normalized=True
- [2026-05-06 20:12:58] assistant / spoken_confirmation / voice: Sure thing. I can speak in different voices, and I will now speak as Online English (India) - Neerja.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:13:10] operator / voice_transcript_partial / voice: voice search enabled speak is on continuous video media loop
  meta: kind=partial | timestamp=1778069590.911326 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:13] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:13:13] assistant / spoken_confirmation / voice: Yes. What do you want to know?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:13:20] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1778069600.308721 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:20] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1778069600.5485947 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:21] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1778069601.4286845 | source=final | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:22] operator / voice_command / voice: yes
  meta: normalized=True
- [2026-05-06 20:13:21] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1778069601.8099208 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:22] operator / voice_transcript_partial / voice: what do
  meta: kind=partial | timestamp=1778069602.0547173 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:22] operator / voice_transcript_partial / voice: what do it
  meta: kind=partial | timestamp=1778069602.308356 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:23] operator / voice_transcript_final / voice: what do you do
  meta: kind=final | timestamp=1778069603.123336 | source=final | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:23] operator / voice_command / voice: what do you do
  meta: normalized=True
- [2026-05-06 20:13:23] assistant / assistant_prompt / text: I can talk normally, answer Smart Sentry questions, help diagnose issues when you ask, and handle supported commands.
  meta: task_kind=prompt | speak_requested=True
- [2026-05-06 20:13:24] assistant / spoken_reply / voice: I can talk normally, answer Smart Sentry questions, help diagnose issues when you ask, and handle supported commands.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-06 20:13:23] operator / voice_transcript_partial / voice: to is
  meta: kind=partial | timestamp=1778069603.6010861 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:23] operator / voice_transcript_partial / voice: to is the
  meta: kind=partial | timestamp=1778069603.8790257 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:24] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1778069604.12981 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:24] operator / voice_transcript_partial / voice: to russian
  meta: kind=partial | timestamp=1778069604.3932183 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:24] operator / voice_transcript_partial / voice: to russian dmitry
  meta: kind=partial | timestamp=1778069604.6538048 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:25] operator / voice_transcript_final / voice: to russian dmitry
  meta: kind=final | timestamp=1778069605.984707 | source=final | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:30] operator / voice_transcript_partial / voice: eileen
  meta: kind=partial | timestamp=1778069610.1368847 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:30] operator / voice_transcript_partial / voice: eileen no
  meta: kind=partial | timestamp=1778069610.3822196 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:30] operator / voice_transcript_partial / voice: eileen not loading
  meta: kind=partial | timestamp=1778069610.6448636 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:30] operator / voice_transcript_partial / voice: eileen no known
  meta: kind=partial | timestamp=1778069610.8809967 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:31] operator / voice_transcript_partial / voice: eileen no known on
  meta: kind=partial | timestamp=1778069611.6304367 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:32] operator / voice_transcript_partial / voice: eileen no known on system
  meta: kind=partial | timestamp=1778069612.0624752 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:32] operator / voice_transcript_partial / voice: eileen no known on the smart sentry
  meta: kind=partial | timestamp=1778069612.1381264 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:32] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question
  meta: kind=partial | timestamp=1778069612.8948472 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:33] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hello
  meta: kind=partial | timestamp=1778069613.8960462 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:34] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hello diagnostics
  meta: kind=partial | timestamp=1778069614.1380517 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:34] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual overlay
  meta: kind=partial | timestamp=1778069614.6314917 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:34] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window
  meta: kind=partial | timestamp=1778069614.8926032 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:35] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual slew order
  meta: kind=partial | timestamp=1778069615.144213 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:35] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on the
  meta: kind=partial | timestamp=1778069615.3803735 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:35] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss
  meta: kind=partial | timestamp=1778069615.6306813 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:35] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss active
  meta: kind=partial | timestamp=1778069615.8856175 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:36] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss hunt
  meta: kind=partial | timestamp=1778069616.138745 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:36] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss
  meta: kind=partial | timestamp=1778069616.3832436 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:36] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on is servo motion
  meta: kind=partial | timestamp=1778069616.885258 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:37] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss search on commands
  meta: kind=partial | timestamp=1778069617.3971827 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:38] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on is servo logs running
  meta: kind=partial | timestamp=1778069618.1611726 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:38] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss search on commands i ask a
  meta: kind=partial | timestamp=1778069618.391495 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:38] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss search on commands i ask a the
  meta: kind=partial | timestamp=1778069618.649313 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:39] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss search on commands i ask a the assistant
  meta: kind=partial | timestamp=1778069619.3817036 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:39] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss search on commands i ask a the ask a
  meta: kind=partial | timestamp=1778069619.65352 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:39] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss search on commands i ask a the ask a the status
  meta: kind=partial | timestamp=1778069619.900915 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:40] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss search on commands i ask a the ask a is change your voice
  meta: kind=partial | timestamp=1778069620.382935 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:41] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss search on commands i ask a the ask a is change your voice to russian
  meta: kind=partial | timestamp=1778069621.1423461 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:41] operator / voice_transcript_partial / voice: eileen no known on the smart sentry question hey diagnose visual is window on loss search on commands i ask a the ask a is change your voice to russian dmitry
  meta: kind=partial | timestamp=1778069621.3805141 | source=vosk | frequency_hz=78.0 | rms=1095 | updated_at=1778069585.5447862
- [2026-05-06 20:13:45] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:13:45] assistant / spoken_confirmation / voice: Yes? I am listening.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:13:48] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1778069628.3458166 | source=vosk | frequency_hz=228.0 | rms=712 | updated_at=1778069624.589079
- [2026-05-06 20:13:49] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1778069629.8159902 | source=final | frequency_hz=228.0 | rms=712 | updated_at=1778069624.589079
- [2026-05-06 20:13:50] operator / voice_command / voice: yes
  meta: normalized=True
- [2026-05-06 20:13:49] operator / voice_transcript_partial / voice: fire
  meta: kind=partial | timestamp=1778069629.874337 | source=vosk | frequency_hz=228.0 | rms=712 | updated_at=1778069624.589079
- [2026-05-06 20:13:50] operator / voice_transcript_partial / voice: fire listening
  meta: kind=partial | timestamp=1778069630.3456817 | source=vosk | frequency_hz=228.0 | rms=712 | updated_at=1778069624.589079
- [2026-05-06 20:13:51] operator / voice_transcript_final / voice: fire listening
  meta: kind=final | timestamp=1778069631.2300682 | source=final | frequency_hz=228.0 | rms=712 | updated_at=1778069624.589079
- [2026-05-06 20:13:51] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1778069631.8900478 | source=vosk | frequency_hz=228.0 | rms=712 | updated_at=1778069624.589079
- [2026-05-06 20:13:51] operator / voice_transcript_partial / voice: change your
  meta: kind=partial | timestamp=1778069631.9035666 | source=vosk | frequency_hz=228.0 | rms=712 | updated_at=1778069624.589079
- [2026-05-06 20:13:52] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778069632.1102521 | source=vosk | frequency_hz=228.0 | rms=712 | updated_at=1778069624.589079
- [2026-05-06 20:13:52] operator / voice_transcript_partial / voice: change your voice to russian
  meta: kind=partial | timestamp=1778069632.3470795 | source=vosk | frequency_hz=228.0 | rms=712 | updated_at=1778069624.589079
- [2026-05-06 20:13:52] operator / voice_transcript_partial / voice: change your voice to russian dmitry
  meta: kind=partial | timestamp=1778069632.5998433 | source=vosk | frequency_hz=228.0 | rms=712 | updated_at=1778069624.589079
- [2026-05-06 20:13:54] operator / voice_transcript_final / voice: change your voice to russian dmitry
  meta: kind=final | timestamp=1778069634.0604854 | source=final | frequency_hz=228.0 | rms=712 | updated_at=1778069624.589079
- [2026-05-06 20:13:54] operator / voice_command / voice: change your voice to russian dmitry
  meta: normalized=True
- [2026-05-06 20:13:55] assistant / spoken_confirmation / voice: Done. Voice changed to Online Russian - Dmitry.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:14:11] operator / voice_transcript_partial / voice: is the
  meta: kind=partial | timestamp=1778069651.1358433 | source=vosk
- [2026-05-06 20:14:11] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778069651.3909037 | source=vosk
- [2026-05-06 20:14:11] operator / voice_transcript_partial / voice: name announcements
  meta: kind=partial | timestamp=1778069651.646713 | source=vosk
- [2026-05-06 20:14:11] operator / voice_transcript_partial / voice: the movement export automatic
  meta: kind=partial | timestamp=1778069651.8733294 | source=vosk
- [2026-05-06 20:14:12] operator / voice_transcript_partial / voice: the movement assistant action current
  meta: kind=partial | timestamp=1778069652.1427321 | source=vosk
- [2026-05-06 20:14:12] operator / voice_transcript_partial / voice: the movement assistant action current anomaly
  meta: kind=partial | timestamp=1778069652.3805645 | source=vosk
- [2026-05-06 20:14:12] operator / voice_transcript_partial / voice: the movement assistant action turn off
  meta: kind=partial | timestamp=1778069652.6235597 | source=vosk
- [2026-05-06 20:14:12] operator / voice_transcript_partial / voice: the movement assistant action turn off name
  meta: kind=partial | timestamp=1778069652.9122653 | source=vosk
- [2026-05-06 20:14:13] operator / voice_transcript_partial / voice: the movement assistant action camera
  meta: kind=partial | timestamp=1778069653.1235332 | source=vosk
- [2026-05-06 20:14:13] operator / voice_transcript_partial / voice: the movement assistant action turn off name disabled
  meta: kind=partial | timestamp=1778069653.3833375 | source=vosk
- [2026-05-06 20:14:13] operator / voice_transcript_partial / voice: the movement assistant action turn off laser movement
  meta: kind=partial | timestamp=1778069653.6240768 | source=vosk
- [2026-05-06 20:14:13] operator / voice_transcript_partial / voice: the movement assistant action turn off laser enabled
  meta: kind=partial | timestamp=1778069653.8841746 | source=vosk
- [2026-05-06 20:14:14] operator / voice_transcript_partial / voice: the movement assistant action turn off name disabled enable
  meta: kind=partial | timestamp=1778069654.1404533 | source=vosk
- [2026-05-06 20:14:14] operator / voice_transcript_partial / voice: the movement assistant action turn off name disabled enable go rest
  meta: kind=partial | timestamp=1778069654.3915548 | source=vosk
- [2026-05-06 20:14:14] operator / voice_transcript_partial / voice: the movement assistant action turn off name disabled enable no
  meta: kind=partial | timestamp=1778069654.6263924 | source=vosk
- [2026-05-06 20:14:15] operator / voice_transcript_partial / voice: the movement assistant action turn off name disabled enable known
  meta: kind=partial | timestamp=1778069655.1259549 | source=vosk
- [2026-05-06 20:14:15] operator / voice_transcript_partial / voice: the movement assistant action turn off name disabled enable name
  meta: kind=partial | timestamp=1778069655.3762932 | source=vosk
- [2026-05-06 20:14:15] operator / voice_transcript_partial / voice: the movement assistant action turn off name disabled enable known
  meta: kind=partial | timestamp=1778069655.6406934 | source=vosk
- [2026-05-06 20:14:16] operator / voice_transcript_final / voice: is the the movement assistant action turn off name disable enable no loop on id
  meta: kind=final | timestamp=1778069656.4544663 | source=final
- [2026-05-06 20:14:17] operator / voice_transcript_partial / voice: model
  meta: kind=partial | timestamp=1778069657.6346228 | source=vosk
- [2026-05-06 20:14:18] operator / voice_transcript_final / voice: model
  meta: kind=final | timestamp=1778069658.6480408 | source=final
- [2026-05-06 20:14:19] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778069659.4072168 | source=vosk | frequency_hz=78.0 | rms=703 | updated_at=1778069659.1600313
- [2026-05-06 20:14:19] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778069659.919479 | source=vosk | frequency_hz=78.0 | rms=703 | updated_at=1778069659.1600313
- [2026-05-06 20:14:20] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:14:20] operator / voice_transcript_partial / voice: alion activate
  meta: kind=partial | timestamp=1778069660.1629531 | source=vosk | frequency_hz=78.0 | rms=703 | updated_at=1778069659.1600313
- [2026-05-06 20:14:20] operator / voice_transcript_partial / voice: the current
  meta: kind=partial | timestamp=1778069660.8712873 | source=vosk | frequency_hz=78.0 | rms=703 | updated_at=1778069659.1600313
- [2026-05-06 20:14:22] operator / voice_transcript_final / voice: buzzer off
  meta: kind=final | timestamp=1778069662.2973032 | source=final | frequency_hz=78.0 | rms=703 | updated_at=1778069659.1600313
- [2026-05-06 20:14:23] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1778069663.5996017 | source=vosk | frequency_hz=78.0 | rms=703 | updated_at=1778069659.1600313
- [2026-05-06 20:14:23] operator / voice_transcript_partial / voice: what the
  meta: kind=partial | timestamp=1778069663.8425763 | source=vosk | frequency_hz=78.0 | rms=703 | updated_at=1778069659.1600313
- [2026-05-06 20:14:24] operator / voice_transcript_final / voice: what the
  meta: kind=final | timestamp=1778069664.4347723 | source=final | frequency_hz=78.0 | rms=703 | updated_at=1778069659.1600313
- [2026-05-06 20:14:25] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1778069665.0967538 | source=vosk | frequency_hz=78.0 | rms=703 | updated_at=1778069659.1600313
- [2026-05-06 20:14:39] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1778069679.6424143 | source=vosk | frequency_hz=90.0 | rms=691 | updated_at=1778069679.6233034
- [2026-05-06 20:14:40] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1778069680.3021636 | source=final | frequency_hz=90.0 | rms=691 | updated_at=1778069679.6233034
- [2026-05-06 20:14:53] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778069693.8780446 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:14:54] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:14:55] assistant / spoken_confirmation / voice: Yes? I am listening.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:14:54] operator / voice_transcript_partial / voice: alion hide
  meta: kind=partial | timestamp=1778069694.6299589 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:14:55] operator / voice_transcript_partial / voice: alion hide the video
  meta: kind=partial | timestamp=1778069695.390695 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:14:55] operator / voice_transcript_partial / voice: alion hide the video scoring
  meta: kind=partial | timestamp=1778069695.6287007 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:26] operator / voice_transcript_partial / voice: system
  meta: kind=partial | timestamp=1778069726.9057124 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:27] operator / voice_transcript_partial / voice: disabled
  meta: kind=partial | timestamp=1778069727.129536 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:27] operator / voice_transcript_partial / voice: disable manual
  meta: kind=partial | timestamp=1778069727.3789904 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:27] operator / voice_transcript_partial / voice: disable pan inversion
  meta: kind=partial | timestamp=1778069727.6544483 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:27] operator / voice_transcript_partial / voice: disable automatic lighting
  meta: kind=partial | timestamp=1778069727.8792403 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:28] operator / voice_transcript_partial / voice: disable ml local actions
  meta: kind=partial | timestamp=1778069728.1290584 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:28] operator / voice_transcript_partial / voice: disable ml local mode ml
  meta: kind=partial | timestamp=1778069728.6301694 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:28] operator / voice_transcript_partial / voice: disable ml local matching enabled
  meta: kind=partial | timestamp=1778069728.9478524 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:29] operator / voice_transcript_partial / voice: disable ml local matching anomaly
  meta: kind=partial | timestamp=1778069729.1316001 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:29] operator / voice_transcript_partial / voice: disable ml local matching on no detection
  meta: kind=partial | timestamp=1778069729.379998 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:29] operator / voice_transcript_partial / voice: disable ml local matching on the video
  meta: kind=partial | timestamp=1778069729.8916566 | source=vosk | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:31] operator / voice_transcript_final / voice: disable in local matching on the video
  meta: kind=final | timestamp=1778069731.2800164 | source=final | frequency_hz=414.0 | rms=211 | updated_at=1778069687.121353
- [2026-05-06 20:15:36] operator / voice_transcript_partial / voice: manual
  meta: kind=partial | timestamp=1778069736.0394306 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:36] operator / voice_transcript_final / voice: active
  meta: kind=final | timestamp=1778069736.418938 | source=final | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:36] operator / voice_transcript_partial / voice: per known
  meta: kind=partial | timestamp=1778069736.5500336 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:36] operator / voice_transcript_partial / voice: ml training
  meta: kind=partial | timestamp=1778069736.7889702 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:37] operator / voice_transcript_partial / voice: can i have a
  meta: kind=partial | timestamp=1778069737.0388608 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:37] operator / voice_transcript_partial / voice: hello travel order
  meta: kind=partial | timestamp=1778069737.2909315 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:38] operator / voice_transcript_final / voice: hello travel
  meta: kind=final | timestamp=1778069738.1654294 | source=final | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:38] operator / voice_transcript_partial / voice: the threat
  meta: kind=partial | timestamp=1778069738.2921948 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:38] operator / voice_transcript_partial / voice: known
  meta: kind=partial | timestamp=1778069738.5391512 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:38] operator / voice_transcript_partial / voice: no fire
  meta: kind=partial | timestamp=1778069738.7897058 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:39] operator / voice_transcript_partial / voice: no per known
  meta: kind=partial | timestamp=1778069739.0524302 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:39] operator / voice_transcript_partial / voice: no fire
  meta: kind=partial | timestamp=1778069739.2885234 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:39] operator / voice_transcript_partial / voice: no buzzer in human voice
  meta: kind=partial | timestamp=1778069739.5379062 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:40] operator / voice_transcript_partial / voice: no fire mask mute
  meta: kind=partial | timestamp=1778069740.6966512 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:40] operator / voice_transcript_partial / voice: no fire mask mute enabled
  meta: kind=partial | timestamp=1778069740.7056708 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:40] operator / voice_transcript_partial / voice: no fire mask mute ml
  meta: kind=partial | timestamp=1778069740.713673 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:41] operator / voice_transcript_final / voice: no per known ml mute ml
  meta: kind=final | timestamp=1778069741.7869918 | source=final | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:42] operator / voice_transcript_partial / voice: window shortcuts
  meta: kind=partial | timestamp=1778069742.4861262 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:42] operator / voice_transcript_partial / voice: alion deactivate
  meta: kind=partial | timestamp=1778069742.7081552 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:42] operator / voice_transcript_partial / voice: window camera
  meta: kind=partial | timestamp=1778069742.961393 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:43] operator / voice_transcript_partial / voice: window guard enabled
  meta: kind=partial | timestamp=1778069743.218111 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:43] operator / voice_transcript_partial / voice: window guard on the pan
  meta: kind=partial | timestamp=1778069743.4929914 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:43] operator / voice_transcript_partial / voice: window guard on the pan inversion
  meta: kind=partial | timestamp=1778069743.7081401 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:44] operator / voice_transcript_partial / voice: window guard on the pan
  meta: kind=partial | timestamp=1778069744.045352 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:44] operator / voice_transcript_partial / voice: window guard on the pan acoustic
  meta: kind=partial | timestamp=1778069744.7064395 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:44] operator / voice_transcript_partial / voice: window guard on the pan the current status
  meta: kind=partial | timestamp=1778069744.985408 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:45] operator / voice_transcript_partial / voice: window guard on the pan acoustic voice
  meta: kind=partial | timestamp=1778069745.228492 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:45] operator / voice_transcript_partial / voice: window guard on the pan acoustic alion
  meta: kind=partial | timestamp=1778069745.4550989 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:46] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:15:46] assistant / spoken_confirmation / voice: I am here. Ask your question.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:15:45] operator / voice_transcript_partial / voice: window guard on the pan acoustic alion decrease
  meta: kind=partial | timestamp=1778069745.7269204 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:45] operator / voice_transcript_partial / voice: window guard on the pan acoustic alion go home
  meta: kind=partial | timestamp=1778069745.9800508 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:46] operator / voice_transcript_partial / voice: window guard on the pan acoustic alion go e
  meta: kind=partial | timestamp=1778069746.2067552 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:46] operator / voice_transcript_partial / voice: window guard on the pan acoustic alion go e lion
  meta: kind=partial | timestamp=1778069746.45746 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:46] operator / voice_transcript_partial / voice: window guard on the pan acoustic alion go rest
  meta: kind=partial | timestamp=1778069746.9725547 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:47] operator / voice_transcript_partial / voice: window guard on the pan acoustic alion go e
  meta: kind=partial | timestamp=1778069747.2259285 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:47] operator / voice_transcript_partial / voice: window guard on the pan acoustic alion go e precision
  meta: kind=partial | timestamp=1778069747.4554446 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:47] operator / voice_transcript_partial / voice: window guard on the pan acoustic alion go e greeting is
  meta: kind=partial | timestamp=1778069747.7077644 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:47] operator / voice_transcript_partial / voice: window guard on the pan acoustic alion go e greeting is adaptive
  meta: kind=partial | timestamp=1778069747.9723027 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
- [2026-05-06 20:15:49] operator / voice_transcript_partial / voice: window guard on the pan acoustic alion go e greeting is of ml
  meta: kind=partial | timestamp=1778069749.0374277 | source=vosk | frequency_hz=230.0 | rms=616 | updated_at=1778069732.0324712
