#!/usr/bin/env python3
from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn

def run():
    #zMove.run(15, 1, distance, robot.motorB, 2750, 0, 2000)
    #zMove.run(90, 0.6, distance, robot.motorB, 2750, 0, 2000)
    #zMove.run(-90, 0.7, distance, robot.motorB, 3500, 0, 2000)
    #zMove.run(-90, 1, time, robot.timer, 10, 0, 2000)
    #gearLash.run(-1, 0.5, 5)
    #zPivot.run(-80, robot.motorC, time, robot.timer, 5)
    #zPivot.run(60, robot.motorC, distance, robot.motorC, 1500)
    #followWall.run(50, 40, distance, robot.motorB, 1500)
    #followWall.run(-60, -70, time, robot.timer, 6)
    #pidLineFollower.run(20, robot.FRONT_LEFT, 1, distance, robot.motorB, 500)
    #pidLineFollower.run(-20, robot.BACK_LEFT, 1, time, robot.timer, 15)
    #pidLineFollower.run(20, robot.FRONT_LEFT, -1, light, robot.FRONT_RIGHT, 90, 100)
    
    def light():
        text = (str(int(robot.calibratedValue(0))) + " " +
        str(int(robot.calibratedValue(1))) + " " +
        str(int(robot.calibratedValue(2))) + " " + 
        str(int(robot.calibratedValue(3))))
        print(text)
        sleep(1)

    def run():
        Zpivot.run()