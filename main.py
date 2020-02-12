"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""
'''
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

from time import sleep
import board
import pulseio

# For the M4 boards:
piezo = pulseio.PWMOut(board.A1, duty_cycle=0, frequency=440, variable_frequency=True)
 
#Experimental Code to test making different notes
ON = (2**15)
OFF = 0
c = 262
d = 294
e = 330
f = 349
notes = [c, c, d, c, f, e]

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.D10
tft_dc = board.D9

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7)

display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)

# Make the display context
splash = displayio.Group(max_size=20)
display.show(splash)

color_bitmap = displayio.Bitmap(128, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00 # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(108, 108, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088 # Purple
inner_sprite = displayio.TileGrid(inner_bitmap,
                                  pixel_shader=inner_palette,
                                  x=10, y=10)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=10, y=10)
splash.append(text_area)

while True:
    pass
    sleep(1)
    for f in notes:
        piezo.frequency = f
        piezo.duty_cycle = ON
        sleep(0.3)
        piezo.duty_cycle = OFF
        sleep(0.3)'''
        
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

def dance4():
    while True:
        for angle in range(60, 120, 5):  # 30 - 150 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            time.sleep(0.01)
            lowRight.angle = 180 - angle
            time.sleep(0.01)
            upperRight.angle = angle
            time.sleep(0.01)
            upperLeft.angle = 180 - angle
            time.sleep(0.01)
        for angle in range(120, 60, -5):  # 150 - 30 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            time.sleep(0.01)
            lowRight.angle = 180 - angle
            time.sleep(0.01)
            upperRight.angle = angle
            time.sleep(0.01)
            upperLeft.angle = 180 - angle
            time.sleep(0.01)

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
            time.sleep(0.01)
            lowRight.angle = 180 - angle
            time.sleep(0.01)
            upperRight.angle = angle
            time.sleep(0.01)
            upperLeft.angle = 180 - angle
            time.sleep(0.01)

        for angle in range(120, 60, -5):  # 150 - 30 degrees, 5 degrees at a time.
            if angle % 10 == 0:
                lowLeft.angle = angle - 20
                time.sleep(0.01)
                lowRight.angle = 180 - angle + 20
                time.sleep(0.01)
                upperRight.angle = angle - 20
                time.sleep(0.01)
                upperLeft.angle = 180 - angle + 20
                time.sleep(0.01)

            lowLeft.angle = angle
            time.sleep(0.15)
            lowRight.angle = 180 - angle
            time.sleep(0.15)
            upperRight.angle = angle
            time.sleep(0.15)
            upperLeft.angle = 180 - angle
            time.sleep(0.15)

        """
        if some command break
        """
    #default position
    lowLeft.angle = 90
    lowRight.angle = 90
    upperLeft.angle = 90
    upperRight.angle = 90


dance4()