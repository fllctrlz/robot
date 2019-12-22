#!/usr/bin/env python3

import time

from util import robot

def run(targetAngle, power=80, direction=1, adjust=30):
    '''turns the robot using gyro sensor. Compares current angle with target angle
    then turns until target angle is reached. Since we use a very high power,
    we will turn to a value less than our desired angle, and turn slowly towards our target angle.
    If we do exceed our target angle, we are still able to turn back towards it at a slow power.'''
    robot.resetAngle()
    power = power * direction
    # Moves the motor at a high power while the gyro sensor angle reading is less than the target angle subtracted from a specified value.
    while abs(robot.getAngle()) < targetAngle - adjust:
        robot.driveBase.on(power, -power)
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
            robot.driveBase.on(5*direction, -5*direction)
            robot.checkAbort()
        robot.driveBase.stop()
    else:
        # Moves the motors in the opposite direction at a low power while the gyro sensor angle reading is less than the target angle.
        while abs(robot.getAngle()) > targetAngle:
            robot.driveBase.on(-5*direction, 5*direction)
            robot.checkAbort()
        robot.driveBase.stop()

