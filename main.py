import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
import time
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
# can change inputs board.A1 etc.
pwm1 = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)
pwm2 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
pwm3 = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
pwm4 = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
lowLeft = servo.Servo(pwm1) #alternative name servo1
lowRight = servo.Servo(pwm2) #alternative name servo2
upperRight = servo.Servo(pwm3) #alternative name servo3
upperLeft = servo.Servo(pwm4) #alternative name servo4

def dance1():
    while True:
        for angle in range(60, 120, 20):  # 30 - 150 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            time.sleep(0.1)
            lowRight.angle = 180 - angle
            time.sleep(0.1)
        for angle in range(120, 60, -20):  # 150 - 30 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            time.sleep(0.1)
            lowRight.angle = 180 - angle
            time.sleep(0.1)
        for angle in range(60, 120, 20):  # 30 - 150 degrees, 5 degrees at a time.
            upLeft.angle = angle
            time.sleep(0.1)
            upRight.angle = 180 - angle
            time.sleep(0.1)
        for angle in range(120, 60, -20):  # 150 - 30 degrees, 5 degrees at a time.
            upLeft.angle = angle
            time.sleep(0.05)
            upRight.angle = 180 - angle
            time.sleep(0.05)

        for angle in range(60, 120, 5):
            lowLeft.angle = angle
            lowRight.angle = 180 - angle
            upLeft.angle = angle
            upRight.angle = 180 - angle
            time.sleep(0.05)
         for angle in range(120, 60, -5):
            lowLeft.angle = angle
            lowRight.angle = 180 - angle
            upLeft.angle = angle
            upRight.angle = 180 - angle
            time.sleep(0.05)

        if time.time() > timeout:
            break

def dance2():
    while True:
        for num in range(10):
            lowLeft.angle = 60
            lowRight.angle = 60
            lowLeft.angle = 120
            lowRight.angle = 120

        for num in range(15):
            upperRight.angle = 50
            upperLeft.angle = 130
            upperLeft.angle = 50
            upperRight.angle = 130

        if time.time() > timeout:
            break

def dance3():
    lowLeft.angle = 90
    lowRight.angle = 90
    upperLeft.angle = 90
    upperRight.angle = 90

    while True:
        for num in range(60, 120, 20):
            if num % 40 == 0:
                lowLeft.angle = num + 20
                lowRight.angle = num - 20
                time.sleep(0.05)

            lowLeft.angle = num
            lowRight.angle = 180 - num
            upperLeft.angle = num
            upperRight.angle = 180 - num
            time.sleep(0.1)

        for num in range(120, 60, -20):
            upperRight.angle = num
            upperLeft.angle = 180 - num
            upperLeft.angle = num
            upperRight.angle = 180 - num
            time.sleep(0.05)
            if num % 40:
                upperRight.angle = num - 20
                upperLeft.angle = num
                time.sleep(0.1)

        if time.time() > timeout:
            lowLeft.angle = 90
            lowRight.angle = 90
            lowLeft.angle = 90
            lowRight.angle = 90
            print("TIMED OUT")
            break

def dance4():
    while True:
        for angle in range(60, 120, 5):  # 30 - 150 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            time.sleep(0.01)
            lowRight.angle = 180 - angle
            time.sleep(0.01)
            upperRight.angle = angle
            time.sleep(0.01)
            upperLeft.angle = 180 - angle
            time.sleep(0.01)
        for angle in range(120, 60, -5):  # 150 - 30 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            time.sleep(0.01)
            lowRight.angle = 180 - angle
            time.sleep(0.01)
            upperRight.angle = angle
            time.sleep(0.01)
            upperLeft.angle = 180 - angle
            time.sleep(0.01)

        for angle in range(60, 120, 5):  # 150 - 30 degrees, 5 degrees at a time.
            if angle % 10 == 0:
                lowLeft.angle = angle - 10
                time.sleep(0.02)
                lowRight.angle = 180 - angle + 10
                time.sleep(0.02)
                upperRight.angle = angle - 10
                time.sleep(0.02)
                upperLeft.angle = 180 - angle + 10
                time.sleep(0.02)

            lowLeft.angle = angle
            time.sleep(0.01)
            lowRight.angle = 180 - angle
            time.sleep(0.01)
            upperRight.angle = angle
            time.sleep(0.01)
            upperLeft.angle = 180 - angle
            time.sleep(0.01)

        for angle in range(120, 60, -5):  # 150 - 30 degrees, 5 degrees at a time.
            if angle % 10 == 0:
                lowLeft.angle = angle - 20
                time.sleep(0.01)
                lowRight.angle = 180 - angle + 20
                time.sleep(0.01)
                upperRight.angle = angle - 20
                time.sleep(0.01)
                upperLeft.angle = 180 - angle + 20
                time.sleep(0.01)

            lowLeft.angle = angle
            time.sleep(0.15)
            lowRight.angle = 180 - angle
            time.sleep(0.15)
            upperRight.angle = angle
            time.sleep(0.15)
            upperLeft.angle = 180 - angle
            time.sleep(0.15)

        """
        if some command break
        """
    #default position
    lowLeft.angle = 90
    lowRight.angle = 90
    upperLeft.angle = 90
    upperRight.angle = 90

def dance6():
    while True:
        for angle in range(60, 120, 20):  # 0 - 180 degrees, 5 degrees at a time.
            leftKnee.angle = angle
            rightKnee.angle = 180 - angle
            time.sleep(0.1)
            if (angle == 90):
                rightFoot.angle = 130
                leftFoot.angle = 50 
                time.sleep(0.1)
                rightFoot.angle = 50
                leftFoot.angle = 130
                time.sleep(0.1)
                rightFoot.angle = 130
                leftFoot.angle = 50
                time.sleep(0.1)

        for angle in range(60, 120, -20):  # 0 - 180 degrees, 5 degrees at a time.
            leftKnee.angle = angle
            rightKnee.angle = angle
            time.sleep(0.1)
            if (angle == 90):
                rightFoot.angle = 130
                leftFoot.angle = 50 
                time.sleep(0.1)
                rightFoot.angle = 50
                leftFoot.angle = 130
                time.sleep(0.1)
                rightFoot.angle = 130
                leftFoot.angle = 50
                time.sleep(0.1)

    leftKnee.angle = 90
    rightKnee.angle = 90
    time.sleep(0.1)


dance1()
dance2()
dance3()
dance4()
dance5()
dance6()