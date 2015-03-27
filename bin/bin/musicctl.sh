#!/bin/bash
# 
# This code is poorly written just an FYI.
# It should work. However musicctl.py is much better.
# This code is probably insecure if someone really tries to exploit it.
# So don't use this in any situation where the user doesn't already have
# shell access.

# Pianobar or mpd?
get_player() {
    if pidof pianobar >/dev/null
    then if pidof mpd >/dev/null && mpc | grep playing >/dev/null
        then player=mpd
        else player=pianobar
        fi
    elif pidof mpd >/dev/null
    then player=mpd
    else exit 1
    fi
    export $player
}

self.pause() {
   get_player
   if [ "$player" == "pianobar" ]
   then pianoctl p
   elif [ "$player" == "mpd" ]
   then mpc toggle >/dev/null
   else exit 1
   fi
}

self.play() {
    pause
}

self.back() {
   get_player
   if [ "$player" == "pianobar" ]
   then pianoctl +
   elif [ "$player" == "mpd" ]
   then mpc prev >/dev/null
   else exit 1
   fi
}

self.next() {
   get_player
   if [ "$player" == "pianobar" ]
   then pianoctl -
   elif [ "$player" == "mpd" ]
   then mpc next >/dev/null
   else exit 1
   fi
}

self.stop() {
   get_player
   if [ "$player" == "pianobar" ]
   then pianoctl q
   elif [ "$player" == "mpd" ]
   then mpc stop >/dev/null
   else exit 1
   fi
}

self.quit() {
   self.stop
}

self.usage() {
   printf "Usage:
   %s pause
   %s play
   %s back 
   %s next
   %s stop
   %s quit\n" "$0" "$0" "$0" "$0" "$0" "$0"
}

self.help() {
   self.usage
}

self.-h() {
   self.usage
}

self.() {
   self.usage
   exit 1
}

self."$1" || exit 1
