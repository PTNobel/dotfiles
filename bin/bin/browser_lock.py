#!/usr/bin/python3

import processes
import subprocess
import time

currentState = processes.Processes()

while True:
    if currentState.is_comm_running('icecat') and \
            currentState.is_comm_running('firefox'):
        subprocess.call(['killall', '-9', 'icecat'])

    time.sleep(5)
