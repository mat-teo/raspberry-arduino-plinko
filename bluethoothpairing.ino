#include "BluetoothSerial.h"
#include <ESP32Servo.h>

Servo myservo;  // create servo object to control a servo

int posVal = 0;    // variable to store the servo position
int servoPin = 15; // Servo motor pin
#define USE_NAME // Comment this to use MAC address instead of a slaveName
const char *pin = "1234"; // Change this to reflect the pin expected by the real slave BT device
 
#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Bluetooth not available or not enabled. It is only available for the ESP32 chip.
#endif
 
BluetoothSerial SerialBT;
 
#ifdef USE_NAME
  String slaveName = "plinko"; // Change this to reflect the real name of your slave BT device
#else
  String MACadd = "AA:BB:CC:11:22:33"; // This only for printing
  uint8_t address[6]  = {0xAA, 0xBB, 0xCC, 0x11, 0x22, 0x33}; // Change this to reflect real MAC address of your slave BT device
#endif
 
String myName = "plinko";
 
const int s1=13;
const int s2=12;
const int s3=14;
const int s4=27;
const int s5=26;
const int s6=25;
const int s7=33;
int inputVal = 0;
int input = 0;

void setup() {
  bool connected;
  myservo.setPeriodHertz(50);           // standard 50 hz servo
  myservo.attach(servoPin, 500, 2500);  // attaches the servo on servoPin to the servo object
  myservo.write(130);
  pinMode(s1,INPUT);    //Pin 2 is connected to the output of proximity sensor
  pinMode(s2,INPUT);
  pinMode(s3,INPUT);
  pinMode(s4,INPUT);    //Pin 2 is connected to the output of proximity sensor
  pinMode(s5,INPUT);
  pinMode(s6,INPUT);
   pinMode(s7,INPUT);

  Serial.begin(115200);

  SerialBT.begin(myName, true);
  Serial.printf("The device \"%s\" started in master mode, make sure slave BT device is on!\n", myName.c_str());
 
  #ifndef USE_NAME
    SerialBT.setPin(pin);
    Serial.println("Using PIN");
  #endif
 
  // connect(address) is fast (up to 10 secs max), connect(slaveName) is slow (up to 30 secs max) as it needs
  // to resolve slaveName to address first, but it allows to connect to different devices with the same name.
  // Set CoreDebugLevel to Info to view devices Bluetooth address and device names
  #ifdef USE_NAME
    connected = SerialBT.connect(slaveName);
    Serial.printf("Connecting to slave BT device named \"%s\"\n", slaveName.c_str());
  #else
    connected = SerialBT.connect(address);
    Serial.print("Connecting to slave BT device with MAC "); Serial.println(MACadd);
  #endif
 
  if(connected) {
    Serial.println("Connected Successfully!");
  } else {
    while(!SerialBT.connected(10000)) {
      Serial.println("Failed to connect. Make sure remote device is available and in range, then restart app.");
    }
  }
  // Disconnect() may take up to 10 secs max
  if (SerialBT.disconnect()) {
    Serial.println("Disconnected Successfully!");
  }
  // This would reconnect to the slaveName(will use address, if resolved) or address used with connect(slaveName/address).
  SerialBT.connect();
  if(connected) {
    Serial.println("Reconnected Successfully!");
  } else {
    while(!SerialBT.connected(10000)) {
      Serial.println("Failed to reconnect. Make sure remote device is available and in range, then restart app.");
    }
  }
}
 
void loop() {
  int input = 0;
  bool inPartita = false;
  char read;
  if (SerialBT.available()) {
    read = SerialBT.read();
  }
  
  if(read=='1'){
    Serial.println("in partita");
    inPartita = true;
    myservo.write(70);
  }
  while(inPartita){
    input=sensore();
    if(input!=0){
      Serial.println(input);
      SerialBT.print(input);
      inPartita=false;
      Serial.println("fine partita");
    }
  }
  myservo.write(130);

 /* if (Serial.available()) {
    SerialBT.write(Serial.read());
  }
  if (SerialBT.available()) {
    Serial.write(SerialBT.read());
  }*/

  delay(50);
}

int sensore(){
  int flag = 0;
  int input = 0;
  if(analogRead(s1)<300){
    flag++;
    input = 2;
  }
  if(analogRead(s2)<300){
    flag++;
    input = 3;
  }
  if(analogRead(s3)<300){
    flag++;
    input = 4;
  }
  if(analogRead(s4)<300){
    flag++;
    input = 5;
  }
  if(analogRead(s5)<300){
    flag++;
    input = 6;
  }
  if(analogRead(s6)<300){
    flag++;
    input = 7;
  }
    if(analogRead(s7)<300){
    flag++;
    input = 8;
  }
  if(flag==1){
    return input;
  }
  return 0;
}