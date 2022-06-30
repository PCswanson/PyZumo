import zumoCommands as robot
from time import sleep
import neopixel
import board

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

lineLED("on")

while True:
    print(S_1())
    sleep(.2)

