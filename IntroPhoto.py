import board
import displayio
import adafruit_imageload
from adafruit_st7735r import ST7735R

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.D11
tft_dc = board.D9

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7)

display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)
 
bitmap, palette = adafruit_imageload.load("/helloimbub" + (str(i+1)) + ".bmp",
                                         bitmap=displayio.Bitmap,
                                         palette=displayio.Palette)
 
# Create a TileGrid to hold the bitmap
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
 
# Create a Group to hold the TileGrid
group = displayio.Group()
 
# Add the TileGrid to the Group
group.append(tile_grid)
 
# Add the Group to the Display
display.show(group)
 
# Loop forever so you can enjoy your image
while True:
    pass