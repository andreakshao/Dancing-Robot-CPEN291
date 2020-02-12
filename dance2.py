#Note: TODO Needs to be tested.
import time
import board
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
# can change inputs board.A1 etc.
pwm1 = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)
pwm2 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
pwm3 = pulseio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)
pwm4 = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
lowLeft = servo.Servo(pwm1)
lowRight = servo.Servo(pwm2)
upperRight = servo.Servo(pwm3)
upperLeft = servo.Servo(pwm4)

timeout = time.time() + 60*5   # 5 minutes from now

def dance2():
    while True:
        for num in range(10):
            lowLeft.angle = 60
            lowRight.angle = 60
            lowLeft.angle = 120
            lowRight.angle = 120

        for num in range(15):
            upperRight.angle = 50
            upperLeft.angle = 130
            upperLeft.angle = 50
            upperRight.angle = 130

        if time.time() > timeout:
            break

dance2()