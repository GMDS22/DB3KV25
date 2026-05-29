# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-09 18:19:42
- Entries: 16
- Roles: {'assistant': 2, 'system': 1, 'operator': 13}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_partial': 12, 'voice_transcript_final': 1}
- Channels: {'text': 2, 'voice': 14}
- Latest operator request: motion on human recovery off
- Latest assistant message: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.
- Assistant text replies were generated without matching spoken assistant lines. Inspect human voice availability or auto-speak configuration.

## Timeline

- [2026-05-09 18:16:01] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-09 18:16:01] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-09 18:16:02] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778321762.7118664 | source=vosk
- [2026-05-09 18:16:17] operator / voice_transcript_partial / voice: human
  meta: kind=partial | timestamp=1778321777.8240168 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:22] operator / voice_transcript_partial / voice: human alion
  meta: kind=partial | timestamp=1778321782.8256876 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:29] operator / voice_transcript_partial / voice: human alion the for
  meta: kind=partial | timestamp=1778321789.073785 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:29] operator / voice_transcript_partial / voice: human alion default
  meta: kind=partial | timestamp=1778321789.5562792 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:35] operator / voice_transcript_partial / voice: motion
  meta: kind=partial | timestamp=1778321795.6937888 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:35] operator / voice_transcript_partial / voice: loss enabled
  meta: kind=partial | timestamp=1778321795.9422197 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:36] operator / voice_transcript_partial / voice: motion on pir
  meta: kind=partial | timestamp=1778321796.193739 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:36] operator / voice_transcript_partial / voice: motion on loss
  meta: kind=partial | timestamp=1778321796.4460874 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:36] operator / voice_transcript_partial / voice: motion on movement keys
  meta: kind=partial | timestamp=1778321796.6950247 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:38] operator / voice_transcript_partial / voice: motion on loss recovery
  meta: kind=partial | timestamp=1778321798.9453025 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:53] operator / voice_transcript_partial / voice: motion on loss recovery on
  meta: kind=partial | timestamp=1778321813.7026386 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:53] operator / voice_transcript_partial / voice: motion on loss recovery off
  meta: kind=partial | timestamp=1778321813.9430852 | source=vosk | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
- [2026-05-09 18:16:55] operator / voice_transcript_final / voice: motion on human recovery off
  meta: kind=final | timestamp=1778321815.824224 | source=final | frequency_hz=372.0 | rms=312 | updated_at=1778321770.3167639
