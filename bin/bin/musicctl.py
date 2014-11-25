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


"""
#!/bin/bash


# Pianobar or mpd?
get_player() {
    if pidof pianobar >/dev/null
    then player=pianoctl 
    elif pidof mpd >/dev/null
    then player=mpc
    else exit 1
    fi
    export $player
}

toggle_pause() {
   if [ "$player" == "pianoctl" ]
   then pianoctl \ 
   elif [ "$player" == "mpc" ]
   then mpc pause
   else exit 1
   fi
}

back() {
   if [ "$player" == "pianoctl" ]
   then exit 0 
   elif [ "$player" == "mpc" ]
   then mpc prev
   else exit 1
   fi
}

next() {
   if [ "$player" == "pianoctl" ]
   then pianoctl n 
   elif [ "$player" == "mpc" ]
   then mpc next
   else exit 1
   fi
}

stop() {
   if [ "$player" == "pianoctl" ]
   then pianoctl q
   elif [ "$player" == "mpc" ]
   then mpc stop
   else exit 1
   fi
}

get_player

case "$1" in
    pause)
        toggle_pause
        ;;
    back)
        back
        ;;
    next)
        next
        ;;
   stop)
        stop
        ;;
    *)
        echo "Usage: $0 {pause|back|next}"
        exit 1
esac

exit $exit
"""
