# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-06 10:59:54
- Entries: 137
- Roles: {'assistant': 6, 'system': 1, 'operator': 130}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_partial': 104, 'voice_transcript_final': 21, 'spoken_confirmation': 4, 'voice_command': 5}
- Channels: {'text': 2, 'voice': 135}
- Latest operator request: status guard loop active targets running
- Latest assistant message: That does not match a known command. Please repeat.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-06 10:53:59] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 10:53:59] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 10:54:02] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778036042.372454 | source=vosk
- [2026-05-06 10:54:10] operator / voice_transcript_partial / voice: id
  meta: kind=partial | timestamp=1778036050.0777783 | source=vosk | frequency_hz=392.0 | rms=358 | updated_at=1778036048.318452
- [2026-05-06 10:54:10] operator / voice_transcript_final / voice: id
  meta: kind=final | timestamp=1778036050.9106874 | source=final | frequency_hz=392.0 | rms=358 | updated_at=1778036048.318452
- [2026-05-06 10:54:19] operator / voice_transcript_partial / voice: id
  meta: kind=partial | timestamp=1778036059.324318 | source=vosk | frequency_hz=392.0 | rms=358 | updated_at=1778036048.318452
- [2026-05-06 10:54:20] operator / voice_transcript_partial / voice: video
  meta: kind=partial | timestamp=1778036060.075177 | source=vosk | frequency_hz=392.0 | rms=358 | updated_at=1778036048.318452
- [2026-05-06 10:54:20] operator / voice_transcript_final / voice: video
  meta: kind=final | timestamp=1778036060.8962293 | source=final | frequency_hz=392.0 | rms=358 | updated_at=1778036048.318452
- [2026-05-06 10:54:39] operator / voice_transcript_partial / voice: output
  meta: kind=partial | timestamp=1778036079.8239813 | source=vosk | frequency_hz=337.1 | rms=333 | updated_at=1778036078.3197343
- [2026-05-06 10:54:40] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1778036080.57612 | source=vosk | frequency_hz=337.1 | rms=333 | updated_at=1778036078.3197343
- [2026-05-06 10:54:41] operator / voice_transcript_final / voice: on
  meta: kind=final | timestamp=1778036081.1557794 | source=final | frequency_hz=337.1 | rms=333 | updated_at=1778036078.3197343
- [2026-05-06 10:54:42] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1778036082.3263028 | source=vosk | frequency_hz=404.0 | rms=374 | updated_at=1778036081.3197198
- [2026-05-06 10:54:43] operator / voice_transcript_partial / voice: on no
  meta: kind=partial | timestamp=1778036083.368985 | source=vosk | frequency_hz=404.0 | rms=374 | updated_at=1778036081.3197198
- [2026-05-06 10:54:44] assistant / spoken_confirmation / voice: System online and listening. You can ask about the runtime or give a command.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 10:54:50] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1778036090.8196661 | source=vosk | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:50] operator / voice_transcript_partial / voice: system on
  meta: kind=partial | timestamp=1778036090.8266792 | source=vosk | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:51] operator / voice_transcript_partial / voice: system on the
  meta: kind=partial | timestamp=1778036091.3290913 | source=vosk | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:51] operator / voice_transcript_partial / voice: system on is
  meta: kind=partial | timestamp=1778036091.5791044 | source=vosk | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:52] operator / voice_transcript_final / voice: system on
  meta: kind=final | timestamp=1778036092.2823396 | source=final | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:52] operator / voice_transcript_partial / voice: ask
  meta: kind=partial | timestamp=1778036092.8257995 | source=vosk | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:53] operator / voice_transcript_partial / voice: ask a lion
  meta: kind=partial | timestamp=1778036093.0759594 | source=vosk | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:53] operator / voice_transcript_partial / voice: ask a
  meta: kind=partial | timestamp=1778036093.3280258 | source=vosk | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:53] operator / voice_transcript_partial / voice: ask event blink
  meta: kind=partial | timestamp=1778036093.576156 | source=vosk | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:53] operator / voice_transcript_partial / voice: ask event runtime
  meta: kind=partial | timestamp=1778036093.8361304 | source=vosk | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:54] operator / voice_transcript_partial / voice: ask event runtime auto
  meta: kind=partial | timestamp=1778036094.3347797 | source=vosk | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:54] operator / voice_transcript_partial / voice: ask event runtime
  meta: kind=partial | timestamp=1778036094.5776498 | source=vosk | frequency_hz=368.6 | rms=350 | updated_at=1778036089.5704215
- [2026-05-06 10:54:55] operator / voice_transcript_partial / voice: ask event runtime command
  meta: kind=partial | timestamp=1778036095.0827043 | source=vosk | frequency_hz=329.2 | rms=339 | updated_at=1778036095.070584
- [2026-05-06 10:54:55] operator / voice_transcript_final / voice: ask event runtime command
  meta: kind=final | timestamp=1778036095.459252 | source=final | frequency_hz=333.0 | rms=333 | updated_at=1778036095.3204305
- [2026-05-06 10:55:40] operator / voice_transcript_partial / voice: running
  meta: kind=partial | timestamp=1778036140.831474 | source=vosk | frequency_hz=372.6 | rms=336 | updated_at=1778036139.5727534
- [2026-05-06 10:55:41] operator / voice_transcript_partial / voice: running pir guard
  meta: kind=partial | timestamp=1778036141.3322942 | source=vosk | frequency_hz=372.6 | rms=336 | updated_at=1778036139.5727534
- [2026-05-06 10:55:41] operator / voice_transcript_partial / voice: running pir
  meta: kind=partial | timestamp=1778036141.58039 | source=vosk | frequency_hz=372.6 | rms=336 | updated_at=1778036139.5727534
- [2026-05-06 10:55:42] operator / voice_transcript_partial / voice: running pir voice
  meta: kind=partial | timestamp=1778036142.0849311 | source=vosk | frequency_hz=372.6 | rms=336 | updated_at=1778036139.5727534
- [2026-05-06 10:55:42] operator / voice_transcript_final / voice: running pir
  meta: kind=final | timestamp=1778036142.474737 | source=final | frequency_hz=372.6 | rms=336 | updated_at=1778036139.5727534
- [2026-05-06 10:55:43] operator / voice_transcript_partial / voice: the one hello
  meta: kind=partial | timestamp=1778036143.833689 | source=vosk | frequency_hz=393.1 | rms=347 | updated_at=1778036143.0725029
- [2026-05-06 10:55:44] operator / voice_transcript_final / voice: the one
  meta: kind=final | timestamp=1778036144.8906467 | source=final | frequency_hz=393.1 | rms=347 | updated_at=1778036143.0725029
- [2026-05-06 10:55:45] operator / voice_transcript_partial / voice: the pir voice
  meta: kind=partial | timestamp=1778036145.5845544 | source=vosk | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:45] operator / voice_transcript_partial / voice: logger is
  meta: kind=partial | timestamp=1778036145.8299448 | source=vosk | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:46] operator / voice_transcript_partial / voice: logger is the
  meta: kind=partial | timestamp=1778036146.3339834 | source=vosk | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:46] operator / voice_transcript_partial / voice: logger is anything else
  meta: kind=partial | timestamp=1778036146.5807025 | source=vosk | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:46] operator / voice_transcript_partial / voice: logger is the export
  meta: kind=partial | timestamp=1778036146.8300562 | source=vosk | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:47] operator / voice_transcript_partial / voice: logger is the is video
  meta: kind=partial | timestamp=1778036147.0805426 | source=vosk | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:47] operator / voice_transcript_partial / voice: the video display is the
  meta: kind=partial | timestamp=1778036147.3307052 | source=vosk | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:47] operator / voice_transcript_partial / voice: the video display is the the
  meta: kind=partial | timestamp=1778036147.8331466 | source=vosk | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:48] operator / voice_transcript_partial / voice: the video display is the the window
  meta: kind=partial | timestamp=1778036148.0819569 | source=vosk | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:48] operator / voice_transcript_partial / voice: the video display is the the window shortcuts
  meta: kind=partial | timestamp=1778036148.3300982 | source=vosk | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:49] operator / voice_transcript_partial / voice: the video display is the the window target matching
  meta: kind=partial | timestamp=1778036149.0866146 | source=vosk | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:49] operator / voice_transcript_final / voice: logger is anything export e is the the window guard
  meta: kind=final | timestamp=1778036149.714072 | source=final | frequency_hz=388.0 | rms=348 | updated_at=1778036144.8941042
- [2026-05-06 10:55:52] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1778036152.443878 | source=vosk | frequency_hz=231.8 | rms=485 | updated_at=1778036151.432979
- [2026-05-06 10:55:52] operator / voice_transcript_partial / voice: a lion enable
  meta: kind=partial | timestamp=1778036152.69231 | source=vosk | frequency_hz=231.8 | rms=485 | updated_at=1778036151.432979
- [2026-05-06 10:55:52] operator / voice_transcript_partial / voice: a lion name announcements
  meta: kind=partial | timestamp=1778036152.9402554 | source=vosk | frequency_hz=231.8 | rms=485 | updated_at=1778036151.432979
- [2026-05-06 10:55:53] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 10:55:59] operator / voice_transcript_partial / voice: status guard loop active
  meta: kind=partial | timestamp=1778036159.190786 | source=vosk | frequency_hz=231.8 | rms=485 | updated_at=1778036151.432979
- [2026-05-06 10:55:59] operator / voice_transcript_partial / voice: status guard loop
  meta: kind=partial | timestamp=1778036159.4417067 | source=vosk | frequency_hz=231.8 | rms=485 | updated_at=1778036151.432979
- [2026-05-06 10:55:59] operator / voice_transcript_partial / voice: status guard loop active
  meta: kind=partial | timestamp=1778036159.6964986 | source=vosk | frequency_hz=231.8 | rms=485 | updated_at=1778036151.432979
- [2026-05-06 10:56:00] operator / voice_transcript_final / voice: standby guard loop active
  meta: kind=final | timestamp=1778036160.0668166 | source=final | frequency_hz=231.8 | rms=485 | updated_at=1778036151.432979
- [2026-05-06 10:56:34] operator / voice_transcript_partial / voice: mask
  meta: kind=partial | timestamp=1778036194.6132798 | source=vosk | frequency_hz=344.4 | rms=324 | updated_at=1778036188.3558793
- [2026-05-06 10:56:34] operator / voice_transcript_partial / voice: mask assistant
  meta: kind=partial | timestamp=1778036194.8663397 | source=vosk | frequency_hz=344.4 | rms=324 | updated_at=1778036188.3558793
- [2026-05-06 10:56:35] operator / voice_transcript_partial / voice: mask
  meta: kind=partial | timestamp=1778036195.1140654 | source=vosk | frequency_hz=344.4 | rms=324 | updated_at=1778036188.3558793
- [2026-05-06 10:56:35] operator / voice_transcript_final / voice: masks id
  meta: kind=final | timestamp=1778036195.7793756 | source=final | frequency_hz=344.4 | rms=324 | updated_at=1778036188.3558793
- [2026-05-06 10:56:36] operator / voice_transcript_partial / voice: hello movement
  meta: kind=partial | timestamp=1778036196.112665 | source=vosk | frequency_hz=344.4 | rms=324 | updated_at=1778036188.3558793
- [2026-05-06 10:56:36] operator / voice_transcript_partial / voice: rest
  meta: kind=partial | timestamp=1778036196.8633735 | source=vosk | frequency_hz=404.0 | rms=337 | updated_at=1778036196.8558574
- [2026-05-06 10:56:37] operator / voice_transcript_final / voice: rest
  meta: kind=final | timestamp=1778036197.4695678 | source=final | frequency_hz=404.0 | rms=337 | updated_at=1778036196.8558574
- [2026-05-06 10:57:02] operator / voice_transcript_final / voice: blink
  meta: kind=final | timestamp=1778036222.7066162 | source=final | frequency_hz=353.2 | rms=352 | updated_at=1778036222.6063347
- [2026-05-06 10:58:01] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1778036281.1179817 | source=vosk | frequency_hz=356.0 | rms=338 | updated_at=1778036280.3597972
- [2026-05-06 10:58:01] operator / voice_transcript_partial / voice: leon engagement
  meta: kind=partial | timestamp=1778036281.6178694 | source=vosk | frequency_hz=356.0 | rms=338 | updated_at=1778036280.3597972
- [2026-05-06 10:58:01] operator / voice_transcript_partial / voice: leon continue conversation
  meta: kind=partial | timestamp=1778036281.8665643 | source=vosk | frequency_hz=356.0 | rms=338 | updated_at=1778036280.3597972
- [2026-05-06 10:58:02] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 10:58:11] operator / voice_transcript_partial / voice: tracking close speak optimise turn the guard hold position is the what's the manual fire the
  meta: kind=partial | timestamp=1778036291.761669 | source=vosk | frequency_hz=364.0 | rms=344 | updated_at=1778036287.2478056
- [2026-05-06 10:58:12] operator / voice_transcript_partial / voice: tracking close speak optimise turn the guard hold position is the what's the media loop
  meta: kind=partial | timestamp=1778036292.0095997 | source=vosk | frequency_hz=364.0 | rms=344 | updated_at=1778036287.2478056
- [2026-05-06 10:58:12] operator / voice_transcript_partial / voice: tracking close speak optimise turn the guard hold position is the what's the media loop active
  meta: kind=partial | timestamp=1778036292.2570112 | source=vosk | frequency_hz=364.0 | rms=344 | updated_at=1778036287.2478056
- [2026-05-06 10:58:12] operator / voice_transcript_partial / voice: tracking close speak optimise turn the guard hold position is the what's the media loop active targets
  meta: kind=partial | timestamp=1778036292.8804326 | source=vosk | frequency_hz=364.0 | rms=344 | updated_at=1778036287.2478056
- [2026-05-06 10:58:13] operator / voice_transcript_partial / voice: tracking close speak optimise turn the guard hold position is the what's the media loop active targets running
  meta: kind=partial | timestamp=1778036293.0052667 | source=vosk | frequency_hz=364.0 | rms=344 | updated_at=1778036287.2478056
- [2026-05-06 10:58:13] operator / voice_transcript_partial / voice: tracking close speak optimise turn the guard hold position is the what's the media loop active targets recognition
  meta: kind=partial | timestamp=1778036293.25572 | source=vosk | frequency_hz=400.0 | rms=354 | updated_at=1778036293.248707
- [2026-05-06 10:58:14] operator / voice_transcript_final / voice: tracking close use window turn turn the guard hold position is the what s the manual fire the loop active targets running
  meta: kind=final | timestamp=1778036294.0117307 | source=final | frequency_hz=379.0 | rms=335 | updated_at=1778036293.4986334
- [2026-05-06 10:58:15] operator / voice_command / voice: tracking close use window turn turn the guard hold position is the what s the manual fire the loop active targets running
  meta: normalized=True
- [2026-05-06 10:58:16] assistant / spoken_confirmation / voice: Understood. Holding position. Tell me when to resume guarding mode.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 10:58:20] operator / voice_transcript_partial / voice: recovery
  meta: kind=partial | timestamp=1778036300.4200146 | source=vosk | frequency_hz=274.6 | rms=763 | updated_at=1778036295.868991
- [2026-05-06 10:58:20] operator / voice_transcript_partial / voice: speak optimization
  meta: kind=partial | timestamp=1778036300.6682367 | source=vosk | frequency_hz=274.6 | rms=763 | updated_at=1778036295.868991
- [2026-05-06 10:58:20] operator / voice_transcript_partial / voice: trigger turn
  meta: kind=partial | timestamp=1778036300.925245 | source=vosk | frequency_hz=274.6 | rms=763 | updated_at=1778036295.868991
- [2026-05-06 10:58:21] operator / voice_transcript_partial / voice: trigger turn guard
  meta: kind=partial | timestamp=1778036301.171341 | source=vosk | frequency_hz=274.6 | rms=763 | updated_at=1778036295.868991
- [2026-05-06 10:58:21] operator / voice_transcript_partial / voice: trigger turn guard precision
  meta: kind=partial | timestamp=1778036301.9176476 | source=vosk | frequency_hz=274.6 | rms=763 | updated_at=1778036295.868991
- [2026-05-06 10:58:23] operator / voice_transcript_final / voice: trigger turn guard precision
  meta: kind=final | timestamp=1778036303.569721 | source=final | frequency_hz=311.3 | rms=354 | updated_at=1778036302.9093213
- [2026-05-06 10:58:34] operator / voice_transcript_partial / voice: run the
  meta: kind=partial | timestamp=1778036314.620116 | source=vosk | frequency_hz=336.0 | rms=349 | updated_at=1778036313.1146443
- [2026-05-06 10:58:35] operator / voice_transcript_partial / voice: run the speak
  meta: kind=partial | timestamp=1778036315.1190755 | source=vosk | frequency_hz=336.0 | rms=349 | updated_at=1778036313.1146443
- [2026-05-06 10:58:35] operator / voice_transcript_partial / voice: run the speech
  meta: kind=partial | timestamp=1778036315.3708332 | source=vosk | frequency_hz=336.0 | rms=349 | updated_at=1778036313.1146443
- [2026-05-06 10:58:35] operator / voice_transcript_partial / voice: run the speech smart
  meta: kind=partial | timestamp=1778036315.6214154 | source=vosk | frequency_hz=336.0 | rms=349 | updated_at=1778036313.1146443
- [2026-05-06 10:58:35] operator / voice_transcript_partial / voice: run the speech smart sentry
  meta: kind=partial | timestamp=1778036315.8701036 | source=vosk | frequency_hz=336.0 | rms=349 | updated_at=1778036313.1146443
- [2026-05-06 10:58:36] operator / voice_transcript_partial / voice: run the speech smart sentry app
  meta: kind=partial | timestamp=1778036316.37158 | source=vosk | frequency_hz=328.0 | rms=337 | updated_at=1778036316.3650546
- [2026-05-06 10:58:37] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778036317.3770044 | source=final | frequency_hz=333.0 | rms=346 | updated_at=1778036317.3649797
- [2026-05-06 10:58:37] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-06 10:58:38] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 10:58:41] operator / voice_transcript_partial / voice: loop active
  meta: kind=partial | timestamp=1778036321.6205132 | source=vosk | frequency_hz=304.0 | rms=345 | updated_at=1778036320.3648975
- [2026-05-06 10:58:41] operator / voice_transcript_partial / voice: loop active targets
  meta: kind=partial | timestamp=1778036321.8842428 | source=vosk | frequency_hz=304.0 | rms=345 | updated_at=1778036320.3648975
- [2026-05-06 10:58:42] operator / voice_transcript_partial / voice: loop active targets running
  meta: kind=partial | timestamp=1778036322.1216397 | source=vosk | frequency_hz=304.0 | rms=345 | updated_at=1778036320.3648975
- [2026-05-06 10:58:42] operator / voice_transcript_final / voice: loop active targets running
  meta: kind=final | timestamp=1778036322.8202558 | source=final | frequency_hz=304.0 | rms=345 | updated_at=1778036320.3648975
- [2026-05-06 10:58:54] operator / voice_transcript_partial / voice: the tracking no one targets
  meta: kind=partial | timestamp=1778036334.5305479 | source=vosk | frequency_hz=288.0 | rms=353 | updated_at=1778036333.3656878
- [2026-05-06 10:58:54] operator / voice_transcript_partial / voice: the tracking no one target
  meta: kind=partial | timestamp=1778036334.6215284 | source=vosk | frequency_hz=288.0 | rms=353 | updated_at=1778036333.3656878
- [2026-05-06 10:58:54] operator / voice_transcript_partial / voice: the tracking no one target view
  meta: kind=partial | timestamp=1778036334.8726785 | source=vosk | frequency_hz=288.0 | rms=353 | updated_at=1778036333.3656878
- [2026-05-06 10:58:56] operator / voice_transcript_final / voice: the tracking no one target view
  meta: kind=final | timestamp=1778036336.2072232 | source=final | frequency_hz=344.0 | rms=345 | updated_at=1778036335.6184597
- [2026-05-06 10:59:15] operator / voice_transcript_partial / voice: local pan
  meta: kind=partial | timestamp=1778036355.548429 | source=vosk | frequency_hz=349.5 | rms=358 | updated_at=1778036339.2177577
- [2026-05-06 10:59:15] operator / voice_transcript_partial / voice: local pan machine of
  meta: kind=partial | timestamp=1778036355.8007972 | source=vosk | frequency_hz=349.5 | rms=358 | updated_at=1778036339.2177577
- [2026-05-06 10:59:16] operator / voice_transcript_partial / voice: local pan machine of rest
  meta: kind=partial | timestamp=1778036356.5695145 | source=vosk | frequency_hz=349.5 | rms=358 | updated_at=1778036339.2177577
- [2026-05-06 10:59:16] operator / voice_transcript_partial / voice: local pan machine of recognition
  meta: kind=partial | timestamp=1778036356.801756 | source=vosk | frequency_hz=349.5 | rms=358 | updated_at=1778036339.2177577
- [2026-05-06 10:59:22] operator / voice_transcript_partial / voice: hey leon
  meta: kind=partial | timestamp=1778036362.5415728 | source=vosk | frequency_hz=320.0 | rms=317 | updated_at=1778036358.5350554
- [2026-05-06 10:59:23] operator / voice_transcript_partial / voice: hey leon no fire
  meta: kind=partial | timestamp=1778036363.5502496 | source=vosk | frequency_hz=320.0 | rms=317 | updated_at=1778036358.5350554
- [2026-05-06 10:59:23] operator / voice_transcript_partial / voice: hey leon loop active
  meta: kind=partial | timestamp=1778036363.7945397 | source=vosk | frequency_hz=320.0 | rms=317 | updated_at=1778036358.5350554
- [2026-05-06 10:59:24] operator / voice_transcript_partial / voice: hey leon loop active shortcuts running
  meta: kind=partial | timestamp=1778036364.5733538 | source=vosk | frequency_hz=320.0 | rms=317 | updated_at=1778036358.5350554
- [2026-05-06 10:59:24] operator / voice_transcript_partial / voice: hey leon loop active training
  meta: kind=partial | timestamp=1778036364.791877 | source=vosk | frequency_hz=320.0 | rms=317 | updated_at=1778036358.5350554
- [2026-05-06 10:59:26] operator / voice_transcript_partial / voice: the tracking
  meta: kind=partial | timestamp=1778036366.040877 | source=vosk | frequency_hz=320.0 | rms=317 | updated_at=1778036358.5350554
- [2026-05-06 10:59:26] operator / voice_transcript_partial / voice: the tracking no
  meta: kind=partial | timestamp=1778036366.5411804 | source=vosk | frequency_hz=320.0 | rms=317 | updated_at=1778036358.5350554
- [2026-05-06 10:59:27] operator / voice_transcript_partial / voice: the tracking no scores
  meta: kind=partial | timestamp=1778036367.9252267 | source=vosk | frequency_hz=320.0 | rms=317 | updated_at=1778036358.5350554
- [2026-05-06 10:59:28] operator / voice_transcript_final / voice: the tracking no scores
  meta: kind=final | timestamp=1778036368.8667774 | source=final | frequency_hz=74.0 | rms=467 | updated_at=1778036368.1764064
- [2026-05-06 10:59:29] operator / voice_command / voice: the tracking no scores
  meta: normalized=True
- [2026-05-06 10:59:30] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 10:59:35] operator / voice_transcript_partial / voice: led is not matching on commands
  meta: kind=partial | timestamp=1778036375.2904584 | source=vosk | frequency_hz=326.4 | rms=331 | updated_at=1778036371.9147942
- [2026-05-06 10:59:35] operator / voice_transcript_partial / voice: led is not matching on commands precision
  meta: kind=partial | timestamp=1778036375.4239104 | source=vosk | frequency_hz=326.4 | rms=331 | updated_at=1778036371.9147942
- [2026-05-06 10:59:35] operator / voice_transcript_partial / voice: led is not matching on commands speech replies
  meta: kind=partial | timestamp=1778036375.6666625 | source=vosk | frequency_hz=326.4 | rms=331 | updated_at=1778036371.9147942
- [2026-05-06 10:59:36] operator / voice_transcript_final / voice: that is not matching on commands
  meta: kind=final | timestamp=1778036376.0845375 | source=final | frequency_hz=326.4 | rms=331 | updated_at=1778036371.9147942
- [2026-05-06 10:59:44] operator / voice_transcript_partial / voice: threat scores
  meta: kind=partial | timestamp=1778036384.847137 | source=vosk | frequency_hz=264.0 | rms=340 | updated_at=1778036384.5804017
- [2026-05-06 10:59:45] operator / voice_transcript_partial / voice: threat
  meta: kind=partial | timestamp=1778036385.3396275 | source=vosk | frequency_hz=264.0 | rms=340 | updated_at=1778036384.5804017
- [2026-05-06 10:59:45] operator / voice_transcript_partial / voice: threat fire
  meta: kind=partial | timestamp=1778036385.5859776 | source=vosk | frequency_hz=264.0 | rms=340 | updated_at=1778036384.5804017
- [2026-05-06 10:59:45] operator / voice_transcript_partial / voice: threat fire disabled
  meta: kind=partial | timestamp=1778036385.8455534 | source=vosk | frequency_hz=264.0 | rms=340 | updated_at=1778036384.5804017
- [2026-05-06 10:59:46] operator / voice_transcript_partial / voice: threat fire disable is
  meta: kind=partial | timestamp=1778036386.3390918 | source=vosk | frequency_hz=264.0 | rms=340 | updated_at=1778036384.5804017
- [2026-05-06 10:59:46] operator / voice_transcript_partial / voice: threat fire test video
  meta: kind=partial | timestamp=1778036386.595889 | source=vosk | frequency_hz=264.0 | rms=340 | updated_at=1778036384.5804017
- [2026-05-06 10:59:46] operator / voice_transcript_partial / voice: threat fire disable visual
  meta: kind=partial | timestamp=1778036386.841309 | source=vosk | frequency_hz=264.0 | rms=340 | updated_at=1778036384.5804017
- [2026-05-06 10:59:47] operator / voice_transcript_partial / voice: threat fire disable visual overlay
  meta: kind=partial | timestamp=1778036387.098343 | source=vosk | frequency_hz=282.0 | rms=350 | updated_at=1778036387.0822926
- [2026-05-06 10:59:47] operator / voice_transcript_partial / voice: threat fire disable visual current
  meta: kind=partial | timestamp=1778036387.8614175 | source=vosk | frequency_hz=277.1 | rms=326 | updated_at=1778036387.330569
- [2026-05-06 10:59:48] operator / voice_transcript_partial / voice: threat fire disable visual current status
  meta: kind=partial | timestamp=1778036388.088299 | source=vosk | frequency_hz=277.1 | rms=326 | updated_at=1778036387.330569
- [2026-05-06 10:59:49] operator / voice_transcript_partial / voice: threat fire disable visual current status engaging scope
  meta: kind=partial | timestamp=1778036389.0911446 | source=vosk | frequency_hz=277.1 | rms=326 | updated_at=1778036387.330569
- [2026-05-06 10:59:49] operator / voice_transcript_final / voice: threat fire disable visual current status engaging
  meta: kind=final | timestamp=1778036389.998054 | source=final | frequency_hz=277.1 | rms=326 | updated_at=1778036387.330569
- [2026-05-06 10:59:50] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1778036390.5961275 | source=vosk | frequency_hz=277.1 | rms=326 | updated_at=1778036387.330569
- [2026-05-06 10:59:51] operator / voice_transcript_partial / voice: status guard
  meta: kind=partial | timestamp=1778036391.1004272 | source=vosk | frequency_hz=277.1 | rms=326 | updated_at=1778036387.330569
- [2026-05-06 10:59:51] operator / voice_transcript_partial / voice: status guard no
  meta: kind=partial | timestamp=1778036391.6023555 | source=vosk | frequency_hz=277.1 | rms=326 | updated_at=1778036387.330569
- [2026-05-06 10:59:51] operator / voice_transcript_partial / voice: status guard loop active
  meta: kind=partial | timestamp=1778036391.8489435 | source=vosk | frequency_hz=277.1 | rms=326 | updated_at=1778036387.330569
- [2026-05-06 10:59:52] operator / voice_transcript_partial / voice: status guard loop active shortcuts
  meta: kind=partial | timestamp=1778036392.352948 | source=vosk | frequency_hz=277.1 | rms=326 | updated_at=1778036387.330569
- [2026-05-06 10:59:52] operator / voice_transcript_partial / voice: status guard loop active targets running
  meta: kind=partial | timestamp=1778036392.6028032 | source=vosk | frequency_hz=277.1 | rms=326 | updated_at=1778036387.330569
- [2026-05-06 10:59:53] operator / voice_transcript_final / voice: status guard loop active targets running
  meta: kind=final | timestamp=1778036393.4582617 | source=final | frequency_hz=392.0 | rms=342 | updated_at=1778036393.3417115
