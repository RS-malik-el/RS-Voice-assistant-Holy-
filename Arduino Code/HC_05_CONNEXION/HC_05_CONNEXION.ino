/*
  e-mail : rachelsysteme@gmail.com
  gitHub : https://github.com/RS-malik-el
  Donation : paypal.me/RachelSysteme

  @AUTEUR: RACHEL SYSTEME
  DATE   : 24/05/2022
  
  @Conçu pour communiquer avec le logiciel : "RS : Voice assistant (Holy)"
  @Tester sur la carte arduino avec le module Bluetooth HC-05
  @Test on the arduino board with the HC-05 Bluetooth module
  
  Ce programme permet de contrôler l'allumage et l'extinction de 4 leds,
  le positionnent du servomoteur à 0° ou 90°. 
*/
#include <SoftwareSerial.h>
#include <Servo.h>

// Constantes
#define _rx     2
#define _tx     3
#define _led1   4
#define _led2   5
#define _led3   6
#define _led4   7
#define _servo  8
// Objet de type SoftwareSerial
SoftwareSerial Bluetooth(_rx,_tx);
// Objet de type Servo
Servo servo;
uint8_t position = 0; // Position servomoteur

void setup() {
  Bluetooth.begin(9600);// Initialisation de la communication
  servo.attach(_servo); // Pin attaché au servo
  servo.write(position);       // Servo à 0°
  // Initialisation des pins comme des sorties
  for (int i = 4; i <= 7; ++i){
    pinMode(i,OUTPUT);
    digitalWrite(i,not LOW);
  }
}

void loop() {
  String reception="";

  // Reception des données
  if(Bluetooth.available()){
    while(true){
      if(Bluetooth.available())
        reception += (char)Bluetooth.read();
      else
        break;
      delay(10);
    }
  }

  // Traitement des données
  if (reception.length()==5 or reception.length()==6){
    // LED 1
    if (reception.charAt(0) == '0')
      digitalWrite(_led1,not LOW);
    else
       digitalWrite(_led1,not HIGH);
    // LED 2
    if (reception.charAt(1) == '0')
      digitalWrite(_led2,not LOW);
    else
       digitalWrite(_led2,not HIGH);
    // LED 3
    if (reception.charAt(2) == '0')
      digitalWrite(_led3,not LOW);
    else
       digitalWrite(_led3,not HIGH);
    // LED 4
    if (reception.charAt(3) == '0')
      digitalWrite(_led4,not LOW);
    else
       digitalWrite(_led4,not HIGH);
    // POSITIONNEMENT DU SERVOMOTEUR
    if (reception.charAt(4) == '0' and position == 90){
      for (int i = 90; i >= 0 ; --i){
        servo.write(i);
        delay(5);
      }
      position = 0;
    }
    if (reception.charAt(4) != '0' and position == 0){
      for (int i = 0; i <= 90 ; ++i){
        servo.write(i);
        delay(5);
      }
      position = 90;
    }
    Bluetooth.flush();
    Bluetooth.write("TRUE"); // Message succès
  }
}
