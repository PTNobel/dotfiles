#!/bin/bash

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
   then mpc toggle
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
   then mpc prev
   else exit 1
   fi
}

self.next() {
   get_player
   if [ "$player" == "pianobar" ]
   then pianoctl \-
   elif [ "$player" == "mpd" ]
   then mpc next
   else exit 1
   fi
}

self.stop() {
   get_player
   if [ "$player" == "pianobar" ]
   then pianoctl q
   elif [ "$player" == "mpd" ]
   then mpc stop
   else exit 1
   fi
}

self."$1"
