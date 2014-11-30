#!/usr/bin/python3

# A python3 port of the bash musicctl program. Should be a drop in replacment.

import os 
import sys

class musicctl:

    def __init__(self):
        if os.system("pidof pianobar >/dev/null") == 0:
            self.player = "pianobar"
        elif os.system("pidof mpd >/dev/null") == 0:
            self.player = "mpd"
        eval("self." + sys.argv[1])()

    def pause(self):
        if self.player == "pianobar":
            os.system("pianoctl \ ")
        elif self.player == "mpd":
            os.system("mpc toggle")

    def back(self):
        if self.player == "pianobar":
            return 0
        elif self.player == "mpd":
            os.system("mpc prev")

    def next(self):
        if self.player == "pianobar":
            os.system("pianoctl n")
        elif self.player == "mpd":
            os.system("mpc next")

    def stop(self):
        if self.player == "pianobar":
            os.system("pianoctl q")
        elif self.player == "mpd":
            os.system("mpc stop")

music = musicctl()
