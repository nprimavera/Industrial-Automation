#!/home/nico/pyenv/bin/python
# NOTE: replace above line with your envrionment's python's path
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

# Import libraries
from urllib.request import urlopen
import json
import time

# Your robot's computer's communication port and IP
MY_PORT = 8888
robot_ip = '192.168.137.204'

# Following variable should be your robot's URL in f-string format - containing MY_PORT
MY_ROBOT_URL = f'http://{robot_ip}:{MY_PORT}'

# Complete the following function
def robot(func, **args):
    """
    Args:
        - func: The function that the robot should perform.
          NOTE:
              a) The webapp4.py script is executed in the robot's terminal and it's currently listening to MY_PORT
              b) That script knows 'func' and its required arguments.
        - **args: arguments of func
          NOTE:
              func(args) should be successfully passed to the robot and receive a response from it.
    Returns:
        None
    """

    # Input arguments - args, need to be in a dictionary - or json format. 
    # It also has to be in 'byte string' format to be able to transfer it over networks.
    # Define a variable named data which is an encoded json of input arguments
    data = json.dumps(args).encode('utf-8')
    
    # Now, using urlopen, process func with its prepared args
    # This should implement func at the robot's port which it's listening
    url = f"{MY_ROBOT_URL}/{func}"
    
    # Send the request to the robot
    with urlopen(url, data=data) as response:
        result = response.read().decode('utf-8')
        print(f"Robot Response: {result}")

# When running this script, it should call the following actions in order with one second pause between them
robot('forward')
time.sleep(1)
robot('backward', speed=4, duration=0.2)
time.sleep(1)
robot('left', speed=2, duration=1)
time.sleep(1)
robot('spin_right')