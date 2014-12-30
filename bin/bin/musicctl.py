#!/usr/bin/python3

# A python3 port of the bash musicctl program. Should be a drop in replacment.

import os 
import sys

class musicctl:

    def __init__(self):
        if os.system("pidof pianobar >/dev/null") == 0:
            if os.system("mpc status | grep playing >/dev/null") == 0:
                self.player = "mpd"
            else:
                self.player = "pianobar"
        elif os.system("pidof mpd >/dev/null") == 0:
            self.player = "mpd"
        try:
            eval("self." + sys.argv[1])()
        except IndexError:
            print("Usage: %s {pause|back|stop|next}" % sys.argv[0])
            exit(1)        

    def pause(self):
        if self.player == "pianobar":
            exit(os.system("pianoctl p"))
        elif self.player == "mpd":
            exit(os.system("mpc toggle"))

    def back(self):
        if self.player == "pianobar":
            exit(os.system*("pianoctl +"))
        elif self.player == "mpd":
            exit(os.system("mpc prev"))

    def next(self):
        if self.player == "pianobar":
            exit(os.system("pianoctl n"))
        elif self.player == "mpd":
            exit(os.system("mpc next"))

    def stop(self):
        if self.player == "pianobar":
            exit(os.system("pianoctl q"))
        elif self.player == "mpd":
            exit(os.system("mpc stop"))

music = musicctl()
