#!/usr/bin/env python3

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

driveBase = MoveTank(OUTPUT_B, OUTPUT_C)

motorDirection = 1

motorB = LargeMotor(OUTPUT_B)
motorC = LargeMotor(OUTPUT_C)
motorD = LargeMotor(OUTPUT_D)

soundGenerator = Sound()


timer = time
startTime = 0

#inputs for into orbit robot:
# FRONT_LEFT = ColorSensor(INPUT_3)
# FRONT_RIGHT = ColorSensor(INPUT_4)
# BACK_LEFT = ColorSensor(INPUT_1)
# BACK_RIGHT = ColorSensor(INPUT_2)
# BACK_RIGHT = GyroSensor(INPUT_1)

# sensors = [
#     FRONT_LEFT,
#     FRONT_RIGHT,
#     BACK_LEFT,
#     BACK_RIGHT
# ]

FRONT = ColorSensor(INPUT_4)
BACK_LEFT = ColorSensor(INPUT_3)
BACK_RIGHT = ColorSensor(INPUT_2)
GYRO = GyroSensor(INPUT_1)


sensors = [
    FRONT,
    BACK_LEFT,
    BACK_RIGHT
]

calibrationMin = []
calibrationMax = []

startAngle = 0

def resetAngle():
    global startAngle
    startAngle = GYRO.angle

def getAngle():
    global startAngle
    return GYRO.angle - startAngle

def resetMotors():
    motorB.reset()
    motorC.reset()

def resetStartTime():
    global startTime
    startTime = timer.time()

def getTime():
    global startTime
    return timer.time() - startTime

def debug(text):
    print(text, file=stderr)

def initCalibration():
    global calibrationMin
    global calibrationMax
    calibrationMin, calibrationMax = calibration.readValues()

def calibratedValue(sensor):
    index = getIndexFromSensor(sensor)
    rawValue = sensors[index].reflected_light_intensity
    calibratedValue = 100.0 * (rawValue - calibrationMin[index]) / (calibrationMax[index] - calibrationMin[index])
    if calibratedValue > 99:
        return 99
    
    if calibratedValue < 1:
        return 1
    
    return calibratedValue

def printSensors():
    debug("BACK_LEFT")
    debug(calibratedValue(BACK_LEFT))
    debug("BACK_RIGHT")
    debug(calibratedValue(BACK_RIGHT))
    debug("FRONT")
    debug(calibratedValue(FRONT))

def getIndexFromSensor(sensor):
    for i in range (len(sensors)):
        if sensor == sensors[i]:
            return i
    return -1

def init():
    initCalibration()
    testGyroDrift()

def afterMission():
    driveBase.stop()

def safeMotorsOn(powerB, powerC):
    driveBase.on(min(100,max(powerB, -100)), min(100,max(powerC, -100)))

def testGyroDrift():
    firstRead = getAngle()
    print("checking for gyro drift")
    sleep(1)
     
    if abs(firstRead - getAngle()) > 1:
        print("gyro is drifting")
        soundGenerator.beep()
        raise Exception ("gyro is drifting")
        sleep(2)
    print ("No drift")
     
def beep():
    soundGenerator.beep()