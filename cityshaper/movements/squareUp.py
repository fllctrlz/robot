#!/usr/bin/env python3
from sys import stderr
from time import sleep

from util import robot
from util import constants

def run(startPower, duration, side = 1):
    '''makes the robot perpendicular to the edge of the black line. Starts at high power
     and moves each motor back then forward based on if the light sensor sees
     greater or less than 50 while decreasing the power, until the power is 0
     and the duration is reached. The rate at which we deccelerate at is
     calculated by dividing our duration by the start power.'''

    startTime = robot.timer.time()
    currentPower = startPower
    # The amount of power we decrease by per second
    powerDecay = startPower / duration
    
    while currentPower >= 0:
        elapsedTime = robot.timer.time() - startTime
        # Changes the current power by subtracting the initial power from the time passed multiplied by the amount of power decreased per second.
        currentPower = startPower - elapsedTime * powerDecay
        currentPower = currentPower * side
        # Checks if the back left light sensor reading is greater than 50 (reading white)
        # If it is, move the motor until the light sensor reads black
        if robot.calibratedValue(robot.BACK_LEFT) > 50:
            robot.motorB.on(currentPower)
        else:
            robot.motorB.on(-currentPower)

        # Checks if the back right light sensor reading is greater than 50 (reading white)
        # If it is, move the motor until the light sensor reads black
        if robot.calibratedValue(robot.BACK_RIGHT) > 50:
            robot.motorC.on(currentPower)
        else:
            robot.motorC.on(-currentPower)

    robot.driveBase.stop()

        