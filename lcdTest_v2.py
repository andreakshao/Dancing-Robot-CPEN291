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
tft_cs = board.D11
tft_dc = board.D9

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7)

display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)


# Make the display context
splash = displayio.Group(max_size=20)

my_label = label.Label(terminalio.FONT, text="My Label Text", color=0x000000, x = 40, y = 40)
splash.append(my_label)

display.show(splash)

while True:
    pass
'''
    sleep(1)
    for f in notes:
        piezo.frequency = f
        piezo.duty_cycle = ON
        sleep(0.3)
        piezo.duty_cycle = OFF
        sleep(0.3)
'''