#!/usr/bin/env python3

from time import time

from util import robot

def run(targetAngle, power, direction=1):
    robot.resetAngle()
    power = power * direction
    while abs(robot.getAngle()) < targetAngle:
        robot.driveBase.on(power, power * -1)
    robot.driveBase.stop()
    while abs(robot.getAngle()) >= targetAngle:
        robot.driveBase.on(-5*direction, 5*direction)
    robot.driveBase.stop()


# turns the robot using gyro sensor. Compares current angle with target angle
#  then turns
#      until target angle is reached. Since we use a very high power,
#  we will overcorrect, to accomodate for this, we turn the other way at a low power until
#  the robot;s angle is exactly equal to the target angle


