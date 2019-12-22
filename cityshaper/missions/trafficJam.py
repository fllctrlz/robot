#!/usr/bin/env python3
from sys import stderr
from time import sleep

from ev3dev2.sound import Sound

from util import robot
#from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn

soundGenerator = Sound()


def run():
   #Traffic Jam Mission
   zMove.run(-50, 1, 1, distance, robot.motorB, 1150)
   robot.motorD.on_for_degrees(speed=30, degrees=165)
   zPivot.run(-70, robot.motorB, time, robot.timer, 1.5)
   #Swing Mission
   zMove.run(50, 1, 1, light, robot.FRONT, 80, 100)
   zMove.run(100, 1, 1, distance, robot.motorB, 110)
   zPivot.run(10, robot.motorB, light, robot.BACK_RIGHT, 80, 100)
   zPivot.run(15, robot.motorB, light, robot.BACK_RIGHT, 0, 20)
   zPivot.run(15, robot.motorB, light, robot.BACK_RIGHT, 80, 100)
   pidLineFollower.run(-8, robot.BACK_RIGHT, 1, distance, robot.motorB, 300, kp = 0.13)
   pidLineFollower.run(-25, robot.BACK_RIGHT, 1, distance, robot.motorB, 900)
   pidLineFollower.run(-15, robot.BACK_RIGHT, 1, light, robot.BACK_LEFT, 0, 30)
   zMove.run(-30, 1, 1, light, robot.BACK_LEFT, 80, 100)
   pidLineFollower.run(-25, robot.BACK_RIGHT, 1, distance, robot.motorB, 350)


   




#    #Traffic Jam Mission
#   # zMove.run(-50, 1, 1, distance, robot.motorB, 1300, 0, 950)
#   # robot.motorD.on_for_degrees(speed=30, degrees=165)
#   # zPivot.run(-70, robot.motorB, time, robot.timer, 1.8)
#    #Swing Mission
#    zMove.run(50, 1, 1, light, robot.FRONT, 80, 100)
#    zMove.run(-100, 1, 1, distance, robot.motorB, 110)
#    sleep(1)
#    zPivot.run(10, robot.motorB, light, robot.BACK_RIGHT, 80,100)
#    zPivot.run(20, robot.motorB, light, robot.BACK_RIGHT, 0, 20)
#    #zMove.run(-25, 1, 1, light, robot.BACK_RIGHT, 80, 100)
#    #zMove.run(-25, 1, 1, light, robot.BACK_RIGHT, 0, 15)
#    #zMove.run(-25, 1, 1, light, robot.BACK_RIGHT, 80, 100)
#    sleep(0.25)
#    pidLineFollower.run(-8, robot.BACK_RIGHT, 1, distance, robot.motorB, 1000, kp = 0.09)
#    sleep(2)
#    pidLineFollower.run(-20, robot.BACK_RIGHT, 1, distance, robot.motorB, 500)
#    zMove.run(-40, 1, 1, light, robot.BACK_LEFT, 75, 100)
#    sleep(0.25)
#    pidLineFollower.run(-25, robot.BACK_RIGHT, 1, distance, robot.motorB, 815)
#    robot.soundGenerator.beep()
#    zMove.run(-50, 1, 1, distance, robot.motorB, 80)
#    zMove.run(20, 1, 1, distance, robot.motorB, 100)
#    #Elevator Mission
#    gyroTurn.run(80, 80, 1)
#    robot.motorD.on_for_degrees(speed=45, degrees=440)
#    zMove.run(-50, 1, 1, distance, robot.motorB, 450)
#    zMove.run(-25, 1, 1, light, robot.BACK_RIGHT,75, 100)
#    # gyroTurn.run(20, 80, 1)
#    zMove.run(-50, 1, 1, distance, robot.motorB, 110)
#    robot.motorD.on_for_degrees(speed=60, degrees=-460)
#    #Construction Mission
#    # gyroTurn.run(60, 80, -1)
#    # zMove.run(-60, 1, 1, distance, robot.motorB, 300)
#    # # gyroTurn.run(65, 30, 1)
#    # # robot.motorD.on_for_degrees(speed=60, degrees=520)
#    # # gyroTurn.run(35, 30, -1)
#    # # zMove.run(-60, 1, 1, distance, robot.motorB, 425)
#    # robot.motorD.on_for_degrees(speed=15, degrees=-313)
#    # sleep(0.5)
#    robot.motorD.on_for_degrees(speed=25, degrees=-5)
#    #Back to Base
#    # zMove.run(60, 1, 1, distance, robot.motorB, 450)
#    gyroTurn.run(40, 80, -1)
#    zMove.run(100, 1, 1, distance, robot.motorB, 1000, startPower=50, kUp=30)
#    gyroTurn.run(46, 30, -1, adjust = 38)
#    zMove.run(100, 1, 1, distance, robot.motorB, 4300, startPower=50, kUp=50)
   