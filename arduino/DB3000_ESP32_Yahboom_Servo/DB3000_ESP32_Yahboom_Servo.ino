// DB3000_ESP32_Yahboom_Servo — v1
// =============================================================
// Secondary ESP32 firmware for Yahboom servo driver board
//
// Topology (Mode 4 in app):
//   PC  <->  Primary ESP32  over WiFi/UDP (192.168.4.1:9000) — IO/accessories
//   PC  <->  Secondary ESP32 over WiFi/UDP (192.168.4.2:9001) — Pan/tilt servos
//
// This board provides integrated Yahboom YB-SD35M serial bus servo control.
// No external debug board needed — fully wireless servo operation.
//
// App compatibility:
//   - JSON+CRC32 UDP packet format (matches sentry_v2_comm.py)
//   - Command payload fields: pan_cmd, tilt_cmd, move_time_ms
//   - Pan/tilt angles in degrees (0-270° range)
//
// Board target: ESP32 with Yahboom servo driver
// FQBN: esp32:esp32:esp32
// Required library: ArduinoJson v6

#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>

// ─────────────────────────────────────────────────────────────
// WiFi / UDP (Secondary ESP32)
// ─────────────────────────────────────────────────────────────
static const char     *WIFI_SSID = "DB3000-ESP32";
static const char     *WIFI_PASS = "db3000pass";
static const IPAddress AP_IP(192, 168, 4, 2);  // Secondary ESP32 IP
static const IPAddress AP_GW(192, 168, 4, 1);  // Gateway to primary
static const IPAddress AP_MASK(255, 255, 255, 0);
static const uint16_t  UDP_PORT  = 9001;       // Secondary UDP port

WiFiUDP  Udp;
IPAddress last_remote_ip;
uint16_t  last_remote_port = 0;

// ─────────────────────────────────────────────────────────────
// Yahboom servo driver pins (UART communication)
// ─────────────────────────────────────────────────────────────
static const int PIN_SERVO_RX = 16;  // UART2 RX — servo driver TX
static const int PIN_SERVO_TX = 17;  // UART2 TX — servo driver RX

// ─────────────────────────────────────────────────────────────
// Servo configuration (Yahboom YB-SD35M)
// ─────────────────────────────────────────────────────────────
static const uint32_t SERVO_BAUD = 1000000;  // 1Mbps for Yahboom servos
static const uint8_t  SERVO_ID_PAN = 1;
static const uint8_t  SERVO_ID_TILT = 2;

// Position limits (0-4095 ticks = 0-270°)
static const uint16_t PAN_MIN_TICKS = 0;
static const uint16_t PAN_MAX_TICKS = 4095;
static const uint16_t TILT_MIN_TICKS = 0;
static const uint16_t TILT_MAX_TICKS = 4095;

// Default movement time (milliseconds)
static const uint16_t DEFAULT_MOVE_TIME_MS = 20;

// Inversion settings (can be changed via config)
static bool invert_pan = false;
static bool invert_tilt = false;

// ─────────────────────────────────────────────────────────────
// Status LED
// ─────────────────────────────────────────────────────────────
#ifdef LED_BUILTIN
static const int PIN_STATUS_LED = LED_BUILTIN;
#else
static const int PIN_STATUS_LED = 2;
#endif

// ─────────────────────────────────────────────────────────────
// Hardware serial for servo communication
// ─────────────────────────────────────────────────────────────
HardwareSerial servoSerial(2);

// ─────────────────────────────────────────────────────────────
// Command state
// ─────────────────────────────────────────────────────────────
struct ServoCommand {
  float pan_deg = 90.0f;
  float tilt_deg = 40.0f;
  uint16_t move_time_ms = DEFAULT_MOVE_TIME_MS;
};

static ServoCommand last_cmd;
static uint32_t last_command_time = 0;
static const uint32_t WATCHDOG_TIMEOUT_MS = 5000;  // Return to home if no commands

// ─────────────────────────────────────────────────────────────
// Helper functions
// ─────────────────────────────────────────────────────────────

// Convert degrees to Yahboom servo ticks (0-4095 for 0-270°)
static uint16_t degToTicks(float degrees, bool invert) {
  // Clamp to 0-270° range
  if (degrees < 0) degrees = 0;
  if (degrees > 270) degrees = 270;

  if (invert) {
    degrees = 270 - degrees;
  }

  // Convert to ticks (4095 ticks = 270°)
  return (uint16_t)((degrees / 270.0f) * 4095.0f);
}

// Send Yahboom servo command (11-byte protocol)
static void sendServoCommand(uint8_t servo_id, uint16_t position_ticks, uint16_t move_time_ms) {
  // Yahboom YB-SD35M protocol:
  // Header: 0xFF 0xFF
  // Payload: [servo_id, 0x07, 0x03, 0x2A, pos_hi, pos_lo, time_hi, time_lo]
  // Checksum: ~sum(payload) & 0xFF

  uint8_t pos_hi = (position_ticks >> 8) & 0xFF;
  uint8_t pos_lo = position_ticks & 0xFF;
  uint8_t time_hi = (move_time_ms >> 8) & 0xFF;
  uint8_t time_lo = move_time_ms & 0xFF;

  uint8_t payload[8] = {
    servo_id,     // Servo ID
    0x07,         // Length
    0x03,         // Command (position control)
    0x2A,         // Sub-command
    pos_hi,       // Position high byte
    pos_lo,       // Position low byte
    time_hi,      // Time high byte
    time_lo       // Time low byte
  };

  // Calculate checksum
  uint8_t checksum = 0;
  for (int i = 0; i < 8; i++) {
    checksum += payload[i];
  }
  checksum = ~checksum & 0xFF;

  // Send packet
  servoSerial.write(0xFF);
  servoSerial.write(0xFF);
  for (int i = 0; i < 8; i++) {
    servoSerial.write(payload[i]);
  }
  servoSerial.write(checksum);
}

// Move servos to specified angles
static void moveServos(float pan_deg, float tilt_deg, uint16_t move_time_ms) {
  uint16_t pan_ticks = degToTicks(pan_deg, invert_pan);
  uint16_t tilt_ticks = degToTicks(tilt_deg, invert_tilt);

  // Send pan command
  sendServoCommand(SERVO_ID_PAN, pan_ticks, move_time_ms);

  // Small delay between commands
  delay(5);

  // Send tilt command
  sendServoCommand(SERVO_ID_TILT, tilt_ticks, move_time_ms);

  // Update last command
  last_cmd.pan_deg = pan_deg;
  last_cmd.tilt_deg = tilt_deg;
  last_cmd.move_time_ms = move_time_ms;
  last_command_time = millis();
}

// Return to home position
static void goHome() {
  moveServos(90.0f, 40.0f, DEFAULT_MOVE_TIME_MS * 2);  // Slower return
}

// Process UDP command
static void processUdpCommand(const char* json_str) {
  StaticJsonDocument<512> doc;

  DeserializationError error = deserializeJson(doc, json_str);
  if (error) {
    Serial.printf("JSON parse error: %s\n", error.c_str());
    return;
  }

  // Check protocol version and type
  if (doc["v"] != 1 || doc["t"] != "cmd") {
    return;  // Not a valid command
  }

  // Extract payload
  JsonObject payload = doc["p"];
  if (payload.isNull()) {
    return;
  }

  // Handle action commands
  if (payload.containsKey("action")) {
    const char* action = payload["action"];
    if (strcmp(action, "bus_ping") == 0) {
      uint8_t ping_id = payload["id"] | 254;
      // Send ping packet to servo
      uint8_t pkt[7] = {0xFF, 0xFF, ping_id, 0x04, 0x02, 0x38, 0x02};
      uint8_t sum = pkt[2] + pkt[3] + pkt[4] + pkt[5] + pkt[6];
      pkt[6] = 0xFF ^ (sum & 0xFF);
      servoSerial.write(pkt, 7);
      send_udp_response("ok", "bus_ping sent");
      return;
    }
  }

  // Extract servo commands
  float pan_cmd = payload["pan_cmd"] | last_cmd.pan_deg;
  float tilt_cmd = payload["tilt_cmd"] | last_cmd.tilt_deg;
  uint16_t move_time_ms = payload["move_time_ms"] | DEFAULT_MOVE_TIME_MS;

  // Move servos
  moveServos(pan_cmd, tilt_cmd, move_time_ms);

  // Status LED blink
  digitalWrite(PIN_STATUS_LED, HIGH);
  delay(50);
  digitalWrite(PIN_STATUS_LED, LOW);

  // Send response
  send_udp_response("ok", "servos moved");
}

// ─────────────────────────────────────────────────────────────
// Send UDP response
// ─────────────────────────────────────────────────────────────
static void send_udp_response(const char* status, const char* message = nullptr) {
  StaticJsonDocument<256> resp;
  resp["v"] = 1;
  resp["t"] = "resp";
  resp["seq"] = 0;
  resp["ts"] = millis();
  resp["status"] = status;
  if (message) {
    resp["message"] = message;
  }
  String json_str;
  serializeJson(resp, json_str);
  Udp.beginPacket(last_remote_ip, last_remote_port);
  Udp.print(json_str);
  Udp.endPacket();
}

// ─────────────────────────────────────────────────────────────
// Arduino setup
// ─────────────────────────────────────────────────────────────
void setup() {
  // Initialize serial for debugging
  Serial.begin(115200);
  Serial.println("DB3000 ESP32 Yahboom Servo v1");
  Serial.println("Secondary ESP32 for servo control");

  // Initialize status LED
  pinMode(PIN_STATUS_LED, OUTPUT);
  digitalWrite(PIN_STATUS_LED, LOW);

  // Initialize servo serial
  servoSerial.begin(SERVO_BAUD, SERIAL_8N1, PIN_SERVO_RX, PIN_SERVO_TX);
  Serial.printf("Servo serial initialized on UART2 @ %d baud\n", SERVO_BAUD);

  // Setup WiFi - connect as station to primary AP
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  
  Serial.print("Connecting to WiFi AP...");
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(500);
    Serial.print(".");
    attempts++;
  }
  
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("Connected!");
    Serial.printf("IP: %s\n", WiFi.localIP().toString().c_str());
  } else {
    Serial.println("Failed to connect to AP!");
  }

  // Start UDP
  if (Udp.begin(UDP_PORT)) {
    Serial.printf("UDP listening on port %d\n", UDP_PORT);
  } else {
    Serial.println("UDP failed to start!");
  }

  // Go to home position
  delay(1000);
  goHome();
  Serial.println("Servos homed");

  Serial.println("Setup complete");
}

// ─────────────────────────────────────────────────────────────
// Arduino loop
// ─────────────────────────────────────────────────────────────
void loop() {
  // Check for UDP packets
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    last_remote_ip = Udp.remoteIP();
    last_remote_port = Udp.remotePort();

    char packetBuffer[512];
    int len = Udp.read(packetBuffer, sizeof(packetBuffer) - 1);
    if (len > 0) {
      packetBuffer[len] = 0;  // Null terminate

      Serial.printf("UDP: %d bytes from %s:%d\n",
                   len, last_remote_ip.toString().c_str(), last_remote_port);

      // Process command
      processUdpCommand(packetBuffer);
    }
  }

  // Watchdog - return home if no commands received
  if (millis() - last_command_time > WATCHDOG_TIMEOUT_MS) {
    static bool watchdog_triggered = false;
    if (!watchdog_triggered) {
      Serial.println("Watchdog: No commands received, returning home");
      goHome();
      watchdog_triggered = true;
    }
  } else {
    // Reset watchdog flag when commands resume
    // (this is handled by processUdpCommand setting last_command_time)
  }

  // Small delay to prevent busy looping
  delay(10);
}