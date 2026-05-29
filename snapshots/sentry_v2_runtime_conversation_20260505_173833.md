# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-05 17:38:33
- Entries: 398
- Roles: {'assistant': 15, 'system': 1, 'operator': 382}
- Event types: {'assistant_prompt': 5, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_partial': 299, 'spoken_confirmation': 9, 'voice_transcript_final': 63, 'voice_command': 20}
- Channels: {'text': 6, 'voice': 392}
- Latest operator request: use nano model
- Latest assistant message: That does not match a known command. Please repeat.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 17:24:32] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 17:24:32] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 17:24:33] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777973073.5717437 | source=vosk
- [2026-05-05 17:24:59] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1777973099.8033242 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:13] assistant / spoken_confirmation / voice: Smart Sentry AI is online. Ask a question or give a command when ready.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 17:25:16] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777973116.3171585 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:16] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777973116.5690017 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:18] operator / voice_transcript_partial / voice: smart sentry aileen i
  meta: kind=partial | timestamp=1777973118.1360538 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:18] operator / voice_transcript_final / voice: smart sentry i
  meta: kind=final | timestamp=1777973118.3896756 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:19] operator / voice_transcript_partial / voice: ask
  meta: kind=partial | timestamp=1777973119.1376026 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:19] operator / voice_transcript_partial / voice: ask a question
  meta: kind=partial | timestamp=1777973119.3834517 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:20] operator / voice_transcript_final / voice: ask a question
  meta: kind=final | timestamp=1777973120.145403 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:20] operator / voice_transcript_partial / voice: command
  meta: kind=partial | timestamp=1777973120.6324635 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:21] operator / voice_transcript_partial / voice: command repeat
  meta: kind=partial | timestamp=1777973121.3821812 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:21] operator / voice_transcript_final / voice: command
  meta: kind=final | timestamp=1777973121.8830194 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:40] operator / voice_transcript_partial / voice: priority
  meta: kind=partial | timestamp=1777973140.6373396 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:40] operator / voice_transcript_partial / voice: to com
  meta: kind=partial | timestamp=1777973140.8847547 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:41] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777973141.1369915 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:25:42] operator / voice_transcript_final / voice: quiet
  meta: kind=final | timestamp=1777973142.3879373 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:28:36] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777973316.6019611 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:28:40] operator / voice_transcript_final / voice: tracking
  meta: kind=final | timestamp=1777973320.1042752 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:29:20] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1777973360.8773768 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:30:27] operator / voice_transcript_partial / voice: disable
  meta: kind=partial | timestamp=1777973427.4736834 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:30:28] operator / voice_transcript_final / voice: disable
  meta: kind=final | timestamp=1777973428.737345 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:30:29] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777973429.220812 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:30:29] operator / voice_transcript_partial / voice: tiny model
  meta: kind=partial | timestamp=1777973429.470184 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:30:29] operator / voice_transcript_partial / voice: priority connect
  meta: kind=partial | timestamp=1777973429.7222295 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:30:34] operator / voice_transcript_final / voice: mode
  meta: kind=final | timestamp=1777973434.0030165 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:30:49] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777973449.4685066 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:30:49] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1777973449.9686115 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:30:54] operator / voice_transcript_final / voice: speed
  meta: kind=final | timestamp=1777973454.2237074 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:23] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777973483.970768 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:24] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777973484.9712527 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:25] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 17:31:28] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777973488.7270467 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:28] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777973488.9708636 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:29] operator / voice_transcript_partial / voice: standby go
  meta: kind=partial | timestamp=1777973489.4691422 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:29] operator / voice_transcript_partial / voice: standby go no
  meta: kind=partial | timestamp=1777973489.9691126 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:30] operator / voice_transcript_partial / voice: standby go no app detection
  meta: kind=partial | timestamp=1777973490.4703848 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:30] operator / voice_transcript_partial / voice: standby go no app to talk
  meta: kind=partial | timestamp=1777973490.720385 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:30] operator / voice_transcript_partial / voice: standby go no app to shortcuts
  meta: kind=partial | timestamp=1777973490.9704437 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:31] operator / voice_transcript_partial / voice: standby go no app to shortcuts wait
  meta: kind=partial | timestamp=1777973491.2290406 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:31] operator / voice_transcript_partial / voice: standby go no app to shortcuts brightness
  meta: kind=partial | timestamp=1777973491.4732175 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:31] operator / voice_transcript_partial / voice: standby go no app to shortcuts wait no
  meta: kind=partial | timestamp=1777973491.726498 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:31] operator / voice_transcript_partial / voice: standby go no app to shortcuts wait no run
  meta: kind=partial | timestamp=1777973491.9697845 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:32] operator / voice_transcript_partial / voice: standby go no app to shortcuts wait no run the
  meta: kind=partial | timestamp=1777973492.2197447 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:32] operator / voice_transcript_partial / voice: standby go no app to shortcuts wait no run the app
  meta: kind=partial | timestamp=1777973492.4693925 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:34] operator / voice_transcript_final / voice: standby go no app to shortcuts wait no run the app
  meta: kind=final | timestamp=1777973494.1620324 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:34] operator / voice_command / voice: standby go no app to shortcuts wait no run the app
  meta: normalized=True
- [2026-05-05 17:31:35] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 17:31:37] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777973497.4285219 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:37] operator / voice_transcript_partial / voice: go to
  meta: kind=partial | timestamp=1777973497.6738977 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:37] operator / voice_transcript_partial / voice: go rest
  meta: kind=partial | timestamp=1777973497.9213219 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:38] operator / voice_transcript_partial / voice: go rest position
  meta: kind=partial | timestamp=1777973498.4224436 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:38] operator / voice_transcript_partial / voice: go rest position app
  meta: kind=partial | timestamp=1777973498.9232423 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:39] operator / voice_transcript_final / voice: go rest
  meta: kind=final | timestamp=1777973499.6722546 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:39] operator / voice_command / voice: go rest
  meta: normalized=True
- [2026-05-05 17:31:40] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 17:31:41] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777973501.670923 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:41] operator / voice_transcript_partial / voice: connect the
  meta: kind=partial | timestamp=1777973501.9219773 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:42] operator / voice_transcript_partial / voice: connect the board
  meta: kind=partial | timestamp=1777973502.1716042 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:42] operator / voice_transcript_partial / voice: connect the board to rest
  meta: kind=partial | timestamp=1777973502.682838 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:43] operator / voice_transcript_partial / voice: connect the board to rest position
  meta: kind=partial | timestamp=1777973503.1755385 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:43] operator / voice_transcript_partial / voice: connect the board to rest position app
  meta: kind=partial | timestamp=1777973503.6713176 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:44] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777973504.4217148 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:44] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-05 17:31:44] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777973504.9214423 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:45] operator / voice_transcript_partial / voice: standby last
  meta: kind=partial | timestamp=1777973505.5185394 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:46] operator / voice_transcript_final / voice: standby last
  meta: kind=final | timestamp=1777973506.5875764 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:46] operator / voice_transcript_partial / voice: app to
  meta: kind=partial | timestamp=1777973506.6244106 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:46] operator / voice_transcript_partial / voice: app to talk
  meta: kind=partial | timestamp=1777973506.8626494 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:47] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 17:31:47] operator / voice_transcript_partial / voice: app to talk less
  meta: kind=partial | timestamp=1777973507.1256135 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:47] operator / voice_transcript_final / voice: app to talk
  meta: kind=final | timestamp=1777973507.6810062 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:48] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777973508.3615577 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:48] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777973508.6226864 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:49] operator / voice_transcript_partial / voice: smart sentry boards
  meta: kind=partial | timestamp=1777973509.3618648 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:49] operator / voice_transcript_partial / voice: smart sentry boards and
  meta: kind=partial | timestamp=1777973509.6113114 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:49] operator / voice_transcript_partial / voice: smart sentry boards and enable
  meta: kind=partial | timestamp=1777973509.8704023 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:50] operator / voice_transcript_final / voice: smart sentry boards
  meta: kind=final | timestamp=1777973510.146888 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:50] operator / voice_transcript_partial / voice: the smart
  meta: kind=partial | timestamp=1777973510.362918 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:50] operator / voice_transcript_partial / voice: disconnect
  meta: kind=partial | timestamp=1777973510.6121306 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:52] operator / voice_transcript_partial / voice: is not
  meta: kind=partial | timestamp=1777973512.119317 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:52] operator / voice_transcript_partial / voice: guarding
  meta: kind=partial | timestamp=1777973512.3793206 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:53] operator / voice_transcript_partial / voice: guarding stay paused
  meta: kind=partial | timestamp=1777973513.1133292 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:53] operator / voice_transcript_final / voice: guarding stay paused
  meta: kind=final | timestamp=1777973513.8936882 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:54] operator / voice_transcript_partial / voice: tell
  meta: kind=partial | timestamp=1777973514.1259189 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:54] operator / voice_transcript_partial / voice: tell me why
  meta: kind=partial | timestamp=1777973514.3616447 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:54] operator / voice_transcript_partial / voice: tell me want to
  meta: kind=partial | timestamp=1777973514.6280315 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:55] operator / voice_transcript_partial / voice: tell me why
  meta: kind=partial | timestamp=1777973515.111996 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:55] operator / voice_transcript_partial / voice: tell me why what
  meta: kind=partial | timestamp=1777973515.621123 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:55] operator / voice_transcript_partial / voice: tell me why what give another
  meta: kind=partial | timestamp=1777973515.8644974 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:56] operator / voice_transcript_partial / voice: tell me why what give enable
  meta: kind=partial | timestamp=1777973516.110961 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:56] operator / voice_transcript_partial / voice: tell me why what give another command
  meta: kind=partial | timestamp=1777973516.363387 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:57] operator / voice_transcript_final / voice: tell me want to what give another command
  meta: kind=final | timestamp=1777973517.3654366 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:31:57] operator / voice_command / voice: tell me want to what give another command
  meta: normalized=True
- [2026-05-05 17:32:01] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777973521.902104 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:02] operator / voice_transcript_final / voice: tracking
  meta: kind=final | timestamp=1777973522.6674645 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:03] operator / voice_transcript_partial / voice: use
  meta: kind=partial | timestamp=1777973523.6234763 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:03] operator / voice_transcript_partial / voice: use wait
  meta: kind=partial | timestamp=1777973523.8806934 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:04] operator / voice_transcript_partial / voice: use wait a joke
  meta: kind=partial | timestamp=1777973524.1465213 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:04] operator / voice_transcript_partial / voice: use with that again
  meta: kind=partial | timestamp=1777973524.3783472 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:04] operator / voice_transcript_partial / voice: use with app to resume guarding
  meta: kind=partial | timestamp=1777973524.628539 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:04] operator / voice_transcript_partial / voice: use with guard
  meta: kind=partial | timestamp=1777973524.8765554 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:05] operator / voice_transcript_partial / voice: use with guard hold position
  meta: kind=partial | timestamp=1777973525.1298895 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:06] operator / voice_transcript_partial / voice: use with guard hold position standby
  meta: kind=partial | timestamp=1777973526.5018804 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:06] operator / voice_transcript_partial / voice: use with guard hold position standby go
  meta: kind=partial | timestamp=1777973526.9832277 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:07] operator / voice_transcript_partial / voice: use with guard hold position standby go no
  meta: kind=partial | timestamp=1777973527.4827645 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:07] operator / voice_transcript_partial / voice: use with guard hold position standby go no app
  meta: kind=partial | timestamp=1777973527.732896 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:07] operator / voice_transcript_partial / voice: use with guard hold position standby go no app detection
  meta: kind=partial | timestamp=1777973527.9904873 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:08] operator / voice_transcript_partial / voice: use with guard hold position standby go no app to talk
  meta: kind=partial | timestamp=1777973528.2352798 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:08] operator / voice_transcript_partial / voice: use with guard hold position standby go no app to talk controller
  meta: kind=partial | timestamp=1777973528.4981024 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:08] operator / voice_transcript_partial / voice: use with guard hold position standby go no app to talk tracking
  meta: kind=partial | timestamp=1777973528.746259 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:10] operator / voice_transcript_final / voice: use wait app joke guard hold position standby go no app to talk tracking
  meta: kind=final | timestamp=1777973530.045669 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:14] operator / voice_transcript_partial / voice: can you
  meta: kind=partial | timestamp=1777973534.5542192 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:14] operator / voice_transcript_partial / voice: can you checking
  meta: kind=partial | timestamp=1777973534.805239 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:15] operator / voice_transcript_partial / voice: can you change
  meta: kind=partial | timestamp=1777973535.0756834 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:15] operator / voice_transcript_partial / voice: can you change the theme
  meta: kind=partial | timestamp=1777973535.306947 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:15] operator / voice_transcript_partial / voice: can you change the
  meta: kind=partial | timestamp=1777973535.5562148 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:15] operator / voice_transcript_partial / voice: can you change the talk less
  meta: kind=partial | timestamp=1777973535.815924 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:16] operator / voice_transcript_partial / voice: can you change the talk less to
  meta: kind=partial | timestamp=1777973536.310046 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:16] operator / voice_transcript_partial / voice: can you change the talk less to joke
  meta: kind=partial | timestamp=1777973536.8047354 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:17] operator / voice_transcript_partial / voice: can you change the talk less the boards
  meta: kind=partial | timestamp=1777973537.5126722 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:17] operator / voice_transcript_final / voice: talk less
  meta: kind=final | timestamp=1777973537.5954278 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:18] operator / voice_command / voice: talk less
  meta: normalized=True
- [2026-05-05 17:32:20] assistant / spoken_confirmation / voice: Understood. I will keep replies shorter and stop automatic assistant speech unless you ask for it.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 17:32:23] operator / voice_transcript_partial / voice: hunter
  meta: kind=partial | timestamp=1777973543.8483152 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:24] operator / voice_transcript_partial / voice: hi use
  meta: kind=partial | timestamp=1777973544.0846968 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:24] operator / voice_transcript_partial / voice: are you do
  meta: kind=partial | timestamp=1777973544.3402724 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:25] operator / voice_transcript_partial / voice: are you do hi
  meta: kind=partial | timestamp=1777973545.0953264 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:25] operator / voice_transcript_partial / voice: are you do hi repeat
  meta: kind=partial | timestamp=1777973545.395922 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:25] operator / voice_transcript_partial / voice: are you do hi repeat it
  meta: kind=partial | timestamp=1777973545.58497 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:25] operator / voice_transcript_partial / voice: are you do hey keep lion
  meta: kind=partial | timestamp=1777973545.8486707 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:26] operator / voice_transcript_partial / voice: are you do hey keep lion shortcuts
  meta: kind=partial | timestamp=1777973546.334422 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:26] operator / voice_transcript_final / voice: elion hi use do hey keep lion shortcuts
  meta: kind=final | timestamp=1777973546.893824 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:27] operator / voice_command / voice: elion hi use do hey keep lion shortcuts
  meta: normalized=True
- [2026-05-05 17:32:27] operator / voice_transcript_partial / voice: com
  meta: kind=partial | timestamp=1777973547.3444643 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:28] operator / voice_transcript_partial / voice: com port
  meta: kind=partial | timestamp=1777973548.0431814 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:28] operator / voice_transcript_partial / voice: stop on commands
  meta: kind=partial | timestamp=1777973548.0648131 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:28] operator / voice_transcript_partial / voice: stop on commands assistant
  meta: kind=partial | timestamp=1777973548.1019273 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:28] operator / voice_transcript_partial / voice: stop on commands assistant auto
  meta: kind=partial | timestamp=1777973548.5956073 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:28] operator / voice_transcript_partial / voice: stop on commands assistant change
  meta: kind=partial | timestamp=1777973548.8419683 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:29] operator / voice_transcript_partial / voice: stop on commands assistant change less
  meta: kind=partial | timestamp=1777973549.08888 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:29] operator / voice_transcript_partial / voice: stop on commands assistant change less you
  meta: kind=partial | timestamp=1777973549.3406973 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:29] operator / voice_transcript_partial / voice: stop on commands assistant change less you ask
  meta: kind=partial | timestamp=1777973549.7013383 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:30] operator / voice_transcript_final / voice: stop on commands assistant change less you ask
  meta: kind=final | timestamp=1777973550.7020445 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:32] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777973552.5623662 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:32] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777973552.709077 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:32] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777973552.9660916 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:33] operator / voice_transcript_partial / voice: tracking port
  meta: kind=partial | timestamp=1777973553.1980488 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:34] operator / voice_transcript_partial / voice: tracking port use
  meta: kind=partial | timestamp=1777973554.1953392 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:34] operator / voice_transcript_partial / voice: tracking port switch profile
  meta: kind=partial | timestamp=1777973554.4579587 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:34] operator / voice_transcript_partial / voice: tracking port switch app to the
  meta: kind=partial | timestamp=1777973554.6973262 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:34] operator / voice_transcript_partial / voice: tracking port switch app to controller
  meta: kind=partial | timestamp=1777973554.94768 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:35] operator / voice_transcript_partial / voice: tracking port switch app to resume guarding
  meta: kind=partial | timestamp=1777973555.2193267 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:35] operator / voice_transcript_partial / voice: tracking port switch app to resume guarding mode
  meta: kind=partial | timestamp=1777973555.7011752 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:35] operator / voice_transcript_final / voice: tracking port switch app to guard
  meta: kind=final | timestamp=1777973555.985391 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:36] operator / voice_command / voice: tracking port switch app to guard
  meta: normalized=True
- [2026-05-05 17:32:36] assistant / assistant_prompt / text: Queued your question behind the current reply.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 17:32:38] assistant / spoken_confirmation / voice: One moment. I will answer after the current reply.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 17:32:40] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777973560.9664054 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:41] operator / voice_transcript_final / voice: what board
  meta: kind=final | timestamp=1777973561.4712129 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:41] operator / voice_transcript_partial / voice: are you
  meta: kind=partial | timestamp=1777973561.944456 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:42] operator / voice_transcript_partial / voice: are you checking
  meta: kind=partial | timestamp=1777973562.7857306 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:42] operator / voice_transcript_partial / voice: are you to ask
  meta: kind=partial | timestamp=1777973562.7950292 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:43] operator / voice_transcript_partial / voice: are you to ask current
  meta: kind=partial | timestamp=1777973563.2138827 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:43] operator / voice_transcript_partial / voice: are you to ask current smart
  meta: kind=partial | timestamp=1777973563.6973152 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:43] operator / voice_transcript_partial / voice: are you to ask current smart sentry
  meta: kind=partial | timestamp=1777973563.952604 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:44] operator / voice_transcript_final / voice: are you to ask current smart
  meta: kind=final | timestamp=1777973564.7206314 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:52] operator / voice_transcript_partial / voice: a current
  meta: kind=partial | timestamp=1777973572.000029 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:52] operator / voice_transcript_partial / voice: a question
  meta: kind=partial | timestamp=1777973572.2359886 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:52] operator / voice_transcript_partial / voice: a question guard
  meta: kind=partial | timestamp=1777973572.735977 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:52] operator / voice_transcript_partial / voice: a question guard detection
  meta: kind=partial | timestamp=1777973572.9854267 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:53] operator / voice_transcript_final / voice: a question guard detection
  meta: kind=final | timestamp=1777973573.7384694 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:54] operator / voice_transcript_partial / voice: style
  meta: kind=partial | timestamp=1777973574.2357337 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:54] operator / voice_transcript_partial / voice: style abort
  meta: kind=partial | timestamp=1777973574.737073 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:54] operator / voice_transcript_final / voice: style alert
  meta: kind=final | timestamp=1777973574.992741 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:56] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777973576.235193 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:56] operator / voice_transcript_partial / voice: disable
  meta: kind=partial | timestamp=1777973576.7373405 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:56] operator / voice_transcript_partial / voice: disable shortcuts
  meta: kind=partial | timestamp=1777973576.9876406 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:57] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1777973577.2495115 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:57] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1777973577.508362 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:57] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777973577.735265 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:59] operator / voice_transcript_final / voice: face
  meta: kind=final | timestamp=1777973579.0117028 | source=final | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:59] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777973579.0192192 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:59] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1777973579.0247269 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:32:59] operator / voice_transcript_partial / voice: current style guard
  meta: kind=partial | timestamp=1777973579.2794414 | source=vosk | frequency_hz=382.0 | rms=537 | updated_at=1777973075.29867
- [2026-05-05 17:33:00] operator / voice_transcript_final / voice: current style guard
  meta: kind=final | timestamp=1777973580.1315544 | source=final | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:01] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777973581.880262 | source=vosk | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:02] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777973582.8721478 | source=vosk | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:03] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=projectile_servo; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 17:33:03] operator / voice_transcript_partial / voice: guard detection
  meta: kind=partial | timestamp=1777973583.1226468 | source=vosk | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:03] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777973583.3759892 | source=final | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:04] operator / voice_transcript_partial / voice: style
  meta: kind=partial | timestamp=1777973584.617584 | source=vosk | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:05] operator / voice_transcript_final / voice: style alert
  meta: kind=final | timestamp=1777973585.3816497 | source=final | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:06] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777973586.8706605 | source=vosk | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:07] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1777973587.371919 | source=final | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:07] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1777973587.6195023 | source=vosk | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:08] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777973588.731164 | source=vosk | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:08] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777973588.7449923 | source=vosk | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:08] operator / voice_transcript_final / voice: face me
  meta: kind=final | timestamp=1777973588.9951122 | source=final | frequency_hz=146.0 | rms=586 | updated_at=1777973579.6133711
- [2026-05-05 17:33:31] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777973611.0381255 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:31] operator / voice_transcript_partial / voice: not face
  meta: kind=partial | timestamp=1777973611.2688158 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:31] operator / voice_transcript_partial / voice: not voice style
  meta: kind=partial | timestamp=1777973611.767769 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:32] operator / voice_transcript_partial / voice: not face same
  meta: kind=partial | timestamp=1777973612.0266504 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:32] operator / voice_transcript_partial / voice: not face say
  meta: kind=partial | timestamp=1777973612.2698855 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:32] operator / voice_transcript_final / voice: your not face say
  meta: kind=final | timestamp=1777973612.9713829 | source=final | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:37] operator / voice_transcript_partial / voice: camera
  meta: kind=partial | timestamp=1777973617.7687001 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:38] operator / voice_transcript_final / voice: camera
  meta: kind=final | timestamp=1777973618.50968 | source=final | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:38] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777973618.5200996 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:39] operator / voice_transcript_partial / voice: lion keep listening
  meta: kind=partial | timestamp=1777973619.0230813 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:39] operator / voice_transcript_partial / voice: lion keep
  meta: kind=partial | timestamp=1777973619.912351 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:40] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 17:33:44] operator / voice_transcript_partial / voice: can
  meta: kind=partial | timestamp=1777973624.1833136 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:44] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777973624.4247499 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:45] operator / voice_transcript_partial / voice: can i lion
  meta: kind=partial | timestamp=1777973625.1886876 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:45] operator / voice_transcript_partial / voice: can i lion same
  meta: kind=partial | timestamp=1777973625.4274657 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:45] operator / voice_transcript_partial / voice: can i lion set
  meta: kind=partial | timestamp=1777973625.7190368 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:46] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 17:33:51] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777973631.6910923 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:51] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777973631.9437902 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:52] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777973632.1860864 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:52] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777973632.4377587 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:52] operator / voice_transcript_partial / voice: lion same
  meta: kind=partial | timestamp=1777973632.9362886 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:53] operator / voice_transcript_partial / voice: lion say
  meta: kind=partial | timestamp=1777973633.1978998 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:53] operator / voice_transcript_partial / voice: lion same but
  meta: kind=partial | timestamp=1777973633.4399965 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:53] operator / voice_transcript_partial / voice: lion say is not
  meta: kind=partial | timestamp=1777973633.6876385 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:54] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 17:33:58] operator / voice_transcript_partial / voice: can
  meta: kind=partial | timestamp=1777973638.444118 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:33:59] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777973639.9751794 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:00] operator / voice_transcript_final / voice: say
  meta: kind=final | timestamp=1777973640.3309631 | source=final | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:06] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777973646.195943 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:06] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777973646.4614894 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:06] operator / voice_transcript_partial / voice: can i face
  meta: kind=partial | timestamp=1777973646.717272 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:06] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777973646.9476068 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:07] operator / voice_transcript_partial / voice: can i hi say
  meta: kind=partial | timestamp=1777973647.4515018 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:07] operator / voice_transcript_partial / voice: can i hi say is not
  meta: kind=partial | timestamp=1777973647.9457061 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:08] operator / voice_transcript_partial / voice: can i hi say is not loading
  meta: kind=partial | timestamp=1777973648.2104466 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:08] operator / voice_transcript_partial / voice: can i hi say is not
  meta: kind=partial | timestamp=1777973648.469716 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:09] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=projectile_servo; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 17:34:09] operator / voice_transcript_final / voice: can i hi say is not board
  meta: kind=final | timestamp=1777973649.2625642 | source=final | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:11] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777973651.71548 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:12] operator / voice_transcript_final / voice: can i
  meta: kind=final | timestamp=1777973652.2352476 | source=final | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:12] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777973652.4643576 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:12] operator / voice_transcript_partial / voice: check status
  meta: kind=partial | timestamp=1777973652.9658065 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:13] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777973653.216833 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:13] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1777973653.5277817 | source=final | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:22] operator / voice_transcript_partial / voice: can
  meta: kind=partial | timestamp=1777973662.4677894 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:23] operator / voice_transcript_final / voice: board
  meta: kind=final | timestamp=1777973663.7264237 | source=final | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:28] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777973668.4971573 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:28] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777973668.7446117 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:29] operator / voice_transcript_partial / voice: can i lion
  meta: kind=partial | timestamp=1777973669.2716274 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:29] operator / voice_transcript_partial / voice: can i lion change
  meta: kind=partial | timestamp=1777973669.7470949 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:30] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 17:34:33] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777973673.2577553 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:33] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777973673.4960065 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:33] operator / voice_transcript_partial / voice: silence
  meta: kind=partial | timestamp=1777973673.7547932 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:33] operator / voice_transcript_partial / voice: profile
  meta: kind=partial | timestamp=1777973673.996082 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:34] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777973674.2462223 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:34] operator / voice_transcript_partial / voice: hi say
  meta: kind=partial | timestamp=1777973674.5111382 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:35] operator / voice_transcript_final / voice: i say
  meta: kind=final | timestamp=1777973675.313709 | source=final | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:38] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777973678.4948971 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:38] operator / voice_transcript_partial / voice: can i face
  meta: kind=partial | timestamp=1777973678.995726 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:39] operator / voice_transcript_partial / voice: can i hi
  meta: kind=partial | timestamp=1777973679.261557 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:39] operator / voice_transcript_partial / voice: can i hi say
  meta: kind=partial | timestamp=1777973679.7583961 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:40] operator / voice_transcript_partial / voice: can i hi say use model
  meta: kind=partial | timestamp=1777973680.2488675 | source=vosk | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:41] operator / voice_transcript_final / voice: can i hi say use model
  meta: kind=final | timestamp=1777973681.2952793 | source=final | frequency_hz=118.0 | rms=318 | updated_at=1777973593.7599566
- [2026-05-05 17:34:41] operator / voice_command / voice: can i hi say use model
  meta: normalized=True
- [2026-05-05 17:35:08] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777973708.8803363 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:09] operator / voice_transcript_final / voice: say
  meta: kind=final | timestamp=1777973709.6259778 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:23] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777973723.8658035 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:24] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777973724.1181724 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:24] operator / voice_transcript_partial / voice: can i lion
  meta: kind=partial | timestamp=1777973724.370374 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:24] operator / voice_transcript_partial / voice: can i talk less
  meta: kind=partial | timestamp=1777973724.6159008 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:24] operator / voice_transcript_partial / voice: can i talk
  meta: kind=partial | timestamp=1777973724.869177 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:25] operator / voice_transcript_partial / voice: can i hi say
  meta: kind=partial | timestamp=1777973725.3657362 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:25] operator / voice_transcript_final / voice: can i hi say
  meta: kind=final | timestamp=1777973725.8755553 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:58] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777973758.6185467 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:59] operator / voice_transcript_partial / voice: can not face
  meta: kind=partial | timestamp=1777973759.1185138 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:59] operator / voice_transcript_partial / voice: can i why
  meta: kind=partial | timestamp=1777973759.3684852 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:59] operator / voice_transcript_partial / voice: can i hi
  meta: kind=partial | timestamp=1777973759.6177373 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:35:59] operator / voice_transcript_partial / voice: can i hi change
  meta: kind=partial | timestamp=1777973759.8961842 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:00] operator / voice_transcript_partial / voice: can i hi change is not
  meta: kind=partial | timestamp=1777973760.387455 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:00] operator / voice_transcript_partial / voice: can i hi change is not loading
  meta: kind=partial | timestamp=1777973760.6194854 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:00] operator / voice_transcript_partial / voice: can i hi change is not
  meta: kind=partial | timestamp=1777973760.8667245 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:01] operator / voice_transcript_final / voice: can i hi change is not
  meta: kind=final | timestamp=1777973761.1781986 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:03] operator / voice_transcript_partial / voice: app
  meta: kind=partial | timestamp=1777973763.3701656 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:03] operator / voice_transcript_partial / voice: app to wait
  meta: kind=partial | timestamp=1777973763.6243908 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:03] operator / voice_transcript_partial / voice: app to be face
  meta: kind=partial | timestamp=1777973763.869395 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:04] operator / voice_transcript_partial / voice: app to be face recognition
  meta: kind=partial | timestamp=1777973764.124641 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:04] operator / voice_transcript_partial / voice: app to be face recognition connect
  meta: kind=partial | timestamp=1777973764.8857882 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:05] operator / voice_transcript_partial / voice: app to be face recognition not
  meta: kind=partial | timestamp=1777973765.1184218 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:05] operator / voice_transcript_partial / voice: app to be face recognition not face
  meta: kind=partial | timestamp=1777973765.3668644 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:05] operator / voice_transcript_partial / voice: app to be face recognition not
  meta: kind=partial | timestamp=1777973765.6658506 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:06] operator / voice_transcript_partial / voice: app to be face recognition not why face detection
  meta: kind=partial | timestamp=1777973766.1257517 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:06] operator / voice_transcript_partial / voice: app to be face recognition not hi say
  meta: kind=partial | timestamp=1777973766.3699794 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:06] operator / voice_transcript_partial / voice: app to be face recognition not hi say is not
  meta: kind=partial | timestamp=1777973766.6165366 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:06] operator / voice_transcript_partial / voice: app to be face recognition not hi say is not loading
  meta: kind=partial | timestamp=1777973766.8885446 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:07] operator / voice_transcript_partial / voice: app to be face recognition not hi say is not
  meta: kind=partial | timestamp=1777973767.1173692 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:07] operator / voice_transcript_final / voice: app to be face recognition not hi say use model
  meta: kind=final | timestamp=1777973767.3735073 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:09] operator / voice_transcript_partial / voice: give
  meta: kind=partial | timestamp=1777973769.1318123 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:09] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1777973769.378932 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:10] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 17:36:10] operator / voice_transcript_partial / voice: alion app to
  meta: kind=partial | timestamp=1777973770.3721879 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:10] operator / voice_transcript_partial / voice: alion app to be
  meta: kind=partial | timestamp=1777973770.617713 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:10] operator / voice_transcript_partial / voice: alion app to be current
  meta: kind=partial | timestamp=1777973770.8815854 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:11] operator / voice_transcript_partial / voice: alion app to be increase
  meta: kind=partial | timestamp=1777973771.146677 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:11] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 17:36:11] operator / voice_transcript_partial / voice: alion app to be face recognition
  meta: kind=partial | timestamp=1777973771.3833163 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:12] operator / voice_transcript_partial / voice: alion app to be face recognition is
  meta: kind=partial | timestamp=1777973772.8478377 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:13] operator / voice_transcript_partial / voice: alion app to be face recognition is not
  meta: kind=partial | timestamp=1777973773.1031966 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:14] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 17:36:14] operator / voice_transcript_final / voice: elion app to be face recognition is not
  meta: kind=final | timestamp=1777973774.2412152 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:15] operator / voice_command / voice: elion app to be face recognition is not
  meta: normalized=True
- [2026-05-05 17:36:22] operator / voice_transcript_partial / voice: can on
  meta: kind=partial | timestamp=1777973782.2292662 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:22] operator / voice_transcript_partial / voice: can on face
  meta: kind=partial | timestamp=1777973782.470835 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:22] operator / voice_transcript_partial / voice: can on hi
  meta: kind=partial | timestamp=1777973782.7110987 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:23] operator / voice_transcript_partial / voice: can on hi same
  meta: kind=partial | timestamp=1777973783.275747 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:23] operator / voice_transcript_partial / voice: can on hi say
  meta: kind=partial | timestamp=1777973783.5771534 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:23] operator / voice_transcript_partial / voice: can on hi say use nano
  meta: kind=partial | timestamp=1777973783.7693582 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:23] operator / voice_transcript_partial / voice: can on hi system is not loading
  meta: kind=partial | timestamp=1777973783.9740877 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:24] operator / voice_transcript_partial / voice: can on hi system is not
  meta: kind=partial | timestamp=1777973784.2177362 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:24] operator / voice_transcript_final / voice: can on hi system is not on
  meta: kind=final | timestamp=1777973784.7533023 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:26] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777973786.9502647 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:27] operator / voice_transcript_partial / voice: a question
  meta: kind=partial | timestamp=1777973787.2248394 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:27] operator / voice_transcript_partial / voice: a question guard
  meta: kind=partial | timestamp=1777973787.951231 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:28] operator / voice_transcript_partial / voice: a question guard detection
  meta: kind=partial | timestamp=1777973788.2000322 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:28] operator / voice_transcript_final / voice: a question guard detection
  meta: kind=final | timestamp=1777973788.4539902 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:29] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777973789.448159 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:29] operator / voice_transcript_partial / voice: set abort
  meta: kind=partial | timestamp=1777973789.696377 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:29] operator / voice_transcript_partial / voice: set abort current
  meta: kind=partial | timestamp=1777973789.9458675 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:30] operator / voice_transcript_partial / voice: say that serial
  meta: kind=partial | timestamp=1777973790.2111373 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:30] operator / voice_transcript_final / voice: set abort serial
  meta: kind=final | timestamp=1777973790.44986 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:31] operator / voice_transcript_partial / voice: human
  meta: kind=partial | timestamp=1777973791.1965313 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:31] operator / voice_transcript_partial / voice: serial
  meta: kind=partial | timestamp=1777973791.4481828 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:31] operator / voice_transcript_final / voice: serial
  meta: kind=final | timestamp=1777973791.9496853 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:32] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777973792.7059412 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:33] operator / voice_transcript_final / voice: speak
  meta: kind=final | timestamp=1777973793.2093065 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:33] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777973793.9554982 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:34] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1777973794.2334957 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:34] operator / voice_transcript_partial / voice: current status again
  meta: kind=partial | timestamp=1777973794.4522402 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:36:34] operator / voice_transcript_final / voice: current speak
  meta: kind=final | timestamp=1777973794.7025797 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:21] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but here is the deterministic face-runtime summary. Root cause: The face runtime looks loaded: backend=opencv_sface, ready_profiles=3/6. If matching still looks wrong, the issue is more likely scene quality, face size, or threshold tuning than a load failure. Runtime facts: camera_open=True, face_backend=opencv_sface, ready_profiles=3/6, preferred_backend=opencv_sface. Suggested fix: Capture a fresh live frame and compare face size, threshold, and profile sample quality. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 17:37:34] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777973854.7183523 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:34] operator / voice_transcript_partial / voice: strict
  meta: kind=partial | timestamp=1777973854.96763 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:35] operator / voice_transcript_partial / voice: strict on
  meta: kind=partial | timestamp=1777973855.2213166 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:35] operator / voice_transcript_partial / voice: decrease the guard
  meta: kind=partial | timestamp=1777973855.475976 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:35] operator / voice_transcript_partial / voice: decrease the guard detection
  meta: kind=partial | timestamp=1777973855.7568586 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:36] operator / voice_transcript_final / voice: decrease the guard detection
  meta: kind=final | timestamp=1777973856.5195029 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:36] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777973856.9674795 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:37] operator / voice_transcript_final / voice: set
  meta: kind=final | timestamp=1777973857.721482 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:39] operator / voice_transcript_partial / voice: best mode
  meta: kind=partial | timestamp=1777973859.4758816 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:40] operator / voice_transcript_partial / voice: disable face
  meta: kind=partial | timestamp=1777973860.2364774 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:40] operator / voice_transcript_partial / voice: disable face lion
  meta: kind=partial | timestamp=1777973860.4944081 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:40] operator / voice_transcript_partial / voice: disable face
  meta: kind=partial | timestamp=1777973860.7175775 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:40] operator / voice_transcript_partial / voice: disable face lion
  meta: kind=partial | timestamp=1777973860.9678407 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:41] operator / voice_transcript_partial / voice: disable face lion current
  meta: kind=partial | timestamp=1777973861.2317064 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:41] operator / voice_transcript_partial / voice: disable face lion current speak
  meta: kind=partial | timestamp=1777973861.7478662 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:42] operator / voice_transcript_partial / voice: disable face lion current speak change
  meta: kind=partial | timestamp=1777973862.4794748 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:43] operator / voice_transcript_final / voice: elion disable face lion current speak
  meta: kind=final | timestamp=1777973863.0493538 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:44] operator / voice_command / voice: elion disable face lion current speak
  meta: normalized=True
- [2026-05-05 17:37:47] assistant / spoken_confirmation / voice: Face recognition is now disabled.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 17:37:49] operator / voice_transcript_partial / voice: a question
  meta: kind=partial | timestamp=1777973869.9675174 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:50] operator / voice_transcript_partial / voice: a question for you
  meta: kind=partial | timestamp=1777973870.715057 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:50] operator / voice_transcript_partial / voice: a question for you checking
  meta: kind=partial | timestamp=1777973870.9758856 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:51] operator / voice_transcript_partial / voice: a question face recognition
  meta: kind=partial | timestamp=1777973871.310847 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:51] operator / voice_transcript_partial / voice: a question face recognition is
  meta: kind=partial | timestamp=1777973871.9676373 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:52] operator / voice_transcript_partial / voice: a question face recognition is not
  meta: kind=partial | timestamp=1777973872.219012 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:52] operator / voice_transcript_partial / voice: a question face recognition is not set
  meta: kind=partial | timestamp=1777973872.7193892 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:53] operator / voice_transcript_final / voice: a question face recognition is not say it
  meta: kind=final | timestamp=1777973873.2223434 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:37:53] operator / voice_command / voice: a question face recognition is not say it
  meta: normalized=True
- [2026-05-05 17:37:55] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 17:38:00] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777973880.2280803 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:00] operator / voice_transcript_partial / voice: that disconnect
  meta: kind=partial | timestamp=1777973880.4705331 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:00] operator / voice_transcript_partial / voice: that is not model
  meta: kind=partial | timestamp=1777973880.7172432 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:00] operator / voice_transcript_partial / voice: that is not question
  meta: kind=partial | timestamp=1777973880.9754035 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:01] operator / voice_transcript_partial / voice: that is not motion mode
  meta: kind=partial | timestamp=1777973881.2234757 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:01] operator / voice_transcript_partial / voice: that is not more strict on commands
  meta: kind=partial | timestamp=1777973881.7899816 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:02] operator / voice_transcript_partial / voice: that is not last command
  meta: kind=partial | timestamp=1777973882.1140263 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:02] operator / voice_transcript_final / voice: that is not last command
  meta: kind=final | timestamp=1777973882.2287612 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:02] operator / voice_transcript_partial / voice: decrease response
  meta: kind=partial | timestamp=1777973882.7204516 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:02] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777973882.9969728 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:05] operator / voice_transcript_final / voice: repeat
  meta: kind=final | timestamp=1777973885.4912689 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:05] operator / voice_transcript_partial / voice: boards
  meta: kind=partial | timestamp=1777973885.9866514 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:06] operator / voice_transcript_partial / voice: pause smart
  meta: kind=partial | timestamp=1777973886.2265632 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:06] operator / voice_transcript_partial / voice: pause smart sentry
  meta: kind=partial | timestamp=1777973886.4698606 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:07] operator / voice_transcript_final / voice: boards
  meta: kind=final | timestamp=1777973887.032981 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:22] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777973902.0739765 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:22] operator / voice_transcript_partial / voice: can i face
  meta: kind=partial | timestamp=1777973902.3470757 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:22] operator / voice_transcript_partial / voice: identify yourself
  meta: kind=partial | timestamp=1777973902.5778606 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:22] operator / voice_transcript_partial / voice: identify
  meta: kind=partial | timestamp=1777973902.8217802 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:23] operator / voice_transcript_partial / voice: identify say theme
  meta: kind=partial | timestamp=1777973903.0907614 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:23] operator / voice_transcript_partial / voice: identify say use nano
  meta: kind=partial | timestamp=1777973903.3248558 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:23] operator / voice_transcript_partial / voice: identify say
  meta: kind=partial | timestamp=1777973903.5752463 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:23] operator / voice_transcript_partial / voice: identify say use nano model
  meta: kind=partial | timestamp=1777973903.8226717 | source=vosk | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:24] operator / voice_transcript_final / voice: use nano model
  meta: kind=final | timestamp=1777973904.6448097 | source=final | frequency_hz=382.0 | rms=377 | updated_at=1777973707.3684025
- [2026-05-05 17:38:25] operator / voice_command / voice: use nano model
  meta: normalized=True
- [2026-05-05 17:38:28] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
