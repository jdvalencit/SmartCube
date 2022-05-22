#include <SoftwareSerial.h>
#include <ArduinoJson.h>
SoftwareSerial nodemcu(D6, D5); // RX, TX

void setup() {
  Serial.begin(9600);
  nodemcu.begin(9600);
  while (!Serial) continue;
}
 
void loop() {
  StaticJsonBuffer<1000> jsonBuffer;
  JsonObject& data = jsonBuffer.parseObject(nodemcu);
  if (data == JsonObject::invalid()) {
    Serial.println("Invalid json object");
    jsonBuffer.clear();
    return;
  }
  Serial.println("JSON object received");
  Serial.print("Temp: ");
  float temp = data["temp"];
  
  Serial.println(temp);
}
