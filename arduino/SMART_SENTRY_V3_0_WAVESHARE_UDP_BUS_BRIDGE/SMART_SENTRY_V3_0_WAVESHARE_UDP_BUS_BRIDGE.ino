// Smart Sentry v3.0 Waveshare UDP Bus Bridge
// Phase 1 bench scaffold: receives UDP JSON, emits Yahboom-style motion packets
// for pan and tilt, and directly drives the confirmed header-backed accessories.

#include <ctype.h>
#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>

enum BusChecksumMode {
  BUS_CHK_SUB = 0,
  BUS_CHK_XOR = 1,
};

static const char *WIFI_SSID = "WAVESHARE-ESP32";
static const char *WIFI_PASS = "smartv3pass";
static const IPAddress AP_IP(192, 168, 4, 1);
static const IPAddress AP_GW(192, 168, 4, 1);
static const IPAddress AP_MASK(255, 255, 255, 0);
static const uint16_t UDP_PORT = 9000;
static const bool WIFI_STABILITY_TEST_MODE = true;
static const uint32_t BUS_BAUD_NORMAL = 1000000;
static const uint32_t BUS_BAUD_TEST = 250000;

static const int PIN_UART_RX = 18;
static const int PIN_UART_TX = 19;
static const uint32_t BUS_BAUD = WIFI_STABILITY_TEST_MODE ? BUS_BAUD_TEST : BUS_BAUD_NORMAL;
static const int PIN_RC_UART_RX = 15;
static const int PIN_RC_UART_TX = 14;
static const uint32_t RC_BAUD = 115200;
static const bool RC_INPUT_ENABLED = false;
static const uint32_t RC_FRAME_TIMEOUT_MS = 500;
static const uint32_t RC_STUB_HOLD_MS = 2500;
static const uint8_t RC_IBUS_FRAME_LEN = 0x20;
static const uint8_t RC_IBUS_FRAME_CMD = 0x40;
static const uint16_t RC_PULSE_MIN_US = 1000;
static const uint16_t RC_PULSE_CENTER_US = 1500;
static const uint16_t RC_PULSE_MAX_US = 2000;
static const uint16_t RC_STICK_DEADBAND_US = 45;
static const uint16_t RC_SWITCH_OFF_THRESHOLD_US = 1400;
static const uint16_t RC_SWITCH_ON_THRESHOLD_US = 1600;
static const uint32_t RC_MOTION_APPLY_INTERVAL_MS = 60;
static const uint16_t RC_MOVE_TIME_MS = 80;
static const int PIN_TRIGGER_MOSFET = 27;
static const int PIN_ACC_RELAY = 25;
static const int PIN_SPARE_RELAY = 26;
static const int PIN_BUZZER = 4;
static const int PIN_LED_RELAY = -1;
static const int PIN_LASER_RELAY = -1;
static const int PIN_TRIGGER_SERVO_PWM = -1;
static const int BUZZER_PWM_RES_BITS = 10;
static const int TRIGGER_SERVO_PWM_RES_BITS = 16;
static const bool LED_RELAY_ASSIGNED = false;
static const bool LASER_RELAY_ASSIGNED = false;
static const bool TRIGGER_SERVO_ASSIGNED = false;
static const bool BUZZER_VOLUME_ASSIGNED = false;
static const bool SPEAKER_VOLUME_ASSIGNED = false;
static const bool SPEAKER_SUPPORTED = false;

enum ControlSourceMode {
  CONTROL_SOURCE_APP = 0,
  CONTROL_SOURCE_RC = 1,
  CONTROL_SOURCE_AUTO = 2,
};

static const uint8_t BUS_ID_PAN = 1;
static const uint8_t BUS_ID_TILT = 2;
static const uint8_t BUS_ID_ACCESSORY = 4;
static const uint8_t REG_GOAL_POSITION = 0x2A;
static const uint8_t BUS_INST_PING = 0x01;
static const uint8_t BUS_INST_WRITE = 0x03;
static const uint8_t BUS_LEN_PING = 0x02;
static const uint8_t BUS_LEN_WRITE_POS = 0x07;
static const uint32_t BUS_PING_TIMEOUT_MS = 120;

static const int PAN_MIN_DEG = 0;
static const int PAN_MAX_DEG = 220;
static const int TILT_MIN_DEG = 0;
static const int TILT_MAX_DEG = 70;
static const int PAN_CENTER_DEG = 90;
static const int TILT_CENTER_DEG = 35;

struct BusMotionRequest {
  bool pending;
  uint8_t servoId;
  int deg;
  uint16_t moveTimeMs;
  int minDeg;
  int maxDeg;
};

struct BusPingWaitResult {
  bool panSubOk;
  bool panXorOk;
  bool tiltSubOk;
  bool tiltXorOk;
};

WiFiUDP udp;
HardwareSerial busSerial(2);
HardwareSerial rcSerial(1);

static int targetPanDeg = 90;
static int targetTiltDeg = 35;
static int lastMoveTimeMs = 120;
static int fireState = 0;
static int safetyState = 1;
static int triggerMode = 0;
static int ledState = 0;
static int laserState = 0;
static int accState = 0;
static int spareState = 0;
static IPAddress lastClientIp;
static uint16_t lastClientPort = 0;
static uint32_t triggerPulseMs = 120;
static bool projectilePulseActive = false;
static uint32_t projectilePulseStartMs = 0;
static bool buzzerPwmReady = false;
static bool triggerServoPwmReady = false;
static int triggerServoRestDeg = 0;
static int triggerServoFireDeg = 45;
static int triggerServoCurrentDeg = 0;
static int triggerServoTargetDeg = 0;
static int triggerServoSpeedDps = 360;
static uint32_t triggerServoLastUpdateMs = 0;
static bool soundActive = false;
static uint32_t soundEndMs = 0;
static bool busLastPingPanSubOk = false;
static bool busLastPingPanXorOk = false;
static bool busLastPingTiltSubOk = false;
static bool busLastPingTiltXorOk = false;
static ControlSourceMode controlSourceMode = CONTROL_SOURCE_APP;
static bool rcLinkActive = false;
static bool rcOverrideActive = false;
static bool rcFailsafeActive = false;
static uint32_t rcFrameAgeMs = 0;
static uint16_t rcChannelUs[6] = {1500, 1500, 1000, 1000, 1000, 1000};
static uint8_t rcLastFrameCounter = 0;
static uint32_t rcLastFrameMs = 0;
static uint32_t rcStubUntilMs = 0;
static bool rcLiveSignalSeen = false;
static uint8_t rcFrameBuffer[RC_IBUS_FRAME_LEN];
static uint8_t rcFrameBufferPos = 0;
static uint32_t rcLastMotionApplyMs = 0;
static bool rcLastFireRequest = false;
static uint32_t lastNetDiagMs = 0;
static portMUX_TYPE busStateMux = portMUX_INITIALIZER_UNLOCKED;
static TaskHandle_t busTaskHandle = nullptr;
static BusMotionRequest pendingPanMotion = {false, BUS_ID_PAN, PAN_CENTER_DEG, 120, PAN_MIN_DEG, PAN_MAX_DEG};
static BusMotionRequest pendingTiltMotion = {false, BUS_ID_TILT, TILT_CENTER_DEG, 120, TILT_MIN_DEG, TILT_MAX_DEG};
static bool busPingBusy = false;
static uint32_t busPingNextRequestId = 1;
static uint32_t busPingPendingRequestId = 0;
static uint32_t busPingResultRequestId = 0;
static BusPingWaitResult busPingResultState = {false, false, false, false};

static void busTask(void *pvParameters);
static void queueBusMotionPacket(uint8_t servoId, int deg, uint16_t moveTimeMs, int minDeg, int maxDeg);
static bool takePendingBusMotion(uint8_t servoId, BusMotionRequest *requestOut);
static uint32_t requestBusPing();
static bool takePendingBusPingRequest(uint32_t *requestIdOut);
static void completeBusPingRequest(uint32_t requestId, const BusPingWaitResult &result);
static bool waitForBusPingResult(uint32_t requestId, uint32_t timeoutMs, BusPingWaitResult *resultOut);

static const char *controlSourceModeName(ControlSourceMode mode) {
  if (mode == CONTROL_SOURCE_RC) return "rc";
  if (mode == CONTROL_SOURCE_AUTO) return "auto";
  return "app";
}

static const char *activeControlSourceName() {
  if (!RC_INPUT_ENABLED) return "app";
  if (controlSourceMode == CONTROL_SOURCE_RC && rcLinkActive) return "rc";
  if (controlSourceMode == CONTROL_SOURCE_AUTO && rcLinkActive && rcOverrideActive) return "rc";
  return "app";
}

static bool parseControlSourceMode(const char *text, ControlSourceMode *modeOut) {
  if (text == nullptr || modeOut == nullptr) return false;
  if (strcmp(text, "app") == 0) {
    *modeOut = CONTROL_SOURCE_APP;
    return true;
  }
  if (strcmp(text, "rc") == 0 || strcmp(text, "flysky") == 0) {
    *modeOut = CONTROL_SOURCE_RC;
    return true;
  }
  if (strcmp(text, "auto") == 0) {
    *modeOut = CONTROL_SOURCE_AUTO;
    return true;
  }
  return false;
}

static bool isRcPulseValid(uint16_t pulseUs) {
  return pulseUs >= 800 && pulseUs <= 2200;
}

static bool isRcSwitchHigh(uint16_t pulseUs) {
  return pulseUs >= RC_SWITCH_ON_THRESHOLD_US;
}

static bool isRcSwitchLow(uint16_t pulseUs) {
  return pulseUs <= RC_SWITCH_OFF_THRESHOLD_US;
}

static bool isRcControlActive() {
  if (!RC_INPUT_ENABLED) return false;
  return strcmp(activeControlSourceName(), "rc") == 0;
}

static int mapRcAxisToDegrees(uint16_t pulseUs, int minDeg, int centerDeg, int maxDeg, int holdDeg) {
  if (!isRcPulseValid(pulseUs)) return holdDeg;

  int lowDeadband = (int)RC_PULSE_CENTER_US - (int)RC_STICK_DEADBAND_US;
  int highDeadband = (int)RC_PULSE_CENTER_US + (int)RC_STICK_DEADBAND_US;
  if ((int)pulseUs >= lowDeadband && (int)pulseUs <= highDeadband) {
    return holdDeg;
  }

  if ((int)pulseUs < lowDeadband) {
    long numer = (long)((int)pulseUs - (int)RC_PULSE_MIN_US);
    long denom = (long)(lowDeadband - (int)RC_PULSE_MIN_US);
    if (denom <= 0) return minDeg;
    numer = constrain(numer, 0L, denom);
    return minDeg + (int)((numer * (long)(centerDeg - minDeg)) / denom);
  }

  long numer = (long)((int)pulseUs - highDeadband);
  long denom = (long)((int)RC_PULSE_MAX_US - highDeadband);
  if (denom <= 0) return maxDeg;
  numer = constrain(numer, 0L, denom);
  return centerDeg + (int)((numer * (long)(maxDeg - centerDeg)) / denom);
}

static void updateRcOverrideState() {
  bool previousOverride = rcOverrideActive;
  bool nextOverride = false;

  if (rcLinkActive && !rcFailsafeActive) {
    if (controlSourceMode == CONTROL_SOURCE_RC) {
      nextOverride = true;
    } else if (controlSourceMode == CONTROL_SOURCE_AUTO) {
      if (isRcSwitchHigh(rcChannelUs[5])) nextOverride = true;
      else if (isRcSwitchLow(rcChannelUs[5])) nextOverride = false;
      else nextOverride = previousOverride;
    }
  }

  rcOverrideActive = nextOverride;
  if (!rcOverrideActive) {
    rcLastFireRequest = false;
  }

  if (previousOverride && !rcOverrideActive) {
    fireState = 0;
    accState = 0;
    spareState = 0;
  }
}

static void applyRcLiveControl(uint32_t nowVal) {
  updateRcOverrideState();
  if (!rcOverrideActive) return;

  int desiredPanDeg = mapRcAxisToDegrees(rcChannelUs[0], PAN_MIN_DEG, PAN_CENTER_DEG, PAN_MAX_DEG, targetPanDeg);
  int desiredTiltDeg = mapRcAxisToDegrees(rcChannelUs[1], TILT_MIN_DEG, TILT_CENTER_DEG, TILT_MAX_DEG, targetTiltDeg);
  bool motionDue = (rcLastMotionApplyMs == 0) || ((nowVal - rcLastMotionApplyMs) >= RC_MOTION_APPLY_INTERVAL_MS);

  if (motionDue && desiredPanDeg != targetPanDeg) {
    queueBusMotionPacket(BUS_ID_PAN, desiredPanDeg, RC_MOVE_TIME_MS, PAN_MIN_DEG, PAN_MAX_DEG);
    targetPanDeg = desiredPanDeg;
    lastMoveTimeMs = RC_MOVE_TIME_MS;
    rcLastMotionApplyMs = nowVal;
  }

  if (motionDue && desiredTiltDeg != targetTiltDeg) {
    queueBusMotionPacket(BUS_ID_TILT, desiredTiltDeg, RC_MOVE_TIME_MS, TILT_MIN_DEG, TILT_MAX_DEG);
    targetTiltDeg = desiredTiltDeg;
    lastMoveTimeMs = RC_MOVE_TIME_MS;
    rcLastMotionApplyMs = nowVal;
  }

  bool fireRequest = isRcSwitchHigh(rcChannelUs[2]);
  if (triggerMode == 0) {
    fireState = fireRequest ? 1 : 0;
  } else if (fireRequest && !rcLastFireRequest && !projectilePulseActive) {
    fireState = 1;
  }
  rcLastFireRequest = fireRequest;

  accState = isRcSwitchHigh(rcChannelUs[3]) ? 1 : 0;
  spareState = isRcSwitchHigh(rcChannelUs[4]) ? 1 : 0;
}

static bool decodeIbusFrame(const uint8_t *frame, size_t len) {
  if (frame == nullptr || len != RC_IBUS_FRAME_LEN) return false;
  if (frame[0] != RC_IBUS_FRAME_LEN || frame[1] != RC_IBUS_FRAME_CMD) return false;

  uint16_t checksum = 0xFFFF;
  for (size_t i = 0; i < RC_IBUS_FRAME_LEN - 2; ++i) {
    checksum = (uint16_t)(checksum - frame[i]);
  }
  uint16_t expected = (uint16_t)frame[RC_IBUS_FRAME_LEN - 2] | ((uint16_t)frame[RC_IBUS_FRAME_LEN - 1] << 8);
  if (checksum != expected) return false;

  bool anyValidChannel = false;
  for (int i = 0; i < 6; ++i) {
    size_t offset = 2 + (size_t)(i * 2);
    uint16_t pulseUs = (uint16_t)frame[offset] | ((uint16_t)frame[offset + 1] << 8);
    if (isRcPulseValid(pulseUs)) {
      rcChannelUs[i] = pulseUs;
      anyValidChannel = true;
    }
  }
  return anyValidChannel;
}

static void updateRcRuntime(uint32_t nowVal) {
  if (!RC_INPUT_ENABLED) {
    rcLinkActive = false;
    rcOverrideActive = false;
    rcFailsafeActive = false;
    rcFrameAgeMs = 0;
    return;
  }

  while (rcSerial.available() > 0) {
    uint8_t value = (uint8_t)rcSerial.read();
    if (rcFrameBufferPos == 0) {
      if (value != RC_IBUS_FRAME_LEN) continue;
      rcFrameBuffer[rcFrameBufferPos++] = value;
      continue;
    }
    if (rcFrameBufferPos == 1) {
      if (value != RC_IBUS_FRAME_CMD) {
        rcFrameBufferPos = 0;
        continue;
      }
      rcFrameBuffer[rcFrameBufferPos++] = value;
      continue;
    }

    rcFrameBuffer[rcFrameBufferPos++] = value;
    if (rcFrameBufferPos >= RC_IBUS_FRAME_LEN) {
      rcFrameBufferPos = 0;
      if (decodeIbusFrame(rcFrameBuffer, RC_IBUS_FRAME_LEN)) {
        rcLastFrameCounter++;
        rcLastFrameMs = nowVal;
        rcStubUntilMs = 0;
        rcLiveSignalSeen = true;
        rcLinkActive = true;
        rcFailsafeActive = false;
      }
    }
  }

  if (rcLastFrameMs > 0) {
    rcFrameAgeMs = nowVal - rcLastFrameMs;
  } else {
    rcFrameAgeMs = 0;
  }

  if (rcStubUntilMs > nowVal) {
    return;
  }

  if (rcLastFrameMs == 0) {
    rcLinkActive = false;
    rcFailsafeActive = rcLiveSignalSeen;
    updateRcOverrideState();
    return;
  }

  if (rcFrameAgeMs > RC_FRAME_TIMEOUT_MS) {
    rcLinkActive = false;
    rcFailsafeActive = true;
  } else {
    rcLinkActive = true;
    rcFailsafeActive = false;
  }
  updateRcOverrideState();
}

static uint32_t crc32_update(uint32_t crc, const uint8_t *data, size_t length) {
  uint32_t value = crc;
  for (size_t i = 0; i < length; ++i) {
    value ^= (uint32_t)data[i];
    for (int bit = 0; bit < 8; ++bit) {
      value = (value & 1U) ? ((value >> 1) ^ 0xEDB88320UL) : (value >> 1);
    }
  }
  return value;
}

static uint32_t crc32_bytes(const uint8_t *data, size_t length) {
  return crc32_update(0xFFFFFFFFUL, data, length) ^ 0xFFFFFFFFUL;
}

static void serialPrintTextPreview(const char *text, size_t len, size_t maxLen) {
  if (text == nullptr || len == 0) {
    Serial.print("<empty>");
    return;
  }
  size_t limit = len < maxLen ? len : maxLen;
  for (size_t i = 0; i < limit; ++i) {
    char c = text[i];
    if (c >= 32 && c <= 126) Serial.print(c);
    else Serial.print('.');
  }
  if (len > limit) Serial.print("...");
}

static uint32_t crc32_json_without_crc(JsonDocument &doc) {
  doc.remove("crc");
  char buffer[1024];
  size_t used = serializeJson(doc, buffer, sizeof(buffer));
  return crc32_bytes((const uint8_t *)buffer, used);
}

static bool parse_crc32_hex(const char *text, uint32_t *valueOut) {
  if (text == nullptr || valueOut == nullptr) return false;
  uint32_t value = 0;
  int digits = 0;
  while (*text != '\0') {
    char c = *text++;
    int nibble = -1;
    if (c >= '0' && c <= '9') nibble = c - '0';
    else if (c >= 'a' && c <= 'f') nibble = 10 + (c - 'a');
    else if (c >= 'A' && c <= 'F') nibble = 10 + (c - 'A');
    else return false;
    value = (value << 4) | (uint32_t)nibble;
    digits++;
  }
  if (digits <= 0 || digits > 8) return false;
  *valueOut = value;
  return true;
}

static void encodeAndSend(JsonDocument &doc, IPAddress ip, uint16_t port) {
  doc.remove("crc");
  char raw[2048];
  size_t rawLen = serializeJson(doc, raw, sizeof(raw));
  uint32_t crc = crc32_bytes((const uint8_t *)raw, rawLen);
  char crcText[9];
  snprintf(crcText, sizeof(crcText), "%08lx", (unsigned long)crc);
  doc["crc"] = crcText;
  char message[2048];
  size_t messageLen = serializeJson(doc, message, sizeof(message));
  Serial.printf("[UDP-TX] %s:%u %u bytes type=%s seq=%d preview=",
                ip.toString().c_str(),
                port,
                (unsigned)messageLen,
                doc["t"] | "?",
                (int)(doc["seq"] | -1));
  serialPrintTextPreview(message, messageLen, 180);
  Serial.println();
  udp.beginPacket(ip, port);
  udp.write((const uint8_t *)message, messageLen);
  udp.endPacket();
}

static void sendAck(int seq, bool ok, IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"] = 1;
  doc["t"] = "ack";
  doc["seq"] = seq;
  doc["ts"] = (uint32_t)millis();
  doc["ok"] = ok;
  JsonObject p = doc["p"].to<JsonObject>();
  p["pan"] = targetPanDeg;
  p["tilt"] = targetTiltDeg;
  p["fire"] = fireState;
  p["safety"] = safetyState;
  p["led"] = ledState;
  p["laser"] = laserState;
  p["acc"] = accState;
  p["spare"] = spareState;
  p["control_source_mode"] = controlSourceModeName(controlSourceMode);
  p["control_source_active"] = activeControlSourceName();
  p["rc_link_active"] = rcLinkActive ? 1 : 0;
  p["rc_override_active"] = rcOverrideActive ? 1 : 0;
  p["rc_failsafe_active"] = rcFailsafeActive ? 1 : 0;
  p["rc_frame_age_ms"] = rcFrameAgeMs;
  JsonObject rc = p["rc"].to<JsonObject>();
  rc["receiver_model"] = "flysky_fs_ia6";
  rc["link_active"] = rcLinkActive;
  rc["override_active"] = rcOverrideActive;
  rc["failsafe_active"] = rcFailsafeActive;
  rc["frame_age_ms"] = rcFrameAgeMs;
  rc["signal_validated"] = rcLiveSignalSeen;
  rc["ch1_us"] = rcChannelUs[0];
  rc["ch2_us"] = rcChannelUs[1];
  rc["ch3_us"] = rcChannelUs[2];
  rc["ch4_us"] = rcChannelUs[3];
  rc["ch5_us"] = rcChannelUs[4];
  rc["ch6_us"] = rcChannelUs[5];
  JsonObject bus = p["bus"].to<JsonObject>();
  bus["pan_sub_ok"] = busLastPingPanSubOk;
  bus["pan_xor_ok"] = busLastPingPanXorOk;
  bus["tilt_sub_ok"] = busLastPingTiltSubOk;
  bus["tilt_xor_ok"] = busLastPingTiltXorOk;
  encodeAndSend(doc, ip, port);
}

static void sendState(IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"] = 1;
  doc["t"] = "state";
  doc["ts"] = (uint32_t)millis();
  JsonObject p = doc["p"].to<JsonObject>();
  p["pan"] = targetPanDeg;
  p["tilt"] = targetTiltDeg;
  p["fire"] = fireState;
  p["safety"] = safetyState;
  p["mode"] = triggerMode;
  p["led"] = ledState;
  p["laser"] = laserState;
  p["acc"] = accState;
  p["spare"] = spareState;
  p["control_source_mode"] = controlSourceModeName(controlSourceMode);
  p["control_source_active"] = activeControlSourceName();
  p["rc_link_active"] = rcLinkActive ? 1 : 0;
  p["rc_override_active"] = rcOverrideActive ? 1 : 0;
  p["rc_failsafe_active"] = rcFailsafeActive ? 1 : 0;
  p["rc_frame_age_ms"] = rcFrameAgeMs;
  JsonObject rc = p["rc"].to<JsonObject>();
  rc["receiver_model"] = "flysky_fs_ia6";
  rc["link_active"] = rcLinkActive;
  rc["override_active"] = rcOverrideActive;
  rc["failsafe_active"] = rcFailsafeActive;
  rc["frame_age_ms"] = rcFrameAgeMs;
  rc["signal_validated"] = rcLiveSignalSeen;
  rc["ch1_us"] = rcChannelUs[0];
  rc["ch2_us"] = rcChannelUs[1];
  rc["ch3_us"] = rcChannelUs[2];
  rc["ch4_us"] = rcChannelUs[3];
  rc["ch5_us"] = rcChannelUs[4];
  rc["ch6_us"] = rcChannelUs[5];
  JsonObject runtime = p["runtime"].to<JsonObject>();
  runtime["source"] = "esp32-state";
  runtime["bus_baud"] = (uint32_t)BUS_BAUD;
  runtime["id_pan"] = BUS_ID_PAN;
  runtime["id_tilt"] = BUS_ID_TILT;
  runtime["id_accessory"] = BUS_ID_ACCESSORY;
  runtime["sound"] = soundActive;
  runtime["header_reference_locked"] = true;
  runtime["control_source_mode"] = controlSourceModeName(controlSourceMode);
  runtime["control_source_active"] = activeControlSourceName();
  runtime["rc_receiver_model"] = "flysky_fs_ia6";
  runtime["rc_signal_validated"] = rcLiveSignalSeen;
  runtime["rc_link_active"] = rcLinkActive;
  runtime["rc_override_active"] = rcOverrideActive;
  runtime["rc_failsafe_active"] = rcFailsafeActive;
  runtime["rc_frame_age_ms"] = rcFrameAgeMs;
  JsonObject bus = p["bus"].to<JsonObject>();
  bus["pan_sub_ok"] = busLastPingPanSubOk;
  bus["pan_xor_ok"] = busLastPingPanXorOk;
  bus["tilt_sub_ok"] = busLastPingTiltSubOk;
  bus["tilt_xor_ok"] = busLastPingTiltXorOk;
  encodeAndSend(doc, ip, port);
}

static void sendCaps(IPAddress ip, uint16_t port) {
  JsonDocument doc;
  doc["v"] = 1;
  doc["t"] = "cap";
  doc["ts"] = (uint32_t)millis();
  JsonObject p = doc["p"].to<JsonObject>();
  p["role"] = "waveshare-v3-bridge";
  p["udp_port"] = UDP_PORT;
  p["bus_baud"] = (uint32_t)BUS_BAUD;
  p["id_pan"] = BUS_ID_PAN;
  p["id_tilt"] = BUS_ID_TILT;
  p["id_accessory"] = BUS_ID_ACCESSORY;
  p["sound_supported"] = true;
  p["raw_payload_supported"] = true;
  p["bus_ping_supported"] = true;
  p["switch_supported"] = false;
  p["rc_input_supported"] = RC_INPUT_ENABLED;
  p["rc_input_planned"] = RC_INPUT_ENABLED ? "active" : "reserved_header_pin_10_gpio15_rx";
  p["rc_input_protocol"] = RC_INPUT_ENABLED ? "ibus_serial" : "disabled";
  p["rc_input_transport"] = RC_INPUT_ENABLED ? "header_pin_10_gpio15_rx" : "disabled";
  p["rc_input_tx_reserved"] = RC_INPUT_ENABLED ? "header_pin_8_gpio14" : "disabled";
  p["rc_mode_supported"] = RC_INPUT_ENABLED;
  p["rc_mode_default"] = "app";
  p["rc_receiver_model"] = "flysky_fs_ia6";
  p["rc_receiver_transport_validated"] = RC_INPUT_ENABLED && rcLiveSignalSeen;
  p["rc_live_decode_enabled"] = RC_INPUT_ENABLED;
  p["rc_source_switch_channel"] = 6;
  p["rc_board_switch_required"] = false;
  p["rc_board_switch_note"] = "use_flysky_ch6_for_local_mode_select_before_adding_extra_board_switch";
  p["rc_fire_requires_hw_switch"] = false;
  p["rc_runtime_stub_supported"] = true;
  p["speaker_supported"] = SPEAKER_SUPPORTED;
  p["led_relay_assigned"] = LED_RELAY_ASSIGNED;
  p["laser_relay_assigned"] = LASER_RELAY_ASSIGNED;
  p["trigger_servo_assigned"] = TRIGGER_SERVO_ASSIGNED;
  p["buzzer_volume_assigned"] = BUZZER_VOLUME_ASSIGNED;
  p["speaker_volume_assigned"] = SPEAKER_VOLUME_ASSIGNED;
  p["header_reference_locked"] = true;
  JsonArray unassigned = p["unassigned_outputs"].to<JsonArray>();
  unassigned.add("led_relay");
  unassigned.add("laser_relay");
  unassigned.add("trigger_servo_pwm");
  unassigned.add("buzzer_volume_adc");
  unassigned.add("speaker_volume_adc");
  JsonArray reserved = p["reserved_outputs"].to<JsonArray>();
  reserved.add("uart_rx_header_10_rc_input");
  reserved.add("uart_tx_header_8_rc_telemetry_reserved");
  if (RC_INPUT_ENABLED) {
    JsonObject rcMap = p["rc_channel_map"].to<JsonObject>();
    rcMap["ch1"] = "pan";
    rcMap["ch2"] = "tilt";
    rcMap["ch3"] = "fire_request";
    rcMap["ch4"] = "acc_relay";
    rcMap["ch5"] = "spare_relay";
    rcMap["ch6"] = "control_source_select";
    JsonArray rcNotes = p["rc_mapping_notes"].to<JsonArray>();
    rcNotes.add("software_safety_still_required_for_trigger_enable");
    rcNotes.add("flysky_ch6_is_the_recommended_local_app_vs_rc_mode_switch");
    JsonArray rcRuntimeFields = p["rc_runtime_fields"].to<JsonArray>();
    rcRuntimeFields.add("link_active");
    rcRuntimeFields.add("override_active");
    rcRuntimeFields.add("failsafe_active");
    rcRuntimeFields.add("frame_age_ms");
    rcRuntimeFields.add("ch1_us");
    rcRuntimeFields.add("ch2_us");
    rcRuntimeFields.add("ch3_us");
    rcRuntimeFields.add("ch4_us");
    rcRuntimeFields.add("ch5_us");
    rcRuntimeFields.add("ch6_us");
  }
  JsonObject pins = p["pins"].to<JsonObject>();
  pins["header_trigger_mosfet"] = 13;
  pins["header_acc_relay"] = 22;
  pins["header_spare_relay"] = 37;
  pins["header_buzzer"] = 7;
  pins["header_uart_tx_reserved"] = 8;
  pins["header_uart_rx_reserved"] = 10;
  pins["header_rc_uart_rx_planned"] = 10;
  pins["header_rc_uart_tx_reserved"] = 8;
  pins["bus_uart_rx_gpio"] = PIN_UART_RX;
  pins["bus_uart_tx_gpio"] = PIN_UART_TX;
  pins["trigger_mosfet"] = PIN_TRIGGER_MOSFET;
  pins["acc_relay"] = PIN_ACC_RELAY;
  pins["spare_relay"] = PIN_SPARE_RELAY;
  pins["buzzer"] = PIN_BUZZER;
  encodeAndSend(doc, ip, port);
}

static bool decodeMessage(char *buffer, size_t len, JsonDocument &doc) {
  DeserializationError err = deserializeJson(doc, buffer, len);
  if (err) {
    Serial.printf("[UDP-DECODE] json parse failed: %s\n", err.c_str());
    return false;
  }
  const char *type = doc["t"] | "?";
  int seq = doc["seq"] | -1;
  if (doc["crc"].isNull()) {
    Serial.printf("[UDP-DECODE] parsed type=%s seq=%d without crc\n", type, seq);
    return true;
  }
  const char *crcText = doc["crc"] | "";
  uint32_t expected = 0;
  if (!parse_crc32_hex(crcText, &expected)) {
    Serial.printf("[UDP-DECODE] bad crc text type=%s seq=%d crc=%s\n", type, seq, crcText);
    return false;
  }
  uint32_t actual = crc32_json_without_crc(doc);
  bool ok = actual == expected;
  Serial.printf("[UDP-DECODE] parsed type=%s seq=%d crc_rx=%08lx crc_calc=%08lx -> %s\n",
                type,
                seq,
                (unsigned long)expected,
                (unsigned long)actual,
                ok ? "OK" : "FAIL");
  return ok;
}

static uint8_t busChecksum(const uint8_t *data, size_t count, BusChecksumMode mode) {
  uint8_t sum = 0;
  for (size_t i = 0; i < count; ++i) sum = (uint8_t)(sum + data[i]);
  if (mode == BUS_CHK_XOR) return (uint8_t)(0xFF ^ sum);
  return (uint8_t)(~sum);
}

static int clampInt(int value, int lo, int hi) {
  if (value < lo) return lo;
  if (value > hi) return hi;
  return value;
}

static uint32_t nowMs() {
  return (uint32_t)millis();
}

static void queueBusMotionPacket(uint8_t servoId, int deg, uint16_t moveTimeMs, int minDeg, int maxDeg) {
  portENTER_CRITICAL(&busStateMux);
  BusMotionRequest *request = servoId == BUS_ID_TILT ? &pendingTiltMotion : &pendingPanMotion;
  request->pending = true;
  request->servoId = servoId;
  request->deg = deg;
  request->moveTimeMs = moveTimeMs;
  request->minDeg = minDeg;
  request->maxDeg = maxDeg;
  portEXIT_CRITICAL(&busStateMux);
}

static bool takePendingBusMotion(uint8_t servoId, BusMotionRequest *requestOut) {
  if (requestOut == nullptr) return false;
  bool haveRequest = false;
  portENTER_CRITICAL(&busStateMux);
  BusMotionRequest *request = servoId == BUS_ID_TILT ? &pendingTiltMotion : &pendingPanMotion;
  if (request->pending) {
    *requestOut = *request;
    request->pending = false;
    haveRequest = true;
  }
  portEXIT_CRITICAL(&busStateMux);
  return haveRequest;
}

static uint32_t requestBusPing() {
  uint32_t requestId = 0;
  portENTER_CRITICAL(&busStateMux);
  if (!busPingBusy && busPingPendingRequestId == 0) {
    requestId = busPingNextRequestId++;
    if (busPingNextRequestId == 0) {
      busPingNextRequestId = 1;
    }
    busPingPendingRequestId = requestId;
    busPingResultRequestId = 0;
  }
  portEXIT_CRITICAL(&busStateMux);
  return requestId;
}

static bool takePendingBusPingRequest(uint32_t *requestIdOut) {
  if (requestIdOut == nullptr) return false;
  bool accepted = false;
  portENTER_CRITICAL(&busStateMux);
  if (!busPingBusy && busPingPendingRequestId != 0) {
    *requestIdOut = busPingPendingRequestId;
    busPingPendingRequestId = 0;
    busPingBusy = true;
    accepted = true;
  }
  portEXIT_CRITICAL(&busStateMux);
  return accepted;
}

static void completeBusPingRequest(uint32_t requestId, const BusPingWaitResult &result) {
  portENTER_CRITICAL(&busStateMux);
  busPingResultState = result;
  busPingResultRequestId = requestId;
  busPingBusy = false;
  busLastPingPanSubOk = result.panSubOk;
  busLastPingPanXorOk = result.panXorOk;
  busLastPingTiltSubOk = result.tiltSubOk;
  busLastPingTiltXorOk = result.tiltXorOk;
  portEXIT_CRITICAL(&busStateMux);
}

static bool waitForBusPingResult(uint32_t requestId, uint32_t timeoutMs, BusPingWaitResult *resultOut) {
  uint32_t startMs = nowMs();
  while ((nowMs() - startMs) < timeoutMs) {
    bool ready = false;
    portENTER_CRITICAL(&busStateMux);
    if (busPingResultRequestId == requestId) {
      if (resultOut != nullptr) {
        *resultOut = busPingResultState;
      }
      busPingResultRequestId = 0;
      ready = true;
    }
    portEXIT_CRITICAL(&busStateMux);
    if (ready) {
      return true;
    }
    delay(1);
  }
  return false;
}

static void busTask(void *pvParameters) {
  (void)pvParameters;
  BusMotionRequest motion;
  for (;;) {
    bool didWork = false;

    if (takePendingBusMotion(BUS_ID_PAN, &motion)) {
      sendBusMotionPacket(motion.servoId, motion.deg, motion.moveTimeMs, motion.minDeg, motion.maxDeg);
      didWork = true;
    }

    if (takePendingBusMotion(BUS_ID_TILT, &motion)) {
      sendBusMotionPacket(motion.servoId, motion.deg, motion.moveTimeMs, motion.minDeg, motion.maxDeg);
      didWork = true;
    }

    uint32_t busPingRequestId = 0;
    if (takePendingBusPingRequest(&busPingRequestId)) {
      BusPingWaitResult result = {
        busTryPing(BUS_ID_PAN, BUS_CHK_SUB, BUS_PING_TIMEOUT_MS),
        busTryPing(BUS_ID_PAN, BUS_CHK_XOR, BUS_PING_TIMEOUT_MS),
        busTryPing(BUS_ID_TILT, BUS_CHK_SUB, BUS_PING_TIMEOUT_MS),
        busTryPing(BUS_ID_TILT, BUS_CHK_XOR, BUS_PING_TIMEOUT_MS),
      };
      completeBusPingRequest(busPingRequestId, result);
      didWork = true;
    }

    vTaskDelay(pdMS_TO_TICKS(didWork ? 1 : 2));
  }
}

static void logNetworkStatus(const char *tag) {
  IPAddress apIp = WiFi.softAPIP();
  Serial.printf("[NET] %s mode=%d ap_ip=%s stations=%d heap=%u\n",
                tag != nullptr ? tag : "diag",
                (int)WiFi.getMode(),
                apIp.toString().c_str(),
                WiFi.softAPgetStationNum(),
                (unsigned)ESP.getFreeHeap());
}

static bool ensureBuzzerPwmReady() {
  if (buzzerPwmReady) return true;
  buzzerPwmReady = ledcAttach(PIN_BUZZER, 2000, BUZZER_PWM_RES_BITS);
  if (buzzerPwmReady) {
    ledcWrite(PIN_BUZZER, 0);
  } else {
    Serial.println("[SOUND] Buzzer PWM init failed");
  }
  return buzzerPwmReady;
}

static void stopSoundTone() {
  if (buzzerPwmReady) {
    ledcWriteTone(PIN_BUZZER, 0);
    ledcWrite(PIN_BUZZER, 0);
  }
  soundActive = false;
  soundEndMs = 0;
}

static uint32_t servoPulseDutyTicks(float pulseUs) {
  const float pwmPeriodUs = 20000.0f;
  const uint32_t maxDuty = (1UL << TRIGGER_SERVO_PWM_RES_BITS) - 1UL;
  float ratio = pulseUs / pwmPeriodUs;
  if (ratio < 0.0f) ratio = 0.0f;
  if (ratio > 1.0f) ratio = 1.0f;
  return (uint32_t)(ratio * (float)maxDuty);
}

static uint32_t servoAngleDutyTicks(int deg) {
  int clamped = clampInt(deg, 0, 180);
  float pulseUs = 1000.0f + (((float)clamped / 180.0f) * 1000.0f);
  return servoPulseDutyTicks(pulseUs);
}

static bool ensureTriggerServoPwmReady() {
  if (!TRIGGER_SERVO_ASSIGNED) return false;
  if (triggerServoPwmReady) return true;
  triggerServoPwmReady = ledcAttach(PIN_TRIGGER_SERVO_PWM, 50, TRIGGER_SERVO_PWM_RES_BITS);
  if (!triggerServoPwmReady) {
    Serial.println("[TRIGSERVO] PWM init failed");
    return false;
  }
  triggerServoCurrentDeg = triggerServoRestDeg;
  triggerServoTargetDeg = triggerServoRestDeg;
  triggerServoLastUpdateMs = nowMs();
  ledcWrite(PIN_TRIGGER_SERVO_PWM, servoAngleDutyTicks(triggerServoRestDeg));
  return true;
}

static void updateTriggerServoOutput(uint32_t nowVal, bool fireActive) {
  if (!TRIGGER_SERVO_ASSIGNED) return;
  if (!ensureTriggerServoPwmReady()) return;

  triggerServoTargetDeg = fireActive ? triggerServoFireDeg : triggerServoRestDeg;
  if (triggerServoCurrentDeg == triggerServoTargetDeg) {
    triggerServoLastUpdateMs = nowVal;
    return;
  }

  if (triggerServoLastUpdateMs == 0) {
    triggerServoLastUpdateMs = nowVal;
  }

  uint32_t elapsedMs = nowVal - triggerServoLastUpdateMs;
  if (elapsedMs == 0) return;

  int step = (int)(((long)triggerServoSpeedDps * (long)elapsedMs) / 1000L);
  if (step <= 0) step = 1;

  if (triggerServoCurrentDeg < triggerServoTargetDeg) {
    triggerServoCurrentDeg = min(triggerServoCurrentDeg + step, triggerServoTargetDeg);
  } else {
    triggerServoCurrentDeg = max(triggerServoCurrentDeg - step, triggerServoTargetDeg);
  }

  ledcWrite(PIN_TRIGGER_SERVO_PWM, servoAngleDutyTicks(triggerServoCurrentDeg));
  triggerServoLastUpdateMs = nowVal;
}

static void startSoundTone(int freqHz, int durationMs, int volumePct) {
  if (!ensureBuzzerPwmReady()) return;
  int freq = clampInt(freqHz, 120, 6000);
  int duration = clampInt(durationMs, 10, 2000);
  int volume = clampInt(volumePct, 0, 100);
  const int dutyMax = (1 << BUZZER_PWM_RES_BITS) - 1;
  const int dutyMin = dutyMax / 32;
  const int dutyPeak = dutyMax / 2;
  int duty = 0;
  if (volume > 0) {
    duty = dutyMin + (((dutyPeak - dutyMin) * volume) / 100);
    duty = clampInt(duty, dutyMin, dutyPeak);
  }
  if (duty <= 0) {
    stopSoundTone();
    return;
  }
  ledcWriteTone(PIN_BUZZER, (uint32_t)freq);
  ledcWrite(PIN_BUZZER, duty);
  soundActive = true;
  soundEndMs = nowMs() + (uint32_t)duration;
  Serial.printf("[SOUND] %d Hz for %d ms @ %d%%\n", freq, duration, volume);
}

static void updateSoundOutput(uint32_t nowVal) {
  if (soundActive && (int32_t)(nowVal - soundEndMs) >= 0) {
    stopSoundTone();
  }
}

static void applyAccessoryOutputs(uint32_t nowVal) {
  if (LED_RELAY_ASSIGNED) {
    digitalWrite(PIN_LED_RELAY, ledState ? HIGH : LOW);
  }
  if (LASER_RELAY_ASSIGNED) {
    digitalWrite(PIN_LASER_RELAY, laserState ? HIGH : LOW);
  }
  digitalWrite(PIN_ACC_RELAY, accState ? HIGH : LOW);
  digitalWrite(PIN_SPARE_RELAY, spareState ? HIGH : LOW);

  bool fireOutputActive = false;

  if (safetyState != 0) {
    digitalWrite(PIN_TRIGGER_MOSFET, LOW);
    projectilePulseActive = false;
    fireState = 0;
    updateTriggerServoOutput(nowVal, false);
    return;
  }

  if (triggerMode == 0) {
    fireOutputActive = fireState ? true : false;
    digitalWrite(PIN_TRIGGER_MOSFET, fireOutputActive ? HIGH : LOW);
    projectilePulseActive = false;
    updateTriggerServoOutput(nowVal, fireOutputActive);
    return;
  }

  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  if (fireState && !projectilePulseActive) {
    projectilePulseActive = true;
    projectilePulseStartMs = nowVal;
    digitalWrite(PIN_TRIGGER_MOSFET, HIGH);
  }
  fireOutputActive = projectilePulseActive;
  if (projectilePulseActive && (nowVal - projectilePulseStartMs) >= triggerPulseMs) {
    digitalWrite(PIN_TRIGGER_MOSFET, LOW);
    projectilePulseActive = false;
    fireState = 0;
    fireOutputActive = false;
  }
  updateTriggerServoOutput(nowVal, fireOutputActive);
}

static uint16_t mapDegreesToTicks(int deg, int minDeg, int maxDeg) {
  int clamped = clampInt(deg, minDeg, maxDeg);
  long spanDeg = (long)(maxDeg - minDeg);
  if (spanDeg <= 0) return 0;
  long shifted = (long)(clamped - minDeg);
  return (uint16_t)((shifted * 4095L) / spanDeg);
}

static void busFlushRx() {
  while (busSerial.available() > 0) {
    (void)busSerial.read();
  }
}

static void serialPrintHexBytes(const uint8_t *data, size_t len) {
  if (data == nullptr || len == 0) {
    Serial.print("<none>");
    return;
  }
  for (size_t i = 0; i < len; ++i) {
    if (i > 0) Serial.print(' ');
    if (data[i] < 16) Serial.print('0');
    Serial.print(data[i], HEX);
  }
}

static void buildBusPingPacket(uint8_t servoId, BusChecksumMode mode, uint8_t *packetOut) {
  packetOut[0] = 0xFF;
  packetOut[1] = 0xFF;
  packetOut[2] = servoId;
  packetOut[3] = BUS_LEN_PING;
  packetOut[4] = BUS_INST_PING;
  packetOut[5] = busChecksum(&packetOut[2], 3, mode);
}

static size_t busReadBytes(uint8_t *buffer, size_t maxLen, uint32_t timeoutMs) {
  size_t count = 0;
  uint32_t start = millis();
  while ((millis() - start) < timeoutMs && count < maxLen) {
    while (busSerial.available() > 0 && count < maxLen) {
      buffer[count++] = (uint8_t)busSerial.read();
    }
    if (count > 0 && busSerial.available() <= 0) {
      delay(1);
    }
  }
  return count;
}

static bool busFindValidPacket(const uint8_t *data, size_t count, uint8_t servoId, BusChecksumMode mode) {
  if (data == nullptr || count < 6) return false;
  for (size_t i = 0; i + 5 < count; ++i) {
    bool headerOk = false;
    if (data[i] == 0xFF && data[i + 1] == 0xFF) headerOk = true;
    if (data[i] == 0xFF && data[i + 1] == 0xF5) headerOk = true;
    if (!headerOk) continue;
    if (data[i + 2] != servoId) continue;
    uint8_t declaredLen = data[i + 3];
    if (declaredLen < 2) continue;
    size_t totalLen = (size_t)declaredLen + 4;
    if (i + totalLen > count) continue;
    uint8_t expectedChecksum = busChecksum(&data[i + 2], totalLen - 3, mode);
    if (expectedChecksum != data[i + totalLen - 1]) continue;
    if (data[i + 4] != 0x00) continue;
    return true;
  }
  return false;
}

static bool busTryPing(uint8_t servoId, BusChecksumMode mode, uint32_t timeoutMs) {
  uint8_t packet[6];
  buildBusPingPacket(servoId, mode, packet);
  busFlushRx();
  busSerial.write(packet, sizeof(packet));
  Serial.printf("[BUSPING] tx id=%u mode=%s bytes=", servoId, mode == BUS_CHK_XOR ? "xor" : "sub");
  serialPrintHexBytes(packet, sizeof(packet));
  Serial.println();
  uint8_t rx[64];
  size_t received = busReadBytes(rx, sizeof(rx), timeoutMs);
  bool ok = busFindValidPacket(rx, received, servoId, mode);
  Serial.printf("[BUSPING] id=%u mode=%s rx=%u -> %s bytes=",
                servoId,
                mode == BUS_CHK_XOR ? "xor" : "sub",
                (unsigned)received,
                ok ? "OK" : "FAIL");
  serialPrintHexBytes(rx, received);
  Serial.println();
  return ok;
}

static void sendBusMotionPacket(uint8_t servoId, int deg, uint16_t moveTimeMs, int minDeg, int maxDeg) {
  uint16_t pos = mapDegreesToTicks(deg, minDeg, maxDeg);
  uint8_t payload[9];
  payload[0] = servoId;
  payload[1] = BUS_LEN_WRITE_POS;
  payload[2] = BUS_INST_WRITE;
  payload[3] = REG_GOAL_POSITION;
  payload[4] = (uint8_t)(pos & 0xFF);
  payload[5] = (uint8_t)((pos >> 8) & 0xFF);
  payload[6] = (uint8_t)(moveTimeMs & 0xFF);
  payload[7] = (uint8_t)((moveTimeMs >> 8) & 0xFF);
  payload[8] = busChecksum(payload, 8, BUS_CHK_SUB);

  busSerial.write(0xFF);
  busSerial.write(0xFF);
  busSerial.write(payload, sizeof(payload));

  Serial.printf("[BUS] motion id=%u deg=%d ticks=%u time=%u\n", servoId, deg, pos, moveTimeMs);
}

static bool handleCommandPayload(const JsonDocument &doc) {
  if (!doc["control_source_mode"].isNull()) {
    ControlSourceMode parsedMode;
    const char *requested = doc["control_source_mode"] | "";
    if (parseControlSourceMode(requested, &parsedMode)) {
      controlSourceMode = parsedMode;
      Serial.printf("[CTRL] control_source_mode=%s\n", controlSourceModeName(controlSourceMode));
    }
  }

  bool rcOwnsMotionAndOutputs = isRcControlActive();

  if (!doc["pan_cmd"].isNull() && !rcOwnsMotionAndOutputs) {
    int pan = clampInt((int)doc["pan_cmd"], PAN_MIN_DEG, PAN_MAX_DEG);
    uint16_t moveTime = (uint16_t)(doc["move_time_ms"] | lastMoveTimeMs);
    queueBusMotionPacket(BUS_ID_PAN, pan, moveTime, PAN_MIN_DEG, PAN_MAX_DEG);
    targetPanDeg = pan;
    lastMoveTimeMs = moveTime;
  }

  if (!doc["tilt_cmd"].isNull() && !rcOwnsMotionAndOutputs) {
    int tilt = clampInt((int)doc["tilt_cmd"], TILT_MIN_DEG, TILT_MAX_DEG);
    uint16_t moveTime = (uint16_t)(doc["move_time_ms"] | lastMoveTimeMs);
    queueBusMotionPacket(BUS_ID_TILT, tilt, moveTime, TILT_MIN_DEG, TILT_MAX_DEG);
    targetTiltDeg = tilt;
    lastMoveTimeMs = moveTime;
  }

  if (!rcOwnsMotionAndOutputs && !doc["fire"].isNull()) {
    fireState = (int)(doc["fire"] | fireState) ? 1 : 0;
  }
  safetyState = (int)(doc["safety"] | safetyState) ? 1 : 0;
  triggerMode = (int)(doc["mode"] | triggerMode) ? 1 : 0;
  if (LED_RELAY_ASSIGNED && !doc["led"].isNull()) {
    ledState = (int)(doc["led"] | ledState) ? 1 : 0;
  } else {
    ledState = 0;
  }
  if (LASER_RELAY_ASSIGNED && !doc["laser"].isNull()) {
    laserState = (int)(doc["laser"] | laserState) ? 1 : 0;
  } else {
    laserState = 0;
  }
  if (!rcOwnsMotionAndOutputs && !doc["acc"].isNull()) {
    accState = (int)(doc["acc"] | accState) ? 1 : 0;
  }
  if (!rcOwnsMotionAndOutputs && !doc["spare"].isNull()) {
    spareState = (int)(doc["spare"] | spareState) ? 1 : 0;
  }

  if (!doc["trigger"].isNull()) {
    JsonVariantConst trigger = doc["trigger"];
    if (!trigger["mode"].isNull()) {
      triggerMode = (int)(trigger["mode"] | triggerMode) ? 1 : 0;
    }
    triggerPulseMs = (uint32_t)clampInt((int)trigger["pulse_ms"] | (int)triggerPulseMs, 10, 2000);
    if (TRIGGER_SERVO_ASSIGNED) {
      int requestedRestDeg = clampInt((int)(trigger["servo_rest_deg"] | triggerServoRestDeg), 0, 180);
      int requestedFireDeg = clampInt((int)(trigger["servo_fire_deg"] | triggerServoFireDeg), requestedRestDeg, 180);
      int requestedSpeedDps = clampInt((int)(trigger["servo_speed_dps"] | triggerServoSpeedDps), 10, 5000);
      triggerServoRestDeg = requestedRestDeg;
      triggerServoFireDeg = requestedFireDeg;
      triggerServoSpeedDps = requestedSpeedDps;
      Serial.printf("[TRIGSERVO] rest=%d fire=%d speed=%d\n",
                    triggerServoRestDeg,
                    triggerServoFireDeg,
                    triggerServoSpeedDps);
    }
  }

  applyAccessoryOutputs(nowMs());
  return true;
}

static void applyRcStubPayload(JsonObject payload) {
  rcLinkActive = bool((int)(payload["rc_link_active"] | (rcLinkActive ? 1 : 0)));
  rcOverrideActive = bool((int)(payload["rc_override_active"] | (rcOverrideActive ? 1 : 0)));
  rcFailsafeActive = bool((int)(payload["rc_failsafe_active"] | (rcFailsafeActive ? 1 : 0)));
  rcFrameAgeMs = (uint32_t)clampInt((int)(payload["rc_frame_age_ms"] | (int)rcFrameAgeMs), 0, 10000);
  for (int i = 0; i < 6; ++i) {
    char key[8];
    snprintf(key, sizeof(key), "ch%d_us", i + 1);
    rcChannelUs[i] = (uint16_t)clampInt((int)(payload[key] | (int)rcChannelUs[i]), 800, 2200);
  }
  if (!payload["control_source_mode"].isNull()) {
    ControlSourceMode parsedMode;
    const char *requested = payload["control_source_mode"] | "";
    if (parseControlSourceMode(requested, &parsedMode)) {
      controlSourceMode = parsedMode;
    }
  }
  rcStubUntilMs = nowMs() + RC_STUB_HOLD_MS;
  Serial.printf("[RCSTUB] link=%d override=%d failsafe=%d age=%lu ch6=%u\n",
                rcLinkActive ? 1 : 0,
                rcOverrideActive ? 1 : 0,
                rcFailsafeActive ? 1 : 0,
                (unsigned long)rcFrameAgeMs,
                (unsigned)rcChannelUs[5]);
}

static void processPacket(char *buffer, size_t len, IPAddress ip, uint16_t port) {
  lastClientIp = ip;
  lastClientPort = port;

  Serial.printf("[UDP-PROC] from %s:%u len=%u preview=",
                ip.toString().c_str(),
                port,
                (unsigned)len);
  serialPrintTextPreview(buffer, len, 180);
  Serial.println();

  JsonDocument doc;
  if (!decodeMessage(buffer, len, doc)) {
    Serial.println("[UDP] decode failed");
    return;
  }

  const char *type = doc["t"] | "";
  int seq = doc["seq"] | 0;
  Serial.printf("[UDP-PROC] dispatch type=%s seq=%d\n", type, seq);

  if (strcmp(type, "hello") == 0) {
    sendAck(seq, true, ip, port);
    sendCaps(ip, port);
    return;
  }
  if (strcmp(type, "hb") == 0) {
    sendState(ip, port);
    return;
  }
  if (strcmp(type, "cmd") == 0) {
    JsonObject payload = doc["p"].as<JsonObject>();
    if (payload.isNull()) {
      sendAck(seq, false, ip, port);
      return;
    }
    if (payload.containsKey("action")) {
      const char *action = payload["action"] | "";
      if (strcmp(action, "bus_ping") == 0) {
        uint32_t requestId = requestBusPing();
        if (requestId == 0) {
          sendAck(seq, false, ip, port);
          return;
        }
        BusPingWaitResult result = {false, false, false, false};
        bool ready = waitForBusPingResult(requestId, 750, &result);
        bool ok = ready && (result.panSubOk || result.panXorOk || result.tiltSubOk || result.tiltXorOk);
        sendAck(seq, ok, ip, port);
        sendState(ip, port);
        return;
      }
      if (strcmp(action, "sound") == 0) {
        int freqHz = payload["freq_hz"] | payload["freq"] | 1200;
        int durationMs = payload["duration_ms"] | 60;
        int volumePct = payload["volume_pct"] | 100;
        startSoundTone(freqHz, durationMs, volumePct);
        sendAck(seq, true, ip, port);
        return;
      }
      if (strcmp(action, "rc_mode") == 0) {
        ControlSourceMode parsedMode;
        const char *requested = payload["mode"] | payload["control_source_mode"] | "";
        bool ok = parseControlSourceMode(requested, &parsedMode);
        if (ok) {
          controlSourceMode = parsedMode;
          Serial.printf("[CTRL] control_source_mode=%s\n", controlSourceModeName(controlSourceMode));
        }
        sendAck(seq, ok, ip, port);
        sendState(ip, port);
        return;
      }
      if (strcmp(action, "rc_stub") == 0) {
        applyRcStubPayload(payload);
        sendAck(seq, true, ip, port);
        sendState(ip, port);
        return;
      }
    }
    bool ok = handleCommandPayload(payload);
    sendAck(seq, ok, ip, port);
    sendState(ip, port);
    return;
  }

  if (doc.containsKey("pan_cmd") || doc.containsKey("tilt_cmd") || doc.containsKey("fire")) {
    bool ok = handleCommandPayload(doc);
    if (ok && ip != IPAddress((uint32_t)0)) {
      sendState(ip, port);
    }
    return;
  }

  Serial.printf("[UDP] ignored packet type='%s'\n", type);
}

void setup() {
  Serial.begin(115200);
  delay(50);

  busSerial.begin(BUS_BAUD, SERIAL_8N1, PIN_UART_RX, PIN_UART_TX);
  Serial.printf("[BOOT] bus uart baud=%u rx=%d tx=%d\n", BUS_BAUD, PIN_UART_RX, PIN_UART_TX);
  Serial.printf("[BOOT] wifi_stability_test_mode=%s normal_bus_baud=%u\n",
                WIFI_STABILITY_TEST_MODE ? "ON" : "OFF",
                BUS_BAUD_NORMAL);
  if (RC_INPUT_ENABLED) {
    rcSerial.begin(RC_BAUD, SERIAL_8N1, PIN_RC_UART_RX, PIN_RC_UART_TX);
    Serial.printf("[BOOT] rc ibus baud=%u rx=%d tx=%d\n", RC_BAUD, PIN_RC_UART_RX, PIN_RC_UART_TX);
  } else {
    Serial.println("[BOOT] rc ibus disabled for bench recovery");
  }

  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  if (LED_RELAY_ASSIGNED) {
    pinMode(PIN_LED_RELAY, OUTPUT);
  }
  if (LASER_RELAY_ASSIGNED) {
    pinMode(PIN_LASER_RELAY, OUTPUT);
  }
  pinMode(PIN_ACC_RELAY, OUTPUT);
  pinMode(PIN_SPARE_RELAY, OUTPUT);

  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  if (LED_RELAY_ASSIGNED) {
    digitalWrite(PIN_LED_RELAY, LOW);
  }
  if (LASER_RELAY_ASSIGNED) {
    digitalWrite(PIN_LASER_RELAY, LOW);
  }
  digitalWrite(PIN_ACC_RELAY, LOW);
  digitalWrite(PIN_SPARE_RELAY, LOW);
  stopSoundTone();
  ensureTriggerServoPwmReady();

  BaseType_t busTaskOk = xTaskCreatePinnedToCore(
    busTask,
    "busTask",
    4096,
    nullptr,
    1,
    &busTaskHandle,
    0);
  Serial.printf("[BOOT] bus task core0=%s\n", busTaskOk == pdPASS ? "OK" : "FAIL");

  WiFi.mode(WIFI_AP);
  delay(100);
  bool apOk = WiFi.softAP(WIFI_SSID, WIFI_PASS);
  delay(250);
  IPAddress apIp = WiFi.softAPIP();
  Serial.printf("[BOOT] ap=%s ip=%s expected_ip=%s stations=%d\n",
                apOk ? "OK" : "FAIL",
                apIp.toString().c_str(),
                AP_IP.toString().c_str(),
                WiFi.softAPgetStationNum());

  uint8_t udpOk = udp.begin(UDP_PORT);
  Serial.printf("[BOOT] udp begin=%s port=%u\n",
                udpOk ? "OK" : "FAIL",
                UDP_PORT);
  logNetworkStatus("boot");
  Serial.println("[BOOT] hardware switch input disabled in current firmware");
  Serial.printf("[BOOT] direct accessory pins: led=%d laser=%d trig_servo=%d trig_mosfet=%d acc=%d spare=%d buzzer=%d\n",
                PIN_LED_RELAY,
                PIN_LASER_RELAY,
                PIN_TRIGGER_SERVO_PWM,
                PIN_TRIGGER_MOSFET,
                PIN_ACC_RELAY,
                PIN_SPARE_RELAY,
                PIN_BUZZER);
  Serial.printf("[BOOT] reserved pins: uart_tx_header=8 uart_rx_header=10\n");
}

void loop() {
  uint32_t nowVal = nowMs();
  if (RC_INPUT_ENABLED) {
    updateRcRuntime(nowVal);
    applyRcLiveControl(nowVal);
  }
  applyAccessoryOutputs(nowVal);
  updateSoundOutput(nowVal);

  if ((nowVal - lastNetDiagMs) >= 5000U) {
    lastNetDiagMs = nowVal;
    logNetworkStatus("loop");
  }

  int packetLen = udp.parsePacket();
  if (packetLen <= 0) {
    delay(1);
    return;
  }

  char buffer[1152];
  int readLen = udp.read(buffer, sizeof(buffer) - 1);
  if (readLen <= 0) {
    return;
  }
  buffer[readLen] = '\0';

  IPAddress ip = udp.remoteIP();
  uint16_t port = udp.remotePort();
  Serial.printf("[UDP-RX] %d bytes from %s:%u\n", readLen, ip.toString().c_str(), port);

  if (readLen >= (int)(sizeof(buffer) - 1)) {
    Serial.println("[UDP] packet truncated");
    delay(1);
    return;
  }
  processPacket(buffer, (size_t)readLen, ip, port);
  delay(1);
}