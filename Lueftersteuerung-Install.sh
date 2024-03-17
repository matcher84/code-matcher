#!/bin/bash
sudo apt update && sudo apt upgrade
sudo apt install python3
sudo apt install python3-rpi.gpio
sudo apt install python3-pip
sudo pip3 install RPi.GPIO

echo '#!/usr/bin/python3
#Lüfterswteuerung
#
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(17, GPIO.LOW)

while 1:
 dateilesen = open("/sys/class/thermal/thermal_zone0/temp", "r")
 temperatur = dateilesen.readline(2)
 dateilesen.close()
 dateis = open("Temp_CPU.txt", "w")
 temperaturout = dateis.write(time.strftime("%d.%m.%Y" "\n%H.%M.%S") + "\nCPU:" + "\n" + temperatur + " Grad")
 dateis.close()
 temperatur = int(temperatur)
 if temperatur<=50:
  GPIO.output(2, GPIO.HIGH)
  GPIO.output(17, GPIO.LOW)
  GPIO.output(3, GPIO.LOW)
  GPIO.output(4, GPIO.LOW)
 if temperatur<=55:
  GPIO.output(3, GPIO.HIGH)
  GPIO.output(17, GPIO.LOW)
  GPIO.output(2, GPIO.LOW)
  GPIO.output(4, GPIO.LOW)
 if temperatur>=58:
  GPIO.output(4, GPIO.HIGH)
  GPIO.output(2, GPIO.LOW)
  GPIO.output(3, GPIO.LOW)
  GPIO.output(17, GPIO.HIGH)
 time.sleep(60)
GPIO.cleanup()' >> Lueftersteuerung.py

chmod +x Lueftersteuerung.py

sudo -u pi crontab -l >> /tmp/pi_crontab.txt

echo "@reboot python3 /home/pi/Lueftersteuerung.py" >> /tmp/pi_crontab.txt #pi muss angepasst an ihren Benutzernamen sein

sudo -u pi crontab -i /tmp/pi_crontab.txt

sudo reboot
