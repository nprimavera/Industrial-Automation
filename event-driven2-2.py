"""
Using 'threading' module in python to run several functions at the same time.
A simple variable tracking.

Ali Dadgar - 2020
"""

import threading
import time

''' global param '''
rob1 = 0 # the event that to be handled in robot()
cam1 = 0 # the even that to be handled in camera()

""" This is a daemon function """
# NOTE: daemon functions run in the background; they also serve other parts of code.
# NOTE: We can run daemon functions in the background until its clients finish their job.
def robot(**kwargs):
    # The input is open to any keyworded arguments.
    global rob1
    # we know that in the passed arguments, we have 'servo1' variable
    incr = kwargs['stepsize']
    while True:
        rob1 += incr
        time.sleep(0.01)

""" client task """
def camera(**kwargs):
    global rob1, cam1
    incr = kwargs['cam_stepsize']
    for _ in range(1000):
        cam1 += incr
        print(rob1, cam1)
        time.sleep(0.01)

robot = threading.Thread(target=robot, kwargs={'stepsize': 2}, daemon=True)
camera = threading.Thread(target=camera, kwargs={'cam_stepsize': 1})

robot.start()
camera.start()