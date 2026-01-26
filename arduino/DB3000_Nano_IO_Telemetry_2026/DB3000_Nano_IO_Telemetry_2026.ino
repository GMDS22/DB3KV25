/*
  DB3000 Nano IO + Telemetry (2026)
  -------------------------------
  Purpose (Dual Port topology):
  - Runs on the Arduino Nano (USB serial COM8 in your setup).
  - Handles IO tokens from the host (fire/relays/safety/mode).
  - Emits TOTAL current telemetry for the app's System Health Monitor:
      STAT I=<milliamps>\n
  Notes:
  - In Dual Port mode, PAN/TILT are driven directly by the Debug Board on COM9.
  - The host may send either:
      * Packed lines:  P..T..F..L..R..G..S..M..\n  (legacy)
      * IO-only lines: F..L..R..G..S..M..\n      (Dual Port)
      * Single-token lines used by test_nano_io.py: L1\n, R0\n, F1\n, S0\n, M0\n
  Safety invariant:
  - S1 = SAFE (default on boot) forces FIRE off.
  - S0 = ARMED allows FIRE.
*/

#include <Arduino.h>
#include <Servo.h>

// -----------------------
// Serial
// -----------------------
static const unsigned long HOST_BAUD = 115200;

// -----------------------
// Pin mapping (adjust to your wiring)
// -----------------------
static const uint8_t PIN_FIRE_MOSFET = 6;
static const uint8_t PIN_LED_RELAY = 4;
static const uint8_t PIN_LASER_RELAY = 5;
static const uint8_t PIN_ACC_RELAY = 7; // accessory token G

// Optional projectile trigger servo
static const uint8_t PIN_TRIGGER_SERVO = 9;
static const int TRIGGER_REST_DEG = 90;
static const int TRIGGER_FIRE_DEG = 120;

// Current sensor (user wiring: A2)
static const uint8_t PIN_CURRENT_SENSOR = A2;

// -----------------------
// Current sensor calibration
// -----------------------
// Update these two constants for your sensor (ACS712 examples):
//  - 5A:  0.185 V/A
//  - 20A: 0.100 V/A
//  - 30A: 0.066 V/A
static const float ADC_REF_V = 5.0f;
static const float SENSOR_ZERO_V = 2.50f;
static const float SENSOR_SENS_V_PER_A = 0.100f;

static const unsigned long CURRENT_REPORT_INTERVAL_MS = 100; // 10 Hz
static const uint8_t CURRENT_SAMPLES = 16;

// -----------------------
// State
// -----------------------
static bool safety_is_safe = true;   // S1 safe by default
static bool mode_projectile = false; // M0 water by default

static int fire_token = 0;
static int led_token = 0;
static int laser_token = 0;
static int acc_token = 0;

// PTEN is accepted for compatibility; Nano does not drive pan/tilt in Dual Port.
static bool enable_pan_tilt_output = false;

static unsigned long last_command_ms = 0;
static unsigned long last_current_ms = 0;

static Servo triggerServo;

// -----------------------
// Helpers
// -----------------------
static inline void applyOutputs() {
  digitalWrite(PIN_LED_RELAY, led_token ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY, laser_token ? HIGH : LOW);
  digitalWrite(PIN_ACC_RELAY, acc_token ? HIGH : LOW);

  // Safety ALWAYS wins.
  if (safety_is_safe) {
    digitalWrite(PIN_FIRE_MOSFET, LOW);
    triggerServo.write(TRIGGER_REST_DEG);
    return;
  }

  // Fire behavior depends on mode.
  if (!mode_projectile) {
    // Water mode: MOSFET/relay
    digitalWrite(PIN_FIRE_MOSFET, fire_token ? HIGH : LOW);
    triggerServo.write(TRIGGER_REST_DEG);
  } else {
    // Projectile mode: servo trigger
    digitalWrite(PIN_FIRE_MOSFET, LOW);
    triggerServo.write(fire_token ? TRIGGER_FIRE_DEG : TRIGGER_REST_DEG);
  }
}

static inline float readCurrentAmps() {
  unsigned long acc = 0;
  for (uint8_t i = 0; i < CURRENT_SAMPLES; i++) {
    acc += (unsigned long)analogRead(PIN_CURRENT_SENSOR);
  }
  const float adc = (float)acc / (float)CURRENT_SAMPLES;
  const float volts = (adc * ADC_REF_V) / 1023.0f;
  float amps = (volts - SENSOR_ZERO_V) / SENSOR_SENS_V_PER_A;
  // Clamp negative noise.
  if (amps < 0.0f) amps = 0.0f;
  return amps;
}

static inline long readCurrentMilliAmps() {
  const float amps = readCurrentAmps();
  long ma = (long)(amps * 1000.0f + 0.5f);
  if (ma < 0) ma = 0;
  return ma;
}

static inline int parseTokenInt(const char *s, char token, int defaultVal) {
  if (!s) return defaultVal;
  const char *p = strchr(s, token);
  if (!p) return defaultVal;
  p++; // after token

  // Skip optional separators/spaces: token may arrive as "PTEN 0" or "S:0" in some logs.
  while (*p == ' ' || *p == ':' || *p == '=') p++;

  bool neg = false;
  if (*p == '-') { neg = true; p++; }
  long v = 0;
  bool any = false;
  while (*p >= '0' && *p <= '9') {
    any = true;
    v = v * 10 + (*p - '0');
    p++;
  }
  if (!any) return defaultVal;
  if (neg) v = -v;
  return (int)v;
}

static inline void respondEncoder() {
  // Host expects: ENCODER_TILT,<tilt_deg>,RAW_COUNT,<count>
  Serial.print(F("ENCODER_TILT,"));
  Serial.print(TRIGGER_REST_DEG);
  Serial.print(F(",RAW_COUNT,"));
  Serial.println(0);
}

static inline void handleLine(char *line) {
  if (!line) return;

  // Trim leading spaces
  while (*line == ' ' || *line == '\t' || *line == '\r' || *line == '\n') line++;
  if (!*line) return;

  // Trim trailing CR/LF
  size_t n = strlen(line);
  while (n > 0 && (line[n - 1] == '\r' || line[n - 1] == '\n' || line[n - 1] == ' ' || line[n - 1] == '\t')) {
    line[n - 1] = 0;
    n--;
  }
  if (!*line) return;

  // Special commands
  if (strncmp(line, "GET_ENCODER", 11) == 0) {
    respondEncoder();
    return;
  }

  // PTEN compatibility (host may send "PTEN0" or "PTEN 0")
  if (strncmp(line, "PTEN", 4) == 0) {
    int v = 0;
    // Accept both formats
    if (line[4] == 0) {
      v = 0;
    } else {
      // Reuse token parser with pseudo-token 'N' by shifting pointer if needed
      // Simpler: parse digits after PTEN
      const char *p = line + 4;
      while (*p == ' ' || *p == '\t' || *p == ':' || *p == '=') p++;
      v = atoi(p);
    }
    enable_pan_tilt_output = (v != 0);
    Serial.print(F("PTEN="));
    Serial.println(enable_pan_tilt_output ? 1 : 0);
    return;
  }

  // Single-token lines (test_nano_io.py sends these)
  // L1, R0, F1, S0, M0, G1
  // FIX 2026-01-26: Check that the line is ACTUALLY a single token (2 chars max)
  // before treating it as such. This prevents packed commands like "F1L1R0G0S0M1"
  // from being misinterpreted as single-token "F1" (which would ignore mode/safety).
  size_t lineLen_check = strlen(line);
  bool isSingleToken = (lineLen_check <= 2) && 
      (line[0] == 'L' || line[0] == 'R' || line[0] == 'F' || line[0] == 'S' || line[0] == 'M' || line[0] == 'G') && 
      (lineLen_check == 1 || line[1] == '0' || line[1] == '1');
  
  if (isSingleToken) {
    char tok = line[0];
    int v = parseTokenInt(line, tok, 0);
    switch (tok) {
      case 'L': led_token = v ? 1 : 0; break;
      case 'R': laser_token = v ? 1 : 0; break;
      case 'G': acc_token = v ? 1 : 0; break;
      case 'F': fire_token = v ? 1 : 0; break;
      case 'S': safety_is_safe = (v != 0); break; // S1 safe, S0 armed
      case 'M': mode_projectile = (v != 0); break; // M1 projectile, M0 water
    }
    last_command_ms = millis();
    applyOutputs();
    return;
  }

  // Packed/combined lines: parse whichever tokens are present.
  // Accept both legacy P..T..F.. etc and Dual Port IO-only F..L..R.. etc.
  led_token = parseTokenInt(line, 'L', led_token) ? 1 : 0;
  laser_token = parseTokenInt(line, 'R', laser_token) ? 1 : 0;
  acc_token = parseTokenInt(line, 'G', acc_token) ? 1 : 0;
  fire_token = parseTokenInt(line, 'F', fire_token) ? 1 : 0;

  // Safety/mode tokens
  safety_is_safe = (parseTokenInt(line, 'S', safety_is_safe ? 1 : 0) != 0);
  mode_projectile = (parseTokenInt(line, 'M', mode_projectile ? 1 : 0) != 0);

  last_command_ms = millis();
  applyOutputs();
}

// -----------------------
// Serial line buffer
// -----------------------
static const size_t LINE_BUF_SIZE = 128;
static char lineBuf[LINE_BUF_SIZE];
static size_t lineLen = 0;

void setup() {
  Serial.begin(HOST_BAUD);

  pinMode(PIN_FIRE_MOSFET, OUTPUT);
  pinMode(PIN_LED_RELAY, OUTPUT);
  pinMode(PIN_LASER_RELAY, OUTPUT);
  pinMode(PIN_ACC_RELAY, OUTPUT);

  digitalWrite(PIN_FIRE_MOSFET, LOW);
  digitalWrite(PIN_LED_RELAY, LOW);
  digitalWrite(PIN_LASER_RELAY, LOW);
  digitalWrite(PIN_ACC_RELAY, LOW);

  triggerServo.attach(PIN_TRIGGER_SERVO);
  triggerServo.write(TRIGGER_REST_DEG);

  last_command_ms = millis();
  last_current_ms = millis();

  Serial.println(F("DB3000 Nano IO Telemetry 2026: READY"));
  Serial.println(F("[CUR] Telemetry: STAT I=<mA>"));
  Serial.println(F("[CUR] Total current sensor pin: A2"));
  Serial.println(F("[DUAL PORT] Nano handles IO + telemetry; PAN/TILT on Debug Board"));

  applyOutputs();
}

void loop() {
  // Non-blocking serial receive
  while (Serial.available() > 0) {
    char ch = (char)Serial.read();

    if (ch == '\n') {
      lineBuf[lineLen] = 0;
      handleLine(lineBuf);
      lineLen = 0;
      continue;
    }
    if (ch == '\r') continue;

    if (lineLen + 1 < LINE_BUF_SIZE) {
      lineBuf[lineLen++] = ch;
    } else {
      // Overflow: reset buffer
      lineLen = 0;
    }
  }

  // Fire watchdog: if host stops talking, force fire OFF.
  const unsigned long now = millis();
  if ((now - last_command_ms) > 1000UL) {
    fire_token = 0;
    applyOutputs();
  }

  // Current telemetry
  if ((now - last_current_ms) >= CURRENT_REPORT_INTERVAL_MS) {
    last_current_ms = now;
    const long totalMa = readCurrentMilliAmps();
    Serial.print(F("STAT I="));
    Serial.println(totalMa);
  }
}
