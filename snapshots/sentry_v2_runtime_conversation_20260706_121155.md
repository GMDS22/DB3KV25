# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-07-06 12:11:55
- Entries: 124
- Roles: {'assistant': 6, 'system': 93, 'operator': 25}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 93, 'spoken_confirmation': 4, 'voice_transcript_partial': 20, 'voice_transcript_final': 3, 'voice_command': 2}
- Channels: {'text': 2, 'voice': 122}
- Latest operator request: you know you re listening
- Latest assistant message: I am listening. Ask your question.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-07-06 11:14:13] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-07-06 11:14:13] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-07-06 11:14:15] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783307655.5492046 | source=vosk
- [2026-07-06 11:14:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783307657.5102282 | source=vosk
- [2026-07-06 11:14:52] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-07-06 11:14:55] operator / voice_transcript_partial / voice: smite
  meta: kind=partial | timestamp=1783307695.994553 | source=vosk | rms=517 | updated_at=1783307695.940956 | frequency_hz=156.3
- [2026-07-06 11:14:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783307696.1903799 | source=vosk | rms=728 | updated_at=1783307696.1903799 | frequency_hz=156.3
- [2026-07-06 11:14:56] operator / voice_transcript_partial / voice: smite century
  meta: kind=partial | timestamp=1783307696.2737215 | source=vosk | rms=728 | updated_at=1783307696.1903799 | frequency_hz=156.3
- [2026-07-06 11:14:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783307696.4437807 | source=vosk | rms=445 | updated_at=1783307696.4437807 | frequency_hz=156.3
- [2026-07-06 11:14:56] operator / voice_transcript_partial / voice: smite century has
  meta: kind=partial | timestamp=1783307696.4687085 | source=vosk | rms=445 | updated_at=1783307696.4437807 | frequency_hz=156.3
- [2026-07-06 11:14:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783307696.6906738 | source=vosk | rms=385 | updated_at=1783307696.6906738 | frequency_hz=156.3
- [2026-07-06 11:14:56] operator / voice_transcript_partial / voice: smite century as radical
  meta: kind=partial | timestamp=1783307696.7301097 | source=vosk | rms=385 | updated_at=1783307696.6906738 | frequency_hz=156.3
- [2026-07-06 11:14:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783307697.3493261 | source=vosk | rms=385 | updated_at=1783307696.6906738 | frequency_hz=156.3
- [2026-07-06 11:14:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783307697.941853 | source=vosk | rms=680 | updated_at=1783307697.941853 | frequency_hz=156.3
- [2026-07-06 11:14:57] operator / voice_transcript_partial / voice: smite century as reddit
  meta: kind=partial | timestamp=1783307697.9782255 | source=vosk | rms=680 | updated_at=1783307697.941853 | frequency_hz=156.3
- [2026-07-06 11:14:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783307698.4419513 | source=vosk | rms=680 | updated_at=1783307697.941853 | frequency_hz=156.3
- [2026-07-06 12:10:08] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783311008.2615428 | source=vosk | rms=680 | updated_at=1783307697.941853 | frequency_hz=156.3
- [2026-07-06 12:10:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311009.0137932 | source=vosk | rms=680 | updated_at=1783307697.941853 | frequency_hz=156.3
- [2026-07-06 12:10:11] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1783311011.9250417 | source=vosk | rms=1082 | updated_at=1783311011.7798183 | frequency_hz=151.3
- [2026-07-06 12:10:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311012.25279 | source=vosk | rms=426 | updated_at=1783311012.25279 | frequency_hz=151.3
- [2026-07-06 12:10:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311012.9496315 | source=vosk | rms=1201 | updated_at=1783311012.9496315 | frequency_hz=151.3
- [2026-07-06 12:10:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311013.2086687 | source=vosk | rms=1200 | updated_at=1783311013.0686343 | frequency_hz=151.3
- [2026-07-06 12:10:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311013.43723 | source=vosk | rms=1863 | updated_at=1783311013.3237443 | frequency_hz=151.3
- [2026-07-06 12:10:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311014.1883478 | source=vosk | rms=1200 | updated_at=1783311014.1883478 | frequency_hz=151.3
- [2026-07-06 12:10:14] operator / voice_transcript_partial / voice: alien start the
  meta: kind=partial | timestamp=1783311014.323405 | source=vosk | rms=1200 | updated_at=1783311014.1883478 | frequency_hz=151.3
- [2026-07-06 12:10:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311014.4117775 | source=vosk | rms=1200 | updated_at=1783311014.323405 | frequency_hz=151.3
- [2026-07-06 12:10:14] operator / voice_transcript_partial / voice: alien start the smart
  meta: kind=partial | timestamp=1783311014.4117775 | source=vosk | rms=1200 | updated_at=1783311014.323405 | frequency_hz=151.3
- [2026-07-06 12:10:14] operator / voice_transcript_partial / voice: alien start the smart center up
  meta: kind=partial | timestamp=1783311014.5351472 | source=vosk | rms=1068 | updated_at=1783311014.4117775 | frequency_hz=236.2
- [2026-07-06 12:10:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311014.5985036 | source=vosk | rms=1200 | updated_at=1783311014.5351472 | frequency_hz=271.8
- [2026-07-06 12:10:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311015.4471717 | source=vosk | rms=1202 | updated_at=1783311015.4471717 | frequency_hz=313.9
- [2026-07-06 12:10:15] operator / voice_transcript_final / voice: elion start the smart center up
  meta: kind=final | timestamp=1783311015.9997122 | source=final | rms=1202 | updated_at=1783311015.4471717 | frequency_hz=313.9
- [2026-07-06 12:10:16] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783311016.1033514 | source=state | rms=1202 | updated_at=1783311015.4471717 | frequency_hz=313.9
- [2026-07-06 12:10:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311016.190856 | source=state | rms=1202 | updated_at=1783311015.4471717 | frequency_hz=313.9
- [2026-07-06 12:10:17] operator / voice_command / voice: start the smart center up
  meta: normalized=True
- [2026-07-06 12:10:17] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-06 12:10:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311016.191856 | source=vosk | rms=653 | updated_at=1783311016.191856 | frequency_hz=313.9
- [2026-07-06 12:10:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311018.9385595 | source=vosk | rms=806 | updated_at=1783311017.952718 | frequency_hz=351.0
- [2026-07-06 12:10:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311020.6996627 | source=vosk | rms=1202 | updated_at=1783311020.6996627 | frequency_hz=351.0
- [2026-07-06 12:10:21] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783311021.5179782 | source=state | rms=1066 | updated_at=1783311020.947382 | frequency_hz=351.0
- [2026-07-06 12:10:21] assistant / spoken_confirmation / voice: Listening window closed. Smart Sentry is not actively guarding right now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-06 12:10:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311020.947382 | source=vosk | rms=1066 | updated_at=1783311020.947382 | frequency_hz=351.0
- [2026-07-06 12:10:21] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783311021.4395914 | source=vosk | rms=1066 | updated_at=1783311020.947382 | frequency_hz=351.0
- [2026-07-06 12:10:27] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783311027.9609325 | source=state | rms=1066 | updated_at=1783311020.947382 | frequency_hz=351.0
- [2026-07-06 12:10:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311027.9619331 | source=state | rms=1066 | updated_at=1783311020.947382 | frequency_hz=351.0
- [2026-07-06 12:10:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311028.2044046 | source=vosk | rms=1066 | updated_at=1783311020.947382 | frequency_hz=351.0
- [2026-07-06 12:10:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311029.9410675 | source=vosk | rms=1203 | updated_at=1783311028.9453354 | frequency_hz=351.0
- [2026-07-06 12:10:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311031.2546983 | source=vosk | rms=1203 | updated_at=1783311028.9453354 | frequency_hz=351.0
- [2026-07-06 12:10:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311034.9600673 | source=vosk | rms=671 | updated_at=1783311034.4426591 | frequency_hz=351.0
- [2026-07-06 12:10:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311035.438951 | source=vosk | rms=671 | updated_at=1783311034.4426591 | frequency_hz=351.0
- [2026-07-06 12:10:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311036.0818465 | source=vosk | rms=671 | updated_at=1783311034.4426591 | frequency_hz=351.0
- [2026-07-06 12:10:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311036.214252 | source=vosk | rms=671 | updated_at=1783311034.4426591 | frequency_hz=351.0
- [2026-07-06 12:10:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311039.1950445 | source=vosk | rms=1201 | updated_at=1783311038.5025074 | frequency_hz=351.0
- [2026-07-06 12:10:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311043.4773629 | source=vosk | rms=1201 | updated_at=1783311038.5025074 | frequency_hz=351.0
- [2026-07-06 12:10:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311043.9399118 | source=vosk | rms=1201 | updated_at=1783311038.5025074 | frequency_hz=351.0
- [2026-07-06 12:10:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311044.9501886 | source=vosk | rms=1202 | updated_at=1783311044.9501886 | frequency_hz=351.0
- [2026-07-06 12:10:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311047.442122 | source=vosk | rms=1083 | updated_at=1783311047.0015872 | frequency_hz=326.9
- [2026-07-06 12:10:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311047.7185237 | source=vosk | rms=2597 | updated_at=1783311047.7185237 | frequency_hz=326.9
- [2026-07-06 12:10:48] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1783311048.4721227 | source=vosk | rms=1201 | updated_at=1783311048.443021 | frequency_hz=314.7
- [2026-07-06 12:10:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311048.693398 | source=vosk | rms=3529 | updated_at=1783311048.693398 | frequency_hz=314.7
- [2026-07-06 12:10:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311049.6785052 | source=vosk | rms=1500 | updated_at=1783311049.6785052 | frequency_hz=314.7
- [2026-07-06 12:10:49] operator / voice_transcript_partial / voice: alien close
  meta: kind=partial | timestamp=1783311049.7562902 | source=vosk | rms=1500 | updated_at=1783311049.6785052 | frequency_hz=314.7
- [2026-07-06 12:10:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311049.9538996 | source=vosk | rms=1201 | updated_at=1783311049.9538996 | frequency_hz=273.9
- [2026-07-06 12:10:49] operator / voice_transcript_partial / voice: alien close to
  meta: kind=partial | timestamp=1783311049.9800599 | source=vosk | rms=1201 | updated_at=1783311049.9538996 | frequency_hz=273.9
- [2026-07-06 12:10:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311050.1856766 | source=vosk | rms=1204 | updated_at=1783311050.1856766 | frequency_hz=267.6
- [2026-07-06 12:10:50] operator / voice_transcript_partial / voice: alien close to smoke
  meta: kind=partial | timestamp=1783311050.2579308 | source=vosk | rms=1204 | updated_at=1783311050.1856766 | frequency_hz=267.6
- [2026-07-06 12:10:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311050.4683177 | source=vosk | rms=1201 | updated_at=1783311050.4683177 | frequency_hz=262.8
- [2026-07-06 12:10:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311050.6830077 | source=vosk | rms=1201 | updated_at=1783311050.6830077 | frequency_hz=245.0
- [2026-07-06 12:10:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311050.9311197 | source=vosk | rms=1201 | updated_at=1783311050.9311197 | frequency_hz=182.3
- [2026-07-06 12:10:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311051.7371042 | source=state | rms=1201 | updated_at=1783311050.9311197 | frequency_hz=182.3
- [2026-07-06 12:10:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311051.7371042 | source=vosk | rms=1204 | updated_at=1783311051.7371042 | frequency_hz=156.3
- [2026-07-06 12:10:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311053.4869502 | source=vosk | rms=1201 | updated_at=1783311053.000409 | frequency_hz=289.9
- [2026-07-06 12:11:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311069.8805907 | source=vosk | rms=1202 | updated_at=1783311069.8805907 | frequency_hz=289.9
- [2026-07-06 12:11:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311070.9707546 | source=vosk | rms=1034 | updated_at=1783311070.3980877 | frequency_hz=289.9
- [2026-07-06 12:11:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311074.411807 | source=vosk | rms=1200 | updated_at=1783311074.411807 | frequency_hz=289.9
- [2026-07-06 12:11:16] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1783311076.2458365 | source=vosk | rms=1200 | updated_at=1783311076.1816778 | frequency_hz=254.6
- [2026-07-06 12:11:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311076.3794892 | source=vosk | rms=4339 | updated_at=1783311076.3794892 | frequency_hz=237.6
- [2026-07-06 12:11:16] operator / voice_transcript_partial / voice: earlier in
  meta: kind=partial | timestamp=1783311076.4818919 | source=vosk | rms=4339 | updated_at=1783311076.3794892 | frequency_hz=237.6
- [2026-07-06 12:11:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311076.6766424 | source=vosk | rms=1777 | updated_at=1783311076.6766424 | frequency_hz=211.1
- [2026-07-06 12:11:16] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1783311076.698399 | source=vosk | rms=1777 | updated_at=1783311076.6766424 | frequency_hz=211.1
- [2026-07-06 12:11:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311077.5967946 | source=vosk | rms=1200 | updated_at=1783311077.5967946 | frequency_hz=211.1
- [2026-07-06 12:11:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311078.608336 | source=vosk | rms=1200 | updated_at=1783311077.5967946 | frequency_hz=211.1
- [2026-07-06 12:11:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311079.1675382 | source=vosk | rms=1181 | updated_at=1783311079.1675382 | frequency_hz=88.0
- [2026-07-06 12:11:19] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1783311079.4789553 | source=final | rms=1181 | updated_at=1783311079.1675382 | frequency_hz=88.0
- [2026-07-06 12:11:20] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-07-06 12:11:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311079.8989532 | source=vosk | rms=1205 | updated_at=1783311079.8989532 | frequency_hz=86.6
- [2026-07-06 12:11:21] assistant / spoken_confirmation / voice: I am listening. Ask your question.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-06 12:11:20] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783311080.3460367 | source=vosk | rms=653 | updated_at=1783311079.914509 | frequency_hz=95.5
- [2026-07-06 12:11:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311080.6302817 | source=vosk | rms=576 | updated_at=1783311080.6302817 | frequency_hz=95.5
- [2026-07-06 12:11:21] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783311081.1273744 | source=vosk | rms=576 | updated_at=1783311080.6302817 | frequency_hz=95.5
- [2026-07-06 12:11:21] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783311081.633128 | source=state | rms=576 | updated_at=1783311080.6302817 | frequency_hz=95.5
- [2026-07-06 12:11:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311081.713771 | source=state | rms=576 | updated_at=1783311080.6302817 | frequency_hz=95.5
- [2026-07-06 12:11:23] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783311083.9615443 | source=state | rms=576 | updated_at=1783311080.6302817 | frequency_hz=95.5
- [2026-07-06 12:11:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311086.595969 | source=vosk | rms=515 | updated_at=1783311086.595969 | frequency_hz=114.0
- [2026-07-06 12:11:27] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783311087.1433287 | source=vosk | rms=515 | updated_at=1783311086.595969 | frequency_hz=114.0
- [2026-07-06 12:11:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311087.5900757 | source=vosk | rms=1200 | updated_at=1783311087.5900757 | frequency_hz=206.4
- [2026-07-06 12:11:28] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783311088.8425949 | source=vosk | rms=445 | updated_at=1783311088.340409 | frequency_hz=223.8
- [2026-07-06 12:11:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311091.379349 | source=vosk | rms=1164 | updated_at=1783311091.379349 | frequency_hz=374.0
- [2026-07-06 12:11:34] operator / voice_transcript_partial / voice: in the
  meta: kind=partial | timestamp=1783311094.6234078 | source=vosk | rms=1203 | updated_at=1783311094.593733 | frequency_hz=298.8
- [2026-07-06 12:11:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311094.8533883 | source=vosk | rms=1200 | updated_at=1783311094.852874 | frequency_hz=298.8
- [2026-07-06 12:11:34] operator / voice_transcript_partial / voice: you know
  meta: kind=partial | timestamp=1783311094.931083 | source=vosk | rms=1200 | updated_at=1783311094.852874 | frequency_hz=298.8
- [2026-07-06 12:11:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311095.1293538 | source=vosk | rms=1201 | updated_at=1783311095.1293538 | frequency_hz=298.8
- [2026-07-06 12:11:35] operator / voice_transcript_partial / voice: you know you're
  meta: kind=partial | timestamp=1783311095.1568825 | source=vosk | rms=1201 | updated_at=1783311095.1293538 | frequency_hz=298.8
- [2026-07-06 12:11:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311095.357538 | source=vosk | rms=541 | updated_at=1783311095.357538 | frequency_hz=318.8
- [2026-07-06 12:11:35] operator / voice_transcript_partial / voice: you know you're listening
  meta: kind=partial | timestamp=1783311095.4018836 | source=vosk | rms=541 | updated_at=1783311095.357538 | frequency_hz=318.8
- [2026-07-06 12:11:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311096.3878074 | source=vosk | rms=525 | updated_at=1783311096.3878074 | frequency_hz=286.3
- [2026-07-06 12:11:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311096.6141984 | source=vosk | rms=1202 | updated_at=1783311096.6141984 | frequency_hz=286.3
- [2026-07-06 12:11:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311096.8739088 | source=vosk | rms=945 | updated_at=1783311096.8739088 | frequency_hz=276.4
- [2026-07-06 12:11:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311097.3396635 | source=vosk | rms=694 | updated_at=1783311097.3396635 | frequency_hz=297.3
- [2026-07-06 12:11:37] operator / voice_transcript_final / voice: you know you re listening
  meta: kind=final | timestamp=1783311097.8130424 | source=final | rms=694 | updated_at=1783311097.3396635 | frequency_hz=297.3
- [2026-07-06 12:11:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311097.92848 | source=vosk | rms=547 | updated_at=1783311097.92848 | frequency_hz=297.3
- [2026-07-06 12:11:39] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783311099.6863468 | source=state | rms=770 | updated_at=1783311099.339732 | frequency_hz=241.8
- [2026-07-06 12:11:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311099.7684991 | source=state | rms=770 | updated_at=1783311099.339732 | frequency_hz=241.8
- [2026-07-06 12:11:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311100.6136913 | source=vosk | rms=610 | updated_at=1783311100.6136913 | frequency_hz=241.8
- [2026-07-06 12:11:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311101.0925014 | source=vosk | rms=610 | updated_at=1783311100.6136913 | frequency_hz=241.8
- [2026-07-06 12:11:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311101.3394368 | source=vosk | rms=1200 | updated_at=1783311101.3394368 | frequency_hz=241.8
- [2026-07-06 12:11:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311102.5951145 | source=vosk | rms=1681 | updated_at=1783311102.09108 | frequency_hz=201.0
- [2026-07-06 12:11:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311102.8411567 | source=vosk | rms=1681 | updated_at=1783311102.09108 | frequency_hz=201.0
- [2026-07-06 12:11:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311103.3932915 | source=vosk | rms=1681 | updated_at=1783311102.09108 | frequency_hz=201.0
- [2026-07-06 12:11:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311103.859458 | source=vosk | rms=1681 | updated_at=1783311102.09108 | frequency_hz=201.0
- [2026-07-06 12:11:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311104.8435042 | source=vosk | rms=578 | updated_at=1783311104.0962625 | frequency_hz=201.0
- [2026-07-06 12:11:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311109.4703841 | source=vosk | rms=1204 | updated_at=1783311109.4703841 | frequency_hz=116.0
- [2026-07-06 12:11:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311111.976341 | source=vosk | rms=1201 | updated_at=1783311110.994663 | frequency_hz=289.1
- [2026-07-06 12:11:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783311112.2236137 | source=vosk | rms=1200 | updated_at=1783311112.2236137 | frequency_hz=289.1
- [2026-07-06 12:11:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783311112.9971902 | source=vosk | rms=1201 | updated_at=1783311112.474474 | frequency_hz=289.1
