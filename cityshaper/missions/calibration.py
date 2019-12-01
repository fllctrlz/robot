#!/usr/bin/env python3

from util import robot
from util import constants


def run():
    '''runs robot for 7 seconds while storing the highest and lowest light sensor readings,
    then store these in a minimum and maximum value file'''

    robot.driveBase.on(-15, -15)
    startTime = robot.timer.time()

    # arrays are empty because we have not read light values yet
    lightMin = []
    lightMax = []

    # sets min and max to unrealistic values so they are overwritten on the first reading
    for i in range(len(robot.sensors)):
        lightMin.append(1000)
        lightMax.append(-1000)

    while robot.timer.time() - startTime < 7:
        # read values for all light sensors
         for i in range(len(robot.sensors)):
            lightReading = robot.sensors[i].reflected_light_intensity 

            # if current values are lower than previous min, current value is now the min
            if lightReading < lightMin[i]: 
                lightMin[i] = lightReading

            # if current values are higher than previous max, current value is now the max
            if lightReading > lightMax[i]: 
                lightMax[i] = lightReading
        
    robot.driveBase.stop()        

    # open the file and write the min values
    file = open("util/minValues.txt", "w+")
    for i in range(len(robot.sensors)):
        file.write(str(lightMin[i]) + "\n")
    file.close()

    # open the file and write the max values
    file = open("util/maxValues.txt", "w+")
    for i in range(len(robot.sensors)):
        file.write(str(lightMax[i]) + "\n")
    file.close()

    # initializes the min and max lists
    robot.initCalibration()

def readValues():
    '''Reads the file line by line, then strips the enter from the String, 
    then converts values to a float and adds them to min array'''
    file = open("util/minValues.txt", "r")
    min = [float(line.rstrip('\n')) for line in file]
    file.close()

    file = open("util/maxValues.txt", "r")
    max = [float(line.rstrip('\n')) for line in file]
    file.close() 
    
    return min, max

 