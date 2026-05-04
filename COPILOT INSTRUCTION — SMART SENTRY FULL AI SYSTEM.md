🧠 COPILOT INSTRUCTION — SMART SENTRY FULL AI SYSTEM
🎯 OBJECTIVE

Transform Smart Sentry into a voice-controlled, AI-assisted, self-tuning operator system that:

Accepts natural language voice commands
Uses offline AI reasoning via Ollama
Provides real-time system analysis
Executes only validated structured actions
Supports conversational follow-ups safely
Auto-tunes performance based on tracking metrics
Displays full AI reasoning before execution in a live dashboard
Speaks all outputs using natural TTS (Azure neural or offline WAV system)
🏗️ SYSTEM ARCHITECTURE (STRICT LAYERS)
🔁 MASTER PIPELINE
Voice Input
   ↓
Speech-to-Text (Vosk offline)
   ↓
Intent Parser (Ollama)
   ↓
📊 AI Decision Dashboard (preview only)
   ↓
Validation Layer (strict rules)
   ↓
Auto-Tuning Engine (optional adjustment)
   ↓
Execution Layer (hardware control only)
   ↓
Voice Feedback (TTS output)
🔵 1. ANALYSIS ENGINE (READ-ONLY AI)
PURPOSE

Provide system status explanation only. No control decisions.

INPUT
Live system state
OUTPUT
Operational description
System behavior summary
Tactical status (idle, tracking, fire-ready)
RULES
Never executes commands
Never modifies state
Always speaks after system updates
PROMPT STYLE
You are a Smart Sentry operator AI.

Describe system behavior based on state:
- tracking status
- target lock
- readiness
- stability

Be concise, tactical, and factual.
Do not accept or execute commands.
🟡 2. COMMAND / INTENT ENGINE (ACTIVE CONTROL)
PURPOSE

Convert natural language into structured actions.

EXAMPLES:
“Increase aiming speed”
“Set brightness to 70”
“Start tracking”
OUTPUT FORMAT (STRICT JSON)
{
  "action": "set_speed",
  "value": 7,
  "confidence": 0.85,
  "needs_clarification": false,
  "question": "",
  "suggestions": []
}
RULES
Only allowed actions from predefined schema
If unclear → ask clarification
Never execute directly
CLARIFICATION EXAMPLE

User:

“Increase speed”

AI:

“What speed level do you want? Low (3), Medium (5), High (8)?”

⚙️ 3. VALIDATION LAYER (HARD SAFETY GATE)
PURPOSE

Ensure all actions are safe before execution.

RULES
Clamp values to allowed ranges
Reject unknown actions
Normalize invalid input
📊 4. LIVE AI DASHBOARD (MANDATORY)
PURPOSE

Show full AI reasoning BEFORE execution.

DISPLAY CONTENT
User command
Parsed intent
Confidence score
Validation result
Auto-tuning adjustments
Final execution plan
RULE

👉 NOTHING executes until shown in dashboard

🧠 5. AUTO-TUNING ENGINE (ADAPTIVE BEHAVIOR)
PURPOSE

Dynamically adjust system performance based on tracking metrics.

METRICS USED
tracking stability
target loss frequency
motor oscillation
response delay
BEHAVIOR EXAMPLES
If instability detected → reduce speed
If lag detected → simplify tracking logic
If target loss increases → improve smoothing
RULES
Only incremental adjustments
Never exceed safe bounds
Always visible in dashboard
🔁 6. EXECUTION LAYER (HARDWARE CONTROL ONLY)
PURPOSE

The ONLY layer allowed to change physical system state.

RULES
Must receive validated + tuned actions
No AI direct control allowed
Must log every action
🎤 7. VOICE SYSTEM (INPUT + OUTPUT)
INPUT
Offline speech-to-text via Vosk
Wake word recommended (“sentry”)
OUTPUT
Pre-generated WAV alerts OR
Azure neural TTS via Azure Speech Service
BEHAVIOR
Instant WAV for alerts:
target detected
tracking engaged
standby
Neural TTS for AI responses:
analysis
suggestions
confirmations
🧠 8. CONVERSATION MODE (SAFE FOLLOW-UPS)
PURPOSE

Handle natural follow-up questions safely.

EXAMPLES:
“What do you suggest?”
“Is it stable?”
“Should I slow it down?”
RULES
Analysis engine handles ONLY informational answers
Command engine handles ONLY actionable requests
No mixing roles
🧠 9. MEMORY SYSTEM (SEPARATED)
memory = {
    "analysis_history": [],
    "command_history": []
}
RULES
Analysis memory = system explanations
Command memory = user actions + intents
Only last 2–3 entries used in prompts
🔐 GLOBAL SAFETY RULES (NON-NEGOTIABLE)
AI NEVER directly controls hardware
Execution ONLY happens through validated layer
Dashboard approval is mandatory
Auto-tuning is incremental only
No blocking calls in main tracking loop
Voice system must never freeze control system
🔁 FINAL SYSTEM BEHAVIOR
EXAMPLE FLOW

User:

“Can you increase aiming speed?”

System:

STT converts voice → text
Ollama parses intent
Dashboard shows:
set_speed = 7
confidence = 0.84
auto-tune adjustment = +1
Final execution = speed 8
System executes

Voice response:

“Speed increased to level 8 due to tracking optimization.”

ANALYSIS EXAMPLE

System state update:

“System is in active tracking mode. Target lock is stable. Motor performance within optimal range.”

FOLLOW-UP EXAMPLE

User:

“What do you suggest?”

AI:

“Reduce speed slightly to improve stability under current oscillation conditions.”

🚀 FINAL RESULT

You now have a system that is:

Voice-controlled
Context-aware
Self-optimizing
Fully transparent (dashboard-driven)
Safe (multi-layer validation)
Offline-capable via Ollama
Human-like in speech via neural TTS