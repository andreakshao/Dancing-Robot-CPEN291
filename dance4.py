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
lowLeft = servo.Servo(pwm1) #alternative name servo1
lowRight = servo.Servo(pwm2) #alternative name servo2
upperRight = servo.Servo(pwm3) #alternative name servo3
upperLeft = servo.Servo(pwm4) #alternative name servo4

timeout = time.time() + 60*5   # 5 minutes from now

def dance4():
    while True:
        for angle in range(60, 120, 5):  # 30 - 150 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            time.sleep(0.05)
            lowRight.angle = 180 - angle
            time.sleep(0.05)
            upperRight.angle = angle
            time.sleep(0.05)
            upperLeft.angle = 180 - angle
            time.sleep(0.05)
        for angle in range(120, 60, -5):  # 150 - 30 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            time.sleep(0.05)
            lowRight.angle = 180 - angle
            time.sleep(0.05)
            upperRight.angle = angle
            time.sleep(0.05)
            upperLeft.angle = 180 - angle
            time.sleep(0.05)

        for angle in range(60, 120, 5):  # 150 - 30 degrees, 5 degrees at a time.
            if angle % 10 == 0:
                lowLeft.angle = angle - 10
                time.sleep(0.02)
                lowRight.angle = 180 - angle + 10
                time.sleep(0.02)
                upperRight.angle = angle - 10
                time.sleep(0.02)
                upperLeft.angle = 180 - angle + 10
                time.sleep(0.02)

            lowLeft.angle = angle
            time.sleep(0.05)
            lowRight.angle = 180 - angle
            time.sleep(0.05)
            upperRight.angle = angle
            time.sleep(0.05)
            upperLeft.angle = 180 - angle
            time.sleep(0.05)

        for angle in range(120, 60, -5):  # 150 - 30 degrees, 5 degrees at a time.
            if angle % 10 == 0:
                lowLeft.angle = angle - 20
                time.sleep(0.10)
                lowRight.angle = 180 - angle + 20
                time.sleep(0.10)
                upperRight.angle = angle - 20
                time.sleep(0.10)
                upperLeft.angle = 180 - angle + 20
                time.sleep(0.10)

            lowLeft.angle = angle
            time.sleep(0.15)
            lowRight.angle = 180 - angle
            time.sleep(0.15)
            upperRight.angle = angle
            time.sleep(0.15)
            upperLeft.angle = 180 - angle
            time.sleep(0.15)


        if time.time() > timeout:
            break


dance4()


