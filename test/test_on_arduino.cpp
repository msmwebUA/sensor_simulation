// Arduino UNO
// 4 sensor inputs
// 1 pulse = 1 revolution
// Results every 10 seconds

const byte SENSOR1 = 4;
const byte SENSOR2 = 5;
const byte SENSOR3 = 6;
const byte SENSOR4 = 7;

unsigned long revolutions[4] = {0, 0, 0, 0};
bool previousState[4] = {HIGH, HIGH, HIGH, HIGH};

unsigned long lastReport = 0;

void setup() {
  Serial.begin(115200);

  // HIGH = sensor released
  // LOW  = sensor connected to GND
  pinMode(SENSOR1, INPUT_PULLUP);
  pinMode(SENSOR2, INPUT_PULLUP);
  pinMode(SENSOR3, INPUT_PULLUP);
  pinMode(SENSOR4, INPUT_PULLUP);

  lastReport = millis();

  Serial.println("RPM counter started");
}

void loop() {
  byte pins[4] = {
    SENSOR1,
    SENSOR2,
    SENSOR3,
    SENSOR4
  };

  // Check all four sensors
  for (byte i = 0; i < 4; i++) {
    bool state = digitalRead(pins[i]);

    // Count HIGH -> LOW transition
    if (previousState[i] == HIGH && state == LOW) {
      revolutions[i]++;
    }

    previousState[i] = state;
  }

  // Print results every 10 seconds
  if (millis() - lastReport >= 10000) {

    Serial.println();
    Serial.println("----- 10 seconds -----");

    Serial.print("S1: ");
    Serial.print(revolutions[0]);
    Serial.println(" revolutions");

    Serial.print("S2: ");
    Serial.print(revolutions[1]);
    Serial.println(" revolutions");

    Serial.print("S3: ");
    Serial.print(revolutions[2]);
    Serial.println(" revolutions");

    Serial.print("S4: ");
    Serial.print(revolutions[3]);
    Serial.println(" revolutions");

    // Reset counters for the next 10 seconds
    for (byte i = 0; i < 4; i++) {
      revolutions[i] = 0;
    }

    lastReport = millis();
  }
}