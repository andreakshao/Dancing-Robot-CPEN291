import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
from time import sleep


# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.D11
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
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=50, y=50)
splash.append(text_area)

while True:
    sleep(1)



"""
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

text = "Hello world"
text_area = label.Label(terminalio.FONT, text=text)
text_area.x = 30
text_area.y = 60
display.show(text_area)

while True:
    pass
    time.sleep(1)