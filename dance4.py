import time
import board
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm1 = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency = 50)
pwm2 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
pwm3 = pulseio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency = 50)
pwm4 = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
lowLeft = servo.Servo(pwm1)
lowRight = servo.Servo(pwm2)
upperRight = servo.Servo(pwm3)
upperLeft = servo.Servo(pwm4)