/*
  ESP32CAM_ESPNOW_SerialBridge_TX.ino

  Role: turret-side node (ESP-NOW <-> Serial)
  - This board sits on the turret side.
  - It receives bytes from the PC-side receiver ESP32-CAM and writes them to Serial.
  - It reads bytes from Serial and sends them back to the PC-side receiver.

  Direct connection: ESP-NOW (no router).

  IMPORTANT:
  - This sketch is a transport bridge only.
  - If you want the turret-side ESP32-CAM to REPLACE the Nano entirely (relays, trigger, current sensor, etc.),
    you will still need to port the DB3000 command parser + IO logic into this firmware.
    This file only provides the wireless pipe.

  Wiring ideas:
  - If you are using an external device on the turret (another MCU, sensor module, etc.), connect it to UART.
  - If you want to use the ESP32-CAM itself for IO, you can extend this sketch to parse incoming commands.

  Setup steps:
  1) Flash this sketch to the turret-side ESP32-CAM.
  2) Open Serial Monitor @ 115200, note MAC.
  3) Put that MAC into the RX sketch PEER_MAC.
  4) Put the RX MAC into this sketch PEER_MAC.
*/

#include <WiFi.h>
#include <esp_now.h>
#include <esp_wifi.h>

// ----------------- USER CONFIG -----------------
// Fill this with the PC-side (RX) ESP32-CAM WiFi MAC address.
static uint8_t PEER_MAC[6] = {0x24, 0x6F, 0x28, 0x00, 0x00, 0x00};

static constexpr uint8_t ESPNOW_CHANNEL = 6;

// Optional LED: ESP32-CAM flash LED is often GPIO4 (AI Thinker).
static constexpr int LED_PIN = 4;
static constexpr bool LED_ACTIVE_HIGH = true;

static constexpr uint32_t SERIAL_BAUD = 115200;
static constexpr uint32_t FLUSH_GAP_MS = 10;
static constexpr size_t   MAX_PAYLOAD = 200;
static constexpr uint8_t  MAX_RETRIES = 3;
static constexpr uint32_t RETRY_MS = 40;
// ------------------------------------------------

static uint16_t crc16_ccitt(const uint8_t* data, size_t len) {
  uint16_t crc = 0xFFFF;
  for (size_t i = 0; i < len; i++) {
    crc ^= (uint16_t)data[i] << 8;
    for (int b = 0; b < 8; b++) {
      crc = (crc & 0x8000) ? (uint16_t)((crc << 1) ^ 0x1021) : (uint16_t)(crc << 1);
    }
  }
  return crc;
}

enum PacketType : uint8_t {
  PKT_DATA = 1,
  PKT_ACK  = 2,
};

struct __attribute__((packed)) PacketHeader {
  uint8_t  type;
  uint16_t seq;
  uint8_t  len;
};

struct __attribute__((packed)) Packet {
  PacketHeader h;
  uint8_t payload[MAX_PAYLOAD];
  uint16_t crc;
};

static uint16_t g_txSeq = 1;
static uint16_t g_lastAcked = 0;

static bool g_havePending = false;
static Packet g_pending{};
static uint8_t g_pendingRetries = 0;
static uint32_t g_pendingLastSendMs = 0;

static uint8_t g_serialBuf[MAX_PAYLOAD];
static size_t g_serialLen = 0;
static uint32_t g_lastSerialByteMs = 0;

static void ledInit() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LED_ACTIVE_HIGH ? LOW : HIGH);
}

static void ledPulse(uint16_t ms = 30) {
  digitalWrite(LED_PIN, LED_ACTIVE_HIGH ? HIGH : LOW);
  delay(ms);
  digitalWrite(LED_PIN, LED_ACTIVE_HIGH ? LOW : HIGH);
}

static bool peerMacLooksUnconfigured() {
  return (PEER_MAC[3] == 0x00 && PEER_MAC[4] == 0x00 && PEER_MAC[5] == 0x00);
}

static void sendAck(uint16_t seq) {
  Packet pkt{};
  pkt.h.type = PKT_ACK;
  pkt.h.seq = seq;
  pkt.h.len = 0;
  pkt.crc = crc16_ccitt((const uint8_t*)&pkt.h, sizeof(pkt.h));
  esp_now_send(PEER_MAC, (const uint8_t*)&pkt, sizeof(PacketHeader) + 2);
}

static void sendData(const uint8_t* data, size_t len) {
  if (len == 0) return;
  if (len > MAX_PAYLOAD) len = MAX_PAYLOAD;

  Packet pkt{};
  pkt.h.type = PKT_DATA;
  pkt.h.seq = g_txSeq++;
  pkt.h.len = (uint8_t)len;
  memcpy(pkt.payload, data, len);

  uint16_t ch = crc16_ccitt((const uint8_t*)&pkt.h, sizeof(pkt.h));
  uint16_t cp = crc16_ccitt(pkt.payload, len);
  pkt.crc = cp ^ ch;

  g_pending = pkt;
  g_havePending = true;
  g_pendingRetries = 0;

  esp_now_send(PEER_MAC, (const uint8_t*)&pkt, sizeof(PacketHeader) + len + 2);
  g_pendingLastSendMs = millis();
}

static void retryIfNeeded() {
  if (!g_havePending) return;
  if (g_lastAcked == g_pending.h.seq) {
    g_havePending = false;
    return;
  }
  uint32_t now = millis();
  if ((now - g_pendingLastSendMs) < RETRY_MS) return;
  if (g_pendingRetries >= MAX_RETRIES) {
    g_havePending = false;
    return;
  }
  g_pendingRetries++;
  esp_now_send(PEER_MAC, (const uint8_t*)&g_pending, sizeof(PacketHeader) + g_pending.h.len + 2);
  g_pendingLastSendMs = now;
}

static void onDataSent(const wifi_tx_info_t* /*info*/, esp_now_send_status_t /*status*/) {
  // no-op
}

static void onDataRecv(const esp_now_recv_info_t* /*info*/, const uint8_t* data, int len) {
  if (len < (int)(sizeof(PacketHeader) + 2)) return;

  const PacketHeader* h = (const PacketHeader*)data;
  const uint8_t* payload = data + sizeof(PacketHeader);
  const uint16_t* pCrc = (const uint16_t*)(data + len - 2);

  if (h->type == PKT_ACK) {
    uint16_t c = crc16_ccitt((const uint8_t*)h, sizeof(PacketHeader));
    if (c != *pCrc) return;
    g_lastAcked = h->seq;
    if (g_havePending && g_pending.h.seq == g_lastAcked) {
      g_havePending = false;
    }
    return;
  }

  if (h->type != PKT_DATA) return;
  if (h->len > MAX_PAYLOAD) return;
  if (len != (int)(sizeof(PacketHeader) + h->len + 2)) return;

  uint16_t ch = crc16_ccitt((const uint8_t*)h, sizeof(PacketHeader));
  uint16_t cp = crc16_ccitt(payload, h->len);
  if ((cp ^ ch) != *pCrc) return;

  Serial.write(payload, h->len);
  sendAck(h->seq);
  ledPulse(10);
}

static bool initEspNow() {
  WiFi.mode(WIFI_STA);
  WiFi.setSleep(false);
  WiFi.disconnect(true, true);

  esp_wifi_set_promiscuous(true);
  esp_wifi_set_channel(ESPNOW_CHANNEL, WIFI_SECOND_CHAN_NONE);
  esp_wifi_set_promiscuous(false);

  if (esp_now_init() != ESP_OK) {
    return false;
  }

  esp_now_register_send_cb(onDataSent);
  esp_now_register_recv_cb(onDataRecv);

  esp_now_peer_info_t peerInfo{};
  memcpy(peerInfo.peer_addr, PEER_MAC, 6);
  peerInfo.channel = ESPNOW_CHANNEL;
  peerInfo.encrypt = false;

  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    return false;
  }

  return true;
}

static void flushSerialIfReady() {
  uint32_t now = millis();
  if (g_serialLen == 0) return;

  for (size_t i = 0; i < g_serialLen; i++) {
    if (g_serialBuf[i] == '\n') {
      sendData(g_serialBuf, g_serialLen);
      g_serialLen = 0;
      return;
    }
  }

  if ((now - g_lastSerialByteMs) >= FLUSH_GAP_MS) {
    sendData(g_serialBuf, g_serialLen);
    g_serialLen = 0;
  }
}

void setup() {
  Serial.begin(SERIAL_BAUD);
  delay(200);

  ledInit();

  Serial.println();
  Serial.println("[ESP-NOW TX] Turret-side serial bridge starting...");
  Serial.print("[ESP-NOW TX] MAC: ");
  Serial.println(WiFi.macAddress());

  if (peerMacLooksUnconfigured()) {
    Serial.println("[ESP-NOW TX] WARNING: PEER_MAC not configured. Set RX MAC in this sketch.");
  }

  if (!initEspNow()) {
    Serial.println("[ESP-NOW TX] ERROR: esp_now_init/add_peer failed");
    while (true) {
      ledPulse(80);
      delay(300);
    }
  }

  Serial.print("[ESP-NOW TX] Channel: ");
  Serial.println(ESPNOW_CHANNEL);
  Serial.println("[ESP-NOW TX] Ready.");
}

void loop() {
  // Read from turret-side Serial and send to PC-side receiver.
  while (Serial.available() > 0) {
    int b = Serial.read();
    if (b < 0) break;

    if (g_serialLen < MAX_PAYLOAD) {
      g_serialBuf[g_serialLen++] = (uint8_t)b;
      g_lastSerialByteMs = millis();
    } else {
      sendData(g_serialBuf, g_serialLen);
      g_serialLen = 0;
    }
  }

  flushSerialIfReady();
  retryIfNeeded();
}
