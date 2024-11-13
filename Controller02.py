#!/Users/nicolinoprimavera/anaconda3/bin/python
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

"""
This script makes crickit's LED blinking for 20 times and then stops.
Notice how this script is different from the first script.
Standard python scripts should be:
    1. Robust and coherent,
    2. Object Oriented
We made this script more coherent and easier to read.
But still, this is not object oriented!
"""

# import required libraries
from adafruit_crickit import crickit
import time

# define hyper parameters
RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)

# set the brightness
crickit.onboard_pixel.brightness = 0.010

def main(count, pause):
    '''
    Args:
    - count: total number of cycles to be controlled
    - pause: the time that each blink should last
    '''
    i = 0
    while i <= count:
        for color in RGB:
            crickit.onboard_pixel.fill(RGB[color])
            time.sleep(pause)
            i += 1
    return
    
if __name__ == "__main__":
    main(20, 0.1)