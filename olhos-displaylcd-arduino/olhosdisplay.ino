#include <LiquidCrystal.h>
 
//seta os pinos do LCD
LiquidCrystal lcd(A5,A4,A0,A1,A2,A3);
               //(RS,E ,D4,D5,D6,D7).

//Olhos abertos:
 byte SIMB1[8] = {B00000,B00000,B00001,B00011,B00111,B00111,B00111,B00111};
 byte SIMB2[8] = {B00000,B00000,B11111,B11111,B11111,B11111,B11111,B11111};
 byte SIMB3[8] = {B00000,B00000,B10000,B11000,B11100,B11100,B11100,B11100};
 byte SIMB4[8] = {B00000,B00000,B00000,B00000,B00000,B00000,B00000,B00000};
 byte SIMB5[8] = {B00111,B00111,B00111,B00111,B00011,B00001,B00000,B00000};
 byte SIMB6[8] = {B11111,B10001,B00000,B00000,B11111,B11111,B00000,B00000};
 byte SIMB7[8] = {B11100,B11100,B11100,B11100,B11000,B10000,B00000,B00000};
 byte SIMB8[8] = {B00000,B00000,B00000,B00000,B00000,B00000,B00000,B00000};


void setup (){
  lcd.begin(16,2);
  lcd.createChar(1,SIMB1);
  lcd.createChar(2,SIMB2);
  lcd.createChar(3,SIMB3);
  lcd.createChar(4,SIMB4);
  lcd.createChar(5,SIMB5);
  lcd.createChar(6,SIMB6);
  lcd.createChar(7,SIMB7);
  lcd.createChar(8,SIMB8);
  
}

void loop(){
  lcd.setCursor(4,0);  
  lcd.write(1);
  lcd.write(2);
  lcd.write(3);
  lcd.write(4);
  lcd.write(1);
  lcd.write(2);
  lcd.write(3);
  lcd.write(4);
  
  lcd.setCursor(4,1);
  lcd.write(5);
  lcd.write(6);
  lcd.write(7);
  lcd.write(8);
  lcd.write(5);
  lcd.write(6);
  lcd.write(7);
  lcd.write(8);
  
  delay(3000);
  lcd.clear();
  delay(1000);
  

 
}
