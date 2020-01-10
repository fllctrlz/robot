#!/usr/bin/env python3

from sys import stderr
from time import sleep

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn

def run():
    #zMove.run(15, 1, 1, distance, robot.motorB, 20)
    #gyroTurn.run(49, 20, -1)
    gyroTurn.run(47, [-0.1, 1], 15, 20)
    zMove.run(90, 1, 1, time, robot.timer, 2.25, slowDownDistance=1000, startPower=60, endPower=40)
    zMove.run(15, 1, 1, time, robot.timer, 2.5, slowDownDistance=1000, startPower=15, endPower=15)
    sleep(0.35)
    zMove.run(-85, 1, 1, distance, robot.motorB, 900)
    #gyroTurn.run(45, 80, -1, 15)
    gyroTurn.run(45, [-1, 1], 80, 15)
    zMove.run(-100, 1, 1, distance, robot.motorB, 1750)
    #gyroTurn.run(90, 80, 1, 20)
    gyroTurn.run(90, [1, -1], 80, 20, slowSpeed=8)
