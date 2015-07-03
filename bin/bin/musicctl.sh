#!/bin/bash
#
#

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

get_player

case "$1" in
  ""|-h|help|usage)
    NAME="$(basename "$0")"
    printf "Usage:
      %s pause
      %s play
      %s back
      %s next
      %s stop
      %s quit
      %s is_playing\n" "$NAME" "$NAME" "$NAME" "$NAME" "$NAME" "$NAME" "$NAME"
      ;;
  *)
    case "$player" in
      pianobar)
        case "$1" in
          pause|play)
            pianoctl p
            ;;
          back|like)
            pianoctl +
            ;;
          next|dislike)
            pianoctl -
            ;;
          stop|quit)
            pianoctl q
            ;;
          is_playing)
            LOGFILE_1="$(mktemp)"
            LOGFILE_2="$(mktemp)"
            strings  ~/.config/pianobar/out | tail -n1 >> "$LOGFILE_1"
            sleep 2
            strings  ~/.config/pianobar/out | tail -n1 >> "$LOGFILE_2"
            if ! diff "$LOGFILE_1" "$LOGFILE_2" ; then
              EXIT=0
            else
              EXIT=1
            fi &>/dev/null
            rm "$LOGFILE_1" "$LOGFILE_2"
            exit $EXIT
            ;;
        esac
        ;;
      mpd)
        case "$1" in
          pause|play)
            mpc toggle >/dev/null
            ;;
          back)
            mpc prev >/dev/null
            ;;
          next)
            mpc next >/dev/null
            ;;
          stop|quit)
            mpc stop >/dev/null
            ;;
          is_playing)
            mpc status | grep playing >/dev/null
            exit $?
            ;;
        esac
    esac
esac
