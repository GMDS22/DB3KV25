# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-05 14:42:03
- Entries: 611
- Roles: {'assistant': 50, 'system': 1, 'operator': 560}
- Event types: {'assistant_prompt': 19, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 21, 'voice_transcript_partial': 378, 'voice_transcript_final': 125, 'voice_command': 57, 'spoken_reply': 9}
- Channels: {'text': 20, 'voice': 591}
- Latest operator request: set
- Latest assistant message: Assistant update. I could not reach the local model, but the top deterministic finding is: Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=on; pir=on. This was generated using local fallback guidance.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 14:29:05] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:29:05] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 14:29:08] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777962548.5571012 | source=vosk
- [2026-05-05 14:29:08] assistant / spoken_confirmation / voice: Smart Sentry AI is online. What do you want me to do first?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:29:27] operator / voice_transcript_partial / voice: can
  meta: kind=partial | timestamp=1777962567.8941984 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:29:28] operator / voice_transcript_partial / voice: can you
  meta: kind=partial | timestamp=1777962568.1443224 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:29:28] operator / voice_transcript_partial / voice: can you connect the
  meta: kind=partial | timestamp=1777962568.3923848 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:29:28] operator / voice_transcript_partial / voice: can you connect the boards
  meta: kind=partial | timestamp=1777962568.8925326 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:29:30] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777962570.0504534 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:29:47] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-05 14:29:48] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 14:29:52] operator / voice_transcript_final / voice: smart
  meta: kind=final | timestamp=1777962592.0760174 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:29:55] operator / voice_transcript_partial / voice: recognition
  meta: kind=partial | timestamp=1777962595.57244 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:29:56] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777962596.584158 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:29:57] operator / voice_transcript_partial / voice: say smart
  meta: kind=partial | timestamp=1777962597.5710754 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:29:57] operator / voice_transcript_partial / voice: say smart sentry
  meta: kind=partial | timestamp=1777962597.8352242 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:29:58] operator / voice_transcript_final / voice: say smart
  meta: kind=final | timestamp=1777962598.668469 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:00] operator / voice_transcript_partial / voice: tell
  meta: kind=partial | timestamp=1777962600.0722904 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:00] operator / voice_transcript_final / voice: task
  meta: kind=final | timestamp=1777962600.5832317 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:02] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777962602.5853212 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:03] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1777962603.08838 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:04] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777962604.3330898 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:10] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777962610.5758584 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:11] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1777962611.0850246 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:11] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777962611.5706747 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:12] operator / voice_transcript_final / voice: face
  meta: kind=final | timestamp=1777962612.738923 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:14] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1777962614.8321586 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:15] operator / voice_transcript_partial / voice: hey alion
  meta: kind=partial | timestamp=1777962615.0786574 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:15] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 14:30:16] operator / voice_transcript_final / voice: elion hey
  meta: kind=final | timestamp=1777962616.3996944 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:16] operator / voice_command / voice: elion hey
  meta: normalized=True
- [2026-05-05 14:30:25] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777962625.582119 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:26] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777962626.5780854 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:26] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 14:30:31] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777962631.5874467 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:31] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777962631.8361683 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:32] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777962632.0741866 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:32] operator / voice_transcript_partial / voice: tracking pause
  meta: kind=partial | timestamp=1777962632.3280945 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:32] operator / voice_transcript_partial / voice: tracking pause smart
  meta: kind=partial | timestamp=1777962632.5825818 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:33] operator / voice_transcript_partial / voice: tracking strict on
  meta: kind=partial | timestamp=1777962633.3282368 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:34] operator / voice_transcript_final / voice: tracking strict on
  meta: kind=final | timestamp=1777962634.7191885 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:34] operator / voice_command / voice: tracking strict on
  meta: normalized=True
- [2026-05-05 14:30:34] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777962634.7329807 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:34] operator / voice_transcript_partial / voice: guard hey
  meta: kind=partial | timestamp=1777962634.9859672 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:35] operator / voice_transcript_final / voice: guard hey
  meta: kind=final | timestamp=1777962635.979765 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:36] operator / voice_command / voice: guard hey
  meta: normalized=True
- [2026-05-05 14:30:40] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777962640.2266345 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:40] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777962640.4894762 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:40] operator / voice_transcript_final / voice: tracking
  meta: kind=final | timestamp=1777962640.9782655 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:41] operator / voice_command / voice: tracking
  meta: normalized=True
- [2026-05-05 14:30:41] operator / voice_transcript_partial / voice: switch profile
  meta: kind=partial | timestamp=1777962641.9772098 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:43] operator / voice_transcript_final / voice: switch a joke
  meta: kind=final | timestamp=1777962643.0157342 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:43] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1777962643.5871677 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:44] operator / voice_transcript_partial / voice: hey position
  meta: kind=partial | timestamp=1777962644.0897412 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:44] operator / voice_transcript_final / voice: hey position
  meta: kind=final | timestamp=1777962644.8405232 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:45] operator / voice_transcript_partial / voice: same
  meta: kind=partial | timestamp=1777962645.1386218 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:45] operator / voice_transcript_partial / voice: same but
  meta: kind=partial | timestamp=1777962645.3383632 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:45] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1777962645.5896223 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:45] operator / voice_transcript_final / voice: it
  meta: kind=final | timestamp=1777962645.8411112 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:46] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777962646.3445406 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:46] operator / voice_transcript_partial / voice: app
  meta: kind=partial | timestamp=1777962646.605767 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:46] operator / voice_transcript_partial / voice: app to
  meta: kind=partial | timestamp=1777962646.8412476 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:47] operator / voice_transcript_partial / voice: talk
  meta: kind=partial | timestamp=1777962647.0979543 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:47] operator / voice_transcript_partial / voice: talk less
  meta: kind=partial | timestamp=1777962647.339824 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:30:48] operator / voice_transcript_final / voice: app talk
  meta: kind=final | timestamp=1777962648.0097651 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:03] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777962663.856052 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:04] operator / voice_transcript_partial / voice: tracking that
  meta: kind=partial | timestamp=1777962664.378224 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:04] operator / voice_transcript_final / voice: tracking that
  meta: kind=final | timestamp=1777962664.8519328 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:05] operator / voice_transcript_partial / voice: style
  meta: kind=partial | timestamp=1777962665.3485615 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:10] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777962670.105637 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:22] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777962682.100361 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:22] operator / voice_transcript_partial / voice: guarding
  meta: kind=partial | timestamp=1777962682.6079493 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:22] operator / voice_transcript_partial / voice: quiet
  meta: kind=partial | timestamp=1777962682.8506286 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:23] operator / voice_transcript_final / voice: elion lion quiet
  meta: kind=final | timestamp=1777962683.1023445 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:23] operator / voice_command / voice: elion lion quiet
  meta: normalized=True
- [2026-05-05 14:31:24] assistant / spoken_confirmation / voice: Received. I started your assistant request about lion quiet in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:31:28] operator / voice_transcript_partial / voice: i
  meta: kind=partial | timestamp=1777962688.358709 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:28] operator / voice_transcript_partial / voice: hi start tracking
  meta: kind=partial | timestamp=1777962688.6024106 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:29] operator / voice_transcript_final / voice: hi start
  meta: kind=final | timestamp=1777962689.364193 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:29] operator / voice_command / voice: hi start
  meta: normalized=True
- [2026-05-05 14:31:33] operator / voice_transcript_partial / voice: identify yourself
  meta: kind=partial | timestamp=1777962693.1250262 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:33] operator / voice_transcript_final / voice: identify
  meta: kind=final | timestamp=1777962693.8653007 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:34] operator / voice_command / voice: identify
  meta: normalized=True
- [2026-05-05 14:31:36] operator / voice_transcript_partial / voice: can
  meta: kind=partial | timestamp=1777962696.2081065 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:36] operator / voice_transcript_partial / voice: can you
  meta: kind=partial | timestamp=1777962696.4461377 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:36] operator / voice_transcript_partial / voice: can you analyze
  meta: kind=partial | timestamp=1777962696.6207383 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:36] operator / voice_transcript_partial / voice: can you analyze the
  meta: kind=partial | timestamp=1777962696.861095 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:37] operator / voice_transcript_partial / voice: can you analyze the app
  meta: kind=partial | timestamp=1777962697.1761277 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:37] operator / voice_transcript_partial / voice: can you analyze stop
  meta: kind=partial | timestamp=1777962697.3632185 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:38] operator / voice_transcript_final / voice: can you analyze stop
  meta: kind=final | timestamp=1777962698.1133137 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:38] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777962698.3638453 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:38] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777962698.6110742 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:38] operator / voice_transcript_partial / voice: e not
  meta: kind=partial | timestamp=1777962698.866848 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:39] operator / voice_transcript_partial / voice: e not why
  meta: kind=partial | timestamp=1777962699.2511442 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:39] operator / voice_transcript_partial / voice: e not why same
  meta: kind=partial | timestamp=1777962699.6161435 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:39] operator / voice_transcript_partial / voice: e not why same but
  meta: kind=partial | timestamp=1777962699.865699 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:40] operator / voice_transcript_final / voice: e not why same
  meta: kind=final | timestamp=1777962700.4024284 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:41] operator / voice_transcript_partial / voice: analyze
  meta: kind=partial | timestamp=1777962701.393085 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:41] operator / voice_transcript_partial / voice: analyze the
  meta: kind=partial | timestamp=1777962701.6398137 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:42] operator / voice_transcript_partial / voice: analyze the behavior
  meta: kind=partial | timestamp=1777962702.1145518 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:43] operator / voice_transcript_final / voice: analyze the behavior
  meta: kind=final | timestamp=1777962703.227894 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:52] operator / voice_transcript_partial / voice: lion set
  meta: kind=partial | timestamp=1777962712.5102165 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:53] operator / voice_transcript_final / voice: elion lion set
  meta: kind=final | timestamp=1777962713.4856791 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:53] operator / voice_command / voice: elion lion set
  meta: normalized=True
- [2026-05-05 14:31:53] assistant / assistant_prompt / text: Assistant request queued: assistant request about lion set (position 1).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:31:54] operator / voice_transcript_partial / voice: but faster
  meta: kind=partial | timestamp=1777962714.7521422 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:55] operator / voice_transcript_final / voice: but faster
  meta: kind=final | timestamp=1777962715.785831 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:56] operator / voice_command / voice: but faster
  meta: normalized=True
- [2026-05-05 14:31:57] assistant / spoken_confirmation / voice: I am still finishing assistant request about lion quiet. I queued your assistant request about lion set. It is number 1 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 14:31:58] operator / voice_transcript_partial / voice: speak
  meta: kind=partial | timestamp=1777962718.0292158 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:59] operator / voice_transcript_final / voice: speak
  meta: kind=final | timestamp=1777962719.1261592 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:31:59] operator / voice_command / voice: speak
  meta: normalized=True
- [2026-05-05 14:32:01] operator / voice_transcript_partial / voice: quiet
  meta: kind=partial | timestamp=1777962721.672045 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:02] operator / voice_transcript_final / voice: quiet
  meta: kind=final | timestamp=1777962722.1896667 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:02] operator / voice_command / voice: quiet
  meta: normalized=True
- [2026-05-05 14:32:11] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777962731.463223 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:12] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777962732.1638267 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:12] operator / voice_transcript_final / voice: sentry
  meta: kind=final | timestamp=1777962732.965011 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:18] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1777962738.0255034 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:18] operator / voice_transcript_partial / voice: voice style
  meta: kind=partial | timestamp=1777962738.5239737 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:18] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1777962738.7771018 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:19] operator / voice_transcript_final / voice: voice
  meta: kind=final | timestamp=1777962739.2719398 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:23] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777962743.534521 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:24] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777962744.0393627 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:24] operator / voice_transcript_partial / voice: why is
  meta: kind=partial | timestamp=1777962744.3115385 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:24] operator / voice_transcript_partial / voice: hi disable
  meta: kind=partial | timestamp=1777962744.5330172 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:24] operator / voice_transcript_final / voice: why
  meta: kind=final | timestamp=1777962744.787131 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:29] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:32:30] assistant / spoken_reply / voice: Assistant update. I could not reach the local model, but the top deterministic finding is: Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=on; pir=on. This was generated using local fallback guidance.
  meta: interrupt=False | assistant_output=True | spoken=False
- [2026-05-05 14:32:30] operator / voice_transcript_partial / voice: not face
  meta: kind=partial | timestamp=1777962750.0523574 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:30] operator / voice_transcript_partial / voice: not why
  meta: kind=partial | timestamp=1777962750.0668201 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:30] operator / voice_transcript_partial / voice: connect smart sentry
  meta: kind=partial | timestamp=1777962750.5334065 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:30] operator / voice_transcript_partial / voice: not lion say
  meta: kind=partial | timestamp=1777962750.7877758 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:31] operator / voice_transcript_final / voice: elion command lion say
  meta: kind=final | timestamp=1777962751.6133714 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:32] operator / voice_command / voice: elion command lion say
  meta: normalized=True
- [2026-05-05 14:32:32] assistant / assistant_prompt / text: Assistant request queued: assistant request about command lion say (position 1).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:32:32] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777962752.7936983 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:33] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777962753.5100405 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:34] operator / voice_command / voice: guard
  meta: normalized=True
- [2026-05-05 14:32:35] assistant / spoken_confirmation / voice: I am still finishing assistant request about lion set. I queued your assistant request about command lion say. It is number 1 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:32:36] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777962756.785284 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:37] operator / voice_transcript_partial / voice: change the
  meta: kind=partial | timestamp=1777962757.1277974 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:37] operator / voice_transcript_partial / voice: change the last
  meta: kind=partial | timestamp=1777962757.5197837 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:37] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777962757.5453165 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:38] operator / voice_transcript_partial / voice: same is not loading
  meta: kind=partial | timestamp=1777962758.0600169 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:38] operator / voice_transcript_partial / voice: hey leon no app
  meta: kind=partial | timestamp=1777962758.2830272 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:39] operator / voice_transcript_partial / voice: hey leon no app shortcuts
  meta: kind=partial | timestamp=1777962759.0337882 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:39] operator / voice_transcript_partial / voice: hey leon no app shortcuts what
  meta: kind=partial | timestamp=1777962759.3100505 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:40] operator / voice_transcript_final / voice: elion say no app shortcuts what
  meta: kind=final | timestamp=1777962760.0796714 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:40] operator / voice_command / voice: elion say no app shortcuts what
  meta: normalized=True
- [2026-05-05 14:32:40] assistant / assistant_prompt / text: Assistant request queued: assistant request about say no app shortcuts what (position 2).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:32:42] assistant / spoken_confirmation / voice: I am still finishing assistant request about lion set. I queued your assistant request about say no app shortcuts what. It is number 2 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:32:43] operator / voice_transcript_partial / voice: are you
  meta: kind=partial | timestamp=1777962763.554165 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:43] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777962763.8316314 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:44] operator / voice_transcript_partial / voice: are you do
  meta: kind=partial | timestamp=1777962764.1784594 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:44] operator / voice_transcript_partial / voice: i use motion
  meta: kind=partial | timestamp=1777962764.3879619 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:44] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777962764.5561268 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:44] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1777962764.8173995 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:45] operator / voice_transcript_partial / voice: assistant auto
  meta: kind=partial | timestamp=1777962765.0923998 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:45] operator / voice_transcript_partial / voice: assistant a question
  meta: kind=partial | timestamp=1777962765.3133922 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:46] operator / voice_transcript_final / voice: i use motion assistant a question
  meta: kind=final | timestamp=1777962766.6265056 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:47] operator / voice_command / voice: i use motion assistant a question
  meta: normalized=True
- [2026-05-05 14:32:48] assistant / assistant_prompt / text: Assistant request queued: assistant request about i use motion assistant a question (position 3).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:32:48] operator / voice_transcript_partial / voice: system
  meta: kind=partial | timestamp=1777962768.2000988 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:48] operator / voice_transcript_partial / voice: assistant auto
  meta: kind=partial | timestamp=1777962768.410993 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:49] operator / voice_transcript_final / voice: system
  meta: kind=final | timestamp=1777962769.2082684 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:50] operator / voice_command / voice: system
  meta: normalized=True
- [2026-05-05 14:32:51] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777962771.165166 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:51] operator / voice_transcript_partial / voice: is not
  meta: kind=partial | timestamp=1777962771.4108975 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:52] operator / voice_transcript_partial / voice: use motion
  meta: kind=partial | timestamp=1777962772.1816113 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:52] operator / voice_transcript_final / voice: use nano model
  meta: kind=final | timestamp=1777962772.8621485 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:53] operator / voice_command / voice: use nano model
  meta: normalized=True
- [2026-05-05 14:32:55] assistant / spoken_confirmation / voice: I am still finishing assistant request about lion set. I queued your assistant request about i use motion assistant a question. It is number 3 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:32:56] operator / voice_transcript_partial / voice: whats
  meta: kind=partial | timestamp=1777962776.0208433 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:56] operator / voice_transcript_partial / voice: what talk
  meta: kind=partial | timestamp=1777962776.3418396 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:56] operator / voice_transcript_partial / voice: what talk less
  meta: kind=partial | timestamp=1777962776.5453143 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:57] operator / voice_transcript_final / voice: what talk
  meta: kind=final | timestamp=1777962777.2938058 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:32:57] operator / voice_command / voice: what talk
  meta: normalized=True
- [2026-05-05 14:33:04] operator / voice_transcript_partial / voice: i yourself
  meta: kind=partial | timestamp=1777962784.661374 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:04] operator / voice_transcript_partial / voice: are you status
  meta: kind=partial | timestamp=1777962784.994017 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:05] operator / voice_transcript_partial / voice: i ask a joke
  meta: kind=partial | timestamp=1777962785.1982844 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:05] operator / voice_transcript_partial / voice: i use detection is
  meta: kind=partial | timestamp=1777962785.5565174 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:05] operator / voice_transcript_partial / voice: i ask a assistant
  meta: kind=partial | timestamp=1777962785.7085137 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:06] operator / voice_transcript_final / voice: i you status
  meta: kind=final | timestamp=1777962786.1819532 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:06] operator / voice_command / voice: i you status
  meta: normalized=True
- [2026-05-05 14:33:06] operator / voice_transcript_partial / voice: question
  meta: kind=partial | timestamp=1777962786.2907188 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:07] operator / voice_transcript_partial / voice: question why
  meta: kind=partial | timestamp=1777962787.3693635 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:07] operator / voice_transcript_partial / voice: question why set
  meta: kind=partial | timestamp=1777962787.7120445 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:08] operator / voice_transcript_partial / voice: question why set i
  meta: kind=partial | timestamp=1777962788.4162805 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:08] operator / voice_transcript_final / voice: question again why set
  meta: kind=final | timestamp=1777962788.6717625 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:09] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:33:09] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1777962789.9327834 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:10] operator / voice_transcript_partial / voice: hey switch
  meta: kind=partial | timestamp=1777962790.2408814 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:10] operator / voice_transcript_final / voice: paused
  meta: kind=final | timestamp=1777962790.4262195 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:15] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777962795.3847115 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:15] operator / voice_transcript_partial / voice: that is not
  meta: kind=partial | timestamp=1777962795.640573 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:16] operator / voice_transcript_partial / voice: that is not that
  meta: kind=partial | timestamp=1777962796.1373985 | source=vosk | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:16] operator / voice_transcript_final / voice: that is not that
  meta: kind=final | timestamp=1777962796.7007158 | source=final | frequency_hz=290.0 | rms=380 | updated_at=1777962562.3870103
- [2026-05-05 14:33:36] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:33:37] assistant / spoken_reply / voice: Assistant update. I could not reach the local model, but the top deterministic finding is: Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=on; pir=on. This was generated using local fallback guidance.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 14:34:01] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777962841.8228626 | source=vosk | frequency_hz=152.0 | rms=538 | updated_at=1777962817.7998888
- [2026-05-05 14:34:03] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1777962843.3190327 | source=vosk | frequency_hz=152.0 | rms=538 | updated_at=1777962817.7998888
- [2026-05-05 14:34:04] operator / voice_transcript_final / voice: detection
  meta: kind=final | timestamp=1777962844.2355726 | source=final | frequency_hz=152.0 | rms=538 | updated_at=1777962817.7998888
- [2026-05-05 14:34:09] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1777962849.3778956 | source=final | frequency_hz=120.0 | rms=544 | updated_at=1777962844.8411922
- [2026-05-05 14:34:13] operator / voice_transcript_partial / voice: motion
  meta: kind=partial | timestamp=1777962853.9919238 | source=vosk | frequency_hz=120.0 | rms=544 | updated_at=1777962844.8411922
- [2026-05-05 14:34:15] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777962855.022062 | source=vosk | frequency_hz=120.0 | rms=544 | updated_at=1777962844.8411922
- [2026-05-05 14:34:15] operator / voice_transcript_final / voice: set
  meta: kind=final | timestamp=1777962855.7551599 | source=final | frequency_hz=120.0 | rms=544 | updated_at=1777962844.8411922
- [2026-05-05 14:34:19] operator / voice_transcript_partial / voice: wrong
  meta: kind=partial | timestamp=1777962859.7237606 | source=vosk | frequency_hz=120.0 | rms=544 | updated_at=1777962844.8411922
- [2026-05-05 14:34:20] operator / voice_transcript_partial / voice: load profile
  meta: kind=partial | timestamp=1777962860.2391696 | source=vosk | frequency_hz=120.0 | rms=544 | updated_at=1777962844.8411922
- [2026-05-05 14:34:21] operator / voice_transcript_final / voice: wrong
  meta: kind=final | timestamp=1777962861.038581 | source=final | frequency_hz=120.0 | rms=544 | updated_at=1777962844.8411922
- [2026-05-05 14:34:30] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777962870.6273723 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:34:30] operator / voice_transcript_partial / voice: guard detection
  meta: kind=partial | timestamp=1777962870.8940988 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:34:31] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777962871.294124 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:34:35] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777962875.1494603 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:34:35] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777962875.3863335 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:34:35] operator / voice_transcript_final / voice: decrease
  meta: kind=final | timestamp=1777962875.8846564 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:34:36] operator / voice_transcript_partial / voice: profile
  meta: kind=partial | timestamp=1777962876.1358154 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:34:37] operator / voice_transcript_partial / voice: speak
  meta: kind=partial | timestamp=1777962877.0351858 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:34:37] operator / voice_transcript_final / voice: speak
  meta: kind=final | timestamp=1777962877.4282072 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:34:42] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:34:43] assistant / spoken_reply / voice: Assistant update. I could not reach the local model, but the top deterministic finding is: Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=on; pir=on. This was generated using local fallback guidance.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 14:35:03] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1777962903.902135 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:04] operator / voice_transcript_partial / voice: assistant auto
  meta: kind=partial | timestamp=1777962904.1412714 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:04] operator / voice_transcript_final / voice: assistant
  meta: kind=final | timestamp=1777962904.896451 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:05] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777962905.143192 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:06] operator / voice_transcript_partial / voice: not model
  meta: kind=partial | timestamp=1777962906.2299027 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:06] operator / voice_transcript_final / voice: not model
  meta: kind=final | timestamp=1777962906.4191206 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:07] operator / voice_transcript_partial / voice: confidence
  meta: kind=partial | timestamp=1777962907.139043 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:10] operator / voice_transcript_partial / voice: object
  meta: kind=partial | timestamp=1777962910.9014666 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:11] operator / voice_transcript_partial / voice: object detection
  meta: kind=partial | timestamp=1777962911.1583452 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:11] operator / voice_transcript_partial / voice: object detection tracking
  meta: kind=partial | timestamp=1777962911.8910599 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:12] operator / voice_transcript_partial / voice: object detection tracking smart
  meta: kind=partial | timestamp=1777962912.1512377 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:12] operator / voice_transcript_final / voice: object detection tracking
  meta: kind=final | timestamp=1777962912.4430916 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:12] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777962912.6527054 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:12] operator / voice_transcript_partial / voice: personality
  meta: kind=partial | timestamp=1777962912.8909328 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:13] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1777962913.391679 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:13] operator / voice_transcript_partial / voice: use large
  meta: kind=partial | timestamp=1777962913.6427937 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:13] operator / voice_transcript_partial / voice: voice lion
  meta: kind=partial | timestamp=1777962913.9013405 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:14] operator / voice_transcript_partial / voice: use large model
  meta: kind=partial | timestamp=1777962914.1603055 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:14] operator / voice_transcript_partial / voice: voice style
  meta: kind=partial | timestamp=1777962914.8446348 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:14] operator / voice_transcript_partial / voice: voice lion repeat
  meta: kind=partial | timestamp=1777962914.9085612 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:15] operator / voice_transcript_partial / voice: voice load profile
  meta: kind=partial | timestamp=1777962915.142012 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:15] operator / voice_transcript_final / voice: use profile
  meta: kind=final | timestamp=1777962915.4258237 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:16] operator / voice_command / voice: use profile
  meta: normalized=True
- [2026-05-05 14:35:17] operator / voice_transcript_partial / voice: rest
  meta: kind=partial | timestamp=1777962917.3893101 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:18] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:35:18] operator / voice_transcript_final / voice: rest
  meta: kind=final | timestamp=1777962918.1408372 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:18] operator / voice_command / voice: rest
  meta: normalized=True
- [2026-05-05 14:35:19] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777962919.4167178 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:20] operator / voice_transcript_partial / voice: last personality
  meta: kind=partial | timestamp=1777962920.1678796 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:20] operator / voice_transcript_final / voice: last
  meta: kind=final | timestamp=1777962920.5708892 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:21] operator / voice_command / voice: last
  meta: normalized=True
- [2026-05-05 14:35:21] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777962921.437973 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:21] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777962921.6416755 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:23] operator / voice_transcript_final / voice: set
  meta: kind=final | timestamp=1777962923.2560208 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:24] operator / voice_command / voice: set
  meta: normalized=True
- [2026-05-05 14:35:23] operator / voice_transcript_partial / voice: neutral
  meta: kind=partial | timestamp=1777962923.3432374 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:24] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:35:23] operator / voice_transcript_final / voice: neutral
  meta: kind=final | timestamp=1777962923.8344965 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:24] operator / voice_command / voice: neutral
  meta: normalized=True
- [2026-05-05 14:35:24] operator / voice_transcript_partial / voice: theme
  meta: kind=partial | timestamp=1777962924.380668 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:24] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777962924.9617655 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:25] operator / voice_transcript_final / voice: theme
  meta: kind=final | timestamp=1777962925.0696383 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:25] operator / voice_command / voice: theme
  meta: normalized=True
- [2026-05-05 14:35:27] operator / voice_transcript_partial / voice: talk
  meta: kind=partial | timestamp=1777962927.073816 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:27] operator / voice_transcript_partial / voice: talk less
  meta: kind=partial | timestamp=1777962927.5847156 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:29] operator / voice_transcript_final / voice: talk less
  meta: kind=final | timestamp=1777962929.299429 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:29] operator / voice_command / voice: talk less
  meta: normalized=True
- [2026-05-05 14:35:32] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:35:32] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 14:35:32] assistant / spoken_confirmation / voice: I think I heard rest. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 14:35:32] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 14:35:32] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 14:35:32] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777962932.5662558 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:32] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777962932.8905036 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:33] operator / voice_transcript_partial / voice: tracking hey
  meta: kind=partial | timestamp=1777962933.0865676 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:33] operator / voice_transcript_partial / voice: tracking hey shortcuts
  meta: kind=partial | timestamp=1777962933.9607046 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:34] operator / voice_transcript_partial / voice: tracking pause smart
  meta: kind=partial | timestamp=1777962934.363219 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:34] operator / voice_transcript_final / voice: tracking hey shortcuts
  meta: kind=final | timestamp=1777962934.6215606 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:35] operator / voice_command / voice: tracking hey shortcuts
  meta: normalized=True
- [2026-05-05 14:35:37] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777962937.6391225 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:38] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1777962938.1884077 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:38] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1777962938.3909078 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:38] operator / voice_command / voice: yes
  meta: normalized=True
- [2026-05-05 14:35:38] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777962938.6467466 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:38] operator / voice_transcript_partial / voice: to com
  meta: kind=partial | timestamp=1777962938.901461 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:43] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777962943.4102585 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:43] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777962943.6553266 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:43] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777962943.898594 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:44] operator / voice_transcript_final / voice: tracking
  meta: kind=final | timestamp=1777962944.1672053 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:44] operator / voice_transcript_partial / voice: joke
  meta: kind=partial | timestamp=1777962944.8932488 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:48] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:35:48] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777962948.968866 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:50] assistant / spoken_reply / voice: Assistant update. I could not reach the local model, but the top deterministic finding is: Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=on; pir=on. This was generated using local fallback guidance.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 14:35:49] operator / voice_transcript_partial / voice: stay leon
  meta: kind=partial | timestamp=1777962949.4617887 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:50] operator / voice_transcript_partial / voice: stay leon no
  meta: kind=partial | timestamp=1777962950.2180939 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:50] operator / voice_transcript_partial / voice: stay leon no app
  meta: kind=partial | timestamp=1777962950.560523 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:50] operator / voice_transcript_partial / voice: stay leon no app to
  meta: kind=partial | timestamp=1777962950.7256827 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:50] operator / voice_transcript_partial / voice: stay leon talk less
  meta: kind=partial | timestamp=1777962950.970031 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:51] operator / voice_transcript_partial / voice: stay leon start tracking
  meta: kind=partial | timestamp=1777962951.2101111 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:51] operator / voice_transcript_partial / voice: stay leon no shortcuts
  meta: kind=partial | timestamp=1777962951.4961958 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:51] operator / voice_transcript_final / voice: elion stay no talk neutral
  meta: kind=final | timestamp=1777962951.7612207 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:35:53] operator / voice_command / voice: elion stay no talk neutral
  meta: normalized=True
- [2026-05-05 14:35:53] assistant / assistant_prompt / text: Assistant request queued: assistant request about stay no talk neutral (position 1).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:35:55] assistant / spoken_confirmation / voice: I am still finishing assistant request about i use motion assistant a question. I queued your assistant request about stay no talk neutral. It is number 1 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:36:08] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1777962968.7927105 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:09] operator / voice_transcript_partial / voice: assistant auto
  meta: kind=partial | timestamp=1777962969.2427576 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:09] operator / voice_transcript_partial / voice: assistant auto speak
  meta: kind=partial | timestamp=1777962969.741118 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:10] operator / voice_transcript_partial / voice: assistant auto
  meta: kind=partial | timestamp=1777962970.476513 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:10] operator / voice_transcript_final / voice: assistant auto
  meta: kind=final | timestamp=1777962970.7565305 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:14] operator / voice_transcript_partial / voice: object detection
  meta: kind=partial | timestamp=1777962974.500758 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:14] operator / voice_transcript_partial / voice: object detection is
  meta: kind=partial | timestamp=1777962974.7917223 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:15] operator / voice_transcript_partial / voice: object detection
  meta: kind=partial | timestamp=1777962975.1510162 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:15] operator / voice_transcript_final / voice: object detection
  meta: kind=final | timestamp=1777962975.4961777 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:16] operator / voice_transcript_partial / voice: object
  meta: kind=partial | timestamp=1777962976.006107 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:16] operator / voice_transcript_partial / voice: object detection
  meta: kind=partial | timestamp=1777962976.224771 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:16] operator / voice_transcript_partial / voice: object
  meta: kind=partial | timestamp=1777962976.9898686 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:17] operator / voice_transcript_partial / voice: object brightness
  meta: kind=partial | timestamp=1777962977.2429452 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:17] operator / voice_transcript_partial / voice: object brightness queued tasks
  meta: kind=partial | timestamp=1777962977.541519 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:18] operator / voice_transcript_partial / voice: object brightness go rest
  meta: kind=partial | timestamp=1777962978.2774928 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:18] operator / voice_transcript_final / voice: object brightness status
  meta: kind=final | timestamp=1777962978.5392475 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:18] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777962978.9764805 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:19] operator / voice_transcript_partial / voice: go home
  meta: kind=partial | timestamp=1777962979.2270987 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:19] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777962979.783838 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:20] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777962980.2276797 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:21] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 14:36:21] operator / voice_transcript_final / voice: you
  meta: kind=final | timestamp=1777962981.0197456 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:22] operator / voice_command / voice: you
  meta: normalized=True
- [2026-05-05 14:36:22] operator / voice_transcript_partial / voice: recognition
  meta: kind=partial | timestamp=1777962982.8145878 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:25] operator / voice_transcript_partial / voice: personality
  meta: kind=partial | timestamp=1777962985.1638358 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:26] operator / voice_transcript_final / voice: personality
  meta: kind=final | timestamp=1777962986.2600524 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:28] operator / voice_command / voice: personality
  meta: normalized=True
- [2026-05-05 14:36:28] assistant / assistant_prompt / text: Assistant request queued: assistant request about personality (position 2).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:36:30] assistant / spoken_confirmation / voice: I am still finishing assistant request about i use motion assistant a question. I queued your assistant request about personality. It is number 2 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:36:30] operator / voice_transcript_partial / voice: want to
  meta: kind=partial | timestamp=1777962990.2246478 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:30] operator / voice_transcript_partial / voice: why face
  meta: kind=partial | timestamp=1777962990.4356294 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:30] operator / voice_transcript_partial / voice: why face detection
  meta: kind=partial | timestamp=1777962990.930776 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:31] operator / voice_transcript_partial / voice: why face
  meta: kind=partial | timestamp=1777962991.2045875 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:31] operator / voice_transcript_final / voice: why face
  meta: kind=final | timestamp=1777962991.468962 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:32] operator / voice_command / voice: why face
  meta: normalized=True
- [2026-05-05 14:36:32] operator / voice_transcript_partial / voice: hold position
  meta: kind=partial | timestamp=1777962992.1113546 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:33] operator / voice_transcript_partial / voice: disconnect
  meta: kind=partial | timestamp=1777962993.35648 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:33] operator / voice_transcript_partial / voice: switch profile
  meta: kind=partial | timestamp=1777962993.6839619 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:34] operator / voice_transcript_final / voice: response delay
  meta: kind=final | timestamp=1777962994.2268417 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:35] operator / voice_command / voice: response delay
  meta: normalized=True
- [2026-05-05 14:36:35] operator / voice_transcript_partial / voice: resume guarding
  meta: kind=partial | timestamp=1777962995.8656535 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:38] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777962998.224944 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:38] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777962998.4519348 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:38] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777962998.7049613 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:38] operator / voice_transcript_partial / voice: tracking ports
  meta: kind=partial | timestamp=1777962998.9743426 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:39] operator / voice_transcript_partial / voice: tracking port
  meta: kind=partial | timestamp=1777962999.225636 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:40] operator / voice_transcript_final / voice: tracking port
  meta: kind=final | timestamp=1777963000.111545 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:41] operator / voice_command / voice: tracking port
  meta: normalized=True
- [2026-05-05 14:36:40] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777963000.1471353 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:40] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777963000.155753 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:40] operator / voice_transcript_partial / voice: all use
  meta: kind=partial | timestamp=1777963000.577983 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:41] operator / voice_transcript_final / voice: all use
  meta: kind=final | timestamp=1777963001.2588708 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:43] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777963003.3989453 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:43] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777963003.7011564 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:43] operator / voice_transcript_partial / voice: tracking port
  meta: kind=partial | timestamp=1777963003.8874264 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:44] operator / voice_transcript_final / voice: tracking port
  meta: kind=final | timestamp=1777963004.135052 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:44] operator / voice_transcript_partial / voice: joke
  meta: kind=partial | timestamp=1777963004.3823242 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:44] operator / voice_transcript_partial / voice: shortcuts
  meta: kind=partial | timestamp=1777963004.6967022 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:45] operator / voice_transcript_final / voice: shortcuts
  meta: kind=final | timestamp=1777963005.469578 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:50] operator / voice_transcript_final / voice: hold position
  meta: kind=final | timestamp=1777963010.4283829 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:52] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777963012.2408652 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:52] operator / voice_transcript_partial / voice: set go
  meta: kind=partial | timestamp=1777963012.731263 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:53] operator / voice_transcript_partial / voice: set not loading
  meta: kind=partial | timestamp=1777963013.2425447 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:53] operator / voice_transcript_partial / voice: set leon go ahead
  meta: kind=partial | timestamp=1777963013.4617739 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:53] operator / voice_transcript_partial / voice: set leon no
  meta: kind=partial | timestamp=1777963013.7796853 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:55] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:36:54] operator / voice_transcript_partial / voice: set leon no talk
  meta: kind=partial | timestamp=1777963014.1622615 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:54] operator / voice_transcript_partial / voice: set leon no shortcuts
  meta: kind=partial | timestamp=1777963014.2530541 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:54] operator / voice_transcript_final / voice: elion set no shortcuts
  meta: kind=final | timestamp=1777963014.9195347 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:56] operator / voice_command / voice: elion set no shortcuts
  meta: normalized=True
- [2026-05-05 14:36:56] assistant / assistant_prompt / text: Assistant request queued: assistant request about set no shortcuts (position 2).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:36:57] assistant / spoken_reply / voice: Assistant update. I could not reach the local model, but the top deterministic finding is: Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=on; pir=on. This was generated using local fallback guidance.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 14:36:58] assistant / spoken_confirmation / voice: I am still finishing assistant request about stay no talk neutral. I queued your assistant request about set no shortcuts. It is number 2 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 14:36:58] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777963018.979775 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:36:59] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777963019.5084803 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:00] operator / voice_command / voice: guard
  meta: normalized=True
- [2026-05-05 14:37:00] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777963020.4942513 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:02] operator / voice_transcript_partial / voice: system
  meta: kind=partial | timestamp=1777963022.2264612 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:02] operator / voice_transcript_partial / voice: sentry cancel
  meta: kind=partial | timestamp=1777963022.4963412 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:02] operator / voice_transcript_partial / voice: sentry yes
  meta: kind=partial | timestamp=1777963022.7901862 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:03] operator / voice_transcript_final / voice: sentry yes
  meta: kind=final | timestamp=1777963023.3208575 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:04] operator / voice_command / voice: sentry yes
  meta: normalized=True
- [2026-05-05 14:37:03] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777963023.4786901 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:04] operator / voice_transcript_partial / voice: decrease confidence
  meta: kind=partial | timestamp=1777963024.4988208 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:04] operator / voice_transcript_partial / voice: decrease speed
  meta: kind=partial | timestamp=1777963024.7587957 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:05] operator / voice_transcript_partial / voice: decrease elliot the
  meta: kind=partial | timestamp=1777963025.6766858 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:05] operator / voice_transcript_partial / voice: decrease elliot the board
  meta: kind=partial | timestamp=1777963025.731112 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:06] operator / voice_transcript_final / voice: elion decrease the board
  meta: kind=final | timestamp=1777963026.0856133 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:06] operator / voice_command / voice: elion decrease the board
  meta: normalized=True
- [2026-05-05 14:37:06] assistant / assistant_prompt / text: Assistant request queued: assistant request about decrease the board (position 3).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:37:08] assistant / spoken_confirmation / voice: I am still finishing assistant request about stay no talk neutral. I queued your assistant request about decrease the board. It is number 3 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:37:17] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1777963037.8738062 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:18] operator / voice_transcript_partial / voice: assistant auto
  meta: kind=partial | timestamp=1777963038.103336 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:18] operator / voice_transcript_final / voice: assistant
  meta: kind=final | timestamp=1777963038.915538 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:19] operator / voice_command / voice: assistant
  meta: normalized=True
- [2026-05-05 14:37:19] operator / voice_transcript_partial / voice: hi
  meta: kind=partial | timestamp=1777963039.103069 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:19] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777963039.3519866 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:19] operator / voice_transcript_partial / voice: not response
  meta: kind=partial | timestamp=1777963039.6411994 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:19] operator / voice_transcript_partial / voice: not resume
  meta: kind=partial | timestamp=1777963039.8433716 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:20] operator / voice_transcript_partial / voice: not resume on
  meta: kind=partial | timestamp=1777963040.3509042 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:20] operator / voice_transcript_partial / voice: not resume on commands
  meta: kind=partial | timestamp=1777963040.623047 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:22] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 14:37:21] operator / voice_transcript_final / voice: not resume on
  meta: kind=final | timestamp=1777963041.0965266 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:21] operator / voice_transcript_partial / voice: shortcuts
  meta: kind=partial | timestamp=1777963041.3421986 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:23] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1777963043.6283796 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:25] operator / voice_transcript_final / voice: detection
  meta: kind=final | timestamp=1777963045.0142348 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:26] operator / voice_transcript_partial / voice: stop
  meta: kind=partial | timestamp=1777963046.496438 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:27] operator / voice_transcript_final / voice: stop
  meta: kind=final | timestamp=1777963047.347825 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:27] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777963047.750978 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:28] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777963048.5895505 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:30] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777963050.2438333 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:30] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777963050.7509162 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:31] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777963051.0053487 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:31] operator / voice_transcript_final / voice: speed smart less
  meta: kind=final | timestamp=1777963051.7470896 | source=final | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:33] operator / voice_transcript_partial / voice: be more
  meta: kind=partial | timestamp=1777963053.3005974 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:33] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777963053.529098 | source=vosk | frequency_hz=90.0 | rms=535 | updated_at=1777962861.5553908
- [2026-05-05 14:37:34] operator / voice_transcript_final / voice: last
  meta: kind=final | timestamp=1777963054.0539744 | source=final | frequency_hz=114.0 | rms=300 | updated_at=1777963053.752875
- [2026-05-05 14:37:35] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777963055.561405 | source=vosk | frequency_hz=114.0 | rms=300 | updated_at=1777963053.752875
- [2026-05-05 14:37:36] operator / voice_transcript_final / voice: set
  meta: kind=final | timestamp=1777963056.0131247 | source=final | frequency_hz=114.0 | rms=300 | updated_at=1777963053.752875
- [2026-05-05 14:37:36] operator / voice_transcript_partial / voice: talk
  meta: kind=partial | timestamp=1777963056.7641912 | source=vosk | frequency_hz=114.0 | rms=300 | updated_at=1777963053.752875
- [2026-05-05 14:37:40] operator / voice_transcript_partial / voice: change personality
  meta: kind=partial | timestamp=1777963060.576371 | source=vosk | frequency_hz=114.0 | rms=300 | updated_at=1777963053.752875
- [2026-05-05 14:37:40] operator / voice_transcript_partial / voice: port
  meta: kind=partial | timestamp=1777963060.7870266 | source=vosk | frequency_hz=114.0 | rms=300 | updated_at=1777963053.752875
- [2026-05-05 14:37:41] operator / voice_transcript_partial / voice: ports on
  meta: kind=partial | timestamp=1777963061.2687306 | source=vosk | frequency_hz=114.0 | rms=300 | updated_at=1777963053.752875
- [2026-05-05 14:37:41] operator / voice_transcript_final / voice: port on
  meta: kind=final | timestamp=1777963061.5570166 | source=final | frequency_hz=114.0 | rms=300 | updated_at=1777963053.752875
- [2026-05-05 14:37:42] operator / voice_transcript_partial / voice: disconnect
  meta: kind=partial | timestamp=1777963062.2596853 | source=vosk | frequency_hz=114.0 | rms=300 | updated_at=1777963053.752875
- [2026-05-05 14:37:46] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777963066.7883592 | source=final | frequency_hz=396.0 | rms=460 | updated_at=1777963065.2805545
- [2026-05-05 14:37:52] operator / voice_transcript_partial / voice: strict
  meta: kind=partial | timestamp=1777963072.310986 | source=vosk | frequency_hz=396.0 | rms=460 | updated_at=1777963065.2805545
- [2026-05-05 14:37:52] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777963072.7965865 | source=vosk | frequency_hz=396.0 | rms=460 | updated_at=1777963065.2805545
- [2026-05-05 14:37:53] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777963073.340891 | source=final | frequency_hz=396.0 | rms=460 | updated_at=1777963065.2805545
- [2026-05-05 14:37:54] operator / voice_transcript_partial / voice: e set
  meta: kind=partial | timestamp=1777963074.5488255 | source=vosk | frequency_hz=396.0 | rms=460 | updated_at=1777963065.2805545
- [2026-05-05 14:37:55] operator / voice_transcript_final / voice: e set
  meta: kind=final | timestamp=1777963075.3139157 | source=final | frequency_hz=396.0 | rms=460 | updated_at=1777963065.2805545
- [2026-05-05 14:37:57] operator / voice_transcript_partial / voice: task
  meta: kind=partial | timestamp=1777963077.1062138 | source=vosk | frequency_hz=396.0 | rms=460 | updated_at=1777963065.2805545
- [2026-05-05 14:37:57] operator / voice_transcript_final / voice: task
  meta: kind=final | timestamp=1777963077.6523569 | source=final | frequency_hz=396.0 | rms=460 | updated_at=1777963065.2805545
- [2026-05-05 14:37:59] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777963079.3129072 | source=vosk | frequency_hz=396.0 | rms=460 | updated_at=1777963065.2805545
- [2026-05-05 14:37:59] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1777963079.5415614 | source=vosk | frequency_hz=396.0 | rms=460 | updated_at=1777963065.2805545
- [2026-05-05 14:37:59] operator / voice_transcript_partial / voice: current speak
  meta: kind=partial | timestamp=1777963079.8042958 | source=vosk | frequency_hz=396.0 | rms=460 | updated_at=1777963065.2805545
- [2026-05-05 14:38:00] operator / voice_transcript_final / voice: current speak
  meta: kind=final | timestamp=1777963080.2949522 | source=final | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:00] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777963080.5271814 | source=vosk | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:01] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:38:01] operator / voice_transcript_final / voice: tracking
  meta: kind=final | timestamp=1777963081.4162252 | source=final | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:01] operator / voice_transcript_partial / voice: to com
  meta: kind=partial | timestamp=1777963081.5403166 | source=vosk | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:01] operator / voice_transcript_partial / voice: to talk
  meta: kind=partial | timestamp=1777963081.777921 | source=vosk | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:02] operator / voice_transcript_partial / voice: to talk is
  meta: kind=partial | timestamp=1777963082.1023178 | source=vosk | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:03] assistant / spoken_reply / voice: Assistant update. I could not reach the local model, but the top deterministic finding is: Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=on; pir=on. This was generated using local fallback guidance.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 14:38:02] operator / voice_transcript_final / voice: to talk is
  meta: kind=final | timestamp=1777963082.7933393 | source=final | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:10] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777963090.3686285 | source=vosk | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:10] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777963090.8853335 | source=final | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:11] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777963091.879046 | source=vosk | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:12] operator / voice_transcript_final / voice: set
  meta: kind=final | timestamp=1777963092.6208868 | source=final | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:13] operator / voice_transcript_partial / voice: want to
  meta: kind=partial | timestamp=1777963093.3682601 | source=vosk | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:14] operator / voice_transcript_partial / voice: want serial
  meta: kind=partial | timestamp=1777963094.144107 | source=vosk | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:14] operator / voice_transcript_partial / voice: want serial yes
  meta: kind=partial | timestamp=1777963094.8753605 | source=vosk | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:15] operator / voice_transcript_final / voice: want serial yes
  meta: kind=final | timestamp=1777963095.125636 | source=final | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:16] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777963096.9574885 | source=vosk | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:18] operator / voice_transcript_final / voice: speak
  meta: kind=final | timestamp=1777963098.2720492 | source=final | frequency_hz=364.0 | rms=341 | updated_at=1777963080.1010678
- [2026-05-05 14:38:45] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777963125.367436 | source=vosk | frequency_hz=360.0 | rms=345 | updated_at=1777963108.6100802
- [2026-05-05 14:38:46] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 14:38:45] operator / voice_transcript_partial / voice: e lion why
  meta: kind=partial | timestamp=1777963125.895343 | source=vosk | frequency_hz=360.0 | rms=345 | updated_at=1777963108.6100802
- [2026-05-05 14:38:46] operator / voice_transcript_partial / voice: e lion set
  meta: kind=partial | timestamp=1777963126.8006263 | source=vosk | frequency_hz=360.0 | rms=345 | updated_at=1777963108.6100802
- [2026-05-05 14:38:48] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 14:38:48] operator / voice_transcript_final / voice: elion set
  meta: kind=final | timestamp=1777963128.063617 | source=final | frequency_hz=360.0 | rms=345 | updated_at=1777963108.6100802
- [2026-05-05 14:38:50] operator / voice_command / voice: elion set
  meta: normalized=True
- [2026-05-05 14:38:50] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777963130.738142 | source=vosk | frequency_hz=360.0 | rms=345 | updated_at=1777963108.6100802
- [2026-05-05 14:38:51] operator / voice_transcript_partial / voice: what say
  meta: kind=partial | timestamp=1777963131.4907322 | source=vosk | frequency_hz=360.0 | rms=345 | updated_at=1777963108.6100802
- [2026-05-05 14:38:52] operator / voice_transcript_final / voice: what say
  meta: kind=final | timestamp=1777963132.2423887 | source=final | frequency_hz=360.0 | rms=345 | updated_at=1777963108.6100802
- [2026-05-05 14:38:53] operator / voice_command / voice: what say
  meta: normalized=True
- [2026-05-05 14:38:58] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777963138.3283648 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:38:58] operator / voice_transcript_partial / voice: can i want
  meta: kind=partial | timestamp=1777963138.5799572 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:38:58] operator / voice_transcript_partial / voice: not lion
  meta: kind=partial | timestamp=1777963138.873498 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:38:59] operator / voice_transcript_partial / voice: not lion same but
  meta: kind=partial | timestamp=1777963139.1221743 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:38:59] operator / voice_transcript_final / voice: elion not lion same
  meta: kind=final | timestamp=1777963139.8439121 | source=final | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:39:00] operator / voice_command / voice: elion not lion same
  meta: normalized=True
- [2026-05-05 14:39:00] assistant / assistant_prompt / text: Assistant request queued: assistant request about not lion same (position 3).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:39:02] assistant / spoken_confirmation / voice: I am still finishing assistant request about personality. I queued your assistant request about not lion same. It is number 3 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 14:39:05] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777963145.0914836 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:39:05] operator / voice_transcript_partial / voice: e not
  meta: kind=partial | timestamp=1777963145.4551623 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:39:05] operator / voice_transcript_partial / voice: e not face
  meta: kind=partial | timestamp=1777963145.5882983 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:39:05] operator / voice_transcript_partial / voice: e lion why
  meta: kind=partial | timestamp=1777963145.8394516 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:39:07] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 14:39:06] operator / voice_transcript_partial / voice: e not hi
  meta: kind=partial | timestamp=1777963146.0868301 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:39:06] operator / voice_transcript_partial / voice: e not hi say
  meta: kind=partial | timestamp=1777963146.3370275 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:39:06] operator / voice_transcript_partial / voice: e not hi say it
  meta: kind=partial | timestamp=1777963146.585382 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:39:07] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:39:06] operator / voice_transcript_partial / voice: e not hi say is not
  meta: kind=partial | timestamp=1777963146.8584144 | source=vosk | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:39:09] assistant / spoken_reply / voice: Assistant update. I could not reach the local model, but the top deterministic finding is: Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=on; pir=on. This was generated using local fallback guidance.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 14:39:08] operator / voice_transcript_final / voice: e not hi say is not
  meta: kind=final | timestamp=1777963148.5532796 | source=final | frequency_hz=396.0 | rms=314 | updated_at=1777963134.2998703
- [2026-05-05 14:39:10] operator / voice_command / voice: e not hi say is not
  meta: normalized=True
- [2026-05-05 14:39:16] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777963156.603544 | source=vosk | frequency_hz=400.0 | rms=329 | updated_at=1777963149.304738
- [2026-05-05 14:39:17] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777963157.3644226 | source=final | frequency_hz=400.0 | rms=329 | updated_at=1777963149.304738
- [2026-05-05 14:39:18] operator / voice_command / voice: guard
  meta: normalized=True
- [2026-05-05 14:39:17] operator / voice_transcript_partial / voice: shortcuts
  meta: kind=partial | timestamp=1777963157.5746517 | source=vosk | frequency_hz=400.0 | rms=329 | updated_at=1777963149.304738
- [2026-05-05 14:39:17] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777963157.821939 | source=vosk | frequency_hz=400.0 | rms=329 | updated_at=1777963149.304738
- [2026-05-05 14:39:18] operator / voice_transcript_partial / voice: set personality
  meta: kind=partial | timestamp=1777963158.5932858 | source=vosk | frequency_hz=400.0 | rms=329 | updated_at=1777963149.304738
- [2026-05-05 14:39:19] operator / voice_transcript_final / voice: set the
  meta: kind=final | timestamp=1777963159.565337 | source=final | frequency_hz=400.0 | rms=329 | updated_at=1777963149.304738
- [2026-05-05 14:39:20] operator / voice_command / voice: set the
  meta: normalized=True
- [2026-05-05 14:39:21] operator / voice_transcript_partial / voice: wait
  meta: kind=partial | timestamp=1777963161.0960104 | source=vosk | frequency_hz=400.0 | rms=329 | updated_at=1777963149.304738
- [2026-05-05 14:39:21] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777963161.3248215 | source=vosk | frequency_hz=400.0 | rms=329 | updated_at=1777963149.304738
- [2026-05-05 14:39:21] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777963161.6000896 | source=vosk | frequency_hz=400.0 | rms=329 | updated_at=1777963149.304738
- [2026-05-05 14:39:22] operator / voice_transcript_final / voice: face
  meta: kind=final | timestamp=1777963162.5160878 | source=final | frequency_hz=400.0 | rms=329 | updated_at=1777963149.304738
- [2026-05-05 14:39:23] operator / voice_command / voice: face
  meta: normalized=True
- [2026-05-05 14:39:45] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777963185.7570205 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:46] operator / voice_transcript_partial / voice: hi
  meta: kind=partial | timestamp=1777963186.0056968 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:46] operator / voice_transcript_partial / voice: hi set
  meta: kind=partial | timestamp=1777963186.5070026 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:47] operator / voice_transcript_final / voice: hi set
  meta: kind=final | timestamp=1777963187.5120385 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:50] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777963190.76131 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:51] operator / voice_transcript_partial / voice: can i face
  meta: kind=partial | timestamp=1777963191.005977 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:51] operator / voice_transcript_partial / voice: can i hi
  meta: kind=partial | timestamp=1777963191.2581685 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:51] operator / voice_transcript_partial / voice: can i hi set
  meta: kind=partial | timestamp=1777963191.505732 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:51] operator / voice_transcript_partial / voice: can i hi same
  meta: kind=partial | timestamp=1777963191.7572806 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:52] operator / voice_transcript_partial / voice: can i hi same but
  meta: kind=partial | timestamp=1777963192.0115886 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:52] operator / voice_transcript_final / voice: can i hi same
  meta: kind=final | timestamp=1777963192.5089624 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:56] operator / voice_transcript_partial / voice: e not
  meta: kind=partial | timestamp=1777963196.76085 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:57] operator / voice_transcript_partial / voice: e not face
  meta: kind=partial | timestamp=1777963197.0111198 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:57] operator / voice_transcript_partial / voice: e not why
  meta: kind=partial | timestamp=1777963197.2691205 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:58] operator / voice_transcript_partial / voice: e not hi set
  meta: kind=partial | timestamp=1777963198.0076032 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:39:58] operator / voice_transcript_final / voice: e not hi set
  meta: kind=final | timestamp=1777963198.7591436 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:08] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777963208.7721379 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:09] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 14:40:09] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777963209.0182729 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:09] operator / voice_transcript_partial / voice: not for
  meta: kind=partial | timestamp=1777963209.267483 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:09] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777963209.5198479 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:10] operator / voice_transcript_partial / voice: not the
  meta: kind=partial | timestamp=1777963210.0218902 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:10] operator / voice_transcript_partial / voice: not theme
  meta: kind=partial | timestamp=1777963210.268459 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:10] operator / voice_transcript_partial / voice: e lion why is not
  meta: kind=partial | timestamp=1777963210.5214012 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:11] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 14:40:12] operator / voice_transcript_final / voice: not why theme is not
  meta: kind=final | timestamp=1777963212.076739 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:13] operator / voice_command / voice: not why theme is not
  meta: normalized=True
- [2026-05-05 14:40:14] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:40:17] assistant / spoken_reply / voice: Assistant update. I could not reach the local model, but the top deterministic finding is: Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=on; pir=on. This was generated using local fallback guidance.
  meta: interrupt=False | assistant_output=True | spoken=False
- [2026-05-05 14:40:18] operator / voice_transcript_partial / voice: camera
  meta: kind=partial | timestamp=1777963218.8924537 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:19] operator / voice_transcript_partial / voice: camera face
  meta: kind=partial | timestamp=1777963219.142547 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:19] operator / voice_transcript_partial / voice: camera profile
  meta: kind=partial | timestamp=1777963219.402297 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:19] operator / voice_transcript_partial / voice: camera face detection
  meta: kind=partial | timestamp=1777963219.6569228 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:19] operator / voice_transcript_partial / voice: can i hi disable
  meta: kind=partial | timestamp=1777963219.8922973 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:20] operator / voice_transcript_partial / voice: can i hi same
  meta: kind=partial | timestamp=1777963220.1440558 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:20] operator / voice_transcript_partial / voice: can i hi say
  meta: kind=partial | timestamp=1777963220.4002256 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:21] operator / voice_transcript_final / voice: camera profile the theme
  meta: kind=final | timestamp=1777963221.0261638 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:22] operator / voice_command / voice: camera profile the theme
  meta: normalized=True
- [2026-05-05 14:40:28] operator / voice_transcript_partial / voice: hi
  meta: kind=partial | timestamp=1777963228.6449623 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:29] operator / voice_transcript_final / voice: hi
  meta: kind=final | timestamp=1777963229.8658714 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:33] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777963233.7819567 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:34] operator / voice_transcript_partial / voice: can i why
  meta: kind=partial | timestamp=1777963234.2925107 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:35] operator / voice_transcript_partial / voice: can i hi set
  meta: kind=partial | timestamp=1777963235.102375 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:35] operator / voice_transcript_final / voice: can i hi theme
  meta: kind=final | timestamp=1777963235.789715 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:40] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777963240.7907588 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:41] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777963241.0434442 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:41] operator / voice_transcript_partial / voice: e not
  meta: kind=partial | timestamp=1777963241.2925127 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:41] operator / voice_transcript_partial / voice: e not why
  meta: kind=partial | timestamp=1777963241.541373 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:42] operator / voice_transcript_partial / voice: e not hi set
  meta: kind=partial | timestamp=1777963242.2913816 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:42] operator / voice_transcript_partial / voice: e not hi set is not
  meta: kind=partial | timestamp=1777963242.8705752 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:43] operator / voice_transcript_final / voice: e not why say is not
  meta: kind=final | timestamp=1777963243.8676045 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:46] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777963246.0429003 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:46] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777963246.830962 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:47] operator / voice_transcript_partial / voice: not same but
  meta: kind=partial | timestamp=1777963247.3823547 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:47] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777963247.7931428 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:48] operator / voice_transcript_partial / voice: not same but faster
  meta: kind=partial | timestamp=1777963248.0431657 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:48] operator / voice_transcript_final / voice: not same board
  meta: kind=final | timestamp=1777963248.5512874 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:53] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777963253.0522306 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:53] operator / voice_transcript_partial / voice: not for
  meta: kind=partial | timestamp=1777963253.314074 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:53] operator / voice_transcript_partial / voice: not for you
  meta: kind=partial | timestamp=1777963253.5516539 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:53] operator / voice_transcript_partial / voice: not for personality
  meta: kind=partial | timestamp=1777963253.8053453 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:54] operator / voice_transcript_partial / voice: not for disable
  meta: kind=partial | timestamp=1777963254.053244 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:54] operator / voice_transcript_partial / voice: not for same but
  meta: kind=partial | timestamp=1777963254.3202915 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:40:54] operator / voice_transcript_final / voice: not for the theme
  meta: kind=final | timestamp=1777963254.8036625 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:03] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777963263.8024983 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:11] operator / voice_transcript_partial / voice: quiet
  meta: kind=partial | timestamp=1777963271.5555036 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:12] operator / voice_transcript_partial / voice: quiet same
  meta: kind=partial | timestamp=1777963272.3054447 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:12] operator / voice_transcript_partial / voice: quiet same but
  meta: kind=partial | timestamp=1777963272.5540755 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:13] operator / voice_transcript_final / voice: quiet same
  meta: kind=final | timestamp=1777963273.3109233 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:17] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777963277.1455982 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:17] operator / voice_transcript_partial / voice: not for
  meta: kind=partial | timestamp=1777963277.3946655 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:17] operator / voice_transcript_partial / voice: not for you
  meta: kind=partial | timestamp=1777963277.643883 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:17] operator / voice_transcript_partial / voice: not what is
  meta: kind=partial | timestamp=1777963277.895057 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:18] operator / voice_transcript_partial / voice: not for you
  meta: kind=partial | timestamp=1777963278.1426635 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:18] operator / voice_transcript_final / voice: not for you
  meta: kind=final | timestamp=1777963278.3939948 | source=final | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:18] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777963278.6435287 | source=vosk | frequency_hz=400.0 | rms=421 | updated_at=1777963181.9892564
- [2026-05-05 14:41:20] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 14:41:22] assistant / spoken_reply / voice: Assistant update. I could not reach the local model, but the top deterministic finding is: Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=on; pir=on. This was generated using local fallback guidance.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 14:41:42] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1777963302.6510818 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:42] operator / voice_transcript_partial / voice: assistant auto
  meta: kind=partial | timestamp=1777963302.968811 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:43] operator / voice_transcript_final / voice: assistant
  meta: kind=final | timestamp=1777963303.415336 | source=final | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:44] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777963304.1491444 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:45] operator / voice_transcript_final / voice: not to
  meta: kind=final | timestamp=1777963305.4624646 | source=final | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:45] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777963305.470048 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:45] operator / voice_transcript_partial / voice: hi talk less
  meta: kind=partial | timestamp=1777963305.8740587 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:46] operator / voice_transcript_final / voice: hi talk
  meta: kind=final | timestamp=1777963306.5850825 | source=final | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:46] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777963306.7506588 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:46] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777963306.9929357 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:47] operator / voice_transcript_final / voice: why
  meta: kind=final | timestamp=1777963307.722414 | source=final | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:47] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1777963307.9704266 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:48] operator / voice_transcript_final / voice: detection
  meta: kind=final | timestamp=1777963308.9719398 | source=final | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:49] operator / voice_transcript_partial / voice: object
  meta: kind=partial | timestamp=1777963309.469882 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:49] operator / voice_transcript_partial / voice: object detection
  meta: kind=partial | timestamp=1777963309.7222922 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:50] operator / voice_transcript_partial / voice: object
  meta: kind=partial | timestamp=1777963310.4697971 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:50] operator / voice_transcript_partial / voice: object tracking
  meta: kind=partial | timestamp=1777963310.721391 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:50] operator / voice_transcript_partial / voice: object tracking disconnect
  meta: kind=partial | timestamp=1777963310.970732 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:51] operator / voice_transcript_partial / voice: object tracking small model
  meta: kind=partial | timestamp=1777963311.2198436 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:51] operator / voice_transcript_partial / voice: object tracking small
  meta: kind=partial | timestamp=1777963311.4710276 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:51] operator / voice_transcript_partial / voice: object tracking small personality
  meta: kind=partial | timestamp=1777963311.7422316 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:51] operator / voice_transcript_partial / voice: object tracking small decrease
  meta: kind=partial | timestamp=1777963311.970033 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:52] operator / voice_transcript_partial / voice: object tracking small decrease guard
  meta: kind=partial | timestamp=1777963312.7373824 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:53] operator / voice_transcript_final / voice: object tracking small decrease guard
  meta: kind=final | timestamp=1777963313.638286 | source=final | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:53] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1777963313.699935 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:41:56] operator / voice_transcript_partial / voice: me ask
  meta: kind=partial | timestamp=1777963316.3185225 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:42:00] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777963320.1818159 | source=vosk | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
- [2026-05-05 14:42:00] operator / voice_transcript_final / voice: set
  meta: kind=final | timestamp=1777963320.809767 | source=final | frequency_hz=400.0 | rms=342 | updated_at=1777963298.6324968
