#!/usr/bin/env python3
from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn

def run():

    robot.showGyroDrift()
    gyroTurn.run(180, [1, -1], 30, 40)
    
    # def light():
    #     text = (str(int(robot.calibratedValue(0))) + " " +
    #     str(int(robot.calibratedValue(1))) + " " +
    #     str(int(robot.calibratedValue(2))) + " " + 
    #     str(int(robot.calibratedValue(3))))
    #     print(text)
    #     sleep(1)
    # def run():
    #     zPivot.run()