// DB3000 ESP32 IO Telemetry Firmware (Dual-Port IO Board)
// --------------------------------------------------------
// Purpose:
//   - Use ESP32 USB serial (e.g., COM10) for IO/safety/trigger tokens from app.
//   - Keep PAN/TILT on Debug Board USB serial (e.g., COM9) handled by the app.
//
// Host command compatibility (same token set as app dual-port path):
//   - Single-token lines: S0, M1, F1, L1, R0, G1
//   - Packed lines also supported: F1L1R0G0S0M1
//
// Safety semantics:
//   - S1 = SAFE   (forces fire outputs OFF)
//   - S0 = ARMED
//
// Trigger mode semantics:
//   - M0 = Water mode (MOSFET output)
//   - M1 = Projectile mode (PWM trigger servo pulse)

#include <Arduino.h>

// ---------------- Serial ----------------
static const uint32_t HOST_BAUD = 115200;

// ---------------- Pin map (ESP32) ----------------
static const int PIN_TRIGGER_MOSFET = 27;
static const int PIN_TRIGGER_SERVO  = 13;
static const int PIN_LED_RELAY      = 32;
static const int PIN_LASER_RELAY    = 33;
static const int PIN_ACC_RELAY      = 25;

// ---------------- Trigger servo PWM (LEDC) ----------------
static const int SERVO_HZ = 50;
static const int SERVO_RES_BITS = 16;
static const int SERVO_MIN_US = 500;
static const int SERVO_MAX_US = 2500;
static const int SERVO_REST_DEG = 0;
static const int SERVO_FIRE_DEG = 40;
static const uint32_t SERVO_FIRE_PULSE_MS = 120;

// ---------------- State ----------------
static bool safety_is_safe = true;     // S1 default
static bool mode_projectile = false;   // M0 default

static int fire_token = 0;
static int led_token = 0;
static int laser_token = 0;
static int acc_token = 0;

static bool projectile_pulse_active = false;
static uint32_t projectile_pulse_start_ms = 0;

static String line_buf;

static uint32_t last_telemetry_ms = 0;

static int clampInt(int v, int lo, int hi) {
  if (v < lo) return lo;
  if (v > hi) return hi;
  return v;
}

static uint32_t degToDutyTicks(int deg) {
  const int clamped = clampInt(deg, 0, 180);
  const uint32_t us = (uint32_t)map(clamped, 0, 180, SERVO_MIN_US, SERVO_MAX_US);
  const uint32_t max_ticks = (1UL << SERVO_RES_BITS) - 1;
  const uint32_t period_us = 1000000UL / SERVO_HZ;
  uint32_t ticks = (us * max_ticks) / period_us;
  if (ticks > max_ticks) ticks = max_ticks;
  return ticks;
}

static void triggerServoSet(bool on) {
  ledcWrite(PIN_TRIGGER_SERVO, degToDutyTicks(on ? SERVO_FIRE_DEG : SERVO_REST_DEG));
}

static int parseTokenInt(const String &line, char token, int fallback) {
  int i = line.indexOf(token);
  if (i < 0 || i + 1 >= (int)line.length()) return fallback;
  int j = i + 1;
  bool neg = false;
  if (line.charAt(j) == '-') {
    neg = true;
    j++;
  }
  int value = 0;
  bool hasDigit = false;
  while (j < (int)line.length()) {
    char c = line.charAt(j);
    if (c < '0' || c > '9') break;
    hasDigit = true;
    value = value * 10 + (c - '0');
    j++;
  }
  if (!hasDigit) return fallback;
  return neg ? -value : value;
}

static void applyOutputs() {
  digitalWrite(PIN_LED_RELAY, led_token ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY, laser_token ? HIGH : LOW);
  digitalWrite(PIN_ACC_RELAY, acc_token ? HIGH : LOW);

  if (safety_is_safe) {
    digitalWrite(PIN_TRIGGER_MOSFET, LOW);
    triggerServoSet(false);
    fire_token = 0;
    projectile_pulse_active = false;
    return;
  }

  if (!mode_projectile) {
    // Water mode: direct MOSFET latch from fire token
    digitalWrite(PIN_TRIGGER_MOSFET, fire_token ? HIGH : LOW);
    triggerServoSet(false);
    projectile_pulse_active = false;
  } else {
    // Projectile mode: pulse servo on rising fire edge, auto-return after pulse window
    digitalWrite(PIN_TRIGGER_MOSFET, LOW);

    if (fire_token && !projectile_pulse_active) {
      projectile_pulse_active = true;
      projectile_pulse_start_ms = millis();
      triggerServoSet(true);
    }

    if (projectile_pulse_active) {
      if ((millis() - projectile_pulse_start_ms) >= SERVO_FIRE_PULSE_MS) {
        triggerServoSet(false);
        projectile_pulse_active = false;
        fire_token = 0;
      }
    } else {
      triggerServoSet(false);
    }
  }
}

static void handleLine(String line) {
  line.trim();
  if (line.length() == 0) return;

  // Uppercase for tolerant parsing
  line.toUpperCase();

  // Parse both packed and single-token variants.
  fire_token  = parseTokenInt(line, 'F', fire_token) ? 1 : 0;
  led_token   = parseTokenInt(line, 'L', led_token) ? 1 : 0;
  laser_token = parseTokenInt(line, 'R', laser_token) ? 1 : 0;
  acc_token   = parseTokenInt(line, 'G', acc_token) ? 1 : 0;

  int s = parseTokenInt(line, 'S', safety_is_safe ? 1 : 0);
  int m = parseTokenInt(line, 'M', mode_projectile ? 1 : 0);
  safety_is_safe = (s != 0);
  mode_projectile = (m != 0);

  applyOutputs();

  Serial.print("ACK ");
  Serial.print("S="); Serial.print(safety_is_safe ? 1 : 0);
  Serial.print(" M="); Serial.print(mode_projectile ? 1 : 0);
  Serial.print(" F="); Serial.print(fire_token);
  Serial.print(" L="); Serial.print(led_token);
  Serial.print(" R="); Serial.print(laser_token);
  Serial.print(" G="); Serial.println(acc_token);
}

void setup() {
  Serial.begin(HOST_BAUD);
  delay(50);

  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  pinMode(PIN_LED_RELAY, OUTPUT);
  pinMode(PIN_LASER_RELAY, OUTPUT);
  pinMode(PIN_ACC_RELAY, OUTPUT);

  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  digitalWrite(PIN_LED_RELAY, LOW);
  digitalWrite(PIN_LASER_RELAY, LOW);
  digitalWrite(PIN_ACC_RELAY, LOW);

  bool ledc_ok = ledcAttach(PIN_TRIGGER_SERVO, SERVO_HZ, SERVO_RES_BITS);
  if (!ledc_ok) {
    Serial.println("[BOOT] LEDC attach failed for trigger servo");
  }
  triggerServoSet(false);

  Serial.println("[BOOT] DB3000_ESP32_IO_Telemetry_2026 ready");
  Serial.println("[BOOT] Expected host tokens: S/M/F/L/R/G over USB serial");
}

void loop() {
  while (Serial.available() > 0) {
    char ch = (char)Serial.read();
    if (ch == '\r') continue;
    if (ch == '\n') {
      handleLine(line_buf);
      line_buf = "";
    } else {
      if (line_buf.length() < 200) line_buf += ch;
    }
  }

  // Keep outputs coherent (projectile pulse timeout handling)
  applyOutputs();

  // Lightweight telemetry line for host logs
  uint32_t now = millis();
  if ((now - last_telemetry_ms) >= 1000) {
    last_telemetry_ms = now;
    Serial.print("STAT S="); Serial.print(safety_is_safe ? 1 : 0);
    Serial.print(" M="); Serial.print(mode_projectile ? 1 : 0);
    Serial.print(" F="); Serial.print(fire_token);
    Serial.print(" L="); Serial.print(led_token);
    Serial.print(" R="); Serial.print(laser_token);
    Serial.print(" G="); Serial.println(acc_token);
  }
}
