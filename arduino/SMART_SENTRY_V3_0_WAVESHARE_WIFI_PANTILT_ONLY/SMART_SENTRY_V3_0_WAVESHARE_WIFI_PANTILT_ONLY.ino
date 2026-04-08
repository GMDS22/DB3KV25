// Smart Sentry v3.0 Waveshare WiFi Pan/Tilt Only
// Final simplified retry: keep the stable SoftAP + UDP control path and drive
// only the pan/tilt bus servos over UART2. No accessory GPIOs are touched.
// FQBN: esp32:esp32:esp32

#include <ArduinoJson.h>
#include <WiFi.h>
#include <WiFiUdp.h>

static const char *WIFI_SSID = "WAVESHARE-ESP32";
static const char *WIFI_PASS = "smartv3pass";
static const IPAddress AP_IP(192, 168, 4, 1);
static const IPAddress AP_GW(192, 168, 4, 1);
static const IPAddress AP_MASK(255, 255, 255, 0);
static const uint16_t UDP_PORT = 9000;

static const int PIN_UART_RX = 18;
static const int PIN_UART_TX = 19;
static const uint32_t BUS_BAUD = 1000000;

static const uint8_t BUS_ID_PAN = 1;
static const uint8_t BUS_ID_TILT = 2;
static const uint8_t BUS_INST_PING = 0x01;
static const uint8_t BUS_INST_WRITE = 0x03;
static const uint8_t BUS_LEN_PING = 0x02;
static const uint8_t BUS_LEN_WRITE_POS = 0x07;
static const uint8_t REG_GOAL_POSITION = 0x2A;

static const int PAN_MIN_DEG = 0;
static const int PAN_MAX_DEG = 220;
static const int TILT_MIN_DEG = 0;
static const int TILT_MAX_DEG = 70;
static const uint16_t DEFAULT_MOVE_TIME_MS = 120;

static const uint32_t UART_SETTLE_MS = 2;
static const uint32_t UART_RX_WINDOW_MS = 15;
static const size_t UART_RX_MAX_BYTES = 64;
static const size_t UART_RX_CHUNK_LIMIT = 16;
static const uint32_t DIAG_INTERVAL_MS = 5000;

enum UartState {
  UART_IDLE,
  UART_WAITING,
  UART_RECEIVING,
};

WiFiUDP udp;
HardwareSerial busSerial(2);

static UartState uartState = UART_IDLE;
static uint32_t uartStartMs = 0;
static uint8_t uartBuffer[UART_RX_MAX_BYTES];
static size_t uartCount = 0;

static uint32_t udpRxCount = 0;
static uint32_t udpTxCount = 0;
static uint32_t uartRxCount = 0;
static uint32_t uartPacketMarkerCount = 0;
static uint32_t uartWindowDoneCount = 0;
static uint32_t uartWindowByteTotal = 0;
static uint32_t maxLoopUs = 0;
static uint32_t lastDiagMs = 0;
static uint8_t lastUartByte = 0;
static int lastPanCmd = 90;
static int lastTiltCmd = 35;
static uint16_t lastMoveTimeMs = DEFAULT_MOVE_TIME_MS;

static uint8_t busChecksum(const uint8_t *data, size_t count) {
  uint8_t sum = 0;
  for (size_t i = 0; i < count; ++i) {
    sum = (uint8_t)(sum + data[i]);
  }
  return (uint8_t)(~sum);
}

static int clampInt(int value, int lo, int hi) {
  if (value < lo) return lo;
  if (value > hi) return hi;
  return value;
}

static uint16_t mapDegreesToTicks(int degrees, int minDegrees, int maxDegrees) {
  int clampedDegrees = clampInt(degrees, minDegrees, maxDegrees);
  long spanDegrees = (long)(maxDegrees - minDegrees);
  if (spanDegrees <= 0) return 0;

  long shifted = (long)(clampedDegrees - minDegrees);
  return (uint16_t)((shifted * 4095L) / spanDegrees);
}

static void uartStartTransaction() {
  uartState = UART_WAITING;
  uartStartMs = millis();
  uartCount = 0;
}

static void uartFinishTransaction() {
  uartState = UART_IDLE;
  if (uartCount > 0) {
    uartWindowDoneCount++;
    uartWindowByteTotal += (uint32_t)uartCount;
  }
}

static void uartProcess() {
  switch (uartState) {
    case UART_IDLE:
      return;

    case UART_WAITING:
      if ((millis() - uartStartMs) >= UART_SETTLE_MS) {
        uartState = UART_RECEIVING;
        uartStartMs = millis();
      }
      return;

    case UART_RECEIVING: {
      if ((millis() - uartStartMs) > UART_RX_WINDOW_MS) {
        uartFinishTransaction();
        return;
      }

      size_t chunkCount = 0;
      while (busSerial.available() > 0 && uartCount < UART_RX_MAX_BYTES && chunkCount < UART_RX_CHUNK_LIMIT) {
        lastUartByte = (uint8_t)busSerial.read();
        uartBuffer[uartCount++] = lastUartByte;
        uartRxCount++;
        if (lastUartByte == 0xFF) {
          uartPacketMarkerCount++;
        }
        chunkCount++;
      }

      if (uartCount >= UART_RX_MAX_BYTES) {
        uartFinishTransaction();
      }
      return;
    }
  }
}

static void writeBusPacket(const uint8_t *packet, size_t packetLen) {
  busSerial.write(packet, packetLen);
  busSerial.flush();
  uartStartTransaction();
}

static void sendBusMotionPacket(uint8_t servoId, int degrees, uint16_t moveTimeMs, int minDegrees, int maxDegrees) {
  uint16_t position = mapDegreesToTicks(degrees, minDegrees, maxDegrees);

  uint8_t packet[11];
  packet[0] = 0xFF;
  packet[1] = 0xFF;
  packet[2] = servoId;
  packet[3] = BUS_LEN_WRITE_POS;
  packet[4] = BUS_INST_WRITE;
  packet[5] = REG_GOAL_POSITION;
  packet[6] = (uint8_t)(position & 0xFF);
  packet[7] = (uint8_t)((position >> 8) & 0xFF);
  packet[8] = (uint8_t)(moveTimeMs & 0xFF);
  packet[9] = (uint8_t)((moveTimeMs >> 8) & 0xFF);
  packet[10] = busChecksum(&packet[2], 8);

  writeBusPacket(packet, sizeof(packet));
}

static void sendBusPing(uint8_t servoId) {
  uint8_t packet[6];
  packet[0] = 0xFF;
  packet[1] = 0xFF;
  packet[2] = servoId;
  packet[3] = BUS_LEN_PING;
  packet[4] = BUS_INST_PING;
  packet[5] = busChecksum(&packet[2], 3);
  writeBusPacket(packet, sizeof(packet));
}

static void sendStructuredReply(IPAddress ip,
                                uint16_t port,
                                int seq,
                                bool parseOk,
                                bool motionQueued,
                                bool pingQueued) {
  StaticJsonDocument<512> reply;
  reply["v"] = 1;
  reply["t"] = "state";
  reply["seq"] = seq;
  reply["parse_ok"] = parseOk;
  reply["motion_queued"] = motionQueued;
  reply["ping_queued"] = pingQueued;
  reply["stations"] = WiFi.softAPgetStationNum();
  reply["heap"] = ESP.getFreeHeap();
  reply["udp_rx"] = udpRxCount;
  reply["udp_tx"] = udpTxCount;
  reply["uart_rx"] = uartRxCount;
  reply["uart_markers"] = uartPacketMarkerCount;
  reply["uart_windows"] = uartWindowDoneCount;
  reply["uart_window_bytes"] = uartWindowByteTotal;
  reply["last_uart_byte"] = lastUartByte;
  reply["last_pan_cmd"] = lastPanCmd;
  reply["last_tilt_cmd"] = lastTiltCmd;
  reply["last_move_time_ms"] = lastMoveTimeMs;
  reply["uart_state"] = (int)uartState;

  char message[512];
  size_t written = serializeJson(reply, message, sizeof(message));
  if (written == 0) return;

  udp.beginPacket(ip, port);
  udp.write((const uint8_t *)message, written);
  udp.endPacket();
  udpTxCount++;
}

static bool parseJsonPayload(char *buffer,
                             size_t bufferLen,
                             int *seqOut,
                             bool *motionQueuedOut,
                             bool *pingQueuedOut) {
  StaticJsonDocument<512> doc;
  DeserializationError err = deserializeJson(doc, buffer, bufferLen);
  if (err) {
    if (seqOut != nullptr) *seqOut = 0;
    if (motionQueuedOut != nullptr) *motionQueuedOut = false;
    if (pingQueuedOut != nullptr) *pingQueuedOut = false;
    return false;
  }

  if (seqOut != nullptr) {
    *seqOut = (int)(doc["seq"] | 0);
  }

  JsonVariantConst payload = doc["p"];
  if (payload.isNull()) {
    payload = doc.as<JsonVariantConst>();
  }

  const int requestedPan = payload["pan_cmd"] | doc["pan_cmd"] | -1;
  const int requestedTilt = payload["tilt_cmd"] | doc["tilt_cmd"] | -1;
  const uint16_t requestedMoveTime = (uint16_t)(payload["move_time_ms"] | doc["move_time_ms"] | DEFAULT_MOVE_TIME_MS);
  const char *action = payload["action"] | doc["action"] | doc["cmd"] | "";

  bool motionQueued = false;
  if (requestedPan >= 0) {
    lastPanCmd = clampInt(requestedPan, PAN_MIN_DEG, PAN_MAX_DEG);
    sendBusMotionPacket(BUS_ID_PAN, lastPanCmd, requestedMoveTime, PAN_MIN_DEG, PAN_MAX_DEG);
    motionQueued = true;
  }
  if (requestedTilt >= 0) {
    lastTiltCmd = clampInt(requestedTilt, TILT_MIN_DEG, TILT_MAX_DEG);
    sendBusMotionPacket(BUS_ID_TILT, lastTiltCmd, requestedMoveTime, TILT_MIN_DEG, TILT_MAX_DEG);
    motionQueued = true;
  }
  if (motionQueued) {
    lastMoveTimeMs = requestedMoveTime;
  }

  bool pingQueued = false;
  if (strcmp(action, "bus_ping") == 0) {
    sendBusPing(BUS_ID_PAN);
    sendBusPing(BUS_ID_TILT);
    pingQueued = true;
  }

  if (motionQueuedOut != nullptr) *motionQueuedOut = motionQueued;
  if (pingQueuedOut != nullptr) *pingQueuedOut = pingQueued;
  return motionQueued || pingQueued || doc.containsKey("seq") || doc.containsKey("p") || doc.containsKey("pan_cmd") || doc.containsKey("tilt_cmd");
}

static void handlePacket(uint8_t *buffer, int readLen, IPAddress ip, uint16_t port) {
  udpRxCount++;

  int seq = 0;
  bool motionQueued = false;
  bool pingQueued = false;

  buffer[readLen] = '\0';
  bool parseOk = parseJsonPayload((char *)buffer, (size_t)readLen, &seq, &motionQueued, &pingQueued);
  sendStructuredReply(ip, port, seq, parseOk, motionQueued, pingQueued);
}

static void logDiag(uint32_t loopUs) {
  Serial.printf("[DIAG] stations=%d heap=%u loop_us=%lu loop_us_max=%lu udp_rx=%lu udp_tx=%lu uart_rx=%lu uart_markers=%lu uart_windows=%lu uart_window_bytes=%lu last_uart=0x%02X last_pan=%d last_tilt=%d last_move_ms=%u uart_state=%d\n",
                WiFi.softAPgetStationNum(),
                (unsigned)ESP.getFreeHeap(),
                (unsigned long)loopUs,
                (unsigned long)maxLoopUs,
                (unsigned long)udpRxCount,
                (unsigned long)udpTxCount,
                (unsigned long)uartRxCount,
                (unsigned long)uartPacketMarkerCount,
                (unsigned long)uartWindowDoneCount,
                (unsigned long)uartWindowByteTotal,
                lastUartByte,
                lastPanCmd,
                lastTiltCmd,
                (unsigned)lastMoveTimeMs,
                (int)uartState);
}

void setup() {
  Serial.begin(115200);
  delay(50);

  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(AP_IP, AP_GW, AP_MASK);
  bool apOk = WiFi.softAP(WIFI_SSID, WIFI_PASS);
  delay(250);

  busSerial.begin(BUS_BAUD, SERIAL_8N1, PIN_UART_RX, PIN_UART_TX);
  uint8_t udpOk = udp.begin(UDP_PORT);

  Serial.printf("[BOOT] sketch=SMART_SENTRY_V3_0_WAVESHARE_WIFI_PANTILT_ONLY ap=%s ip=%s stations=%d\n",
                apOk ? "OK" : "FAIL",
                WiFi.softAPIP().toString().c_str(),
                WiFi.softAPgetStationNum());
  Serial.printf("[BOOT] udp=%s port=%u\n", udpOk ? "OK" : "FAIL", UDP_PORT);
  Serial.printf("[BOOT] bus_uart baud=%u rx=%d tx=%d ids={pan:%u tilt:%u}\n",
                (unsigned)BUS_BAUD,
                PIN_UART_RX,
                PIN_UART_TX,
                BUS_ID_PAN,
                BUS_ID_TILT);
  Serial.println("[BOOT] accessories disabled: no GPIO outputs are initialized in this sketch");
}

void loop() {
  uint32_t loopStartUs = micros();

  uartProcess();

  int packetLen = udp.parsePacket();
  if (packetLen > 0) {
    uint8_t buffer[768];
    int readLen = udp.read(buffer, sizeof(buffer) - 1);
    if (readLen > 0) {
      handlePacket(buffer, readLen, udp.remoteIP(), udp.remotePort());
    }
  }

  uint32_t loopUs = micros() - loopStartUs;
  if (loopUs > maxLoopUs) {
    maxLoopUs = loopUs;
  }

  if ((millis() - lastDiagMs) >= DIAG_INTERVAL_MS) {
    lastDiagMs = millis();
    logDiag(loopUs);
  }

  delay(1);
}