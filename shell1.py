"""
Basic shell to operate robot.
"""
# import required libraries
import cmd # python's cmd library
import motor # the motor.py library that you created

# A shell object to operate robot
class RobotShell(cmd.Cmd):
intro = 'Welcome to the robot shell. Type help or ? to list commands.'
prompt = '(robot) '

# NOTE: whatever users enters in the shell's command line, is stored in 'line'
def do_forward(self, line):
    # call motor's forward() without passing any arguments
    motor.forward()

def do_backward(self, line):
    # call motor's backward() without passing any arguments
    motor.backward()
    # This loops the RobotShell object until your cancel the script
    # Note, this is not the right way of exiting a program, we do this in order to focus the main parts of this script.
    RobotShell().cmdloop()