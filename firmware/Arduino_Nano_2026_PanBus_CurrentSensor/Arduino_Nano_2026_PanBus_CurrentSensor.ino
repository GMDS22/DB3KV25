/*
Arduino Nano Firmware (2026): Pan Serial-Bus + Total Current Sensor + PWM Tilt

GOAL
- Remain compatible with the existing DB3000 host serial protocol and expectations.
- Add total current monitoring (via analog current sensor) reported over USB serial.
- Pan is upgraded to a serial-bus servo (protocol depends on your servo family).
- Tilt remains a standard PWM hobby servo (Servo.h).

HOST (Python) EXPECTATIONS CONFIRMED IN REPO
1) Command protocol (single line, newline-terminated):
   P{pan}T{tilt}F{fire}L{led}R{laser}G{acc}S{safety}M{mode}\n
   Example:
   P42T70F0L0R0G0S1M0\n
2) Encoder request:
   Host may send:
   GET_ENCODER\n
   Host expects response:
   ENCODER_TILT,<tilt_deg>,RAW_COUNT,<count>\n
   NOTE: Tilt encoder hardware is optional/not installed in current builds.
   This sketch returns the last commanded tilt as encoder tilt, count=0.

3) Tilt safety parsing on host:
   Host only latches on explicit words like "TILT SAFETY SWITCH TRIGGERED".
   Do NOT spam generic "TILT SAFETY: OK" lines.

CURRENT MONITORING OUTPUT
- This sketch periodically prints a status line:
   STAT I=<milliamps>\n
- Optional (if you implement pan bus telemetry): add fields like IPAN=<mA>.

IMPORTANT: Pan serial-bus servo protocol
- The repo does NOT specify the exact serial-bus servo family.
- This sketch includes a configurable driver layer.
- You must choose/configure the bus protocol and wiring.

Tested compatibility focus:
- Serial baud default: 115200 (matches app defaults)
- Token parsing is robust and ignores malformed lines.

*/

#include <Arduino.h>
#include <Servo.h>
#include <EEPROM.h>

// -----------------------
// Serial configuration
// -----------------------
static const unsigned long HOST_BAUD = 115200;

// -----------------------
// Pins (adjust to your wiring)
// -----------------------
// Tilt PWM servo
static const uint8_t PIN_TILT_SERVO = 9;

// Firing output (MOSFET / relay / transistor)
static const uint8_t PIN_FIRE = 6;

// Relays / accessories
static const uint8_t PIN_LED_RELAY = 4;
static const uint8_t PIN_LASER_RELAY = 5;
static const uint8_t PIN_ACC_RELAY = 7;  // accessory token G

// Current sensor (analog)
static const uint8_t PIN_CURRENT_SENSOR = A0;

// Optional tilt safety switch input (hardware may not exist)
static const bool TILT_SAFETY_SWITCH_INSTALLED = false;
static const uint8_t PIN_TILT_SAFETY_SWITCH = 2; // must be interrupt-capable if used
static const bool TILT_SAFETY_ACTIVE_LOW = true;

// -----------------------
// Servo limits (must be >= host expected range)
// Host defaults (from repo docs): PAN 0..220, TILT 0..70
// -----------------------
static const int PAN_MIN_DEG = 0;
static const int PAN_MAX_DEG = 220;
static const int TILT_MIN_DEG = 0;
static const int TILT_MAX_DEG = 70;

// -----------------------
// Home defaults + EEPROM
// Existing logs show firmware prints "Loaded home Pan=90 Tilt=60".
// Keep defaults aligned with observed behavior unless you want otherwise.
// -----------------------
static const int HOME_PAN_DEFAULT = 90;
static const int HOME_TILT_DEFAULT = 60;

static const uint16_t EEPROM_MAGIC = 0xB30A;
static const int EEPROM_ADDR_MAGIC = 0;
static const int EEPROM_ADDR_HOME_PAN = EEPROM_ADDR_MAGIC + sizeof(EEPROM_MAGIC);
static const int EEPROM_ADDR_HOME_TILT = EEPROM_ADDR_HOME_PAN + sizeof(int);

// -----------------------
// Current sensor calibration
// -----------------------
// Set these based on your sensor module.
// Examples:
// - ACS712 5A: 185 mV/A, 2.5V zero
// - ACS712 20A: 100 mV/A, 2.5V zero
// - ACS712 30A: 66 mV/A, 2.5V zero

static const float ADC_REF_V = 5.0f;              // Nano default (assuming 5V reference)
static const float SENSOR_ZERO_V = 2.50f;         // adjust after measuring no-load output
static const float SENSOR_SENS_V_PER_A = 0.100f;  // volts per amp (adjust to your sensor)

// Current reporting behavior
static const unsigned long CURRENT_REPORT_INTERVAL_MS = 100; // 10 Hz
static const unsigned int CURRENT_SAMPLES = 16;              // oversampling to reduce noise

// -----------------------
// Pan servo serial-bus driver selection
// -----------------------
// Choose ONE:
//   PAN_BUS_PROTOCOL_NONE    -> compile-only stub (no real pan motion)
//   PAN_BUS_PROTOCOL_YD_SD35M -> Yahboom YD-SD35M (smart serial bus servo; 115200 UART via driver board)
//   PAN_BUS_PROTOCOL_LX16A   -> alias for the same 0x55 0x55 family (LewanSoul LX-16A / similar)
//
// IMPORTANT: Only enable a protocol that matches your servo family.
// -----------------------
#define PAN_BUS_PROTOCOL_NONE 1
// #define PAN_BUS_PROTOCOL_YD_SD35M 1
// #define PAN_BUS_PROTOCOL_LX16A 1

#if defined(PAN_BUS_PROTOCOL_YD_SD35M) || defined(PAN_BUS_PROTOCOL_LX16A)
  #include <SoftwareSerial.h>

  // Serial bus wiring assumptions (YD-SD35M typical):
  // - Use the YD-SD35M driver/debug board.
  // - Connect Nano UART (TX/RX) to the board's RX/TX pins (two-wire UART).
  // - The board converts two-wire UART into the servo's single-wire bus interface.
  // - Baud rate per product sheet: 115200.

  static const uint8_t PIN_PANBUS_RX = 10;
  static const uint8_t PIN_PANBUS_TX = 11;
  static const unsigned long PANBUS_BAUD = 115200;

  static const uint8_t PAN_SERVO_ID = 1;

  SoftwareSerial PanBus(PIN_PANBUS_RX, PIN_PANBUS_TX);

  // Optional direction pin for RS485/half-duplex transceiver
  static const bool PANBUS_USE_DIR_PIN = false;
  static const uint8_t PIN_PANBUS_DIR = 8;

#endif

// -----------------------
// State
// -----------------------
Servo tiltServo;

static int homePanDeg = HOME_PAN_DEFAULT;
static int homeTiltDeg = HOME_TILT_DEFAULT;

static int lastPanDeg = HOME_PAN_DEFAULT;
static int lastTiltDeg = HOME_TILT_DEFAULT;

static unsigned long lastCommandMs = 0;
static unsigned long lastCurrentReportMs = 0;

static bool tiltSafetyLocked = false; // only meaningful if switch installed

// -----------------------
// Helpers
// -----------------------
static int clampInt(int v, int lo, int hi) {
  if (v < lo) return lo;
  if (v > hi) return hi;
  return v;
}

static void eepromLoadHome() {
  uint16_t magic = 0;
  EEPROM.get(EEPROM_ADDR_MAGIC, magic);
  if (magic != EEPROM_MAGIC) {
    // Initialize EEPROM with defaults
    EEPROM.put(EEPROM_ADDR_MAGIC, EEPROM_MAGIC);
    EEPROM.put(EEPROM_ADDR_HOME_PAN, homePanDeg);
    EEPROM.put(EEPROM_ADDR_HOME_TILT, homeTiltDeg);
    return;
  }

  int hp = HOME_PAN_DEFAULT;
  int ht = HOME_TILT_DEFAULT;
  EEPROM.get(EEPROM_ADDR_HOME_PAN, hp);
  EEPROM.get(EEPROM_ADDR_HOME_TILT, ht);

  // Defensive clamp
  homePanDeg = clampInt(hp, PAN_MIN_DEG, PAN_MAX_DEG);
  homeTiltDeg = clampInt(ht, TILT_MIN_DEG, TILT_MAX_DEG);
}

static void printHome() {
  Serial.print(F("Home Pan="));
  Serial.print(homePanDeg);
  Serial.print(F(" Home Tilt="));
  Serial.println(homeTiltDeg);
}

static float readCurrentAmps() {
  unsigned long acc = 0;
  for (unsigned int i = 0; i < CURRENT_SAMPLES; i++) {
    acc += (unsigned long)analogRead(PIN_CURRENT_SENSOR);
  }
  float adc = (float)acc / (float)CURRENT_SAMPLES;
  float volts = (adc * ADC_REF_V) / 1023.0f;
  float amps = (volts - SENSOR_ZERO_V) / SENSOR_SENS_V_PER_A;
  if (amps < 0.0f) amps = 0.0f; // clamp noise below zero
  return amps;
}

static long readCurrentMilliAmps() {
  float amps = readCurrentAmps();
  long ma = (long)(amps * 1000.0f + 0.5f);
  if (ma < 0) ma = 0;
  return ma;
}

// -----------------------
// Pan bus driver layer
// -----------------------
static void panBusBegin() {
#if defined(PAN_BUS_PROTOCOL_YD_SD35M) || defined(PAN_BUS_PROTOCOL_LX16A)
  PanBus.begin(PANBUS_BAUD);
  if (PANBUS_USE_DIR_PIN) {
    pinMode(PIN_PANBUS_DIR, OUTPUT);
    digitalWrite(PIN_PANBUS_DIR, LOW);
  }
#endif
}

static void panBusWriteDeg(int panDeg) {
  panDeg = clampInt(panDeg, PAN_MIN_DEG, PAN_MAX_DEG);

#if defined(PAN_BUS_PROTOCOL_NONE)
  // Stub: keep lastPanDeg updated, but do not move hardware.
  (void)panDeg;
  return;
#elif defined(PAN_BUS_PROTOCOL_YD_SD35M) || defined(PAN_BUS_PROTOCOL_LX16A)
  // 0x55 0x55 family command packet (commonly used by "smart serial bus servo" ecosystems):
  // Header(0x55 0x55), ID, LEN, CMD, params..., checksum
  // CMD 1 = move time write: [pos_low, pos_high, time_low, time_high]
  // pos units are typically 0..1000 scaled to the servo's mechanical range.
  // For YD-SD35M, the product sheet lists ~270° rotation range and 115200 baud.

  // Map degrees (0..SERVO_RANGE_DEG) to 0..SERVO_MAX_TICKS.
  // NOTE: Your turret uses PAN 0..220, which is within a 270° servo range.
  const int SERVO_RANGE_DEG = 270;
  const int SERVO_MAX_TICKS = 1000;
  int deg = clampInt(panDeg, 0, SERVO_RANGE_DEG);
  int ticks = (deg * SERVO_MAX_TICKS) / SERVO_RANGE_DEG;
  ticks = clampInt(ticks, 0, SERVO_MAX_TICKS);

  // Movement time (ms)
  const uint16_t moveTime = 80;

  uint8_t pkt[10];
  pkt[0] = 0x55;
  pkt[1] = 0x55;
  pkt[2] = PAN_SERVO_ID;
  pkt[3] = 7;          // length
  pkt[4] = 1;          // CMD_MOVE_TIME_WRITE
  pkt[5] = (uint8_t)(ticks & 0xFF);
  pkt[6] = (uint8_t)((ticks >> 8) & 0xFF);
  pkt[7] = (uint8_t)(moveTime & 0xFF);
  pkt[8] = (uint8_t)((moveTime >> 8) & 0xFF);

  uint8_t sum = 0;
  for (int i = 2; i <= 8; i++) sum += pkt[i];
  pkt[9] = (uint8_t)(~sum);

  if (PANBUS_USE_DIR_PIN) digitalWrite(PIN_PANBUS_DIR, HIGH);
  PanBus.write(pkt, sizeof(pkt));
  PanBus.flush();
  if (PANBUS_USE_DIR_PIN) digitalWrite(PIN_PANBUS_DIR, LOW);

  return;
#else
  (void)panDeg;
  return;
#endif
}

// -----------------------
// Command parsing
// -----------------------

struct Cmd {
  int panDeg;
  int tiltDeg;
  int fire;
  int led;
  int laser;
  int acc;
  int safety;
  int mode;
  bool valid;
};

static int parseTokenInt(const char* s, char token, int defaultVal) {
  const char* p = strchr(s, token);
  if (!p) return defaultVal;
  p++; // after token
  bool neg = false;
  if (*p == '-') { neg = true; p++; }
  long v = 0;
  bool any = false;
  while (*p >= '0' && *p <= '9') {
    any = true;
    v = v * 10 + (*p - '0');
    p++;
  }
  if (!any) return defaultVal;
  if (neg) v = -v;
  return (int)v;
}

static Cmd parseCommandLine(const char* line) {
  Cmd c;
  c.panDeg = lastPanDeg;
  c.tiltDeg = lastTiltDeg;
  c.fire = 0;
  c.led = 0;
  c.laser = 0;
  c.acc = 0;
  c.safety = 1;
  c.mode = 0;
  c.valid = false;

  // Command line must start with 'P' and include at least 'T'
  if (!line || line[0] != 'P') return c;
  if (!strchr(line, 'T')) return c;

  c.panDeg = parseTokenInt(line, 'P', c.panDeg);
  c.tiltDeg = parseTokenInt(line, 'T', c.tiltDeg);
  c.fire = parseTokenInt(line, 'F', c.fire);
  c.led = parseTokenInt(line, 'L', c.led);
  c.laser = parseTokenInt(line, 'R', c.laser);
  c.acc = parseTokenInt(line, 'G', c.acc);
  c.safety = parseTokenInt(line, 'S', c.safety);
  c.mode = parseTokenInt(line, 'M', c.mode);

  c.valid = true;
  return c;
}

static void applyCommand(const Cmd& c, const char* rawLine) {
  (void)rawLine;

  lastCommandMs = millis();

  // Clamp degrees to known safe limits
  int panDeg = clampInt(c.panDeg, PAN_MIN_DEG, PAN_MAX_DEG);
  int tiltDeg = clampInt(c.tiltDeg, TILT_MIN_DEG, TILT_MAX_DEG);

  // Apply tilt safety lock if installed
  if (TILT_SAFETY_SWITCH_INSTALLED && tiltSafetyLocked) {
    // Do not update tilt if locked; keep lastTiltDeg
    tiltDeg = lastTiltDeg;
  }

  // Move servos
  panBusWriteDeg(panDeg);
  tiltServo.write(tiltDeg);

  lastPanDeg = panDeg;
  lastTiltDeg = tiltDeg;

  // Outputs
  digitalWrite(PIN_LED_RELAY, c.led ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY, c.laser ? HIGH : LOW);
  digitalWrite(PIN_ACC_RELAY, c.acc ? HIGH : LOW);

  // Safety: if safe, force fire off.
  const bool safe = (c.safety != 0);
  if (safe) {
    digitalWrite(PIN_FIRE, LOW);
  } else {
    // Fire each time the host requests it (rapid-fire friendly)
    digitalWrite(PIN_FIRE, c.fire ? HIGH : LOW);
  }

  // Optional: echo command for debugging (keep light)
  Serial.print(F("[CMD] "));
  Serial.print(rawLine);
  Serial.print(F(" -> Pan="));
  Serial.print(panDeg);
  Serial.print(F(" Tilt="));
  Serial.print(tiltDeg);
  Serial.print(F(" | Fire="));
  Serial.print(c.fire);
  Serial.print(F(" Mode="));
  Serial.print(c.mode ? F("BB") : F("Water"));
  Serial.print(F(" | LED="));
  Serial.print(c.led);
  Serial.print(F(" Laser="));
  Serial.print(c.laser);
  Serial.print(F(" Acc3="));
  Serial.print(c.acc);
  Serial.print(F(" | Safety="));
  Serial.println(c.safety);

  // Fire debug lines (matches existing log style loosely)
  if (c.fire == 0) {
    // Avoid spamming too much; but existing firmware prints this occasionally.
    // Keep it minimal.
    // Serial.println(F("[FIRE] Water trigger OFF"));
  }
}

static void respondEncoder() {
  // Host expects: ENCODER_TILT,<tilt>,RAW_COUNT,<count>
  Serial.print(F("ENCODER_TILT,"));
  Serial.print(lastTiltDeg);
  Serial.print(F(",RAW_COUNT,"));
  Serial.println(0);
}

static void maybeReportCurrent() {
  const unsigned long now = millis();
  if (now - lastCurrentReportMs < CURRENT_REPORT_INTERVAL_MS) return;
  lastCurrentReportMs = now;

  long totalMa = readCurrentMilliAmps();

  Serial.print(F("STAT I="));
  Serial.println(totalMa);
}

static void updateFireWatchdog() {
  // Defensive: if host stops sending commands, force fire OFF.
  // Keep this lenient so rapid-fire pulses and normal tracking are unaffected.
  const unsigned long now = millis();
  const unsigned long FIRE_WATCHDOG_MS = 1000;
  if (now - lastCommandMs > FIRE_WATCHDOG_MS) {
    digitalWrite(PIN_FIRE, LOW);
  }
}

static void updateTiltSafety() {
  if (!TILT_SAFETY_SWITCH_INSTALLED) return;

  bool raw = digitalRead(PIN_TILT_SAFETY_SWITCH);
  bool triggered = TILT_SAFETY_ACTIVE_LOW ? (raw == LOW) : (raw == HIGH);

  if (triggered && !tiltSafetyLocked) {
    tiltSafetyLocked = true;
    Serial.println(F("TILT SAFETY SWITCH TRIGGERED"));
  } else if (!triggered && tiltSafetyLocked) {
    tiltSafetyLocked = false;
    Serial.println(F("TILT SAFETY SWITCH RESET"));
  }
}

// -----------------------
// Serial line buffer
// -----------------------
static const size_t LINE_BUF_SIZE = 96;
static char lineBuf[LINE_BUF_SIZE];
static size_t lineLen = 0;

static void handleLine(const char* line) {
  if (!line || !line[0]) return;

  // Trim CR
  size_t n = strlen(line);
  while (n > 0 && (line[n - 1] == '\r' || line[n - 1] == '\n')) {
    n--;
  }
  if (n == 0) return;

  // Special command
  if (strncmp(line, "GET_ENCODER", 11) == 0) {
    respondEncoder();
    return;
  }

  // Main command
  Cmd c = parseCommandLine(line);
  if (!c.valid) {
    // Ignore malformed line
    return;
  }

  applyCommand(c, line);
}

void setup() {
  Serial.begin(HOST_BAUD);

  pinMode(PIN_FIRE, OUTPUT);
  digitalWrite(PIN_FIRE, LOW);

  pinMode(PIN_LED_RELAY, OUTPUT);
  pinMode(PIN_LASER_RELAY, OUTPUT);
  pinMode(PIN_ACC_RELAY, OUTPUT);
  digitalWrite(PIN_LED_RELAY, LOW);
  digitalWrite(PIN_LASER_RELAY, LOW);
  digitalWrite(PIN_ACC_RELAY, LOW);

  if (TILT_SAFETY_SWITCH_INSTALLED) {
    pinMode(PIN_TILT_SAFETY_SWITCH, INPUT_PULLUP);
  }

  // Tilt PWM servo
  tiltServo.attach(PIN_TILT_SERVO);

  // Pan bus
  panBusBegin();

  // EEPROM home
  eepromLoadHome();

  // Initialize positions
  lastPanDeg = clampInt(homePanDeg, PAN_MIN_DEG, PAN_MAX_DEG);
  lastTiltDeg = clampInt(homeTiltDeg, TILT_MIN_DEG, TILT_MAX_DEG);

  // Apply initial positions
  panBusWriteDeg(lastPanDeg);
  tiltServo.write(lastTiltDeg);

  // Startup prints (match existing logs loosely)
  Serial.print(F("[EEPROM] Loaded home Pan="));
  Serial.print(homePanDeg);
  Serial.print(F(" Tilt="));
  Serial.println(homeTiltDeg);

  Serial.println(F("=== Turret Ready ==="));
  Serial.println(F("No startup sweep (initial movement disabled). Ready to receive commands."));

  lastCommandMs = millis();
  lastCurrentReportMs = millis();
}

void loop() {
  // Read incoming serial non-blocking
  while (Serial.available() > 0) {
    char ch = (char)Serial.read();

    if (ch == '\n') {
      lineBuf[lineLen] = '\0';
      handleLine(lineBuf);
      lineLen = 0;
      continue;
    }

    // ignore CR
    if (ch == '\r') {
      continue;
    }

    if (lineLen + 1 < LINE_BUF_SIZE) {
      lineBuf[lineLen++] = ch;
    } else {
      // overflow: reset buffer to avoid partial garbage
      lineLen = 0;
    }
  }

  updateTiltSafety();
  updateFireWatchdog();
  maybeReportCurrent();
}
