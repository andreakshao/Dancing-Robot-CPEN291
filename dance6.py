#import statements
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
    # set position to forward facing
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    time.sleep(1) # sleep for 1 second
    while True:
        for angle in range(60, 120, 10):  # 60 - 120 degrees, 1 degrees at a time.
            upLeft.angle = angle # left knee angle
            upRight.angle = 180 - angle # set right knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
            if (angle == 90):
                lowRight.angle = 130 # set right foot angle
                lowLeft.angle = 50  # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                lowRight.angle = 50 # set right foot angle
                lowLeft.angle = 130 # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                lowRight.angle = 130 # set right foot angle
                lowLeft.angle = 50 # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds

        for angle in range(60, 120, -10): # 60 - 120 degrees, 1 degrees at a time.
            upLeft.angle = angle # set left knee angle
            upRight.angle = angle # set right knee angle
            time.sleep(0.1)
            if (angle == 90):
                lowRight.angle = 130 # set right foot angle
                lowLeft.angle = 50 #set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                lowRight.angle = 50 # set right foot angle
                lowLeft.angle = 130 # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                lowRight.angle = 130 # set right foot angle
                lowLeft.angle = 50 # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
    
dance6()
