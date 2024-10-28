#!/usr/bin/env python3
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

"""
Basic shell to operate robot.
We'll add full functionality to this script.
All command line options defined in motor.py could be processed now in this shell script.
"""

# Import libraries
import cmd
import motor

# Define a function that receives a passed 'line' and retrieves required command line 
# Information such as 'duration' and 'speed' which will be consumed by motor objects.
def get_kwargs(line):
    # line: whatever the user types after the function's name
    # First, we make a dictionary of arguments to return: kwargs
    kwargs = dict()
    
    # Split the passed line into its components - assuming that the user needs to type: <command> num1 num2
    items = line.split()    # now, items is a list such that items = [num1, num2]
    
    # Put the first item item in 'duration' field of the dictioary and the second item in 'speed' field of the dictionary
    if len(items) > 0:  # If there are parameters passed
        kwargs['duration'] = float(items[0])  # Set the first item as duration

    if len(items) > 1:  # If there's a second item, it's the speed
        kwargs['speed'] = float(items[1])  # Set the second item as speed
    
    return kwargs
 
# A complete shell object to operate robot
class RobotShell(cmd.Cmd):
    intro = 'Welcome to the robot shell. Type help or ? to list commands.'
    prompt = '(robot)'
 
    def do_Quit(self, line):
        return True
 
    def precmd(self, line):
        print('executing', repr(line))
        return line
 
    def do_forward(self, line):
        motor.forward(**get_kwargs(line))
 
    def do_backward(self, line):
        motor.backward(**get_kwargs(line))
 
    def do_right(self, line):
        motor.right(**get_kwargs(line))
 
    def do_left(self, line):
        motor.left(**get_kwargs(line))
 
    def do_spin_right(self, line):
        motor.spin_right(**get_kwargs(line))
 
    def do_spin_left(self, line):
        motor.spin_left(**get_kwargs(line))

RobotShell().cmdloop()