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
float extern Ki, Kd, Kp;
Ki=0.05; Kd=0.01; Kp=0.05;
float extern error_, SumError, LastError;
SumError=0; LastError=0;
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

//test
void PID_control(int l3,int l2,int l1,int r1,int r2,int r3){
  //當越外側讀到的值越大，error越大
  //設定right為正，left為負
  //採樣週期
  //穩態誤差：響應時間、與期望值的差
  //積分時間：減小誤差
  //微分時間：加快響應速度，偵測誤差變化趨勢
  error_ = -0.05*l3 - 0.03*l2 - 0.01*l1 + 0.01*r1 + 0.03*r2 + 0.05*r3;  //有待測試
  SumError += error_;
  error_ = Kp*error + Ki*SumError + Kd*(error - LastError);
  MotorWriting(100+error, 100-error);   //輸入：左 右
  
}
