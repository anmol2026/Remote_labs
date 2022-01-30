void setup() {
  // put your setup code here, to run once:
  pinMode(3,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0)
  {
     char c = Serial.read();
     if(c=='0'){
        Serial.println("STOP");
        digitalWrite(3,HIGH);
        delay(15000);
        Serial.println("RUN");
        digitalWrite(3,LOW);
     }
  }
}
