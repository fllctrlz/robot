#!/usr/bin/env python3
from sys import stderr
from time import sleep

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn


def run():
   zMove.run(-50, 1, 1, distance, robot.motorB, 1300, 0, 950)
   robot.motorD.on_for_degrees(speed=40, degrees=300)
   gyroTurn.run(30, 40, -1)
   zMove.run(50, 1, 1, distance, robot.motorB, 250, 0, 100)
   robot.beep()
   zPivot.run(40, motorB, light, robot.BACK_LEFT, 150, 0, 100)