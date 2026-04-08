// Smart Sentry v3.0 Nano ID4 Accessory Listener
// Phase 1 bench scaffold: passively listens for Yahboom-style packets addressed
// to ID 4 and drives trigger and accessory outputs locally.

#include <Arduino.h>
#include <SoftwareSerial.h>
#include <Servo.h>

static const uint32_t HOST_BAUD = 115200;
static const uint32_t BUS_BAUD = 115200;

static const int PIN_BUS_RX = 10;
static const int PIN_BUS_TX_UNUSED = 11;

static const uint8_t DEVICE_ID = 4;
static const uint8_t REG_ACCESSORY_FLAGS = 0x40;
static const uint8_t REG_TRIGGER_CONFIG = 0x41;
static const uint8_t REG_HEARTBEAT = 0x42;

static const int PIN_TRIGGER_SERVO = 9;
static const int PIN_TRIGGER_MOSFET = 3;
static const int PIN_LED_RELAY = 4;
static const int PIN_LASER_RELAY = 5;
static const int PIN_ACC_RELAY = 6;
static const int PIN_SPARE_RELAY = 7;

static const uint8_t RX_MAX = 16;

Servo triggerServo;
SoftwareSerial busSerial(PIN_BUS_RX, PIN_BUS_TX_UNUSED);

static uint8_t rxBuf[RX_MAX];
static uint8_t rxIndex = 0;
static uint8_t headerState = 0;

static bool safetyArmed = false;
static bool projectileMode = false;
static bool ledOn = false;
static bool laserOn = false;
static bool accOn = false;
static bool spareOn = false;
static bool fireRequest = false;

static uint8_t triggerRestDeg = 0;
static uint8_t triggerFireDeg = 45;
static uint16_t triggerPulseMs = 120;
static bool triggerPulseActive = false;
static uint32_t triggerPulseStartMs = 0;
static uint8_t lastSequence = 0;

static uint8_t inverseSum(const uint8_t *data, size_t count) {
  uint8_t sum = 0;
  for (size_t i = 0; i < count; ++i) sum = (uint8_t)(sum + data[i]);
  return (uint8_t)(~sum);
}

static void applyOutputs() {
  digitalWrite(PIN_LED_RELAY, ledOn ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY, laserOn ? HIGH : LOW);
  digitalWrite(PIN_ACC_RELAY, accOn ? HIGH : LOW);
  digitalWrite(PIN_SPARE_RELAY, spareOn ? HIGH : LOW);

  if (!safetyArmed) {
    digitalWrite(PIN_TRIGGER_MOSFET, LOW);
    triggerServo.write(triggerRestDeg);
    triggerPulseActive = false;
    fireRequest = false;
    return;
  }

  if (!projectileMode) {
    digitalWrite(PIN_TRIGGER_MOSFET, fireRequest ? HIGH : LOW);
    triggerServo.write(triggerRestDeg);
    triggerPulseActive = false;
    return;
  }

  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  if (fireRequest && !triggerPulseActive) {
    triggerPulseActive = true;
    triggerPulseStartMs = millis();
    triggerServo.write(triggerFireDeg);
  }

  if (triggerPulseActive && (millis() - triggerPulseStartMs) >= triggerPulseMs) {
    triggerServo.write(triggerRestDeg);
    triggerPulseActive = false;
    fireRequest = false;
  }
}

static void decodeAccessoryFlags(uint8_t flags) {
  fireRequest = (flags & (1 << 0)) != 0;
  safetyArmed = (flags & (1 << 1)) != 0;
  projectileMode = (flags & (1 << 2)) != 0;
  ledOn = (flags & (1 << 3)) != 0;
  laserOn = (flags & (1 << 4)) != 0;
  accOn = (flags & (1 << 5)) != 0;
  spareOn = (flags & (1 << 6)) != 0;

  Serial.print("ACK flags=");
  Serial.println(flags, HEX);
}

static void handleRegisterWrite(const uint8_t *packet, uint8_t declaredLen) {
  uint8_t reg = packet[5];
  const uint8_t *data = &packet[6];
  uint8_t dataLen = declaredLen >= 4 ? (uint8_t)(declaredLen - 3) : 0;

  if (reg == REG_ACCESSORY_FLAGS && dataLen >= 1) {
    decodeAccessoryFlags(data[0]);
  } else if (reg == REG_TRIGGER_CONFIG && dataLen >= 3) {
    triggerRestDeg = data[0];
    triggerFireDeg = data[1];
    triggerPulseMs = (uint16_t)data[2] * 10U;
    Serial.print("ACK trig rest=");
    Serial.print(triggerRestDeg);
    Serial.print(" fire=");
    Serial.print(triggerFireDeg);
    Serial.print(" pulse=");
    Serial.println(triggerPulseMs);
  } else if (reg == REG_HEARTBEAT && dataLen >= 1) {
    lastSequence = data[0];
    Serial.print("ACK seq=");
    Serial.println(lastSequence);
  }
}

static void parseBusByte(uint8_t value) {
  if (headerState == 0) {
    if (value == 0xFF) headerState = 1;
    return;
  }
  if (headerState == 1) {
    if (value == 0xFF) {
      headerState = 2;
      rxIndex = 0;
    } else {
      headerState = 0;
    }
    return;
  }

  if (rxIndex < RX_MAX) rxBuf[rxIndex++] = value;
  if (rxIndex < 2) return;

  uint8_t declaredLen = rxBuf[1];
  uint8_t expectedBytes = (uint8_t)(declaredLen + 2);
  if (expectedBytes > RX_MAX) {
    headerState = 0;
    rxIndex = 0;
    return;
  }
  if (rxIndex < expectedBytes) return;

  headerState = 0;

  if (rxBuf[0] != DEVICE_ID) {
    rxIndex = 0;
    return;
  }

  uint8_t checksum = inverseSum(rxBuf, (size_t)(expectedBytes - 1));
  if (checksum != rxBuf[expectedBytes - 1]) {
    Serial.println("WARN checksum");
    rxIndex = 0;
    return;
  }

  if (expectedBytes >= 6 && rxBuf[2] == 0x03) {
    handleRegisterWrite(rxBuf - 0, declaredLen);
  }
  rxIndex = 0;
}

void setup() {
  Serial.begin(HOST_BAUD);
  busSerial.begin(BUS_BAUD);

  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  pinMode(PIN_LED_RELAY, OUTPUT);
  pinMode(PIN_LASER_RELAY, OUTPUT);
  pinMode(PIN_ACC_RELAY, OUTPUT);
  pinMode(PIN_SPARE_RELAY, OUTPUT);

  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  digitalWrite(PIN_LED_RELAY, LOW);
  digitalWrite(PIN_LASER_RELAY, LOW);
  digitalWrite(PIN_ACC_RELAY, LOW);
  digitalWrite(PIN_SPARE_RELAY, LOW);

  triggerServo.attach(PIN_TRIGGER_SERVO);
  triggerServo.write(triggerRestDeg);

  Serial.print("[BOOT] Smart Sentry v3 Nano ID4 listener ready on RX pin ");
  Serial.println(PIN_BUS_RX);
}

void loop() {
  while (busSerial.available() > 0) {
    parseBusByte((uint8_t)busSerial.read());
  }

  applyOutputs();
}