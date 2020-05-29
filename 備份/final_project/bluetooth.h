/***************************************************************************/
// File			  [bluetooth.h]
// Author		  [Erik Kuo]
// Synopsis		[Code for bluetooth communication]
// Functions  [ask_BT, send_msg, send_byte]
// Modify		  [2020/03/27 Erik Kuo]
/***************************************************************************/

/*if you have no idea how to start*/
/*check out what you have learned from week 2*/

#include<SoftwareSerial.h>
enum BT_CMD {
  NOTHING,TURNRIGHT,TURNLEFT,READ,HAULT,START,RESTART,TIGHT
  // TODO: add your own command type here
};

BT_CMD ask_BT(){
    BT_CMD message=NOTHING;
    char cmd;
    if(BT.available()){
      // TODO:
      // 1. get cmd from SoftwareSerial object: BT
      cmd = BT.read();
      BT.write(cmd);
      // 2. link bluetooth message to your own command type
      if(cmd =='1'){message=NOTHING; Serial.println(message);}
      if(cmd =='3'){message=TURNRIGHT; Serial.println(message);}
      if(cmd =='4'){message=TURNLEFT; Serial.println(message);}
      if(cmd =='2'){message=READ; Serial.println(message);}
      if(cmd =='5'){message=HAULT; Serial.println(message);}
      if(cmd =='s'){message=START; Serial.println(message);}
      if(cmd =='c'){message=RESTART;Serial.println("i can move again" );}
      if(cmd =='g'){message=TIGHT;}
      #ifdef DEBUG
      Serial.print("cmd : ");
      Serial.println(cmd);
      #endif
    }
    //else{//Serial.println("i dont have induction!!");}
    return message;
}// ask_BT

// send msg back through SoftwareSerial object: BT
// can use send_byte alternatively to send msg back
// (but need to convert to byte type)
void send_msg(const char& msg)
{    BT.write(msg);
    Serial.println("I snd it !");
     // TODO:
}// send_msg
//讓車子到達轉彎點時，回傳到達訊號


// send UID back through SoftwareSerial object: BT
void send_byte(byte *id, byte& idSize) {
  for (byte i = 0; i < idSize; i++) {  // Send UID consequently.
    BT.write(id[i]);
  }
  #ifdef DEBUG
  Serial.print("Sent id: ");
  for (byte i = 0; i < idSize; i++) {  // Show UID consequently.
    Serial.print(id[i], HEX);
  }
  Serial.println();
  #endif
}// send_byte
