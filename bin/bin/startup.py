#!/usr/bin/python3

import os
import sys
import datetime
import subprocess

log="/home/parth/.parth/date.log"
autostart="/home/parth/.i3/autostart"
bootstrap="/home/parth/.i3/bootstrap"
log_file=open(log, 'r')
today=str(datetime.date.today())
autostart_file_list=open(autostart,'r')
bootstrap_file_list=open(bootstrap,'r')
commands=list()
bootstrap_commands=list()

raw_commands=autostart_file_list.readlines() + bootstrap_file_list.readlines()
raw_bootstarp_commands=bootstrap_file_list.readlines()

for i in raw_commands:
    var=i.replace('\n','')
    commands.append(var)
for i in raw_bootstarp_commands:
    var=i.replace('\n','')
    bootstrap_commands.append(var)

#print(commands)
def update_log(log_file,log):
    log_file.close()
    log_file_writeable=open(log,'w')
    log_file_writeable.write(today)
    log_file_writeable.close()
    
def success(commands):
    print("starting first boot routine")
    for i in commands:
        os.system(i + " &")
        #os.spawnl(os.P_NOWAIT,i)
"""    for i in commands:
        #os.system("setsid " + str(i))
        call_command = ["setsid"]
        print(commands)
        print(i)
        for j in commands:
            var=j.split(' ')
            print(j)
            for l in var:
                call_command.append(l)
                print(call_command)
                print(subprocess.call(call_command))
"""
#print(commands)
if len(sys.argv) > 1:
    if sys.argv[1] == "-f":
       success(commands)

elif log_file.read() == today:
   log_file.close()
   print("The computer has already booted today")
   if len(sys.argv) > 1:
       if sys.argv[1] == "-b":
           success(bootstrap_commands)
elif log_file.read() != today and os.system('xrandr | grep HDMI1 | grep connected') == 1:
    success(bootstrap_commands)

else:
    update_log(log_file,log)
    success(commands)

exit(0)
