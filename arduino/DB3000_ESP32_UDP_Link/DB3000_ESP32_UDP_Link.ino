// DB3000 ESP32 UDP Link Firmware
// ---------------------------------------------
// Receives JSON+CRC32 commands over UDP and drives the turret IO.
// Default network mode is AP at 192.168.4.1 (matches app defaults).
//
// Libraries:
// - ArduinoJson (v6)
//
// Board target: ESP32 DevKit v1 (WROOM-32)
// Upload via Arduino IDE.

#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>

// -------------------------
// WiFi / UDP
// -------------------------
static const char *WIFI_SSID = "DB3000-ESP32";
static const char *WIFI_PASS = "db3000pass";

static const IPAddress AP_IP(192, 168, 4, 1);
static const IPAddress AP_GW(192, 168, 4, 1);
static const IPAddress AP_MASK(255, 255, 255, 0);

static const uint16_t UDP_PORT = 9000;

WiFiUDP Udp;
IPAddress last_remote_ip;
uint16_t last_remote_port = 0;

// -------------------------
// Pin Map (ESP32 DevKit v1)
// -------------------------
static const int PIN_UART_RX = 16;  // UART2 RX (debug board TX)
static const int PIN_UART_TX = 17;  // UART2 TX (debug board RX)

static const int PIN_PAN_SERVO = 25;    // PWM
static const int PIN_TILT_SERVO = 26;   // PWM
static const int PIN_TRIGGER_MOSFET = 27;  // Water mode
static const int PIN_TRIGGER_SERVO = 13;   // Projectile mode
static const int PIN_LED_RELAY = 32;
static const int PIN_LASER_RELAY = 33;

static const int PIN_CURR_PAN = 36;   // ADC1
static const int PIN_CURR_TILT = 39;  // ADC1
static const int PIN_CURR_TOTAL = 34; // ADC1

// -------------------------
// Servo PWM (LEDC)
// -------------------------
static const int SERVO_HZ = 50;
static const int SERVO_RES_BITS = 16;

static const int SERVO_MIN_US = 500;
static const int SERVO_MAX_US = 2500;

static const int TRIGGER_SERVO_REST_DEG = 0;
static const int TRIGGER_SERVO_FIRE_DEG = 40;
static const uint32_t TRIGGER_PULSE_MS = 120;

// -------------------------
// Config
// -------------------------
struct LimitsConfig {
  int pan_min = 0;
  int pan_max = 220;
  int tilt_min = 0;
  int tilt_max = 70;
};

struct HomeConfig {
  int pan = 90;
  int tilt = 40;
  float speed = 10.0f;
  float max_speed_dps = 25.0f;
};

struct TriggerConfig {
  int mode = 0;  // 0 = water (MOSFET), 1 = projectile (servo)
  float cooldown_s = 1.5f;
  float max_fire_s = 3.0f;
};

struct RapidFireConfig {
  bool enabled = false;
  int rate_hz = 1;
  float duty = 0.5f;
};

struct CurrentProtectionConfig {
  bool enabled = false;
  bool block_fire = true;
  bool block_motion = true;
  bool latch = false;
  int trip_pan_mA = 0;
  int trip_tilt_mA = 0;
  int trip_total_mA = 0;
  int trip_hold_ms = 250;
  int clear_hold_ms = 750;
  int hysteresis_mA = 250;
};

struct TiltSafetyConfig {
  bool installed = false;
  bool enabled = false;
};

LimitsConfig limits_cfg;
HomeConfig home_cfg;
TriggerConfig trigger_cfg;
RapidFireConfig rapid_cfg;
CurrentProtectionConfig current_cfg;
TiltSafetyConfig tilt_safety_cfg;

// -------------------------
// State
// -------------------------
static int target_pan = 90;
static int target_tilt = 40;

static int safety_state = 1; // 1 = safe/locked, 0 = armed
static int led_state = 0;
static int laser_state = 0;
static int fire_request = 0;
static bool fire_hold = false;

static uint32_t last_cmd_ms = 0;
static uint32_t last_state_ms = 0;

static uint32_t last_fire_start_ms = 0;
static bool fire_active = false;
static bool rapid_fire_active = false;

static uint32_t trip_start_ms = 0;
static bool current_fault = false;

// ADC conversion (adjust to match your sensors)
static const float PAN_MA_PER_ADC = 1.0f;
static const float TILT_MA_PER_ADC = 1.0f;
static const float TOTAL_MA_PER_ADC = 1.0f;

// -------------------------
// CRC32
// -------------------------
static uint32_t crc32_update(uint32_t crc, uint8_t data) {
  crc ^= data;
  for (int i = 0; i < 8; ++i) {
    if (crc & 1) {
      crc = (crc >> 1) ^ 0xEDB88320UL;
    } else {
      crc >>= 1;
    }
  }
  return crc;
}

static uint32_t crc32_compute(const uint8_t *data, size_t len) {
  uint32_t crc = 0xFFFFFFFFUL;
  for (size_t i = 0; i < len; ++i) {
    crc = crc32_update(crc, data[i]);
  }
  return ~crc;
}

// -------------------------
// Helpers
// -------------------------
static int clamp_int(int v, int lo, int hi) {
  if (v < lo) return lo;
  if (v > hi) return hi;
  return v;
}

static uint32_t now_ms() {
  return millis();
}

static uint32_t deg_to_duty_us(int deg) {
  int clamped = clamp_int(deg, 0, 180);
  return (uint32_t)map(clamped, 0, 180, SERVO_MIN_US, SERVO_MAX_US);
}

static uint32_t duty_us_to_ticks(uint32_t us) {
  uint32_t max_ticks = (1UL << SERVO_RES_BITS) - 1;
  uint32_t period_us = 1000000UL / SERVO_HZ;
  uint32_t ticks = (us * max_ticks) / period_us;
  if (ticks > max_ticks) ticks = max_ticks;
  return ticks;
}

static void servo_write_deg(int pin, int deg) {
  uint32_t us = deg_to_duty_us(deg);
  uint32_t ticks = duty_us_to_ticks(us);
  ledcWrite(pin, ticks);
}

static int read_current_mA(int pin, float scale) {
  int adc = analogRead(pin);
  return (int)(adc * scale);
}

// -------------------------
// Output control
// -------------------------
static void update_motion_outputs(bool motion_blocked) {
  if (motion_blocked) {
    return;
  }
  servo_write_deg(PIN_PAN_SERVO, target_pan);
  servo_write_deg(PIN_TILT_SERVO, target_tilt);
}

static void update_accessories() {
  digitalWrite(PIN_LED_RELAY, led_state ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY, laser_state ? HIGH : LOW);
}

static void set_mosfet(bool on) {
  digitalWrite(PIN_TRIGGER_MOSFET, on ? HIGH : LOW);
}

static void trigger_servo_fire(bool on) {
  servo_write_deg(PIN_TRIGGER_SERVO, on ? TRIGGER_SERVO_FIRE_DEG : TRIGGER_SERVO_REST_DEG);
}

static void update_fire_outputs(uint32_t now_ms, bool fire_blocked) {
  if (fire_blocked) {
    fire_active = false;
    rapid_fire_active = false;
    set_mosfet(false);
    trigger_servo_fire(false);
    return;
  }

  bool want_fire = (fire_request != 0);
  if (!want_fire) {
    fire_active = false;
    rapid_fire_active = false;
    set_mosfet(false);
    trigger_servo_fire(false);
    return;
  }

  if (trigger_cfg.mode == 0) {
    // Water (MOSFET)
    if (rapid_cfg.enabled) {
      int rate_hz = max(1, rapid_cfg.rate_hz);
      float duty = rapid_cfg.duty;
      if (duty < 0.05f) duty = 0.05f;
      if (duty > 0.95f) duty = 0.95f;
      uint32_t period_ms = 1000UL / (uint32_t)rate_hz;
      uint32_t on_ms = (uint32_t)((float)period_ms * duty);
      uint32_t phase = (now_ms % period_ms);
      bool on = (phase < on_ms);
      set_mosfet(on);
      fire_active = on;
      rapid_fire_active = true;
      return;
    }

    set_mosfet(true);
    fire_active = true;
    rapid_fire_active = false;
    return;
  }

  // Projectile (trigger servo)
  if (!fire_active) {
    fire_active = true;
    last_fire_start_ms = now_ms;
    trigger_servo_fire(true);
  } else {
    if ((now_ms - last_fire_start_ms) > TRIGGER_PULSE_MS) {
      trigger_servo_fire(false);
    }
  }
}

// -------------------------
// UDP JSON
// -------------------------
static bool decode_message(char *buffer, size_t len, DynamicJsonDocument &doc) {
  DeserializationError err = deserializeJson(doc, buffer, len);
  if (err) {
    return false;
  }

  if (!doc.containsKey("crc")) {
    return false;
  }

  const char *crc_str = doc["crc"];
  doc.remove("crc");

  String compact;
  serializeJson(doc, compact);
  uint32_t crc = crc32_compute((const uint8_t *)compact.c_str(), compact.length());

  char calc[9];
  snprintf(calc, sizeof(calc), "%08x", (unsigned int)crc);
  if (strcasecmp(calc, crc_str) != 0) {
    return false;
  }

  return true;
}

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

static void send_ack(int seq, bool ok, IPAddress ip, uint16_t port) {
  StaticJsonDocument<512> doc;
  doc["v"] = 1;
  doc["t"] = "ack";
  doc["seq"] = seq;
  doc["ts"] = (uint32_t)now_ms();
  doc["ok"] = ok;

  JsonObject state = doc.createNestedObject("state");
  state["pan"] = target_pan;
  state["tilt"] = target_tilt;
  state["fire"] = fire_active ? 1 : 0;
  state["safety"] = safety_state;
  state["mode"] = trigger_cfg.mode;
  state["current_fault"] = current_fault;

  encode_and_send(doc, ip, port);
}

static void send_caps(IPAddress ip, uint16_t port) {
  StaticJsonDocument<768> doc;
  doc["v"] = 1;
  doc["t"] = "cap";
  doc["seq"] = 0;
  doc["ts"] = (uint32_t)now_ms();

  JsonObject caps = doc.createNestedObject("p");
  caps["proto"] = 1;
  caps["fw"] = "db3000-esp32-udp-v1";

  JsonObject pins = caps.createNestedObject("pins");
  pins["uart_rx"] = PIN_UART_RX;
  pins["uart_tx"] = PIN_UART_TX;
  pins["pan_pwm"] = PIN_PAN_SERVO;
  pins["tilt_pwm"] = PIN_TILT_SERVO;
  pins["mosfet"] = PIN_TRIGGER_MOSFET;
  pins["trigger_servo"] = PIN_TRIGGER_SERVO;
  pins["led"] = PIN_LED_RELAY;
  pins["laser"] = PIN_LASER_RELAY;
  pins["curr_pan"] = PIN_CURR_PAN;
  pins["curr_tilt"] = PIN_CURR_TILT;
  pins["curr_total"] = PIN_CURR_TOTAL;

  encode_and_send(doc, ip, port);
}

static void send_state(IPAddress ip, uint16_t port) {
  StaticJsonDocument<768> doc;
  doc["v"] = 1;
  doc["t"] = "state";
  doc["seq"] = 0;
  doc["ts"] = (uint32_t)now_ms();

  JsonObject state = doc.createNestedObject("p");
  state["pan"] = target_pan;
  state["tilt"] = target_tilt;
  state["fire"] = fire_active ? 1 : 0;
  state["safety"] = safety_state;
  state["mode"] = trigger_cfg.mode;
  state["current_fault"] = current_fault;

  JsonObject currents = state.createNestedObject("current_mA");
  currents["pan"] = read_current_mA(PIN_CURR_PAN, PAN_MA_PER_ADC);
  currents["tilt"] = read_current_mA(PIN_CURR_TILT, TILT_MA_PER_ADC);
  currents["total"] = read_current_mA(PIN_CURR_TOTAL, TOTAL_MA_PER_ADC);

  encode_and_send(doc, ip, port);
}

// -------------------------
// Command handling
// -------------------------
static void apply_config(JsonObject cfg) {
  if (cfg.containsKey("limits")) {
    JsonObject lim = cfg["limits"];
    limits_cfg.pan_min = lim["pan_min"] | limits_cfg.pan_min;
    limits_cfg.pan_max = lim["pan_max"] | limits_cfg.pan_max;
    limits_cfg.tilt_min = lim["tilt_min"] | limits_cfg.tilt_min;
    limits_cfg.tilt_max = lim["tilt_max"] | limits_cfg.tilt_max;
  }

  if (cfg.containsKey("home")) {
    JsonObject home = cfg["home"];
    home_cfg.pan = home["pan"] | home_cfg.pan;
    home_cfg.tilt = home["tilt"] | home_cfg.tilt;
    home_cfg.speed = home["speed"] | home_cfg.speed;
    home_cfg.max_speed_dps = home["max_speed_dps"] | home_cfg.max_speed_dps;
  }

  if (cfg.containsKey("trigger")) {
    JsonObject trig = cfg["trigger"];
    trigger_cfg.mode = trig["mode"] | trigger_cfg.mode;
    trigger_cfg.cooldown_s = trig["cooldown_s"] | trigger_cfg.cooldown_s;
    trigger_cfg.max_fire_s = trig["max_fire_s"] | trigger_cfg.max_fire_s;
  }

  if (cfg.containsKey("rapid_fire")) {
    JsonObject rf = cfg["rapid_fire"];
    rapid_cfg.enabled = rf["enabled"] | rapid_cfg.enabled;
    rapid_cfg.rate_hz = rf["rate_hz"] | rapid_cfg.rate_hz;
    rapid_cfg.duty = rf["duty"] | rapid_cfg.duty;
  }

  if (cfg.containsKey("current_protection")) {
    JsonObject cp = cfg["current_protection"];
    current_cfg.enabled = cp["enabled"] | current_cfg.enabled;
    current_cfg.block_fire = cp["block_fire"] | current_cfg.block_fire;
    current_cfg.block_motion = cp["block_motion"] | current_cfg.block_motion;
    current_cfg.latch = cp["latch"] | current_cfg.latch;
    current_cfg.trip_pan_mA = cp["trip_pan_mA"] | current_cfg.trip_pan_mA;
    current_cfg.trip_tilt_mA = cp["trip_tilt_mA"] | current_cfg.trip_tilt_mA;
    current_cfg.trip_total_mA = cp["trip_total_mA"] | current_cfg.trip_total_mA;
    current_cfg.trip_hold_ms = cp["trip_hold_ms"] | current_cfg.trip_hold_ms;
    current_cfg.clear_hold_ms = cp["clear_hold_ms"] | current_cfg.clear_hold_ms;
    current_cfg.hysteresis_mA = cp["hysteresis_mA"] | current_cfg.hysteresis_mA;
  }

  if (cfg.containsKey("tilt_safety")) {
    JsonObject ts = cfg["tilt_safety"];
    tilt_safety_cfg.installed = ts["installed"] | tilt_safety_cfg.installed;
    tilt_safety_cfg.enabled = ts["enabled"] | tilt_safety_cfg.enabled;
  }
}

static void apply_command(JsonObject payload) {
  if (payload.containsKey("safety")) {
    safety_state = payload["safety"];
  }
  if (payload.containsKey("led")) {
    led_state = payload["led"];
  }
  if (payload.containsKey("laser")) {
    laser_state = payload["laser"];
  }
  if (payload.containsKey("mode")) {
    trigger_cfg.mode = payload["mode"];
  }

  if (payload.containsKey("fire_hold")) {
    fire_hold = payload["fire_hold"];
  }
  if (payload.containsKey("fire")) {
    fire_request = payload["fire"];
  }

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

  target_pan = clamp_int(target_pan, limits_cfg.pan_min, limits_cfg.pan_max);
  target_tilt = clamp_int(target_tilt, limits_cfg.tilt_min, limits_cfg.tilt_max);

  if (payload.containsKey("rapid_fire")) {
    JsonObject rf = payload["rapid_fire"];
    rapid_cfg.enabled = rf["enabled"] | rapid_cfg.enabled;
    rapid_cfg.rate_hz = rf["rate_hz"] | rapid_cfg.rate_hz;
    rapid_cfg.duty = rf["duty"] | rapid_cfg.duty;
  }
}

static void process_packet(char *buffer, size_t len, IPAddress ip, uint16_t port) {
  DynamicJsonDocument doc(2048);
  if (!decode_message(buffer, len, doc)) {
    return;
  }

  const char *type = doc["t"] | "";
  int seq = doc["seq"] | 0;

  if (strcmp(type, "hello") == 0) {
    send_ack(seq, true, ip, port);
    send_caps(ip, port);
    return;
  }

  if (strcmp(type, "hb") == 0) {
    // Heartbeat: optionally reply with state
    send_state(ip, port);
    return;
  }

  if (strcmp(type, "cmd") == 0) {
    JsonObject payload = doc["p"].as<JsonObject>();
    if (payload.containsKey("action")) {
      const char *action = payload["action"] | "";
      if (strcmp(action, "config") == 0) {
        apply_config(payload);
        send_ack(seq, true, ip, port);
      } else if (strcmp(action, "encoder_request") == 0) {
        send_ack(seq, true, ip, port);
        send_state(ip, port);
      } else {
        send_ack(seq, false, ip, port);
      }
    } else {
      apply_command(payload);
      send_ack(seq, true, ip, port);
    }
  }
}

// -------------------------
// Setup / Loop
// -------------------------
void setup() {
  Serial.begin(115200);

  // Outputs
  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  pinMode(PIN_LED_RELAY, OUTPUT);
  pinMode(PIN_LASER_RELAY, OUTPUT);

  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  digitalWrite(PIN_LED_RELAY, LOW);
  digitalWrite(PIN_LASER_RELAY, LOW);

  // PWM
  ledcAttach(PIN_PAN_SERVO, SERVO_HZ, SERVO_RES_BITS);
  ledcAttach(PIN_TILT_SERVO, SERVO_HZ, SERVO_RES_BITS);
  ledcAttach(PIN_TRIGGER_SERVO, SERVO_HZ, SERVO_RES_BITS);

  servo_write_deg(PIN_PAN_SERVO, home_cfg.pan);
  servo_write_deg(PIN_TILT_SERVO, home_cfg.tilt);
  servo_write_deg(PIN_TRIGGER_SERVO, TRIGGER_SERVO_REST_DEG);

  analogReadResolution(12);
  analogSetPinAttenuation(PIN_CURR_PAN, ADC_11db);
  analogSetPinAttenuation(PIN_CURR_TILT, ADC_11db);
  analogSetPinAttenuation(PIN_CURR_TOTAL, ADC_11db);

  // WiFi AP
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(AP_IP, AP_GW, AP_MASK);
  WiFi.softAP(WIFI_SSID, WIFI_PASS);

  Udp.begin(UDP_PORT);
  last_cmd_ms = now_ms();
}

void loop() {
  uint32_t now = now_ms();

  int packet_size = Udp.parsePacket();
  if (packet_size > 0) {
    static char buffer[2048];
    int len = Udp.read(buffer, sizeof(buffer) - 1);
    if (len > 0) {
      buffer[len] = '\0';
      last_remote_ip = Udp.remoteIP();
      last_remote_port = Udp.remotePort();
      last_cmd_ms = now;
      process_packet(buffer, (size_t)len, last_remote_ip, last_remote_port);
    }
  }

  // Current protection
  int pan_mA = read_current_mA(PIN_CURR_PAN, PAN_MA_PER_ADC);
  int tilt_mA = read_current_mA(PIN_CURR_TILT, TILT_MA_PER_ADC);
  int total_mA = read_current_mA(PIN_CURR_TOTAL, TOTAL_MA_PER_ADC);

  bool over_pan = (current_cfg.trip_pan_mA > 0) && (pan_mA >= current_cfg.trip_pan_mA);
  bool over_tilt = (current_cfg.trip_tilt_mA > 0) && (tilt_mA >= current_cfg.trip_tilt_mA);
  bool over_total = (current_cfg.trip_total_mA > 0) && (total_mA >= current_cfg.trip_total_mA);
  bool over_any = over_pan || over_tilt || over_total;

  if (current_cfg.enabled) {
    if (over_any) {
      if (trip_start_ms == 0) {
        trip_start_ms = now;
      }
      if ((now - trip_start_ms) >= (uint32_t)current_cfg.trip_hold_ms) {
        current_fault = true;
      }
    } else {
      trip_start_ms = 0;
      if (!current_cfg.latch) {
        current_fault = false;
      } else if (current_fault) {
        int clear_pan = current_cfg.trip_pan_mA - current_cfg.hysteresis_mA;
        int clear_tilt = current_cfg.trip_tilt_mA - current_cfg.hysteresis_mA;
        int clear_total = current_cfg.trip_total_mA - current_cfg.hysteresis_mA;
        bool clear_ok = true;
        if (current_cfg.trip_pan_mA > 0 && pan_mA > clear_pan) clear_ok = false;
        if (current_cfg.trip_tilt_mA > 0 && tilt_mA > clear_tilt) clear_ok = false;
        if (current_cfg.trip_total_mA > 0 && total_mA > clear_total) clear_ok = false;
        if (clear_ok && (now - trip_start_ms) >= (uint32_t)current_cfg.clear_hold_ms) {
          current_fault = false;
        }
      }
    }
  } else {
    current_fault = false;
  }

  bool fire_blocked = (safety_state != 0) || (current_fault && current_cfg.block_fire);
  bool motion_blocked = (current_fault && current_cfg.block_motion);

  update_motion_outputs(motion_blocked);
  update_accessories();
  update_fire_outputs(now, fire_blocked);

  // Link timeout safety: stop firing if no recent commands
  if ((now - last_cmd_ms) > 1000) {
    fire_request = 0;
  }

  // Periodic state broadcast
  if (last_remote_port != 0 && (now - last_state_ms) > 250) {
    last_state_ms = now;
    send_state(last_remote_ip, last_remote_port);
  }
}
