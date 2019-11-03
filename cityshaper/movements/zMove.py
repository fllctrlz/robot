#!/usr/bin/env python3
from sys import stderr

from util import robot
from util import constants

def run(targetPower, turn, turnDirection, condition, exitSensor, val1, val2 = 0, 
    slowDownDistance = 10000, startPower = 30, endPower = 15, stop = True):

    '''moves the robot forward or on an arc with error correction by finding
     the difference in the distance traveled by each motor multipled by the arc
     (variable called turn). It also uses acceleration and deceleration
     by adding a constant until the target power is reached, then the robot moves
     at the target power until the slow down distance is reached, then the power decrases by
     subtracting the constant until the end power is reached, in which case the robot
     keeps moving until the end distance is reached.'''

    robot.resetMotors()
    robot.resetStartTime()
    direction = 1 if targetPower > 0 else -1

    targetPower = abs(targetPower)

    currentPower = startPower
    accelerating = True

    while not condition(exitSensor, val1, val2):

        distanceB = abs(robot.motorB.position)
        distanceC = abs(robot.motorC.position)

        if distanceB > slowDownDistance and currentPower > endPower:
            currentPower = currentPower - constants.kDown
        elif accelerating:
            currentPower = currentPower + constants.kUp
            if currentPower >= targetPower:
                accelerating = False

        if turnDirection == 1:
            error = constants.kWiggle * (distanceB - distanceC * turn)
        else:
            error = constants.kWiggle * (distanceB * turn - distanceC)
        powerB = currentPower - error
        powerC = currentPower + error
        robot.debug(error)

        robot.safeMotorsOn(powerB * robot.motorDirection * direction, powerC * robot.motorDirection * direction) 

    if stop:
        robot.driveBase.stop()

