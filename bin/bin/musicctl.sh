#!/bin/bash
#
# This code is poorly written just an FYI.
# It should work. However musicctl.py is much better.
# This code is probably insecure if someone really tries to exploit it.
# So don't use this in any situation where the user doesn't already have
# shell access.

# Pianobar or mpd?
get_player() {
    if pidof pianobar >/dev/null; then
       if pidof mpd >/dev/null && mpc | grep playing >/dev/null; then
         player=mpd
       else
         player=pianobar
       fi
    elif pidof mpd >/dev/null; then
        player=mpd
    else
        exit 1
    fi
    export $player
}

self_pause() {
   get_player
   if [ "$player" == "pianobar" ]; then
      pianoctl p
   elif [ "$player" == "mpd" ]; then
      mpc toggle >/dev/null
   else
      exit 1
   fi
}

self_play() {
    self_pause
}

self_back() {
   get_player
   if [ "$player" == "pianobar" ]; then
      pianoctl +
   elif [ "$player" == "mpd" ]; then
      mpc prev >/dev/null
   else
      exit 1
   fi
}

self_next() {
   get_player
   if [ "$player" == "pianobar" ]; then
      pianoctl -
   elif [ "$player" == "mpd" ]; then
      mpc next >/dev/null
   else
      exit 1
   fi
}

self_stop() {
   get_player
   if [ "$player" == "pianobar" ]; then
      pianoctl q
   elif [ "$player" == "mpd" ]; then
      mpc stop >/dev/null
   else
      exit 1
   fi
}

self_quit() {
   self_stop
}

self_usage() {
   printf "Usage:
   %s pause
   %s play
   %s back
   %s next
   %s stop
   %s quit\n" "$0" "$0" "$0" "$0" "$0" "$0"
}

self_help() {
   self_usage
}

self_-h() {
   self_usage
}

self_() {
   self_usage
   exit 1
}

self_"$1" || exit 1
