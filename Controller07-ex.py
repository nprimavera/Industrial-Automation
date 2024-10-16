"""
Basics of how the robot motor driver works.
If touch sensor 1 is touched, it'll change LED color to 'red' and,
then will drive the robot for 0.3 seconds with full power.
"""

# import required libraries
import time
from adafruit_crickit import crickit as ck

# define hyper parameters
# define reference dictionary of colors
RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)
# the motor drive time
DELAY = 0.3
# the board's LED brightness level
ck.onboard_pixel.brightness = 0.01
# Body of the script
while True:
    # check the current status of touch sensors 1 and 3
    # if sensor 3 is touched, exit or break the loop
    ?
    # set the motors' throttle value
    # set the LED color
    # run the motor
    ?