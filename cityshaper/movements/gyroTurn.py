#!/usr/bin/env python3

import time

from util import robot

def run(targetAngle, power=70, direction=1, adjust=30, slowPower=4):
    '''turns the robot using gyro sensor. Compares current angle with target angle
    then turns until target angle is reached. Since we use a very high power,
    we will turn to a value less than our desired angle, and turn slowly towards our target angle.
    If we do exceed our target angle, we are still able to turn back towards it at a slow power.'''
    robot.resetAngle()
    power = power * direction
    while abs(robot.getAngle()) < targetAngle - adjust:
        robot.driveBase.on(power, -power)
        robot.checkAbort()

    robot.driveBase.stop()
    robot.sleep(0.1)
    robot.debug("before error")
    robot.debug(targetAngle-abs(robot.getAngle()))
    
    if abs(robot.getAngle()) < targetAngle:
        while abs(robot.getAngle()) < targetAngle:
            robot.driveBase.on(slowPower*direction, -slowPower*direction)
            robot.checkAbort()
        robot.driveBase.stop()
    else:
        while abs(robot.getAngle()) > targetAngle:
            robot.driveBase.on(-slowPower*direction, slowPower*direction)
            robot.checkAbort()
        robot.driveBase.stop()

    robot.debug("after error")
    robot.debug(targetAngle-abs(robot.getAngle()))

