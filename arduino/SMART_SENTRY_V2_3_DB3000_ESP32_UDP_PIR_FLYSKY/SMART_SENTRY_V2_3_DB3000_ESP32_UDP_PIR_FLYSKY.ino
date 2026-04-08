// SMART_SENTRY_V2_3_DB3000_ESP32_UDP_PIR_FLYSKY — v2.3
// =============================================================
// Combined firmware: WiFi/UDP turret control + PIR blind-spot sensors
// + FlySky FS-iA6 i-Bus receiver telemetry and control-source selection
//
// Topology (Mode 2 in app):
//   PC  <->  ESP32  over WiFi/UDP (192.168.4.1:9000)
//   Debug Board  <->  ESP32  over UART2 (GPIO16 RX / GPIO17 TX)
//   ESP32 USB stays available for Serial diagnostics and flashing
//
// App compatibility:
//   - JSON+CRC32 UDP packet format (matches sentry_v2_comm.py)
//   - Command payload fields: pan_cmd, tilt_cmd, fire, safety,
//     led, laser, mode, move_time_ms, pir_enabled, rapid_fire
//   - Sound action payload: {"action":"sound","freq_hz":N,"duration_ms":M}
//   - Control-source payload: {"action":"rc_mode","mode":"app|rc"}
//   - Safety: 0=ARMED, 1=LOCKED
//   - Trigger mode: 0=water(MOSFET), 1=projectile(servo)
//   - PIR events sent back as {"v":1,"t":"pir_event","p":{"sensor_id":N,"timestamp_ms":T}}
//
// PIR pin note:
//   GPIO 34 and GPIO 39 are shared with current-sense ADC inputs.
//   When ENABLE_PIR_SUPPORT=1, current sensing on those two pins is
//   disabled and they are reconfigured as PIR inputs.
//   GPIO 35 (PIR 0) and GPIO 36 (current pan) have no conflict.
//
// Board target: ESP32 DevKit v1 (WROOM-32)
// FQBN: esp32:esp32:esp32
// Required library: ArduinoJson v6

// ─────────────────────────────────────────────────────────────
// Feature flags
// ─────────────────────────────────────────────────────────────
#define ENABLE_PIR_SUPPORT 1   // 1 = compile PIR code, 0 = full current sensing

// NOTE: Must be defined before Arduino auto-generates prototypes.
enum BusChecksumMode {
  BUS_CHK_SUB = 0,
  BUS_CHK_XOR = 1,
};

#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>
#include <esp_system.h>

// ─────────────────────────────────────────────────────────────
// WiFi / UDP
// ─────────────────────────────────────────────────────────────
static const char     *WIFI_SSID = "DB3000-ESP32";
static const char     *WIFI_PASS = "db3000pass";
static const IPAddress AP_IP(192, 168, 4, 1);
static const IPAddress AP_GW(192, 168, 4, 1);
static const IPAddress AP_MASK(255, 255, 255, 0);
static const uint16_t  UDP_PORT  = 9000;

WiFiUDP  Udp;
IPAddress last_remote_ip;
uint16_t  last_remote_port = 0;

// ─────────────────────────────────────────────────────────────
// Pin map (ESP32 DevKit v1)
// ─────────────────────────────────────────────────────────────
static const int PIN_UART_RX        = 16;   // UART2 RX — debug board TX
static const int PIN_UART_TX        = 17;   // UART2 TX — debug board RX
static const int PIN_TRIGGER_MOSFET = 27;   // Water-mode trigger relay
static const int PIN_TRIGGER_SERVO  = 13;   // Projectile trigger servo (PWM)
static const int PIN_PAN_SERVO      = 12;   // Pan servo (PWM) - Waveshare servo header
static const int PIN_TILT_SERVO     = 14;   // Tilt servo (PWM) - Waveshare servo header
static const int PIN_LED_RELAY      = 32;   // LED relay
static const int PIN_LASER_RELAY    = 33;   // Laser relay
static const int PIN_ACC_RELAY      = 25;   // Accessory relay
static const int PIN_SPARE_RELAY    = 26;   // Spare relay
static const int PIN_BUZZER         = 4;    // Passive buzzer / tone output
static const int BUZZER_PWM_RES_BITS = 10;
static const int PIN_SWEEP_BUTTON   = 0;    // DevKit BOOT button (active LOW)
static const int PIN_RC_UART_RX     = 21;   // FlySky FS-iA6 i-Bus RX
static const int PIN_RC_UART_TX     = -1;   // unused
static const int PIN_RC_MODE_SWITCH = 22;   // APP/RC physical source switch (active LOW => RC)
static const uint32_t RC_BAUD       = 115200;
static const bool RC_INPUT_ENABLED  = true;
static const uint32_t RC_FRAME_TIMEOUT_MS = 500;
static const uint8_t RC_IBUS_FRAME_LEN = 0x20;
static const uint8_t RC_IBUS_FRAME_CMD = 0x40;
static const uint16_t RC_PULSE_MIN_US = 1000;
static const uint16_t RC_PULSE_CENTER_US = 1500;
static const uint16_t RC_PULSE_MAX_US = 2000;
static const uint16_t RC_STICK_DEADBAND_US = 45;
static const uint16_t RC_SWITCH_ON_THRESHOLD_US = 1600;
static const uint16_t RC_SWITCH_OFF_THRESHOLD_US = 1400;
static const uint32_t RC_MOTION_APPLY_INTERVAL_MS = 60;
static const uint16_t RC_MOVE_TIME_MS = 80;

enum ControlSourceMode {
  CONTROL_SOURCE_APP = 0,
  CONTROL_SOURCE_RC = 1,
  CONTROL_SOURCE_AUTO = 2,
};

// ADC current sensing (input-only, GPIO 34-39)
static const int PIN_CURR_PAN   = 36;   // No PIR conflict

#if ENABLE_PIR_SUPPORT
// When PIR is enabled, GPIO 34 and 39 become PIR inputs.
// Current sensing on those two channels is skipped.
static const int PIN_CURR_TILT  = -1;   // Disabled (GPIO 39 used by PIR 2)
static const int PIN_CURR_TOTAL = -1;   // Disabled (GPIO 34 used by PIR 1)
#else
static const int PIN_CURR_TILT  = 39;
static const int PIN_CURR_TOTAL = 34;
#endif

// Status LED
// Use GPIO2 explicitly so an external LED can mirror command activity even when
// the onboard LED is hidden inside the turret base.
static const int PIN_STATUS_LED = 2;

// ─────────────────────────────────────────────────────────────
// PIR sensors (input-only GPIO, active HIGH)
// ─────────────────────────────────────────────────────────────
#if ENABLE_PIR_SUPPORT
static const int PIR_COUNT             = 3;
static const int PIR_PINS[PIR_COUNT]   = {35, 34, 39};
// Sensor positions (cue pan angles, equal 90° coverage zones):
//   Sensor 0  GPIO 35  — right zone  (cue ~45°)
//   Sensor 1  GPIO 34  — front zone  (cue ~135°)
//   Sensor 2  GPIO 39  — left zone   (cue ~225°)
static const uint32_t PIR_DEBOUNCE_MS  = 200;

static bool     pir_enabled                  = false;
static bool     pir_last_state[PIR_COUNT]    = {false, false, false};
static uint32_t pir_last_event_ms[PIR_COUNT] = {0, 0, 0};
#endif

// ─────────────────────────────────────────────────────────────
// Trigger servo PWM (LEDC)
// ─────────────────────────────────────────────────────────────
static const int      SERVO_HZ              = 50;
static const int      SERVO_RES_BITS        = 16;
static const int      SERVO_MIN_US          = 500;
static const int      SERVO_MAX_US          = 2500;
static const int      TRIGGER_SERVO_REST_DEG_DEFAULT  = 0;
static const int      TRIGGER_SERVO_FIRE_DEG_DEFAULT  = 45;
static const int      TRIGGER_SERVO_SPEED_DPS_DEFAULT = 360;
static const uint32_t TRIGGER_PULSE_MS                = 120;

// ─────────────────────────────────────────────────────────────
// Bus servo (debug board over UART2)
// ─────────────────────────────────────────────────────────────
static const uint32_t BUS_BAUD      = 1000000;
static const uint8_t  BUS_ID_PAN    = 1;
static const uint8_t  BUS_ID_TILT   = 2;
static const uint16_t PAN_TICKS_MIN  = 0;
static const uint16_t PAN_TICKS_MAX  = 4095;
static const uint16_t TILT_TICKS_MIN = 0;
static const uint16_t TILT_TICKS_MAX = 4095;
static const bool     INVERT_PAN    = false;
static const bool     INVERT_TILT   = false;
static const uint16_t MOVE_TIME_BIG_MS   = 10;
static const uint16_t MOVE_TIME_MED_MS   = 14;
static const uint16_t MOVE_TIME_SMALL_MS = 18;
static const uint16_t MOVE_TIME_TINY_MS  = 22;

HardwareSerial busSerial(2);
HardwareSerial rcSerial(1);
static uint32_t bus_baud_active = BUS_BAUD;

// ─────────────────────────────────────────────────────────────
// Config structs
// ─────────────────────────────────────────────────────────────
struct LimitsConfig {
  int pan_min  = 0;   int pan_max  = 220;
  int tilt_min = 0;   int tilt_max = 70;
};
struct HomeConfig {
  int   pan           = 90;
  int   tilt          = 40;
  float speed         = 10.0f;
  float max_speed_dps = 25.0f;
};
struct TriggerConfig {
  int   mode       = 0;    // 0=water, 1=projectile
  float cooldown_s = 1.5f;
  float max_fire_s = 3.0f;
  int   servo_rest_deg = TRIGGER_SERVO_REST_DEG_DEFAULT;
  int   servo_fire_deg = TRIGGER_SERVO_FIRE_DEG_DEFAULT;
  int   servo_speed_dps = TRIGGER_SERVO_SPEED_DPS_DEFAULT;
};
struct RapidFireConfig {
  bool  enabled  = false;
  int   rate_hz  = 1;
  float duty     = 0.5f;
};
struct CurrentProtectionConfig {
  bool enabled      = false;
  bool block_fire   = true;
  bool block_motion = true;
  bool latch        = false;
  int  trip_pan_mA     = 0;
  int  trip_tilt_mA    = 0;
  int  trip_total_mA   = 0;
  int  trip_hold_ms    = 250;
  int  clear_hold_ms   = 750;
  int  hysteresis_mA   = 250;
};
struct TiltSafetyConfig {
  bool installed = false;
  bool enabled   = false;
};

LimitsConfig            limits_cfg;
HomeConfig              home_cfg;
TriggerConfig           trigger_cfg;
RapidFireConfig         rapid_cfg;
CurrentProtectionConfig current_cfg;
TiltSafetyConfig        tilt_safety_cfg;

// ─────────────────────────────────────────────────────────────
// Runtime state
// ─────────────────────────────────────────────────────────────
static int  target_pan  = 90;
static int  target_tilt = 40;
static int  safety_state = 1;   // 1=locked, 0=armed  (matches app: S1=safe, S0=armed)
static int  led_state    = 0;
static int  laser_state  = 0;
static int  acc_state    = 0;
static int  spare_state  = 0;
static int  fire_request = 0;
static bool fire_hold    = false;

static uint32_t last_cmd_ms      = 0;
static uint32_t last_state_ms    = 0;
static uint32_t last_fire_start_ms = 0;
static bool     fire_active        = false;
static bool     rapid_fire_active  = false;
static bool     trigger_servo_pwm_ready = false;
static float    trigger_servo_current_deg = (float)TRIGGER_SERVO_REST_DEG_DEFAULT;
static float    trigger_servo_target_deg  = (float)TRIGGER_SERVO_REST_DEG_DEFAULT;
static uint32_t trigger_servo_last_step_ms = 0;
static bool     pir_event_blink_enabled = false;
static bool     buzzer_pwm_ready = false;
static bool     sound_active = false;
static uint32_t sound_end_ms = 0;
static int      sound_freq_hz = 0;
static int      sound_volume_pct = 100;

static uint32_t trip_start_ms  = 0;
static bool     current_fault  = false;
static int      latest_pan_mA  = 0;
static int      latest_tilt_mA = 0;
static int      latest_total_mA = 0;

static int      last_sent_pan  = -1;
static int      last_sent_tilt = -1;
static uint32_t last_bus_send_ms = 0;

static uint16_t move_time_override_ms       = 0;
static uint32_t move_time_override_until_ms = 0;

static const float PAN_MA_PER_ADC   = 1.0f;
static const float TILT_MA_PER_ADC  = 1.0f;
static const float TOTAL_MA_PER_ADC = 1.0f;

static uint32_t cmd_count        = 0;
static uint32_t crc_fail_count   = 0;
static uint32_t parse_fail_count = 0;
static uint32_t bus_send_count   = 0;
static bool     first_client_seen = false;
static ControlSourceMode control_source_mode = CONTROL_SOURCE_APP;
static bool     rc_link_active = false;
static bool     rc_override_active = false;
static bool     rc_failsafe_active = false;
static uint32_t rc_frame_age_ms = 0;
static uint16_t rc_channel_us[6] = {1500, 1500, 1000, 1000, 1000, 1000};
static uint32_t rc_last_frame_ms = 0;
static uint8_t  rc_frame_buffer[RC_IBUS_FRAME_LEN];
static uint8_t  rc_frame_buffer_pos = 0;
static uint32_t rc_last_motion_apply_ms = 0;
static bool     rc_last_fire_request = false;
static bool     rc_switch_raw_low = false;
static bool     rc_switch_stable_low = false;
static uint32_t rc_switch_last_change_ms = 0;
static const uint32_t RC_SWITCH_DEBOUNCE_MS = 35;

// ─────────────────────────────────────────────────────────────
// Button sweep
// ─────────────────────────────────────────────────────────────
static const uint32_t SWEEP_BUTTON_DEBOUNCE_MS = 35;
static const uint16_t SWEEP_MOVE_TIME_MS = 2500;
static const uint32_t SWEEP_STEP_HOLD_MS = 2800;
static const uint8_t  SWEEP_STEP_COUNT   = 6;

static bool     sweep_button_raw_pressed     = false;
static bool     sweep_button_stable_pressed  = false;
static uint32_t sweep_button_last_change_ms  = 0;
static bool     sweep_active                 = false;
static uint8_t  sweep_step_index             = 0;
static bool     sweep_step_initialized       = false;
static uint32_t sweep_step_started_ms        = 0;

// ─────────────────────────────────────────────────────────────
// Status LED blink engine (non-blocking, queued)
//   1 pulse  = motion command
//   2 pulses = fire command
//   3 pulses = accessory (LED/laser)
//   4 pulses = safety toggle
//   5 pulses = mode/sweep
//   6 pulses = PIR event
// ─────────────────────────────────────────────────────────────
static const uint8_t BLINK_QUEUE_CAP = 12;
static uint8_t blink_queue[BLINK_QUEUE_CAP];
static uint8_t blink_q_head = 0;
static uint8_t blink_q_tail = 0;

static uint8_t  blink_pulses_remaining = 0;
static bool     blink_led_on           = false;
static uint32_t blink_next_toggle_ms   = 0;
static uint16_t blink_on_ms            = 80;
static uint16_t blink_off_ms           = 80;
static bool     blink_enabled          = true;

static inline void set_status_led(bool on) {
  digitalWrite(PIN_STATUS_LED, on ? HIGH : LOW);
}

static bool blink_queue_is_empty() {
  return blink_q_head == blink_q_tail;
}
static bool blink_queue_push(uint8_t pulses) {
  if (pulses == 0) return false;
  uint8_t next_tail = (uint8_t)((blink_q_tail + 1U) % BLINK_QUEUE_CAP);
  if (next_tail == blink_q_head) return false;
  blink_queue[blink_q_tail] = pulses;
  blink_q_tail = next_tail;
  return true;
}
static bool blink_queue_pop(uint8_t *out) {
  if (blink_queue_is_empty() || out == nullptr) return false;
  *out = blink_queue[blink_q_head];
  blink_q_head = (uint8_t)((blink_q_head + 1U) % BLINK_QUEUE_CAP);
  return true;
}
static void status_led_begin_pattern(uint8_t pulses, uint16_t on_ms, uint16_t off_ms) {
  if (!blink_enabled || pulses == 0) return;
  blink_pulses_remaining = pulses;
  blink_on_ms  = (on_ms  < 20) ? 20 : on_ms;
  blink_off_ms = (off_ms < 20) ? 20 : off_ms;
  blink_led_on = true;
  set_status_led(true);
  blink_next_toggle_ms = millis() + (uint32_t)blink_on_ms;
}
static void status_led_enqueue_pattern(uint8_t pulses) {
  if (!blink_enabled || pulses == 0) return;
  if (!blink_queue_push(pulses))
    Serial.println("[LED] Blink queue full; dropping pattern");
}
static void status_led_tick(uint32_t now_val) {
  if (!blink_enabled) return;
  if (blink_pulses_remaining == 0) {
    uint8_t nxt = 0;
    if (blink_queue_pop(&nxt)) status_led_begin_pattern(nxt, 80, 90);
    return;
  }
  if (now_val < blink_next_toggle_ms) return;
  if (blink_led_on) {
    set_status_led(false);
    blink_led_on = false;
    blink_pulses_remaining--;
    blink_next_toggle_ms = now_val + (uint32_t)blink_off_ms;
  } else {
    if (blink_pulses_remaining > 0) {
      set_status_led(true);
      blink_led_on = true;
      blink_next_toggle_ms = now_val + (uint32_t)blink_on_ms;
    }
  }
}

// ─────────────────────────────────────────────────────────────
// Forward declarations
// ─────────────────────────────────────────────────────────────
static void run_self_test();
static void update_button_sweep(uint32_t now_val);
static void bus_flush_rx();
static void bus_reinit(uint32_t baud);

// ─────────────────────────────────────────────────────────────
// CRC32
// ─────────────────────────────────────────────────────────────
static uint32_t crc32_update(uint32_t crc, uint8_t data) {
  crc ^= data;
  for (int i = 0; i < 8; ++i)
    crc = (crc & 1) ? ((crc >> 1) ^ 0xEDB88320UL) : (crc >> 1);
  return crc;
}
static uint32_t crc32_compute(const uint8_t *data, size_t len) {
  uint32_t crc = 0xFFFFFFFFUL;
  for (size_t i = 0; i < len; ++i) crc = crc32_update(crc, data[i]);
  return ~crc;
}

// ─────────────────────────────────────────────────────────────
// General helpers
// ─────────────────────────────────────────────────────────────
static int clamp_int(int v, int lo, int hi) {
  if (v < lo) return lo;
  if (v > hi) return hi;
  return v;
}
static int apply_invert_and_clamp(int deg, int minDeg, int maxDeg, bool invert) {
  deg = clamp_int(deg, minDeg, maxDeg);
  if (!invert) return deg;
  return minDeg + ((maxDeg - minDeg) - (deg - minDeg));
}
static uint32_t now_ms() { return millis(); }
static uint32_t deg_to_duty_us(int deg) {
  int clamped = clamp_int(deg, 0, 180);
  return (uint32_t)map(clamped, 0, 180, SERVO_MIN_US, SERVO_MAX_US);
}
static uint16_t compute_move_time_ms(int delta) {
  if (delta < 0) delta = -delta;
  if (delta >= 30) return MOVE_TIME_BIG_MS;
  if (delta >= 15) return MOVE_TIME_MED_MS;
  if (delta >=  7) return MOVE_TIME_SMALL_MS;
  return MOVE_TIME_TINY_MS;
}
static uint16_t map_deg_to_ticks(int deg, int minDeg, int maxDeg,
                                 uint16_t ticksMin, uint16_t ticksMax) {
  deg = clamp_int(deg, minDeg, maxDeg);
  int degSpan = maxDeg - minDeg;
  if (degSpan <= 0) return ticksMin;
  long ticksSpan = (long)ticksMax - (long)ticksMin;
  long ticks = (long)ticksMin + ((long)(deg - minDeg) * ticksSpan) / (long)degSpan;
  long lo = (ticksMin < ticksMax) ? ticksMin : ticksMax;
  long hi = (ticksMin < ticksMax) ? ticksMax : ticksMin;
  if (ticks < lo) ticks = lo;
  if (ticks > hi) ticks = hi;
  return (uint16_t)ticks;
}
static uint32_t duty_us_to_ticks(uint32_t us) {
  uint32_t max_ticks  = (1UL << SERVO_RES_BITS) - 1;
  uint32_t period_us  = 1000000UL / SERVO_HZ;
  uint32_t ticks      = (us * max_ticks) / period_us;
  return (ticks > max_ticks) ? max_ticks : ticks;
}
static int clamp_servo_angle(int deg) {
  return clamp_int(deg, 0, 180);
}
static bool ensure_buzzer_pwm_ready() {
  if (buzzer_pwm_ready) return true;
  buzzer_pwm_ready = ledcAttach(PIN_BUZZER, 2000, BUZZER_PWM_RES_BITS);
  if (buzzer_pwm_ready) {
    ledcWrite(PIN_BUZZER, 0);
  }
  return buzzer_pwm_ready;
}
static void stop_sound_tone() {
  if (buzzer_pwm_ready) {
    ledcWriteTone(PIN_BUZZER, 0);
    ledcWrite(PIN_BUZZER, 0);
  }
  sound_active = false;
  sound_end_ms = 0;
  sound_freq_hz = 0;
}
static void start_sound_tone(int freq_hz, int duration_ms, int volume_pct = 100) {
  if (!ensure_buzzer_pwm_ready()) {
    Serial.println("[SOUND] Buzzer PWM init failed");
    return;
  }
  int freq = clamp_int(freq_hz, 120, 6000);
  int duration = clamp_int(duration_ms, 10, 2000);
  int volume = clamp_int(volume_pct, 0, 100);
  const int duty_max = (1 << BUZZER_PWM_RES_BITS) - 1;
  const int duty_min = duty_max / 32;
  const int duty_peak = duty_max / 2;
  int duty = 0;
  if (volume > 0) {
    duty = duty_min + (((duty_peak - duty_min) * volume) / 100);
    duty = clamp_int(duty, duty_min, duty_peak);
  }
  if (duty <= 0) {
    stop_sound_tone();
    return;
  }
  ledcWriteTone(PIN_BUZZER, (uint32_t)freq);
  ledcWrite(PIN_BUZZER, duty);
  sound_active = true;
  sound_freq_hz = freq;
  sound_volume_pct = volume;
  sound_end_ms = now_ms() + (uint32_t)duration;
  Serial.printf("[SOUND] %d Hz for %d ms @ %d%% duty=%d/%d peak=%d\n", freq, duration, volume, duty, duty_max, duty_peak);
}
static void update_sound_output(uint32_t now_val) {
  if (sound_active && (int32_t)(now_val - sound_end_ms) >= 0) {
    stop_sound_tone();
  }
}
static int clamped_home_pan()  { return clamp_int(home_cfg.pan,  limits_cfg.pan_min,  limits_cfg.pan_max);  }
static int clamped_home_tilt() { return clamp_int(home_cfg.tilt, limits_cfg.tilt_min, limits_cfg.tilt_max); }
static int read_current_mA(int pin, float scale) {
  if (pin < 0) return 0;
  return (int)(analogRead(pin) * scale);
}

static const char *control_source_mode_name(ControlSourceMode mode) {
  if (mode == CONTROL_SOURCE_RC) return "rc";
  if (mode == CONTROL_SOURCE_AUTO) return "auto";
  return "app";
}
static const char *active_control_source_name() {
  if (!RC_INPUT_ENABLED) return "app";
  if (control_source_mode == CONTROL_SOURCE_RC && rc_link_active) return "rc";
  if (control_source_mode == CONTROL_SOURCE_AUTO && rc_link_active && rc_override_active) return "rc";
  return "app";
}
static bool parse_control_source_mode(const char *text, ControlSourceMode *mode_out) {
  if (text == nullptr || mode_out == nullptr) return false;
  if (strcmp(text, "app") == 0) {
    *mode_out = CONTROL_SOURCE_APP;
    return true;
  }
  if (strcmp(text, "rc") == 0 || strcmp(text, "flysky") == 0) {
    *mode_out = CONTROL_SOURCE_RC;
    return true;
  }
  if (strcmp(text, "auto") == 0) {
    *mode_out = CONTROL_SOURCE_AUTO;
    return true;
  }
  return false;
}
static bool is_rc_pulse_valid(uint16_t pulse_us) {
  return pulse_us >= 800 && pulse_us <= 2200;
}
static bool is_rc_switch_high(uint16_t pulse_us) {
  return pulse_us >= RC_SWITCH_ON_THRESHOLD_US;
}
static bool is_rc_switch_low(uint16_t pulse_us) {
  return pulse_us <= RC_SWITCH_OFF_THRESHOLD_US;
}
static bool is_rc_control_active() {
  return strcmp(active_control_source_name(), "rc") == 0;
}
static int map_rc_axis_to_degrees(uint16_t pulse_us, int min_deg, int center_deg, int max_deg, int hold_deg) {
  if (!is_rc_pulse_valid(pulse_us)) return hold_deg;

  int low_deadband = (int)RC_PULSE_CENTER_US - (int)RC_STICK_DEADBAND_US;
  int high_deadband = (int)RC_PULSE_CENTER_US + (int)RC_STICK_DEADBAND_US;
  if ((int)pulse_us >= low_deadband && (int)pulse_us <= high_deadband) {
    return hold_deg;
  }

  if ((int)pulse_us < low_deadband) {
    long numer = (long)((int)pulse_us - (int)RC_PULSE_MIN_US);
    long denom = (long)(low_deadband - (int)RC_PULSE_MIN_US);
    if (denom <= 0) return min_deg;
    numer = constrain(numer, 0L, denom);
    return min_deg + (int)((numer * (long)(center_deg - min_deg)) / denom);
  }

  long numer = (long)((int)pulse_us - high_deadband);
  long denom = (long)((int)RC_PULSE_MAX_US - high_deadband);
  if (denom <= 0) return max_deg;
  numer = constrain(numer, 0L, denom);
  return center_deg + (int)((numer * (long)(max_deg - center_deg)) / denom);
}
static void update_rc_override_state() {
  bool previous_override = rc_override_active;
  bool next_override = false;

  if (rc_link_active && !rc_failsafe_active) {
    if (control_source_mode == CONTROL_SOURCE_RC) {
      next_override = true;
    } else if (control_source_mode == CONTROL_SOURCE_AUTO) {
      if (is_rc_switch_high(rc_channel_us[5])) next_override = true;
      else if (is_rc_switch_low(rc_channel_us[5])) next_override = false;
      else next_override = previous_override;
    }
  }

  rc_override_active = next_override;
  if (!rc_override_active) {
    rc_last_fire_request = false;
  }
  if (previous_override && !rc_override_active) {
    fire_request = 0;
    acc_state = 0;
    spare_state = 0;
  }
}
static void apply_rc_live_control(uint32_t now_val) {
  update_rc_override_state();
  if (!rc_override_active) return;

  int desired_pan = map_rc_axis_to_degrees(rc_channel_us[0], limits_cfg.pan_min, clamped_home_pan(), limits_cfg.pan_max, target_pan);
  int desired_tilt = map_rc_axis_to_degrees(rc_channel_us[1], limits_cfg.tilt_min, clamped_home_tilt(), limits_cfg.tilt_max, target_tilt);
  bool motion_due = (rc_last_motion_apply_ms == 0) || ((now_val - rc_last_motion_apply_ms) >= RC_MOTION_APPLY_INTERVAL_MS);
  if (motion_due) {
    target_pan = clamp_int(desired_pan, limits_cfg.pan_min, limits_cfg.pan_max);
    target_tilt = clamp_int(desired_tilt, limits_cfg.tilt_min, limits_cfg.tilt_max);
    move_time_override_ms = RC_MOVE_TIME_MS;
    move_time_override_until_ms = now_val + 250;
    rc_last_motion_apply_ms = now_val;
  }

  bool fire_request_now = is_rc_switch_high(rc_channel_us[2]);
  if (trigger_cfg.mode == 0) {
    fire_request = fire_request_now ? 1 : 0;
  } else if (fire_request_now && !rc_last_fire_request && !fire_active) {
    fire_request = 1;
  }
  rc_last_fire_request = fire_request_now;

  acc_state = is_rc_switch_high(rc_channel_us[3]) ? 1 : 0;
  spare_state = is_rc_switch_high(rc_channel_us[4]) ? 1 : 0;
}
static bool decode_ibus_frame(const uint8_t *frame, size_t len) {
  if (frame == nullptr || len != RC_IBUS_FRAME_LEN) return false;
  if (frame[0] != RC_IBUS_FRAME_LEN || frame[1] != RC_IBUS_FRAME_CMD) return false;

  uint16_t checksum = 0xFFFF;
  for (size_t i = 0; i < RC_IBUS_FRAME_LEN - 2; ++i) {
    checksum = (uint16_t)(checksum - frame[i]);
  }
  uint16_t expected = (uint16_t)frame[RC_IBUS_FRAME_LEN - 2] | ((uint16_t)frame[RC_IBUS_FRAME_LEN - 1] << 8);
  if (checksum != expected) return false;

  bool any_valid = false;
  for (int i = 0; i < 6; ++i) {
    size_t offset = 2 + (size_t)(i * 2);
    uint16_t pulse_us = (uint16_t)frame[offset] | ((uint16_t)frame[offset + 1] << 8);
    if (is_rc_pulse_valid(pulse_us)) {
      rc_channel_us[i] = pulse_us;
      any_valid = true;
    }
  }
  return any_valid;
}
static void update_rc_runtime(uint32_t now_val) {
  if (!RC_INPUT_ENABLED) {
    rc_link_active = false;
    rc_override_active = false;
    rc_failsafe_active = false;
    rc_frame_age_ms = 0;
    return;
  }

  while (rcSerial.available() > 0) {
    int b = rcSerial.read();
    if (b < 0) break;
    uint8_t byte_val = (uint8_t)b;
    if (rc_frame_buffer_pos == 0 && byte_val != RC_IBUS_FRAME_LEN) {
      continue;
    }
    if (rc_frame_buffer_pos == 1 && byte_val != RC_IBUS_FRAME_CMD) {
      rc_frame_buffer_pos = 0;
      continue;
    }

    rc_frame_buffer[rc_frame_buffer_pos++] = byte_val;
    if (rc_frame_buffer_pos >= RC_IBUS_FRAME_LEN) {
      if (decode_ibus_frame(rc_frame_buffer, RC_IBUS_FRAME_LEN)) {
        rc_last_frame_ms = now_val;
        rc_link_active = true;
        rc_failsafe_active = false;
      }
      rc_frame_buffer_pos = 0;
    }
  }

  if (rc_last_frame_ms == 0) {
    rc_link_active = false;
    rc_failsafe_active = false;
    rc_frame_age_ms = 0;
  } else {
    rc_frame_age_ms = now_val - rc_last_frame_ms;
    if (rc_frame_age_ms > RC_FRAME_TIMEOUT_MS) {
      rc_link_active = false;
      rc_failsafe_active = true;
    }
  }
  update_rc_override_state();
}
static void update_rc_mode_switch(uint32_t now_val) {
  bool raw_low = (digitalRead(PIN_RC_MODE_SWITCH) == LOW);
  if (raw_low != rc_switch_raw_low) {
    rc_switch_raw_low = raw_low;
    rc_switch_last_change_ms = now_val;
  }
  if ((now_val - rc_switch_last_change_ms) >= RC_SWITCH_DEBOUNCE_MS && rc_switch_stable_low != rc_switch_raw_low) {
    rc_switch_stable_low = rc_switch_raw_low;
    control_source_mode = rc_switch_stable_low ? CONTROL_SOURCE_RC : CONTROL_SOURCE_APP;
    Serial.printf("[RC] mode switch -> %s\n", control_source_mode_name(control_source_mode));
  }
}

// ─────────────────────────────────────────────────────────────
// Button sweep
// ─────────────────────────────────────────────────────────────
static bool get_sweep_step_target(uint8_t idx, int *panOut, int *tiltOut) {
  if (!panOut || !tiltOut) return false;
  switch (idx) {
    case 0: *panOut = clamped_home_pan();    *tiltOut = clamped_home_tilt(); return true;
    case 1: *panOut = limits_cfg.pan_min;   *tiltOut = limits_cfg.tilt_min; return true;
    case 2: *panOut = limits_cfg.pan_max;   *tiltOut = limits_cfg.tilt_min; return true;
    case 3: *panOut = limits_cfg.pan_max;   *tiltOut = limits_cfg.tilt_max; return true;
    case 4: *panOut = limits_cfg.pan_min;   *tiltOut = limits_cfg.tilt_max; return true;
    case 5: *panOut = clamped_home_pan();   *tiltOut = clamped_home_tilt(); return true;
    default: return false;
  }
}
static void start_button_sweep(uint32_t now_val) {
  if (sweep_active) return;
  sweep_active           = true;
  sweep_step_index       = 0;
  sweep_step_initialized = false;
  sweep_step_started_ms  = now_val;
  Serial.printf("[SWEEP] Start pan[%d..%d] tilt[%d..%d]\n",
                limits_cfg.pan_min, limits_cfg.pan_max,
                limits_cfg.tilt_min, limits_cfg.tilt_max);
  status_led_enqueue_pattern(5);
}
static void finish_button_sweep() {
  sweep_active     = false;
  sweep_step_index = 0;
  sweep_step_initialized = false;
  target_pan  = clamped_home_pan();
  target_tilt = clamped_home_tilt();
  Serial.printf("[SWEEP] Complete -> home pan=%d tilt=%d\n", target_pan, target_tilt);
  status_led_enqueue_pattern(5);
}
static void update_button_sweep(uint32_t now_val) {
  bool raw = (digitalRead(PIN_SWEEP_BUTTON) == LOW);
  if (raw != sweep_button_raw_pressed) {
    sweep_button_raw_pressed      = raw;
    sweep_button_last_change_ms   = now_val;
  }
  if ((now_val - sweep_button_last_change_ms) >= SWEEP_BUTTON_DEBOUNCE_MS &&
      sweep_button_stable_pressed != sweep_button_raw_pressed) {
    sweep_button_stable_pressed = sweep_button_raw_pressed;
    if (sweep_button_stable_pressed) start_button_sweep(now_val);
  }
  if (!sweep_active) return;
  if (!sweep_step_initialized) {
    int sp = clamped_home_pan(), st = clamped_home_tilt();
    if (!get_sweep_step_target(sweep_step_index, &sp, &st)) {
      finish_button_sweep(); return;
    }
    target_pan  = sp;
    target_tilt = st;
    sweep_step_started_ms  = now_val;
    sweep_step_initialized = true;
    Serial.printf("[SWEEP] Step %u/%u -> pan=%d tilt=%d\n",
                  (unsigned)(sweep_step_index + 1), (unsigned)SWEEP_STEP_COUNT,
                  target_pan, target_tilt);
  }
  if ((now_val - sweep_step_started_ms) < SWEEP_STEP_HOLD_MS) return;
  sweep_step_index++;
  sweep_step_initialized = false;
  if (sweep_step_index >= SWEEP_STEP_COUNT) finish_button_sweep();
}

// ─────────────────────────────────────────────────────────────
// Trigger servo PWM
// ─────────────────────────────────────────────────────────────
static bool ensure_trigger_servo_pwm_ready() {
  if (trigger_servo_pwm_ready) return true;
  bool ok = ledcAttach(PIN_TRIGGER_SERVO, SERVO_HZ, SERVO_RES_BITS);
  Serial.printf("[FIRE] LEDC attach: %s\n", ok ? "OK" : "FAILED!");
  trigger_servo_pwm_ready = ok;
  return ok;
}
static void servo_write_deg(int pin, int deg) {
  // Initialize PWM for servo pins as needed
  static bool pan_servo_ready = false;
  static bool tilt_servo_ready = false;

  if (pin == PIN_TRIGGER_SERVO && !trigger_servo_pwm_ready) {
    trigger_servo_pwm_ready = ledcAttach(PIN_TRIGGER_SERVO, SERVO_HZ, SERVO_RES_BITS);
    Serial.printf("[SERVO] Trigger PWM init: %s\n", trigger_servo_pwm_ready ? "OK" : "FAILED!");
  }
  if (pin == PIN_PAN_SERVO && !pan_servo_ready) {
    pan_servo_ready = ledcAttach(PIN_PAN_SERVO, SERVO_HZ, SERVO_RES_BITS);
    Serial.printf("[SERVO] Pan PWM init: %s\n", pan_servo_ready ? "OK" : "FAILED!");
  }
  if (pin == PIN_TILT_SERVO && !tilt_servo_ready) {
    tilt_servo_ready = ledcAttach(PIN_TILT_SERVO, SERVO_HZ, SERVO_RES_BITS);
    Serial.printf("[SERVO] Tilt PWM init: %s\n", tilt_servo_ready ? "OK" : "FAILED!");
  }

  ledcWrite(pin, duty_us_to_ticks(deg_to_duty_us(deg)));
}

// ─────────────────────────────────────────────────────────────
// Bus servo helpers
// ─────────────────────────────────────────────────────────────
static BusChecksumMode bus_chk_mode   = BUS_CHK_XOR;
static bool            bus_chk_locked = false;

static uint8_t bus_checksum(const uint8_t *pkt, uint8_t startIdx,
                             uint8_t endIdxInclusive, BusChecksumMode mode) {
  uint16_t sum = 0;
  for (uint8_t i = startIdx; i <= endIdxInclusive; i++) sum += pkt[i];
  uint8_t s = (uint8_t)(sum & 0xFF);
  return (mode == BUS_CHK_XOR) ? (uint8_t)((0xFF ^ s) & 0xFF) : (uint8_t)((0xFF - s) & 0xFF);
}
static void bus_write(const uint8_t *data, size_t len) {
  busSerial.write(data, len);
  busSerial.flush();
}
static void bus_flush_rx() {
  while (busSerial.available() > 0) (void)busSerial.read();
}
static void bus_reinit(uint32_t baud) {
  bus_baud_active = baud;
  Serial.printf("[BUS] Reinit UART2 baud=%u\n", (unsigned)baud);
  busSerial.end();
  delay(20);
  busSerial.begin(bus_baud_active, SERIAL_8N1, PIN_UART_RX, PIN_UART_TX);
  delay(10);
  bus_flush_rx();
}
static size_t bus_read_bytes(uint8_t *out, size_t cap, uint32_t timeoutMs) {
  uint32_t start = now_ms();
  size_t n = 0;
  while ((now_ms() - start) < timeoutMs && n < cap) {
    while (busSerial.available() > 0 && n < cap) {
      int b = busSerial.read();
      if (b >= 0) out[n++] = (uint8_t)b;
    }
    if (n >= 4) break;
    delay(1);
  }
  return n;
}
static bool bus_find_valid_packet(const uint8_t *buf, size_t n, uint8_t wantId,
                                  BusChecksumMode mode, uint8_t *outLen) {
  if (!buf || n < 6) return false;
  for (size_t i = 0; i + 5 < n; i++) {
    if (buf[i] != 0xFF || buf[i+1] != 0xFF) continue;
    uint8_t id = buf[i+2], len = buf[i+3];
    if (wantId != 0xFF && id != wantId) continue;
    if (len < 2) continue;
    size_t total = 4 + (size_t)len;
    if (i + total > n) continue;
    uint8_t chk  = buf[i + total - 1];
    uint8_t calc = bus_checksum(buf + i, 2, (uint8_t)(2 + len - 2), mode);
    if (chk != calc) continue;
    if (outLen) *outLen = len;
    return true;
  }
  return false;
}
static void build_bus_ping_pkt(uint8_t id, BusChecksumMode mode, uint8_t *out, size_t cap) {
  if (!out || cap < 6) return;
  out[0] = 0xFF; out[1] = 0xFF; out[2] = id; out[3] = 0x02; out[4] = 0x01;
  out[5] = bus_checksum(out, 2, 4, mode);
}
static bool bus_try_ping(uint8_t id, BusChecksumMode mode, uint32_t timeoutMs, size_t *rxOut) {
  bus_flush_rx();
  uint8_t pkt[6];
  build_bus_ping_pkt(id, mode, pkt, 6);
  bus_write(pkt, 6);
  uint8_t rx[64];
  size_t n = bus_read_bytes(rx, sizeof(rx), timeoutMs);
  if (rxOut) *rxOut = n;
  bool ok = bus_find_valid_packet(rx, n, id, mode, nullptr);
  Serial.printf("[BUSPING] id=%u mode=%s rx=%u -> %s\n",
                id, (mode == BUS_CHK_XOR) ? "xor" : "sub", (unsigned)n, ok ? "OK" : "FAIL");
  return ok;
}
static void bus_send_position_pkt(uint8_t id, int deg, uint16_t moveTimeMs, BusChecksumMode mode) {
  uint16_t ticksMin = (id == BUS_ID_TILT) ? TILT_TICKS_MIN : PAN_TICKS_MIN;
  uint16_t ticksMax = (id == BUS_ID_TILT) ? TILT_TICKS_MAX : PAN_TICKS_MAX;
  int minDeg        = (id == BUS_ID_TILT) ? limits_cfg.tilt_min : limits_cfg.pan_min;
  int maxDeg        = (id == BUS_ID_TILT) ? limits_cfg.tilt_max : limits_cfg.pan_max;
  uint16_t pos      = map_deg_to_ticks(deg, minDeg, maxDeg, ticksMin, ticksMax);
  uint8_t pkt[11];
  pkt[0]  = 0xFF; pkt[1]  = 0xFF; pkt[2]  = id;
  pkt[3]  = 0x07; pkt[4]  = 0x03; pkt[5]  = 0x2A;
  pkt[6]  = (pos >> 8) & 0xFF;  pkt[7]  = pos & 0xFF;
  pkt[8]  = (moveTimeMs >> 8) & 0xFF; pkt[9] = moveTimeMs & 0xFF;
  pkt[10] = bus_checksum(pkt, 2, 9, mode);
  bus_write(pkt, 11);
  bus_send_count++;
  Serial.printf("[BUS] ID=%d deg=%d ticks=%u time=%ums\n", id, deg, pos, moveTimeMs);
}
static void set_bus_servo_angle(uint8_t id, int deg, uint16_t moveTimeMs) {
  if (!bus_chk_locked) {
    bus_send_position_pkt(id, deg, moveTimeMs, BUS_CHK_SUB);
    bus_send_position_pkt(id, deg, moveTimeMs, BUS_CHK_XOR);
    return;
  }
  bus_send_position_pkt(id, deg, moveTimeMs, bus_chk_mode);
}

// ─────────────────────────────────────────────────────────────
// Output control
// ─────────────────────────────────────────────────────────────
static void update_motion_outputs(bool blocked) {
  if (blocked) return;
  int pan  = apply_invert_and_clamp(target_pan,  limits_cfg.pan_min,  limits_cfg.pan_max,  INVERT_PAN);
  int tilt = apply_invert_and_clamp(target_tilt, limits_cfg.tilt_min, limits_cfg.tilt_max, INVERT_TILT);
  uint32_t now    = now_ms();
  bool changed    = (pan != last_sent_pan) || (tilt != last_sent_tilt);
  if (!changed && sweep_active) return;
  if (!changed && (now - last_bus_send_ms) < 250) return;

  int pan_delta  = (last_sent_pan  < 0) ? 0 : (pan  - last_sent_pan);
  int tilt_delta = (last_sent_tilt < 0) ? 0 : (tilt - last_sent_tilt);
  uint16_t pan_time  = compute_move_time_ms(pan_delta);
  uint16_t tilt_time = compute_move_time_ms(tilt_delta);

  if (sweep_active) {
    pan_time = tilt_time = SWEEP_MOVE_TIME_MS;
  } else if (move_time_override_ms > 0 && now <= move_time_override_until_ms) {
    pan_time = tilt_time = move_time_override_ms;
  }
  if (changed)
    Serial.printf("[MOTION] Pan %d->%d (%ums)  Tilt %d->%d (%ums)\n",
                  last_sent_pan, pan, pan_time, last_sent_tilt, tilt, tilt_time);
  // Use PWM servos instead of serial bus
  servo_write_deg(PIN_PAN_SERVO,  pan);
  servo_write_deg(PIN_TILT_SERVO, tilt);
  last_sent_pan    = pan;
  last_sent_tilt   = tilt;
  last_bus_send_ms = now;
}
static void update_accessories() {
  digitalWrite(PIN_LED_RELAY,    led_state   ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY,  laser_state ? HIGH : LOW);
  digitalWrite(PIN_ACC_RELAY,    acc_state   ? HIGH : LOW);
  digitalWrite(PIN_SPARE_RELAY,  spare_state ? HIGH : LOW);
}
static void set_mosfet(bool on) { digitalWrite(PIN_TRIGGER_MOSFET, on ? HIGH : LOW); }
static void set_trigger_servo_target(bool fire_state) {
  trigger_servo_target_deg = (float)(fire_state ? clamp_servo_angle(trigger_cfg.servo_fire_deg)
                                                : clamp_servo_angle(trigger_cfg.servo_rest_deg));
}
static void update_trigger_servo_motion(uint32_t now_val) {
  if (trigger_servo_last_step_ms == 0) {
    trigger_servo_last_step_ms = now_val;
    servo_write_deg(PIN_TRIGGER_SERVO, (int)(trigger_servo_current_deg + 0.5f));
    return;
  }

  uint32_t elapsed_ms = now_val - trigger_servo_last_step_ms;
  if (elapsed_ms == 0) return;
  trigger_servo_last_step_ms = now_val;

  float speed_dps = (float)max(10, trigger_cfg.servo_speed_dps);
  float max_step = speed_dps * ((float)elapsed_ms / 1000.0f);
  float delta = trigger_servo_target_deg - trigger_servo_current_deg;
  float abs_delta = (delta < 0.0f) ? -delta : delta;
  if (abs_delta <= max_step) {
    trigger_servo_current_deg = trigger_servo_target_deg;
  } else {
    trigger_servo_current_deg += (delta > 0.0f) ? max_step : -max_step;
  }
  servo_write_deg(PIN_TRIGGER_SERVO, (int)(trigger_servo_current_deg + 0.5f));
}
static void update_fire_outputs(uint32_t now_val, bool blocked) {
  if (blocked) {
    fire_active = rapid_fire_active = false;
    set_mosfet(false); set_trigger_servo_target(false);
    return;
  }
  if (!fire_request) {
    fire_active = rapid_fire_active = false;
    set_mosfet(false); set_trigger_servo_target(false);
    return;
  }
  if (trigger_cfg.mode == 0) {
    // Water (MOSFET with optional rapid fire)
    if (rapid_cfg.enabled) {
      int rate_hz = max(1, rapid_cfg.rate_hz);
      float duty  = rapid_cfg.duty;
      if (duty < 0.05f) duty = 0.05f;
      if (duty > 0.95f) duty = 0.95f;
      uint32_t period_ms = 1000UL / (uint32_t)rate_hz;
      bool on = ((now_val % period_ms) < (uint32_t)((float)period_ms * duty));
      set_mosfet(on); fire_active = on; rapid_fire_active = true;
      return;
    }
    set_mosfet(true); fire_active = true; rapid_fire_active = false;
    return;
  }
  // Projectile (trigger servo pulse)
  if (!fire_active) {
    fire_active = true;
    last_fire_start_ms = now_val;
    set_trigger_servo_target(true);
    Serial.println("[FIRE] Trigger servo -> FIRE");
  } else if ((now_val - last_fire_start_ms) > TRIGGER_PULSE_MS) {
    set_trigger_servo_target(false);
    fire_active = false;
    fire_request = 0;
    Serial.println("[FIRE] Trigger servo -> REST");
  }
}

// ─────────────────────────────────────────────────────────────
// PIR monitoring
// ─────────────────────────────────────────────────────────────
#if ENABLE_PIR_SUPPORT
static void send_pir_event(int sensor_id, uint32_t ts_ms);   // forward

static void update_pir_sensors(uint32_t now_val) {
  if (!pir_enabled) return;
  for (int i = 0; i < PIR_COUNT; i++) {
    bool state = (digitalRead(PIR_PINS[i]) == HIGH);
    if (state && !pir_last_state[i]) {
      if ((now_val - pir_last_event_ms[i]) >= PIR_DEBOUNCE_MS) {
        pir_last_event_ms[i] = now_val;
        Serial.printf("[PIR] Sensor %d triggered (GPIO%d) t=%u\n",
                      i, PIR_PINS[i], (unsigned)now_val);
        if (pir_event_blink_enabled) status_led_enqueue_pattern(6);
        send_pir_event(i, now_val);
      }
    }
    pir_last_state[i] = state;
  }
}
#endif

// ─────────────────────────────────────────────────────────────
// UDP JSON codec
// ─────────────────────────────────────────────────────────────
static void encode_and_send(JsonDocument &doc, IPAddress ip, uint16_t port) {
  String compact;
  serializeJson(doc, compact);
  uint32_t crc = crc32_compute((const uint8_t *)compact.c_str(), compact.length());
  char crc_hex[9];
  snprintf(crc_hex, sizeof(crc_hex), "%08x", (unsigned int)crc);
  doc["crc"] = crc_hex;
  String payload;
  serializeJson(doc, payload);
  Udp.beginPacket(ip, port);
  Udp.write((const uint8_t *)payload.c_str(), payload.length());
  Udp.endPacket();
}

static bool decode_message(char *buffer, size_t len, JsonDocument &doc) {
  DeserializationError err = deserializeJson(doc, buffer, len);
  if (err) {
    parse_fail_count++;
    Serial.printf("[ERR] JSON parse: %s | %.120s\n", err.c_str(), buffer);
    return false;
  }
  if (!doc["crc"].is<const char*>()) {
    parse_fail_count++;
    Serial.printf("[ERR] Missing crc | %.120s\n", buffer);
    return false;
  }
  const char *crc_str = doc["crc"];
  char crc_copy[16] = {0};
  snprintf(crc_copy, sizeof(crc_copy), "%s", crc_str);
  doc.remove("crc");
  String compact;
  serializeJson(doc, compact);
  uint32_t crc = crc32_compute((const uint8_t *)compact.c_str(), compact.length());
  char calc[9];
  snprintf(calc, sizeof(calc), "%08x", (unsigned int)crc);
  if (strcasecmp(calc, crc_copy) != 0) {
    crc_fail_count++;
    Serial.printf("[ERR] CRC mismatch calc=%s recv=%s | %.80s\n", calc, crc_copy, buffer);
    return false;
  }
  return true;
}

// ─────────────────────────────────────────────────────────────
// UDP reply builders
// ─────────────────────────────────────────────────────────────
static void send_ack(int seq, bool ok, IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"] = 1; doc["t"] = "ack"; doc["seq"] = seq;
  doc["ts"] = (uint32_t)now_ms(); doc["ok"] = ok;
  JsonObject s = doc["state"].to<JsonObject>();
  s["pan"]           = target_pan;  s["tilt"]         = target_tilt;
  s["fire"]          = fire_active ? 1 : 0;
  s["safety"]        = safety_state; s["mode"]         = trigger_cfg.mode;
  s["current_fault"] = current_fault;
#if ENABLE_PIR_SUPPORT
  s["pir_enabled"] = pir_enabled ? 1 : 0;
#endif
  JsonObject p = doc["p"].to<JsonObject>();
  p["control_source_mode"] = control_source_mode_name(control_source_mode);
  p["control_source_active"] = active_control_source_name();
  p["rc_link_active"] = rc_link_active ? 1 : 0;
  p["rc_override_active"] = rc_override_active ? 1 : 0;
  p["rc_failsafe_active"] = rc_failsafe_active ? 1 : 0;
  p["rc_frame_age_ms"] = rc_frame_age_ms;
  JsonObject rc = p["rc"].to<JsonObject>();
  rc["receiver_model"] = "flysky_fs_ia6";
  rc["link_active"] = rc_link_active;
  rc["override_active"] = rc_override_active;
  rc["failsafe_active"] = rc_failsafe_active;
  rc["frame_age_ms"] = rc_frame_age_ms;
  rc["ch1_us"] = rc_channel_us[0];
  rc["ch2_us"] = rc_channel_us[1];
  rc["ch3_us"] = rc_channel_us[2];
  rc["ch4_us"] = rc_channel_us[3];
  rc["ch5_us"] = rc_channel_us[4];
  rc["ch6_us"] = rc_channel_us[5];
  encode_and_send(doc, ip, port);
}

static void send_caps(IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"] = 1; doc["t"] = "cap"; doc["seq"] = 0; doc["ts"] = (uint32_t)now_ms();
  JsonObject caps = doc["p"].to<JsonObject>();
  caps["proto"] = 1;
  caps["fw"]    = "smart-sentry-v2.3-db3000-esp32-udp-pir-flysky";
  caps["role"] = "db3000_wifi_io";
  caps["sound_supported"] = true;
  caps["switch_supported"] = false;
  caps["header_reference_locked"] = false;
  caps["rc_input_supported"] = RC_INPUT_ENABLED;
  caps["rc_input_protocol"] = "ibus";
  caps["rc_mode_supported"] = RC_INPUT_ENABLED;
  caps["rc_mode_default"] = "app";
  caps["rc_receiver_model"] = "flysky_fs_ia6";
  caps["rc_source_switch_channel"] = 6;
  caps["rc_board_switch_required"] = false;
  caps["rc_board_switch_note"] = "gpio22_selects_app_or_rc_mode_without_breaking_app_fallback_when_receiver_is_missing";
#if ENABLE_PIR_SUPPORT
  caps["pir_support"] = true;
  caps["pir_count"]   = PIR_COUNT;
  JsonArray pir_pins_arr = caps["pir_pins"].to<JsonArray>();
  for (int i = 0; i < PIR_COUNT; i++) pir_pins_arr.add(PIR_PINS[i]);
#else
  caps["pir_support"] = false;
#endif
  JsonObject pins = caps["pins"].to<JsonObject>();
  pins["uart_rx"] = PIN_UART_RX; pins["uart_tx"] = PIN_UART_TX;
  pins["mosfet"]  = PIN_TRIGGER_MOSFET; pins["trigger_servo"] = PIN_TRIGGER_SERVO;
  pins["pan_servo"] = PIN_PAN_SERVO; pins["tilt_servo"] = PIN_TILT_SERVO;
  pins["led"]     = PIN_LED_RELAY;      pins["laser"] = PIN_LASER_RELAY;
  pins["acc"]     = PIN_ACC_RELAY;      pins["spare"] = PIN_SPARE_RELAY;
  pins["buzzer"]  = PIN_BUZZER;
  pins["header_trigger_mosfet"] = PIN_TRIGGER_MOSFET;
  pins["header_rc_uart_rx_planned"] = PIN_RC_UART_RX;
  pins["rc_mode_switch_gpio"] = PIN_RC_MODE_SWITCH;
  encode_and_send(doc, ip, port);
  Serial.printf("[TX] Caps -> %s:%u\n", ip.toString().c_str(), port);
}

static void send_state(IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"] = 1; doc["t"] = "state"; doc["seq"] = 0; doc["ts"] = (uint32_t)now_ms();
  JsonObject s = doc["p"].to<JsonObject>();
  s["pan"]           = target_pan;  s["tilt"]         = target_tilt;
  s["fire"]          = fire_active ? 1 : 0;
  s["safety"]        = safety_state; s["mode"]         = trigger_cfg.mode;
  s["current_fault"] = current_fault;
  s["pan_mA"]        = latest_pan_mA;
  s["tilt_mA"]       = latest_tilt_mA;
  s["total_mA"]      = latest_total_mA;
  s["control_source_mode"] = control_source_mode_name(control_source_mode);
  s["control_source_active"] = active_control_source_name();
  s["rc_link_active"] = rc_link_active ? 1 : 0;
  s["rc_override_active"] = rc_override_active ? 1 : 0;
  s["rc_failsafe_active"] = rc_failsafe_active ? 1 : 0;
  s["rc_frame_age_ms"] = rc_frame_age_ms;
#if ENABLE_PIR_SUPPORT
  s["pir_enabled"] = pir_enabled ? 1 : 0;
#endif
  JsonObject rc = s["rc"].to<JsonObject>();
  rc["receiver_model"] = "flysky_fs_ia6";
  rc["link_active"] = rc_link_active;
  rc["override_active"] = rc_override_active;
  rc["failsafe_active"] = rc_failsafe_active;
  rc["frame_age_ms"] = rc_frame_age_ms;
  rc["ch1_us"] = rc_channel_us[0];
  rc["ch2_us"] = rc_channel_us[1];
  rc["ch3_us"] = rc_channel_us[2];
  rc["ch4_us"] = rc_channel_us[3];
  rc["ch5_us"] = rc_channel_us[4];
  rc["ch6_us"] = rc_channel_us[5];
  JsonObject bus = s["bus"].to<JsonObject>();
  bus["send_count"] = bus_send_count;
  bus["baud"]       = (uint32_t)bus_baud_active;
  bus["chk_locked"] = bus_chk_locked;
  bus["chk_mode"]   = bus_chk_locked ? ((bus_chk_mode == BUS_CHK_XOR) ? "xor" : "sub") : "auto";
  encode_and_send(doc, ip, port);
}

#if ENABLE_PIR_SUPPORT
static void send_pir_event(int sensor_id, uint32_t ts_ms) {
  if (last_remote_port == 0) return;   // No client connected yet
  JsonDocument doc;
  doc["v"]  = 1; doc["t"] = "pir_event"; doc["seq"] = 0;
  doc["ts"] = (uint32_t)now_ms();
  JsonObject p = doc["p"].to<JsonObject>();
  p["sensor_id"]    = sensor_id;
  p["timestamp_ms"] = ts_ms;
  encode_and_send(doc, last_remote_ip, last_remote_port);
  Serial.printf("[TX] PIR event sensor=%d ts=%u -> %s:%u\n",
                sensor_id, (unsigned)ts_ms,
                last_remote_ip.toString().c_str(), last_remote_port);
}
#endif

// ─────────────────────────────────────────────────────────────
// Config application
// ─────────────────────────────────────────────────────────────
static void apply_config(JsonObject cfg) {
  Serial.println("[CFG] Applying config...");
  if (cfg.containsKey("limits")) {
    JsonObject lim = cfg["limits"];
    limits_cfg.pan_min  = lim["pan_min"]  | limits_cfg.pan_min;
    limits_cfg.pan_max  = lim["pan_max"]  | limits_cfg.pan_max;
    limits_cfg.tilt_min = lim["tilt_min"] | limits_cfg.tilt_min;
    limits_cfg.tilt_max = lim["tilt_max"] | limits_cfg.tilt_max;
  }
  if (cfg.containsKey("home")) {
    JsonObject h = cfg["home"];
    home_cfg.pan  = h["pan"]  | home_cfg.pan;
    home_cfg.tilt = h["tilt"] | home_cfg.tilt;
  }
  if (cfg.containsKey("trigger")) {
    JsonObject t = cfg["trigger"];
    trigger_cfg.mode       = t["mode"]       | trigger_cfg.mode;
    trigger_cfg.cooldown_s = t["cooldown_s"] | trigger_cfg.cooldown_s;
    trigger_cfg.max_fire_s = t["max_fire_s"] | trigger_cfg.max_fire_s;
    trigger_cfg.servo_rest_deg = clamp_servo_angle(t["servo_rest_deg"] | trigger_cfg.servo_rest_deg);
    trigger_cfg.servo_fire_deg = clamp_servo_angle(t["servo_fire_deg"] | trigger_cfg.servo_fire_deg);
    if (trigger_cfg.servo_fire_deg < trigger_cfg.servo_rest_deg) {
      trigger_cfg.servo_fire_deg = trigger_cfg.servo_rest_deg;
    }
    trigger_cfg.servo_speed_dps = max(10, (int)(t["servo_speed_dps"] | trigger_cfg.servo_speed_dps));
    if (!fire_active) {
      trigger_servo_current_deg = (float)trigger_cfg.servo_rest_deg;
      trigger_servo_target_deg = (float)trigger_cfg.servo_rest_deg;
      servo_write_deg(PIN_TRIGGER_SERVO, trigger_cfg.servo_rest_deg);
    }
  }
  if (cfg.containsKey("pir")) {
    JsonObject pir = cfg["pir"];
    pir_event_blink_enabled = ((int)(pir["event_blink"] | (pir_event_blink_enabled ? 1 : 0))) != 0;
  }
  if (cfg.containsKey("rapid_fire")) {
    JsonObject rf = cfg["rapid_fire"];
    rapid_cfg.enabled = rf["enabled"] | rapid_cfg.enabled;
    rapid_cfg.rate_hz = rf["rate_hz"] | rapid_cfg.rate_hz;
    rapid_cfg.duty    = rf["duty"]    | rapid_cfg.duty;
  }
  if (cfg.containsKey("current_protection")) {
    JsonObject cp = cfg["current_protection"];
    current_cfg.enabled       = cp["enabled"]       | current_cfg.enabled;
    current_cfg.block_fire    = cp["block_fire"]    | current_cfg.block_fire;
    current_cfg.block_motion  = cp["block_motion"]  | current_cfg.block_motion;
    current_cfg.latch         = cp["latch"]         | current_cfg.latch;
    current_cfg.trip_pan_mA   = cp["trip_pan_mA"]   | current_cfg.trip_pan_mA;
    current_cfg.trip_tilt_mA  = cp["trip_tilt_mA"]  | current_cfg.trip_tilt_mA;
    current_cfg.trip_total_mA = cp["trip_total_mA"] | current_cfg.trip_total_mA;
    current_cfg.trip_hold_ms  = cp["trip_hold_ms"]  | current_cfg.trip_hold_ms;
    current_cfg.clear_hold_ms = cp["clear_hold_ms"] | current_cfg.clear_hold_ms;
    current_cfg.hysteresis_mA = cp["hysteresis_mA"] | current_cfg.hysteresis_mA;
  }
}

// ─────────────────────────────────────────────────────────────
// Command application
// ─────────────────────────────────────────────────────────────
static void apply_command(JsonObject payload) {
  cmd_count++;
  bool blink_safety = false, blink_mode = false, blink_fire = false;
  bool blink_accessory = false, blink_motion = false;

  if (payload.containsKey("control_source_mode")) {
    ControlSourceMode parsed_mode;
    const char *requested = payload["control_source_mode"] | "";
    if (parse_control_source_mode(requested, &parsed_mode)) {
      control_source_mode = parsed_mode;
      Serial.printf("[CTRL] control_source_mode=%s\n", control_source_mode_name(control_source_mode));
      blink_mode = true;
    }
  }

  bool rc_owns_motion_and_outputs = is_rc_control_active();

  if (payload.containsKey("safety")) {
    int prev = safety_state;
    safety_state = payload["safety"];
    if (prev != safety_state) {
      blink_safety = true;
      Serial.printf("[CMD] safety: %d->%d (%s)\n", prev, safety_state,
                    safety_state == 0 ? "ARMED" : "LOCKED");
    }
  }
  if (!rc_owns_motion_and_outputs && payload.containsKey("led")) {
    int prev = led_state; led_state = payload["led"];
    if (prev != led_state) blink_accessory = true;
  }
  if (!rc_owns_motion_and_outputs && payload.containsKey("laser")) {
    int prev = laser_state; laser_state = payload["laser"];
    if (prev != laser_state) blink_accessory = true;
  }
  if (!rc_owns_motion_and_outputs && payload.containsKey("acc")) {
    int prev = acc_state; acc_state = payload["acc"];
    if (prev != acc_state) blink_accessory = true;
  }
  if (!rc_owns_motion_and_outputs && payload.containsKey("spare")) {
    int prev = spare_state; spare_state = payload["spare"];
    if (prev != spare_state) blink_accessory = true;
  }
  if (payload.containsKey("mode")) {
    int prev = trigger_cfg.mode; trigger_cfg.mode = payload["mode"];
    if (prev != trigger_cfg.mode) blink_mode = true;
  }
  if (!rc_owns_motion_and_outputs && payload.containsKey("fire_hold")) {
    bool prev = fire_hold; fire_hold = payload["fire_hold"];
    if (prev != fire_hold) blink_fire = true;
  }
  if (!rc_owns_motion_and_outputs && payload.containsKey("fire")) {
    int prev = fire_request; fire_request = payload["fire"];
    if (prev != fire_request) {
      blink_fire = true;
      Serial.printf("[CMD] fire: %d->%d (mode=%d safety=%d)\n",
                    prev, fire_request, trigger_cfg.mode, safety_state);
      if (fire_request && safety_state != 0)
        Serial.println("[WARN] FIRE_BLOCKED: safety is LOCKED (S=1). Send safety=0 to arm.");
    }
  }

#if ENABLE_PIR_SUPPORT
  if (payload.containsKey("pir_enabled")) {
    bool prev = pir_enabled;
    pir_enabled = (int)payload["pir_enabled"] != 0;
    if (prev != pir_enabled)
      Serial.printf("[CMD] pir_enabled: %s->%s\n",
                    prev ? "true" : "false",
                    pir_enabled ? "true" : "false");
  }
#endif

  int prev_pan = target_pan, prev_tilt = target_tilt;
  if (!rc_owns_motion_and_outputs && payload.containsKey("pan_cmd"))
    target_pan  = payload["pan_cmd"];
  else if (!rc_owns_motion_and_outputs && payload.containsKey("pan"))
    target_pan  = (int)(payload["pan"].as<float>() + 0.5f);
  if (!rc_owns_motion_and_outputs && payload.containsKey("tilt_cmd"))
    target_tilt = payload["tilt_cmd"];
  else if (!rc_owns_motion_and_outputs && payload.containsKey("tilt"))
    target_tilt = (int)(payload["tilt"].as<float>() + 0.5f);

  target_pan  = clamp_int(target_pan,  limits_cfg.pan_min,  limits_cfg.pan_max);
  target_tilt = clamp_int(target_tilt, limits_cfg.tilt_min, limits_cfg.tilt_max);

  if (!rc_owns_motion_and_outputs && payload.containsKey("move_time_ms")) {
    int mt = payload["move_time_ms"] | 0;
    mt = clamp_int(mt, 0, 5000);
    move_time_override_ms       = (uint16_t)mt;
    move_time_override_until_ms = now_ms() + 5000;
  }
  if (target_pan != prev_pan || target_tilt != prev_tilt) {
    blink_motion = true;
    Serial.printf("[CMD] pos: pan %d->%d  tilt %d->%d\n",
                  prev_pan, target_pan, prev_tilt, target_tilt);
  }
  if (!rc_owns_motion_and_outputs && payload.containsKey("rapid_fire")) {
    JsonObject rf = payload["rapid_fire"];
    rapid_cfg.enabled = rf["enabled"] | rapid_cfg.enabled;
    rapid_cfg.rate_hz = rf["rate_hz"] | rapid_cfg.rate_hz;
    rapid_cfg.duty    = rf["duty"]    | rapid_cfg.duty;
    blink_fire = true;
  }

  if (blink_safety)    status_led_enqueue_pattern(4);
  if (blink_mode)      status_led_enqueue_pattern(5);
  if (blink_accessory) status_led_enqueue_pattern(3);
  if (blink_fire)      status_led_enqueue_pattern(2);
  if (blink_motion)    status_led_enqueue_pattern(1);
}

// ─────────────────────────────────────────────────────────────
// Packet dispatcher
// ─────────────────────────────────────────────────────────────
static void send_ack_busdiag(int seq, bool ok, IPAddress ip, uint16_t port,
                             bool pan_ok, bool tilt_ok, uint32_t rx_pan, uint32_t rx_tilt,
                             const char *mode_str, bool bridge_rx_ok) {
  JsonDocument doc;
  doc["v"] = 1; doc["t"] = "ack"; doc["seq"] = seq;
  doc["ts"] = (uint32_t)now_ms(); doc["ok"] = ok;
  JsonObject st = doc["state"].to<JsonObject>();
  st["pan"] = target_pan; st["tilt"] = target_tilt;
  st["fire"] = fire_active ? 1 : 0; st["safety"] = safety_state;
  JsonObject p = doc["p"].to<JsonObject>();
  JsonObject bus = p["bus"].to<JsonObject>();
  bus["pan_ok"] = pan_ok; bus["tilt_ok"] = tilt_ok;
  bus["rx_pan"] = rx_pan; bus["rx_tilt"] = rx_tilt;
  bus["bridge_rx_ok"] = bridge_rx_ok;
  bus["chk_mode"]   = mode_str; bus["chk_locked"] = bus_chk_locked;
  bus["bus_send_count"] = bus_send_count; bus["baud"] = (uint32_t)bus_baud_active;
  encode_and_send(doc, ip, port);
}

static void process_packet(char *buffer, size_t len, IPAddress ip, uint16_t port) {
  if (!first_client_seen) {
    first_client_seen = true;
    Serial.printf("[LINK] *** First client: %s:%u ***\n", ip.toString().c_str(), port);
  }
  Serial.printf("[RX] %u bytes from %s:%u | %.100s%s\n",
                (unsigned)len, ip.toString().c_str(), port,
                buffer, len > 100 ? "..." : "");

  JsonDocument doc;
  if (!decode_message(buffer, len, doc)) {
    Serial.printf("[ERR] Decode fail (crc_fail=%u parse_fail=%u)\n",
                  crc_fail_count, parse_fail_count);
    return;
  }

  const char *type = doc["t"] | "";
  int seq          = doc["seq"] | 0;
  Serial.printf("[MSG] type='%s' seq=%d\n", type, seq);

  if (strcmp(type, "hello") == 0) {
    send_ack(seq, true, ip, port);
    send_caps(ip, port);
    return;
  }
  if (strcmp(type, "hb") == 0) {
    send_state(ip, port);
    return;
  }
  if (strcmp(type, "cmd") == 0) {
    JsonObject payload = doc["p"].as<JsonObject>();
    if (payload.containsKey("action")) {
      const char *action = payload["action"] | "";
      Serial.printf("[CMD] action='%s'\n", action);
      if (strcmp(action, "config") == 0) {
        apply_config(payload); send_ack(seq, true, ip, port);
      } else if (strcmp(action, "rc_mode") == 0) {
        ControlSourceMode parsed_mode;
        const char *requested = payload["mode"] | payload["control_source_mode"] | "";
        bool ok_mode = parse_control_source_mode(requested, &parsed_mode);
        if (ok_mode) {
          control_source_mode = parsed_mode;
          Serial.printf("[CTRL] control_source_mode=%s\n", control_source_mode_name(control_source_mode));
        }
        send_ack(seq, ok_mode, ip, port);
      } else if (strcmp(action, "sound") == 0) {
        int freq_hz = payload["freq_hz"] | payload["freq"] | 1200;
        int duration_ms = payload["duration_ms"] | 60;
        int volume_pct = payload["volume_pct"] | 100;
        start_sound_tone(freq_hz, duration_ms, volume_pct);
        send_ack(seq, true, ip, port);
      } else if (strcmp(action, "encoder_request") == 0) {
        send_ack(seq, true, ip, port); send_state(ip, port);
      } else if (strcmp(action, "bus_ping") == 0) {
        size_t rx_psub = 0, rx_pxor = 0, rx_tsub = 0, rx_txor = 0;
        bool p_sub = false, p_xor = false, t_sub = false, t_xor = false;
        auto do_pings = [&]() {
          rx_psub = rx_pxor = rx_tsub = rx_txor = 0;
          p_sub = bus_try_ping(BUS_ID_PAN,  BUS_CHK_SUB, 50, &rx_psub);
          p_xor = bus_try_ping(BUS_ID_PAN,  BUS_CHK_XOR, 50, &rx_pxor);
          t_sub = bus_try_ping(BUS_ID_TILT, BUS_CHK_SUB, 50, &rx_tsub);
          t_xor = bus_try_ping(BUS_ID_TILT, BUS_CHK_XOR, 50, &rx_txor);
        };
        do_pings();
        if (!(p_sub || p_xor || t_sub || t_xor)) {
          const uint32_t candidates[] = {BUS_BAUD, 115200, 57600, 38400};
          for (size_t ci = 0; ci < 4; ci++) {
            if (candidates[ci] == bus_baud_active) continue;
            bus_reinit(candidates[ci]); do_pings();
            if (p_sub || p_xor || t_sub || t_xor) break;
          }
        }
        if (!bus_chk_locked) {
          if (p_xor || t_xor) { bus_chk_mode = BUS_CHK_XOR; bus_chk_locked = true; Serial.println("[BUSPING] Locked: xor"); }
          else if (p_sub || t_sub) { bus_chk_mode = BUS_CHK_SUB; bus_chk_locked = true; Serial.println("[BUSPING] Locked: sub"); }
        }
        bool pan_ok  = bus_chk_locked ? ((bus_chk_mode == BUS_CHK_XOR) ? p_xor : p_sub) : (p_sub || p_xor);
        bool tilt_ok = bus_chk_locked ? ((bus_chk_mode == BUS_CHK_XOR) ? t_xor : t_sub) : (t_sub || t_xor);
        const char *mode_str = bus_chk_locked ? ((bus_chk_mode == BUS_CHK_XOR) ? "xor" : "sub") : "auto";
        uint32_t rx_pan  = bus_chk_locked ? (uint32_t)((bus_chk_mode == BUS_CHK_XOR) ? rx_pxor : rx_psub)
                                           : (uint32_t)((rx_psub > rx_pxor) ? rx_psub : rx_pxor);
        uint32_t rx_tilt = bus_chk_locked ? (uint32_t)((bus_chk_mode == BUS_CHK_XOR) ? rx_txor : rx_tsub)
                                           : (uint32_t)((rx_tsub > rx_txor) ? rx_tsub : rx_txor);
        bool bridge_rx_ok = (rx_pan > 0 && rx_tilt > 0);
        send_ack_busdiag(seq, (pan_ok || tilt_ok || bridge_rx_ok), ip, port,
                         pan_ok, tilt_ok, rx_pan, rx_tilt, mode_str, bridge_rx_ok);
      } else if (strcmp(action, "test_id") == 0) {
        // Test arbitrary servo ID: {"t":"cmd","action":"test_id","id":3,"deg":90,"time":1000}
        uint8_t test_id = payload["id"] | 1;  // Default to 1 if not specified
        int test_deg = payload["deg"] | 90;  // Default to 90° if not specified
        uint16_t test_time = payload["time"] | 1000; // Default to 1000ms if not specified
        Serial.printf("[TEST_ID] Testing servo ID %d to %d° in %ums\n", test_id, test_deg, test_time);
        // Send to both pan and tilt IDs for testing
        set_bus_servo_angle(test_id, test_deg, test_time);
        send_ack(seq, true, ip, port);
      } else if (strcmp(action, "test") == 0) {
        run_self_test(); send_ack(seq, true, ip, port);
      } else {
        Serial.printf("[WARN] Unknown action: '%s'\n", action);
        send_ack(seq, false, ip, port);
      }
    } else {
      apply_command(payload);
      send_ack(seq, true, ip, port);
    }
    return;
  }
  Serial.printf("[WARN] Unknown msg type: '%s'\n", type);
}

// ─────────────────────────────────────────────────────────────
// Pin validation
// ─────────────────────────────────────────────────────────────
static void validate_pins() {
  Serial.println("[BOOT] Pin validation:");
  Serial.printf("  TRIG_SERVO  GPIO%d  PWM=%s\n",  PIN_TRIGGER_SERVO, (PIN_TRIGGER_SERVO < 34) ? "YES" : "NO");
  Serial.printf("  PAN_SERVO   GPIO%d  PWM=%s\n",  PIN_PAN_SERVO,     (PIN_PAN_SERVO < 34) ? "YES" : "NO");
  Serial.printf("  TILT_SERVO  GPIO%d  PWM=%s\n",  PIN_TILT_SERVO,    (PIN_TILT_SERVO < 34) ? "YES" : "NO");
  Serial.printf("  STATUS_LED  GPIO%d\n",           PIN_STATUS_LED);
  Serial.printf("  UART2_RX    GPIO%d  %s\n",       PIN_UART_RX,  (PIN_UART_RX  == 16) ? "DEFAULT" : "NON-DEFAULT");
  Serial.printf("  UART2_TX    GPIO%d  %s\n",       PIN_UART_TX,  (PIN_UART_TX  == 17) ? "DEFAULT" : "NON-DEFAULT");
  Serial.printf("  RC_UART_RX  GPIO%d\n",           PIN_RC_UART_RX);
  Serial.printf("  RC_MODE_SW  GPIO%d  active LOW => RC\n", PIN_RC_MODE_SWITCH);
  Serial.printf("  MOSFET      GPIO%d\n",           PIN_TRIGGER_MOSFET);
  Serial.printf("  LED_RELAY   GPIO%d\n",           PIN_LED_RELAY);
  Serial.printf("  LASER_RELAY GPIO%d\n",           PIN_LASER_RELAY);
  Serial.printf("  BUZZER      GPIO%d\n",           PIN_BUZZER);
  Serial.printf("  CURR_PAN    GPIO%d\n",           PIN_CURR_PAN);
#if ENABLE_PIR_SUPPORT
  Serial.println("  PIR enabled: GPIO 34/39 are PIR inputs (curr tilt/total sensing disabled)");
  for (int i = 0; i < PIR_COUNT; i++)
    Serial.printf("  PIR[%d]  GPIO%d\n", i, PIR_PINS[i]);
#else
  Serial.printf("  CURR_TILT   GPIO%d\n",           PIN_CURR_TILT);
  Serial.printf("  CURR_TOTAL  GPIO%d\n",           PIN_CURR_TOTAL);
#endif
  Serial.println("[BOOT] Pin validation done.");
}

// ─────────────────────────────────────────────────────────────
// Self-test
// ─────────────────────────────────────────────────────────────
static void run_self_test() {
  Serial.println("[TEST] ==== Hardware Self-Test ====");
  Serial.println("[TEST] 1/5 Trigger servo: 0->40->0");
  servo_write_deg(PIN_TRIGGER_SERVO, 0);   delay(400);
  servo_write_deg(PIN_TRIGGER_SERVO, 40);  delay(400);
  servo_write_deg(PIN_TRIGGER_SERVO, 0);   delay(400);
  Serial.println("[TEST] 2/5 LED relay toggle");
  digitalWrite(PIN_LED_RELAY, HIGH); delay(300); digitalWrite(PIN_LED_RELAY, LOW); delay(200);
  Serial.println("[TEST] 3/5 Laser relay toggle");
  digitalWrite(PIN_LASER_RELAY, HIGH); delay(300); digitalWrite(PIN_LASER_RELAY, LOW); delay(200);
  Serial.println("[TEST] 4/5 MOSFET pulse");
  digitalWrite(PIN_TRIGGER_MOSFET, HIGH); delay(150); digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  Serial.println("[TEST] 5/5 PWM servo home (Pan=90 Tilt=40)");
  servo_write_deg(PIN_PAN_SERVO,  90); delay(100);
  servo_write_deg(PIN_TILT_SERVO, 40); delay(600);
  Serial.println("[TEST] ==== Self-Test Complete ====");
}

// ─────────────────────────────────────────────────────────────
// Reset reason
// ─────────────────────────────────────────────────────────────
static void log_reset_reason() {
  esp_reset_reason_t r = esp_reset_reason();
  const char *rstr = "Unknown";
  switch (r) {
    case ESP_RST_POWERON:   rstr = "Power-on"; break;
    case ESP_RST_EXT:       rstr = "External"; break;
    case ESP_RST_SW:        rstr = "Software"; break;
    case ESP_RST_PANIC:     rstr = "Panic/exception"; break;
    case ESP_RST_INT_WDT:   rstr = "Interrupt WDT"; break;
    case ESP_RST_TASK_WDT:  rstr = "Task WDT"; break;
    case ESP_RST_DEEPSLEEP: rstr = "Deep-sleep wake"; break;
    case ESP_RST_BROWNOUT:  rstr = "*** BROWNOUT ***"; break;
    default: break;
  }
  Serial.printf("[BOOT] Reset reason: %s\n", rstr);
}

// ─────────────────────────────────────────────────────────────
// Setup
// ─────────────────────────────────────────────────────────────
void setup() {
  Serial.begin(115200);
  while (!Serial && millis() < 2000) {}

  Serial.println();
  Serial.println("================================================");
  Serial.println("  SMART_SENTRY_V2_3_DB3000_ESP32_UDP_PIR_FLYSKY");
  Serial.println("  WiFi/UDP control + PIR blind-spot sensors");
  Serial.println("  FlySky FS-iA6 i-Bus runtime + APP/RC mode switch");
  Serial.printf("  Compiled: %s %s\n", __DATE__, __TIME__);
  Serial.printf("  SDK: %s   Heap: %u\n", ESP.getSdkVersion(), ESP.getFreeHeap());
  Serial.println("================================================");
  log_reset_reason();
  validate_pins();

  // UART2 — bus servos
  busSerial.begin(bus_baud_active, SERIAL_8N1, PIN_UART_RX, PIN_UART_TX);
  Serial.printf("[BOOT] UART2 baud=%u RX=GPIO%d TX=GPIO%d\n",
                (unsigned)bus_baud_active, PIN_UART_RX, PIN_UART_TX);

  // Digital outputs
  pinMode(PIN_TRIGGER_MOSFET, OUTPUT); digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  pinMode(PIN_LED_RELAY,      OUTPUT); digitalWrite(PIN_LED_RELAY,      LOW);
  pinMode(PIN_LASER_RELAY,    OUTPUT); digitalWrite(PIN_LASER_RELAY,    LOW);
  pinMode(PIN_ACC_RELAY,      OUTPUT); digitalWrite(PIN_ACC_RELAY,      LOW);
  pinMode(PIN_SPARE_RELAY,    OUTPUT); digitalWrite(PIN_SPARE_RELAY,    LOW);
  pinMode(PIN_BUZZER,         OUTPUT); digitalWrite(PIN_BUZZER,         LOW);
  pinMode(PIN_STATUS_LED,     OUTPUT); set_status_led(false);
  pinMode(PIN_SWEEP_BUTTON,   INPUT_PULLUP);
  pinMode(PIN_RC_MODE_SWITCH, INPUT_PULLUP);
  trigger_servo_current_deg = (float)TRIGGER_SERVO_REST_DEG_DEFAULT;
  trigger_servo_target_deg = (float)TRIGGER_SERVO_REST_DEG_DEFAULT;
  trigger_servo_last_step_ms = millis();
  rc_switch_raw_low = (digitalRead(PIN_RC_MODE_SWITCH) == LOW);
  rc_switch_stable_low = rc_switch_raw_low;
  rc_switch_last_change_ms = millis();
  control_source_mode = rc_switch_stable_low ? CONTROL_SOURCE_RC : CONTROL_SOURCE_APP;
  rcSerial.begin(RC_BAUD, SERIAL_8N1, PIN_RC_UART_RX, PIN_RC_UART_TX);

  // ADC (only pins not used as PIR inputs)
  analogReadResolution(12);
  analogSetPinAttenuation(PIN_CURR_PAN, ADC_11db);
#if !ENABLE_PIR_SUPPORT
  analogSetPinAttenuation(PIN_CURR_TILT,  ADC_11db);
  analogSetPinAttenuation(PIN_CURR_TOTAL, ADC_11db);
#endif

  // PIR inputs
#if ENABLE_PIR_SUPPORT
  for (int i = 0; i < PIR_COUNT; i++) {
    pinMode(PIR_PINS[i], INPUT);   // active HIGH, no internal pull needed
    pir_last_state[i]    = false;
    pir_last_event_ms[i] = 0;
  }
  Serial.printf("[BOOT] PIR sensors: GPIO%d GPIO%d GPIO%d\n",
                PIR_PINS[0], PIR_PINS[1], PIR_PINS[2]);
#endif

  // WiFi AP
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(AP_IP, AP_GW, AP_MASK);
  bool wifi_ok = WiFi.softAP(WIFI_SSID, WIFI_PASS);
  Serial.printf("[BOOT] WiFi AP '%s': %s  IP=%s\n",
                WIFI_SSID, wifi_ok ? "OK" : "FAILED",
                WiFi.softAPIP().toString().c_str());

  // UDP
  Udp.begin(UDP_PORT);
  Serial.printf("[BOOT] UDP port %u ready\n", UDP_PORT);
  Serial.printf("[BOOT] FlySky i-Bus RX GPIO%d @ %u baud | mode switch GPIO%d initial=%s\n",
                PIN_RC_UART_RX, (unsigned)RC_BAUD, PIN_RC_MODE_SWITCH,
                control_source_mode_name(control_source_mode));

  last_cmd_ms = now_ms();
  Serial.println("================================================");
  Serial.printf("  READY  WiFi='%s'  %s:%u\n", WIFI_SSID, AP_IP.toString().c_str(), UDP_PORT);
#if ENABLE_PIR_SUPPORT
  Serial.println("  PIR: ENABLED (GPIO 35/34/39)");
#else
  Serial.println("  PIR: DISABLED");
#endif
  Serial.println("================================================\n");
}

// ─────────────────────────────────────────────────────────────
// Main loop
// ─────────────────────────────────────────────────────────────
void loop() {
  uint32_t now = now_ms();

  update_rc_mode_switch(now);
  update_rc_runtime(now);
  if (is_rc_control_active()) {
    apply_rc_live_control(now);
  }

  // UDP receive
  int pkt = Udp.parsePacket();
  if (pkt > 0) {
    static char buffer[2048];
    int len = Udp.read(buffer, sizeof(buffer) - 1);
    if (len > 0) {
      buffer[len]      = '\0';
      last_remote_ip   = Udp.remoteIP();
      last_remote_port = Udp.remotePort();
      last_cmd_ms      = now;
      process_packet(buffer, (size_t)len, last_remote_ip, last_remote_port);
    }
  }

  // Current protection
  int pan_mA   = read_current_mA(PIN_CURR_PAN,   PAN_MA_PER_ADC);
  int tilt_mA  = read_current_mA(PIN_CURR_TILT,  TILT_MA_PER_ADC);    // 0 when PIR enabled
  int total_mA = read_current_mA(PIN_CURR_TOTAL, TOTAL_MA_PER_ADC);   // 0 when PIR enabled
  latest_pan_mA = pan_mA;
  latest_tilt_mA = tilt_mA;
  latest_total_mA = total_mA;
  bool over_any = false;
  if (current_cfg.enabled) {
    bool op = (current_cfg.trip_pan_mA   > 0) && (pan_mA   >= current_cfg.trip_pan_mA);
    bool ot = (current_cfg.trip_tilt_mA  > 0) && (tilt_mA  >= current_cfg.trip_tilt_mA);
    bool ox = (current_cfg.trip_total_mA > 0) && (total_mA >= current_cfg.trip_total_mA);
    over_any = op || ot || ox;
    if (over_any) {
      if (trip_start_ms == 0) trip_start_ms = now;
      if ((now - trip_start_ms) >= (uint32_t)current_cfg.trip_hold_ms && !current_fault) {
        current_fault = true; Serial.println("[CURR] *** FAULT TRIPPED ***");
      }
    } else {
      trip_start_ms = 0;
      if (!current_cfg.latch && current_fault) { current_fault = false; Serial.println("[CURR] Fault cleared"); }
    }
  } else {
    current_fault = false;
  }

  bool fire_blocked   = (safety_state != 0) || (current_fault && current_cfg.block_fire);
  bool motion_blocked = (current_fault && current_cfg.block_motion);

  update_button_sweep(now);
  update_motion_outputs(motion_blocked);
  update_accessories();
  update_fire_outputs(now, fire_blocked);
  update_trigger_servo_motion(now);
  update_sound_output(now);

#if ENABLE_PIR_SUPPORT
  update_pir_sensors(now);
#endif

  // Link timeout — kill fire if app stops sending
  if ((now - last_cmd_ms) > 1000 && fire_request != 0) {
    Serial.println("[LINK] Timeout >1s — fire stopped");
    fire_request = 0;
  }

  status_led_tick(now);

  // Periodic state to client
  if (last_remote_port != 0 && (now - last_state_ms) > 250) {
    last_state_ms = now;
    send_state(last_remote_ip, last_remote_port);
  }

  // Periodic diagnostics (every 10 s)
  static uint32_t last_diag_ms = 0;
  if ((now - last_diag_ms) > 10000) {
    last_diag_ms = now;
    Serial.printf("[DIAG] up=%us cmds=%u bus=%u crc_f=%u parse_f=%u "
                  "heap=%u safety=%d fire=%d pan=%d tilt=%d",
                  now / 1000, cmd_count, bus_send_count,
                  crc_fail_count, parse_fail_count,
                  ESP.getFreeHeap(), safety_state,
                  fire_request, target_pan, target_tilt);
#if ENABLE_PIR_SUPPORT
    Serial.printf(" pir=%s", pir_enabled ? "on" : "off");
#endif
    Serial.println();
  }
}
