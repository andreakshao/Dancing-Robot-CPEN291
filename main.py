# adding import statements
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
import time
import pulseio
from adafruit_motor import servo
import simpleio
import adafruit_hcsr04

# create a PWMOut object on Pin A2.
# can change inputs board.A1 etc.
pwm1 = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)
pwm2 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
pwm3 = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
pwm4 = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
lowLeft = servo.Servo(pwm1) #alternative name servo1
lowRight = servo.Servo(pwm2) #alternative name servo2
upRight = servo.Servo(pwm3) #alternative name servo3
upLeft = servo.Servo(pwm4) #alternative name servo4

# setting up sonar to use pin out D3 and D4
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D4)

# Release any resources currently in use for the displays
displayio.release_displays()

# setting up LCD board
spi = board.SPI()
tft_cs = board.D11
tft_dc = board.D9
# setting up the LCD board so the code knows the size of the screen
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D7)
display = ST7735R(display_bus, width=128, height=128)

# Make the display context
splash = displayio.Group(max_size=20)
my_label = label.Label(terminalio.FONT, text="My Label Text", color=0xFFFFFF, x = 40, y = 40)
splash.append(my_label)
display.show(splash)

# setting up text to display on LCD
text = "Hello world"
text_area = label.Label(terminalio.FONT, text=text)
text_area.x = 30
text_area.y = 60
display.show(text_area)

# Define pin connected to piezo buzzer.
# creating a bunch of note varriables to help create the song
PIEZO_PIN = board.A1
NOTE_B0  =31
NOTE_C1  =33
NOTE_CS1 =35
NOTE_D1  =37
NOTE_DS1 =39
NOTE_E1  =41
NOTE_F1  =44
NOTE_FS1 =46
NOTE_G1  =49
NOTE_GS1 =52
NOTE_A1  =55
NOTE_AS1 =58
NOTE_B1  =62
NOTE_C2  =65
NOTE_CS2 =69
NOTE_D2  =73
NOTE_DS2 =78
NOTE_E2  =82
NOTE_F2  =87
NOTE_FS2 =93
NOTE_G2  =98
NOTE_GS2 =104
NOTE_A2  =110
NOTE_AS2 =117
NOTE_B2  =123
NOTE_C3  =131
NOTE_CS3 =139
NOTE_D3  =147
NOTE_DS3 =156
NOTE_E3  =165
NOTE_F3  =175
NOTE_FS3 =185
NOTE_G3  =196
NOTE_GS3 =208
NOTE_A3  =220
NOTE_AS3 =233
NOTE_B3  =247
NOTE_C4  =262
NOTE_CS4 =277
NOTE_D4  =294
NOTE_DS4 =311
NOTE_E4  =330
NOTE_F4  =349
NOTE_FS4 =370
NOTE_G4  =392
NOTE_GS4 =415
NOTE_A4  =440
NOTE_AS4 =466
NOTE_B4  =494
NOTE_C5  =523
NOTE_CS5 =554
NOTE_D5  =587
NOTE_DS5 =622
NOTE_E5  =659
NOTE_F5  =698
NOTE_FS5 =740
NOTE_G5  =784
NOTE_GS5 =831
NOTE_A5  =880
NOTE_AS5 =932
NOTE_B5  =988
NOTE_C6  =1047
NOTE_CS6 =1109
NOTE_D6  =1175
NOTE_DS6 =1245
NOTE_E6  =1319
NOTE_F6  =1397
NOTE_FS6 =1480
NOTE_G6  =1568
NOTE_GS6 =1661
NOTE_A6  =1760
NOTE_AS6 =1865
NOTE_B6  =1976
NOTE_C7  =2093
NOTE_CS7 =2217
NOTE_D7  =2349
NOTE_DS7 =2489
NOTE_E7  =2637
NOTE_F7  =2794
NOTE_FS7 =2960
NOTE_G7  =3136
NOTE_GS7 =3322
NOTE_A7  =3520
NOTE_AS7 =3729
NOTE_B7  =3951
NOTE_C8  =4186
NOTE_CS8 =4435
NOTE_D8  =4699
NOTE_DS8 =4978
# this allows us to set up how long each note plays for
wholeNote = 2
halfNote = 1
quarterNote = 0.5
eighthNote = 0.25
sixteenthNote = 0.125

# creating a list of notes 
notes = [NOTE_C4, NOTE_C4, NOTE_D4, NOTE_C4, NOTE_F4, NOTE_E4]
# this is a list for our song shootingStars this list of notes corresponds with the list of notes in the shooting Stars Beats
shootingStarsNotes = [
    NOTE_DS5, NOTE_DS5, 0, NOTE_E5, NOTE_B4, NOTE_GS4, NOTE_DS5,
    NOTE_DS5, NOTE_DS5, 0, NOTE_E5, NOTE_B4, NOTE_GS4, NOTE_DS5,
    NOTE_DS5, NOTE_DS5, 0, NOTE_E5, NOTE_B4, NOTE_GS4, NOTE_DS5,
    NOTE_DS5, NOTE_DS5, 0, NOTE_E5, NOTE_DS5, NOTE_B4, NOTE_GS4,
    NOTE_FS5, NOTE_FS5, NOTE_GS5, NOTE_DS5, NOTE_B4, NOTE_FS5,
    NOTE_FS5, NOTE_FS5, NOTE_GS5, NOTE_DS5, NOTE_B4, NOTE_FS5, 
    NOTE_FS5, NOTE_FS5, NOTE_GS5, NOTE_DS5, NOTE_B4, NOTE_FS5, 
    NOTE_FS5, NOTE_FS5, NOTE_DS5, NOTE_E5, NOTE_DS5, NOTE_B4, NOTE_GS4,
    NOTE_DS5, NOTE_DS5, 0, NOTE_E5, NOTE_B4, NOTE_GS4, NOTE_DS5,
    NOTE_DS5, NOTE_DS5, 0, NOTE_E5, NOTE_B4, NOTE_GS4, NOTE_DS5,
    NOTE_DS5, NOTE_DS5, 0, NOTE_E5, NOTE_B4, NOTE_GS4, NOTE_DS5,
    NOTE_DS5, NOTE_DS5, 0, NOTE_E5, NOTE_DS5, NOTE_B4, NOTE_GS4
    ]
# this is a list that has the length of each note above
shootingStarsBeats = [
    quarterNote+eighthNote, sixteenthNote, sixteenthNote, quarterNote, eighthNote, sixteenthNote, sixteenthNote, 
    quarterNote+eighthNote, sixteenthNote, sixteenthNote, quarterNote, eighthNote, sixteenthNote, sixteenthNote, 
    quarterNote+eighthNote, sixteenthNote, sixteenthNote, quarterNote, eighthNote, sixteenthNote, sixteenthNote,
    quarterNote+eighthNote, sixteenthNote, sixteenthNote, eighthNote, eighthNote, eighthNote, eighthNote,
    quarterNote+eighthNote, eighthNote, quarterNote, eighthNote, sixteenthNote, sixteenthNote,
    quarterNote+eighthNote, eighthNote, quarterNote, eighthNote, sixteenthNote, sixteenthNote,
    quarterNote+eighthNote, eighthNote, quarterNote, eighthNote, sixteenthNote, sixteenthNote,
    quarterNote+eighthNote, eighthNote, eighthNote, eighthNote, eighthNote, sixteenthNote, sixteenthNote,
    quarterNote+eighthNote, sixteenthNote, sixteenthNote, quarterNote, eighthNote, sixteenthNote, sixteenthNote,
    quarterNote+eighthNote, sixteenthNote, sixteenthNote, quarterNote, eighthNote, sixteenthNote, sixteenthNote,
    quarterNote+eighthNote, sixteenthNote, sixteenthNote, quarterNote, eighthNote, sixteenthNote, sixteenthNote,
    quarterNote+eighthNote, sixteenthNote, sixteenthNote, eighthNote, eighthNote, eighthNote, eighthNote
    ]
# a list of notes for mii
miiChannelNotes = [
    NOTE_FS5, NOTE_A5, NOTE_CS6, NOTE_A5, NOTE_FS5, 
    NOTE_D5, NOTE_D5, NOTE_D5, 0, NOTE_CS5,
    NOTE_D5, NOTE_FS5, NOTE_A5, NOTE_CS6, NOTE_A5, NOTE_FS5,
    NOTE_E6, NOTE_DS6, NOTE_D6, 0,
    NOTE_GS5, 0, NOTE_CS6, NOTE_FS5, 0, NOTE_CS6, 0, NOTE_GS5, 
    0, NOTE_CS6, 0, NOTE_A5, NOTE_FS5, 0, NOTE_E5, 0,
    NOTE_E5, NOTE_E5, NOTE_E5, 0, NOTE_E5, NOTE_E5,
    NOTE_E5, 0, NOTE_DS5, NOTE_D5, NOTE_CS5
]
# a list of beat length. Each time has a note that it matches in the list "miiChannelNotes"
miiChannelBeats = [
    quarterNote, eighthNote, quarterNote, quarterNote, eighthNote,
    eighthNote, eighthNote, eighthNote, halfNote, eighthNote,
    eighthNote, eighthNote, eighthNote, quarterNote, quarterNote, eighthNote, 
    quarterNote, eighthNote, eighthNote, quarterNote+eighthNote, 
    eighthNote, eighthNote, eighthNote, eighthNote, eighthNote, eighthNote, eighthNote, eighthNote,
    eighthNote, eighthNote, eighthNote, eighthNote, eighthNote, eighthNote, eighthNote, eighthNote,
    eighthNote, eighthNote, eighthNote, quarterNote+eighthNote, eighthNote, eighthNote,
    eighthNote, eighthNote+quarterNote, quarterNote, quarterNote
]

def miiProgram():
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    # this makes the robot face forward

    while 1:
        for index in range(0, len(miiChannelBeats), 1):
            simpleio.tone(PIEZO_PIN, miiChannelNotes[index], duration=(miiChannelBeats[index])/1.5) # play the miiChannel Song
            try:
                if (sonar.distance > 25):
                    return 0 # if the distance of the sonar is greater than 25cm stop playing the song
            except RuntimeError:
                print("Retrying!")
            time.sleep(0.1) # wait 0.1 seconds

def checkBuzzer():
    try:
        distance = sonar.distance # get the distance from the sonar
        # check if distance is less than 4cm
        if (distance < 4):
            miiProgram() # if the sonor distance is less than 4cm run the miiProgram
    except RuntimeError:
        print("Retrying!") # error message
        

index = 0
def dance1():
    global index # make sure the global varriable index can be accessed 
    index = 0 # this is the very first dance move. Set index to zero so restart the shooting star song

    # setting up text to display on LCD
    text = "Starting Dance1!"
    text_area = label.Label(terminalio.FONT, text=text)
    text_area.x = 30
    text_area.y = 60
    display.show(text_area)
    
    print("Dance 1") # print the word Dance 1
    lowLeft.angle = 90 # set angle of left foot
    lowRight.angle = 90 # set angle of right foot
    upLeft.angle = 90 # set angle of left knee
    upRight.angle = 90 # set angle of right foot
    for num in range(5):
        lowLeft.angle = 60 # set left foot
        # Because we only have one processor and we want to do two things at the same time we make it seem like it is threading
        # so we play the buzzer
        # the buzzer is given a note from the list shootingStarsNotes and its corresponding duration from shootingStarsBeats
        # both of these places are determined by the global varrialbe index which is increased by 1 after each note
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        lowLeft.angle = 120 # set left foot angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        lowLeft.angle = 60 # set left foot angle
    lowLeft.angle = 90 # set left foot angle
    for num in range(5):
        upLeft.angle = 60 # set left knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        upLeft.angle = 120 # set left knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        upLeft.angle = 60 # set left knee angle

    for num in range(5):
        lowRight.angle = 120 # set right foot angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        lowRight.angle = 60 # set right foot angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        lowRight.angle = 120 # set right foot angle
    lowRight.angle = 90 # set right foot angle
    for num in range(5):
        upRight.angle = 120 # set right knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        upRight.angle = 60 # set right knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        upRight.angle = 120 # set right knee angle


def dance2():
    global index # make sure the global varriable index can be accessed 
    if (index >= len(shootingStarsBeats) - 30):
        index = 0 # if index is greater than the shootingStar song restart the song
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    time.sleep(0.1) # sleep for 1 second
    
    count = 0
    while count < 2:
        # run this loop twice
        upLeft.angle = 130 # set left knee anlge
        upRight.angle = 50 # set right knee angle
        checkBuzzer()

        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        upLeft.angle = 50 # set left knee angle
        upRight.angle = 130 # set right knee angle
        checkBuzzer()

        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        lowLeft.angle = 110 # set left foot angle
        checkBuzzer()

        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        lowLeft.angle = 90 # set left foot angle
        lowRight.angle = 60 # set right foot angle
        checkBuzzer()

        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        lowRight.angle = 90 # set right foot angle
        lowLeft.angle = 110 # set left foot angle
        checkBuzzer()

        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        lowLeft.angle = 90 # set left foot angle
        lowRight.angle = 60 # set right foot angle
        checkBuzzer()

        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        lowRight.angle = 90 # set right foot angle
        lowLeft.angle = 110 # set left foot angle
        checkBuzzer()

        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        lowLeft.angle = 90 # set left foot angle
        lowRight.angle = 60 # set right foot angle
        checkBuzzer()

        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        lowRight.angle = 90 # set right foot angle
        count += 1 # increases count by 1

    # setting up text to display on LCD
    text = "Starting Dance 2!"
    text_area = label.Label(terminalio.FONT, text=text)
    text_area.x = 30
    text_area.y = 60
    display.show(text_area)
    
    print("Dance 2")

def dance3():
    global index # make sure the global varriable index can be accessed 
    if (index >= len(shootingStarsBeats) - 30):
        index = 0 # if index is greater than the shootingStar song restart the song

    # setting up text to display on LCD
    text = "Starting Dance 3!"
    text_area = label.Label(terminalio.FONT, text=text)
    text_area.x = 30
    text_area.y = 60
    display.show(text_area)
    
    print("Dance 3")
    lowLeft.angle = 90 # set left foot angle
    lowRight.angle = 90 # set right foot angle
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    time.sleep(0.1) # sleep for 0.1 seconds
    for num in range(60, 120, 20):
        if num % 40 == 0:
            # if num is a multiple of 40 do the following
            lowLeft.angle = num + 10 # set left foot angle
            lowRight.angle = num - 10 # set right foot angle
            # Because we only have one processor and we want to do two things at the same time we make it seem like it is threading
            # so we play the buzzer
            # the buzzer is given a note from the list shootingStarsNotes and its corresponding duration from shootingStarsBeats
            # both of these places are determined by the global varrialbe index which is increased by 1 after each note
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
            index = index + 1 # increase the index by 1
            checkBuzzer()

        lowLeft.angle = num # set left foot angle
        lowRight.angle = 180 - num # set right foot angle
        upLeft.angle = num # set left knee angle
        upRight.angle = 180 - num # set right knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()

    for num in range(120, 60, -20):
        upRight.angle = num # set right knee angle
        upLeft.angle = 180 - num # set left knee angle
        upLeft.angle = num # set left knee angle
        upRight.angle = 180 - num # set right knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        if num % 40 == 0:
            # if num is a multiple of 40 do the following
            upRight.angle = num - 10 # set right knee angle
            upLeft.angle = num + 10 # set left knee angle
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
            index = index + 1 # increase the index by 1
            checkBuzzer()

def dance4():
    global index # make sure the global varriable index can be accessed 
    if (index >= len(shootingStarsBeats) - 30):
        index = 0 # if index is greater than the shootingStar song restart the song

    # setting up text to display on LCD
    text = "Starting Dance4!"
    text_area = label.Label(terminalio.FONT, text=text)
    text_area.x = 30
    text_area.y = 60
    display.show(text_area)
    
    print("Dance 4")
    for angle in range(70, 110, 20):  # 30 - 150 degrees, 5 degrees at a time.
        lowLeft.angle = angle # set left foot angle
        # Because we only have one processor and we want to do two things at the same time we make it seem like it is threading
        # so we play the buzzer
        # the buzzer is given a note from the list shootingStarsNotes and its corresponding duration from shootingStarsBeats
        # both of these places are determined by the global varrialbe index which is increased by 1 after each note
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        lowRight.angle = 180 - angle # set right foot angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1
        upRight.angle = angle # set right knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        upLeft.angle = 180 - angle # set left knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1
    for angle in range(110, 70, -20):  # 150 - 30 degrees, 5 degrees at a time.
        lowLeft.angle = angle # set left foot angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        lowRight.angle = 180 - angle # set right foot angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1
        upRight.angle = angle # set right knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        upLeft.angle = 180 - angle # set left knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1

    for angle in range(70, 110, 20):  # 150 - 30 degrees, 5 degrees at a time.
        if angle % 90 == 0:
            # if the angle is a multiple of 90 do the following
            lowLeft.angle = angle - 10 # set left foot angle
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
            index = index + 1 # increase the index by 1
            checkBuzzer()
            lowRight.angle = 180 - angle + 10 # set right foot angle
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
            index = index + 1 # increase the index by 1
            upRight.angle = angle - 10 # set right knee angle
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
            index = index + 1 # increase the index by 1
            checkBuzzer()
            upLeft.angle = 180 - angle + 10 # set left knee angle
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
            index = index + 1 # increase the index by 1

        lowLeft.angle = angle # set left foot angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        lowRight.angle = 180 - angle # set right foot angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1
        upRight.angle = angle # set right knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        upLeft.angle = 180 - angle # set left knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])  # play the buzzer
        index = index + 1 # increase the index by 1

    for angle in range(110, 70, -20):  # 150 - 30 degrees, 5 degrees at a time.
        if angle % 90 == 0:
            # if angle is a multiple of 90 do the following
            lowLeft.angle = angle - 20 # set left foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            checkBuzzer()
            lowRight.angle = 180 - angle + 20 # set right foot angle
            time.sleep(0.1) # sleep for 0.1 seconds
            upRight.angle = angle - 20 # set right knee angle
            time.sleep(0.1) # sleep for 0.1 seconds
            checkBuzzer()
            upLeft.angle = 180 - angle + 20 # set left knee angle
            time.sleep(0.1) # sleep for 0.1 seconds

    lowLeft.angle = angle # set left foot angle
    simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
    index = index + 1 # increase the index by 1
    checkBuzzer()
    lowRight.angle = 180 - angle # set right foot angle
    simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
    index = index + 1 # increase the index by 1
    upRight.angle = angle # set right knee angle
    simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
    index = index + 1 # increase the index by 1
    checkBuzzer()
    upLeft.angle = 180 - angle # set left knee angle
    simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
    index = index + 1 # increase the index by 1

def dance5():
    global index # make sure the global varriable index can be accessed 
    if (index >= len(shootingStarsBeats) - 30):
        index = 0 # if index is greater than the shootingStar song restart the song

    # setting up text to display on LCD
    text = "Starting Dance5!"
    text_area = label.Label(terminalio.FONT, text=text)
    text_area.x = 30
    text_area.y = 60
    display.show(text_area)
    
    print("Dance 5")
    count = 0
    # this dance makes it shift backwards
    while count < 5:
        upRight.angle = 60 # set right knee angle
        upLeft.angle = 60 # set left knee angle
        checkBuzzer()
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        upLeft.angle = 120 # set left knee angle
        upRight.angle = 120 # set right knee angle
        checkBuzzer()
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        upRight.angle = 60 # set right knee angle
        upLeft.angle = 60 # set left knee angle
        checkBuzzer()
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        upRight.angle = 120 # set right knee angle
        upLeft.angle = 120 # set left knee angle
        checkBuzzer()
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        upRight.angle = 60 # set right knee angle
        upLeft.angle = 60 # set left knee angle
        checkBuzzer()
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        count += 1 # increase count by 1

def dance6():
    global index # make sure the global varriable index can be accessed 
    if (index >= len(shootingStarsBeats) - 30):
        index = 0 # if index is greater than the shootingStar song restart the song

    # setting up text to display on LCD
    text = "Starting Dance 6!"
    text_area = label.Label(terminalio.FONT, text=text)
    text_area.x = 30
    text_area.y = 60
    display.show(text_area)
    
    print("Dance 6")
    count = 0 # set count to 0
    while count < 3:
        # run this set of code 3 times
        lowLeft.angle = 90 # set left foot angle
        lowRight.angle = 90 # set right foot angle
        upLeft.angle = 90 # set left knee angle
        upRight.angle = 90 # set right knee angle
        for angle in range(60, 120, 10):  # 0 - 180 degrees, 5 degrees at a time.
            upLeft.angle = angle # set left knee angle
            upRight.angle = 180 - angle # set right knee angle
            # Because we only have one processor and we want to do two things at the same time we make it seem like it is threading
            # so we play the buzzer
            # the buzzer is given a note from the list shootingStarsNotes and its corresponding duration from shootingStarsBeats
            # both of these places are determined by the global varrialbe index which is increased by 1 after each note
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
            index = index + 1 # increase the index by 1
            checkBuzzer()
            if (angle == 90):
                lowRight.angle = 120 # set right foot angle
                lowLeft.angle = 60  # set left foot angle
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
                index = index + 1 # increase the index by 1
                lowRight.angle = 60 # set right foot angel
                lowLeft.angle = 120 # set left foot angle
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
                index = index + 1 # increase the index by 1
                checkBuzzer()
                lowRight.angle = 120 # set right foot angle
                lowLeft.angle = 60 # set left foot angle
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
                index = index + 1 # increase the index by 1

        for angle in range(60, 120, -10):  # 0 - 180 degrees, 5 degrees at a time.
            upLeft.angle = angle # set left knee angle
            upRight.angle = angle # set right knee angle
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
            index = index + 1 # increase the index by 1
            checkBuzzer()
            if (angle == 90):
                # run this code only if the angle is 90 degrees
                lowRight.angle = 120 # set right foot angle
                lowLeft.angle = 60 #set left foot angle
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
                index = index + 1 # increase the index by 1
                lowRight.angle = 60 # set right foot angle
                lowLeft.angle = 120 # set left foot angle
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
                index = index + 1 # increase the index by 1
                checkBuzzer()
                lowRight.angle = 120 # set right foot angle
                lowLeft.angle = 60 # set left foot angle
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
                index = index + 1 # increase the index by 1

        upLeft.angle = 90 # set left knee angle
        upRight.angle = 90 # set right knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the buzzer
        index = index + 1 # increase the index by 1
        checkBuzzer()
        count+=1 # increase the count by 1

lowLeft.angle = 90 # set left foot angle
lowRight.angle = 90 # set right foot angle
upLeft.angle = 90 # set left knee angle
upRight.angle = 90 # set right knee angle
time.sleep(1) # sleep for one second
while True:
    pass
    # this is our main function. It runs on a loop and has all our dances
    dance1() # dance 1
    dance2() # dance 2
    dance3() # dance 3
    dance4() # dance 4
    dance5() # dance 5
    dance6() # dance 6
    time.sleep(0.5)
    # do the splits
    upLeft.angle = 90 # set left knee angle
    upRight.angle = 90 # set right knee angle
    lowLeft.angle = 160 # set left foot angle
    lowRight.angle = 20 # set right foot angle
    time.sleep(5) # wait 5 seconds to restart the dance