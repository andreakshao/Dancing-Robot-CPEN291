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
low_left_servo = servo.Servo(pwm1) #alternative name servo1
low_right_servo = servo.Servo(pwm2) #alternative name servo2
up_left_servo = servo.Servo(pwm3) #alternative name servo3
up_right_servo = servo.Servo(pwm4) #alternative name servo4

timeout = time.time() + 60*5   # 5 minutes from now

def danceTest_1():
    while True:
        for angle in range(60, 120, 5):  # 30 - 150 degrees, 5 degrees at a time.
            low_left_servo.angle = angle
            time.sleep(0.05)
            low_right_servo.angle = 180 - angle
            time.sleep(0.05)
        for angle in range(120, 60, -5):  # 150 - 30 degrees, 5 degrees at a time.
            low_left_servo.angle = angle
            time.sleep(0.05)
            low_right_servo.angle = 180 - angle
            time.sleep(0.05)
        for angle in range(60, 120, 5):  # 30 - 150 degrees, 5 degrees at a time.
            up_left_servo.angle = angle
            time.sleep(0.05)
            up_right_servo.angle = 180 - angle
            time.sleep(0.05)
        for angle in range(120, 60, -5):  # 150 - 30 degrees, 5 degrees at a time.
            up_left_servo.angle = angle
            time.sleep(0.05)
            up_right_servo.angle = 180 - angle
            time.sleep(0.05)

        # for angle in range(60, 120, 5):
        #     low_left_servo.angle = angle
        #     low_right_servo.angle = 180 - angle
        #     up_left_servo.angle = angle
        #     up_right_servo.angle = 180 - angle
        #     time.sleep(0.05)
        # for angle in range(120, 60, -5):
        #     low_left_servo.angle = angle
        #     low_right_servo.angle = 180 - angle
        #     up_left_servo.angle = angle
        #     up_right_servo.angle = 180 - angle
        #     time.sleep(0.05)

        if time.time() > timeout:
            break


danceTest_1()

