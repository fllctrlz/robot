#!/usr/bin/env python3

from util import robot

def run():
    currAngle = robot.GYRO.angle
    lastAngle = currAngle
    robot.resetStartTime()
    timeStep = 3
    while robot.getTime() <= 10:
        currAngle = robot.GYRO.angle
        diff = currAngle - lastAngle
        driftRate = diff/timeStep
        print(currAngle - lastAngle)
        lastAngle = currAngle
        robot.sleep(timeStep)