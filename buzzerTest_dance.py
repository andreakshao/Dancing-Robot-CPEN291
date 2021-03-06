# adding import statements
import simpleio
import time
import board
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm1 = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency = 50)
pwm2 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency = 50)
pwm3 = pulseio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency = 50)
pwm4 = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=  50)
# Create a servo object, my_servo.
lowLeft = servo.Servo(pwm1) #alternative name servo1
lowRight = servo.Servo(pwm2) #alternative name servo2
upRight = servo.Servo(pwm3) #alternative name servo3
upLeft = servo.Servo(pwm4) #alternative name servo4

# Define pin connected to piezo buzzer.
PIEZO_PIN = board.A1
# define a series of notes
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

timeout = time.time() + 10   # 30 seconds each minutes from now

index = 0

def new_dance1():
    global index # a global varriable to access the position of the notes for the buzzer

    while index < len(shootingStarsBeats):
        lowLeft.angle = 90 # set left foot angle
        lowRight.angle = 90 # set right foot angle
        upperLeft.angle = 90 # set left knee angle
        upperRight.angle = 90 # set right knee angle
        #first part of dance
        lowLeft.angle = 120 # set left foot angle
        lowRight.angle = 60 # set right foot angle
        # Because we only have one processor and we want to do two things at the same time we make it seem like it is threading
        # so we play the buzzer
        # the buzzer is given a note from the list shootingStarsNotes and its corresponding duration from shootingStarsBeats
        # both of these places are determined by the global varrialbe index which is increased by 1 after each note
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the note
        index = index + 1 # increase the index
        if index == len(shootingStarsBeats):
            # if index is equal to length of song restart the song
            index = 0 # set index to zero

        lowLeft.angle = 60 # set left foot angle
        lowRight.angle = 120 # set right foot angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the note
        index = index + 1 # increase the index
        if index == len(shootingStarsBeats):
            # if index is equal to length of song restart the song
            index = 0 # set index to zero

        lowLeft.angle = 90 # set left foot angle
        lowRight.angle = 90 # set right foot angle
        upperLeft.angle = 120 # set left knee angle
        upperRight.angle = 60 # set right knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the note
        index = index + 1 # increase the index
        if index == len(shootingStarsBeats):
            # if index is equal to length of song restart the song
            index = 0 # set index to zero

        upperLeft.angle = 60 # set left knee angle
        upperRight.angle = 120 # set right knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the note
        index = index + 1 # increase the index
        if index == len(shootingStarsBeats):
            # if index is equal to length of song restart the song
            index = 0 # set index to zero

        if time.time() > timeout: #or other conditions, example (if distance read)
            # this helped with testing to stop the program after a certain time
            # these four lines make the robot face forward
            lowLeft.angle = 90 # set left foot angle
            lowRight.angle = 90 # set right foot angle
            upperLeft.angle = 90 # set left knee angle
            upperRight.angle = 90 # set right knee angle
            break #return

def new_dance2():
    global index

    while index < len(shootingStarsBeats):
        lowLeft.angle = 90 # set left foot angle
        lowRight.angle = 90 # set right foot angle
        upperLeft.angle = 90 # set left knee angle
        upperRight.angle = 90 # set right knee angle

        #first part of dance
        lowLeft.angle = 100 # set left foot angle
        upperLeft.angle = 120 # set left knee angle
        # Because we only have one processor and we want to do two things at the same time we make it seem like it is threading
        # so we play the buzzer
        # the buzzer is given a note from the list shootingStarsNotes and its corresponding duration from shootingStarsBeats
        # both of these places are determined by the global varrialbe index which is increased by 1 after each note
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the note
        index = index + 1 # increase the index
        if index == len(shootingStarsBeats):
            # if index is equal to length of song restart the song
            index = 0 # set index to zero

        lowLeft.angle = 80 # set left foot angle
        upperLeft.angle = 60 # set left knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the note
        index = index + 1  # increase the index
        if index == len(shootingStarsBeats):
            # if index is equal to length of song restart the song
            index = 0 # set index to zero


        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the note
        index = index + 1 # increase the index
        if index == len(shootingStarsBeats):
            # if index is equal to length of song restart the song
            index = 0 # set index to zero

        lowLeft.angle = 90 # set left foot angle
        upperLeft.angle = 90 # set left knee angle
        lowRight.angle = 100 # set right foot angle
        upperRight.angle = 120 # set right knee anlge
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the note
        index = index + 1 # increase the index
        if index == len(shootingStarsBeats):
            # if index is equal to length of song restart the song
            index = 0 # set index to zero

        lowRight.angle = 80 # set right foot angle
        upperRight.angle = 60 # set right knee angle
        simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index]) # play the note
        index = index + 1 # increase the index
        if index == len(shootingStarsBeats):
            # if index is equal to length of song restart the song
            index = 0 # set index to zero

        if time.time() > timeout: #or other conditions, example (if distance read)
            # this helped with testing to stop the program after a certain time
            # these four lines make the robot face forward
            lowLeft.angle = 90 # set left foot angle
            lowRight.angle = 90 # set right foot angle
            upperLeft.angle = 90 # set left knee angle
            upperRight.angle = 90 # set right knee angle
            break #or return

new_dance1() # this starts dance one
timeout = time.time() + 30
new_dance2() # this starts dance two



"""
def dance4():
    global index
    while True:
        for angle in range(70, 110, 20):  # 30 - 150 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            lowRight.angle = 180 - angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            upperRight.angle = angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            upperLeft.angle = 180 - angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
        for angle in range(110, 70, -20):  # 150 - 30 degrees, 5 degrees at a time.
            lowLeft.angle = angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            lowRight.angle = 180 - angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            upperRight.angle = angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            upperLeft.angle = 180 - angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])

        if time.time() > timeout:
            print("BREAK")
            return


        #if some command break

    #default position
    lowLeft.angle = 90
    lowRight.angle = 90
    upperLeft.angle = 90
    upperRight.angle = 90

def dance5():
    global index
    while True:
        for angle in range(70, 110, 20):  # 150 - 30 degrees, 5 degrees at a time.
            if angle % 90 == 0:
                lowLeft.angle = angle - 10
                index = index + 1
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
                lowRight.angle = 180 - angle + 10
                index = index + 1
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
                upperRight.angle = angle - 10
                index = index + 1
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
                upperLeft.angle = 180 - angle + 10
                index = index + 1
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])

            lowLeft.angle = angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            lowRight.angle = 180 - angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            upperRight.angle = angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            upperLeft.angle = 180 - angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])

            if time.time() > timeout:
                print("BREAK")
                return

        for angle in range(110, 70, -20):  # 150 - 30 degrees, 5 degrees at a time.
            if angle % 90 == 0:
                lowLeft.angle = angle - 20
                index = index + 1
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
                lowRight.angle = 180 - angle + 20
                index = index + 1
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
                upperRight.angle = angle - 20
                index = index + 1
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
                upperLeft.angle = 180 - angle + 20
                index = index + 1
                simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])

            lowLeft.angle = angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            lowRight.angle = 180 - angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            upperRight.angle = angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])
            upperLeft.angle = 180 - angle
            index = index + 1
            simpleio.tone(PIEZO_PIN, shootingStarsNotes[index], duration=shootingStarsBeats[index])

            if time.time() > timeout:
                print("BREAK")
                return

        if time.time() > timeout:
            print("BREAK")
            return

dance4()
timeout = time.time() + 30
dance5()
"""