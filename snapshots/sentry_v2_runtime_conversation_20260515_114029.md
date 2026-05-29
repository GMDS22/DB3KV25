# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-15 11:40:29
- Entries: 121
- Roles: {'assistant': 5, 'system': 39, 'operator': 77}
- Event types: {'assistant_prompt': 2, 'assistant_analysis': 1, 'voice_status': 39, 'voice_transcript_partial': 60, 'voice_transcript_final': 13, 'voice_command': 4, 'spoken_confirmation': 1, 'spoken_reply': 1}
- Channels: {'text': 3, 'voice': 118}
- Latest operator request: event
- Latest assistant message: My role is normal conversation first, then Smart Sentry help, diagnostics, and supported command handling when needed.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-15 11:32:21] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-15 11:32:21] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-15 11:32:26] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778815946.7037117 | source=vosk
- [2026-05-15 11:32:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815947.234802 | source=vosk
- [2026-05-15 11:32:31] operator / voice_transcript_partial / voice: human
  meta: kind=partial | timestamp=1778815951.7447853 | source=vosk
- [2026-05-15 11:32:31] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1778815951.9914336 | source=vosk
- [2026-05-15 11:32:33] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778815953.6697733 | source=final
- [2026-05-15 11:32:33] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-15 11:32:33] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778815953.6707747 | source=vosk
- [2026-05-15 11:32:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815953.6707747 | source=vosk
- [2026-05-15 11:32:33] assistant / spoken_confirmation / voice: Yes. What do you want to know?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-15 11:32:35] system / voice_status / voice: processing
  meta: kind=status | timestamp=1778815955.4277797 | source=state | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778815955.4307795 | source=state | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815955.6700835 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:36] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778815956.6917217 | source=state | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815956.1713855 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:38] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1778815958.9536564 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:39] operator / voice_transcript_partial / voice: yes switching
  meta: kind=partial | timestamp=1778815959.2059553 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:39] operator / voice_transcript_partial / voice: yes what do you want
  meta: kind=partial | timestamp=1778815959.4551585 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:39] operator / voice_transcript_partial / voice: yes what do you want tuning
  meta: kind=partial | timestamp=1778815959.7027154 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:40] operator / voice_transcript_final / voice: what do you do
  meta: kind=final | timestamp=1778815960.387764 | source=final | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:40] system / voice_status / voice: processing
  meta: kind=status | timestamp=1778815960.4163816 | source=state | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:40] system / voice_status / voice: heard
  meta: kind=status | timestamp=1778815960.4163816 | source=state | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:33:04] operator / voice_command / voice: what do you do
  meta: normalized=True
- [2026-05-15 11:33:04] assistant / assistant_prompt / text: My role is normal conversation first, then Smart Sentry help, diagnostics, and supported command handling when needed.
  meta: task_kind=prompt | speak_requested=True
- [2026-05-15 11:33:04] assistant / spoken_reply / voice: My role is normal conversation first, then Smart Sentry help, diagnostics, and supported command handling when needed.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-15 11:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815961.198692 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:41] operator / voice_transcript_partial / voice: yes what do you want to
  meta: kind=partial | timestamp=1778815961.2062042 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:41] operator / voice_transcript_partial / voice: yes what do you want to no detection
  meta: kind=partial | timestamp=1778815961.456013 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:41] operator / voice_transcript_partial / voice: yes what do you want to no
  meta: kind=partial | timestamp=1778815961.7054813 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:41] operator / voice_transcript_partial / voice: yes what do you want to known turn the sound
  meta: kind=partial | timestamp=1778815961.958972 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:42] operator / voice_transcript_partial / voice: yes what do you want to no buzzer the guard
  meta: kind=partial | timestamp=1778815962.2059731 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:42] operator / voice_transcript_partial / voice: yes what do you want to no buzzer need inactive
  meta: kind=partial | timestamp=1778815962.454796 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:42] operator / voice_transcript_partial / voice: yes what do you want to no buzzer need the
  meta: kind=partial | timestamp=1778815962.9569523 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:43] operator / voice_transcript_partial / voice: yes what do you want to no buzzer need the on
  meta: kind=partial | timestamp=1778815963.204231 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778815963.6989632 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:44] operator / voice_transcript_final / voice: yes what do you want to no buzzer need the on
  meta: kind=final | timestamp=1778815964.0097888 | source=final | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815968.9489064 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:48] operator / voice_transcript_partial / voice: yes what do you want to no buzzer need the on loss
  meta: kind=partial | timestamp=1778815968.9554172 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778815969.69857 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:50] operator / voice_transcript_final / voice: yes what do you want to no buzzer need the on loss
  meta: kind=final | timestamp=1778815970.12844 | source=final | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815970.3729177 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:50] operator / voice_transcript_partial / voice: yes what do you want to no buzzer need the on loss
  meta: kind=partial | timestamp=1778815970.3812084 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:52] operator / voice_transcript_final / voice: yes what do you want to no what s buzzer need the on loss
  meta: kind=final | timestamp=1778815972.0561702 | source=final | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815973.332818 | source=vosk | frequency_hz=398.0 | rms=1031 | updated_at=1778815954.4213169
- [2026-05-15 11:32:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778815974.0827792 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:32:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815975.8323133 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:32:56] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1778815976.3399606 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:32:56] operator / voice_transcript_partial / voice: logging
  meta: kind=partial | timestamp=1778815976.5906322 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:32:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778815977.0821846 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:32:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815979.3319144 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:32:59] operator / voice_transcript_partial / voice: logging enabled
  meta: kind=partial | timestamp=1778815979.8380418 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:33:00] operator / voice_transcript_partial / voice: logging enabled the pir
  meta: kind=partial | timestamp=1778815980.3422756 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:33:00] operator / voice_transcript_partial / voice: logging enabled the pir the elliot
  meta: kind=partial | timestamp=1778815980.8543828 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:33:01] operator / voice_transcript_partial / voice: logging enabled the pir the elliot i
  meta: kind=partial | timestamp=1778815981.0877552 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:33:02] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778815982.3606808 | source=partial-timeout | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:33:04] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-15 11:33:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815982.3606808 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:33:02] operator / voice_transcript_partial / voice: logging enabled the pir the elliot i current
  meta: kind=partial | timestamp=1778815982.368225 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:33:04] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778815984.3526297 | source=partial-timeout | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:33:05] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-15 11:33:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815984.8543494 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:33:06] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778815986.0134053 | source=vosk | frequency_hz=278.0 | rms=1038 | updated_at=1778815973.581956
- [2026-05-15 11:33:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815986.0134053 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:07] operator / voice_transcript_partial / voice: microphone
  meta: kind=partial | timestamp=1778815987.5228777 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:08] operator / voice_transcript_final / voice: microphone
  meta: kind=final | timestamp=1778815988.257478 | source=final | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815988.368651 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:08] operator / voice_transcript_partial / voice: microphone recent
  meta: kind=partial | timestamp=1778815988.3921869 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:08] operator / voice_transcript_partial / voice: microphone recent per session
  meta: kind=partial | timestamp=1778815988.7764788 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:09] operator / voice_transcript_partial / voice: microphone recent precision pan
  meta: kind=partial | timestamp=1778815989.0283916 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:09] operator / voice_transcript_partial / voice: microphone recent precision faster
  meta: kind=partial | timestamp=1778815989.5225751 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:09] operator / voice_transcript_partial / voice: microphone recent precision test
  meta: kind=partial | timestamp=1778815989.7697494 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:10] operator / voice_transcript_partial / voice: microphone recent precision test announcements
  meta: kind=partial | timestamp=1778815990.0266354 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:10] operator / voice_transcript_partial / voice: microphone recent precision test smart sentry
  meta: kind=partial | timestamp=1778815990.2743473 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:11] operator / voice_transcript_partial / voice: microphone recent precision test smart sentry how can
  meta: kind=partial | timestamp=1778815991.0296612 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:11] operator / voice_transcript_partial / voice: microphone recent precision test smart sentry how can diagnostics
  meta: kind=partial | timestamp=1778815991.5242627 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:12] operator / voice_transcript_partial / voice: microphone recent precision test smart sentry how can diagnostics trace
  meta: kind=partial | timestamp=1778815992.5396187 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:12] operator / voice_transcript_partial / voice: microphone recent precision test smart sentry how can diagnostics display
  meta: kind=partial | timestamp=1778815992.7759135 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:13] operator / voice_transcript_partial / voice: microphone recent precision test smart sentry how can diagnostics trace diagnostics
  meta: kind=partial | timestamp=1778815993.0259004 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:13] operator / voice_transcript_partial / voice: microphone recent precision test smart sentry how can diagnostics last command
  meta: kind=partial | timestamp=1778815993.5345967 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:14] operator / voice_transcript_final / voice: microphone recent precision test smart sentry how can diagnostics last command
  meta: kind=final | timestamp=1778815994.4100544 | source=final | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815994.6101322 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:14] operator / voice_transcript_partial / voice: microphone recent precision test smart sentry how can diagnostics last command elian make
  meta: kind=partial | timestamp=1778815994.6201358 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:15] operator / voice_transcript_partial / voice: microphone recent precision test smart sentry how can diagnostics last command
  meta: kind=partial | timestamp=1778815995.1240704 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:15] operator / voice_transcript_final / voice: microphone recent precision test smart sentry how can diagnostics last command
  meta: kind=final | timestamp=1778815995.9286923 | source=final | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815996.0753465 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:16] operator / voice_transcript_final / voice: microphone recent precision faster and smart sentry how can diagnostics last command enable
  meta: kind=final | timestamp=1778815996.5205212 | source=final | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:17] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778815997.1354558 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:17] system / voice_status / voice: processing
  meta: kind=status | timestamp=1778815997.1354558 | source=state | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:17] system / voice_status / voice: heard
  meta: kind=status | timestamp=1778815997.1354558 | source=state | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778815997.1364572 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:17] operator / voice_transcript_partial / voice: pan
  meta: kind=partial | timestamp=1778815997.1444569 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:17] operator / voice_transcript_partial / voice: pan target
  meta: kind=partial | timestamp=1778815997.1559634 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:18] operator / voice_transcript_partial / voice: pan pir guard visible
  meta: kind=partial | timestamp=1778815998.3950746 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:19] operator / voice_transcript_partial / voice: pan pir guard visible the
  meta: kind=partial | timestamp=1778815999.1462739 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:19] operator / voice_transcript_partial / voice: pan pir guard visible the overlay
  meta: kind=partial | timestamp=1778815999.395449 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:19] operator / voice_transcript_partial / voice: pan pir guard visible alien is the
  meta: kind=partial | timestamp=1778815999.8973658 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:20] operator / voice_transcript_partial / voice: pan pir guard visible alien is the window on
  meta: kind=partial | timestamp=1778816000.1500578 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:20] operator / voice_transcript_partial / voice: pan pir guard visible alien is the window on no
  meta: kind=partial | timestamp=1778816000.3968072 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:20] operator / voice_transcript_partial / voice: pan pir guard visible alien is the window on no movement
  meta: kind=partial | timestamp=1778816000.646126 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:22] operator / voice_transcript_final / voice: pan pir guard visible the is the window on no movement
  meta: kind=final | timestamp=1778816002.2525575 | source=final | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816002.624153 | source=vosk | frequency_hz=412.0 | rms=976 | updated_at=1778815986.0134053
- [2026-05-15 11:33:23] operator / voice_transcript_partial / voice: event
  meta: kind=partial | timestamp=1778816003.9026272 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:24] operator / voice_transcript_final / voice: event
  meta: kind=final | timestamp=1778816004.6287541 | source=final | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816004.662819 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:24] operator / voice_transcript_partial / voice: reporting enabled
  meta: kind=partial | timestamp=1778816004.699405 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:24] operator / voice_transcript_partial / voice: reporting the alerts
  meta: kind=partial | timestamp=1778816004.8975692 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:25] operator / voice_transcript_partial / voice: one hello deactivate
  meta: kind=partial | timestamp=1778816005.146497 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:25] operator / voice_transcript_partial / voice: one hello the aiming enabled
  meta: kind=partial | timestamp=1778816005.3955228 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:25] operator / voice_transcript_partial / voice: one hello the human voice
  meta: kind=partial | timestamp=1778816005.9134922 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:26] operator / voice_transcript_partial / voice: one hello the ml scoring
  meta: kind=partial | timestamp=1778816006.146538 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816006.63576 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816008.636768 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:28] operator / voice_transcript_partial / voice: one hello the video display
  meta: kind=partial | timestamp=1778816008.664296 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816009.1358387 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816010.6350741 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:31] operator / voice_transcript_partial / voice: one hello the video display anomaly trigger
  meta: kind=partial | timestamp=1778816011.5746615 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:32] operator / voice_transcript_partial / voice: one hello the video display anomaly trigger want
  meta: kind=partial | timestamp=1778816012.071859 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:32] operator / voice_transcript_partial / voice: one hello the video display anomaly trigger what is
  meta: kind=partial | timestamp=1778816012.3239138 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:32] operator / voice_transcript_partial / voice: one hello the video display anomaly trigger what is acoustic
  meta: kind=partial | timestamp=1778816012.5751767 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
- [2026-05-15 11:33:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816013.0651033 | source=vosk | frequency_hz=214.0 | rms=1606 | updated_at=1778816003.1352663
