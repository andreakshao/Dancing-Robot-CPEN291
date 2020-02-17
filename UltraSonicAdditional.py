import time
import board
import adafruit_hcsr04
#Change the pins
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D4, timeout = 1.0)
#Use this to check the distance
while True:
    try:
        print(sonar.distance)
    except RuntimeError:
        print("Retrying!")
    time.sleep(1.0)