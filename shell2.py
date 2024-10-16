"""
Basic shell to operate robot.
We'll add command line option as so the duration and speed could be also passed to
the library.
We'll also add Quit option to exit the shell.
"""

# import requried ilbraries
import cmd
import motor

# A shell object to operate robot
class RobotShell(cmd.Cmd):
intro = 'Welcome to the robot shell. Type help or ? to list commands.'
prompt = '(robot) '
def do_Quit(self, line):
    return True
def do_forward(self, line):
    if line:
        duration = float(line)
        motor.forward(duration)
    else:
        motor.forward()
def do_backward(self, line):
    if line:
        duration = float(line)
        motor.backward(duration)
    else:
        motor.backward()
        RobotShell().cmdloop()