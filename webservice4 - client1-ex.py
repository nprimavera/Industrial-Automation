#!/home/ali/pyenv/bin/python
# NOTE: replace above line with your envrionment's python's path
# import the required library to execute external commands

from urllib.request import urlopen
import json
import time

# Your robot's computer's communication port
MY_PORT = ?

# Following variable should be your robot's url in f-string format - containing
MY_PORT
MY_ROBOT_URL = ?

# Complete the following function
def robot(func, **args):
    """
    Args:
    - func: The function that the robot should perform.
    NOTE:
    a) The webapp4.py script is executed in the robot's terminal and it's
    currently listening to MY_PORT
    b) That script knows 'func' and its required arguments.
    - **args: arguments of func
    NOTE:
    func(args) should be successfully passed to the robot and receive a
    response from it.
    Returns:
    None
    """
    # Input arguments - args, need to be in a dictionary - or json format.
    # It also has to be in 'byte string' format to be able to transfer it over networks.
    # Define a variable named data which is an encoded json of input arguments
    data = ?
    # Now, using urlopen, process func with its prepared args
    # This should implement func at the robot's port which it's listening
    ?
    # When running this script, it should call the following actions in order with one second pause between them
    robot('forward')
    time.sleep(1)
    robot('backward', speed=4, duration=0.2)
    time.sleep(1)
    robot('left', speed=2, duration=1)
    time.sleep(1)
    robot('spin_right')