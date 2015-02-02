#!/bin/bash

# Pianobar or mpd?
get_player() {
    if pidof pianobar >/dev/null
    then if mpc | grep playing >/dev/null
        then player=mpd
        else player=pianobar 
        fi
    elif pidof mpd >/dev/null
    then player=mpd
    else exit 1
    fi
    export $player
}

pause() {
   get_player
   if [ "$player" == "pianobar" ]
   then pianoctl p
   elif [ "$player" == "mpd" ]
   then mpc toggle
   else exit 1
   fi
}

play() {
    pause
}

back() {
   get_player
   if [ "$player" == "pianobar" ]
   then pianoctl + 
   elif [ "$player" == "mpd" ]
   then mpc prev
   else exit 1
   fi
}

next() {
   get_player
   if [ "$player" == "pianobar" ]
   then pianoctl \-
   elif [ "$player" == "mpd" ]
   then mpc next
   else exit 1
   fi
}

stop() {
   get_player
   if [ "$player" == "pianobar" ]
   then pianoctl q
   elif [ "$player" == "mpd" ]
   then mpc stop
   else exit 1
   fi
}

$1
