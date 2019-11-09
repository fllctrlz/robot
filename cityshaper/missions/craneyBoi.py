#!/usr/bin/env python3

from sys import stderr
from time import sleep

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall,gyroTurn

def run():
    zMove.run(-30, 1, 1, distance, robot.motorB, 800)
    gyroTurn.run(20, 40, -1)
    zMove.run(-30, 1, 1, distance, robot.motorB, 450)
    gyroTurn.run(20, 40, 1)
    #drives forward and uses gyro sensor to adjust to be straight on with the box
    zMove.run(-15, 1, 1, distance, robot.motorB, 780)
    #pushes block forward and lowers crane arm
    zMove.run(-5, 1, 1, distance, robot.motorB, 200)
    zMove.run(100, 0.91, 1, distance, robot.motorB, 2000, startPower = 50)
    #drives back to base

