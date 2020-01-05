#!/usr/bin/env python3

# stderr prints to VSCode output window to help us debug
from sys import stderr
import time
from time import sleep

from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.button import Button
from ev3dev2.sound import Sound

from missions import calibration

from movements import squareUp, pidLineFollower, zMove, zPivot

# Prevents collision of the time function
# We import time from our exitCondition module as timeLocal
from util.exitConditions import time as timeLocal

# Object that controls the movement of both motors
driveBase = MoveTank(OUTPUT_B, OUTPUT_C)

# When motorDirection is 1, drive forward, if it is -1, drive backward
motorDirection = 1

motorB = LargeMotor(OUTPUT_B)
motorC = LargeMotor(OUTPUT_C)
motorD = LargeMotor(OUTPUT_D)

soundGenerator = Sound()

# Re-export the timer from the time module
timer = time
startTime = 0

FRONT = ColorSensor(INPUT_4)
BACK_LEFT = ColorSensor(INPUT_3)
BACK_RIGHT = ColorSensor(INPUT_2)
GYRO = GyroSensor(INPUT_1)

# List of light sensor inputs
sensors = [
    FRONT,
    BACK_LEFT,
    BACK_RIGHT
]

calibrationMin = []
calibrationMax = []

# Records the current angle when resetAngle is called
# We use it to make Gyro movements relative to the startAngle
startAngle = 0

def resetAngle():
    '''Reset the startAngle so the angle returned by getAngle is relative to the beginning of the turn'''
    global startAngle
    startAngle = GYRO.angle

def getAngle():
    '''Gets the current angle from when the last resetAngle was called'''
    global startAngle
    return GYRO.angle - startAngle

def resetMotors():
    '''Resets the rotational sensors to 0'''
    motorB.reset()
    motorC.reset()

def resetStartTime():
    '''Resets the timer to 0'''
    global startTime
    startTime = timer.time()

def getTime():
    '''Gets the time from when the last resetStartTime was called'''
    global startTime
    return timer.time() - startTime

def debug(text):
    '''Print text to the VSCode output window'''
    print(text, file=stderr)

def initCalibration():
    '''Reads the values stored in the calibration file'''
    global calibrationMin
    global calibrationMax
    calibrationMin, calibrationMax = calibration.readValues()

def calibratedValue(sensor):
    '''scales current light sensor readings to values between 0 and 100
    and clamps the value between 0 and 100'''
    index = getIndexFromSensor(sensor)
    rawValue = sensors[index].reflected_light_intensity
    calibratedValue = 100.0 * (rawValue - calibrationMin[index]) / (calibrationMax[index] - calibrationMin[index])
    return min(100.0, max(0.0, calibratedValue))

def printSensors():
    '''prints the calibrated values for each sensor (used for debugging)'''
    debug("BACK_LEFT")
    debug(calibratedValue(BACK_LEFT))
    debug("BACK_RIGHT")
    debug(calibratedValue(BACK_RIGHT))
    debug("FRONT")
    debug(calibratedValue(FRONT))

def getIndexFromSensor(sensor):
    '''finds the index of the light sensor object'''
    for i in range (len(sensors)):
        if sensor == sensors[i]:
            return i
    return -1

def init():
    '''uses these functions in main program to use light sensors and test gyro drift'''
    initCalibration()
    testGyroDrift()

def afterMission():
    '''stops drive motors and releases tension of attachment motor'''
    driveBase.stop()
    motorD.off(brake=False)

def safeMotorsOn(powerB, powerC):
    '''ensures that motor powers don't exceed -100 and 100, if they do, scales down values'''
    driveBase.on(min(100,max(powerB, -100)), min(100,max(powerC, -100)))

def testGyroDrift():
    '''checks for drift by comparing currAngle to prevAngle one second ago,
    if gyro is drifting, robot beeps and you unplug and replug sensor to clear drift'''
    firstRead = getAngle()
    print("checking for gyro drift")
    sleep(1)
     
    if abs(firstRead - getAngle()) > 0.2:
        print("gyro is drifting")
        soundGenerator.beep()
        raise Exception ("gyro is drifting")
        sleep(2)
    print ("No drift")
     
def beep():
    '''beeps'''
    soundGenerator.beep()


def sleep(seconds):
    '''special pause that exits when up button is pressed'''
    resetStartTime()
    while not timeLocal(timer, seconds, 0):
        pass

def checkAbort():
    '''check if the up button is pressed, if it is, raise an exception and exit the program'''
    if Button().up:
        raise Exception("button up was pressed")
