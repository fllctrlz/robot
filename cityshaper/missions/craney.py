#!/usr/bin/env python3

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn

def run():
    #zMove.run(80, 1, 1, distance, robot.motorB, 800)
    # gyroTurn.run(20, direction = -1, adjust = 10)
    #gyroTurn.run(30, [-1, 1], 20, adjust = 10)
    zMove.run(31, 1, 1, distance, robot.motorB, 540)
    # gyroTurn.run(18, 50, 1, adjust = 5)
    gyroTurn.run(28, [1, -1], 15, 10)
    #drives forward and uses gyro sensor to adjust to be straight on with the box
    zMove.run(10, 1, 1, distance, robot.motorB, 1140)
    # pushes block forward and lowers crane arm
    zMove.run(5, 1, 1, distance, robot.motorB, 700)
    zMove.run(-100, 1, 1, distance, robot.motorB, 750, startPower = 50)
    # gyroTurn.run(90, 60, -1, adjust = 15)
    gyroTurn.run(90, [-1, 1], 60)
    zMove.run(-100, 1, 1, distance, robot.motorB, 1050, startPower = 60)
    #drives back and turns into base

