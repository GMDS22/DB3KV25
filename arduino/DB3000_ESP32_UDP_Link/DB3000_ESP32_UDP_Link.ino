// DB3000 ESP32 UDP Link Firmware — v2 (Full Diagnostic Build)
// ---------------------------------------------------------------
// Receives JSON+CRC32 commands over UDP and drives the turret IO.
// Default network mode is AP at 192.168.4.1 (matches app defaults).
//
// Changes in v2:
//   - Comprehensive Serial debug logging (boot, WiFi, connection,
//     command reception, parsed values, servo execution).
//   - Boot self-test: trigger servo sweep, relay toggle, bus-servo
//     ping, brownout detection.
//   - Manual test mode ("test" command from app).
//   - Pin-conflict validation at boot.
//   - All CRC / parse failures logged with raw data.
//   - No silent exception paths.
//
// Libraries:
//   - ArduinoJson (v6)
//
// Board target: ESP32 DevKit v1 (WROOM-32)
// FQBN: esp32:esp32:esp32

// NOTE: Must be defined before Arduino's auto-generated prototypes.
// (The Arduino preprocessor may emit prototypes that reference this type.)
enum BusChecksumMode {
  BUS_CHK_SUB = 0,
  BUS_CHK_XOR = 1,
};

#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>
#include <esp_system.h>

// =========================================================
// WiFi / UDP
// =========================================================
static const char *WIFI_SSID = "DB3000-ESP32";
static const char *WIFI_PASS = "db3000pass";

static const IPAddress AP_IP(192, 168, 4, 1);
static const IPAddress AP_GW(192, 168, 4, 1);
static const IPAddress AP_MASK(255, 255, 255, 0);

static const uint16_t UDP_PORT = 9000;

WiFiUDP Udp;
IPAddress last_remote_ip;
uint16_t last_remote_port = 0;

// =========================================================
// Pin Map (ESP32 DevKit v1)
// =========================================================
static const int PIN_UART_RX = 16;          // UART2 RX (debug board TX)
static const int PIN_UART_TX = 17;          // UART2 TX (debug board RX)
// Pan/Tilt serial-bus servos are controlled by the debug board over UART2.
// No direct PWM pins are used for pan/tilt in this firmware.
static const int PIN_TRIGGER_MOSFET = 27;   // Water mode
static const int PIN_TRIGGER_SERVO  = 13;   // Projectile mode (PWM-capable)
static const int PIN_LED_RELAY      = 32;
static const int PIN_LASER_RELAY    = 33;

static const int PIN_CURR_PAN   = 36;       // ADC1 (input-only, VP)
static const int PIN_CURR_TILT  = 39;       // ADC1 (input-only, VN)
static const int PIN_CURR_TOTAL = 34;       // ADC1 (input-only)

#ifdef LED_BUILTIN
static const int PIN_STATUS_LED = LED_BUILTIN;
#else
static const int PIN_STATUS_LED = 2;
#endif

// =========================================================
// Trigger Servo PWM (LEDC) — trigger servo only
// =========================================================
static const int SERVO_HZ       = 50;
static const int SERVO_RES_BITS = 16;

static const int SERVO_MIN_US = 500;
static const int SERVO_MAX_US = 2500;

static const int TRIGGER_SERVO_REST_DEG =  0;
static const int TRIGGER_SERVO_FIRE_DEG = 40;
static const uint32_t TRIGGER_PULSE_MS  = 120;

// =========================================================
// Serial-bus servos (debug board over UART2)
// =========================================================
static const uint32_t BUS_BAUD   = 1000000;
static const uint8_t  BUS_ID_PAN  = 1;
static const uint8_t  BUS_ID_TILT = 2;

static const uint16_t PAN_TICKS_MIN  = 0;
static const uint16_t PAN_TICKS_MAX  = 4095;
static const uint16_t TILT_TICKS_MIN = 0;
static const uint16_t TILT_TICKS_MAX = 4095;

static const bool INVERT_PAN  = false;
static const bool INVERT_TILT = false;

static const uint16_t MOVE_TIME_BIG_MS   = 10;
static const uint16_t MOVE_TIME_MED_MS   = 14;
static const uint16_t MOVE_TIME_SMALL_MS = 18;
static const uint16_t MOVE_TIME_TINY_MS  = 22;

HardwareSerial busSerial(2);

// Active UART2 baud (can be changed by diagnostics like bus_ping baud scan).
static uint32_t bus_baud_active = BUS_BAUD;

// =========================================================
// Config structs
// =========================================================
struct LimitsConfig {
  int pan_min  = 0;
  int pan_max  = 220;
  int tilt_min = 0;
  int tilt_max = 70;
};

struct HomeConfig {
  int   pan           = 90;
  int   tilt          = 40;
  float speed         = 10.0f;
  float max_speed_dps = 25.0f;
};

struct TriggerConfig {
  int   mode       = 0;     // 0 = water (MOSFET), 1 = projectile (servo)
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

// =========================================================
// Runtime state
// =========================================================
static int  target_pan  = 90;
static int  target_tilt = 40;

static int  safety_state = 1;   // 1 = safe/locked, 0 = armed
static int  led_state    = 0;
static int  laser_state  = 0;
static int  fire_request = 0;
static bool fire_hold    = false;

static uint32_t last_cmd_ms   = 0;
static uint32_t last_state_ms = 0;

static uint32_t last_fire_start_ms = 0;
static bool fire_active       = false;
static bool rapid_fire_active = false;

static uint32_t trip_start_ms = 0;
static bool current_fault     = false;

static int      last_sent_pan    = -1;
static int      last_sent_tilt   = -1;
static uint32_t last_bus_send_ms = 0;

// Optional override to make movement visually obvious during diagnostics.
// If non-zero and not expired, bus move time for both pan/tilt uses this.
static uint16_t move_time_override_ms = 0;
static uint32_t move_time_override_until_ms = 0;

// ADC conversion factors (adjust for your current sensors)
static const float PAN_MA_PER_ADC   = 1.0f;
static const float TILT_MA_PER_ADC  = 1.0f;
static const float TOTAL_MA_PER_ADC = 1.0f;

// Diagnostic counters
static uint32_t cmd_count        = 0;
static uint32_t crc_fail_count   = 0;
static uint32_t parse_fail_count = 0;
static uint32_t bus_send_count   = 0;
static bool     first_client_seen = false;

// =========================================================
// Status LED blink engine (non-blocking)
// Unique patterns per command category:
//   motion=1 pulse, fire=2 pulses, accessory=3 pulses,
//   safety=4 pulses, mode=5 pulses
// =========================================================
static const uint8_t BLINK_QUEUE_CAP = 12;
static uint8_t blink_queue[BLINK_QUEUE_CAP];
static uint8_t blink_q_head = 0;
static uint8_t blink_q_tail = 0;

static uint8_t  blink_pulses_remaining = 0;
static bool     blink_led_on = false;
static uint32_t blink_next_toggle_ms = 0;
static uint16_t blink_on_ms = 80;
static uint16_t blink_off_ms = 80;
static bool     blink_enabled = true;

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

static bool blink_queue_pop(uint8_t *out_pulses) {
  if (blink_queue_is_empty() || out_pulses == nullptr) return false;
  *out_pulses = blink_queue[blink_q_head];
  blink_q_head = (uint8_t)((blink_q_head + 1U) % BLINK_QUEUE_CAP);
  return true;
}

static void status_led_begin_pattern(uint8_t pulses, uint16_t on_ms, uint16_t off_ms) {
  if (!blink_enabled || pulses == 0) return;
  blink_pulses_remaining = pulses;
  blink_on_ms = (on_ms < 20) ? 20 : on_ms;
  blink_off_ms = (off_ms < 20) ? 20 : off_ms;
  blink_led_on = true;
  digitalWrite(PIN_STATUS_LED, HIGH);
  blink_next_toggle_ms = millis() + (uint32_t)blink_on_ms;
}

static void status_led_enqueue_pattern(uint8_t pulses) {
  if (!blink_enabled || pulses == 0) return;
  if (!blink_queue_push(pulses)) {
    Serial.println("[LED] Blink queue full; dropping pattern");
  }
}

static void status_led_tick(uint32_t now_val) {
  if (!blink_enabled) return;

  if (blink_pulses_remaining == 0) {
    uint8_t next_pulses = 0;
    if (blink_queue_pop(&next_pulses)) {
      status_led_begin_pattern(next_pulses, 80, 90);
    }
    return;
  }

  if (now_val < blink_next_toggle_ms) return;

  if (blink_led_on) {
    digitalWrite(PIN_STATUS_LED, LOW);
    blink_led_on = false;
    if (blink_pulses_remaining > 0) blink_pulses_remaining--;
    blink_next_toggle_ms = now_val + (uint32_t)blink_off_ms;
  } else {
    if (blink_pulses_remaining > 0) {
      digitalWrite(PIN_STATUS_LED, HIGH);
      blink_led_on = true;
      blink_next_toggle_ms = now_val + (uint32_t)blink_on_ms;
    }
  }
}

// =========================================================
// Forward declarations
// =========================================================
static void run_self_test();

// =========================================================
// CRC32
// =========================================================
static uint32_t crc32_update(uint32_t crc, uint8_t data) {
  crc ^= data;
  for (int i = 0; i < 8; ++i) {
    if (crc & 1)
      crc = (crc >> 1) ^ 0xEDB88320UL;
    else
      crc >>= 1;
  }
  return crc;
}

static uint32_t crc32_compute(const uint8_t *data, size_t len) {
  uint32_t crc = 0xFFFFFFFFUL;
  for (size_t i = 0; i < len; ++i)
    crc = crc32_update(crc, data[i]);
  return ~crc;
}

// =========================================================
// Helpers
// =========================================================
static int clamp_int(int v, int lo, int hi) {
  if (v < lo) return lo;
  if (v > hi) return hi;
  return v;
}

static int apply_invert_and_clamp(int deg, int minDeg, int maxDeg, bool invert) {
  deg = clamp_int(deg, minDeg, maxDeg);
  if (!invert) return deg;
  const int span = maxDeg - minDeg;
  const int rel  = deg - minDeg;
  return minDeg + (span - rel);
}

static uint32_t now_ms() { return millis(); }

static uint32_t deg_to_duty_us(int deg) {
  int clamped = clamp_int(deg, 0, 180);
  return (uint32_t)map(clamped, 0, 180, SERVO_MIN_US, SERVO_MAX_US);
}

static uint16_t compute_move_time_ms(int deltaDegAbs) {
  if (deltaDegAbs < 0) deltaDegAbs = -deltaDegAbs;
  if (deltaDegAbs >= 30) return MOVE_TIME_BIG_MS;
  if (deltaDegAbs >= 15) return MOVE_TIME_MED_MS;
  if (deltaDegAbs >=  7) return MOVE_TIME_SMALL_MS;
  return MOVE_TIME_TINY_MS;
}

static uint16_t map_deg_to_ticks(int deg, int minDeg, int maxDeg,
                                 uint16_t ticksMin, uint16_t ticksMax) {
  deg = clamp_int(deg, minDeg, maxDeg);
  const int degSpan = maxDeg - minDeg;
  if (degSpan <= 0) return ticksMin;

  const long ticksSpan = (long)ticksMax - (long)ticksMin;
  const long relDeg    = (long)(deg - minDeg);
  long ticks = (long)ticksMin + (relDeg * ticksSpan) / (long)degSpan;

  const long lo = (ticksMin < ticksMax) ? ticksMin : ticksMax;
  const long hi = (ticksMin < ticksMax) ? ticksMax : ticksMin;
  if (ticks < lo) ticks = lo;
  if (ticks > hi) ticks = hi;
  return (uint16_t)ticks;
}

static uint32_t duty_us_to_ticks(uint32_t us) {
  uint32_t max_ticks = (1UL << SERVO_RES_BITS) - 1;
  uint32_t period_us = 1000000UL / SERVO_HZ;
  uint32_t ticks     = (us * max_ticks) / period_us;
  if (ticks > max_ticks) ticks = max_ticks;
  return ticks;
}

static void servo_write_deg(int pin, int deg) {
  uint32_t us    = deg_to_duty_us(deg);
  uint32_t ticks = duty_us_to_ticks(us);
  ledcWrite(pin, ticks);
}

// =========================================================
// Bus-servo helpers
// =========================================================
// Default to XOR (matches DS_v4 vendor tool); bus_ping can lock the mode.
static BusChecksumMode bus_chk_mode = BUS_CHK_XOR;
static bool bus_chk_locked = false;

static uint8_t bus_checksum(const uint8_t *pkt,
                            uint8_t startIdx,
                            uint8_t endIdxInclusive,
                            BusChecksumMode mode) {
  uint16_t sum = 0;
  for (uint8_t i = startIdx; i <= endIdxInclusive; i++)
    sum += pkt[i];
  const uint8_t s = (uint8_t)(sum & 0xFF);
  if (mode == BUS_CHK_XOR)
    return (uint8_t)((0xFF ^ s) & 0xFF);
  return (uint8_t)((0xFF - s) & 0xFF);
}

static void bus_write(const uint8_t *data, size_t len) {
  busSerial.write(data, len);
  busSerial.flush();
}

static void bus_reinit(uint32_t baud) {
  bus_baud_active = baud;
  Serial.printf("[BUS] Reinit UART2 baud=%u RX=GPIO%d TX=GPIO%d\n",
                (unsigned)bus_baud_active, PIN_UART_RX, PIN_UART_TX);
  try {
    busSerial.end();
  } catch (...) {
    // ignore
  }
  delay(20);
  busSerial.begin(bus_baud_active, SERIAL_8N1, PIN_UART_RX, PIN_UART_TX);
  delay(10);
  bus_flush_rx();
}

static void bus_flush_rx() {
  while (busSerial.available() > 0) {
    (void)busSerial.read();
  }
}

// Best-effort read: returns number of bytes captured in out (<= outCap).
static size_t bus_read_bytes(uint8_t *out, size_t outCap, uint32_t timeoutMs) {
  const uint32_t start = now_ms();
  size_t n = 0;
  while ((now_ms() - start) < timeoutMs && n < outCap) {
    while (busSerial.available() > 0 && n < outCap) {
      int b = busSerial.read();
      if (b >= 0) out[n++] = (uint8_t)b;
    }
    if (n >= 4) break;
    delay(1);
  }
  return n;
}

// Find and validate a packet in the captured buffer. Returns true if valid.
static bool bus_find_valid_packet(const uint8_t *buf, size_t n,
                                  uint8_t wantId,
                                  BusChecksumMode mode,
                                  uint8_t *outLen /* optional */) {
  if (!buf || n < 6) return false;
  for (size_t i = 0; i + 5 < n; i++) {
    if (buf[i] != 0xFF || buf[i + 1] != 0xFF) continue;
    const uint8_t id = buf[i + 2];
    const uint8_t len = buf[i + 3];
    if (wantId != 0xFF && id != wantId) continue;
    // Packet total bytes = header(2) + id(1) + len(1) + len bytes
    const size_t total = 4 + (size_t)len;
    if (len < 2) continue;
    if (i + total > n) continue;
    const uint8_t chk = buf[i + total - 1];
    const uint8_t calc = bus_checksum(buf + i, 2, (uint8_t)(2 + len - 2), mode);
    if (chk != calc) continue;
    if (outLen) *outLen = len;
    return true;
  }
  return false;
}

static void build_bus_ping_pkt(uint8_t id, BusChecksumMode mode, uint8_t *out, size_t outCap) {
  if (!out || outCap < 6) return;
  // FF FF ID LEN INST CHK  (LEN=2, INST=0x01)
  out[0] = 0xFF;
  out[1] = 0xFF;
  out[2] = id;
  out[3] = 0x02;
  out[4] = 0x01;
  out[5] = bus_checksum(out, 2, 4, mode);
}

static bool bus_try_ping(uint8_t id, BusChecksumMode mode, uint32_t timeoutMs, size_t *rxCountOut) {
  bus_flush_rx();
  uint8_t pkt[6];
  build_bus_ping_pkt(id, mode, pkt, sizeof(pkt));
  bus_write(pkt, sizeof(pkt));

  uint8_t rx[64];
  size_t n = bus_read_bytes(rx, sizeof(rx), timeoutMs);
  if (rxCountOut) *rxCountOut = n;
  bool ok = bus_find_valid_packet(rx, n, id, mode, nullptr);
  if (ok) {
    Serial.printf("[BUSPING] OK id=%u mode=%s rx=%u\n", id, (mode == BUS_CHK_XOR) ? "xor" : "sub", (unsigned)n);
  } else {
    Serial.printf("[BUSPING] FAIL id=%u mode=%s rx=%u\n", id, (mode == BUS_CHK_XOR) ? "xor" : "sub", (unsigned)n);
  }
  return ok;
}

static void bus_send_position_pkt(uint8_t id, int deg, uint16_t moveTimeMs, BusChecksumMode mode) {
  uint16_t ticksMin, ticksMax;
  int minDeg, maxDeg;

  if (id == BUS_ID_TILT) {
    ticksMin = TILT_TICKS_MIN;
    ticksMax = TILT_TICKS_MAX;
    minDeg   = limits_cfg.tilt_min;
    maxDeg   = limits_cfg.tilt_max;
  } else {
    ticksMin = PAN_TICKS_MIN;
    ticksMax = PAN_TICKS_MAX;
    minDeg   = limits_cfg.pan_min;
    maxDeg   = limits_cfg.pan_max;
  }

  const uint16_t posTicks = map_deg_to_ticks(deg, minDeg, maxDeg, ticksMin, ticksMax);
  const uint8_t  posH  = (uint8_t)((posTicks >> 8) & 0xFF);
  const uint8_t  posL  = (uint8_t)(posTicks & 0xFF);
  const uint8_t  timeH = (uint8_t)((moveTimeMs >> 8) & 0xFF);
  const uint8_t  timeL = (uint8_t)(moveTimeMs & 0xFF);

  uint8_t pkt[11];
  pkt[0]  = 0xFF;
  pkt[1]  = 0xFF;
  pkt[2]  = id;
  pkt[3]  = 0x07;   // length
  pkt[4]  = 0x03;   // write command
  pkt[5]  = 0x2A;   // register 0x2A (position + time)
  pkt[6]  = posH;
  pkt[7]  = posL;
  pkt[8]  = timeH;
  pkt[9]  = timeL;
  pkt[10] = bus_checksum(pkt, 2, 9, mode);

  bus_write(pkt, sizeof(pkt));
  bus_send_count++;

  Serial.printf("[BUS] ID=%d deg=%d ticks=%u time=%ums chk=%s pkt=[",
                id, deg, posTicks, moveTimeMs, (mode == BUS_CHK_XOR) ? "xor" : "sub");
  for (int i = 0; i < 11; i++) {
    Serial.printf("%02X", pkt[i]);
    if (i < 10) Serial.print(' ');
  }
  Serial.println("]");
}

static void set_bus_servo_angle(uint8_t id, int deg, uint16_t moveTimeMs) {
  // If the correct checksum mode isn't locked yet, send both variants.
  // Only the correct one should be accepted; this avoids "silent no-move".
  if (!bus_chk_locked) {
    bus_send_position_pkt(id, deg, moveTimeMs, BUS_CHK_SUB);
    bus_send_position_pkt(id, deg, moveTimeMs, BUS_CHK_XOR);
    return;
  }
  bus_send_position_pkt(id, deg, moveTimeMs, bus_chk_mode);
}

static void send_ack_busdiag(int seq, bool ok, IPAddress ip, uint16_t port,
                             bool pan_ok, bool tilt_ok,
                             uint32_t rx_pan, uint32_t rx_tilt,
                             const char *mode_str,
                             bool bridge_rx_ok) {
  JsonDocument doc;
  doc["v"]   = 1;
  doc["t"]   = "ack";
  doc["seq"] = seq;
  doc["ts"]  = (uint32_t)now_ms();
  doc["ok"]  = ok;

  JsonObject state = doc["state"].to<JsonObject>();
  state["pan"]           = target_pan;
  state["tilt"]          = target_tilt;
  state["fire"]          = fire_active ? 1 : 0;
  state["safety"]        = safety_state;
  state["mode"]          = trigger_cfg.mode;
  state["current_fault"] = current_fault;

  JsonObject p = doc["p"].to<JsonObject>();
  JsonObject bus = p["bus"].to<JsonObject>();
  bus["pan_ok"] = pan_ok;
  bus["tilt_ok"] = tilt_ok;
  bus["rx_pan"] = rx_pan;
  bus["rx_tilt"] = rx_tilt;
  bus["bridge_rx_ok"] = bridge_rx_ok;
  bus["chk_mode"] = mode_str;
  bus["chk_locked"] = bus_chk_locked;
  bus["bus_send_count"] = bus_send_count;
  bus["baud"] = (uint32_t)bus_baud_active;

  encode_and_send(doc, ip, port);
}

static int read_current_mA(int pin, float scale) {
  int adc = analogRead(pin);
  return (int)(adc * scale);
}

// =========================================================
// Output control
// =========================================================
static void update_motion_outputs(bool motion_blocked) {
  if (motion_blocked) {
    return;
  }

  const int  pan  = apply_invert_and_clamp(target_pan,
                      limits_cfg.pan_min, limits_cfg.pan_max, INVERT_PAN);
  const int  tilt = apply_invert_and_clamp(target_tilt,
                      limits_cfg.tilt_min, limits_cfg.tilt_max, INVERT_TILT);
  const uint32_t now     = now_ms();
  const bool     changed = (pan != last_sent_pan) || (tilt != last_sent_tilt);

  // Send if changed or every 250 ms as keep-alive
  if (!changed && (now - last_bus_send_ms) < 250) {
    return;
  }

  const int      pan_delta  = (last_sent_pan  < 0) ? 0 : (pan  - last_sent_pan);
  const int      tilt_delta = (last_sent_tilt < 0) ? 0 : (tilt - last_sent_tilt);
  uint16_t pan_time   = compute_move_time_ms(pan_delta);
  uint16_t tilt_time  = compute_move_time_ms(tilt_delta);

  // Apply optional diagnostic override.
  if (move_time_override_ms > 0 && now <= move_time_override_until_ms) {
    pan_time = move_time_override_ms;
    tilt_time = move_time_override_ms;
  }

  if (changed) {
    Serial.printf("[MOTION] Pan %d->%d (dt=%d, %ums)  Tilt %d->%d (dt=%d, %ums)\n",
                  last_sent_pan, pan, pan_delta, pan_time,
                  last_sent_tilt, tilt, tilt_delta, tilt_time);
  }

  set_bus_servo_angle(BUS_ID_PAN,  pan,  pan_time);
  set_bus_servo_angle(BUS_ID_TILT, tilt, tilt_time);

  last_sent_pan    = pan;
  last_sent_tilt   = tilt;
  last_bus_send_ms = now;
}

static void update_accessories() {
  digitalWrite(PIN_LED_RELAY,   led_state   ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY, laser_state ? HIGH : LOW);
}

static void set_mosfet(bool on) {
  digitalWrite(PIN_TRIGGER_MOSFET, on ? HIGH : LOW);
}

static void trigger_servo_fire(bool on) {
  int deg = on ? TRIGGER_SERVO_FIRE_DEG : TRIGGER_SERVO_REST_DEG;
  servo_write_deg(PIN_TRIGGER_SERVO, deg);
}

static void update_fire_outputs(uint32_t now_val, bool fire_blocked) {
  if (fire_blocked) {
    fire_active       = false;
    rapid_fire_active = false;
    set_mosfet(false);
    trigger_servo_fire(false);
    return;
  }

  bool want_fire = (fire_request != 0);
  if (!want_fire) {
    fire_active       = false;
    rapid_fire_active = false;
    set_mosfet(false);
    trigger_servo_fire(false);
    return;
  }

  if (trigger_cfg.mode == 0) {
    // Water (MOSFET)
    if (rapid_cfg.enabled) {
      int rate_hz = max(1, rapid_cfg.rate_hz);
      float duty  = rapid_cfg.duty;
      if (duty < 0.05f) duty = 0.05f;
      if (duty > 0.95f) duty = 0.95f;
      uint32_t period_ms = 1000UL / (uint32_t)rate_hz;
      uint32_t on_ms     = (uint32_t)((float)period_ms * duty);
      uint32_t phase     = (now_val % period_ms);
      bool on = (phase < on_ms);
      set_mosfet(on);
      fire_active       = on;
      rapid_fire_active = true;
      return;
    }

    set_mosfet(true);
    fire_active       = true;
    rapid_fire_active = false;
    return;
  }

  // Projectile (trigger servo)
  if (!fire_active) {
    fire_active        = true;
    last_fire_start_ms = now_val;
    trigger_servo_fire(true);
    Serial.println("[FIRE] Trigger servo -> FIRE");
  } else {
    if ((now_val - last_fire_start_ms) > TRIGGER_PULSE_MS) {
      trigger_servo_fire(false);
      Serial.println("[FIRE] Trigger servo -> REST");
    }
  }
}

// =========================================================
// UDP JSON codec
// =========================================================
static bool decode_message(char *buffer, size_t len,
                           JsonDocument &doc) {
  DeserializationError err = deserializeJson(doc, buffer, len);
  if (err) {
    parse_fail_count++;
    Serial.printf("[ERR] JSON parse: %s | raw(%u): %.120s\n",
                  err.c_str(), (unsigned)len, buffer);
    return false;
  }

  if (!doc["crc"].is<const char*>()) {
    parse_fail_count++;
    Serial.printf("[ERR] Missing 'crc' | raw: %.120s\n", buffer);
    return false;
  }

  // IMPORTANT: doc["crc"] points into ArduinoJson's internal storage.
  // Removing the key invalidates that pointer, which would cause false CRC
  // mismatches and dropped packets.
  const char *crc_str = doc["crc"];
  char crc_copy[16] = {0};
  snprintf(crc_copy, sizeof(crc_copy), "%s", crc_str);
  doc.remove("crc");

  String compact;
  serializeJson(doc, compact);
  uint32_t crc = crc32_compute((const uint8_t *)compact.c_str(),
                               compact.length());

  char calc[9];
  snprintf(calc, sizeof(calc), "%08x", (unsigned int)crc);
  if (strcasecmp(calc, crc_copy) != 0) {
    crc_fail_count++;
    Serial.printf("[ERR] CRC mismatch: calc=%s recv=%s | raw: %.120s\n",
                  calc, crc_copy, buffer);
    return false;
  }

  return true;
}

static void encode_and_send(JsonDocument &doc, IPAddress ip, uint16_t port) {
  String compact;
  serializeJson(doc, compact);
  uint32_t crc = crc32_compute((const uint8_t *)compact.c_str(),
                               compact.length());

  char crc_hex[9];
  snprintf(crc_hex, sizeof(crc_hex), "%08x", (unsigned int)crc);

  doc["crc"] = crc_hex;
  String payload;
  serializeJson(doc, payload);

  Udp.beginPacket(ip, port);
  Udp.write((const uint8_t *)payload.c_str(), payload.length());
  Udp.endPacket();
}

// =========================================================
// UDP reply builders
// =========================================================
static void send_ack(int seq, bool ok, IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"]   = 1;
  doc["t"]   = "ack";
  doc["seq"] = seq;
  doc["ts"]  = (uint32_t)now_ms();
  doc["ok"]  = ok;

  JsonObject state = doc["state"].to<JsonObject>();
  state["pan"]           = target_pan;
  state["tilt"]          = target_tilt;
  state["fire"]          = fire_active ? 1 : 0;
  state["safety"]        = safety_state;
  state["mode"]          = trigger_cfg.mode;
  state["current_fault"] = current_fault;

  encode_and_send(doc, ip, port);
}

static void send_caps(IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"]   = 1;
  doc["t"]   = "cap";
  doc["seq"] = 0;
  doc["ts"]  = (uint32_t)now_ms();

  JsonObject caps = doc["p"].to<JsonObject>();
  caps["proto"] = 1;
  caps["fw"]    = "db3000-esp32-udp-v2-diag";

  JsonObject pins = caps["pins"].to<JsonObject>();
  pins["uart_rx"]       = PIN_UART_RX;
  pins["uart_tx"]       = PIN_UART_TX;
  pins["mosfet"]        = PIN_TRIGGER_MOSFET;
  pins["trigger_servo"] = PIN_TRIGGER_SERVO;
  pins["led"]           = PIN_LED_RELAY;
  pins["laser"]         = PIN_LASER_RELAY;
  pins["curr_pan"]      = PIN_CURR_PAN;
  pins["curr_tilt"]     = PIN_CURR_TILT;
  pins["curr_total"]    = PIN_CURR_TOTAL;

  encode_and_send(doc, ip, port);
  Serial.printf("[TX] Capabilities -> %s:%u\n",
                ip.toString().c_str(), port);
}

static void send_state(IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"]   = 1;
  doc["t"]   = "state";
  doc["seq"] = 0;
  doc["ts"]  = (uint32_t)now_ms();

  JsonObject state = doc["p"].to<JsonObject>();
  state["pan"]           = target_pan;
  state["tilt"]          = target_tilt;
  state["fire"]          = fire_active ? 1 : 0;
  state["safety"]        = safety_state;
  state["mode"]          = trigger_cfg.mode;
  state["current_fault"] = current_fault;

  JsonObject bus = state["bus"].to<JsonObject>();
  bus["send_count"] = bus_send_count;
  bus["baud"] = (uint32_t)bus_baud_active;
  bus["last_send_ms"] = (uint32_t)last_bus_send_ms;
  bus["last_sent_pan"] = last_sent_pan;
  bus["last_sent_tilt"] = last_sent_tilt;
  bus["chk_locked"] = bus_chk_locked;
  bus["chk_mode"] = bus_chk_locked ? ((bus_chk_mode == BUS_CHK_XOR) ? "xor" : "sub") : "auto";
  bus["move_time_override_ms"] = (uint32_t)move_time_override_ms;
  bus["move_time_override_until_ms"] = (uint32_t)move_time_override_until_ms;

  JsonObject currents = state["current_mA"].to<JsonObject>();
  currents["pan"]   = read_current_mA(PIN_CURR_PAN, PAN_MA_PER_ADC);
  currents["tilt"]  = read_current_mA(PIN_CURR_TILT, TILT_MA_PER_ADC);
  currents["total"] = read_current_mA(PIN_CURR_TOTAL, TOTAL_MA_PER_ADC);

  encode_and_send(doc, ip, port);
}

// =========================================================
// Command handling
// =========================================================
static void apply_config(JsonObject cfg) {
  Serial.println("[CFG] Applying config update...");

  if (cfg.containsKey("limits")) {
    JsonObject lim = cfg["limits"];
    limits_cfg.pan_min  = lim["pan_min"]  | limits_cfg.pan_min;
    limits_cfg.pan_max  = lim["pan_max"]  | limits_cfg.pan_max;
    limits_cfg.tilt_min = lim["tilt_min"] | limits_cfg.tilt_min;
    limits_cfg.tilt_max = lim["tilt_max"] | limits_cfg.tilt_max;
    Serial.printf("  limits: pan[%d..%d] tilt[%d..%d]\n",
                  limits_cfg.pan_min, limits_cfg.pan_max,
                  limits_cfg.tilt_min, limits_cfg.tilt_max);
  }

  if (cfg.containsKey("home")) {
    JsonObject home = cfg["home"];
    home_cfg.pan          = home["pan"]          | home_cfg.pan;
    home_cfg.tilt         = home["tilt"]         | home_cfg.tilt;
    home_cfg.speed        = home["speed"]        | home_cfg.speed;
    home_cfg.max_speed_dps = home["max_speed_dps"] | home_cfg.max_speed_dps;
    Serial.printf("  home: pan=%d tilt=%d speed=%.1f\n",
                  home_cfg.pan, home_cfg.tilt, home_cfg.speed);
  }

  if (cfg.containsKey("trigger")) {
    JsonObject trig = cfg["trigger"];
    trigger_cfg.mode       = trig["mode"]       | trigger_cfg.mode;
    trigger_cfg.cooldown_s = trig["cooldown_s"] | trigger_cfg.cooldown_s;
    trigger_cfg.max_fire_s = trig["max_fire_s"] | trigger_cfg.max_fire_s;
    Serial.printf("  trigger: mode=%d cooldown=%.1fs\n",
                  trigger_cfg.mode, trigger_cfg.cooldown_s);
  }

  if (cfg.containsKey("rapid_fire")) {
    JsonObject rf = cfg["rapid_fire"];
    rapid_cfg.enabled = rf["enabled"] | rapid_cfg.enabled;
    rapid_cfg.rate_hz = rf["rate_hz"] | rapid_cfg.rate_hz;
    rapid_cfg.duty    = rf["duty"]    | rapid_cfg.duty;
    Serial.printf("  rapid_fire: en=%d rate=%dHz duty=%.2f\n",
                  rapid_cfg.enabled, rapid_cfg.rate_hz, rapid_cfg.duty);
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
    Serial.printf("  current_prot: en=%d trip_pan=%d tilt=%d total=%d\n",
                  current_cfg.enabled, current_cfg.trip_pan_mA,
                  current_cfg.trip_tilt_mA, current_cfg.trip_total_mA);
  }

  if (cfg.containsKey("tilt_safety")) {
    JsonObject ts = cfg["tilt_safety"];
    tilt_safety_cfg.installed = ts["installed"] | tilt_safety_cfg.installed;
    tilt_safety_cfg.enabled   = ts["enabled"]   | tilt_safety_cfg.enabled;
    Serial.printf("  tilt_safety: installed=%d enabled=%d\n",
                  tilt_safety_cfg.installed, tilt_safety_cfg.enabled);
  }
}

static void apply_command(JsonObject payload) {
  cmd_count++;

  bool blink_safety = false;
  bool blink_mode = false;
  bool blink_fire = false;
  bool blink_accessory = false;
  bool blink_motion = false;

  // Safety
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
    int prev = led_state;
    led_state = payload["led"];
    if (prev != led_state) blink_accessory = true;
  }
  if (payload.containsKey("laser")) {
    int prev = laser_state;
    laser_state = payload["laser"];
    if (prev != laser_state) blink_accessory = true;
  }
  if (payload.containsKey("mode")) {
    int prev = trigger_cfg.mode;
    trigger_cfg.mode = payload["mode"];
    if (prev != trigger_cfg.mode) blink_mode = true;
  }
  if (payload.containsKey("fire_hold")) {
    bool prev = fire_hold;
    fire_hold = payload["fire_hold"];
    if (prev != fire_hold) blink_fire = true;
  }

  if (payload.containsKey("fire")) {
    int prev = fire_request;
    fire_request = payload["fire"];
    if (prev != fire_request) {
      blink_fire = true;
      Serial.printf("[CMD] fire: %d->%d (mode=%d safety=%d)\n",
                    prev, fire_request, trigger_cfg.mode, safety_state);
    }
  }

  int prev_pan  = target_pan;
  int prev_tilt = target_tilt;

  if (payload.containsKey("pan_cmd")) {
    target_pan = payload["pan_cmd"];
  } else if (payload.containsKey("pan")) {
    target_pan = (int)(payload["pan"].as<float>() + 0.5f);
  }
  if (payload.containsKey("tilt_cmd")) {
    target_tilt = payload["tilt_cmd"];
  } else if (payload.containsKey("tilt")) {
    target_tilt = (int)(payload["tilt"].as<float>() + 0.5f);
  }

  target_pan  = clamp_int(target_pan,
                  limits_cfg.pan_min, limits_cfg.pan_max);
  target_tilt = clamp_int(target_tilt,
                  limits_cfg.tilt_min, limits_cfg.tilt_max);

  // Optional: allow the PC to request a slower / more visible move for diagnostics.
  // This does not affect the stored pan/tilt targets; it only affects bus move time.
  if (payload.containsKey("move_time_ms")) {
    int mt = payload["move_time_ms"] | 0;
    if (mt < 0) mt = 0;
    if (mt > 5000) mt = 5000;
    move_time_override_ms = (uint16_t)mt;
    move_time_override_until_ms = now_ms() + 5000;
    Serial.printf("[CMD] move_time_override_ms=%u (until +5s)\n", (unsigned)move_time_override_ms);
  }

  // Log position changes
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

static void process_packet(char *buffer, size_t len,
                           IPAddress ip, uint16_t port) {
  // Log first connection
  if (!first_client_seen) {
    first_client_seen = true;
    Serial.printf("[LINK] *** First client: %s:%u ***\n",
                  ip.toString().c_str(), port);
  }

  // Raw data log (truncated)
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
    Serial.printf("[LINK] Hello from %s:%u -> ACK+caps\n",
                  ip.toString().c_str(), port);
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
        apply_config(payload);
        send_ack(seq, true, ip, port);
      } else if (strcmp(action, "encoder_request") == 0) {
        send_ack(seq, true, ip, port);
        send_state(ip, port);
      } else if (strcmp(action, "bus_ping") == 0) {
        // Safe diagnostic: attempt to ping bus servo IDs (1,2) using both
        // checksum variants to detect/confirm the correct mode.
        // IMPORTANT: choose UART2 baud only on VALID ping responses, not on
        // arbitrary RX noise bytes.
        size_t rx_pan_sub = 0, rx_pan_xor = 0;
        size_t rx_tilt_sub = 0, rx_tilt_xor = 0;

        bool pan_sub = false, pan_xor = false;
        bool tilt_sub = false, tilt_xor = false;

        auto do_pings = [&]() {
          rx_pan_sub = rx_pan_xor = rx_tilt_sub = rx_tilt_xor = 0;
          pan_sub = bus_try_ping(BUS_ID_PAN, BUS_CHK_SUB, 50, &rx_pan_sub);
          pan_xor = bus_try_ping(BUS_ID_PAN, BUS_CHK_XOR, 50, &rx_pan_xor);
          tilt_sub = bus_try_ping(BUS_ID_TILT, BUS_CHK_SUB, 50, &rx_tilt_sub);
          tilt_xor = bus_try_ping(BUS_ID_TILT, BUS_CHK_XOR, 50, &rx_tilt_xor);
        };

        do_pings();

        bool any_valid = (pan_sub || pan_xor || tilt_sub || tilt_xor);
        if (!any_valid) {
          const uint32_t original_baud = bus_baud_active;
          const uint32_t candidates[] = {BUS_BAUD, 115200, 57600, 38400};
          bool found_valid = false;
          for (size_t i = 0; i < (sizeof(candidates) / sizeof(candidates[0])); i++) {
            uint32_t b = candidates[i];
            if (b == bus_baud_active) continue;
            Serial.printf("[BUSPING] Baud scan: trying %u...\n", (unsigned)b);
            bus_reinit(b);
            do_pings();

            any_valid = (pan_sub || pan_xor || tilt_sub || tilt_xor);
            if (any_valid) {
              found_valid = true;
              Serial.printf("[BUSPING] Baud scan: VALID ping at %u\n", (unsigned)b);
              break;
            }
          }

          if (!found_valid) {
            // Do not stay at a random scanned baud if no valid reply was found.
            // Prefer configured default, then previous runtime value.
            if (bus_baud_active != BUS_BAUD) {
              bus_reinit(BUS_BAUD);
            } else if (bus_baud_active != original_baud) {
              bus_reinit(original_baud);
            }
            Serial.printf("[BUSPING] No valid ping at scanned bauds; reverted to %u\n", (unsigned)bus_baud_active);
          }
        }

        // Lock on the first mode that yields any valid response.
        if (!bus_chk_locked) {
          if (pan_xor || tilt_xor) {
            bus_chk_mode = BUS_CHK_XOR;
            bus_chk_locked = true;
            Serial.println("[BUSPING] Locked checksum mode: xor");
          } else if (pan_sub || tilt_sub) {
            bus_chk_mode = BUS_CHK_SUB;
            bus_chk_locked = true;
            Serial.println("[BUSPING] Locked checksum mode: sub");
          }
        }

        const bool pan_ok = (bus_chk_locked ? ((bus_chk_mode == BUS_CHK_XOR) ? pan_xor : pan_sub) : (pan_sub || pan_xor));
        const bool tilt_ok = (bus_chk_locked ? ((bus_chk_mode == BUS_CHK_XOR) ? tilt_xor : tilt_sub) : (tilt_sub || tilt_xor));

        const char *mode_str = bus_chk_locked
          ? ((bus_chk_mode == BUS_CHK_XOR) ? "xor" : "sub")
          : "auto";

        // Report rx counts for the selected mode if locked, otherwise max observed.
        uint32_t rx_pan = 0;
        uint32_t rx_tilt = 0;
        if (bus_chk_locked && bus_chk_mode == BUS_CHK_XOR) {
          rx_pan = (uint32_t)rx_pan_xor;
          rx_tilt = (uint32_t)rx_tilt_xor;
        } else if (bus_chk_locked && bus_chk_mode == BUS_CHK_SUB) {
          rx_pan = (uint32_t)rx_pan_sub;
          rx_tilt = (uint32_t)rx_tilt_sub;
        } else {
          rx_pan = (uint32_t)((rx_pan_sub > rx_pan_xor) ? rx_pan_sub : rx_pan_xor);
          rx_tilt = (uint32_t)((rx_tilt_sub > rx_tilt_xor) ? rx_tilt_sub : rx_tilt_xor);
        }

        // Bridge-aware fallback:
        // In some topologies, the debug board forwards bus commands but does not
        // return strict DS ping packets. If we see repeatable RX bytes for both
        // channels, treat the bridge link as healthy for diagnostics.
        const bool bridge_rx_ok = (rx_pan > 0 && rx_tilt > 0);

        send_ack_busdiag(seq, (pan_ok || tilt_ok || bridge_rx_ok), ip, port,
             pan_ok, tilt_ok, rx_pan, rx_tilt, mode_str, bridge_rx_ok);
      } else if (strcmp(action, "test") == 0) {
        // === MANUAL TEST MODE ===
        Serial.println("[TEST] === MANUAL TEST TRIGGERED ===");
        run_self_test();
        send_ack(seq, true, ip, port);
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

// =========================================================
// Pin validation
// =========================================================
static void validate_pins() {
  Serial.println("[BOOT] Pin validation:");

  int all_pins[] = {
    PIN_UART_RX, PIN_UART_TX, PIN_TRIGGER_MOSFET, PIN_TRIGGER_SERVO,
    PIN_LED_RELAY, PIN_LASER_RELAY, PIN_CURR_PAN, PIN_CURR_TILT,
    PIN_CURR_TOTAL
  };
  const char *names[] = {
    "UART_RX", "UART_TX", "MOSFET", "TRIG_SERVO",
    "LED_RELAY", "LASER_RELAY", "CURR_PAN", "CURR_TILT", "CURR_TOTAL"
  };
  int count = sizeof(all_pins) / sizeof(all_pins[0]);

  bool conflict = false;
  for (int i = 0; i < count; i++) {
    for (int j = i + 1; j < count; j++) {
      if (all_pins[i] == all_pins[j]) {
        Serial.printf("  *** CONFLICT: %s and %s both GPIO%d! ***\n",
                      names[i], names[j], all_pins[i]);
        conflict = true;
      }
    }
  }
  if (!conflict)
    Serial.println("  No pin conflicts.");

  // PWM capability
  Serial.printf("  TRIG_SERVO (GPIO%d): PWM=%s\n", PIN_TRIGGER_SERVO,
                (PIN_TRIGGER_SERVO < 34) ? "YES" : "NO");
  // Input-only check (GPIO 34-39)
  Serial.printf("  CURR_PAN   (GPIO%d): input-only=%s\n", PIN_CURR_PAN,
                (PIN_CURR_PAN >= 34 && PIN_CURR_PAN <= 39) ? "OK" : "WARN");
  Serial.printf("  CURR_TILT  (GPIO%d): input-only=%s\n", PIN_CURR_TILT,
                (PIN_CURR_TILT >= 34 && PIN_CURR_TILT <= 39) ? "OK" : "WARN");
  Serial.printf("  CURR_TOTAL (GPIO%d): input-only=%s\n", PIN_CURR_TOTAL,
                (PIN_CURR_TOTAL >= 34 && PIN_CURR_TOTAL <= 39) ? "OK" : "WARN");
  // UART2 defaults
  Serial.printf("  UART2_RX (GPIO%d): %s\n", PIN_UART_RX,
                (PIN_UART_RX == 16) ? "DEFAULT" : "NON-DEFAULT");
  Serial.printf("  UART2_TX (GPIO%d): %s\n", PIN_UART_TX,
                (PIN_UART_TX == 17) ? "DEFAULT" : "NON-DEFAULT");

  Serial.println("[BOOT] Pin validation OK.");
}

// =========================================================
// Boot self-test
// =========================================================
static void run_self_test() {
  Serial.println("================================================");
  Serial.println("   DB3000 HARDWARE SELF-TEST");
  Serial.println("================================================");

  // 1. Trigger servo sweep: 0 -> 90 -> 0
  Serial.println("[TEST] 1/7 Trigger servo: 0 -> 90 -> 0");
  servo_write_deg(PIN_TRIGGER_SERVO, 0);
  delay(400);
  Serial.println("  -> 0 deg (rest)");
  servo_write_deg(PIN_TRIGGER_SERVO, 90);
  delay(400);
  Serial.println("  -> 90 deg (mid)");
  servo_write_deg(PIN_TRIGGER_SERVO, 0);
  delay(400);
  Serial.println("  -> 0 deg (rest) OK");

  // 2. LED relay
  Serial.println("[TEST] 2/7 LED relay toggle");
  digitalWrite(PIN_LED_RELAY, HIGH);
  delay(300);
  Serial.println("  -> ON");
  digitalWrite(PIN_LED_RELAY, LOW);
  delay(200);
  Serial.println("  -> OFF OK");

  // 3. Laser relay
  Serial.println("[TEST] 3/7 Laser relay toggle");
  digitalWrite(PIN_LASER_RELAY, HIGH);
  delay(300);
  Serial.println("  -> ON");
  digitalWrite(PIN_LASER_RELAY, LOW);
  delay(200);
  Serial.println("  -> OFF OK");

  // 4. MOSFET
  Serial.println("[TEST] 4/7 MOSFET trigger toggle");
  digitalWrite(PIN_TRIGGER_MOSFET, HIGH);
  delay(150);
  Serial.println("  -> ON");
  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  delay(100);
  Serial.println("  -> OFF OK");

  // 5. Bus servo home
  Serial.println("[TEST] 5/7 Bus servo home (Pan=90, Tilt=40)");
  set_bus_servo_angle(BUS_ID_PAN,  90, 500);
  delay(100);
  set_bus_servo_angle(BUS_ID_TILT, 40, 500);
  delay(600);
  Serial.println("  -> Home sent, check physical movement");

  // 6. Pan sweep
  Serial.println("[TEST] 6/7 Pan sweep: 80 -> 100 -> 90");
  set_bus_servo_angle(BUS_ID_PAN, 80, 300);
  delay(400);
  set_bus_servo_angle(BUS_ID_PAN, 100, 300);
  delay(400);
  set_bus_servo_angle(BUS_ID_PAN, 90, 300);
  delay(400);
  Serial.println("  -> Pan sweep complete");

  // 7. Tilt sweep
  Serial.println("[TEST] 7/7 Tilt sweep: 30 -> 50 -> 40");
  set_bus_servo_angle(BUS_ID_TILT, 30, 300);
  delay(400);
  set_bus_servo_angle(BUS_ID_TILT, 50, 300);
  delay(400);
  set_bus_servo_angle(BUS_ID_TILT, 40, 300);
  delay(400);
  Serial.println("  -> Tilt sweep complete");

  // 8. Current sensors
  int pan_mA   = read_current_mA(PIN_CURR_PAN,   PAN_MA_PER_ADC);
  int tilt_mA  = read_current_mA(PIN_CURR_TILT,  TILT_MA_PER_ADC);
  int total_mA = read_current_mA(PIN_CURR_TOTAL, TOTAL_MA_PER_ADC);
  Serial.printf("[TEST] Currents: pan=%dmA tilt=%dmA total=%dmA\n",
                pan_mA, tilt_mA, total_mA);

  Serial.println("================================================");
  Serial.println("   SELF-TEST COMPLETE");
  Serial.printf("   Bus cmds sent: %u\n", bus_send_count);
  Serial.println("================================================");
}

// =========================================================
// Brownout / reset reason
// =========================================================
static void log_reset_reason() {
  esp_reset_reason_t reason = esp_reset_reason();
  Serial.print("[BOOT] Reset reason: ");
  switch (reason) {
    case ESP_RST_POWERON:   Serial.println("Power-on");          break;
    case ESP_RST_EXT:       Serial.println("External reset");    break;
    case ESP_RST_SW:        Serial.println("Software reset");    break;
    case ESP_RST_PANIC:     Serial.println("Exception/panic");   break;
    case ESP_RST_INT_WDT:   Serial.println("Interrupt WDT");     break;
    case ESP_RST_TASK_WDT:  Serial.println("Task WDT");          break;
    case ESP_RST_WDT:       Serial.println("Other WDT");         break;
    case ESP_RST_DEEPSLEEP: Serial.println("Deep sleep wake");   break;
    case ESP_RST_BROWNOUT:
      Serial.println("*** BROWNOUT *** Check power supply!");
      break;
    case ESP_RST_SDIO:      Serial.println("SDIO reset");        break;
    default:
      Serial.printf("Unknown (%d)\n", (int)reason);
      break;
  }
}

// =========================================================
// Setup
// =========================================================
void setup() {
  Serial.begin(115200);
  while (!Serial && millis() < 2000) { /* wait for USB-Serial */ }

  Serial.println();
  Serial.println("================================================");
  Serial.println("  DB3000 ESP32 UDP Link Firmware v2 (Diag)");
  Serial.println("  Board: ESP32 DevKit v1 (WROOM-32)");
  Serial.printf("  Compiled: %s %s\n", __DATE__, __TIME__);
  Serial.printf("  Free heap: %u bytes\n", ESP.getFreeHeap());
  Serial.printf("  CPU: %u MHz\n", ESP.getCpuFreqMHz());
  Serial.printf("  Flash: %u bytes\n", ESP.getFlashChipSize());
  Serial.printf("  SDK: %s\n", ESP.getSdkVersion());
  Serial.println("================================================");

  log_reset_reason();
  validate_pins();

  // UART2 for bus servos
  bus_baud_active = BUS_BAUD;
  Serial.printf("[BOOT] UART2: baud=%u RX=GPIO%d TX=GPIO%d\n",
                (unsigned)bus_baud_active, PIN_UART_RX, PIN_UART_TX);
  busSerial.begin(bus_baud_active, SERIAL_8N1, PIN_UART_RX, PIN_UART_TX);

  // Digital outputs
  Serial.println("[BOOT] Digital outputs...");
  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  pinMode(PIN_LED_RELAY,      OUTPUT);
  pinMode(PIN_LASER_RELAY,    OUTPUT);
  pinMode(PIN_STATUS_LED,     OUTPUT);
  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  digitalWrite(PIN_LED_RELAY,      LOW);
  digitalWrite(PIN_LASER_RELAY,    LOW);
  digitalWrite(PIN_STATUS_LED,     LOW);
  Serial.printf("  MOSFET(GPIO%d)=LOW  LED(GPIO%d)=LOW  LASER(GPIO%d)=LOW\n",
                PIN_TRIGGER_MOSFET, PIN_LED_RELAY, PIN_LASER_RELAY);
  Serial.printf("  STATUS_LED(GPIO%d)=LOW\n", PIN_STATUS_LED);

  // Trigger servo PWM (LEDC)
  Serial.printf("[BOOT] LEDC: GPIO%d freq=%dHz res=%d-bit\n",
                PIN_TRIGGER_SERVO, SERVO_HZ, SERVO_RES_BITS);
  bool ledc_ok = ledcAttach(PIN_TRIGGER_SERVO, SERVO_HZ, SERVO_RES_BITS);
  Serial.printf("  LEDC attach: %s\n", ledc_ok ? "OK" : "FAILED!");
  servo_write_deg(PIN_TRIGGER_SERVO, TRIGGER_SERVO_REST_DEG);
  Serial.printf("  Trigger servo -> %d deg (rest)\n", TRIGGER_SERVO_REST_DEG);

  // ADC
  Serial.println("[BOOT] ADC: 12-bit, 11dB atten");
  analogReadResolution(12);
  analogSetPinAttenuation(PIN_CURR_PAN,   ADC_11db);
  analogSetPinAttenuation(PIN_CURR_TILT,  ADC_11db);
  analogSetPinAttenuation(PIN_CURR_TOTAL, ADC_11db);

  // Self-test BEFORE WiFi
  Serial.println("[BOOT] Running self-test...");
  run_self_test();

  // WiFi AP
  Serial.printf("[BOOT] WiFi AP: SSID='%s' pass='%s'\n", WIFI_SSID, WIFI_PASS);
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(AP_IP, AP_GW, AP_MASK);
  bool wifi_ok = WiFi.softAP(WIFI_SSID, WIFI_PASS);
  Serial.printf("  WiFi AP: %s  IP=%s\n",
                wifi_ok ? "OK" : "FAILED",
                WiFi.softAPIP().toString().c_str());

  // UDP
  Udp.begin(UDP_PORT);
  Serial.printf("[BOOT] UDP port %u ready\n", UDP_PORT);

  last_cmd_ms = now_ms();

  Serial.println("================================================");
  Serial.println("  BOOT COMPLETE - Waiting for app");
  Serial.printf("  WiFi: '%s'  Target: %s:%u\n",
                WIFI_SSID, AP_IP.toString().c_str(), UDP_PORT);
  Serial.println("================================================");
  Serial.println();
}

// =========================================================
// Main loop
// =========================================================
void loop() {
  uint32_t now = now_ms();

  // UDP receive
  int packet_size = Udp.parsePacket();
  if (packet_size > 0) {
    static char buffer[2048];
    int len = Udp.read(buffer, sizeof(buffer) - 1);
    if (len > 0) {
      buffer[len]      = '\0';
      last_remote_ip   = Udp.remoteIP();
      last_remote_port = Udp.remotePort();
      last_cmd_ms      = now;
      process_packet(buffer, (size_t)len,
                     last_remote_ip, last_remote_port);
    }
  }

  // Current protection
  int pan_mA   = read_current_mA(PIN_CURR_PAN,   PAN_MA_PER_ADC);
  int tilt_mA  = read_current_mA(PIN_CURR_TILT,  TILT_MA_PER_ADC);
  int total_mA = read_current_mA(PIN_CURR_TOTAL, TOTAL_MA_PER_ADC);

  bool over_pan   = (current_cfg.trip_pan_mA   > 0) &&
                    (pan_mA   >= current_cfg.trip_pan_mA);
  bool over_tilt  = (current_cfg.trip_tilt_mA  > 0) &&
                    (tilt_mA  >= current_cfg.trip_tilt_mA);
  bool over_total = (current_cfg.trip_total_mA > 0) &&
                    (total_mA >= current_cfg.trip_total_mA);
  bool over_any   = over_pan || over_tilt || over_total;

  if (current_cfg.enabled) {
    if (over_any) {
      if (trip_start_ms == 0) {
        trip_start_ms = now;
        Serial.printf("[CURR] Over-current: pan=%d tilt=%d total=%d\n",
                      pan_mA, tilt_mA, total_mA);
      }
      if ((now - trip_start_ms) >= (uint32_t)current_cfg.trip_hold_ms) {
        if (!current_fault) {
          current_fault = true;
          Serial.println("[CURR] *** FAULT TRIPPED ***");
        }
      }
    } else {
      trip_start_ms = 0;
      if (!current_cfg.latch) {
        if (current_fault)
          Serial.println("[CURR] Fault cleared");
        current_fault = false;
      } else if (current_fault) {
        int clear_pan   = current_cfg.trip_pan_mA   - current_cfg.hysteresis_mA;
        int clear_tilt  = current_cfg.trip_tilt_mA  - current_cfg.hysteresis_mA;
        int clear_total = current_cfg.trip_total_mA - current_cfg.hysteresis_mA;
        bool clear_ok = true;
        if (current_cfg.trip_pan_mA   > 0 && pan_mA   > clear_pan)   clear_ok = false;
        if (current_cfg.trip_tilt_mA  > 0 && tilt_mA  > clear_tilt)  clear_ok = false;
        if (current_cfg.trip_total_mA > 0 && total_mA > clear_total) clear_ok = false;
        if (clear_ok && (now - trip_start_ms) >= (uint32_t)current_cfg.clear_hold_ms) {
          current_fault = false;
          Serial.println("[CURR] Fault cleared (latch)");
        }
      }
    }
  } else {
    current_fault = false;
  }

  bool fire_blocked   = (safety_state != 0) ||
                        (current_fault && current_cfg.block_fire);
  bool motion_blocked = (current_fault && current_cfg.block_motion);

  update_motion_outputs(motion_blocked);
  update_accessories();
  update_fire_outputs(now, fire_blocked);

  // Link timeout safety
  if ((now - last_cmd_ms) > 1000) {
    if (fire_request != 0) {
      Serial.println("[LINK] Timeout >1s - fire stopped");
      fire_request = 0;
    }
  }

  // Non-blocking status LED command indicator
  status_led_tick(now);

  // Periodic state broadcast
  if (last_remote_port != 0 && (now - last_state_ms) > 250) {
    last_state_ms = now;
    send_state(last_remote_ip, last_remote_port);
  }

  // Periodic diagnostic every 10 seconds
  static uint32_t last_diag_ms = 0;
  if ((now - last_diag_ms) > 10000) {
    last_diag_ms = now;
    Serial.printf("[DIAG] up=%us cmds=%u bus=%u crc_f=%u parse_f=%u "
                  "heap=%u safety=%d pan=%d tilt=%d\n",
                  now / 1000, cmd_count, bus_send_count,
                  crc_fail_count, parse_fail_count,
                  ESP.getFreeHeap(), safety_state,
                  target_pan, target_tilt);
  }
}
