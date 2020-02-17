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

timeout = time.time() + 60*5   # 5 minutes from now

def dance7():
    # center the feet and knees
    lowLeft.angle = 90
    lowRight.angle = 90
    upLeft.angle = 90
    upRight.angle = 90
    while True:
        # lift left foot, move right foot, lower left foot
        lowLeft.angle = 120
        time.sleep(0.2)
        lowRight.angle = 80
        time.sleep(0.2)
        upRight.angle = 50
        time.sleep(0.2)
        lowLeft.angle = 90
        time.sleep(0.2)

        # lift right foot, reset right knee, move left foot, lower right foot 
        lowRight.angle = 120
        time.sleep(0.2)
        lowLeft.angle = 80
        time.sleep(0.2)
        upRight.angle = 90
        time.sleep(0.2)
        upLeft.angle = 50
        time.sleep(0.2)
        lowRight.angle = 90
        time.sleep(0.2)
dance7()