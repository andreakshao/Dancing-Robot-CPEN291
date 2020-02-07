import time
import board
import pulseio
from adafruit import servo


# create a PWMOut object on Pin A2.
leftKneePwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
rightKneePwm = pulseio.PWMOut(board.__, duty_cycle=2 ** 15, frequency=50)
leftFootPwm = pulseio.PWMOut(board.__, duty_cycle=2 ** 15, frequency=50)
rightFootPwm = pulseio.PWMOut(board.__, duty_cycle=2 ** 15, frequency=50)
 
# Create a servo object, my_servo.
leftKnee = servo.Servo(leftKneePwm)
rightKnee = servo.Servo(rightKneePwm)
leftFoot = servo.Servo(leftFootPwm)
rightFoot = servo.Servo(rightFootPwm)
 

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        leftKnee.angle = angle
        rightKnee.angle = angle
        time.sleep(0.05)
        if (angle == 90):
            rightFoot.angle = 180
            leftFoot.angle = 180
            time.sleep(0.05)
            rightFoot.angle = 0
            leftFoot.angle = 0
            time.sleep(0.05)
            rightFoot.angle = 90
            leftFoot.angle = 90
        time.sleep(0.05)

    for angle in range(180, 5, -5):  # 0 - 180 degrees, 5 degrees at a time.
        leftKnee.angle = angle
        rightKnee.angle = angle
        time.sleep(0.05)
        if (angle == 90):
            rightFoot.angle = 180
            leftFoot.angle = 180
            time.sleep(0.05)
            rightFoot.angle = 0
            leftFoot.angle = 0
            time.sleep(0.05)
            rightFoot.angle = 90
            leftFoot.angle = 90
        time.sleep(0.05)

    left
    for count in range(0, 19, 1):


        