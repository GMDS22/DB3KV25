/*
  DB3000 ESP32-CAM Serial Bus Servo Firmware (No Camera)
  ------------------------------------------------------
  Recommended board: ESP32-CAM (AI-Thinker).
  Host serial (USB): UART0 @ 115200
  Debug board serial: UART2 @ 115200

  Wiring (full-duplex UART):
    ESP32 GPIO14 (TX2) -> Debug board RX
    ESP32 GPIO13 (RX2) <- Debug board TX
    GND <-> GND

  Note: ESP32-CAM uses 3.3V IO. If debug board expects 5V, use level shifting.
*/

#include <Arduino.h>

// ---------------------------
// Serial configuration
// ---------------------------
static const uint32_t HOST_BAUD = 115200;
static const uint32_t BUS_BAUD  = 115200;

static const int PIN_BUS_RX = 13; // UART2 RX
static const int PIN_BUS_TX = 14; // UART2 TX

HardwareSerial busSerial(2);

// ---------------------------
// Pin mapping (adjust if needed)
// ---------------------------
static const uint8_t PIN_TRIGGER_MOSFET = 12;
static const uint8_t PIN_TRIGGER_SERVO  = 4;  // ESP32-CAM flash LED pin; change if you have a dedicated servo pin
static const uint8_t PIN_LED_RELAY      = 15;
static const uint8_t PIN_LASER_RELAY    = 2;

// ---------------------------
// Servo settings (PWM via LEDC)
// ---------------------------
static const int SERVO_CH = 0;
static const int SERVO_HZ = 50;
static const int SERVO_BITS = 16;
static const int TRIG_SERVO_REST_DEG = 20;
static const int TRIG_SERVO_FIRE_DEG = 70;
static const uint16_t TRIG_PULSE_MS  = 90;
static const uint16_t TRIG_COOLDOWN_MS = 120;

// ---------------------------
// Serial bus servo config
// ---------------------------
static const uint8_t BUS_ID_PAN  = 1;
static const uint8_t BUS_ID_TILT = 2;

static const int PAN_MIN_DEG  = 0;
static const int PAN_MAX_DEG  = 220;
static const int TILT_MIN_DEG = 0;
static const int TILT_MAX_DEG = 70;

static const uint16_t PAN_TICKS_MIN  = 0;
static const uint16_t PAN_TICKS_MAX  = 4095;
static const uint16_t TILT_TICKS_MIN = 0;
static const uint16_t TILT_TICKS_MAX = 4095;

static const bool INVERT_PAN  = false;
static const bool INVERT_TILT = false;

static const uint16_t DEFAULT_MOVE_TIME_MS = 60;

// ---------------------------
// Host command state
// ---------------------------
struct HostCommand {
  int panDeg = 90;
  int tiltDeg = 40;
  int fire = 0;   // F
  int led = 0;    // L
  int laser = 0;  // R
  int acc = 0;    // G
  int safety = 1; // S (1=safe)
  int mode = 0;   // M (1=BB servo)
};

static HostCommand cmd;
static bool enablePanTiltOutput = true;
static int lastFireToken = 0;
static uint32_t lastFireMs = 0;

// ---------------------------
// Helpers
// ---------------------------
static inline int clampInt(int v, int lo, int hi) {
  if (v < lo) return lo;
  if (v > hi) return hi;
  return v;
}

static inline int applyInvertAndClamp(int deg, int minDeg, int maxDeg, bool invert) {
  deg = clampInt(deg, minDeg, maxDeg);
  if (!invert) return deg;
  const int span = maxDeg - minDeg;
  const int rel = deg - minDeg;
  return minDeg + (span - rel);
}

static inline uint16_t mapDegToTicks(int deg, int minDeg, int maxDeg, uint16_t ticksMin, uint16_t ticksMax) {
  deg = clampInt(deg, minDeg, maxDeg);
  const int degSpan = maxDeg - minDeg;
  if (degSpan <= 0) return ticksMin;

  const long ticksSpan = (long)ticksMax - (long)ticksMin;
  const long relDeg = (long)(deg - minDeg);
  long ticks = (long)ticksMin + (relDeg * ticksSpan) / (long)degSpan;

  const long lo = (ticksMin < ticksMax) ? ticksMin : ticksMax;
  const long hi = (ticksMin < ticksMax) ? ticksMax : ticksMin;
  if (ticks < lo) ticks = lo;
  if (ticks > hi) ticks = hi;
  return (uint16_t)ticks;
}

static inline uint8_t checksum_ff_minus_sum(const uint8_t *pkt, uint8_t startIdx, uint8_t endIdxInclusive) {
  uint16_t sum = 0;
  for (uint8_t i = startIdx; i <= endIdxInclusive; i++) {
    sum += pkt[i];
  }
  return (uint8_t)(0xFF - (sum & 0xFF));
}

static inline void busWrite(const uint8_t *data, size_t len) {
  busSerial.write(data, len);
  busSerial.flush();
}

// ---------------------------
// Servo PWM (LEDC)
// ---------------------------
static inline uint32_t pulseToDutyUs(uint32_t pulseUs) {
  // duty = pulseUs / periodUs * 2^bits
  const uint32_t periodUs = 1000000UL / SERVO_HZ;
  const uint32_t maxDuty = (1UL << SERVO_BITS) - 1;
  return (pulseUs * maxDuty) / periodUs;
}

static void servoWriteDeg(int deg) {
  deg = clampInt(deg, 0, 180);
  const uint32_t pulseUs = 500 + (uint32_t)deg * 2000UL / 180UL; // 500..2500us
  ledcWrite(SERVO_CH, pulseToDutyUs(pulseUs));
}

// ---------------------------
// Serial-bus servo protocol (Yahboom/DS_v4)
// ---------------------------
static void setBusServoAngle(uint8_t id, int deg, uint16_t moveTimeMs) {
  uint16_t ticksMin = 0;
  uint16_t ticksMax = 4095;
  int minDeg = 0;
  int maxDeg = 270;

  if (id == BUS_ID_PAN) {
    ticksMin = PAN_TICKS_MIN;
    ticksMax = PAN_TICKS_MAX;
    minDeg = PAN_MIN_DEG;
    maxDeg = PAN_MAX_DEG;
  } else if (id == BUS_ID_TILT) {
    ticksMin = TILT_TICKS_MIN;
    ticksMax = TILT_TICKS_MAX;
    minDeg = TILT_MIN_DEG;
    maxDeg = TILT_MAX_DEG;
  }

  const uint16_t posTicks = mapDegToTicks(deg, minDeg, maxDeg, ticksMin, ticksMax);
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

static bool busPing(uint8_t id, uint16_t timeoutMs) {
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

  busWrite(pkt, sizeof(pkt));

  const uint32_t start = millis();
  uint8_t buf[32];
  uint8_t n = 0;
  while ((millis() - start) < timeoutMs && n < sizeof(buf)) {
    if (busSerial.available() > 0) {
      buf[n++] = (uint8_t)busSerial.read();
      if (n >= 3) {
        for (uint8_t i = 0; i + 2 < n; i++) {
          if (buf[i] == 0xFF && buf[i + 2] == id) {
            return true;
          }
        }
      }
    }
  }
  return false;
}

static void applyPanTilt() {
  const int pan = applyInvertAndClamp(cmd.panDeg, PAN_MIN_DEG, PAN_MAX_DEG, INVERT_PAN);
  const int tilt = applyInvertAndClamp(cmd.tiltDeg, TILT_MIN_DEG, TILT_MAX_DEG, INVERT_TILT);

  setBusServoAngle(BUS_ID_PAN, pan, DEFAULT_MOVE_TIME_MS);
  setBusServoAngle(BUS_ID_TILT, tilt, DEFAULT_MOVE_TIME_MS);
}

// ---------------------------
// Trigger handling
// ---------------------------
static bool isArmed() {
  return cmd.safety == 0;
}

static void setMosfet(bool on) {
  digitalWrite(PIN_TRIGGER_MOSFET, on ? HIGH : LOW);
}

static void pulseTriggerServo() {
  const uint32_t now = millis();
  if (now - lastFireMs < TRIG_COOLDOWN_MS) return;

  servoWriteDeg(TRIG_SERVO_FIRE_DEG);
  delay(TRIG_PULSE_MS);
  servoWriteDeg(TRIG_SERVO_REST_DEG);

  lastFireMs = now;
}

static void applyTrigger() {
  if (!isArmed()) {
    setMosfet(false);
    servoWriteDeg(TRIG_SERVO_REST_DEG);
    lastFireToken = cmd.fire;
    return;
  }

  if (cmd.mode == 0) {
    setMosfet(cmd.fire != 0);
  } else {
    const bool rising = (cmd.fire != 0) && (lastFireToken == 0);
    if (rising) {
      pulseTriggerServo();
    }
    setMosfet(false);
  }

  lastFireToken = cmd.fire;
}

static void applyAccessories() {
  digitalWrite(PIN_LED_RELAY, cmd.led ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY, cmd.laser ? HIGH : LOW);
}

// ---------------------------
// Host command parsing
// ---------------------------
static bool parsePackedCommand(const char *line, HostCommand &out) {
  auto findTok = [&](char tok, int &value) -> bool {
    const char *p = strchr(line, tok);
    if (!p) return false;
    p++;
    value = atoi(p);
    return true;
  };

  HostCommand c = out;

  (void)findTok('P', c.panDeg);
  (void)findTok('T', c.tiltDeg);
  bool ok = true;
  ok = findTok('F', c.fire) && ok;
  ok = findTok('L', c.led) && ok;
  ok = findTok('R', c.laser) && ok;
  findTok('G', c.acc);
  ok = findTok('S', c.safety) && ok;
  ok = findTok('M', c.mode) && ok;

  if (!ok) return false;

  c.panDeg = clampInt(c.panDeg, PAN_MIN_DEG, PAN_MAX_DEG);
  c.tiltDeg = clampInt(c.tiltDeg, TILT_MIN_DEG, TILT_MAX_DEG);
  c.fire = (c.fire != 0) ? 1 : 0;
  c.led = (c.led != 0) ? 1 : 0;
  c.laser = (c.laser != 0) ? 1 : 0;
  c.safety = (c.safety != 0) ? 1 : 0;
  c.mode = (c.mode != 0) ? 1 : 0;

  out = c;
  return true;
}

static bool readLineFromHost(char *buf, size_t bufLen) {
  static size_t idx = 0;

  while (Serial.available() > 0) {
    char ch = (char)Serial.read();
    if (ch == '\r') continue;

    if (ch == '\n') {
      buf[idx] = 0;
      idx = 0;
      return true;
    }

    if (idx + 1 < bufLen) {
      buf[idx++] = ch;
    } else {
      idx = 0;
    }
  }

  return false;
}

void setup() {
  Serial.begin(HOST_BAUD);
  busSerial.begin(BUS_BAUD, SERIAL_8N1, PIN_BUS_RX, PIN_BUS_TX);

  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  pinMode(PIN_LED_RELAY, OUTPUT);
  pinMode(PIN_LASER_RELAY, OUTPUT);

  setMosfet(false);
  digitalWrite(PIN_LED_RELAY, LOW);
  digitalWrite(PIN_LASER_RELAY, LOW);

  ledcSetup(SERVO_CH, SERVO_HZ, SERVO_BITS);
  ledcAttachPin(PIN_TRIGGER_SERVO, SERVO_CH);
  servoWriteDeg(TRIG_SERVO_REST_DEG);

  Serial.println(F("DB3000 ESP32-CAM SerialBus: READY"));
}

void loop() {
  static char line[96];

  if (readLineFromHost(line, sizeof(line))) {
    if (line[0] == 0) {
      // ignore empty
    } else {
      if (strncmp(line, "BUSPING", 7) == 0) {
        int id = 0;
        if (strlen(line) > 7) {
          id = atoi(line + 7);
        }

        if (id <= 0) {
          const bool ok1 = busPing(BUS_ID_PAN, 80);
          const bool ok2 = busPing(BUS_ID_TILT, 80);
          Serial.print(F("BUSPING PAN(id="));
          Serial.print(BUS_ID_PAN);
          Serial.print(F(")="));
          Serial.print(ok1 ? F("OK") : F("FAIL"));
          Serial.print(F(" TILT(id="));
          Serial.print(BUS_ID_TILT);
          Serial.print(F(")="));
          Serial.println(ok2 ? F("OK") : F("FAIL"));
        } else {
          const bool ok = busPing((uint8_t)id, 80);
          Serial.print(F("BUSPING id="));
          Serial.print(id);
          Serial.print(F("="));
          Serial.println(ok ? F("OK") : F("FAIL"));
        }
        return;
      }

      if (strncmp(line, "PTEN", 4) == 0) {
        int v = 1;
        if (strlen(line) > 4) {
          v = atoi(line + 4);
        }
        enablePanTiltOutput = (v != 0);
        Serial.print(F("PTEN="));
        Serial.println(enablePanTiltOutput ? F("1") : F("0"));
        return;
      }

      HostCommand next = cmd;
      if (parsePackedCommand(line, next)) {
        cmd = next;
        applyAccessories();
        if (enablePanTiltOutput) {
          applyPanTilt();
        }
        applyTrigger();
      } else {
        Serial.print(F("WARN BAD_CMD "));
        Serial.println(line);
      }
    }
  }
}
