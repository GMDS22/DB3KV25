/*
  DB3000 Nano Direct Serial Bus Servo Test (2026)
  -----------------------------------------------
  Purpose:
  - Test a serial-bus servo directly from Arduino Nano (no debug board).
  - Helps isolate whether the servo or debug board is faulty.

  Bus style:
  - Single-wire half-duplex TTL bus on one Nano pin.

  Wiring (direct):
  - Nano D10 <-> Servo DATA (recommended through ~1k series resistor)
  - Nano GND  -> Servo GND
  - External PSU + -> Servo V+
  - External PSU - -> Servo GND
  - Common ground is mandatory.

  Safety:
  - Do NOT power the servo from Nano 5V.
*/

#include <Arduino.h>
#include <SoftwareSerial.h>

static const uint8_t PIN_BUS_IO = 10; // single-wire half-duplex bus pin
static const unsigned long HOST_BAUD = 115200;
static const unsigned long BUS_BAUD = 115200;

// Default test ID. Use serial command "ID <n>" if your servo uses another ID.
static uint8_t targetId = 1;

// Protocol angle mapping (Yahboom-style 0..4095 ticks for 0..270 degrees).
static const int SERVO_MIN_DEG_PROTOCOL = 0;
static const int SERVO_MAX_DEG_PROTOCOL = 270;
static const uint16_t SERVO_MIN_TICKS = 0;
static const uint16_t SERVO_MAX_TICKS = 4095;

// Sweep range (safe-ish defaults; adjust for your mechanism).
static const int SWEEP_MIN_DEG = 20;
static const int SWEEP_MAX_DEG = 240;

SoftwareSerial busSerial(PIN_BUS_IO, PIN_BUS_IO); // RX, TX on same pin

static uint8_t checksum_ff_minus_sum(const uint8_t *pkt, uint8_t startIdx, uint8_t endIdxInclusive) {
  uint16_t sum = 0;
  for (uint8_t i = startIdx; i <= endIdxInclusive; i++) {
    sum += pkt[i];
  }
  return (uint8_t)(0xFF - (sum & 0xFF));
}

static int clampInt(int v, int lo, int hi) {
  if (v < lo) return lo;
  if (v > hi) return hi;
  return v;
}

static uint16_t mapDegToTicks(int deg) {
  deg = clampInt(deg, SERVO_MIN_DEG_PROTOCOL, SERVO_MAX_DEG_PROTOCOL);

  const long degSpan = (long)SERVO_MAX_DEG_PROTOCOL - (long)SERVO_MIN_DEG_PROTOCOL;
  const long tickSpan = (long)SERVO_MAX_TICKS - (long)SERVO_MIN_TICKS;
  const long relDeg = (long)deg - (long)SERVO_MIN_DEG_PROTOCOL;

  long ticks = (long)SERVO_MIN_TICKS + (relDeg * tickSpan) / degSpan;
  if (ticks < SERVO_MIN_TICKS) ticks = SERVO_MIN_TICKS;
  if (ticks > SERVO_MAX_TICKS) ticks = SERVO_MAX_TICKS;
  return (uint16_t)ticks;
}

static void busWriteHalfDuplex(const uint8_t *data, size_t len) {
  pinMode(PIN_BUS_IO, OUTPUT);
  delayMicroseconds(30);
  busSerial.write(data, len);
  busSerial.flush();
  delayMicroseconds(80);
  pinMode(PIN_BUS_IO, INPUT);
}

static void sendMove(uint8_t id, int deg, uint16_t moveTimeMs) {
  const uint16_t posTicks = mapDegToTicks(deg);
  const uint8_t posH = (uint8_t)((posTicks >> 8) & 0xFF);
  const uint8_t posL = (uint8_t)(posTicks & 0xFF);
  const uint8_t timeH = (uint8_t)((moveTimeMs >> 8) & 0xFF);
  const uint8_t timeL = (uint8_t)(moveTimeMs & 0xFF);

  uint8_t pkt[11];
  pkt[0] = 0xFF;
  pkt[1] = 0xFF;
  pkt[2] = id;
  pkt[3] = 0x07;
  pkt[4] = 0x03;
  pkt[5] = 0x2A;
  pkt[6] = posH;
  pkt[7] = posL;
  pkt[8] = timeH;
  pkt[9] = timeL;
  pkt[10] = checksum_ff_minus_sum(pkt, 2, 9);

  busWriteHalfDuplex(pkt, sizeof(pkt));
}

static bool pingServo(uint8_t id, uint16_t timeoutMs) {
  // Ping packet: FF FF ID 02 01 CHK
  uint8_t pkt[6];
  pkt[0] = 0xFF;
  pkt[1] = 0xFF;
  pkt[2] = id;
  pkt[3] = 0x02;
  pkt[4] = 0x01;
  pkt[5] = checksum_ff_minus_sum(pkt, 2, 4);

  while (busSerial.available() > 0) {
    (void)busSerial.read();
  }

  busWriteHalfDuplex(pkt, sizeof(pkt));

  const uint32_t start = millis();
  uint8_t buf[32];
  uint8_t n = 0;
  while ((millis() - start) < timeoutMs && n < sizeof(buf)) {
    if (busSerial.available() > 0) {
      buf[n++] = (uint8_t)busSerial.read();
      if (n >= 6) {
        for (uint8_t i = 0; i + 5 < n; i++) {
          if (buf[i] == 0xFF && buf[i + 1] == 0xF5 && buf[i + 2] == id) {
            return true;
          }
        }
      }
    }
  }
  return false;
}

static void scanIds() {
  Serial.println(F("Scanning IDs 1..20"));
  bool foundAny = false;
  for (uint8_t id = 1; id <= 20; id++) {
    if (pingServo(id, 50)) {
      Serial.print(F("FOUND ID="));
      Serial.println(id);
      foundAny = true;
    }
    delay(8);
  }
  if (!foundAny) {
    Serial.println(F("No servo response in range 1..20"));
  }
}

static void runSweepCycle() {
  sendMove(targetId, SWEEP_MIN_DEG, 220);
  Serial.print(F("MOVE ID=")); Serial.print(targetId); Serial.print(F(" DEG=")); Serial.println(SWEEP_MIN_DEG);
  delay(650);

  sendMove(targetId, SWEEP_MAX_DEG, 220);
  Serial.print(F("MOVE ID=")); Serial.print(targetId); Serial.print(F(" DEG=")); Serial.println(SWEEP_MAX_DEG);
  delay(650);

  sendMove(targetId, (SWEEP_MIN_DEG + SWEEP_MAX_DEG) / 2, 220);
  Serial.print(F("MOVE ID=")); Serial.print(targetId); Serial.print(F(" DEG=")); Serial.println((SWEEP_MIN_DEG + SWEEP_MAX_DEG) / 2);
  delay(500);
}

// Simple serial commands:
// SCAN
// ID <n>
// MOVE <deg>
// SWEEP
static char lineBuf[64];
static size_t lineLen = 0;
static bool sweepEnabled = true;

static void handleCommand(char *line) {
  while (*line == ' ' || *line == '\t') line++;
  if (*line == 0) return;

  if (strncmp(line, "SCAN", 4) == 0) {
    scanIds();
    return;
  }

  if (strncmp(line, "SWEEP", 5) == 0) {
    sweepEnabled = true;
    Serial.println(F("SWEEP ON"));
    return;
  }

  if (strncmp(line, "STOP", 4) == 0) {
    sweepEnabled = false;
    Serial.println(F("SWEEP OFF"));
    return;
  }

  if (strncmp(line, "ID", 2) == 0) {
    int id = atoi(line + 2);
    if (id >= 1 && id <= 253) {
      targetId = (uint8_t)id;
      Serial.print(F("TARGET ID="));
      Serial.println(targetId);
    } else {
      Serial.println(F("ID must be 1..253"));
    }
    return;
  }

  if (strncmp(line, "MOVE", 4) == 0) {
    int deg = atoi(line + 4);
    deg = clampInt(deg, SERVO_MIN_DEG_PROTOCOL, SERVO_MAX_DEG_PROTOCOL);
    sendMove(targetId, deg, 200);
    Serial.print(F("MOVE ID=")); Serial.print(targetId); Serial.print(F(" DEG=")); Serial.println(deg);
    return;
  }

  Serial.println(F("Commands: SCAN | ID <n> | MOVE <deg> | SWEEP | STOP"));
}

void setup() {
  Serial.begin(HOST_BAUD);
  busSerial.begin(BUS_BAUD);

  pinMode(PIN_BUS_IO, INPUT);

  delay(400);
  Serial.println(F("Direct serial bus servo test started."));
  Serial.println(F("Commands: SCAN | ID <n> | MOVE <deg> | SWEEP | STOP"));
  Serial.println(F("Default: running sweep on ID=1"));

  scanIds();
}

void loop() {
  while (Serial.available() > 0) {
    char c = (char)Serial.read();
    if (c == '\r' || c == '\n') {
      if (lineLen > 0) {
        lineBuf[lineLen] = 0;
        handleCommand(lineBuf);
        lineLen = 0;
      }
    } else if (lineLen + 1 < sizeof(lineBuf)) {
      lineBuf[lineLen++] = c;
    }
  }

  if (sweepEnabled) {
    runSweepCycle();
  } else {
    delay(20);
  }
}
