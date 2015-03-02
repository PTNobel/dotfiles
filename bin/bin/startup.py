#!/usr/bin/python3

import os
import sys
import datetime
import re


# Usage: warning(as, many, objects, as, desired)
# Will print everything passed to it to stderr with the prefix WARNING:
def warning(*objs):
    printed_list = 'WARNING: '
    for i in objs:
        printed_list += str(i)
    print(printed_list, file=sys.stderr)

# processargs() goes through sys.argv and returns a dictionary that specifies
# whether the associated flag was passed.
# Usage: processargs() accepts no arguements.
def processargs():
    output = {"weekly":None, "verbose":None, "bootstrap":None, "force":None}
    for i in sys.argv:
        if i == "-v" or i == "--verbose":
            output["verbose"] = True
        elif i == "-b":
            output["bootstrap"] = True
        elif i == "-f":
            output["force"] = True
        elif i == "-w":
            output["weeky"] = True
    return output

arguements = processargs()

# verboseprint() finctions similarly to warning() accept it only exists if
# arguements["verbose"] is true, or when -v is present. It is intended to dump
# objects into stdout.
# Usage: verboseprint(as,  many, objects, as, desired)
if arguements["verbose"]:
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to
        # stuff everything to be printed into a single string
        for arg in args:
            print(arg)
else:
    verboseprint = lambda *a: None      # do-nothing function

# Begin checking to make sure this is the only version of startup.py to be
# running. This helps fight issues with multiple instances of startup.py
# launching processes repeatedly.
def check_if_pid_is_startuppy(pidnum):
    python_check = re.findall(r"python", str(open(os.path.join('/proc', pidnum, 'cmdline'), 'rb').read()))
    startup_check = re.findall(r"startup", str(open(os.path.join('/proc', pidnum, 'cmdline'), 'rb').read()))
    if python_check == [] or startup_check == []:
        return False
    else:
        return True

pids = [pid for pid in os.listdir('/proc') if pid.isdigit() and pid != str(os.getpid())]

verboseprint(pids)
verboseprint(str(os.getpid()))

if os.getpid() in pids:
    verboseprint('Something\'s weird... pids containts os.getpid()', pids, os.getpid())

for pid in pids:
    try:
        verboseprint(pid)
        if pid == str(os.getpid()):
            print('This script')
        verboseprint(open(os.path.join('/proc/', pid, 'cmdline'), 'rb').read())
        if check_if_pid_is_startuppy(pid):
            warning("Is there another " + sys.argv[0] + " running?")
            exit(4)
        else:
            verboseprint(pid + " is not startup.py")
    except IOError: # proc has already terminated
        verboseprint(pid + " has terminated")
        continue

# Variable definitions this should cover everything.
date_log = os.environ['HOME'] + "/.parth/date.log"
autostart = os.environ['HOME'] + "/.i3/autostart"
bootstrap = os.environ['HOME'] + "/.i3/bootstrap"
week = os.environ['HOME'] + "/.i3/weekly_tasks"
date_log_file = open(date_log, 'r')
log_value = date_log_file.read()
date_log_file.close()
today = str(datetime.date.today())
autostart_file_list = open(autostart, 'r')
bootstrap_file_list = open(bootstrap, 'r')
weekly_file_list = open(week, 'r')
run_log_name = "startup." + os.environ["DISPLAY"][1:] +'.log'

# removes unnecessary characters from a list.
def clean_list(input_list):
    output_list = list()
    for i in input_list:
        var = i.replace('\n', '')
        output_list.append(var)
    return output_list

raw_commands = autostart_file_list.readlines()
raw_bootstarp_commands = bootstrap_file_list.readlines()
raw_weekly = weekly_file_list.readlines()
raw_commands += raw_bootstarp_commands

command_list = clean_list(raw_commands)
bootstrap_commands = clean_list(raw_bootstarp_commands)
weekly = clean_list(raw_weekly)

# writes today's date to a log file.
def update_log(log):
    log_file_writeable = open(log, 'w')
    log_file_writeable.write(today)
    log_file_writeable.close()

# Iterates through the list commands, and executes the commands. It then
# creates run_log_str in /tmp/
def success(commands, run_log_str):
    verboseprint(commands)
    for i in commands:
        verboseprint(i)
        if os.system('urxvt -e exit') != 0:
            warning('Something\'s very wrong with this X server')
            warning('Dazed and confused and quitting now')
            os.system('dmesg >/tmp/dmesg.X.' + os.environ['DISPLAY'][1:] +'.log')
            exit(6)
        os.system(i + ' >/dev/null &')
    run_log = open('/tmp/' + run_log_str, mode='w')
    run_log.write('We finished.\n')
    run_log.close()

if os.system('urxvt -e exit') != 0:
    warning('Something\'s very wrong with this X server')
    warning('Dazed and confused and quitting now')
    os.system('dmesg >/tmp/dmesg.X.' + os.environ['DISPLAY'][1:] +'.log')
    exit(5)

elif arguements["force"]:
    success(command_list, run_log_name)

elif arguements["bootstrap"]:
    success(bootstrap_commands, run_log_name)

elif arguements["weekly"]:
    command_list += weekly
    success(command_list, run_log_name)

elif run_log_name in os.listdir('/tmp'):
    warning('Already ran')
    exit(8)

elif os.system('xrandr | grep HDMI1 | grep disconnected >/dev/null') == 0:
    success(bootstrap_commands, run_log_name)

elif log_value != today:
    if datetime.date.today().weekday() == 4 or arguements["weekly"]:
        command_list += weekly
    update_log(date_log)
    success(command_list, run_log_name)

else:
    success(bootstrap_commands, run_log_name)

exit(0)
