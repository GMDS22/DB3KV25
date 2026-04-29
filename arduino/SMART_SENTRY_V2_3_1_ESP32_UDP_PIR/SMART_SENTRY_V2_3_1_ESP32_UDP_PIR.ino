// SMART_SENTRY_V2_3_1_ESP32_UDP_PIR — v2.3.1
// =============================================================
// Combined firmware: WiFi/UDP turret control + PIR blind-spot sensors
// Target app release: Smart Sentry v2.3.1
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
//   - Sound action payload: {"action":"sound","freq_hz":N,"duration_ms":M,"volume_pct":V}
//   - Rest action payload: {"action":"rest"}
//   - Sweep action payload: {"action":"sweep"}
//   - Link-loss safe mode: disables fire, turns off relays, and silences PIR
//     event emission after app inactivity or client disconnect
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
static const char     *WIFI_SSID = "SMART-SENTRY-V2.3";
static const char     *WIFI_PASS = "db3000pass";
static const IPAddress AP_IP(192, 168, 4, 1);
static const IPAddress AP_GW(192, 168, 4, 1);
static const IPAddress AP_MASK(255, 255, 255, 0);
static const uint16_t  UDP_PORT  = 9000;
static const int       AP_CHANNEL = 6;
static const bool      AP_SSID_HIDDEN = false;
static const int       AP_MAX_CONNECTIONS = 4;

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
static const int PIN_BOOT_BUTTON    = 0;    // DevKit BOOT button (reserved for boot strapping)

// ---- Accessory PWM via LEDC (optional MOSFET dimming) --------------------------------
// 0 = standard ON/OFF via digitalWrite – factory default, safe for relay hardware.
// 1 = 8-bit LEDC PWM for LED, Laser, ACC, and Spare outputs via MOSFET driver.
// NOTE: only flip to 1 after MOSFET driver hardware is installed on every output channel.
//       The app sends 0-255 for each channel: 0=off, 1=full-on compat, 2-255=literal duty.
#define ACCESSORY_PWM_ENABLED  1
#define ACCESSORY_PWM_FREQ_HZ  5000u
#define ACCESSORY_PWM_BITS     8

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
static const uint16_t MOTION_PLAN_MIN_MS = 40;
static const uint16_t MOTION_UPDATE_INTERVAL_MS = 15;
static const float    MOTION_SETTLE_DEADBAND_DEG = 0.35f;
static const float    MOTION_MIN_STEP_DEG = 0.18f;
static const float    MOTION_MAX_STEP_DEG = 6.0f;

HardwareSerial busSerial(2);
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
struct RestConfig {
  int pan  = 90;
  int tilt = 55;
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
RestConfig              rest_cfg;
TriggerConfig           trigger_cfg;
RapidFireConfig         rapid_cfg;
CurrentProtectionConfig current_cfg;
TiltSafetyConfig        tilt_safety_cfg;
static bool             rest_cfg_explicit = false;

// ─────────────────────────────────────────────────────────────
// Runtime state
// ─────────────────────────────────────────────────────────────
static int  target_pan  = 90;
static int  target_tilt = 40;
static bool allow_rest_tilt_motion = false;
static int  safety_state = 1;   // 1=locked, 0=armed  (matches app: S1=safe, S0=armed)
static int  led_state    = 0;
static int  laser_state  = 0;
static int  acc_state    = 0;
static int  spare_state  = 0;
static int  fire_request = 0;
static bool fire_hold    = false;

static uint32_t last_cmd_ms      = 0;
static uint32_t last_state_ms    = 0;
static uint32_t last_mosfet_fire_start_ms = 0;
static bool     fire_active        = false;
static bool     rapid_fire_active  = false;
static bool     trigger_servo_pwm_ready = false;
static float    trigger_servo_current_deg = (float)TRIGGER_SERVO_REST_DEG_DEFAULT;
static float    trigger_servo_target_deg  = (float)TRIGGER_SERVO_REST_DEG_DEFAULT;
static uint32_t trigger_servo_last_step_ms = 0;
static bool     pir_event_blink_enabled = false;
static bool     acc_pwm_ready    = false;  // ACCESSORY_PWM_ENABLED: true once all four acc pins attached
static bool     buzzer_pwm_ready = false;
static bool     sound_active = false;
static uint8_t  sound_owner = 0;
static uint32_t sound_end_ms = 0;
static int      sound_freq_hz = 0;
static int      sound_volume_pct = 100;
static uint8_t  motion_cue_mode = 0;
static uint8_t  motion_cue_step = 0;
static uint32_t motion_cue_next_ms = 0;
static uint32_t motion_cue_keepalive_until_ms = 0;

static uint32_t trip_start_ms  = 0;
static bool     current_fault  = false;
static int      latest_pan_mA  = 0;
static int      latest_tilt_mA = 0;
static int      latest_total_mA = 0;

static int      last_sent_pan  = -1;
static int      last_sent_tilt = -1;
static uint32_t last_bus_send_ms = 0;
static float    current_output_pan_deg = 90.0f;
static float    current_output_tilt_deg = 40.0f;
static int      motion_plan_pan = 90;
static int      motion_plan_tilt = 40;
static uint16_t motion_plan_time_ms = MOTION_PLAN_MIN_MS;
static uint32_t motion_plan_started_ms = 0;
static uint32_t last_motion_update_ms = 0;
static bool     motion_output_initialized = false;

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
static uint32_t last_wifi_check_ms = 0;
static uint32_t wifi_recover_count = 0;
static bool     link_safe_mode_active = true;

static const uint32_t LINK_IDLE_SAFE_TIMEOUT_MS = 1500;
static const uint8_t  SOUND_OWNER_NONE = 0;
static const uint8_t  SOUND_OWNER_COMMAND = 1;
static const uint8_t  SOUND_OWNER_MANEUVER = 2;
static const uint8_t  MOTION_CUE_NONE = 0;
static const uint8_t  MOTION_CUE_WAKE = 1;
static const uint8_t  MOTION_CUE_REST = 2;
static const float    MOTION_CUE_START_MIN_DELTA_DEG = 1.4f;
static const float    MOTION_CUE_REST_NEAR_DEG = 8.0f;
static const float    MOTION_CUE_SETTLE_DEG = 0.9f;
static const uint32_t MOTION_CUE_REFRESH_MS = 320;
static const uint8_t  MOTION_CUE_VOLUME_PCT = 48;

// ─────────────────────────────────────────────────────────────
// Command sweep
// ─────────────────────────────────────────────────────────────
static const uint16_t SWEEP_MOVE_TIME_MS = 2500;
static const uint32_t SWEEP_STEP_HOLD_MS = 2800;
static const uint8_t  SWEEP_STEP_COUNT   = 6;

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
//   5 pulses = mode or sweep
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
static void update_sweep_sequence(uint32_t now_val);
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
static float step_toward_target(float current_deg, float target_deg,
                                uint32_t elapsed_ms, uint16_t plan_time_ms) {
  float delta = target_deg - current_deg;
  float abs_delta = fabsf(delta);
  if (abs_delta <= MOTION_SETTLE_DEADBAND_DEG) return target_deg;

  float duration_ms = (plan_time_ms > 0) ? (float)plan_time_ms : (float)MOTION_PLAN_MIN_MS;
  float step = abs_delta * ((float)elapsed_ms / duration_ms);
  if (step < MOTION_MIN_STEP_DEG) step = MOTION_MIN_STEP_DEG;
  if (step > MOTION_MAX_STEP_DEG) step = MOTION_MAX_STEP_DEG;
  if (step >= abs_delta) return target_deg;
  return current_deg + ((delta > 0.0f) ? step : -step);
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
  pinMode(PIN_BUZZER, OUTPUT);
  digitalWrite(PIN_BUZZER, LOW);
  buzzer_pwm_ready = ledcAttach(PIN_BUZZER, 2000, BUZZER_PWM_RES_BITS);
  if (buzzer_pwm_ready) {
    ledcWrite(PIN_BUZZER, 0);
  } else {
    Serial.println("[SOUND] Buzzer PWM attach failed");
  }
  return buzzer_pwm_ready;
}
static void stop_sound_tone() {
  if (buzzer_pwm_ready) {
    ledcWriteTone(PIN_BUZZER, 0);
    ledcWrite(PIN_BUZZER, 0);
  }
  sound_active = false;
  sound_owner = SOUND_OWNER_NONE;
  sound_end_ms = 0;
  sound_freq_hz = 0;
}
static float max_angle_delta_deg(float pan_a, float tilt_a, float pan_b, float tilt_b) {
  return max(fabsf(pan_a - pan_b), fabsf(tilt_a - tilt_b));
}
static void stop_motion_cue(bool silence = true) {
  motion_cue_mode = MOTION_CUE_NONE;
  motion_cue_step = 0;
  motion_cue_next_ms = 0;
  motion_cue_keepalive_until_ms = 0;
  if (silence && sound_active && sound_owner == SOUND_OWNER_MANEUVER) {
    stop_sound_tone();
  }
}
static void refresh_motion_cue(uint32_t now_val) {
  if (motion_cue_mode == MOTION_CUE_NONE) return;
  uint32_t keepalive = now_val + MOTION_CUE_REFRESH_MS;
  if ((int32_t)(keepalive - motion_cue_keepalive_until_ms) > 0) {
    motion_cue_keepalive_until_ms = keepalive;
  }
}
static void start_motion_cue(uint8_t mode, uint32_t now_val, bool restart_pattern = true) {
  if (mode == MOTION_CUE_NONE) return;
  bool mode_changed = motion_cue_mode != mode;
  if (mode_changed || restart_pattern) {
    motion_cue_step = 0;
    motion_cue_next_ms = now_val;
  }
  if (mode_changed && sound_active && sound_owner == SOUND_OWNER_MANEUVER) {
    stop_sound_tone();
  }
  motion_cue_mode = mode;
  refresh_motion_cue(now_val);
}
static void start_sound_tone(int freq_hz, int duration_ms, int volume_pct = 100, uint8_t owner = SOUND_OWNER_COMMAND) {
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
  sound_owner = owner;
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
static void update_motion_cue(uint32_t now_val) {
  if (motion_cue_mode == MOTION_CUE_NONE) return;

  float remaining_deg = max_angle_delta_deg(
    (float)target_pan,
    (float)target_tilt,
    current_output_pan_deg,
    current_output_tilt_deg
  );
  if (remaining_deg > MOTION_CUE_SETTLE_DEG) {
    refresh_motion_cue(now_val);
  } else if ((int32_t)(now_val - motion_cue_keepalive_until_ms) >= 0) {
    stop_motion_cue(true);
    return;
  }

  if (sound_active) {
    return;
  }
  if ((int32_t)(now_val - motion_cue_next_ms) < 0) {
    return;
  }

  int freq = 0;
  int duration = 0;
  int gap = 0;
  if (motion_cue_mode == MOTION_CUE_WAKE) {
    static const int WAKE_FREQS[] = {760, 930, 1110, 1280};
    static const int WAKE_DURATIONS[] = {54, 60, 68, 84};
    static const int WAKE_GAPS[] = {28, 30, 34, 52};
    const uint8_t count = (uint8_t)(sizeof(WAKE_FREQS) / sizeof(WAKE_FREQS[0]));
    uint8_t idx = motion_cue_step % count;
    freq = WAKE_FREQS[idx];
    duration = WAKE_DURATIONS[idx];
    gap = WAKE_GAPS[idx];
    motion_cue_step = (uint8_t)((idx + 1U) % count);
  } else if (motion_cue_mode == MOTION_CUE_REST) {
    static const int REST_FREQS[] = {1240, 1040, 860, 690};
    static const int REST_DURATIONS[] = {62, 72, 84, 112};
    static const int REST_GAPS[] = {34, 38, 42, 64};
    const uint8_t count = (uint8_t)(sizeof(REST_FREQS) / sizeof(REST_FREQS[0]));
    uint8_t idx = motion_cue_step % count;
    freq = REST_FREQS[idx];
    duration = REST_DURATIONS[idx];
    gap = REST_GAPS[idx];
    motion_cue_step = (uint8_t)((idx + 1U) % count);
  } else {
    stop_motion_cue(false);
    return;
  }

  start_sound_tone(freq, duration, MOTION_CUE_VOLUME_PCT, SOUND_OWNER_MANEUVER);
  motion_cue_next_ms = now_val + (uint32_t)(duration + gap);
}

static bool start_wifi_ap() {
  WiFi.persistent(false);
  WiFi.setSleep(false);
  WiFi.mode(WIFI_AP);
  WiFi.softAPdisconnect(true);
  delay(20);
  WiFi.softAPConfig(AP_IP, AP_GW, AP_MASK);
  WiFi.setTxPower(WIFI_POWER_19_5dBm);
  bool wifi_ok = WiFi.softAP(WIFI_SSID, WIFI_PASS, AP_CHANNEL, AP_SSID_HIDDEN ? 1 : 0, AP_MAX_CONNECTIONS);
  delay(120);
  Serial.printf("[WIFI] AP '%s': %s IP=%s channel=%d hidden=%d clients=%d mac=%s\n",
                WIFI_SSID,
                wifi_ok ? "OK" : "FAILED",
                WiFi.softAPIP().toString().c_str(),
                WiFi.channel(),
                AP_SSID_HIDDEN ? 1 : 0,
                WiFi.softAPgetStationNum(),
                WiFi.softAPmacAddress().c_str());
  return wifi_ok;
}

static void ensure_wifi_ap_ready(uint32_t now_val) {
  if ((now_val - last_wifi_check_ms) < 2000) return;
  last_wifi_check_ms = now_val;

  bool ap_mode = (WiFi.getMode() & WIFI_AP) != 0;
  bool ip_ok = WiFi.softAPIP() == AP_IP;
  if (ap_mode && ip_ok) return;

  wifi_recover_count++;
  Serial.printf("[WIFI] AP supervisor recovery #%u mode=%d ip=%s\n",
                (unsigned)wifi_recover_count,
                (int)WiFi.getMode(),
                WiFi.softAPIP().toString().c_str());
  stop_sound_tone();
  Udp.stop();
  bool wifi_ok = start_wifi_ap();
  Udp.begin(UDP_PORT);
  Serial.printf("[WIFI] UDP restart after AP recovery: %s\n", wifi_ok ? "OK" : "FAILED");
}
static int clamped_home_pan()  { return clamp_int(home_cfg.pan,  limits_cfg.pan_min,  limits_cfg.pan_max);  }
static int clamped_home_tilt() { return clamp_int(home_cfg.tilt, limits_cfg.tilt_min, limits_cfg.tilt_max); }
static int clamped_rest_pan()  { return clamp_int(rest_cfg.pan,  limits_cfg.pan_min,  limits_cfg.pan_max);  }
static int clamped_rest_tilt() { return clamp_int(rest_cfg.tilt, 0, limits_cfg.tilt_max); }
static int read_current_mA(int pin, float scale) {
  if (pin < 0) return 0;
  return (int)(analogRead(pin) * scale);
}

static void clear_remote_endpoint() {
  last_remote_ip = IPAddress();
  last_remote_port = 0;
}

#if ENABLE_PIR_SUPPORT
static void reset_pir_runtime_state() {
  for (int i = 0; i < PIR_COUNT; i++) {
    pir_last_state[i] = (digitalRead(PIR_PINS[i]) == HIGH);
    pir_last_event_ms[i] = 0;
  }
}
#endif

static void enter_link_safe_mode(const char *reason) {
  if (link_safe_mode_active) return;

  link_safe_mode_active = true;
  stop_motion_cue(false);
  allow_rest_tilt_motion = false;
  safety_state = 1;
  fire_request = 0;
  fire_hold = false;
  fire_active = false;
  rapid_fire_active = false;
  led_state = 0;
  laser_state = 0;
  acc_state = 0;
  spare_state = 0;
  move_time_override_ms = 0;
  move_time_override_until_ms = 0;
  set_mosfet(false);
  set_trigger_servo_target(false);
  stop_sound_tone();
#if ENABLE_PIR_SUPPORT
  pir_enabled = false;
  reset_pir_runtime_state();
#endif
  clear_remote_endpoint();
  Serial.printf("[LINK] Safe mode engaged: %s\n", reason ? reason : "unspecified");
}

static void note_link_activity() {
  if (link_safe_mode_active) {
    link_safe_mode_active = false;
    Serial.println("[LINK] Client activity detected; leaving safe mode");
#if ENABLE_PIR_SUPPORT
    reset_pir_runtime_state();
#endif
  }
  last_cmd_ms = now_ms();
}

// ─────────────────────────────────────────────────────────────
// Command sweep
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
static void start_sweep_sequence(uint32_t now_val) {
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
static void finish_sweep_sequence() {
  sweep_active     = false;
  sweep_step_index = 0;
  sweep_step_initialized = false;
  target_pan  = clamped_home_pan();
  target_tilt = clamped_home_tilt();
  Serial.printf("[SWEEP] Complete -> home pan=%d tilt=%d\n", target_pan, target_tilt);
  status_led_enqueue_pattern(5);
}
static void update_sweep_sequence(uint32_t now_val) {
  if (!sweep_active) return;
  if (!sweep_step_initialized) {
    int sp = clamped_home_pan(), st = clamped_home_tilt();
    if (!get_sweep_step_target(sweep_step_index, &sp, &st)) {
      finish_sweep_sequence(); return;
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
  if (sweep_step_index >= SWEEP_STEP_COUNT) finish_sweep_sequence();
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
  int minDeg        = (id == BUS_ID_TILT) ? (allow_rest_tilt_motion ? 0 : limits_cfg.tilt_min) : limits_cfg.pan_min;
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
  int tilt = apply_invert_and_clamp(target_tilt, allow_rest_tilt_motion ? 0 : limits_cfg.tilt_min, limits_cfg.tilt_max, INVERT_TILT);
  uint32_t now    = now_ms();
  if (!motion_output_initialized) {
    current_output_pan_deg = (float)pan;
    current_output_tilt_deg = (float)tilt;
    motion_plan_pan = pan;
    motion_plan_tilt = tilt;
    motion_plan_time_ms = MOTION_PLAN_MIN_MS;
    motion_plan_started_ms = now;
    last_motion_update_ms = now;
    servo_write_deg(PIN_PAN_SERVO, pan);
    servo_write_deg(PIN_TILT_SERVO, tilt);
    last_sent_pan = pan;
    last_sent_tilt = tilt;
    last_bus_send_ms = now;
    motion_output_initialized = true;
    return;
  }

  bool target_changed = (pan != motion_plan_pan) || (tilt != motion_plan_tilt);
  if (target_changed) {
    int pan_delta = (int)lroundf((float)pan - current_output_pan_deg);
    int tilt_delta = (int)lroundf((float)tilt - current_output_tilt_deg);
    uint16_t pan_time = compute_move_time_ms(pan_delta);
    uint16_t tilt_time = compute_move_time_ms(tilt_delta);
    uint16_t sync_time = (pan_time > tilt_time) ? pan_time : tilt_time;
    if (sweep_active) {
      sync_time = SWEEP_MOVE_TIME_MS;
    } else if (move_time_override_ms > 0 && now <= move_time_override_until_ms) {
      sync_time = move_time_override_ms;
    }
    if (sync_time < MOTION_PLAN_MIN_MS) sync_time = MOTION_PLAN_MIN_MS;
    motion_plan_pan = pan;
    motion_plan_tilt = tilt;
    motion_plan_time_ms = sync_time;
    motion_plan_started_ms = now;
    Serial.printf("[MOTION] Plan pan %d->%d  tilt %d->%d  sync=%ums\n",
                  last_sent_pan, pan, last_sent_tilt, tilt, sync_time);
  } else if ((now - last_motion_update_ms) < MOTION_UPDATE_INTERVAL_MS) {
    return;
  }

  uint32_t elapsed_ms = now - last_motion_update_ms;
  if (elapsed_ms == 0) elapsed_ms = 1;
  last_motion_update_ms = now;

  current_output_pan_deg = step_toward_target(current_output_pan_deg, (float)motion_plan_pan, elapsed_ms, motion_plan_time_ms);
  current_output_tilt_deg = step_toward_target(current_output_tilt_deg, (float)motion_plan_tilt, elapsed_ms, motion_plan_time_ms);

  int out_pan = clamp_int((int)lroundf(current_output_pan_deg), limits_cfg.pan_min, limits_cfg.pan_max);
  int out_tilt = clamp_int((int)lroundf(current_output_tilt_deg), allow_rest_tilt_motion ? 0 : limits_cfg.tilt_min, limits_cfg.tilt_max);
  bool changed = (out_pan != last_sent_pan) || (out_tilt != last_sent_tilt);
  if (!changed) return;

  servo_write_deg(PIN_PAN_SERVO, out_pan);
  servo_write_deg(PIN_TILT_SERVO, out_tilt);
  last_sent_pan = out_pan;
  last_sent_tilt = out_tilt;
  last_bus_send_ms = now;
}
static void update_accessories() {
#if ACCESSORY_PWM_ENABLED
  if (acc_pwm_ready) {
    // PWM path: maps 0=off, 1=full-on compat, 2-255=literal duty cycle.
    auto acc_pwm_duty = [](int s) -> uint8_t {
      return (s <= 0) ? 0 : (s == 1) ? 255 : (uint8_t)s;
    };
    ledcWrite(PIN_LED_RELAY,   acc_pwm_duty(led_state));
    ledcWrite(PIN_LASER_RELAY, acc_pwm_duty(laser_state));
    ledcWrite(PIN_ACC_RELAY,   acc_pwm_duty(acc_state));
    ledcWrite(PIN_SPARE_RELAY, acc_pwm_duty(spare_state));
    return;
  }
  // Fall through to digital path if LEDC attach failed at boot.
#endif
  // Standard ON/OFF relay path.
  digitalWrite(PIN_LED_RELAY,   led_state   ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY, laser_state ? HIGH : LOW);
  digitalWrite(PIN_ACC_RELAY,   acc_state   ? HIGH : LOW);
  digitalWrite(PIN_SPARE_RELAY, spare_state ? HIGH : LOW);
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
    // Water (MOSFET pulse)
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
    // Single pulse
    if (!fire_active) {
      fire_active = true;
      last_mosfet_fire_start_ms = now_val;
      set_mosfet(true);
      Serial.println("[FIRE] MOSFET -> ON");
    } else if ((now_val - last_mosfet_fire_start_ms) > (uint32_t)trigger_cfg.mosfet_pulse_ms) {
      set_mosfet(false);
      fire_active = false;
      fire_request = 0;
      Serial.println("[FIRE] MOSFET -> OFF");
    }
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
  s["rest_pan"]      = clamped_rest_pan();
  s["rest_tilt"]     = clamped_rest_tilt();
  s["fire"]          = fire_active ? 1 : 0;
  s["safety"]        = safety_state; s["mode"]         = trigger_cfg.mode;
  s["current_fault"] = current_fault;
  s["control_source_mode"] = "app";
  s["control_source_active"] = "app";
  s["pan_mA_valid"]  = true;
  s["tilt_mA_valid"] = (PIN_CURR_TILT >= 0);
  s["total_mA_valid"] = (PIN_CURR_TOTAL >= 0);
#if ENABLE_PIR_SUPPORT
  s["pir_enabled"] = pir_enabled ? 1 : 0;
#endif
  encode_and_send(doc, ip, port);
}

static void send_caps(IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"] = 1; doc["t"] = "cap"; doc["seq"] = 0; doc["ts"] = (uint32_t)now_ms();
  JsonObject caps = doc["p"].to<JsonObject>();
  caps["proto"] = 1;
  caps["fw"]    = "smart-sentry-v2.3.1-esp32-udp-pir";
  caps["role"]  = "smart-sentry-v2.3.1-wifi-io";
  caps["manual_sweep_action"] = true;
  caps["rest_action"] = true;
  caps["rest_position_config"] = true;
  caps["sound_supported"] = true;
  caps["speaker_supported"] = false;
  caps["switch_supported"] = false;
  caps["current_pan_supported"] = true;
  caps["current_tilt_supported"] = (PIN_CURR_TILT >= 0);
  caps["current_total_supported"] = (PIN_CURR_TOTAL >= 0);
  caps["led_relay_assigned"] = true;
  caps["laser_relay_assigned"] = true;
  caps["trigger_servo_assigned"] = true;
#if ACCESSORY_PWM_ENABLED
  caps["accessory_pwm_enabled"] = acc_pwm_ready;
#else
  caps["accessory_pwm_enabled"] = false;
#endif
  caps["buzzer_volume_assigned"] = true;
  caps["speaker_volume_assigned"] = false;
  caps["header_reference_locked"] = false;
  caps["rc_input_supported"] = false;
  caps["rc_mode_supported"] = false;
  caps["rc_mode_default"] = "app";
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
  pins["boot_button"] = PIN_BOOT_BUTTON;
  encode_and_send(doc, ip, port);
  Serial.printf("[TX] Caps -> %s:%u\n", ip.toString().c_str(), port);
}

static void send_state(IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"] = 1; doc["t"] = "state"; doc["seq"] = 0; doc["ts"] = (uint32_t)now_ms();
  JsonObject s = doc["p"].to<JsonObject>();
  s["pan"]           = target_pan;  s["tilt"]         = target_tilt;
  s["rest_pan"]      = clamped_rest_pan();
  s["rest_tilt"]     = clamped_rest_tilt();
  s["fire"]          = fire_active ? 1 : 0;
  s["safety"]        = safety_state; s["mode"]         = trigger_cfg.mode;
  s["current_fault"] = current_fault;
  s["pan_mA"]        = latest_pan_mA;
  s["tilt_mA"]       = latest_tilt_mA;
  s["total_mA"]      = latest_total_mA;
  s["pan_mA_valid"]  = true;
  s["tilt_mA_valid"] = (PIN_CURR_TILT >= 0);
  s["total_mA_valid"] = (PIN_CURR_TOTAL >= 0);
  s["control_source_mode"] = "app";
  s["control_source_active"] = "app";
#if ENABLE_PIR_SUPPORT
  s["pir_enabled"] = pir_enabled ? 1 : 0;
#endif
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
    if (!rest_cfg_explicit) {
      rest_cfg.pan = home_cfg.pan;
      rest_cfg.tilt = home_cfg.tilt;
    }
  }
  if (cfg.containsKey("rest")) {
    JsonObject r = cfg["rest"];
    rest_cfg.pan  = r["pan"]  | rest_cfg.pan;
    rest_cfg.tilt = r["tilt"] | rest_cfg.tilt;
    rest_cfg_explicit = true;
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
  allow_rest_tilt_motion = (payload["allow_rest_tilt"] | 0) != 0;
  bool blink_safety = false, blink_mode = false, blink_fire = false;
  bool blink_accessory = false, blink_motion = false;

  if (payload.containsKey("safety")) {
    int prev = safety_state;
    safety_state = payload["safety"];
    if (prev != safety_state) {
      blink_safety = true;
      Serial.printf("[CMD] safety: %d->%d (%s)\n", prev, safety_state,
                    safety_state == 0 ? "ARMED" : "LOCKED");
    }
  }
  if (payload.containsKey("led")) {
    int prev = led_state; led_state = payload["led"];
    if (prev != led_state) blink_accessory = true;
  }
  if (payload.containsKey("laser")) {
    int prev = laser_state; laser_state = payload["laser"];
    if (prev != laser_state) blink_accessory = true;
  }
  if (payload.containsKey("acc")) {
    int prev = acc_state; acc_state = payload["acc"];
    if (prev != acc_state) blink_accessory = true;
  }
  if (payload.containsKey("spare")) {
    int prev = spare_state; spare_state = payload["spare"];
    if (prev != spare_state) blink_accessory = true;
  }
  if (payload.containsKey("mode")) {
    int prev = trigger_cfg.mode; trigger_cfg.mode = payload["mode"];
    if (prev != trigger_cfg.mode) blink_mode = true;
  }
  if (payload.containsKey("fire_hold")) {
    bool prev = fire_hold; fire_hold = payload["fire_hold"];
    if (prev != fire_hold) blink_fire = true;
  }
  if (payload.containsKey("fire")) {
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
  if (payload.containsKey("pan_cmd"))
    target_pan  = payload["pan_cmd"];
  else if (payload.containsKey("pan"))
    target_pan  = (int)(payload["pan"].as<float>() + 0.5f);
  if (payload.containsKey("tilt_cmd"))
    target_tilt = payload["tilt_cmd"];
  else if (payload.containsKey("tilt"))
    target_tilt = (int)(payload["tilt"].as<float>() + 0.5f);

  target_pan  = clamp_int(target_pan,  limits_cfg.pan_min,  limits_cfg.pan_max);
  target_tilt = clamp_int(target_tilt, allow_rest_tilt_motion ? 0 : limits_cfg.tilt_min, limits_cfg.tilt_max);

  if (payload.containsKey("move_time_ms")) {
    int mt = payload["move_time_ms"] | 0;
    mt = clamp_int(mt, 0, 5000);
    move_time_override_ms       = (uint16_t)mt;
    move_time_override_until_ms = now_ms() + 5000;
  }
  float output_pan = motion_output_initialized ? current_output_pan_deg : (float)prev_pan;
  float output_tilt = motion_output_initialized ? current_output_tilt_deg : (float)prev_tilt;
  float current_to_rest = max_angle_delta_deg(
    output_pan,
    output_tilt,
    (float)clamped_rest_pan(),
    (float)clamped_rest_tilt()
  );
  float target_to_rest = max_angle_delta_deg(
    (float)target_pan,
    (float)target_tilt,
    (float)clamped_rest_pan(),
    (float)clamped_rest_tilt()
  );
  float command_delta = max_angle_delta_deg(
    (float)prev_pan,
    (float)prev_tilt,
    (float)target_pan,
    (float)target_tilt
  );
  uint32_t command_now = now_ms();
  bool rest_like_move =
    allow_rest_tilt_motion &&
    current_to_rest > MOTION_CUE_REST_NEAR_DEG &&
    (target_to_rest + 0.75f) < current_to_rest &&
    command_delta >= MOTION_CUE_START_MIN_DELTA_DEG;
  bool wake_like_move =
    !allow_rest_tilt_motion &&
    current_to_rest <= MOTION_CUE_REST_NEAR_DEG &&
    target_to_rest >= (current_to_rest + 1.0f) &&
    command_delta >= MOTION_CUE_START_MIN_DELTA_DEG;
  if (rest_like_move) {
    start_motion_cue(MOTION_CUE_REST, command_now, motion_cue_mode != MOTION_CUE_REST);
  } else if (wake_like_move) {
    start_motion_cue(MOTION_CUE_WAKE, command_now, motion_cue_mode != MOTION_CUE_WAKE);
  } else if (motion_cue_mode != MOTION_CUE_NONE && command_delta >= 0.25f) {
    refresh_motion_cue(command_now);
  }
  if (target_pan != prev_pan || target_tilt != prev_tilt) {
    blink_motion = true;
    Serial.printf("[CMD] pos: pan %d->%d  tilt %d->%d\n",
                  prev_pan, target_pan, prev_tilt, target_tilt);
  }
  if (payload.containsKey("rapid_fire")) {
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
      } else if (strcmp(action, "sound") == 0) {
        int freq_hz = payload["freq_hz"] | payload["freq"] | 1200;
        int duration_ms = payload["duration_ms"] | 60;
        int volume_pct = payload["volume_pct"] | 100;
        start_sound_tone(freq_hz, duration_ms, volume_pct, SOUND_OWNER_COMMAND);
        send_ack(seq, true, ip, port);
      } else if (strcmp(action, "rest") == 0) {
        allow_rest_tilt_motion = true;
        target_pan = clamped_rest_pan();
        target_tilt = clamped_rest_tilt();
        start_motion_cue(MOTION_CUE_REST, now_ms(), true);
        send_ack(seq, true, ip, port);
      } else if (strcmp(action, "sweep") == 0) {
        start_sweep_sequence(now_ms());
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
  Serial.printf("  MOSFET      GPIO%d\n",           PIN_TRIGGER_MOSFET);
  Serial.printf("  LED_RELAY   GPIO%d\n",           PIN_LED_RELAY);
  Serial.printf("  LASER_RELAY GPIO%d\n",           PIN_LASER_RELAY);
  Serial.printf("  BUZZER      GPIO%d\n",           PIN_BUZZER);
  Serial.printf("  BOOT_BTN    GPIO%d  reserved for boot strap only\n", PIN_BOOT_BUTTON);
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
  Serial.println("  SMART_SENTRY_V2_3_1_ESP32_UDP_PIR  v2.3.1");
  Serial.println("  WiFi/UDP control + PIR blind-spot sensors + app sweep action");
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
#if ACCESSORY_PWM_ENABLED
  // Attach LEDC PWM channels for all four accessory outputs.
  {
    bool ok_led   = ledcAttach(PIN_LED_RELAY,   ACCESSORY_PWM_FREQ_HZ, ACCESSORY_PWM_BITS);
    bool ok_laser = ledcAttach(PIN_LASER_RELAY, ACCESSORY_PWM_FREQ_HZ, ACCESSORY_PWM_BITS);
    bool ok_acc   = ledcAttach(PIN_ACC_RELAY,   ACCESSORY_PWM_FREQ_HZ, ACCESSORY_PWM_BITS);
    bool ok_spare = ledcAttach(PIN_SPARE_RELAY, ACCESSORY_PWM_FREQ_HZ, ACCESSORY_PWM_BITS);
    acc_pwm_ready = ok_led && ok_laser && ok_acc && ok_spare;
    Serial.printf("[BOOT] Accessory PWM attach: LED=%s LASER=%s ACC=%s SPARE=%s -> %s\n",
                  ok_led   ? "OK" : "FAIL",
                  ok_laser ? "OK" : "FAIL",
                  ok_acc   ? "OK" : "FAIL",
                  ok_spare ? "OK" : "FAIL",
                  acc_pwm_ready ? "ALL OK" : "PARTIAL/FAIL - PWM mode disabled");
    if (!acc_pwm_ready) {
      // If any channel failed, release the ones that succeeded and fall back
      // to plain digital output so the accessory pins remain functional.
      pinMode(PIN_LED_RELAY,   OUTPUT); digitalWrite(PIN_LED_RELAY,   LOW);
      pinMode(PIN_LASER_RELAY, OUTPUT); digitalWrite(PIN_LASER_RELAY, LOW);
      pinMode(PIN_ACC_RELAY,   OUTPUT); digitalWrite(PIN_ACC_RELAY,   LOW);
      pinMode(PIN_SPARE_RELAY, OUTPUT); digitalWrite(PIN_SPARE_RELAY, LOW);
    }
  }
#endif
  pinMode(PIN_BUZZER,         OUTPUT); digitalWrite(PIN_BUZZER,         LOW);
  pinMode(PIN_STATUS_LED,     OUTPUT); set_status_led(false);
  trigger_servo_current_deg = (float)TRIGGER_SERVO_REST_DEG_DEFAULT;
  trigger_servo_target_deg = (float)TRIGGER_SERVO_REST_DEG_DEFAULT;
  trigger_servo_last_step_ms = millis();

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
  bool wifi_ok = start_wifi_ap();

  // UDP
  Udp.begin(UDP_PORT);
  Serial.printf("[BOOT] UDP port %u ready\n", UDP_PORT);

  if (wifi_ok) {
    start_sound_tone(1560, 90, 70);
  }

  current_output_pan_deg = (float)target_pan;
  current_output_tilt_deg = (float)target_tilt;
  motion_plan_pan = target_pan;
  motion_plan_tilt = target_tilt;
  motion_plan_time_ms = MOTION_PLAN_MIN_MS;
  motion_plan_started_ms = now_ms();
  last_motion_update_ms = motion_plan_started_ms;

  last_cmd_ms = now_ms();
  link_safe_mode_active = false;
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

  if ((now - last_cmd_ms) > LINK_IDLE_SAFE_TIMEOUT_MS) {
    enter_link_safe_mode("app inactivity timeout");
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
      note_link_activity();
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

  update_sweep_sequence(now);
  update_motion_outputs(motion_blocked);
  update_accessories();
  update_fire_outputs(now, fire_blocked);
  update_trigger_servo_motion(now);
  update_sound_output(now);
  update_motion_cue(now);
  ensure_wifi_ap_ready(now);

#if ENABLE_PIR_SUPPORT
  update_pir_sensors(now);
#endif

  if (WiFi.softAPgetStationNum() <= 0 && !link_safe_mode_active) {
    enter_link_safe_mode("no WiFi stations connected");
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
                  "heap=%u safety=%d fire=%d pan=%d tilt=%d wifi_clients=%d wifi_recovers=%u",
                  now / 1000, cmd_count, bus_send_count,
                  crc_fail_count, parse_fail_count,
                  ESP.getFreeHeap(), safety_state,
                  fire_request, target_pan, target_tilt,
                  WiFi.softAPgetStationNum(), (unsigned)wifi_recover_count);
#if ENABLE_PIR_SUPPORT
    Serial.printf(" pir=%s", pir_enabled ? "on" : "off");
#endif
    Serial.println();
  }

  delay(1);
}
