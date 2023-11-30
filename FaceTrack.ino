#include <Servo.h>

Servo servoX;
Servo servoY;

void setup() {
  Serial.begin(9600);
  pinMode(4,OUTPUT);
  servoX.attach(2);
  servoY.attach(10);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int commaIndex = data.indexOf(',');
    
    if (commaIndex != -1) {
      String xStr = data.substring(0, commaIndex);
      String yStr = data.substring(commaIndex + 1);

      // Convert string values to integers
      int x = xStr.toInt();
      int y = yStr.toInt();
      analogWrite(2,15);
      int servoXAngle = map(x, 0, 1280, 0, 180);
      int servoYAngle = map(y, 0, 720, 0, 180);

      servoXAngle = constrain(servoXAngle, 0, 180);
      servoYAngle = constrain(servoYAngle, 0, 180);

      servoX.write(-(servoXAngle-180));
      servoY.write(servoYAngle);

      Serial.print("Servo X: ");
      Serial.print(servoXAngle);
      Serial.print(" Servo Y: ");
      Serial.println(servoYAngle);
    }
  }
}
