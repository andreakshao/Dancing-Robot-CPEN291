import board

import simpleio


# Define pin connected to piezo buzzer.
PIEZO_PIN = board.A1

# Define a list of tones/music notes to play.
c = 262  # C4
d = 294  # D4
e = 330  # E4
f = 349  # F4
g = 392  # G4
a = 440  # A4
b = 494  # B4
notes = [c, c, d, c, f, e]


# Main loop will go through each tone in order up and down.
while True:
    # Play tones going from start to end of list.
    for note in notes:
        simpleio.tone(PIEZO_PIN, note, duration=0.5)
