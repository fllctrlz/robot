#!/usr/bin/env python3
from util import robot
from time import sleep
from util.exitConditions import distance, time, light

def run (direction, delay = 0.2, power = 5):
    robot.resetStartTime()
    robot.resetMotors()
    motorPower = power*direction*robot.motorDirection
    robot.safeMotorsOn(motorPower, motorPower)    
    while not condition (time, robot.timer, delay, 0):
        pass
    robot.driveBase.stop()
