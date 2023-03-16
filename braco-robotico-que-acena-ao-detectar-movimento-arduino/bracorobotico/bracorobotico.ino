#include <Servo.h>

#define PIR 5

Servo servoBase; 
Servo servoDireita;
Servo servoEsquerda;
Servo servoGarra;

int pos = 0;

void setup() 
  {
  pinMode(PIR, INPUT);
  Serial.begin(9600);
  Serial.println("PROGRAMA INICIADO");
  servoBase.attach(13); 
  servoDireita.attach(11); 
  servoEsquerda.attach(9); 
  servoGarra.attach(7);    
}

void loop() 
{
  bool valorPIR = digitalRead(PIR);
  
  if (valorPIR) {
    
    Serial.println("Obstáculo Detectado");
    servoDireita.write(80);
    servoEsquerda.write(180);
    servoGarra.write(80); //80 fechado e 180 aberto
    servoBase.write(100);
    for (int vezes=0; vezes<2;vezes ++)
    {
      for(pos = 65; pos <= 135; pos += 1) //BASE
      {
        servoBase.write(pos);
        delay(6);
      }
      
        for(pos = 80; pos <= 180; pos += 1) //GARRA
      {
        servoGarra.write(pos); //GARRA
        delay(3);
      }
      
        for(pos = 135; pos>=65; pos -=1) //BASE
      {
        servoBase.write(pos);
        delay(6);
      }
      
        for(pos = 180; pos>=80; pos -=1) //GARRA
      {
        servoGarra.write(pos);
        delay(3);
      }
      
      delay(200);
    }

    for(pos = 65; pos<=100; pos +=1) //BASE
      {
        servoBase.write(pos);
        delay(7);
      }
  }
}
