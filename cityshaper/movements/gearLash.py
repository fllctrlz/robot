#!/usr/bin/env python3

from util import robot
from time import sleep

from util.exitConditions import distance, time, light

def run(direction, delay = 0.2, power = 5):
    '''Moves the motors at a very low power for a short time 
    in order to minimize the slippage of the gears inside the motors of the robot.'''
    robot.resetStartTime()
    robot.resetMotors()
    motorPower = power*direction*robot.motorDirection
    robot.safeMotorsOn(motorPower, motorPower)    
    # Check if the time is equal to the amount set at the beginning of the function
    while not condition(time, robot.timer, delay, 0):
        pass
    robot.driveBase.stop()
