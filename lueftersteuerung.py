#!/usr/bin/python3
#Lüfter CPU
#
import RPi.GPIO as GPIO
import time

fan = 37 #Lüfter

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(fan, GPIO.OUT)
    GPIO.output(fan, GPIO.LOW)

setup()

try:
    while True:
        dateil = open("/sys/class/thermal/thermal_zone0/temp", "r")
        temp = dateil.readline(2)
        dateil.close()
        dateis = open("Temp_CPU.txt", "w")
        tempout = dateis.write(time.strftime("%d.%m.%Y" "\n%H.%M.%S") + "\nCPU:" + "\n" + temp + " Gra>
        dateis.close()
        tempc = int(temp)
        print (tempc)
        if tempc <= 50:
            GPIO.output(fan, GPIO.LOW)
        if tempc >= 65:
            GPIO.output(fan, GPIO.HIGH)
        time.sleep(60)

except KeyboardInterrupt:
    GPIO.cleanup()