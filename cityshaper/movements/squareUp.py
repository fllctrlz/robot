#!/usr/bin/env python3
from sys import stderr
from time import sleep

from util import robot
from util import constants

def run(startPower, duration, side = 1):

    '''makes robot perpendicular to edge of black line. Starts at high power
     and moves each motor back then forward based on if the light sensor sees
     greater or less than 50while decreasing the power, until the power is 0
     and the duration is reached. The rate at which we deccelerate at is
     calculated by dividing our duration by the start power'''

    startTime = robot.timer.time()
    currentPower = startPower
    powerDecay = startPower / duration
    
    while currentPower >= 0:
        elapsedTime = robot.timer.time() - startTime
        currentPower = startPower - elapsedTime * powerDecay
        currentPower = currentPower * side
    
        if robot.calibratedValue(robot.BACK_LEFT) > 50:
            robot.motorB.on(currentPower)
        else:
            robot.motorB.on(-currentPower)

        if robot.calibratedValue(robot.BACK_RIGHT) > 50:
            robot.motorC.on(currentPower)
        else:
            robot.motorC.on(-currentPower)

    robot.driveBase.stop()

        