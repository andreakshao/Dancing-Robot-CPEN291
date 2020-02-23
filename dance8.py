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

def dance8():
    lowLeft.angle = 90
    lowRight.angle = 90
    while True:
        upRight.angle = 60
        upLeft.angle = 60
        time.sleep(0.2)
        upLeft.angle = 120
        upRight.angle = 120
        time.sleep(0.6)
        upRight.angle = 60
        upLeft.angle = 60
        time.sleep(0.2)
        upRight.angle = 120
        upLeft.angle = 120
        time.sleep(0.2)
        upRight.angle = 60
        upLeft.angle = 60
        
dance8()