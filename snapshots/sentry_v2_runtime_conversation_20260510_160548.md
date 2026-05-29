# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-10 16:05:48
- Entries: 59
- Roles: {'assistant': 3, 'system': 1, 'operator': 55}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 1, 'voice_transcript_partial': 45, 'voice_transcript_final': 10}
- Channels: {'text': 2, 'voice': 57}
- Latest operator request: current loop
- Latest assistant message: The smart Sentry is now online. Say the command.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-10 16:02:44] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-10 16:02:44] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-10 16:02:48] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778400168.2956083 | source=vosk
- [2026-05-10 16:03:30] assistant / spoken_confirmation / voice: The smart Sentry is now online. Say the command.
  meta: interrupt=True | assistant_output=False | spoken=False
- [2026-05-10 16:03:58] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778400238.956979 | source=vosk
- [2026-05-10 16:04:00] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1778400240.7114353 | source=vosk
- [2026-05-10 16:04:01] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1778400241.8369691 | source=final
- [2026-05-10 16:04:03] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778400243.1210616 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:04] operator / voice_transcript_partial / voice: is manual
  meta: kind=partial | timestamp=1778400244.1197925 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:05] operator / voice_transcript_final / voice: is
  meta: kind=final | timestamp=1778400245.2168286 | source=final | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:06] operator / voice_transcript_partial / voice: include logs
  meta: kind=partial | timestamp=1778400246.8709211 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:07] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1778400247.1213162 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:09] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1778400249.6251085 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:10] operator / voice_transcript_partial / voice: leon turn on
  meta: kind=partial | timestamp=1778400250.119585 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:12] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1778400252.124388 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:18] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778400258.8686476 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:19] operator / voice_transcript_final / voice: is
  meta: kind=final | timestamp=1778400259.7138236 | source=final | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:22] operator / voice_transcript_partial / voice: the status
  meta: kind=partial | timestamp=1778400262.6196175 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:32] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1778400272.1319675 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:32] operator / voice_transcript_partial / voice: the current
  meta: kind=partial | timestamp=1778400272.3852851 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:38] operator / voice_transcript_partial / voice: trigger
  meta: kind=partial | timestamp=1778400278.3843799 | source=vosk | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:44] operator / voice_transcript_final / voice: trigger
  meta: kind=final | timestamp=1778400284.4878263 | source=final | frequency_hz=110.0 | rms=902 | updated_at=1778400242.361549
- [2026-05-10 16:04:49] operator / voice_transcript_partial / voice: view
  meta: kind=partial | timestamp=1778400289.153095 | source=vosk | frequency_hz=280.0 | rms=1201 | updated_at=1778400288.6444776
- [2026-05-10 16:04:50] operator / voice_transcript_final / voice: view
  meta: kind=final | timestamp=1778400290.9497724 | source=final | frequency_hz=323.5 | rms=1201 | updated_at=1778400290.146006
- [2026-05-10 16:04:52] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778400292.225818 | source=vosk | frequency_hz=278.1 | rms=1105 | updated_at=1778400291.4657423
- [2026-05-10 16:04:54] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1778400294.5718775 | source=final | frequency_hz=278.1 | rms=1105 | updated_at=1778400291.4657423
- [2026-05-10 16:05:05] operator / voice_transcript_partial / voice: turn off
  meta: kind=partial | timestamp=1778400305.223191 | source=vosk | frequency_hz=366.0 | rms=2196 | updated_at=1778400302.7165222
- [2026-05-10 16:05:05] operator / voice_transcript_partial / voice: feed
  meta: kind=partial | timestamp=1778400305.4786673 | source=vosk | frequency_hz=366.0 | rms=2196 | updated_at=1778400302.7165222
- [2026-05-10 16:05:05] operator / voice_transcript_partial / voice: view status
  meta: kind=partial | timestamp=1778400305.9776437 | source=vosk | frequency_hz=366.0 | rms=2196 | updated_at=1778400302.7165222
- [2026-05-10 16:05:06] operator / voice_transcript_partial / voice: of slew order
  meta: kind=partial | timestamp=1778400306.473094 | source=vosk | frequency_hz=366.0 | rms=2196 | updated_at=1778400302.7165222
- [2026-05-10 16:05:20] operator / voice_transcript_partial / voice: of slew
  meta: kind=partial | timestamp=1778400320.7257292 | source=vosk | frequency_hz=366.0 | rms=2196 | updated_at=1778400302.7165222
- [2026-05-10 16:05:21] operator / voice_transcript_final / voice: of slew
  meta: kind=final | timestamp=1778400321.0622244 | source=final | frequency_hz=366.0 | rms=2196 | updated_at=1778400302.7165222
- [2026-05-10 16:05:21] operator / voice_transcript_partial / voice: accessory
  meta: kind=partial | timestamp=1778400321.2277825 | source=vosk | frequency_hz=366.0 | rms=2196 | updated_at=1778400302.7165222
- [2026-05-10 16:05:23] operator / voice_transcript_final / voice: accessory
  meta: kind=final | timestamp=1778400323.0627515 | source=final | frequency_hz=366.0 | rms=2196 | updated_at=1778400302.7165222
- [2026-05-10 16:05:23] operator / voice_transcript_partial / voice: movement
  meta: kind=partial | timestamp=1778400323.4718633 | source=vosk | frequency_hz=366.0 | rms=2196 | updated_at=1778400302.7165222
- [2026-05-10 16:05:23] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1778400323.7224512 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:24] operator / voice_transcript_partial / voice: slew the machine
  meta: kind=partial | timestamp=1778400324.222346 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:24] operator / voice_transcript_partial / voice: e model
  meta: kind=partial | timestamp=1778400324.4720535 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:27] operator / voice_transcript_partial / voice: e mode
  meta: kind=partial | timestamp=1778400327.7362602 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:27] operator / voice_transcript_partial / voice: e mode is
  meta: kind=partial | timestamp=1778400327.9751751 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:28] operator / voice_transcript_partial / voice: e mode is known
  meta: kind=partial | timestamp=1778400328.2242491 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:28] operator / voice_transcript_partial / voice: e mode is not the
  meta: kind=partial | timestamp=1778400328.473159 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:29] operator / voice_transcript_partial / voice: e mode is not the no
  meta: kind=partial | timestamp=1778400329.222341 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:29] operator / voice_transcript_partial / voice: e mode is not the natural
  meta: kind=partial | timestamp=1778400329.4819422 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:33] operator / voice_transcript_partial / voice: e mode is not the
  meta: kind=partial | timestamp=1778400333.9788673 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:34] operator / voice_transcript_partial / voice: e mode is not the continuous
  meta: kind=partial | timestamp=1778400334.2224085 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:34] operator / voice_transcript_partial / voice: e mode is not the no
  meta: kind=partial | timestamp=1778400334.4732604 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:34] operator / voice_transcript_partial / voice: e mode is not the no detection
  meta: kind=partial | timestamp=1778400334.7249746 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:35] operator / voice_transcript_partial / voice: e mode is not the no the tuning
  meta: kind=partial | timestamp=1778400335.2222476 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:35] operator / voice_transcript_partial / voice: e mode is not the no the to
  meta: kind=partial | timestamp=1778400335.7224162 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:36] operator / voice_transcript_partial / voice: e mode is not the no the to movement
  meta: kind=partial | timestamp=1778400336.227003 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:37] operator / voice_transcript_final / voice: slew id e mode is not the no the to
  meta: kind=final | timestamp=1778400337.6230285 | source=final | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:37] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778400337.9840446 | source=vosk | frequency_hz=364.0 | rms=1837 | updated_at=1778400323.7162158
- [2026-05-10 16:05:38] operator / voice_transcript_partial / voice: keyboard movement
  meta: kind=partial | timestamp=1778400338.2225323 | source=vosk | frequency_hz=346.0 | rms=5610 | updated_at=1778400338.2170196
- [2026-05-10 16:05:38] operator / voice_transcript_partial / voice: current leon
  meta: kind=partial | timestamp=1778400338.4761481 | source=vosk | frequency_hz=348.1 | rms=3956 | updated_at=1778400338.4669318
- [2026-05-10 16:05:40] operator / voice_transcript_partial / voice: keyboard movement
  meta: kind=partial | timestamp=1778400340.9751954 | source=vosk | frequency_hz=348.1 | rms=3956 | updated_at=1778400338.4669318
- [2026-05-10 16:05:41] operator / voice_transcript_partial / voice: current leon
  meta: kind=partial | timestamp=1778400341.2233386 | source=vosk | frequency_hz=418.0 | rms=5320 | updated_at=1778400341.2169747
- [2026-05-10 16:05:41] operator / voice_transcript_final / voice: current loop
  meta: kind=final | timestamp=1778400341.5732527 | source=final | frequency_hz=418.0 | rms=5320 | updated_at=1778400341.2169747
- [2026-05-10 16:05:41] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778400341.7240162 | source=vosk | frequency_hz=418.0 | rms=5320 | updated_at=1778400341.2169747
