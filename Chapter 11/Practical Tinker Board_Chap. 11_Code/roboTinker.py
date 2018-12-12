'''
The MIT License

Copyright <2018> <Liz Clark>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

#  Requires the Adafruit Motor HAT Python Library: https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library

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
