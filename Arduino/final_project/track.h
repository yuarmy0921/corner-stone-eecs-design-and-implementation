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
double Ki=0.04,Kd=0.08,Kp=0.4;
double error_,SumError=0,LastError=0;
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
  /*int n1,n2,n3,n4,n5;
  n1=l3+l2;
  n2=l2+l1;
  n3=l1+r1;
  n4=r1+r2;
  n5=r2+r3;
  if(n1>1900){}
  //error = 0.03*l3+0.018*l2+0.006*l1-0.006*r1-0.018*r2-0.03*r3;
  error=0.01*n1+0.03*n2-0.03*n4-0.01*n5;
  Serial.println(error);
  MotorWriting(64-0.5*error,64+0.5*error);*/
   Serial.println(l3);
    Serial.println(l2);
     Serial.println(l1);
      Serial.println(r1);
       Serial.println(r2);
        Serial.println(r3);
         
  error = 3.0*l3+1.7*l2+1.0*l1-1.0*r1-1.7*r2-3.0*r3;
  error = error/11.4;
  MotorWriting(64*(1-2*error),64*(1+2*error));
  Serial.println(error);
}// tracking

//test
void PID_control(int l3,int l2,int l1,int r1,int r2,int r3){
  //當越外側讀到的值越大，error越大
  //設定right為正，left為負
  //採樣週期
  //穩態誤差：響應時間、與期望值的差
  //積分時間：減小誤差
  //微分時間：加快響應速度，偵測誤差變化趨勢
  error_ = -0.07*l3 - 0.06*l2 - 0.01*l1 + 0.01*r1 + 0.06*r2 + 0.07*r3;  //有待測試
 
  //SumError += error_;
  error_ = Kp*error_ + Ki*SumError + Kd*(error_- LastError);
  LastError = error_;
  
  //Serial.println(error_);
         
  MotorWriting(70-error_, 70+error_);   //輸入：左 右
  /*Serial.println(" ");
  Serial.print("error: ");
  Serial.println(error_);
  Serial.print("left: ");
  Serial.println(70-error_);
  Serial.print("right: ");
  Serial.println(70+error_);
  */
}
