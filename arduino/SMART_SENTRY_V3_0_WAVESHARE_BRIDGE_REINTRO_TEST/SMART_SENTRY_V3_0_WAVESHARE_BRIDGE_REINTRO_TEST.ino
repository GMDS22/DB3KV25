// Smart Sentry v3.0 Waveshare Bridge Reintroduction Test
// Controlled step-by-step firmware path built from the known-good SoftAP + UDP echo baseline.

#include <WiFi.h>
#include <WiFiUdp.h>

#ifndef REINTRO_STEP
#define REINTRO_STEP 6
#endif

#ifndef REINTRO_UART_RX_PIN
#define REINTRO_UART_RX_PIN 18
#endif

#ifndef REINTRO_UART_TX_PIN
#define REINTRO_UART_TX_PIN 19
#endif

#ifndef REINTRO_UART_BAUD
#define REINTRO_UART_BAUD 250000
#endif

#ifndef REINTRO_UART_INIT_DELAY_MS
#define REINTRO_UART_INIT_DELAY_MS 0
#endif

#ifndef REINTRO_UART_TASK_MODE
#define REINTRO_UART_TASK_MODE 0
#endif

#ifndef REINTRO_UART_RING_MODE
#define REINTRO_UART_RING_MODE 0
#endif

#ifndef REINTRO_UART_STATE_MACHINE_MODE
#define REINTRO_UART_STATE_MACHINE_MODE 0
#endif

#ifndef UART_RX_WINDOW_MS
#define UART_RX_WINDOW_MS 15
#endif

#ifndef UART_RX_MAX_BYTES
#define UART_RX_MAX_BYTES 64
#endif

#ifndef UART_RX_CHUNK_LIMIT
#define UART_RX_CHUNK_LIMIT 16
#endif

#if REINTRO_STEP >= 2
#include <ArduinoJson.h>
#endif

static const char *WIFI_SSID = "WAVESHARE-ESP32";
static const char *WIFI_PASS = "smartv3pass";
static const uint16_t UDP_PORT = 9000;

static const int PIN_TRIGGER_MOSFET = 27;
static const int PIN_ACC_RELAY = 25;
static const int PIN_SPARE_RELAY = 26;
static const int PIN_BUZZER = 4;
static const int PIN_UART_RX = REINTRO_UART_RX_PIN;
static const int PIN_UART_TX = REINTRO_UART_TX_PIN;
static const uint32_t BUS_BAUD = REINTRO_UART_BAUD;
static const uint8_t BUS_ID_PAN = 1;
static const uint8_t BUS_ID_TILT = 2;
static const uint8_t BUS_INST_PING = 0x01;
static const uint8_t BUS_INST_WRITE = 0x03;
static const uint8_t BUS_LEN_PING = 0x02;
static const uint8_t BUS_LEN_WRITE_POS = 0x07;
static const uint8_t REG_GOAL_POSITION = 0x2A;
static const uint32_t BUS_PING_TIMEOUT_MS = 60;
static const int PAN_MIN_DEG = 0;
static const int PAN_MAX_DEG = 220;
static const int TILT_MIN_DEG = 0;
static const int TILT_MAX_DEG = 70;

WiFiUDP udp;

#if REINTRO_STEP >= 6
HardwareSerial busSerial(2);
#if REINTRO_UART_TASK_MODE
TaskHandle_t uartTaskHandle = nullptr;
#endif
#endif

static uint32_t lastDiagMs = 0;
static uint32_t loopCount = 0;
static uint32_t udpRxCount = 0;
static uint32_t udpTxCount = 0;
static uint32_t uartRxCount = 0;
static uint32_t uartParsedCount = 0;
static uint32_t maxLoopUs = 0;
static uint8_t lastUartByte = 0;
static uint32_t lastUartYieldMs = 0;
static uint32_t uartWindowDoneCount = 0;
static uint32_t uartWindowByteTotal = 0;
#if REINTRO_UART_STATE_MACHINE_MODE && REINTRO_STEP >= 7
enum UartState {
  UART_IDLE,
  UART_WAITING,
  UART_RECEIVING
};

static UartState uartState = UART_IDLE;
static uint32_t uartStartTime = 0;
static uint8_t uartBuffer[UART_RX_MAX_BYTES];
static size_t uartCount = 0;
#endif
#if REINTRO_UART_RING_MODE && REINTRO_STEP >= 8
static const uint16_t UART_RING_SIZE = 128;
static volatile uint8_t uartRing[UART_RING_SIZE];
static volatile uint16_t uartRingHead = 0;
static volatile uint16_t uartRingTail = 0;
static volatile uint32_t uartRingDropped = 0;
static portMUX_TYPE uartRingMux = portMUX_INITIALIZER_UNLOCKED;
#endif
static int triggerState = 0;
static int accState = 0;
static int spareState = 0;
static int buzzerState = 0;

static int *stateForPin(int pin) {
  if (pin == PIN_BUZZER) return &buzzerState;
  if (pin == PIN_TRIGGER_MOSFET) return &triggerState;
  if (pin == PIN_ACC_RELAY) return &accState;
  if (pin == PIN_SPARE_RELAY) return &spareState;
  return nullptr;
}

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

static uint16_t mapDegreesToTicks(int deg, int minDeg, int maxDeg) {
  int clamped = clampInt(deg, minDeg, maxDeg);
  long spanDeg = (long)(maxDeg - minDeg);
  if (spanDeg <= 0) return 0;
  long shifted = (long)(clamped - minDeg);
  return (uint16_t)((shifted * 4095L) / spanDeg);
}

static void initAccessoryPins() {
#if REINTRO_STEP >= 4
  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  pinMode(PIN_ACC_RELAY, OUTPUT);
  pinMode(PIN_SPARE_RELAY, OUTPUT);
  pinMode(PIN_BUZZER, OUTPUT);
  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  digitalWrite(PIN_ACC_RELAY, LOW);
  digitalWrite(PIN_SPARE_RELAY, LOW);
  digitalWrite(PIN_BUZZER, LOW);
#endif
}

static void applyAccessoryOutputs() {
#if REINTRO_STEP >= 5
  digitalWrite(PIN_TRIGGER_MOSFET, triggerState ? HIGH : LOW);
  digitalWrite(PIN_ACC_RELAY, accState ? HIGH : LOW);
  digitalWrite(PIN_SPARE_RELAY, spareState ? HIGH : LOW);
  digitalWrite(PIN_BUZZER, buzzerState ? HIGH : LOW);
#endif
}

#if REINTRO_STEP >= 6
static void initBusSerial() {
  if (REINTRO_UART_INIT_DELAY_MS > 0) {
    delay(REINTRO_UART_INIT_DELAY_MS);
  }
  busSerial.begin(BUS_BAUD, SERIAL_8N1, PIN_UART_RX, PIN_UART_TX);
  Serial.printf("[BOOT] uart2 begin baud=%u rx=%d tx=%d init_delay_ms=%u\n",
                BUS_BAUD,
                PIN_UART_RX,
                PIN_UART_TX,
                (unsigned)REINTRO_UART_INIT_DELAY_MS);
}

#if REINTRO_UART_STATE_MACHINE_MODE && REINTRO_STEP >= 7
static void uartStartTransaction() {
  uartState = UART_WAITING;
  uartStartTime = millis();
  uartCount = 0;
}

static void uartFinishTransaction() {
  uartState = UART_IDLE;
  if (uartCount > 0) {
    uartWindowDoneCount++;
    uartWindowByteTotal += (uint32_t)uartCount;
    Serial.printf("[UART] done, %u bytes\n", (unsigned)uartCount);
  }
}

static void uartProcess() {
  switch (uartState) {
    case UART_IDLE:
      return;

    case UART_WAITING:
      if ((millis() - uartStartTime) >= 2U) {
        uartState = UART_RECEIVING;
        uartStartTime = millis();
      }
      break;

    case UART_RECEIVING: {
      if ((millis() - uartStartTime) > UART_RX_WINDOW_MS) {
        uartFinishTransaction();
        return;
      }

      size_t chunk = 0;
      while (busSerial.available() > 0 &&
             uartCount < UART_RX_MAX_BYTES &&
             chunk < UART_RX_CHUNK_LIMIT) {
        lastUartByte = (uint8_t)busSerial.read();
        uartBuffer[uartCount++] = lastUartByte;
        uartRxCount++;
        if (lastUartByte == 0xFF) {
          uartParsedCount++;
        }
        chunk++;
      }

      if (uartCount >= UART_RX_MAX_BYTES) {
        uartFinishTransaction();
      }
      break;
    }
  }
}

static void writeBusPacket(const uint8_t *packet, size_t len, bool startTransaction) {
  busSerial.write(packet, len);
  busSerial.flush();
  if (startTransaction) {
    uartStartTransaction();
  }
}
#endif

static void handleSafeUartRead() {
#if REINTRO_STEP >= 7
  if (busSerial.available() > 0) {
    lastUartByte = (uint8_t)busSerial.read();
    uartRxCount++;
  }
  uint32_t nowVal = millis();
  if ((nowVal - lastUartYieldMs) > 1U) {
    lastUartYieldMs = nowVal;
    delay(0);
  }
#endif
}

static void boundedReadBusBuffer() {
#if REINTRO_STEP >= 8
  int budget = 16;
  while (budget > 0 && busSerial.available() > 0) {
    lastUartByte = (uint8_t)busSerial.read();
    uartRxCount++;
    budget--;
    if (lastUartByte == 0xFF) {
      uartParsedCount++;
    }
  }
#endif
}

#if REINTRO_UART_RING_MODE && REINTRO_STEP >= 8
static void pushUartRingByte(uint8_t value) {
  portENTER_CRITICAL(&uartRingMux);
  uint16_t nextHead = (uint16_t)((uartRingHead + 1U) % UART_RING_SIZE);
  if (nextHead == uartRingTail) {
    uartRingDropped++;
  } else {
    uartRing[uartRingHead] = value;
    uartRingHead = nextHead;
  }
  portEXIT_CRITICAL(&uartRingMux);
}

static bool popUartRingByte(uint8_t *valueOut) {
  bool ok = false;
  portENTER_CRITICAL(&uartRingMux);
  if (uartRingTail != uartRingHead) {
    *valueOut = uartRing[uartRingTail];
    uartRingTail = (uint16_t)((uartRingTail + 1U) % UART_RING_SIZE);
    ok = true;
  }
  portEXIT_CRITICAL(&uartRingMux);
  return ok;
}

static void fillUartRingBuffer() {
  int budget = 16;
  while (budget > 0 && busSerial.available() > 0) {
    lastUartByte = (uint8_t)busSerial.read();
    uartRxCount++;
    pushUartRingByte(lastUartByte);
    budget--;
  }
}

static void processUartRingBuffer() {
  int budget = 16;
  uint8_t value = 0;
  while (budget > 0 && popUartRingByte(&value)) {
    lastUartByte = value;
    if (value == 0xFF) {
      uartParsedCount++;
    }
    budget--;
  }
}
#endif

#if REINTRO_UART_TASK_MODE && REINTRO_STEP >= 8
static void uartPollTask(void *parameter) {
  (void)parameter;
  for (;;) {
#if REINTRO_UART_RING_MODE
    fillUartRingBuffer();
#else
    boundedReadBusBuffer();
#endif
    vTaskDelay(1);
  }
}
#endif

static void sendBusMotionPacket(uint8_t servoId, int deg, uint16_t moveTimeMs, int minDeg, int maxDeg) {
#if REINTRO_STEP >= 9
  uint16_t pos = mapDegreesToTicks(deg, minDeg, maxDeg);
  uint8_t packet[11];
  packet[0] = 0xFF;
  packet[1] = 0xFF;
  packet[2] = servoId;
  packet[3] = BUS_LEN_WRITE_POS;
  packet[4] = BUS_INST_WRITE;
  packet[5] = REG_GOAL_POSITION;
  packet[6] = (uint8_t)(pos & 0xFF);
  packet[7] = (uint8_t)((pos >> 8) & 0xFF);
  packet[8] = (uint8_t)(moveTimeMs & 0xFF);
  packet[9] = (uint8_t)((moveTimeMs >> 8) & 0xFF);
  packet[10] = busChecksum(&packet[2], 8);
#if REINTRO_UART_STATE_MACHINE_MODE && REINTRO_STEP >= 7
  writeBusPacket(packet, sizeof(packet), true);
#else
  busSerial.write(packet, sizeof(packet));
#endif
#else
  (void)servoId;
  (void)deg;
  (void)moveTimeMs;
  (void)minDeg;
  (void)maxDeg;
#endif
}

static bool tryBusPing(uint8_t servoId) {
#if REINTRO_STEP >= 9
  uint8_t packet[6];
  packet[0] = 0xFF;
  packet[1] = 0xFF;
  packet[2] = servoId;
  packet[3] = BUS_LEN_PING;
  packet[4] = BUS_INST_PING;
  packet[5] = busChecksum(&packet[2], 3);
  while (busSerial.available() > 0) {
    (void)busSerial.read();
  }
#if REINTRO_UART_STATE_MACHINE_MODE && REINTRO_STEP >= 7
  writeBusPacket(packet, sizeof(packet), true);
  return false;
#else
  busSerial.write(packet, sizeof(packet));
  uint32_t startMs = millis();
  while ((millis() - startMs) < BUS_PING_TIMEOUT_MS) {
    if (busSerial.available() > 0) {
      uartRxCount += (uint32_t)busSerial.available();
      return true;
    }
    delay(1);
  }
#endif
#else
  (void)servoId;
#endif
  return false;
}
#endif

static void logDiag(const char *tag, uint32_t loopUs) {
  Serial.printf("[DIAG] %s step=%d stations=%d heap=%u loop_us=%lu loop_us_max=%lu udp_rx=%lu udp_tx=%lu uart_rx=%lu uart_parse=%lu uart_sm=%d uart_sm_state=%d uart_sm_done=%lu uart_sm_bytes=%lu\n",
                tag,
                REINTRO_STEP,
                WiFi.softAPgetStationNum(),
                (unsigned)ESP.getFreeHeap(),
                (unsigned long)loopUs,
                (unsigned long)maxLoopUs,
                (unsigned long)udpRxCount,
                (unsigned long)udpTxCount,
                (unsigned long)uartRxCount,
                (unsigned long)uartParsedCount,
                REINTRO_UART_STATE_MACHINE_MODE ? 1 : 0,
#if REINTRO_UART_STATE_MACHINE_MODE && REINTRO_STEP >= 7
                (int)uartState,
#else
                0,
#endif
                (unsigned long)uartWindowDoneCount,
                (unsigned long)uartWindowByteTotal);
}

static void sendRawEcho(IPAddress ip, uint16_t port, const uint8_t *data, size_t len) {
  udp.beginPacket(ip, port);
  udp.write(data, len);
  udp.endPacket();
  udpTxCount++;
}

#if REINTRO_STEP >= 3
static void sendStructuredReply(IPAddress ip, uint16_t port, int seq, bool parseOk) {
  char message[384];
  int written = snprintf(message,
                         sizeof(message),
                         "{\"v\":1,\"t\":\"state\",\"seq\":%d,\"step\":%d,\"parse_ok\":%s,\"stations\":%d,\"heap\":%u,\"udp_rx\":%lu,\"udp_tx\":%lu,\"uart_rx\":%lu,\"uart_parse\":%lu}",
                         seq,
                         REINTRO_STEP,
                         parseOk ? "true" : "false",
                         WiFi.softAPgetStationNum(),
                         (unsigned)ESP.getFreeHeap(),
                         (unsigned long)udpRxCount,
                         (unsigned long)udpTxCount,
                         (unsigned long)uartRxCount,
                         (unsigned long)uartParsedCount);
  if (written < 0) return;
  udp.beginPacket(ip, port);
  udp.write((const uint8_t *)message, (size_t)written);
  udp.endPacket();
  udpTxCount++;
}
#endif

#if REINTRO_STEP >= 2
static bool parseJsonPayload(char *buffer, size_t len, int *seqOut) {
  StaticJsonDocument<512> doc;
  DeserializationError err = deserializeJson(doc, buffer, len);
  bool ok = !err;
  if (seqOut != nullptr) {
    *seqOut = ok ? (int)(doc["seq"] | 0) : 0;
  }
#if REINTRO_STEP >= 5
  if (ok) {
    const char *cmd = doc["cmd"] | doc["action"] | "";
    if (strcmp(cmd, "set") == 0) {
      int pin = doc["pin"] | -1;
      int value = (int)(doc["value"] | 0) ? 1 : 0;
      int *targetState = stateForPin(pin);
      if (targetState != nullptr) {
        *targetState = value;
      } else {
        ok = false;
      }
    }

    JsonVariantConst payload = doc["p"];
    if (ok && !payload.isNull()) {
      triggerState = (int)(payload["fire"] | triggerState) ? 1 : 0;
      accState = (int)(payload["acc"] | accState) ? 1 : 0;
      spareState = (int)(payload["spare"] | spareState) ? 1 : 0;
      buzzerState = (int)(payload["buzz"] | buzzerState) ? 1 : 0;
    }
#if REINTRO_STEP >= 9
    int panCmd = payload["pan_cmd"] | -1;
    int tiltCmd = payload["tilt_cmd"] | -1;
    if (panCmd >= 0) {
      sendBusMotionPacket(BUS_ID_PAN, panCmd, 120, PAN_MIN_DEG, PAN_MAX_DEG);
    }
    if (tiltCmd >= 0) {
      sendBusMotionPacket(BUS_ID_TILT, tiltCmd, 120, TILT_MIN_DEG, TILT_MAX_DEG);
    }
    const char *action = payload["action"] | "";
    if (strcmp(action, "bus_ping") == 0) {
      bool panOk = tryBusPing(BUS_ID_PAN);
      bool tiltOk = tryBusPing(BUS_ID_TILT);
      uartParsedCount += panOk ? 1U : 0U;
      uartParsedCount += tiltOk ? 1U : 0U;
    }
#endif
  }
#endif
  return ok;
}
#endif

static void handlePacket(uint8_t *buffer, int readLen, IPAddress ip, uint16_t port) {
  udpRxCount++;

#if REINTRO_STEP == 1
  sendRawEcho(ip, port, buffer, (size_t)readLen);
  return;
#endif

  int seq = 0;
  bool parseOk = false;
#if REINTRO_STEP >= 2
  buffer[readLen] = '\0';
  parseOk = parseJsonPayload((char *)buffer, (size_t)readLen, &seq);
#endif

#if REINTRO_STEP >= 5
  applyAccessoryOutputs();
#endif

#if REINTRO_STEP >= 3
  sendStructuredReply(ip, port, seq, parseOk);
#else
  sendRawEcho(ip, port, buffer, (size_t)readLen);
#endif
}

void setup() {
  Serial.begin(115200);
  delay(50);

  WiFi.mode(WIFI_AP);
  delay(100);

  bool apOk = WiFi.softAP(WIFI_SSID, WIFI_PASS);
  delay(250);

  IPAddress apIp = WiFi.softAPIP();
  uint8_t udpOk = udp.begin(UDP_PORT);

  Serial.printf("[BOOT] step=%d ap=%s ip=%s stations=%d\n",
                REINTRO_STEP,
                apOk ? "OK" : "FAIL",
                apIp.toString().c_str(),
                WiFi.softAPgetStationNum());
  Serial.printf("[BOOT] udp begin=%s port=%u\n",
                udpOk ? "OK" : "FAIL",
                UDP_PORT);
  Serial.printf("[BOOT] features parse_shell=%d json=%d structured_reply=%d gpio_init=%d gpio_control=%d uart_init=%d uart_rx_light=%d uart_rx_full=%d full_bridge=%d\n",
                REINTRO_STEP >= 1,
                REINTRO_STEP >= 2,
                REINTRO_STEP >= 3,
                REINTRO_STEP >= 4,
                REINTRO_STEP >= 5,
                REINTRO_STEP >= 6,
                REINTRO_STEP >= 7,
                REINTRO_STEP >= 8,
                REINTRO_STEP >= 9);
  Serial.printf("[BOOT] uart_task_mode=%d\n", REINTRO_UART_TASK_MODE ? 1 : 0);
  Serial.printf("[BOOT] uart_ring_mode=%d\n", REINTRO_UART_RING_MODE ? 1 : 0);
  Serial.printf("[BOOT] uart_state_machine_mode=%d rx_window_ms=%u rx_max_bytes=%u rx_chunk_limit=%u\n",
                REINTRO_UART_STATE_MACHINE_MODE ? 1 : 0,
                (unsigned)UART_RX_WINDOW_MS,
                (unsigned)UART_RX_MAX_BYTES,
                (unsigned)UART_RX_CHUNK_LIMIT);
  Serial.printf("[BOOT] step5_cmd={\"cmd\":\"set\",\"pin\":25,\"value\":1} step6a_uart_baud=%u uart_rx=%d uart_tx=%d\n",
                BUS_BAUD,
                PIN_UART_RX,
                PIN_UART_TX);

  initAccessoryPins();
#if REINTRO_STEP >= 6
  initBusSerial();
#if REINTRO_UART_TASK_MODE && REINTRO_STEP >= 8
  xTaskCreatePinnedToCore(uartPollTask, "uartPoll", 4096, nullptr, 1, &uartTaskHandle, 0);
#endif
#endif
}

void loop() {
  uint32_t loopStartUs = micros();
  loopCount++;

#if REINTRO_STEP >= 7
#if REINTRO_UART_STATE_MACHINE_MODE
  uartProcess();
#elif !REINTRO_UART_TASK_MODE
  handleSafeUartRead();
#if !REINTRO_UART_TASK_MODE
#if REINTRO_STEP >= 8
#if REINTRO_UART_RING_MODE
  processUartRingBuffer();
#else
  boundedReadBusBuffer();
#endif
#endif
#endif
#endif
#endif

  int packetLen = udp.parsePacket();
  if (packetLen > 0) {
    uint8_t buffer[768];
    int readLen = udp.read(buffer, sizeof(buffer) - 1);
    if (readLen > 0) {
      IPAddress ip = udp.remoteIP();
      uint16_t port = udp.remotePort();
      handlePacket(buffer, readLen, ip, port);
    }
  }

  uint32_t loopUs = micros() - loopStartUs;
  if (loopUs > maxLoopUs) {
    maxLoopUs = loopUs;
  }
  if ((millis() - lastDiagMs) >= 5000U) {
    lastDiagMs = millis();
    logDiag("loop", loopUs);
  }

  delay(1);
}