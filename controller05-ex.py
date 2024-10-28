#!/usr/bin/env python3
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

"""
You need to complete this script on your own in the lab.
This is how this script should work:
    pressing touch 1 -> turns LED to blue.
    pressing touch 2 -> turns LED to green.
    pressing touch 3 -> turns LED to red.
    pressing touch 4 -> exits the script.
"""

# Import required libraries
from adafruit_crickit import crickit

# Set the intensity of LED
crickit.onboard_pixel.brightness = 0.01

# Define a dictionary of RGB colors
RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)

def main():
    # YOUR CODE STARTS HERE
    print("Enter sensor input (1, 2, 3, 4):  ")

    while True:
        # Check touch sensors
        if crickit.touch_1.value:
            crickit.onboard_pixel.fill(RGB['blue'])             # pressing touch 1 -> turns LED to blue.
            print('Touch sensor 1 pressed. LED turned blue.')
        elif crickit.touch_2.value:
            crickit.onboard_pixel.fill(RGB['green'])            # pressing touch 2 -> turns LED to green.
            print('Touch sensor 2 pressed. LED turned green.')
        elif crickit.touch_3.value:
            crickit.onboard_pixel.fill(RGB['red'])              # pressing touch 3 -> turns LED to red.
            print('Touch sensor 3 pressed. LED turned red.')
        elif crickit.touch_4.value:
            print('Touch sensor 4 pressed. Exiting the program...')
            break                                               # pressing touch 4 -> exits the script.
    # YOUR CODE ENDS HERE

if __name__ == "__main__":
    main()