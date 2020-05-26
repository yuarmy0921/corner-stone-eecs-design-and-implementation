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
  l3 = analogRead(L3);
  l2 = analogRead(L2);
  l1 = analogRead(L1);
  r1 = analogRead(R1);
  r2 = analogRead(R2);
  r3 = analogRead(R3);
}
 
// variable for motor power
int _Tp=90;

// enum for car states, 不懂得可以自己google C++ enum
enum ControlState
{
   HAULT_STATE,
   SEARCH_STATE,
};


void loop()
{
  if(lastInstruct == instruct){
    PID_control(l3, l2, l1, r1, r2, r3);
    MotorWriting(70-error_, 70+error_);   //輸入：左 右
    } 
  else{
    //一直轉直到error > 0
    //再回到循跡模式
    if(instruct == TURNRIGHT){
      while(error == 0){
        right_turn();
        error = PID_control(l3, l2, l1, r1, r2, r3);
      }
    } else if(instruct == TURNLEFT){
      while(error == 0){
        left_turn();
        error = PID_control(l3, l2, l1, r1, r2, r3);
      }
    } else {
    
    }
  } 
 
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
