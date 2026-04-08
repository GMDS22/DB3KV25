// Smart Sentry v3.0 Waveshare WiFi UDP Echo Test
// Minimal SoftAP + UDP echo sketch used to separate WiFi-core issues from
// bridge-architecture issues under load.

#include <WiFi.h>
#include <WiFiUdp.h>

static const char *WIFI_SSID = "WAVESHARE-ESP32";
static const char *WIFI_PASS = "smartv3pass";
static const uint16_t UDP_PORT = 9000;

WiFiUDP udp;
static uint32_t lastDiagMs = 0;

void setup() {
  Serial.begin(115200);
  delay(50);

  WiFi.mode(WIFI_AP);
  delay(100);

  bool apOk = WiFi.softAP(WIFI_SSID, WIFI_PASS);
  delay(250);

  IPAddress apIp = WiFi.softAPIP();
  uint8_t udpOk = udp.begin(UDP_PORT);

  Serial.printf("[BOOT] ap=%s ip=%s stations=%d\n",
                apOk ? "OK" : "FAIL",
                apIp.toString().c_str(),
                WiFi.softAPgetStationNum());
  Serial.printf("[BOOT] udp begin=%s port=%u\n",
                udpOk ? "OK" : "FAIL",
                UDP_PORT);
}

void loop() {
  uint32_t nowVal = millis();
  if ((nowVal - lastDiagMs) >= 5000U) {
    lastDiagMs = nowVal;
    Serial.printf("[NET] ap_ip=%s stations=%d heap=%u\n",
                  WiFi.softAPIP().toString().c_str(),
                  WiFi.softAPgetStationNum(),
                  (unsigned)ESP.getFreeHeap());
  }

  int packetLen = udp.parsePacket();
  if (packetLen > 0) {
    char buffer[512];
    int readLen = udp.read(buffer, sizeof(buffer) - 1);
    if (readLen > 0) {
      buffer[readLen] = '\0';
      IPAddress ip = udp.remoteIP();
      uint16_t port = udp.remotePort();
      Serial.printf("[UDP-RX] %d bytes from %s:%u payload=%s\n",
                    readLen,
                    ip.toString().c_str(),
                    port,
                    buffer);
      udp.beginPacket(ip, port);
      udp.write((const uint8_t *)buffer, readLen);
      udp.endPacket();
    }
  }

  delay(1);
}