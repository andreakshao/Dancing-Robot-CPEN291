from time import sleep
import board
import pulseio

# For the M4 boards:
piezo = pulseio.PWMOut(board.A1, duty_cycle=0, frequency=440, variable_frequency=True)
 
while True:
    for f in (262, 294, 330, 349, 392, 440, 494, 523):
        piezo.frequency = f
        piezo.duty_cycle = 65536 // 2  # On 50%
        time.sleep(0.25)  # On for 1/4 second
        piezo.duty_cycle = 0  # Off
        time.sleep(0.05)  # Pause between notes
    time.sleep(0.5)



#Experimental Code to test making different notes
ON = 2**15
OFF = 0
c = 262
d = 294
e = 330
f = 349
notes = [c, c, d, c, f, e]
while True:
    for f in notes:
        piezo.frequency = f
        piezo.duty_cycle = ON
        time.sleep(0.2)
        piezo.duty_cycle = OFF
        time.sleep(0.2)

