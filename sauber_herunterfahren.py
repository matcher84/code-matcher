#!/usr/bin/python3
#sauber Herunterfahren
#sudo shutdown -h now
#
import RPi.GPIO as GPIO
import time, os

hftaster = 36 #sauber Herunterfahren
slon = 31 #Status LED ON

def setup():
   GPIO.setmode(GPIO.BOARD)
   GPIO.setwarnings(False)
   GPIO.setup(hftaster, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
   GPIO.setup(slon, GPIO.OUT)
   GPIO.input(hftaster)
   GPIO.output(slon, GPIO.LOW)

def herunterfahren():
   time.sleep(5)
   GPIO.output(slon, GPIO.LOW)
   os.system("sudo shutdown -h now")
   GPIO.cleanup()

setup()

try:
   while True:
      GPIO.output(slon, GPIO.HIGH)
      if GPIO.input(hftaster) == 1:
         herunterfahren()
         GPIO.cleanup()

except KeyboardInterrupt:
   GPIO.cleanup()