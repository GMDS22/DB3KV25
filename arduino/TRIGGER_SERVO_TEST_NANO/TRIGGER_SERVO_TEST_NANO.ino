/*
 * Smart Sentry Nano Trigger Servo Test Sketch
 * 
 * Purpose: Isolate and test the trigger servo mechanism to identify why servo won't move
 * while MOSFET trigger works correctly.
 * 
 * Features:
 * - Direct servo control testing
 * - Serial command interface for testing
 * - Debug output for servo signals
 * - Pulse timing verification
 * - Safety/projectile mode simulation
 * - Real-time servo position feedback
 */

#include <Arduino.h>
#include <Servo.h>

// Pin definitions (matching original firmware)
static const int PIN_TRIGGER_SERVO = 9;
static const int PIN_TRIGGER_MOSFET = 3;
static const int PIN_LED_RELAY = 4;
static const int PIN_LASER_RELAY = 5;
static const int PIN_ACC_RELAY = 6;
static const int PIN_SPARE_RELAY = 7;

// Servo configuration
static const uint8_t TRIGGER_REST_DEG = 0;
static const uint8_t TRIGGER_FIRE_DEG = 45;
static const uint16_t TRIGGER_PULSE_MS = 120;
static const uint8_t TRIGGER_SPEED_DPS = 360;

// Test variables
Servo triggerServo;
bool safetyArmed = false;
bool projectileMode = false;
bool fireRequest = false;
bool triggerPulseActive = false;
uint32_t triggerPulseStartMs = 0;
uint32_t lastDebugMs = 0;
uint32_t servoAttachTime = 0;

// Serial command buffer
static const int CMD_BUFFER_SIZE = 64;
char cmdBuffer[CMD_BUFFER_SIZE];
int cmdIndex = 0;

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);
  
  Serial.println("=== SMART SENTRY TRIGGER SERVO TEST ===");
  Serial.println("Testing servo control mechanism isolation");
  Serial.println();
  
  // Initialize pins
  pinMode(PIN_TRIGGER_MOSFET, OUTPUT);
  pinMode(PIN_LED_RELAY, OUTPUT);
  pinMode(PIN_LASER_RELAY, OUTPUT);
  pinMode(PIN_ACC_RELAY, OUTPUT);
  pinMode(PIN_SPARE_RELAY, OUTPUT);
  
  // Set initial states
  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  digitalWrite(PIN_LED_RELAY, LOW);
  digitalWrite(PIN_LASER_RELAY, LOW);
  digitalWrite(PIN_ACC_RELAY, LOW);
  digitalWrite(PIN_SPARE_RELAY, LOW);
  
  // Initialize servo
  Serial.print("Attaching servo to pin ");
  Serial.println(PIN_TRIGGER_SERVO);
  
  triggerServo.attach(PIN_TRIGGER_SERVO);
  servoAttachTime = millis();
  
  // Test servo attachment
  Serial.print("Testing servo attachment... ");
  triggerServo.write(TRIGGER_REST_DEG);
  delay(500);
  
  // Verify servo is attached by reading pulse width
  int pulseWidth = triggerServo.readMicroseconds();
  Serial.print("Servo pulse width at rest: ");
  Serial.print(pulseWidth);
  Serial.println("us");
  
  if (pulseWidth < 500 || pulseWidth > 2500) {
    Serial.println("WARNING: Servo may not be properly attached!");
  } else {
    Serial.println("Servo attached successfully");
  }
  
  Serial.println();
  Serial.println("=== COMMANDS ===");
  Serial.println("ARM         - Arm safety system");
  Serial.println("DISARM      - Disarm safety system");
  Serial.println("PROJECTILE  - Toggle projectile mode");
  Serial.println("FIRE        - Fire trigger (single pulse)");
  Serial.println("HOLD        - Hold trigger in fire position");
  Serial.println("RELEASE     - Release trigger to rest");
  Serial.println("TEST        - Run automated test sequence");
  Serial.println("SERVO <deg> - Move servo to specific angle (0-180)");
  Serial.println("PULSE <ms>  - Test pulse duration (10-2000ms)");
  Serial.println("STATUS      - Show current system status");
  Serial.println();
  Serial.println("Ready for commands...");
}

void loop() {
  // Process serial commands
  while (Serial.available() > 0) {
    char c = Serial.read();
    if (c == '\n' || c == '\r') {
      if (cmdIndex > 0) {
        cmdBuffer[cmdIndex] = '\0';
        processCommand(cmdBuffer);
        cmdIndex = 0;
      }
    } else if (cmdIndex < CMD_BUFFER_SIZE - 1) {
      cmdBuffer[cmdIndex++] = toupper(c);
    }
  }
  
  // Handle trigger pulse timing
  handleTriggerPulse();
  
  // Debug output every 2 seconds
  if (millis() - lastDebugMs > 2000) {
    printDebugStatus();
    lastDebugMs = millis();
  }
  
  delay(10);
}

void processCommand(char* cmd) {
  Serial.print("CMD: ");
  Serial.println(cmd);
  
  if (strcmp(cmd, "ARM") == 0) {
    safetyArmed = true;
    Serial.println("Safety ARMED");
  } else if (strcmp(cmd, "DISARM") == 0) {
    safetyArmed = false;
    Serial.println("Safety DISARMED");
  } else if (strcmp(cmd, "PROJECTILE") == 0) {
    projectileMode = !projectileMode;
    Serial.print("Projectile mode: ");
    Serial.println(projectileMode ? "ON" : "OFF");
  } else if (strcmp(cmd, "FIRE") == 0) {
    fireRequest = true;
    Serial.println("Fire request sent");
  } else if (strcmp(cmd, "HOLD") == 0) {
    Serial.println("Holding trigger in fire position");
    triggerServo.write(TRIGGER_FIRE_DEG);
  } else if (strcmp(cmd, "RELEASE") == 0) {
    Serial.println("Releasing trigger to rest");
    triggerServo.write(TRIGGER_REST_DEG);
    triggerPulseActive = false;
    fireRequest = false;
  } else if (strcmp(cmd, "TEST") == 0) {
    runAutomatedTest();
  } else if (strncmp(cmd, "SERVO ", 6) == 0) {
    int angle = atoi(cmd + 6);
    if (angle >= 0 && angle <= 180) {
      Serial.print("Moving servo to ");
      Serial.print(angle);
      Serial.println(" degrees");
      triggerServo.write(angle);
    } else {
      Serial.println("Invalid angle. Use 0-180");
    }
  } else if (strncmp(cmd, "PULSE ", 6) == 0) {
    int pulseMs = atoi(cmd + 6);
    if (pulseMs >= 10 && pulseMs <= 2000) {
      Serial.print("Testing pulse for ");
      Serial.print(pulseMs);
      Serial.println("ms");
      testServoPulse(pulseMs);
    } else {
      Serial.println("Invalid pulse duration. Use 10-2000ms");
    }
  } else if (strcmp(cmd, "STATUS") == 0) {
    printDetailedStatus();
  } else {
    Serial.println("Unknown command");
  }
  
  Serial.println();
}

void handleTriggerPulse() {
  // This replicates the exact logic from the original firmware
  if (!safetyArmed) {
    digitalWrite(PIN_TRIGGER_MOSFET, LOW);
    triggerServo.write(TRIGGER_REST_DEG);
    triggerPulseActive = false;
    fireRequest = false;
    return;
  }

  if (!projectileMode) {
    digitalWrite(PIN_TRIGGER_MOSFET, fireRequest ? HIGH : LOW);
    triggerServo.write(TRIGGER_REST_DEG);
    triggerPulseActive = false;
    return;
  }

  digitalWrite(PIN_TRIGGER_MOSFET, LOW);
  if (fireRequest && !triggerPulseActive) {
    triggerPulseActive = true;
    triggerPulseStartMs = millis();
    Serial.print("Starting servo pulse to ");
    Serial.print(TRIGGER_FIRE_DEG);
    Serial.println(" degrees");
    triggerServo.write(TRIGGER_FIRE_DEG);
  }

  if (triggerPulseActive && (millis() - triggerPulseStartMs) >= TRIGGER_PULSE_MS) {
    Serial.print("Ending servo pulse, returning to ");
    Serial.print(TRIGGER_REST_DEG);
    Serial.println(" degrees");
    triggerServo.write(TRIGGER_REST_DEG);
    triggerPulseActive = false;
    fireRequest = false;
  }
}

void testServoPulse(int pulseMs) {
  Serial.println("=== SERVO PULSE TEST ===");
  
  // Move to rest position first
  triggerServo.write(TRIGGER_REST_DEG);
  delay(500);
  
  Serial.print("Moving to fire position (");
  Serial.print(TRIGGER_FIRE_DEG);
  Serial.println(" degrees)");
  triggerServo.write(TRIGGER_FIRE_DEG);
  
  // Hold for specified duration
  delay(pulseMs);
  
  Serial.print("Returning to rest position (");
  Serial.print(TRIGGER_REST_DEG);
  Serial.println(" degrees)");
  triggerServo.write(TRIGGER_REST_DEG);
  
  Serial.println("Pulse test complete");
}

void runAutomatedTest() {
  Serial.println("=== AUTOMATED TEST SEQUENCE ===");
  
  // Test 1: Basic servo movement
  Serial.println("Test 1: Basic servo movement");
  for (int angle = 0; angle <= 180; angle += 45) {
    Serial.print("Moving to ");
    Serial.print(angle);
    Serial.println(" degrees");
    triggerServo.write(angle);
    delay(1000);
  }
  
  // Test 2: Return to rest
  Serial.println("Test 2: Return to rest");
  triggerServo.write(TRIGGER_REST_DEG);
  delay(1000);
  
  // Test 3: Safety armed + projectile mode
  Serial.println("Test 3: Safety armed + projectile mode");
  safetyArmed = true;
  projectileMode = true;
  fireRequest = true;
  
  // Wait for pulse to complete
  while (triggerPulseActive) {
    handleTriggerPulse();
    delay(10);
  }
  
  // Test 4: MOSFET mode
  Serial.println("Test 4: MOSFET mode");
  projectileMode = false;
  fireRequest = true;
  delay(500);
  fireRequest = false;
  
  // Reset to safe state
  safetyArmed = false;
  triggerServo.write(TRIGGER_REST_DEG);
  
  Serial.println("Automated test complete");
}

void printDebugStatus() {
  Serial.print("DEBUG: Safety=");
  Serial.print(safetyArmed ? "ARMED" : "DISARMED");
  Serial.print(" Projectile=");
  Serial.print(projectileMode ? "ON" : "OFF");
  Serial.print(" FireRequest=");
  Serial.print(fireRequest ? "YES" : "NO");
  Serial.print(" PulseActive=");
  Serial.print(triggerPulseActive ? "YES" : "NO");
  Serial.print(" ServoPos=");
  Serial.print(triggerServo.read());
  Serial.print("deg PulseWidth=");
  Serial.print(triggerServo.readMicroseconds());
  Serial.println("us");
}

void printDetailedStatus() {
  Serial.println("=== DETAILED STATUS ===");
  Serial.print("Safety System: ");
  Serial.println(safetyArmed ? "ARMED" : "DISARMED");
  Serial.print("Trigger Mode: ");
  Serial.println(projectileMode ? "PROJECTILE (Servo)" : "MOSFET");
  Serial.print("Fire Request: ");
  Serial.println(fireRequest ? "ACTIVE" : "INACTIVE");
  Serial.print("Pulse Active: ");
  Serial.println(triggerPulseActive ? "YES" : "NO");
  Serial.print("Servo Position: ");
  Serial.print(triggerServo.read());
  Serial.println(" degrees");
  Serial.print("Servo Pulse Width: ");
  Serial.print(triggerServo.readMicroseconds());
  Serial.println(" microseconds");
  Serial.print("MOSFET State: ");
  Serial.println(digitalRead(PIN_TRIGGER_MOSFET) ? "HIGH" : "LOW");
  Serial.print("Servo Attached: ");
  Serial.println(triggerServo.attached() ? "YES" : "NO");
  Serial.print("Uptime: ");
  Serial.print(millis());
  Serial.println("ms");
  Serial.println("==================");
}
