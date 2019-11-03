#!/usr/bin/env python3
from sys import stderr

from util import robot
from util import constants


def run(powerB, powerC, condition, exitSensor, val1, val2=0, stop=True):
    robot.resetStartTime()
    robot.resetMotors()
    robot.safeMotorsOn(powerB, powerC)
    while not condition(exitSensor, val1, val2):
        pass
    if stop:
        robot.driveBase.stop()

