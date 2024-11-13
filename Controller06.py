#!/Users/nicolinoprimavera/anaconda3/bin/python
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

"""
Basics of how the robot motor driver works.
We will drive robot for 0.5 second.
"""

# import required libraries
import time
from adafruit_crickit import crickit

# hyper parameters
# The time that the robot should move
DELAY = 0.5     # drive the robot for 0.5 second

# Turn the motors on
# We should never assign 100% of signal to the motors (never use 1.0 throttle value)
crickit.dc_motor_1.throttle = 0.9
crickit.dc_motor_2.throttle = 0.9

time.sleep(DELAY)

# Turn the motors off
crickit.dc_motor_1.throttle = 0
crickit.dc_motor_2.throttle = 0