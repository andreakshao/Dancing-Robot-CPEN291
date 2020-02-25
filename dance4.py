# import statements
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
lowLeft = servo.Servo(pwm1)
lowRight = servo.Servo(pwm2)
upRight = servo.Servo(pwm3)
upLeft = servo.Servo(pwm4)

def dance4():
    # set position to forward facing
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    time.sleep(1) # sleep for 1 second
    while True:
        for angle in range(70, 110, 20):  # 70 - 110 degrees, 20 degrees at a time.
            lowLeft.angle = angle # set left foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            lowRight.angle = 180 - angle # set right foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upRight.angle = angle # set right knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upLeft.angle = 180 - angle # set left knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
        for angle in range(110, 70, -20):  # 70 - 110 degrees, 20 degrees at a time.
            lowLeft.angle = angle # set left foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            lowRight.angle = 180 - angle # set right foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upRight.angle = angle # set right knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upLeft.angle = 180 - angle # set left knee angle
            time.sleep(0.1) # sleep for 0.1 seconds

        for angle in range(70, 110, 20):  # 70 - 110 degrees, 20 degrees at a time.
            if angle % 90 == 0:
                lowLeft.angle = angle - 10 # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                lowRight.angle = 180 - angle + 10 # set right foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                upRight.angle = angle - 10 # set right knee angle
                time.sleep(0.1) # sleep for 0.1 seconds
                upLeft.angle = 180 - angle + 10 # set left knee angle
                time.sleep(0.1) # sleep for 0.1 seconds

            lowLeft.angle = angle # set left foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            lowRight.angle = 180 - angle # set right foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upRight.angle = angle # set right knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upLeft.angle = 180 - angle # set left knee angle
            time.sleep(0.1) # sleep for 0.1 seconds

        for angle in range(110, 70, -20):  # 70 - 110 degrees, 20 degrees at a time.
            if angle % 90 == 0: # if the angle is a multiple of 90 run this chunk of code
                lowLeft.angle = angle - 20 # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                lowRight.angle = 180 - angle + 20 # set right foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                upRight.angle = angle - 20 # set right knee angle
                time.sleep(0.1) # sleep for 0.1 seconds
                upLeft.angle = 180 - angle + 20 # set left knee angle
                time.sleep(0.1) # sleep for 0.1 seconds

            lowLeft.angle = angle # set left foot angle
            time.sleep(0.15) # sleep for 0.15 seconds
            lowRight.angle = 180 - angle # set right foot angle
            time.sleep(0.15) # sleep for 0.15 seconds
            upRight.angle = angle # set right knee angle
            time.sleep(0.15) # sleep for 0.15 seconds
            upLeft.angle = 180 - angle # set left knee angle
            time.sleep(0.15) # sleep for 0.15 seconds


dance4()