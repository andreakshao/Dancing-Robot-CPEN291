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
upRight = servo.Servo(pwm3) #alternative name servo3
upLeft = servo.Servo(pwm4) #alternative name servo4

def dance1():
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

def dance2():
    for num in range(5):
        lowLeft.angle = 60
        time.sleep(0.15)
        lowLeft.angle = 120
        time.sleep(0.15)
        lowLeft.angle = 60
    lowLeft.angle = 90
    for num in range(5):
        upLeft.angle = 60
        time.sleep(0.1)
        upLeft.angle = 120
        time.sleep(0.1)
        upLeft.angle = 60

    for num in range(5):
        lowRight.angle = 120
        time.sleep(0.15)
        lowRight.angle = 60
        time.sleep(0.15)
        lowRight.angle = 120
    lowRight.angle = 90
    for num in range(5):
        upRight.angle = 120
        time.sleep(0.1)
        upRight.angle = 60
        time.sleep(0.1)
        upRight.angle = 120

def dance3():
    lowLeft.angle = 90
    lowRight.angle = 90
    upLeft.angle = 90
    upRight.angle = 90
    for num in range(60, 120, 20):
        if num % 40 == 0:
            lowLeft.angle = num + 20
            lowRight.angle = num - 20
            time.sleep(0.05)

        lowLeft.angle = num
        lowRight.angle = 180 - num
        upLeft.angle = num
        upRight.angle = 180 - num
        time.sleep(0.1)

    for num in range(120, 60, -20):
        upRight.angle = num
        upLeft.angle = 180 - num
        upLeft.angle = num
        upRight.angle = 180 - num
        time.sleep(0.05)
        if num % 40:
            upRight.angle = num - 20
            upLeft.angle = num
            time.sleep(0.1)

def dance4():
    for angle in range(70, 110, 20):  # 30 - 150 degrees, 5 degrees at a time.
        lowLeft.angle = angle
        time.sleep(0.1)
        lowRight.angle = 180 - angle
        time.sleep(0.1)
        upRight.angle = angle
        time.sleep(0.1)
        upLeft.angle = 180 - angle
        time.sleep(0.1)
    for angle in range(110, 70, -20):  # 150 - 30 degrees, 5 degrees at a time.
        lowLeft.angle = angle
        time.sleep(0.1)
        lowRight.angle = 180 - angle
        time.sleep(0.1)
        upRight.angle = angle
        time.sleep(0.1)
        upLeft.angle = 180 - angle
        time.sleep(0.1)

    for angle in range(70, 110, 20):  # 150 - 30 degrees, 5 degrees at a time.
        if angle % 90 == 0:
            lowLeft.angle = angle - 10
            time.sleep(0.1)
            lowRight.angle = 180 - angle + 10
            time.sleep(0.1)
            upRight.angle = angle - 10
            time.sleep(0.1)
            upLeft.angle = 180 - angle + 10
            time.sleep(0.1)

        lowLeft.angle = angle
        time.sleep(0.1)
        lowRight.angle = 180 - angle
        time.sleep(0.1)
        upRight.angle = angle
        time.sleep(0.1)
        upLeft.angle = 180 - angle
        time.sleep(0.1)

    for angle in range(110, 70, -20):  # 150 - 30 degrees, 5 degrees at a time.
        if angle % 90 == 0:
            lowLeft.angle = angle - 20
            time.sleep(0.1)
            lowRight.angle = 180 - angle + 20
            time.sleep(0.1)
            upRight.angle = angle - 20
            time.sleep(0.1)
            upLeft.angle = 180 - angle + 20
            time.sleep(0.1)

    lowLeft.angle = angle
    time.sleep(0.15)
    lowRight.angle = 180 - angle
    time.sleep(0.15)
    upRight.angle = angle
    time.sleep(0.15)
    upLeft.angle = 180 - angle
    time.sleep(0.15)

def dance5():
    lowRight.angle = 60
    time.sleep(0.2)
    lowRight.angle = 120
    time.sleep(0.2)
    lowRight.angle = 60
    time.sleep(0.2)
    lowRight.angle = 120
    time.sleep(0.2)
    lowRight.angle = 90
            
    lowLeft.angle = 60
    time.sleep(0.2)
    lowLeft.angle = 120
    time.sleep(0.2)
    lowLeft.angle = 60
    time.sleep(0.2)
    lowLeft.angle = 120
    time.sleep(0.2)
    lowLeft.angle = 90

def dance6():
    for angle in range(60, 120, 10):  # 0 - 180 degrees, 5 degrees at a time.
        upLeft.angle = angle
        upRight.angle = 180 - angle
        time.sleep(0.1)
        if (angle == 90):
            lowRight.angle = 130
            lowLeft.angle = 50 
            time.sleep(0.1)
            lowRight.angle = 50
            lowLeft.angle = 130
            time.sleep(0.1)
            lowRight.angle = 130
            lowLeft.angle = 50
            time.sleep(0.1)

    for angle in range(60, 120, -10):  # 0 - 180 degrees, 5 degrees at a time.
        upLeft.angle = angle
        upRight.angle = angle
        time.sleep(0.1)
        if (angle == 90):
            lowRight.angle = 130
            lowLeft.angle = 50 
            time.sleep(0.1)
            lowRight.angle = 50
            lowLeft.angle = 130
            time.sleep(0.1)
            lowRight.angle = 130
            lowLeft.angle = 50
            time.sleep(0.1)

    upLeft.angle = 90
    upRight.angle = 90
    time.sleep(0.1)

while true:
    dance1()
    dance2()
    dance3()
    dance4()
    dance5()
    dance6()