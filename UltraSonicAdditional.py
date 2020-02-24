# import statements
import time
import board
import adafruit_hcsr04
#Change the pins
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D4, timeout = 1.0) # set pins for sonar
#Use this to check the distance
while True:
    try:
        print(sonar.distance) # print the distance read for sonar
    except RuntimeError:
        print("Retrying!") # if there is an error print error message
    time.sleep(1.0) # sleep for 1 second