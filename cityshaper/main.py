#!/usr/bin/env python3
import os

os.system("setfont Lat15-TerminusBold14")
from sys import stderr
from time import sleep

from ev3dev2.button import Button
from ev3dev2.sound import Sound

from util import robot
from util import constants

import traceback

from missions import craneyBoi, blockDelivery1, trafficJam, redCircle, showGyro, calibration, testoPesto

# The Sound class creates a new instance that is assigned to the variable created.
soundGenerator = Sound()
buttonListener = Button()

selectedProgram = 0
missionNames = ["craneyBoi", "blockDelivery1", "trafficJam", "redCircle", "showGyro", "calibration", "testoPesto"]
missions = [craneyBoi, blockDelivery1, trafficJam, redCircle, showGyro, calibration, testoPesto]
numMissions = len(missionNames)


def left(pressed):
    global selectedProgram
    if pressed and selectedProgram > 0:
        #soundGenerator.play_tone(700, 0.5)
        selectedProgram = selectedProgram - 1
        print(missionNames[selectedProgram])


def right(pressed):
    global selectedProgram
    if pressed and selectedProgram < numMissions - 1:
        #soundGenerator.play_tone(1500, 0.5)
        selectedProgram = selectedProgram + 1
        print(missionNames[selectedProgram])


def enter(pressed):

    global selectedProgram
    if pressed:
        soundGenerator.beep()
        try:
            missions[selectedProgram].run()
            if selectedProgram < numMissions-1:
                selectedProgram = selectedProgram + 1
        except:
            soundGenerator.beep()
            #robot.debug(traceback.print_exc())
            robot.debug("EXCEPTION")
        robot.afterMission()
        print(missionNames[selectedProgram])


buttonListener.on_left = left
buttonListener.on_right = right
buttonListener.on_enter = enter

soundGenerator.beep()

robot.init()

#redCircle.run()


print(missionNames[selectedProgram])
while True:
    buttonListener.process()
    robot.printSensors()
    sleep(0.1)
    robot.debug("x")
