#!/Users/nicolinoprimavera/anaconda3/bin/python
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

# import the required library to execute external commands
from datetime import datetime # we'd record date and time when there is a http request
from tornado.web import RequestHandler, Application # fine tune our web application
from tornado.ioloop import IOLoop # the main object that runs the robot server
import sys
import json
import motor

# Your robot's computer's communication port
PORT = 8888

# The main object that executes the handler
class Handler(RequestHandler):
    def get(self, name):
        stamp = datetime.now().isoformat()
        self.write(dict(stamp=stamp))

def post(self, name):
    # Make a json dictionary of the passed command
    args = json.loads(self.request.body or '{}')
    # Define the function from motor, wrt the passed 'name'
    func = getattr(motor, name)
    # Execute that function
    func(**args)
    self.write(dict(status='success'))
    # define the application
    app = Application([('/(.*)', Handler)])
    # define the port to connect to the robot's server
    app.listen(PORT)
    # start the robot server
    IOLoop.current().start()