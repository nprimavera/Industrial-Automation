#!/usr/bin/env python3
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

"""
A sample library to move robot.
"""

# Import libraries
from adafruit_crickit import crickit as ck
import time
import os
from functools import partial

'''
NOTE:
Familiarize yourself with python's functool.partial
It's a very powerful tool to create a customized function with pre-defined or new arguments. 
'''

# Hyper parameters of your robot that you found in controller09-ex.py exercise.
# NOTE: each robot is different; if you haven't found it yet, go back to that exercise and find these coefficients.
SyncForwardR = 0.9    # the right motor's sync coefficient when it moves forward
SyncBackwardR = 0.9   # the right motor's sync coefficient when it moves backward

# We now define two standard dictionaries which the script will refer it:
MOTOR = {'R': ck.dc_motor_2, 'L': ck.dc_motor_1}            # dictionary of motors
THROTTLE_SPEED = {0: 0, 1: 0.35, 2: 0.5, 3: 0.7, 4: 0.9}    # dictionary of speeds; 0: stop, 4: max speed

# A function to set the motor speed and direction
def set_throttle(motor_name, speed, factor=1):
    """
    Args:
        - motor_name: 'R' or 'L'
        - speed: the throttle speed from the THROTTLE_SPEED dictionary's keys
        - factor: 1 or -1 showing forward or backward motions - the default is forward (1)
    Output:
        - applies current to the dc motors wrt the SyncForwardR or SyncBackwardR hyper params
    """

    # If the motor_name is 'R' then, we have to apply sync coefficients - depending on the direction:
    sync = 1  # Default sync factor

    if motor_name == 'R':       # Right motor
        if factor == 1:         # Forward motion
            sync = SyncForwardR
        elif factor == -1:      # Backward motion
            sync = SyncBackwardR
            
    # Now, we set the throttle speed to the given motor:
    MOTOR[motor_name].throttle = THROTTLE_SPEED[speed] * sync * factor

# A function to move the robot, with all default values
def move(duration=0.3, speed=2, factor_r=1, factor_l=1):
    """
    Args:
        - duration: the time that the motion will be executed, default: 0.3 sec
        - speed: the motor speed from THROTTLE_SPEED dictionary, default: speed 2 (50% of max throttle)
        - factor_r, factor_l: 1 or -1 : show which direction the motor should rotate
    Output:
        - the motors' motion
    """

    # Set the throttle speed to the right motor
    set_throttle('R', speed, factor_r)
    
    # Set the throttle speed to the left motor
    set_throttle('L', speed, factor_l)
    
    # Set the sleep time = duration
    time.sleep(duration)
    
    # Turn off both motors by setting up the throttles to 0
    MOTOR['R'].throttle = 0
    MOTOR['L'].throttle = 0
 

# Now we leverage power of 'partial' to redefine move() function and create new functions out of it.
# We define forward, backward, right, left, spin_right and spin_left functions

forward = partial(move)    # The new function forward() will use the same arguments as move() do.
backward = partial(move, factor_r=-1, factor_l=-1)    # The new function will use negative factors to move backward.
right = partial(move, factor_r=0.5)                   # right(): to turn right, we decrease right motor's throttle factor.
left = partial(move, factor_l=0.5)                    # left(): to turn left, we decrease left motor's throttle factor.
spin_right = partial(move, factor_r=-1, factor_l=1)   # spin_right()
spin_left = partial(move, factor_r=1, factor_l=-1)    # spin_left()
noop = lambda: None                                   # a function that returns nothing - for web service and web app use (later)