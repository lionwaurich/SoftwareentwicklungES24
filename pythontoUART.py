import serial

# Öffne die serielle Verbindung
ser = serial.Serial('/dev/ttyACM0', 115200)  # Ersetze /dev/ttyUSB0 durch den korrekten Port

try:
    while True:
        # Eingabe vom Benutzer lesen
        user_input = input("Gib den Zustand ein (oder 'q' zum Beenden): ")
        
        # Sende die Eingabe an den Arduino
        ser.write((user_input + '\n').encode())
        
        # Beenden, wenn 'q' eingegeben wurde
        if user_input.lower() == 'q':
            break
finally:
    ser.close()
