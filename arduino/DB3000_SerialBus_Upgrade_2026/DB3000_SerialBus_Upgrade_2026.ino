// Forward declarations for Arduino's auto-generated function prototypes.
// The Arduino build pipeline injects prototypes after #include lines; if a
// prototype references a struct declared later in the file, compilation fails.
struct CurrentCal;
struct HostCommand;

/*
  DB3000 Serial Bus Servo Upgrade (2026)
  -------------------------------------
  هدف: Upgrade Pan & Tilt to serial-bus servos via a debug board, while keeping trigger system intact.

  Host -> MCU command format (unchanged):
    P{pan}T{tilt}F{fire}L{led}R{laser}G{acc}S{safety}M{mode}\n
  Notes:
  - Safety token: S0 = ARMED, S1 = SAFE  (matches app/turret_enhancements.py formatting)
  - Mode token:   M1 = Projectile (BB Servo trigger), M0 = Water (MOSFET trigger)

  Telemetry (MCU -> Host):
    - If per-servo sensors are installed:
        CUR PmA=<pan_mA> TmA=<tilt_mA> TOTmA=<total_mA>\n
    - If only a TOTAL current sensor is installed:
        STAT I=<milliamps>\n
  IMPORTANT INVARIANT:
  - Trigger actuator remains separate from Pan/Tilt.
    * Water mode: MOSFET output pin.
    * Projectile mode: dedicated PWM trigger servo.

  You MUST adapt the serial-bus servo protocol to your servo model/debug board.
  The sketch provides an abstraction layer (ServoBusTransport + setBusServoAngle()).
*/

#include <Arduino.h>
#include <SoftwareSerial.h>
#include <Servo.h>

// ---------------------------
// Pin Mapping (Arduino Nano)
// ---------------------------

// Serial bus (to debug board)
// IMPORTANT: Many debug boards expect a UART.
// Set BUS_HALF_DUPLEX=1 if your board uses a single-wire data line (RX/TX tied).
#define BUS_HALF_DUPLEX 0

#if BUS_HALF_DUPLEX
static const uint8_t PIN_BUS_IO = 11; // single-wire data line
static const uint8_t PIN_BUS_RX = PIN_BUS_IO; // Nano RX  <- Debug board TX (shared)
static const uint8_t PIN_BUS_TX = PIN_BUS_IO; // Nano TX  -> Debug board RX (shared)
#else
static const uint8_t PIN_BUS_RX = 10; // Nano RX  <- Debug board TX
static const uint8_t PIN_BUS_TX = 11; // Nano TX  -> Debug board RX
#endif

// Trigger outputs (must remain supported)
static const uint8_t PIN_TRIGGER_MOSFET = 4; // Water mode output (via MOSFET driver)
static const uint8_t PIN_TRIGGER_SERVO  = 3; // Projectile mode trigger servo (PWM)

// Accessory outputs
static const uint8_t PIN_LED_RELAY   = 5; // LED relay/MOSFET driver
static const uint8_t PIN_LASER_RELAY = 6; // Laser relay/MOSFET driver

// Current sensing (analog)
// IMPORTANT: Sensors are OPTIONAL.
// If sensors are not installed, disable them here to avoid floating ADC noise.
// - per-servo (pan/tilt) sensors are typically on the debug board
// - total current is typically a dedicated sensor installed on the power feed
#define ENABLE_PAN_TILT_CURRENT_SENSORS 0
#define ENABLE_TOTAL_CURRENT_SENSOR 0

#if ENABLE_PAN_TILT_CURRENT_SENSORS
static const uint8_t PIN_CURR_PAN_A   = A0;
static const uint8_t PIN_CURR_TILT_A  = A1;
#endif
#if ENABLE_TOTAL_CURRENT_SENSOR
static const uint8_t PIN_CURR_TOTAL_A = A2;
#endif

// ---------------------------
// Serial configuration
// ---------------------------

static const uint32_t HOST_BAUD = 115200;
static const uint32_t BUS_BAUD  = 57600; // lowered for SoftwareSerial reliability on Nano

SoftwareSerial busSerial(PIN_BUS_RX, PIN_BUS_TX); // RX, TX

// ---------------------------
// Serial bus servo config
// ---------------------------

// Servo details (MUST fill in based on actual hardware):
// - Exact model name/vendor:
// - Protocol framing (half-duplex vs full-duplex TTL UART):
// - Required baud rate(s):
// - Angle units / limits / inversion rules:

// IDs on the serial bus
static const uint8_t BUS_ID_PAN  = 1;
static const uint8_t BUS_ID_TILT = 2;

// Limits (degrees) - keep aligned with host UI limits
static const int PAN_MIN_DEG  = 0;
static const int PAN_MAX_DEG  = 220;
static const int TILT_MIN_DEG = 0;
static const int TILT_MAX_DEG = 70;

// Serial-bus servo position units (ticks)
// Yahboom YB-SD35M debug tool uses 0..4095 with center at 2048.
// Map host degrees (PAN/TILT ranges above) onto these endpoints.
static const uint16_t PAN_TICKS_MIN  = 0;
static const uint16_t PAN_TICKS_MAX  = 4095;
static const uint16_t TILT_TICKS_MIN = 0;
static const uint16_t TILT_TICKS_MAX = 4095;

// Direction invert (set true if axis moves opposite)
static const bool INVERT_PAN  = false;
static const bool INVERT_TILT = false;

// Optional speed/accel mapping (placeholder)
static const uint16_t DEFAULT_MOVE_TIME_MS = 60; // servo-side move time; tune for smoothness

// ---------------------------
// Trigger config
// ---------------------------

Servo triggerServo;

// Projectile trigger servo angles (tune for your mechanism)
static const int TRIG_SERVO_REST_DEG = 20;
static const int TRIG_SERVO_FIRE_DEG = 70;
static const uint16_t TRIG_PULSE_MS  = 90;
static const uint16_t TRIG_COOLDOWN_MS = 120;

// ---------------------------
// Current conversion config
// ---------------------------

// All current values reported in mA.
// These conversion factors depend on your hardware.
// Provide a simple linear model: mA = slope_mA_per_count * adc + offset_mA.

struct CurrentCal {
  float slope_mA_per_count;
  float offset_mA;
};

// Default placeholders (MUST calibrate)
static const CurrentCal CAL_PAN   = { 5.0f, 0.0f };
static const CurrentCal CAL_TILT  = { 5.0f, 0.0f };
static const CurrentCal CAL_TOTAL = { 5.0f, 0.0f };

static inline int adcToMilliAmps(int adc, const CurrentCal &cal) {
  float mA = cal.slope_mA_per_count * (float)adc + cal.offset_mA;
  if (mA < 0) mA = 0;
  return (int)(mA + 0.5f);
}

// Telemetry rate
static const uint16_t TELEMETRY_HZ = 10;
static uint32_t lastTelemetryMs = 0;

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

// Dual-port support: allow host to disable pan/tilt bus output so Nano can be
// used for IO-only (trigger/relays/safety) while a PC drives pan/tilt directly.
static bool enablePanTiltOutput = true;

static int lastFireToken = 0;
static uint32_t lastFireMs = 0;

// ---------------------------
// Utilities
// ---------------------------

static inline int clampInt(int v, int lo, int hi) {
  if (v < lo) return lo;
  if (v > hi) return hi;
  return v;
}

static inline int applyInvertAndClamp(int deg, int minDeg, int maxDeg, bool invert) {
  deg = clampInt(deg, minDeg, maxDeg);
  if (!invert) return deg;
  // invert around the midpoint of the allowed range
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
#if BUS_HALF_DUPLEX
  pinMode(PIN_BUS_TX, OUTPUT);
#endif
  busSerial.write(data, len);
  busSerial.flush();
#if BUS_HALF_DUPLEX
  pinMode(PIN_BUS_RX, INPUT);
#endif
}

// ---------------------------
// Serial-bus servo protocol adapter
// ---------------------------

/*
  IMPORTANT:
  This function MUST be adapted to your servo model/debug board protocol.

  Common patterns:
  - LewanSoul/LX-16A style: binary packets, position 0..1000, time in ms
  - Feetech/STS/SC series: different packet framing
  - Debug board may already abstract to a simple ASCII protocol (e.g., "#1P1500T50")

  This sketch now implements the protocol observed in Yahboom's Windows debug tool
  ("Servo debugging platform v2.1" / DS_v4_* functions extracted from servo.exe):

  Write position (ADDR=0x2A):
    FF FF ID 07 03 2A POS_H POS_L TIME_H TIME_L CHK

  Read present position (ADDR=0x38, LEN=2):
    FF FF ID 04 02 38 02 CHK

  Checksum matches the tool exactly:
    CHK = 0xFF ^ (sum(bytes[2..(N-3)]) & 0xFF)
  i.e. it excludes the last parameter byte and the checksum byte.
*/
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
  pkt[3] = 0x07; // length
  pkt[4] = 0x03; // WRITE
  pkt[5] = 0x2A; // goal position register
  pkt[6] = posH;
  pkt[7] = posL;
  pkt[8] = timeH;
  pkt[9] = timeL;

  // Checksum observed from the vendor debug tool packets:
  //   chk = 0xFF - (sum(pkt[2..9]) % 256)
  pkt[10] = checksum_ff_minus_sum(pkt, 2, 9);

  busWrite(pkt, sizeof(pkt));
}

static bool busPing(uint8_t id, uint16_t timeoutMs) {
  // Ping packet from debug tool:
  //   FF FF ID 02 01 CHK
  uint8_t pkt[6];
  pkt[0] = 0xFF;
  pkt[1] = 0xFF;
  pkt[2] = id;
  pkt[3] = 0x02;
  pkt[4] = 0x01;
  pkt[5] = checksum_ff_minus_sum(pkt, 2, 4);

  // Clear any stale RX bytes
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
      // Typical response observed: FF F5 ID 02 00 CHK
      // We'll declare success if we see the ID and at least one 0xFF.
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
// Trigger handling (must remain intact)
// ---------------------------

static bool isArmed() {
  return cmd.safety == 0;
}

static void setMosfet(bool on) {
  digitalWrite(PIN_TRIGGER_MOSFET, on ? HIGH : LOW);
}

static void pulseTriggerServo() {
  // Fire pulse with cooldown; do NOT block for long.
  const uint32_t now = millis();
  if (now - lastFireMs < TRIG_COOLDOWN_MS) return;

  triggerServo.write(TRIG_SERVO_FIRE_DEG);
  delay(TRIG_PULSE_MS);
  triggerServo.write(TRIG_SERVO_REST_DEG);

  lastFireMs = now;
}

static void applyTrigger() {
  // Mode: M1 = BB servo trigger, M0 = MOSFET trigger
  if (!isArmed()) {
    // Always force trigger outputs to safe state.
    setMosfet(false);
    // Keep trigger servo at rest.
    triggerServo.write(TRIG_SERVO_REST_DEG);
    lastFireToken = cmd.fire;
    return;
  }

  if (cmd.mode == 0) {
    // Water (MOSFET): follow fire token directly (supports hold)
    setMosfet(cmd.fire != 0);
  } else {
    // Projectile (BB servo): pulse on rising edge
    const bool rising = (cmd.fire != 0) && (lastFireToken == 0);
    if (rising) {
      pulseTriggerServo();
    }
    // Ensure MOSFET is off in BB mode
    setMosfet(false);
  }

  lastFireToken = cmd.fire;
}

// ---------------------------
// Accessory outputs
// ---------------------------

static void applyAccessories() {
  digitalWrite(PIN_LED_RELAY, cmd.led ? HIGH : LOW);
  digitalWrite(PIN_LASER_RELAY, cmd.laser ? HIGH : LOW);
}

// ---------------------------
// Telemetry
// ---------------------------

static void sendTelemetryIfDue() {
  const uint32_t now = millis();
  const uint32_t interval = (TELEMETRY_HZ == 0) ? 1000 : (1000UL / TELEMETRY_HZ);
  if (now - lastTelemetryMs < interval) return;

  // If no sensors are installed/enabled, do not emit current telemetry.
  // Host will treat missing telemetry as "not available".
  if (!ENABLE_PAN_TILT_CURRENT_SENSORS && !ENABLE_TOTAL_CURRENT_SENSOR) {
    lastTelemetryMs = now;
    return;
  }

  int panmA = 0;
  int tiltmA = 0;
  int totmA = 0;

#if ENABLE_PAN_TILT_CURRENT_SENSORS
  const int panAdc = analogRead(PIN_CURR_PAN_A);
  const int tiltAdc = analogRead(PIN_CURR_TILT_A);
  panmA = adcToMilliAmps(panAdc, CAL_PAN);
  tiltmA = adcToMilliAmps(tiltAdc, CAL_TILT);
#endif

#if ENABLE_TOTAL_CURRENT_SENSOR
  const int totAdc = analogRead(PIN_CURR_TOTAL_A);
  totmA = adcToMilliAmps(totAdc, CAL_TOTAL);
#endif

#if ENABLE_PAN_TILT_CURRENT_SENSORS
  Serial.print(F("CUR PmA="));
  Serial.print(panmA);
  Serial.print(F(" TmA="));
  Serial.print(tiltmA);
  Serial.print(F(" TOTmA="));
  Serial.print(totmA);
  Serial.print('\n');
#else
  // Total-only format (backward-compatible with host parser)
  Serial.print(F("STAT I="));
  Serial.print(totmA);
  Serial.print('\n');
#endif

  lastTelemetryMs = now;
}

// ---------------------------
// Host command parsing
// ---------------------------

static bool parsePackedCommand(const char *line, HostCommand &out) {
  // Expected tokens: P.. T.. F.. L.. R.. G.. S.. M..
  // Robust-ish scan: find each letter and parse following integer.

  auto findTok = [&](char tok, int &value) -> bool {
    const char *p = strchr(line, tok);
    if (!p) return false;
    p++;
    // allow optional sign
    value = atoi(p);
    return true;
  };

  HostCommand c = out;

  // IO tokens must exist; P/T are optional so host can send IO-only lines.
  bool ok = true;
  // Optional P/T
  (void)findTok('P', c.panDeg);
  (void)findTok('T', c.tiltDeg);
  // Required IO tokens
  ok = findTok('F', c.fire) && ok;
  ok = findTok('L', c.led) && ok;
  ok = findTok('R', c.laser) && ok;
  // G optional
  findTok('G', c.acc);
  ok = findTok('S', c.safety) && ok;
  ok = findTok('M', c.mode) && ok;

  if (!ok) return false;

  // Clamp basic fields
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
      // overflow -> reset
      idx = 0;
    }
  }

  return false;
}

// ---------------------------
// Setup / Loop
// ---------------------------

void setup() {
  Serial.begin(HOST_BAUD);
  busSerial.begin(BUS_BAUD);

#if BUS_HALF_DUPLEX
  pinMode(PIN_BUS_RX, INPUT);
#endif

  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  pinMode(PIN_LED_RELAY, OUTPUT);
  pinMode(PIN_LASER_RELAY, OUTPUT);

  setMosfet(false);
  digitalWrite(PIN_LED_RELAY, LOW);
  digitalWrite(PIN_LASER_RELAY, LOW);

  triggerServo.attach(PIN_TRIGGER_SERVO);
  triggerServo.write(TRIG_SERVO_REST_DEG);

  // Optional: ADC reference
  // analogReference(DEFAULT);

  // Startup banner
  Serial.println(F("DB3000 SerialBus Upgrade 2026: READY"));
}

void loop() {
  static char line[96];

  // 1) Read command(s) from host
  if (readLineFromHost(line, sizeof(line))) {
    if (line[0] == 0) {
      // ignore empty
    } else {
      // Diagnostics: confirm bus wiring + servo presence.
      // Send from host as: "BUSPING" (pings IDs 1 and 2)
      // or "BUSPING 2" (pings a specific ID)
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

      // Dual-port support: PTEN 0/1 disables/enables pan/tilt output.
      // Use this when a PC directly drives servos via the debug board.
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

        // Apply outputs immediately
        applyAccessories();
        if (enablePanTiltOutput) {
          applyPanTilt();
        }
        applyTrigger();

      } else {
        // Unknown line; ignore but do not block
        Serial.print(F("WARN BAD_CMD "));
        Serial.println(line);
      }
    }
  }

  // 2) Telemetry
  sendTelemetryIfDue();
}
