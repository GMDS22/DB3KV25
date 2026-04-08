#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>

static const char *AP_SSID = "SMART-SENTRY-V3";
static const char *AP_PASS = "12345678";
static const uint16_t UDP_PORT = 9000;

static const int PIN_BUZZER = 4;
static const int PIN_TRIGGER = 27;
static const int PIN_RELAY1 = 25;
static const int PIN_RELAY2 = 26;

WiFiUDP udp;
unsigned long lastDiag = 0;

void handleUDP();

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println();
  Serial.println("[BOOT] Step 1-4 Bridge Test Starting");

  pinMode(PIN_BUZZER, OUTPUT);
  pinMode(PIN_TRIGGER, OUTPUT);
  pinMode(PIN_RELAY1, OUTPUT);
  pinMode(PIN_RELAY2, OUTPUT);

  digitalWrite(PIN_BUZZER, LOW);
  digitalWrite(PIN_TRIGGER, LOW);
  digitalWrite(PIN_RELAY1, LOW);
  digitalWrite(PIN_RELAY2, LOW);

  Serial.println("[GPIO] Initialized (no control active)");

  WiFi.mode(WIFI_AP);
  WiFi.softAP(AP_SSID, AP_PASS);

  IPAddress ip = WiFi.softAPIP();
  Serial.print("[WIFI] AP IP: ");
  Serial.println(ip);

  if (udp.begin(UDP_PORT)) {
    Serial.println("[UDP] Listening on port 9000");
  } else {
    Serial.println("[UDP] FAILED to start");
  }
}

void loop() {
  handleUDP();

  if (millis() - lastDiag > 2000) {
    lastDiag = millis();
    Serial.printf("[DIAG] stations=%d heap=%u\n",
                  WiFi.softAPgetStationNum(),
                  ESP.getFreeHeap());
  }

  delay(1);
}

void handleUDP() {
  int packetSize = udp.parsePacket();
  if (!packetSize) return;

  char buffer[512];
  int len = udp.read(buffer, sizeof(buffer) - 1);
  if (len <= 0) return;

  buffer[len] = '\0';

  Serial.print("[UDP RX] ");
  Serial.println(buffer);

  StaticJsonDocument<256> doc;
  DeserializationError err = deserializeJson(doc, buffer);

  StaticJsonDocument<256> resp;

  if (err) {
    resp["status"] = "parse_error";
  } else {
    resp["status"] = "ok";

    if (doc.containsKey("cmd")) {
      resp["cmd"] = doc["cmd"].as<const char *>();
    }

    resp["free_heap"] = ESP.getFreeHeap();
    resp["stations"] = WiFi.softAPgetStationNum();
  }

  char out[256];
  size_t outLen = serializeJson(resp, out);

  udp.beginPacket(udp.remoteIP(), udp.remotePort());
  udp.write((uint8_t *)out, outLen);
  udp.endPacket();

  Serial.print("[UDP TX] ");
  Serial.println(out);
}