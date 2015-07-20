int TriggerPin3 = 10;
int EchoPin3 = 9;

int TriggerPin2 = 8;
int EchoPin2 = 7;

int TriggerPin1 = 12;
int EchoPin1 = 13;

float speedOfSound = 340; // in m/s
float targetDistance; //in cm
float pingTime;

void setup() {
  Serial.begin(115200);
  pinMode(TriggerPin1,OUTPUT);
  pinMode(EchoPin1,INPUT);
  
  pinMode(TriggerPin2,OUTPUT);
  pinMode(EchoPin2,INPUT);


  pinMode(TriggerPin3,OUTPUT);
  pinMode(EchoPin3,INPUT);


  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
}

void loop() {
  
  digitalWrite(TriggerPin1,LOW);
  delayMicroseconds(50);
  digitalWrite(TriggerPin1,HIGH);
  delayMicroseconds(10);
  digitalWrite(TriggerPin1,LOW);
  
  pingTime = pulseIn(EchoPin1,HIGH);
  
  pingTime = pingTime / 1000000.0; // in seconds
  targetDistance = 100*speedOfSound*pingTime / 2; // unit:  cm/microseconds
  
  if(targetDistance<=40)
  {
    digitalWrite(6, HIGH);
  Serial.print(targetDistance);
  Serial.println(" 1");
  }
  else 
  {
    digitalWrite(6, LOW);
  }  
  
  digitalWrite(TriggerPin2,LOW);
  delayMicroseconds(50);
  digitalWrite(TriggerPin2,HIGH);
  delayMicroseconds(10);
  digitalWrite(TriggerPin2,LOW);
  
  pingTime = pulseIn(EchoPin2,HIGH);
  
  pingTime = pingTime / 1000000.0; // in seconds
  targetDistance = 100*speedOfSound*pingTime / 2; // unit:  cm/microseconds
  
  if(targetDistance<=40)
  {
    digitalWrite(5, HIGH);
    Serial.print(targetDistance);
    Serial.println(" 2");
  }
  else 
  {
    digitalWrite(5, LOW);
  }

  

  digitalWrite(TriggerPin3,LOW);
  delayMicroseconds(50);
  digitalWrite(TriggerPin3,HIGH);
  delayMicroseconds(10);
  digitalWrite(TriggerPin3,LOW);
  
  pingTime = pulseIn(EchoPin3,HIGH);
  
  pingTime = pingTime / 1000000.0; // in seconds
  targetDistance = 100*speedOfSound*pingTime / 2; // unit:  cm/microseconds
  
  if(targetDistance<=40)
  {
    digitalWrite(4, HIGH);
  Serial.print(targetDistance);
  Serial.println(" 3");
  }
  else 
  {
    digitalWrite(4, LOW);
  }
  
  //Serial.println("");
  //Serial.println("");
  
  delay(10);
}

