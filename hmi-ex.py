#!/home/ali/pyenv/bin/python

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.log import enable_pretty_logging
from datetime import datetime
from os.path import dirname
import time
import os

# import the machine's required library
pass

# Hyper parameters:
# your assigned port to talk to your robot:
PORT = 8888

# define a variable to be able to detect the robot's error/status
DEBUG = bool(os.environ.get('ROBOT_DEBUG'))

# The basic handler object to handle our web requests
class Handler(RequestHandler):

    def get(self, name):
        stamp = datetime.now().isoformat()
        self.render('hmi.html', stamp=stamp)

    def post(self, name):
        # Args: name: is the box which is selected in the remote computer
        # do the proper action here wrt the posted 'name'
        # define a function to perform machine's assigned task.
        # Use getattr() you learned in Assignment 2
        pass
        # return to orignial state
        self.redirect('/')

# start the script

# First enable logging output
enable_pretty_logging()

# define a dictionary of required variables to pass to our application
settings = dict(debug=DEBUG)

# call the application - we use regular expression to capture any command line options
# these format will match all movement command patterns
app = Application([('/([a-z_]*)', Handler)], **settings)

# now listen to it 
app.listen(PORT)

# make this a loop
IOLoop.current().start()