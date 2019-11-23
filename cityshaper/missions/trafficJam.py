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
   zPivot.run(-45, robot.motorB, time, robot.timer, 2)
   zMove.run(50, 1, 1, light, robot.FRONT, 90, 100)
   zPivot.run(15, robot.motorB, light, robot.BACK_RIGHT, 85, 100)
   sleep(0.25)
   zPivot.run(15, robot.motorB, light, robot.BACK_RIGHT, 0, 15)
   sleep(0.25)
   zPivot.run(15, robot.motorB, light, robot.BACK_RIGHT, 85, 100)
   sleep(0.25)
   pidLineFollower.run(-25, robot.BACK_RIGHT, 1, distance, robot.motorB, 1300)
   zMove.run(-50, 1, 1, light, robot.BACK_LEFT, 85, 100)
   pidLineFollower.run(-25, robot.BACK_RIGHT, 1, distance, robot.motorB, 815)
   zMove.run(-50, 1, 1, distance, robot.motorB, 80)
   zMove.run(50, 1, 1, distance, robot.motorB, 100)
   gyroTurn.run(80, 80, 1)
   zMove.run(-50, 1, 1, distance, robot.motorB, 300)
   zMove.run(-50, 1, 1, light, robot.BACK_LEFT, 85, 100)
   robot.motorD.on_for_degrees(speed=60, degrees=360)
   zMove.run(-50, 1, 1, distance, robot.motorB, 170)
   robot.motorD.on_for_degrees(speed=60, degrees=-360)