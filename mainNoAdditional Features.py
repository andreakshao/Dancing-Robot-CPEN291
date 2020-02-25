# adding import statements
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
import time
import pulseio
from adafruit_motor import servo
import simpleio
import adafruit_hcsr04

# create a PWMOut object on Pin A2.
# can change inputs board.A1 etc.
pwm1 = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)
pwm2 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
pwm3 = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
pwm4 = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
lowLeft = servo.Servo(pwm1) #alternative name servo1
lowRight = servo.Servo(pwm2) #alternative name servo2
upRight = servo.Servo(pwm3) #alternative name servo3
upLeft = servo.Servo(pwm4) #alternative name servo4

# setting up sonar to use pin out D3 and D4
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D4)

# Release any resources currently in use for the displays
displayio.release_displays()

# setting up LCD board
spi = board.SPI()
tft_cs = board.D11
tft_dc = board.D9
# setting up the LCD board so the code knows the size of the screen
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7)
display = ST7735R(display_bus, width=128, height=128)

# Make the display context
splash = displayio.Group(max_size=20)
my_label = label.Label(terminalio.FONT, text="My Label Text", color=0xFFFFFF, x = 40, y = 40)
splash.append(my_label)
display.show(splash)

# setting up text to display on LCD
text = "Hello world"
text_area = label.Label(terminalio.FONT, text=text)
text_area.x = 30
text_area.y = 60
display.show(text_area)

def dance1():
    lowLeft.angle = 90 # set angle of left foot
    lowRight.angle = 90 # set angle of right foot
    upLeft.angle = 90 # set angle of left knee
    upRight.angle = 90 # set angle of right foot
    for num in range(5):
        lowLeft.angle = 60 # set left foot
        time.sleep(0.15) # sleep for 0.15 seconds
        lowLeft.angle = 120 # set left foot angle
        time.sleep(0.15) # sleep for 0.15 seconds
        lowLeft.angle = 60 # set left foot angle
    lowLeft.angle = 90 # set left foot angle
    for num in range(5):
        upLeft.angle = 60 # set left knee angle
        time.sleep(0.15) # sleep for 0.15 seconds
        upLeft.angle = 120 # set left knee angle
        time.sleep(0.15) # sleep for 0.15 seconds
        upLeft.angle = 60 # set left knee angle

    for num in range(5):
        lowRight.angle = 120 # set right foot angle
        time.sleep(0.15) # sleep for 0.15 seconds
        lowRight.angle = 60 # set right foot angle
        time.sleep(0.15) # sleep for 0.15 seconds
        lowRight.angle = 120 # set right foot angle
    lowRight.angle = 90 # set right foot angle
    for num in range(5):
        upRight.angle = 120 # set right knee angle
        time.sleep(0.15) # sleep for 0.15 seconds
        upRight.angle = 60 # set right knee angle
        time.sleep(0.15) # sleep for 0.15 seconds
        upRight.angle = 120 # set right knee angle

def dance2():
    count = 0 # set count to zero
    while count < 2:
        # run this loop twice
        upLeft.angle = 130 # set left knee anlge
        upRight.angle = 50 # set right knee angle
        time.sleep(0.5) # sleep for 0.5 seconds
        upLeft.angle = 50 # set left knee angle
        upRight.angle = 130 # set right knee angle
        time.sleep(0.5) # sleep for 0.5 seconds
        lowLeft.angle = 110 # set left foot angle
        time.sleep(0.5) # sleep for 0.5 seconds
        lowLeft.angle = 90 # set left foot angle
        lowRight.angle = 60 # set right foot angle
        time.sleep(0.5) # sleep for 0.5 seconds
        lowRight.angle = 90 # set right foot angle
        lowLeft.angle = 110 # set left foot angle
        time.sleep(0.5) # sleep for 0.5 seconds
        lowLeft.angle = 90 # set left foot angle
        lowRight.angle = 60 # set right foot angle
        time.sleep(0.5) # sleep for 0.5 seconds
        lowRight.angle = 90 # set right foot angle
        lowLeft.angle = 110 # set left foot angle
        time.sleep(0.5) # sleep for 0.5 seconds
        lowLeft.angle = 90 # set left foot angle
        lowRight.angle = 60 # set right foot angle
        time.sleep(0.5) # sleep for 0.5 seconds
        lowRight.angle = 90 # set right foot angle
        count += 1 # increases count by 1

def dance3():
    count = 0 # set count to zero
    lowLeft.angle = 90 # set angle of left foot
    lowRight.angle = 90 # set angle of right foot
    upLeft.angle = 90 # set angle of left knee
    upRight.angle = 90 # set angle of right foot
    time.sleep(0.1) # sleep for 0.1 seconds
    while count < 5: # run this set of moves 10 times
        for num in range(60, 120, 20):
            if num % 40 == 0:
                # if num is a multiple of 40 do the following
                lowLeft.angle = num + 10 # set left foot angle
                lowRight.angle = num - 10 # set right foot angle
                time.sleep(0.2) # sleep for 0.1 seconds
            lowLeft.angle = num # set left foot angle
            lowRight.angle = 180 - num # set right foot angle
            upLeft.angle = num # set left knee angle
            upRight.angle = 180 - num # set right knee angle
            time.sleep(0.2) # sleep for 0.2 seconds
            lowLeft.angle = 90 # set left foot angle
            lowRight.angle = 90 # set right foot angle

        for num in range(120, 60, -20):
            upRight.angle = num # set right knee angle
            upLeft.angle = 180 - num # set left knee angle
            upLeft.angle = num # set left knee angle
            upRight.angle = 180 - num # set right knee angle
            time.sleep(0.2) # sleep for 0.2 seconds
            if num % 40:
                # if num is a multiple of 40 do the following
                upRight.angle = num - 10 # set right knee angle
                upLeft.angle = num + 10 # set left knee angle
                time.sleep(0.2) # sleep for 0.2 seconds
        count += 1 # increase count by 1

def dance4():
    for angle in range(70, 110, 20):  # 30 - 150 degrees, 5 degrees at a time.
        lowLeft.angle = angle # set left foot angle
        time.sleep(0.1) # sleep for 0.1 seconds
        lowRight.angle = 180 - angle # set right foot angle
        time.sleep(0.1) # sleep for 0.1 seconds
        upRight.angle = angle # set right knee angle
        time.sleep(0.1) # sleep for 0.1 seconds
        upLeft.angle = 180 - angle # set left knee angle
        time.sleep(0.1) # sleep for 0.1 seconds
    for angle in range(110, 70, -20):  # 150 - 30 degrees, 5 degrees at a time.
        lowLeft.angle = angle # set left foot angle
        time.sleep(0.1) # sleep for 0.1 seconds
        lowRight.angle = 180 - angle # set right foot angle
        time.sleep(0.1) # sleep for 0.1 seconds
        upRight.angle = angle # set right knee angle
        time.sleep(0.1) # sleep for 0.1 seconds
        upLeft.angle = 180 - angle # set left knee angle
        time.sleep(0.1) # sleep for 0.1 seconds
    for angle in range(70, 110, 20):  # 150 - 30 degrees, 5 degrees at a time.
        if angle % 90 == 0:
            # if the angle is a multiple of 90 do the following
            lowLeft.angle = angle - 10 # set left foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            lowRight.angle = 180 - angle + 10 # set right foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upRight.angle = angle - 10 # set right knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upLeft.angle = 180 - angle + 10 # set left knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
        lowLeft.angle = angle # set left foot angle
        time.sleep(0.1) # sleep for 0.1 seconds
        lowRight.angle = 180 - angle # set right foot angle
        time.sleep(0.1) # sleep for 0.1 seconds
        upRight.angle = angle # set right knee angle
        time.sleep(0.1) # sleep for 0.1 seconds
        upLeft.angle = 180 - angle # set left knee angle
        time.sleep(0.1) # sleep for 0.1 seconds

    for angle in range(110, 70, -20):  # 150 - 30 degrees, 5 degrees at a time.
        if angle % 90 == 0:
            # if angle is a multiple of 90 do the following
            lowLeft.angle = angle - 20 # set left foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            lowRight.angle = 180 - angle + 20 # set right foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upRight.angle = angle - 20 # set right knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upLeft.angle = 180 - angle + 20 # set left knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
    lowLeft.angle = angle # set left foot angle
    time.sleep(0.15) # sleep for 0.15 seconds
    lowRight.angle = 180 - angle # set right foot angle
    time.sleep(0.15) # sleep for 0.15 seconds
    upRight.angle = angle # set right knee angle
    time.sleep(0.15) # sleep for 0.15 seconds
    upLeft.angle = 180 - angle # set left knee angle
    time.sleep(0.15) # sleep for 0.15 seconds

def dance5():
    count = 0 # set count equal to zero
    # this dance makes it shift backwards
    while count < 5:
        upRight.angle = 60 # set right knee angle
        upLeft.angle = 60 # set left knee angle
        time.sleep(0.2) # sleep for 0.2 secnods
        upLeft.angle = 120 # set left knee angle
        upRight.angle = 120 # set right knee angle
        time.sleep(0.2) # sleep for 0.2 secnods
        upRight.angle = 60 # set right knee angle
        upLeft.angle = 60 # set left knee angle
        time.sleep(0.2) # sleep for 0.2 secnods
        upRight.angle = 120 # set right knee angle
        upLeft.angle = 120 # set left knee angle
        time.sleep(0.2) # sleep for 0.2 secnods
        upRight.angle = 60 # set right knee angle
        upLeft.angle = 60 # set left knee angle
        time.sleep(0.2) # sleep for 0.2 seconds
        count += 1 # increase count by 1

def dance6():
    count = 0 # set count to 0
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    while count < 3:
        # run this set of code 3 times
        for angle in range(60, 120, 10):  # 0 - 180 degrees, 5 degrees at a time.
            upLeft.angle = angle # set left knee angle
            upRight.angle = 180 - angle # set right knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
            if (angle == 90):
                lowRight.angle = 120 # set right foot angle
                lowLeft.angle = 60  # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                lowRight.angle = 60 # set right foot angel
                lowLeft.angle = 120 # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                lowRight.angle = 120 # set right foot angle
                lowLeft.angle = 60 # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds

        for angle in range(60, 120, -10):  # 0 - 180 degrees, 5 degrees at a time.
            upLeft.angle = angle # set left knee angle
            upRight.angle = angle # set right knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
            if (angle == 90):
                # run this code only if the angle is 90 degrees
                lowRight.angle = 120 # set right foot angle
                lowLeft.angle = 60 #set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                lowRight.angle = 60 # set right foot angle
                lowLeft.angle = 120 # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds
                lowRight.angle = 120 # set right foot angle
                lowLeft.angle = 60 # set left foot angle
                time.sleep(0.1) # sleep for 0.1 seconds

        upLeft.angle = 90 # set left knee angle
        upRight.angle = 90 # set right knee angle
        time.sleep(0.1) # sleep for 0.1 seconds
        count+=1 # increase the count by 1

lowLeft.angle = 90 # set left foot angle
lowRight.angle = 90 # set right foot angle
upLeft.angle = 90 # set left knee angle
upRight.angle = 90 # set right knee angle
time.sleep(1) # sleep for one second
while True:
    pass
    # this is our main function. It runs on a loop and has all our dances
    dance1() # dance 1
    time.sleep(1) # wait one second inbetween each dance move
    dance2() # dance 2
    time.sleep(1) # wait one second inbetween each dance move
    dance3() # dance 3
    time.sleep(1) # wait one second inbetween each dance move
    dance4() # dance 4
    time.sleep(1) # wait one second inbetween each dance move
    dance5() # dance 5
    time.sleep(1) # wait one second inbetween each dance move
    dance6() # dance 6
    time.sleep(1) # wait one second inbetween each dance move
    #do the splits
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    lowLeft.angle = 160 # set left foot angle
    lowRight.angle = 20 # set right foot angle
    time.sleep(5) # wait 5 seconds to restart the dance