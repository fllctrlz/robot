#!/usr/bin/env python3
from sys import stderr

from util import robot
from util import constants


def run(targetPower, motor, condition, exitSensor, val1, val2 = 0, 
    slowDownDistance = 800, startPower = 10, endPower = 10, stop = True):

    '''turns the robot by setting the specified motor (one that is not turning)to 0.
     Based on the inputed direction the other motor moves backwards or forwards
     by multiplying the power by the direction. It also uses acceleration and deceleration
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

        distance = abs(motor.position)

        if distance > slowDownDistance and currentPower > endPower:
            currentPower = currentPower - constants.kDown
        elif accelerating:
            currentPower = currentPower + constants.kUp
            if currentPower >= targetPower:
                accelerating = False

        power = currentPower

        motor.on(power * robot.motorDirection * direction) 

    if stop:
        robot.driveBase.stop()

