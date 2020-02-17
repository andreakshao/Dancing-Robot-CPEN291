import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

from time import sleep
import board

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.D11
tft_dc = board.D9

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7)

display = ST7735R(display_bus, width=128, height=128)


# Make the display context
splash = displayio.Group(max_size=20)

my_label = label.Label(terminalio.FONT, text="My Label Text", color=0xFFFFFF, x = 40, y = 40)
splash.append(my_label)

display.show(splash)

text = "Hello world"
text_area = label.Label(terminalio.FONT, text=text)
text_area.x = 10
text_area.y = 10
board.DISPLAY.show(text_area)

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