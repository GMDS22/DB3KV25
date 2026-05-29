# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-05 15:19:53
- Entries: 441
- Roles: {'assistant': 18, 'system': 1, 'operator': 422}
- Event types: {'assistant_prompt': 3, 'assistant_analysis': 2, 'voice_status': 1, 'spoken_confirmation': 11, 'voice_transcript_partial': 308, 'voice_transcript_final': 90, 'voice_command': 24, 'spoken_reply': 2}
- Channels: {'text': 5, 'voice': 436}
- Latest operator request: tracking
- Latest assistant message: I am still finishing assistant request about why help personality. I queued your runtime analysis request about the motion mode increase report recognition but loading. It is number 1 in line.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 15:06:13] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 15:06:13] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 15:06:15] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777964775.7207994 | source=vosk
- [2026-05-05 15:06:16] assistant / spoken_confirmation / voice: Smart Sentry AI is online. Ask a question or give a command when ready.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 15:06:20] operator / voice_transcript_partial / voice: analyze
  meta: kind=partial | timestamp=1777964780.9102752 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:06:21] operator / voice_transcript_final / voice: is
  meta: kind=final | timestamp=1777964781.660765 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:06:22] operator / voice_transcript_partial / voice: ask
  meta: kind=partial | timestamp=1777964782.6119213 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:06:22] operator / voice_transcript_partial / voice: ask a question
  meta: kind=partial | timestamp=1777964782.658949 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:06:23] operator / voice_transcript_final / voice: ask a question
  meta: kind=final | timestamp=1777964783.6596978 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:06:26] operator / voice_transcript_partial / voice: run
  meta: kind=partial | timestamp=1777964786.1577017 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:06:26] operator / voice_transcript_partial / voice: run the smart
  meta: kind=partial | timestamp=1777964786.4078307 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:06:26] operator / voice_transcript_partial / voice: run the smart sentry
  meta: kind=partial | timestamp=1777964786.6589994 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:06:27] operator / voice_transcript_final / voice: run the smart sentry
  meta: kind=final | timestamp=1777964787.6593244 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:12] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1777964832.6614947 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:12] operator / voice_transcript_partial / voice: me
  meta: kind=partial | timestamp=1777964832.9114277 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:13] operator / voice_transcript_partial / voice: me a
  meta: kind=partial | timestamp=1777964833.4088285 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:13] operator / voice_transcript_final / voice: me
  meta: kind=final | timestamp=1777964833.665077 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:14] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777964834.9130135 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:15] operator / voice_transcript_partial / voice: decrease silence
  meta: kind=partial | timestamp=1777964835.1602998 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:15] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777964835.412024 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:15] operator / voice_transcript_final / voice: decrease
  meta: kind=final | timestamp=1777964835.6633155 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:43] operator / voice_transcript_partial / voice: stop
  meta: kind=partial | timestamp=1777964863.1624892 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:43] operator / voice_transcript_final / voice: stop
  meta: kind=final | timestamp=1777964863.9350646 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:55] operator / voice_transcript_partial / voice: listening
  meta: kind=partial | timestamp=1777964875.412771 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:07:55] operator / voice_transcript_final / voice: listening
  meta: kind=final | timestamp=1777964875.9216695 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:05] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777964945.915284 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:06] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777964946.1661654 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:06] operator / voice_transcript_final / voice: resume
  meta: kind=final | timestamp=1777964946.9161587 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:07] operator / voice_transcript_partial / voice: me
  meta: kind=partial | timestamp=1777964947.4155443 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:07] operator / voice_transcript_partial / voice: medium model
  meta: kind=partial | timestamp=1777964947.6707504 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:07] operator / voice_transcript_partial / voice: medium the
  meta: kind=partial | timestamp=1777964947.920131 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:08] operator / voice_transcript_final / voice: medium the
  meta: kind=final | timestamp=1777964948.6688647 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:11] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1777964951.6659112 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:11] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:09:11] operator / voice_transcript_partial / voice: e leon
  meta: kind=partial | timestamp=1777964951.9163122 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:15] operator / voice_transcript_partial / voice: set brightness
  meta: kind=partial | timestamp=1777964955.4175074 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:15] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777964955.6685903 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:15] operator / voice_transcript_final / voice: say that
  meta: kind=final | timestamp=1777964955.918895 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:16] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777964956.4199092 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:17] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777964957.4152768 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:17] operator / voice_transcript_final / voice: to it
  meta: kind=final | timestamp=1777964957.9188223 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:19] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777964959.4160306 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:19] operator / voice_transcript_partial / voice: connect the
  meta: kind=partial | timestamp=1777964959.678947 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:19] operator / voice_transcript_partial / voice: connect the boards
  meta: kind=partial | timestamp=1777964959.9196784 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:20] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777964960.414927 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:20] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-05 15:09:21] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 15:09:25] operator / voice_transcript_partial / voice: response delay
  meta: kind=partial | timestamp=1777964965.6021836 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:25] operator / voice_transcript_final / voice: status
  meta: kind=final | timestamp=1777964965.9444199 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:29] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777964969.1683428 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:30] operator / voice_transcript_partial / voice: say smart
  meta: kind=partial | timestamp=1777964970.166235 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:30] operator / voice_transcript_partial / voice: say smart sentry
  meta: kind=partial | timestamp=1777964970.4167182 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:31] operator / voice_transcript_partial / voice: say smart sentry ask
  meta: kind=partial | timestamp=1777964971.416147 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:31] operator / voice_transcript_partial / voice: say smart sentry ask a question
  meta: kind=partial | timestamp=1777964971.667024 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:32] operator / voice_transcript_final / voice: can say smart sentry ask a question
  meta: kind=final | timestamp=1777964972.1724987 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:44] operator / voice_transcript_partial / voice: in hey
  meta: kind=partial | timestamp=1777964984.4158678 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:44] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777964984.6714654 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:45] operator / voice_transcript_partial / voice: enable the
  meta: kind=partial | timestamp=1777964985.233024 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:45] operator / voice_transcript_partial / voice: enable the face
  meta: kind=partial | timestamp=1777964985.422345 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:45] operator / voice_transcript_partial / voice: enable the face yolo
  meta: kind=partial | timestamp=1777964985.6652825 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:45] operator / voice_transcript_partial / voice: enable the face yolo recognition
  meta: kind=partial | timestamp=1777964985.916155 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:46] operator / voice_transcript_final / voice: enable face recognition
  meta: kind=final | timestamp=1777964986.9279425 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:47] operator / voice_command / voice: enable face recognition
  meta: normalized=True
- [2026-05-05 15:09:48] assistant / spoken_confirmation / voice: Face recognition is now enabled.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 15:09:50] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1777964990.4177113 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:50] operator / voice_transcript_partial / voice: face recognition
  meta: kind=partial | timestamp=1777964990.668137 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:51] operator / voice_transcript_partial / voice: face recognition is face
  meta: kind=partial | timestamp=1777964991.6679082 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:51] operator / voice_transcript_partial / voice: face recognition is tell
  meta: kind=partial | timestamp=1777964991.9186835 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:52] operator / voice_transcript_partial / voice: face recognition is tell a
  meta: kind=partial | timestamp=1777964992.1674914 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:52] operator / voice_transcript_partial / voice: face recognition is help
  meta: kind=partial | timestamp=1777964992.421178 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:53] operator / voice_transcript_final / voice: face recognition is help
  meta: kind=final | timestamp=1777964993.298482 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:09:53] operator / voice_command / voice: face recognition is help
  meta: normalized=True
- [2026-05-05 15:09:54] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 15:10:00] operator / voice_transcript_partial / voice: repeat that
  meta: kind=partial | timestamp=1777965000.3203657 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:01] operator / voice_transcript_final / voice: repeat that
  meta: kind=final | timestamp=1777965001.0968177 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:02] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777965002.8626354 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:02] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777965002.9106762 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:13] operator / voice_transcript_partial / voice: analyze
  meta: kind=partial | timestamp=1777965013.3828692 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:13] operator / voice_transcript_partial / voice: analyze the
  meta: kind=partial | timestamp=1777965013.869509 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:14] operator / voice_transcript_partial / voice: analyze the current
  meta: kind=partial | timestamp=1777965014.1201677 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:14] operator / voice_transcript_partial / voice: analyze the current app
  meta: kind=partial | timestamp=1777965014.3841202 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:14] operator / voice_transcript_partial / voice: analyze the current app run
  meta: kind=partial | timestamp=1777965014.620657 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:14] operator / voice_transcript_partial / voice: analyze the current app run tiny
  meta: kind=partial | timestamp=1777965014.8709528 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:15] operator / voice_transcript_partial / voice: analyze the current app run tiny model
  meta: kind=partial | timestamp=1777965015.1264153 | source=vosk | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:16] operator / voice_transcript_final / voice: analyze the current app run tiny
  meta: kind=final | timestamp=1777965016.4835954 | source=final | frequency_hz=278.0 | rms=926 | updated_at=1777964776.251171
- [2026-05-05 15:10:45] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777965045.5704346 | source=vosk | frequency_hz=370.0 | rms=343 | updated_at=1777965017.8122506
- [2026-05-05 15:10:46] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777965046.5692573 | source=final | frequency_hz=370.0 | rms=343 | updated_at=1777965017.8122506
- [2026-05-05 15:10:46] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:11:14] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777965074.397735 | source=vosk | frequency_hz=370.0 | rms=343 | updated_at=1777965017.8122506
- [2026-05-05 15:11:14] operator / voice_transcript_partial / voice: alien i have a question
  meta: kind=partial | timestamp=1777965074.8895266 | source=vosk | frequency_hz=370.0 | rms=343 | updated_at=1777965017.8122506
- [2026-05-05 15:11:15] operator / voice_transcript_final / voice: elion i have a question
  meta: kind=final | timestamp=1777965075.8406103 | source=final | frequency_hz=370.0 | rms=343 | updated_at=1777965017.8122506
- [2026-05-05 15:11:16] operator / voice_command / voice: elion i have a question
  meta: normalized=True
- [2026-05-05 15:11:17] assistant / spoken_confirmation / voice: I am listening. Ask your question.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 15:11:20] operator / voice_transcript_partial / voice: i
  meta: kind=partial | timestamp=1777965080.3793006 | source=vosk | frequency_hz=370.0 | rms=343 | updated_at=1777965017.8122506
- [2026-05-05 15:11:20] operator / voice_transcript_final / voice: i
  meta: kind=final | timestamp=1777965080.878352 | source=final | frequency_hz=370.0 | rms=343 | updated_at=1777965017.8122506
- [2026-05-05 15:11:21] operator / voice_transcript_partial / voice: ask
  meta: kind=partial | timestamp=1777965081.877594 | source=vosk | frequency_hz=370.0 | rms=343 | updated_at=1777965017.8122506
- [2026-05-05 15:11:21] operator / voice_transcript_partial / voice: ask a question
  meta: kind=partial | timestamp=1777965081.8816168 | source=vosk | frequency_hz=370.0 | rms=343 | updated_at=1777965017.8122506
- [2026-05-05 15:11:23] operator / voice_transcript_final / voice: ask a question
  meta: kind=final | timestamp=1777965083.16837 | source=final | frequency_hz=370.0 | rms=343 | updated_at=1777965017.8122506
- [2026-05-05 15:11:25] operator / voice_transcript_partial / voice: hi
  meta: kind=partial | timestamp=1777965085.4593105 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:11:25] operator / voice_transcript_partial / voice: hi can i
  meta: kind=partial | timestamp=1777965085.7091765 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:11:25] operator / voice_transcript_partial / voice: hi can i a
  meta: kind=partial | timestamp=1777965085.97184 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:11:26] operator / voice_transcript_partial / voice: hi can i a board
  meta: kind=partial | timestamp=1777965086.4584382 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:11:26] operator / voice_transcript_final / voice: hi can i a board
  meta: kind=final | timestamp=1777965086.9602234 | source=final | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:11:27] operator / voice_transcript_partial / voice: disconnect
  meta: kind=partial | timestamp=1777965087.4593747 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:11:27] operator / voice_transcript_partial / voice: the app
  meta: kind=partial | timestamp=1777965087.713841 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:11:28] operator / voice_transcript_final / voice: the app
  meta: kind=final | timestamp=1777965088.4609041 | source=final | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:11:56] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777965116.2107427 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:11:56] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:11:56] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777965116.470509 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:11:57] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777965117.3553402 | source=final | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:30] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777965150.9654713 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:31] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777965151.4633064 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:31] operator / voice_transcript_partial / voice: guard detection
  meta: kind=partial | timestamp=1777965151.7458308 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:32] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777965152.2108908 | source=final | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:32] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777965152.9635937 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:33] operator / voice_transcript_partial / voice: set abort
  meta: kind=partial | timestamp=1777965153.4979815 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:33] operator / voice_transcript_partial / voice: set personality
  meta: kind=partial | timestamp=1777965153.7132225 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:33] operator / voice_transcript_final / voice: set
  meta: kind=final | timestamp=1777965153.9746659 | source=final | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:35] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777965155.2363229 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:35] operator / voice_transcript_partial / voice: a lion best mode
  meta: kind=partial | timestamp=1777965155.7155595 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:36] operator / voice_transcript_final / voice: elion yes
  meta: kind=final | timestamp=1777965156.293821 | source=final | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:37] operator / voice_command / voice: elion yes
  meta: normalized=True
- [2026-05-05 15:12:36] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777965156.7126958 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:36] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777965156.9799302 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:37] operator / voice_transcript_final / voice: rest
  meta: kind=final | timestamp=1777965157.235477 | source=final | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:38] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777965158.2727566 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:38] operator / voice_transcript_partial / voice: current speed
  meta: kind=partial | timestamp=1777965158.285281 | source=vosk | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:39] operator / voice_transcript_final / voice: current speed
  meta: kind=final | timestamp=1777965159.488816 | source=final | frequency_hz=78.0 | rms=492 | updated_at=1777965083.703978
- [2026-05-05 15:12:59] operator / voice_transcript_partial / voice: check
  meta: kind=partial | timestamp=1777965179.5152442 | source=vosk | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:12:59] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777965179.7561114 | source=vosk | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:00] operator / voice_transcript_partial / voice: change of last
  meta: kind=partial | timestamp=1777965180.5131812 | source=vosk | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:01] operator / voice_transcript_partial / voice: change of why
  meta: kind=partial | timestamp=1777965181.0213318 | source=vosk | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:02] operator / voice_transcript_partial / voice: change of why sentinel
  meta: kind=partial | timestamp=1777965182.0070338 | source=vosk | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:02] operator / voice_transcript_partial / voice: change of why set personality
  meta: kind=partial | timestamp=1777965182.2591424 | source=vosk | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:02] operator / voice_transcript_partial / voice: change of why set yes
  meta: kind=partial | timestamp=1777965182.5074327 | source=vosk | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:03] operator / voice_transcript_final / voice: change of why set yes
  meta: kind=final | timestamp=1777965183.0296624 | source=final | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:04] operator / voice_transcript_partial / voice: personality
  meta: kind=partial | timestamp=1777965184.256842 | source=vosk | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:04] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777965184.5069697 | source=vosk | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:05] operator / voice_transcript_final / voice: ports
  meta: kind=final | timestamp=1777965185.0080063 | source=final | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:09] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777965189.7595546 | source=vosk | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:10] operator / voice_transcript_partial / voice: change theme
  meta: kind=partial | timestamp=1777965190.2647302 | source=vosk | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:10] operator / voice_transcript_final / voice: change theme
  meta: kind=final | timestamp=1777965190.962819 | source=final | frequency_hz=106.0 | rms=555 | updated_at=1777965159.9903204
- [2026-05-05 15:13:16] operator / voice_transcript_partial / voice: can you
  meta: kind=partial | timestamp=1777965196.6766055 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:17] operator / voice_transcript_partial / voice: can you app to
  meta: kind=partial | timestamp=1777965197.1533504 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:17] operator / voice_transcript_partial / voice: can you app to wait
  meta: kind=partial | timestamp=1777965197.4201322 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:17] operator / voice_transcript_partial / voice: can you app to wait disable
  meta: kind=partial | timestamp=1777965197.9027667 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:18] operator / voice_transcript_partial / voice: can you app to wait disable tracking
  meta: kind=partial | timestamp=1777965198.4039824 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:18] operator / voice_transcript_partial / voice: can you app to wait disable to your
  meta: kind=partial | timestamp=1777965198.6547647 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:18] operator / voice_transcript_partial / voice: can you app to wait disable to your help
  meta: kind=partial | timestamp=1777965198.9239728 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:19] operator / voice_transcript_final / voice: can you app to wait disable to your
  meta: kind=final | timestamp=1777965199.40556 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:20] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777965200.4142008 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:20] operator / voice_transcript_partial / voice: identify yourself
  meta: kind=partial | timestamp=1777965200.9056382 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:21] operator / voice_transcript_partial / voice: identify
  meta: kind=partial | timestamp=1777965201.4042659 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:21] operator / voice_transcript_partial / voice: identify same but
  meta: kind=partial | timestamp=1777965201.6714377 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:22] operator / voice_transcript_final / voice: identify same
  meta: kind=final | timestamp=1777965202.1567311 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:24] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777965204.5675764 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:24] operator / voice_transcript_partial / voice: disable
  meta: kind=partial | timestamp=1777965204.831869 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:25] operator / voice_transcript_final / voice: disable
  meta: kind=final | timestamp=1777965205.8180084 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:28] operator / voice_transcript_partial / voice: hi
  meta: kind=partial | timestamp=1777965208.0695238 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:28] operator / voice_transcript_partial / voice: hi same but
  meta: kind=partial | timestamp=1777965208.5675569 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:29] operator / voice_transcript_final / voice: hi same
  meta: kind=final | timestamp=1777965209.3401465 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:30] operator / voice_transcript_partial / voice: home disable
  meta: kind=partial | timestamp=1777965210.8210518 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:31] operator / voice_transcript_partial / voice: home disable the
  meta: kind=partial | timestamp=1777965211.3276894 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:32] operator / voice_transcript_final / voice: home disable the
  meta: kind=final | timestamp=1777965212.7142966 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:34] operator / voice_transcript_partial / voice: profile
  meta: kind=partial | timestamp=1777965214.188931 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:35] operator / voice_transcript_final / voice: profile
  meta: kind=final | timestamp=1777965215.1318262 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:35] operator / voice_transcript_partial / voice: is not
  meta: kind=partial | timestamp=1777965215.1389773 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:39] operator / voice_transcript_final / voice: not
  meta: kind=final | timestamp=1777965219.9320116 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:40] operator / voice_transcript_partial / voice: can i
  meta: kind=partial | timestamp=1777965220.6811006 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:41] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777965221.931106 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:42] operator / voice_transcript_final / voice: can i say
  meta: kind=final | timestamp=1777965222.6828687 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:50] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777965230.1920562 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:50] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777965230.4417477 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:13:51] operator / voice_transcript_final / voice: why else
  meta: kind=final | timestamp=1777965231.8921993 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:00] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1777965240.9849017 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:04] operator / voice_transcript_partial / voice: what are
  meta: kind=partial | timestamp=1777965244.6695068 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:06] operator / voice_transcript_partial / voice: but faster
  meta: kind=partial | timestamp=1777965246.4339993 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:25] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777965265.6822228 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:25] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777965265.9233925 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:26] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777965266.1715732 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:26] operator / voice_transcript_partial / voice: elliot tell
  meta: kind=partial | timestamp=1777965266.4238853 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:26] operator / voice_transcript_partial / voice: elliot tell me a
  meta: kind=partial | timestamp=1777965266.6893892 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:26] operator / voice_transcript_partial / voice: elliot tell me a joke
  meta: kind=partial | timestamp=1777965266.9230828 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:27] operator / voice_transcript_final / voice: elion tell me a joke
  meta: kind=final | timestamp=1777965267.739483 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:28] operator / voice_command / voice: elion tell me a joke
  meta: normalized=True
- [2026-05-05 15:14:28] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777965268.4237747 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:28] operator / voice_transcript_final / voice: why
  meta: kind=final | timestamp=1777965268.9775722 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:30] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] Parsed Intent: - action=none confidence=1.00 clarification=False Here is a sentry joke. I asked the turret for small talk, and it said it was still calibrating the punchline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 15:14:29] operator / voice_transcript_partial / voice: close camera
  meta: kind=partial | timestamp=1777965269.4217453 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:30] operator / voice_transcript_final / voice: close
  meta: kind=final | timestamp=1777965270.19979 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:31] assistant / spoken_reply / voice: Assistant update. Here is a sentry joke. I asked the turret for small talk, and it said it was still calibrating the punchline.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 15:14:32] assistant / spoken_confirmation / voice: Received. I started your assistant request about tell me a joke in the background.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 15:14:32] operator / voice_transcript_partial / voice: nano
  meta: kind=partial | timestamp=1777965272.5688488 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:32] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777965272.8587263 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:33] operator / voice_transcript_partial / voice: no personality
  meta: kind=partial | timestamp=1777965273.0704255 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:33] operator / voice_transcript_partial / voice: no ports
  meta: kind=partial | timestamp=1777965273.5623627 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:33] operator / voice_transcript_final / voice: no ports
  meta: kind=final | timestamp=1777965273.818887 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:34] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1777965274.5813115 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:35] operator / voice_transcript_partial / voice: assistant auto
  meta: kind=partial | timestamp=1777965275.0981073 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:35] operator / voice_transcript_final / voice: assistant
  meta: kind=final | timestamp=1777965275.5640945 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:37] operator / voice_transcript_partial / voice: i have
  meta: kind=partial | timestamp=1777965277.821483 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:38] operator / voice_transcript_partial / voice: i ask
  meta: kind=partial | timestamp=1777965278.078004 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:38] operator / voice_transcript_partial / voice: i ask a
  meta: kind=partial | timestamp=1777965278.3350184 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:38] operator / voice_transcript_partial / voice: i ask a joke
  meta: kind=partial | timestamp=1777965278.5733373 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:39] operator / voice_transcript_partial / voice: i ask a joke smart
  meta: kind=partial | timestamp=1777965279.063737 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:39] operator / voice_transcript_final / voice: i ask a joke
  meta: kind=final | timestamp=1777965279.3493412 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:39] operator / voice_transcript_partial / voice: wrong
  meta: kind=partial | timestamp=1777965279.5683115 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:40] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777965280.3511877 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:40] operator / voice_transcript_partial / voice: want to
  meta: kind=partial | timestamp=1777965280.8200374 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:14:41] operator / voice_transcript_final / voice: warm
  meta: kind=final | timestamp=1777965281.3156118 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:00] operator / voice_transcript_partial / voice: faster
  meta: kind=partial | timestamp=1777965300.8357697 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:06] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1777965306.8520799 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:07] operator / voice_transcript_partial / voice: hey open
  meta: kind=partial | timestamp=1777965307.8583705 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:07] operator / voice_transcript_partial / voice: hey go
  meta: kind=partial | timestamp=1777965307.8735905 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:08] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777965308.1276553 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:09] operator / voice_transcript_final / voice: hey guard
  meta: kind=final | timestamp=1777965309.1240036 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:11] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777965311.385449 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:11] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777965311.644745 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:11] operator / voice_transcript_partial / voice: stay paused
  meta: kind=partial | timestamp=1777965311.8744714 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:12] operator / voice_transcript_partial / voice: connect the
  meta: kind=partial | timestamp=1777965312.1266596 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:12] operator / voice_transcript_partial / voice: connect the last
  meta: kind=partial | timestamp=1777965312.3935719 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:12] operator / voice_transcript_partial / voice: stay not loading
  meta: kind=partial | timestamp=1777965312.6615307 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:13] operator / voice_transcript_partial / voice: say it again
  meta: kind=partial | timestamp=1777965313.1274943 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:13] operator / voice_transcript_partial / voice: connect the last task
  meta: kind=partial | timestamp=1777965313.3866334 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:13] operator / voice_transcript_partial / voice: connect the smart sentry
  meta: kind=partial | timestamp=1777965313.6258233 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:13] operator / voice_transcript_partial / voice: say it again start tracking
  meta: kind=partial | timestamp=1777965313.8760223 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:14] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777965314.1315463 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:15] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-05 15:15:18] assistant / spoken_confirmation / voice: Smart Sentry boards are already connected. What is next?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 15:15:19] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1777965319.238257 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:20] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777965320.8933716 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:21] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777965321.1938913 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:21] operator / voice_transcript_final / voice: smart sentry
  meta: kind=final | timestamp=1777965321.959381 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:23] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1777965323.6367598 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:23] operator / voice_transcript_partial / voice: personality
  meta: kind=partial | timestamp=1777965323.6790721 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:24] operator / voice_transcript_final / voice: personality
  meta: kind=final | timestamp=1777965324.39469 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:25] operator / voice_command / voice: personality
  meta: normalized=True
- [2026-05-05 15:15:27] operator / voice_transcript_partial / voice: faster
  meta: kind=partial | timestamp=1777965327.0561557 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:27] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777965327.1741138 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:28] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1777965328.6103108 | source=final | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:28] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777965328.6179543 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:28] operator / voice_transcript_partial / voice: what are
  meta: kind=partial | timestamp=1777965328.6265295 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:30] assistant / spoken_confirmation / voice: Received. I started your assistant request about personality in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 15:15:28] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777965328.8696365 | source=vosk | frequency_hz=314.0 | rms=288 | updated_at=1777965193.1479306
- [2026-05-05 15:15:31] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:15:32] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1777965332.7130227 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:32] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777965332.941885 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:33] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777965333.8964016 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:35] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:15:35] operator / voice_transcript_partial / voice: i
  meta: kind=partial | timestamp=1777965335.9356759 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:36] operator / voice_transcript_partial / voice: i start e lion
  meta: kind=partial | timestamp=1777965336.5660264 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:36] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:15:36] operator / voice_transcript_final / voice: i start e
  meta: kind=final | timestamp=1777965336.9900208 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:37] operator / voice_transcript_partial / voice: question
  meta: kind=partial | timestamp=1777965337.1608136 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:37] operator / voice_transcript_final / voice: question
  meta: kind=final | timestamp=1777965337.9277203 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:38] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777965338.1670282 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:39] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777965339.1869957 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:39] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1777965339.7185218 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:44] operator / voice_transcript_partial / voice: close
  meta: kind=partial | timestamp=1777965344.414627 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:44] operator / voice_transcript_partial / voice: close the
  meta: kind=partial | timestamp=1777965344.6623218 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:44] operator / voice_transcript_partial / voice: close the app
  meta: kind=partial | timestamp=1777965344.9120443 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:15:46] operator / voice_transcript_final / voice: close the app
  meta: kind=final | timestamp=1777965346.0714698 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:32] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=projectile_servo; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 15:16:33] assistant / spoken_reply / voice: Assistant update. Current runtime status: Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=projectile_servo; burst=6@70ms; return_delay=1. 50s; face=on; pir=on.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 15:16:49] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1777965409.6998866 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:50] operator / voice_transcript_partial / voice: hi system report
  meta: kind=partial | timestamp=1777965410.165751 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:50] operator / voice_transcript_final / voice: hi status
  meta: kind=final | timestamp=1777965410.4262915 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:51] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777965411.9145672 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:52] operator / voice_transcript_final / voice: status
  meta: kind=final | timestamp=1777965412.7075617 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:52] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777965412.9703176 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:53] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1777965413.1860619 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:54] operator / voice_transcript_final / voice: detection
  meta: kind=final | timestamp=1777965414.2835827 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:55] operator / voice_transcript_partial / voice: joke
  meta: kind=partial | timestamp=1777965415.4641263 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:55] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777965415.740549 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:55] operator / voice_transcript_partial / voice: tracking disconnect
  meta: kind=partial | timestamp=1777965415.9868836 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:56] operator / voice_transcript_partial / voice: tracking is not
  meta: kind=partial | timestamp=1777965416.2152307 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:56] operator / voice_transcript_partial / voice: tracking is not personality
  meta: kind=partial | timestamp=1777965416.7161162 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:57] operator / voice_transcript_final / voice: tracking not ports
  meta: kind=final | timestamp=1777965417.004552 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:57] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777965417.89937 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:58] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1777965418.3671944 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:58] operator / voice_transcript_partial / voice: switch
  meta: kind=partial | timestamp=1777965418.497143 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:58] operator / voice_transcript_partial / voice: switch profile
  meta: kind=partial | timestamp=1777965418.743594 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:59] operator / voice_transcript_final / voice: switch
  meta: kind=final | timestamp=1777965419.5004976 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:16:59] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777965419.7444198 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:00] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777965420.7249267 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:01] operator / voice_transcript_partial / voice: to ask
  meta: kind=partial | timestamp=1777965421.4696913 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:01] operator / voice_transcript_partial / voice: rest
  meta: kind=partial | timestamp=1777965421.7176533 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:02] operator / voice_transcript_final / voice: smart rest
  meta: kind=final | timestamp=1777965422.2220104 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:04] operator / voice_transcript_partial / voice: personality
  meta: kind=partial | timestamp=1777965424.2274857 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:04] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1777965424.7434616 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:05] operator / voice_transcript_final / voice: boards
  meta: kind=final | timestamp=1777965425.3644454 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:05] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777965425.7147048 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:06] operator / voice_transcript_partial / voice: set speed
  meta: kind=partial | timestamp=1777965426.4833863 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:06] operator / voice_transcript_final / voice: set
  meta: kind=final | timestamp=1777965426.7179246 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:07] operator / voice_transcript_partial / voice: controller
  meta: kind=partial | timestamp=1777965427.216408 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:07] operator / voice_transcript_partial / voice: tiny
  meta: kind=partial | timestamp=1777965427.8401973 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:07] operator / voice_transcript_partial / voice: tiny model
  meta: kind=partial | timestamp=1777965427.8736804 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:08] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777965428.4790382 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:08] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777965428.96654 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:09] operator / voice_transcript_partial / voice: smart default
  meta: kind=partial | timestamp=1777965429.2171052 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:09] operator / voice_transcript_partial / voice: smart give another
  meta: kind=partial | timestamp=1777965429.5393412 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:10] operator / voice_transcript_final / voice: tiny smart give
  meta: kind=final | timestamp=1777965430.036985 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:10] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1777965430.7205727 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:11] operator / voice_transcript_partial / voice: not loading
  meta: kind=partial | timestamp=1777965431.3092508 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:11] operator / voice_transcript_final / voice: not loading
  meta: kind=final | timestamp=1777965431.4815836 | source=final | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:14] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777965434.6041894 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:15] operator / voice_transcript_partial / voice: why face
  meta: kind=partial | timestamp=1777965435.2791083 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:15] operator / voice_transcript_partial / voice: lion personality
  meta: kind=partial | timestamp=1777965435.5280313 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:16] operator / voice_transcript_partial / voice: lion close camera
  meta: kind=partial | timestamp=1777965436.2161496 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:17] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:17:26] operator / voice_transcript_partial / voice: eileen app
  meta: kind=partial | timestamp=1777965446.4825623 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:27] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:17:31] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777965451.7260811 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:31] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777965451.9700358 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:32] operator / voice_transcript_partial / voice: lion no
  meta: kind=partial | timestamp=1777965452.487646 | source=vosk | frequency_hz=314.0 | rms=331 | updated_at=1777965329.3673723
- [2026-05-05 15:17:33] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:17:37] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777965457.2078285 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:17:37] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777965457.6206794 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:17:37] operator / voice_transcript_partial / voice: why your help
  meta: kind=partial | timestamp=1777965457.7069452 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:17:39] operator / voice_transcript_partial / voice: why your help voice
  meta: kind=partial | timestamp=1777965459.0138457 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:17:39] operator / voice_transcript_final / voice: why your help
  meta: kind=final | timestamp=1777965459.6197765 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:17:40] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1777965460.766784 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:17:41] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777965461.008922 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:17:41] operator / voice_transcript_partial / voice: that nano model
  meta: kind=partial | timestamp=1777965461.551222 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:17:42] operator / voice_transcript_final / voice: that help
  meta: kind=final | timestamp=1777965462.29376 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:07] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1777965487.9998682 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:08] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777965488.2787797 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:09] operator / voice_transcript_final / voice: what
  meta: kind=final | timestamp=1777965489.045999 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:14] operator / voice_transcript_partial / voice: personality
  meta: kind=partial | timestamp=1777965494.267385 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:15] operator / voice_transcript_partial / voice: voice style
  meta: kind=partial | timestamp=1777965495.4991968 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:16] operator / voice_transcript_partial / voice: voice style help
  meta: kind=partial | timestamp=1777965496.3257055 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:16] operator / voice_transcript_partial / voice: voice style help personality
  meta: kind=partial | timestamp=1777965496.5357792 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:17] operator / voice_transcript_final / voice: voice style help
  meta: kind=final | timestamp=1777965497.1827369 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:18] operator / voice_command / voice: voice style help
  meta: normalized=True
- [2026-05-05 15:18:20] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 15:18:22] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777965502.7833076 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:23] operator / voice_transcript_partial / voice: that is not
  meta: kind=partial | timestamp=1777965503.0133617 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:23] operator / voice_transcript_partial / voice: that is not loading
  meta: kind=partial | timestamp=1777965503.2559886 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:23] operator / voice_transcript_partial / voice: that is not
  meta: kind=partial | timestamp=1777965503.500553 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:23] operator / voice_transcript_partial / voice: that is not motion mode
  meta: kind=partial | timestamp=1777965503.7845118 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:24] operator / voice_transcript_final / voice: that is not that
  meta: kind=final | timestamp=1777965504.4455478 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:32] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777965512.2696965 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:32] operator / voice_transcript_partial / voice: hi repeat
  meta: kind=partial | timestamp=1777965512.5080378 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:33] operator / voice_transcript_final / voice: repeat
  meta: kind=final | timestamp=1777965513.0346057 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:33] operator / voice_transcript_partial / voice: personality
  meta: kind=partial | timestamp=1777965513.798081 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:33] operator / voice_transcript_partial / voice: for
  meta: kind=partial | timestamp=1777965513.8110766 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:33] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1777965513.8391585 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:34] operator / voice_transcript_partial / voice: resume guarding mode
  meta: kind=partial | timestamp=1777965514.079368 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:34] operator / voice_transcript_final / voice: say guard
  meta: kind=final | timestamp=1777965514.9847918 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:37] operator / voice_transcript_partial / voice: the board another
  meta: kind=partial | timestamp=1777965517.5768378 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:37] operator / voice_transcript_partial / voice: the be more strict
  meta: kind=partial | timestamp=1777965517.816698 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:38] operator / voice_transcript_final / voice: the board mode
  meta: kind=final | timestamp=1777965518.5604055 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:48] operator / voice_transcript_partial / voice: silence threshold
  meta: kind=partial | timestamp=1777965528.580827 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:49] operator / voice_transcript_final / voice: link
  meta: kind=final | timestamp=1777965529.0997016 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:56] operator / voice_transcript_partial / voice: hi
  meta: kind=partial | timestamp=1777965536.3139474 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:56] operator / voice_transcript_partial / voice: hi cancel
  meta: kind=partial | timestamp=1777965536.6254327 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:56] operator / voice_transcript_partial / voice: hi
  meta: kind=partial | timestamp=1777965536.8331501 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:57] operator / voice_transcript_partial / voice: personality
  meta: kind=partial | timestamp=1777965537.3102093 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:57] operator / voice_transcript_partial / voice: hi voice
  meta: kind=partial | timestamp=1777965537.5557566 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:57] operator / voice_transcript_final / voice: hi ports
  meta: kind=final | timestamp=1777965537.8834097 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:58] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777965538.6136465 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:58] operator / voice_transcript_partial / voice: hold position
  meta: kind=partial | timestamp=1777965538.812663 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:59] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777965539.0777655 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:59] operator / voice_transcript_partial / voice: but app
  meta: kind=partial | timestamp=1777965539.3331022 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:18:59] operator / voice_transcript_partial / voice: but app why
  meta: kind=partial | timestamp=1777965539.817348 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:00] operator / voice_transcript_partial / voice: but app hi repeat
  meta: kind=partial | timestamp=1777965540.1139243 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:00] operator / voice_transcript_partial / voice: but app to
  meta: kind=partial | timestamp=1777965540.9406765 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:01] operator / voice_transcript_partial / voice: but app hi repeat aileen close camera
  meta: kind=partial | timestamp=1777965541.075238 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:02] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:19:03] operator / voice_transcript_partial / voice: loading
  meta: kind=partial | timestamp=1777965543.812405 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:04] operator / voice_transcript_partial / voice: loading loading
  meta: kind=partial | timestamp=1777965544.3346987 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:04] operator / voice_transcript_partial / voice: loading loading that
  meta: kind=partial | timestamp=1777965544.5814035 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:05] operator / voice_transcript_final / voice: loading loading that
  meta: kind=final | timestamp=1777965545.4505646 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:07] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777965547.836196 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:09] operator / voice_transcript_partial / voice: why personality
  meta: kind=partial | timestamp=1777965549.0865383 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:09] operator / voice_transcript_partial / voice: lion close camera
  meta: kind=partial | timestamp=1777965549.479787 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:09] operator / voice_transcript_final / voice: why yourself
  meta: kind=final | timestamp=1777965549.9178774 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:12] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777965552.5808163 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:13] operator / voice_transcript_partial / voice: why face
  meta: kind=partial | timestamp=1777965553.078471 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:13] operator / voice_transcript_partial / voice: why help
  meta: kind=partial | timestamp=1777965553.3368828 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:13] operator / voice_transcript_partial / voice: why help personality
  meta: kind=partial | timestamp=1777965553.8523088 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:14] operator / voice_transcript_final / voice: why help personality
  meta: kind=final | timestamp=1777965554.621716 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:16] operator / voice_command / voice: why help personality
  meta: normalized=True
- [2026-05-05 15:19:15] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777965555.0831902 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:16] operator / voice_transcript_partial / voice: the motion mode
  meta: kind=partial | timestamp=1777965556.0805411 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:16] operator / voice_transcript_partial / voice: the com
  meta: kind=partial | timestamp=1777965556.333451 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:16] operator / voice_transcript_partial / voice: the motion mode personality
  meta: kind=partial | timestamp=1777965556.5572484 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:16] operator / voice_transcript_partial / voice: the motion mode increase recognition
  meta: kind=partial | timestamp=1777965556.8253303 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:17] operator / voice_transcript_partial / voice: the motion mode increase report
  meta: kind=partial | timestamp=1777965557.325921 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:17] operator / voice_transcript_partial / voice: the motion mode increase report eileen but
  meta: kind=partial | timestamp=1777965557.5592635 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:17] operator / voice_transcript_partial / voice: the motion mode increase report eileen but faster
  meta: kind=partial | timestamp=1777965557.8243475 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:18] operator / voice_transcript_partial / voice: the motion mode increase report aileen be less
  meta: kind=partial | timestamp=1777965558.136947 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:18] operator / voice_transcript_partial / voice: the motion mode increase recognition not loading
  meta: kind=partial | timestamp=1777965558.3394494 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:20] assistant / spoken_confirmation / voice: Received. I started your assistant request about why help personality in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 15:19:19] operator / voice_transcript_final / voice: the motion mode increase report recognition but loading
  meta: kind=final | timestamp=1777965559.0924883 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:20] operator / voice_command / voice: the motion mode increase report recognition but loading
  meta: normalized=True
- [2026-05-05 15:19:21] assistant / assistant_analysis / text: Assistant request queued: runtime analysis request about the motion mode increase report recognition but loading (position 1).
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 15:19:19] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1777965559.339139 | source=vosk | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:20] operator / voice_transcript_final / voice: on
  meta: kind=final | timestamp=1777965560.3817835 | source=final | frequency_hz=408.0 | rms=295 | updated_at=1777965456.4536548
- [2026-05-05 15:19:23] assistant / spoken_confirmation / voice: I am still finishing assistant request about why help personality. I queued your runtime analysis request about the motion mode increase report recognition but loading. It is number 1 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 15:19:26] operator / voice_transcript_partial / voice: medium
  meta: kind=partial | timestamp=1777965566.5020905 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:26] operator / voice_transcript_partial / voice: human
  meta: kind=partial | timestamp=1777965566.7307603 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:27] operator / voice_transcript_partial / voice: human never
  meta: kind=partial | timestamp=1777965567.18708 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:27] operator / voice_transcript_partial / voice: you motion app to
  meta: kind=partial | timestamp=1777965567.4321165 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:27] operator / voice_transcript_partial / voice: human never clear the
  meta: kind=partial | timestamp=1777965567.5885575 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:27] operator / voice_transcript_partial / voice: human never clear the smart
  meta: kind=partial | timestamp=1777965567.803566 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:28] operator / voice_transcript_partial / voice: human never clear the
  meta: kind=partial | timestamp=1777965568.077332 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:28] operator / voice_transcript_partial / voice: human never clear
  meta: kind=partial | timestamp=1777965568.297525 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:28] operator / voice_transcript_partial / voice: human never clear auto current
  meta: kind=partial | timestamp=1777965568.5076845 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:29] operator / voice_transcript_partial / voice: human never clear auto current app
  meta: kind=partial | timestamp=1777965569.0717669 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:29] operator / voice_transcript_partial / voice: human never clear auto current open camera
  meta: kind=partial | timestamp=1777965569.3207996 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:29] operator / voice_transcript_partial / voice: human never clear auto current open nano enable
  meta: kind=partial | timestamp=1777965569.7236955 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:30] operator / voice_transcript_partial / voice: human never clear auto current open current app again
  meta: kind=partial | timestamp=1777965570.01699 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:30] operator / voice_transcript_partial / voice: human never clear auto current open nano enable alion repeat
  meta: kind=partial | timestamp=1777965570.2213879 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:30] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:19:30] operator / voice_transcript_partial / voice: human never clear auto current open nano enable alion repeat it
  meta: kind=partial | timestamp=1777965570.7926464 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:30] operator / voice_transcript_partial / voice: human never clear auto current open nano enable alion repeat that
  meta: kind=partial | timestamp=1777965570.8909547 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:31] operator / voice_transcript_partial / voice: human never clear auto current open nano enable alion repeat it is in nano
  meta: kind=partial | timestamp=1777965571.3676393 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:31] operator / voice_transcript_partial / voice: human never clear auto current open nano enable alion repeat that me
  meta: kind=partial | timestamp=1777965571.7068675 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:31] operator / voice_transcript_partial / voice: human never clear auto current open nano enable alion repeat that me leon
  meta: kind=partial | timestamp=1777965571.9030588 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:32] operator / voice_transcript_partial / voice: human never clear auto current open nano enable alion repeat that me alien
  meta: kind=partial | timestamp=1777965572.0826683 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:32] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:19:34] operator / voice_transcript_partial / voice: human voice
  meta: kind=partial | timestamp=1777965574.0861652 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:34] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777965574.2988057 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:34] operator / voice_transcript_partial / voice: the nano model
  meta: kind=partial | timestamp=1777965574.5853148 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:34] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777965574.8023973 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:38] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777965578.1631312 | source=final | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:39] operator / voice_transcript_partial / voice: i want
  meta: kind=partial | timestamp=1777965579.6421185 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:39] operator / voice_transcript_partial / voice: report
  meta: kind=partial | timestamp=1777965579.6501627 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:39] operator / voice_transcript_partial / voice: loading conversation
  meta: kind=partial | timestamp=1777965579.87892 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:40] operator / voice_transcript_partial / voice: loading personality
  meta: kind=partial | timestamp=1777965580.147746 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:40] operator / voice_transcript_partial / voice: loading boards alien
  meta: kind=partial | timestamp=1777965580.5076814 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:40] operator / voice_transcript_partial / voice: loading boards alien question
  meta: kind=partial | timestamp=1777965580.6868823 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:40] operator / voice_transcript_partial / voice: loading boards alien last
  meta: kind=partial | timestamp=1777965580.917724 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:41] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 15:19:45] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777965585.635296 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:45] operator / voice_transcript_partial / voice: is not
  meta: kind=partial | timestamp=1777965585.8550806 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:46] operator / voice_transcript_final / voice: is not
  meta: kind=final | timestamp=1777965586.6194925 | source=final | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:51] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777965591.4399774 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:51] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777965591.7201676 | source=vosk | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
- [2026-05-05 15:19:51] operator / voice_transcript_final / voice: tracking
  meta: kind=final | timestamp=1777965591.9869795 | source=final | frequency_hz=202.0 | rms=588 | updated_at=1777965565.9983068
