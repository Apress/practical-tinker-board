#  Requires the Adafruit Motor HAT Python Library

import time
import Robot
import readchar

LEFT_TRIM = 0
RIGHT_TRIM = 0

robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

try:
    while True:
        key = readchar.readkey()
        
        if (key == 'w'):
            robot.forward(150)
            print("forward\n")
            time.sleep(0.1)
        elif (key == 'a'):
            robot.left(150)
            print("left\n")
            time.sleep(0.1)
        elif (key == 'd'):
            robot.right(150)
            print("right\n")
            time.sleep(0.1)
        elif (key == 'b'):
            robot.stop()
            print('brake!\n')
            time.sleep(0.1)
        elif (key == 's'):
            robot.backward(150)
            print("backwards\n")
            time.sleep(0.1)
        time.sleep(0.5)
except KeyboardInterrupt: GPIO.cleanup()
