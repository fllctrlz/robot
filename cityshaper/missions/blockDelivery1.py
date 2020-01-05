from sys import stderr
from time import sleep

from util import robot
from util import constants
from util.exitConditions import distance, time, light

from movements import squareUp, pidLineFollower, zMove, gearLash, zPivot, followWall, gyroTurn


def run():
    zMove.run(80, 1, 1, distance, robot.motorB, 1250, 0, 950)
    zMove.run(-80, 1, 1, distance, robot.motorB, 350)
    # gyroTurn.run(90, 60, -1)
    gyroTurn.run(90, [-1, 1], 60)
    zMove.run(-90, 1, 1, distance, robot.motorB, 1000)