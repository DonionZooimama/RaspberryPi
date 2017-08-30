
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)
while True:
        GPIO.output(32, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(32, GPIO.LOW)
        time.sleep(0.3)

