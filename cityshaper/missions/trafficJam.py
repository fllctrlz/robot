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
   #Traffic Jam Mission
   zMove.run(-50, 1, 1, distance, robot.motorB, 1300, 0, 950)
   robot.motorD.on_for_degrees(speed=40, degrees=160)
   zPivot.run(-45, robot.motorB, time, robot.timer, 1.4)
   #Swing Mission
   zMove.run(50, 1, 1, distance, robot.motorB, 250)
   gyroTurn.run(50, 35, 1)
   zMove.run(-30, 1, 1, light, robot.BACK_RIGHT, 80, 100)
   zMove.run(-30, 1, 1, light, robot.BACK_RIGHT, 0, 15)
   zMove.run(-30, 1, 1, light, robot.BACK_RIGHT, 80, 100)
   pidLineFollower.run(-25, robot.BACK_RIGHT, 1, distance, robot.motorB, 400, kp=0.1)
   zMove.run(-50, 1, 1, light, robot.BACK_LEFT, 85, 100)
   pidLineFollower.run(-25, robot.BACK_RIGHT, 1, distance, robot.motorB, 815)
   zMove.run(-50, 1, 1, distance, robot.motorB, 80)
   zMove.run(50, 1, 1, distance, robot.motorB, 100)
   #Elevator Mission
   gyroTurn.run(80, 30, 1)
   zMove.run(-50, 1, 1, distance, robot.motorB, 300)
   zMove.run(-25, 1, 1, light, robot.BACK_LEFT, 85, 100)
   robot.motorD.on_for_degrees(speed=60, degrees=360)
   zMove.run(-50, 1, 1, distance, robot.motorB, 185)
   robot.motorD.on_for_degrees(speed=60, degrees=-360)
   #Construction Mission
   gyroTurn.run(40, 30, -1)
   zMove.run(-60, 1, 1, distance, robot.motorB, 575)
   gyroTurn.run(58, 30, 1)
   robot.motorD.on_for_degrees(speed=60, degrees=500)
   zMove.run(-60, 1, 1, distance, robot.motorB, 500)
   robot.motorD.on_for_degrees(speed=25, degrees=-400)
   sleep(0.5)
   robot.motorD.on_for_degrees(speed=25, degrees=-5)
   #Back to Base
   zMove.run(60, 1, 1, distance, robot.motorB, 450)
   gyroTurn.run(45, 30, -1)
   zMove.run(100, 1, 1, distance, robot.motorB, 800)
   gyroTurn.run(55, 30, -1)
   zMove.run(100, 1, 1, distance, robot.motorB, 4850)
   