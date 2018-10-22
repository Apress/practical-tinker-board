import ASUS.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

LED = 11

GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        print ("led on")
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        print ("led off")
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt: GPIO.cleanup()
