#!/usr/bin/env python3
import os

# Enlarge the font on the EV3 Display
os.system("setfont Lat15-TerminusBold14")

from sys import stderr
from time import sleep

from ev3dev2.button import Button
from ev3dev2.sound import Sound

from util import robot
from util import constants

import traceback

from missions import craney, blockDelivery1, trafficJam, redCircle, showGyro, cleanTires, calibration, testoPesto, tree

# The Sound class creates a new instance that is assigned to the variable created.
soundGenerator = Sound()
# buttonListener generates an event when the user presses the button
buttonListener = Button()

selectedProgram = 0 
# These are our missions
missionNames = ["craney", "trafficJam", "tree", "blockDelivery1", "redCircle", "calibration", "cleanTires", "showGyro"]
missions = [craney, trafficJam, tree, blockDelivery1, redCircle, calibration, cleanTires, showGyro]
numMissions = len(missionNames)

# buttonListener is called when the user presses the left button
def left(pressed):
    global selectedProgram
    if pressed and selectedProgram > 0:
        selectedProgram = selectedProgram - 1
        print(missionNames[selectedProgram])

# buttonListener is called when the user presses the right button
def right(pressed):
    global selectedProgram
    if pressed and selectedProgram < numMissions - 1:
        selectedProgram = selectedProgram + 1
        print(missionNames[selectedProgram])

# buttonListener is called when the user presses the enter (middle) button
def enter(pressed):
    global selectedProgram
    if pressed:
        soundGenerator.beep()
        try:
            missions[selectedProgram].run()
            if selectedProgram < numMissions-1:
                selectedProgram = selectedProgram + 1
        except  Exception as e:
            soundGenerator.beep()
            robot.debug("EXCEPTION")
            robot.debug(e)
            selectedProgram = selectedProgram + 1
        robot.afterMission() 
        print(missionNames[selectedProgram])

# Register the buttonListener
buttonListener.on_left = left
buttonListener.on_right = right
buttonListener.on_enter = enter

soundGenerator.beep()

# Read the calibrated values and test if the Gyro is drifting
robot.init()
#testoPesto.run()

print(missionNames[selectedProgram])
# Our Main Loop
while True:
    # Check if any buttons are pressed, and call the corresponding event handler
    buttonListener.process()
    # Debounce; Make sure the user has time to release the button
    sleep(0.1)