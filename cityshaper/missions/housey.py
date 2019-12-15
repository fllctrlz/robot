#!/usr/bin/env python3
from sys import stderr
from time import sleep

from ev3dev2.sound import Sound

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn

def run ():
    zMove.run(100, 1, 1, distance, robot.motorB, 2100, slowDownDistance = 910, kDown = 0.6)
    gyroTurn.run(25, direction = -1)
    zMove.run(100, 1, 1, distance, robot.motorB, 1600)
    zMove.run(25, 1, 1, distance, robot.motorB, 600)
    sleep(0.5)
    zMove.run(-100, 1, 1, distance, robot.motorB, 300, kUp = 100, startPower = 40)
    gyroTurn.run(10)
    zMove.run(-100, 1, 1, distance, robot.motorB, 5000, kUp = 100, startPower = 40)
