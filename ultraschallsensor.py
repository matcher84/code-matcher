#!/usr/bin/python3
#ultraschallsensor
#
import RPi.GPIO as GPIO
import time

# Pin-Konfiguration
TRIG_PIN = 22
ECHO_PIN = 23

# GPIO-Modus festlegen
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def get_distance():
    # Trigger-Pin auf HIGH für 10us setzen, um den Sensor zu triggern
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Warte auf das HIGH-Signal am Echo-Pin
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    # Warte auf das LOW-Signal am Echo-Pin
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Berechne die Pulszeit
    pulse_duration = pulse_end - pulse_start

    # Berechne die Entfernung (Schallgeschwindigkeit = ca. 343 m/s)
    distance = pulse_duration * 17150

    # Entfernung auf zwei Dezimalstellen runden
    distance = round(distance, 0)

    return distance

try:
    while True:
        distance = get_distance()
#        print(f"Entfernung: {distance} cm")
        entfernung = int(distance)
        time.sleep(1)
#        print(f"Entfernung: {entfernung} cm")
except KeyboardInterrupt:
    print("Messung gestoppt")
finally:
    GPIO.cleanup()