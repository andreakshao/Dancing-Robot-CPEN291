#Note: TODO Needs to be tested.
import time
import board
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
upLeft = servo.Servo(pwm3) #alternative name servo3
upRight = servo.Servo(pwm4) #alternative name servo4

timeout = time.time() + 60*5   # 5 minutes from now

def dance1():
    lowLeft.angle = 90
    lowRight.angle = 90
    upLeft.angle = 90
    upRight.angle = 90
    time.sleep(1)
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

dance1()


