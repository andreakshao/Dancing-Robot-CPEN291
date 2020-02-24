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
    # set position to forward facing
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    time.sleep(1) # sleep for 1 second
    while True:
        for angle in range(60, 120, 20):  # 60 - 120 degrees, 20 degrees at a time.
            lowLeft.angle = angle # set left foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            lowRight.angle = 180 - angle # set right foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
        for angle in range(120, 60, -20):  # 120 - 60 degrees, 20 degrees at a time.
            lowLeft.angle = angle # set left foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            lowRight.angle = 180 - angle # set right foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
        for angle in range(60, 120, 20):  # 60 - 120 degrees, 20 degrees at a time.
            upLeft.angle = angle # set left knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upRight.angle = 180 - angle # set right knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
        for angle in range(120, 60, -20):  # 120 - 60 degrees, 20 degrees at a time.
            upLeft.angle = angle # set left knee angle
            time.sleep(0.05) # sleep for 0.05 seconds
            upRight.angle = 180 - angle # set right knee angle
            time.sleep(0.05) # sleep for 0.05 seconds
        for angle in range(60, 120, 5): # 60 - 120 degrees, 5 degrees at a time.
            lowLeft.angle = angle # set left foot angle
            lowRight.angle = 180 - angle # set right foot angle
            upLeft.angle = angle # set left knee angle
            upRight.angle = 180 - angle # set right knee angle
            time.sleep(0.05) # sleep for 0.05 seconds
        for angle in range(120, 60, -5):# 120 - 60 degrees, 5 degrees at a time.
            lowLeft.angle = angle # set left foot angle
            lowRight.angle = 180 - angle # set right foot angle
            upLeft.angle = angle # set left knee angle
            upRight.angle = 180 - angle # set right knee angle
            time.sleep(0.05) # sleep for 0.05 seconds

dance1()


