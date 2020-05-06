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
}// MotorWriting

// P/PID control Tracking
void tracking(int l1,int l2,int l3,int r3,int r2,int r1){
  //TODO: complete your P/PID tracking code
}// tracking
