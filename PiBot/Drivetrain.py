import PiMotor
import RPi.GPIO as GPIO  
import time
import random
from Bluetooth import *

rightMotors = PiMotor.Motor("MOTOR1",1)
leftMotors = PiMotor.Motor("MOTOR2",1)
mode = 0
run = False
data = None

#ultrasonic = PiMotor.Sensor("ULTRASONIC", 1)
#ultrasonic.sonicCheck()


class Data:
    def setData(cmd):
        data = cmd
            
    def getData():
        return data
        
class Motors:
    def driveMotors(speed):
        correctedSpeed = speed*100
        if correctedSpeed > 0:
            rightMotors.forward(correctedSpeed)
            leftMotors.forward(correctedSpeed)
        elif correctedSpeed < 0:
            rightMotors.reverse(correctedSpeed)
            leftMotors.reverse(correctedSpeed)

    def turnMotors(speed):
        correctedSpeed = speed*100
        if correctedSpeed > 0:
            rightMotors.reverse(correctedSpeed)
            leftMotors.forward(correctedSpeed)
        elif correctedSpeed < 0:
            rightMotors.forward(correctedSpeed)
            leftMotors.reverse(correctedSpeed)

    def stopMotors():
        leftMotors.stop()
        rightMotors.stop()

def enable(enable):
    run = enable


while run:
    
    if data == "Park":
         mode = 0
    elif data == "Teleop":
         mode = 1
    elif data == "Auto":
         mode = 2
        
    if mode == 1:
        if data == "Forward":
            driveMotors(1)
        elif data == "Backward":
            driveMotors(-1)
        elif data == "Left":
            turnMotors(-1)
        elif data == "Right":
            turnMotors(1)
        else:
            stopMotors()
                
    if mode == 2:
        randNum = random.randint(50,300)
        print(randNum)






