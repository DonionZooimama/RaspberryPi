
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
while True:
        GPIO.output(8, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(8, GPIO.LOW)
        time.sleep(0.05)

