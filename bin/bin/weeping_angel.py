#!/usr/bin/python

from os import system
from time import sleep


def angel():
    for i in range(1, 5):
        system("feh --bg-scale ~/Pictures/Weeping\ Angel/" + str(i) + ".JPG")
        sleep(5)

while True:
    angel()
