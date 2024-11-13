"""
# Define list of events and what should be implemented when that event happens.
# This list could be origninally an empty dictionary (events = {}).

events = {
    "event1": [func1(), func2(), func3()],
    "event2": [func2()],
    "event3": [func3(), func1(), func3()]
}

Each of these functions are 'subscribers' or 'handlers' of each event.
For instance, func1() is subscribed to event1 and event3.

Ali Dadgar - 2020
""" 

events = {}
""" function that registers an event """
# Receives a function and updates 'events' dictionary.
# This is basically subscribing an event
def register(event: str, function: callable):
    if not event in events:
        # If event is not in the list -> register it.
        events[event] = [function]
    else:
        # The event is already exits -> append to the list.
        events[event].append(function)

""" function to dispatch an event """
# Dispatch: mokhabere kardan
# Implements the requested 'event' using the passed 'data'.
# 'data' could be **kwargs as well. This might decrease functions' significance in large projects.
def dispatch(event: str, data):
    if not event in events:
        # If the requested 'event' does not exist -> we don't need to do anything.
        return
    else:
        # The 'event' exists -> implement it (post the event)
        for handler in events[event]:
            handler(data)

# NOTE:
# Following are different handlers, that handle required events.

""" Event: puts robot in zero (start) position """
def robot_zero():
    pass

""" Event: puts the robot in ground position """
def robot_grount_position():
    pass

""" Event: turn on the camera """
def camera_on():
    pass

""" Event: turn off the camera """
def camera_off():
    pass

def main():
    # register required events
    register('robotStartPosition', robot_zero)
    register('cameraOn', camera_on)
    register('robotGroundPosition', robot_grount_position)