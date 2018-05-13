import PiMotor
import RPi.GPIO as GPIO  
import time
import random
from Bluetooth import *

rightMotors = PiMotor.Motor("MOTOR1",1)
leftMotors = PiMotor.Motor("MOTOR2",1)
mode = 0
run = True
global data
data = None

#ultrasonic = PiMotor.Sensor("ULTRASONIC", 1)
#ultrasonic.sonicCheck()

def setData(cmd):
    data = cmd
        
def getData():
    return data


while run:
    
    if data == "Park":
         mode = 0
    elif data == "Teleop":
         mode = 1
    elif data == "Auto":
         mode = 2
        
    if mode == 1:
        if data == "Forward":
            rightMotors.forward(100)
            leftMotors.forward(100)
        elif data == "Backward":
            rightMotors.reverse(100)
            leftMotors.reverse(100)
        elif data == "Left":
            rightMotors.forward(100)
            leftMotors.reverse(100)
        elif data == "Right":
            rightMotors.reverse(100)
            leftMotors.forward(100)
        else:
            rightMotors.stop()
            leftMotors.stop()
                
    if mode == 2:
        randNum = random.randint(50,300)
        print(randNum)






