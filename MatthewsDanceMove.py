import time
import board
import pulseio
from adafruit import servo


# create a PWMOut object on Pin A2.
leftKneePwm = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)
rightKneePwm = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
leftFootPwm = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
rightFootPwm = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)
 
# Create a servo object, my_servo.
leftKnee = servo.Servo(leftKneePwm)
rightKnee = servo.Servo(rightKneePwm)
leftFoot = servo.Servo(leftFootPwm)
rightFoot = servo.Servo(rightFootPwm)
 

while True:
    for angle in range(70, 110, 20):  # 0 - 180 degrees, 5 degrees at a time.
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

    for angle in range(70, 110, -20):  # 0 - 180 degrees, 5 degrees at a time.
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
