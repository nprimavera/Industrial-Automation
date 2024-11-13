#!/Users/nicolinoprimavera/anaconda3/bin/python
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

# NOTE: notice how we tell the script which python it should use to execte.
# import required libraries

from argparse import ArgumentParser
import motor

# A function to receive all arguments and pass to the main script
# It's a good practice to keep this function separate for debugging/maintenace purposes

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('name', help='name of the motion') # the name of the
    motion: forward, backward, etc.
    parser.add_argument('--duration', help='duration of the motion', type=float)
    # duration of that motion
    parser.add_argument('--speed', help='speed of the motion', type=int)
    # the speed of that motion
    return vars(parser.parse_args())

def main():
    # receive arguments and get rid of 'name'
    args = parse_args()
    name = args.pop('name') # the name of the function to do the motion:
    forward, backward, etc.
    # define a function 'func' which dynamically receives the attributes of the required object 'name'
    # getattr() is python's power
    func = getattr(motor, name)
    # build a dictionary of arguments to pass to our 'func'
    kwargs = {k: v for k, v in args.items() if v}
    print(f"calling {name} with args: {kwargs}")
    func(**kwargs)
    if __name__ == "__main__":
        main()