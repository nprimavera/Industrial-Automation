"""
Basic shell to operate robot.
We'll add full functionality to this script.
All command line options defined in motor.py could be processed now in this shell
script.
"""

# import required libraries
import cmd
import motor

# Define a function that receives a passed 'line' and retrieves required command line
# information such as 'duration' and 'speed' which will be consumed by motor objects.

def get_kwargs(line):
    # line: whatever the user types after the function's name
    # first, we make a dictionary of arguments to return: kwargs
    kwargs = dict()
    # split the passed line into its components - assuming that the user needs to
    type: <command> num1 num2
    items = line.split() # now, items is a list such that items = [num1, num2]
    # put the first item item in 'duration' field of the dictioary
    # and the second item in 'speed' field of the dictionary
    ?
    return kwargs

# A complete shell object to operate robot
class RobotShell(cmd.Cmd):
    intro = 'Welcome to the robot shell. Type help or ? to list commands.'
    prompt = '(robot) '

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