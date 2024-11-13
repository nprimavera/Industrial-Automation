"""
Using 'threading' module in python to run several functions at the same time.

Ali Dadgar - 2020
"""

import threading
import time

''' global param '''
text = "" # to be handled in the function: read_file()

""" This is a daemon function """
# NOTE: daemon functions run in the background; they also serve other parts of code.
# NOTE: We can run daemon functions in the background until its clients finish their job.
def read_file(**kwargs):
    # The input is open to any keyworded arguments.
    global text
    # we know that in the passed arguments, we have 'path' variable
    file_path = kwargs['path'] 
    while True:
        with open(file_path, 'r') as fp:
            text = fp.read()
        #time.sleep(0.1)

""" client task """
def print_file():
    for _ in range(1000):
        print(text)
        #time.sleep(0.1)

t1 = threading.Thread(target=read_file, kwargs={'path': "text_file.txt"},daemon=True)
t2 = threading.Thread(target=print_file)

t1.start()
t2.start()