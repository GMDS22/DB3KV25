// ESP8266 ESPNOW Serial Bridge (RX / USB-side)
// USB Serial <-> ESP-NOW
//
// How to use:
// 1) Flash this sketch to the ESP8266 that will be plugged into the laptop (USB).
// 2) Flash the TX sketch to the ESP8266 on the turret.
// 3) Open Serial Monitor at 115200 on both and note each device's MAC.
// 4) Paste the peer MAC into the other sketch (PEER_MAC), reflash both (recommended for unicast reliability).
//
// Notes:
// - ESP-NOW requires both devices to be on the same Wi-Fi channel.
// - This code uses a fixed channel for predictability.

#include <Arduino.h>
#include <ESP8266WiFi.h>

extern "C" {
#include <espnow.h>
#include <user_interface.h>
}

// ---------------- Config ----------------

static constexpr uint8_t ESPNOW_CHANNEL = 1;
static constexpr uint32_t SERIAL_BAUD = 115200;

// Set to the peer's MAC for unicast (recommended). If left as FF:FF... it will broadcast.
static uint8_t PEER_MAC[6] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};

static constexpr uint16_t MAX_PAYLOAD = 200;
static constexpr uint16_t RING_SIZE = 1024;

static constexpr uint8_t MAX_RETRIES = 6;
static constexpr uint32_t RETRY_MS = 35;

// Send buffered serial when newline arrives or after idle gap.
static constexpr uint32_t SERIAL_IDLE_FLUSH_MS = 12;

// ---------------- Packet ----------------

enum PacketType : uint8_t {
  PKT_DATA = 1,
  PKT_ACK = 2,
};

struct __attribute__((packed)) Packet {
  uint8_t type;
  uint8_t seq;
  uint16_t len;
  uint8_t payload[MAX_PAYLOAD];
  uint16_t crc;
};

static uint16_t crc16_ccitt(const uint8_t* data, size_t len) {
  uint16_t crc = 0xFFFF;
  for (size_t i = 0; i < len; i++) {
    crc ^= (uint16_t)data[i] << 8;
    for (uint8_t b = 0; b < 8; b++) {
      if (crc & 0x8000) crc = (crc << 1) ^ 0x1021;
      else crc <<= 1;
    }
  }
  return crc;
}

static uint16_t packet_crc(const Packet& p) {
  // CRC over header + payload (excluding crc field)
  const size_t headerLen = sizeof(p.type) + sizeof(p.seq) + sizeof(p.len);
  uint16_t crc = 0xFFFF;
  crc = crc16_ccitt(reinterpret_cast<const uint8_t*>(&p), headerLen);
  crc ^= crc16_ccitt(p.payload, p.len);
  return crc;
}

// ---------------- RX ring (ESP-NOW -> Serial) ----------------

static uint8_t rxRing[RING_SIZE];
static volatile uint16_t rxHead = 0;
static volatile uint16_t rxTail = 0;

static inline bool ringPush(uint8_t b) {
  const uint16_t next = (uint16_t)((rxHead + 1) % RING_SIZE);
  if (next == rxTail) return false;
  rxRing[rxHead] = b;
  rxHead = next;
  return true;
}

static inline int ringPop() {
  if (rxTail == rxHead) return -1;
  const uint8_t b = rxRing[rxTail];
  rxTail = (uint16_t)((rxTail + 1) % RING_SIZE);
  return (int)b;
}

// ---------------- TX state (Serial -> ESP-NOW) ----------------

static uint8_t txSeq = 0;
static Packet pending{};
static bool pendingActive = false;
static uint8_t pendingRetries = 0;
static uint32_t pendingLastSendMs = 0;

static uint8_t lastPeerMac[6] = {0};
static bool haveLastPeerMac = false;

static volatile bool ackReady = false;
static volatile uint8_t ackSeq = 0;
static uint8_t ackMac[6] = {0};

static uint8_t serialBuf[MAX_PAYLOAD];
static uint16_t serialBufLen = 0;
static uint32_t lastSerialByteMs = 0;

static void printMac(const uint8_t* mac) {
  for (int i = 0; i < 6; i++) {
    if (i) Serial.print(":");
    if (mac[i] < 16) Serial.print("0");
    Serial.print(mac[i], HEX);
  }
}

static bool isBroadcastMac(const uint8_t* mac) {
  for (int i = 0; i < 6; i++) {
    if (mac[i] != 0xFF) return false;
  }
  return true;
}

static void ensurePeer(const uint8_t* mac) {
  // Safe to call repeatedly; espnow will ignore duplicates.
  esp_now_add_peer(const_cast<uint8_t*>(mac), ESP_NOW_ROLE_COMBO, ESPNOW_CHANNEL, nullptr, 0);
}

static bool sendPacketTo(const uint8_t* mac, const Packet& pkt) {
  ensurePeer(mac);
  const uint16_t totalLen = (uint16_t)(sizeof(pkt.type) + sizeof(pkt.seq) + sizeof(pkt.len) + pkt.len + sizeof(pkt.crc));
  return esp_now_send(const_cast<uint8_t*>(mac), (uint8_t*)&pkt, totalLen) == 0;
}

static void startPendingSend(const uint8_t* dstMac, const uint8_t* data, uint16_t len) {
  if (len == 0 || len > MAX_PAYLOAD) return;

  pending = {};
  pending.type = PKT_DATA;
  pending.seq = txSeq++;
  pending.len = len;
  memcpy(pending.payload, data, len);
  pending.crc = packet_crc(pending);

  pendingActive = true;
  pendingRetries = 0;
  pendingLastSendMs = 0;

  (void)sendPacketTo(dstMac, pending);
  pendingLastSendMs = millis();
}

static void flushSerialIfNeeded(bool force) {
  const uint32_t now = millis();
  if (serialBufLen == 0) return;
  if (!force) {
    if (serialBuf[serialBufLen - 1] != '\n' && (now - lastSerialByteMs) < SERIAL_IDLE_FLUSH_MS) return;
  }
  if (pendingActive) return; // wait for ACK

  const uint8_t* dst = PEER_MAC;
  if (isBroadcastMac(PEER_MAC) && haveLastPeerMac) dst = lastPeerMac;

  startPendingSend(dst, serialBuf, serialBufLen);
  serialBufLen = 0;
}

// ---------------- ESP-NOW callbacks ----------------

static void onDataSent(uint8_t* mac_addr, uint8_t sendStatus) {
  (void)mac_addr;
  (void)sendStatus;
  // Actual reliability handled by ACK packets; we keep this callback minimal.
}

static void onDataRecv(uint8_t* mac, uint8_t* incomingData, uint8_t len) {
  if (len < (int)(sizeof(uint8_t) + sizeof(uint8_t) + sizeof(uint16_t) + sizeof(uint16_t))) return;

  Packet p{};
  const uint8_t* raw = incomingData;
  p.type = raw[0];
  p.seq = raw[1];
  memcpy(&p.len, raw + 2, sizeof(uint16_t));
  if (p.len > MAX_PAYLOAD) return;

  const uint16_t expectedLen = (uint16_t)(sizeof(uint8_t) + sizeof(uint8_t) + sizeof(uint16_t) + p.len + sizeof(uint16_t));
  if (len != expectedLen) return;

  if (p.len) memcpy(p.payload, raw + 4, p.len);
  memcpy(&p.crc, raw + 4 + p.len, sizeof(uint16_t));

  const uint16_t calc = packet_crc(p);
  if (calc != p.crc) return;

  // Track last sender for dynamic unicast if PEER_MAC is broadcast.
  memcpy(lastPeerMac, mac, 6);
  haveLastPeerMac = true;

  if (p.type == PKT_DATA) {
    for (uint16_t i = 0; i < p.len; i++) {
      ringPush(p.payload[i]);
    }

    // Queue an ACK back to sender.
    memcpy(ackMac, mac, 6);
    ackSeq = p.seq;
    ackReady = true;
  } else if (p.type == PKT_ACK) {
    if (pendingActive && p.seq == pending.seq) {
      pendingActive = false;
      pendingRetries = 0;
    }
  }
}

static void sendAckIfReady() {
  if (!ackReady) return;
  ackReady = false;

  Packet ack{};
  ack.type = PKT_ACK;
  ack.seq = ackSeq;
  ack.len = 0;
  ack.crc = packet_crc(ack);

  (void)sendPacketTo(ackMac, ack);
}

static void retryPendingIfNeeded() {
  if (!pendingActive) return;
  const uint32_t now = millis();
  if ((now - pendingLastSendMs) < RETRY_MS) return;

  if (pendingRetries >= MAX_RETRIES) {
    pendingActive = false;
    pendingRetries = 0;
    return;
  }

  const uint8_t* dst = PEER_MAC;
  if (isBroadcastMac(PEER_MAC) && haveLastPeerMac) dst = lastPeerMac;

  (void)sendPacketTo(dst, pending);
  pendingLastSendMs = now;
  pendingRetries++;
}

// ---------------- Setup/loop ----------------

static void setupEspNow() {
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();

  wifi_set_channel(ESPNOW_CHANNEL);

  if (esp_now_init() != 0) {
    Serial.println("ESP-NOW init failed");
    return;
  }

  esp_now_set_self_role(ESP_NOW_ROLE_COMBO);
  esp_now_register_send_cb(onDataSent);
  esp_now_register_recv_cb(onDataRecv);

  // Add broadcast peer always, so first contact works.
  uint8_t broadcast[6] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};
  ensurePeer(broadcast);

  // If user provided explicit peer MAC, add it now.
  if (!isBroadcastMac(PEER_MAC)) ensurePeer(PEER_MAC);
}

void setup() {
  Serial.begin(SERIAL_BAUD);
  delay(200);

  Serial.println();
  Serial.println("ESP8266 ESPNOW SerialBridge RX (USB-side)");
  Serial.print("My MAC: ");
  uint8_t mac[6];
  WiFi.macAddress(mac);
  printMac(mac);
  Serial.println();

  setupEspNow();
}

void loop() {
  // Serial -> ESP-NOW
  while (Serial.available() > 0) {
    const int c = Serial.read();
    if (c < 0) break;

    if (serialBufLen < MAX_PAYLOAD) {
      serialBuf[serialBufLen++] = (uint8_t)c;
      lastSerialByteMs = millis();
    }

    if ((uint8_t)c == '\n') {
      flushSerialIfNeeded(true);
    }
  }

  flushSerialIfNeeded(false);
  retryPendingIfNeeded();
  sendAckIfReady();

  // ESP-NOW -> Serial
  int b;
  while ((b = ringPop()) >= 0) {
    Serial.write((uint8_t)b);
  }
}
