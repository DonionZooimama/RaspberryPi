import RPi.GPIO as GPIO

on = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
while True:
    GPIO.output(18,on)
    on != on
