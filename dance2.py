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
lowLeft = servo.Servo(pwm1)
lowRight = servo.Servo(pwm2)
upRight = servo.Servo(pwm3)
upLeft = servo.Servo(pwm4)

def dance2():
    # set position to forward facing
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    time.sleep(1) # sleep for 1 second
    while True:
        count = 0
        while count < 2:
            # run this loop twice
            upLeft.angle = 130 # set left knee anlge
            upRight.angle = 50 # set right knee angle
            time.sleep(0.5) # sleep for 0.5 seconds
            upLeft.angle = 50 # set left knee angle
            upRight.angle = 130 # set right knee angle
            time.sleep(0.5) # sleep for 0.5 seconds
            lowLeft.angle = 110 # set left foot angle
            time.sleep(0.5) # sleep for 0.5 seconds
            lowLeft.angle = 90 # set left foot angle
            lowRight.angle = 60 # set right foot angle
            time.sleep(0.5) # sleep for 0.5 seconds
            lowRight.angle = 90 # set right foot angle
            lowLeft.angle = 110 # set left foot angle
            time.sleep(0.5) # sleep for 0.5 seconds
            lowLeft.angle = 90 # set left foot angle
            lowRight.angle = 60 # set right foot angle
            time.sleep(0.5) # sleep for 0.5 seconds
            lowRight.angle = 90 # set right foot angle
            lowLeft.angle = 110 # set left foot angle
            time.sleep(0.5) # sleep for 0.5 seconds
            lowLeft.angle = 90 # set left foot angle
            lowRight.angle = 60 # set right foot angle
            time.sleep(0.5) # sleep for 0.5 seconds
            lowRight.angle = 90 # set right foot angle
            count += 1 # increases count by 1
dance2()