#!/usr/bin/env python3
from sys import stderr

from ev3dev2.button import Button

from util import robot, constants

def distance(motor, value, unused):
    '''returns True if the distance travelled exceeds the set value'''
    #print(motor.position, file = stderr)
    if Button().up:
        raise Exception("button up was pressed")
    return abs(motor.position) > value

def time(timer, value, unused):
    '''returns True if the time elapsed since timerReset exceeds the set value'''
    #print(timer.time() - robot.startTime, file = stderr)
    if Button().up:
        raise Exception("button up was pressed")
    return timer.time() - robot.startTime > value

def light(sensor, value1, value2):
    '''returns True if the light reading is within the set threshold'''
    if Button().up:
        raise Exception("button up was pressed")
    return robot.calibratedValue(sensor) >=value1 and robot.calibratedValue(sensor) <=value2


    

