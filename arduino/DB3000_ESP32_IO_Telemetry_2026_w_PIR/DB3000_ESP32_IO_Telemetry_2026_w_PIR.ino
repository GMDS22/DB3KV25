// DB3000 ESP32 IO Telemetry Firmware with PIR Support (Dual-Port IO Board)
// -----------------------------------------------------------------------
// Purpose:
//   - Use ESP32 USB serial (e.g., COM10) for IO/safety/trigger tokens from app.
//   - Keep PAN/TILT on Debug Board USB serial (e.g., COM9) handled by the app.
//   - Monitor 3 PIR motion sensors and report detection events to host.
//
// Host command compatibility (same token set as app dual-port path):
//   - Single-token lines: S0, M1, F1, L1, R0, G1, P1 (P = PIR enable)
//   - Packed lines also supported: F1L1R0G0S0M1P1
//
// Safety semantics:
//   - S1 = SAFE   (forces fire outputs OFF)
//   - S0 = ARMED
//
// Trigger mode semantics:
//   - M0 = Water mode (MOSFET output)
//   - M1 = Projectile mode (PWM trigger servo pulse)
//
// PIR control semantics:
//   - P0 = PIR disabled (no sensor monitoring)
//   - P1 = PIR enabled (monitor 3 sensors for motion events)
//
// PIR telemetry format (sent when motion detected):
//   - PIR_EVENT sensor_id=X timestamp=YYYY
//     where X is 0, 1, or 2 for the 3 sensors

#include <Arduino.h>

// ========== Configuration ==========
#define ENABLE_PIR_SUPPORT 1      // Set to 1 to compile PIR code, 0 to disable

// ========== Serial ==========
static const uint32_t HOST_BAUD = 115200;

// ========== Pin Assignments (ESP32) ==========
// Output relays
static const int PIN_TRIGGER_MOSFET = 27;
static const int PIN_TRIGGER_SERVO  = 13;
static const int PIN_LED_RELAY      = 32;
static const int PIN_LASER_RELAY    = 33;
static const int PIN_ACC_RELAY      = 25;
static const int PIN_SPARE_RELAY    = 26;   // Spare relay
static const int PIN_STATUS_LED     = 2;    // ESP32 onboard status LED (blink on command changes)

// PIR input sensors (GPIO pins with internal pull-down, active HIGH)
static const int PIN_PIR_SENSOR_0   = 35;   // Sensor 0 — right zone  (cue ~45°)
static const int PIN_PIR_SENSOR_1   = 34;   // Sensor 1 — front zone  (cue ~135°)
static const int PIN_PIR_SENSOR_2   = 39;   // Sensor 2 — left zone   (cue ~225°)

// ========== Trigger Servo PWM (LEDC) ==========
static const int SERVO_HZ = 50;
static const int SERVO_RES_BITS = 16;
static const int SERVO_MIN_US = 500;
static const int SERVO_MAX_US = 2500;
static const int SERVO_REST_DEG = 0;
static const int SERVO_FIRE_DEG = 40;
static const uint32_t SERVO_FIRE_PULSE_MS = 120;

// ========== Runtime Trigger Config (app-controlled tokens) ==========
static uint32_t trigger_mosfet_pulse_ms = SERVO_FIRE_PULSE_MS;  // J token
static int trigger_mosfet_cycle_count = 1;                      // K token
static uint32_t trigger_mosfet_cycle_off_ms = 50;               // N token
static bool trigger_output_active_low = false;                  // X token
static int trigger_servo_rest_deg = SERVO_REST_DEG;             // U token
static int trigger_servo_fire_deg = SERVO_FIRE_DEG;             // V token
static int trigger_servo_speed_dps = 360;                       // H token (stored for parity)

static bool pir_event_blink_enabled = false;                    // B token

// ========== PIR Configuration ==========
#if ENABLE_PIR_SUPPORT
static const int PIR_SENSOR_COUNT = 3;
static const int PIR_PINS[PIR_SENSOR_COUNT] = {
  PIN_PIR_SENSOR_0,
  PIN_PIR_SENSOR_1,
  PIN_PIR_SENSOR_2
};

// Debounce: minimum milliseconds between event reports for same sensor
static const uint32_t PIR_DEBOUNCE_MS = 200;

// PIR state tracking
static bool pir_enabled = false;               // Master PIR enable flag
static uint32_t pir_last_event_ms[PIR_SENSOR_COUNT] = {0, 0, 0};
static bool pir_last_state[PIR_SENSOR_COUNT] = {false, false, false};
#endif

// ========== State ==========
static bool safety_is_safe = true;     // S1 default
static bool mode_projectile = false;   // M0 default

static int fire_token = 0;
static int led_token = 0;
static int laser_token = 0;
static int acc_token = 0;
static int spare_token = 0;

static bool projectile_pulse_active = false;
static uint32_t projectile_pulse_start_ms = 0;

static bool mosfet_cycle_active = false;
static bool mosfet_cycle_on_phase = false;
static uint32_t mosfet_cycle_phase_start_ms = 0;
static int mosfet_cycle_pulses_remaining = 0;
static int last_fire_cmd = 0;

static String line_buf;

static uint32_t last_telemetry_ms = 0;

// ========== Command Blink Indicator ==========
static bool blink_active = false;
static bool blink_led_on = false;
static uint8_t blink_toggles_remaining = 0;
static uint32_t blink_next_ms = 0;
static const uint16_t BLINK_ON_MS = 60;
static const uint16_t BLINK_OFF_MS = 60;

static void startStatusBlink(uint8_t pulse_count) {
  uint8_t toggles = (uint8_t)(pulse_count * 2);
  if (toggles == 0) return;
  if (blink_toggles_remaining < toggles) {
    blink_toggles_remaining = toggles;
  }
  blink_active = true;
  blink_led_on = true;
  digitalWrite(PIN_STATUS_LED, HIGH);
  blink_next_ms = millis() + BLINK_ON_MS;
}

static void updateStatusBlink() {
  if (!blink_active) return;
  uint32_t now = millis();
  if ((int32_t)(now - blink_next_ms) < 0) return;

  blink_led_on = !blink_led_on;
  digitalWrite(PIN_STATUS_LED, blink_led_on ? HIGH : LOW);
  if (blink_toggles_remaining > 0) {
    blink_toggles_remaining--;
  }

  if (blink_toggles_remaining == 0) {
    blink_active = false;
    blink_led_on = false;
    digitalWrite(PIN_STATUS_LED, LOW);
    return;
  }

  blink_next_ms = now + (blink_led_on ? BLINK_ON_MS : BLINK_OFF_MS);
}

// ========== Utility Functions ==========
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

static void writeTriggerMosfet(bool logical_on) {
  bool pin_high = trigger_output_active_low ? !logical_on : logical_on;
  digitalWrite(PIN_TRIGGER_MOSFET, pin_high ? HIGH : LOW);
}

static void triggerServoSet(bool on) {
  ledcWrite(PIN_TRIGGER_SERVO, degToDutyTicks(on ? trigger_servo_fire_deg : trigger_servo_rest_deg));
}

static uint32_t projectilePulseMsFromRuntime() {
  const int delta_deg = abs(trigger_servo_fire_deg - trigger_servo_rest_deg);
  const int speed = clampInt(trigger_servo_speed_dps, 10, 5000);
  uint32_t travel_ms = (uint32_t)((1000UL * (uint32_t)delta_deg) / (uint32_t)speed);
  uint32_t hold_ms = 40;
  uint32_t total = travel_ms + hold_ms;
  if (total < 20) total = 20;
  if (total > 2000) total = 2000;
  return total;
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

// ========== Output Control ==========
static void applyOutputs() {
  digitalWrite(PIN_LED_RELAY, led_token ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY, laser_token ? HIGH : LOW);
  digitalWrite(PIN_ACC_RELAY, acc_token ? HIGH : LOW);
  digitalWrite(PIN_SPARE_RELAY, spare_token ? HIGH : LOW);

  if (safety_is_safe) {
    writeTriggerMosfet(false);
    triggerServoSet(false);
    fire_token = 0;
    projectile_pulse_active = false;
    mosfet_cycle_active = false;
    mosfet_cycle_on_phase = false;
    mosfet_cycle_pulses_remaining = 0;
    last_fire_cmd = 0;
    return;
  }

  if (!mode_projectile) {
    // Water mode: fire token triggers configurable MOSFET pulse cycle.
    const uint32_t now = millis();
    if (fire_token && !last_fire_cmd && !mosfet_cycle_active) {
      mosfet_cycle_active = true;
      mosfet_cycle_on_phase = true;
      mosfet_cycle_phase_start_ms = now;
      mosfet_cycle_pulses_remaining = clampInt(trigger_mosfet_cycle_count, 1, 20);
      writeTriggerMosfet(true);
    }

    if (mosfet_cycle_active) {
      if (mosfet_cycle_on_phase) {
        if ((now - mosfet_cycle_phase_start_ms) >= trigger_mosfet_pulse_ms) {
          mosfet_cycle_on_phase = false;
          mosfet_cycle_phase_start_ms = now;
          mosfet_cycle_pulses_remaining--;
          writeTriggerMosfet(false);
          if (mosfet_cycle_pulses_remaining <= 0) {
            mosfet_cycle_active = false;
            fire_token = 0;
          }
        }
      } else {
        if ((now - mosfet_cycle_phase_start_ms) >= trigger_mosfet_cycle_off_ms) {
          if (mosfet_cycle_pulses_remaining > 0) {
            mosfet_cycle_on_phase = true;
            mosfet_cycle_phase_start_ms = now;
            writeTriggerMosfet(true);
          } else {
            mosfet_cycle_active = false;
            fire_token = 0;
            writeTriggerMosfet(false);
          }
        }
      }
    } else {
      writeTriggerMosfet(false);
      if (!fire_token) {
        last_fire_cmd = 0;
      }
    }

    last_fire_cmd = fire_token ? 1 : 0;
    triggerServoSet(false);
    projectile_pulse_active = false;
  } else {
    // Projectile mode: pulse servo on rising fire edge, auto-return after pulse window
    writeTriggerMosfet(false);
    mosfet_cycle_active = false;
    mosfet_cycle_on_phase = false;
    mosfet_cycle_pulses_remaining = 0;

    if (fire_token && !projectile_pulse_active) {
      projectile_pulse_active = true;
      projectile_pulse_start_ms = millis();
      triggerServoSet(true);
    }

    if (projectile_pulse_active) {
      if ((millis() - projectile_pulse_start_ms) >= projectilePulseMsFromRuntime()) {
        triggerServoSet(false);
        projectile_pulse_active = false;
        fire_token = 0;
      }
    } else {
      triggerServoSet(false);
    }
  }
}

// ========== PIR Monitoring ==========
#if ENABLE_PIR_SUPPORT
static void updatePIRSensors() {
  if (!pir_enabled) return;

  uint32_t now = millis();

  for (int i = 0; i < PIR_SENSOR_COUNT; i++) {
    bool current_state = digitalRead(PIR_PINS[i]) == HIGH;

    // Detect rising edge (motion detected) with debounce
    if (current_state && !pir_last_state[i]) {
      if ((now - pir_last_event_ms[i]) >= PIR_DEBOUNCE_MS) {
        pir_last_event_ms[i] = now;
        reportPIREvent(i, now);
      }
    }

    pir_last_state[i] = current_state;
  }
}

static void reportPIREvent(int sensor_id, uint32_t timestamp) {
  if (pir_event_blink_enabled) {
    startStatusBlink(2);
  }
  Serial.print("PIR_EVENT sensor_id=");
  Serial.print(sensor_id);
  Serial.print(" timestamp=");
  Serial.println(timestamp);
}
#endif

// ========== Command Parsing ==========
static void handleLine(String line) {
  line.trim();
  if (line.length() == 0) return;

  // Echo the command for debugging
  Serial.print("RECV: ");
  Serial.println(line);

  // Uppercase for tolerant parsing
  line.toUpperCase();

  const int prev_fire = fire_token;
  const int prev_led = led_token;
  const int prev_laser = laser_token;
  const int prev_acc = acc_token;
  const int prev_spare = spare_token;
  const bool prev_safety = safety_is_safe;
  const bool prev_mode = mode_projectile;

  // Parse both packed and single-token variants.
  fire_token  = parseTokenInt(line, 'F', fire_token) ? 1 : 0;
  led_token   = parseTokenInt(line, 'L', led_token) ? 1 : 0;
  laser_token = parseTokenInt(line, 'R', laser_token) ? 1 : 0;
  acc_token   = parseTokenInt(line, 'G', acc_token) ? 1 : 0;
  spare_token = parseTokenInt(line, 'A', spare_token) ? 1 : 0;

  int s = parseTokenInt(line, 'S', safety_is_safe ? 1 : 0);
  int m = parseTokenInt(line, 'M', mode_projectile ? 1 : 0);
  safety_is_safe = (s != 0);
  mode_projectile = (m != 0);

    int x = parseTokenInt(line, 'X', trigger_output_active_low ? 1 : 0);
    trigger_output_active_low = (x != 0);

    trigger_mosfet_pulse_ms = (uint32_t)clampInt(
      parseTokenInt(line, 'J', (int)trigger_mosfet_pulse_ms), 10, 2000);
    trigger_mosfet_cycle_count = clampInt(
      parseTokenInt(line, 'K', trigger_mosfet_cycle_count), 1, 20);
    trigger_mosfet_cycle_off_ms = (uint32_t)clampInt(
      parseTokenInt(line, 'N', (int)trigger_mosfet_cycle_off_ms), 10, 2000);

    int u = clampInt(parseTokenInt(line, 'U', trigger_servo_rest_deg), 0, 180);
    int v = clampInt(parseTokenInt(line, 'V', trigger_servo_fire_deg), 0, 180);
    if (v <= u) {
    v = clampInt(u + 1, 0, 180);
    }
    trigger_servo_rest_deg = u;
    trigger_servo_fire_deg = v;
    trigger_servo_speed_dps = clampInt(
      parseTokenInt(line, 'H', trigger_servo_speed_dps), 10, 5000);

    int b = parseTokenInt(line, 'B', pir_event_blink_enabled ? 1 : 0);
    pir_event_blink_enabled = (b != 0);

  bool accessory_changed =
      (prev_led != led_token) ||
      (prev_laser != laser_token) ||
      (prev_acc != acc_token) ||
      (prev_spare != spare_token) ||
      (prev_safety != safety_is_safe) ||
      (prev_mode != mode_projectile);
  bool fire_changed = (prev_fire != fire_token);

  // Blink LED on ANY command receipt (not just changes)
  startStatusBlink(1);

  if (fire_token && safety_is_safe) {
    Serial.println("WARN FIRE_BLOCKED_SAFETY S=1 (send S0 to arm)");
  }

#if ENABLE_PIR_SUPPORT
  int p = parseTokenInt(line, 'P', pir_enabled ? 1 : 0);
  pir_enabled = (p != 0);
#endif

  applyOutputs();

  // Echo back full state
  Serial.print("ACK ");
  Serial.print("S="); Serial.print(safety_is_safe ? 1 : 0);
  Serial.print(" M="); Serial.print(mode_projectile ? 1 : 0);
  Serial.print(" F="); Serial.print(fire_token);
  Serial.print(" L="); Serial.print(led_token);
  Serial.print(" R="); Serial.print(laser_token);
  Serial.print(" G="); Serial.print(acc_token);
  Serial.print(" A="); Serial.print(spare_token);
  Serial.print(" X="); Serial.print(trigger_output_active_low ? 1 : 0);
  Serial.print(" J="); Serial.print((int)trigger_mosfet_pulse_ms);
  Serial.print(" K="); Serial.print(trigger_mosfet_cycle_count);
  Serial.print(" N="); Serial.print((int)trigger_mosfet_cycle_off_ms);
  Serial.print(" U="); Serial.print(trigger_servo_rest_deg);
  Serial.print(" V="); Serial.print(trigger_servo_fire_deg);
  Serial.print(" H="); Serial.print(trigger_servo_speed_dps);
  Serial.print(" B="); Serial.print(pir_event_blink_enabled ? 1 : 0);

#if ENABLE_PIR_SUPPORT
  Serial.print(" P="); Serial.print(pir_enabled ? 1 : 0);
#endif

  Serial.println();
}

// ========== Setup ==========
void setup() {
  Serial.begin(HOST_BAUD);
  delay(50);

  // Output relays
  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  pinMode(PIN_LED_RELAY, OUTPUT);
  pinMode(PIN_LASER_RELAY, OUTPUT);
  pinMode(PIN_ACC_RELAY, OUTPUT);
  pinMode(PIN_SPARE_RELAY, OUTPUT);
  pinMode(PIN_STATUS_LED, OUTPUT);

  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  digitalWrite(PIN_LED_RELAY, LOW);
  digitalWrite(PIN_LASER_RELAY, LOW);
  digitalWrite(PIN_ACC_RELAY, LOW);
  digitalWrite(PIN_SPARE_RELAY, LOW);
  digitalWrite(PIN_STATUS_LED, LOW);

  // Trigger servo PWM
  bool ledc_ok = ledcAttach(PIN_TRIGGER_SERVO, SERVO_HZ, SERVO_RES_BITS);
  if (!ledc_ok) {
    Serial.println("[BOOT] LEDC attach failed for trigger servo");
  }
  triggerServoSet(false);

#if ENABLE_PIR_SUPPORT
  // PIR sensors (input, active HIGH)
  for (int i = 0; i < PIR_SENSOR_COUNT; i++) {
    pinMode(PIR_PINS[i], INPUT);  // Using internal pull-down (ESP32 default)
    pir_last_state[i] = false;
    pir_last_event_ms[i] = 0;
  }
  Serial.println("[BOOT] PIR support enabled. Sensors: GPIO35, GPIO34, GPIO39");
#else
  Serial.println("[BOOT] PIR support disabled (ENABLE_PIR_SUPPORT=0)");
#endif

  Serial.println("[BOOT] DB3000_ESP32_IO_Telemetry_2026_w_PIR ready");
  Serial.println("[BOOT] Expected host tokens: S/M/F/L/R/G/A/X/J/K/N/U/V/H/B over USB serial");
#if ENABLE_PIR_SUPPORT
  Serial.println("[BOOT] Additional token: P (PIR enable/disable)");
#endif
}

// ========== Main Loop ==========
void loop() {
  // Process incoming serial commands
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

  // Blink confirmation LED when fire/accessory/safety/mode changes are received.
  updateStatusBlink();

#if ENABLE_PIR_SUPPORT
  // Monitor PIR sensors and report events
  updatePIRSensors();
#endif

  // Lightweight telemetry line for host logs (periodic status update)
  uint32_t now = millis();
  if ((now - last_telemetry_ms) >= 1000) {
    last_telemetry_ms = now;
    Serial.print("STAT S="); Serial.print(safety_is_safe ? 1 : 0);
    Serial.print(" M="); Serial.print(mode_projectile ? 1 : 0);
    Serial.print(" F="); Serial.print(fire_token);
    Serial.print(" L="); Serial.print(led_token);
    Serial.print(" R="); Serial.print(laser_token);
    Serial.print(" G="); Serial.print(acc_token);
    Serial.print(" A="); Serial.print(spare_token);
    Serial.print(" X="); Serial.print(trigger_output_active_low ? 1 : 0);
    Serial.print(" J="); Serial.print((int)trigger_mosfet_pulse_ms);
    Serial.print(" K="); Serial.print(trigger_mosfet_cycle_count);
    Serial.print(" N="); Serial.print((int)trigger_mosfet_cycle_off_ms);
    Serial.print(" U="); Serial.print(trigger_servo_rest_deg);
    Serial.print(" V="); Serial.print(trigger_servo_fire_deg);
    Serial.print(" H="); Serial.print(trigger_servo_speed_dps);
    Serial.print(" B="); Serial.print(pir_event_blink_enabled ? 1 : 0);

#if ENABLE_PIR_SUPPORT
    Serial.print(" P="); Serial.print(pir_enabled ? 1 : 0);
#endif

    Serial.println();
  }
}
