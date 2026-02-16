// DB3000 ESP32 Direct Debug-Board Link (Arduino IDE friendly)
// Topology: PC <-> ESP32 (WiFi/UDP) <-> Debug Board (UART2 RX16/TX17)
//
// Requires library:
//   - ArduinoJson (v6)
//
// ESP32 Board: ESP32 Dev Module

#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>

// ---------------- WiFi / UDP ----------------
static const char *WIFI_SSID = "DB3000-ESP32";
static const char *WIFI_PASS = "db3000pass";

static const IPAddress AP_IP(192, 168, 4, 1);
static const IPAddress AP_GW(192, 168, 4, 1);
static const IPAddress AP_MASK(255, 255, 255, 0);

static const uint16_t UDP_PORT = 9000;
WiFiUDP Udp;
IPAddress last_remote_ip;
uint16_t last_remote_port = 0;

// ---------------- UART2 (to debug board) ----------------
static const int PIN_UART_RX = 16;   // ESP32 RX2 <- debug board TX
static const int PIN_UART_TX = 17;   // ESP32 TX2 -> debug board RX
static const uint32_t BUS_BAUD = 1000000;
HardwareSerial busSerial(2);

// ---------------- Local IO pins (optional but app-compatible) ----------------
static const int PIN_TRIGGER_MOSFET = 27;   // Water mode
static const int PIN_TRIGGER_SERVO  = 13;   // Projectile mode (PWM)
static const int PIN_LED_RELAY      = 32;
static const int PIN_LASER_RELAY    = 33;

static const int SERVO_HZ = 50;
static const int SERVO_RES_BITS = 16;
static const int SERVO_MIN_US = 500;
static const int SERVO_MAX_US = 2500;
static const int SERVO_REST_DEG = 0;
static const int SERVO_FIRE_DEG = 40;
static const uint32_t SERVO_FIRE_PULSE_MS = 120;

// ---------------- Bus servo IDs / limits ----------------
static const uint8_t BUS_ID_PAN = 1;
static const uint8_t BUS_ID_TILT = 2;

static const int PAN_MIN = 0;
static const int PAN_MAX = 220;
static const int TILT_MIN = 0;
static const int TILT_MAX = 70;

static uint8_t bus_id_pan = BUS_ID_PAN;
static uint8_t bus_id_tilt = BUS_ID_TILT;
static uint16_t bus_pan_ticks_min = 0;
static uint16_t bus_pan_ticks_max = 4095;
static uint16_t bus_tilt_ticks_min = 0;
static uint16_t bus_tilt_ticks_max = 4095;
static bool bus_word_swap = false;

static int target_pan = 90;
static int target_tilt = 40;
static int safety_state = 1; // 1=locked, 0=armed
static int trigger_mode = 0; // 0=water/mosfet, 1=projectile/servo
static int led_state = 0;
static int laser_state = 0;
static int fire_request = 0;
static bool fire_hold = false;

static bool rapid_fire_enabled = false;
static int rapid_fire_rate_hz = 1;
static float rapid_fire_duty = 0.5f;

static uint32_t trigger_cooldown_ms = 1500;
static uint32_t trigger_max_fire_ms = 3000;
static bool fire_active = false;
static bool rapid_fire_active = false;
static uint32_t fire_start_ms = 0;
static uint32_t last_projectile_shot_ms = 0;

static int last_sent_pan = -1;
static int last_sent_tilt = -1;
static uint32_t last_bus_send_ms = 0;
static uint32_t bus_send_count = 0;
static uint32_t last_state_ms = 0;

static uint16_t move_time_override_ms = 0;
static uint32_t move_time_override_until_ms = 0;

static bool bus_chk_locked = false;
static bool bus_chk_xor = false; // false=sub, true=xor

// ---------------- CRC32 ----------------
static uint32_t crc32_update(uint32_t crc, uint8_t data) {
  crc ^= data;
  for (int i = 0; i < 8; ++i) {
    if (crc & 1) crc = (crc >> 1) ^ 0xEDB88320UL;
    else crc >>= 1;
  }
  return crc;
}

static uint32_t crc32_compute(const uint8_t *data, size_t len) {
  uint32_t crc = 0xFFFFFFFFUL;
  for (size_t i = 0; i < len; ++i) crc = crc32_update(crc, data[i]);
  return ~crc;
}

// ---------------- Helpers ----------------
static int clamp_int(int v, int lo, int hi) {
  if (v < lo) return lo;
  if (v > hi) return hi;
  return v;
}

static uint32_t now_ms() { return millis(); }

static uint8_t bus_checksum(const uint8_t *buf, int fromIdx, int toIdx, bool useXor) {
  uint16_t sum = 0;
  for (int i = fromIdx; i <= toIdx; i++) sum += buf[i];
  sum &= 0xFF;
  if (useXor) return (uint8_t)(0xFF ^ sum);
  return (uint8_t)(0xFF - sum);
}

static uint32_t deg_to_duty_ticks(int deg) {
  const int clamped = clamp_int(deg, 0, 180);
  const uint32_t us = (uint32_t)map(clamped, 0, 180, SERVO_MIN_US, SERVO_MAX_US);
  const uint32_t max_ticks = (1UL << SERVO_RES_BITS) - 1;
  const uint32_t period_us = 1000000UL / SERVO_HZ;
  uint32_t ticks = (us * max_ticks) / period_us;
  if (ticks > max_ticks) ticks = max_ticks;
  return ticks;
}

static void trigger_servo_set(bool on) {
  ledcWrite(PIN_TRIGGER_SERVO, deg_to_duty_ticks(on ? SERVO_FIRE_DEG : SERVO_REST_DEG));
}

static void trigger_mosfet_set(bool on) {
  digitalWrite(PIN_TRIGGER_MOSFET, on ? HIGH : LOW);
}

static void update_relay_outputs() {
  digitalWrite(PIN_LED_RELAY, led_state ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY, laser_state ? HIGH : LOW);
}

static void clear_fire_outputs() {
  trigger_mosfet_set(false);
  trigger_servo_set(false);
  fire_active = false;
  rapid_fire_active = false;
}

static void update_fire_outputs() {
  const uint32_t now = now_ms();

  if (safety_state != 0) {
    clear_fire_outputs();
    return;
  }

  if (fire_request == 0) {
    clear_fire_outputs();
    return;
  }

  if (trigger_mode == 0) {
    bool out_on = true;
    if (rapid_fire_enabled) {
      const int rate = clamp_int(rapid_fire_rate_hz, 1, 50);
      const uint32_t period_ms = (uint32_t)(1000U / (uint32_t)rate);
      const float duty = (rapid_fire_duty < 0.05f) ? 0.05f : ((rapid_fire_duty > 0.95f) ? 0.95f : rapid_fire_duty);
      const uint32_t on_ms = (uint32_t)((float)period_ms * duty);
      const uint32_t phase = (period_ms > 0) ? (now % period_ms) : 0;
      out_on = (phase < on_ms);
      rapid_fire_active = true;
    } else {
      rapid_fire_active = false;
    }
    trigger_mosfet_set(out_on);
    trigger_servo_set(false);
    fire_active = out_on;
    if (out_on && fire_start_ms == 0) fire_start_ms = now;
    if ((trigger_max_fire_ms > 0) && fire_start_ms > 0 && (now - fire_start_ms) > trigger_max_fire_ms && !fire_hold) {
      fire_request = 0;
      clear_fire_outputs();
    }
    return;
  }

  trigger_mosfet_set(false);
  rapid_fire_active = false;
  if (!fire_active) {
    if ((now - last_projectile_shot_ms) >= trigger_cooldown_ms) {
      fire_active = true;
      fire_start_ms = now;
      last_projectile_shot_ms = now;
      trigger_servo_set(true);
    }
  } else {
    if ((now - fire_start_ms) >= SERVO_FIRE_PULSE_MS) {
      trigger_servo_set(false);
      fire_active = false;
      if (!fire_hold) fire_request = 0;
    }
  }
}

static uint16_t map_deg_to_ticks(int deg, int minDeg, int maxDeg, uint16_t ticksMin, uint16_t ticksMax) {
  deg = clamp_int(deg, minDeg, maxDeg);
  long num = (long)(deg - minDeg) * (long)(ticksMax - ticksMin);
  long den = (long)(maxDeg - minDeg);
  if (den <= 0) return ticksMin;
  return (uint16_t)(ticksMin + (num / den));
}

static uint16_t compute_move_time_ms(int deltaAbs) {
  if (deltaAbs < 0) deltaAbs = -deltaAbs;
  if (deltaAbs >= 30) return 10;
  if (deltaAbs >= 15) return 14;
  if (deltaAbs >= 7) return 18;
  return 22;
}

static void bus_write(const uint8_t *buf, size_t len) {
  busSerial.write(buf, len);
  busSerial.flush();
}

static void bus_send_position_pkt(uint8_t id, int deg, uint16_t moveTimeMs, bool useXor) {
  uint16_t ticks = (id == bus_id_pan)
    ? map_deg_to_ticks(deg, PAN_MIN, PAN_MAX, bus_pan_ticks_min, bus_pan_ticks_max)
    : map_deg_to_ticks(deg, TILT_MIN, TILT_MAX, bus_tilt_ticks_min, bus_tilt_ticks_max);

  uint8_t posH = (ticks >> 8) & 0xFF;
  uint8_t posL = ticks & 0xFF;
  uint8_t tH = (moveTimeMs >> 8) & 0xFF;
  uint8_t tL = moveTimeMs & 0xFF;

  uint8_t pkt[11];
  uint8_t b6 = posH, b7 = posL, b8 = tH, b9 = tL;
  if (bus_word_swap) {
    b6 = posL; b7 = posH; b8 = tL; b9 = tH;
  }

  pkt[0] = 0xFF; pkt[1] = 0xFF; pkt[2] = id; pkt[3] = 0x07; pkt[4] = 0x03;
  pkt[5] = 0x2A; pkt[6] = b6; pkt[7] = b7; pkt[8] = b8; pkt[9] = b9;
  pkt[10] = bus_checksum(pkt, 2, 9, useXor);

  bus_write(pkt, sizeof(pkt));
  bus_send_count++;
}

static void set_bus_servo_angle(uint8_t id, int deg, uint16_t moveTimeMs) {
  if (!bus_chk_locked) {
    bus_send_position_pkt(id, deg, moveTimeMs, false); // sub
    bus_send_position_pkt(id, deg, moveTimeMs, true);  // xor
    return;
  }
  bus_send_position_pkt(id, deg, moveTimeMs, bus_chk_xor);
}

static bool bus_try_ping(uint8_t id, bool useXor, uint16_t timeoutMs, size_t *rxCountOut) {
  uint8_t pkt[6];
  pkt[0] = 0xFF; pkt[1] = 0xFF; pkt[2] = id; pkt[3] = 0x02; pkt[4] = 0x01;
  pkt[5] = bus_checksum(pkt, 2, 4, useXor);

  while (busSerial.available()) (void)busSerial.read();
  bus_write(pkt, sizeof(pkt));

  uint32_t t0 = now_ms();
  uint8_t rx[32];
  size_t n = 0;
  while ((now_ms() - t0) < timeoutMs && n < sizeof(rx)) {
    if (busSerial.available()) rx[n++] = (uint8_t)busSerial.read();
  }
  if (rxCountOut) *rxCountOut = n;

  if (n >= 6) {
    for (size_t i = 0; i + 2 < n; i++) {
      if (rx[i] == 0xFF && rx[i + 1] == 0xFF && rx[i + 2] == id) return true;
    }
  }
  return false;
}

static void update_motion_outputs() {
  const int pan = clamp_int(target_pan, PAN_MIN, PAN_MAX);
  const int tilt = clamp_int(target_tilt, TILT_MIN, TILT_MAX);
  const uint32_t now = now_ms();
  const bool changed = (pan != last_sent_pan) || (tilt != last_sent_tilt);

  if (!changed && (now - last_bus_send_ms) < 250) return;

  const int pan_delta = (last_sent_pan < 0) ? 0 : (pan - last_sent_pan);
  const int tilt_delta = (last_sent_tilt < 0) ? 0 : (tilt - last_sent_tilt);
  uint16_t pan_time = compute_move_time_ms(pan_delta);
  uint16_t tilt_time = compute_move_time_ms(tilt_delta);

  if (move_time_override_ms > 0 && now <= move_time_override_until_ms) {
    pan_time = move_time_override_ms;
    tilt_time = move_time_override_ms;
  }

  set_bus_servo_angle(bus_id_pan, pan, pan_time);
  set_bus_servo_angle(bus_id_tilt, tilt, tilt_time);

  last_sent_pan = pan;
  last_sent_tilt = tilt;
  last_bus_send_ms = now;
}

// ---------------- UDP JSON codec ----------------
static bool decode_message(char *buffer, size_t len, DynamicJsonDocument &doc) {
  DeserializationError err = deserializeJson(doc, buffer, len);
  if (err) return false;
  if (!doc["crc"].is<const char*>()) return false;

  const char *crc_str = doc["crc"];
  char crc_copy[16] = {0};
  snprintf(crc_copy, sizeof(crc_copy), "%s", crc_str);
  doc.remove("crc");

  String compact;
  serializeJson(doc, compact);
  uint32_t crc = crc32_compute((const uint8_t*)compact.c_str(), compact.length());

  char calc[9];
  snprintf(calc, sizeof(calc), "%08x", (unsigned int)crc);
  if (strcasecmp(calc, crc_copy) != 0) return false;
  return true;
}

static void encode_and_send(DynamicJsonDocument &doc, IPAddress ip, uint16_t port) {
  String compact;
  serializeJson(doc, compact);
  uint32_t crc = crc32_compute((const uint8_t*)compact.c_str(), compact.length());

  char crc_hex[9];
  snprintf(crc_hex, sizeof(crc_hex), "%08x", (unsigned int)crc);
  doc["crc"] = crc_hex;

  String payload;
  serializeJson(doc, payload);

  Udp.beginPacket(ip, port);
  Udp.write((const uint8_t*)payload.c_str(), payload.length());
  Udp.endPacket();
}

static void send_state(IPAddress ip, uint16_t port) {
  DynamicJsonDocument doc(1024);
  doc["v"] = 1;
  doc["t"] = "state";
  doc["seq"] = 0;
  doc["ts"] = (uint32_t)now_ms();

  JsonObject p = doc["p"].to<JsonObject>();
  p["pan"] = target_pan;
  p["tilt"] = target_tilt;
  p["safety"] = safety_state;
  p["mode"] = trigger_mode;
  p["fire"] = fire_active ? 1 : 0;
  p["led"] = led_state;
  p["laser"] = laser_state;
  p["rapid_fire_active"] = rapid_fire_active;
  p["current_fault"] = false;

  JsonObject bus = p["bus"].to<JsonObject>();
  bus["send_count"] = bus_send_count;
  bus["baud"] = BUS_BAUD;
  bus["last_send_ms"] = (uint32_t)last_bus_send_ms;
  bus["last_sent_pan"] = last_sent_pan;
  bus["last_sent_tilt"] = last_sent_tilt;
  bus["chk_locked"] = bus_chk_locked;
  bus["chk_mode"] = bus_chk_locked ? (bus_chk_xor ? "xor" : "sub") : "auto";
  bus["pan_id"] = bus_id_pan;
  bus["tilt_id"] = bus_id_tilt;
  bus["pan_ticks_max"] = bus_pan_ticks_max;
  bus["tilt_ticks_max"] = bus_tilt_ticks_max;
  bus["word_swap"] = bus_word_swap;

  encode_and_send(doc, ip, port);
}

static void send_ack(int seq, bool ok, IPAddress ip, uint16_t port) {
  DynamicJsonDocument doc(512);
  doc["v"] = 1;
  doc["t"] = "ack";
  doc["seq"] = seq;
  doc["ts"] = (uint32_t)now_ms();
  doc["ok"] = ok;

  JsonObject st = doc["state"].to<JsonObject>();
  st["pan"] = target_pan;
  st["tilt"] = target_tilt;
  st["safety"] = safety_state;
  st["mode"] = trigger_mode;
  st["fire"] = fire_active ? 1 : 0;
  st["led"] = led_state;
  st["laser"] = laser_state;

  encode_and_send(doc, ip, port);
}

static void send_caps(IPAddress ip, uint16_t port) {
  DynamicJsonDocument doc(512);
  doc["v"] = 1;
  doc["t"] = "cap";
  doc["seq"] = 0;
  doc["ts"] = (uint32_t)now_ms();

  JsonObject caps = doc["p"].to<JsonObject>();
  caps["proto"] = 1;
  caps["fw"] = "db3000-esp32-direct-debugboard";
  JsonObject pins = caps["pins"].to<JsonObject>();
  pins["uart_rx"] = PIN_UART_RX;
  pins["uart_tx"] = PIN_UART_TX;
  pins["mosfet"] = PIN_TRIGGER_MOSFET;
  pins["trigger_servo"] = PIN_TRIGGER_SERVO;
  pins["led"] = PIN_LED_RELAY;
  pins["laser"] = PIN_LASER_RELAY;

  encode_and_send(doc, ip, port);
}

static void send_ack_busdiag(int seq, bool ok, IPAddress ip, uint16_t port,
                             bool pan_ok, bool tilt_ok, uint32_t rx_pan, uint32_t rx_tilt,
                             const char *chk_mode, bool bridge_rx_ok) {
  DynamicJsonDocument doc(1024);
  doc["v"] = 1;
  doc["t"] = "ack";
  doc["seq"] = seq;
  doc["ts"] = (uint32_t)now_ms();
  doc["ok"] = ok;

  JsonObject st = doc["state"].to<JsonObject>();
  st["pan"] = target_pan;
  st["tilt"] = target_tilt;
  st["safety"] = safety_state;

  JsonObject p = doc["p"].to<JsonObject>();
  JsonObject b = p["bus"].to<JsonObject>();
  b["pan_ok"] = pan_ok;
  b["tilt_ok"] = tilt_ok;
  b["rx_pan"] = rx_pan;
  b["rx_tilt"] = rx_tilt;
  b["bridge_rx_ok"] = bridge_rx_ok;
  b["chk_mode"] = chk_mode;
  b["chk_locked"] = bus_chk_locked;
  b["bus_send_count"] = bus_send_count;
  b["baud"] = BUS_BAUD;

  encode_and_send(doc, ip, port);
}

static void process_packet(char *buffer, size_t len, IPAddress ip, uint16_t port) {
  DynamicJsonDocument doc(2048);
  if (!decode_message(buffer, len, doc)) return;

  const char *type = doc["t"] | "";
  int seq = doc["seq"] | 0;

  if (strcmp(type, "hello") == 0) {
    last_remote_ip = ip;
    last_remote_port = port;
    send_ack(seq, true, ip, port);
    send_caps(ip, port);
    return;
  }

  if (strcmp(type, "hb") == 0) {
    last_remote_ip = ip;
    last_remote_port = port;
    send_state(ip, port);
    return;
  }

  if (strcmp(type, "cmd") != 0) return;
  JsonObject payload = doc["p"].as<JsonObject>();

  if (payload.containsKey("action")) {
    const char *action = payload["action"] | "";

    if (strcmp(action, "encoder_request") == 0) {
      send_ack(seq, true, ip, port);
      send_state(ip, port);
      return;
    }

    if (strcmp(action, "bus_ping") == 0) {
      size_t rx_pan_sub = 0, rx_pan_xor = 0, rx_tilt_sub = 0, rx_tilt_xor = 0;
      bool pan_sub = bus_try_ping(bus_id_pan, false, 50, &rx_pan_sub);
      bool pan_xor = bus_try_ping(bus_id_pan, true, 50, &rx_pan_xor);
      bool tilt_sub = bus_try_ping(bus_id_tilt, false, 50, &rx_tilt_sub);
      bool tilt_xor = bus_try_ping(bus_id_tilt, true, 50, &rx_tilt_xor);

      if (!bus_chk_locked) {
        if (pan_xor || tilt_xor) {
          bus_chk_locked = true;
          bus_chk_xor = true;
        } else if (pan_sub || tilt_sub) {
          bus_chk_locked = true;
          bus_chk_xor = false;
        }
      }

      bool pan_ok = bus_chk_locked ? (bus_chk_xor ? pan_xor : pan_sub) : (pan_sub || pan_xor);
      bool tilt_ok = bus_chk_locked ? (bus_chk_xor ? tilt_xor : tilt_sub) : (tilt_sub || tilt_xor);
      uint32_t rx_pan = bus_chk_locked ? (bus_chk_xor ? rx_pan_xor : rx_pan_sub) : (uint32_t)max(rx_pan_sub, rx_pan_xor);
      uint32_t rx_tilt = bus_chk_locked ? (bus_chk_xor ? rx_tilt_xor : rx_tilt_sub) : (uint32_t)max(rx_tilt_sub, rx_tilt_xor);
      bool bridge_rx_ok = (rx_pan > 0 && rx_tilt > 0);
      const char *mode = bus_chk_locked ? (bus_chk_xor ? "xor" : "sub") : "auto";

      send_ack_busdiag(seq, (pan_ok || tilt_ok || bridge_rx_ok), ip, port,
                       pan_ok, tilt_ok, rx_pan, rx_tilt, mode, bridge_rx_ok);
      return;
    }

    if (strcmp(action, "config") == 0) {
      if (payload.containsKey("limits")) {
        JsonObject limits = payload["limits"].as<JsonObject>();
        int pmin = limits["pan_min"] | PAN_MIN;
        int pmax = limits["pan_max"] | PAN_MAX;
        int tmin = limits["tilt_min"] | TILT_MIN;
        int tmax = limits["tilt_max"] | TILT_MAX;
        target_pan = clamp_int(target_pan, pmin, pmax);
        target_tilt = clamp_int(target_tilt, tmin, tmax);
      }

      if (payload.containsKey("home")) {
        JsonObject home = payload["home"].as<JsonObject>();
        target_pan = clamp_int((home["pan"] | target_pan), PAN_MIN, PAN_MAX);
        target_tilt = clamp_int((home["tilt"] | target_tilt), TILT_MIN, TILT_MAX);
      }

      if (payload.containsKey("trigger")) {
        JsonObject trig = payload["trigger"].as<JsonObject>();
        trigger_mode = clamp_int((trig["mode"] | trigger_mode), 0, 1);
        const float cd_s = trig["cooldown_s"] | ((float)trigger_cooldown_ms / 1000.0f);
        const float mf_s = trig["max_fire_s"] | ((float)trigger_max_fire_ms / 1000.0f);
        trigger_cooldown_ms = (uint32_t)clamp_int((int)(cd_s * 1000.0f), 0, 30000);
        trigger_max_fire_ms = (uint32_t)clamp_int((int)(mf_s * 1000.0f), 0, 30000);
      }

      if (payload.containsKey("rapid_fire")) {
        JsonObject rf = payload["rapid_fire"].as<JsonObject>();
        rapid_fire_enabled = rf["enabled"] | rapid_fire_enabled;
        rapid_fire_rate_hz = clamp_int((rf["rate_hz"] | rapid_fire_rate_hz), 1, 50);
        float duty = rf["duty"] | rapid_fire_duty;
        if (duty < 0.05f) duty = 0.05f;
        if (duty > 0.95f) duty = 0.95f;
        rapid_fire_duty = duty;
      }

      if (payload.containsKey("bus")) {
        JsonObject buscfg = payload["bus"].as<JsonObject>();
        int pid = buscfg["pan_id"] | bus_id_pan;
        int tid = buscfg["tilt_id"] | bus_id_tilt;
        bus_id_pan = (uint8_t)clamp_int(pid, 1, 253);
        bus_id_tilt = (uint8_t)clamp_int(tid, 1, 253);

        int pmax = buscfg["pan_ticks_max"] | bus_pan_ticks_max;
        int tmax = buscfg["tilt_ticks_max"] | bus_tilt_ticks_max;
        bus_pan_ticks_max = (uint16_t)clamp_int(pmax, 300, 4095);
        bus_tilt_ticks_max = (uint16_t)clamp_int(tmax, 300, 4095);

        if (buscfg.containsKey("word_swap")) {
          bus_word_swap = bool(buscfg["word_swap"]);
        }

        const char *profile = buscfg["profile"] | "";
        if (strcmp(profile, "lx16a") == 0) {
          bus_pan_ticks_min = 0;
          bus_tilt_ticks_min = 0;
          bus_pan_ticks_max = 1000;
          bus_tilt_ticks_max = 1000;
          bus_word_swap = true;
        } else if (strcmp(profile, "yb_4095") == 0) {
          bus_pan_ticks_min = 0;
          bus_tilt_ticks_min = 0;
          bus_pan_ticks_max = 4095;
          bus_tilt_ticks_max = 4095;
          bus_word_swap = false;
        }
      }

      send_ack(seq, true, ip, port);
      send_state(ip, port);
      return;
    }
  }

  // Normal movement/flags packet
  if (payload.containsKey("safety")) safety_state = payload["safety"];
  if (payload.containsKey("mode")) trigger_mode = clamp_int(payload["mode"], 0, 1);
  if (payload.containsKey("led")) led_state = payload["led"] ? 1 : 0;
  if (payload.containsKey("laser")) laser_state = payload["laser"] ? 1 : 0;
  if (payload.containsKey("fire")) fire_request = payload["fire"] ? 1 : 0;
  if (payload.containsKey("fire_hold")) fire_hold = payload["fire_hold"];

  if (payload.containsKey("rapid_fire")) {
    JsonObject rf = payload["rapid_fire"].as<JsonObject>();
    rapid_fire_enabled = rf["enabled"] | rapid_fire_enabled;
    rapid_fire_rate_hz = clamp_int((rf["rate_hz"] | rapid_fire_rate_hz), 1, 50);
    float duty = rf["duty"] | rapid_fire_duty;
    if (duty < 0.05f) duty = 0.05f;
    if (duty > 0.95f) duty = 0.95f;
    rapid_fire_duty = duty;
  }

  if (payload.containsKey("pan_cmd")) target_pan = payload["pan_cmd"];
  else if (payload.containsKey("pan")) target_pan = (int)(payload["pan"].as<float>() + 0.5f);

  if (payload.containsKey("tilt_cmd")) target_tilt = payload["tilt_cmd"];
  else if (payload.containsKey("tilt")) target_tilt = (int)(payload["tilt"].as<float>() + 0.5f);

  target_pan = clamp_int(target_pan, PAN_MIN, PAN_MAX);
  target_tilt = clamp_int(target_tilt, TILT_MIN, TILT_MAX);

  if (payload.containsKey("move_time_ms")) {
    int mt = payload["move_time_ms"] | 0;
    mt = clamp_int(mt, 0, 5000);
    move_time_override_ms = (uint16_t)mt;
    move_time_override_until_ms = now_ms() + 5000;
  }

  update_relay_outputs();
  update_motion_outputs();
  update_fire_outputs();
  send_ack(seq, true, ip, port);
  send_state(ip, port);
}

void setup() {
  Serial.begin(115200);
  delay(100);
  Serial.println("\n[BOOT] DB3000_ESP32_DIRECT_DEBUGBOARD");

  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  pinMode(PIN_LED_RELAY, OUTPUT);
  pinMode(PIN_LASER_RELAY, OUTPUT);
  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  digitalWrite(PIN_LED_RELAY, LOW);
  digitalWrite(PIN_LASER_RELAY, LOW);

  bool ledc_ok = ledcAttach(PIN_TRIGGER_SERVO, SERVO_HZ, SERVO_RES_BITS);
  if (!ledc_ok) {
    Serial.println("[BOOT] LEDC attach failed for trigger servo pin");
  }
  trigger_servo_set(false);

  busSerial.begin(BUS_BAUD, SERIAL_8N1, PIN_UART_RX, PIN_UART_TX);
  Serial.printf("[BOOT] UART2 baud=%u RX=%d TX=%d\n", BUS_BAUD, PIN_UART_RX, PIN_UART_TX);

  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(AP_IP, AP_GW, AP_MASK);
  if (!WiFi.softAP(WIFI_SSID, WIFI_PASS)) {
    Serial.println("[BOOT] WiFi AP failed");
  } else {
    Serial.printf("[BOOT] WiFi AP OK SSID=%s IP=%s\n", WIFI_SSID, WiFi.softAPIP().toString().c_str());
  }

  Udp.begin(UDP_PORT);
  Serial.printf("[BOOT] UDP port %u ready\n", UDP_PORT);
}

void loop() {
  int packetSize = Udp.parsePacket();
  if (packetSize > 0) {
    static char buf[2048];
    int len = Udp.read((uint8_t*)buf, sizeof(buf) - 1);
    if (len > 0) {
      buf[len] = '\0';
      process_packet(buf, (size_t)len, Udp.remoteIP(), Udp.remotePort());
    }
  }

  update_relay_outputs();
  update_motion_outputs();
  update_fire_outputs();

  if (last_remote_port != 0 && (now_ms() - last_state_ms) > 250) {
    last_state_ms = now_ms();
    send_state(last_remote_ip, last_remote_port);
  }
}
