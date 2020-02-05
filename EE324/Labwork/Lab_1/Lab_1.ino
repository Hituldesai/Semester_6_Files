double K_p = 200;
double K_d = 500;
double K_i = 0.002;

const int pinH   = 2;
const int pinL   = 3;
const int enable = 13;

double refValue;
double currValue;
double error;
double prevError;
double derivative;
double integral = 0;
double dt;
double control;
unsigned long prevTime;
unsigned long currTime;

void setup() {
  refValue = analogRead(A0);

  refValue += 512;
//  refValue += 10.0/360.0 * 1024.0;
  //refValue += 10/360.0*1024;
  
  if(refValue > 1023){
    refValue -= 1024;
  }
  refValue = refValue * 360 / 1024.0;
  refValue = refValue - 30;
  if(refValue > 360){
    refValue -= 360;
  }
  if(refValue < 0){
    refValue += 360;
  }
//   refValue=(refValue-30)*360/350.0;
   
  if(refValue > 90 && refValue < 270){
    refValue +=10;
  }
  else{
    refValue -= 10;
  }
  //refValue += 10;
  pinMode(pinH,   OUTPUT);
  pinMode(pinH,   OUTPUT);
  pinMode(enable, OUTPUT);

  analogWrite(pinH, 0);
  analogWrite(pinL, 0);
  digitalWrite(enable, HIGH);

  currTime = millis();
  prevTime = currTime;

  Serial.begin(9600);
}

void loop() {
  currValue = analogRead(A0);
  currValue = currValue * 360 / 1024.0;
    currValue = currValue - 30;
  if(currValue > 360){
    currValue -= 360;
  }
  if(currValue < 0){
    currValue += 360;
  }
  currTime = millis();
  error     = currValue - refValue;
  if(error > 180){
    error -= 360;
  }
  else if(error < -180){
    error += 360;
  }
  
  dt = currTime - prevTime;
  integral  += error * dt;
  derivative = (error - prevError) / dt;
  prevError  = error;
  if(abs(error) < 3.6){
    K_p = 5;
    K_i = 0;}
  control    = (K_p * error + K_d * derivative + K_i * integral) ;
  if(control > 0){
    analogWrite(pinH, min(abs(control), 255));
    analogWrite(pinL, 0);
  }
  else{
    analogWrite(pinL, min(abs(control), 255));
    analogWrite(pinH, 0);
  }
  prevTime = currTime;
  //Serial.print(error);Serial.print(" ");Serial.print(K_p * error);Serial.print(" ");Serial.print(K_d * derivative);Serial.print(" ");Serial.println(K_i * integral);
  Serial.print(error);Serial.print(" ");Serial.print(currTime);Serial.println(";");
}
