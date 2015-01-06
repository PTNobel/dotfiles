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
   if [ "$player" == "pianobar" ]
   then pianoctl p
   elif [ "$player" == "mpd" ]
   then mpc toggle
   else exit 1
   fi
}

back() {
   if [ "$player" == "pianobar" ]
   then pianoctl + 
   elif [ "$player" == "mpd" ]
   then mpc prev
   else exit 1
   fi
}

next() {
   if [ "$player" == "pianobar" ]
   then pianoctl \-
   elif [ "$player" == "mpd" ]
   then mpc next
   else exit 1
   fi
}

stop() {
   if [ "$player" == "pianobar" ]
   then pianoctl q
   elif [ "$player" == "mpd" ]
   then mpc stop
   else exit 1
   fi
}

eval $1

#case "$1" in
    #pause)
        #get_player
        #pause
        #;;
    #back)
        #get_player
        #back
        #;;
    #next)
        #get_player
        #next
        #;;
   #stop)
        #get_player
        #stop
        #;;
    #*)
        #echo "Usage: $0 {pause|back|next}"
        #exit 1
        #;;
#esac
