#!/usr/bin/env python3

"""
A class that implements all robot movement matters.
Write this script in a way that receives left and right motor values,
with the duration it has to travel.
"""

from adafruit_crickit import crickit as ck
import time
import argparse

# Define a class to handle all robot matters
class Robot:
    def __init__(self):
        # define LED variables
        self.RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)
        self.LEDBrightness = ck.onboard_pixel.brightness
        self.LEDBrightness = 0.01
        # define a dictionary of motors
        self.Motors = {'R': ck.dc_motor_2, 'L':ck.dc_motor_1}
        # define synchronization parameter
        # this coefficient will be applied to the right motor
        self.SyncForwardR = ?
        self.SyncBackwardR = ?
    def _set_throttle(self, motor, value):
        """
        Args:
        - motor: Cricket's motor object
        - value: the throttle value - motor's input signal intensity 0 to 1
        """
        motor.throttle = value
    def move(self, valueR, valueL, Duration):
        """
        Args:
        - valueR: the throttle value of the right motor (0 to 1)
        - valueL: the throttle value of the left motor (0 to 1)
        - Duration: the time that the robot should move (sec)
        """
        # check the valueR and set the proper value for motor's throttle
        ?
        # drive the motor and stop it
        ?
    def main(args):
        # check the validity of args
        if not (args.left and args.right and args.duration):
            print("Specify input params. Use -h for help.")
        exit()
        if not args or not (-0.9 <= args.left <= 0.9 and -0.9 <= args.right <= 0.9 and
            0 <= args.duration <= 30):
            print("Not valid input parameters.")
        exit(1)

# define a robot instance
robot = Robot()
# move the instance
robot.move(args.left, args.right, args.duration)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Robot input parameters.")
    parser.add_argument("-l", "--left", type=float, help="The left motor's signal value.")
    parser.add_argument("-r", "--right", type=float, help="The right motor's signal value.")
    parser.add_argument("-d", "--duration", type=float, help="The time lapse that the robot should move.")
    args = parser.parse_args()
main(args)