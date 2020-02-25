# import statements
import time
import board
import pulseio
from adafruit_motor import servo

# pwm deceleration
pwm1 = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency = 50)
pwm2 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency = 50)
pwm3 = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency = 50)
pwm4 = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=  50)

# servo motor decleration
lowLeft = servo.Servo(pwm1)
lowRight = servo.Servo(pwm2)
upRight = servo.Servo(pwm3)
upLeft = servo.Servo(pwm4)

def dance3():
    # set position to forward facing
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    time.sleep(1) # sleep for 1 second
    while True:
        for num in range(60, 120, 20): # 60 - 120 degrees, 20 degrees at a time.
            if num % 40 == 0:
                # if num is a multiple of 40 run these lines
                lowLeft.angle = num + 20 # set left foot angle
                lowRight.angle = num - 20 # set right foot angle
                time.sleep(0.05) # sleep for 0.05 seconds

            lowLeft.angle = num # set left foot angle
            lowRight.angle = 180 - num # set right foot angle
            upLeft.angle = num # set left knee angle
            upRight.angle = 180 - num # set right knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
            lowLeft.angle = 90
            lowRight.angle = 90

        for num in range(120, 60, -20): # 60 - 120 degrees, 20 degrees at a time.
            upRight.angle = num # set right knee angle
            upLeft.angle = 180 - num # set left knee angle
            upLeft.angle = num # set left knee angle
            upRight.angle = 180 - num # set right knee angle
            time.sleep(0.05) # sleep for 0.05 seconds
            if num % 40:
                # if num is a multiple of 40 run these 3 lines
                upRight.angle = num - 20 # set right knee angle
                upLeft.angle = num # set left knee angle
                time.sleep(0.1) # sleep for 0.1 seconds

dance3()