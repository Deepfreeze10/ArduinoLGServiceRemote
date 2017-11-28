#include <IRremote.h>
#include <SoftwareSerial.h>
#include <Wire.h>

SoftwareSerial mySerial(8, 9); // RX, TX

IRsend irsend;

unsigned long ezAdjust = 0x20DFDF20; 
unsigned long inStart = 0x20DFFF00;
//unsigned long powerOnly = 0x20DFC837;
//unsigned long inStop = 0x20DFC837;
// https://sourceforge.net/p/lirc-remotes/code/ci/master/tree/remotes/lg/42H3000.lircd.conf
unsigned long key0 = 0x20DF08F7;
unsigned long key1 = 0x20DF8877;
unsigned long key2 = 0x20DF48B7;
unsigned long key3 = 0x20DFC837;
unsigned long key4 = 0x20DF28D7;
unsigned long key5 = 0x20DFA857;
unsigned long key6 = 0x20DF6897;
unsigned long key7 = 0x20DFE817;
unsigned long key8 = 0x20DF18E7;
unsigned long key9 = 0x20DF9867;

unsigned short int keyCount = 12;
unsigned long keys[] = {
  key0,key1,key2,key3,key4,key5,key6,key7,key8,key9,ezAdjust,inStart
};

void pressButton(unsigned short int button)
{
  if (button<12){
    for (int i = 0; i < 3; i++) {
      irsend.sendNEC(keys[button], 32);
      delay(100);
    }
  }
}

void setup() {
  // put your setup code here, to run once:  
  Wire.begin(); // join i2c bus (address optional for master)
  Serial.begin(9600); // same as in your c++ script
  //Serial1.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
  mySerial.println("Hello, world?");
}

byte buttonByte1=0;
byte buttonByte2=0;
unsigned short int buttonInt=0;
int incomingByte = 0;   // for incoming serial data


void loop() {
  //mySerial.println("Hello, ?");
  //Serial1.println("Hello ....");
  // Read Serial input data when available
  if (Serial.available() > 5)
  {
    buttonByte1 = Serial.read();
    buttonByte2 = Serial.read();
    //mySerial.println(motor1Byte1);
    //mySerial.println(motor1Byte2);
    buttonInt = (buttonByte2<<8)|(buttonByte1);
    //mySerial.println(m1Angle);
    //Serial1.println(m1Angle);

    pressButton(buttonInt);
  }
}
