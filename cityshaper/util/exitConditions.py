#!/usr/bin/env python3
from sys import stderr

from ev3dev2.button import Button

from util import robot, constants

def distance(motor, value, unused):
    #print(motor.position, file = stderr)
    if Button().up:
        raise Exception("button up was pressed")
    return abs(motor.position) > value

def time(timer, value, unused):
    #print(timer.time() - robot.startTime, file = stderr)
    if Button().up:
        raise Exception("button up was pressed")
    return timer.time() - robot.startTime > value

def light(sensor, value1, value2):
    if Button().up:
        raise Exception("button up was pressed")
    return robot.calibratedValue(sensor) >=value1 and robot.calibratedValue(sensor) <=value2

    #TODO finish gyro exit
def gyro(sensor, value1, value2):
    pass


    

