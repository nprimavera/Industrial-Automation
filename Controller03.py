#!/Users/nicolinoprimavera/anaconda3/bin/python
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

"""
This script shows basics of I2C used in Raspberry Pi to connect with Crickit.
Connection b/w Rasp Pi and Crickit via Inter-Integrated Circuit communication protocol on Rasp Pi
"""

import board

i2c = board.I2C()
devices = i2c.scan()

# The answer is an array of natural numbers showing the decimal address of all device that attached to i2c bus
# e.g. [73]
# print the natural numbers and the hexadecimal value of the first item.

print(devices)
print(hex(devices[0]))

# NOTE: This should be the same as you discovered when used i2cdetect -y 1