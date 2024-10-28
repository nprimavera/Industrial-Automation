#!/home/nico/pyenv/bin/python
# NOTE: replace above line with your envrionment's python's path
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

# Import libraries
from http.client import HTTPConnection
import json
import time

# Your robot's computer's communication port
PORT = 8888
NAME = "192.168.137.204"

# Define an http connection
connection = HTTPConnection(f"{NAME}:{PORT}")

# Complete the following function
def robot(connection, func, **args):
    """
    Args:
        - connection: HTTPConnection() associated with NAME and PORT of your robot.
        - func: The function that the robot should perform.
          NOTE:
              a) The webapp4.py script is executed in the robot's terminal and it's currently listening to PORT
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
    
    # Now, using the 'connection' variable defined above, we process func with its prepared data
    # This should implement func at the robot's port which it's listening
    # The arguments for connection.request are POST, func with slash prefix to separate with POST and data
    connection.request("POST", f"/{func}", body=data, headers={"Content-Type": "application/json"})

    # Now, we read the response as we listen to the robot's port:
    with connection.getresponse() as response:
        response.read()

# When running this script, it should call the following actions in order with one second pause between them
robot(connection, 'spin_left')
robot(connection, 'forward', speed=4, duration=2)
robot(connection, 'left', speed=1, duration=0.5)
robot(connection, 'spin_right', duration=1)
robot(connection, 'backward', speed=1, duration=2)

# **************  NETWORK CONNECTION SPEED ANALYSES **************

# Defining a null function - using noop in motor.py
# We use this function to network's speed statistics
# NOTE: This analysis is crucial for any network operated machines
def robot_null(connection):
    # get the current peformance counter
    t1 = time.perf_counter()

    # now we call the robot with no action expected
    robot(connection, 'noop')

    # get the time after calling robot
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.    # milliseconds
                
# Now, we want to compute the connection time statistics using robot_null() function - calling it for 100 times
from statistics import mean, stdev
first_call = robot_null(connection)

# Call robot_null 100 times and store in 'stats'
stats = [robot_null(connection) for _ in range(100)]
print(f"time of first call: {first_call}")
print(f"time, average: {mean(stats)}")
print(f"time, max: {max(stats)}")
print(f"time, min: {min(stats)}")
print(f"timem stdev: {stdev(stats)}")