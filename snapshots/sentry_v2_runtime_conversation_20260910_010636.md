# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-09-10 01:06:36
- Entries: 249
- Roles: {'assistant': 3, 'system': 147, 'operator': 99}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 147, 'voice_transcript_partial': 95, 'voice_transcript_final': 4, 'spoken_confirmation': 1}
- Channels: {'text': 2, 'voice': 247}
- Latest operator request: yeah be dead
- Latest assistant message: Smart Sentry is ready.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-09-10 00:20:51] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-09-10 00:20:51] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-09-10 00:20:55] system / voice_status / voice: listening
  meta: kind=status | timestamp=1788970855.3554862 | source=vosk
- [2026-09-10 00:20:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970856.3627176 | source=vosk | rms=513 | updated_at=1788970856.3627176
- [2026-09-10 00:20:57] operator / voice_transcript_partial / voice: responding
  meta: kind=partial | timestamp=1788970857.5175397 | source=vosk | rms=320 | updated_at=1788970857.361832
- [2026-09-10 00:20:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970857.6118317 | source=vosk | rms=321 | updated_at=1788970857.6118317
- [2026-09-10 00:20:57] operator / voice_transcript_partial / voice: responding to an
  meta: kind=partial | timestamp=1788970857.7611332 | source=vosk | rms=321 | updated_at=1788970857.6118317
- [2026-09-10 00:20:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970857.8614619 | source=vosk | rms=319 | updated_at=1788970857.8614619
- [2026-09-10 00:20:57] operator / voice_transcript_partial / voice: responding to any
  meta: kind=partial | timestamp=1788970857.9951334 | source=vosk | rms=319 | updated_at=1788970857.8614619
- [2026-09-10 00:20:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970858.6127152 | source=vosk | rms=762 | updated_at=1788970858.6127152
- [2026-09-10 00:20:58] operator / voice_transcript_partial / voice: responding to any expressed
  meta: kind=partial | timestamp=1788970858.6534941 | source=vosk | rms=762 | updated_at=1788970858.6127152
- [2026-09-10 00:20:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970858.8610456 | source=vosk | rms=828 | updated_at=1788970858.8610456
- [2026-09-10 00:20:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970859.112317 | source=vosk | rms=890 | updated_at=1788970859.1118
- [2026-09-10 00:20:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970859.361615 | source=vosk | rms=186 | updated_at=1788970859.361615
- [2026-09-10 00:20:59] operator / voice_transcript_partial / voice: responding to any expressed yeah
  meta: kind=partial | timestamp=1788970859.389781 | source=vosk | rms=186 | updated_at=1788970859.361615
- [2026-09-10 00:20:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970859.6137419 | source=vosk | rms=720 | updated_at=1788970859.6137419
- [2026-09-10 00:20:59] operator / voice_transcript_partial / voice: responding to any expressed yeah yeah
  meta: kind=partial | timestamp=1788970859.6312153 | source=vosk | rms=720 | updated_at=1788970859.6137419
- [2026-09-10 00:20:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970859.862435 | source=vosk | rms=558 | updated_at=1788970859.862435
- [2026-09-10 00:21:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970860.3622274 | source=vosk | rms=312 | updated_at=1788970860.3622274
- [2026-09-10 00:21:00] operator / voice_transcript_partial / voice: responding to any expressed yeah yeah you're right i
  meta: kind=partial | timestamp=1788970860.4978163 | source=vosk | rms=312 | updated_at=1788970860.3622274
- [2026-09-10 00:21:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970860.6125314 | source=vosk | rms=749 | updated_at=1788970860.6120098
- [2026-09-10 00:21:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970860.8618205 | source=vosk | rms=825 | updated_at=1788970860.8618205
- [2026-09-10 00:21:00] operator / voice_transcript_partial / voice: responding to any expressed yeah yeah you're right i have
  meta: kind=partial | timestamp=1788970860.9970977 | source=vosk | rms=825 | updated_at=1788970860.8618205
- [2026-09-10 00:21:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970861.1112216 | source=vosk | rms=649 | updated_at=1788970861.1112216
- [2026-09-10 00:21:01] operator / voice_transcript_partial / voice: responding to any expressed yeah yeah you're right i'm not
  meta: kind=partial | timestamp=1788970861.2000384 | source=vosk | rms=649 | updated_at=1788970861.1112216
- [2026-09-10 00:21:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970861.3611517 | source=vosk | rms=276 | updated_at=1788970861.3611517
- [2026-09-10 00:21:01] operator / voice_transcript_partial / voice: responding to any expressed yeah yeah you're right i have not been
  meta: kind=partial | timestamp=1788970861.4502525 | source=vosk | rms=276 | updated_at=1788970861.3611517
- [2026-09-10 00:21:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970861.6116896 | source=vosk | rms=263 | updated_at=1788970861.6116896
- [2026-09-10 00:21:01] operator / voice_transcript_partial / voice: responding to any expressed yeah yeah you're right i'm not putting
  meta: kind=partial | timestamp=1788970861.6866224 | source=vosk | rms=263 | updated_at=1788970861.6116896
- [2026-09-10 00:21:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970861.862888 | source=vosk | rms=771 | updated_at=1788970861.861379
- [2026-09-10 00:21:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970862.1134264 | source=vosk | rms=564 | updated_at=1788970862.1134264
- [2026-09-10 00:21:02] operator / voice_transcript_partial / voice: responding to any expressed yeah yeah you're right i have not been a regular
  meta: kind=partial | timestamp=1788970862.213871 | source=vosk | rms=564 | updated_at=1788970862.1134264
- [2026-09-10 00:21:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970862.3627074 | source=vosk | rms=648 | updated_at=1788970862.3627074
- [2026-09-10 00:21:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970862.6131175 | source=vosk | rms=552 | updated_at=1788970862.6126003
- [2026-09-10 00:21:02] operator / voice_transcript_partial / voice: responding to any expressed yeah yeah you're right i have not been a regulated
  meta: kind=partial | timestamp=1788970862.7391462 | source=vosk | rms=552 | updated_at=1788970862.6126003
- [2026-09-10 00:21:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970862.862269 | source=vosk | rms=369 | updated_at=1788970862.862269
- [2026-09-10 00:21:02] operator / voice_transcript_partial / voice: responding to any expressed yeah yeah you're right i have not been a regular
  meta: kind=partial | timestamp=1788970862.976744 | source=vosk | rms=369 | updated_at=1788970862.862269
- [2026-09-10 00:21:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970863.112475 | source=vosk | rms=335 | updated_at=1788970863.112475
- [2026-09-10 00:21:03] operator / voice_transcript_partial / voice: responding to any expressed yeah yeah you're right i have not been a radioactive isotope
  meta: kind=partial | timestamp=1788970863.1699798 | source=vosk | rms=335 | updated_at=1788970863.112475
- [2026-09-10 00:21:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970863.362078 | source=vosk | rms=241 | updated_at=1788970863.362078
- [2026-09-10 00:21:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970863.8622851 | source=vosk | rms=241 | updated_at=1788970863.362078
- [2026-09-10 00:21:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970864.1122034 | source=vosk | rms=289 | updated_at=1788970864.1122034
- [2026-09-10 00:21:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970864.361429 | source=vosk | rms=912 | updated_at=1788970864.361429
- [2026-09-10 00:21:04] operator / voice_transcript_final / voice: responding to any expressed yeah yeah you re right i have not a right attitude
  meta: kind=final | timestamp=1788970864.8038173 | source=final | rms=912 | updated_at=1788970864.361429
- [2026-09-10 00:21:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970864.924031 | source=vosk | rms=912 | updated_at=1788970864.361429
- [2026-09-10 00:21:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970864.924031 | source=vosk | rms=460 | updated_at=1788970864.924031
- [2026-09-10 00:21:05] operator / voice_transcript_partial / voice: okay
  meta: kind=partial | timestamp=1788970865.1209497 | source=vosk | rms=310 | updated_at=1788970865.1118438
- [2026-09-10 00:21:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970865.3625395 | source=vosk | rms=916 | updated_at=1788970865.3625395
- [2026-09-10 00:21:05] operator / voice_transcript_partial / voice: okay in
  meta: kind=partial | timestamp=1788970865.388896 | source=vosk | rms=916 | updated_at=1788970865.3625395
- [2026-09-10 00:21:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970865.6125886 | source=vosk | rms=376 | updated_at=1788970865.6125886
- [2026-09-10 00:21:05] operator / voice_transcript_partial / voice: okay
  meta: kind=partial | timestamp=1788970865.6529367 | source=vosk | rms=376 | updated_at=1788970865.6125886
- [2026-09-10 00:21:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970865.8610618 | source=vosk | rms=208 | updated_at=1788970865.8610618
- [2026-09-10 00:21:05] operator / voice_transcript_partial / voice: okay in a
  meta: kind=partial | timestamp=1788970865.95954 | source=vosk | rms=208 | updated_at=1788970865.8610618
- [2026-09-10 00:21:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970866.1119595 | source=vosk | rms=573 | updated_at=1788970866.1119595
- [2026-09-10 00:21:06] operator / voice_transcript_partial / voice: okay adding
  meta: kind=partial | timestamp=1788970866.1652846 | source=vosk | rms=573 | updated_at=1788970866.1119595
- [2026-09-10 00:21:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970866.6124644 | source=vosk | rms=668 | updated_at=1788970866.6124644
- [2026-09-10 00:21:32] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-09-10 00:21:06] operator / voice_transcript_partial / voice: okay i've been through
  meta: kind=partial | timestamp=1788970866.680707 | source=vosk | rms=668 | updated_at=1788970866.6124644
- [2026-09-10 00:21:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970866.8622894 | source=vosk | rms=412 | updated_at=1788970866.8622894
- [2026-09-10 00:21:06] operator / voice_transcript_partial / voice: okay adding strict
  meta: kind=partial | timestamp=1788970866.977087 | source=vosk | rms=412 | updated_at=1788970866.8622894
- [2026-09-10 00:21:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970867.1122293 | source=vosk | rms=627 | updated_at=1788970867.1122293
- [2026-09-10 00:21:07] operator / voice_transcript_partial / voice: okay adding shrugged his shoulders
  meta: kind=partial | timestamp=1788970867.1355784 | source=vosk | rms=627 | updated_at=1788970867.1122293
- [2026-09-10 00:21:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970867.3616273 | source=vosk | rms=498 | updated_at=1788970867.3616273
- [2026-09-10 00:21:07] operator / voice_transcript_partial / voice: okay i've been struck his
  meta: kind=partial | timestamp=1788970867.400564 | source=vosk | rms=498 | updated_at=1788970867.3616273
- [2026-09-10 00:21:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970867.6114225 | source=vosk | rms=498 | updated_at=1788970867.3616273
- [2026-09-10 00:21:07] operator / voice_transcript_partial / voice: okay i've been struck his description
  meta: kind=partial | timestamp=1788970867.6761868 | source=vosk | rms=498 | updated_at=1788970867.3616273
- [2026-09-10 00:21:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970867.8622487 | source=vosk | rms=821 | updated_at=1788970867.8622487
- [2026-09-10 00:21:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970868.1126342 | source=vosk | rms=821 | updated_at=1788970867.8622487
- [2026-09-10 00:21:08] operator / voice_transcript_partial / voice: okay i've been struck his description is that
  meta: kind=partial | timestamp=1788970868.151313 | source=vosk | rms=821 | updated_at=1788970867.8622487
- [2026-09-10 00:21:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970868.6120672 | source=vosk | rms=821 | updated_at=1788970867.8622487
- [2026-09-10 00:21:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970868.8611188 | source=vosk | rms=821 | updated_at=1788970867.8622487
- [2026-09-10 00:21:08] operator / voice_transcript_partial / voice: okay i've been struck his description is that a good
  meta: kind=partial | timestamp=1788970868.9552903 | source=vosk | rms=821 | updated_at=1788970867.8622487
- [2026-09-10 00:21:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970869.1119525 | source=vosk | rms=821 | updated_at=1788970867.8622487
- [2026-09-10 00:21:09] operator / voice_transcript_partial / voice: okay i've been struck his description is that of when we
  meta: kind=partial | timestamp=1788970869.1620238 | source=vosk | rms=821 | updated_at=1788970867.8622487
- [2026-09-10 00:21:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970869.611593 | source=vosk | rms=821 | updated_at=1788970867.8622487
- [2026-09-10 00:21:09] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally
  meta: kind=partial | timestamp=1788970869.6227436 | source=vosk | rms=821 | updated_at=1788970867.8622487
- [2026-09-10 00:21:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970870.1114025 | source=vosk | rms=821 | updated_at=1788970867.8622487
- [2026-09-10 00:21:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970870.6116412 | source=vosk | rms=1072 | updated_at=1788970870.6116412
- [2026-09-10 00:21:10] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into
  meta: kind=partial | timestamp=1788970870.6519034 | source=vosk | rms=1072 | updated_at=1788970870.6116412
- [2026-09-10 00:21:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970871.1128504 | source=vosk | rms=725 | updated_at=1788970871.1118479
- [2026-09-10 00:21:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970871.3620453 | source=vosk | rms=595 | updated_at=1788970871.3620453
- [2026-09-10 00:21:11] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm
  meta: kind=partial | timestamp=1788970871.401361 | source=vosk | rms=595 | updated_at=1788970871.3620453
- [2026-09-10 00:21:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970871.6113012 | source=vosk | rms=608 | updated_at=1788970871.6113012
- [2026-09-10 00:21:11] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into our i mean
  meta: kind=partial | timestamp=1788970871.649022 | source=vosk | rms=608 | updated_at=1788970871.6113012
- [2026-09-10 00:21:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970871.8619556 | source=vosk | rms=494 | updated_at=1788970871.8619556
- [2026-09-10 00:21:11] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into our i mean that
  meta: kind=partial | timestamp=1788970871.9256618 | source=vosk | rms=494 | updated_at=1788970871.8619556
- [2026-09-10 00:21:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970872.1119628 | source=vosk | rms=494 | updated_at=1788970871.8619556
- [2026-09-10 00:21:12] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if
  meta: kind=partial | timestamp=1788970872.146163 | source=vosk | rms=494 | updated_at=1788970871.8619556
- [2026-09-10 00:21:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970872.36171 | source=vosk | rms=494 | updated_at=1788970871.8619556
- [2026-09-10 00:21:12] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it were
  meta: kind=partial | timestamp=1788970872.3841474 | source=vosk | rms=494 | updated_at=1788970871.8619556
- [2026-09-10 00:21:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970872.6117926 | source=vosk | rms=864 | updated_at=1788970872.6117926
- [2026-09-10 00:21:12] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it would
  meta: kind=partial | timestamp=1788970872.6354752 | source=vosk | rms=864 | updated_at=1788970872.6117926
- [2026-09-10 00:21:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970872.861224 | source=vosk | rms=908 | updated_at=1788970872.861224
- [2026-09-10 00:21:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970873.1115344 | source=vosk | rms=771 | updated_at=1788970873.1115344
- [2026-09-10 00:21:13] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it would bypass
  meta: kind=partial | timestamp=1788970873.167626 | source=vosk | rms=771 | updated_at=1788970873.1115344
- [2026-09-10 00:21:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970873.3611376 | source=vosk | rms=541 | updated_at=1788970873.3611376
- [2026-09-10 00:21:13] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and
  meta: kind=partial | timestamp=1788970873.4232676 | source=vosk | rms=541 | updated_at=1788970873.3611376
- [2026-09-10 00:21:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970873.8615842 | source=vosk | rms=858 | updated_at=1788970873.8615842
- [2026-09-10 00:21:13] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five hundred
  meta: kind=partial | timestamp=1788970873.9343598 | source=vosk | rms=858 | updated_at=1788970873.8615842
- [2026-09-10 00:21:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970874.1117063 | source=vosk | rms=881 | updated_at=1788970874.1117063
- [2026-09-10 00:21:14] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had a bank or
  meta: kind=partial | timestamp=1788970874.1746826 | source=vosk | rms=881 | updated_at=1788970874.1117063
- [2026-09-10 00:21:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970874.3629637 | source=vosk | rms=1094 | updated_at=1788970874.3629637
- [2026-09-10 00:21:14] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five hundred
  meta: kind=partial | timestamp=1788970874.4139233 | source=vosk | rms=1094 | updated_at=1788970874.3629637
- [2026-09-10 00:21:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970874.6119082 | source=vosk | rms=764 | updated_at=1788970874.6119082
- [2026-09-10 00:21:14] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by
  meta: kind=partial | timestamp=1788970874.674236 | source=vosk | rms=764 | updated_at=1788970874.6119082
- [2026-09-10 00:21:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970875.1113353 | source=vosk | rms=764 | updated_at=1788970874.6119082
- [2026-09-10 00:21:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970875.8612344 | source=vosk | rms=764 | updated_at=1788970874.6119082
- [2026-09-10 00:21:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970876.3618002 | source=vosk | rms=764 | updated_at=1788970874.6119082
- [2026-09-10 00:21:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970876.6117353 | source=vosk | rms=764 | updated_at=1788970874.6119082
- [2026-09-10 00:21:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970876.862198 | source=vosk | rms=851 | updated_at=1788970876.862198
- [2026-09-10 00:21:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970877.1118436 | source=vosk | rms=851 | updated_at=1788970876.862198
- [2026-09-10 00:21:17] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by ideas
  meta: kind=partial | timestamp=1788970877.156472 | source=vosk | rms=851 | updated_at=1788970876.862198
- [2026-09-10 00:21:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970877.363627 | source=vosk | rms=851 | updated_at=1788970876.862198
- [2026-09-10 00:21:17] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably
  meta: kind=partial | timestamp=1788970877.391245 | source=vosk | rms=851 | updated_at=1788970876.862198
- [2026-09-10 00:21:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970877.6117663 | source=vosk | rms=676 | updated_at=1788970877.6117663
- [2026-09-10 00:21:17] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little
  meta: kind=partial | timestamp=1788970877.6426015 | source=vosk | rms=676 | updated_at=1788970877.6117663
- [2026-09-10 00:21:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970877.8611312 | source=vosk | rms=581 | updated_at=1788970877.8611312
- [2026-09-10 00:21:17] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much
  meta: kind=partial | timestamp=1788970877.9181864 | source=vosk | rms=581 | updated_at=1788970877.8611312
- [2026-09-10 00:21:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970878.1116378 | source=vosk | rms=618 | updated_at=1788970878.1116378
- [2026-09-10 00:21:18] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more
  meta: kind=partial | timestamp=1788970878.145441 | source=vosk | rms=618 | updated_at=1788970878.1116378
- [2026-09-10 00:21:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970878.3620312 | source=vosk | rms=578 | updated_at=1788970878.3620312
- [2026-09-10 00:21:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970878.6118155 | source=vosk | rms=578 | updated_at=1788970878.3620312
- [2026-09-10 00:21:18] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right
  meta: kind=partial | timestamp=1788970878.6493957 | source=vosk | rms=578 | updated_at=1788970878.3620312
- [2026-09-10 00:21:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970878.8618248 | source=vosk | rms=936 | updated_at=1788970878.8618248
- [2026-09-10 00:21:18] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to
  meta: kind=partial | timestamp=1788970878.8927066 | source=vosk | rms=936 | updated_at=1788970878.8618248
- [2026-09-10 00:21:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970879.1120703 | source=vosk | rms=703 | updated_at=1788970879.1120703
- [2026-09-10 00:21:19] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to eighteen
  meta: kind=partial | timestamp=1788970879.1447675 | source=vosk | rms=703 | updated_at=1788970879.1120703
- [2026-09-10 00:21:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970879.6115382 | source=vosk | rms=547 | updated_at=1788970879.6115382
- [2026-09-10 00:21:19] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to a
  meta: kind=partial | timestamp=1788970879.647048 | source=vosk | rms=547 | updated_at=1788970879.6115382
- [2026-09-10 00:21:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970879.8615072 | source=vosk | rms=465 | updated_at=1788970879.8615072
- [2026-09-10 00:21:19] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i asked
  meta: kind=partial | timestamp=1788970879.9261389 | source=vosk | rms=465 | updated_at=1788970879.8615072
- [2026-09-10 00:21:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970880.1119647 | source=vosk | rms=465 | updated_at=1788970879.8615072
- [2026-09-10 00:21:20] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think
  meta: kind=partial | timestamp=1788970880.1555321 | source=vosk | rms=465 | updated_at=1788970879.8615072
- [2026-09-10 00:21:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970880.362997 | source=vosk | rms=507 | updated_at=1788970880.362997
- [2026-09-10 00:21:20] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that it
  meta: kind=partial | timestamp=1788970880.3760517 | source=vosk | rms=507 | updated_at=1788970880.362997
- [2026-09-10 00:21:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970880.6126697 | source=vosk | rms=627 | updated_at=1788970880.6126697
- [2026-09-10 00:21:20] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the guy
  meta: kind=partial | timestamp=1788970880.665227 | source=vosk | rms=627 | updated_at=1788970880.6126697
- [2026-09-10 00:21:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970880.861261 | source=vosk | rms=627 | updated_at=1788970880.6126697
- [2026-09-10 00:21:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970881.3613665 | source=vosk | rms=643 | updated_at=1788970881.3613665
- [2026-09-10 00:21:21] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea
  meta: kind=partial | timestamp=1788970881.3784087 | source=vosk | rms=643 | updated_at=1788970881.3613665
- [2026-09-10 00:21:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970881.8615398 | source=vosk | rms=643 | updated_at=1788970881.3613665
- [2026-09-10 00:21:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970882.8618095 | source=vosk | rms=643 | updated_at=1788970881.3613665
- [2026-09-10 00:21:22] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get
  meta: kind=partial | timestamp=1788970882.8859715 | source=vosk | rms=643 | updated_at=1788970881.3613665
- [2026-09-10 00:21:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970883.3629737 | source=vosk | rms=643 | updated_at=1788970881.3613665
- [2026-09-10 00:21:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970883.8616064 | source=vosk | rms=643 | updated_at=1788970881.3613665
- [2026-09-10 00:21:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970884.1116178 | source=vosk | rms=643 | updated_at=1788970881.3613665
- [2026-09-10 00:21:24] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your
  meta: kind=partial | timestamp=1788970884.1355011 | source=vosk | rms=643 | updated_at=1788970881.3613665
- [2026-09-10 00:21:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970884.3616204 | source=vosk | rms=600 | updated_at=1788970884.3616204
- [2026-09-10 00:21:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970884.6111329 | source=vosk | rms=600 | updated_at=1788970884.3616204
- [2026-09-10 00:21:24] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your role
  meta: kind=partial | timestamp=1788970884.7013688 | source=vosk | rms=600 | updated_at=1788970884.3616204
- [2026-09-10 00:21:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970884.8616083 | source=vosk | rms=778 | updated_at=1788970884.8616083
- [2026-09-10 00:21:24] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your well i don't
  meta: kind=partial | timestamp=1788970884.9090586 | source=vosk | rms=778 | updated_at=1788970884.8616083
- [2026-09-10 00:21:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970885.3616693 | source=vosk | rms=778 | updated_at=1788970884.8616083
- [2026-09-10 00:21:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970885.611542 | source=vosk | rms=778 | updated_at=1788970884.8616083
- [2026-09-10 00:21:25] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your well i don't know how
  meta: kind=partial | timestamp=1788970885.658759 | source=vosk | rms=778 | updated_at=1788970884.8616083
- [2026-09-10 00:21:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970885.8614 | source=vosk | rms=778 | updated_at=1788970884.8616083
- [2026-09-10 00:21:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970886.1113896 | source=vosk | rms=778 | updated_at=1788970884.8616083
- [2026-09-10 00:21:26] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your well i don't know how to much
  meta: kind=partial | timestamp=1788970886.135878 | source=vosk | rms=778 | updated_at=1788970884.8616083
- [2026-09-10 00:21:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970886.6117437 | source=vosk | rms=613 | updated_at=1788970886.6117437
- [2026-09-10 00:21:26] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your well i don't know how to much for your
  meta: kind=partial | timestamp=1788970886.6529934 | source=vosk | rms=613 | updated_at=1788970886.6117437
- [2026-09-10 00:21:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970886.8627872 | source=vosk | rms=512 | updated_at=1788970886.8627872
- [2026-09-10 00:21:26] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your well i don't know how to much for your title
  meta: kind=partial | timestamp=1788970886.9143589 | source=vosk | rms=512 | updated_at=1788970886.8627872
- [2026-09-10 00:21:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970887.1113954 | source=vosk | rms=512 | updated_at=1788970886.8627872
- [2026-09-10 00:21:27] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your well i don't know how to much for your can i tell you what
  meta: kind=partial | timestamp=1788970887.1384714 | source=vosk | rms=512 | updated_at=1788970886.8627872
- [2026-09-10 00:21:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970887.3614507 | source=vosk | rms=512 | updated_at=1788970886.8627872
- [2026-09-10 00:21:27] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your well i don't know how to much for your can i tell you what he told
  meta: kind=partial | timestamp=1788970887.4177997 | source=vosk | rms=512 | updated_at=1788970886.8627872
- [2026-09-10 00:21:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970887.6114955 | source=vosk | rms=512 | updated_at=1788970886.8627872
- [2026-09-10 00:21:27] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your well i don't know how to much for your can i tell you what he told us
  meta: kind=partial | timestamp=1788970887.6636097 | source=vosk | rms=512 | updated_at=1788970886.8627872
- [2026-09-10 00:21:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970888.1122851 | source=vosk | rms=512 | updated_at=1788970886.8627872
- [2026-09-10 00:21:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970888.61199 | source=vosk | rms=512 | updated_at=1788970886.8627872
- [2026-09-10 00:21:28] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your well i don't know how to much for your can i tell you what he told us about it
  meta: kind=partial | timestamp=1788970888.6435857 | source=vosk | rms=512 | updated_at=1788970886.8627872
- [2026-09-10 00:21:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970888.8615272 | source=vosk | rms=1140 | updated_at=1788970888.8615272
- [2026-09-10 00:21:28] operator / voice_transcript_partial / voice: okay i've been struck his description is that it literally into i'm i'm even if it was five and had advised by idea probably a little too much more right age to and i don't think that if the good idea to get your well i don't know how to much for your can i tell you what he told us about
  meta: kind=partial | timestamp=1788970888.884351 | source=vosk | rms=1140 | updated_at=1788970888.8615272
- [2026-09-10 00:21:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970889.1120958 | source=vosk | rms=1140 | updated_at=1788970888.8615272
- [2026-09-10 00:21:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970889.6127422 | source=vosk | rms=1140 | updated_at=1788970888.8615272
- [2026-09-10 00:21:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970890.361782 | source=vosk | rms=1140 | updated_at=1788970888.8615272
- [2026-09-10 00:21:31] operator / voice_transcript_final / voice: okay adding strict his description is that of literally into i m i m even if it would buy that i had advised by idea probably a little too much more right age to and i don t think that if the good idea to get your well i don t know how to much for your can i tell you what he told us about it
  meta: kind=final | timestamp=1788970891.3176498 | source=final | rms=1140 | updated_at=1788970888.8615272
- [2026-09-10 00:21:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970892.0635052 | source=vosk | rms=1140 | updated_at=1788970888.8615272
- [2026-09-10 00:21:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970892.0635052 | source=vosk | rms=1140 | updated_at=1788970888.8615272
- [2026-09-10 00:21:32] operator / voice_transcript_partial / voice: so is
  meta: kind=partial | timestamp=1788970892.195452 | source=vosk | rms=1140 | updated_at=1788970888.8615272
- [2026-09-10 00:21:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970892.246323 | source=vosk | rms=1140 | updated_at=1788970888.8615272
- [2026-09-10 00:21:32] operator / voice_transcript_partial / voice: so he said you
  meta: kind=partial | timestamp=1788970892.246323 | source=vosk | rms=1140 | updated_at=1788970888.8615272
- [2026-09-10 00:21:32] operator / voice_transcript_partial / voice: so he said you guys
  meta: kind=partial | timestamp=1788970892.2758505 | source=vosk | rms=495 | updated_at=1788970892.246323
- [2026-09-10 00:21:32] operator / voice_transcript_partial / voice: so he said you guys got
  meta: kind=partial | timestamp=1788970892.3171606 | source=vosk | rms=495 | updated_at=1788970892.246323
- [2026-09-10 00:21:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970892.6124299 | source=vosk | rms=495 | updated_at=1788970892.246323
- [2026-09-10 00:21:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970892.8627806 | source=vosk | rms=495 | updated_at=1788970892.246323
- [2026-09-10 00:21:32] operator / voice_transcript_partial / voice: so he said you guys got set up as
  meta: kind=partial | timestamp=1788970892.8913722 | source=vosk | rms=495 | updated_at=1788970892.246323
- [2026-09-10 00:21:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970893.112646 | source=vosk | rms=710 | updated_at=1788970893.112646
- [2026-09-10 00:21:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970893.362991 | source=vosk | rms=710 | updated_at=1788970893.112646
- [2026-09-10 00:21:33] operator / voice_transcript_partial / voice: so he said you guys got set up as your
  meta: kind=partial | timestamp=1788970893.3749866 | source=vosk | rms=710 | updated_at=1788970893.112646
- [2026-09-10 00:21:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970893.6114516 | source=vosk | rms=437 | updated_at=1788970893.6114516
- [2026-09-10 00:21:33] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's
  meta: kind=partial | timestamp=1788970893.621511 | source=vosk | rms=437 | updated_at=1788970893.6114516
- [2026-09-10 00:21:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970894.1127477 | source=vosk | rms=437 | updated_at=1788970893.6114516
- [2026-09-10 00:21:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970894.6115427 | source=vosk | rms=1016 | updated_at=1788970894.6115427
- [2026-09-10 00:21:34] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each
  meta: kind=partial | timestamp=1788970894.6446476 | source=vosk | rms=1016 | updated_at=1788970894.6115427
- [2026-09-10 00:21:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970894.9819665 | source=vosk | rms=439 | updated_at=1788970894.9819665
- [2026-09-10 00:21:35] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's knowledge on
  meta: kind=partial | timestamp=1788970895.069253 | source=vosk | rms=439 | updated_at=1788970894.9819665
- [2026-09-10 00:21:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970895.6128252 | source=vosk | rms=439 | updated_at=1788970894.9819665
- [2026-09-10 00:21:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970896.6126494 | source=vosk | rms=439 | updated_at=1788970894.9819665
- [2026-09-10 00:21:36] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah
  meta: kind=partial | timestamp=1788970896.6501029 | source=vosk | rms=439 | updated_at=1788970894.9819665
- [2026-09-10 00:21:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970896.8614783 | source=vosk | rms=658 | updated_at=1788970896.8614783
- [2026-09-10 00:21:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970897.1119895 | source=vosk | rms=1139 | updated_at=1788970897.1119895
- [2026-09-10 00:21:37] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah he says
  meta: kind=partial | timestamp=1788970897.2612538 | source=vosk | rms=1139 | updated_at=1788970897.1119895
- [2026-09-10 00:21:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970897.3628914 | source=vosk | rms=714 | updated_at=1788970897.3628914
- [2026-09-10 00:21:37] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said the smartest
  meta: kind=partial | timestamp=1788970897.4145203 | source=vosk | rms=714 | updated_at=1788970897.3628914
- [2026-09-10 00:21:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970897.6126273 | source=vosk | rms=537 | updated_at=1788970897.6126273
- [2026-09-10 00:21:37] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said smart
  meta: kind=partial | timestamp=1788970897.6580012 | source=vosk | rms=537 | updated_at=1788970897.6126273
- [2026-09-10 00:21:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970897.8614056 | source=vosk | rms=787 | updated_at=1788970897.8614056
- [2026-09-10 00:21:37] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said smart century is
  meta: kind=partial | timestamp=1788970897.8958411 | source=vosk | rms=787 | updated_at=1788970897.8614056
- [2026-09-10 00:21:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970898.3627799 | source=vosk | rms=787 | updated_at=1788970897.8614056
- [2026-09-10 00:21:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970898.6130102 | source=vosk | rms=539 | updated_at=1788970898.6130102
- [2026-09-10 00:21:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970898.8627627 | source=vosk | rms=539 | updated_at=1788970898.6130102
- [2026-09-10 00:21:38] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said smart century is my entire
  meta: kind=partial | timestamp=1788970898.9243903 | source=vosk | rms=539 | updated_at=1788970898.6130102
- [2026-09-10 00:21:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970899.113434 | source=vosk | rms=539 | updated_at=1788970898.6130102
- [2026-09-10 00:21:39] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said smart century is were times when
  meta: kind=partial | timestamp=1788970899.152728 | source=vosk | rms=539 | updated_at=1788970898.6130102
- [2026-09-10 00:21:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970899.3631392 | source=vosk | rms=429 | updated_at=1788970899.3626354
- [2026-09-10 00:21:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970899.862843 | source=vosk | rms=429 | updated_at=1788970899.3626354
- [2026-09-10 00:21:39] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said smart century is my time with that
  meta: kind=partial | timestamp=1788970899.9999945 | source=vosk | rms=429 | updated_at=1788970899.3626354
- [2026-09-10 00:21:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970900.114728 | source=vosk | rms=490 | updated_at=1788970900.114728
- [2026-09-10 00:21:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970900.3626754 | source=vosk | rms=541 | updated_at=1788970900.3626754
- [2026-09-10 00:21:40] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said smart century is my time with that phrase
  meta: kind=partial | timestamp=1788970900.411909 | source=vosk | rms=541 | updated_at=1788970900.3626754
- [2026-09-10 00:21:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970900.6125865 | source=vosk | rms=541 | updated_at=1788970900.3626754
- [2026-09-10 00:21:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970900.862962 | source=vosk | rms=632 | updated_at=1788970900.862962
- [2026-09-10 00:21:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970901.1128676 | source=vosk | rms=632 | updated_at=1788970900.862962
- [2026-09-10 00:21:41] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said smart century is my time with that phrase makes
  meta: kind=partial | timestamp=1788970901.147611 | source=vosk | rms=632 | updated_at=1788970900.862962
- [2026-09-10 00:21:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970901.3634174 | source=vosk | rms=632 | updated_at=1788970900.862962
- [2026-09-10 00:21:41] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said smart century is my time with that phrase make out
  meta: kind=partial | timestamp=1788970901.397928 | source=vosk | rms=632 | updated_at=1788970900.862962
- [2026-09-10 00:21:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970901.6126232 | source=vosk | rms=483 | updated_at=1788970901.6126232
- [2026-09-10 00:21:41] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said smart century is my time with that phrase make out on
  meta: kind=partial | timestamp=1788970901.631412 | source=vosk | rms=483 | updated_at=1788970901.6126232
- [2026-09-10 00:21:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970902.1177847 | source=vosk | rms=483 | updated_at=1788970901.6126232
- [2026-09-10 00:21:42] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said smart century is my time with that phrase make out on special
  meta: kind=partial | timestamp=1788970902.176253 | source=vosk | rms=483 | updated_at=1788970901.6126232
- [2026-09-10 00:21:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970902.61704 | source=vosk | rms=475 | updated_at=1788970902.61704
- [2026-09-10 00:21:42] operator / voice_transcript_partial / voice: so he said you guys got set up as your mom's know each other ah said smart century is my time with that phrase make out on his bed
  meta: kind=partial | timestamp=1788970902.6643445 | source=vosk | rms=475 | updated_at=1788970902.61704
- [2026-09-10 00:21:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970902.862681 | source=vosk | rms=677 | updated_at=1788970902.862681
- [2026-09-10 00:21:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970903.1129856 | source=vosk | rms=677 | updated_at=1788970902.862681
- [2026-09-10 00:21:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970903.3629797 | source=vosk | rms=541 | updated_at=1788970903.3629797
- [2026-09-10 00:21:44] operator / voice_transcript_final / voice: so he said you guys got set of as your mom s know on ah said smart sentry is my time with that phrase make out on his bed
  meta: kind=final | timestamp=1788970904.128394 | source=final | rms=541 | updated_at=1788970903.3629797
- [2026-09-10 00:21:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970904.9084837 | source=vosk | rms=541 | updated_at=1788970903.3629797
- [2026-09-10 00:21:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970904.9084837 | source=vosk | rms=1159 | updated_at=1788970904.9084837
- [2026-09-10 00:21:45] operator / voice_transcript_partial / voice: yeah
  meta: kind=partial | timestamp=1788970905.089776 | source=vosk | rms=494 | updated_at=1788970905.0297227
- [2026-09-10 00:21:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970905.0907793 | source=vosk | rms=494 | updated_at=1788970905.0297227
- [2026-09-10 00:21:45] operator / voice_transcript_partial / voice: yeah began
  meta: kind=partial | timestamp=1788970905.1815886 | source=vosk | rms=494 | updated_at=1788970905.0297227
- [2026-09-10 00:21:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970905.369466 | source=vosk | rms=550 | updated_at=1788970905.369466
- [2026-09-10 00:21:45] operator / voice_transcript_partial / voice: yeah be dead
  meta: kind=partial | timestamp=1788970905.435803 | source=vosk | rms=550 | updated_at=1788970905.369466
- [2026-09-10 00:21:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970905.6126268 | source=vosk | rms=1155 | updated_at=1788970905.6126268
- [2026-09-10 00:21:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970905.8631465 | source=vosk | rms=965 | updated_at=1788970905.8631465
- [2026-09-10 00:21:46] operator / voice_transcript_final / voice: yeah be dead
  meta: kind=final | timestamp=1788970906.4142897 | source=final | rms=965 | updated_at=1788970905.8631465
- [2026-09-10 00:21:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788970906.5835578 | source=vosk | rms=965 | updated_at=1788970905.8631465
- [2026-09-10 00:21:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788970906.5835578 | source=vosk | rms=888 | updated_at=1788970906.5835578
