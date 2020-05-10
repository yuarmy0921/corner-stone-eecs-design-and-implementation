/***************************************************************************/
// File			  [node.h]
// Author		  [Erik Kuo, Joshua Lin]
// Synopsis		[Code for managing car movement when encounter a node]
// Functions  [/* add on yout own! */]
// Modify		  [2020/03/027 Erik Kuo]
/***************************************************************************/

#include <SoftwareSerial.h>
#include <Wire.h>

/*===========================import variable===========================*/
int extern r1, l1, r2, l2, r3, l3;
int extern _Tp;
/*===========================import variable===========================*/

// TODO: add some function to control your car when encounter a node
// here are something you can try: left_turn, right_turn... etc.

void right_turn(){
  digitalWrite(MotorL_I1,HIGH);
  digitalWrite(MotorL_I2,LOW);
  digitalWrite(MotorR_I3,HIGH);
  digitalWrite(MotorR_I4,LOW);
  //參數未調整
  analogWrite(ENA,100);
  analogWrite(ENB,100);
  delay(600);
}
void left_turn(){
  digitalWrite(MotorL_I1,LOW);
  digitalWrite(MotorL_I2,HIGH);
  digitalWrite(MotorR_I3,LOW);
  digitalWrite(MotorR_I4,HIGH);
  //參數未調整
  analogWrite(ENA,100);
  analogWrite(ENB,100);
  delay(500);
}
void U_turn(){
  digitalWrite(MotorL_I1,HIGH);
  digitalWrite(MotorL_I2,LOW);
  digitalWrite(MotorR_I3,HIGH);
  digitalWrite(MotorR_I4,LOW);
  //參數未調整
  analogWrite(ENA,100);
  analogWrite(ENB,100);
  delay(1000);
}
