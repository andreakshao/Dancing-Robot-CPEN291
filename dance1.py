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
        for num in range(5):
            lowLeft.angle = 60 # set left foot
            time.sleep(0.15) # sleep for 0.15 seconds
            lowLeft.angle = 120 # set left foot angle
            time.sleep(0.15) # sleep for 0.15 seconds
            lowLeft.angle = 60 # set left foot angle
        lowLeft.angle = 90 # set left foot angle
        for num in range(5):
            upLeft.angle = 60 # set left knee angle
            time.sleep(0.15) # sleep for 0.15 seconds
            upLeft.angle = 120 # set left knee angle
            time.sleep(0.15) # sleep for 0.15 seconds
            upLeft.angle = 60 # set left knee angle

        for num in range(5):
            lowRight.angle = 120 # set right foot angle
            time.sleep(0.15) # sleep for 0.15 seconds
            lowRight.angle = 60 # set right foot angle
            time.sleep(0.15) # sleep for 0.15 seconds
            lowRight.angle = 120 # set right foot angle
        lowRight.angle = 90 # set right foot angle
        for num in range(5):
            upRight.angle = 120 # set right knee angle
            time.sleep(0.15) # sleep for 0.15 seconds
            upRight.angle = 60 # set right knee angle
            time.sleep(0.15) # sleep for 0.15 seconds
            upRight.angle = 120 # set right knee angle
dance1()


