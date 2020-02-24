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

def dance7():
    # set position to forward facing
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    time.sleep(1) # sleep for 1 second
    while True:
        # lift left foot, move right foot, lower left foot
        lowLeft.angle = 120 # set left foot angle
        time.sleep(0.2) # sleep for 0.2 seconds
        lowRight.angle = 80 # set right foot angle
        time.sleep(0.2) # sleep for 0.2 seconds
        upRight.angle = 50 # set right knee angle
        time.sleep(0.2) # sleep for 0.2 seconds
        lowLeft.angle = 90 # set left foot angle
        time.sleep(0.2) # sleep for 0.2 seconds

        # lift right foot, reset right knee, move left foot, lower right foot 
        lowRight.angle = 120 # set right foot angle
        time.sleep(0.2) # sleep for 0.2 seconds
        lowLeft.angle = 80 # set left foot angle
        time.sleep(0.2) # sleep for 0.2 seconds
        upRight.angle = 90 # set right knee angle
        time.sleep(0.2) # sleep for 0.2 seconds
        upLeft.angle = 50 # set left knee angle
        time.sleep(0.2) # sleep for 0.2 seconds
        lowRight.angle = 90 # set right foot angle
        time.sleep(0.2) # sleep for 0.2 seconds
dance7()