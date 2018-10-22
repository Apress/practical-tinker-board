import ASUS.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

LED = 11
button = 13

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

try:
    while True:
        if GPIO.input(button) == False:
            GPIO.output(LED, True)
            print("pressed")
            time.sleep(.1)
        else:
            GPIO.output(LED, False)
            print("off")
            time.sleep(.1)
except KeyboardInterrupt: GPIO.cleanup()
