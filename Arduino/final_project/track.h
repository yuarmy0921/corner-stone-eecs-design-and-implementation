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
double extern error;
/*===========================import variable===========================*/

// Write the voltage to motor.

void MotorWriting(double vL, double vR) {
  // TODO: use L298N to control motor voltage & direction
  double truevR;
  double truevL; 
  if(vR<0){
    truevR = -vR;
    digitalWrite(MotorR_I3, HIGH);
    digitalWrite(MotorR_I4, LOW);
  }
  else{
    truevR = vR;
    digitalWrite(MotorR_I3, LOW);
    digitalWrite(MotorR_I4, HIGH);
  }
  if(vL<0){
    truevL = -vL;
    digitalWrite(MotorL_I1, LOW);
    digitalWrite(MotorL_I2, HIGH);
  }
  else{
    truevL = vL;
    digitalWrite(MotorL_I1, HIGH);
    digitalWrite(MotorL_I2, LOW);
  }
  analogWrite(ENA,truevR);
  analogWrite(ENB,truevL);
  
}// MotorWriting

// P/PID control Tracking
void tracking(int l3,int l2,int l1,int r1,int r2,int r3){
  //TODO: complete your P/PID tracking code
  error = 0.05*l3+0.03*l2+0.01*l1-0.01*r1-0.03*r2-0.05*r3;
  MotorWriting(100-error,100+error); 
}// tracking
