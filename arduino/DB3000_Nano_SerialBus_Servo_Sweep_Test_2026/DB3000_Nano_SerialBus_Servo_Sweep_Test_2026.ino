/*
  DB3000 Nano Serial Bus Servo Sweep Test (2026)
  ----------------------------------------------
  Purpose:
  - Standalone movement test for serial bus servos using an Arduino Nano.
  - Lets you validate servo wiring/IDs/protocol separately from the main app.

  Expected protocol (Yahboom debug board observed format):
    FF FF ID 07 03 2A POS_H POS_L TIME_H TIME_L CHK
    CHK = 0xFF - (sum(bytes[2..9]) & 0xFF)

  Wiring (Nano <-> Debug Board):
  - D11 (TX) -> Debug board RX
  - D10 (RX) <- Debug board TX
  - GND common between Nano, debug board, and servo power supply

  IMPORTANT:
  - Do NOT power bus servos from Nano 5V.
  - Use dedicated servo power.
  - Default IDs in this sketch: PAN=1, TILT=2.
*/

#include <Arduino.h>
#include <SoftwareSerial.h>

static const uint8_t PIN_BUS_RX = 10; // Nano RX <- debug board TX
static const uint8_t PIN_BUS_TX = 11; // Nano TX -> debug board RX

static const unsigned long HOST_BAUD = 115200;
static const unsigned long BUS_BAUD = 115200;

static const uint8_t SERVO_ID_PAN = 1;
static const uint8_t SERVO_ID_TILT = 2;

// Mechanical test range. Adjust if your mount cannot safely use full travel.
static const int PAN_MIN_DEG = 30;
static const int PAN_MAX_DEG = 210;
static const int TILT_MIN_DEG = 20;
static const int TILT_MAX_DEG = 140;

// Mapping to servo protocol position ticks (0..4095 for 0..270 deg).
static const int SERVO_MIN_DEG_PROTOCOL = 0;
static const int SERVO_MAX_DEG_PROTOCOL = 270;
static const uint16_t SERVO_MIN_TICKS = 0;
static const uint16_t SERVO_MAX_TICKS = 4095;

static const uint16_t MOVE_TIME_MS = 180;
static const uint16_t STEP_DELAY_MS = 240;

SoftwareSerial busSerial(PIN_BUS_RX, PIN_BUS_TX); // RX, TX

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

static void busWrite(const uint8_t *data, size_t len) {
  busSerial.write(data, len);
  busSerial.flush();
}

static void writeServoPosition(uint8_t id, int deg, uint16_t moveTimeMs) {
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

  busWrite(pkt, sizeof(pkt));
}

static void moveBoth(int panDeg, int tiltDeg) {
  writeServoPosition(SERVO_ID_PAN, panDeg, MOVE_TIME_MS);
  delay(4);
  writeServoPosition(SERVO_ID_TILT, tiltDeg, MOVE_TIME_MS);

  Serial.print(F("MOVE pan="));
  Serial.print(panDeg);
  Serial.print(F(" tilt="));
  Serial.println(tiltDeg);
}

void setup() {
  Serial.begin(HOST_BAUD);
  busSerial.begin(BUS_BAUD);

  delay(300);
  Serial.println(F("Nano serial bus servo sweep test starting..."));
  Serial.println(F("Pattern: center -> corners -> sweep loop"));

  // Initial center position.
  moveBoth((PAN_MIN_DEG + PAN_MAX_DEG) / 2, (TILT_MIN_DEG + TILT_MAX_DEG) / 2);
  delay(700);

  // Corner checks.
  moveBoth(PAN_MIN_DEG, TILT_MIN_DEG);
  delay(600);
  moveBoth(PAN_MAX_DEG, TILT_MAX_DEG);
  delay(600);
}

void loop() {
  // Repeating box sweep pattern for visible movement test.
  moveBoth(PAN_MIN_DEG, TILT_MIN_DEG);
  delay(STEP_DELAY_MS);

  moveBoth(PAN_MAX_DEG, TILT_MIN_DEG);
  delay(STEP_DELAY_MS);

  moveBoth(PAN_MAX_DEG, TILT_MAX_DEG);
  delay(STEP_DELAY_MS);

  moveBoth(PAN_MIN_DEG, TILT_MAX_DEG);
  delay(STEP_DELAY_MS);

  moveBoth((PAN_MIN_DEG + PAN_MAX_DEG) / 2, (TILT_MIN_DEG + TILT_MAX_DEG) / 2);
  delay(450);
}
