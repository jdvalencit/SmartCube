#include <ESP8266WiFi.h>
#include "ThingSpeak.h"

int prox = 0;
char ssid[] = "POCO X3 Pro";
char pass[] = "Davidzito23";  
int keyIndex = 0;   
WiFiClient  client;

unsigned long myChannelNumber = 1684778;
const char * myWriteAPIKey = "TNNUUUG471LLV9WR";

int number1 = random(0,20);
int number2 = random(0,20);
int number3 = random(0,20);

void setup() {
  pinMode(prox,INPUT);
  Serial.begin(115200); 
  while (!Serial) {
    
  }
  
  WiFi.mode(WIFI_STA); 
  ThingSpeak.begin(client);
}

void loop() {
  int value = 0;
  value = analogRead(prox);
  Serial.println(value);
  
  
  if(WiFi.status() != WL_CONNECTED){
    Serial.print("Attempting to connect to SSID. ");
    while(WiFi.status() != WL_CONNECTED){
      WiFi.begin(ssid, pass);
      Serial.print(".");
      delay(5000);     
    } 
    Serial.println("\nConnected.");
  }
  
  if(value < 20 and value > 10){
    ThingSpeak.setField(1, value);
  }
  
  ThingSpeak.setField(2, number2);
  ThingSpeak.setField(3, number3);

  
  int x = ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);
  
  if(x == 200){
    Serial.println("Channel update successful.");
  }
  else{
    Serial.println("Problem updating channel. HTTP error code " + String(x));
  }

  number1 = random(0,20);
  number2 = random(0,20);
  number3 = random(0,20);
  
  delay(2000);
}
