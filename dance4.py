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
lowLeft = servo.Servo(pwm1) #alternative name servo1
lowRight = servo.Servo(pwm2) #alternative name servo2
upperRight = servo.Servo(pwm3) #alternative name servo3
upperLeft = servo.Servo(pwm4) #alternative name servo4

timeout = time.time() + 60*5   # 5 minutes from now

def dance4():
    while True:
        for angle in range(70, 110, 20):  # 30 - 150 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            time.sleep(0.01)
            lowRight.angle = 180 - angle
            time.sleep(0.01)
            upperRight.angle = angle
            time.sleep(0.01)
            upperLeft.angle = 180 - angle
            time.sleep(0.01)
        for angle in range(110, 70, -20):  # 150 - 30 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            time.sleep(0.01)
            lowRight.angle = 180 - angle
            time.sleep(0.01)
            upperRight.angle = angle
            time.sleep(0.01)
            upperLeft.angle = 180 - angle
            time.sleep(0.01)

        for angle in range(70, 110, 20):  # 150 - 30 degrees, 5 degrees at a time.
            if angle % 90 == 0:
                lowLeft.angle = angle - 10
                lowRight.angle = 180 - angle + 10
                upperRight.angle = angle - 10
                upperLeft.angle = 180 - angle + 10
                time.sleep(0.1)

            lowLeft.angle = angle
            time.sleep(0.01)
            lowRight.angle = 180 - angle
            time.sleep(0.01)
            upperRight.angle = angle
            time.sleep(0.01)
            upperLeft.angle = 180 - angle
            time.sleep(0.01)

        for angle in range(110, 70, -20):  # 150 - 30 degrees, 5 degrees at a time.
            if angle % 90 == 0:
                lowLeft.angle = angle - 20
                lowRight.angle = 180 - angle + 20
                upperRight.angle = angle - 20
                upperLeft.angle = 180 - angle + 20
                time.sleep(0.1)

            lowLeft.angle = angle
            time.sleep(0.15)
            lowRight.angle = 180 - angle
            time.sleep(0.15)
            upperRight.angle = angle
            time.sleep(0.15)
            upperLeft.angle = 180 - angle
            time.sleep(0.15)


        if time.time() > timeout:
            print("BREAK")
            break

        """
        if some command break
        """
    #default position
    lowLeft.angle = 90
    lowRight.angle = 90
    upperLeft.angle = 90
    upperRight.angle = 90


dance4()


