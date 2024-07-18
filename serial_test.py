import serial

def main():
    # Öffnen der seriellen Verbindung
    try:
        ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
        print("Serielle Verbindung geöffnet")
    except serial.SerialException as e:
        print(f"Fehler beim Öffnen der seriellen Verbindung: {e}")
        return
    
    try:
        while True:
            if ser.in_waiting > 0:
                try:
                    state = ser.readline().decode('utf-8').strip()
                    print("Empfangen:", state)  # Debugging-Ausgabe
                except Exception as e:
                    print(f"Fehler beim Lesen der seriellen Daten: {e}")
            else:
                print("Keine Daten verfügbar")  # Debugging-Ausgabe
            time.sleep(0.1)  # Kurze Pause, um das Graphenfenster zu aktualisieren
    finally:
        ser.close()  # Stelle sicher, dass der serielle Port sauber geschlossen wird
        print("Serielle Verbindung geschlossen")

if __name__ == "__main__":
    main()
