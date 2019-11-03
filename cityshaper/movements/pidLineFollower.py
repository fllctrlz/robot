#!/usr/bin/env python3

#TODO add derivative
from time import time 

from util import robot
from util import constants
from ev3dev2.sound import Sound

def run(targetPower, pidSensor, side, condition, exitSensor, val1, 
val2 = 0, kp = constants.kp, stop = True):

    '''follows the edge of the black line smoothly with the specified light
     sensor'''

    robot.resetMotors()
    robot.resetStartTime()
    direction = 1 if targetPower > 0 else -1

    while not condition(exitSensor, val1, val2):
        error = robot.calibratedValue(pidSensor) - constants.optimal
        pTerm = error * kp * side * direction
        robot.safeMotorsOn(
            robot.motorDirection * targetPower + pTerm,
            robot.motorDirection * targetPower - pTerm
            )  
    if stop:
        robot.driveBase.stop()