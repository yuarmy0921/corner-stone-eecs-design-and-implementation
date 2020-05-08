/***************************************************************************/
// File			  [track.h]
// Author		  [Erik Kuo]
// Synopsis		[Code used for tracking]
// Functions  [MotorWriting, tracking]
// Modify		  [2020/03/27 Erik Kuo]
/***************************************************************************/

#include <SoftwareSerial.h>
#include <Wire.h>

/*if you have no idea how to start*/
/*check out what you have learned from week 1 & 6*/
/*feel free to add your own function for convenience*/

/*===========================import variable===========================*/
int extern _Tp;
/*===========================import variable===========================*/

// Write the voltage to motor.
void MotorWriting(double vL, double vR) {
  // TODO: use L298N to control motor voltage & direction
  double truevR;
  double truevL; 
  if(vR<0){
    truevR = -vR;
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
  }
  else{
    truevR = vR;
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
  }
  if(vL<0){
    truevL = -vL;
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
  }
  else{
    truevL = vL;
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
  }
  analogWrite(ENA,truevR);
  analogWrite(ENB,truevL);
  
}// MotorWriting

// P/PID control Tracking
void tracking(int l1,int l2,int l3,int r3,int r2,int r1){
  //TODO: complete your P/PID tracking code
}// tracking
