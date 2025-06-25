#!/usr/bin/python3
#sensor abstand Boden
#stop alle Motoren
#
import RPi.GPIO as GPIO
import time, os

abboden = 29 #abstand Boden
stopallmotors = 1 #Motorstop

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(abboden, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.input(abboden)

#def angehoben():

try:
    setup()
    while True:
        if GPIO.input(abboden) == 1:
            stopallmotors = 1
        if GPIO.input(abboden) == 0:
            stopallmotors = 0
#        print (stopallmotors)

except KeyboardInterrupt:
    GPIO.cleanup()