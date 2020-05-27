/***************************************************************************/
// File       [final_project.ino]
// Author     [Erik Kuo]
// Synopsis   [Code for managing main process]
// Functions  [setup, loop, Search_Mode, Hault_Mode, SetState]
// Modify     [2020/03/27 Erik Kuo]
/***************************************************************************/

#define DEBUG // debug flag

// for BlueTooth
#include<SoftwareSerial.h>
// for RFID
#include <SPI.h>
#include <MFRC522.h>

/*===========================define pin & create module object================================*/
// BlueTooth
SoftwareSerial BT(9,8);   // TX,RX on bluetooth module, 請按照自己車上的接線寫入腳位
// L298N, 請按照自己車上的接線寫入腳位(左右不一定要跟註解寫的一樣)
#define MotorL_I1     7 //定義 I1 接腳（左）
#define MotorL_I2     4 //定義 I2 接腳（左）
#define MotorR_I3     3 //定義 I3 接腳（又）
#define MotorR_I4     2 //定義 I4 接腳（又）
#define ENB    6 //定義 ENB (PWM調速) 接腳RIGHT
#define ENA    5 //定義 ENA (PWM調速) 接腳LEFT
// 循線模組, 請按照自己車上的接線寫入腳位
#define L3 A0
#define L2 A1
#define L1 A2
#define R1 A3
#define R2 A4
#define R3 A5
// RFID, 請按照自己車上的接線寫入腳位
#define RST_PIN      0        // 讀卡機的重置腳位
#define SS_PIN       10       // 晶片選擇腳位
MFRC522 mfrc522(SS_PIN, RST_PIN);  // 建立MFRC522物件
/*===========================define pin & create module object===========================*/

/*===========================declare function prototypes===========================*/
// search graph
void Search_Mode();
// wait for command
void Hault_Mode();
void SetState();
/*===========================declare function prototypes===========================*/

/*===========================define function===========================*/
void setup()
{
   //bluetooth initialization
   BT.begin(9600);
   //Serial window
   Serial.begin(9600);
   //RFID initial
   SPI.begin();
   mfrc522.PCD_Init();
   //L298N pin
   pinMode(MotorL_I1,   OUTPUT);
   pinMode(MotorL_I2,   OUTPUT);
   pinMode(MotorR_I3,   OUTPUT);
   pinMode(MotorR_I4,   OUTPUT);
   pinMode(ENA, OUTPUT);
   pinMode(ENB, OUTPUT);
   //tracking pin
   pinMode(L3, INPUT);
   pinMode(L2, INPUT);
   pinMode(L1, INPUT);
   pinMode(R1, INPUT);
   pinMode(R2, INPUT);
   pinMode(R3, INPUT);
#ifdef DEBUG
  Serial.println("Start!");
#endif
}// setup

// Import header files
#include "RFID.h"
#include "track.h"
#include "bluetooth.h"
#include "node.h"

// initalize parameter

// variables for 循線模組
int l3, l2, l1, r1, r2, r3;
double error;
int flag=0;
int delayfornodes=0;
void Sensor(){
  
  if(ask_BT()==5){flag=1;Serial.println("Now i can move");  Serial.println("full version");}
  
  if(ask_BT()==4){flag=0;Serial.println("Stop!!!!");}  
  
  if(flag==1){
    if(l3+l2+l1+r1+r2+r3>4000&&delayfornodes==0){
      Serial.println("i find a node!");
      send_msg('k');
      MotorWriting(0,0);
      delay(500);
      
      BT_CMD instruct;
      instruct = ask_BT();
      
      if(instruct==NOTHING){
        MotorWriting(150,150);
        delay(240);//860isok
        MotorWriting(0,0);
        delay(500);
         l3 = analogRead(L3);
         l2 = analogRead(L2);
         l1 = analogRead(L1);
         r1 = analogRead(R1);
         r2 = analogRead(R2);
         r3 = analogRead(R3);
         while(l1+l2+l3+r1+r2+r3<900){     
         l3 = analogRead(L3);
         l2 = analogRead(L2);
         l1 = analogRead(L1);
         r1 = analogRead(R1);
         r2 = analogRead(R2);
         r3 = analogRead(R3);
         MotorWriting(0,80);
         delay(80);
         MotorWriting(0,0);
         delay(20);
         }
   
      
        delayfornodes=1;
       }//讓車子剛好走到底，未調整
      if(instruct==TURNRIGHT){
        
        /*MotorWriting(80,80);
        delay(400);
        MotorWriting(0,0);
        delay(2000);*/
        right_turn();
        
        Serial.println("RRRRRRRRR");
        delayfornodes=1;
       }//讓車子剛好走到底，未調整
      if(instruct==TURNLEFT){
        /*MotorWriting(80,80);
        delay(500);
        MotorWriting(0,0);
        delay(100);*/
        left_turn();
        
        Serial.println("LLLLLLLLL");
        delayfornodes=1;
       }//讓車子剛好走到底，未調整
      if(instruct==READ){
        Serial.println("UUUUUUUUUU");
        //讀卡片rfid
        byte* id;
        byte idSize = 0;
        id = rfid(idSize);
        send_byte(id,idSize);
        delay(2000);
        BT_CMD second;
        second = ask_BT();
        while(1){
          if(second==RESTART){break;}  
          else if(second==TIGHT){
            byte* id;
            byte idSize = 0;
            id = rfid(idSize);
            send_byte(id,idSize);
            second = ask_BT();
          }
          else {second = ask_BT();}
         }
        //需考慮rfid開頭跟n一樣時的可能性
        
        U_turn();
        delayfornodes=1;
      }
      else{Serial.println("wheres my instruct");}
    }
    else{
      PID_control(l3,l2,l1,r1,r2,r3);
      delayfornodes=0;
      delay(50);
    }
  
  }
  else{
    MotorWriting(0,0);
  }
}
 
// variable for motor power
int _Tp=90;

// enum for car states, 不懂得可以自己google C++ enum
enum ControlState
{
   HAULT_STATE,
   SEARCH_STATE,
};

ControlState _state=HAULT_STATE;

// enum for bluetooth message, reference in bluetooth.h line 2
BT_CMD _cmd = NOTHING;
int small = 0;int yee = 0;
void loop()
{ 
  l3 = analogRead(L3);
  l2 = analogRead(L2);
  l1 = analogRead(L1);
  r1 = analogRead(R1);
  r2 = analogRead(R2);
  r3 = analogRead(R3);
  //right_turn();
Sensor();
  //MotorWriting(70,76);
  //PID_control(l3,l2,l1,r1,r2,r3);
  //U_turn();
  /*if(l3+l2+l1+r1+r2+r3>4000&&small%3==0&&yee==0){right_turn();small++;}
  if(l3+l2+l1+r1+r2+r3>4000&&small%3==1&&yee==0){right_turn();small++;}
  if(l3+l2+l1+r1+r2+r3>4000&&small%3==2&&yee==0){MotorWriting(0,0);delay(500);U_turn();small++;yee++;}
  if(l3+l2+l1+r1+r2+r3>4000&&small%3==0&&yee==0){left_turn();small++;}
  if(l3+l2+l1+r1+r2+r3>4000&&small%3==1&&yee==0){left_turn();small++;}
  if(l3+l2+l1+r1+r2+r3>4000&&small%3==2&&yee==0){MotorWriting(0,0);delay(500);U_turn();small++;yee++;}
  else{PID_control(l3,l2,l1,r1,r2,r3);}*/
   /*
   // search graph
   if(_state == SEARCH_STATE) Search_Mode();
   // wait for command
   else if(_state == HAULT_STATE) Hault_Mode();
   SetState();
   */
}// loop

/*
 void SetState()
{ 
  Sensor();
  // TODO:
  // 1. Get command from bluetooth 
  // 2. Change state if need
}// SetState
*/
void Hault_Mode()
{ 
  // TODO: let your car stay still
  
}// Hault_Mode

void Search_Mode()
{
  // TODO: let your car search graph(maze) according to bluetooth command from computer(python code)
}// Search_Mode


/*===========================define function===========================*/
