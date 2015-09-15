#!/usr/bin/python3

import process
import subprocess
import time


while True:
    process.update_buffers()
    if process.is_comm_running('icecat') and \
            process.is_comm_running('firefox'):
        subprocess.call(['killall', '-9', 'icecat'])

    time.sleep(5)
