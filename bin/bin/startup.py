#!/usr/bin/python3

import os
import sys
import datetime


def warning(*objs):
    printed_list = 'WARNING: '
    for i in objs:
        printed_list += str(i)
    print(printed_list, file=sys.stderr)

def processargs():
    output = {"verbose":None, "bootstrap":None, "force":None}
    for i in sys.argv:
        if i == "-v" or i == "--verbose":
            output["verbose"] = True
        elif i == "-b":
            output["bootstrap"] = True
        elif i == "-f":
            output["force"] = True
    return output

arguements = processargs()

if arguements["verbose"]:
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to
        # stuff everything to be printed into a single string
        for arg in args:
            print(arg)
else:
    verboseprint = lambda *a: None      # do-nothing function

date_log = "/home/parth/.parth/date.log"
autostart = "/home/parth/.i3/autostart"
bootstrap = "/home/parth/.i3/bootstrap"
week = "/home/parth/.i3/weekly_tasks"
date_log_file = open(date_log, 'r')
log_value = date_log_file.read()
date_log_file.close()
today = str(datetime.date.today())
autostart_file_list = open(autostart, 'r')
bootstrap_file_list = open(bootstrap, 'r')
weekly_file_list = open(week, 'r')

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

def update_log(log):
    log_file_writeable = open(log, 'w')
    log_file_writeable.write(today)
    log_file_writeable.close()

def success(commands):
    for i in commands:
        os.system(i + " >/dev/null &")
        #os.spawnl(os.P_NOWAIT, i)
#print(commands)

if os.system('urxvt -e exit') != 0:
    print('Something\'s very wrong with this X server')
    print('Dazed and confused and quitting now')
    exit(5)

elif arguements["force"]:
    success(command_list)

elif arguements["bootstrap"]:
    success(bootstrap_commands)

elif os.system('xrandr | grep HDMI1 | grep disconnected >/dev/null') == 0:
    success(bootstrap_commands)

elif log_value != today:
    if datetime.date.today().weekday() == 4:
        command_list += weekly
    update_log(date_log)
    success(command_list)

else:
    success(bootstrap_commands)


exit(0)
