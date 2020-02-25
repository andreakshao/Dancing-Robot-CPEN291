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
upLeft = servo.Servo(pwm3)
upRight = servo.Servo(pwm4)

def dance10():
    # set position to forward facing
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    time.sleep(1) # sleep for 1 second
    while True:
        upLeft.angle = 130
        upRight.angle = 50
        time.sleep(2)
        upLeft.angle = 50
        upRight.angle = 130
        time.sleep(2)
        lowLeft.angle = 110
        time.sleep(2)
        lowLeft.angle = 90

        upLeft.angle = 130
        upRight.angle = 50
        time.sleep(2)
        upLeft.angle = 50
        upRight.angle = 130
        time.sleep(2)
        lowRight.angle = 110
        time.sleep(2)
        lowRight.angle = 90
            
dance10()



