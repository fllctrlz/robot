#!/usr/bin/env python3

from ev3dev2.sound import Sound

from util import robot
from util import constants

def run(targetPower, pidSensor, side, condition, exitSensor, val1, 
val2 = 0, kp = constants.kp, stop = True):

    '''Follows the edge of the black line smoothly with the specified light
     sensor. Follow the edge at the speed, sensor, and side pecified by the user in the first three parameters.
     The condition can be chosen as distance, light, or time, and the values on which these exit can be modified.
     The second last parameter allows the user to change the constant that changes the error to a value to add to the motors, which allows for the choice of sharper or
     smoother turns.'''

    robot.resetMotors()
    robot.resetStartTime()

    direction = 1 if targetPower > 0 else -1

    # Checking if the set exit condition is met
    while not condition(exitSensor, val1, val2):
        # Calculates the error by taking the current reflected light intensity and subtracting it by the optimal value (half black, half white)
        error = robot.calibratedValue(pidSensor) - constants.optimal
        # Calculates the pTerm by multiplying the error by a constant less than one to lower the value. 
        # It then multiplies by the side and direction, which can change which side or which direction it follows the line.
        pTerm = error * kp * side * direction
        robot.safeMotorsOn(
            # Add the pTerm to one motor power and subtract it from the other
            robot.motorDirection * targetPower + pTerm,
            robot.motorDirection * targetPower - pTerm
            )              
    if stop:
        robot.driveBase.stop()