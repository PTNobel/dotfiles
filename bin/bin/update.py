#!/usr/bin/python3

import subprocess
import threading
import time
# import sys

before_yaourt = [
    ['backup.sh'],
    ['update_tools_helper', 'pkgfile'],
    ['update_tools_helper', 'abs'],
]

popens_to_wait_on = []

yaourt = [
    ['update_tools_helper', 'alpm'],
    ['yaourt', '-Sua'],
]

after_yaourt = [
    ['update_tools_helper', 'mlocate'],
    ['update_tools_helper', 'man'],
    ['update_tools_helper', 'units'],
]


def print_stdout(aPopen):
    while aPopen.returncode is None:
        out, err = aPopen.communicate()
        print(out.decode('utf-8'))
        aPopen.poll()
        time.sleep(12)


for i in before_yaourt:
    popens_to_wait_on.append(subprocess.Popen(i, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE))

for i in yaourt:
    subprocess.call(i)

for i in after_yaourt:
    popens_to_wait_on.append(subprocess.Popen(i, stdout=subprocess.PIPE))

for i in popens_to_wait_on:
    var = threading.Thread(target=print_stdout, args=[i])
    var.start()
