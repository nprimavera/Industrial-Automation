#!/usr/bin/env python3
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

"""
Basics of how the robot motor driver works.
If touch sensor 1 is touched, it'll change LED color to 'red' and,
then will drive the robot for 0.3 seconds with full power.
"""

# Import libraries
import time
from adafruit_crickit import crickit as ck

# Define hyper parameters
RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)     # Define reference dictionary of colors
DELAY = 0.3                                                 # The motor drive time
ck.onboard_pixel.brightness = 0.01                          # The board's LED brightness level

# Body of the script
while True:
    # check the current status of touch sensors 1 and 3
    # if sensor 3 is touched, exit or break the loop
    if ck.touch_3.value:
        print("Touch sensor 3 pressed. Exiting...")
        break

    # if touch sensor 1 is pressed
    if ck.touch_1.value:
        # set the motors' throttle value to full power
        ck.dc_motor_1.throttle = 0.9
        ck.dc_motor_2.throttle = 0.9
        
        # Set the LED color to red
        ck.onboard_pixel.fill(RGB['red'])

        # Run the motor for the specified delay time
        time.sleep(DELAY)

        # stop the motors after the delay
        ck.dc_motor_1.throttle = 0
        ck.dc_motor_2.throttle = 0

        print("Touch sensor 1 pressed. LED set to red, motors ran for 0.3 seconds.")