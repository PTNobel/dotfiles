#!/usr/bin/python3

import os
import sys
import datetime

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

if len(sys.argv) > 1:
    if sys.argv[1] == "-f":
        success(command_list)
    elif sys.argv[1] == "-b":
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
