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

timeout = time.time() + 60*5   # 5 minutes from now

def dance3():
    lowLeft.angle = 90
    lowRight.angle = 90
    upperLeft.angle = 90
    upperRight.angle = 90

    while True:
        for num in range(60, 120, 20):
            if num % 40 == 0:
                lowLeft.angle = num + 20
                lowRight.angle = num - 20
                time.sleep(0.05)

            lowLeft.angle = num
            lowRight.angle = 180 - num
            upperLeft.angle = num
            upperRight.angle = 180 - num
            time.sleep(0.1)

        for num in range(120, 60, -20):
            upperRight.angle = num
            upperLeft.angle = 180 - num
            upperLeft.angle = num
            upperRight.angle = 180 - num
            time.sleep(0.05)
            if num % 40:
                upperRight.angle = num - 20
                upperLeft.angle = num
                time.sleep(0.1)

        if time.time() > timeout:
            lowLeft.angle = 90
            lowRight.angle = 90
            upperLeft.angle = 90
            upperRight.angle = 90
            print("TIMED OUT")
            break

def moveBackDance():
    lowLeft.angle = 90
    lowRight.angle = 90
    upperLeft.angle = 90
    upperRight.angle = 90
    while True:

        lowLeft.angle = 90
        lowRight.angle = 90
        upperLeft.angle = 90
        upperRight.angle = 90
        time.sleep(0.2)
        upperLeft.angle = 110
        upperRight.angle = 70
        time.sleep(0.05)
        lowLeft.angle = 110
        lowRight.angle = 70
        time.sleep(0.1)

        if time.time() > timeout:
            lowLeft.angle = 90
            lowRight.angle = 90
            upperLeft.angle = 90
            upperRight.angle = 90
            print("TIMED OUT")
            break


def moveForwardDance():
    return

dance3()

    

