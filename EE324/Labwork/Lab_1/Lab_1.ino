double kp = 1;
double kd = 1;
double ki = 1;

const int pinH = 2;
const int pinL = 3;
const int enable = 31;

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
  // put your setup code here, to run once:
  refValue = analogRead(A0);
  
  refValue += 512;
  if(refValue > 1023){
    refValue -= 1024;    
  }
  
  pinMode(pinH,OUTPUT);
  pinMode(pinL,OUTPUT);
  pinMode(enable,OUTPUT);

  analogWrite(pinH,0);
  analogWrite(pinL,0);
  digitalWrite(enable,HIGH);

  currTime = millis();
  prevTime = currTime;
  
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  currValue = analogRead(A0);
  error = currValue - refValue;
  if(error > 511){
    error -= 1024;
  }
  
  currTime = millis();
  dt = currTime - prevTime;
  prevTime = currTime;
  
  integral += error * dt;
  derivative = (error - prevError) / dt;
  prevError = error;
  
  control = (kp * error + kd * derivative + ki * integral)/4;

//  delay(100);

  if(control > 0){
    analogWrite(pinH,min(abs(control),255));
    analogWrite(pinL,0);
  }
  else{
    analogWrite(pinL,min(abs(control),255));
    analogWrite(pinH,0);
  }
}
