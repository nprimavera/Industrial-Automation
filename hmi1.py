#!/home/dimitris/pyenv/bin/python

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.log import enable_pretty_logging
from datetime import datetime
from os.path import dirname
import time
import os



# Hyper parameters:
# your assigned port to talk to your robot:
PORT = 8888
# define a variable to be able to detect the robot's error/status
DEBUG = bool(os.environ.get('ROBOT_DEBUG'))
 


# The basic handler object to handle our web requests
class Handler(RequestHandler):

    def get(self, name):
        stamp = datetime.now().isoformat()
        self.render('hmi1.html', stamp=stamp)

    def post(self, name):
        if name == 'choice_a':
            # Action for choice A:
            # If user clicks on choice A, this function should do the proper action
            pass
        if name == 'choice_b':
            # Action for choice B
            # If user clicks on choice B, this function should do the proper action
            pass
        # redirect the web page to its original location:
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

