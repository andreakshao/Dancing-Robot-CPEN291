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

display = ST7735R(display_bus, width=128, height=128)


# Make the display context
splash = displayio.Group(max_size=20)

my_label = label.Label(terminalio.FONT, text="My Label Text", color=0xFFFFFF, x = 40, y = 40)
splash.append(my_label)

display.show(splash)

text1 = "DANCE 1"
text2 = "DANCE 2"
text3 = "DANCE 3"
text4 = "DANCE 4"
text5 = "DANCE 5"
text6 = "DANCE 6"
text_area = label.Label(terminalio.FONT, text=text1)
text_area.x = 10
text_area.y = 10
display.show(text_area)

#What might this do?
text_area = label.Label(terminalio.FONT, text=text2)
text_area.x = 10
text_area.y = 10
display.show(text_area)

while True:
    pass
    time.sleep(1)


# POOL OF NAMES:
# THE TIPPY-TAP
# TIP TAP TOE
# SCREWDRIVER
# SHAKER
# WICKED LIMBS
# TORNADO
# PHANTOM WALKER
# ATTITIUDE TURNS
# THE OCTOPUS
# ALL THAT JAZZ
# DANSATION
# DANSPIRATION
# FEET OF WONDER
# FEET OF FIRE
# STEPPIN' OUT
