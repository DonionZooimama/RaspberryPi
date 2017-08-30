
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
while True:
        for i in range(3):
                GPIO.output(16, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(16, GPIO.LOW)
                time.sleep(0.2)
        for i in range(3):
                GPIO.output(16, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(16, GPIO.LOW)
                time.sleep(0.5)
        
