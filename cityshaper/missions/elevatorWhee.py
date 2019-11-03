#!/usr/bin/env python3

from util import robot
from util import constants
from util.exitConditions import distance, time, light
from movements import pidLineFollower


def run():
    #pidLineFollower.run(20, robot.FRONT_LEFT, 1, distance, robot.motorB, 500)
    pidLineFollower.run(-10, robot.FRONT, 1, time, robot.timer, 30)
    #pidLineFollower.run(20, robot.FRONT_LEFT, -1, light, robot.FRONT_RIGHT, 90, 100)