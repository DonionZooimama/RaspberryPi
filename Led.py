
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
while True:
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(32, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(32, GPIO.LOW)

