import ASUS.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

photoPin = 11

def sensorData():
    readPin = 0
    GPIO.setup(photoPin, GPIO.OUT)
    GPIO.output(photoPin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(photoPin, GPIO.IN)

    while (GPIO.input(photoPin) == GPIO.LOW):
        readPin += 1
    return readPin

try:
    while True:
        print sensorData()
except KeyboardInterrupt: GPIO.cleanup()
