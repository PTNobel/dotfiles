#!/usr/bin/python

import os
import time

def angel():
    for i in range(1, 5):
        os.system("feh --bg-scale ~/Pictures/Weeping\ Angel/" + str(i) + ".JPG")
        time.sleep(5)

while True:
    angel()
