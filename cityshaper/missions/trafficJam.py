#!/usr/bin/env python3
from sys import stderr
from time import sleep

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn


def run():
   zMove.run(-80, 1, 1, distance, robot.motorB, 1250, 0, 950)
   robot.motorA.on_for_degrees(speed=80, degrees=240)