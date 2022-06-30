import zumoCommands as robot
from time import sleep
import neopixel
import board

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3


for i in range(0,3):
    robot.setRightSpeed(50)
    robot.setLeftSpeed(50)
    led[0] = (0,255,0)
    sleep(2)
    robot.setRightSpeed(-50)
    robot.setLeftSpeed(-50)
    led[0] = (255,0,0)
    sleep(2)
    robot.setLeftSpeed(50)
    led[0] = (0,0,255)
    sleep(2)
    robot.setLeftSpeed(-50)
    robot.setRightSpeed(50)
    led[0] = (255,255,255)
    sleep(2)
    print("loop " + str(i))

robot.setLeftSpeed(0)
robot.setRightSpeed(0)

robot.sTurnRight(50)
led[0] = (0,255,255)
sleep(3)
robot.sTurnRight(0)
sleep(3)
robot.sTurnLeft(50)
led[0] = (0,255,0)
sleep(3)
robot.sTurnLeft(0)
sleep(3)

robot.cTurnRight(10,50)
led[0] = (0,255,255)
sleep(3)
robot.cTurnRight(0,0)
sleep(3)
robot.cTurnLeft(10,50)
led[0] = (0,255,0)
sleep(3)
robot.cTurnLeft(0,0)
sleep(3)

