// DB3000_ESP32_UDP_PIR — v1
// =============================================================
// Combined firmware: WiFi/UDP turret control + PIR blind-spot sensors
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
static const int PIN_LED_RELAY      = 32;   // LED relay
static const int PIN_LASER_RELAY    = 33;   // Laser relay
static const int PIN_ACC_RELAY      = 25;   // Accessory relay
static const int PIN_SPARE_RELAY    = 26;   // Spare relay
static const int PIN_SWEEP_BUTTON   = 0;    // DevKit BOOT button (active LOW)

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
#ifdef LED_BUILTIN
static const int PIN_STATUS_LED = LED_BUILTIN;
#else
static const int PIN_STATUS_LED = 2;
#endif

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
static const int      TRIGGER_SERVO_REST_DEG = 0;
static const int      TRIGGER_SERVO_FIRE_DEG = 40;
static const uint32_t TRIGGER_PULSE_MS       = 120;

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

static uint32_t trip_start_ms  = 0;
static bool     current_fault  = false;

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
  digitalWrite(PIN_STATUS_LED, HIGH);
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
    digitalWrite(PIN_STATUS_LED, LOW);
    blink_led_on = false;
    blink_pulses_remaining--;
    blink_next_toggle_ms = now_val + (uint32_t)blink_off_ms;
  } else {
    if (blink_pulses_remaining > 0) {
      digitalWrite(PIN_STATUS_LED, HIGH);
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
static int clamped_home_pan()  { return clamp_int(home_cfg.pan,  limits_cfg.pan_min,  limits_cfg.pan_max);  }
static int clamped_home_tilt() { return clamp_int(home_cfg.tilt, limits_cfg.tilt_min, limits_cfg.tilt_max); }
static int read_current_mA(int pin, float scale) {
  if (pin < 0) return 0;
  return (int)(analogRead(pin) * scale);
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
  if (pin == PIN_TRIGGER_SERVO && !ensure_trigger_servo_pwm_ready()) return;
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
  set_bus_servo_angle(BUS_ID_PAN,  pan,  pan_time);
  set_bus_servo_angle(BUS_ID_TILT, tilt, tilt_time);
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
static void trigger_servo_fire(bool on) {
  servo_write_deg(PIN_TRIGGER_SERVO, on ? TRIGGER_SERVO_FIRE_DEG : TRIGGER_SERVO_REST_DEG);
}
static void update_fire_outputs(uint32_t now_val, bool blocked) {
  if (blocked) {
    fire_active = rapid_fire_active = false;
    set_mosfet(false); trigger_servo_fire(false);
    return;
  }
  if (!fire_request) {
    fire_active = rapid_fire_active = false;
    set_mosfet(false); trigger_servo_fire(false);
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
    trigger_servo_fire(true);
    Serial.println("[FIRE] Trigger servo -> FIRE");
  } else if ((now_val - last_fire_start_ms) > TRIGGER_PULSE_MS) {
    trigger_servo_fire(false);
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
        status_led_enqueue_pattern(6);
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
  encode_and_send(doc, ip, port);
}

static void send_caps(IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"] = 1; doc["t"] = "cap"; doc["seq"] = 0; doc["ts"] = (uint32_t)now_ms();
  JsonObject caps = doc["p"].to<JsonObject>();
  caps["proto"] = 1;
  caps["fw"]    = "db3000-esp32-udp-pir-v1";
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
  pins["led"]     = PIN_LED_RELAY;      pins["laser"] = PIN_LASER_RELAY;
  pins["acc"]     = PIN_ACC_RELAY;      pins["spare"] = PIN_SPARE_RELAY;
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
  }
  if (cfg.containsKey("trigger")) {
    JsonObject t = cfg["trigger"];
    trigger_cfg.mode       = t["mode"]       | trigger_cfg.mode;
    trigger_cfg.cooldown_s = t["cooldown_s"] | trigger_cfg.cooldown_s;
    trigger_cfg.max_fire_s = t["max_fire_s"] | trigger_cfg.max_fire_s;
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
  target_tilt = clamp_int(target_tilt, limits_cfg.tilt_min, limits_cfg.tilt_max);

  if (payload.containsKey("move_time_ms")) {
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
  Serial.printf("  STATUS_LED  GPIO%d\n",           PIN_STATUS_LED);
  Serial.printf("  UART2_RX    GPIO%d  %s\n",       PIN_UART_RX,  (PIN_UART_RX  == 16) ? "DEFAULT" : "NON-DEFAULT");
  Serial.printf("  UART2_TX    GPIO%d  %s\n",       PIN_UART_TX,  (PIN_UART_TX  == 17) ? "DEFAULT" : "NON-DEFAULT");
  Serial.printf("  MOSFET      GPIO%d\n",           PIN_TRIGGER_MOSFET);
  Serial.printf("  LED_RELAY   GPIO%d\n",           PIN_LED_RELAY);
  Serial.printf("  LASER_RELAY GPIO%d\n",           PIN_LASER_RELAY);
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
  Serial.println("[TEST] 5/5 Bus servo home (Pan=90 Tilt=40)");
  set_bus_servo_angle(BUS_ID_PAN,  90, 500); delay(100);
  set_bus_servo_angle(BUS_ID_TILT, 40, 500); delay(600);
  int pan_mA = read_current_mA(PIN_CURR_PAN, PAN_MA_PER_ADC);
  Serial.printf("[TEST] Pan current: %dmA\n", pan_mA);
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
  Serial.println("  DB3000_ESP32_UDP_PIR  v1");
  Serial.println("  WiFi/UDP control + PIR blind-spot sensors");
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
  pinMode(PIN_STATUS_LED,     OUTPUT); digitalWrite(PIN_STATUS_LED,     LOW);
  pinMode(PIN_SWEEP_BUTTON,   INPUT_PULLUP);

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
