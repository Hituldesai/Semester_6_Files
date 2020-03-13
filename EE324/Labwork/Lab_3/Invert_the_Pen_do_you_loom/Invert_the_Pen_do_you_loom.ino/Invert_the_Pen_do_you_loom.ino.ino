#define sel1 38
#define sel2 39
#define rst_ 40
#define clk 12

int       alpha, theta;
double    aAcPv, tAcPv, aAcPr, tAcPr, aDerv, tDerv, u;
byte      alpha1, alpha2, theta1, theta2;
const double pi = 3.14159265;

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
  aAcPr = 0;
  tAcPr = 0;
  aAcPv = 0;
  tAcPv = 0;
  
  DDRC  = 0b00000000;
  DDRA  = 0b00000000;

  Serial.begin(9600);
}

void loop()
{
  digitalWrite(sel1, HIGH);
  digitalWrite(sel2, LOW);
  alpha1 = PINC;
  digitalWrite(sel1, LOW);
  digitalWrite(sel2, LOW);
  alpha2 = PINC;
  alpha  = word(alpha2, alpha1);
  aAcPv  = aAcPr;
  aAcPr  = float(alpha)*pi/1000.0;
  aDerv  = aAcPr - aAcPv;
  
  digitalWrite(sel1, HIGH);
  digitalWrite(sel2, LOW);
  theta1 = PINA;
  digitalWrite(sel1, LOW);
  digitalWrite(sel2, LOW);
  theta2 = PINA;
  theta  = word(theta2, theta1);
  tAcPv  = tAcPr;
  tAcPr  = float(theta)*pi/1000.0;
  tDerv  = tAcPr - tAcPv;
  
  Serial.print(" alpha = "); Serial.print(aAcPr); Serial.print(" and theta = "); Serial.println(tAcPr);
  Serial.print(" aDerv = "); Serial.print(aDerv); Serial.print(" and tDerv = "); Serial.println(tDerv);
  
  double K[4] = {-2.23606797749981, 26.6206812801476, -0.945081597923937, 3.29130028676845};
  double x[4] = {tAcPr, aAcPr, tDerv, aDerv};
  u = 0;
  for (int i = 0; i<4; i++)
  {
    u = K[i]*x[i];
  }
  Serial.print("   Input = "); Serial.println(u);
  Serial.println("");
}
