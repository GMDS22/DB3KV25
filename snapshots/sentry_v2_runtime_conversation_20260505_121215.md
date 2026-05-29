# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-05 12:12:15
- Entries: 238
- Roles: {'assistant': 3, 'system': 1, 'operator': 234}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 1, 'voice_transcript_partial': 196, 'voice_transcript_final': 38}
- Channels: {'text': 2, 'voice': 236}
- Latest operator request: of the half
- Latest assistant message: Elion is ready. Say a task and I will execute it step by step.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 12:08:10] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 12:08:10] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 12:08:12] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777954092.462457 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:13] assistant / spoken_confirmation / voice: Elion is ready. Say a task and I will execute it step by step.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 12:08:13] operator / voice_transcript_partial / voice: if
  meta: kind=partial | timestamp=1777954093.8896666 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:14] operator / voice_transcript_final / voice: if
  meta: kind=final | timestamp=1777954094.756549 | source=final | confidence=0.57 | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:15] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1777954095.1769133 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:15] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777954095.7913322 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:16] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777954096.1967192 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:16] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777954096.4119337 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:16] operator / voice_transcript_partial / voice: hoover
  meta: kind=partial | timestamp=1777954096.6271248 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:16] operator / voice_transcript_partial / voice: you move
  meta: kind=partial | timestamp=1777954096.8351343 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:17] operator / voice_transcript_partial / voice: one of the
  meta: kind=partial | timestamp=1777954097.4462194 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:18] operator / voice_transcript_partial / voice: one of the month of
  meta: kind=partial | timestamp=1777954098.8649192 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:20] operator / voice_transcript_final / voice: one of the month of
  meta: kind=final | timestamp=1777954100.2873867 | source=final | confidence=0.27 | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:20] operator / voice_transcript_partial / voice: us
  meta: kind=partial | timestamp=1777954100.2873867 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:20] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777954100.6909769 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:21] operator / voice_transcript_final / voice: of
  meta: kind=final | timestamp=1777954101.314299 | source=final | confidence=0.56 | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:23] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777954103.9852648 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:24] operator / voice_transcript_partial / voice: death
  meta: kind=partial | timestamp=1777954104.3914502 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:24] operator / voice_transcript_partial / voice: the death of
  meta: kind=partial | timestamp=1777954104.6087053 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:25] operator / voice_transcript_partial / voice: the death of tiff
  meta: kind=partial | timestamp=1777954105.8343294 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:26] operator / voice_transcript_final / voice: the death of tiff
  meta: kind=final | timestamp=1777954106.4439547 | source=final | confidence=0.53 | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:27] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777954107.6710272 | source=windows | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:28] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777954108.2806966 | source=final | confidence=0.7 | frequency_hz=324.2 | rms=145 | updated_at=1777954091.41981
- [2026-05-05 12:08:31] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777954111.9277847 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:31] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777954111.9277847 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:32] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777954112.3324654 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:33] operator / voice_transcript_partial / voice: the evidence
  meta: kind=partial | timestamp=1777954113.1440134 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:33] operator / voice_transcript_partial / voice: the civil
  meta: kind=partial | timestamp=1777954113.5515625 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:33] operator / voice_transcript_partial / voice: the lives of women
  meta: kind=partial | timestamp=1777954113.75564 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:33] operator / voice_transcript_partial / voice: the evidence of a woman who
  meta: kind=partial | timestamp=1777954113.9604142 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:34] operator / voice_transcript_partial / voice: the evidence of a woman who in
  meta: kind=partial | timestamp=1777954114.570566 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:34] operator / voice_transcript_partial / voice: the evidence of a woman who in his
  meta: kind=partial | timestamp=1777954114.7758923 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:34] operator / voice_transcript_partial / voice: the sense of when and how and if
  meta: kind=partial | timestamp=1777954114.9762974 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:35] operator / voice_transcript_partial / voice: the evidence of a little and too far
  meta: kind=partial | timestamp=1777954115.178741 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:35] operator / voice_transcript_partial / voice: the evidence of a woman who in his civil war has
  meta: kind=partial | timestamp=1777954115.3834963 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:35] operator / voice_transcript_partial / voice: the lives of women and minorities in
  meta: kind=partial | timestamp=1777954115.5873249 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:36] operator / voice_transcript_partial / voice: the evidence of a woman who in his heart is in hiding
  meta: kind=partial | timestamp=1777954116.402373 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:37] operator / voice_transcript_final / voice: the evidence of a woman who in his heart is in hiding
  meta: kind=final | timestamp=1777954117.018425 | source=final | confidence=0.24 | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:40] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777954120.3104613 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:43] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777954123.1567264 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:43] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777954123.358652 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:44] operator / voice_transcript_partial / voice: fifth of
  meta: kind=partial | timestamp=1777954124.1687407 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:44] operator / voice_transcript_partial / voice: kiss of death
  meta: kind=partial | timestamp=1777954124.9834504 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:45] operator / voice_transcript_final / voice: kiss of death
  meta: kind=final | timestamp=1777954125.794543 | source=final | confidence=0.31 | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:45] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777954125.9930913 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:45] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777954125.9930913 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:46] operator / voice_transcript_partial / voice: has been
  meta: kind=partial | timestamp=1777954126.4015703 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:46] operator / voice_transcript_partial / voice: is the
  meta: kind=partial | timestamp=1777954126.6055915 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:46] operator / voice_transcript_partial / voice: extrusion
  meta: kind=partial | timestamp=1777954126.808637 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:47] operator / voice_transcript_partial / voice: slim than the
  meta: kind=partial | timestamp=1777954127.6365898 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:47] operator / voice_transcript_partial / voice: extrusion in
  meta: kind=partial | timestamp=1777954127.8394048 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:48] operator / voice_transcript_final / voice: extrusion in
  meta: kind=final | timestamp=1777954128.244212 | source=final | confidence=0.13 | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:52] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777954132.32761 | source=windows | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:53] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777954133.561477 | source=final | confidence=0.0 | frequency_hz=414.1 | rms=678 | updated_at=1777954111.7641444
- [2026-05-05 12:08:55] operator / voice_transcript_partial / voice: end
  meta: kind=partial | timestamp=1777954135.1791818 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:08:55] operator / voice_transcript_partial / voice: movie
  meta: kind=partial | timestamp=1777954135.3826582 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:08:56] operator / voice_transcript_partial / voice: movie in
  meta: kind=partial | timestamp=1777954136.401631 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:08:56] operator / voice_transcript_partial / voice: movie-
  meta: kind=partial | timestamp=1777954136.6069276 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:08:56] operator / voice_transcript_partial / voice: movie they have
  meta: kind=partial | timestamp=1777954136.8121748 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:08:57] operator / voice_transcript_partial / voice: movie they have a
  meta: kind=partial | timestamp=1777954137.017439 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:08:58] operator / voice_transcript_final / voice: movie they have a
  meta: kind=final | timestamp=1777954138.258033 | source=final | confidence=0.21 | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:21] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777954161.856502 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:21] operator / voice_transcript_partial / voice: use
  meta: kind=partial | timestamp=1777954161.856502 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:23] operator / voice_transcript_final / voice: eighth
  meta: kind=final | timestamp=1777954163.0713544 | source=final | confidence=0.18 | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:24] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777954164.307476 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:34] operator / voice_transcript_partial / voice: through
  meta: kind=partial | timestamp=1777954174.0786545 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:34] operator / voice_transcript_partial / voice: through the
  meta: kind=partial | timestamp=1777954174.4798124 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:34] operator / voice_transcript_partial / voice: through the end
  meta: kind=partial | timestamp=1777954174.682563 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:34] operator / voice_transcript_partial / voice: through the indian
  meta: kind=partial | timestamp=1777954174.887597 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:35] operator / voice_transcript_partial / voice: through the indian woman
  meta: kind=partial | timestamp=1777954175.0889013 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:36] operator / voice_transcript_final / voice: through the indian woman
  meta: kind=final | timestamp=1777954176.3106682 | source=final | confidence=0.25 | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:37] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777954177.3233583 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:37] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777954177.5255015 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:37] operator / voice_transcript_partial / voice: of the
  meta: kind=partial | timestamp=1777954177.72843 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:38] operator / voice_transcript_partial / voice: living room
  meta: kind=partial | timestamp=1777954178.5398808 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:38] operator / voice_transcript_partial / voice: living rooms
  meta: kind=partial | timestamp=1777954178.7447448 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:39] operator / voice_transcript_partial / voice: living rooms and
  meta: kind=partial | timestamp=1777954179.1513371 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:39] operator / voice_transcript_partial / voice: living rooms among the
  meta: kind=partial | timestamp=1777954179.3545723 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:39] operator / voice_transcript_partial / voice: of living has come into
  meta: kind=partial | timestamp=1777954179.5565655 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:39] operator / voice_transcript_partial / voice: living rooms and influence
  meta: kind=partial | timestamp=1777954179.7584143 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:40] operator / voice_transcript_final / voice: living rooms and influence
  meta: kind=final | timestamp=1777954180.928657 | source=final | confidence=0.13 | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:42] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777954182.8060915 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:43] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777954183.0108428 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:43] operator / voice_transcript_final / voice: one
  meta: kind=final | timestamp=1777954183.619799 | source=final | confidence=0.43 | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:46] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777954186.4681072 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:46] operator / voice_transcript_partial / voice: visit
  meta: kind=partial | timestamp=1777954186.6721163 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:46] operator / voice_transcript_partial / voice: is to
  meta: kind=partial | timestamp=1777954186.8771448 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:47] operator / voice_transcript_partial / voice: is to have
  meta: kind=partial | timestamp=1777954187.4890418 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:47] operator / voice_transcript_partial / voice: is to a new
  meta: kind=partial | timestamp=1777954187.8939 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:48] operator / voice_transcript_partial / voice: to two and
  meta: kind=partial | timestamp=1777954188.097675 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:48] operator / voice_transcript_partial / voice: to two and one
  meta: kind=partial | timestamp=1777954188.5026405 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:49] operator / voice_transcript_partial / voice: to two and one is
  meta: kind=partial | timestamp=1777954189.317116 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:50] operator / voice_transcript_final / voice: to two and one is
  meta: kind=final | timestamp=1777954190.1350021 | source=final | confidence=0.1 | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:50] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777954190.5399494 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:51] operator / voice_transcript_partial / voice: is on the
  meta: kind=partial | timestamp=1777954191.1549776 | source=windows | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:09:52] operator / voice_transcript_final / voice: is on the
  meta: kind=final | timestamp=1777954192.1704416 | source=final | confidence=0.55 | frequency_hz=393.3 | rms=612 | updated_at=1777954134.8048325
- [2026-05-05 12:10:01] operator / voice_transcript_partial / voice: rear
  meta: kind=partial | timestamp=1777954201.3223286 | source=windows | frequency_hz=382.6 | rms=350 | updated_at=1777954201.2460275
- [2026-05-05 12:10:01] operator / voice_transcript_partial / voice: moon
  meta: kind=partial | timestamp=1777954201.5261335 | source=windows | frequency_hz=367.6 | rms=327 | updated_at=1777954201.3661227
- [2026-05-05 12:10:02] operator / voice_transcript_partial / voice: removes
  meta: kind=partial | timestamp=1777954202.1383731 | source=windows | frequency_hz=367.6 | rms=327 | updated_at=1777954201.3661227
- [2026-05-05 12:10:02] operator / voice_transcript_partial / voice: moves are
  meta: kind=partial | timestamp=1777954202.343058 | source=windows | frequency_hz=367.6 | rms=327 | updated_at=1777954201.3661227
- [2026-05-05 12:10:02] operator / voice_transcript_partial / voice: ruins of
  meta: kind=partial | timestamp=1777954202.5472884 | source=windows | frequency_hz=382.5 | rms=178 | updated_at=1777954202.52625
- [2026-05-05 12:10:02] operator / voice_transcript_partial / voice: way to susan
  meta: kind=partial | timestamp=1777954202.9534144 | source=windows | frequency_hz=351.6 | rms=197 | updated_at=1777954202.9062796
- [2026-05-05 12:10:03] operator / voice_transcript_partial / voice: reviews for the move
  meta: kind=partial | timestamp=1777954203.5584815 | source=windows | frequency_hz=346.1 | rms=197 | updated_at=1777954203.0361178
- [2026-05-05 12:10:04] operator / voice_transcript_final / voice: reviews for the move
  meta: kind=final | timestamp=1777954204.589115 | source=final | confidence=0.19 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:04] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777954204.589115 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:05] operator / voice_transcript_partial / voice: an inch
  meta: kind=partial | timestamp=1777954205.2036335 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:06] operator / voice_transcript_partial / voice: an inch to
  meta: kind=partial | timestamp=1777954206.0183308 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:06] operator / voice_transcript_final / voice: an inch to
  meta: kind=final | timestamp=1777954206.4350493 | source=final | confidence=0.26 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:13] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777954213.1542134 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:13] operator / voice_transcript_partial / voice: six
  meta: kind=partial | timestamp=1777954213.3585443 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:13] operator / voice_transcript_partial / voice: see some
  meta: kind=partial | timestamp=1777954213.5615256 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:13] operator / voice_transcript_partial / voice: cease and
  meta: kind=partial | timestamp=1777954213.7674782 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:13] operator / voice_transcript_partial / voice: susan and
  meta: kind=partial | timestamp=1777954213.971438 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:14] operator / voice_transcript_partial / voice: season as an
  meta: kind=partial | timestamp=1777954214.585181 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:14] operator / voice_transcript_partial / voice: susan and
  meta: kind=partial | timestamp=1777954214.7910576 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:14] operator / voice_transcript_partial / voice: susan and it's
  meta: kind=partial | timestamp=1777954214.9976482 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:15] operator / voice_transcript_partial / voice: season and has since
  meta: kind=partial | timestamp=1777954215.2038043 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:15] operator / voice_transcript_partial / voice: susan and cities and
  meta: kind=partial | timestamp=1777954215.8174393 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:16] operator / voice_transcript_final / voice: susan and cities and
  meta: kind=final | timestamp=1777954216.4290638 | source=final | confidence=0.23 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:17] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1777954217.2430272 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:17] operator / voice_transcript_final / voice: it s
  meta: kind=final | timestamp=1777954217.8698807 | source=final | confidence=0.72 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:20] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777954220.4989426 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:20] operator / voice_transcript_partial / voice: move
  meta: kind=partial | timestamp=1777954220.4989426 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:20] operator / voice_transcript_partial / voice: moving
  meta: kind=partial | timestamp=1777954220.7036552 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:21] operator / voice_transcript_partial / voice: move
  meta: kind=partial | timestamp=1777954221.1116626 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:21] operator / voice_transcript_final / voice: move
  meta: kind=final | timestamp=1777954221.3178003 | source=final | confidence=0.61 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:22] operator / voice_transcript_partial / voice: them
  meta: kind=partial | timestamp=1777954222.7662044 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:22] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777954222.9692376 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:23] operator / voice_transcript_partial / voice: among the
  meta: kind=partial | timestamp=1777954223.380665 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:23] operator / voice_transcript_partial / voice: the money the city
  meta: kind=partial | timestamp=1777954223.987472 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:24] operator / voice_transcript_partial / voice: among the city's
  meta: kind=partial | timestamp=1777954224.1904986 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:24] operator / voice_transcript_partial / voice: among the cities in the
  meta: kind=partial | timestamp=1777954224.393479 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:25] operator / voice_transcript_partial / voice: among the city's high-
  meta: kind=partial | timestamp=1777954225.2129242 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:25] operator / voice_transcript_final / voice: among the city s high
  meta: kind=final | timestamp=1777954225.8260415 | source=final | confidence=0.1 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:27] operator / voice_transcript_partial / voice: run
  meta: kind=partial | timestamp=1777954227.4736524 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:28] operator / voice_transcript_partial / voice: room of
  meta: kind=partial | timestamp=1777954228.6885514 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:29] operator / voice_transcript_final / voice: room of
  meta: kind=final | timestamp=1777954229.712651 | source=final | confidence=0.47 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:31] operator / voice_transcript_partial / voice: his
  meta: kind=partial | timestamp=1777954231.1345613 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:35] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777954235.2219222 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:35] operator / voice_transcript_partial / voice: his
  meta: kind=partial | timestamp=1777954235.4244516 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:35] operator / voice_transcript_partial / voice: his window
  meta: kind=partial | timestamp=1777954235.6308603 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:36] operator / voice_transcript_partial / voice: his of the
  meta: kind=partial | timestamp=1777954236.0377564 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:36] operator / voice_transcript_partial / voice: his window is
  meta: kind=partial | timestamp=1777954236.241303 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:36] operator / voice_transcript_partial / voice: his window is on
  meta: kind=partial | timestamp=1777954236.4442766 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:37] operator / voice_transcript_partial / voice: his of the death of an
  meta: kind=partial | timestamp=1777954237.2601798 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:37] operator / voice_transcript_partial / voice: his window is on in
  meta: kind=partial | timestamp=1777954237.4638276 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:37] operator / voice_transcript_partial / voice: his window is on in the
  meta: kind=partial | timestamp=1777954237.667282 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:38] operator / voice_transcript_partial / voice: his window is on in the house is
  meta: kind=partial | timestamp=1777954238.483024 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:38] operator / voice_transcript_partial / voice: his window is on in the houses and
  meta: kind=partial | timestamp=1777954238.6856055 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:39] operator / voice_transcript_final / voice: his window is on in the houses and
  meta: kind=final | timestamp=1777954239.506785 | source=final | confidence=0.22 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:40] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777954240.724569 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:41] operator / voice_transcript_partial / voice: their
  meta: kind=partial | timestamp=1777954241.9422238 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:42] operator / voice_transcript_partial / voice: there is a
  meta: kind=partial | timestamp=1777954242.5526836 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:43] operator / voice_transcript_partial / voice: there is a fifth
  meta: kind=partial | timestamp=1777954243.1591728 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:43] operator / voice_transcript_partial / voice: there is of the
  meta: kind=partial | timestamp=1777954243.5658548 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:44] operator / voice_transcript_partial / voice: therein lies in the name of the
  meta: kind=partial | timestamp=1777954244.3780499 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:45] operator / voice_transcript_final / voice: therein lies in the name of the
  meta: kind=final | timestamp=1777954245.6010237 | source=final | confidence=0.13 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:47] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777954247.0308795 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:47] operator / voice_transcript_partial / voice: death of
  meta: kind=partial | timestamp=1777954247.6410787 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:48] operator / voice_transcript_final / voice: death of
  meta: kind=final | timestamp=1777954248.4579496 | source=final | confidence=0.3 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:49] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777954249.0654218 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:50] operator / voice_transcript_final / voice: an
  meta: kind=final | timestamp=1777954250.5712428 | source=final | confidence=0.39 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:50] operator / voice_transcript_partial / voice: eighth
  meta: kind=partial | timestamp=1777954250.572248 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:51] operator / voice_transcript_partial / voice: eighth of
  meta: kind=partial | timestamp=1777954251.3033974 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:51] operator / voice_transcript_partial / voice: eighth of the
  meta: kind=partial | timestamp=1777954251.710138 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:52] operator / voice_transcript_partial / voice: eighth of them has a
  meta: kind=partial | timestamp=1777954252.3182487 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:52] operator / voice_transcript_partial / voice: eighth of them has a pool of
  meta: kind=partial | timestamp=1777954252.932775 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:53] operator / voice_transcript_final / voice: eighth of them has a pool of
  meta: kind=final | timestamp=1777954253.5562043 | source=final | confidence=0.51 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:55] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777954255.3815289 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:57] operator / voice_transcript_partial / voice: if
  meta: kind=partial | timestamp=1777954257.6218822 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:57] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777954257.8249047 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:58] operator / voice_transcript_partial / voice: death and
  meta: kind=partial | timestamp=1777954258.6374156 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:58] operator / voice_transcript_partial / voice: of none of
  meta: kind=partial | timestamp=1777954258.8409538 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:10:59] operator / voice_transcript_final / voice: of none of
  meta: kind=final | timestamp=1777954259.4564695 | source=final | confidence=0.09 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:00] operator / voice_transcript_partial / voice: us
  meta: kind=partial | timestamp=1777954260.2696998 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:01] operator / voice_transcript_final / voice: us
  meta: kind=final | timestamp=1777954261.4321995 | source=final | confidence=0.46 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:01] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777954261.8975852 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:02] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777954262.1010957 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:02] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777954262.3050525 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:02] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777954262.5095837 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:02] operator / voice_transcript_partial / voice: in office
  meta: kind=partial | timestamp=1777954262.7135067 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:03] operator / voice_transcript_partial / voice: in the office of
  meta: kind=partial | timestamp=1777954263.1205232 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:03] operator / voice_transcript_final / voice: in office
  meta: kind=final | timestamp=1777954263.3251133 | source=final | confidence=0.27 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:31] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777954291.4372294 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:32] operator / voice_transcript_partial / voice: he ha
  meta: kind=partial | timestamp=1777954292.049953 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:32] operator / voice_transcript_partial / voice: he ha in
  meta: kind=partial | timestamp=1777954292.9002185 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:33] operator / voice_transcript_partial / voice: he ha ha ha
  meta: kind=partial | timestamp=1777954293.1313055 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:33] operator / voice_transcript_partial / voice: he ha ve-
  meta: kind=partial | timestamp=1777954293.5650444 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:36] operator / voice_transcript_partial / voice: he ha ve-one
  meta: kind=partial | timestamp=1777954296.44793 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:36] operator / voice_transcript_partial / voice: he ha in one of
  meta: kind=partial | timestamp=1777954296.6542451 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:36] operator / voice_transcript_partial / voice: he ha ve-off
  meta: kind=partial | timestamp=1777954296.8687994 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:37] operator / voice_transcript_partial / voice: he ha ve-off in
  meta: kind=partial | timestamp=1777954297.4820457 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:37] operator / voice_transcript_partial / voice: he ha ha ha ha ha ha ha ha
  meta: kind=partial | timestamp=1777954297.7112005 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:38] operator / voice_transcript_partial / voice: he ha ha ha ha ha ha ha ha ha
  meta: kind=partial | timestamp=1777954298.3099413 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:38] operator / voice_transcript_final / voice: he ha ha ha ha ha ha ha ha ha
  meta: kind=final | timestamp=1777954298.924684 | source=final | confidence=0.35 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:40] operator / voice_transcript_partial / voice: ha
  meta: kind=partial | timestamp=1777954300.6501167 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:40] operator / voice_transcript_partial / voice: -
  meta: kind=partial | timestamp=1777954300.8516598 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:41] operator / voice_transcript_partial / voice: life
  meta: kind=partial | timestamp=1777954301.0550838 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:42] operator / voice_transcript_partial / voice: life he
  meta: kind=partial | timestamp=1777954302.075037 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:42] operator / voice_transcript_partial / voice: life in
  meta: kind=partial | timestamp=1777954302.2730122 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:42] operator / voice_transcript_partial / voice: life in the
  meta: kind=partial | timestamp=1777954302.4770718 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:42] operator / voice_transcript_partial / voice: life in a high
  meta: kind=partial | timestamp=1777954302.889465 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:43] operator / voice_transcript_final / voice: life in a high
  meta: kind=final | timestamp=1777954303.5335894 | source=final | confidence=0.28 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:43] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777954303.8183634 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:44] operator / voice_transcript_partial / voice: heel
  meta: kind=partial | timestamp=1777954304.0261917 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:44] operator / voice_transcript_partial / voice: heel is
  meta: kind=partial | timestamp=1777954304.639124 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:44] operator / voice_transcript_partial / voice: heel is one
  meta: kind=partial | timestamp=1777954304.8460891 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:45] operator / voice_transcript_partial / voice: heel he has
  meta: kind=partial | timestamp=1777954305.048485 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:45] operator / voice_transcript_partial / voice: heel and have
  meta: kind=partial | timestamp=1777954305.2495198 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:45] operator / voice_transcript_partial / voice: heel and who
  meta: kind=partial | timestamp=1777954305.6595027 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:45] operator / voice_transcript_partial / voice: heel and have
  meta: kind=partial | timestamp=1777954305.8792653 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:46] operator / voice_transcript_partial / voice: heel and who he
  meta: kind=partial | timestamp=1777954306.0770571 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:46] operator / voice_transcript_partial / voice: heel and who he is
  meta: kind=partial | timestamp=1777954306.287658 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:47] operator / voice_transcript_final / voice: heel and who he is
  meta: kind=final | timestamp=1777954307.3392406 | source=final | confidence=0.3 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:48] operator / voice_transcript_partial / voice: gay
  meta: kind=partial | timestamp=1777954308.6018693 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:49] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777954309.008571 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:49] operator / voice_transcript_final / voice: he
  meta: kind=final | timestamp=1777954309.4482925 | source=final | confidence=0.7 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:51] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777954311.0794969 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:51] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777954311.6915507 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:52] operator / voice_transcript_partial / voice: the isi
  meta: kind=partial | timestamp=1777954312.0973244 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:52] operator / voice_transcript_partial / voice: the eyes of
  meta: kind=partial | timestamp=1777954312.3038185 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:53] operator / voice_transcript_partial / voice: the eyes of the
  meta: kind=partial | timestamp=1777954313.4107156 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:53] operator / voice_transcript_partial / voice: the one who is a
  meta: kind=partial | timestamp=1777954313.4112227 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:53] operator / voice_transcript_partial / voice: the one that has
  meta: kind=partial | timestamp=1777954313.6704214 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:54] operator / voice_transcript_partial / voice: the one that has won
  meta: kind=partial | timestamp=1777954314.0215614 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:54] operator / voice_transcript_partial / voice: the one that has claimed he
  meta: kind=partial | timestamp=1777954314.8370702 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:55] operator / voice_transcript_final / voice: the one that has claimed he
  meta: kind=final | timestamp=1777954315.655286 | source=final | confidence=0.15 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:56] operator / voice_transcript_partial / voice: may
  meta: kind=partial | timestamp=1777954316.5456698 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:56] operator / voice_transcript_partial / voice: name
  meta: kind=partial | timestamp=1777954316.9526377 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:11:57] operator / voice_transcript_final / voice: name
  meta: kind=final | timestamp=1777954317.3795514 | source=final | confidence=0.79 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:12:09] operator / voice_transcript_partial / voice: of the
  meta: kind=partial | timestamp=1777954329.0723789 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:12:09] operator / voice_transcript_partial / voice: may
  meta: kind=partial | timestamp=1777954329.4778574 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:12:09] operator / voice_transcript_partial / voice: game
  meta: kind=partial | timestamp=1777954329.6853485 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:12:09] operator / voice_transcript_partial / voice: of the half
  meta: kind=partial | timestamp=1777954329.888263 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:12:10] operator / voice_transcript_partial / voice: of the half-
  meta: kind=partial | timestamp=1777954330.8637526 | source=windows | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
- [2026-05-05 12:12:11] operator / voice_transcript_final / voice: of the half
  meta: kind=final | timestamp=1777954331.8518755 | source=final | confidence=0.34 | frequency_hz=356.2 | rms=143 | updated_at=1777954204.186363
