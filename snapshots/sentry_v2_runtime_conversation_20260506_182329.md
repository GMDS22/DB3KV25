# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-06 18:23:29
- Entries: 134
- Roles: {'assistant': 13, 'system': 1, 'operator': 120}
- Event types: {'assistant_prompt': 2, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_final': 15, 'voice_transcript_partial': 94, 'voice_command': 11, 'spoken_confirmation': 10}
- Channels: {'text': 3, 'voice': 131}
- Latest operator request: resume guarding mode
- Latest assistant message: Resuming guarding mode now.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-06 18:18:20] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 18:18:20] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 18:18:21] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778062701.2307098 | source=vosk
- [2026-05-06 18:18:58] operator / voice_transcript_final / voice: hey
  meta: kind=final | timestamp=1778062738.0679498 | source=final | frequency_hz=372.0 | rms=271 | updated_at=1778062710.4770844
- [2026-05-06 18:19:32] operator / voice_transcript_final / voice: hey
  meta: kind=final | timestamp=1778062772.9399753 | source=final | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:19:54] operator / voice_transcript_final / voice: hey
  meta: kind=final | timestamp=1778062794.0731716 | source=final | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:20:46] operator / voice_transcript_partial / voice: off
  meta: kind=partial | timestamp=1778062846.6938944 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:20:47] operator / voice_transcript_final / voice: off
  meta: kind=final | timestamp=1778062847.5412412 | source=final | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:44] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1778062904.7892423 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:45] operator / voice_transcript_partial / voice: e assistant
  meta: kind=partial | timestamp=1778062905.048757 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:45] operator / voice_transcript_partial / voice: deactivate
  meta: kind=partial | timestamp=1778062905.294493 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:45] operator / voice_transcript_partial / voice: deactivate manual
  meta: kind=partial | timestamp=1778062905.547325 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:45] operator / voice_transcript_partial / voice: deactivate the after loss
  meta: kind=partial | timestamp=1778062905.7887998 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:46] operator / voice_transcript_partial / voice: deactivate the after
  meta: kind=partial | timestamp=1778062906.0424414 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:46] operator / voice_transcript_partial / voice: deactivate the after precision
  meta: kind=partial | timestamp=1778062906.2945879 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:46] operator / voice_transcript_partial / voice: deactivate the after precision no detection
  meta: kind=partial | timestamp=1778062906.7991545 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:47] operator / voice_transcript_partial / voice: deactivate the after precision make a greeting
  meta: kind=partial | timestamp=1778062907.0411859 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:47] operator / voice_transcript_partial / voice: deactivate the after precision logging loop
  meta: kind=partial | timestamp=1778062907.2908301 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:47] operator / voice_transcript_partial / voice: deactivate the after precision make a joke
  meta: kind=partial | timestamp=1778062907.5383782 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:48] operator / voice_transcript_partial / voice: deactivate the after precision make a joke response
  meta: kind=partial | timestamp=1778062908.040874 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:48] operator / voice_transcript_partial / voice: deactivate the after precision make a joke switch voice
  meta: kind=partial | timestamp=1778062908.5439687 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:48] operator / voice_transcript_partial / voice: deactivate the after precision make a joke visual the assistant
  meta: kind=partial | timestamp=1778062908.790088 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:49] operator / voice_transcript_partial / voice: deactivate the after precision make a joke switch voice speech
  meta: kind=partial | timestamp=1778062909.542731 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:49] operator / voice_transcript_partial / voice: deactivate the after precision make a joke visual overlay status keyboard controls
  meta: kind=partial | timestamp=1778062909.789404 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:50] operator / voice_transcript_partial / voice: deactivate the after precision make a joke switch voice speak cue
  meta: kind=partial | timestamp=1778062910.0431945 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:50] operator / voice_transcript_partial / voice: deactivate the after precision make a joke switch voice speak cue guard
  meta: kind=partial | timestamp=1778062910.3085744 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:50] operator / voice_transcript_partial / voice: deactivate the after precision make a joke switch voice speak cue guard cleanup
  meta: kind=partial | timestamp=1778062910.5421739 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:50] operator / voice_transcript_partial / voice: deactivate the after precision make a joke switch voice speak cue guard close show
  meta: kind=partial | timestamp=1778062910.7899914 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:52] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 18:21:52] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778062912.2138975 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:52] operator / voice_transcript_partial / voice: is suppress
  meta: kind=partial | timestamp=1778062912.539545 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:52] operator / voice_transcript_partial / voice: is spare ml
  meta: kind=partial | timestamp=1778062912.7976491 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:53] operator / voice_transcript_partial / voice: is spare manual
  meta: kind=partial | timestamp=1778062913.0379872 | source=vosk | frequency_hz=296.0 | rms=473 | updated_at=1778062738.821304
- [2026-05-06 18:21:54] assistant / spoken_confirmation / voice: Yes. What do you want to know?
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 18:21:57] operator / voice_transcript_partial / voice: alien is target
  meta: kind=partial | timestamp=1778062917.8015926 | source=vosk | frequency_hz=100.7 | rms=816 | updated_at=1778062915.8940625
- [2026-05-06 18:21:57] operator / voice_transcript_partial / voice: alien is targets running
  meta: kind=partial | timestamp=1778062917.9071271 | source=vosk | frequency_hz=100.7 | rms=816 | updated_at=1778062915.8940625
- [2026-05-06 18:21:58] operator / voice_transcript_partial / voice: alien is targets running name
  meta: kind=partial | timestamp=1778062918.9038527 | source=vosk | frequency_hz=100.7 | rms=816 | updated_at=1778062915.8940625
- [2026-05-06 18:22:00] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 18:22:01] assistant / spoken_confirmation / voice: I am here. Ask your question.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 18:22:05] operator / voice_transcript_partial / voice: e ask
  meta: kind=partial | timestamp=1778062925.1589386 | source=vosk | frequency_hz=100.7 | rms=816 | updated_at=1778062915.8940625
- [2026-05-06 18:22:05] operator / voice_transcript_partial / voice: e ask a question
  meta: kind=partial | timestamp=1778062925.1663964 | source=vosk | frequency_hz=100.7 | rms=816 | updated_at=1778062915.8940625
- [2026-05-06 18:22:06] operator / voice_transcript_final / voice: e ask a question
  meta: kind=final | timestamp=1778062926.4731405 | source=final | frequency_hz=194.0 | rms=479 | updated_at=1778062925.9104192
- [2026-05-06 18:22:06] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1778062926.531272 | source=vosk | frequency_hz=194.0 | rms=479 | updated_at=1778062925.9104192
- [2026-05-06 18:22:06] operator / voice_transcript_partial / voice: who are you
  meta: kind=partial | timestamp=1778062926.6660283 | source=vosk | frequency_hz=194.0 | rms=479 | updated_at=1778062925.9104192
- [2026-05-06 18:22:07] operator / voice_transcript_final / voice: who are you
  meta: kind=final | timestamp=1778062927.5693376 | source=final | frequency_hz=194.0 | rms=479 | updated_at=1778062925.9104192
- [2026-05-06 18:22:07] operator / voice_command / voice: who are you
  meta: normalized=True
- [2026-05-06 18:22:16] operator / voice_transcript_partial / voice: standby guard
  meta: kind=partial | timestamp=1778062936.5890758 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:16] operator / voice_transcript_partial / voice: standby guard no
  meta: kind=partial | timestamp=1778062936.8367398 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:17] operator / voice_transcript_partial / voice: standby guard no active
  meta: kind=partial | timestamp=1778062937.3419707 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:17] operator / voice_transcript_partial / voice: standby guard no active target
  meta: kind=partial | timestamp=1778062937.5881653 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:18] operator / voice_transcript_partial / voice: standby guard no active targets running
  meta: kind=partial | timestamp=1778062938.032614 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:18] operator / voice_transcript_partial / voice: standby guard no active targets running no
  meta: kind=partial | timestamp=1778062938.451873 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:18] operator / voice_transcript_partial / voice: standby guard no active targets running no tell me
  meta: kind=partial | timestamp=1778062938.87002 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:19] operator / voice_transcript_partial / voice: standby guard no active targets running no tell me a
  meta: kind=partial | timestamp=1778062939.087955 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:19] operator / voice_transcript_partial / voice: standby guard no active targets running no tell me a do
  meta: kind=partial | timestamp=1778062939.3467708 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:20] operator / voice_transcript_final / voice: standby guard no active targets running no tell me a do
  meta: kind=final | timestamp=1778062940.2547135 | source=final | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:25] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778062945.1070263 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:25] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 18:22:26] operator / voice_transcript_partial / voice: alion turn
  meta: kind=partial | timestamp=1778062946.118729 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:26] operator / voice_transcript_partial / voice: alion tell me a
  meta: kind=partial | timestamp=1778062946.3507924 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:26] operator / voice_transcript_partial / voice: alion tell me
  meta: kind=partial | timestamp=1778062946.609243 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:27] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 18:22:28] assistant / assistant_prompt / text: I am Elion Mesk, Elion for short. I am the AI assistant voice inside Smart Sentry.
  meta: task_kind=prompt | speak_requested=True
- [2026-05-06 18:22:28] assistant / spoken_confirmation / voice: Yes? I am listening.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 18:22:29] assistant / spoken_confirmation / voice: Yes. What do you want to know?
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 18:22:32] operator / voice_transcript_partial / voice: tracking voice use leon
  meta: kind=partial | timestamp=1778062952.2160046 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:32] operator / voice_transcript_partial / voice: tracking voice use wait
  meta: kind=partial | timestamp=1778062952.358712 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:32] operator / voice_transcript_partial / voice: tracking voice use leon activate turn
  meta: kind=partial | timestamp=1778062952.6067169 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:33] operator / voice_transcript_partial / voice: tracking voice use leon activate turn guard
  meta: kind=partial | timestamp=1778062953.644896 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:33] operator / voice_transcript_partial / voice: tracking voice use leon activate turn guard home
  meta: kind=partial | timestamp=1778062953.6538997 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:33] operator / voice_transcript_partial / voice: tracking voice use leon activate turn guard hold position
  meta: kind=partial | timestamp=1778062953.660619 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:34] operator / voice_transcript_partial / voice: tracking voice use leon activate turn guard hold position status
  meta: kind=partial | timestamp=1778062954.6610177 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:34] operator / voice_transcript_partial / voice: tracking voice use leon activate turn guard hold position face detection
  meta: kind=partial | timestamp=1778062954.9124913 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:35] operator / voice_transcript_partial / voice: tracking voice use leon activate turn guard hold position face detection not
  meta: kind=partial | timestamp=1778062955.4137583 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:35] operator / voice_transcript_partial / voice: tracking voice use leon activate turn guard hold position face detection not working
  meta: kind=partial | timestamp=1778062955.661935 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:37] operator / voice_transcript_final / voice: tracking paused use wait activate turn guard hold position face detection not working
  meta: kind=final | timestamp=1778062957.2417707 | source=final | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:37] operator / voice_command / voice: tracking paused use wait activate turn guard hold position face detection not working
  meta: normalized=True
- [2026-05-06 18:22:38] assistant / spoken_confirmation / voice: Understood. Holding position. Tell me when to resume guarding mode.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 18:22:42] operator / voice_transcript_partial / voice: tracking paused use leon turn turn guard hold position
  meta: kind=partial | timestamp=1778062962.7141914 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:43] operator / voice_transcript_partial / voice: tracking paused use leon turn turn guard hold position run
  meta: kind=partial | timestamp=1778062963.9901743 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:44] operator / voice_transcript_partial / voice: tracking paused use leon turn turn guard hold position run smart
  meta: kind=partial | timestamp=1778062964.1616764 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:44] operator / voice_transcript_partial / voice: tracking paused use leon turn turn guard hold position run smart sentry
  meta: kind=partial | timestamp=1778062964.4121547 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:45] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778062965.4257686 | source=final | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:45] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-06 18:22:46] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 18:22:50] operator / voice_transcript_partial / voice: status guard no active targets running
  meta: kind=partial | timestamp=1778062970.4133937 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:50] operator / voice_transcript_partial / voice: status guard no active targets running no
  meta: kind=partial | timestamp=1778062970.664577 | source=vosk | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:51] operator / voice_transcript_final / voice: status guard no active targets running no
  meta: kind=final | timestamp=1778062971.801336 | source=final | frequency_hz=90.0 | rms=754 | updated_at=1778062932.3621528
- [2026-05-06 18:22:53] operator / voice_transcript_partial / voice: port
  meta: kind=partial | timestamp=1778062973.7910168 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:22:54] operator / voice_transcript_partial / voice: port view
  meta: kind=partial | timestamp=1778062974.1718204 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:22:54] operator / voice_transcript_final / voice: port
  meta: kind=final | timestamp=1778062974.4163043 | source=final | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:22:57] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778062977.287665 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:22:57] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 18:22:58] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778062978.400095 | source=final | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:22:58] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1778062978.8337991 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:22:59] assistant / spoken_confirmation / voice: Yes? I am listening.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 18:23:02] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1778062982.0600598 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:02] operator / voice_transcript_partial / voice: tracking voice
  meta: kind=partial | timestamp=1778062982.298532 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:02] operator / voice_transcript_partial / voice: tracking paused
  meta: kind=partial | timestamp=1778062982.7979746 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:03] operator / voice_transcript_partial / voice: tracking paused e
  meta: kind=partial | timestamp=1778062983.0526538 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:03] operator / voice_transcript_partial / voice: tracking paused e lion
  meta: kind=partial | timestamp=1778062983.3011458 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:03] operator / voice_transcript_partial / voice: tracking paused keys recovery
  meta: kind=partial | timestamp=1778062983.5488818 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:03] operator / voice_transcript_partial / voice: tracking paused e lion activate
  meta: kind=partial | timestamp=1778062983.7977722 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:04] operator / voice_transcript_partial / voice: tracking paused hey leon turn
  meta: kind=partial | timestamp=1778062984.0499465 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:04] operator / voice_transcript_partial / voice: tracking paused hey leon turn guard home
  meta: kind=partial | timestamp=1778062984.553028 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:04] operator / voice_transcript_partial / voice: tracking paused hey leon turn guard hold position
  meta: kind=partial | timestamp=1778062984.7988863 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:05] operator / voice_transcript_partial / voice: tracking paused hey leon turn guard hold position alion
  meta: kind=partial | timestamp=1778062985.299204 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:05] operator / voice_transcript_partial / voice: tracking paused hey leon turn guard hold position alien
  meta: kind=partial | timestamp=1778062985.5515583 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:07] operator / voice_transcript_partial / voice: tracking paused hey leon turn guard hold position alien who are you
  meta: kind=partial | timestamp=1778062987.4817157 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:08] operator / voice_transcript_final / voice: elion tracking paused use turn to guard hold position who are you
  meta: kind=final | timestamp=1778062988.0651286 | source=final | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:08] operator / voice_command / voice: elion tracking paused use turn to guard hold position who are you
  meta: normalized=True
- [2026-05-06 18:23:08] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1778062988.2981205 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:08] operator / voice_transcript_partial / voice: tracking voice
  meta: kind=partial | timestamp=1778062988.558175 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:09] operator / voice_transcript_partial / voice: tracking voice target
  meta: kind=partial | timestamp=1778062989.5502558 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:09] operator / voice_transcript_partial / voice: tracking voice target is hello
  meta: kind=partial | timestamp=1778062989.8001378 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:11] assistant / spoken_confirmation / voice: Understood. Holding position. Tell me when to resume guarding mode.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 18:23:14] operator / voice_transcript_partial / voice: tracking voice target is hello the guard hey precision standby guard no active targets running the tracking
  meta: kind=partial | timestamp=1778062994.7999697 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:15] operator / voice_transcript_partial / voice: tracking voice target is hello the guard hey precision standby guard no active targets running the tracking voice
  meta: kind=partial | timestamp=1778062995.0503712 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:15] operator / voice_transcript_partial / voice: tracking voice target is hello the guard hey precision standby guard no active targets running the tracking paused
  meta: kind=partial | timestamp=1778062995.3008142 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:16] operator / voice_transcript_partial / voice: tracking voice target is hello the guard hey precision standby guard no active targets running the tracking paused target matching
  meta: kind=partial | timestamp=1778062996.0498123 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:16] operator / voice_transcript_partial / voice: tracking voice target is hello the guard hey precision standby guard no active targets running the tracking paused target is
  meta: kind=partial | timestamp=1778062996.2999296 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:16] operator / voice_transcript_partial / voice: tracking voice target is hello the guard hey precision standby guard no active targets running the tracking paused target is hello the guard
  meta: kind=partial | timestamp=1778062996.553344 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:16] operator / voice_transcript_partial / voice: tracking voice target is hello the guard hey precision standby guard no active targets running the tracking paused target is hello the guard hey
  meta: kind=partial | timestamp=1778062996.7992327 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:17] operator / voice_transcript_partial / voice: tracking voice target is hello the guard hey precision standby guard no active targets running the tracking paused target is hello the guard hold position
  meta: kind=partial | timestamp=1778062997.0493195 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:18] operator / voice_transcript_final / voice: tracking voice target is hello the guard hey precision standby guard no active targets running the tracking paused target is hello the guard hold position
  meta: kind=final | timestamp=1778062998.39527 | source=final | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:19] operator / voice_command / voice: tracking voice target is hello the guard hey precision standby guard no active targets running the tracking paused target is hello the guard hold position
  meta: normalized=True
- [2026-05-06 18:23:20] assistant / spoken_confirmation / voice: Understood. Holding position. Tell me when to resume guarding mode.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 18:23:25] operator / voice_transcript_partial / voice: on the search hold position tell me why to
  meta: kind=partial | timestamp=1778063005.201251 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:25] operator / voice_transcript_partial / voice: on the search hold position tell me why to resume
  meta: kind=partial | timestamp=1778063005.4478872 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:25] operator / voice_transcript_partial / voice: on the search hold position tell me why to resume guarding
  meta: kind=partial | timestamp=1778063005.6996605 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:25] operator / voice_transcript_partial / voice: on the search hold position tell me why to resume guarding mode
  meta: kind=partial | timestamp=1778063005.9499838 | source=vosk | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:27] operator / voice_transcript_final / voice: resume guarding mode
  meta: kind=final | timestamp=1778063007.2035582 | source=final | frequency_hz=114.0 | rms=858 | updated_at=1778062973.0325074
- [2026-05-06 18:23:27] operator / voice_command / voice: resume guarding mode
  meta: normalized=True
- [2026-05-06 18:23:28] assistant / spoken_confirmation / voice: Resuming guarding mode now.
  meta: interrupt=False | assistant_output=False | spoken=False
