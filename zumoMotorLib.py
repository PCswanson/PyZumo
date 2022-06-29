# Motor Libraries for Zumo Bot


import board
from digitalio import DigitalInOut, Direction, Pull
import pulseio
import math

# Declare motor control ports
PWM_L = pulseio.PWMOut(board.D10, frequency=20000, duty_cycle=0)
PWM_R = pulseio.PWMOut(board.D9, frequency=20000, duty_cycle=0)
DIR_L = DigitalInOut(board.D8)
DIR_L.direction = Direction.OUTPUT
DIR_R = DigitalInOut(board.D7)
DIR_R.direction = Direction.OUTPUT

DIR_L.value = False
DIR_R.value = False


def setLeftDir(dir):
    # send F to drive left motor forward, R for reverse
    if dir == "F":
        DIR_L.value = False
        print("left forward")
    elif dir == "R":
        DIR_L.value = True
        print("left reverse")
    else:
        print("Error in direction command")

def setRightDir(dir):
    # send F to drive right motor forward, R for reverse
    if dir == "F":
        DIR_R.value = False
        print("right forward")
    elif dir == "R":
        DIR_R.value = True
        print("right reverse")
    else:
        print("Error in direction command")


def setLeftSpeed(speed):
    #send 0-100 to set left motor speed
    if speed < 0:
        speed = -speed
        leftMotorDir("R")

    elif speed > 100:
        speed = 100
        leftMotorDir("F")

    else:
        leftMotorDir("F")

    PWM_L.duty_cycle = speed*655

def setRightSpeed(speed):
    #send 0-100 to set right motor speed
    if speed < 0:
        speed = -speed
        rightMotorDir("R")

    elif speed > 100:
        speed = 100
        rightMotorDir("F")

    else:
        rightMotorDir("F")

    PWM_R.duty_cycle = speed*655

def sTurnRight(speed):
    #send speed 0-100 to spin right

    setRightDir(R)
    setRightSpeed(speed)
    setLeftDir(F)
    setLeftSpeed(speed)


def sTurnLeft(speed):
    #send speed 0-100 to spin left

    setRightDir(F)
    setRightSpeed(speed)
    setLeftDir(R)
    setLeftSpeed(speed)


def cTurnRight(radius,speed):
    #send approx radius (0-50) in cm to trace that sized circle to the right
    radiusO = radius + 8
    Ci = 2 * math.pi * radius
    Co = 2 * math.pi * radiusO
    ratio = Co/Ci
    setLeftDir(F)
    setLeftSpeed(speed)
    setRightDir(F)
    setRightSpeed(speed * ratio)


def cTurnLeft(radius,speed):
    #send approx radius (0-50) in cm to trace that sized circle to the left
    radiusO = radius + 8
    Ci = 2 * math.pi * radius
    Co = 2 * math.pi * radiusO
    ratio = Co/Ci
    setRightDir(F)
    setRightSpeed(speed)
    setLeftDir(F)
    setLeftSpeed(speed * ratio)

    