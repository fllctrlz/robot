#!/usr/bin/env python3

from util import robot
from util import constants


def run():
    robot.driveBase.on(-15, -15)
    startTime = robot.timer.time()

    colorSensorPorts = []

    lightMin = []
    lightMax = []

    for i in range(len(robot.sensors)):
        lightMin.append(1000)
        lightMax.append(-1000)

    while robot.timer.time() - startTime < 7:
         for i in range(len(robot.sensors)):
            lightReading = robot.sensors[i].reflected_light_intensity 

            if lightReading < lightMin[i]: 
                lightMin[i] = lightReading

            if lightReading > lightMax[i]: 
                lightMax[i] = lightReading
        
    robot.driveBase.stop()        

    file = open("util/minValues.txt", "w+")
    for i in range(len(robot.sensors)):
        file.write(str(lightMin[i]) + "\n")
    file.close()

    file = open("util/maxValues.txt", "w+")
    for i in range(len(robot.sensors)):
        file.write(str(lightMax[i]) + "\n")
    file.close()

    robot.initCalibration()

def testWrite():
    file = open("util/minValues.txt", "w+")
    file.write(str(10) + "\n")
    file.write(str(-5) + "\n")
    file.write(str(15) + "\n")
    file.write(str(10) + "\n")
    file.close()

    file = open("util/maxValues.txt", "w+")
    file.write(str(100) + "\n")
    file.write(str(106) + "\n")
    file.write(str(133) + "\n")
    file.write(str(89) + "\n")
    file.close()

def readValues():
    #TODO - if the files don't exist, initialize the arrays' with 0 & 100
    file = open("util/minValues.txt", "r")
    min = [float(line.rstrip('\n')) for line in file]
    file.close()

    file = open("util/maxValues.txt", "r")
    max = [float(line.rstrip('\n')) for line in file]
    file.close() 
    
    return min, max

 