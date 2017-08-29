
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(4,GPIO.OUT)
while True:
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.02)

