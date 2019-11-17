#!/usr/bin/env python3
from sys import stderr
from time import sleep

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn


def run():
   zMove.run(-50, 1, 1, distance, robot.motorB, 1300, 0, 950)
   robot.motorD.on_for_degrees(speed=40, degrees=160)
   gyroTurn.run(30, 40, -1)
   zMove.run(50, 1, 1, distance, robot.motorB, 150, 0, 100)
   gyroTurn.run(50, 50, 1) 
   zMove.run(-70, 1, -1, distance, robot.motorB, 650, 0, 1000)
   pidLineFollower.run(-25, robot.BACK_RIGHT, 1, distance, robot.motorB, 1000)
   