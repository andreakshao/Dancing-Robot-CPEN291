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

timeout = time.time() + 60*5   # 5 minutes from now

def dance5():
    while True:
            lowRight.angle = 60
            time.sleep(0.2)
            lowRight.angle = 120
            time.sleep(0.2)
            lowRight.angle = 60
            time.sleep(0.2)
            lowRight.angle = 120
            time.sleep(0.2)
            lowRight.angle = 90
            
            lowLeft.angle = 60
            time.sleep(0.2)
            lowLeft.angle = 120
            time.sleep(0.2)
            lowLeft.angle = 60
            time.sleep(0.2)
            lowLeft.angle = 120
            time.sleep(0.2)
            lowLeft.angle = 90
            
            
dance5()