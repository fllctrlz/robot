#!/usr/bin/env python3

import time

from util import constants
from util import robot
from util.exitConditions import distance, time, light

def run(targetAngle, motor = [1,-1], power = 80, adjust = 30, slowSpeed = 4):
    '''turns the robot using gyro sensor. Compares current angle with target angle
    then turns until target angle is reached. Since we use a very high power,
    we will turn to a value less than our desired angle, and turn slowly towards our target angle.
    If we do exceed our target angle, we are still able to turn back towards it at a slow power.'''
    robot.resetAngle()
    # Moves the motor at a high power while the gyro sensor angle reading is less than the target angle subtracted from a specified value.
    while abs(robot.getAngle()) < targetAngle - adjust:
        # try:
            robot.driveBase.on(power*motor[0], power*motor[1])
            robot.checkAbort()
    # Prints the error between the target angle and the gyro sensor angle reading to the VSCode output window for debugging purposes.
    robot.driveBase.stop()
    robot.sleep(0.1)
    robot.debug("before error")
    robot.debug(targetAngle-abs(robot.getAngle()))
    # Checks whether the gyro sensor angle reading is less than or greater than the set target angle.
    if abs(robot.getAngle()) < targetAngle:
        # Moves the motors in one direction at a low power while the gyro sensor angle reading is less than the target angle.
        while abs(robot.getAngle()) < targetAngle:
            robot.driveBase.on(slowSpeed*motor[0], slowSpeed*motor[1])
            robot.checkAbort()
        robot.driveBase.stop()
    else:
        # Moves the motors in the opposite direction at a low power while the gyro sensor angle reading is less than the target angle.
        while abs(robot.getAngle()) > targetAngle:
            robot.driveBase.on(-slowSpeed*motor[0], -slowSpeed*motor[1])
            robot.checkAbort()
        robot.driveBase.stop()
    robot.debug(targetAngle-abs(robot.getAngle()))

