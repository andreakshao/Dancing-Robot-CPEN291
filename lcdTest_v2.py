import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
import time
import board

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
    time.sleep(1)
