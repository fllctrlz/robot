#!/usr/bin/env python3
import os

# Enlarge the font on the EV3 Display
os.system("setfont Lat15-TerminusBold14")

from time import sleep
import time

from ev3dev2.button import Button

from util import robot
from util import constants

import traceback

from missions import craney, blockDelivery1, trafficJam, redCircle, showGyro, calibration, testoPesto, housey

# buttonListener generates an event when the user presses the button
buttonListener = Button()

selectedProgram = 0 
# These are our missions
missionNames = ["craney", "trafficJam", "blockDelivery1", "housey", "redCircle", "calibration"]
missions = [craney, trafficJam, blockDelivery1, housey, redCircle, calibration]
numMissions = len(missionNames)

# buttonListener is called when the user presses the left button
def left(pressed):
    global selectedProgram
    if pressed and selectedProgram > 0:
        selectedProgram = selectedProgram - 1
        robot.displayOnBrick(missionNames[selectedProgram])
        #print(missionNames[selectedProgram])

# buttonListener is called when the user presses the right button
def right(pressed):
    global selectedProgram
    if pressed and selectedProgram < numMissions - 1:
        selectedProgram = selectedProgram + 1
        robot.displayOnBrick(missionNames[selectedProgram])
        #print(missionNames[selectedProgram])

# buttonListener is called when the user presses the enter (middle) button
def enter(pressed):
    global selectedProgram
    if pressed:
        robot.beep()
        try:
            missions[selectedProgram].run()
            if selectedProgram < numMissions-1:
                selectedProgram = selectedProgram + 1
        except:
            robot.beep()
            robot.debug("Check abort")
            selectedProgram = selectedProgram + 1
        robot.afterMission()
        if selectedProgram >= numMissions:
            selectedProgram = selectedProgram + 1
        robot.displayOnBrick(missionNames[selectedProgram])
        #print(missionNames[selectedProgram])

# Register the buttonListener
buttonListener.on_left = left
buttonListener.on_right = right
buttonListener.on_enter = enter

# Read the calibrated values and test if the Gyro is drifting

robot.init()
robot.beep()

robot.beep()

robot.displayOnBrick(missionNames[selectedProgram])
#print(missionNames[selectedProgram])

currTime = time.time()
prevTime = currTime

def printCyclesPerSecond():
    global currTime
    global prevTime
    currTime = time.time()
    cyclesPerSecond = 1/(currTime-prevTime)
    prevTime = currTime
    robot.debug(cyclesPerSecond)

# Our Main Loop
while True:
    #printCyclesPerSecond()
    # Check if any buttons are pressed, and call the corresponding event handler
    buttonListener.process()
    robot.updateDisplay()
    # Debounce; Make sure the user has time to release the button
    sleep(0.01)