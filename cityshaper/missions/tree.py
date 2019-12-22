#!/usr/bin/env python3

from sys import stderr
from time import sleep

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn

def run():
    zMove.run(100, 1, 1, time, robot.timer, 3.25, slowDownDistance=800, startPower=60, endPower=40)
    sleep(0.35)
    zMove.run(-85, 1, 1, distance, robot.motorB, 900)
    gyroTurn.run(45, 80, -1, 15)
    zMove.run(-100, 1, 1, distance, robot.motorB, 1750)
    gyroTurn.run(90, 80, 1, 20)
