import time
import board
import pulseio
from adafruit_motor import servo


# create a PWMOut object on Pin A2.
pwm1 = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)
pwm2 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
pwm3 = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
pwm4 = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.

lowLeft = servo.Servo(pwm1)
lowRight = servo.Servo(pwm2)
upRight = servo.Servo(pwm3)
upLeft = servo.Servo(pwm4)

def dance6():
    lowLeft.angle = 90
    lowRight.angle = 90
    upLeft.angle = 90
    upRight.angle = 90
    time.sleep(1)
    while True:
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
    
dance6()
