void setup() ***REMOVED***
  // put your setup code here, to run once:
  pinMode(3,OUTPUT);
  Serial.begin(9600);
}

void loop() ***REMOVED***
  // put your main code here, to run repeatedly:
  if(Serial.available()>0)
  ***REMOVED***
     char c = Serial.read();
     if(c=='0')***REMOVED***
        Serial.println("STOP");
        digitalWrite(3,HIGH);
        delay(15000);
        Serial.println("RUN");
        digitalWrite(3,LOW);
   ***REMOVED***
***REMOVED***
}
