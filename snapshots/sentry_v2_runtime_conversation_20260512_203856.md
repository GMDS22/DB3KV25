# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-12 20:38:56
- Entries: 86
- Roles: {'assistant': 3, 'system': 1, 'operator': 82}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 2, 'voice_status': 1, 'voice_transcript_partial': 72, 'voice_transcript_final': 9, 'voice_command': 1}
- Channels: {'text': 3, 'voice': 83}
- Latest operator request: the adaptive loss turn on
- Latest assistant message: Assistant is disabled.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.
- Assistant text replies were generated without matching spoken assistant lines. Inspect human voice availability or auto-speak configuration.

## Timeline

- [2026-05-12 20:11:58] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-12 20:11:58] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-12 20:12:00] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778587920.2080472 | source=vosk
- [2026-05-12 20:12:03] operator / voice_transcript_partial / voice: guard is adaptive
  meta: kind=partial | timestamp=1778587923.9791195 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:04] operator / voice_transcript_partial / voice: guard is acoustic
  meta: kind=partial | timestamp=1778587924.2310472 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:04] operator / voice_transcript_partial / voice: guard is adaptive e
  meta: kind=partial | timestamp=1778587924.4808948 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:04] operator / voice_transcript_partial / voice: guard is adaptive keys
  meta: kind=partial | timestamp=1778587924.7317407 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:06] operator / voice_transcript_final / voice: guard is a do keys
  meta: kind=final | timestamp=1778587926.084594 | source=final | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:06] operator / voice_transcript_partial / voice: status of
  meta: kind=partial | timestamp=1778587926.7290397 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:06] operator / voice_transcript_partial / voice: status of e lion
  meta: kind=partial | timestamp=1778587926.9810212 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:07] operator / voice_transcript_partial / voice: status of media
  meta: kind=partial | timestamp=1778587927.2318518 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:07] operator / voice_transcript_partial / voice: status of elliot ask
  meta: kind=partial | timestamp=1778587927.7347753 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:07] operator / voice_transcript_partial / voice: status of media guard is
  meta: kind=partial | timestamp=1778587927.9804056 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:10] operator / voice_transcript_final / voice: status of media guard
  meta: kind=final | timestamp=1778587930.0901043 | source=final | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:11] operator / voice_transcript_partial / voice: natural
  meta: kind=partial | timestamp=1778587931.4804661 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:11] operator / voice_transcript_partial / voice: known accessory
  meta: kind=partial | timestamp=1778587931.7295938 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:13] operator / voice_transcript_partial / voice: known accessory you
  meta: kind=partial | timestamp=1778587933.7286375 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:16] operator / voice_transcript_final / voice: known accessory you
  meta: kind=final | timestamp=1778587936.8659878 | source=final | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:28] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1778587948.9790416 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:12:29] operator / voice_transcript_partial / voice: guarding mode
  meta: kind=partial | timestamp=1778587949.2296047 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:02] operator / voice_transcript_partial / voice: guarding mode greeting
  meta: kind=partial | timestamp=1778587982.482176 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:02] operator / voice_transcript_partial / voice: guarding mode recent
  meta: kind=partial | timestamp=1778587982.7320247 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:04] operator / voice_transcript_partial / voice: guarding mode recent logs
  meta: kind=partial | timestamp=1778587984.235921 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:04] operator / voice_transcript_partial / voice: guarding mode recent logs running
  meta: kind=partial | timestamp=1778587984.4835932 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:05] operator / voice_transcript_partial / voice: guarding mode recent logs enabled
  meta: kind=partial | timestamp=1778587985.9849124 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:07] operator / voice_transcript_final / voice: guarding mode recent logs running
  meta: kind=final | timestamp=1778587987.893646 | source=final | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:08] operator / voice_transcript_partial / voice: target matching
  meta: kind=partial | timestamp=1778587988.7359993 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:08] operator / voice_transcript_partial / voice: mode
  meta: kind=partial | timestamp=1778587988.9838336 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:10] operator / voice_transcript_partial / voice: model
  meta: kind=partial | timestamp=1778587990.7336202 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:20] operator / voice_transcript_partial / voice: runtime analysis
  meta: kind=partial | timestamp=1778588000.247146 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:20] operator / voice_transcript_partial / voice: hey leon enable
  meta: kind=partial | timestamp=1778588000.4825125 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:20] operator / voice_transcript_partial / voice: hey leon enable acoustic
  meta: kind=partial | timestamp=1778588000.7454412 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:20] operator / voice_transcript_partial / voice: hey leon enable spoken alerts
  meta: kind=partial | timestamp=1778588000.9857867 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:21] operator / voice_transcript_partial / voice: hey leon enable elian
  meta: kind=partial | timestamp=1778588001.2338834 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:22] operator / voice_transcript_partial / voice: hey leon enable elian turn on
  meta: kind=partial | timestamp=1778588002.0639281 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:22] operator / voice_transcript_partial / voice: hey leon enable elian automatic
  meta: kind=partial | timestamp=1778588002.0837898 | source=vosk | frequency_hz=118.2 | rms=809 | updated_at=1778587922.2233424
- [2026-05-12 20:13:24] operator / voice_transcript_partial / voice: hey leon enable elian enable the movement of is
  meta: kind=partial | timestamp=1778588004.019981 | source=vosk | frequency_hz=204.0 | rms=849 | updated_at=1778588003.2619736
- [2026-05-12 20:13:26] operator / voice_transcript_partial / voice: hey leon enable elian automatic prompted
  meta: kind=partial | timestamp=1778588006.7726455 | source=vosk | frequency_hz=204.0 | rms=849 | updated_at=1778588003.2619736
- [2026-05-12 20:13:27] operator / voice_transcript_partial / voice: hey leon enable elian automatic prompted auto
  meta: kind=partial | timestamp=1778588007.032387 | source=vosk | frequency_hz=204.0 | rms=849 | updated_at=1778588003.2619736
- [2026-05-12 20:13:27] operator / voice_transcript_partial / voice: hey leon enable elian enable the manual movement
  meta: kind=partial | timestamp=1778588007.2719257 | source=vosk | frequency_hz=204.0 | rms=849 | updated_at=1778588003.2619736
- [2026-05-12 20:13:27] operator / voice_transcript_partial / voice: hey leon enable elian enable the movement of is slew order
  meta: kind=partial | timestamp=1778588007.5250003 | source=vosk | frequency_hz=204.0 | rms=849 | updated_at=1778588003.2619736
- [2026-05-12 20:13:29] operator / voice_transcript_partial / voice: hey leon enable elian automatic motion the
  meta: kind=partial | timestamp=1778588009.5364506 | source=vosk | frequency_hz=204.0 | rms=849 | updated_at=1778588003.2619736
- [2026-05-12 20:13:32] operator / voice_transcript_partial / voice: hey leon enable elian automatic motion
  meta: kind=partial | timestamp=1778588012.0266273 | source=vosk | frequency_hz=204.0 | rms=849 | updated_at=1778588003.2619736
- [2026-05-12 20:13:36] operator / voice_transcript_partial / voice: hey leon enable elian automatic motion the
  meta: kind=partial | timestamp=1778588016.0274165 | source=vosk | frequency_hz=204.0 | rms=849 | updated_at=1778588003.2619736
- [2026-05-12 20:13:39] operator / voice_transcript_partial / voice: hey leon enable elian automatic motion the auto export
  meta: kind=partial | timestamp=1778588019.2750354 | source=vosk | frequency_hz=204.0 | rms=849 | updated_at=1778588003.2619736
- [2026-05-12 20:13:40] operator / voice_transcript_final / voice: elion enable enable the movement of is prompted auto motion guard is not loading
  meta: kind=final | timestamp=1778588020.2307284 | source=final | frequency_hz=204.0 | rms=849 | updated_at=1778588003.2619736
- [2026-05-12 20:13:40] operator / voice_command / voice: enable enable the movement of is prompted auto motion guard is not loading
  meta: normalized=True
- [2026-05-12 20:13:40] assistant / assistant_analysis / text: Assistant is disabled.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-12 20:13:40] operator / voice_transcript_partial / voice: what is
  meta: kind=partial | timestamp=1778588020.8865333 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:41] operator / voice_transcript_partial / voice: once per known
  meta: kind=partial | timestamp=1778588021.3875885 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:42] operator / voice_transcript_partial / voice: what is pir the
  meta: kind=partial | timestamp=1778588022.1362119 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:47] operator / voice_transcript_partial / voice: what is pir the one manual
  meta: kind=partial | timestamp=1778588027.1421714 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:47] operator / voice_transcript_partial / voice: what is pir the one on
  meta: kind=partial | timestamp=1778588027.388202 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:47] operator / voice_transcript_partial / voice: what is pir the one on no detection
  meta: kind=partial | timestamp=1778588027.6392572 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:48] operator / voice_transcript_partial / voice: what is pir the one on leon decrease
  meta: kind=partial | timestamp=1778588028.3944273 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:48] operator / voice_transcript_partial / voice: what is pir the one on recovery the
  meta: kind=partial | timestamp=1778588028.6364684 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:48] operator / voice_transcript_partial / voice: what is pir the one on recovery the camera
  meta: kind=partial | timestamp=1778588028.8871949 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:49] operator / voice_transcript_partial / voice: what is pir the one on recovery the candidates
  meta: kind=partial | timestamp=1778588029.5235498 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:49] operator / voice_transcript_partial / voice: what is pir the one on recovery the candidates that again
  meta: kind=partial | timestamp=1778588029.6374545 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:49] operator / voice_transcript_partial / voice: what is pir the one on recovery the candidates that again one
  meta: kind=partial | timestamp=1778588029.8885179 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:50] operator / voice_transcript_partial / voice: what is pir the one on recovery the candidates that again one hello
  meta: kind=partial | timestamp=1778588030.1380231 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:52] operator / voice_transcript_partial / voice: what is pir the one on recovery the candidates that again one anomaly
  meta: kind=partial | timestamp=1778588032.6417265 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:13:53] operator / voice_transcript_partial / voice: what is pir the one on recovery the candidates that again one another
  meta: kind=partial | timestamp=1778588033.64128 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:15:31] operator / voice_transcript_partial / voice: what is pir the one on recovery the candidates that again one another enabled
  meta: kind=partial | timestamp=1778588131.6383386 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:15:31] operator / voice_transcript_partial / voice: what is pir the one on recovery the candidates that again voice reports
  meta: kind=partial | timestamp=1778588131.896395 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:15:33] operator / voice_transcript_final / voice: enable what is pir the one on recovery the candidates that again one another command
  meta: kind=final | timestamp=1778588133.655156 | source=final | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:17:52] operator / voice_transcript_partial / voice: blink
  meta: kind=partial | timestamp=1778588272.8964348 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:17:55] operator / voice_transcript_partial / voice: blink of
  meta: kind=partial | timestamp=1778588275.3929625 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:17:55] operator / voice_transcript_partial / voice: blink of auto
  meta: kind=partial | timestamp=1778588275.6413968 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:17:55] operator / voice_transcript_partial / voice: blink of auto greeting
  meta: kind=partial | timestamp=1778588275.894064 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:17:56] operator / voice_transcript_partial / voice: blink of auto video
  meta: kind=partial | timestamp=1778588276.1462479 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:17:57] operator / voice_transcript_partial / voice: blink of auto video zone masks
  meta: kind=partial | timestamp=1778588277.39299 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:17:59] operator / voice_transcript_partial / voice: blink of auto video loop
  meta: kind=partial | timestamp=1778588279.141404 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:15] operator / voice_transcript_partial / voice: blink of auto video loop leon
  meta: kind=partial | timestamp=1778588295.9186616 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:16] operator / voice_transcript_partial / voice: blink of auto video loop leon deactivate
  meta: kind=partial | timestamp=1778588296.38954 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:19] operator / voice_transcript_partial / voice: blink of auto video loop leon
  meta: kind=partial | timestamp=1778588299.3113956 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:21] operator / voice_transcript_final / voice: blink of of video loop
  meta: kind=final | timestamp=1778588301.0356936 | source=final | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:22] operator / voice_transcript_partial / voice: optimisation
  meta: kind=partial | timestamp=1778588302.4131393 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:23] operator / voice_transcript_partial / voice: after greeting
  meta: kind=partial | timestamp=1778588303.6622224 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:25] operator / voice_transcript_final / voice: after greeting
  meta: kind=final | timestamp=1778588305.5412679 | source=final | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:34] operator / voice_transcript_partial / voice: output
  meta: kind=partial | timestamp=1778588314.7525778 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:42] operator / voice_transcript_partial / voice: the adaptive
  meta: kind=partial | timestamp=1778588322.4160194 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:44] operator / voice_transcript_partial / voice: the adaptive loss
  meta: kind=partial | timestamp=1778588324.1806037 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:44] operator / voice_transcript_partial / voice: enable the last on
  meta: kind=partial | timestamp=1778588324.6619904 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:48] operator / voice_transcript_partial / voice: the adaptive loss diagnostics
  meta: kind=partial | timestamp=1778588328.1621945 | source=vosk | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
- [2026-05-12 20:18:51] operator / voice_transcript_final / voice: the adaptive loss turn on
  meta: kind=final | timestamp=1778588331.064984 | source=final | frequency_hz=62.0 | rms=1201 | updated_at=1778588020.8804507
