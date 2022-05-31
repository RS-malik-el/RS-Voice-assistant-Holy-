/*
  e-mail : rachelsysteme@gmail.com
  gitHub : https://github.com/RS-malik-el
  Donation : paypal.me/RachelSysteme

  @AUTEUR: RACHEL SYSTEME
  DATE   : 24/05/2022
  
  @Conçu pour communiquer avec le logiciel : "RS : Voice assistant (Holy)"
  @Tester sur la carte arduino / Test on the arduino board 
  
  Ce programme permet de contrôler l'allumage et l'extinction de 4 leds,
  le positionnent du servomoteur à 0° ou 90°. Les instructions sont envoyées 
  par communication série. 
*/
#include <Servo.h>

// Constantes
#define _led1   2
#define _led2   3
#define _led3   4
#define _led4   5
#define _servo  6
// Objet de type Servo
Servo servo;
uint8_t position = 0; // Position servomoteur

void setup() {
  Serial.begin(9600);   // Initialisation de la communication
  servo.attach(_servo); // Pin attaché au servo
  servo.write(position);// Servo à 0°
  // Initialisation des pins comme des sorties
  for (int i = 2; i <= 5; ++i){
    pinMode(i,OUTPUT);
    digitalWrite(i,not LOW);
  }
}

void loop() {
  byte reception[5]={};

  // Reception des données
  if(Serial.available()){
    Serial.readBytes(reception,5);
     
    // Mise à jour des sorties
    // LED 1
    if (reception[0] == 0)
      digitalWrite(_led1,not LOW);
    else
       digitalWrite(_led1,not HIGH);
    // LED 2
    if (reception[1] == 0)
      digitalWrite(_led2,not LOW);
    else
       digitalWrite(_led2,not HIGH);
    // LED 3
    if (reception[2] == 0)
      digitalWrite(_led3,not LOW);
    else
       digitalWrite(_led3,not HIGH);
    // LED 4
    if (reception[3] == 0)
      digitalWrite(_led4,not LOW);
    else
       digitalWrite(_led4,not HIGH);
    // POSITIONNEMENT DU SERVOMOTEUR
    if (reception[4] == 0 and position == 90){
      for (int i = 90; i >= 0 ; --i){
        servo.write(i);
        delay(5);
      }
      position = 0;
    }
    if (reception[4] == 90 and position == 0){
      for (int i = 0; i <= 90 ; ++i){
        servo.write(i);
        delay(5);
      }
      position = 90;
    }
    Serial.write("TRUE"); // Message succès
  }
}
