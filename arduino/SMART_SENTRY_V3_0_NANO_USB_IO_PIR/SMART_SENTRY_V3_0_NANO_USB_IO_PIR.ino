// SMART_SENTRY_V3_0_NANO_USB_IO_PIR
// ---------------------------------
// Drop-in USB serial IO board replacement for the ESP32 dual-USB path.
//
// Runtime topology:
//   - PC <-> Arduino Nano over USB serial for IO, trigger, PIR, and buzzer.
//   - PC <-> Servo debug board over USB serial for Yahboom pan/tilt bus motion.
//
// Host command compatibility:
//   - Packed or single-token lines: F/L/R/G/A/S/M/J/K/N/U/V/H/B/P
//   - Sound cue lines: SOUND:<freq_hz>:<duration_ms>[:<volume_pct>]
//
// Important contract notes:
//   - No desktop app transport changes are required.
//   - Select the Nano COM port as the ESP32/IO COM port in Smart Sentry.
//   - LED PWM maps 0=off, 1=full-on compatibility, 2-255=literal duty cycle.
//   - The classic Nano has no internal pulldown input mode. PIR inputs therefore
//     expect modules that idle LOW or external pulldown resistors.

#include <Arduino.h>
#include <Servo.h>

#define ENABLE_PIR_SUPPORT 1
#define ACCESSORY_PWM_ENABLED 1

static const uint32_t HOST_BAUD = 115200;

// Pin map chosen to avoid timer conflicts on the ATmega328P:
//   - Servo library uses Timer1
//   - Custom buzzer wave generation uses Timer2
//   - LED PWM uses Timer0 on D5
static const uint8_t PIN_BUZZER = 4;
static const uint8_t PIN_LED_PWM = 5;
static const uint8_t PIN_LASER = 6;
static const uint8_t PIN_ACC_RELAY = 7;
static const uint8_t PIN_TRIGGER_MOSFET = 8;
static const uint8_t PIN_TRIGGER_SERVO = 9;
static const uint8_t PIN_SPARE_RELAY = A3;
static const uint8_t PIN_STATUS_LED = LED_BUILTIN;

static const uint8_t PIN_PIR_SENSOR_0 = A0;
static const uint8_t PIN_PIR_SENSOR_1 = A1;
static const uint8_t PIN_PIR_SENSOR_2 = A2;

static const int SERVO_REST_DEG_DEFAULT = 0;
static const int SERVO_FIRE_DEG_DEFAULT = 45;
static const int SERVO_SPEED_DPS_DEFAULT = 360;
static const uint32_t TRIGGER_PULSE_MS = 120;         // minimum projectile hold floor; final hold tracks servo travel/speed
static const uint32_t MOSFET_PULSE_MS_DEFAULT = 120;
static const uint8_t MOSFET_CYCLE_COUNT_DEFAULT = 1;
static const uint32_t MOSFET_CYCLE_OFF_MS_DEFAULT = 50;

#if ENABLE_PIR_SUPPORT
static const uint8_t PIR_SENSOR_COUNT = 3;
static const uint8_t PIR_PINS[PIR_SENSOR_COUNT] = {
  PIN_PIR_SENSOR_0,
  PIN_PIR_SENSOR_1,
  PIN_PIR_SENSOR_2,
};
static const uint32_t PIR_DEBOUNCE_MS = 200;
static bool pir_enabled = false;
static bool pir_last_state[PIR_SENSOR_COUNT] = {false, false, false};
static uint32_t pir_last_event_ms[PIR_SENSOR_COUNT] = {0, 0, 0};
#endif

static bool safety_is_safe = true;
static bool mode_projectile = false;
static bool pir_event_blink_enabled = false;

static int fire_token = 0;
static int led_value = 0;
static int laser_token = 0;
static int acc_token = 0;
static int spare_token = 0;

static int trigger_servo_rest_deg = SERVO_REST_DEG_DEFAULT;
static int trigger_servo_fire_deg = SERVO_FIRE_DEG_DEFAULT;
static int trigger_servo_speed_dps = SERVO_SPEED_DPS_DEFAULT;
static int trigger_mosfet_pulse_ms = (int)MOSFET_PULSE_MS_DEFAULT;
static int trigger_mosfet_cycle_count = (int)MOSFET_CYCLE_COUNT_DEFAULT;
static int trigger_mosfet_cycle_off_ms = (int)MOSFET_CYCLE_OFF_MS_DEFAULT;
static float trigger_servo_current_deg = (float)SERVO_REST_DEG_DEFAULT;
static float trigger_servo_target_deg = (float)SERVO_REST_DEG_DEFAULT;
static uint32_t trigger_servo_last_step_ms = 0;

static bool projectile_pulse_active = false;
static uint32_t projectile_pulse_start_ms = 0;
static bool mosfet_sequence_active = false;
static bool mosfet_sequence_output_high = false;
static bool mosfet_fire_request_latched = false;
static int mosfet_cycles_remaining = 0;
static uint32_t mosfet_phase_start_ms = 0;

static bool sound_active = false;
static uint32_t sound_end_ms = 0;
static int sound_freq_hz = 0;
static int sound_volume_pct = 0;

static volatile bool sound_wave_active = false;
static volatile bool sound_wave_high_phase = false;
static volatile uint8_t sound_wave_high_ocr = 0;
static volatile uint8_t sound_wave_low_ocr = 0;
static volatile uint8_t sound_wave_cs_bits = 0;

struct Timer2PrescalerConfig {
  uint16_t divisor;
  uint8_t cs_bits;
};

static const Timer2PrescalerConfig TIMER2_PRESCALERS[] = {
  {1, _BV(CS20)},
  {8, _BV(CS21)},
  {32, (uint8_t)(_BV(CS21) | _BV(CS20))},
  {64, _BV(CS22)},
  {128, (uint8_t)(_BV(CS22) | _BV(CS20))},
  {256, (uint8_t)(_BV(CS22) | _BV(CS21))},
  {1024, (uint8_t)(_BV(CS22) | _BV(CS21) | _BV(CS20))},
};

static bool blink_active = false;
static bool blink_led_on = false;
static uint8_t blink_toggles_remaining = 0;
static uint32_t blink_next_ms = 0;
static const uint16_t BLINK_ON_MS = 60;
static const uint16_t BLINK_OFF_MS = 60;

static char line_buf[160];
static uint8_t line_len = 0;
static uint32_t last_telemetry_ms = 0;

static Servo triggerServo;

static int clampInt(int value, int low, int high) {
  if (value < low) return low;
  if (value > high) return high;
  return value;
}

static int clampServoAngle(int value) {
  return clampInt(value, 0, 180);
}

static bool startsWithIgnoreCase(const char *text, const char *prefix) {
  if (text == nullptr || prefix == nullptr) return false;
  while (*prefix != '\0') {
    if (*text == '\0') return false;
    char lhs = (char)toupper((unsigned char)*text);
    char rhs = (char)toupper((unsigned char)*prefix);
    if (lhs != rhs) return false;
    ++text;
    ++prefix;
  }
  return true;
}

static int parseTokenInt(const char *text, char token, int fallback) {
  if (text == nullptr) return fallback;
  char wanted = (char)toupper((unsigned char)token);
  for (size_t index = 0; text[index] != '\0'; ++index) {
    char current = (char)toupper((unsigned char)text[index]);
    if (current != wanted) continue;

    size_t cursor = index + 1;
    bool negative = false;
    if (text[cursor] == '-') {
      negative = true;
      ++cursor;
    }

    long value = 0;
    bool has_digit = false;
    while (text[cursor] >= '0' && text[cursor] <= '9') {
      has_digit = true;
      value = (value * 10L) + (long)(text[cursor] - '0');
      ++cursor;
    }
    if (!has_digit) return fallback;
    if (negative) value = -value;
    return (int)value;
  }
  return fallback;
}

static bool parseSoundCommand(const char *line, int *freq_hz, int *duration_ms, int *volume_pct) {
  if (!startsWithIgnoreCase(line, "SOUND:")) return false;
  const char *cursor = line + 6;
  char *end_ptr = nullptr;
  long freq = strtol(cursor, &end_ptr, 10);
  if (end_ptr == cursor || *end_ptr != ':') return false;

  cursor = end_ptr + 1;
  long duration = strtol(cursor, &end_ptr, 10);
  if (end_ptr == cursor) return false;

  long volume = 100;
  if (*end_ptr == ':') {
    cursor = end_ptr + 1;
    volume = strtol(cursor, &end_ptr, 10);
    if (end_ptr == cursor) return false;
  }

  while (*end_ptr == ' ' || *end_ptr == '\t') {
    ++end_ptr;
  }
  if (*end_ptr != '\0') return false;

  if (freq_hz != nullptr) *freq_hz = (int)freq;
  if (duration_ms != nullptr) *duration_ms = (int)duration;
  if (volume_pct != nullptr) *volume_pct = (int)volume;
  return true;
}

static void startStatusBlink(uint8_t pulse_count) {
  uint8_t toggles = (uint8_t)(pulse_count * 2U);
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
    --blink_toggles_remaining;
  }

  if (blink_toggles_remaining == 0) {
    blink_active = false;
    blink_led_on = false;
    digitalWrite(PIN_STATUS_LED, LOW);
    return;
  }

  blink_next_ms = now + (blink_led_on ? BLINK_ON_MS : BLINK_OFF_MS);
}

static void buzzerOutputHigh() {
  PORTD |= _BV(PD4);
}

static void buzzerOutputLow() {
  PORTD &= (uint8_t)~_BV(PD4);
}

static bool selectSoundTimerPrescaler(uint32_t max_interval_us, uint16_t *divisor, uint8_t *cs_bits) {
  const uint32_t cpu_mhz = (uint32_t)(F_CPU / 1000000UL);
  for (size_t index = 0; index < (sizeof(TIMER2_PRESCALERS) / sizeof(TIMER2_PRESCALERS[0])); ++index) {
    const Timer2PrescalerConfig cfg = TIMER2_PRESCALERS[index];
    uint32_t ticks = ((max_interval_us * cpu_mhz) + (cfg.divisor / 2U)) / cfg.divisor;
    if (ticks == 0U) ticks = 1U;
    if (ticks <= 256U) {
      if (divisor != nullptr) *divisor = cfg.divisor;
      if (cs_bits != nullptr) *cs_bits = cfg.cs_bits;
      return true;
    }
  }
  return false;
}

static uint8_t timer2IntervalToOcr(uint32_t interval_us, uint16_t divisor) {
  const uint32_t cpu_mhz = (uint32_t)(F_CPU / 1000000UL);
  uint32_t ticks = ((interval_us * cpu_mhz) + (divisor / 2U)) / divisor;
  if (ticks == 0U) ticks = 1U;
  if (ticks > 256U) ticks = 256U;
  return (uint8_t)(ticks - 1U);
}

ISR(TIMER2_COMPA_vect) {
  if (!sound_wave_active) {
    buzzerOutputLow();
    return;
  }

  if (sound_wave_high_phase) {
    buzzerOutputLow();
    OCR2A = sound_wave_low_ocr;
    sound_wave_high_phase = false;
    return;
  }

  buzzerOutputHigh();
  OCR2A = sound_wave_high_ocr;
  sound_wave_high_phase = true;
}

static void stopSoundTone() {
  noInterrupts();
  sound_wave_active = false;
  sound_wave_high_phase = false;
  TIMSK2 &= (uint8_t)~_BV(OCIE2A);
  TCCR2A = 0;
  TCCR2B = 0;
  TCNT2 = 0;
  OCR2A = 0;
  interrupts();

  buzzerOutputLow();
  sound_active = false;
  sound_end_ms = 0;
  sound_freq_hz = 0;
  sound_volume_pct = 0;
}

static void startSoundTone(int freq_hz, int duration_ms, int volume_pct) {
  int freq = clampInt(freq_hz, 120, 6000);
  int duration = clampInt(duration_ms, 10, 2000);
  int volume = clampInt(volume_pct, 0, 100);
  if (volume <= 0) {
    stopSoundTone();
    return;
  }

  uint32_t period_us = max(1UL, 1000000UL / (uint32_t)freq);
  uint32_t duty_pct = (uint32_t)volume;
  if (duty_pct >= 100U) duty_pct = 99U;
  if (duty_pct == 0U) duty_pct = 1U;

  uint32_t high_us = ((period_us * duty_pct) + 50U) / 100U;
  if (high_us == 0U) high_us = 1U;
  if (high_us >= period_us) high_us = period_us - 1U;
  uint32_t low_us = period_us - high_us;
  if (low_us == 0U) low_us = 1U;

  uint16_t divisor = 0;
  uint8_t cs_bits = 0;
  if (!selectSoundTimerPrescaler((high_us > low_us) ? high_us : low_us, &divisor, &cs_bits)) {
    stopSoundTone();
    return;
  }

  uint8_t high_ocr = timer2IntervalToOcr(high_us, divisor);
  uint8_t low_ocr = timer2IntervalToOcr(low_us, divisor);

  stopSoundTone();
  noInterrupts();
  TCCR2A = _BV(WGM21);
  TCCR2B = 0;
  TCNT2 = 0;
  sound_wave_high_ocr = high_ocr;
  sound_wave_low_ocr = low_ocr;
  sound_wave_cs_bits = cs_bits;
  sound_wave_high_phase = true;
  sound_wave_active = true;
  OCR2A = sound_wave_high_ocr;
  TIFR2 = _BV(OCF2A);
  TIMSK2 |= _BV(OCIE2A);
  buzzerOutputHigh();
  TCCR2B = sound_wave_cs_bits;
  interrupts();

  sound_active = true;
  sound_freq_hz = freq;
  sound_volume_pct = volume;
  sound_end_ms = millis() + (uint32_t)duration;
}

static void updateSoundTone(uint32_t now_ms) {
  if (!sound_active) return;
  if ((int32_t)(now_ms - sound_end_ms) < 0) return;
  stopSoundTone();
}

static void triggerServoWriteDeg(int deg) {
  triggerServo.write(clampServoAngle(deg));
}

static void setTriggerServoTarget(bool fire_state) {
  trigger_servo_target_deg = (float)(fire_state ? clampServoAngle(trigger_servo_fire_deg)
                                                : clampServoAngle(trigger_servo_rest_deg));
}

static uint32_t computeProjectileHoldMs() {
  int travel_deg = trigger_servo_fire_deg - trigger_servo_rest_deg;
  if (travel_deg < 0) {
    travel_deg = -travel_deg;
  }

  float speed_dps = (float)max(10, trigger_servo_speed_dps);
  uint32_t travel_ms = (uint32_t)((((float)travel_deg) * 1000.0f) / speed_dps + 0.5f);
  uint32_t hold_ms = travel_ms + 35U;
  if (hold_ms < (uint32_t)TRIGGER_PULSE_MS) {
    hold_ms = (uint32_t)TRIGGER_PULSE_MS;
  }
  if (hold_ms > 2000U) {
    hold_ms = 2000U;
  }
  return hold_ms;
}

static void updateTriggerServoMotion() {
  uint32_t now = millis();
  if (trigger_servo_last_step_ms == 0) {
    trigger_servo_last_step_ms = now;
    triggerServoWriteDeg((int)(trigger_servo_current_deg + 0.5f));
    return;
  }

  uint32_t elapsed_ms = now - trigger_servo_last_step_ms;
  if (elapsed_ms == 0) return;
  trigger_servo_last_step_ms = now;

  float speed_dps = (float)max(10, trigger_servo_speed_dps);
  float max_step = speed_dps * ((float)elapsed_ms / 1000.0f);
  float delta = trigger_servo_target_deg - trigger_servo_current_deg;
  float abs_delta = (delta < 0.0f) ? -delta : delta;
  if (abs_delta <= max_step) {
    trigger_servo_current_deg = trigger_servo_target_deg;
  } else {
    trigger_servo_current_deg += (delta > 0.0f) ? max_step : -max_step;
  }
  triggerServoWriteDeg((int)(trigger_servo_current_deg + 0.5f));
}

static void stopMosfetSequence() {
  mosfet_sequence_active = false;
  mosfet_sequence_output_high = false;
  mosfet_cycles_remaining = 0;
  mosfet_phase_start_ms = 0;
  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
}

static void startMosfetSequence() {
  mosfet_sequence_active = true;
  mosfet_sequence_output_high = true;
  mosfet_cycles_remaining = max(1, trigger_mosfet_cycle_count);
  mosfet_phase_start_ms = millis();
  digitalWrite(PIN_TRIGGER_MOSFET, HIGH);
}

static void updateMosfetSequence(uint32_t now_ms) {
  if (!mosfet_sequence_active) {
    digitalWrite(PIN_TRIGGER_MOSFET, LOW);
    return;
  }

  if (mosfet_sequence_output_high) {
    if ((now_ms - mosfet_phase_start_ms) < (uint32_t)max(10, trigger_mosfet_pulse_ms)) {
      return;
    }
    --mosfet_cycles_remaining;
    if (mosfet_cycles_remaining <= 0) {
      stopMosfetSequence();
      fire_token = 0;
      return;
    }
    mosfet_sequence_output_high = false;
    mosfet_phase_start_ms = now_ms;
    digitalWrite(PIN_TRIGGER_MOSFET, LOW);
    return;
  }

  if ((now_ms - mosfet_phase_start_ms) < (uint32_t)max(10, trigger_mosfet_cycle_off_ms)) {
    return;
  }
  mosfet_sequence_output_high = true;
  mosfet_phase_start_ms = now_ms;
  digitalWrite(PIN_TRIGGER_MOSFET, HIGH);
}

static void writeLedOutput(int led_pwm_value) {
#if ACCESSORY_PWM_ENABLED
  int duty = (led_pwm_value <= 0) ? 0 : (led_pwm_value == 1) ? 255 : clampInt(led_pwm_value, 0, 255);
  analogWrite(PIN_LED_PWM, duty);
#else
  digitalWrite(PIN_LED_PWM, led_pwm_value > 0 ? HIGH : LOW);
#endif
}

#if ENABLE_PIR_SUPPORT
static void reportPIREvent(int sensor_id, uint32_t timestamp_ms) {
  if (pir_event_blink_enabled) startStatusBlink(6);
  Serial.print(F("PIR_EVENT sensor_id="));
  Serial.print(sensor_id);
  Serial.print(F(" timestamp="));
  Serial.println(timestamp_ms);
}

static void updatePIRSensors() {
  if (!pir_enabled) return;

  uint32_t now = millis();
  for (uint8_t index = 0; index < PIR_SENSOR_COUNT; ++index) {
    bool current_state = digitalRead(PIR_PINS[index]) == HIGH;
    if (current_state && !pir_last_state[index]) {
      if ((now - pir_last_event_ms[index]) >= PIR_DEBOUNCE_MS) {
        pir_last_event_ms[index] = now;
        reportPIREvent((int)index, now);
      }
    }
    pir_last_state[index] = current_state;
  }
}
#endif

static void applyOutputs() {
  writeLedOutput(led_value);
  digitalWrite(PIN_LASER, laser_token ? HIGH : LOW);
  digitalWrite(PIN_ACC_RELAY, acc_token ? HIGH : LOW);
  digitalWrite(PIN_SPARE_RELAY, spare_token ? HIGH : LOW);
  uint32_t now_ms = millis();

  if (safety_is_safe) {
    stopMosfetSequence();
    mosfet_fire_request_latched = false;
    setTriggerServoTarget(false);
    fire_token = 0;
    projectile_pulse_active = false;
    return;
  }

  if (!mode_projectile) {
    setTriggerServoTarget(false);
    projectile_pulse_active = false;
    if (fire_token == 0) {
      mosfet_fire_request_latched = false;
    }
    if (fire_token && !mosfet_fire_request_latched && !mosfet_sequence_active) {
      startMosfetSequence();
      mosfet_fire_request_latched = true;
    }
    updateMosfetSequence(now_ms);
    setTriggerServoTarget(false);
    return;
  }

  stopMosfetSequence();
  mosfet_fire_request_latched = false;
  if (fire_token && !projectile_pulse_active) {
    projectile_pulse_active = true;
    projectile_pulse_start_ms = now_ms;
    setTriggerServoTarget(true);
  }

  if (projectile_pulse_active) {
    // Match the desktop app contract: projectile dwell comes from visible
    // trigger-servo travel/speed settings, not the hidden water-mode pulse knob.
    uint32_t hold_ms = computeProjectileHoldMs();
    if ((now_ms - projectile_pulse_start_ms) >= hold_ms) {
      setTriggerServoTarget(false);
      projectile_pulse_active = false;
      fire_token = 0;
    }
  } else {
    setTriggerServoTarget(false);
  }
}

static void printStateLine(const __FlashStringHelper *prefix) {
  Serial.print(prefix);
  Serial.print(F(" S=")); Serial.print(safety_is_safe ? 1 : 0);
  Serial.print(F(" M=")); Serial.print(mode_projectile ? 1 : 0);
  Serial.print(F(" F=")); Serial.print(fire_token);
  Serial.print(F(" L=")); Serial.print(led_value);
  Serial.print(F(" R=")); Serial.print(laser_token);
  Serial.print(F(" G=")); Serial.print(acc_token);
  Serial.print(F(" A=")); Serial.print(spare_token);
  Serial.print(F(" J=")); Serial.print(trigger_mosfet_pulse_ms);
  Serial.print(F(" K=")); Serial.print(trigger_mosfet_cycle_count);
  Serial.print(F(" N=")); Serial.print(trigger_mosfet_cycle_off_ms);
  Serial.print(F(" U=")); Serial.print(trigger_servo_rest_deg);
  Serial.print(F(" V=")); Serial.print(trigger_servo_fire_deg);
  Serial.print(F(" H=")); Serial.print(trigger_servo_speed_dps);
  Serial.print(F(" B=")); Serial.print(pir_event_blink_enabled ? 1 : 0);
#if ENABLE_PIR_SUPPORT
  Serial.print(F(" P=")); Serial.print(pir_enabled ? 1 : 0);
#endif
  Serial.println();
}

static void handleLine(const char *line) {
  if (line == nullptr || line[0] == '\0') return;

  Serial.print(F("RECV: "));
  Serial.println(line);

  int sound_freq = 0;
  int sound_duration = 0;
  int sound_volume = 100;
  if (parseSoundCommand(line, &sound_freq, &sound_duration, &sound_volume)) {
    startStatusBlink(1);
    startSoundTone(sound_freq, sound_duration, sound_volume);
    Serial.print(F("ACK SOUND freq="));
    Serial.print(clampInt(sound_freq, 120, 6000));
    Serial.print(F(" duration="));
    Serial.print(clampInt(sound_duration, 10, 2000));
    Serial.print(F(" volume="));
    Serial.println(clampInt(sound_volume, 0, 100));
    return;
  }

  fire_token = parseTokenInt(line, 'F', fire_token) ? 1 : 0;
  led_value = clampInt(parseTokenInt(line, 'L', led_value), 0, 255);
  laser_token = parseTokenInt(line, 'R', laser_token) ? 1 : 0;
  acc_token = parseTokenInt(line, 'G', acc_token) ? 1 : 0;
  spare_token = parseTokenInt(line, 'A', spare_token) ? 1 : 0;

  int safety_value = parseTokenInt(line, 'S', safety_is_safe ? 1 : 0);
  int mode_value = parseTokenInt(line, 'M', mode_projectile ? 1 : 0);
  int mosfet_pulse_ms = parseTokenInt(line, 'J', trigger_mosfet_pulse_ms);
  int mosfet_cycle_count = parseTokenInt(line, 'K', trigger_mosfet_cycle_count);
  int mosfet_cycle_off_ms = parseTokenInt(line, 'N', trigger_mosfet_cycle_off_ms);
  int rest_deg = parseTokenInt(line, 'U', trigger_servo_rest_deg);
  int fire_deg = parseTokenInt(line, 'V', trigger_servo_fire_deg);
  int speed_dps = parseTokenInt(line, 'H', trigger_servo_speed_dps);
  int pir_blink = parseTokenInt(line, 'B', pir_event_blink_enabled ? 1 : 0);

  safety_is_safe = (safety_value != 0);
  mode_projectile = (mode_value != 0);
  trigger_mosfet_pulse_ms = clampInt(mosfet_pulse_ms, 10, 2000);
  trigger_mosfet_cycle_count = clampInt(mosfet_cycle_count, 1, 20);
  trigger_mosfet_cycle_off_ms = clampInt(mosfet_cycle_off_ms, 10, 2000);
  trigger_servo_rest_deg = clampServoAngle(rest_deg);
  trigger_servo_fire_deg = clampServoAngle(fire_deg);
  if (trigger_servo_fire_deg < trigger_servo_rest_deg) {
    trigger_servo_fire_deg = trigger_servo_rest_deg;
  }
  trigger_servo_speed_dps = max(10, speed_dps);
  pir_event_blink_enabled = (pir_blink != 0);

#if ENABLE_PIR_SUPPORT
  int pir_value = parseTokenInt(line, 'P', pir_enabled ? 1 : 0);
  pir_enabled = (pir_value != 0);
#endif

  startStatusBlink(1);

  if (fire_token && safety_is_safe) {
    Serial.println(F("WARN FIRE_BLOCKED_SAFETY S=1 (send S0 to arm)"));
  }

  applyOutputs();
  printStateLine(F("ACK"));
}

void setup() {
  Serial.begin(HOST_BAUD);
  delay(50);

  pinMode(PIN_BUZZER, OUTPUT);
  pinMode(PIN_LED_PWM, OUTPUT);
  pinMode(PIN_LASER, OUTPUT);
  pinMode(PIN_ACC_RELAY, OUTPUT);
  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  pinMode(PIN_SPARE_RELAY, OUTPUT);
  pinMode(PIN_STATUS_LED, OUTPUT);

  digitalWrite(PIN_BUZZER, LOW);
  digitalWrite(PIN_LASER, LOW);
  digitalWrite(PIN_ACC_RELAY, LOW);
  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  digitalWrite(PIN_SPARE_RELAY, LOW);
  digitalWrite(PIN_STATUS_LED, LOW);
  analogWrite(PIN_LED_PWM, 0);

  triggerServo.attach(PIN_TRIGGER_SERVO);
  trigger_servo_current_deg = (float)trigger_servo_rest_deg;
  trigger_servo_target_deg = (float)trigger_servo_rest_deg;
  trigger_servo_last_step_ms = millis();
  triggerServoWriteDeg(trigger_servo_rest_deg);

#if ENABLE_PIR_SUPPORT
  for (uint8_t index = 0; index < PIR_SENSOR_COUNT; ++index) {
    pinMode(PIR_PINS[index], INPUT);
    pir_last_state[index] = false;
    pir_last_event_ms[index] = 0;
  }
  Serial.println(F("[BOOT] PIR support enabled on A0/A1/A2"));
#else
  Serial.println(F("[BOOT] PIR support disabled (ENABLE_PIR_SUPPORT=0)"));
#endif

  Serial.println(F("[BOOT] SMART_SENTRY_V3_0_NANO_USB_IO_PIR ready"));
  Serial.println(F("[BOOT] Select this Nano COM port as the Smart Sentry IO/ESP32 port"));
  Serial.println(F("[BOOT] Host tokens: S/M/F/L/R/G/A/J/K/N/U/V/H/B/P plus SOUND:<freq>:<ms>[:<volume>]"));
}

void loop() {
  while (Serial.available() > 0) {
    char ch = (char)Serial.read();
    if (ch == '\r') continue;
    if (ch == '\n') {
      line_buf[line_len] = '\0';
      handleLine(line_buf);
      line_len = 0;
      line_buf[0] = '\0';
    } else if (line_len < (sizeof(line_buf) - 1U)) {
      line_buf[line_len++] = ch;
    }
  }

  applyOutputs();
  updateTriggerServoMotion();
  updateStatusBlink();

  uint32_t now = millis();
  updateSoundTone(now);

#if ENABLE_PIR_SUPPORT
  updatePIRSensors();
#endif

  if ((now - last_telemetry_ms) >= 1000UL) {
    last_telemetry_ms = now;
    printStateLine(F("STAT"));
  }
}