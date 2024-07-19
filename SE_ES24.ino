#include <Arduino.h>
#include <SoftwareSerial.h>
#include <FrameStream.h>
#include <Frameiterator.h>


// SoftwareSerial Pins (10 und 11 können beliebig geändert werden)
SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
  // Öffne die Hardware-Serial-Kommunikation mit 115200 Baud für die Kommunikation mit dem PC
  Serial.begin(115200);

  // Öffne die Software-Serial-Kommunikation mit 115200 Baud für die Kommunikation mit dem Raspberry Pi
  mySerial.begin(115200);

  // Warte darauf, dass die serielle Verbindung verfügbar wird
  while (!Serial) {
    ; // Warte auf die Verbindung
  }

  // Senden einer initialen Nachricht an den Benutzer
  Serial.println("Arduino bereit. Bitte geben Sie den Zustand ein:");
}

void loop() {
  // Prüfe, ob Daten vom seriellen Monitor verfügbar sind
  if (Serial.available() > 0) {
    // Lese die Eingabe vom seriellen Monitor
    String input = Serial.readStringUntil('\n');
    input.trim(); // Entferne etwaige Whitespace- oder Steuerzeichen

    // Debugging-Ausgabe
    Serial.print("Empfangene Eingabe: ");
    Serial.println(input);

    // Überprüfe die Eingabe
    if (input.equalsIgnoreCase("q")) {
      // Beenden der Schleife, wenn 'q' eingegeben wird
      Serial.println("Beenden des Programms...");
      mySerial.println("q");
      mySerial.flush(); // Ensure all data is sent
      while(true) {}
    }

    // Sende den eingegebenen Zustand an den Raspberry Pi
    mySerial.println(input);
    mySerial.flush(); // Ensure all data is sent

    // Bestätige die Eingabe im Terminal
    Serial.println("Zustand gesendet: " + input);
    Serial.println("Bitte nächsten Zustand eingeben oder 'q' zum Beenden:");
  }

  // Eine kleine Verzögerung, um das Polling zu verlangsamen
  delay(100);
}
