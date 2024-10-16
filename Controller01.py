"""
The first script to check overall connections and software installation of your
robot.
We simply change Crickit's LED's color.
Make sure this works on your robot.
You may change the color manually, save and re-run to see other colors.
"""

# import the required library
from adafruit_crickit import crickit

# set the intensity of LED
crickit.onboard_pixel.brightness = 0.01

# define a dictionary of RGB colors
RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)

# set the LED light to blue
crickit.onboard_pixel.fill(RGB['blue'])