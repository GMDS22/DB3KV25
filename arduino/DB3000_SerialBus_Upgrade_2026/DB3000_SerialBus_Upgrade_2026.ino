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
    CUR PmA=<pan_mA> TmA=<tilt_mA> TOTmA=<total_mA>\n
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
// IMPORTANT: Many debug boards expect a UART. These pins assume separate RX/TX.
// If your board uses half-duplex single-wire, see notes in setBusServoAngle().
static const uint8_t PIN_BUS_RX = 10; // Nano RX  <- Debug board TX
static const uint8_t PIN_BUS_TX = 11; // Nano TX  -> Debug board RX

// Trigger outputs (must remain supported)
static const uint8_t PIN_TRIGGER_MOSFET = 4; // Water mode output (via MOSFET driver)
static const uint8_t PIN_TRIGGER_SERVO  = 3; // Projectile mode trigger servo (PWM)

// Accessory outputs
static const uint8_t PIN_LED_RELAY   = 5; // LED relay/MOSFET driver
static const uint8_t PIN_LASER_RELAY = 6; // Laser relay/MOSFET driver

// Current sensing (analog)
// Assumption: debug board exposes analog current sense for pan & tilt;
// total current comes from a dedicated sensor.
static const uint8_t PIN_CURR_PAN_A   = A0;
static const uint8_t PIN_CURR_TILT_A  = A1;
static const uint8_t PIN_CURR_TOTAL_A = A2;

// ---------------------------
// Serial configuration
// ---------------------------

static const uint32_t HOST_BAUD = 115200;
static const uint32_t BUS_BAUD  = 115200; // adjust if your bus servos require different rate

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

  This sketch currently assumes an ASCII adapter protocol supported by your debug board:
    SB,<id>,<deg>,<time_ms>\n
  Example:
    SB,1,90,60

  If your debug board uses a different protocol, replace the body of this function.
*/
static void setBusServoAngle(uint8_t id, int deg, uint16_t moveTimeMs) {
  // Use a simple ASCII framing to keep this sketch self-contained.
  // Replace with your real bus-servo packets.
  busSerial.print(F("SB,"));
  busSerial.print(id);
  busSerial.print(F(","));
  busSerial.print(deg);
  busSerial.print(F(","));
  busSerial.print(moveTimeMs);
  busSerial.print('\n');
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

  const int panAdc = analogRead(PIN_CURR_PAN_A);
  const int tiltAdc = analogRead(PIN_CURR_TILT_A);
  const int totAdc = analogRead(PIN_CURR_TOTAL_A);

  const int panmA = adcToMilliAmps(panAdc, CAL_PAN);
  const int tiltmA = adcToMilliAmps(tiltAdc, CAL_TILT);
  const int totmA = adcToMilliAmps(totAdc, CAL_TOTAL);

  Serial.print(F("CUR PmA="));
  Serial.print(panmA);
  Serial.print(F(" TmA="));
  Serial.print(tiltmA);
  Serial.print(F(" TOTmA="));
  Serial.print(totmA);
  Serial.print('\n');

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
  bool ok = true;

  ok = findTok('P', c.panDeg) && ok;
  ok = findTok('T', c.tiltDeg) && ok;
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
      HostCommand next = cmd;
      if (parsePackedCommand(line, next)) {
        cmd = next;

        // Apply outputs immediately
        applyAccessories();
        applyPanTilt();
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
