import time

def distance():
    gpio.output(24, True)           # Sensor on
    time.sleep(0.00001)             # Sleep for 10 microseconds
    gpio.output(24, False)          # Sensor off

    while gpio.input(23) == 0:      # If ECHO Pin low, record no-signal time
        nosig = time.time()

    while gpio.input(23) == 1:      # If ECHO Pin high, record signal time
        sig = time.time()

    timeleft = sig - nosig          # Find time difference
    speedSound = 331.5 + (0.6 * temperature)    # calculate speed of sound
    speedSound = speedSound * 100
    dist = (timeleft * speedSound) / 2          # calculate distance, divide by 2 since we go to and from destination

    if (dist < 8):
        lowLeft.angle = 90
        lowRight.angle = 90
        upLeft.angle = 90
        upRight.angle = 90
        distance()
        