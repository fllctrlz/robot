#!/usr/bin/env python3

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn

def run():
    zMove.run(100, 1, 1, distance, robot.motorB, 80000, slowDownDistance=80000)

