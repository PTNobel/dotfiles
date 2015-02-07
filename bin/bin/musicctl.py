#!/usr/bin/python3

# A python3 port of the bash musicctl program. Should be a drop in replacment.

from __future__ import print_function
import os
import sys
import time


def usage():
    print("Usage: %s {play|pause|back|stop|next|help}" % sys.argv[0])

def warning(*objs):
    printed_list = 'WARNING: '
    for i in objs:
        printed_list += i
    print(printed_list, file=sys.stderr)

def processargs():
    output = {"verbose":None, "input":None}
    for i in sys.argv:
        if i == "-h":
            usage()
        if i == "-v" or i == "--verbose":
            output["verbose"] = True
    if len(sys.argv) == 1:
        output = None
        warning("Not enough argurements")
        usage()
        exit(1)
    elif len(sys.argv) >= 2:
        output["input"] = sys.argv[len(sys.argv) - 1]
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

class musicctl:
    def __init__(self):
        self.get_player()
        try:
            eval("self." + sys.argv[len(sys.argv) - 1])()
        except IndexError:
            verboseprint(sys.argv, len(sys.argv))
            usage()
            exit(1)
        verboseprint(self.player, self)

    def get_player(self):
        if os.system("pidof mpd >/dev/null") == 0:
            if os.system("pidof pianobar >/dev/null") == 0:
                if os.system("mpc status | grep playing &>/dev/null") == 0:
                    self.player = "mpd"
                else:
                    self.player = "pianobar"
            else:
                self.player = "mpd"
        elif os.system("pidof pianobar >/dev/null") == 0:
            self.player = "pianobar"
        else:
            warning("No music player found")
            exit(1)

    def play(self):
        self.pause()

    def pause(self):
        if self.player == "pianobar":
            exit(os.system("pianoctl p"))
        elif self.player == "mpd":
            exit(os.system("mpc toggle >/dev/null"))

    def back(self):
        if self.player == "pianobar":
            exit(os.system("pianoctl +"))
        elif self.player == "mpd":
            exit(os.system("mpc prev >/dev/null"))

    def next(self):
        if self.player == "pianobar":
            exit(os.system("pianoctl -"))
        elif self.player == "mpd":
            exit(os.system("mpc next >/dev/null"))

    def stop(self):
        if self.player == "pianobar":
            exit_code = os.system("pianoctl q")
            time.sleep(1)
            if os.system("pidof pianobar") == 0:
                exit(os.system("killall pianobar"))
            else:
                exit(exit_code)
        elif self.player == "mpd":
            exit(os.system("mpc stop >/dev/null"))
    def tired(self):
        if self.player == "pianobar":
            exit(os.system("pianoctl t"))
        elif self.player == "mpd":
            exit(os.system("mpc next >/dev/null"))

    def help(self):
        verboseprint(self.player)
        usage()
        exit(0)

music = musicctl()
