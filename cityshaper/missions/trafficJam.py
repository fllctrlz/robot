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
   robot.motorD.on_for_degrees(speed=30, degrees=165)
   zPivot.run(-45, robot.motorB, time, robot.timer, 1.4)
   #Swing Mission
   zMove.run(50, 1, 1, distance, robot.motorB, 350)
   gyroTurn.run(50, 80, 1)
   zMove.run(-25, 1, 1, light, robot.BACK_RIGHT, 80, 100)
   zMove.run(-25, 1, 1, light, robot.BACK_RIGHT, 0, 15)
   zMove.run(-25, 1, 1, light, robot.BACK_RIGHT, 80, 100)
   sleep(0.25)
   gyroTurn.run(10, 80, -1)
   pidLineFollower.run(-10, robot.BACK_RIGHT, 1, distance, robot.motorB, 400)
   pidLineFollower.run(-25, robot.BACK_RIGHT, 1, distance, robot.motorB, 300)
   zMove.run(-50, 1, 1, light, robot.BACK_LEFT, 85, 100)
   sleep(0.25)
   pidLineFollower.run(-25, robot.BACK_RIGHT, 1, distance, robot.motorB, 815)
   zMove.run(-50, 1, 1, distance, robot.motorB, 80)
   zMove.run(20, 1, 1, distance, robot.motorB, 100)
   #Elevator Mission
   gyroTurn.run(72, 80, 1)
   zMove.run(-50, 1, 1, distance, robot.motorB, 390)
   zMove.run(-25, 1, 1, light, robot.BACK_LEFT, 85, 100)
   gyroTurn.run(27, 80, 1)
   robot.motorD.on_for_degrees(speed=45, degrees=440)
   zMove.run(-50, 1, 1, distance, robot.motorB, 140)
   robot.motorD.on_for_degrees(speed=60, degrees=-460)
   #Construction Mission
   gyroTurn.run(55, 80, -1)
   zMove.run(-60, 1, 1, distance, robot.motorB, 675)
   gyroTurn.run(65, 30, 1)
   robot.motorD.on_for_degrees(speed=60, degrees=520)
   zMove.run(-60, 1, 1, distance, robot.motorB, 425)
   robot.motorD.on_for_degrees(speed=15, degrees=-313)
   sleep(0.5)
   robot.motorD.on_for_degrees(speed=25, degrees=-5)
   #Back to Base
   zMove.run(60, 1, 1, distance, robot.motorB, 450)
   gyroTurn.run(70, 80, -1)
   zMove.run(100, 1, 1, distance, robot.motorB, 1600, startPower=50, kUp=30.0)
   gyroTurn.run(30, 30, -1)
   zMove.run(100, 1, 1, distance, robot.motorB, 4190, startPower=50, kUp=50.0)