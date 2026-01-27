/*
  ESP32CAM_ESPNOW_SerialBridge_RX.ino

  Role: PC-side receiver dongle (USB Serial <-> ESP-NOW)
  - Plug this ESP32-CAM into the PC via a USB-serial adapter.
  - It exposes a COM port. Your Python app talks to this COM port.
  - It forwards bytes over ESP-NOW to the turret-side ESP32-CAM.
  - It receives bytes from the turret-side ESP32-CAM and prints them to Serial.

  Direct connection: ESP-NOW (no router).

  Setup steps:
  1) Flash this sketch to the PC-side ESP32-CAM.
  2) Open Serial Monitor @ 115200 and note the printed MAC.
  3) Put that MAC into the TX sketch's PEER_MAC.
  4) Flash the TX sketch, note its MAC, put it into this sketch's PEER_MAC.

  Notes:
  - This is a byte bridge. It does NOT implement DB3000 IO logic; it only transports data.
  - Recommended: keep baud at 115200 to match the existing Nano protocol defaults.
*/

#include <WiFi.h>
#include <esp_now.h>
#include <esp_wifi.h>

// ----------------- USER CONFIG -----------------
// Fill this with the turret-side (TX) ESP32-CAM WiFi MAC address.
// Example: {0x24,0x6F,0x28,0xAA,0xBB,0xCC}
static uint8_t PEER_MAC[6] = {0x24, 0x6F, 0x28, 0x00, 0x00, 0x00};

// Both sides MUST use the same WiFi channel for ESP-NOW.
static constexpr uint8_t ESPNOW_CHANNEL = 6;

// Optional LED: ESP32-CAM flash LED is often GPIO4 (AI Thinker).
static constexpr int LED_PIN = 4;
static constexpr bool LED_ACTIVE_HIGH = true;

// Bridge tuning
static constexpr uint32_t SERIAL_BAUD = 115200;
static constexpr uint32_t FLUSH_GAP_MS = 10;   // flush serial buffer if idle for this long
static constexpr size_t   MAX_PAYLOAD = 200;   // <= 240 recommended for ESP-NOW
static constexpr uint8_t  MAX_RETRIES = 3;
static constexpr uint32_t RETRY_MS = 40;
// ------------------------------------------------

// Simple CRC16-CCITT (0x1021) for payload integrity.
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

  // CRC includes header + payload bytes (combined by XOR)
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
    // Drop packet; link is lossy.
    g_havePending = false;
    return;
  }
  g_pendingRetries++;
  esp_now_send(PEER_MAC, (const uint8_t*)&g_pending, sizeof(PacketHeader) + g_pending.h.len + 2);
  g_pendingLastSendMs = now;
}

static void onDataSent(const wifi_tx_info_t* /*info*/, esp_now_send_status_t /*status*/) {
  // esp_now_send_status_t only reports enqueue/PHY status, not end-to-end.
}

static void onDataRecv(const esp_now_recv_info_t* /*info*/, const uint8_t* data, int len) {
  if (len < (int)(sizeof(PacketHeader) + 2)) return;

  const PacketHeader* h = (const PacketHeader*)data;
  const uint8_t* payload = data + sizeof(PacketHeader);
  const uint16_t* pCrc = (const uint16_t*)(data + len - 2);

  if (h->type == PKT_ACK) {
    // CRC check
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

  // Verify CRC
  uint16_t ch = crc16_ccitt((const uint8_t*)h, sizeof(PacketHeader));
  uint16_t cp = crc16_ccitt(payload, h->len);
  uint16_t combined = cp ^ ch;
  if (combined != *pCrc) return;

  // Output to USB Serial (PC reads this)
  Serial.write(payload, h->len);

  // ACK back
  sendAck(h->seq);

  // Visual debug
  ledPulse(10);
}

static bool initEspNow() {
  WiFi.mode(WIFI_STA);
  WiFi.setSleep(false);
  WiFi.disconnect(true, true);

  // Force WiFi channel for ESP-NOW
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

  // Flush if newline present
  for (size_t i = 0; i < g_serialLen; i++) {
    if (g_serialBuf[i] == '\n') {
      sendData(g_serialBuf, g_serialLen);
      g_serialLen = 0;
      return;
    }
  }

  // Flush if idle gap
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
  Serial.println("[ESP-NOW RX] PC-side serial bridge starting...");
  Serial.print("[ESP-NOW RX] MAC: ");
  Serial.println(WiFi.macAddress());

  if (peerMacLooksUnconfigured()) {
    Serial.println("[ESP-NOW RX] WARNING: PEER_MAC not configured. Set TX MAC in this sketch.");
  }

  if (!initEspNow()) {
    Serial.println("[ESP-NOW RX] ERROR: esp_now_init/add_peer failed");
    while (true) {
      ledPulse(80);
      delay(300);
    }
  }

  Serial.print("[ESP-NOW RX] Channel: ");
  Serial.println(ESPNOW_CHANNEL);
  Serial.println("[ESP-NOW RX] Ready. This COM port is your wireless link.");
}

void loop() {
  // Read from USB Serial and send to peer
  while (Serial.available() > 0) {
    int b = Serial.read();
    if (b < 0) break;

    if (g_serialLen < MAX_PAYLOAD) {
      g_serialBuf[g_serialLen++] = (uint8_t)b;
      g_lastSerialByteMs = millis();
    } else {
      // Buffer full; flush.
      sendData(g_serialBuf, g_serialLen);
      g_serialLen = 0;
    }
  }

  flushSerialIfReady();
  retryIfNeeded();
}
