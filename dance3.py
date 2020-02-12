import time
import board
import pulseio
from adafruit_motor import servo

pwm1 = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency = 50)
pwm2 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency = 50)
pwm3 = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency = 50)
pwm4 = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=  50)

lowLeft = servo.Servo(pwm1)
lowRight = servo.Servo(pwm2)
upperRight = servo.Servo(pwm3)
upperLeft = servo.Servo(pwm4)

def dance3():
    lowLeft.angle = 60
    lowRight.angle = 120
    upperRight.angle = 120
    upperLeft.angle = 60

    upperLeft.angle = 120
    lowLeft.angle = 120
    time.sleep(0.1)
    lowLeft.angle = 60
    time.sleep(0.5)
    upperLeft.angle = 60

    

