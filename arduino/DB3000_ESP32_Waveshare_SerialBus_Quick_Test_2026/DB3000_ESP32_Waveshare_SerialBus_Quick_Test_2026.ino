/*
  DB3000 ESP32 Waveshare Serial Bus Auto-Probe Test (2026)
  ---------------------------------------------------------
  Purpose:
  - ESP32-only movement test for integrated serial-bus driver boards.
  - Tries multiple baud rates and checksum modes for Yahboom-style packets.

  Why:
  - If there is a baud/protocol mismatch, this sketch cycles combinations so
    one phase should produce movement when routing is correct.

  Wiring mode expected:
  - PC connected to ESP32 Type-C only (for flash/logs)
  - Servo powered externally
  - UART switch set to ESP32 control path
*/

#include <Arduino.h>

static const uint32_t HOST_BAUD = 115200;

static const int PIN_SERVO_RX = 16;
static const int PIN_SERVO_TX = 17;

static const uint8_t SERVO_ID_PAN = 1;
static const uint8_t SERVO_ID_TILT = 2;

static const uint32_t BAUD_OPTIONS[] = {115200, 1000000, 57600, 230400};
static const size_t BAUD_COUNT = sizeof(BAUD_OPTIONS) / sizeof(BAUD_OPTIONS[0]);

enum ChecksumMode {
  CHK_SUB = 0, // 0xFF - sum
  CHK_XOR = 1  // 0xFF ^ sum
};

static const uint16_t MOVE_TIME_MS = 350;
static const uint32_t PHASE_HOLD_MS = 9000;

HardwareSerial servoSerial(2);

static int clampInt(int value, int minValue, int maxValue) {
  if (value < minValue) return minValue;
  if (value > maxValue) return maxValue;
  return value;
}

static uint16_t degToTicks(int deg) {
  deg = clampInt(deg, 0, 270);
  return (uint16_t)((deg * 4095L) / 270L);
}

static uint8_t calcChecksum(const uint8_t *pkt, uint8_t startIdx, uint8_t endIdxInclusive, ChecksumMode mode) {
  uint16_t sum = 0;
  for (uint8_t i = startIdx; i <= endIdxInclusive; i++) {
    sum += pkt[i];
  }
  const uint8_t s = (uint8_t)(sum & 0xFF);
  if (mode == CHK_XOR) return (uint8_t)(0xFF ^ s);
  return (uint8_t)(0xFF - s);
}

static void sendMove(uint8_t servoId, int deg, uint16_t moveTimeMs, ChecksumMode chkMode) {
  const uint16_t posTicks = degToTicks(deg);
  uint8_t pkt[11];

  pkt[0] = 0xFF;
  pkt[1] = 0xFF;
  pkt[2] = servoId;
  pkt[3] = 0x07;
  pkt[4] = 0x03;
  pkt[5] = 0x2A;
  pkt[6] = (uint8_t)((posTicks >> 8) & 0xFF);
  pkt[7] = (uint8_t)(posTicks & 0xFF);
  pkt[8] = (uint8_t)((moveTimeMs >> 8) & 0xFF);
  pkt[9] = (uint8_t)(moveTimeMs & 0xFF);
  pkt[10] = calcChecksum(pkt, 2, 9, chkMode);

  servoSerial.write(pkt, sizeof(pkt));
  servoSerial.flush();
}

static void moveBoth(int panDeg, int tiltDeg, uint16_t moveTimeMs, ChecksumMode chkMode) {
  sendMove(SERVO_ID_PAN, panDeg, moveTimeMs, chkMode);
  delay(5);
  sendMove(SERVO_ID_TILT, tiltDeg, moveTimeMs, chkMode);

  Serial.print("MOVE pan=");
  Serial.print(panDeg);
  Serial.print(" tilt=");
  Serial.print(tiltDeg);
  Serial.print(" time=");
  Serial.print(moveTimeMs);
  Serial.print(" chk=");
  Serial.println((chkMode == CHK_SUB) ? "SUB" : "XOR");
}

static void runPhase(uint32_t baud, ChecksumMode chkMode) {
  Serial.println();
  Serial.println("========================================");
  Serial.print("PHASE baud=");
  Serial.print(baud);
  Serial.print(" checksum=");
  Serial.println((chkMode == CHK_SUB) ? "SUB" : "XOR");
  Serial.println("========================================");

  servoSerial.begin(baud, SERIAL_8N1, PIN_SERVO_RX, PIN_SERVO_TX);
  delay(100);

  const uint32_t phaseStart = millis();
  while ((millis() - phaseStart) < PHASE_HOLD_MS) {
    moveBoth(135, 135, 500, chkMode);
    delay(900);
    moveBoth(35, 35, MOVE_TIME_MS, chkMode);
    delay(1100);
    moveBoth(235, 235, MOVE_TIME_MS, chkMode);
    delay(1100);
    moveBoth(60, 210, MOVE_TIME_MS, chkMode);
    delay(1100);
    moveBoth(210, 60, MOVE_TIME_MS, chkMode);
    delay(1100);
  }

  servoSerial.end();
  delay(150);
}

void setup() {
  Serial.begin(HOST_BAUD);
  delay(400);

  Serial.println("ESP32 Waveshare serial-bus AUTO-PROBE test");
  Serial.println("USB: ESP32 Type-C only");
  Serial.println("Servo power: external supply required");
  Serial.println("Switch: set UART control to ESP32 path");
}

void loop() {
  for (size_t i = 0; i < BAUD_COUNT; i++) {
    runPhase(BAUD_OPTIONS[i], CHK_SUB);
    runPhase(BAUD_OPTIONS[i], CHK_XOR);
  }
}