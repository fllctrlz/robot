#!/usr/bin/env python3
from sys import stderr
from time import sleep

from ev3dev2.sound import Sound

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn

soundGenerator = Sound()

def run():
    zMove.run(100, 1, 1, distance, robot.motorB, 1850, slowDownDistance=1000)
    zMove.run(100, 1, 1, light, robot.FRONT, 85,100)
    robot.motorD.on_for_degrees(speed=35, degrees=360)
    zMove.run(100, 1, 1, light, robot.BACK_LEFT, 85, 100)
    soundGenerator.beep()
    sleep(0.5) 
    squareUp.run(30, 3, 1)
    gyroTurn.run(95, 40, 1)
    zMove.run(100, 1, 1, distance, robot.motorB, 2150)