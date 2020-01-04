#!/usr/bin/env python3
from sys import stderr
from time import sleep

from ev3dev2.sound import Sound

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn



def run():    
    zMove.run(100, 1, 1, distance, robot.motorB, 1850, slowDownDistance=1500, stop=False)
    robot.soundGenerator.beep()
    zMove.run(100, 1, 1, light, robot.FRONT, 85, 100)
    robot.motorD.on_for_degrees(speed=-15, degrees=300)
    zMove.run(100, 1, 1, light, robot.BACK_LEFT, 85, 100)
    soundGenerator = Sound()
    soundGenerator.beep()
    sleep(0.5) 
    squareUp.run(20, 2.5, 1)
    zMove.run(-50, 1, 1, distance, robot.motorB, 150)
    #gyroTurn.run(90, 80, 1)
    gyroTurn.run(90, [1, -1], 40, adjust = 15)
    robot.motorD.on_for_degrees(speed=50, degrees=625)
    #gyroTurn.run(180, 80, 1)
    gyroTurn.run(180, [1, -1], 30, 40)
    zMove.run(-100, 1, 1, distance, robot.motorB, 2040)
    sleep(1)
    zPivot.run(50,robot.motorB, distance, robot.motorB, 200, robot.motorB)
    