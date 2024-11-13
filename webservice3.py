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

# Your robot's computer's communication port
# Assign a port number that your robot will use to listen to the outside requests
PORT = 8888

# The main object that defines and executes the handler
class Handler(RequestHandler):
    def get(self):
        # Define a stamp to write back to the requester
        # our stamp is the current date and time - to be returned back to the requester
        stamp = datetime.now().isoformat()
        self.write(dict(stamp=stamp))
        # Body of the script
        # define the application
        app = Application([("/", Handler)])
        # define the port that the robot's server will allow requester to connect
        # the defined app should listen to the outside requests through our defined port:
        app.listen(PORT)
        # start the robot server
        IOLoop.current().start()