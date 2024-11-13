#!/Users/nicolinoprimavera/anaconda3/bin/python
"""
Nicolino Primavera 
Industrial Automation
Assignment 2
10/24/24 
"""

# NOTE: replace above line with your envrionment's python's path
# import the required library to execute external commands

from subprocess import check_output
# define hyper parameters
USER = 'ali' # your uni or your raspberrypi's username
HOST = '10.206.17.37' # your raspberrypi's terminal name or ip address
CMD = '~/pyenv/bin/python ~/bin/webservice1.py' # the script that we're going to invoke
# define a function which receives a user, host and a host_command
# then executes that host_command in the host machine.
# NOTE: make sure you're comfortable with f-strings.

def run_ssh(user, host, host_command):
    shell_command = ['ssh', f'{user}@{host}', host_command]
    check_output(shell_command)

def main():
    # we define set of commands that we can run remotely on our robot:
    commands = ['forward', 'backward', 'spin_left', 'right', 'spin_right', 'left']
    for command in commands:
        print(f'running {command} command ...')
        run_ssh(USER, HOST, CMD + ' ' + command)
        main()