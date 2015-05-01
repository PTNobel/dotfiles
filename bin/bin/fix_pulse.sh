#!/bin/bash

get_pa_sink() {
    pactl list | grep Sink | awk '/Sink/{print $2}' | grep \# | sed s/\#//
}

main() {
  ORIG_VOLUME=$(pacmd list-sinks|grep -A 15 "* index: "| \
                awk '/volume: front/{ print $5 }' | sed 's/%//g')
  for i in $(pactl list | grep Sink | \
             awk '/Sink/{print $2}' | grep \# | sed s/\#//); do
      pactl set-sink-volume "$i" "${ORIG_VOLUME}%"
  done
}

main "$@"
