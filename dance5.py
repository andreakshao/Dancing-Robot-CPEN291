#import statements
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

def dance5():
    # set position to forward facing
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    time.sleep(1) # sleep for 1 second
    while True:
        count = 0
        # this dance makes it shift backwards
        while count < 5:
            upRight.angle = 60 # set right knee angle
            upLeft.angle = 60 # set left knee angle
            time.sleep(0.2) # sleep for 0.2 secnods
            upLeft.angle = 120 # set left knee angle
            upRight.angle = 120 # set right knee angle
            time.sleep(0.2) # sleep for 0.2 secnods
            upRight.angle = 60 # set right knee angle
            upLeft.angle = 60 # set left knee angle
            time.sleep(0.2) # sleep for 0.2 secnods
            upRight.angle = 120 # set right knee angle
            upLeft.angle = 120 # set left knee angle
            time.sleep(0.2) # sleep for 0.2 secnods
            upRight.angle = 60 # set right knee angle
            upLeft.angle = 60 # set left knee angle
            time.sleep(0.2) # sleep for 0.2 seconds
            count += 1 # increase count by 1
            
            
dance5()