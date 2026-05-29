# SMART SENTRY V3.5.3 Runtime Conversation Export

- Generated: 2026-05-05 00:11:15
- Entries: 1104
- Roles: {'assistant': 127, 'system': 1, 'operator': 976}
- Event types: {'assistant_prompt': 41, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 84, 'voice_transcript_partial': 728, 'voice_transcript_final': 140, 'voice_command': 108, 'spoken_reply': 1}
- Channels: {'text': 42, 'voice': 1062}
- Latest operator request: sentry the com
- Latest assistant message: I am still finishing assistant request about commands repeat. I queued your assistant request about threshold the mode delay. It is number 27 in line.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-04 23:59:42] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:59:42] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-04 23:59:43] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777910383.9590528 | source=vosk
- [2026-05-04 23:59:45] assistant / spoken_confirmation / voice: System online and listening. Do you want me to connect boards, enable sentry, or run another task?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:59:49] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777910389.7650826 | source=vosk | frequency_hz=261.9 | rms=248 | updated_at=1777910387.2587316
- [2026-05-04 23:59:50] operator / voice_transcript_partial / voice: stop on lion
  meta: kind=partial | timestamp=1777910390.0141947 | source=vosk | frequency_hz=261.9 | rms=248 | updated_at=1777910387.2587316
- [2026-05-04 23:59:50] operator / voice_transcript_partial / voice: stop on lion analyze
  meta: kind=partial | timestamp=1777910390.2649114 | source=vosk | frequency_hz=261.9 | rms=248 | updated_at=1777910387.2587316
- [2026-05-04 23:59:50] operator / voice_transcript_partial / voice: stop on lion and less
  meta: kind=partial | timestamp=1777910390.5143197 | source=vosk | frequency_hz=261.9 | rms=248 | updated_at=1777910387.2587316
- [2026-05-04 23:59:50] operator / voice_transcript_partial / voice: stop on lion and less enable
  meta: kind=partial | timestamp=1777910390.765302 | source=vosk | frequency_hz=261.9 | rms=248 | updated_at=1777910387.2587316
- [2026-05-04 23:59:51] operator / voice_transcript_partial / voice: stop on lion and less
  meta: kind=partial | timestamp=1777910391.017294 | source=vosk | frequency_hz=260.0 | rms=255 | updated_at=1777910391.0082781
- [2026-05-04 23:59:51] operator / voice_transcript_final / voice: stop on lion and less
  meta: kind=final | timestamp=1777910391.2674944 | source=final | frequency_hz=260.0 | rms=255 | updated_at=1777910391.0082781
- [2026-05-04 23:59:51] operator / voice_command / voice: stop on lion and less
  meta: normalized=True
- [2026-05-04 23:59:51] operator / voice_transcript_partial / voice: do you
  meta: kind=partial | timestamp=1777910391.5149198 | source=vosk | frequency_hz=260.0 | rms=255 | updated_at=1777910391.0082781
- [2026-05-04 23:59:51] operator / voice_transcript_partial / voice: do you what
  meta: kind=partial | timestamp=1777910391.7642307 | source=vosk | frequency_hz=260.0 | rms=255 | updated_at=1777910391.0082781
- [2026-05-04 23:59:52] operator / voice_transcript_partial / voice: do you what be to
  meta: kind=partial | timestamp=1777910392.0157995 | source=vosk | frequency_hz=260.0 | rms=255 | updated_at=1777910391.0082781
- [2026-05-04 23:59:52] operator / voice_transcript_partial / voice: do you what be to connect
  meta: kind=partial | timestamp=1777910392.2648249 | source=vosk | frequency_hz=260.0 | rms=255 | updated_at=1777910391.0082781
- [2026-05-04 23:59:52] operator / voice_transcript_partial / voice: do you what be to connect boards
  meta: kind=partial | timestamp=1777910392.7649267 | source=vosk | frequency_hz=260.0 | rms=255 | updated_at=1777910391.0082781
- [2026-05-04 23:59:53] operator / voice_transcript_partial / voice: do you what be to connect boards enable
  meta: kind=partial | timestamp=1777910393.0138805 | source=vosk | frequency_hz=260.0 | rms=255 | updated_at=1777910391.0082781
- [2026-05-04 23:59:53] operator / voice_transcript_partial / voice: do you what be to connect boards enable sentry
  meta: kind=partial | timestamp=1777910393.7651763 | source=vosk | frequency_hz=260.0 | rms=255 | updated_at=1777910391.0082781
- [2026-05-04 23:59:54] operator / voice_transcript_partial / voice: do you what be to connect boards enable sentry all run
  meta: kind=partial | timestamp=1777910394.2658415 | source=vosk | frequency_hz=260.0 | rms=255 | updated_at=1777910391.0082781
- [2026-05-04 23:59:54] operator / voice_transcript_partial / voice: do you what be to connect boards enable sentry all run analyze
  meta: kind=partial | timestamp=1777910394.5164561 | source=vosk | frequency_hz=260.0 | rms=255 | updated_at=1777910391.0082781
- [2026-05-04 23:59:55] operator / voice_transcript_partial / voice: do you what be to connect boards enable sentry all run analyze task
  meta: kind=partial | timestamp=1777910395.0131018 | source=vosk | frequency_hz=248.0 | rms=245 | updated_at=1777910395.008566
- [2026-05-04 23:59:55] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777910395.5160997 | source=final | frequency_hz=257.8 | rms=262 | updated_at=1777910395.2598157
- [2026-05-04 23:59:55] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-04 23:59:55] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777910395.7902894 | source=vosk | frequency_hz=257.8 | rms=262 | updated_at=1777910395.2598157
- [2026-05-04 23:59:56] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777910396.1281567 | source=vosk | frequency_hz=257.8 | rms=262 | updated_at=1777910395.2598157
- [2026-05-04 23:59:57] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1777910397.422233 | source=final | frequency_hz=255.2 | rms=262 | updated_at=1777910397.1190085
- [2026-05-05 00:00:21] operator / voice_command / voice: yes
  meta: normalized=True
- [2026-05-04 23:59:59] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777910399.372408 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-04 23:59:59] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777910399.6237786 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:00] operator / voice_transcript_partial / voice: smart sentry boards
  meta: kind=partial | timestamp=1777910400.125234 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:00] operator / voice_transcript_partial / voice: smart sentry boards connect it again
  meta: kind=partial | timestamp=1777910400.6275012 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:00] operator / voice_transcript_partial / voice: smart sentry boards connect it on the smart
  meta: kind=partial | timestamp=1777910400.875114 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:01] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme
  meta: kind=partial | timestamp=1777910401.124046 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:01] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme override
  meta: kind=partial | timestamp=1777910401.3732252 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:01] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme analyze
  meta: kind=partial | timestamp=1777910401.6239605 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:01] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything else
  meta: kind=partial | timestamp=1777910401.8756874 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:02] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what
  meta: kind=partial | timestamp=1777910402.3782613 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:02] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what do never
  meta: kind=partial | timestamp=1777910402.8737397 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:03] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect
  meta: kind=partial | timestamp=1777910403.123245 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:03] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you
  meta: kind=partial | timestamp=1777910403.6254656 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:03] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you confirm
  meta: kind=partial | timestamp=1777910403.8748484 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:04] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say it
  meta: kind=partial | timestamp=1777910404.1246252 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:04] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say enable
  meta: kind=partial | timestamp=1777910404.3745754 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:04] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say enable smart
  meta: kind=partial | timestamp=1777910404.624268 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:05] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say enable smart sentry
  meta: kind=partial | timestamp=1777910405.123837 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:05] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say enable smart sentry boards
  meta: kind=partial | timestamp=1777910405.6252232 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:05] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say enable smart sentry board home
  meta: kind=partial | timestamp=1777910405.8739414 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:06] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say enable smart sentry board alien
  meta: kind=partial | timestamp=1777910406.125988 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:06] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say enable smart sentry board alien task
  meta: kind=partial | timestamp=1777910406.6278846 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:07] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say enable smart sentry board alien task repeat
  meta: kind=partial | timestamp=1777910407.1263638 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:07] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say enable smart sentry board alien task repeat check
  meta: kind=partial | timestamp=1777910407.3746715 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:07] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say enable smart sentry board alien task e lion
  meta: kind=partial | timestamp=1777910407.6257694 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:21] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:00:08] operator / voice_transcript_partial / voice: smart sentry boards connect it on the theme to anything what it connect you queued say enable smart sentry board alien task repeat stop no
  meta: kind=partial | timestamp=1777910408.3882816 | source=vosk | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:09] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1777910409.5478964 | source=final | frequency_hz=244.6 | rms=262 | updated_at=1777910398.6189466
- [2026-05-05 00:00:21] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-05 00:00:11] operator / voice_transcript_partial / voice: boards
  meta: kind=partial | timestamp=1777910411.0658488 | source=vosk | frequency_hz=140.0 | rms=831 | updated_at=1777910409.5489402
- [2026-05-05 00:00:11] operator / voice_transcript_final / voice: boards
  meta: kind=final | timestamp=1777910411.5666065 | source=final | frequency_hz=140.0 | rms=831 | updated_at=1777910409.5489402
- [2026-05-05 00:00:21] operator / voice_command / voice: boards
  meta: normalized=True
- [2026-05-05 00:00:15] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777910415.3151836 | source=vosk | frequency_hz=360.0 | rms=234 | updated_at=1777910414.3087294
- [2026-05-05 00:00:15] operator / voice_transcript_partial / voice: do it and
  meta: kind=partial | timestamp=1777910415.5686746 | source=vosk | frequency_hz=360.0 | rms=234 | updated_at=1777910414.3087294
- [2026-05-05 00:00:15] operator / voice_transcript_partial / voice: do resume
  meta: kind=partial | timestamp=1777910415.8155239 | source=vosk | frequency_hz=360.0 | rms=234 | updated_at=1777910414.3087294
- [2026-05-05 00:00:16] operator / voice_transcript_partial / voice: do resume strict
  meta: kind=partial | timestamp=1777910416.3161054 | source=vosk | frequency_hz=360.0 | rms=234 | updated_at=1777910414.3087294
- [2026-05-05 00:00:16] operator / voice_transcript_partial / voice: do it and enable
  meta: kind=partial | timestamp=1777910416.5673473 | source=vosk | frequency_hz=360.0 | rms=234 | updated_at=1777910414.3087294
- [2026-05-05 00:00:16] operator / voice_transcript_final / voice: you do sentry
  meta: kind=final | timestamp=1777910416.8187206 | source=final | frequency_hz=360.0 | rms=234 | updated_at=1777910414.3087294
- [2026-05-05 00:00:21] operator / voice_command / voice: you do sentry
  meta: normalized=True
- [2026-05-05 00:00:19] operator / voice_transcript_partial / voice: but
  meta: kind=partial | timestamp=1777910419.5647416 | source=vosk | frequency_hz=328.0 | rms=252 | updated_at=1777910418.5600626
- [2026-05-05 00:00:20] operator / voice_transcript_partial / voice: to com
  meta: kind=partial | timestamp=1777910420.3166327 | source=vosk | frequency_hz=304.0 | rms=234 | updated_at=1777910420.3101132
- [2026-05-05 00:00:20] operator / voice_transcript_partial / voice: stop
  meta: kind=partial | timestamp=1777910420.5674398 | source=vosk | frequency_hz=322.2 | rms=237 | updated_at=1777910420.5598285
- [2026-05-05 00:00:21] operator / voice_transcript_final / voice: but faster
  meta: kind=final | timestamp=1777910421.316857 | source=final | frequency_hz=322.2 | rms=237 | updated_at=1777910420.5598285
- [2026-05-05 00:00:22] operator / voice_command / voice: but faster
  meta: normalized=True
- [2026-05-05 00:00:22] assistant / assistant_prompt / text: Assistant request queued: assistant request about but faster (position 1).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:00:22] operator / voice_transcript_partial / voice: less
  meta: kind=partial | timestamp=1777910422.3175337 | source=vosk | frequency_hz=322.2 | rms=237 | updated_at=1777910420.5598285
- [2026-05-05 00:00:22] operator / voice_transcript_partial / voice: less enable
  meta: kind=partial | timestamp=1777910422.5685484 | source=vosk | frequency_hz=322.2 | rms=237 | updated_at=1777910420.5598285
- [2026-05-05 00:00:22] operator / voice_transcript_partial / voice: less strict
  meta: kind=partial | timestamp=1777910422.817266 | source=vosk | frequency_hz=322.2 | rms=237 | updated_at=1777910420.5598285
- [2026-05-05 00:00:23] operator / voice_transcript_partial / voice: resume status
  meta: kind=partial | timestamp=1777910423.0820467 | source=vosk | frequency_hz=322.2 | rms=237 | updated_at=1777910420.5598285
- [2026-05-05 00:00:23] operator / voice_transcript_partial / voice: resume status connect
  meta: kind=partial | timestamp=1777910423.3275087 | source=vosk | frequency_hz=322.2 | rms=237 | updated_at=1777910420.5598285
- [2026-05-05 00:00:24] operator / voice_transcript_final / voice: resume status connect
  meta: kind=final | timestamp=1777910424.3191688 | source=final | frequency_hz=368.0 | rms=233 | updated_at=1777910423.5609984
- [2026-05-05 00:00:24] operator / voice_command / voice: resume status connect
  meta: normalized=True
- [2026-05-05 00:00:25] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:00:25] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:00:25] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:00:25] assistant / spoken_confirmation / voice: Received. I started your assistant request about you do sentry in the background.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:00:25] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:00:25] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:00:25] assistant / spoken_confirmation / voice: I am still finishing assistant request about you do sentry. I queued your assistant request about but faster. It is number 1 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:00:25] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:00:26] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777910426.0912094 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:26] operator / voice_transcript_partial / voice: standby go
  meta: kind=partial | timestamp=1777910426.3413558 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:26] operator / voice_transcript_partial / voice: standby guarding
  meta: kind=partial | timestamp=1777910426.574326 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:26] operator / voice_transcript_partial / voice: standby guarding mode
  meta: kind=partial | timestamp=1777910426.8404093 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:27] operator / voice_transcript_partial / voice: standby go it no
  meta: kind=partial | timestamp=1777910427.0676298 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:27] operator / voice_transcript_partial / voice: standby go it no app to
  meta: kind=partial | timestamp=1777910427.321878 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:27] operator / voice_transcript_partial / voice: standby go it no app to talk
  meta: kind=partial | timestamp=1777910427.572741 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:27] operator / voice_transcript_partial / voice: standby go it no app to talk it
  meta: kind=partial | timestamp=1777910427.8173563 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:28] operator / voice_transcript_final / voice: standby go it no unk
  meta: kind=final | timestamp=1777910428.0862696 | source=final | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:28] operator / voice_command / voice: standby go it no unk
  meta: normalized=True
- [2026-05-05 00:00:28] operator / voice_transcript_partial / voice: never
  meta: kind=partial | timestamp=1777910428.3190107 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:28] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777910428.5666935 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:29] operator / voice_transcript_partial / voice: no clear the smart
  meta: kind=partial | timestamp=1777910429.073629 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:29] operator / voice_transcript_partial / voice: no clear the smart sentry
  meta: kind=partial | timestamp=1777910429.321621 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:30] operator / voice_transcript_partial / voice: no clear the smart sentry enable
  meta: kind=partial | timestamp=1777910430.0884519 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:30] operator / voice_transcript_partial / voice: no clear the smart sentry enable last
  meta: kind=partial | timestamp=1777910430.8250504 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:31] operator / voice_transcript_partial / voice: no clear the smart sentry enable never
  meta: kind=partial | timestamp=1777910431.088077 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:31] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable
  meta: kind=partial | timestamp=1777910431.3479943 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:31] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the
  meta: kind=partial | timestamp=1777910431.5669599 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:31] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable it
  meta: kind=partial | timestamp=1777910431.8402374 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:32] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the a
  meta: kind=partial | timestamp=1777910432.0703588 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:32] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the a brightness
  meta: kind=partial | timestamp=1777910432.3178248 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:32] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify
  meta: kind=partial | timestamp=1777910432.5750039 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:32] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify yourself
  meta: kind=partial | timestamp=1777910432.8178787 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:33] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify
  meta: kind=partial | timestamp=1777910433.067624 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:33] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify say it
  meta: kind=partial | timestamp=1777910433.3233619 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:33] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify say
  meta: kind=partial | timestamp=1777910433.577499 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:33] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify say go
  meta: kind=partial | timestamp=1777910433.81915 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:34] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify say guarding
  meta: kind=partial | timestamp=1777910434.0704277 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:34] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify say guarding mode
  meta: kind=partial | timestamp=1777910434.3331904 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:34] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify say go ahead no
  meta: kind=partial | timestamp=1777910434.5744767 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:34] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify say go ahead no app to
  meta: kind=partial | timestamp=1777910434.8241427 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:35] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify say go ahead no app to talk
  meta: kind=partial | timestamp=1777910435.0778258 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:35] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify say go ahead no app to talk less
  meta: kind=partial | timestamp=1777910435.5707555 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:35] operator / voice_transcript_partial / voice: no clear the smart sentry enable never disable the app identify say go ahead no app to talk enable
  meta: kind=partial | timestamp=1777910435.8269732 | source=vosk | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:36] operator / voice_transcript_final / voice: no clear the smart sentry enable never disable the app identify say go override no app to talk enable
  meta: kind=final | timestamp=1777910436.8233867 | source=final | frequency_hz=350.8 | rms=242 | updated_at=1777910425.3152874
- [2026-05-05 00:00:36] operator / voice_command / voice: no clear the smart sentry enable never disable the app identify say go override no app to talk enable
  meta: normalized=True
- [2026-05-05 00:00:37] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:00:37] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:00:40] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777910440.3890543 | source=vosk | frequency_hz=355.3 | rms=239 | updated_at=1777910439.8105958
- [2026-05-05 00:00:40] operator / voice_transcript_partial / voice: do be to anything
  meta: kind=partial | timestamp=1777910440.62283 | source=vosk | frequency_hz=355.3 | rms=239 | updated_at=1777910439.8105958
- [2026-05-05 00:00:41] operator / voice_transcript_partial / voice: do be to anything else
  meta: kind=partial | timestamp=1777910441.0817316 | source=vosk | frequency_hz=377.4 | rms=235 | updated_at=1777910441.0752258
- [2026-05-05 00:00:41] operator / voice_transcript_final / voice: do be to anything
  meta: kind=final | timestamp=1777910441.8777974 | source=final | frequency_hz=377.4 | rms=235 | updated_at=1777910441.0752258
- [2026-05-05 00:00:41] operator / voice_command / voice: do be to anything
  meta: normalized=True
- [2026-05-05 00:00:42] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:00:43] operator / voice_transcript_partial / voice: ahead the report
  meta: kind=partial | timestamp=1777910443.8545046 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:44] operator / voice_transcript_partial / voice: ahead the resume last
  meta: kind=partial | timestamp=1777910444.0863194 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:44] operator / voice_transcript_partial / voice: ahead the resume last but override
  meta: kind=partial | timestamp=1777910444.8281636 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:45] operator / voice_transcript_partial / voice: ahead the resume last on e
  meta: kind=partial | timestamp=1777910445.1285417 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:45] operator / voice_transcript_partial / voice: ahead the resume last on e the
  meta: kind=partial | timestamp=1777910445.3267546 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:45] operator / voice_transcript_partial / voice: ahead the resume last on e the rest
  meta: kind=partial | timestamp=1777910445.5831623 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:45] operator / voice_transcript_partial / voice: ahead the resume last on e the rest it again
  meta: kind=partial | timestamp=1777910445.827744 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:46] operator / voice_transcript_partial / voice: ahead the resume last on e the rest it all brightness
  meta: kind=partial | timestamp=1777910446.081755 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:46] operator / voice_transcript_partial / voice: ahead the resume last on e the rest it override connect
  meta: kind=partial | timestamp=1777910446.3361652 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:46] operator / voice_transcript_partial / voice: ahead the resume last on e the rest it app are
  meta: kind=partial | timestamp=1777910446.5849578 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:46] operator / voice_transcript_partial / voice: ahead the resume last on e the rest it app are are you do
  meta: kind=partial | timestamp=1777910446.8492293 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:47] operator / voice_transcript_partial / voice: ahead the resume last on e the rest it app are are you and override
  meta: kind=partial | timestamp=1777910447.0940342 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:47] operator / voice_transcript_partial / voice: ahead the resume last on e the rest it app are are you and override the
  meta: kind=partial | timestamp=1777910447.32648 | source=vosk | frequency_hz=342.9 | rms=245 | updated_at=1777910442.821145
- [2026-05-05 00:00:48] operator / voice_transcript_final / voice: ahead the resume last but on e the rest it app are are you and override sentry
  meta: kind=final | timestamp=1777910448.3875363 | source=final | frequency_hz=407.6 | rms=237 | updated_at=1777910448.3201716
- [2026-05-05 00:00:48] operator / voice_command / voice: ahead the resume last but on e the rest it app are are you and override sentry
  meta: normalized=True
- [2026-05-05 00:00:49] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:00:49] operator / voice_transcript_partial / voice: eileen override
  meta: kind=partial | timestamp=1777910449.6238878 | source=vosk | frequency_hz=384.6 | rms=236 | updated_at=1777910448.8204718
- [2026-05-05 00:00:49] operator / voice_transcript_partial / voice: enable elian
  meta: kind=partial | timestamp=1777910449.8327947 | source=vosk | frequency_hz=384.6 | rms=236 | updated_at=1777910448.8204718
- [2026-05-05 00:00:50] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:00:50] operator / voice_transcript_partial / voice: eileen abort current
  meta: kind=partial | timestamp=1777910450.8286948 | source=vosk | frequency_hz=384.6 | rms=236 | updated_at=1777910448.8204718
- [2026-05-05 00:00:50] operator / voice_transcript_partial / voice: eileen abort current the
  meta: kind=partial | timestamp=1777910450.848572 | source=vosk | frequency_hz=384.6 | rms=236 | updated_at=1777910448.8204718
- [2026-05-05 00:00:51] operator / voice_transcript_partial / voice: eileen abort current the boards
  meta: kind=partial | timestamp=1777910451.044381 | source=vosk | frequency_hz=82.0 | rms=399 | updated_at=1777910451.0254774
- [2026-05-05 00:00:51] operator / voice_transcript_partial / voice: eileen abort current the boards are you
  meta: kind=partial | timestamp=1777910451.9611366 | source=vosk | frequency_hz=82.0 | rms=399 | updated_at=1777910451.0254774
- [2026-05-05 00:00:52] operator / voice_transcript_final / voice: abort current the boards
  meta: kind=final | timestamp=1777910452.0085604 | source=final | frequency_hz=135.2 | rms=1143 | updated_at=1777910451.9717052
- [2026-05-05 00:00:52] operator / voice_command / voice: abort current the boards
  meta: normalized=True
- [2026-05-05 00:00:53] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:00:54] operator / voice_transcript_partial / voice: e the
  meta: kind=partial | timestamp=1777910454.499867 | source=vosk | frequency_hz=128.5 | rms=1183 | updated_at=1777910452.4731827
- [2026-05-05 00:00:54] operator / voice_transcript_partial / voice: e the resume
  meta: kind=partial | timestamp=1777910454.7290895 | source=vosk | frequency_hz=128.5 | rms=1183 | updated_at=1777910452.4731827
- [2026-05-05 00:00:55] operator / voice_transcript_final / voice: e the unk
  meta: kind=final | timestamp=1777910455.4848955 | source=final | frequency_hz=128.5 | rms=1183 | updated_at=1777910452.4731827
- [2026-05-05 00:00:55] operator / voice_command / voice: e the unk
  meta: normalized=True
- [2026-05-05 00:00:55] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777910455.755423 | source=vosk | frequency_hz=128.5 | rms=1183 | updated_at=1777910452.4731827
- [2026-05-05 00:00:56] operator / voice_transcript_partial / voice: change the
  meta: kind=partial | timestamp=1777910456.042399 | source=vosk | frequency_hz=128.5 | rms=1183 | updated_at=1777910452.4731827
- [2026-05-05 00:00:56] operator / voice_transcript_partial / voice: change smart
  meta: kind=partial | timestamp=1777910456.3024733 | source=vosk | frequency_hz=128.5 | rms=1183 | updated_at=1777910452.4731827
- [2026-05-05 00:00:56] operator / voice_transcript_partial / voice: change smart sentry
  meta: kind=partial | timestamp=1777910456.5618055 | source=vosk | frequency_hz=128.5 | rms=1183 | updated_at=1777910452.4731827
- [2026-05-05 00:00:57] operator / voice_transcript_partial / voice: change smart sentry sentry
  meta: kind=partial | timestamp=1777910457.0620105 | source=vosk | frequency_hz=128.5 | rms=1183 | updated_at=1777910452.4731827
- [2026-05-05 00:00:57] operator / voice_transcript_final / voice: change smart sentry sentry
  meta: kind=final | timestamp=1777910457.7514193 | source=final | frequency_hz=295.0 | rms=291 | updated_at=1777910457.7224011
- [2026-05-05 00:00:57] operator / voice_command / voice: change smart sentry sentry
  meta: normalized=True
- [2026-05-05 00:00:57] assistant / assistant_prompt / text: Assistant request queued: assistant request about change smart sentry sentry (position 2).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:00:58] assistant / spoken_confirmation / voice: I am still finishing assistant request about e the unk. I queued your assistant request about change smart sentry sentry. It is number 2 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:00:58] assistant / spoken_confirmation / voice: Received. I started your assistant request about e the unk in the background.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:00:59] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777910459.8194792 | source=vosk | frequency_hz=284.9 | rms=279 | updated_at=1777910458.9739065
- [2026-05-05 00:01:00] operator / voice_transcript_partial / voice: tracking pause
  meta: kind=partial | timestamp=1777910460.5438662 | source=vosk | frequency_hz=284.9 | rms=279 | updated_at=1777910458.9739065
- [2026-05-05 00:01:00] operator / voice_transcript_partial / voice: tracking pause smart
  meta: kind=partial | timestamp=1777910460.82807 | source=vosk | frequency_hz=284.9 | rms=279 | updated_at=1777910458.9739065
- [2026-05-05 00:01:01] operator / voice_transcript_partial / voice: tracking last task
  meta: kind=partial | timestamp=1777910461.091556 | source=vosk | frequency_hz=284.9 | rms=279 | updated_at=1777910458.9739065
- [2026-05-05 00:01:01] operator / voice_transcript_partial / voice: tracking pause current
  meta: kind=partial | timestamp=1777910461.270915 | source=vosk | frequency_hz=284.9 | rms=279 | updated_at=1777910458.9739065
- [2026-05-05 00:01:01] operator / voice_transcript_partial / voice: tracking pause current home
  meta: kind=partial | timestamp=1777910461.542401 | source=vosk | frequency_hz=284.9 | rms=279 | updated_at=1777910458.9739065
- [2026-05-05 00:01:01] operator / voice_transcript_partial / voice: tracking pause current queued in guarding
  meta: kind=partial | timestamp=1777910461.8153183 | source=vosk | frequency_hz=284.9 | rms=279 | updated_at=1777910458.9739065
- [2026-05-05 00:01:02] operator / voice_transcript_partial / voice: tracking pause current queued in go home
  meta: kind=partial | timestamp=1777910462.3718922 | source=vosk | frequency_hz=284.9 | rms=279 | updated_at=1777910458.9739065
- [2026-05-05 00:01:02] operator / voice_transcript_final / voice: go home
  meta: kind=final | timestamp=1777910462.814187 | source=final | frequency_hz=284.0 | rms=293 | updated_at=1777910462.7649987
- [2026-05-05 00:01:02] operator / voice_command / voice: go home
  meta: normalized=True
- [2026-05-05 00:01:03] assistant / spoken_confirmation / voice: Going to guard home position now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:01:06] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777910466.1695738 | source=vosk | frequency_hz=283.5 | rms=292 | updated_at=1777910465.0271323
- [2026-05-05 00:01:06] operator / voice_transcript_partial / voice: lion stop
  meta: kind=partial | timestamp=1777910466.3154967 | source=vosk | frequency_hz=283.5 | rms=292 | updated_at=1777910465.0271323
- [2026-05-05 00:01:06] operator / voice_transcript_partial / voice: lion stop increase
  meta: kind=partial | timestamp=1777910466.592146 | source=vosk | frequency_hz=283.5 | rms=292 | updated_at=1777910465.0271323
- [2026-05-05 00:01:06] operator / voice_transcript_partial / voice: lion stop in
  meta: kind=partial | timestamp=1777910466.8251963 | source=vosk | frequency_hz=283.5 | rms=292 | updated_at=1777910465.0271323
- [2026-05-05 00:01:07] operator / voice_transcript_final / voice: stop that
  meta: kind=final | timestamp=1777910467.119585 | source=final | frequency_hz=283.5 | rms=292 | updated_at=1777910465.0271323
- [2026-05-05 00:01:07] operator / voice_command / voice: stop that
  meta: normalized=True
- [2026-05-05 00:01:07] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777910467.335419 | source=vosk | frequency_hz=283.5 | rms=292 | updated_at=1777910465.0271323
- [2026-05-05 00:01:07] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777910467.5964937 | source=vosk | frequency_hz=283.5 | rms=292 | updated_at=1777910465.0271323
- [2026-05-05 00:01:07] operator / voice_transcript_partial / voice: last alien
  meta: kind=partial | timestamp=1777910467.8504925 | source=vosk | frequency_hz=283.5 | rms=292 | updated_at=1777910465.0271323
- [2026-05-05 00:01:09] operator / voice_transcript_partial / voice: last the all queued
  meta: kind=partial | timestamp=1777910469.0696387 | source=vosk | frequency_hz=308.0 | rms=294 | updated_at=1777910468.3028212
- [2026-05-05 00:01:09] operator / voice_transcript_partial / voice: last the all queued yourself
  meta: kind=partial | timestamp=1777910469.316176 | source=vosk | frequency_hz=308.0 | rms=294 | updated_at=1777910468.3028212
- [2026-05-05 00:01:09] operator / voice_transcript_partial / voice: last the all queued response
  meta: kind=partial | timestamp=1777910469.5708632 | source=vosk | frequency_hz=308.0 | rms=294 | updated_at=1777910468.3028212
- [2026-05-05 00:01:09] operator / voice_transcript_partial / voice: last the all queued yourself
  meta: kind=partial | timestamp=1777910469.8188012 | source=vosk | frequency_hz=308.0 | rms=294 | updated_at=1777910468.3028212
- [2026-05-05 00:01:10] operator / voice_transcript_partial / voice: last the all queued resume last
  meta: kind=partial | timestamp=1777910470.0635507 | source=vosk | frequency_hz=308.0 | rms=294 | updated_at=1777910468.3028212
- [2026-05-05 00:01:10] operator / voice_transcript_partial / voice: last the all queued resume last change
  meta: kind=partial | timestamp=1777910470.5781367 | source=vosk | frequency_hz=308.0 | rms=294 | updated_at=1777910468.3028212
- [2026-05-05 00:01:10] operator / voice_transcript_partial / voice: last the all queued resume last change theme
  meta: kind=partial | timestamp=1777910470.8106277 | source=vosk | frequency_hz=308.0 | rms=294 | updated_at=1777910468.3028212
- [2026-05-05 00:01:11] operator / voice_transcript_partial / voice: last the all queued resume last change
  meta: kind=partial | timestamp=1777910471.0605357 | source=vosk | frequency_hz=308.0 | rms=294 | updated_at=1777910468.3028212
- [2026-05-05 00:01:11] operator / voice_transcript_partial / voice: last the all queued resume last change sentry
  meta: kind=partial | timestamp=1777910471.3114893 | source=vosk | frequency_hz=308.0 | rms=294 | updated_at=1777910468.3028212
- [2026-05-05 00:01:11] operator / voice_transcript_partial / voice: last the all queued resume last change sentry sentry
  meta: kind=partial | timestamp=1777910471.8109925 | source=vosk | frequency_hz=308.0 | rms=294 | updated_at=1777910468.3028212
- [2026-05-05 00:01:12] operator / voice_transcript_partial / voice: last the all queued resume last change sentry sentry it
  meta: kind=partial | timestamp=1777910472.5609448 | source=vosk | frequency_hz=400.0 | rms=304 | updated_at=1777910472.0535753
- [2026-05-05 00:01:13] operator / voice_transcript_partial / voice: last the all queued resume last change sentry sentry it [unk]
  meta: kind=partial | timestamp=1777910473.062095 | source=vosk | frequency_hz=400.0 | rms=304 | updated_at=1777910472.0535753
- [2026-05-05 00:01:13] operator / voice_transcript_partial / voice: last the all queued resume last change sentry sentry it [unk] to anything
  meta: kind=partial | timestamp=1777910473.318513 | source=vosk | frequency_hz=400.0 | rms=304 | updated_at=1777910472.0535753
- [2026-05-05 00:01:13] operator / voice_transcript_partial / voice: last the all queued resume last change sentry sentry it [unk] lion
  meta: kind=partial | timestamp=1777910473.566918 | source=vosk | frequency_hz=248.0 | rms=299 | updated_at=1777910473.5594022
- [2026-05-05 00:01:14] operator / voice_transcript_final / voice: last the all queued yourself last change sentry sentry it unk to and lion
  meta: kind=final | timestamp=1777910474.3123887 | source=final | frequency_hz=259.6 | rms=287 | updated_at=1777910474.0537083
- [2026-05-05 00:01:14] operator / voice_command / voice: last the all queued yourself last change sentry sentry it unk to and lion
  meta: normalized=True
- [2026-05-05 00:01:14] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777910474.571988 | source=vosk | frequency_hz=259.6 | rms=287 | updated_at=1777910474.0537083
- [2026-05-05 00:01:14] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777910474.811531 | source=vosk | frequency_hz=259.6 | rms=287 | updated_at=1777910474.0537083
- [2026-05-05 00:01:15] operator / voice_transcript_partial / voice: cancel all
  meta: kind=partial | timestamp=1777910475.0595136 | source=vosk | frequency_hz=259.6 | rms=287 | updated_at=1777910474.0537083
- [2026-05-05 00:01:15] operator / voice_transcript_partial / voice: cancel all tasks
  meta: kind=partial | timestamp=1777910475.3110938 | source=vosk | frequency_hz=259.6 | rms=287 | updated_at=1777910474.0537083
- [2026-05-05 00:01:15] operator / voice_transcript_partial / voice: cancel all tasks in queue
  meta: kind=partial | timestamp=1777910475.8133085 | source=vosk | frequency_hz=259.6 | rms=287 | updated_at=1777910474.0537083
- [2026-05-05 00:01:16] operator / voice_transcript_final / voice: cancel all tasks in queue
  meta: kind=final | timestamp=1777910476.830557 | source=final | frequency_hz=365.8 | rms=302 | updated_at=1777910476.803012
- [2026-05-05 00:01:17] operator / voice_command / voice: cancel all tasks in queue
  meta: normalized=True
- [2026-05-05 00:01:17] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:01:17] assistant / spoken_confirmation / voice: Cancelled assistant request about e the unk. What do you want me to do next?
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:01:17] assistant / spoken_confirmation / voice: Received. I started your assistant request about last the all queued yourself last change sentry sentr. in the background.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:01:19] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777910479.097322 | source=vosk | frequency_hz=263.4 | rms=292 | updated_at=1777910478.0544348
- [2026-05-05 00:01:19] operator / voice_transcript_partial / voice: standby guarding
  meta: kind=partial | timestamp=1777910479.3215053 | source=vosk | frequency_hz=263.4 | rms=292 | updated_at=1777910478.0544348
- [2026-05-05 00:01:19] operator / voice_transcript_partial / voice: standby guarding no
  meta: kind=partial | timestamp=1777910479.8309405 | source=vosk | frequency_hz=263.4 | rms=292 | updated_at=1777910478.0544348
- [2026-05-05 00:01:20] operator / voice_transcript_partial / voice: standby guarding no app to
  meta: kind=partial | timestamp=1777910480.099437 | source=vosk | frequency_hz=263.4 | rms=292 | updated_at=1777910478.0544348
- [2026-05-05 00:01:20] operator / voice_transcript_partial / voice: standby guarding no app to talk
  meta: kind=partial | timestamp=1777910480.3305027 | source=vosk | frequency_hz=263.4 | rms=292 | updated_at=1777910478.0544348
- [2026-05-05 00:01:20] operator / voice_transcript_partial / voice: standby guarding no app to talk it
  meta: kind=partial | timestamp=1777910480.585405 | source=vosk | frequency_hz=263.4 | rms=292 | updated_at=1777910478.0544348
- [2026-05-05 00:01:20] operator / voice_transcript_final / voice: standby go it no app to unk
  meta: kind=final | timestamp=1777910480.8264713 | source=final | frequency_hz=263.4 | rms=292 | updated_at=1777910478.0544348
- [2026-05-05 00:01:20] operator / voice_command / voice: standby go it no app to unk
  meta: normalized=True
- [2026-05-05 00:01:21] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777910481.0731075 | source=vosk | frequency_hz=263.4 | rms=292 | updated_at=1777910478.0544348
- [2026-05-05 00:01:21] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777910481.8326545 | source=final | frequency_hz=263.4 | rms=292 | updated_at=1777910478.0544348
- [2026-05-05 00:01:22] operator / voice_command / voice: no
  meta: normalized=True
- [2026-05-05 00:01:22] assistant / assistant_prompt / text: Assistant request queued: assistant request about no (position 3).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:01:22] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:01:22] assistant / spoken_confirmation / voice: I am still finishing assistant request about last the all queued yourself last change sentry sentr. I queued your assistant request about no. It is number 3 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:01:25] operator / voice_transcript_partial / voice: go increase
  meta: kind=partial | timestamp=1777910485.9031463 | source=vosk | frequency_hz=270.1 | rms=298 | updated_at=1777910484.5638428
- [2026-05-05 00:01:26] operator / voice_transcript_partial / voice: go in to rest
  meta: kind=partial | timestamp=1777910486.1144207 | source=vosk | frequency_hz=270.1 | rms=298 | updated_at=1777910484.5638428
- [2026-05-05 00:01:26] operator / voice_transcript_partial / voice: go in to rest disconnect
  meta: kind=partial | timestamp=1777910486.8423882 | source=vosk | frequency_hz=270.1 | rms=298 | updated_at=1777910484.5638428
- [2026-05-05 00:01:27] operator / voice_transcript_partial / voice: go in to rest resume no
  meta: kind=partial | timestamp=1777910487.1019287 | source=vosk | frequency_hz=340.0 | rms=296 | updated_at=1777910487.09433
- [2026-05-05 00:01:27] operator / voice_transcript_final / voice: go rest
  meta: kind=final | timestamp=1777910487.648964 | source=final | frequency_hz=350.8 | rms=310 | updated_at=1777910487.6281466
- [2026-05-05 00:01:27] operator / voice_command / voice: go rest
  meta: normalized=True
- [2026-05-05 00:01:28] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:01:30] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777910490.3345973 | source=vosk | frequency_hz=321.4 | rms=326 | updated_at=1777910488.3158484
- [2026-05-05 00:01:30] operator / voice_transcript_partial / voice: to anything go
  meta: kind=partial | timestamp=1777910490.6306243 | source=vosk | frequency_hz=321.4 | rms=326 | updated_at=1777910488.3158484
- [2026-05-05 00:01:30] operator / voice_transcript_partial / voice: resume guarding
  meta: kind=partial | timestamp=1777910490.851366 | source=vosk | frequency_hz=321.4 | rms=326 | updated_at=1777910488.3158484
- [2026-05-05 00:01:31] operator / voice_transcript_partial / voice: resume guarding mode
  meta: kind=partial | timestamp=1777910491.119194 | source=vosk | frequency_hz=321.4 | rms=326 | updated_at=1777910488.3158484
- [2026-05-05 00:01:31] operator / voice_transcript_partial / voice: to anything current app
  meta: kind=partial | timestamp=1777910491.35235 | source=vosk | frequency_hz=321.4 | rms=326 | updated_at=1777910488.3158484
- [2026-05-05 00:01:31] operator / voice_transcript_partial / voice: to anything current app to
  meta: kind=partial | timestamp=1777910491.6031122 | source=vosk | frequency_hz=321.4 | rms=326 | updated_at=1777910488.3158484
- [2026-05-05 00:01:32] operator / voice_transcript_partial / voice: to anything current app to com
  meta: kind=partial | timestamp=1777910492.5915375 | source=vosk | frequency_hz=321.4 | rms=326 | updated_at=1777910488.3158484
- [2026-05-05 00:01:32] operator / voice_transcript_partial / voice: to anything current app to on
  meta: kind=partial | timestamp=1777910492.8359802 | source=vosk | frequency_hz=321.4 | rms=326 | updated_at=1777910488.3158484
- [2026-05-05 00:01:33] operator / voice_transcript_partial / voice: to anything current app to on commands
  meta: kind=partial | timestamp=1777910493.116677 | source=vosk | frequency_hz=321.4 | rms=326 | updated_at=1777910488.3158484
- [2026-05-05 00:01:33] operator / voice_transcript_final / voice: anything current app to on
  meta: kind=final | timestamp=1777910493.8350897 | source=final | frequency_hz=321.4 | rms=326 | updated_at=1777910488.3158484
- [2026-05-05 00:01:34] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777910494.6130064 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:35] operator / voice_transcript_partial / voice: last task
  meta: kind=partial | timestamp=1777910495.0792432 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:35] operator / voice_transcript_partial / voice: last tracking
  meta: kind=partial | timestamp=1777910495.3373544 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:35] operator / voice_transcript_partial / voice: last tracking priority
  meta: kind=partial | timestamp=1777910495.5811434 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:35] operator / voice_transcript_partial / voice: last tracking
  meta: kind=partial | timestamp=1777910495.83126 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:36] operator / voice_transcript_partial / voice: last tracking pause smart
  meta: kind=partial | timestamp=1777910496.09325 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:36] operator / voice_transcript_partial / voice: last tracking pause
  meta: kind=partial | timestamp=1777910496.3312979 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:36] operator / voice_transcript_partial / voice: last tracking pause current
  meta: kind=partial | timestamp=1777910496.5815754 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:36] operator / voice_transcript_partial / voice: last tracking pause task disconnect
  meta: kind=partial | timestamp=1777910496.8312373 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:37] operator / voice_transcript_partial / voice: last tracking pause task disable
  meta: kind=partial | timestamp=1777910497.0805094 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:37] operator / voice_transcript_partial / voice: last tracking pause task disable the guarding
  meta: kind=partial | timestamp=1777910497.3319216 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:37] operator / voice_transcript_partial / voice: last tracking pause task disable the go home
  meta: kind=partial | timestamp=1777910497.8403647 | source=vosk | frequency_hz=308.0 | rms=286 | updated_at=1777910494.5883162
- [2026-05-05 00:01:38] operator / voice_transcript_final / voice: go home
  meta: kind=final | timestamp=1777910498.338448 | source=final | frequency_hz=349.6 | rms=304 | updated_at=1777910498.3229015
- [2026-05-05 00:01:41] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777910501.8323805 | source=vosk | frequency_hz=340.3 | rms=519 | updated_at=1777910501.0733604
- [2026-05-05 00:01:42] operator / voice_transcript_partial / voice: commands
  meta: kind=partial | timestamp=1777910502.0834787 | source=vosk | frequency_hz=340.3 | rms=519 | updated_at=1777910501.0733604
- [2026-05-05 00:01:42] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777910502.3328695 | source=vosk | frequency_hz=340.3 | rms=519 | updated_at=1777910501.0733604
- [2026-05-05 00:01:43] operator / voice_transcript_final / voice: commands
  meta: kind=final | timestamp=1777910503.6047873 | source=final | frequency_hz=340.3 | rms=519 | updated_at=1777910501.0733604
- [2026-05-05 00:01:43] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777910503.836947 | source=vosk | frequency_hz=340.3 | rms=519 | updated_at=1777910501.0733604
- [2026-05-05 00:01:44] operator / voice_transcript_partial / voice: a no
  meta: kind=partial | timestamp=1777910504.3331075 | source=vosk | frequency_hz=340.3 | rms=519 | updated_at=1777910501.0733604
- [2026-05-05 00:01:45] operator / voice_transcript_final / voice: a no
  meta: kind=final | timestamp=1777910505.0859382 | source=final | frequency_hz=336.0 | rms=279 | updated_at=1777910505.0739148
- [2026-05-05 00:01:46] operator / voice_transcript_partial / voice: stop
  meta: kind=partial | timestamp=1777910506.3306367 | source=vosk | frequency_hz=332.5 | rms=286 | updated_at=1777910505.3288593
- [2026-05-05 00:01:47] operator / voice_transcript_final / voice: stop
  meta: kind=final | timestamp=1777910507.081204 | source=final | frequency_hz=332.5 | rms=286 | updated_at=1777910505.3288593
- [2026-05-05 00:01:49] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777910509.8412802 | source=vosk | frequency_hz=310.4 | rms=283 | updated_at=1777910509.0741189
- [2026-05-05 00:01:50] operator / voice_transcript_partial / voice: to mode
  meta: kind=partial | timestamp=1777910510.3303308 | source=vosk | frequency_hz=310.4 | rms=283 | updated_at=1777910509.0741189
- [2026-05-05 00:01:50] operator / voice_transcript_partial / voice: to smart sentry
  meta: kind=partial | timestamp=1777910510.582027 | source=vosk | frequency_hz=310.4 | rms=283 | updated_at=1777910509.0741189
- [2026-05-05 00:01:51] operator / voice_transcript_final / voice: to mode
  meta: kind=final | timestamp=1777910511.0838532 | source=final | frequency_hz=310.4 | rms=283 | updated_at=1777910509.0741189
- [2026-05-05 00:01:51] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777910511.330622 | source=vosk | frequency_hz=310.4 | rms=283 | updated_at=1777910509.0741189
- [2026-05-05 00:01:52] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777910512.3302088 | source=vosk | frequency_hz=310.4 | rms=283 | updated_at=1777910509.0741189
- [2026-05-05 00:01:54] operator / voice_transcript_partial / voice: stop
  meta: kind=partial | timestamp=1777910514.855807 | source=vosk | frequency_hz=331.8 | rms=273 | updated_at=1777910513.8253062
- [2026-05-05 00:01:55] operator / voice_transcript_partial / voice: stop that
  meta: kind=partial | timestamp=1777910515.3607047 | source=vosk | frequency_hz=331.8 | rms=273 | updated_at=1777910513.8253062
- [2026-05-05 00:01:55] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777910515.6039784 | source=final | frequency_hz=331.8 | rms=273 | updated_at=1777910513.8253062
- [2026-05-05 00:01:57] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777910517.6022115 | source=vosk | frequency_hz=283.0 | rms=290 | updated_at=1777910516.3464825
- [2026-05-05 00:01:57] operator / voice_transcript_partial / voice: standby go
  meta: kind=partial | timestamp=1777910517.8547523 | source=vosk | frequency_hz=283.0 | rms=290 | updated_at=1777910516.3464825
- [2026-05-05 00:01:58] operator / voice_transcript_partial / voice: standby guarding
  meta: kind=partial | timestamp=1777910518.1197617 | source=vosk | frequency_hz=283.0 | rms=290 | updated_at=1777910516.3464825
- [2026-05-05 00:01:58] operator / voice_transcript_partial / voice: standby guarding mode
  meta: kind=partial | timestamp=1777910518.3513355 | source=vosk | frequency_hz=283.0 | rms=290 | updated_at=1777910516.3464825
- [2026-05-05 00:01:58] operator / voice_transcript_partial / voice: standby go ahead no
  meta: kind=partial | timestamp=1777910518.6036 | source=vosk | frequency_hz=283.0 | rms=290 | updated_at=1777910516.3464825
- [2026-05-05 00:01:58] operator / voice_transcript_partial / voice: standby go ahead no app to
  meta: kind=partial | timestamp=1777910518.853774 | source=vosk | frequency_hz=283.0 | rms=290 | updated_at=1777910516.3464825
- [2026-05-05 00:01:59] operator / voice_transcript_partial / voice: standby go ahead no app to talk
  meta: kind=partial | timestamp=1777910519.3573115 | source=vosk | frequency_hz=283.0 | rms=290 | updated_at=1777910516.3464825
- [2026-05-05 00:01:59] operator / voice_transcript_partial / voice: standby go ahead no app to talk it
  meta: kind=partial | timestamp=1777910519.6126945 | source=vosk | frequency_hz=283.0 | rms=290 | updated_at=1777910516.3464825
- [2026-05-05 00:01:59] operator / voice_transcript_partial / voice: standby go ahead no app to talk it brightness
  meta: kind=partial | timestamp=1777910519.8622842 | source=vosk | frequency_hz=283.0 | rms=290 | updated_at=1777910516.3464825
- [2026-05-05 00:02:00] operator / voice_transcript_partial / voice: standby go ahead no app to talk it no
  meta: kind=partial | timestamp=1777910520.1126008 | source=vosk | frequency_hz=283.0 | rms=290 | updated_at=1777910516.3464825
- [2026-05-05 00:02:00] operator / voice_transcript_final / voice: standby go it no app to talk it no
  meta: kind=final | timestamp=1777910520.6049175 | source=final | frequency_hz=292.6 | rms=286 | updated_at=1777910520.5953443
- [2026-05-05 00:02:02] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777910522.119762 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:02] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777910522.3633997 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:02] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777910522.61332 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:02] operator / voice_transcript_partial / voice: tracking pause to
  meta: kind=partial | timestamp=1777910522.8643003 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:03] operator / voice_transcript_partial / voice: tracking pause go
  meta: kind=partial | timestamp=1777910523.1123495 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:03] operator / voice_transcript_partial / voice: tracking pause go it again
  meta: kind=partial | timestamp=1777910523.362206 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:03] operator / voice_transcript_partial / voice: tracking pause go e to guarding
  meta: kind=partial | timestamp=1777910523.622365 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:03] operator / voice_transcript_partial / voice: tracking pause go e to com
  meta: kind=partial | timestamp=1777910523.8760264 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:04] operator / voice_transcript_final / voice: tracking pause go it again
  meta: kind=final | timestamp=1777910524.125266 | source=final | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:04] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777910524.3698633 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:04] operator / voice_transcript_partial / voice: stop
  meta: kind=partial | timestamp=1777910524.6200523 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:05] operator / voice_transcript_partial / voice: stop go
  meta: kind=partial | timestamp=1777910525.1210024 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:05] operator / voice_transcript_partial / voice: stop
  meta: kind=partial | timestamp=1777910525.6166654 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:05] operator / voice_transcript_partial / voice: stop standby
  meta: kind=partial | timestamp=1777910525.8638482 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:06] operator / voice_transcript_partial / voice: stop standby go
  meta: kind=partial | timestamp=1777910526.36218 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:06] operator / voice_transcript_partial / voice: stop standby go no
  meta: kind=partial | timestamp=1777910526.8635902 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:07] operator / voice_transcript_partial / voice: stop standby go no app to
  meta: kind=partial | timestamp=1777910527.1223767 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:07] operator / voice_transcript_partial / voice: stop standby go no app to talk
  meta: kind=partial | timestamp=1777910527.6205683 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:07] operator / voice_transcript_partial / voice: stop standby go no app to talk yes
  meta: kind=partial | timestamp=1777910527.8676162 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:08] operator / voice_transcript_final / voice: stop go standby go no app to talk yes
  meta: kind=final | timestamp=1777910528.1407976 | source=final | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:10] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777910530.1165109 | source=vosk | frequency_hz=273.9 | rms=282 | updated_at=1777910521.607094
- [2026-05-05 00:02:11] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1777910531.1214128 | source=final | frequency_hz=256.0 | rms=873 | updated_at=1777910530.611582
- [2026-05-05 00:02:12] operator / voice_transcript_partial / voice: app
  meta: kind=partial | timestamp=1777910532.6316652 | source=vosk | frequency_hz=248.3 | rms=599 | updated_at=1777910531.6246254
- [2026-05-05 00:02:13] operator / voice_transcript_final / voice: app
  meta: kind=final | timestamp=1777910533.3816652 | source=final | frequency_hz=303.8 | rms=290 | updated_at=1777910533.3746624
- [2026-05-05 00:02:19] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:02:24] operator / voice_transcript_partial / voice: priority
  meta: kind=partial | timestamp=1777910544.9441097 | source=vosk | frequency_hz=320.7 | rms=315 | updated_at=1777910544.1496768
- [2026-05-05 00:02:25] operator / voice_transcript_partial / voice: lion app to
  meta: kind=partial | timestamp=1777910545.1525826 | source=vosk | frequency_hz=320.7 | rms=315 | updated_at=1777910544.1496768
- [2026-05-05 00:02:25] operator / voice_transcript_partial / voice: lion app to anything
  meta: kind=partial | timestamp=1777910545.3909702 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:25] operator / voice_transcript_partial / voice: lion app to anything else
  meta: kind=partial | timestamp=1777910545.8843946 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:26] operator / voice_transcript_partial / voice: lion app to anything the smart
  meta: kind=partial | timestamp=1777910546.1592019 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:26] operator / voice_transcript_partial / voice: lion app to anything the smart sentry
  meta: kind=partial | timestamp=1777910546.6308286 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:26] operator / voice_transcript_partial / voice: lion app to anything the smart theme to
  meta: kind=partial | timestamp=1777910546.8829517 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:27] operator / voice_transcript_partial / voice: lion app to anything the smart theme to mode
  meta: kind=partial | timestamp=1777910547.632726 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:28] operator / voice_transcript_partial / voice: lion app to anything the smart theme to mode a priority
  meta: kind=partial | timestamp=1777910548.135692 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:28] operator / voice_transcript_partial / voice: lion app to anything the smart theme to mode abort current
  meta: kind=partial | timestamp=1777910548.384768 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:28] operator / voice_transcript_partial / voice: lion app to anything the smart theme to mode a port go ahead
  meta: kind=partial | timestamp=1777910548.9041746 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:29] operator / voice_transcript_partial / voice: lion app to anything the smart theme to mode a port to com
  meta: kind=partial | timestamp=1777910549.131968 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:29] operator / voice_transcript_partial / voice: lion app to anything the smart theme to mode a port to com status
  meta: kind=partial | timestamp=1777910549.3824525 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:30] operator / voice_transcript_final / voice: lion app to anything the smart last repeat it to mode a port to com status
  meta: kind=final | timestamp=1777910550.1358237 | source=final | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:30] operator / voice_command / voice: lion app to anything the smart last repeat it to mode a port to com status
  meta: normalized=True
- [2026-05-05 00:02:30] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910550.6329026 | source=vosk | frequency_hz=309.3 | rms=321 | updated_at=1777910545.375858
- [2026-05-05 00:02:35] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:02:35] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777910555.1709402 | source=final | frequency_hz=388.0 | rms=334 | updated_at=1777910554.6253486
- [2026-05-05 00:02:35] operator / voice_command / voice: unk
  meta: normalized=True
- [2026-05-05 00:02:35] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777910555.5107932 | source=vosk | frequency_hz=388.0 | rms=334 | updated_at=1777910554.6253486
- [2026-05-05 00:02:35] operator / voice_transcript_partial / voice: strict on
  meta: kind=partial | timestamp=1777910555.7121897 | source=vosk | frequency_hz=388.0 | rms=334 | updated_at=1777910554.6253486
- [2026-05-05 00:02:36] operator / voice_transcript_partial / voice: strict
  meta: kind=partial | timestamp=1777910556.019084 | source=vosk | frequency_hz=388.0 | rms=334 | updated_at=1777910554.6253486
- [2026-05-05 00:02:36] operator / voice_transcript_partial / voice: strict eileen
  meta: kind=partial | timestamp=1777910556.5148375 | source=vosk | frequency_hz=408.0 | rms=316 | updated_at=1777910556.135381
- [2026-05-05 00:02:37] operator / voice_transcript_final / voice: strict
  meta: kind=final | timestamp=1777910557.21639 | source=final | frequency_hz=387.0 | rms=301 | updated_at=1777910557.123895
- [2026-05-05 00:02:37] operator / voice_command / voice: strict
  meta: normalized=True
- [2026-05-05 00:02:37] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777910557.7245147 | source=vosk | frequency_hz=387.0 | rms=301 | updated_at=1777910557.123895
- [2026-05-05 00:02:37] operator / voice_transcript_partial / voice: and cancel
  meta: kind=partial | timestamp=1777910557.9696686 | source=vosk | frequency_hz=387.0 | rms=301 | updated_at=1777910557.123895
- [2026-05-05 00:02:38] operator / voice_transcript_partial / voice: and current serial
  meta: kind=partial | timestamp=1777910558.2277617 | source=vosk | frequency_hz=387.0 | rms=301 | updated_at=1777910557.123895
- [2026-05-05 00:02:38] operator / voice_transcript_partial / voice: and cancel
  meta: kind=partial | timestamp=1777910558.5150373 | source=vosk | frequency_hz=387.0 | rms=301 | updated_at=1777910557.123895
- [2026-05-05 00:02:39] operator / voice_transcript_final / voice: and current serial
  meta: kind=final | timestamp=1777910559.3648274 | source=final | frequency_hz=329.7 | rms=306 | updated_at=1777910558.9548163
- [2026-05-05 00:02:39] operator / voice_command / voice: and current serial
  meta: normalized=True
- [2026-05-05 00:02:40] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777910560.052821 | source=vosk | frequency_hz=302.5 | rms=303 | updated_at=1777910559.3648274
- [2026-05-05 00:02:40] operator / voice_transcript_partial / voice: that delay
  meta: kind=partial | timestamp=1777910560.3016026 | source=vosk | frequency_hz=302.5 | rms=303 | updated_at=1777910559.3648274
- [2026-05-05 00:02:40] operator / voice_transcript_partial / voice: that diagnostics
  meta: kind=partial | timestamp=1777910560.5569127 | source=vosk | frequency_hz=302.5 | rms=303 | updated_at=1777910559.3648274
- [2026-05-05 00:02:41] operator / voice_transcript_partial / voice: that diagnostics no commands
  meta: kind=partial | timestamp=1777910561.3018355 | source=vosk | frequency_hz=302.5 | rms=303 | updated_at=1777910559.3648274
- [2026-05-05 00:02:42] operator / voice_transcript_partial / voice: that diagnostics no commands eileen
  meta: kind=partial | timestamp=1777910562.3015761 | source=vosk | frequency_hz=302.5 | rms=303 | updated_at=1777910559.3648274
- [2026-05-05 00:02:42] operator / voice_transcript_partial / voice: that diagnostics no commands aileen repeat
  meta: kind=partial | timestamp=1777910562.5610442 | source=vosk | frequency_hz=302.5 | rms=303 | updated_at=1777910559.3648274
- [2026-05-05 00:02:43] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:02:43] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:02:43] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:02:47] operator / voice_transcript_final / voice: that do no that no commands repeat
  meta: kind=final | timestamp=1777910567.4025655 | source=final | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:47] operator / voice_command / voice: that do no that no commands repeat
  meta: normalized=True
- [2026-05-05 00:02:48] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777910568.1606803 | source=vosk | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:48] operator / voice_transcript_partial / voice: stop that
  meta: kind=partial | timestamp=1777910568.4027112 | source=vosk | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:48] operator / voice_transcript_partial / voice: stop that no
  meta: kind=partial | timestamp=1777910568.6485581 | source=vosk | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:49] operator / voice_transcript_final / voice: stop that
  meta: kind=final | timestamp=1777910569.1509643 | source=final | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:49] operator / voice_command / voice: stop that
  meta: normalized=True
- [2026-05-05 00:02:49] operator / voice_transcript_partial / voice: aileen
  meta: kind=partial | timestamp=1777910569.8970275 | source=vosk | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:50] operator / voice_transcript_partial / voice: aileen repeat
  meta: kind=partial | timestamp=1777910570.1556363 | source=vosk | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:51] operator / voice_transcript_final / voice: repeat
  meta: kind=final | timestamp=1777910571.171755 | source=final | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:51] operator / voice_command / voice: repeat
  meta: normalized=True
- [2026-05-05 00:02:51] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777910571.39774 | source=vosk | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:51] operator / voice_transcript_partial / voice: again you
  meta: kind=partial | timestamp=1777910571.6694481 | source=vosk | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:51] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777910571.9014225 | source=vosk | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:52] operator / voice_transcript_partial / voice: connect eileen do
  meta: kind=partial | timestamp=1777910572.1644425 | source=vosk | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:52] operator / voice_transcript_partial / voice: connect eileen go
  meta: kind=partial | timestamp=1777910572.3980951 | source=vosk | frequency_hz=224.7 | rms=461 | updated_at=1777910567.393048
- [2026-05-05 00:02:52] assistant / spoken_confirmation / voice: Received. I started your assistant request about repeat in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:02:53] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:02:53] assistant / spoken_confirmation / voice: Cancelled assistant request about but faster. What do you want me to do next?
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:02:53] operator / voice_transcript_final / voice: connect go
  meta: kind=final | timestamp=1777910573.2509046 | source=final | frequency_hz=376.0 | rms=352 | updated_at=1777910572.65098
- [2026-05-05 00:02:53] operator / voice_command / voice: connect go
  meta: normalized=True
- [2026-05-05 00:02:53] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777910573.4393697 | source=vosk | frequency_hz=376.0 | rms=352 | updated_at=1777910572.65098
- [2026-05-05 00:02:53] operator / voice_transcript_partial / voice: change increase
  meta: kind=partial | timestamp=1777910573.667263 | source=vosk | frequency_hz=376.0 | rms=352 | updated_at=1777910572.65098
- [2026-05-05 00:02:53] operator / voice_transcript_partial / voice: change theme guarding
  meta: kind=partial | timestamp=1777910573.9094846 | source=vosk | frequency_hz=376.0 | rms=352 | updated_at=1777910572.65098
- [2026-05-05 00:02:54] operator / voice_transcript_partial / voice: change the current no
  meta: kind=partial | timestamp=1777910574.1854794 | source=vosk | frequency_hz=376.0 | rms=352 | updated_at=1777910572.65098
- [2026-05-05 00:02:54] operator / voice_transcript_partial / voice: change the current no app to
  meta: kind=partial | timestamp=1777910574.6574945 | source=vosk | frequency_hz=376.0 | rms=352 | updated_at=1777910572.65098
- [2026-05-05 00:02:54] operator / voice_transcript_partial / voice: change the current no app to talk
  meta: kind=partial | timestamp=1777910574.9111104 | source=vosk | frequency_hz=376.0 | rms=352 | updated_at=1777910572.65098
- [2026-05-05 00:02:55] operator / voice_transcript_partial / voice: change the current no app to talk it
  meta: kind=partial | timestamp=1777910575.1788106 | source=vosk | frequency_hz=376.0 | rms=352 | updated_at=1777910572.65098
- [2026-05-05 00:02:55] operator / voice_transcript_partial / voice: change the current no app to talk it brightness
  meta: kind=partial | timestamp=1777910575.4148107 | source=vosk | frequency_hz=376.0 | rms=352 | updated_at=1777910572.65098
- [2026-05-05 00:02:56] operator / voice_transcript_final / voice: change the it no app to talk it brightness
  meta: kind=final | timestamp=1777910576.450515 | source=final | frequency_hz=368.6 | rms=381 | updated_at=1777910576.442301
- [2026-05-05 00:02:56] operator / voice_command / voice: change the it no app to talk it brightness
  meta: normalized=True
- [2026-05-05 00:02:57] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:02:57] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:02:57] operator / voice_transcript_partial / voice: increase
  meta: kind=partial | timestamp=1777910577.7427123 | source=vosk | frequency_hz=368.6 | rms=381 | updated_at=1777910576.442301
- [2026-05-05 00:02:57] operator / voice_transcript_partial / voice: pause
  meta: kind=partial | timestamp=1777910577.9869523 | source=vosk | frequency_hz=368.6 | rms=381 | updated_at=1777910576.442301
- [2026-05-05 00:02:58] operator / voice_transcript_partial / voice: pause smart
  meta: kind=partial | timestamp=1777910578.2396848 | source=vosk | frequency_hz=368.6 | rms=381 | updated_at=1777910576.442301
- [2026-05-05 00:02:58] operator / voice_transcript_partial / voice: queued tasks
  meta: kind=partial | timestamp=1777910578.5172668 | source=vosk | frequency_hz=368.6 | rms=381 | updated_at=1777910576.442301
- [2026-05-05 00:02:58] operator / voice_transcript_partial / voice: pause current
  meta: kind=partial | timestamp=1777910578.7525754 | source=vosk | frequency_hz=368.6 | rms=381 | updated_at=1777910576.442301
- [2026-05-05 00:02:58] operator / voice_transcript_partial / voice: pause current it
  meta: kind=partial | timestamp=1777910578.9981499 | source=vosk | frequency_hz=368.6 | rms=381 | updated_at=1777910576.442301
- [2026-05-05 00:02:59] operator / voice_transcript_partial / voice: pause current it home
  meta: kind=partial | timestamp=1777910579.2432806 | source=vosk | frequency_hz=368.6 | rms=381 | updated_at=1777910576.442301
- [2026-05-05 00:02:59] operator / voice_transcript_partial / voice: pause current it home the current
  meta: kind=partial | timestamp=1777910579.48829 | source=vosk | frequency_hz=368.6 | rms=381 | updated_at=1777910576.442301
- [2026-05-05 00:02:59] operator / voice_transcript_partial / voice: pause current it home the go mind
  meta: kind=partial | timestamp=1777910579.9885342 | source=vosk | frequency_hz=368.6 | rms=381 | updated_at=1777910576.442301
- [2026-05-05 00:03:00] operator / voice_transcript_partial / voice: pause current it home the go be identify
  meta: kind=partial | timestamp=1777910580.2384884 | source=vosk | frequency_hz=368.6 | rms=381 | updated_at=1777910576.442301
- [2026-05-05 00:03:00] operator / voice_transcript_partial / voice: pause current it home the go be a do
  meta: kind=partial | timestamp=1777910580.4941182 | source=vosk | frequency_hz=312.0 | rms=321 | updated_at=1777910580.4809437
- [2026-05-05 00:03:01] operator / voice_transcript_final / voice: pause current it home the go be a do
  meta: kind=final | timestamp=1777910581.0629787 | source=final | frequency_hz=296.6 | rms=317 | updated_at=1777910580.7309015
- [2026-05-05 00:03:01] operator / voice_command / voice: pause current it home the go be a do
  meta: normalized=True
- [2026-05-05 00:03:01] assistant / assistant_prompt / text: Assistant request queued: assistant request about pause current it home the go be a do (position 3).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:03:02] assistant / spoken_confirmation / voice: I am still finishing assistant request about repeat. I queued your assistant request about pause current it home the go be a do. It is number 3 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:03:02] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777910582.9876127 | source=vosk | frequency_hz=308.2 | rms=338 | updated_at=1777910582.2334664
- [2026-05-05 00:03:03] operator / voice_transcript_partial / voice: elliot do
  meta: kind=partial | timestamp=1777910583.2452922 | source=vosk | frequency_hz=308.2 | rms=338 | updated_at=1777910582.2334664
- [2026-05-05 00:03:04] operator / voice_transcript_final / voice: to do
  meta: kind=final | timestamp=1777910584.6135411 | source=final | frequency_hz=291.7 | rms=330 | updated_at=1777910583.9810905
- [2026-05-05 00:03:04] operator / voice_command / voice: to do
  meta: normalized=True
- [2026-05-05 00:03:04] assistant / assistant_prompt / text: Assistant request queued: assistant request about to do (position 4).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:03:05] assistant / spoken_confirmation / voice: I am still finishing assistant request about repeat. I queued your assistant request about to do. It is number 4 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:03:06] operator / voice_transcript_partial / voice: increase
  meta: kind=partial | timestamp=1777910586.037986 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:06] operator / voice_transcript_partial / voice: rest
  meta: kind=partial | timestamp=1777910586.2736628 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:06] operator / voice_transcript_partial / voice: rest override
  meta: kind=partial | timestamp=1777910586.7762456 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:07] operator / voice_transcript_partial / voice: rest on e
  meta: kind=partial | timestamp=1777910587.026215 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:07] operator / voice_transcript_partial / voice: rest on e the
  meta: kind=partial | timestamp=1777910587.2837834 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:07] operator / voice_transcript_partial / voice: rest on e the rest
  meta: kind=partial | timestamp=1777910587.5216181 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:07] operator / voice_transcript_partial / voice: rest on e the rest it
  meta: kind=partial | timestamp=1777910587.7930248 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:08] operator / voice_transcript_partial / voice: rest on e the rest it all brightness
  meta: kind=partial | timestamp=1777910588.0438902 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:08] operator / voice_transcript_partial / voice: rest on e the rest it override connect
  meta: kind=partial | timestamp=1777910588.2816522 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:08] operator / voice_transcript_partial / voice: rest on e the rest it app are it again change
  meta: kind=partial | timestamp=1777910588.5237818 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:08] operator / voice_transcript_partial / voice: rest on e the rest it app are it again change the
  meta: kind=partial | timestamp=1777910588.7717927 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:09] operator / voice_transcript_partial / voice: rest on e the rest it app are it again change smart
  meta: kind=partial | timestamp=1777910589.0230029 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:09] operator / voice_transcript_partial / voice: rest on e the rest it app are it again change smart sentry
  meta: kind=partial | timestamp=1777910589.2803168 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:10] operator / voice_transcript_partial / voice: rest on e the rest it app are it again change smart sentry abort lion
  meta: kind=partial | timestamp=1777910590.268846 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:10] operator / voice_transcript_partial / voice: rest on e the rest it app are it again change smart sentry abort lion enable
  meta: kind=partial | timestamp=1777910590.5211334 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:10] operator / voice_transcript_partial / voice: rest on e the rest it app are it again change smart sentry abort lion in queue
  meta: kind=partial | timestamp=1777910590.7697773 | source=vosk | frequency_hz=262.4 | rms=870 | updated_at=1777910585.5235875
- [2026-05-05 00:03:11] operator / voice_transcript_partial / voice: rest on e the rest it app are it again change smart sentry abort lion in more
  meta: kind=partial | timestamp=1777910591.0198092 | source=vosk | frequency_hz=380.0 | rms=305 | updated_at=1777910591.0122905
- [2026-05-05 00:03:11] operator / voice_transcript_partial / voice: rest on e the rest it app are it again change smart sentry abort lion in more strict
  meta: kind=partial | timestamp=1777910591.2694554 | source=vosk | frequency_hz=378.6 | rms=315 | updated_at=1777910591.2619467
- [2026-05-05 00:03:11] operator / voice_transcript_final / voice: repeat rest on e the rest it app are it again change smart sentry abort lion in more
  meta: kind=final | timestamp=1777910591.7748394 | source=final | frequency_hz=328.7 | rms=302 | updated_at=1777910591.7623236
- [2026-05-05 00:03:11] operator / voice_command / voice: repeat rest on e the rest it app are it again change smart sentry abort lion in more
  meta: normalized=True
- [2026-05-05 00:03:12] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:03:13] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777910593.0267358 | source=vosk | frequency_hz=283.7 | rms=303 | updated_at=1777910592.512574
- [2026-05-05 00:03:13] operator / voice_transcript_partial / voice: go that
  meta: kind=partial | timestamp=1777910593.272455 | source=vosk | frequency_hz=283.7 | rms=303 | updated_at=1777910592.512574
- [2026-05-05 00:03:13] operator / voice_transcript_partial / voice: go that be
  meta: kind=partial | timestamp=1777910593.521072 | source=vosk | frequency_hz=283.7 | rms=303 | updated_at=1777910592.512574
- [2026-05-05 00:03:13] operator / voice_transcript_partial / voice: go that
  meta: kind=partial | timestamp=1777910593.770323 | source=vosk | frequency_hz=283.7 | rms=303 | updated_at=1777910592.512574
- [2026-05-05 00:03:14] operator / voice_transcript_partial / voice: go that be
  meta: kind=partial | timestamp=1777910594.0239408 | source=vosk | frequency_hz=283.7 | rms=303 | updated_at=1777910592.512574
- [2026-05-05 00:03:15] operator / voice_transcript_final / voice: go that be a
  meta: kind=final | timestamp=1777910595.2789173 | source=final | frequency_hz=236.0 | rms=312 | updated_at=1777910595.2699027
- [2026-05-05 00:03:15] operator / voice_command / voice: go that be a
  meta: normalized=True
- [2026-05-05 00:03:16] operator / voice_transcript_partial / voice: ahead the
  meta: kind=partial | timestamp=1777910596.2699335 | source=vosk | frequency_hz=236.0 | rms=312 | updated_at=1777910595.2699027
- [2026-05-05 00:03:16] operator / voice_transcript_partial / voice: ahead the report
  meta: kind=partial | timestamp=1777910596.5182283 | source=vosk | frequency_hz=236.0 | rms=312 | updated_at=1777910595.2699027
- [2026-05-05 00:03:17] operator / voice_transcript_final / voice: ahead the report
  meta: kind=final | timestamp=1777910597.7257242 | source=final | frequency_hz=236.0 | rms=312 | updated_at=1777910595.2699027
- [2026-05-05 00:03:17] operator / voice_command / voice: ahead the report
  meta: normalized=True
- [2026-05-05 00:03:17] operator / voice_transcript_partial / voice: override
  meta: kind=partial | timestamp=1777910597.732741 | source=vosk | frequency_hz=236.0 | rms=312 | updated_at=1777910595.2699027
- [2026-05-05 00:03:17] operator / voice_transcript_partial / voice: on e lion
  meta: kind=partial | timestamp=1777910597.7808425 | source=vosk | frequency_hz=236.0 | rms=312 | updated_at=1777910595.2699027
- [2026-05-05 00:03:18] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:03:18] operator / voice_transcript_partial / voice: override
  meta: kind=partial | timestamp=1777910598.0192049 | source=vosk | frequency_hz=236.0 | rms=312 | updated_at=1777910595.2699027
- [2026-05-05 00:03:18] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910598.2731187 | source=vosk | frequency_hz=236.0 | rms=312 | updated_at=1777910595.2699027
- [2026-05-05 00:03:19] operator / voice_transcript_partial / voice: [unk] the
  meta: kind=partial | timestamp=1777910599.7716753 | source=vosk | frequency_hz=236.0 | rms=312 | updated_at=1777910595.2699027
- [2026-05-05 00:03:20] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910600.01909 | source=vosk | frequency_hz=236.0 | rms=312 | updated_at=1777910595.2699027
- [2026-05-05 00:03:22] operator / voice_transcript_partial / voice: [unk] standby
  meta: kind=partial | timestamp=1777910602.27037 | source=vosk | frequency_hz=260.0 | rms=412 | updated_at=1777910601.2640102
- [2026-05-05 00:03:22] operator / voice_transcript_partial / voice: [unk] standby go
  meta: kind=partial | timestamp=1777910602.518811 | source=vosk | frequency_hz=260.0 | rms=412 | updated_at=1777910601.2640102
- [2026-05-05 00:03:22] operator / voice_transcript_partial / voice: [unk] standby guarding
  meta: kind=partial | timestamp=1777910602.7825694 | source=vosk | frequency_hz=260.0 | rms=412 | updated_at=1777910601.2640102
- [2026-05-05 00:03:23] operator / voice_transcript_partial / voice: [unk] standby go it
  meta: kind=partial | timestamp=1777910603.0240932 | source=vosk | frequency_hz=260.0 | rms=412 | updated_at=1777910601.2640102
- [2026-05-05 00:03:23] operator / voice_transcript_partial / voice: [unk] standby go it no
  meta: kind=partial | timestamp=1777910603.2694294 | source=vosk | frequency_hz=260.0 | rms=412 | updated_at=1777910601.2640102
- [2026-05-05 00:03:23] operator / voice_transcript_partial / voice: [unk] standby go it no app to
  meta: kind=partial | timestamp=1777910603.5428562 | source=vosk | frequency_hz=260.0 | rms=412 | updated_at=1777910601.2640102
- [2026-05-05 00:03:23] operator / voice_transcript_partial / voice: [unk] standby go it no app to talk
  meta: kind=partial | timestamp=1777910603.7759726 | source=vosk | frequency_hz=260.0 | rms=412 | updated_at=1777910601.2640102
- [2026-05-05 00:03:24] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:03:24] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:03:24] operator / voice_transcript_final / voice: unk standby go it no unk
  meta: kind=final | timestamp=1777910604.8264914 | source=final | frequency_hz=260.0 | rms=412 | updated_at=1777910601.2640102
- [2026-05-05 00:03:24] operator / voice_command / voice: unk standby go it no unk
  meta: normalized=True
- [2026-05-05 00:03:24] operator / voice_transcript_partial / voice: never
  meta: kind=partial | timestamp=1777910604.8340087 | source=vosk | frequency_hz=348.0 | rms=289 | updated_at=1777910604.8264914
- [2026-05-05 00:03:24] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777910604.8440235 | source=vosk | frequency_hz=328.4 | rms=305 | updated_at=1777910604.8340087
- [2026-05-05 00:03:25] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777910605.093076 | source=final | frequency_hz=328.4 | rms=305 | updated_at=1777910604.8340087
- [2026-05-05 00:03:26] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:03:26] operator / voice_transcript_partial / voice: that the
  meta: kind=partial | timestamp=1777910606.7030523 | source=vosk | frequency_hz=328.4 | rms=305 | updated_at=1777910604.8340087
- [2026-05-05 00:03:26] operator / voice_transcript_partial / voice: that the app that
  meta: kind=partial | timestamp=1777910606.9152517 | source=vosk | frequency_hz=328.4 | rms=305 | updated_at=1777910604.8340087
- [2026-05-05 00:03:27] operator / voice_transcript_partial / voice: that the app that delay
  meta: kind=partial | timestamp=1777910607.1877236 | source=vosk | frequency_hz=328.4 | rms=305 | updated_at=1777910604.8340087
- [2026-05-05 00:03:27] operator / voice_transcript_partial / voice: that the app that diagnostics
  meta: kind=partial | timestamp=1777910607.4045954 | source=vosk | frequency_hz=328.4 | rms=305 | updated_at=1777910604.8340087
- [2026-05-05 00:03:27] operator / voice_transcript_final / voice: that the app that do unk
  meta: kind=final | timestamp=1777910607.9320104 | source=final | frequency_hz=328.4 | rms=305 | updated_at=1777910604.8340087
- [2026-05-05 00:03:28] operator / voice_command / voice: that the app that do unk
  meta: normalized=True
- [2026-05-05 00:03:28] assistant / assistant_prompt / text: Assistant request queued: assistant request about that the app that do unk (position 5).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:03:28] operator / voice_transcript_partial / voice: commands
  meta: kind=partial | timestamp=1777910608.406153 | source=vosk | frequency_hz=328.4 | rms=305 | updated_at=1777910604.8340087
- [2026-05-05 00:03:29] operator / voice_transcript_partial / voice: commands aileen repeat
  meta: kind=partial | timestamp=1777910609.404999 | source=vosk | frequency_hz=328.4 | rms=305 | updated_at=1777910604.8340087
- [2026-05-05 00:03:30] operator / voice_transcript_final / voice: commands repeat
  meta: kind=final | timestamp=1777910610.955336 | source=final | frequency_hz=368.0 | rms=290 | updated_at=1777910610.1583788
- [2026-05-05 00:03:31] operator / voice_command / voice: commands repeat
  meta: normalized=True
- [2026-05-05 00:03:31] assistant / assistant_prompt / text: Assistant request queued: assistant request about commands repeat (position 6).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:03:32] assistant / spoken_confirmation / voice: I am still finishing assistant request about repeat. I queued your assistant request about commands repeat. It is number 6 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:03:32] assistant / spoken_confirmation / voice: I am still finishing assistant request about repeat. I queued your assistant request about that the app that do unk. It is number 5 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:03:32] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777910612.9839036 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:33] operator / voice_transcript_partial / voice: say lion
  meta: kind=partial | timestamp=1777910613.2082245 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:33] operator / voice_transcript_partial / voice: sentry elliot
  meta: kind=partial | timestamp=1777910613.5292652 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:33] operator / voice_transcript_partial / voice: sentry elliot no
  meta: kind=partial | timestamp=1777910613.7223008 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:34] operator / voice_transcript_partial / voice: sentry elliot no app to com
  meta: kind=partial | timestamp=1777910614.2061377 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:34] operator / voice_transcript_partial / voice: sentry elliot no app to com cancel
  meta: kind=partial | timestamp=1777910614.7057736 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:34] operator / voice_transcript_partial / voice: sentry elliot no app to com again brightness
  meta: kind=partial | timestamp=1777910614.954024 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:35] operator / voice_transcript_final / voice: sentry no app to com again brightness
  meta: kind=final | timestamp=1777910615.7194037 | source=final | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:35] operator / voice_command / voice: sentry no app to com again brightness
  meta: normalized=True
- [2026-05-05 00:03:36] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777910616.2037327 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:36] operator / voice_transcript_partial / voice: current change
  meta: kind=partial | timestamp=1777910616.457867 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:37] operator / voice_transcript_partial / voice: current change theme
  meta: kind=partial | timestamp=1777910617.4569435 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:37] operator / voice_transcript_partial / voice: current change theme to com
  meta: kind=partial | timestamp=1777910617.7088559 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:37] operator / voice_transcript_partial / voice: current change theme to com rest
  meta: kind=partial | timestamp=1777910617.956941 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:38] operator / voice_transcript_partial / voice: current change theme to com rest abort
  meta: kind=partial | timestamp=1777910618.2039845 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:38] operator / voice_transcript_partial / voice: current change theme to com rest app repeat
  meta: kind=partial | timestamp=1777910618.4563475 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:38] operator / voice_transcript_partial / voice: current change theme to com rest app repeat it
  meta: kind=partial | timestamp=1777910618.7179391 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:38] operator / voice_transcript_partial / voice: current change theme to com rest app repeat change
  meta: kind=partial | timestamp=1777910618.9540873 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:39] operator / voice_transcript_partial / voice: current change theme to com rest app repeat change yourself
  meta: kind=partial | timestamp=1777910619.2082534 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:39] operator / voice_transcript_partial / voice: current change theme to com rest app repeat change check status
  meta: kind=partial | timestamp=1777910619.4553542 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:39] operator / voice_transcript_partial / voice: current change theme to com rest app repeat change check sentry
  meta: kind=partial | timestamp=1777910619.7044034 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:39] operator / voice_transcript_partial / voice: current change theme to com rest app repeat change check sensitivity
  meta: kind=partial | timestamp=1777910619.9581306 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:40] operator / voice_transcript_partial / voice: current change theme to com rest app repeat change check sentry decrease
  meta: kind=partial | timestamp=1777910620.459877 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:40] operator / voice_transcript_partial / voice: current change theme to com rest app repeat change check sentry decrease abort current
  meta: kind=partial | timestamp=1777910620.9562004 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:41] operator / voice_transcript_partial / voice: current change theme to com rest app repeat change check sentry decrease abort commands
  meta: kind=partial | timestamp=1777910621.2042785 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:41] operator / voice_transcript_partial / voice: current change theme to com rest app repeat change check sentry decrease abort commands repeat
  meta: kind=partial | timestamp=1777910621.7078488 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:42] operator / voice_transcript_partial / voice: current change theme to com rest app repeat change check sentry decrease abort commands repeat it
  meta: kind=partial | timestamp=1777910622.205413 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:42] operator / voice_transcript_partial / voice: current change theme to com rest app repeat change check sentry decrease abort commands repeat it no
  meta: kind=partial | timestamp=1777910622.706357 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:42] operator / voice_transcript_final / voice: change theme
  meta: kind=final | timestamp=1777910622.9568784 | source=final | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:43] operator / voice_command / voice: change theme
  meta: normalized=True
- [2026-05-05 00:03:43] operator / voice_transcript_partial / voice: in last
  meta: kind=partial | timestamp=1777910623.458472 | source=vosk | frequency_hz=302.4 | rms=303 | updated_at=1777910612.1983232
- [2026-05-05 00:03:43] operator / voice_transcript_partial / voice: in last priority
  meta: kind=partial | timestamp=1777910623.9545782 | source=vosk | frequency_hz=288.0 | rms=310 | updated_at=1777910623.6977155
- [2026-05-05 00:03:44] operator / voice_transcript_partial / voice: in last brightness
  meta: kind=partial | timestamp=1777910624.2044346 | source=vosk | frequency_hz=288.0 | rms=310 | updated_at=1777910623.6977155
- [2026-05-05 00:03:45] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:03:45] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:03:45] operator / voice_transcript_final / voice: in last brightness
  meta: kind=final | timestamp=1777910625.0426886 | source=final | frequency_hz=288.0 | rms=310 | updated_at=1777910623.6977155
- [2026-05-05 00:03:45] operator / voice_command / voice: in last brightness
  meta: normalized=True
- [2026-05-05 00:03:45] operator / voice_transcript_partial / voice: brightness
  meta: kind=partial | timestamp=1777910625.596189 | source=vosk | frequency_hz=323.0 | rms=371 | updated_at=1777910625.0441918
- [2026-05-05 00:03:45] operator / voice_transcript_partial / voice: priority
  meta: kind=partial | timestamp=1777910625.8377972 | source=vosk | frequency_hz=323.0 | rms=371 | updated_at=1777910625.0441918
- [2026-05-05 00:03:46] operator / voice_transcript_partial / voice: priority go
  meta: kind=partial | timestamp=1777910626.08753 | source=vosk | frequency_hz=323.0 | rms=371 | updated_at=1777910625.0441918
- [2026-05-05 00:03:46] operator / voice_transcript_partial / voice: priority go lion
  meta: kind=partial | timestamp=1777910626.5849535 | source=vosk | frequency_hz=323.0 | rms=371 | updated_at=1777910625.0441918
- [2026-05-05 00:03:47] operator / voice_transcript_final / voice: priority go delay
  meta: kind=final | timestamp=1777910627.315684 | source=final | frequency_hz=271.3 | rms=308 | updated_at=1777910627.3076625
- [2026-05-05 00:03:47] operator / voice_command / voice: priority go delay
  meta: normalized=True
- [2026-05-05 00:03:48] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:03:48] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:03:53] operator / voice_transcript_partial / voice: strict
  meta: kind=partial | timestamp=1777910633.9667804 | source=vosk
- [2026-05-05 00:03:55] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777910635.7177093 | source=vosk | frequency_hz=289.2 | rms=334 | updated_at=1777910635.2075825
- [2026-05-05 00:03:56] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777910636.7198794 | source=vosk | frequency_hz=289.2 | rms=334 | updated_at=1777910635.2075825
- [2026-05-05 00:03:56] operator / voice_transcript_final / voice: sentry
  meta: kind=final | timestamp=1777910636.9678838 | source=final | frequency_hz=289.2 | rms=334 | updated_at=1777910635.2075825
- [2026-05-05 00:03:57] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777910637.2157922 | source=vosk | frequency_hz=289.2 | rms=334 | updated_at=1777910635.2075825
- [2026-05-05 00:03:57] operator / voice_transcript_final / voice: tracking
  meta: kind=final | timestamp=1777910637.9670954 | source=final | frequency_hz=289.2 | rms=334 | updated_at=1777910635.2075825
- [2026-05-05 00:04:10] operator / voice_transcript_partial / voice: delay
  meta: kind=partial | timestamp=1777910650.0805614 | source=vosk | frequency_hz=339.2 | rms=332 | updated_at=1777910648.074719
- [2026-05-05 00:04:10] operator / voice_transcript_partial / voice: to com
  meta: kind=partial | timestamp=1777910650.579837 | source=vosk | frequency_hz=339.2 | rms=332 | updated_at=1777910648.074719
- [2026-05-05 00:04:10] operator / voice_transcript_final / voice: delay
  meta: kind=final | timestamp=1777910650.832937 | source=final | frequency_hz=339.2 | rms=332 | updated_at=1777910648.074719
- [2026-05-05 00:04:11] operator / voice_transcript_partial / voice: diagnostics
  meta: kind=partial | timestamp=1777910651.0800743 | source=vosk | frequency_hz=402.0 | rms=329 | updated_at=1777910651.0735664
- [2026-05-05 00:04:12] operator / voice_transcript_final / voice: delay
  meta: kind=final | timestamp=1777910652.4129455 | source=final | frequency_hz=315.1 | rms=317 | updated_at=1777910651.5771937
- [2026-05-05 00:04:13] operator / voice_transcript_partial / voice: home
  meta: kind=partial | timestamp=1777910653.6324415 | source=vosk | frequency_hz=302.8 | rms=317 | updated_at=1777910652.413976
- [2026-05-05 00:04:13] operator / voice_transcript_final / voice: home
  meta: kind=final | timestamp=1777910653.647125 | source=final | frequency_hz=265.4 | rms=882 | updated_at=1777910653.6324415
- [2026-05-05 00:04:15] operator / voice_transcript_partial / voice: serial
  meta: kind=partial | timestamp=1777910655.4045603 | source=vosk | frequency_hz=234.8 | rms=333 | updated_at=1777910654.6371334
- [2026-05-05 00:04:15] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777910655.639842 | source=vosk | frequency_hz=234.8 | rms=333 | updated_at=1777910654.6371334
- [2026-05-05 00:04:16] operator / voice_transcript_partial / voice: serial less strict
  meta: kind=partial | timestamp=1777910656.14048 | source=vosk | frequency_hz=234.8 | rms=333 | updated_at=1777910654.6371334
- [2026-05-05 00:04:16] operator / voice_transcript_partial / voice: say all tasks
  meta: kind=partial | timestamp=1777910656.6421664 | source=vosk | frequency_hz=396.0 | rms=351 | updated_at=1777910656.6331618
- [2026-05-05 00:04:16] operator / voice_transcript_partial / voice: say all tasks in
  meta: kind=partial | timestamp=1777910656.8949425 | source=vosk | frequency_hz=396.0 | rms=351 | updated_at=1777910656.6331618
- [2026-05-05 00:04:17] operator / voice_transcript_partial / voice: say all tasks in queue
  meta: kind=partial | timestamp=1777910657.3907876 | source=vosk | frequency_hz=396.0 | rms=351 | updated_at=1777910656.6331618
- [2026-05-05 00:04:17] operator / voice_transcript_partial / voice: say all tasks in
  meta: kind=partial | timestamp=1777910657.641185 | source=vosk | frequency_hz=393.2 | rms=349 | updated_at=1777910657.6326578
- [2026-05-05 00:04:17] operator / voice_transcript_partial / voice: say all tasks in alien
  meta: kind=partial | timestamp=1777910657.892296 | source=vosk | frequency_hz=393.2 | rms=349 | updated_at=1777910657.6326578
- [2026-05-05 00:04:18] operator / voice_transcript_partial / voice: say all tasks in be more
  meta: kind=partial | timestamp=1777910658.1422374 | source=vosk | frequency_hz=393.2 | rms=349 | updated_at=1777910657.6326578
- [2026-05-05 00:04:18] operator / voice_transcript_partial / voice: say all tasks in alien abort elliot
  meta: kind=partial | timestamp=1777910658.4112773 | source=vosk | frequency_hz=383.0 | rms=364 | updated_at=1777910658.3914518
- [2026-05-05 00:04:18] operator / voice_transcript_partial / voice: say all tasks in alien abort elliot again
  meta: kind=partial | timestamp=1777910658.6440427 | source=vosk | frequency_hz=379.1 | rms=367 | updated_at=1777910658.632531
- [2026-05-05 00:04:18] operator / voice_transcript_partial / voice: say all tasks in alien go
  meta: kind=partial | timestamp=1777910658.8904035 | source=vosk | frequency_hz=379.1 | rms=367 | updated_at=1777910658.632531
- [2026-05-05 00:04:19] operator / voice_transcript_partial / voice: say all tasks in alien go boards
  meta: kind=partial | timestamp=1777910659.1412683 | source=vosk | frequency_hz=379.1 | rms=367 | updated_at=1777910658.632531
- [2026-05-05 00:04:19] operator / voice_transcript_partial / voice: say all tasks in alien who are guarding
  meta: kind=partial | timestamp=1777910659.3932743 | source=vosk | frequency_hz=379.1 | rms=367 | updated_at=1777910658.632531
- [2026-05-05 00:04:19] operator / voice_transcript_partial / voice: say all tasks in alien who are guarding mode
  meta: kind=partial | timestamp=1777910659.6390004 | source=vosk | frequency_hz=379.1 | rms=367 | updated_at=1777910658.632531
- [2026-05-05 00:04:19] operator / voice_transcript_partial / voice: say all tasks in alien who are guarding and enable
  meta: kind=partial | timestamp=1777910659.8923914 | source=vosk | frequency_hz=379.1 | rms=367 | updated_at=1777910658.632531
- [2026-05-05 00:04:20] operator / voice_transcript_final / voice: say all tasks in abort elliot go board guarding and
  meta: kind=final | timestamp=1777910660.6482196 | source=final | frequency_hz=261.2 | rms=318 | updated_at=1777910660.6331835
- [2026-05-05 00:04:20] operator / voice_command / voice: say all tasks in abort elliot go board guarding and
  meta: normalized=True
- [2026-05-05 00:04:22] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:04:23] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777910663.7124672 | source=vosk | frequency_hz=284.4 | rms=323 | updated_at=1777910663.0550416
- [2026-05-05 00:04:23] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:04:23] operator / voice_transcript_partial / voice: e the app
  meta: kind=partial | timestamp=1777910663.9673996 | source=vosk | frequency_hz=284.4 | rms=323 | updated_at=1777910663.0550416
- [2026-05-05 00:04:24] operator / voice_transcript_partial / voice: e the app to
  meta: kind=partial | timestamp=1777910664.212334 | source=vosk | frequency_hz=284.4 | rms=323 | updated_at=1777910663.0550416
- [2026-05-05 00:04:24] operator / voice_transcript_partial / voice: e the smart
  meta: kind=partial | timestamp=1777910664.4629052 | source=vosk | frequency_hz=284.4 | rms=323 | updated_at=1777910663.0550416
- [2026-05-05 00:04:36] operator / voice_transcript_final / voice: mind
  meta: kind=final | timestamp=1777910676.9539042 | source=final | frequency_hz=383.7 | rms=291 | updated_at=1777910676.9223528
- [2026-05-05 00:04:38] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777910678.1785817 | source=vosk | frequency_hz=348.8 | rms=313 | updated_at=1777910677.672127
- [2026-05-05 00:04:42] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777910682.1844194 | source=vosk | frequency_hz=299.4 | rms=312 | updated_at=1777910681.421753
- [2026-05-05 00:04:42] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777910682.44043 | source=vosk | frequency_hz=299.4 | rms=312 | updated_at=1777910681.421753
- [2026-05-05 00:04:42] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777910682.6919467 | source=final | frequency_hz=299.4 | rms=312 | updated_at=1777910681.421753
- [2026-05-05 00:04:46] operator / voice_transcript_partial / voice: com
  meta: kind=partial | timestamp=1777910686.189658 | source=vosk | frequency_hz=324.4 | rms=508 | updated_at=1777910685.6729708
- [2026-05-05 00:04:46] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910686.4352596 | source=vosk | frequency_hz=324.4 | rms=508 | updated_at=1777910685.6729708
- [2026-05-05 00:04:47] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777910687.9290996 | source=final | frequency_hz=276.2 | rms=310 | updated_at=1777910687.922087
- [2026-05-05 00:04:55] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777910695.9671743 | source=vosk | frequency_hz=352.0 | rms=862 | updated_at=1777910692.6998622
- [2026-05-05 00:04:56] operator / voice_transcript_partial / voice: smart sentry you
  meta: kind=partial | timestamp=1777910696.4617121 | source=vosk | frequency_hz=352.0 | rms=862 | updated_at=1777910692.6998622
- [2026-05-05 00:04:56] operator / voice_transcript_partial / voice: smart sentry you and enable
  meta: kind=partial | timestamp=1777910696.707707 | source=vosk | frequency_hz=352.0 | rms=862 | updated_at=1777910692.6998622
- [2026-05-05 00:04:56] operator / voice_transcript_partial / voice: smart sentry you analyze
  meta: kind=partial | timestamp=1777910696.9577372 | source=vosk | frequency_hz=352.0 | rms=862 | updated_at=1777910692.6998622
- [2026-05-05 00:04:57] operator / voice_transcript_partial / voice: smart sentry you analyze mode
  meta: kind=partial | timestamp=1777910697.2068126 | source=vosk | frequency_hz=352.0 | rms=862 | updated_at=1777910692.6998622
- [2026-05-05 00:04:57] operator / voice_transcript_partial / voice: smart sentry you analyze on
  meta: kind=partial | timestamp=1777910697.458927 | source=vosk | frequency_hz=352.0 | rms=862 | updated_at=1777910692.6998622
- [2026-05-05 00:04:57] operator / voice_transcript_partial / voice: smart sentry you analyze mode resume last
  meta: kind=partial | timestamp=1777910697.7118447 | source=vosk | frequency_hz=332.0 | rms=324 | updated_at=1777910697.6998198
- [2026-05-05 00:04:57] operator / voice_transcript_partial / voice: smart sentry you analyze on lion
  meta: kind=partial | timestamp=1777910697.958578 | source=vosk | frequency_hz=351.6 | rms=364 | updated_at=1777910697.9500618
- [2026-05-05 00:04:58] operator / voice_transcript_partial / voice: smart sentry you analyze on lion go
  meta: kind=partial | timestamp=1777910698.4585156 | source=vosk | frequency_hz=351.6 | rms=364 | updated_at=1777910697.9500618
- [2026-05-05 00:04:58] operator / voice_transcript_partial / voice: smart sentry you analyze on lion go status
  meta: kind=partial | timestamp=1777910698.7079234 | source=vosk | frequency_hz=351.6 | rms=364 | updated_at=1777910697.9500618
- [2026-05-05 00:04:59] operator / voice_transcript_partial / voice: smart sentry you analyze on lion go status serial
  meta: kind=partial | timestamp=1777910699.207721 | source=vosk | frequency_hz=351.6 | rms=364 | updated_at=1777910697.9500618
- [2026-05-05 00:04:59] operator / voice_transcript_partial / voice: smart sentry you analyze on lion go sensitivity resume
  meta: kind=partial | timestamp=1777910699.4563835 | source=vosk | frequency_hz=351.6 | rms=364 | updated_at=1777910697.9500618
- [2026-05-05 00:04:59] operator / voice_transcript_partial / voice: smart sentry you analyze on lion go sensitivity resume status
  meta: kind=partial | timestamp=1777910699.9607005 | source=vosk | frequency_hz=351.6 | rms=364 | updated_at=1777910697.9500618
- [2026-05-05 00:05:00] operator / voice_transcript_partial / voice: smart sentry you analyze on lion go sensitivity resume say
  meta: kind=partial | timestamp=1777910700.2062147 | source=vosk | frequency_hz=351.6 | rms=364 | updated_at=1777910697.9500618
- [2026-05-05 00:05:00] operator / voice_transcript_partial / voice: smart sentry you analyze on lion go sensitivity resume status report go
  meta: kind=partial | timestamp=1777910700.4575593 | source=vosk | frequency_hz=351.6 | rms=364 | updated_at=1777910697.9500618
- [2026-05-05 00:05:00] operator / voice_transcript_partial / voice: smart sentry you analyze on lion go sensitivity resume status report yes
  meta: kind=partial | timestamp=1777910700.7099326 | source=vosk | frequency_hz=351.6 | rms=364 | updated_at=1777910697.9500618
- [2026-05-05 00:05:01] operator / voice_transcript_final / voice: status report
  meta: kind=final | timestamp=1777910701.2109804 | source=final | frequency_hz=271.2 | rms=311 | updated_at=1777910701.199733
- [2026-05-05 00:05:01] operator / voice_transcript_partial / voice: boards
  meta: kind=partial | timestamp=1777910701.9686656 | source=vosk | frequency_hz=271.2 | rms=311 | updated_at=1777910701.199733
- [2026-05-05 00:05:02] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777910702.2170863 | source=vosk | frequency_hz=271.2 | rms=311 | updated_at=1777910701.199733
- [2026-05-05 00:05:02] operator / voice_transcript_partial / voice: same but
  meta: kind=partial | timestamp=1777910702.4858181 | source=vosk | frequency_hz=271.2 | rms=311 | updated_at=1777910701.199733
- [2026-05-05 00:05:02] operator / voice_transcript_partial / voice: same but queued
  meta: kind=partial | timestamp=1777910702.710086 | source=vosk | frequency_hz=348.0 | rms=334 | updated_at=1777910702.7000666
- [2026-05-05 00:05:03] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:05:02] operator / voice_transcript_partial / voice: same but queued tasks
  meta: kind=partial | timestamp=1777910702.9566848 | source=vosk | frequency_hz=352.2 | rms=320 | updated_at=1777910702.9500241
- [2026-05-05 00:05:03] operator / voice_transcript_final / voice: same but queued
  meta: kind=final | timestamp=1777910703.707829 | source=final | frequency_hz=261.8 | rms=322 | updated_at=1777910703.700316
- [2026-05-05 00:05:08] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777910708.6083589 | source=vosk | frequency_hz=320.1 | rms=345 | updated_at=1777910708.09646
- [2026-05-05 00:05:08] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777910708.8732429 | source=vosk | frequency_hz=350.9 | rms=379 | updated_at=1777910708.8469594
- [2026-05-05 00:05:09] operator / voice_transcript_partial / voice: guarding
  meta: kind=partial | timestamp=1777910709.104879 | source=vosk | frequency_hz=361.8 | rms=363 | updated_at=1777910709.0973437
- [2026-05-05 00:05:09] operator / voice_transcript_partial / voice: guarding mode
  meta: kind=partial | timestamp=1777910709.3541963 | source=vosk | frequency_hz=361.2 | rms=354 | updated_at=1777910709.3471816
- [2026-05-05 00:05:09] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777910709.6079304 | source=vosk | frequency_hz=365.7 | rms=328 | updated_at=1777910709.5984168
- [2026-05-05 00:05:09] operator / voice_transcript_final / voice: go
  meta: kind=final | timestamp=1777910709.8570356 | source=final | frequency_hz=352.5 | rms=323 | updated_at=1777910709.8480272
- [2026-05-05 00:05:12] operator / voice_transcript_partial / voice: increase
  meta: kind=partial | timestamp=1777910712.3584123 | source=vosk | frequency_hz=318.4 | rms=335 | updated_at=1777910712.3483186
- [2026-05-05 00:05:14] operator / voice_transcript_partial / voice: that identify
  meta: kind=partial | timestamp=1777910714.374313 | source=vosk | frequency_hz=351.3 | rms=304 | updated_at=1777910713.0979195
- [2026-05-05 00:05:14] operator / voice_transcript_partial / voice: that a lion e
  meta: kind=partial | timestamp=1777910714.8550642 | source=vosk | frequency_hz=351.3 | rms=304 | updated_at=1777910713.0979195
- [2026-05-05 00:05:15] operator / voice_transcript_partial / voice: that identify the
  meta: kind=partial | timestamp=1777910715.1063693 | source=vosk | frequency_hz=351.3 | rms=304 | updated_at=1777910713.0979195
- [2026-05-05 00:05:24] operator / voice_transcript_partial / voice: same
  meta: kind=partial | timestamp=1777910724.2579277 | source=vosk | frequency_hz=269.2 | rms=333 | updated_at=1777910724.2517605
- [2026-05-05 00:05:24] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777910724.5015867 | source=vosk | frequency_hz=288.4 | rms=318 | updated_at=1777910724.4955757
- [2026-05-05 00:05:25] operator / voice_transcript_final / voice: same
  meta: kind=final | timestamp=1777910725.0018792 | source=final | frequency_hz=318.2 | rms=306 | updated_at=1777910724.9946804
- [2026-05-05 00:05:29] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777910729.7048435 | source=vosk | frequency_hz=357.6 | rms=315 | updated_at=1777910727.6478949
- [2026-05-05 00:05:29] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777910729.9541724 | source=vosk | frequency_hz=406.0 | rms=346 | updated_at=1777910729.9476616
- [2026-05-05 00:05:30] operator / voice_transcript_partial / voice: smart you
  meta: kind=partial | timestamp=1777910730.2058866 | source=vosk | frequency_hz=406.0 | rms=346 | updated_at=1777910729.9476616
- [2026-05-05 00:05:30] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777910730.4542868 | source=vosk | frequency_hz=406.0 | rms=346 | updated_at=1777910729.9476616
- [2026-05-05 00:05:31] operator / voice_transcript_partial / voice: lion decrease brightness
  meta: kind=partial | timestamp=1777910731.2065668 | source=vosk | frequency_hz=406.0 | rms=346 | updated_at=1777910729.9476616
- [2026-05-05 00:05:31] operator / voice_transcript_partial / voice: lion check the theme
  meta: kind=partial | timestamp=1777910731.4553006 | source=vosk | frequency_hz=406.0 | rms=346 | updated_at=1777910729.9476616
- [2026-05-05 00:05:31] operator / voice_transcript_final / voice: smart you check the theme
  meta: kind=final | timestamp=1777910731.9759972 | source=final | frequency_hz=306.0 | rms=321 | updated_at=1777910731.9556894
- [2026-05-05 00:05:32] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777910732.4538884 | source=vosk | frequency_hz=306.0 | rms=321 | updated_at=1777910731.9556894
- [2026-05-05 00:05:35] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777910735.4773607 | source=vosk | frequency_hz=416.0 | rms=512 | updated_at=1777910734.970717
- [2026-05-05 00:05:36] operator / voice_transcript_partial / voice: go do
  meta: kind=partial | timestamp=1777910736.2283072 | source=vosk | frequency_hz=416.0 | rms=512 | updated_at=1777910734.970717
- [2026-05-05 00:05:36] operator / voice_transcript_partial / voice: go delay
  meta: kind=partial | timestamp=1777910736.4778364 | source=vosk | frequency_hz=272.0 | rms=320 | updated_at=1777910736.47082
- [2026-05-05 00:05:37] operator / voice_transcript_final / voice: go delay
  meta: kind=final | timestamp=1777910737.2281938 | source=final | frequency_hz=250.6 | rms=316 | updated_at=1777910737.2201648
- [2026-05-05 00:05:38] operator / voice_transcript_partial / voice: again
  meta: kind=partial | timestamp=1777910738.2285147 | source=vosk | frequency_hz=256.9 | rms=401 | updated_at=1777910737.720682
- [2026-05-05 00:05:38] operator / voice_transcript_partial / voice: a decrease
  meta: kind=partial | timestamp=1777910738.4775007 | source=vosk | frequency_hz=256.9 | rms=401 | updated_at=1777910737.720682
- [2026-05-05 00:05:38] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777910738.9845679 | source=vosk | frequency_hz=276.2 | rms=327 | updated_at=1777910738.9700272
- [2026-05-05 00:05:39] operator / voice_transcript_final / voice: last
  meta: kind=final | timestamp=1777910739.4831724 | source=final | frequency_hz=309.7 | rms=313 | updated_at=1777910739.4706514
- [2026-05-05 00:05:40] operator / voice_transcript_partial / voice: again
  meta: kind=partial | timestamp=1777910740.2264555 | source=vosk | frequency_hz=346.9 | rms=315 | updated_at=1777910739.7204883
- [2026-05-05 00:05:40] operator / voice_transcript_partial / voice: again report
  meta: kind=partial | timestamp=1777910740.9772356 | source=vosk | frequency_hz=346.9 | rms=315 | updated_at=1777910739.7204883
- [2026-05-05 00:05:41] operator / voice_transcript_partial / voice: again report delay
  meta: kind=partial | timestamp=1777910741.4770317 | source=vosk | frequency_hz=346.9 | rms=315 | updated_at=1777910739.7204883
- [2026-05-05 00:05:41] operator / voice_transcript_partial / voice: again report the last
  meta: kind=partial | timestamp=1777910741.7282703 | source=vosk | frequency_hz=346.9 | rms=315 | updated_at=1777910739.7204883
- [2026-05-05 00:05:41] operator / voice_transcript_partial / voice: again report the last and
  meta: kind=partial | timestamp=1777910741.979053 | source=vosk | frequency_hz=346.9 | rms=315 | updated_at=1777910739.7204883
- [2026-05-05 00:05:42] operator / voice_transcript_partial / voice: again report the last the never
  meta: kind=partial | timestamp=1777910742.24692 | source=vosk | frequency_hz=346.9 | rms=315 | updated_at=1777910739.7204883
- [2026-05-05 00:05:42] operator / voice_transcript_partial / voice: again report the last the no the smart
  meta: kind=partial | timestamp=1777910742.4808884 | source=vosk | frequency_hz=346.9 | rms=315 | updated_at=1777910739.7204883
- [2026-05-05 00:05:43] operator / voice_transcript_partial / voice: again report the last the no the status report
  meta: kind=partial | timestamp=1777910743.7266984 | source=vosk | frequency_hz=346.9 | rms=315 | updated_at=1777910739.7204883
- [2026-05-05 00:05:43] operator / voice_transcript_partial / voice: again report the last the no the status guarding
  meta: kind=partial | timestamp=1777910743.9782522 | source=vosk | frequency_hz=346.9 | rms=315 | updated_at=1777910739.7204883
- [2026-05-05 00:05:44] operator / voice_transcript_partial / voice: again report the last the no the status brightness
  meta: kind=partial | timestamp=1777910744.228467 | source=vosk | frequency_hz=272.0 | rms=313 | updated_at=1777910744.220658
- [2026-05-05 00:05:44] operator / voice_transcript_final / voice: again report the last the no the status brightness
  meta: kind=final | timestamp=1777910744.9827287 | source=final | frequency_hz=321.9 | rms=314 | updated_at=1777910744.9706998
- [2026-05-05 00:05:47] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777910747.7262838 | source=vosk | frequency_hz=349.4 | rms=308 | updated_at=1777910746.9708834
- [2026-05-05 00:05:47] operator / voice_transcript_partial / voice: a port
  meta: kind=partial | timestamp=1777910747.9782262 | source=vosk | frequency_hz=349.4 | rms=308 | updated_at=1777910746.9708834
- [2026-05-05 00:05:48] operator / voice_transcript_final / voice: a unk
  meta: kind=final | timestamp=1777910748.479045 | source=final | frequency_hz=349.4 | rms=308 | updated_at=1777910746.9708834
- [2026-05-05 00:05:49] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777910749.9800038 | source=vosk | frequency_hz=252.0 | rms=313 | updated_at=1777910749.2210405
- [2026-05-05 00:05:50] operator / voice_transcript_partial / voice: do you do
  meta: kind=partial | timestamp=1777910750.4827583 | source=vosk | frequency_hz=252.0 | rms=313 | updated_at=1777910749.2210405
- [2026-05-05 00:05:50] operator / voice_transcript_partial / voice: decrease brightness
  meta: kind=partial | timestamp=1777910750.9780464 | source=vosk | frequency_hz=252.0 | rms=313 | updated_at=1777910749.2210405
- [2026-05-05 00:05:51] operator / voice_transcript_partial / voice: do you do run do
  meta: kind=partial | timestamp=1777910751.4829626 | source=vosk | frequency_hz=252.0 | rms=313 | updated_at=1777910749.2210405
- [2026-05-05 00:05:51] operator / voice_transcript_final / voice: do you do run do
  meta: kind=final | timestamp=1777910751.7288089 | source=final | frequency_hz=324.0 | rms=325 | updated_at=1777910751.7211275
- [2026-05-05 00:05:57] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777910757.2276247 | source=vosk | frequency_hz=374.0 | rms=330 | updated_at=1777910756.971315
- [2026-05-05 00:05:58] operator / voice_transcript_final / voice: do do
  meta: kind=final | timestamp=1777910758.8237636 | source=final | frequency_hz=335.9 | rms=321 | updated_at=1777910757.9729195
- [2026-05-05 00:05:58] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777910758.8463948 | source=vosk | frequency_hz=335.9 | rms=321 | updated_at=1777910757.9729195
- [2026-05-05 00:05:59] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777910759.3410757 | source=vosk | frequency_hz=308.6 | rms=254 | updated_at=1777910759.0849156
- [2026-05-05 00:06:00] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777910760.0951061 | source=final | frequency_hz=293.0 | rms=319 | updated_at=1777910760.0850813
- [2026-05-05 00:06:06] operator / voice_transcript_partial / voice: but faster
  meta: kind=partial | timestamp=1777910766.3472989 | source=vosk | frequency_hz=291.3 | rms=326 | updated_at=1777910765.3349283
- [2026-05-05 00:06:06] operator / voice_transcript_partial / voice: but but
  meta: kind=partial | timestamp=1777910766.5911057 | source=vosk | frequency_hz=291.3 | rms=326 | updated_at=1777910765.3349283
- [2026-05-05 00:06:06] operator / voice_transcript_final / voice: in but unk
  meta: kind=final | timestamp=1777910766.8463938 | source=final | frequency_hz=291.3 | rms=326 | updated_at=1777910765.3349283
- [2026-05-05 00:06:07] operator / voice_transcript_partial / voice: the last
  meta: kind=partial | timestamp=1777910767.0914552 | source=vosk | frequency_hz=291.3 | rms=326 | updated_at=1777910765.3349283
- [2026-05-05 00:06:08] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:06:09] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777910769.8488214 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:10] operator / voice_transcript_partial / voice: e decrease
  meta: kind=partial | timestamp=1777910770.0914893 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:10] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777910770.6344006 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:10] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777910770.6429098 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:10] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:06:11] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777910771.11655 | source=final | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:11] operator / voice_command / voice: no
  meta: normalized=True
- [2026-05-05 00:06:11] assistant / assistant_prompt / text: Assistant request queued: assistant request about no (position 4).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:06:11] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777910771.3413148 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:12] operator / voice_transcript_partial / voice: the last
  meta: kind=partial | timestamp=1777910772.0931008 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:13] operator / voice_transcript_final / voice: the last
  meta: kind=final | timestamp=1777910773.0704772 | source=final | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:13] operator / voice_command / voice: the last
  meta: normalized=True
- [2026-05-05 00:06:13] assistant / assistant_prompt / text: Assistant request queued: assistant request about the last (position 5).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:06:13] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777910773.3765705 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:14] operator / voice_transcript_partial / voice: mind
  meta: kind=partial | timestamp=1777910774.0930655 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:14] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910774.3832753 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:15] operator / voice_transcript_partial / voice: [unk] elian
  meta: kind=partial | timestamp=1777910775.0923965 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:15] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:06:15] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910775.3498118 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:16] assistant / spoken_confirmation / voice: I am still finishing assistant request about pause current it home the go be a do. I queued your assistant request about the last. It is number 5 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:06:16] assistant / spoken_confirmation / voice: I am still finishing assistant request about pause current it home the go be a do. I queued your assistant request about no. It is number 4 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:06:17] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777910777.918168 | source=final | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:18] operator / voice_command / voice: unk
  meta: normalized=True
- [2026-05-05 00:06:18] assistant / assistant_prompt / text: Assistant request queued: assistant request about unk (position 6).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:06:18] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777910778.0966027 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:19] operator / voice_transcript_partial / voice: lion connect
  meta: kind=partial | timestamp=1777910779.4655182 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:19] operator / voice_transcript_partial / voice: lion be more strict
  meta: kind=partial | timestamp=1777910779.7347052 | source=vosk | frequency_hz=389.9 | rms=678 | updated_at=1777910769.0928657
- [2026-05-05 00:06:20] operator / voice_transcript_final / voice: lion go mode
  meta: kind=final | timestamp=1777910780.32186 | source=final | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:20] operator / voice_command / voice: lion go mode
  meta: normalized=True
- [2026-05-05 00:06:20] assistant / assistant_prompt / text: Assistant request queued: assistant request about lion go mode (position 7).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:06:20] operator / voice_transcript_partial / voice: but elian
  meta: kind=partial | timestamp=1777910780.7565773 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:21] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:06:21] operator / voice_transcript_partial / voice: but faster
  meta: kind=partial | timestamp=1777910781.2163723 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:21] operator / voice_transcript_partial / voice: but guarding mode
  meta: kind=partial | timestamp=1777910781.4667158 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:21] operator / voice_transcript_partial / voice: but elian abort
  meta: kind=partial | timestamp=1777910781.7137 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:22] operator / voice_transcript_partial / voice: but elian abort the
  meta: kind=partial | timestamp=1777910782.2284906 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:22] operator / voice_transcript_partial / voice: but elian abort the board
  meta: kind=partial | timestamp=1777910782.466262 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:22] operator / voice_transcript_final / voice: but abort the board
  meta: kind=final | timestamp=1777910782.7223146 | source=final | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:23] operator / voice_command / voice: but abort the board
  meta: normalized=True
- [2026-05-05 00:06:23] assistant / assistant_prompt / text: Assistant request queued: assistant request about but abort the board (position 8).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:06:24] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777910784.2318094 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:24] operator / voice_transcript_partial / voice: never mind
  meta: kind=partial | timestamp=1777910784.4828374 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:24] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910784.7337403 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:26] assistant / spoken_confirmation / voice: I am still finishing assistant request about pause current it home the go be a do. I queued your assistant request about lion go mode. It is number 7 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:06:26] assistant / spoken_confirmation / voice: I am still finishing assistant request about pause current it home the go be a do. I queued your assistant request about unk. It is number 6 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:06:26] assistant / spoken_confirmation / voice: I am still finishing assistant request about pause current it home the go be a do. I queued your assistant request about but abort the board. It is number 8 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:06:25] operator / voice_transcript_partial / voice: [unk] again
  meta: kind=partial | timestamp=1777910785.7715127 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:26] operator / voice_transcript_partial / voice: [unk] again e
  meta: kind=partial | timestamp=1777910786.5102224 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:26] operator / voice_transcript_partial / voice: [unk] again e lion
  meta: kind=partial | timestamp=1777910786.7469 | source=vosk | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:27] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:06:27] operator / voice_transcript_final / voice: unk again e no
  meta: kind=final | timestamp=1777910787.496589 | source=final | frequency_hz=362.0 | rms=229 | updated_at=1777910779.955158
- [2026-05-05 00:06:27] operator / voice_command / voice: unk again e no
  meta: normalized=True
- [2026-05-05 00:06:27] assistant / assistant_prompt / text: Assistant request queued: assistant request about unk again e no (position 9).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:06:29] assistant / spoken_confirmation / voice: I am still finishing assistant request about pause current it home the go be a do. I queued your assistant request about unk again e no. It is number 9 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:06:31] operator / voice_transcript_partial / voice: increase
  meta: kind=partial | timestamp=1777910791.7615876 | source=vosk | frequency_hz=400.0 | rms=266 | updated_at=1777910789.4860258
- [2026-05-05 00:06:32] operator / voice_transcript_partial / voice: increase you do
  meta: kind=partial | timestamp=1777910792.0047026 | source=vosk | frequency_hz=400.0 | rms=266 | updated_at=1777910789.4860258
- [2026-05-05 00:06:32] operator / voice_transcript_partial / voice: increase
  meta: kind=partial | timestamp=1777910792.2498238 | source=vosk | frequency_hz=400.0 | rms=266 | updated_at=1777910789.4860258
- [2026-05-05 00:06:32] operator / voice_transcript_partial / voice: increase response
  meta: kind=partial | timestamp=1777910792.506935 | source=vosk | frequency_hz=400.0 | rms=266 | updated_at=1777910789.4860258
- [2026-05-05 00:06:32] operator / voice_transcript_partial / voice: report
  meta: kind=partial | timestamp=1777910792.746635 | source=vosk | frequency_hz=400.0 | rms=266 | updated_at=1777910789.4860258
- [2026-05-05 00:06:33] operator / voice_transcript_final / voice: increase report
  meta: kind=final | timestamp=1777910793.0368314 | source=final | frequency_hz=400.0 | rms=266 | updated_at=1777910789.4860258
- [2026-05-05 00:06:33] operator / voice_command / voice: increase report
  meta: normalized=True
- [2026-05-05 00:06:33] operator / voice_transcript_partial / voice: abort
  meta: kind=partial | timestamp=1777910793.5192504 | source=vosk | frequency_hz=400.0 | rms=266 | updated_at=1777910789.4860258
- [2026-05-05 00:06:34] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:06:36] operator / voice_transcript_partial / voice: identify
  meta: kind=partial | timestamp=1777910796.2777324 | source=vosk | frequency_hz=326.2 | rms=285 | updated_at=1777910795.7612727
- [2026-05-05 00:06:37] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777910797.2424247 | source=vosk | frequency_hz=326.2 | rms=285 | updated_at=1777910795.7612727
- [2026-05-05 00:06:37] operator / voice_transcript_final / voice: repeat it
  meta: kind=final | timestamp=1777910797.9967077 | source=final | frequency_hz=326.2 | rms=285 | updated_at=1777910795.7612727
- [2026-05-05 00:06:38] operator / voice_command / voice: repeat it
  meta: normalized=True
- [2026-05-05 00:06:38] assistant / assistant_prompt / text: Assistant request queued: assistant request about repeat it (position 10).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:06:38] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777910798.4922504 | source=vosk | frequency_hz=326.2 | rms=285 | updated_at=1777910795.7612727
- [2026-05-05 00:06:39] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777910799.494898 | source=final | frequency_hz=326.2 | rms=285 | updated_at=1777910795.7612727
- [2026-05-05 00:06:39] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:06:40] assistant / spoken_confirmation / voice: I am still finishing assistant request about pause current it home the go be a do. I queued your assistant request about repeat it. It is number 10 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:06:40] operator / voice_transcript_partial / voice: disconnect
  meta: kind=partial | timestamp=1777910800.9116824 | source=vosk | frequency_hz=326.2 | rms=285 | updated_at=1777910795.7612727
- [2026-05-05 00:06:41] operator / voice_transcript_partial / voice: disconnect queued
  meta: kind=partial | timestamp=1777910801.257846 | source=vosk | frequency_hz=326.2 | rms=285 | updated_at=1777910795.7612727
- [2026-05-05 00:06:41] operator / voice_transcript_partial / voice: disconnect current e
  meta: kind=partial | timestamp=1777910801.498512 | source=vosk | frequency_hz=326.2 | rms=285 | updated_at=1777910795.7612727
- [2026-05-05 00:06:41] operator / voice_transcript_partial / voice: disconnect current e lion
  meta: kind=partial | timestamp=1777910801.9520068 | source=vosk | frequency_hz=326.2 | rms=285 | updated_at=1777910795.7612727
- [2026-05-05 00:06:43] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:06:42] operator / voice_transcript_partial / voice: disconnect current e e
  meta: kind=partial | timestamp=1777910802.6841927 | source=vosk | frequency_hz=326.2 | rms=285 | updated_at=1777910795.7612727
- [2026-05-05 00:06:42] operator / voice_transcript_partial / voice: disconnect current e e lion
  meta: kind=partial | timestamp=1777910802.9123213 | source=vosk | frequency_hz=166.0 | rms=1203 | updated_at=1777910802.903799
- [2026-05-05 00:06:44] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:06:43] operator / voice_transcript_partial / voice: disconnect current e e the
  meta: kind=partial | timestamp=1777910803.8331285 | source=vosk | frequency_hz=163.9 | rms=367 | updated_at=1777910803.8221085
- [2026-05-05 00:06:44] operator / voice_transcript_partial / voice: disconnect current e e that
  meta: kind=partial | timestamp=1777910804.0799444 | source=vosk | frequency_hz=163.9 | rms=367 | updated_at=1777910803.8221085
- [2026-05-05 00:06:44] operator / voice_transcript_final / voice: disconnect current e e that
  meta: kind=final | timestamp=1777910804.7576187 | source=final | frequency_hz=163.9 | rms=367 | updated_at=1777910803.8221085
- [2026-05-05 00:06:45] operator / voice_command / voice: disconnect current e e that
  meta: normalized=True
- [2026-05-05 00:06:45] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777910805.890764 | source=vosk | frequency_hz=163.9 | rms=367 | updated_at=1777910803.8221085
- [2026-05-05 00:06:46] operator / voice_transcript_partial / voice: lion increase
  meta: kind=partial | timestamp=1777910806.1308193 | source=vosk | frequency_hz=163.9 | rms=367 | updated_at=1777910803.8221085
- [2026-05-05 00:06:46] operator / voice_transcript_final / voice: lion
  meta: kind=final | timestamp=1777910806.4518764 | source=final | frequency_hz=163.9 | rms=367 | updated_at=1777910803.8221085
- [2026-05-05 00:06:48] operator / voice_command / voice: lion
  meta: normalized=True
- [2026-05-05 00:06:48] assistant / assistant_prompt / text: Assistant request queued: assistant request about lion (position 11).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:06:50] assistant / spoken_confirmation / voice: I am still finishing assistant request about pause current it home the go be a do. I queued your assistant request about lion. It is number 11 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:06:50] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:06:56] operator / voice_transcript_partial / voice: behaviour
  meta: kind=partial | timestamp=1777910816.613663 | source=vosk | frequency_hz=304.0 | rms=279 | updated_at=1777910815.3440018
- [2026-05-05 00:06:56] operator / voice_transcript_partial / voice: the theme
  meta: kind=partial | timestamp=1777910816.8540268 | source=vosk | frequency_hz=304.0 | rms=279 | updated_at=1777910815.3440018
- [2026-05-05 00:06:57] operator / voice_transcript_partial / voice: the theme be
  meta: kind=partial | timestamp=1777910817.3528328 | source=vosk | frequency_hz=304.0 | rms=279 | updated_at=1777910815.3440018
- [2026-05-05 00:06:58] operator / voice_transcript_final / voice: the theme
  meta: kind=final | timestamp=1777910818.1023276 | source=final | frequency_hz=289.4 | rms=260 | updated_at=1777910818.092819
- [2026-05-05 00:07:00] operator / voice_transcript_partial / voice: strict
  meta: kind=partial | timestamp=1777910820.126602 | source=vosk | frequency_hz=318.3 | rms=283 | updated_at=1777910819.0935082
- [2026-05-05 00:07:00] operator / voice_transcript_partial / voice: strict the
  meta: kind=partial | timestamp=1777910820.6016128 | source=vosk | frequency_hz=318.3 | rms=283 | updated_at=1777910819.0935082
- [2026-05-05 00:07:00] operator / voice_transcript_partial / voice: strict disable the
  meta: kind=partial | timestamp=1777910820.85018 | source=vosk | frequency_hz=318.3 | rms=283 | updated_at=1777910819.0935082
- [2026-05-05 00:07:01] operator / voice_transcript_final / voice: that strict disable the
  meta: kind=final | timestamp=1777910821.8706791 | source=final | frequency_hz=378.0 | rms=311 | updated_at=1777910821.3436644
- [2026-05-05 00:07:04] operator / voice_transcript_partial / voice: override
  meta: kind=partial | timestamp=1777910824.8497736 | source=vosk | frequency_hz=271.7 | rms=298 | updated_at=1777910823.599523
- [2026-05-05 00:07:05] operator / voice_transcript_partial / voice: override go
  meta: kind=partial | timestamp=1777910825.100908 | source=vosk | frequency_hz=271.7 | rms=298 | updated_at=1777910823.599523
- [2026-05-05 00:07:05] operator / voice_transcript_partial / voice: override again
  meta: kind=partial | timestamp=1777910825.3497808 | source=vosk | frequency_hz=271.7 | rms=298 | updated_at=1777910823.599523
- [2026-05-05 00:07:05] operator / voice_transcript_partial / voice: override go ahead that
  meta: kind=partial | timestamp=1777910825.6062093 | source=vosk | frequency_hz=271.7 | rms=298 | updated_at=1777910823.599523
- [2026-05-05 00:07:06] operator / voice_transcript_final / voice: override go ahead that
  meta: kind=final | timestamp=1777910826.1037154 | source=final | frequency_hz=364.0 | rms=290 | updated_at=1777910826.0947106
- [2026-05-05 00:07:06] operator / voice_command / voice: override go ahead that
  meta: normalized=True
- [2026-05-05 00:07:07] operator / voice_transcript_partial / voice: again
  meta: kind=partial | timestamp=1777910827.0858293 | source=vosk | frequency_hz=364.0 | rms=290 | updated_at=1777910826.0947106
- [2026-05-05 00:07:07] operator / voice_transcript_partial / voice: it again
  meta: kind=partial | timestamp=1777910827.5808592 | source=vosk | frequency_hz=364.0 | rms=290 | updated_at=1777910826.0947106
- [2026-05-05 00:07:08] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777910828.1066124 | source=vosk | frequency_hz=308.0 | rms=307 | updated_at=1777910828.073569
- [2026-05-05 00:07:08] operator / voice_transcript_partial / voice: it again
  meta: kind=partial | timestamp=1777910828.33008 | source=vosk | frequency_hz=298.2 | rms=292 | updated_at=1777910828.323569
- [2026-05-05 00:07:08] operator / voice_transcript_final / voice: it again
  meta: kind=final | timestamp=1777910828.8303177 | source=final | frequency_hz=278.6 | rms=293 | updated_at=1777910828.8233154
- [2026-05-05 00:07:09] operator / voice_command / voice: it again
  meta: normalized=True
- [2026-05-05 00:07:10] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:07:10] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:07:10] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777910830.9891539 | source=vosk | frequency_hz=301.1 | rms=321 | updated_at=1777910829.5742004
- [2026-05-05 00:07:10] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777910830.9941664 | source=vosk | frequency_hz=301.1 | rms=321 | updated_at=1777910829.5742004
- [2026-05-05 00:07:11] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777910831.4961424 | source=vosk | frequency_hz=301.1 | rms=321 | updated_at=1777910829.5742004
- [2026-05-05 00:07:12] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:07:12] operator / voice_transcript_final / voice: e
  meta: kind=final | timestamp=1777910832.1154275 | source=final | frequency_hz=219.7 | rms=303 | updated_at=1777910832.103252
- [2026-05-05 00:07:12] operator / voice_command / voice: e
  meta: normalized=True
- [2026-05-05 00:07:12] operator / voice_transcript_partial / voice: the smart
  meta: kind=partial | timestamp=1777910832.8528657 | source=vosk | frequency_hz=219.7 | rms=303 | updated_at=1777910832.103252
- [2026-05-05 00:07:13] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777910833.1052287 | source=vosk | frequency_hz=219.7 | rms=303 | updated_at=1777910832.103252
- [2026-05-05 00:07:13] operator / voice_transcript_partial / voice: the smart
  meta: kind=partial | timestamp=1777910833.352205 | source=vosk | frequency_hz=219.7 | rms=303 | updated_at=1777910832.103252
- [2026-05-05 00:07:13] operator / voice_transcript_partial / voice: the stop that you do
  meta: kind=partial | timestamp=1777910833.6019816 | source=vosk | frequency_hz=219.7 | rms=303 | updated_at=1777910832.103252
- [2026-05-05 00:07:15] assistant / spoken_confirmation / voice: Received. I started your assistant request about e in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:07:13] operator / voice_transcript_partial / voice: the stop that
  meta: kind=partial | timestamp=1777910833.8532314 | source=vosk | frequency_hz=219.7 | rms=303 | updated_at=1777910832.103252
- [2026-05-05 00:07:15] operator / voice_transcript_partial / voice: the stop that on commands
  meta: kind=partial | timestamp=1777910835.0109756 | source=vosk | frequency_hz=219.7 | rms=303 | updated_at=1777910832.103252
- [2026-05-05 00:07:17] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777910837.6126144 | source=vosk | frequency_hz=288.4 | rms=281 | updated_at=1777910836.599441
- [2026-05-05 00:07:18] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777910838.1912065 | source=vosk | frequency_hz=398.0 | rms=283 | updated_at=1777910838.1591382
- [2026-05-05 00:07:19] operator / voice_transcript_partial / voice: enable response
  meta: kind=partial | timestamp=1777910839.0705662 | source=vosk | frequency_hz=398.0 | rms=283 | updated_at=1777910838.1591382
- [2026-05-05 00:07:19] operator / voice_transcript_partial / voice: enable resume
  meta: kind=partial | timestamp=1777910839.3634489 | source=vosk | frequency_hz=398.0 | rms=283 | updated_at=1777910838.1591382
- [2026-05-05 00:07:19] operator / voice_transcript_final / voice: mode enable resume
  meta: kind=final | timestamp=1777910839.8088682 | source=final | frequency_hz=398.0 | rms=283 | updated_at=1777910838.1591382
- [2026-05-05 00:07:20] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777910840.0551195 | source=vosk | frequency_hz=398.0 | rms=283 | updated_at=1777910838.1591382
- [2026-05-05 00:07:20] operator / voice_transcript_partial / voice: to anything else
  meta: kind=partial | timestamp=1777910840.5505984 | source=vosk | frequency_hz=398.0 | rms=283 | updated_at=1777910838.1591382
- [2026-05-05 00:07:21] operator / voice_transcript_partial / voice: and enable
  meta: kind=partial | timestamp=1777910841.8052452 | source=vosk | frequency_hz=398.0 | rms=283 | updated_at=1777910838.1591382
- [2026-05-05 00:07:22] operator / voice_transcript_partial / voice: and the
  meta: kind=partial | timestamp=1777910842.302002 | source=vosk | frequency_hz=398.0 | rms=283 | updated_at=1777910838.1591382
- [2026-05-05 00:07:22] operator / voice_transcript_final / voice: and e that
  meta: kind=final | timestamp=1777910842.902658 | source=final | frequency_hz=398.0 | rms=283 | updated_at=1777910838.1591382
- [2026-05-05 00:07:24] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777910844.5538409 | source=vosk | frequency_hz=284.8 | rms=278 | updated_at=1777910844.0447278
- [2026-05-05 00:07:25] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777910845.2998655 | source=vosk | frequency_hz=284.8 | rms=278 | updated_at=1777910844.0447278
- [2026-05-05 00:07:25] operator / voice_transcript_final / voice: a
  meta: kind=final | timestamp=1777910845.812363 | source=final | frequency_hz=284.8 | rms=278 | updated_at=1777910844.0447278
- [2026-05-05 00:07:26] operator / voice_transcript_partial / voice: alion enable
  meta: kind=partial | timestamp=1777910846.8080592 | source=vosk | frequency_hz=284.8 | rms=278 | updated_at=1777910844.0447278
- [2026-05-05 00:07:26] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:07:27] operator / voice_transcript_partial / voice: repeat it again
  meta: kind=partial | timestamp=1777910847.3007445 | source=vosk | frequency_hz=284.8 | rms=278 | updated_at=1777910844.0447278
- [2026-05-05 00:07:27] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777910847.8026574 | source=vosk | frequency_hz=284.8 | rms=278 | updated_at=1777910844.0447278
- [2026-05-05 00:07:28] operator / voice_transcript_partial / voice: the but faster
  meta: kind=partial | timestamp=1777910848.0511498 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:28] operator / voice_transcript_final / voice: the board
  meta: kind=final | timestamp=1777910848.5527186 | source=final | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:29] operator / voice_command / voice: the board
  meta: normalized=True
- [2026-05-05 00:07:29] assistant / assistant_prompt / text: Assistant request queued: assistant request about the board (position 12).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:07:29] operator / voice_transcript_partial / voice: strict the
  meta: kind=partial | timestamp=1777910849.3224843 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:29] operator / voice_transcript_partial / voice: strict the app
  meta: kind=partial | timestamp=1777910849.5521827 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:29] operator / voice_transcript_partial / voice: strict the
  meta: kind=partial | timestamp=1777910849.804863 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:30] operator / voice_transcript_final / voice: strict the
  meta: kind=final | timestamp=1777910850.3023775 | source=final | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:30] operator / voice_command / voice: strict the
  meta: normalized=True
- [2026-05-05 00:07:30] assistant / assistant_prompt / text: Assistant request queued: assistant request about strict the (position 13).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:07:32] assistant / spoken_confirmation / voice: I am still finishing assistant request about e. I queued your assistant request about strict the. It is number 13 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:07:32] assistant / spoken_confirmation / voice: I am still finishing assistant request about e. I queued your assistant request about the board. It is number 12 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:07:33] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777910853.0276375 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:34] operator / voice_transcript_partial / voice: go ahead
  meta: kind=partial | timestamp=1777910854.0470579 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:34] operator / voice_transcript_partial / voice: go rest
  meta: kind=partial | timestamp=1777910854.4296923 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:34] operator / voice_transcript_partial / voice: no and enable
  meta: kind=partial | timestamp=1777910854.5370555 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:34] operator / voice_transcript_partial / voice: boards and speed
  meta: kind=partial | timestamp=1777910854.8020942 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:35] operator / voice_transcript_partial / voice: boards and enable connect
  meta: kind=partial | timestamp=1777910855.055227 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:35] operator / voice_transcript_partial / voice: go rest analyze the guarding
  meta: kind=partial | timestamp=1777910855.2753344 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:35] operator / voice_transcript_partial / voice: boards and it again it again
  meta: kind=partial | timestamp=1777910855.5353112 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:36] operator / voice_transcript_final / voice: go boards and smart again it again
  meta: kind=final | timestamp=1777910856.301102 | source=final | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:36] operator / voice_command / voice: go boards and smart again it again
  meta: normalized=True
- [2026-05-05 00:07:36] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777910856.7753723 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:37] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777910857.2778873 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:37] operator / voice_transcript_partial / voice: current app
  meta: kind=partial | timestamp=1777910857.5258913 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:38] operator / voice_transcript_partial / voice: current app to com
  meta: kind=partial | timestamp=1777910858.0324259 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:38] operator / voice_transcript_partial / voice: current app sensitivity
  meta: kind=partial | timestamp=1777910858.2819517 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:38] operator / voice_transcript_final / voice: but app sensitivity
  meta: kind=final | timestamp=1777910858.5284457 | source=final | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:38] operator / voice_command / voice: but app sensitivity
  meta: normalized=True
- [2026-05-05 00:07:38] assistant / assistant_prompt / text: Assistant request queued: assistant request about but app sensitivity (position 14).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:07:39] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:07:40] assistant / spoken_confirmation / voice: I am still finishing assistant request about e. I queued your assistant request about but app sensitivity. It is number 14 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:07:40] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910860.280143 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:40] operator / voice_transcript_partial / voice: elian
  meta: kind=partial | timestamp=1777910860.5372076 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:41] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:07:41] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910861.0455859 | source=vosk | frequency_hz=332.0 | rms=245 | updated_at=1777910848.0436378
- [2026-05-05 00:07:42] operator / voice_transcript_partial / voice: elian a
  meta: kind=partial | timestamp=1777910862.7986648 | source=vosk | frequency_hz=392.0 | rms=477 | updated_at=1777910861.7967565
- [2026-05-05 00:07:43] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:07:43] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910863.335257 | source=vosk | frequency_hz=392.0 | rms=477 | updated_at=1777910861.7967565
- [2026-05-05 00:07:43] operator / voice_transcript_partial / voice: elian decrease
  meta: kind=partial | timestamp=1777910863.593331 | source=vosk | frequency_hz=392.0 | rms=477 | updated_at=1777910861.7967565
- [2026-05-05 00:07:43] operator / voice_transcript_partial / voice: elian a aileen repeat enable
  meta: kind=partial | timestamp=1777910863.8103328 | source=vosk | frequency_hz=392.0 | rms=477 | updated_at=1777910861.7967565
- [2026-05-05 00:07:44] operator / voice_transcript_partial / voice: elian a aileen repeat enable the
  meta: kind=partial | timestamp=1777910864.0691597 | source=vosk | frequency_hz=392.0 | rms=477 | updated_at=1777910861.7967565
- [2026-05-05 00:07:44] operator / voice_transcript_partial / voice: elian a aileen repeat enable smart sentry
  meta: kind=partial | timestamp=1777910864.325306 | source=vosk | frequency_hz=392.0 | rms=477 | updated_at=1777910861.7967565
- [2026-05-05 00:07:45] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:07:45] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777910865.3118615 | source=final | frequency_hz=392.0 | rms=477 | updated_at=1777910861.7967565
- [2026-05-05 00:07:46] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 00:07:46] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777910866.3195944 | source=vosk | frequency_hz=70.0 | rms=1201 | updated_at=1777910865.5532315
- [2026-05-05 00:07:46] operator / voice_transcript_partial / voice: change smart
  meta: kind=partial | timestamp=1777910866.8015153 | source=vosk | frequency_hz=70.0 | rms=1201 | updated_at=1777910865.5532315
- [2026-05-05 00:07:47] operator / voice_transcript_partial / voice: change smart sentry
  meta: kind=partial | timestamp=1777910867.0504413 | source=vosk | frequency_hz=70.0 | rms=1201 | updated_at=1777910865.5532315
- [2026-05-05 00:07:48] operator / voice_transcript_final / voice: change smart sentry
  meta: kind=final | timestamp=1777910868.0946984 | source=final | frequency_hz=70.0 | rms=1201 | updated_at=1777910865.5532315
- [2026-05-05 00:07:49] operator / voice_command / voice: change smart sentry
  meta: normalized=True
- [2026-05-05 00:07:50] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:07:50] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:07:50] operator / voice_transcript_partial / voice: theme go
  meta: kind=partial | timestamp=1777910870.5655856 | source=vosk | frequency_hz=343.4 | rms=236 | updated_at=1777910869.5436344
- [2026-05-05 00:07:51] operator / voice_transcript_partial / voice: theme go no
  meta: kind=partial | timestamp=1777910871.3052235 | source=vosk | frequency_hz=343.4 | rms=236 | updated_at=1777910869.5436344
- [2026-05-05 00:07:52] operator / voice_transcript_final / voice: theme go no
  meta: kind=final | timestamp=1777910872.058485 | source=final | frequency_hz=343.4 | rms=236 | updated_at=1777910869.5436344
- [2026-05-05 00:07:52] operator / voice_command / voice: theme go no
  meta: normalized=True
- [2026-05-05 00:07:52] assistant / assistant_prompt / text: Assistant request queued: assistant request about theme go no (position 15).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:07:52] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777910872.360224 | source=vosk | frequency_hz=343.4 | rms=236 | updated_at=1777910869.5436344
- [2026-05-05 00:07:52] operator / voice_transcript_partial / voice: lion say
  meta: kind=partial | timestamp=1777910872.5572667 | source=vosk | frequency_hz=343.4 | rms=236 | updated_at=1777910869.5436344
- [2026-05-05 00:07:53] operator / voice_transcript_partial / voice: lion say it
  meta: kind=partial | timestamp=1777910873.0505555 | source=vosk | frequency_hz=343.4 | rms=236 | updated_at=1777910869.5436344
- [2026-05-05 00:07:54] operator / voice_transcript_final / voice: in say
  meta: kind=final | timestamp=1777910874.451041 | source=final | frequency_hz=343.4 | rms=236 | updated_at=1777910869.5436344
- [2026-05-05 00:07:55] operator / voice_command / voice: in say
  meta: normalized=True
- [2026-05-05 00:07:55] assistant / assistant_prompt / text: Assistant request queued: assistant request about in say (position 16).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:07:54] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777910874.7942815 | source=vosk | frequency_hz=343.4 | rms=236 | updated_at=1777910869.5436344
- [2026-05-05 00:07:55] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:07:55] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777910875.654885 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:07:55] operator / voice_transcript_final / voice: e
  meta: kind=final | timestamp=1777910875.8205159 | source=final | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:07:56] operator / voice_command / voice: e
  meta: normalized=True
- [2026-05-05 00:07:56] assistant / assistant_prompt / text: Assistant request queued: assistant request about e (position 17).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:07:56] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777910876.2785623 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:07:56] operator / voice_transcript_partial / voice: to strict on
  meta: kind=partial | timestamp=1777910876.5299702 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:07:56] operator / voice_transcript_partial / voice: to strict on commands
  meta: kind=partial | timestamp=1777910876.7784057 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:07:57] operator / voice_transcript_partial / voice: to strict on alien
  meta: kind=partial | timestamp=1777910877.032894 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:07:57] operator / voice_transcript_partial / voice: to strict on alien increase
  meta: kind=partial | timestamp=1777910877.284364 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:07:57] operator / voice_transcript_partial / voice: to strict on alien connect smart
  meta: kind=partial | timestamp=1777910877.7814531 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:07:58] operator / voice_transcript_partial / voice: to strict on alien connect smart connect
  meta: kind=partial | timestamp=1777910878.277962 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:07:58] operator / voice_transcript_final / voice: to strict on increase smart confirm
  meta: kind=final | timestamp=1777910878.9146502 | source=final | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:07:59] operator / voice_command / voice: to strict on increase smart confirm
  meta: normalized=True
- [2026-05-05 00:08:00] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777910880.3474967 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:00] operator / voice_transcript_partial / voice: theme
  meta: kind=partial | timestamp=1777910880.5978308 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:00] operator / voice_transcript_partial / voice: theme go
  meta: kind=partial | timestamp=1777910880.848879 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:01] operator / voice_transcript_partial / voice: theme guarding mode
  meta: kind=partial | timestamp=1777910881.3489902 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:01] operator / voice_transcript_final / voice: theme go no
  meta: kind=final | timestamp=1777910881.6002314 | source=final | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:02] operator / voice_command / voice: theme go no
  meta: normalized=True
- [2026-05-05 00:08:02] assistant / assistant_prompt / text: Assistant request queued: assistant request about theme go no (position 18).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:08:01] operator / voice_transcript_partial / voice: app
  meta: kind=partial | timestamp=1777910881.84949 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:02] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777910882.6068041 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:03] assistant / spoken_confirmation / voice: I am still finishing assistant request about e. I queued your assistant request about theme go no. It is number 18 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:08:03] assistant / spoken_confirmation / voice: I am still finishing assistant request about e. I queued your assistant request about e. It is number 17 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:08:03] assistant / spoken_confirmation / voice: I am still finishing assistant request about e. I queued your assistant request about theme go no. It is number 15 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:08:03] assistant / spoken_confirmation / voice: I am still finishing assistant request about e. I queued your assistant request about in say. It is number 16 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:08:03] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:08:07] operator / voice_transcript_partial / voice: eileen
  meta: kind=partial | timestamp=1777910887.8660314 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:08] operator / voice_transcript_partial / voice: aileen increase
  meta: kind=partial | timestamp=1777910888.0971491 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:08] operator / voice_transcript_partial / voice: are you in queue
  meta: kind=partial | timestamp=1777910888.3474026 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:08] operator / voice_transcript_final / voice: are you in queue
  meta: kind=final | timestamp=1777910888.9926803 | source=final | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:09] operator / voice_command / voice: are you in queue
  meta: normalized=True
- [2026-05-05 00:08:09] assistant / assistant_prompt / text: Assistant request queued: assistant request about are you in queue (position 19).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:08:10] operator / voice_transcript_partial / voice: on commands
  meta: kind=partial | timestamp=1777910890.096854 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:11] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777910891.0977283 | source=vosk | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:12] assistant / spoken_confirmation / voice: I am still finishing assistant request about e. I queued your assistant request about are you in queue. It is number 19 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:08:13] operator / voice_transcript_final / voice: confirm
  meta: kind=final | timestamp=1777910893.852714 | source=final | frequency_hz=404.0 | rms=1028 | updated_at=1777910875.270698
- [2026-05-05 00:08:17] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:08:20] operator / voice_transcript_partial / voice: do you do
  meta: kind=partial | timestamp=1777910900.0973344 | source=vosk | frequency_hz=337.4 | rms=229 | updated_at=1777910897.8436205
- [2026-05-05 00:08:20] operator / voice_transcript_partial / voice: do you no
  meta: kind=partial | timestamp=1777910900.3466299 | source=vosk | frequency_hz=337.4 | rms=229 | updated_at=1777910897.8436205
- [2026-05-05 00:08:20] operator / voice_transcript_partial / voice: do you no repeat
  meta: kind=partial | timestamp=1777910900.847898 | source=vosk | frequency_hz=384.8 | rms=243 | updated_at=1777910900.8403795
- [2026-05-05 00:08:21] operator / voice_transcript_final / voice: do you no repeat it
  meta: kind=final | timestamp=1777910901.1017838 | source=final | frequency_hz=384.8 | rms=243 | updated_at=1777910900.8403795
- [2026-05-05 00:08:25] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777910905.8477156 | source=vosk | frequency_hz=334.0 | rms=278 | updated_at=1777910904.3409278
- [2026-05-05 00:08:26] operator / voice_transcript_partial / voice: do you
  meta: kind=partial | timestamp=1777910906.0989203 | source=vosk | frequency_hz=334.0 | rms=278 | updated_at=1777910904.3409278
- [2026-05-05 00:08:26] operator / voice_transcript_partial / voice: do you e lion
  meta: kind=partial | timestamp=1777910906.5974789 | source=vosk | frequency_hz=334.0 | rms=278 | updated_at=1777910904.3409278
- [2026-05-05 00:08:27] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:08:26] operator / voice_transcript_partial / voice: do you enable the
  meta: kind=partial | timestamp=1777910906.9842947 | source=vosk | frequency_hz=334.0 | rms=278 | updated_at=1777910904.3409278
- [2026-05-05 00:08:27] operator / voice_transcript_partial / voice: do you enable the that
  meta: kind=partial | timestamp=1777910907.099597 | source=vosk | frequency_hz=334.0 | rms=278 | updated_at=1777910904.3409278
- [2026-05-05 00:08:27] operator / voice_transcript_final / voice: do you enable the that
  meta: kind=final | timestamp=1777910907.4318168 | source=final | frequency_hz=334.0 | rms=278 | updated_at=1777910904.3409278
- [2026-05-05 00:08:28] operator / voice_command / voice: do you enable the that
  meta: normalized=True
- [2026-05-05 00:08:29] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:08:31] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777910911.7683237 | source=vosk | frequency_hz=341.0 | rms=272 | updated_at=1777910911.0102077
- [2026-05-05 00:08:32] operator / voice_transcript_partial / voice: theme increase
  meta: kind=partial | timestamp=1777910912.016903 | source=vosk | frequency_hz=341.0 | rms=272 | updated_at=1777910911.0102077
- [2026-05-05 00:08:32] operator / voice_transcript_partial / voice: theme go
  meta: kind=partial | timestamp=1777910912.268424 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:32] operator / voice_transcript_partial / voice: theme go no
  meta: kind=partial | timestamp=1777910912.7686377 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:33] operator / voice_transcript_partial / voice: theme go no identify
  meta: kind=partial | timestamp=1777910913.272804 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:33] operator / voice_transcript_partial / voice: theme go no app it again
  meta: kind=partial | timestamp=1777910913.5200374 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:33] operator / voice_transcript_partial / voice: theme go no app it again smart
  meta: kind=partial | timestamp=1777910913.7689745 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:34] operator / voice_transcript_partial / voice: theme go no app it again smart sentry
  meta: kind=partial | timestamp=1777910914.0171995 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:34] operator / voice_transcript_final / voice: theme go no app it again smart
  meta: kind=final | timestamp=1777910914.5209718 | source=final | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:35] operator / voice_command / voice: theme go no app it again smart
  meta: normalized=True
- [2026-05-05 00:08:35] assistant / assistant_prompt / text: Assistant request queued: assistant request about theme go no app it again smart (position 19).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:08:36] assistant / spoken_confirmation / voice: I am still finishing assistant request about to do. I queued your assistant request about theme go no app it again smart. It is number 19 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:08:37] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777910917.778042 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:38] operator / voice_transcript_partial / voice: it again
  meta: kind=partial | timestamp=1777910918.3185194 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:38] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777910918.5377505 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:38] operator / voice_transcript_partial / voice: go sentry
  meta: kind=partial | timestamp=1777910918.778292 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:39] operator / voice_transcript_partial / voice: go sentry connect
  meta: kind=partial | timestamp=1777910919.0732841 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:39] operator / voice_transcript_partial / voice: go sentry connect alien
  meta: kind=partial | timestamp=1777910919.2986007 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:39] operator / voice_transcript_final / voice: go sentry it again
  meta: kind=final | timestamp=1777910919.772198 | source=final | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:40] operator / voice_command / voice: go sentry it again
  meta: normalized=True
- [2026-05-05 00:08:40] assistant / assistant_prompt / text: Assistant request queued: assistant request about go sentry it again (position 20).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:08:40] operator / voice_transcript_partial / voice: the app behaviour
  meta: kind=partial | timestamp=1777910920.848769 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:41] operator / voice_transcript_partial / voice: standby e
  meta: kind=partial | timestamp=1777910921.1010687 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:41] assistant / spoken_confirmation / voice: I am still finishing assistant request about to do. I queued your assistant request about go sentry it again. It is number 20 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:08:41] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910921.6220984 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:45] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777910925.1059275 | source=final | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:45] operator / voice_transcript_partial / voice: report
  meta: kind=partial | timestamp=1777910925.3507414 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:45] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777910925.5993905 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:45] operator / voice_transcript_partial / voice: decrease abort
  meta: kind=partial | timestamp=1777910925.8484094 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:46] operator / voice_transcript_partial / voice: decrease abort be
  meta: kind=partial | timestamp=1777910926.098593 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:46] operator / voice_transcript_partial / voice: decrease abort override
  meta: kind=partial | timestamp=1777910926.3502097 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:46] operator / voice_transcript_final / voice: decrease abort theme
  meta: kind=final | timestamp=1777910926.6031394 | source=final | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:47] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777910927.0980802 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:47] operator / voice_transcript_partial / voice: go home
  meta: kind=partial | timestamp=1777910927.3488438 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:48] operator / voice_transcript_partial / voice: go home and enable
  meta: kind=partial | timestamp=1777910928.09788 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:48] operator / voice_transcript_partial / voice: go home anything else
  meta: kind=partial | timestamp=1777910928.3499284 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:48] operator / voice_transcript_partial / voice: go home anything repeat
  meta: kind=partial | timestamp=1777910928.6129994 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:48] operator / voice_transcript_partial / voice: go home anything be enable
  meta: kind=partial | timestamp=1777910928.8476202 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:49] operator / voice_transcript_partial / voice: go home anything be enable the
  meta: kind=partial | timestamp=1777910929.5994308 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:49] operator / voice_transcript_partial / voice: go home anything be enable the last
  meta: kind=partial | timestamp=1777910929.85004 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:50] operator / voice_transcript_partial / voice: go home anything be enable e lion
  meta: kind=partial | timestamp=1777910930.0984285 | source=vosk | frequency_hz=343.4 | rms=340 | updated_at=1777910912.2611928
- [2026-05-05 00:08:50] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:08:50] operator / voice_transcript_partial / voice: go home anything be enable e lion but faster
  meta: kind=partial | timestamp=1777910930.6572006 | source=vosk | frequency_hz=328.8 | rms=747 | updated_at=1777910930.5966427
- [2026-05-05 00:08:51] operator / voice_transcript_final / voice: go home
  meta: kind=final | timestamp=1777910931.2052054 | source=final | frequency_hz=313.1 | rms=300 | updated_at=1777910930.8418422
- [2026-05-05 00:08:51] operator / voice_command / voice: go home
  meta: normalized=True
- [2026-05-05 00:08:51] operator / voice_transcript_partial / voice: never
  meta: kind=partial | timestamp=1777910931.3601549 | source=vosk | frequency_hz=313.1 | rms=300 | updated_at=1777910930.8418422
- [2026-05-05 00:08:51] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777910931.5993536 | source=vosk | frequency_hz=313.1 | rms=300 | updated_at=1777910930.8418422
- [2026-05-05 00:08:51] operator / voice_transcript_partial / voice: enable the run
  meta: kind=partial | timestamp=1777910931.8608806 | source=vosk | frequency_hz=313.1 | rms=300 | updated_at=1777910930.8418422
- [2026-05-05 00:08:52] operator / voice_transcript_partial / voice: enable the run be less
  meta: kind=partial | timestamp=1777910932.1082025 | source=vosk | frequency_hz=313.1 | rms=300 | updated_at=1777910930.8418422
- [2026-05-05 00:08:52] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910932.367574 | source=vosk | frequency_hz=313.1 | rms=300 | updated_at=1777910930.8418422
- [2026-05-05 00:08:53] assistant / spoken_confirmation / voice: Going to guard home position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:08:54] operator / voice_transcript_partial / voice: enable that and enable the theme guarding
  meta: kind=partial | timestamp=1777910934.9754794 | source=vosk | frequency_hz=416.0 | rms=314 | updated_at=1777910933.6020272
- [2026-05-05 00:08:55] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910935.240318 | source=vosk | frequency_hz=416.0 | rms=314 | updated_at=1777910933.6020272
- [2026-05-05 00:08:55] operator / voice_transcript_partial / voice: enable that and enable the theme guarding mode
  meta: kind=partial | timestamp=1777910935.4714525 | source=vosk | frequency_hz=416.0 | rms=314 | updated_at=1777910933.6020272
- [2026-05-05 00:08:55] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777910935.7078068 | source=vosk | frequency_hz=416.0 | rms=314 | updated_at=1777910933.6020272
- [2026-05-05 00:08:55] operator / voice_transcript_partial / voice: enable that and enable the theme current app
  meta: kind=partial | timestamp=1777910935.9833217 | source=vosk | frequency_hz=416.0 | rms=314 | updated_at=1777910933.6020272
- [2026-05-05 00:08:56] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777910936.2190316 | source=final | frequency_hz=416.0 | rms=314 | updated_at=1777910933.6020272
- [2026-05-05 00:08:56] operator / voice_command / voice: unk
  meta: normalized=True
- [2026-05-05 00:08:56] assistant / assistant_prompt / text: Assistant request queued: assistant request about unk (position 21).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:08:56] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777910936.7161443 | source=vosk | frequency_hz=416.0 | rms=314 | updated_at=1777910933.6020272
- [2026-05-05 00:08:57] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777910937.0985322 | source=vosk | frequency_hz=268.0 | rms=315 | updated_at=1777910936.9432962
- [2026-05-05 00:08:57] operator / voice_transcript_partial / voice: lion no
  meta: kind=partial | timestamp=1777910937.3213573 | source=vosk | frequency_hz=268.0 | rms=315 | updated_at=1777910936.9432962
- [2026-05-05 00:08:58] assistant / spoken_confirmation / voice: I am still finishing assistant request about to do. I queued your assistant request about unk. It is number 21 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:08:57] operator / voice_transcript_partial / voice: lion no alien
  meta: kind=partial | timestamp=1777910937.825521 | source=vosk | frequency_hz=268.0 | rms=315 | updated_at=1777910936.9432962
- [2026-05-05 00:08:58] operator / voice_transcript_final / voice: lion no
  meta: kind=final | timestamp=1777910938.3857436 | source=final | frequency_hz=268.0 | rms=315 | updated_at=1777910936.9432962
- [2026-05-05 00:08:58] operator / voice_command / voice: lion no
  meta: normalized=True
- [2026-05-05 00:08:58] assistant / assistant_prompt / text: Assistant request queued: assistant request about lion no (position 22).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:08:58] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777910938.568862 | source=vosk | frequency_hz=268.0 | rms=315 | updated_at=1777910936.9432962
- [2026-05-05 00:08:59] operator / voice_transcript_final / voice: speed
  meta: kind=final | timestamp=1777910939.558559 | source=final | frequency_hz=268.0 | rms=315 | updated_at=1777910936.9432962
- [2026-05-05 00:08:59] operator / voice_command / voice: speed
  meta: normalized=True
- [2026-05-05 00:08:59] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1777910939.5685782 | source=vosk | frequency_hz=268.0 | rms=315 | updated_at=1777910936.9432962
- [2026-05-05 00:08:59] operator / voice_transcript_partial / voice: it again
  meta: kind=partial | timestamp=1777910939.830936 | source=vosk | frequency_hz=268.0 | rms=315 | updated_at=1777910936.9432962
- [2026-05-05 00:09:00] assistant / spoken_confirmation / voice: I am still finishing assistant request about to do. I queued your assistant request about lion no. It is number 22 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:09:00] operator / voice_transcript_partial / voice: it again smart
  meta: kind=partial | timestamp=1777910940.0679028 | source=vosk | frequency_hz=268.0 | rms=315 | updated_at=1777910936.9432962
- [2026-05-05 00:09:00] operator / voice_transcript_partial / voice: it again smart sentry
  meta: kind=partial | timestamp=1777910940.3253572 | source=vosk | frequency_hz=268.0 | rms=315 | updated_at=1777910936.9432962
- [2026-05-05 00:09:00] operator / voice_transcript_partial / voice: it again smart no
  meta: kind=partial | timestamp=1777910940.5770445 | source=vosk | frequency_hz=268.0 | rms=315 | updated_at=1777910936.9432962
- [2026-05-05 00:09:02] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:09:01] operator / voice_transcript_final / voice: that again smart no
  meta: kind=final | timestamp=1777910941.360285 | source=final | frequency_hz=312.0 | rms=311 | updated_at=1777910941.063904
- [2026-05-05 00:09:02] operator / voice_command / voice: that again smart no
  meta: normalized=True
- [2026-05-05 00:09:02] assistant / assistant_prompt / text: Assistant request queued: assistant request about that again smart no (position 23).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:09:04] assistant / spoken_confirmation / voice: I am still finishing assistant request about to do. I queued your assistant request about that again smart no. It is number 23 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:09:19] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1777910959.9959378 | source=vosk | frequency_hz=340.5 | rms=323 | updated_at=1777910958.9863882
- [2026-05-05 00:09:20] operator / voice_transcript_partial / voice: who are you
  meta: kind=partial | timestamp=1777910960.2445433 | source=vosk | frequency_hz=355.7 | rms=315 | updated_at=1777910960.2360358
- [2026-05-05 00:09:21] operator / voice_transcript_final / voice: who are you
  meta: kind=final | timestamp=1777910961.0026329 | source=final | frequency_hz=288.4 | rms=307 | updated_at=1777910960.991586
- [2026-05-05 00:09:22] operator / voice_transcript_partial / voice: elian
  meta: kind=partial | timestamp=1777910962.7446177 | source=vosk | frequency_hz=344.9 | rms=445 | updated_at=1777910961.991058
- [2026-05-05 00:09:23] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:09:24] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:09:24] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777910964.4054456 | source=final | frequency_hz=327.5 | rms=309 | updated_at=1777910963.2639902
- [2026-05-05 00:09:24] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777910964.6927903 | source=vosk | frequency_hz=327.5 | rms=309 | updated_at=1777910963.2639902
- [2026-05-05 00:09:25] operator / voice_transcript_partial / voice: no resume
  meta: kind=partial | timestamp=1777910965.4325218 | source=vosk | frequency_hz=327.5 | rms=309 | updated_at=1777910963.2639902
- [2026-05-05 00:09:25] operator / voice_transcript_partial / voice: no resume last
  meta: kind=partial | timestamp=1777910965.6874623 | source=vosk | frequency_hz=327.5 | rms=309 | updated_at=1777910963.2639902
- [2026-05-05 00:09:25] operator / voice_transcript_partial / voice: no resume speed
  meta: kind=partial | timestamp=1777910965.923901 | source=vosk | frequency_hz=327.5 | rms=309 | updated_at=1777910963.2639902
- [2026-05-05 00:09:27] operator / voice_transcript_final / voice: no resume speed
  meta: kind=final | timestamp=1777910967.230678 | source=final | frequency_hz=285.2 | rms=323 | updated_at=1777910967.169335
- [2026-05-05 00:09:28] operator / voice_command / voice: no resume speed
  meta: normalized=True
- [2026-05-05 00:09:28] assistant / assistant_prompt / text: Assistant request queued: assistant request about no resume speed (position 23).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:09:29] assistant / spoken_confirmation / voice: I am still finishing assistant request about that the app that do unk. I queued your assistant request about no resume speed. It is number 23 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:09:33] operator / voice_transcript_partial / voice: be no
  meta: kind=partial | timestamp=1777910973.672824 | source=vosk | frequency_hz=301.2 | rms=319 | updated_at=1777910973.1637194
- [2026-05-05 00:09:34] operator / voice_transcript_partial / voice: be no a
  meta: kind=partial | timestamp=1777910974.4199102 | source=vosk | frequency_hz=301.2 | rms=319 | updated_at=1777910973.1637194
- [2026-05-05 00:09:34] operator / voice_transcript_partial / voice: be no a lion
  meta: kind=partial | timestamp=1777910974.6709335 | source=vosk | frequency_hz=332.0 | rms=318 | updated_at=1777910974.6649218
- [2026-05-05 00:09:35] operator / voice_transcript_partial / voice: be no a
  meta: kind=partial | timestamp=1777910975.1720676 | source=vosk | frequency_hz=332.0 | rms=318 | updated_at=1777910974.6649218
- [2026-05-05 00:09:35] operator / voice_transcript_partial / voice: be no a say
  meta: kind=partial | timestamp=1777910975.4341862 | source=vosk | frequency_hz=332.0 | rms=318 | updated_at=1777910974.6649218
- [2026-05-05 00:09:35] operator / voice_transcript_partial / voice: be no a say sentry
  meta: kind=partial | timestamp=1777910975.6707315 | source=vosk | frequency_hz=332.0 | rms=318 | updated_at=1777910974.6649218
- [2026-05-05 00:09:35] operator / voice_transcript_partial / voice: be no a say same decrease
  meta: kind=partial | timestamp=1777910975.922527 | source=vosk | frequency_hz=362.8 | rms=335 | updated_at=1777910975.9155219
- [2026-05-05 00:09:36] operator / voice_transcript_partial / voice: be no a say anything else
  meta: kind=partial | timestamp=1777910976.171552 | source=vosk | frequency_hz=335.2 | rms=315 | updated_at=1777910976.1648176
- [2026-05-05 00:09:36] operator / voice_transcript_final / voice: be no a say anything
  meta: kind=final | timestamp=1777910976.955622 | source=final | frequency_hz=292.1 | rms=313 | updated_at=1777910976.919578
- [2026-05-05 00:09:37] operator / voice_command / voice: be no a say anything
  meta: normalized=True
- [2026-05-05 00:09:37] assistant / assistant_prompt / text: Assistant request queued: assistant request about be no a say anything (position 24).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:09:38] assistant / spoken_confirmation / voice: I am still finishing assistant request about that the app that do unk. I queued your assistant request about be no a say anything. It is number 24 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:09:39] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777910979.85912 | source=vosk | frequency_hz=335.6 | rms=327 | updated_at=1777910978.4142659
- [2026-05-05 00:09:40] operator / voice_transcript_final / voice: sentry
  meta: kind=final | timestamp=1777910980.8911827 | source=final | frequency_hz=242.3 | rms=318 | updated_at=1777910980.8805811
- [2026-05-05 00:09:43] assistant / spoken_reply / voice: Assistant request queued: assistant request about be no a say anything (position 24).
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 00:09:50] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777910990.6178715 | source=vosk | frequency_hz=315.6 | rms=302 | updated_at=1777910989.11033
- [2026-05-05 00:09:51] operator / voice_transcript_partial / voice: the smart
  meta: kind=partial | timestamp=1777910991.3855321 | source=vosk | frequency_hz=315.6 | rms=302 | updated_at=1777910989.11033
- [2026-05-05 00:09:51] operator / voice_transcript_partial / voice: the change
  meta: kind=partial | timestamp=1777910991.621425 | source=vosk | frequency_hz=315.6 | rms=302 | updated_at=1777910989.11033
- [2026-05-05 00:09:51] operator / voice_transcript_partial / voice: the say that
  meta: kind=partial | timestamp=1777910991.8703337 | source=vosk | frequency_hz=280.0 | rms=292 | updated_at=1777910991.8608155
- [2026-05-05 00:09:52] operator / voice_transcript_final / voice: the say that
  meta: kind=final | timestamp=1777910992.9522612 | source=final | frequency_hz=313.6 | rms=291 | updated_at=1777910992.9412212
- [2026-05-05 00:10:03] operator / voice_transcript_final / voice: less
  meta: kind=final | timestamp=1777911003.5495856 | source=final | frequency_hz=301.4 | rms=289 | updated_at=1777911002.942662
- [2026-05-05 00:10:06] operator / voice_transcript_partial / voice: anything
  meta: kind=partial | timestamp=1777911006.0595121 | source=vosk | frequency_hz=334.3 | rms=294 | updated_at=1777911004.7998505
- [2026-05-05 00:10:06] operator / voice_transcript_partial / voice: it again
  meta: kind=partial | timestamp=1777911006.3160205 | source=vosk | frequency_hz=418.0 | rms=317 | updated_at=1777911006.3080168
- [2026-05-05 00:10:06] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777911006.556913 | source=vosk | frequency_hz=418.0 | rms=317 | updated_at=1777911006.3080168
- [2026-05-05 00:10:06] operator / voice_transcript_partial / voice: do it again
  meta: kind=partial | timestamp=1777911006.816916 | source=vosk | frequency_hz=418.0 | rms=317 | updated_at=1777911006.3080168
- [2026-05-05 00:10:07] operator / voice_transcript_partial / voice: no delay
  meta: kind=partial | timestamp=1777911007.057001 | source=vosk | frequency_hz=418.0 | rms=317 | updated_at=1777911006.3080168
- [2026-05-05 00:10:07] operator / voice_transcript_partial / voice: theme to anything
  meta: kind=partial | timestamp=1777911007.3172119 | source=vosk | frequency_hz=418.0 | rms=317 | updated_at=1777911006.3080168
- [2026-05-05 00:10:07] operator / voice_transcript_partial / voice: theme to anything else
  meta: kind=partial | timestamp=1777911007.564819 | source=vosk | frequency_hz=418.0 | rms=317 | updated_at=1777911006.3080168
- [2026-05-05 00:10:08] operator / voice_transcript_partial / voice: theme to anything
  meta: kind=partial | timestamp=1777911008.3320117 | source=vosk | frequency_hz=418.0 | rms=317 | updated_at=1777911006.3080168
- [2026-05-05 00:10:08] operator / voice_transcript_final / voice: it on commands
  meta: kind=final | timestamp=1777911008.5620365 | source=final | frequency_hz=418.0 | rms=317 | updated_at=1777911006.3080168
- [2026-05-05 00:10:09] operator / voice_transcript_partial / voice: analyze
  meta: kind=partial | timestamp=1777911009.8093283 | source=vosk | frequency_hz=348.0 | rms=277 | updated_at=1777911009.3121765
- [2026-05-05 00:10:10] operator / voice_transcript_partial / voice: and enable
  meta: kind=partial | timestamp=1777911010.0583005 | source=vosk | frequency_hz=348.0 | rms=277 | updated_at=1777911009.3121765
- [2026-05-05 00:10:10] operator / voice_transcript_partial / voice: that again
  meta: kind=partial | timestamp=1777911010.3313022 | source=vosk | frequency_hz=348.0 | rms=277 | updated_at=1777911009.3121765
- [2026-05-05 00:10:10] operator / voice_transcript_partial / voice: and enable smart
  meta: kind=partial | timestamp=1777911010.5572503 | source=vosk | frequency_hz=348.0 | rms=277 | updated_at=1777911009.3121765
- [2026-05-05 00:10:11] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777911011.0571501 | source=vosk | frequency_hz=348.0 | rms=277 | updated_at=1777911009.3121765
- [2026-05-05 00:10:12] operator / voice_transcript_final / voice: that again say
  meta: kind=final | timestamp=1777911012.2283876 | source=final | frequency_hz=348.0 | rms=277 | updated_at=1777911009.3121765
- [2026-05-05 00:10:12] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777911012.5559604 | source=vosk | frequency_hz=348.0 | rms=277 | updated_at=1777911009.3121765
- [2026-05-05 00:10:12] operator / voice_transcript_partial / voice: do on commands
  meta: kind=partial | timestamp=1777911012.8085785 | source=vosk | frequency_hz=348.0 | rms=277 | updated_at=1777911009.3121765
- [2026-05-05 00:10:23] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777911023.3513753 | source=vosk | frequency_hz=306.8 | rms=279 | updated_at=1777911022.591656
- [2026-05-05 00:10:23] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777911023.6010606 | source=vosk | frequency_hz=303.0 | rms=275 | updated_at=1777911023.5932126
- [2026-05-05 00:10:24] operator / voice_transcript_partial / voice: a e lion
  meta: kind=partial | timestamp=1777911024.3460233 | source=vosk | frequency_hz=321.6 | rms=286 | updated_at=1777911023.8387704
- [2026-05-05 00:10:24] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:10:24] operator / voice_transcript_partial / voice: a alien
  meta: kind=partial | timestamp=1777911024.61469 | source=vosk | frequency_hz=321.6 | rms=286 | updated_at=1777911023.8387704
- [2026-05-05 00:10:25] operator / voice_transcript_final / voice: a
  meta: kind=final | timestamp=1777911025.9103343 | source=final | frequency_hz=282.9 | rms=286 | updated_at=1777911025.8402126
- [2026-05-05 00:10:26] operator / voice_command / voice: a
  meta: normalized=True
- [2026-05-05 00:10:26] assistant / assistant_prompt / text: Assistant request queued: assistant request about a (position 25).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:10:27] assistant / spoken_confirmation / voice: I am still finishing assistant request about that the app that do unk. I queued your assistant request about a. It is number 25 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:10:28] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777911028.3557801 | source=vosk | frequency_hz=344.7 | rms=286 | updated_at=1777911028.3396642
- [2026-05-05 00:10:29] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777911029.8005776 | source=final | frequency_hz=344.7 | rms=286 | updated_at=1777911028.3396642
- [2026-05-05 00:10:30] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:10:31] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:10:33] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777911033.8478906 | source=vosk | frequency_hz=280.9 | rms=270 | updated_at=1777911031.0891297
- [2026-05-05 00:10:35] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777911035.5423954 | source=final | frequency_hz=410.0 | rms=310 | updated_at=1777911034.8387015
- [2026-05-05 00:10:35] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:10:42] operator / voice_transcript_partial / voice: brightness
  meta: kind=partial | timestamp=1777911042.0504832 | source=vosk | frequency_hz=353.7 | rms=304 | updated_at=1777911041.543841
- [2026-05-05 00:10:42] operator / voice_transcript_partial / voice: board alion analyze
  meta: kind=partial | timestamp=1777911042.5501058 | source=vosk | frequency_hz=353.7 | rms=304 | updated_at=1777911041.543841
- [2026-05-05 00:10:43] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:10:42] operator / voice_transcript_partial / voice: enable alion
  meta: kind=partial | timestamp=1777911042.8006847 | source=vosk | frequency_hz=348.9 | rms=293 | updated_at=1777911042.7946694
- [2026-05-05 00:10:43] operator / voice_transcript_final / voice: brightness
  meta: kind=final | timestamp=1777911043.0537663 | source=final | frequency_hz=337.4 | rms=292 | updated_at=1777911043.0447059
- [2026-05-05 00:10:44] operator / voice_command / voice: brightness
  meta: normalized=True
- [2026-05-05 00:10:44] assistant / assistant_prompt / text: Assistant request queued: assistant request about brightness (position 25).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:10:45] assistant / spoken_confirmation / voice: I am still finishing assistant request about commands repeat. I queued your assistant request about brightness. It is number 25 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:10:47] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777911047.5679188 | source=vosk | frequency_hz=275.1 | rms=292 | updated_at=1777911046.7981026
- [2026-05-05 00:10:48] operator / voice_transcript_partial / voice: yourself be status
  meta: kind=partial | timestamp=1777911048.3016737 | source=vosk | frequency_hz=275.1 | rms=292 | updated_at=1777911046.7981026
- [2026-05-05 00:10:48] operator / voice_transcript_final / voice: yourself unk
  meta: kind=final | timestamp=1777911048.7388225 | source=final | frequency_hz=275.1 | rms=292 | updated_at=1777911046.7981026
- [2026-05-05 00:10:49] operator / voice_command / voice: yourself unk
  meta: normalized=True
- [2026-05-05 00:10:49] assistant / assistant_prompt / text: Assistant request queued: assistant request about yourself unk (position 26).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:10:49] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777911049.3003018 | source=vosk | frequency_hz=275.1 | rms=292 | updated_at=1777911046.7981026
- [2026-05-05 00:10:49] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777911049.5568051 | source=vosk | frequency_hz=275.1 | rms=292 | updated_at=1777911046.7981026
- [2026-05-05 00:10:50] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777911050.3034184 | source=final | frequency_hz=342.0 | rms=865 | updated_at=1777911049.793892
- [2026-05-05 00:10:50] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:10:51] operator / voice_transcript_partial / voice: run
  meta: kind=partial | timestamp=1777911051.56646 | source=vosk | frequency_hz=342.0 | rms=865 | updated_at=1777911049.793892
- [2026-05-05 00:10:51] operator / voice_transcript_partial / voice: threshold
  meta: kind=partial | timestamp=1777911051.8123176 | source=vosk | frequency_hz=342.0 | rms=865 | updated_at=1777911049.793892
- [2026-05-05 00:10:53] assistant / spoken_confirmation / voice: I am still finishing assistant request about commands repeat. I queued your assistant request about yourself unk. It is number 26 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:10:52] operator / voice_transcript_partial / voice: threshold decrease
  meta: kind=partial | timestamp=1777911052.5540295 | source=vosk | frequency_hz=344.0 | rms=282 | updated_at=1777911052.0451868
- [2026-05-05 00:10:52] operator / voice_transcript_partial / voice: threshold delay
  meta: kind=partial | timestamp=1777911052.8006952 | source=vosk | frequency_hz=344.0 | rms=282 | updated_at=1777911052.0451868
- [2026-05-05 00:10:53] operator / voice_transcript_partial / voice: threshold theme to
  meta: kind=partial | timestamp=1777911053.0668945 | source=vosk | frequency_hz=344.0 | rms=282 | updated_at=1777911052.0451868
- [2026-05-05 00:10:53] operator / voice_transcript_partial / voice: threshold the mode decrease
  meta: kind=partial | timestamp=1777911053.3008456 | source=vosk | frequency_hz=344.0 | rms=282 | updated_at=1777911052.0451868
- [2026-05-05 00:10:53] operator / voice_transcript_partial / voice: threshold do you do
  meta: kind=partial | timestamp=1777911053.5653138 | source=vosk | frequency_hz=344.0 | rms=282 | updated_at=1777911052.0451868
- [2026-05-05 00:10:54] operator / voice_transcript_final / voice: threshold the mode delay
  meta: kind=final | timestamp=1777911054.6309664 | source=final | frequency_hz=344.0 | rms=282 | updated_at=1777911052.0451868
- [2026-05-05 00:10:55] operator / voice_command / voice: threshold the mode delay
  meta: normalized=True
- [2026-05-05 00:10:56] assistant / assistant_prompt / text: Assistant request queued: assistant request about threshold the mode delay (position 27).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:10:58] assistant / spoken_confirmation / voice: I am still finishing assistant request about commands repeat. I queued your assistant request about threshold the mode delay. It is number 27 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:11:01] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777911061.5711544 | source=vosk | frequency_hz=293.0 | rms=277 | updated_at=1777911061.05806
- [2026-05-05 00:11:02] operator / voice_transcript_partial / voice: say sentry
  meta: kind=partial | timestamp=1777911062.0635588 | source=vosk | frequency_hz=293.0 | rms=277 | updated_at=1777911061.05806
- [2026-05-05 00:11:02] operator / voice_transcript_partial / voice: say sentry decrease
  meta: kind=partial | timestamp=1777911062.5650966 | source=vosk | frequency_hz=293.0 | rms=277 | updated_at=1777911061.05806
- [2026-05-05 00:11:02] operator / voice_transcript_final / voice: say sentry
  meta: kind=final | timestamp=1777911062.8311336 | source=final | frequency_hz=293.0 | rms=277 | updated_at=1777911061.05806
- [2026-05-05 00:11:06] operator / voice_transcript_partial / voice: guarding
  meta: kind=partial | timestamp=1777911066.4686017 | source=vosk | frequency_hz=296.7 | rms=281 | updated_at=1777911065.713525
- [2026-05-05 00:11:06] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777911066.727017 | source=vosk | frequency_hz=296.7 | rms=281 | updated_at=1777911065.713525
- [2026-05-05 00:11:06] operator / voice_transcript_partial / voice: go rest
  meta: kind=partial | timestamp=1777911066.9694045 | source=vosk | frequency_hz=296.7 | rms=281 | updated_at=1777911065.713525
- [2026-05-05 00:11:07] operator / voice_transcript_final / voice: go
  meta: kind=final | timestamp=1777911067.2212043 | source=final | frequency_hz=296.7 | rms=281 | updated_at=1777911065.713525
- [2026-05-05 00:11:09] operator / voice_transcript_partial / voice: do it
  meta: kind=partial | timestamp=1777911069.2204132 | source=vosk | frequency_hz=331.6 | rms=357 | updated_at=1777911068.7117994
- [2026-05-05 00:11:09] operator / voice_transcript_partial / voice: sentry what
  meta: kind=partial | timestamp=1777911069.7183816 | source=vosk | frequency_hz=331.6 | rms=357 | updated_at=1777911068.7117994
- [2026-05-05 00:11:09] operator / voice_transcript_partial / voice: sentry the
  meta: kind=partial | timestamp=1777911069.9700987 | source=vosk | frequency_hz=327.5 | rms=290 | updated_at=1777911069.9625893
- [2026-05-05 00:11:10] operator / voice_transcript_partial / voice: sentry the com
  meta: kind=partial | timestamp=1777911070.2183585 | source=vosk | frequency_hz=330.5 | rms=267 | updated_at=1777911070.2128181
- [2026-05-05 00:11:10] operator / voice_transcript_final / voice: sentry the com
  meta: kind=final | timestamp=1777911070.9717324 | source=final | frequency_hz=352.9 | rms=279 | updated_at=1777911070.9617026
- [2026-05-05 00:11:12] operator / voice_transcript_partial / voice: delay
  meta: kind=partial | timestamp=1777911072.724459 | source=vosk | frequency_hz=352.3 | rms=278 | updated_at=1777911071.465509
