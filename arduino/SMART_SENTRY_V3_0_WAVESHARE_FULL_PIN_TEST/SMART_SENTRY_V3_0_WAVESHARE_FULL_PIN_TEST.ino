#include <Arduino.h>

enum BusChecksumMode {
  BUS_CHK_SUB = 0,
  BUS_CHK_XOR = 1,
};

static const uint32_t SERIAL_BAUD = 115200;
static const uint32_t BUS_BAUD = 1000000;

static const int PIN_BUS_UART_RX = 18;
static const int PIN_BUS_UART_TX = 19;
static const int PIN_BUZZER = 4;
static const int PIN_TRIGGER_MOSFET = 27;
static const int PIN_ACC_RELAY = 25;
static const int PIN_SPARE_RELAY = 26;
static const int PIN_SWITCH_INPUT = 21;
static const int PIN_SPEAKER_RESERVED = 5;
static const int PIN_PROVISIONAL_GPIO13 = 13;
static const int PIN_PROVISIONAL_GPIO19 = 19;
static const int PIN_OPTIONAL_TRIGGER_PWM = 16;

static const int HEADER_BUZZER = 7;
static const int HEADER_UART_TX_RESERVED = 8;
static const int HEADER_UART_RX_RESERVED = 10;
static const int HEADER_TRIGGER_MOSFET = 13;
static const int HEADER_ACC_RELAY = 22;
static const int HEADER_SPEAKER_RESERVED = 29;
static const int HEADER_PROVISIONAL_GPIO13 = 33;
static const int HEADER_PROVISIONAL_GPIO19 = 35;
static const int HEADER_OPTIONAL_TRIGGER_PWM = 36;
static const int HEADER_SPARE_RELAY = 37;
static const int HEADER_SWITCH_INPUT = 40;

static const int PAN_MIN_DEG = 0;
static const int PAN_MAX_DEG = 220;
static const int TILT_MIN_DEG = 0;
static const int TILT_MAX_DEG = 70;
static const int PAN_CENTER_DEG = 90;
static const int TILT_CENTER_DEG = 35;
static const uint8_t BUS_ID_PAN = 1;
static const uint8_t BUS_ID_TILT = 2;
static const uint8_t REG_GOAL_POSITION = 0x2A;
static const int BUZZER_PWM_RES_BITS = 10;

HardwareSerial busSerial(2);

struct DigitalTestPin {
  char command;
  const char *description;
  int gpio;
  int headerPin;
  const char *notes;
};

static const DigitalTestPin DIGITAL_TESTS[] = {
  {'1', "Trigger MOSFET output", PIN_TRIGGER_MOSFET, HEADER_TRIGGER_MOSFET, "Use LED+resistor only if the real trigger load is disconnected."},
  {'2', "Accessory relay output", PIN_ACC_RELAY, HEADER_ACC_RELAY, "Use a simple LED test or relay-module input, not a bare load."},
  {'3', "Spare relay output", PIN_SPARE_RELAY, HEADER_SPARE_RELAY, "Use a simple LED test or relay-module input, not a bare load."},
  {'4', "Speaker reserved pin", PIN_SPEAKER_RESERVED, HEADER_SPEAKER_RESERVED, "Reserved path. LED-only screening; do not attach active speaker hardware."},
  {'5', "Provisional candidate A", PIN_PROVISIONAL_GPIO13, HEADER_PROVISIONAL_GPIO13, "Simple LED-only screening candidate for future LED or accessory output."},
  {'6', "Provisional candidate B", PIN_PROVISIONAL_GPIO19, HEADER_PROVISIONAL_GPIO19, "Simple LED-only screening candidate for future LED or accessory output."},
};

static bool autoTestDone = false;
static bool buzzerPwmReady = false;

static int clampInt(int value, int lo, int hi) {
  if (value < lo) return lo;
  if (value > hi) return hi;
  return value;
}

static uint16_t mapDegreesToTicks(int deg, int minDeg, int maxDeg) {
  int clamped = clampInt(deg, minDeg, maxDeg);
  long spanDeg = (long)(maxDeg - minDeg);
  if (spanDeg <= 0) return 0;
  long shifted = (long)(clamped - minDeg);
  return (uint16_t)((shifted * 4095L) / spanDeg);
}

static uint8_t busChecksum(const uint8_t *data, size_t count, BusChecksumMode mode) {
  uint8_t sum = 0;
  for (size_t i = 0; i < count; ++i) {
    sum = (uint8_t)(sum + data[i]);
  }
  if (mode == BUS_CHK_XOR) return (uint8_t)(0xFF ^ sum);
  return (uint8_t)(~sum);
}

static void busFlushRx() {
  while (busSerial.available() > 0) {
    (void)busSerial.read();
  }
}

static void buildBusPingPacket(uint8_t servoId, BusChecksumMode mode, uint8_t *packetOut) {
  packetOut[0] = 0xFF;
  packetOut[1] = 0xFF;
  packetOut[2] = servoId;
  packetOut[3] = 0x02;
  packetOut[4] = 0x01;
  packetOut[5] = busChecksum(&packetOut[2], 3, mode);
}

static size_t busReadBytes(uint8_t *buffer, size_t maxLen, uint32_t timeoutMs) {
  size_t count = 0;
  uint32_t start = millis();
  while ((millis() - start) < timeoutMs && count < maxLen) {
    while (busSerial.available() > 0 && count < maxLen) {
      buffer[count++] = (uint8_t)busSerial.read();
    }
    if (count > 0 && busSerial.available() <= 0) {
      delay(1);
    }
  }
  return count;
}

static bool busFindValidPacket(const uint8_t *data, size_t count, uint8_t servoId, BusChecksumMode mode) {
  if (data == nullptr || count < 6) return false;
  for (size_t i = 0; i + 5 < count; ++i) {
    bool headerOk = false;
    if (data[i] == 0xFF && data[i + 1] == 0xFF) headerOk = true;
    if (data[i] == 0xFF && data[i + 1] == 0xF5) headerOk = true;
    if (!headerOk) continue;
    if (data[i + 2] != servoId) continue;
    uint8_t declaredLen = data[i + 3];
    if (declaredLen < 2) continue;
    size_t totalLen = (size_t)declaredLen + 4;
    if (i + totalLen > count) continue;
    uint8_t expectedChecksum = busChecksum(&data[i + 2], totalLen - 3, mode);
    if (expectedChecksum != data[i + totalLen - 1]) continue;
    if (data[i + 4] != 0x00) continue;
    return true;
  }
  return false;
}

static bool busTryPing(uint8_t servoId, BusChecksumMode mode, uint32_t timeoutMs) {
  uint8_t packet[6];
  buildBusPingPacket(servoId, mode, packet);
  busFlushRx();
  busSerial.write(packet, sizeof(packet));
  uint8_t rx[64];
  size_t received = busReadBytes(rx, sizeof(rx), timeoutMs);
  bool ok = busFindValidPacket(rx, received, servoId, mode);
  Serial.printf("[BUSPING] id=%u mode=%s rx=%u -> %s\n",
                servoId,
                mode == BUS_CHK_XOR ? "xor" : "sub",
                (unsigned)received,
                ok ? "OK" : "FAIL");
  return ok;
}

static void sendBusMotionPacket(uint8_t servoId, int deg, uint16_t moveTimeMs, int minDeg, int maxDeg) {
  uint16_t pos = mapDegreesToTicks(deg, minDeg, maxDeg);
  uint8_t payload[9];
  payload[0] = servoId;
  payload[1] = 0x07;
  payload[2] = 0x03;
  payload[3] = REG_GOAL_POSITION;
  payload[4] = (uint8_t)(pos & 0xFF);
  payload[5] = (uint8_t)((pos >> 8) & 0xFF);
  payload[6] = (uint8_t)(moveTimeMs & 0xFF);
  payload[7] = (uint8_t)((moveTimeMs >> 8) & 0xFF);
  payload[8] = busChecksum(payload, 8, BUS_CHK_SUB);

  busSerial.write(0xFF);
  busSerial.write(0xFF);
  busSerial.write(payload, sizeof(payload));

  Serial.printf("[BUS] motion id=%u deg=%d ticks=%u time=%u\n",
                servoId,
                deg,
                pos,
                moveTimeMs);
}

static bool ensureBuzzerPwmReady() {
  if (buzzerPwmReady) return true;
  buzzerPwmReady = ledcAttach(PIN_BUZZER, 2000, BUZZER_PWM_RES_BITS);
  if (!buzzerPwmReady) {
    Serial.println("[BUZZER] PWM init failed");
    return false;
  }
  ledcWrite(PIN_BUZZER, 0);
  return true;
}

static void allOutputsOff() {
  for (size_t i = 0; i < (sizeof(DIGITAL_TESTS) / sizeof(DIGITAL_TESTS[0])); ++i) {
    digitalWrite(DIGITAL_TESTS[i].gpio, LOW);
  }
  if (buzzerPwmReady) {
    ledcWrite(PIN_BUZZER, 0);
  }
}

static void printHeaderLine() {
  Serial.println();
  Serial.println("============================================================");
  Serial.println("SMART SENTRY V3 WAVESHARE FULL PIN TEST");
  Serial.println("============================================================");
}

static void printPinSummary() {
  printHeaderLine();
  Serial.println("Confirmed active tests:");
  Serial.printf("  Bus servo mount RX/TX: GPIO%d/GPIO%d -> tested through pan/tilt bus ping and motion\n", PIN_BUS_UART_RX, PIN_BUS_UART_TX);
  Serial.printf("  Header %d | GPIO%d | Buzzer output\n", HEADER_BUZZER, PIN_BUZZER);
  Serial.printf("  Header %d | GPIO%d | Trigger MOSFET output\n", HEADER_TRIGGER_MOSFET, PIN_TRIGGER_MOSFET);
  Serial.printf("  Header %d | GPIO%d | Accessory relay output\n", HEADER_ACC_RELAY, PIN_ACC_RELAY);
  Serial.printf("  Header %d | GPIO%d | Spare relay output\n", HEADER_SPARE_RELAY, PIN_SPARE_RELAY);
  Serial.printf("  Header %d | GPIO%d | Switch input\n", HEADER_SWITCH_INPUT, PIN_SWITCH_INPUT);
  Serial.println();
  Serial.println("Reserved or screening-only tests:");
  Serial.printf("  Header %d | GPIO%d | Speaker reserved pin -> LED-only screening\n", HEADER_SPEAKER_RESERVED, PIN_SPEAKER_RESERVED);
  Serial.printf("  Header %d | GPIO%d | Provisional candidate A -> LED-only screening\n", HEADER_PROVISIONAL_GPIO13, PIN_PROVISIONAL_GPIO13);
  Serial.printf("  Header %d | GPIO%d | Provisional candidate B -> LED-only screening\n", HEADER_PROVISIONAL_GPIO19, PIN_PROVISIONAL_GPIO19);
  Serial.printf("  Header %d | GPIO%d | UART TX reserved -> skipped\n", HEADER_UART_TX_RESERVED, 14);
  Serial.printf("  Header %d | GPIO%d | UART RX reserved -> skipped\n", HEADER_UART_RX_RESERVED, 15);
  Serial.println();
  Serial.println("Optional only, not auto-run:");
  Serial.printf("  Header %d | GPIO%d | Trigger-servo PWM candidate -> only test if bus servos are disconnected\n", HEADER_OPTIONAL_TRIGGER_PWM, PIN_OPTIONAL_TRIGGER_PWM);
  Serial.println();
  Serial.println("For LED tests: use an LED with a resistor or a protected LED module to GND.");
  Serial.println("Do not attach bare loads directly to a GPIO pin.");
  Serial.println();
}

static void printMenu() {
  Serial.println("Serial commands:");
  Serial.println("  a = run full automatic test sequence");
  Serial.println("  b = bus ping + pan/tilt sweep");
  Serial.println("  z = buzzer tone test");
  Serial.println("  1 = trigger MOSFET output test");
  Serial.println("  2 = accessory relay output test");
  Serial.println("  3 = spare relay output test");
  Serial.println("  4 = speaker reserved pin LED test");
  Serial.println("  5 = provisional candidate A LED test");
  Serial.println("  6 = provisional candidate B LED test");
  Serial.println("  s = monitor switch input for 10 seconds");
  Serial.println("  p = optional trigger-servo PWM candidate test on GPIO16/header36");
  Serial.println("  m = print menu again");
  Serial.println();
}

static void runBuzzerTest() {
  Serial.printf("[TEST] Buzzer output | Header %d | GPIO%d\n", HEADER_BUZZER, PIN_BUZZER);
  if (!ensureBuzzerPwmReady()) return;

  Serial.println("[TEST] Playing 1200 Hz for 300 ms");
  ledcWriteTone(PIN_BUZZER, 1200);
  delay(300);
  ledcWrite(PIN_BUZZER, 0);
  delay(150);

  Serial.println("[TEST] Playing 1800 Hz for 300 ms");
  ledcWriteTone(PIN_BUZZER, 1800);
  delay(300);
  ledcWrite(PIN_BUZZER, 0);
  delay(150);

  Serial.println("[TEST] Playing 2400 Hz for 300 ms");
  ledcWriteTone(PIN_BUZZER, 2400);
  delay(300);
  ledcWrite(PIN_BUZZER, 0);
  Serial.println("[TEST] Buzzer test complete");
  Serial.println();
}

static void runDigitalBlinkTest(const DigitalTestPin &testPin, int cycles, int onMs, int offMs) {
  Serial.printf("[TEST] %s | Header %d | GPIO%d\n", testPin.description, testPin.headerPin, testPin.gpio);
  Serial.printf("[TEST] Note: %s\n", testPin.notes);

  for (int i = 0; i < cycles; ++i) {
    Serial.printf("[TEST] Cycle %d/%d -> ON\n", i + 1, cycles);
    digitalWrite(testPin.gpio, HIGH);
    delay(onMs);
    Serial.printf("[TEST] Cycle %d/%d -> OFF\n", i + 1, cycles);
    digitalWrite(testPin.gpio, LOW);
    delay(offMs);
  }

  digitalWrite(testPin.gpio, LOW);
  Serial.printf("[TEST] %s complete\n", testPin.description);
  Serial.println();
}

static void runSwitchMonitor(uint32_t durationMs) {
  Serial.printf("[TEST] Switch input | Header %d | GPIO%d\n", HEADER_SWITCH_INPUT, PIN_SWITCH_INPUT);
  Serial.println("[TEST] Open switch should read HIGH/1. Closed to GND should read LOW/0.");
  uint32_t start = millis();
  int lastState = digitalRead(PIN_SWITCH_INPUT);
  Serial.printf("[TEST] Initial state = %d\n", lastState == LOW ? 0 : 1);
  while ((millis() - start) < durationMs) {
    int state = digitalRead(PIN_SWITCH_INPUT);
    if (state != lastState) {
      lastState = state;
      Serial.printf("[TEST] Switch changed -> %d\n", lastState == LOW ? 0 : 1);
    }
    delay(50);
  }
  Serial.println("[TEST] Switch monitor complete");
  Serial.println();
}

static void runBusTestSequence() {
  Serial.println("[TEST] Bus servo path using the bus servo mount on GPIO16/GPIO17");
  Serial.println("[TEST] Make sure pan and tilt servos are connected to the serial bus mount.");
  bool panSub = busTryPing(BUS_ID_PAN, BUS_CHK_SUB, 60);
  bool panXor = busTryPing(BUS_ID_PAN, BUS_CHK_XOR, 60);
  bool tiltSub = busTryPing(BUS_ID_TILT, BUS_CHK_SUB, 60);
  bool tiltXor = busTryPing(BUS_ID_TILT, BUS_CHK_XOR, 60);
  Serial.printf("[TEST] Pan ping ok = %s\n", (panSub || panXor) ? "YES" : "NO");
  Serial.printf("[TEST] Tilt ping ok = %s\n", (tiltSub || tiltXor) ? "YES" : "NO");
  Serial.println();

  Serial.println("[TEST] Pan sweep -> center, left, right, center");
  sendBusMotionPacket(BUS_ID_PAN, PAN_CENTER_DEG, 300, PAN_MIN_DEG, PAN_MAX_DEG);
  delay(700);
  sendBusMotionPacket(BUS_ID_PAN, 20, 350, PAN_MIN_DEG, PAN_MAX_DEG);
  delay(900);
  sendBusMotionPacket(BUS_ID_PAN, 160, 350, PAN_MIN_DEG, PAN_MAX_DEG);
  delay(900);
  sendBusMotionPacket(BUS_ID_PAN, PAN_CENTER_DEG, 300, PAN_MIN_DEG, PAN_MAX_DEG);
  delay(700);
  Serial.println();

  Serial.println("[TEST] Tilt sweep -> center, low, high, center");
  sendBusMotionPacket(BUS_ID_TILT, TILT_CENTER_DEG, 300, TILT_MIN_DEG, TILT_MAX_DEG);
  delay(700);
  sendBusMotionPacket(BUS_ID_TILT, 10, 350, TILT_MIN_DEG, TILT_MAX_DEG);
  delay(900);
  sendBusMotionPacket(BUS_ID_TILT, 55, 350, TILT_MIN_DEG, TILT_MAX_DEG);
  delay(900);
  sendBusMotionPacket(BUS_ID_TILT, TILT_CENTER_DEG, 300, TILT_MIN_DEG, TILT_MAX_DEG);
  delay(700);

  Serial.println("[TEST] Bus servo sequence complete");
  Serial.println();
}

static uint32_t servoPulseDutyTicks(float pulseUs) {
  const float pwmPeriodUs = 20000.0f;
  const uint32_t maxDuty = (1UL << 16) - 1UL;
  float ratio = pulseUs / pwmPeriodUs;
  if (ratio < 0.0f) ratio = 0.0f;
  if (ratio > 1.0f) ratio = 1.0f;
  return (uint32_t)(ratio * (float)maxDuty);
}

static void runOptionalTriggerServoPwmTest() {
  Serial.println("[TEST] OPTIONAL trigger-servo PWM candidate");
  Serial.printf("[TEST] Header %d | GPIO%d\n", HEADER_OPTIONAL_TRIGGER_PWM, PIN_OPTIONAL_TRIGGER_PWM);
  Serial.println("[TEST] WARNING: This reuses the bus UART RX pin. Disconnect pan/tilt servos first.");

  busSerial.end();
  delay(50);
  bool pwmReady = ledcAttach(PIN_OPTIONAL_TRIGGER_PWM, 50, 16);
  if (!pwmReady) {
    Serial.println("[TEST] PWM attach failed on GPIO16");
    busSerial.begin(BUS_BAUD, SERIAL_8N1, PIN_BUS_UART_RX, PIN_BUS_UART_TX);
    return;
  }

  Serial.println("[TEST] Sending 1.0 ms pulse for 2 seconds");
  ledcWrite(PIN_OPTIONAL_TRIGGER_PWM, servoPulseDutyTicks(1000.0f));
  delay(2000);
  Serial.println("[TEST] Sending 1.5 ms pulse for 2 seconds");
  ledcWrite(PIN_OPTIONAL_TRIGGER_PWM, servoPulseDutyTicks(1500.0f));
  delay(2000);
  Serial.println("[TEST] Sending 2.0 ms pulse for 2 seconds");
  ledcWrite(PIN_OPTIONAL_TRIGGER_PWM, servoPulseDutyTicks(2000.0f));
  delay(2000);
  ledcWrite(PIN_OPTIONAL_TRIGGER_PWM, 0);
  pinMode(PIN_OPTIONAL_TRIGGER_PWM, INPUT);
  busSerial.begin(BUS_BAUD, SERIAL_8N1, PIN_BUS_UART_RX, PIN_BUS_UART_TX);
  Serial.println("[TEST] Optional trigger-servo PWM test complete");
  Serial.println();
}

static void runFullAutoTest() {
  printHeaderLine();
  Serial.println("[AUTO] Starting full automatic test sequence");
  Serial.println();

  runBusTestSequence();
  runBuzzerTest();
  for (size_t i = 0; i < (sizeof(DIGITAL_TESTS) / sizeof(DIGITAL_TESTS[0])); ++i) {
    runDigitalBlinkTest(DIGITAL_TESTS[i], 3, 500, 300);
  }
  runSwitchMonitor(10000);

  Serial.println("[AUTO] Full automatic test sequence complete");
  Serial.println();
  printMenu();
}

static void handleSerialCommand(char command) {
  switch (command) {
    case 'a':
    case 'A':
      runFullAutoTest();
      break;
    case 'b':
    case 'B':
      runBusTestSequence();
      break;
    case 'z':
    case 'Z':
      runBuzzerTest();
      break;
    case '1':
    case '2':
    case '3':
    case '4':
    case '5':
    case '6':
      for (size_t i = 0; i < (sizeof(DIGITAL_TESTS) / sizeof(DIGITAL_TESTS[0])); ++i) {
        if (DIGITAL_TESTS[i].command == command) {
          runDigitalBlinkTest(DIGITAL_TESTS[i], 3, 500, 300);
          break;
        }
      }
      break;
    case 's':
    case 'S':
      runSwitchMonitor(10000);
      break;
    case 'p':
    case 'P':
      runOptionalTriggerServoPwmTest();
      break;
    case 'm':
    case 'M':
      printMenu();
      break;
    default:
      if (command != '\r' && command != '\n' && command != ' ') {
        Serial.printf("[INFO] Unknown command '%c'\n", command);
        printMenu();
      }
      break;
  }
}

void setup() {
  Serial.begin(SERIAL_BAUD);
  delay(1200);

  pinMode(PIN_SWITCH_INPUT, INPUT_PULLUP);
  for (size_t i = 0; i < (sizeof(DIGITAL_TESTS) / sizeof(DIGITAL_TESTS[0])); ++i) {
    pinMode(DIGITAL_TESTS[i].gpio, OUTPUT);
    digitalWrite(DIGITAL_TESTS[i].gpio, LOW);
  }
  pinMode(PIN_BUZZER, OUTPUT);
  digitalWrite(PIN_BUZZER, LOW);

  busSerial.begin(BUS_BAUD, SERIAL_8N1, PIN_BUS_UART_RX, PIN_BUS_UART_TX);

  printPinSummary();
  printMenu();
}

void loop() {
  if (!autoTestDone && millis() > 1500) {
    autoTestDone = true;
    runFullAutoTest();
  }

  while (Serial.available() > 0) {
    char command = (char)Serial.read();
    handleSerialCommand(command);
  }

  delay(5);
}