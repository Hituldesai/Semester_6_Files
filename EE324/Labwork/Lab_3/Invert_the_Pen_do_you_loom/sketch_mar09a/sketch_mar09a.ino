#define sel1 38
#define sel2 39
#define rst_ 40
#define clk 12
#define input1 8
#define input2 9

int alpha,theta,input;
float ftheta,falpha,dtheta,dalpha,thetaprev,alphaprev,finput;
int voltage;
float k1,k2,k3,k4;
long int prevtime,currtime;
byte alpha1, alpha2, theta1, theta2;

/*
int abs(int x){
  if(x > 0) return x;
  return  -x;
}*/


void setup()
 {
  pinMode(sel1, OUTPUT);
  pinMode(sel2, OUTPUT);
  pinMode(rst_, OUTPUT);
  pinMode(clk, OUTPUT);

  TCCR1B=0x01;
  analogWrite(clk, 127);

  digitalWrite(rst_, LOW);
  delay(1000);
  digitalWrite(rst_, HIGH);

 alpha = 0;
 theta = 0;
 thetaprev = 0;
 alphaprev = 0;
 prevtime = millis();
 currtime = millis();
 DDRC=0b00000000;
 DDRA= 0b00000000;

  Serial.begin(9600);

}

void loop()
 {
  digitalWrite(sel1, HIGH);
  digitalWrite(sel2, LOW);
  theta1=PINC;
  digitalWrite(sel1, LOW);
  digitalWrite(sel2, LOW);
  theta2=PINC;
  theta=word(theta2, theta1);
  ftheta = theta * 3.14159265 / 1024;
  currtime = millis();
  Serial.print(currtime/1000.0);Serial.print("\t");
  Serial.print(ftheta*180/3.1416);Serial.print("\t");
  digitalWrite(sel1, HIGH);
  digitalWrite(sel2, LOW);
  alpha1=PINA;
  digitalWrite(sel1, LOW);
  digitalWrite(sel2, LOW);
  alpha2=PINA;
  alpha=word(alpha2, alpha1);
  falpha = alpha * 3.14159265 / 1024 ;
  Serial.print(falpha*180/3.1416); Serial.print("\t");Serial.println(";");

  dtheta = 1000.0 * (ftheta - thetaprev) / (currtime - prevtime);
  dalpha = 1000.0 * (falpha - alphaprev) / (currtime - prevtime);
k1 = -4.472136; 
 k2 = 52.511015; 
 k3 = -2.060511; 
 k4 = 6.800946;
  finput = k1 * ftheta + k2 * falpha + k3 * dtheta + k4 * dalpha;
  input = finput * 255.0 / 12.0 ;
  if(input > 255){
    input = 255;
  }
  else if(input < -255){
    input = -255;
  }
  if(input > 0){
    analogWrite(input1, abs(input));
    analogWrite(input2, 0);
  }
  else{
    analogWrite(input1, 0);
    analogWrite(input2, abs(input));
  }
  thetaprev = ftheta;
  alphaprev = falpha;
  prevtime = currtime;
}
