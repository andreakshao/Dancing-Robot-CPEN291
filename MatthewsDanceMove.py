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
    for angle in range(60, 120, 5):  # 0 - 180 degrees, 5 degrees at a time.
        leftKnee.angle = angle
        rightKnee.angle = 180 - angle
        time.sleep(0.05)
        if (angle == 90):
            rightFoot.angle = 120
            leftFoot.angle = 60 
            time.sleep(0.05)
            rightFoot.angle = 60
            leftFoot.angle = 120
            time.sleep(0.05)
            rightFoot.angle = 120
            leftFoot.angle = 60
        time.sleep(0.05)

    for angle in range(120, 60, -5):  # 0 - 180 degrees, 5 degrees at a time.
        leftKnee.angle = angle
        rightKnee.angle = angle
        time.sleep(0.05)
        if (angle == 90):
            rightFoot.angle = 120
            leftFoot.angle = 60 
            time.sleep(0.05)
            rightFoot.angle = 60
            leftFoot.angle = 120
            time.sleep(0.05)
            rightFoot.angle = 120
            leftFoot.angle = 60
        time.sleep(0.05)

    leftKnee.angle = 90
    rightKnee.angle = 90
    time.sleep(0.10)
