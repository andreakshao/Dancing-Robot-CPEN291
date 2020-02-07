#Note: TODO Needs to be tested.
import time
import board
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm1 = pulseio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
pwm2 = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
pwm3 = pulseio.PWMOut(board.A3, duty_cycle=2 ** 15, frequency=50)
pwm4 = pulseio.PWMOut(board.A4, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
low_left_servo = servo.Servo(pwm1) #alternative name servo1
low_right_servo = servo.Servo(pwm2) #alternative name servo2
up_left_servo = servo.Servo(pwm3) #alternative name servo3
up_right_servo = servo.Servo(pwm4) #alternative name servo4

while True:
    for angle in range(30, 180, 5):  # 30 - 150 degrees, 5 degrees at a time.
        low_left_servo.angle = angle
        low_right_servo.angle = angle - 180
        time.sleep(0.05)
    for angle in range(180, 0, -5):  # 150 - 30 degrees, 5 degrees at a time.
        low_left_servo.angle = angle
        low_right_servo.angle = angle - 180
        time.sleep(0.05)
