
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(6,GPIO.OUT)
while True:
        GPIO.output(6, GPIO.HIGH)
        time.sleep(0.8)
        GPIO.output(6, GPIO.LOW)
        time.sleep(0.8)

