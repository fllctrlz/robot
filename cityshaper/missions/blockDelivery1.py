from sys import stderr
from time import sleep

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn


def run():
    zMove.run(80, 1, 1, distance, robot.motorB, 1400, 0, 950)
    zMove.run(-80, 1, 1, distance, robot.motorB, 150)
    gyroTurn.run(90, 60, -1)
    zMove.run(-90, 1, 1, distance, robot.motorB, 600)