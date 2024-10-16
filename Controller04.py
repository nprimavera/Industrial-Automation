"""
This script investigates the status of touch sensors.
"""

# import required library
from adafruit_crickit import crickit

# get the current status of touch sensor 1
touch1_status = crickit.touch_1.value

# post a sign for the user:
print('touch the sensor number 1 exit the program ...')

# wait until touch sensor 1 is touched
while not touch1_status:
    touch1_status = crickit.touch_1.value
    pass
# end of program - inform the user that the sensor is touchedm before exiting the program.
print('sensor 1 is touched.')